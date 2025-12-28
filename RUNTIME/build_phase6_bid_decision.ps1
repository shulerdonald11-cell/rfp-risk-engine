param(
    [string]$RepoRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"

# ---- Paths ----
$scorecardPath   = Join-Path $RepoRoot "OUTPUT\risk_scorecard_v1.json"
$configPath      = Join-Path $RepoRoot "PHASE6\SCORING_CONFIG_v1.json"
$gapsPath        = Join-Path $RepoRoot "OUTPUT\gaps_v0.md"
$outputPath      = Join-Path $RepoRoot "OUTPUT\bid_decision_v1.md"

# ---- Load inputs ----
$scorecard = Get-Content $scorecardPath -Raw | ConvertFrom-Json
$config    = Get-Content $configPath -Raw | ConvertFrom-Json
$gapsText  = Get-Content $gapsPath -Raw

$overall = $scorecard.scores.overall

# ---- Decision band ----
if ($overall -le $config.decision_thresholds.proceed_max) {
    $decision = "PROCEED"
} elseif ($overall -le $config.decision_thresholds.proceed_with_conditions_max) {
    $decision = "PROCEED WITH CONDITIONS"
} else {
    $decision = "NO-BID"
}

# ---- Confidence calculation (simple + deterministic) ----
$edgeDist = [math]::Min(
    [math]::Abs($overall - $config.decision_thresholds.proceed_max),
    [math]::Abs($overall - $config.decision_thresholds.proceed_with_conditions_max)
)

$confidence = [math]::Min(100, 50 + $edgeDist)

# ---- Markdown output ----
$md = @"
# Phase 6 Bid Decision

**Decision:** $decision  
**Confidence:** $confidence%

---

## Risk Scores
- Pricing Risk: $($scorecard.scores.pricing)
- Execution Risk: $($scorecard.scores.execution)
- Overall Risk: $overall

---

## Basis
Decision derived deterministically from Phase 6 scoring configuration **$($config.version)**  
and Phase 5 enrichment intelligence.

No enrichment signals were modified.

---

## Known Gaps
The following unanswered or partially defined areas may materially affect execution or pricing:


---

## Notes
- Adjust decision thresholds via `PHASE6/SCORING_CONFIG_*.json`
- Re-run Phase 6 scripts to regenerate outputs
"@

$md | Out-File $outputPath -Encoding utf8 -Force

Write-Host "Bid decision written to OUTPUT\bid_decision_v1.md"
