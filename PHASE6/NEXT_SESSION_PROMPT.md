You are operating in EXECUTION MODE.

PROJECT:
RFP Risk & Scope Engine

LOCKED STATE:
- Phase 4: Runtime Readiness (LOCKED)
- Phase 5: Enrichment & Risk Intelligence (LOCKED)
- Phase 6: Risk Scoring, Bid Decisioning, and Narrative Outputs (LOCKED)

AUTHORITATIVE PHASE 6 ARTIFACTS (READ-ONLY):
- PHASE6/PHASE6_LOCK.md
- PHASE6/PHASE6_SCOPE.md
- PHASE6/INPUT_CONTRACT.md
- PHASE6/OUTPUT_TARGETS.md
- PHASE6/RISK_SCORING_PHILOSOPHY.md
- PHASE6/SCORING_CONFIG_v1.json
- OUTPUT/risk_scorecard_v1.json
- OUTPUT/bid_decision_v1.md
- OUTPUT/executive_risk_summary_v1.md
- OUTPUT/pricing_risk_v1.json
- OUTPUT/execution_risk_v1.json
- OUTPUT/phase6_build_manifest_v1.json

IMMUTABLE INPUTS:
- MASTER_UNIVERSE_SPEC_v1.1.md
- Canonical Water AMI question universe
- ENRICHMENT/enrichment_map_v1.1.json
- OUTPUT/risk_summary_v1.md
- OUTPUT/gaps_v0.md

RULES:
- Phase 6 outputs may NOT be modified or regenerated
- Enrichment and canonical scope may NOT be edited
- Any changes to scoring require a NEW Phase 6 config version and re-lock

NEXT OBJECTIVE:
Proceed with Phase 7 (consumption, UI, multi-domain expansion, or historical pressure testing) using Phase 6 outputs as authoritative truth.
