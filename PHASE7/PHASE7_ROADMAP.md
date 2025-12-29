# PHASE 7 — Roadmap (Rails First, Intelligence Later)

## Phase 7-lite (Local, No DB)
Goal: store run ledger + inputs without breaking Phase 6.

1) Create folders + schemas
- Add PHASE7 and schema definitions for:
  - run_ledger_entry_v1
  - answers_snapshot_v1
  - approval_item_v1

2) Implement filesystem Run Ledger writer (adjacent to Phase 6)
- On run completion (orchestration layer):
  - write a run ledger JSON per run
  - store answers snapshot per run
- Keep Phase 6 output files untouched.

3) Add basic “Project Mode” organization (still filesystem)
- Either:
  - keep current runs folder and add project pointers in ledger
  - or optionally mirror runs under project folders

## Phase 7 proper (Still Local, Still Minimal)
4) SME annotations + approval queue
- Store annotations with status workflow:
  - DRAFT → PENDING_APPROVAL → APPROVED / REJECTED

5) RFP artifact registry (metadata-only supported)
- Allow creating an RFP record without storing raw files.
- Link future runs to rfp_id.

## What Can Be Tested Locally
- ledger files get written
- answers snapshots persist
- annotations persist
- approval status changes
- no impact to Phase 6 outputs

## What Requires Cloud Later (Not Now)
- Multi-tenant auth + isolation enforcement
- Object storage for uploads
- DB for indexing/search
- Any global shared knowledge needs legal + policy controls

## Explicit NOT YET Decisions
- No cloud accounts, billing, or deployment.
- No reverse-RFP ingestion pipeline in Phase 7 deliverables.
- No global shared knowledge base until tenant isolation + policy exist.
