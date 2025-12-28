param(
    [string]$RepoRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"

# ---- Paths ----
$scorecardPath = Join-Path $RepoRoot "OUTPUT\risk_scorecard_v1.json"
$decisionPath  = Join-Path $RepoRoot "OUTPUT\bid_decision_v1.md"
$riskSummaryPath = Join-Path $RepoRoot "OUTPUT\risk_summary_v1.md"
$configPath    = Join-Path $RepoRoot "PHASE6\SCORING_CONFIG_v1.json"
$outputPath    = Join-Path $RepoRoot "OUTPUT\executive_risk_summary_v1.md"

# ---- Load inputs ----
$scorecard   = Get-Content $scorecardPath -Raw | ConvertFrom-Json
$decisionMd  = Get-Content $decisionPath -Raw
$riskSummary = Get-Content $riskSummaryPath -Raw
$config      = Get-Content $configPath -Raw | ConvertFrom-Json

# ---- Extract decision line ----
$decisionLine = ($decisionMd -split "`n" | Where-Object { $_ -match "\*\*Decision:\*\*" })[0]

# ---- Markdown output ----
$md = @"
# Executive Risk Summary

## Snapshot
$decisionLine  
**Pricing Risk Score:** $($scorecard.scores.pricing)  
**Execution Risk Score:** $($scorecard.scores.execution)  
**Overall Risk Score:** $($scorecard.scores.overall)

---

## What Is Driving Risk
The following summary reflects aggregated Phase 5 enrichment signals and deterministic Phase 6 scoring logic.

$riskSummary

---

## Interpretation for Leadership
- Scores are normalized to a 0–100 scale
- Thresholds are governed by **$($config.version)**
- No enrichment signals or canonical scope questions were modified
- Changes to outcomes require only threshold or weighting adjustments

---

## Action Guidance
- **PROCEED**: Risk profile aligns with historical delivery tolerance  
- **PROCEED WITH CONDITIONS**: Bid contingent on clarifications and pricing protections  
- **NO-BID**: Risk concentration exceeds acceptable exposure without structural changes

---

Generated automatically by Phase 6.
"@

$md | Out-File $outputPath -Encoding utf8 -Force

Write-Host "Executive risk summary written to OUTPUT\executive_risk_summary_v1.md"
