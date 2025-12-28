# MASTER UNIVERSE SPECIFICATION v1.0

## RFP Risk & Scope Engine — Water AMI Installation (Domain v1.0)

**Status:** LOCK-READY (Post-Reconciliation)
**Mode:** EXECUTION
**Authority:** This document (v1.0) + Engine rules from prior spec lineage
**Primary Domain:** Water AMI Installation
**Engine Scope:** Domain-agnostic

---

## 0. AUTHORITY & VERSIONING

1. **This document is immutable.** Any modifications require explicit versioning (v1.1, v1.2, etc.).
2. **Machine IDs are the source of truth.** Once locked, IDs never change.
3. **Legacy artifacts are inputs only.** Their question IDs (A/B/C/D, PIT, INSIDE) are not authoritative post-reconciliation.

---

## 1. ENGINE vs DOMAIN (NON-NEGOTIABLE)

### 1.1 Engine Layer

The Engine Layer is reusable and domain-agnostic. It provides:

* Canonical question schema
* Deterministic runtime rules
* ID authority rules
* Token philosophy (tokens generated from answers, not authored here)
* No silent assumptions

### 1.2 Domain Layer

The Domain Layer supplies:

* Water AMI questions (CORE + extensions)
* Execution contexts (PIT, INSIDE, COMMERCIAL)
* Water-specific risk discovery coverage

**Rule:** The Domain may extend; it may not modify the Engine.

---

## 2. EXECUTION CONTEXTS

ExecutionContexts are modifiers, not separate universes:

* **PIT**
* **INSIDE**
* **COMMERCIAL**

Questions are authored once; applicability is controlled via `executionContexts`.

---

## 3. CANONICAL QUESTION UNIVERSE (POST-RECONCILIATION)

### 3.1 Canonical Files (Authoritative)

```
DOMAINS/WATER_AMI/questions/
├── core.json
├── pit_extensions.json
└── inside_extensions.json
```

* `core.json` is the single authoritative home for shared intent questions.
* `pit_extensions.json` contains PIT-only governance questions that cannot be expressed in CORE.
* `inside_extensions.json` contains INSIDE-only questions driven by customer access and interior risk.

---

## 4. ID AUTHORITY (LOCK-READY)

### 4.1 Canonical Pattern

```
<UTILITY>.<SECTION>.<SEQUENCE>
```

* Utility prefix: `W` (Water)
* Sections used in Water v1.0:

  * `CORE`
  * `PIT`
  * `INSIDE`

Examples:

* `W.CORE.110`
* `W.PIT.610`
* `W.INSIDE.110`

### 4.2 Ordering Rules

* Numeric ordering is authoritative.
* Gaps of **10** required.
* Order reflects **risk discovery**, not UI flow.

---

## 5. RECONCILIATION RESULT (WHAT CHANGED FROM LEGACY)

### 5.1 De-duplication Outcome

Legacy PIT A–D contained duplicates of CORE intent. Under v1.0:

* **CORE owns shared intent** across PIT and INSIDE.
* PIT A–D question clones are deprecated (not authored as separate questions).

### 5.2 No Wording Normalization in v1.0

* Prompts remain verbatim from their source artifacts.
* Wording normalization is deferred to a future version if explicitly instructed.

---

## 6. WATER DOMAIN COVERAGE (v1.0)

### 6.1 CORE Coverage

CORE covers:

* Program context and compliance
* Legacy environment and data readiness
* Customer outreach and completion governance
* Storage, custody, staging, disposal
* Survey readiness and exception handling

### 6.2 PIT Extensions Coverage

PIT extensions cover:

* Deployment strategy
* Routing and route governance
* RTU/UIR handling
* Data provisioning, validation, and closure impacts
* Seasonal/historic constraints
* Non-reading responsibility

### 6.3 INSIDE Extensions Coverage

INSIDE extensions cover:

* Indoor inclusion and scale
* Scheduling, appointments, outreach cadence
* Route closure definitions for probabilistic access
* Refusals and liability assignment
* Water shutoff methods, valve condition, curb stop governance
* Emergency response and restoration verification

---

## 7. LOCKED vs EXTENSIBLE (v1.0)

### 7.1 Locked in v1.0

* Engine vs Domain separation
* ID authority and ordering rules
* Canonical file split (core/pit/inside)
* Determinism expectation

### 7.2 Extensible in future versions

* Question wording normalization
* Additional execution contexts
* Additional domain industries (Electric/Gas)
* Token registry generation
* Runtime weighting/risk scoring enhancements

---

## 8. STOP CONDITIONS

* This v1.0 document establishes the lock-ready canonical universe.
* Any additions, deletions, rewording, or ID changes must be performed in a versioned update.

---

## FINAL DECLARATION

This v1.0 spec defines a single, coherent MASTER universe for Water AMI Installation that:

* Eliminates duplicate authored questions
* Prevents silent assumptions
* Separates Engine logic from Domain content
* Supports PIT and INSIDE execution without branching chaos
