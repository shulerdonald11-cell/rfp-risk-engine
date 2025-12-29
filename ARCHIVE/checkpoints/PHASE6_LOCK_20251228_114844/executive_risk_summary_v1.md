# Executive Risk Summary

## Snapshot
*  
**Pricing Risk Score:** 44  
**Execution Risk Score:** 44  
**Overall Risk Score:** 44

---

## What Is Driving Risk
The following summary reflects aggregated Phase 5 enrichment signals and deterministic Phase 6 scoring logic.

# Water AMI Risk Summary (v1)

Generated: 2025-12-28 10:55:09
Source: OUTPUT/gaps_v0.md (unanswered) + ENRICHMENT/enrichment_map_v1.1.json
Rule: Intelligence lives outside canonical question files; no wording/ID/order changes.

## Top Unanswered Risks (High-Impact Subset)

* W.INSIDE.340 | Score: 95 | HIGH | Interior Damage/Leak Liability
* W.CORE.250 | Score: 92 | HIGH | Data Readiness
* W.CORE.270 | Score: 90 | HIGH | Data Reliance/Change Control
* W.INSIDE.210 | Score: 90 | HIGH | Customer Access/Scheduling
* W.CORE.140 | Score: 88 | HIGH | Compliance/Labor
* W.INSIDE.360 | Score: 88 | HIGH | Shutoff Method/Isolation Risk
* W.PIT.730 | Score: 88 | HIGH | Data Provisioning
* W.PIT.700 | Score: 87 | HIGH | Progression Protection
* W.CORE.320 | Score: 86 | HIGH | Survey/Front-End Risk Burn Down
* W.INSIDE.390 | Score: 86 | HIGH | Valve Replacement Authorization
* W.PIT.770 | Score: 86 | HIGH | Non-Read Liability
* W.PIT.680 | Score: 85 | HIGH | RTU Scope Leakage
* W.INSIDE.250 | Score: 84 | HIGH | Call Center/Dispatch
* W.PIT.660 | Score: 84 | HIGH | Route Governance/Throughput
* W.PIT.690 | Score: 83 | HIGH | UIR Dependency

## Risk Detail (By Category)

### Call Center/Dispatch

#### W.INSIDE.250 (Score 84, HIGH)

Prompt: Will contractor-provided call center and dispatch capability be required for indoor scheduling?

Impact: Pricing: Call center is a real cost center; pretending otherwise is expensive | Scope: Same-day fills, cancellation recovery

If unanswered (default): Assume call center needed for meaningful indoor volume; include in pricing if undefined

Mitigation guidance: Define staffing hours, channels, language needs, and dispatch authority

### Compliance/Labor

#### W.CORE.140 (Score 88, HIGH)

Prompt: Are there any labor compliance or workforce requirements applicable to this project?

Impact: Pricing: Prevailing wage / Davis-Bacon / PLA / union requirements can swing unit pricing materially | Scope: Crew composition, productivity assumptions, mobilization and admin burden

If unanswered (default): Assume prevailing wage / compliance unknown; carry contingency and require disclosure pre-award

Mitigation guidance: Require explicit labor compliance language and funding source disclosure early

### Customer Access/Scheduling

#### W.INSIDE.210 (Score 90, HIGH)

Prompt: Who is responsible for customer outreach and appointment scheduling for indoor meter installations?

Impact: Pricing: Who owns scheduling drives staffing, call center cost, failure rate | Scope: Completion curve, cancellations, no-response plateau

If unanswered (default): Assume contractor-led scheduling is required for performance; price call center if unknown

Mitigation guidance: Define roles, outreach plan, and utility support actions

### Data Provisioning

#### W.PIT.730 (Score 88, HIGH)

Prompt: Will the Utility provide a master CIS/service data file?

Impact: Pricing: No master file = manual build of work orders, high admin cost | Scope: Start-up timeline, integration, quality

If unanswered (default): Assume master file exists but may be incomplete; require sample and refresh plan

Mitigation guidance: Require sample extract, cadence, transfer method, and defect process

### Data Readiness

#### W.CORE.250 (Score 92, HIGH)

Prompt: Will the utility provide service-level or asset-level data to support installation planning?

Impact: Pricing: No/partial asset data forces survey labor or conservative production rates | Scope: Material kitting, truck load-outs, failed visits, rework, schedule slip

If unanswered (default): Assume data is partial unless proven otherwise; include survey/add-alternate or contingency

Mitigation guidance: Require sample extract + data dictionary + accuracy statement; align change control to data defects

### Data Reliance/Change Control

#### W.CORE.270 (Score 90, HIGH)

Prompt: How should existing service-level or asset-level data be relied upon for installation planning and deployment?

Impact: Pricing: If contractor must validate everything, price rises (survey + failed installs) | Scope: Disputes over productivity and exceptions if data is informational only

If unanswered (default): Assume data requires validation; trigger survey recommendation and explicit exception workflow

Mitigation guidance: Contract language: who owns data accuracy, what happens when it is wrong, and how exceptions are paid

### Interior Damage/Leak Liability

#### W.INSIDE.340 (Score 95, HIGH)

Prompt: How should responsibility be assigned for leaks or damage associated with indoor installations?

Impact: Pricing: Unlimited liability = unlimited pricing | Scope: Claims, customer satisfaction, emergency response

If unanswered (default): Contractor liable for workmanship only; pre-existing plumbing is utility/customer

Mitigation guidance: Define criteria, documentation, response time, and claim workflow

### Non-Read Liability

#### W.PIT.770 (Score 86, HIGH)

Prompt: If installation is correct but communication fails due to system/material constraints, how is responsibility assigned?

Impact: Pricing: If contractor eats comm failures, bids get padded | Scope: Warranty disputes and rework

If unanswered (default): Assume ownership is case-by-case unless clarified; flag as major commercial risk

Mitigation guidance: Separate install workmanship vs system/material constraints; set responsibility boundaries

### Progression Protection

#### W.PIT.700 (Score 87, HIGH)

Prompt: If RTU/UIR items remain unresolved due to utility-side delays, may the contractor advance to new routes?

Impact: Pricing: No protection forces repeated revisits and kills production | Scope: Schedule certainty and cashflow

If unanswered (default): Assume contractor must be allowed to advance when blocked by utility delays

Mitigation guidance: Add progression rule: unresolved RTU/UIR does not block new routes after documentation

### Route Governance/Throughput

#### W.PIT.660 (Score 84, HIGH)

Prompt: Will route-level completion thresholds be required before advancing?

Impact: Pricing: Hard gating thresholds reduce productivity and increase revisits | Scope: Route closure definition, RTU/UIR backlog, completion plateau risk

If unanswered (default): Assume gating exists unless explicitly denied; require progression protection language

Mitigation guidance: Define closure dispositions + allow advance when remaining are RTU/UIR/no-access

### RTU Scope Leakage

#### W.PIT.680 (Score 85, HIGH)

Prompt: How should locations outside contractor scope be handled?

Impact: Pricing: Undefined RTU = contractor absorbs out-of-scope time unless paid | Scope: Exception handling, reconciliation, program closeout

If unanswered (default): Assume RTU exists; require formal disposition + commercial treatment

Mitigation guidance: Define RTU reasons, documentation, and payment rules (attempt fee or unit credit)

### Shutoff Method/Isolation Risk

#### W.INSIDE.360 (Score 88, HIGH)

Prompt: What is the expected primary method for shutting off water during indoor meter replacement?

Impact: Pricing: If curb stop/valves are unreliable, installs slow and risk skyrockets | Scope: Crew tooling, escalation needs, failure modes

If unanswered (default): Assume interior valve preferred with curb stop backup; require curb stop authorization clarity

Mitigation guidance: Define isolation method, backup plan, and who responds when isolation fails

### Survey/Front-End Risk Burn Down

#### W.CORE.320 (Score 86, HIGH)

Prompt: Will a pre-deployment field survey or audit be required to validate asset data, site conditions, or work scope prior to installation?

Impact: Pricing: Survey cost vs embedding contingency into unit price | Scope: Schedule sequencing (survey -> kitting -> install) and gating to start

If unanswered (default): Assume limited survey required if data uncertainty exists; propose optional add-alternate

Mitigation guidance: Define survey scope, deliverables, acceptance, and how survey results adjust quantities

### UIR Dependency

#### W.PIT.690 (Score 83, HIGH)

Prompt: How should locations requiring utility action be handled?

Impact: Pricing: UIR delays create idle time, route churn, remobilization | Scope: Utility responsiveness, backlog management

If unanswered (default): Assume UIR occurs; require SLA/response windows or progression protection

Mitigation guidance: Define utility action SLA and contractor right to advance

### Valve Replacement Authorization

#### W.INSIDE.390 (Score 86, HIGH)

Prompt: If an interior shutoff valve is non-functional, is replacement authorized?

Impact: Pricing: No authorization creates abandonments and revisits; yes creates material + labor costs | Scope: Customer coordination, utility dispatch needs

If unanswered (default): Assume not authorized unless defined; include contingency line item if unknown

Mitigation guidance: Define decision tree: replace under allowance vs utility responsibility


---

## Interpretation for Leadership
- Scores are normalized to a 0–100 scale
- Thresholds are governed by **SCORING_CONFIG_v1**
- No enrichment signals or canonical scope questions were modified
- Changes to outcomes require only threshold or weighting adjustments

---

## Action Guidance
- **PROCEED**: Risk profile aligns with historical delivery tolerance  
- **PROCEED WITH CONDITIONS**: Bid contingent on clarifications and pricing protections  
- **NO-BID**: Risk concentration exceeds acceptable exposure without structural changes

---

Generated automatically by Phase 6.
