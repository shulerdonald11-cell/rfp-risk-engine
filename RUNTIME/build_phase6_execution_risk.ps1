param(
    [string]$RepoRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"

# ---- Paths ----
$enrichmentPath = Join-Path $RepoRoot "ENRICHMENT\enrichment_map_v1.1.json"
$scorecardPath  = Join-Path $RepoRoot "OUTPUT\risk_scorecard_v1.json"
$configPath     = Join-Path $RepoRoot "PHASE6\SCORING_CONFIG_v1.json"
$outputPath     = Join-Path $RepoRoot "OUTPUT\execution_risk_v1.json"

# ---- Load inputs ----
$enrichment = Get-Content $enrichmentPath -Raw | ConvertFrom-Json
$scorecard  = Get-Content $scorecardPath -Raw | ConvertFrom-Json
$config     = Get-Content $configPath -Raw | ConvertFrom-Json

# ---- Normalize execution-relevant entries ----
$executionEntries = @()

foreach ($e in $enrichment.entries) {

    if ($e.signals.scopeImpacts.Count -gt 0) {

        $defaults = @()
        if ($e.PSObject.Properties.Name -contains "defaults") {
            $defaults = $e.defaults
        }

        $clarifications = @()
        if ($e.PSObject.Properties.Name -contains "clarifications") {
            $clarifications = $e.clarifications
        }

        $dependencies = @()
        if ($e.PSObject.Properties.Name -contains "dependencies") {
            $dependencies = $e.dependencies
        }

        $executionEntries += [PSCustomObject]@{
            questionId = $e.questionId
            category   = $e.risk.category
            score      = $e.risk.score
            impacts    = $e.signals.scopeImpacts
            defaults   = $defaults
            clarifications = $clarifications
            dependencies   = $dependencies
        }
    }
}

# ---- Aggregate by category ----
$byCategory = @()

$groups = $executionEntries | Group-Object category

foreach ($g in $groups) {

    $group = $g.Group

    $byCategory += [PSCustomObject]@{
        category = $g.Name
        count_entries = $group.Count
        max_score = ($group.score | Measure-Object -Maximum).Maximum
        avg_score = [math]::Round(($group.score | Measure-Object -Average).Average, 1)
        question_ids = ($group.questionId | Sort-Object)
        scopeImpacts = ($group | ForEach-Object { $_.impacts } | Select-Object -Unique)
        defaultsIfUnanswered = ($group | ForEach-Object { $_.defaults } | Select-Object -Unique)
        requiredClarifications = ($group | ForEach-Object { $_.clarifications } | Select-Object -Unique)
        dependencies = ($group | ForEach-Object { $_.dependencies } | Select-Object -Unique)
    }
}

$byCategory = $byCategory | Sort-Object max_score -Descending

# ---- Output ----
$result = @{
    version = "execution_risk_v1"
    generatedUtc = (Get-Date).ToUniversalTime().ToString("o")
    execution_risk_score = $scorecard.scores.execution
    configVersion = $config.version
    executionRiskByCategory = $byCategory
}

$result | ConvertTo-Json -Depth 6 | Out-File $outputPath -Encoding utf8 -Force

Write-Host "Execution risk breakdown written to OUTPUT\execution_risk_v1.json"
