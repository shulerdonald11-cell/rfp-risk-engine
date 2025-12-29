# PHASE 7 — Conceptual Data Model (Not Coded)

## Design Principles
- Phase 6 outputs remain authoritative artifacts; Phase 7 stores pointers + context.
- Every stored item has:
  - stable ID
  - tenant boundary
  - provenance (who/when/source)
  - versioning strategy
- Everything stored must be explainable.

---

## Core Entities

### Tenant
- tenant_id
- name
- plan_tier
- data_policy (private_only | mixed | share_opt_in)
- created_at

### User
- user_id
- tenant_id
- role (owner | admin | sme | viewer)
- created_at

### Project
- project_id
- tenant_id
- name
- utility_id (nullable)
- description
- created_at

### Utility
- utility_id
- display_name
- visibility (public | tenant_only | redacted)
- notes

### Run (Ledger Entry)
- run_id
- tenant_id
- project_id
- mode (forward_scope | reverse_rfp)
- triggered_by_user_id
- timestamp
- phase6_inputs:
  - answers_ref
  - enrichment_version
  - scoring_config_version
- phase6_outputs:
  - output files (exact filenames, unchanged)
  - output locations (paths now; URIs later)
- status (success | failed)
- error_ref (if failed)

### Answers Snapshot
- answers_id
- run_id
- schema_version
- content_hash
- storage_ref
- created_at

### RFP Artifact (Document Record)
- rfp_id
- tenant_id
- utility_id (nullable)
- title
- issue_date (nullable)
- due_date (nullable)
- access_policy (store_raw_allowed | metadata_only | restricted)
- raw_files[] (optional pointers)
- normalized_text_ref (future)
- created_at

### Addendum
- addendum_id
- rfp_id
- number_or_label
- date
- access_policy
- raw_files[] (optional)
- created_at

### Knowledge Observation (Adjunct Memory)
- observation_id
- tenant_id
- scope (tenant_only | share_candidate)
- canonical_refs[] (question IDs)
- source_type (run_output | sme_note | rfp_clause | postmortem)
- source_ref (run_id/output_file OR rfp_id/addendum_id)
- claim
- evidence (text + pointers)
- confidence (low|med|high)
- created_by
- created_at

### SME Annotation
- annotation_id
- tenant_id
- created_by_user_id
- target_type (question | run_output | rfp_clause | project)
- target_ref (questionId OR run_id+file OR rfp_id+clause)
- content (markdown)
- tags[]
- created_at

### Approval Item (Trust Gate)
- approval_id
- tenant_id
- submitted_by
- payload_type (observation | annotation)
- payload_ref
- status (pending | approved | rejected)
- reviewed_by
- reviewed_at
- decision_notes

---

## Versioning Strategy
- Phase 6 artifacts: versioned by locked filename contract.
- Phase 7 schemas: semantic versioning.
- Stored objects include:
  - schema_version
  - content_hash
  - created_at

---

## Data Retention / Privacy Rules
- access_policy = metadata_only:
  - store only metadata + hashes
  - do NOT store raw or extracted text
- restricted:
  - tenant_only, no sharing, no cross-tenant analytics
- shared knowledge must be derived + de-identified.
