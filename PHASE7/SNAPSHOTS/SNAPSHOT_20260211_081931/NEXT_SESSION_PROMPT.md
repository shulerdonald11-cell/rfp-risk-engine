You are operating in EXECUTION MODE (baby steps only).

PROJECT:
RFP Risk & Scope Engine — Water AMI

REPO ROOT:
C:\Users\shule\Documents\Shuler LLC\RFP_RISK_ENGINE

AUTHORITATIVE DOCS:
- Phase 6 is LOCKED (PHASE6/*.md + SCORING_CONFIG_v1.json).
- Phase 7 is a non-breaking memory/ledger layer.
- Phase 8 is orchestration + UI; it must not rewrite Phase 6 outputs.

CURRENT VERIFIED STATE:
- Runtime runs live in OUTPUTS/runs/<run_id>/.
- Phase 7 stub exists:
  ENGINE/phase7/build_enrichment_from_answers_stub_v1.py
- Phase 6 runner exists and writes to run folder:
  APP/phase6_runner.py

THIS SESSION OBJECTIVE (MVP v0.1 hardening):
1) Define minimal answers_snapshot.json contract (schema + example + validation rules).
2) Create ONE orchestrator command/script that:
   - creates run folder
   - writes answers_snapshot.json
   - runs Phase 7 stub -> enrichment_map_run_v1.1.json
   - runs Phase 6 runner -> run/phase6 outputs
3) Fail-fast if any required file is missing.
4) No AI integration yet. No reverse-RFP ingestion yet (Phase 9+).

GUARDRAILS:
- Do NOT overwrite OUTPUT/.
- Do NOT modify Phase 6 lock docs.
- Small changes only; keep it deterministic.
