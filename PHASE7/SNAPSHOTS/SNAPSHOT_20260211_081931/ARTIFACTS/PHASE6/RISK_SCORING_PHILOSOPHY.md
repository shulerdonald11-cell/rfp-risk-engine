# Risk Scoring Philosophy (Optional)

## Goals
- Keep scoring explainable and stable across projects
- Separate **pricing risk** from **execution risk**
- Provide a clear basis for bid qualifiers, contingency, or no-bid

## Suggested Scoring Model (initial)
- Each risk entry has:
  - severity (impact magnitude)
  - likelihood (probability of occurring)
  - controllability (contractor ability to mitigate)
  - detectability (can we find it early)
- Roll-up scores:
  - pricing_risk_score (0-100)
  - execution_risk_score (0-100)
  - overall_risk_score (0-100) with weighted model

## Decision Guidance (initial)
- 0-39: Proceed
- 40-69: Proceed with conditions/contingency
- 70-100: No-bid unless risk is contractually removed or margin absorbs it

## Principles
- If the utility owns the uncertainty and won’t define it, price goes up or the bid dies.
- Unlimited liability equals unlimited pricing.
- Route governance and UIR/RTU rules determine whether production is real or fantasy.