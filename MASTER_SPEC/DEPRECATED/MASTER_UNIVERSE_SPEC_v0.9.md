NOTE:
This version (v0.9) is deprecated.
See MASTER_UNIVERSE_SPEC_v1.0.md for the authoritative specification.

# MASTER UNIVERSE SPECIFICATION v0.9

## RFP Risk & Scope Engine — Water AMI Installation (Domain v1.0)

**Status:** DESIGN — LOCK-READY
**Mode:** REBUILD / REBASE
**Authority:** This document only
**Primary Domain:** Water AMI Installation
**Engine Scope:** Domain-agnostic

---

## 0. CORE DECLARATION (ENGINE vs DOMAIN)

This system defines a **domain-agnostic RFP Risk & Scope Engine**, instantiated in v1.0 for **Water AMI Installation**.

* The **Engine Layer** is universal and reusable across industries.
* The **Domain Layer** supplies industry-specific questions, risks, and language.
* Future industries (Electric, Gas, non-utility trades, other RFP-driven niches) are supported by adding new domain bundles **without modifying the Engine Layer**.

This document governs both layers.

---

## 1. ENGINE LAYER (DOMAIN-AGNOSTIC)

### 1.1 Engine Purpose

The Engine exists to:

* Surface **explicit risk**
* Eliminate **silent assumptions**
* Produce **deterministic scope outputs**
* Support **bidirectional inference**:

  * Question → Scope (Owner / Utility)
  * RFP → Risk (Contractor / Engineer)

The Engine is **access-agnostic** and unaware of licensing, subscriptions, or user identity.

---

### 1.2 Canonical Question Model (Engine Schema)

```json
{
  "questionId": "W.CORE.110",
  "humanLabel": "Program Start Date",
  "order": 110,
  "domainId": "WATER_AMI",
  "section": "CORE",
  "executionContexts": ["PIT", "INSIDE", "COMMERCIAL"],
  "prompt": "string (verbatim, procurement-safe)",
  "answerType": "single | multi | number | date | text | matrix",
  "options": [],
  "notesEnabled": true,
  "helperText": "best practice + implications",
  "riskIntent": ["schedule", "productivity", "liability"],
  "status": "draft | normalized | lock_ready"
}
```

Rules:

* Questions are authored **once**
* Applicability is handled via `executionContexts`
* No branching logic lives inside questions

---

### 1.3 ID Authority (LOCKED)

* **Machine IDs are the source of truth**
* Human labels are presentation only
* IDs never change once locked

**Canonical Pattern**

```
<UTILITY>.<SECTION>.<SEQUENCE>
```

Examples:

* `W.CORE.110`
* `W.EXEC.240`
* `E.CORE.110`
* `G.COMM.315`

---

### 1.4 Ordering Model

* Numeric ordering is authoritative
* Gaps of 10 required
* Order reflects **risk discovery**, not UI flow
* ExecutionContexts may suppress visibility but may not reorder questions

---

### 1.5 Notes & Assumptions

* Notes are **first-class data**
* Any assumption must be traceable to a question, answer, or explicit unknown
* Notes feed scope language, risk summaries, and knowledge harvesting

No silent assumptions. Ever.

---

## 2. ANSWER TOKEN ENGINE

### 2.1 Token Philosophy (LOCKED)

Tokens are **machine-readable semantic facts** derived from answers.

* Internal plumbing
* Human-readable
* Stable across wording changes
* Not directly exposed to users

---

### 2.2 Token Structure

```
<DOMAIN>.<QUESTIONID>.<MEANING>
```

Examples:

* `WATER.W.CORE.110.START_DATE_UNKNOWN`
* `WATER.W.INSIDE.315.APPOINTMENTS_REQUIRED`
* `WATER.W.COMM.410.METER_SIZE_LARGE`

---

### 2.3 Token Rules

* One token per explicit meaning
* Multi-select answers emit multiple tokens
* Tokens stack, never overwrite
* Notes do not emit tokens directly

---

### 2.4 Unknowns & Escalation

Unknown answers:

* Increase risk
* Shift liability to issuer
* Justify escalation

Escalation ladder:

```
Unknowns → Risk ↑ → Consulting Recommended → Survey (if justified)
```

No hard blocking.

---

## 3. RUNTIME ENGINE

### 3.1 Determinism Rule

Identical inputs MUST produce materially identical outputs.

---

### 3.2 Flow Rules

* One question at a time
* Forward / Back always allowed
* Restart resets session
* Unknowns are allowed and surfaced

---

### 3.3 Branching Rule (LOCKED)

Branching may:

* Control visibility
* Adjust emphasis
* Increase risk weighting

Branching may NOT:

* Rewrite reality
* Reorder the universe
* Create alternate scope structures

---

## 4. KNOWLEDGE HARVESTING ENGINE

### 4.1 Knowledge Model

* Notes may be token-tagged and context-aware
* Notes may be anonymized and harvested
* No auto-promotion
* All knowledge requires approval

This forms a **living standards engine**.

---

## 5. ACCESS & ENTITLEMENT (OUT OF SCOPE)

Licensing, subscriptions, and usage limits exist **above** the Engine and do not influence scope logic.

---

# DOMAIN LAYER — WATER AMI INSTALLATION (v1.0)

## 6. Execution Contexts

ExecutionContexts are modifiers, not bundles:

* PIT
* INSIDE
* COMMERCIAL

---

## 7. Water Meter Classification

* **Small** — typically residential
* **Intermediate** — 1.5–2 in (commercial or residential irrigation)
* **Large** — ≥3 in (commercial / industrial)

---

## 8. Commercial Logic

Commercial meters introduce:

* Access scheduling complexity
* Lower completion certainty
* Higher productivity variance
* Elevated liability exposure

Handled via tokens, risk language, and consulting escalation.

---

## 9. Survey & Consulting Logic

* Surveys are best practice
* Consulting precedes surveys
* Surveys are justified, not forced

---

## 10. NON-NEGOTIABLE PRINCIPLES

1. No duplicate questions
2. No silent assumptions
3. No PIT-only universes
4. No branching chaos
5. Clarity over completeness
6. Explicit risk over false precision

---

## 11. LOCKED vs EXTENSIBLE

**Locked in v1.0**

* Engine schema
* ID authority
* Token philosophy
* Determinism rules
* Risk escalation logic

**Extensible**

* Question wording
* Domain bundles
* Additional industries
* Consulting products
* AI ingestion adapters

---

## 12. LOCAL & GITHUB FOLDER STRUCTURE (REFERENCE)

```text
RFP_RISK_ENGINE/
│
├── README.md
├── MASTER_SPEC/
│   └── MASTER_UNIVERSE_SPEC_v0.9.md
│
├── ENGINE/
│   ├── schema/
│   │   ├── question.schema.json
│   │   ├── token.schema.json
│   │   └── runtime.rules.md
│   ├── methodology/
│   │   └── engine_philosophy.md
│   └── knowledge/
│       └── harvesting_rules.md
│
├── DOMAINS/
│   ├── WATER_AMI/
│   │   ├── questions/
│   │   │   ├── core.json
│   │   │   ├── pit_extensions.json
│   │   │   ├── inside_extensions.json
│   │   │   └── commercial_extensions.json
│   │   ├── tokens/
│   │   │   └── water_token_registry_draft.json
│   │   ├── methodology/
│   │   │   └── water_ami_methodology.md
│   │   └── README.md
│   │
│   ├── ELECTRIC_AMI/        # future
│   └── GAS_AMI/             # future
│
├── INGESTION/
│   ├── rfp_parsers/
│   ├── auto_answering/
│   └── risk_extraction/
│
├── OUTPUTS/
│   ├── scope_generation/
│   ├── risk_summaries/
│   └── assumptions/
│
└── ARCHIVE/
    └── legacy_inputs/
```

---

## FINAL DECLARATION

This system is designed to outlive Water AMI, outscale individual companies, and expose risk wherever RFPs attempt to hide it.
