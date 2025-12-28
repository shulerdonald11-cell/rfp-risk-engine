# SMUS AMI Scope Methodology — Core (B1–B9) v1.0
Status: LOCKED (Verbatim)
Purpose: Preserve Don Shuler IP / reasoning behind scope questions for reuse in GPT tools, consulting, and training.

## B1 — Existing meters & read system
Intent: We need to know what they know and what they have. This is the existing type of system: direct read, AMR, AMI, and what brand (EPLERA, ITRON, Badger FixBase, Sensus FixBase, Badger Cellular, etc.). Also provide details related to the existing meter types (mechanical vs existing solid state) and we are really only talking about the ones that are going to be removed.

## B2 — Meter material / construction (recycling value)
Intent: We want to know the meter body material (brass, plastic, mixed). This is mostly for recycling ability and recycling value. Understanding brand meters helps the contractor know potential recycling value. This matters depending on whether the utility recycles themselves or the contractor manages it.

## B2a — Battery disposal
Intent: If there’s an existing AMI system in place, there are likely lithium batteries being removed. There is typically a disposal cost associated with battery recycling. This should be explicitly surfaced.

## B3 — Asset/service-level data for planning (materials + efficiency + survey trigger)
Intent: Contractor needs to plan and load trucks based on what they believe is out there. This includes lids and can also apply to yoke setters and expansion wheels, additional plumbing conditions, bushing adapters, spool pieces, lay lengths, and other materials. This dictates whether a survey is required. Location and asset-level information is critical.

Terminology precision: Yoke setters use expansion wheels (a pertinence that goes onto the meter so it can fit properly within the yoke setter).

## B3a — What data elements are included
Intent: Split question to avoid over-reliance on notes alone while still allowing notes to capture nuance. The AI layer should be able to decipher notes for what goes into the RFP vs what they don’t know and where survey services are justified. Survey can be full or targeted (e.g., lids-only) depending on what they know.

## B4 — How data should be relied upon (risk allocation / change orders / contingency)
Key reality: Contractors price based on efficiency. Planning dictates efficiency. If planning is wrong, efficiency is wrong and the contractor’s price is wrong.

Risk allocation: If utility wants to shift revisit risk to the contractor, contractor will include contingency which affects pricing. If utility retains risk, change orders are likely when data is inaccurate and causes revisits / rework. If they don’t know answers, that’s fine, but they must understand cost implications.

## B5 — Data refresh cadence
Reality: Small/short-burn projects (e.g., ~3 months / <2,000 meters) can often work with a one-time file and minor manual changes. Longer projects have churn: move-in/move-out, maintenance changes, ongoing reads, and normal operations that change the database.

Best practice is conditional: Daily updates are helpful for larger projects but increase integration cost and complexity. Some utilities prefer flat file Excel and manual updates daily/weekly/monthly depending on burn and sophistication. Contractor tier and WOMS maturity matter.

## B6 — Data exchange method
Why it matters: Integration cost and effort on both sides.

- API integration is sophisticated, highest complexity and cost.
- SFTP is preferred: contractor can drop files automatically; utility can grab manually or script import to billing.
- Portal-based exchange is useful for less sophisticated utilities that can’t set up or manage SFTP access.
- Spreadsheet/manual exchange is common for smaller, less sophisticated utilities and contractors.

Notes should capture what they are comfortable with so scope language reflects reality.

## B6a — Utility-defined work types in the data stream
Pattern: Utility sends data via SFTP (or sometimes API) that includes work type codes per location (meter+endpoint, endpoint-only, register-only, etc.), typically on larger programs (>10k meters) and multi-year projects.

Tradeoff: This can reduce survey needs if accurate, but increases complexity and can create contractor inefficiency if work types change daily over time. More complexity = more cost.

## B7 — Exceptions, bounced files, reconciliation workflows
Reality: Data mismatches generate system exceptions on the utility side. Some exceptions are field errors; some require utility reconciliation. Mature WOMS environments handle this via exception reports bounced back and forth, tracked actions, correction cycles, and re-submitted files.

This question sets expectations: who reconciles, how, and with what workflow maturity.

## B8 — Survey authorization & scope — lids are the dominant pit risk
Key risk driver: Lids. If the AMI system requires lid drilling, lid cutting, or lid swapping across varied sizes, that is the biggest risk for planning.

Certain AMI systems have requirements related to pit/vault/lid conditions. This must be considered in choosing full vs limited survey scope.

## B9 — Survey responsibility/funding/accountability + pay item reality
Accountability: If utility performs survey, utility is responsible for data accuracy; inaccuracies drive inefficiency and change orders. Best practice is contractor performs survey and utility pays for it, especially when contractor is responsible for procuring materials.

Field reality story: If unqualified personnel collect bad data, materials get ordered wrong, deployment suffers, and contractor gets blamed while scrambling to keep crews productive.

Commercial best practice: Survey should be a pay item when possible. Pay per unit (small/intermediate/large categories), pricing depends on data collected and scope complexity:
- lids only
- lifting lids to inspect meters
- dirt levels
- bushings/adapters
- other field conditions
