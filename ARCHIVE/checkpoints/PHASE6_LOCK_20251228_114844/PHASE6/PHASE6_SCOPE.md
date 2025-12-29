# PHASE 6 Scope

## Purpose
Phase 6 adds **risk scoring, bid decisioning, and executive narrative outputs** by consuming Phase 4 and Phase 5 outputs.

## Allowed
- Read Phase 5 outputs:
  - ENRICHMENT/enrichment_map_v1.1.json
  - OUTPUT/risk_summary_v1.md
- Read Phase 4 outputs:
  - OUTPUT/validation_v0.json
  - OUTPUT/scope_v0.md
  - OUTPUT/gaps_v0.md
- Produce derived artifacts in OUTPUT/ (new files only)

## Not Allowed
- No edits to canonical question JSON files
- No edits to MASTER_UNIVERSE_SPEC
- No edits to Phase 4 build scripts
- No edits to Phase 5 enrichment outputs
- No inventing new questions

## Non-negotiables
- Deterministic behavior (same inputs => same outputs)
- Explainable scoring (no mystery math)
- Separation of pricing risk vs execution risk