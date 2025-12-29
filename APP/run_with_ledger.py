import argparse
import subprocess
import sys
from datetime import datetime
import uuid
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

def make_run_id() -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    suffix = uuid.uuid4().hex[:8]
    return f"{ts}_{suffix}"

def main():
    p = argparse.ArgumentParser(description="Run Phase 6 then write Phase 7 run ledger (non-breaking wrapper).")
    p.add_argument("--answers-json", dest="answers_json", required=True, help="Path to answers JSON (required).")
    p.add_argument("--tenant-id", dest="tenant_id", default="local-default")
    p.add_argument("--project-id", dest="project_id", default="default")
    p.add_argument("--phase6-version", dest="phase6_version", default="locked-v1")
    args = p.parse_args()

    answers_path = Path(args.answers_json)
    if not answers_path.exists():
        print(f"ERROR: answers json not found: {answers_path}", file=sys.stderr)
        return 2

    run_id = make_run_id()
    print(f"RUN_ID={run_id}")

    # 1) Run Phase 6 (writes to OUTPUT/ exactly as before)
    from APP.phase6_runner import run_once
    run_once()
    print("OK: Phase 6 outputs written to OUTPUT/")

    # 2) Write Phase 7 ledger (writes under OUTPUTS/runs/<run_id>/)
    ledger_py = REPO_ROOT / "ENGINE" / "phase7" / "write_run_ledger.py"
    if not ledger_py.exists():
        print(f"ERROR: missing ledger writer: {ledger_py}", file=sys.stderr)
        return 3

    cmd = [
        sys.executable, str(ledger_py),
        "--run-id", run_id,
        "--answers-json", str(answers_path),
        "--repo-root", str(REPO_ROOT),
        "--tenant-id", args.tenant_id,
        "--project-id", args.project_id,
        "--phase6-version", args.phase6_version,
    ]

    r = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if r.returncode != 0:
        print("WARN: Phase 7 ledger writer failed. Phase 6 outputs remain valid.", file=sys.stderr)
        return r.returncode

    print("OK: Phase 7 run ledger written.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
