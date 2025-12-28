# PHASE 6 LOCK — RISK SCORING & BID DECISIONING

**Status:** LOCKED  
**Date Locked:** 2025-12-28 11:48:23 UTC  
**Engine:** RFP Risk & Scope Engine

---

## Scope of Lock
Phase 6 implements deterministic:
- Risk aggregation
- Pricing vs execution separation
- Bid / no-bid decisioning
- Executive narrative outputs
- Audit manifest generation

All logic consumes only Phase 5 outputs and Phase 6 control documents.

---

## Authoritative Phase 6 Control Documents (LOCKED)
- PHASE6/PHASE6_SCOPE.md
- PHASE6/INPUT_CONTRACT.md
- PHASE6/OUTPUT_TARGETS.md
- PHASE6/RISK_SCORING_PHILOSOPHY.md

---

## Authoritative Phase 6 Configuration
- PHASE6/SCORING_CONFIG_v1.json

⚠ Changes require:
- Version bump (e.g., v2)
- Full Phase 6 rebuild
- New manifest

---

## Authoritative Phase 6 Outputs (LOCKED)
- OUTPUT/risk_scorecard_v1.json
- OUTPUT/bid_decision_v1.md
- OUTPUT/executive_risk_summary_v1.md
- OUTPUT/pricing_risk_v1.json
- OUTPUT/execution_risk_v1.json
- OUTPUT/phase6_build_manifest_v1.json

---

## Explicitly Forbidden
- Editing Phase 5 enrichment outputs in place
- Modifying canonical questions or master spec
- Altering Phase 6 outputs without regeneration

---

## Permitted Future Actions
- Pressure testing via SCORING_CONFIG versioning
- New Phase 7 consumers
- New domains using Phase 6 as a reference pattern

---

Phase 6 is considered **complete, reproducible, and immutable** as of this lock.
