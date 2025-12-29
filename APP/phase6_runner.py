import json
import os
from pathlib import Path
from datetime import datetime
import uuid

REPO_ROOT = Path(__file__).resolve().parents[1]

PHASE6_CFG = REPO_ROOT / "PHASE6" / "SCORING_CONFIG_v1.json"
ENRICHMENT = REPO_ROOT / "ENRICHMENT" / "enrichment_map_v1.1.json"

OUTPUT = REPO_ROOT / "OUTPUT"
RUNS_ROOT = REPO_ROOT / "OUTPUTS" / "runs"

OUT_RISK_SCORECARD = OUTPUT / "risk_scorecard_v1.json"
OUT_PRICING_RISK   = OUTPUT / "pricing_risk_v1.json"
OUT_EXEC_RISK      = OUTPUT / "execution_risk_v1.json"
OUT_EXEC_SUMMARY   = OUTPUT / "executive_risk_summary_v1.md"
OUT_BID_DECISION   = OUTPUT / "bid_decision_v1.md"
OUT_MANIFEST       = OUTPUT / "phase6_build_manifest_v1.json"

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

def compute_phase6(cfg: dict, enrichment: dict) -> dict:
    """
    Deterministic, explainable scoring:
    - Uses ONLY SCORING_CONFIG_v1.json + enrichment_map_v1.1.json
    - Separates pricing vs execution based on impacts arrays (if present)
    - Aggregates into a risk scorecard + decision output
    """
    entries = safe_list(enrichment.get("entries"))

    # Config defaults (won't explode if config is sparse)
    scoring = cfg.get("scoring", {})
    decision = cfg.get("decision", {})

    # Weights (optional): { severity: { low: 5, medium: 10, high: 20 } }
    sev_weights = scoring.get("severity_weights", {"low": 5, "medium": 10, "high": 20})

    # Thresholds (optional)
    # Example expected keys:
    # decision.thresholds = { "bid": 0-30, "caution": 31-60, "no_bid": 61-100 }
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

    # Overall score: deterministic rule (configurable later)
    overall_mode = scoring.get("overall_mode", "max")  # "max" or "avg"
    if overall_mode == "avg":
        overall_score = int(round((pricing_score + execution_score) / 2))
    else:
        overall_score = max(pricing_score, execution_score)

    # Decision bucket
    def bucket(score: int) -> str:
        b = "caution"
        bid_cfg = thresholds.get("bid", {})
        cau_cfg = thresholds.get("caution", {})
        nob_cfg = thresholds.get("no_bid", {})

        if "max" in bid_cfg and score <= int(bid_cfg["max"]):
            return "bid"
        if "min" in nob_cfg and score >= int(nob_cfg["min"]):
            return "no_bid"
        # caution default window
        min_c = int(cau_cfg.get("min", 31))
        max_c = int(cau_cfg.get("max", 60))
        if min_c <= score <= max_c:
            return "caution"
        # fallback
        if score < min_c:
            return "bid"
        return "no_bid"

    decision_bucket = bucket(overall_score)

    # Confidence indicator: deterministic mapping
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

def run_once(enrichment_path: Path = None) -> dict:
    cfg = read_json(PHASE6_CFG)
    enrichment = read_json(enrichment_path or ENRICHMENT)

    result = compute_phase6(cfg, enrichment)

    # Write primary outputs (same filenames)
    write_json(OUT_RISK_SCORECARD, {
        "scores": result["scores"],
        "decision": result["decision"]
    })
    write_json(OUT_PRICING_RISK, result["pricing"])
    write_json(OUT_EXEC_RISK, result["execution"])
    write_text(OUT_EXEC_SUMMARY, render_exec_summary(result))
    write_text(OUT_BID_DECISION, render_bid_decision(result))

    manifest = {
        "phase": 6,
        "generated_at_utc": datetime.utcnow().isoformat() + "Z",
        "inputs": {
            "scoring_config": str(PHASE6_CFG.relative_to(REPO_ROOT)),
            "enrichment_map": str(ENRICHMENT.relative_to(REPO_ROOT))
        },
        "outputs": [
            str(OUT_RISK_SCORECARD.relative_to(REPO_ROOT)),
            str(OUT_BID_DECISION.relative_to(REPO_ROOT)),
            str(OUT_EXEC_SUMMARY.relative_to(REPO_ROOT)),
            str(OUT_PRICING_RISK.relative_to(REPO_ROOT)),
            str(OUT_EXEC_RISK.relative_to(REPO_ROOT)),
        ]
    }
    write_json(OUT_MANIFEST, manifest)

    return result

def main():
    run_once()
    print("OK: Phase 6 outputs written to OUTPUT/")

if __name__ == "__main__":
    main()

