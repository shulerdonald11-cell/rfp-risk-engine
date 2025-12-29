import json
from pathlib import Path
from datetime import datetime, timezone

def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))

def write_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--run-dir", required=True, help="Path to OUTPUTS/runs/<run_id>")
    args = p.parse_args()

    run_dir = Path(args.run_dir).resolve()
    answers_path = run_dir / "answers_snapshot.json"
    if not answers_path.exists():
        raise SystemExit(f"Missing answers snapshot: {answers_path}")

    answers = read_json(answers_path)

    # STUB enrichment map that is valid shape-wise
    # Replace later with real question->signal mapping logic
    out = {
        "schema_version": "enrichment_map_v1.1",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),
        "source": {
            "type": "answers_snapshot",
            "path": "answers_snapshot.json"
        },
        "entries": []
    }

    out_path = run_dir / "enrichment_map_run_v1.1.json"
    write_json(out_path, out)
    print(f"OK: wrote {out_path}")

if __name__ == "__main__":
    main()
