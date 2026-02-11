import json
from pathlib import Path
from datetime import datetime, timezone
import uuid

REPO_ROOT = Path(__file__).resolve().parents[1]

PHASE6_CFG = REPO_ROOT / "PHASE6" / "SCORING_CONFIG_v1.json"
DEFAULT_ENRICHMENT = REPO_ROOT / "ENRICHMENT" / "enrichment_map_v1.1.json"

OUTPUT_LOCKED = REPO_ROOT / "OUTPUT"                # canonical locked baseline (DO NOT WRITE)
RUNS_ROOT     = REPO_ROOT / "OUTPUTS" / "runs"      # runtime executions live here

def read_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return json.loads(path.read_text(encoding="utf-8-sig"))

def write_json(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=False), encoding="utf-8")

def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def safe_list(x):
    return x if isinstance(x, list) else []

def safe_str(x):
    return x if isinstance(x, str) else ""

def make_run_root() -> Path:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "_" + uuid.uuid4().hex[:8]
    run_root = RUNS_ROOT / run_id
    run_root.mkdir(parents=True, exist_ok=True)
    return run_root

def compute_phase6(cfg: dict, enrichment: dict) -> dict:
    entries = safe_list(enrichment.get("entries"))

    scoring = cfg.get("scoring", {})
    decision = cfg.get("decision", {})

    sev_weights = scoring.get("severity_weights", {"low": 5, "medium": 10, "high": 20})

    thresholds = decision.get("thresholds", {
        "bid": {"max": 30},
        "caution": {"min": 31, "max": 60},
        "no_bid": {"min": 61}
    })

    pricing_items = []
    execution_items = []

    pricing_score = 0
    execution_score = 0

    for e in entries:
        eid = safe_str(e.get("id"))
        qid = safe_str(e.get("questionId"))
        title = safe_str(e.get("title"))
        severity = safe_str(e.get("severity")).lower() or "medium"
        weight = int(sev_weights.get(severity, sev_weights.get("medium", 10)))

        signals = e.get("signals", {}) if isinstance(e.get("signals"), dict) else {}
        pricing_impacts = safe_list(signals.get("pricingImpacts"))
        scope_impacts = safe_list(signals.get("scopeImpacts"))

        base = {
            "id": eid,
            "questionId": qid,
            "title": title,
            "severity": severity,
            "weight": weight,
            "summary": safe_str(e.get("summary")),
            "evidence": safe_list(e.get("evidence")),
            "mitigations": safe_list(e.get("mitigations")),
            "dependencies": safe_list(e.get("dependencies")),
            "clarifications": safe_list(e.get("clarifications")),
        }

        if pricing_impacts:
            pricing_score += weight
            pricing_items.append({**base, "impacts": pricing_impacts})

        if scope_impacts:
            execution_score += weight
            execution_items.append({**base, "impacts": scope_impacts})

    overall_mode = scoring.get("overall_mode", "max")  # "max" or "avg"
    if overall_mode == "avg":
        overall_score = int(round((pricing_score + execution_score) / 2))
    else:
        overall_score = max(pricing_score, execution_score)

    def bucket(score: int) -> str:
        bid_cfg = thresholds.get("bid", {})
        cau_cfg = thresholds.get("caution", {})
        nob_cfg = thresholds.get("no_bid", {})

        if "max" in bid_cfg and score <= int(bid_cfg["max"]):
            return "bid"
        if "min" in nob_cfg and score >= int(nob_cfg["min"]):
            return "no_bid"

        min_c = int(cau_cfg.get("min", 31))
        max_c = int(cau_cfg.get("max", 60))
        if min_c <= score <= max_c:
            return "caution"

        if score < min_c:
            return "bid"
        return "no_bid"

    decision_bucket = bucket(overall_score)

    confidence_map = decision.get("confidence", {
        "bid": 0.85,
        "caution": 0.60,
        "no_bid": 0.25
    })
    confidence = float(confidence_map.get(decision_bucket, 0.60))

    return {
        "scores": {
            "overall": overall_score,
            "pricing": pricing_score,
            "execution": execution_score,
            "overall_mode": overall_mode
        },
        "decision": {
            "bucket": decision_bucket,
            "confidence": confidence
        },
        "pricing": {
            "score": pricing_score,
            "items": pricing_items
        },
        "execution": {
            "score": execution_score,
            "items": execution_items
        }
    }

def render_exec_summary(result: dict) -> str:
    s = result["scores"]
    d = result["decision"]
    top_exec = result["execution"]["items"][:10]
    top_price = result["pricing"]["items"][:10]

    lines = []
    lines.append("# Executive Risk Summary (Phase 6)")
    lines.append("")
    lines.append(f"- Overall Score: **{s['overall']}**")
    lines.append(f"- Pricing Score: **{s['pricing']}**")
    lines.append(f"- Execution Score: **{s['execution']}**")
    lines.append(f"- Decision: **{d['bucket'].upper()}** (confidence {d['confidence']:.2f})")
    lines.append("")
    lines.append("## Top Execution Risks")
    if not top_exec:
        lines.append("- None flagged from enrichment signals.")
    else:
        for x in top_exec:
            lines.append(f"- [{x.get('severity','')}] {x.get('questionId','')} {x.get('title','')}".strip())
    lines.append("")
    lines.append("## Top Pricing Risks")
    if not top_price:
        lines.append("- None flagged from enrichment signals.")
    else:
        for x in top_price:
            lines.append(f"- [{x.get('severity','')}] {x.get('questionId','')} {x.get('title','')}".strip())
    lines.append("")
    return "\n".join(lines)

def render_bid_decision(result: dict) -> str:
    s = result["scores"]
    d = result["decision"]
    lines = []
    lines.append("# Bid Decision (Phase 6)")
    lines.append("")
    lines.append(f"Decision: **{d['bucket'].upper()}**")
    lines.append(f"Confidence: **{d['confidence']:.2f}**")
    lines.append("")
    lines.append("## Scores")
    lines.append(f"- Overall: {s['overall']}")
    lines.append(f"- Pricing: {s['pricing']}")
    lines.append(f"- Execution: {s['execution']}")
    lines.append("")
    return "\n".join(lines)

def run_once(enrichment_path: Path = None, run_root: Path = None) -> Path:
    cfg = read_json(PHASE6_CFG)

    enrichment_path = enrichment_path or DEFAULT_ENRICHMENT
    enrichment_path = enrichment_path.resolve()
    enrichment = read_json(enrichment_path)

    result = compute_phase6(cfg, enrichment)

    run_root = (run_root.resolve() if run_root else make_run_root())
    phase6_dir = run_root / "phase6"
    phase6_dir.mkdir(parents=True, exist_ok=True)

    out_risk_scorecard = phase6_dir / "risk_scorecard_v1.json"
    out_pricing_risk   = phase6_dir / "pricing_risk_v1.json"
    out_exec_risk      = phase6_dir / "execution_risk_v1.json"
    out_exec_summary   = phase6_dir / "executive_risk_summary_v1.md"
    out_bid_decision   = phase6_dir / "bid_decision_v1.md"
    out_manifest       = phase6_dir / "phase6_build_manifest_v1.json"

    write_json(out_risk_scorecard, {
        "scores": result["scores"],
        "decision": result["decision"]
    })
    write_json(out_pricing_risk, result["pricing"])
    write_json(out_exec_risk, result["execution"])
    write_text(out_exec_summary, render_exec_summary(result))
    write_text(out_bid_decision, render_bid_decision(result))

    # relative paths for manifest (best-effort)
    def rel(p: Path) -> str:
        try:
            return str(p.resolve().relative_to(REPO_ROOT))
        except Exception:
            return str(p)

    manifest = {
        "phase": 6,
        "generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "inputs": {
            "scoring_config": rel(PHASE6_CFG),
            "enrichment_map": rel(enrichment_path)
        },
        "outputs": [
            rel(out_risk_scorecard),
            rel(out_bid_decision),
            rel(out_exec_summary),
            rel(out_pricing_risk),
            rel(out_exec_risk),
            rel(out_manifest),
        ]
    }
    write_json(out_manifest, manifest)

    return phase6_dir

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--enrichment", default=str(DEFAULT_ENRICHMENT), help="Path to enrichment map JSON")
    p.add_argument("--run-dir", default=None, help="Path to OUTPUTS/runs/<run_id> (writes into <run-dir>/phase6)")
    args = p.parse_args()

    enrich = Path(args.enrichment)
    run_root = Path(args.run_dir) if args.run_dir else None

    phase6_dir = run_once(enrich, run_root)
    print(f"OK: Phase 6 outputs written to {phase6_dir}")

if __name__ == "__main__":
    main()
