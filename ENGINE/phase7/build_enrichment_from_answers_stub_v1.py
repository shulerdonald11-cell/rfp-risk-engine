import json
from pathlib import Path
from datetime import datetime, timezone

def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))

def write_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=False), encoding="utf-8")

def safe_list(x):
    return x if isinstance(x, list) else []

def safe_str(x):
    return x if isinstance(x, str) else ""

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--run-dir", required=True, help="Path to OUTPUTS/runs/<run_id>")
    args = p.parse_args()

    run_dir = Path(args.run_dir).resolve()
    answers_path = run_dir / "answers_snapshot.json"
    if not answers_path.exists():
        raise SystemExit(f"Missing answers snapshot: {answers_path}")

    answers_doc = read_json(answers_path)
    answers = safe_list(answers_doc.get("answers"))

    entries = []

    # MVP ENRICHMENT RULE:
    # - If an answer includes pricingImpacts and/or scopeImpacts, we emit an enrichment entry.
    # - This is a bridge: later we derive these from real question mapping logic + AI extraction.
    for a in answers:
        qid = safe_str(a.get("questionId"))
        if not qid:
            continue

        # Optional helper fields the UI/AI can populate
        title = safe_str(a.get("title")) or qid
        summary = safe_str(a.get("summary")) or safe_str(a.get("notes"))
        severity = safe_str(a.get("severity")).lower() or "medium"

        signals = a.get("signals") if isinstance(a.get("signals"), dict) else {}
        pricing_impacts = safe_list(signals.get("pricingImpacts"))
        scope_impacts   = safe_list(signals.get("scopeImpacts"))

        if not pricing_impacts and not scope_impacts:
            # Nothing to enrich yet (MVP)
            continue

        entry = {
            "id": f"ENR_{qid}",
            "questionId": qid,
            "title": title,
            "severity": severity,
            "summary": summary,
            "evidence": safe_list(a.get("evidence")),
            "mitigations": safe_list(a.get("mitigations")),
            "dependencies": safe_list(a.get("dependencies")),
            "clarifications": safe_list(a.get("clarifications")),
            "signals": {
                "pricingImpacts": pricing_impacts,
                "scopeImpacts": scope_impacts
            }
        }
        entries.append(entry)

    out = {
        "schema_version": "enrichment_map_v1.1",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),
        "source": {
            "type": "answers_snapshot",
            "path": "answers_snapshot.json"
        },
        "entries": entries
    }

    out_path = run_dir / "enrichment_map_run_v1.1.json"
    write_json(out_path, out)
    print(f"OK: wrote {out_path} (entries={len(entries)})")

if __name__ == "__main__":
    main()
