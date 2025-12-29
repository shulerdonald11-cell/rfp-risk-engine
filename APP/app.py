from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from datetime import datetime
import uuid
import shutil

from APP.phase6_runner import run_once

REPO_ROOT = Path(__file__).resolve().parents[1]

OUTPUT = REPO_ROOT / "OUTPUT"
RUNS_ROOT = REPO_ROOT / "OUTPUTS" / "runs"

PHASE6_FILES = [
    "risk_scorecard_v1.json",
    "bid_decision_v1.md",
    "executive_risk_summary_v1.md",
    "pricing_risk_v1.json",
    "execution_risk_v1.json",
    "phase6_build_manifest_v1.json",
]

app = FastAPI(title="RFP Risk Engine (Local)")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run")
def run_engine():
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    rid = f"{ts}_{uuid.uuid4().hex[:8]}"
    run_dir = RUNS_ROOT / rid
    run_dir.mkdir(parents=True, exist_ok=False)

    # Run Phase 6 deterministically via Python (no PowerShell)
    try:
        _ = run_once()
        (run_dir / "stdout.txt").write_text("OK: phase6_runner.py executed\n", encoding="utf-8")
        (run_dir / "stderr.txt").write_text("", encoding="utf-8")
    except Exception as ex:
        (run_dir / "stdout.txt").write_text("", encoding="utf-8")
        (run_dir / "stderr.txt").write_text(str(ex) + "\n", encoding="utf-8")
        raise HTTPException(status_code=500, detail={
            "error": "Engine run failed",
            "run_id": rid,
            "exception": str(ex)
        })

    copied = []
    missing = []
    for fn in PHASE6_FILES:
        src = OUTPUT / fn
        if src.exists():
            shutil.copy2(src, run_dir / fn)
            copied.append(fn)
        else:
            missing.append(fn)

    status = "success" if not missing else "partial_success"

    return JSONResponse({
        "status": status,
        "run_id": rid,
        "copied": copied,
        "missing": missing
    })

@app.get("/runs/{run_id}/output/{filename}")
def get_run_output(run_id: str, filename: str):
    fp = RUNS_ROOT / run_id / filename
    if not fp.exists():
        raise HTTPException(status_code=404, detail=f"Not found: runs/{run_id}/{filename}")
    return FileResponse(fp)
