param(
    [string]$RepoRoot = (Get-Location).Path
)

$ErrorActionPreference = "Stop"

Write-Host "=== Phase 6 Full Run Start ==="

$steps = @(
    "RUNTIME\build_phase6_risk_scorecard.ps1",
    "RUNTIME\build_phase6_bid_decision.ps1",
    "RUNTIME\build_phase6_executive_summary.ps1",
    "RUNTIME\build_phase6_pricing_risk.ps1",
    "RUNTIME\build_phase6_execution_risk.ps1",
    "RUNTIME\build_phase6_manifest.ps1"
)

foreach ($s in $steps) {
    $full = Join-Path $RepoRoot $s
    if (-not (Test-Path $full)) { throw "Missing script: $s" }

    Write-Host "Running: $s"
    & $full -RepoRoot $RepoRoot
}

Write-Host "=== Phase 6 Full Run Complete ==="
Write-Host "Outputs are in: OUTPUT\"
