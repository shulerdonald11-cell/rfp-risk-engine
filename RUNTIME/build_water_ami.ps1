param(
  [string]$RepoRoot = "C:\Users\shule\Documents\Shuler LLC\RFP_RISK_ENGINE",
  [switch]$RebuildBundle = $false,
  [switch]$MakeSampleAnswers = $false
)

$ErrorActionPreference = "Stop"

$BundlePath = Join-Path $RepoRoot "DOMAINS\WATER_AMI\QUESTIONS\runtime_bundle_v1.1.json"
$CorePath   = Join-Path $RepoRoot "DOMAINS\WATER_AMI\QUESTIONS\core.json"
$PitPath    = Join-Path $RepoRoot "DOMAINS\WATER_AMI\QUESTIONS\pit_extensions.json"
$InsidePath = Join-Path $RepoRoot "DOMAINS\WATER_AMI\QUESTIONS\inside_extensions.json"

$AnsPath    = Join-Path $RepoRoot "RUNTIME\answers\sample_answers_v1.json"

$OutDir     = Join-Path $RepoRoot "OUTPUT"
$ScopePath  = Join-Path $OutDir "scope_v0.md"
$GapsPath   = Join-Path $OutDir "gaps_v0.md"
$ValPath    = Join-Path $OutDir "validation_v0.json"

New-Item -ItemType Directory -Force -Path (Join-Path $RepoRoot "RUNTIME\answers") | Out-Null
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

function Load-Json($path) {
  if (!(Test-Path $path)) { throw "Missing: $path" }
  return (Get-Content $path -Raw | ConvertFrom-Json)
}

function Write-Json($obj, $path, $depth=50) {
  $obj | ConvertTo-Json -Depth $depth | Set-Content -Path $path -Encoding UTF8
}

# --- Optional: Rebuild runtime bundle from canonical JSON files
if ($RebuildBundle) {
  $core   = Load-Json $CorePath
  $pit    = Load-Json $PitPath
  $inside = Load-Json $InsidePath

  # Support canonical files that are either arrays or wrapped {questions:[...]}
  function Extract-Questions($x) {
    if ($x -is [System.Array]) { return $x }
    if ($null -ne $x.questions -and ($x.questions -is [System.Array])) { return $x.questions }
    throw "Canonical file format unexpected; expected array or object with .questions[]"
  }

  $bundle = [ordered]@{
    bundleId   = "water_ami_universe_v1.1_locked"
    createdAt  = (Get-Date).ToString("s")
    sources    = @("core.json","pit_extensions.json","inside_extensions.json")
    questions  = @(
      [ordered]@{ domainId="WATER_AMI"; section="CORE";  questions = (Extract-Questions $core) },
      [ordered]@{ domainId="WATER_AMI"; section="PIT";   questions = (Extract-Questions $pit) },
      [ordered]@{ domainId="WATER_AMI"; section="INSIDE";questions = (Extract-Questions $inside) }
    )
  }

  Write-Json $bundle $BundlePath 80
  Write-Host "Rebuilt bundle: $BundlePath"
}

# --- Load runtime bundle
$bundle = Load-Json $BundlePath

# Flatten questions
$all = @()
foreach ($secObj in $bundle.questions) {
  if ($secObj.questions -is [System.Array]) { $all += $secObj.questions }
}

if ($all.Count -eq 0) { throw "Bundle contains no questions to process." }

# --- Optional: Create sample answers from real IDs
if ($MakeSampleAnswers) {
  $pickPerSection = 3
  $targets = @()

  foreach ($sec in @("CORE","PIT","INSIDE")) {
    $secQs = $all | Where-Object { $_.section -eq $sec -and $_.questionId } | Sort-Object order | Select-Object -First $pickPerSection
    $targets += ($secQs | ForEach-Object { $_.questionId })
  }

  $answers = [ordered]@{}
  foreach ($id in $targets) { $answers[$id] = "Unknown" }

  $payload = [ordered]@{
    bundleId = $bundle.bundleId
    projectMeta = [ordered]@{
      client = "Sample Utility"
      projectName = "AMI Deployment Pilot"
      createdAt = (Get-Date).ToString("yyyy-MM-dd")
    }
    answers = $answers
  }

  Write-Json $payload $AnsPath 20
  Write-Host "Wrote sample answers: $AnsPath"
}

# --- Load answers
$ans = Load-Json $AnsPath

# Index questions by ID
$qById = @{}
foreach ($q in $all) { if ($q.questionId) { $qById[$q.questionId] = $q } }

# Validate answer keys exist in universe + basic structure
$validation = [ordered]@{
  bundleId = $bundle.bundleId
  answersFile = $AnsPath
  missingInUniverse = @()
  providedCount = 0
  unknownCount = 0
  sections = [ordered]@{ CORE=0; PIT=0; INSIDE=0 }
}

foreach ($k in $ans.answers.PSObject.Properties.Name) {
  $validation.providedCount++
  $v = $ans.answers.$k
  if ($v -eq "Unknown" -or [string]::IsNullOrWhiteSpace([string]$v)) { $validation.unknownCount++ }

  if (-not $qById.ContainsKey($k)) {
    $validation.missingInUniverse += $k
  } else {
    $sec = $qById[$k].section
    if ($validation.sections.Contains($sec)) { $validation.sections[$sec]++ }
  }
}

Write-Json $validation $ValPath 20
Write-Host "Wrote validation: $ValPath"

# --- Generate Scope Markdown (only for provided answers)
$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# Water AMI Scope Summary (DRAFT)")
$lines.Add("")
$lines.Add("Bundle: $($ans.bundleId)")
$lines.Add("Client: $($ans.projectMeta.client)")
$lines.Add("Project: $($ans.projectMeta.projectName)")
$lines.Add("Created: $($ans.projectMeta.createdAt)")
$lines.Add("")

foreach ($sec in @("CORE","PIT","INSIDE")) {
  $lines.Add("## $sec")
  $secQs = $all | Where-Object { $_.section -eq $sec } | Sort-Object order
  $any = $false

  foreach ($q in $secQs) {
    $qid = $q.questionId
    if ($null -ne $qid -and $ans.answers.PSObject.Properties.Name -contains $qid) {
      $any = $true
      $val = $ans.answers.$qid
      $prompt = $q.prompt
      if ([string]::IsNullOrWhiteSpace($prompt)) { $prompt = "(no prompt found)" }
      $lines.Add("- **$qid**: $val  | $prompt")
    }
  }

  if (-not $any) { $lines.Add("- (no answers provided in this section)") }
  $lines.Add("")
}

$lines | Set-Content -Path $ScopePath -Encoding UTF8
Write-Host "Generated scope: $ScopePath"

# --- Generate Gaps report: unanswered questions in the universe
$gapLines = New-Object System.Collections.Generic.List[string]
$gapLines.Add("# Water AMI Gaps Report (DRAFT)")
$gapLines.Add("")
$gapLines.Add("Bundle: $($bundle.bundleId)")
$gapLines.Add("Answers file: $AnsPath")
$gapLines.Add("Generated: $(Get-Date -Format 'yyyy-MM-dd')")
$gapLines.Add("")

foreach ($sec in @("CORE","PIT","INSIDE")) {
  $gapLines.Add("## $sec")
  $secQs = $all | Where-Object { $_.section -eq $sec } | Sort-Object order
  $unanswered = 0

  foreach ($q in $secQs) {
    $qid = $q.questionId
    if ($null -eq $qid) { continue }
    if (-not ($ans.answers.PSObject.Properties.Name -contains $qid)) {
      $unanswered++
      $gapLines.Add("- **$qid** (unanswered) | $($q.prompt)")
    }
  }

  $gapLines.Add("")
  $gapLines.Add("Unanswered in ${sec}: $unanswered")
  $gapLines.Add("")
}

$gapLines | Set-Content -Path $GapsPath -Encoding UTF8
Write-Host "Generated gaps: $GapsPath"

Write-Host "BUILD COMPLETE"
