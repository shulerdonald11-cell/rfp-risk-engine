param(
    [string]$RepoRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"

# ---- Paths ----
$enrichmentPath = Join-Path $RepoRoot "ENRICHMENT\enrichment_map_v1.1.json"
$scorecardPath  = Join-Path $RepoRoot "OUTPUT\risk_scorecard_v1.json"
$configPath     = Join-Path $RepoRoot "PHASE6\SCORING_CONFIG_v1.json"
$outputPath     = Join-Path $RepoRoot "OUTPUT\pricing_risk_v1.json"

# ---- Load inputs ----
$enrichment = Get-Content $enrichmentPath -Raw | ConvertFrom-Json
$scorecard  = Get-Content $scorecardPath -Raw | ConvertFrom-Json
$config     = Get-Content $configPath -Raw | ConvertFrom-Json

# ---- Filter pricing-relevant entries ----
$pricingEntries = foreach ($e in $enrichment.entries) {
    if ($e.signals.pricingDrivers.Count -gt 0) {
        [PSCustomObject]@{
            questionId = $e.questionId
            category   = $e.risk.category
            score      = $e.risk.score
            drivers    = $e.signals.pricingDrivers
            defaults   = $e.defaults
            clarifications = $e.clarifications
        }
    }
}

# ---- Aggregate by category ----
$byCategory = $pricingEntries |
    Group-Object category |
    ForEach-Object {
        [PSCustomObject]@{
            category = $_.Name
            count_entries = $_.Count
            max_score = ($_.Group.score | Measure-Object -Maximum).Maximum
            avg_score = [math]::Round(($_.Group.score | Measure-Object -Average).Average, 1)
            question_ids = ($_.Group.questionId | Sort-Object)
            pricingDrivers = ($_.Group.drivers | Select-Object -Unique)
            defaultsIfUnanswered = ($_.Group.defaults | Select-Object -Unique)
            recommendedQualifiers = ($_.Group.clarifications | Select-Object -Unique)
        }
    } |
    Sort-Object max_score -Descending

# ---- Output ----
$result = @{
    version = "pricing_risk_v1"
    generatedUtc = (Get-Date).ToUniversalTime().ToString("o")
    pricing_risk_score = $scorecard.scores.pricing
    configVersion = $config.version
    pricingRiskByCategory = $byCategory
}

$result | ConvertTo-Json -Depth 6 | Out-File $outputPath -Encoding utf8 -Force

Write-Host "Pricing risk breakdown written to OUTPUT\pricing_risk_v1.json"
