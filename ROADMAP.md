# RFP Risk & Scope Engine — Roadmap

**Last updated:** 2025-12-29 12:51:57  
**Repo:** C:\Users\shule\Documents\Shuler LLC\RFP_RISK_ENGINE

## Current State (As of this roadmap)
- Phase 4: Runtime Readiness — **LOCKED**
- Phase 5: Enrichment & Risk Intelligence — **LOCKED**
- Phase 6: Risk Scoring + Decisioning + Narratives — **LOCKED**
- Local execution proven:
  - PowerShell full run writes Phase 6 outputs to OUTPUT/
  - FastAPI wrapper proven locally
  - Docker container build + run proven locally

## Non-Negotiables (System Design)
1) **Deterministic core stays deterministic**
   - Scoring outputs are explainable from inputs
   - No “learning” modifies scoring logic
2) **Canonical universe remains immutable**
   - Question IDs, wording, and enrichment map are read-only
3) **Bolt-ons are allowed only via defined interfaces**
   - Storage Port (local filesystem today, cloud later)
   - Run Ledger Port (JSON today, DB later)
   - Ingestion Port (manual file drop today, upload pipeline later)

---

## Milestone 1 — Local Product Mode (Next)
Goal: run the engine like a real product on one machine, repeatedly, without tribal knowledge.

Deliverables:
- One command to start API
- One command to run Phase 6 and retrieve artifacts
- Outputs persist per run under OUTPUTS/runs/{run_id}/
- Verified endpoints documented in checkpoint snapshot

Exit criteria:
- 3 consecutive runs produce identical schema outputs (content varies, structure does not)
- Run artifacts retrievable through HTTP

---

## Milestone 2 — Phase 7-lite Rails (Schemas + Ledger Only)
Goal: define the future “knowledge base” rails without building cloud or AI retrieval.

Deliverables:
- Evidence manifest schema (documents, versions, tags, outcomes)
- Run ledger schema (inputs + config + outputs + hashes)
- App writes run_ledger.json per run (no DB required yet)

Exit criteria:
- Every run produces a run_ledger.json
- Run ledger references Phase 6 outputs without changing Phase 6 schemas

---

## Milestone 3 — Reverse Mode Ingestion (RFP -> Risk)
Goal: ingest an existing RFP/addendum package and map it against canonical questions.

Deliverables:
- RFP package structure (rfp_id, doc_id)
- Parsed text artifacts stored with the run
- Gap detection report (verbatim evidence pointers)

Exit criteria:
- Can drop in a real RFP and produce gaps + risk outputs without guesswork

---

## Milestone 4 — Helper Context Layer (No Canonical Changes)
Goal: create rationale/helper text/examples as a separate layer for AI-assisted answering later.

Deliverables:
- Helper context files keyed by question_id
- No edits to canonical questions
- Versioned helper bundle

Exit criteria:
- Helper context can be used by an LLM without changing scoring engine

---

## Milestone 5 — Public Hosting (Later, optional until needed)
Goal: hosted container + storage + multi-user/tenant model.

Notes:
- No dependency on developer workstation
- Storage moves to object storage; metadata moves to DB
- Domain wiring for smartmeterus.com occurs here

Exit criteria:
- Hosted endpoint runs from non-local compute
- Uploads + outputs persist independent of desktop
