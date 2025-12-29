from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from pathlib import Path
from datetime import datetime, timezone
import uuid
import json
import shutil

from APP.phase6_runner import run_once

REPO_ROOT = Path(__file__).resolve().parents[1]
BUNDLE = REPO_ROOT / "DOMAINS" / "WATER_AMI" / "questions" / "runtime_bundle_v1.1.json"

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

app = FastAPI(title="RFP Risk Engine Questionnaire API (Local)")

def read_json_utf8sig(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def write_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/questions")
def get_questions():
    if not BUNDLE.exists():
        raise HTTPException(status_code=500, detail=f"Missing bundle: {BUNDLE}")
    return JSONResponse(read_json_utf8sig(BUNDLE))

@app.post("/answers")
def post_answers(payload: dict):
    # capture-only (no scoring)
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    run_id = f"{ts}_{uuid.uuid4().hex[:8]}"
    run_dir = RUNS_ROOT / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    write_json(run_dir / "answers.json", payload)

    return {
        "status": "saved",
        "run_id": run_id,
        "path": f"OUTPUTS/runs/{run_id}/answers.json"
    }

@app.post("/submit")
def submit_and_run(payload: dict):
    """
    Full flow:
    - save answers snapshot under OUTPUTS/runs/<run_id>/
    - write run_ledger_v1.json (Phase 7 rail)
    - run Phase 6 deterministically
    - copy Phase 6 outputs into the run folder
    """
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    run_id = f"{ts}_{uuid.uuid4().hex[:8]}"
    run_dir = RUNS_ROOT / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    # Save answers snapshot
    write_json(run_dir / "answers_snapshot.json", payload)

    # Phase 7 rail: run ledger
    ledger = {
        "schema_version": "run_ledger_v1",
        "run_id": run_id,
        "tenant_id": payload.get("tenant_id", "local-default"),
        "project_id": payload.get("project_id", "default"),
        "executed_at": datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),
        "phase6_version": "locked-v1",
        "inputs": {
            "answers_snapshot": "answers_snapshot.json"
        },
        "outputs": {
            "directory": f"OUTPUTS/runs/{run_id}"
        }
    }
    write_json(run_dir / "run_ledger_v1.json", ledger)

    # Run Phase 6
    try:
        _ = run_once()
        (run_dir / "stdout.txt").write_text("OK: phase6_runner.py executed\n", encoding="utf-8")
        (run_dir / "stderr.txt").write_text("", encoding="utf-8")
    except Exception as ex:
        (run_dir / "stdout.txt").write_text("", encoding="utf-8")
        (run_dir / "stderr.txt").write_text(str(ex) + "\n", encoding="utf-8")
        raise HTTPException(status_code=500, detail={"error": "Phase 6 run failed", "run_id": run_id, "exception": str(ex)})

    copied, missing = [], []
    for fn in PHASE6_FILES:
        src = OUTPUT / fn
        if src.exists():
            shutil.copy2(src, run_dir / fn)
            copied.append(fn)
        else:
            missing.append(fn)

    status = "success" if not missing else "partial_success"
    return {
        "status": status,
        "run_id": run_id,
        "copied": copied,
        "missing": missing
    }

@app.get("/runs/{run_id}/output/{filename}")
def get_run_output(run_id: str, filename: str):
    fp = RUNS_ROOT / run_id / filename
    if not fp.exists():
        raise HTTPException(status_code=404, detail=f"Not found: OUTPUTS/runs/{run_id}/{filename}")
    return FileResponse(fp)


@app.post("/submit_full")
def submit_full(payload: dict):
    from APP.phase6_runner import run_once
    from subprocess import run

    RUNS_ROOT.mkdir(parents=True, exist_ok=True)

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    run_id = f"{ts}_{uuid.uuid4().hex[:8]}"
    run_dir = RUNS_ROOT / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    # 1) write answers
    answers_path = run_dir / "answers_snapshot.json"
    answers_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    # 2) build run-scoped enrichment
    enrich_script = REPO_ROOT / "ENGINE" / "phase7" / "build_enrichment_from_answers_stub_v1.py"
    run([
        "python",
        str(enrich_script),
        "--run-dir",
        str(run_dir)
    ], check=True)

    enrichment_path = run_dir / "enrichment_map_run_v1.1.json"

    # 3) run Phase 6 using run-scoped enrichment
    _ = run_once(enrichment_path=enrichment_path)

    # 4) copy outputs
    copied = []
    for fn in PHASE6_FILES:
        src = OUTPUT / fn
        if src.exists():
            shutil.copy2(src, run_dir / fn)
            copied.append(fn)

    return {
        "status": "success",
        "run_id": run_id,
        "outputs": copied
    }
