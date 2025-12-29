# Phase 6 Output Targets

Phase 6 will generate **derived artifacts only** (no mutation of canonical inputs).

## Candidate Outputs (to be finalized)
- OUTPUT/risk_scorecard_v1.json  
  Purpose: Machine-readable consolidated risk signal per category + roll-up score

- OUTPUT/pricing_risk_v1.json  
  Purpose: Pricing-specific risk drivers, contingency guidance, qualifiers

- OUTPUT/execution_risk_v1.json  
  Purpose: Execution-specific risks (access, throughput, dependencies, claims)

- OUTPUT/bid_decision_v1.md  
  Purpose: Clear Bid / No-Bid / Bid-With-Conditions narrative

- OUTPUT/executive_risk_summary_v1.md  
  Purpose: Executive-facing summary with top drivers, mitigations, assumptions

## Output Rules
- Outputs must cite their source inputs (file paths + generation timestamp)
- Outputs must be deterministic from inputs