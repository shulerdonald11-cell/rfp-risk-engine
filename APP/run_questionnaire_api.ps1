$ErrorActionPreference = 'Stop'

$repo = Split-Path -Parent $(Split-Path -Parent $(Resolve-Path $MyInvocation.MyCommand.Path))
Set-Location $repo

if (!(Test-Path ".venv\Scripts\python.exe")) {
  throw "Missing venv. Create it with: python -m venv .venv"
}

.\.venv\Scripts\python.exe -m uvicorn APP.questionnaire_api:app --reload --port 8000
