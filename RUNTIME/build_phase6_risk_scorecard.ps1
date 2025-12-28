param(
    [string]$RepoRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"

# ---- Paths ----
$scoringConfigPath = Join-Path $RepoRoot "PHASE6\SCORING_CONFIG_v1.json"
$enrichmentPath    = Join-Path $RepoRoot "ENRICHMENT\enrichment_map_v1.1.json"
$gapsPath          = Join-Path $RepoRoot "OUTPUT\gaps_v0.md"
$outputPath        = Join-Path $RepoRoot "OUTPUT\risk_scorecard_v1.json"

# ---- Load inputs ----
$scoringConfig = Get-Content $scoringConfigPath -Raw | ConvertFrom-Json
$enrichment    = Get-Content $enrichmentPath -Raw | ConvertFrom-Json

# ---- Flatten enrichment entries ----
$entries = $enrichment.entries

if (-not $entries) {
    throw "No enrichment entries found."
}

# ---- Classify pricing vs execution ----
$classified = foreach ($e in $entries) {
    $pricing   = ($e.signals.pricingDrivers.Count -gt 0)
    $execution = ($e.signals.scopeImpacts.Count -gt 0)

    [PSCustomObject]@{
        questionId = $e.questionId
        category   = $e.risk.category
        score      = $e.risk.score
        pricing    = $pricing
        execution  = $execution
    }
}

# ---- Aggregate ----
$pricingScores   = @()
$executionScores = @()

foreach ($c in $classified) {
    if ($c.pricing -and $c.execution) {
        $pricingScores   += ($c.score * $scoringConfig.mixed_risk_split)
        $executionScores += ($c.score * $scoringConfig.mixed_risk_split)
    } elseif ($c.pricing) {
        $pricingScores += $c.score
    } elseif ($c.execution) {
        $executionScores += $c.score
    }
}

$pricingRisk   = if ($pricingScores.Count)   { [math]::Round(($pricingScores | Measure-Object -Average).Average) } else { 0 }
$executionRisk = if ($executionScores.Count) { [math]::Round(($executionScores | Measure-Object -Average).Average) } else { 0 }

$overallRisk = [math]::Round(
    ($pricingRisk * $scoringConfig.weights.pricing) +
    ($executionRisk * $scoringConfig.weights.execution)
)

# ---- Output ----
$result = @{
    version = "risk_scorecard_v1"
    generatedUtc = (Get-Date).ToUniversalTime().ToString("o")
    scores = @{
        pricing   = $pricingRisk
        execution = $executionRisk
        overall   = $overallRisk
    }
    configVersion = $scoringConfig.version
}

$result | ConvertTo-Json -Depth 5 | Out-File $outputPath -Encoding utf8 -Force

Write-Host "Phase 6 risk scorecard written to OUTPUT\risk_scorecard_v1.json"
