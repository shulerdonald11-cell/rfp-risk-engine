# SYSTEM SNAPSHOT ADDENDUM — Phase 7 + Phase 8 (Non-Breaking)

## Phase 6 Status (Locked)
Phase 6 remains LOCKED and IMMUTABLE:
- deterministic scoring and narrative generation
- output filenames and formats unchanged
- FastAPI wrapper contains no business logic
- /run and /runs/{id}/output/{file} remain the runtime contract

## Phase 7 Definition (Optional Rails)
Phase 7 is an adjacent layer that:
- stores run ledger entries and inputs
- stores SME annotations and approval queue
- stores RFP metadata and (when permitted) raw files
- enables future reverse-RFP and comparative analytics
Phase 7 must not modify Phase 6 outputs or logic.

## Phase 8 Definition (Orchestration + UI Wiring)
Phase 8 is a presentation/orchestration layer that:
- provides Scope Builder UI (questionnaire or answers JSON upload)
- triggers Phase 6 via POST /run
- displays Phase 6 outputs verbatim
- writes Phase 7-lite ledger artifacts as non-breaking add-ons

Reverse-RFP upload is secondary and not part of Phase 8 primary MVP flow.
