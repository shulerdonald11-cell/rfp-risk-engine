# PHASE 8 — Orchestration + UI (Revised MVP)

## Purpose
Phase 8 wires SmartMeterUS.com (or a web shell) to the locked Phase 6 engine so you can run end-to-end and SEE it work.

## Primary MVP Flow (Non-Negotiable)
1) User chooses:
   - (A) Fill questionnaire UI (Scope Builder)
   - (B) Upload answers JSON
2) System validates the answers payload (schema-level only)
3) System calls Phase 6 via FastAPI:
   - POST /run
4) System displays Phase 6 outputs verbatim (no rewriting):
   - risk scorecard
   - pricing risk
   - execution risk
   - bid decision narrative
   - executive summary
   - build manifest
5) System writes Phase 7-lite rails (adjacent artifacts only):
   - run ledger entry
   - answers snapshot reference

## Secondary Flow (Explicitly NOT MVP)
- Upload RFP / addendum documents for reverse analysis
- Clause extraction / mapping to canonical questions
These are Phase 9+.

## Storage (Phase 8 uses Phase 7-lite rails)
Filesystem only at first.
No database required.

## Boundaries
- Phase 6 is a black box: call it; do not modify it.
- Phase 8 must not rewrite Phase 6 outputs.
- Phase 8 may only add adjacent files and UI.

## NOT YET
- No public multi-tenant deployment
- No global shared knowledge base
- No reverse-RFP ingestion
