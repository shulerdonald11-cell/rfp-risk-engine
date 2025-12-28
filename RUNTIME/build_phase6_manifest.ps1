param(
    [string]$RepoRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"

# ---- Paths ----
$configPath = Join-Path $RepoRoot "PHASE6\SCORING_CONFIG_v1.json"
$manifestPath = Join-Path $RepoRoot "OUTPUT\phase6_build_manifest_v1.json"

$outputFiles = @(
    "OUTPUT\risk_scorecard_v1.json",
    "OUTPUT\bid_decision_v1.md",
    "OUTPUT\executive_risk_summary_v1.md",
    "OUTPUT\pricing_risk_v1.json",
    "OUTPUT\execution_risk_v1.json"
)

# ---- Load config ----
$config = Get-Content $configPath -Raw | ConvertFrom-Json

# ---- Check outputs ----
$missing = @()
foreach ($file in $outputFiles) {
    if (-not (Test-Path (Join-Path $RepoRoot $file))) {
        $missing += $file
    }
}

$status = if ($missing.Count -eq 0) { "SUCCESS" } else { "INCOMPLETE" }

# ---- Build manifest ----
$manifest = @{
    version = "phase6_build_manifest_v1"
    generatedUtc = (Get-Date).ToUniversalTime().ToString("o")
    status = $status
    scoringConfigVersion = $config.version
    inputs = @{
        enrichment = "ENRICHMENT/enrichment_map_v1.1.json"
        phase5Summary = "OUTPUT/risk_summary_v1.md"
        gaps = "OUTPUT/gaps_v0.md"
    }
    outputs = $outputFiles
    missingOutputs = $missing
}

$manifest | ConvertTo-Json -Depth 5 | Out-File $manifestPath -Encoding utf8 -Force

Write-Host "Phase 6 build manifest written to OUTPUT\phase6_build_manifest_v1.json"
