import json
import shutil
from pathlib import Path
from datetime import datetime
import argparse

def write_run_ledger(
    repo_root: Path,
    run_id: str,
    answers_json_path: Path,
    phase6_version: str = "locked-v1",
    tenant_id: str = "local-default",
    project_id: str = "default",
):
    runs_root = repo_root / "OUTPUTS" / "runs" / run_id
    runs_root.mkdir(parents=True, exist_ok=True)

    answers_dest = runs_root / "answers_snapshot.json"
    shutil.copyfile(answers_json_path, answers_dest)

    ledger = {
        "schema_version": "run_ledger_v1",
        "run_id": run_id,
        "tenant_id": tenant_id,
        "project_id": project_id,
        "executed_at": datetime.utcnow().isoformat() + "Z",
        "phase6_version": phase6_version,
        "inputs": {
            "answers_snapshot": "answers_snapshot.json"
        },
        "outputs": {
            "directory": f"OUTPUTS/runs/{run_id}"
        }
    }

    ledger_path = runs_root / "run_ledger_v1.json"
    with ledger_path.open("w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2)

    print(f"Phase 7 run ledger written: {ledger_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Write Phase 7 run ledger")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--answers-json", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--phase6-version", default="locked-v1")
    parser.add_argument("--tenant-id", default="local-default")
    parser.add_argument("--project-id", default="default")

    args = parser.parse_args()

    write_run_ledger(
        repo_root=Path(args.repo_root).resolve(),
        run_id=args.run_id,
        answers_json_path=Path(args.answers_json).resolve(),
        phase6_version=args.phase6_version,
        tenant_id=args.tenant_id,
        project_id=args.project_id,
    )
