# PHASE 7 — Concept (Optional Intelligence + Memory Layer)

## Purpose
Phase 7 adds a **non-breaking extension layer** around the locked Phase 6 deterministic engine:
- Persists run metadata (run ledger) and user-submitted inputs
- Stores RFP/source documents (when allowed) and normalized “artifacts”
- Captures SME annotations with an approval workflow
- Enables future comparative analytics across utilities/projects without changing Phase 6

Phase 6 remains the execution core and output contract authority.

## Scope (What Phase 7 Includes)
1) **Run Ledger (Phase 7-lite)**
   - Record: who ran what, when, with which inputs, and where outputs were stored.
   - No changes to Phase 6 output filenames or formats.

2) **Knowledge Objects**
   - Structured records for: utilities, projects, RFPs, addenda, and extracted “observations”.
   - “Observations” are explicitly NOT canonical truth. They are adjunct memory.

3) **SME Annotation Capture**
   - Store expert commentary tied to:
     - specific canonical question IDs
     - specific output artifacts
     - specific RFP clauses/pages (future)
   - Includes approval workflow (owner approves; later vetted experts contribute).

4) **Retention + Privacy Rails**
   - Store raw documents only when permitted.
   - Support “metadata-only” storage when NDA/restrictions exist.

## Boundaries vs Phase 6 (Non-Negotiable)
- Phase 6 is LOCKED and IMMUTABLE (logic + outputs + contracts).
- Phase 7 may only:
  - create new folders/files
  - store metadata
  - store copies of inputs (answers, uploaded docs) as separate artifacts
- Phase 7 must NOT:
  - modify Phase 6 outputs
  - reinterpret scoring
  - mutate canonical questions/spec/enrichment

## What Remains Local (Near Term)
- Everything can run on the local developer machine and local Docker container.
- Storage can be filesystem-only for Phase 7-lite.

## What Eventually Must Be Cloud (Later)
Only when you actually go multi-user/public:
- Object storage for uploads + run artifacts
- Auth + tenant isolation
- Database for ledger + indexing

Cloud is explicitly NOT part of Phase 7 execution right now.

## “Shared Knowledge” vs “Never Global”
- Never Global:
  - any NDA-protected raw documents
  - any customer/asset-level data files
  - anything uploaded under explicit confidentiality
- Potentially Shared (subscription-tier gated):
  - utility identity + high-level project metadata (if not restricted)
  - de-identified risk frequencies derived from many runs
  - sanitized learnings without proprietary attachments

## Phase 7 Success Criteria
You can run Scope Builder → Phase 6 and see:
- outputs
- run ledger entry
- stored answers snapshot
- optional links to uploaded docs (when allowed)
All without changing Phase 6.
