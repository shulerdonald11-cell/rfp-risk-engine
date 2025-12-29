# PHASE 6 — SYSTEM SNAPSHOT (RFP Risk & Scope Engine)

## 1. Snapshot Metadata
- Date (Local): 2025-12-29 09:43 America/Chicago
- Phase Status:
  - Phase 4: Runtime Readiness — LOCKED
  - Phase 5: Enrichment & Risk Intelligence — LOCKED
  - Phase 6: Risk Scoring, Decisioning, Narratives — LOCKED
- Git Tag: phase6-locked-20251228
- Repo Root: RFP_RISK_ENGINE

Purpose:
Preserve a complete system state so development can resume without loss of architectural intent.

---

## 2. What This System Is (Plain English)
The RFP Risk Engine is a **bi-directional scope intelligence system** for Water AMI projects.

It supports:
1) **Forward Mode** — generating scope and RFP language from structured scope answers  
2) **Reverse Mode** — analyzing existing RFPs and addendums to quantify risk and identify gaps

Both modes use the same canonical question universe, enrichment logic, and scoring philosophy.

---

## 3. Canonical Truth (What Is Immutable)
The following are **read-only and locked**:

- MASTER_SPEC/CURRENT/MASTER_UNIVERSE_SPEC_v1.1.md
- Canonical Water AMI question universe (DOMAINS/WATER_AMI/questions/*.json)
- Question IDs and wording
- ENRICHMENT/enrichment_map_v1.1.json
- Phase 6 control docs and config under PHASE6/

No phase may modify these artifacts without a versioned unlock and explicit lock documentation.

---

## 4. Dual-Mode Operation Model

### Mode A — Forward (Scope → RFP)
**Purpose**
Assist owners / consultants in building complete, defensible RFP scopes.

**Mechanics**
- Canonical questions are answered directly (human) or assisted by AI in the future.
- Enrichment fires during scope formation.
- Risk signals surface before bid stage decisions.

**Outputs**
- Scope narratives suitable for procurement language
- Explicit assumptions and clarifications
- Early risk indicators to pressure-test scope completeness

---

### Mode B — Reverse (RFP → Risk)
**Purpose**
Analyze third-party RFPs and addendums to quantify bid risk and detect gaps.

**Mechanics**
- Ingest unstructured documents (future ingestion layer/UI).
- Map RFP language against canonical questions.
- Identify missing answers, ambiguity, contradictions, and risk triggers.
- Score deterministically using Phase 6 config and Phase 5 enrichment outputs.

**Outputs**
- Risk scorecard
- Pricing vs execution risk split
- Bid / no-bid confidence indicator
- Executive narrative summaries
- Gap list aligned to canonical questions

---

## 5. Phase 6 Outputs (Current State)
Phase 6 produces deterministic artifacts in OUTPUT/:

- OUTPUT/risk_scorecard_v1.json
- OUTPUT/pricing_risk_v1.json
- OUTPUT/execution_risk_v1.json
- OUTPUT/bid_decision_v1.md
- OUTPUT/executive_risk_summary_v1.md
- OUTPUT/phase6_build_manifest_v1.json

These outputs are reproducible from locked inputs and Phase 6 control docs.

---

## 6. Runtime & Environments

### Local Development
- Windows + PowerShell available for legacy orchestration and builder scripts
- Python virtualenv (.venv)
- FastAPI app under APP/ exposes HTTP endpoints
- Deterministic execution via Python runner (preferred) and/or PowerShell scripts

### Containerized Runtime
- Docker Desktop + Linux container
- FastAPI exposed on port 8000
- Python runner executes Phase 6 without Windows PowerShell dependency
- Outputs match local run artifacts

Cloud deployment is not assumed yet.

---

## 7. What Is Explicitly Out of Scope (As of This Snapshot)
- Modifying canonical questions or IDs
- Using external data sources to fill gaps
- Guesswork / “industry typical” assumptions outside control docs
- Auto-pricing or cost estimation (risk only)
- White-label UI implementation (planned future work)

---

## 8. Planned Extensions (Acknowledged, Not Implemented)

### 8.1 Question Helper Context Layer (Non-mutating)
Goal: provide additional context *about* canonical questions without changing them.
- Why the question exists (rationale)
- Helper text / definitions
- Examples / edge cases
- Implementation notes for AI-assisted guidance

Recommended future location:
- QUESTION_INTELLIGENCE/ (new folder)
  - helpers.json
  - rationale.md
  - examples.md

### 8.2 Reverse-Mode Ingestion (Upload RFP + Addendums)
Goal: upload and parse RFP documents, align to canonical questions, then score.
- Document upload endpoint/UI
- Extraction pipeline → canonical mapping
- Gap / ambiguity reporting
- Risk scoring using locked Phase 6 logic

### 8.3 White-Label / Multi-Tenant Support
Goal: tenant isolation + per-tenant configuration (branding, thresholds within allowed bounds).

### 8.4 Historical Back-Testing
Goal: replay historical bids and compare outcomes vs scores.
- Establish acceptance criteria and calibration process
- Adjust thresholds via config (not code) with version control

---

## 9. Guardrails Going Forward
- Canonical universe remains immutable
- Enhancements layer around questions, not into them
- All scoring remains explainable and deterministic
- Config changes (thresholds/weights) must be versioned and documented
- New phases must add explicit lock documentation similar to PHASE6/PHASE6_LOCK.md

---

## 10. Resume Instructions (For Next Session)
1) Load this snapshot and Phase 6 lock docs.
2) Treat Phase 6 as locked (no redesign).
3) Choose the next track explicitly:
   - Track A: Helper Context Layer
   - Track B: Reverse-Mode Ingestion
   - Track C: Production deployment (smartmeterus.com)
4) Execute in small steps with repo artifacts, minimal freehand edits.


---

## 11. Repository Layout (Authoritative as of 2025-12-29)

The following reflects the on-disk structure of the RFP Risk Engine repository at the time this snapshot was taken.

\\\
Folder PATH listing for volume Windows
Volume serial number is 7851-A8BC
C:.
|   .dockerignore
|   .gitignore
|   build_water_ami_phase5.ps1
|   Dockerfile
|   phase5_source.ps1.txt
|   repo_structure_check.txt
|   _patch_phase5.ps1
|   _write_phase5.ps1
|   
+---.venv
|   |   .gitignore
|   |   pyvenv.cfg
|   |   
|   +---Include
|   +---Lib
|   |   \---site-packages
|   |       |   typing_extensions.py
|   |       |   
|   |       +---annotated_types
|   |       |   |   py.typed
|   |       |   |   test_cases.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           test_cases.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---annotated_types-0.7.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---anyio
|   |       |   |   from_thread.py
|   |       |   |   functools.py
|   |       |   |   lowlevel.py
|   |       |   |   py.typed
|   |       |   |   pytest_plugin.py
|   |       |   |   to_interpreter.py
|   |       |   |   to_process.py
|   |       |   |   to_thread.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---abc
|   |       |   |   |   _eventloop.py
|   |       |   |   |   _resources.py
|   |       |   |   |   _sockets.py
|   |       |   |   |   _streams.py
|   |       |   |   |   _subprocesses.py
|   |       |   |   |   _tasks.py
|   |       |   |   |   _testing.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _eventloop.cpython-314.pyc
|   |       |   |           _resources.cpython-314.pyc
|   |       |   |           _sockets.cpython-314.pyc
|   |       |   |           _streams.cpython-314.pyc
|   |       |   |           _subprocesses.cpython-314.pyc
|   |       |   |           _tasks.cpython-314.pyc
|   |       |   |           _testing.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---streams
|   |       |   |   |   buffered.py
|   |       |   |   |   file.py
|   |       |   |   |   memory.py
|   |       |   |   |   stapled.py
|   |       |   |   |   text.py
|   |       |   |   |   tls.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           buffered.cpython-314.pyc
|   |       |   |           file.cpython-314.pyc
|   |       |   |           memory.cpython-314.pyc
|   |       |   |           stapled.cpython-314.pyc
|   |       |   |           text.cpython-314.pyc
|   |       |   |           tls.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---_backends
|   |       |   |   |   _asyncio.py
|   |       |   |   |   _trio.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _asyncio.cpython-314.pyc
|   |       |   |           _trio.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---_core
|   |       |   |   |   _asyncio_selector_thread.py
|   |       |   |   |   _contextmanagers.py
|   |       |   |   |   _eventloop.py
|   |       |   |   |   _exceptions.py
|   |       |   |   |   _fileio.py
|   |       |   |   |   _resources.py
|   |       |   |   |   _signals.py
|   |       |   |   |   _sockets.py
|   |       |   |   |   _streams.py
|   |       |   |   |   _subprocesses.py
|   |       |   |   |   _synchronization.py
|   |       |   |   |   _tasks.py
|   |       |   |   |   _tempfile.py
|   |       |   |   |   _testing.py
|   |       |   |   |   _typedattr.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _asyncio_selector_thread.cpython-314.pyc
|   |       |   |           _contextmanagers.cpython-314.pyc
|   |       |   |           _eventloop.cpython-314.pyc
|   |       |   |           _exceptions.cpython-314.pyc
|   |       |   |           _fileio.cpython-314.pyc
|   |       |   |           _resources.cpython-314.pyc
|   |       |   |           _signals.cpython-314.pyc
|   |       |   |           _sockets.cpython-314.pyc
|   |       |   |           _streams.cpython-314.pyc
|   |       |   |           _subprocesses.cpython-314.pyc
|   |       |   |           _synchronization.cpython-314.pyc
|   |       |   |           _tasks.cpython-314.pyc
|   |       |   |           _tempfile.cpython-314.pyc
|   |       |   |           _testing.cpython-314.pyc
|   |       |   |           _typedattr.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           from_thread.cpython-314.pyc
|   |       |           functools.cpython-314.pyc
|   |       |           lowlevel.cpython-314.pyc
|   |       |           pytest_plugin.cpython-314.pyc
|   |       |           to_interpreter.cpython-314.pyc
|   |       |           to_process.cpython-314.pyc
|   |       |           to_thread.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---anyio-4.12.0.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---click
|   |       |   |   core.py
|   |       |   |   decorators.py
|   |       |   |   exceptions.py
|   |       |   |   formatting.py
|   |       |   |   globals.py
|   |       |   |   parser.py
|   |       |   |   py.typed
|   |       |   |   shell_completion.py
|   |       |   |   termui.py
|   |       |   |   testing.py
|   |       |   |   types.py
|   |       |   |   utils.py
|   |       |   |   _compat.py
|   |       |   |   _termui_impl.py
|   |       |   |   _textwrap.py
|   |       |   |   _utils.py
|   |       |   |   _winconsole.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           core.cpython-314.pyc
|   |       |           decorators.cpython-314.pyc
|   |       |           exceptions.cpython-314.pyc
|   |       |           formatting.cpython-314.pyc
|   |       |           globals.cpython-314.pyc
|   |       |           parser.cpython-314.pyc
|   |       |           shell_completion.cpython-314.pyc
|   |       |           termui.cpython-314.pyc
|   |       |           testing.cpython-314.pyc
|   |       |           types.cpython-314.pyc
|   |       |           utils.cpython-314.pyc
|   |       |           _compat.cpython-314.pyc
|   |       |           _termui_impl.cpython-314.pyc
|   |       |           _textwrap.cpython-314.pyc
|   |       |           _utils.cpython-314.pyc
|   |       |           _winconsole.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---click-8.3.1.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.txt
|   |       |           
|   |       +---colorama
|   |       |   |   ansi.py
|   |       |   |   ansitowin32.py
|   |       |   |   initialise.py
|   |       |   |   win32.py
|   |       |   |   winterm.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---tests
|   |       |   |   |   ansitowin32_test.py
|   |       |   |   |   ansi_test.py
|   |       |   |   |   initialise_test.py
|   |       |   |   |   isatty_test.py
|   |       |   |   |   utils.py
|   |       |   |   |   winterm_test.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           ansitowin32_test.cpython-314.pyc
|   |       |   |           ansi_test.cpython-314.pyc
|   |       |   |           initialise_test.cpython-314.pyc
|   |       |   |           isatty_test.cpython-314.pyc
|   |       |   |           utils.cpython-314.pyc
|   |       |   |           winterm_test.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           ansi.cpython-314.pyc
|   |       |           ansitowin32.cpython-314.pyc
|   |       |           initialise.cpython-314.pyc
|   |       |           win32.cpython-314.pyc
|   |       |           winterm.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---colorama-0.4.6.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.txt
|   |       |           
|   |       +---fastapi
|   |       |   |   applications.py
|   |       |   |   background.py
|   |       |   |   cli.py
|   |       |   |   concurrency.py
|   |       |   |   datastructures.py
|   |       |   |   encoders.py
|   |       |   |   exceptions.py
|   |       |   |   exception_handlers.py
|   |       |   |   logger.py
|   |       |   |   params.py
|   |       |   |   param_functions.py
|   |       |   |   py.typed
|   |       |   |   requests.py
|   |       |   |   responses.py
|   |       |   |   routing.py
|   |       |   |   staticfiles.py
|   |       |   |   templating.py
|   |       |   |   testclient.py
|   |       |   |   types.py
|   |       |   |   utils.py
|   |       |   |   websockets.py
|   |       |   |   _compat.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   +---dependencies
|   |       |   |   |   models.py
|   |       |   |   |   utils.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           models.cpython-314.pyc
|   |       |   |           utils.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---middleware
|   |       |   |   |   cors.py
|   |       |   |   |   gzip.py
|   |       |   |   |   httpsredirect.py
|   |       |   |   |   trustedhost.py
|   |       |   |   |   wsgi.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           cors.cpython-314.pyc
|   |       |   |           gzip.cpython-314.pyc
|   |       |   |           httpsredirect.cpython-314.pyc
|   |       |   |           trustedhost.cpython-314.pyc
|   |       |   |           wsgi.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---openapi
|   |       |   |   |   constants.py
|   |       |   |   |   docs.py
|   |       |   |   |   models.py
|   |       |   |   |   utils.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           constants.cpython-314.pyc
|   |       |   |           docs.cpython-314.pyc
|   |       |   |           models.cpython-314.pyc
|   |       |   |           utils.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---security
|   |       |   |   |   api_key.py
|   |       |   |   |   base.py
|   |       |   |   |   http.py
|   |       |   |   |   oauth2.py
|   |       |   |   |   open_id_connect_url.py
|   |       |   |   |   utils.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           api_key.cpython-314.pyc
|   |       |   |           base.cpython-314.pyc
|   |       |   |           http.cpython-314.pyc
|   |       |   |           oauth2.cpython-314.pyc
|   |       |   |           open_id_connect_url.cpython-314.pyc
|   |       |   |           utils.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           applications.cpython-314.pyc
|   |       |           background.cpython-314.pyc
|   |       |           cli.cpython-314.pyc
|   |       |           concurrency.cpython-314.pyc
|   |       |           datastructures.cpython-314.pyc
|   |       |           encoders.cpython-314.pyc
|   |       |           exceptions.cpython-314.pyc
|   |       |           exception_handlers.cpython-314.pyc
|   |       |           logger.cpython-314.pyc
|   |       |           params.cpython-314.pyc
|   |       |           param_functions.cpython-314.pyc
|   |       |           requests.cpython-314.pyc
|   |       |           responses.cpython-314.pyc
|   |       |           routing.cpython-314.pyc
|   |       |           staticfiles.cpython-314.pyc
|   |       |           templating.cpython-314.pyc
|   |       |           testclient.cpython-314.pyc
|   |       |           types.cpython-314.pyc
|   |       |           utils.cpython-314.pyc
|   |       |           websockets.cpython-314.pyc
|   |       |           _compat.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           __main__.cpython-314.pyc
|   |       |           
|   |       +---fastapi-0.115.6.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---h11
|   |       |   |   py.typed
|   |       |   |   _abnf.py
|   |       |   |   _connection.py
|   |       |   |   _events.py
|   |       |   |   _headers.py
|   |       |   |   _readers.py
|   |       |   |   _receivebuffer.py
|   |       |   |   _state.py
|   |       |   |   _util.py
|   |       |   |   _version.py
|   |       |   |   _writers.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           _abnf.cpython-314.pyc
|   |       |           _connection.cpython-314.pyc
|   |       |           _events.cpython-314.pyc
|   |       |           _headers.cpython-314.pyc
|   |       |           _readers.cpython-314.pyc
|   |       |           _receivebuffer.cpython-314.pyc
|   |       |           _state.cpython-314.pyc
|   |       |           _util.cpython-314.pyc
|   |       |           _version.cpython-314.pyc
|   |       |           _writers.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---h11-0.16.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   top_level.txt
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.txt
|   |       |           
|   |       +---idna
|   |       |   |   codec.py
|   |       |   |   compat.py
|   |       |   |   core.py
|   |       |   |   idnadata.py
|   |       |   |   intranges.py
|   |       |   |   package_data.py
|   |       |   |   py.typed
|   |       |   |   uts46data.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           codec.cpython-314.pyc
|   |       |           compat.cpython-314.pyc
|   |       |           core.cpython-314.pyc
|   |       |           idnadata.cpython-314.pyc
|   |       |           intranges.cpython-314.pyc
|   |       |           package_data.cpython-314.pyc
|   |       |           uts46data.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---idna-3.11.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.md
|   |       |           
|   |       +---pip
|   |       |   |   py.typed
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   __pip-runner__.py
|   |       |   |   
|   |       |   +---_internal
|   |       |   |   |   build_env.py
|   |       |   |   |   cache.py
|   |       |   |   |   configuration.py
|   |       |   |   |   exceptions.py
|   |       |   |   |   main.py
|   |       |   |   |   pyproject.py
|   |       |   |   |   self_outdated_check.py
|   |       |   |   |   wheel_builder.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---cli
|   |       |   |   |   |   autocompletion.py
|   |       |   |   |   |   base_command.py
|   |       |   |   |   |   cmdoptions.py
|   |       |   |   |   |   command_context.py
|   |       |   |   |   |   index_command.py
|   |       |   |   |   |   main.py
|   |       |   |   |   |   main_parser.py
|   |       |   |   |   |   parser.py
|   |       |   |   |   |   progress_bars.py
|   |       |   |   |   |   req_command.py
|   |       |   |   |   |   spinners.py
|   |       |   |   |   |   status_codes.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           autocompletion.cpython-314.pyc
|   |       |   |   |           base_command.cpython-314.pyc
|   |       |   |   |           cmdoptions.cpython-314.pyc
|   |       |   |   |           command_context.cpython-314.pyc
|   |       |   |   |           index_command.cpython-314.pyc
|   |       |   |   |           main.cpython-314.pyc
|   |       |   |   |           main_parser.cpython-314.pyc
|   |       |   |   |           parser.cpython-314.pyc
|   |       |   |   |           progress_bars.cpython-314.pyc
|   |       |   |   |           req_command.cpython-314.pyc
|   |       |   |   |           spinners.cpython-314.pyc
|   |       |   |   |           status_codes.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---commands
|   |       |   |   |   |   cache.py
|   |       |   |   |   |   check.py
|   |       |   |   |   |   completion.py
|   |       |   |   |   |   configuration.py
|   |       |   |   |   |   debug.py
|   |       |   |   |   |   download.py
|   |       |   |   |   |   freeze.py
|   |       |   |   |   |   hash.py
|   |       |   |   |   |   help.py
|   |       |   |   |   |   index.py
|   |       |   |   |   |   inspect.py
|   |       |   |   |   |   install.py
|   |       |   |   |   |   list.py
|   |       |   |   |   |   lock.py
|   |       |   |   |   |   search.py
|   |       |   |   |   |   show.py
|   |       |   |   |   |   uninstall.py
|   |       |   |   |   |   wheel.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           cache.cpython-314.pyc
|   |       |   |   |           check.cpython-314.pyc
|   |       |   |   |           completion.cpython-314.pyc
|   |       |   |   |           configuration.cpython-314.pyc
|   |       |   |   |           debug.cpython-314.pyc
|   |       |   |   |           download.cpython-314.pyc
|   |       |   |   |           freeze.cpython-314.pyc
|   |       |   |   |           hash.cpython-314.pyc
|   |       |   |   |           help.cpython-314.pyc
|   |       |   |   |           index.cpython-314.pyc
|   |       |   |   |           inspect.cpython-314.pyc
|   |       |   |   |           install.cpython-314.pyc
|   |       |   |   |           list.cpython-314.pyc
|   |       |   |   |           lock.cpython-314.pyc
|   |       |   |   |           search.cpython-314.pyc
|   |       |   |   |           show.cpython-314.pyc
|   |       |   |   |           uninstall.cpython-314.pyc
|   |       |   |   |           wheel.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---distributions
|   |       |   |   |   |   base.py
|   |       |   |   |   |   installed.py
|   |       |   |   |   |   sdist.py
|   |       |   |   |   |   wheel.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-314.pyc
|   |       |   |   |           installed.cpython-314.pyc
|   |       |   |   |           sdist.cpython-314.pyc
|   |       |   |   |           wheel.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---index
|   |       |   |   |   |   collector.py
|   |       |   |   |   |   package_finder.py
|   |       |   |   |   |   sources.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           collector.cpython-314.pyc
|   |       |   |   |           package_finder.cpython-314.pyc
|   |       |   |   |           sources.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---locations
|   |       |   |   |   |   base.py
|   |       |   |   |   |   _distutils.py
|   |       |   |   |   |   _sysconfig.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-314.pyc
|   |       |   |   |           _distutils.cpython-314.pyc
|   |       |   |   |           _sysconfig.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---metadata
|   |       |   |   |   |   base.py
|   |       |   |   |   |   pkg_resources.py
|   |       |   |   |   |   _json.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---importlib
|   |       |   |   |   |   |   _compat.py
|   |       |   |   |   |   |   _dists.py
|   |       |   |   |   |   |   _envs.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           _compat.cpython-314.pyc
|   |       |   |   |   |           _dists.cpython-314.pyc
|   |       |   |   |   |           _envs.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-314.pyc
|   |       |   |   |           pkg_resources.cpython-314.pyc
|   |       |   |   |           _json.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---models
|   |       |   |   |   |   candidate.py
|   |       |   |   |   |   direct_url.py
|   |       |   |   |   |   format_control.py
|   |       |   |   |   |   index.py
|   |       |   |   |   |   installation_report.py
|   |       |   |   |   |   link.py
|   |       |   |   |   |   pylock.py
|   |       |   |   |   |   scheme.py
|   |       |   |   |   |   search_scope.py
|   |       |   |   |   |   selection_prefs.py
|   |       |   |   |   |   target_python.py
|   |       |   |   |   |   wheel.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           candidate.cpython-314.pyc
|   |       |   |   |           direct_url.cpython-314.pyc
|   |       |   |   |           format_control.cpython-314.pyc
|   |       |   |   |           index.cpython-314.pyc
|   |       |   |   |           installation_report.cpython-314.pyc
|   |       |   |   |           link.cpython-314.pyc
|   |       |   |   |           pylock.cpython-314.pyc
|   |       |   |   |           scheme.cpython-314.pyc
|   |       |   |   |           search_scope.cpython-314.pyc
|   |       |   |   |           selection_prefs.cpython-314.pyc
|   |       |   |   |           target_python.cpython-314.pyc
|   |       |   |   |           wheel.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---network
|   |       |   |   |   |   auth.py
|   |       |   |   |   |   cache.py
|   |       |   |   |   |   download.py
|   |       |   |   |   |   lazy_wheel.py
|   |       |   |   |   |   session.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   xmlrpc.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           auth.cpython-314.pyc
|   |       |   |   |           cache.cpython-314.pyc
|   |       |   |   |           download.cpython-314.pyc
|   |       |   |   |           lazy_wheel.cpython-314.pyc
|   |       |   |   |           session.cpython-314.pyc
|   |       |   |   |           utils.cpython-314.pyc
|   |       |   |   |           xmlrpc.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---operations
|   |       |   |   |   |   check.py
|   |       |   |   |   |   freeze.py
|   |       |   |   |   |   prepare.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---build
|   |       |   |   |   |   |   build_tracker.py
|   |       |   |   |   |   |   metadata.py
|   |       |   |   |   |   |   metadata_editable.py
|   |       |   |   |   |   |   wheel.py
|   |       |   |   |   |   |   wheel_editable.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           build_tracker.cpython-314.pyc
|   |       |   |   |   |           metadata.cpython-314.pyc
|   |       |   |   |   |           metadata_editable.cpython-314.pyc
|   |       |   |   |   |           wheel.cpython-314.pyc
|   |       |   |   |   |           wheel_editable.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---install
|   |       |   |   |   |   |   wheel.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           wheel.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           check.cpython-314.pyc
|   |       |   |   |           freeze.cpython-314.pyc
|   |       |   |   |           prepare.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---req
|   |       |   |   |   |   constructors.py
|   |       |   |   |   |   req_dependency_group.py
|   |       |   |   |   |   req_file.py
|   |       |   |   |   |   req_install.py
|   |       |   |   |   |   req_set.py
|   |       |   |   |   |   req_uninstall.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           constructors.cpython-314.pyc
|   |       |   |   |           req_dependency_group.cpython-314.pyc
|   |       |   |   |           req_file.cpython-314.pyc
|   |       |   |   |           req_install.cpython-314.pyc
|   |       |   |   |           req_set.cpython-314.pyc
|   |       |   |   |           req_uninstall.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---resolution
|   |       |   |   |   |   base.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---legacy
|   |       |   |   |   |   |   resolver.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           resolver.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---resolvelib
|   |       |   |   |   |   |   base.py
|   |       |   |   |   |   |   candidates.py
|   |       |   |   |   |   |   factory.py
|   |       |   |   |   |   |   found_candidates.py
|   |       |   |   |   |   |   provider.py
|   |       |   |   |   |   |   reporter.py
|   |       |   |   |   |   |   requirements.py
|   |       |   |   |   |   |   resolver.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           base.cpython-314.pyc
|   |       |   |   |   |           candidates.cpython-314.pyc
|   |       |   |   |   |           factory.cpython-314.pyc
|   |       |   |   |   |           found_candidates.cpython-314.pyc
|   |       |   |   |   |           provider.cpython-314.pyc
|   |       |   |   |   |           reporter.cpython-314.pyc
|   |       |   |   |   |           requirements.cpython-314.pyc
|   |       |   |   |   |           resolver.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           base.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---utils
|   |       |   |   |   |   appdirs.py
|   |       |   |   |   |   compat.py
|   |       |   |   |   |   compatibility_tags.py
|   |       |   |   |   |   datetime.py
|   |       |   |   |   |   deprecation.py
|   |       |   |   |   |   direct_url_helpers.py
|   |       |   |   |   |   egg_link.py
|   |       |   |   |   |   entrypoints.py
|   |       |   |   |   |   filesystem.py
|   |       |   |   |   |   filetypes.py
|   |       |   |   |   |   glibc.py
|   |       |   |   |   |   hashes.py
|   |       |   |   |   |   logging.py
|   |       |   |   |   |   misc.py
|   |       |   |   |   |   packaging.py
|   |       |   |   |   |   retry.py
|   |       |   |   |   |   subprocess.py
|   |       |   |   |   |   temp_dir.py
|   |       |   |   |   |   unpacking.py
|   |       |   |   |   |   urls.py
|   |       |   |   |   |   virtualenv.py
|   |       |   |   |   |   wheel.py
|   |       |   |   |   |   _jaraco_text.py
|   |       |   |   |   |   _log.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           appdirs.cpython-314.pyc
|   |       |   |   |           compat.cpython-314.pyc
|   |       |   |   |           compatibility_tags.cpython-314.pyc
|   |       |   |   |           datetime.cpython-314.pyc
|   |       |   |   |           deprecation.cpython-314.pyc
|   |       |   |   |           direct_url_helpers.cpython-314.pyc
|   |       |   |   |           egg_link.cpython-314.pyc
|   |       |   |   |           entrypoints.cpython-314.pyc
|   |       |   |   |           filesystem.cpython-314.pyc
|   |       |   |   |           filetypes.cpython-314.pyc
|   |       |   |   |           glibc.cpython-314.pyc
|   |       |   |   |           hashes.cpython-314.pyc
|   |       |   |   |           logging.cpython-314.pyc
|   |       |   |   |           misc.cpython-314.pyc
|   |       |   |   |           packaging.cpython-314.pyc
|   |       |   |   |           retry.cpython-314.pyc
|   |       |   |   |           subprocess.cpython-314.pyc
|   |       |   |   |           temp_dir.cpython-314.pyc
|   |       |   |   |           unpacking.cpython-314.pyc
|   |       |   |   |           urls.cpython-314.pyc
|   |       |   |   |           virtualenv.cpython-314.pyc
|   |       |   |   |           wheel.cpython-314.pyc
|   |       |   |   |           _jaraco_text.cpython-314.pyc
|   |       |   |   |           _log.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---vcs
|   |       |   |   |   |   bazaar.py
|   |       |   |   |   |   git.py
|   |       |   |   |   |   mercurial.py
|   |       |   |   |   |   subversion.py
|   |       |   |   |   |   versioncontrol.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           bazaar.cpython-314.pyc
|   |       |   |   |           git.cpython-314.pyc
|   |       |   |   |           mercurial.cpython-314.pyc
|   |       |   |   |           subversion.cpython-314.pyc
|   |       |   |   |           versioncontrol.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           build_env.cpython-314.pyc
|   |       |   |           cache.cpython-314.pyc
|   |       |   |           configuration.cpython-314.pyc
|   |       |   |           exceptions.cpython-314.pyc
|   |       |   |           main.cpython-314.pyc
|   |       |   |           pyproject.cpython-314.pyc
|   |       |   |           self_outdated_check.cpython-314.pyc
|   |       |   |           wheel_builder.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---_vendor
|   |       |   |   |   README.rst
|   |       |   |   |   vendor.txt
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---cachecontrol
|   |       |   |   |   |   adapter.py
|   |       |   |   |   |   cache.py
|   |       |   |   |   |   controller.py
|   |       |   |   |   |   filewrapper.py
|   |       |   |   |   |   heuristics.py
|   |       |   |   |   |   LICENSE.txt
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   serialize.py
|   |       |   |   |   |   wrapper.py
|   |       |   |   |   |   _cmd.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---caches
|   |       |   |   |   |   |   file_cache.py
|   |       |   |   |   |   |   redis_cache.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           file_cache.cpython-314.pyc
|   |       |   |   |   |           redis_cache.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           adapter.cpython-314.pyc
|   |       |   |   |           cache.cpython-314.pyc
|   |       |   |   |           controller.cpython-314.pyc
|   |       |   |   |           filewrapper.cpython-314.pyc
|   |       |   |   |           heuristics.cpython-314.pyc
|   |       |   |   |           serialize.cpython-314.pyc
|   |       |   |   |           wrapper.cpython-314.pyc
|   |       |   |   |           _cmd.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---certifi
|   |       |   |   |   |   cacert.pem
|   |       |   |   |   |   core.py
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           core.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           __main__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---dependency_groups
|   |       |   |   |   |   LICENSE.txt
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   _implementation.py
|   |       |   |   |   |   _lint_dependency_groups.py
|   |       |   |   |   |   _pip_wrapper.py
|   |       |   |   |   |   _toml_compat.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _implementation.cpython-314.pyc
|   |       |   |   |           _lint_dependency_groups.cpython-314.pyc
|   |       |   |   |           _pip_wrapper.cpython-314.pyc
|   |       |   |   |           _toml_compat.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           __main__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---distlib
|   |       |   |   |   |   compat.py
|   |       |   |   |   |   LICENSE.txt
|   |       |   |   |   |   resources.py
|   |       |   |   |   |   scripts.py
|   |       |   |   |   |   t32.exe
|   |       |   |   |   |   t64-arm.exe
|   |       |   |   |   |   t64.exe
|   |       |   |   |   |   util.py
|   |       |   |   |   |   w32.exe
|   |       |   |   |   |   w64-arm.exe
|   |       |   |   |   |   w64.exe
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           compat.cpython-314.pyc
|   |       |   |   |           resources.cpython-314.pyc
|   |       |   |   |           scripts.cpython-314.pyc
|   |       |   |   |           util.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---distro
|   |       |   |   |   |   distro.py
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           distro.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           __main__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---idna
|   |       |   |   |   |   codec.py
|   |       |   |   |   |   compat.py
|   |       |   |   |   |   core.py
|   |       |   |   |   |   idnadata.py
|   |       |   |   |   |   intranges.py
|   |       |   |   |   |   LICENSE.md
|   |       |   |   |   |   package_data.py
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   uts46data.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           codec.cpython-314.pyc
|   |       |   |   |           compat.cpython-314.pyc
|   |       |   |   |           core.cpython-314.pyc
|   |       |   |   |           idnadata.cpython-314.pyc
|   |       |   |   |           intranges.cpython-314.pyc
|   |       |   |   |           package_data.cpython-314.pyc
|   |       |   |   |           uts46data.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---msgpack
|   |       |   |   |   |   COPYING
|   |       |   |   |   |   exceptions.py
|   |       |   |   |   |   ext.py
|   |       |   |   |   |   fallback.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           exceptions.cpython-314.pyc
|   |       |   |   |           ext.cpython-314.pyc
|   |       |   |   |           fallback.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---packaging
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   LICENSE.APACHE
|   |       |   |   |   |   LICENSE.BSD
|   |       |   |   |   |   markers.py
|   |       |   |   |   |   metadata.py
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   requirements.py
|   |       |   |   |   |   specifiers.py
|   |       |   |   |   |   tags.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   version.py
|   |       |   |   |   |   _elffile.py
|   |       |   |   |   |   _manylinux.py
|   |       |   |   |   |   _musllinux.py
|   |       |   |   |   |   _parser.py
|   |       |   |   |   |   _structures.py
|   |       |   |   |   |   _tokenizer.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---licenses
|   |       |   |   |   |   |   _spdx.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           _spdx.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           markers.cpython-314.pyc
|   |       |   |   |           metadata.cpython-314.pyc
|   |       |   |   |           requirements.cpython-314.pyc
|   |       |   |   |           specifiers.cpython-314.pyc
|   |       |   |   |           tags.cpython-314.pyc
|   |       |   |   |           utils.cpython-314.pyc
|   |       |   |   |           version.cpython-314.pyc
|   |       |   |   |           _elffile.cpython-314.pyc
|   |       |   |   |           _manylinux.cpython-314.pyc
|   |       |   |   |           _musllinux.cpython-314.pyc
|   |       |   |   |           _parser.cpython-314.pyc
|   |       |   |   |           _structures.cpython-314.pyc
|   |       |   |   |           _tokenizer.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---pkg_resources
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---platformdirs
|   |       |   |   |   |   android.py
|   |       |   |   |   |   api.py
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   macos.py
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   unix.py
|   |       |   |   |   |   version.py
|   |       |   |   |   |   windows.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           android.cpython-314.pyc
|   |       |   |   |           api.cpython-314.pyc
|   |       |   |   |           macos.cpython-314.pyc
|   |       |   |   |           unix.cpython-314.pyc
|   |       |   |   |           version.cpython-314.pyc
|   |       |   |   |           windows.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           __main__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---pygments
|   |       |   |   |   |   console.py
|   |       |   |   |   |   filter.py
|   |       |   |   |   |   formatter.py
|   |       |   |   |   |   lexer.py
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   modeline.py
|   |       |   |   |   |   plugin.py
|   |       |   |   |   |   regexopt.py
|   |       |   |   |   |   scanner.py
|   |       |   |   |   |   sphinxext.py
|   |       |   |   |   |   style.py
|   |       |   |   |   |   token.py
|   |       |   |   |   |   unistring.py
|   |       |   |   |   |   util.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   +---filters
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---formatters
|   |       |   |   |   |   |   _mapping.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           _mapping.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---lexers
|   |       |   |   |   |   |   python.py
|   |       |   |   |   |   |   _mapping.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           python.cpython-314.pyc
|   |       |   |   |   |           _mapping.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---styles
|   |       |   |   |   |   |   _mapping.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           _mapping.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           console.cpython-314.pyc
|   |       |   |   |           filter.cpython-314.pyc
|   |       |   |   |           formatter.cpython-314.pyc
|   |       |   |   |           lexer.cpython-314.pyc
|   |       |   |   |           modeline.cpython-314.pyc
|   |       |   |   |           plugin.cpython-314.pyc
|   |       |   |   |           regexopt.cpython-314.pyc
|   |       |   |   |           scanner.cpython-314.pyc
|   |       |   |   |           sphinxext.cpython-314.pyc
|   |       |   |   |           style.cpython-314.pyc
|   |       |   |   |           token.cpython-314.pyc
|   |       |   |   |           unistring.cpython-314.pyc
|   |       |   |   |           util.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           __main__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---pyproject_hooks
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   _impl.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---_in_process
|   |       |   |   |   |   |   _in_process.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           _in_process.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _impl.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---requests
|   |       |   |   |   |   adapters.py
|   |       |   |   |   |   api.py
|   |       |   |   |   |   auth.py
|   |       |   |   |   |   certs.py
|   |       |   |   |   |   compat.py
|   |       |   |   |   |   cookies.py
|   |       |   |   |   |   exceptions.py
|   |       |   |   |   |   help.py
|   |       |   |   |   |   hooks.py
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   models.py
|   |       |   |   |   |   packages.py
|   |       |   |   |   |   sessions.py
|   |       |   |   |   |   status_codes.py
|   |       |   |   |   |   structures.py
|   |       |   |   |   |   utils.py
|   |       |   |   |   |   _internal_utils.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __version__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           adapters.cpython-314.pyc
|   |       |   |   |           api.cpython-314.pyc
|   |       |   |   |           auth.cpython-314.pyc
|   |       |   |   |           certs.cpython-314.pyc
|   |       |   |   |           compat.cpython-314.pyc
|   |       |   |   |           cookies.cpython-314.pyc
|   |       |   |   |           exceptions.cpython-314.pyc
|   |       |   |   |           help.cpython-314.pyc
|   |       |   |   |           hooks.cpython-314.pyc
|   |       |   |   |           models.cpython-314.pyc
|   |       |   |   |           packages.cpython-314.pyc
|   |       |   |   |           sessions.cpython-314.pyc
|   |       |   |   |           status_codes.cpython-314.pyc
|   |       |   |   |           structures.cpython-314.pyc
|   |       |   |   |           utils.cpython-314.pyc
|   |       |   |   |           _internal_utils.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           __version__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---resolvelib
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   providers.py
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   reporters.py
|   |       |   |   |   |   structs.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---resolvers
|   |       |   |   |   |   |   abstract.py
|   |       |   |   |   |   |   criterion.py
|   |       |   |   |   |   |   exceptions.py
|   |       |   |   |   |   |   resolution.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           abstract.cpython-314.pyc
|   |       |   |   |   |           criterion.cpython-314.pyc
|   |       |   |   |   |           exceptions.cpython-314.pyc
|   |       |   |   |   |           resolution.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           providers.cpython-314.pyc
|   |       |   |   |           reporters.cpython-314.pyc
|   |       |   |   |           structs.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---rich
|   |       |   |   |   |   abc.py
|   |       |   |   |   |   align.py
|   |       |   |   |   |   ansi.py
|   |       |   |   |   |   bar.py
|   |       |   |   |   |   box.py
|   |       |   |   |   |   cells.py
|   |       |   |   |   |   color.py
|   |       |   |   |   |   color_triplet.py
|   |       |   |   |   |   columns.py
|   |       |   |   |   |   console.py
|   |       |   |   |   |   constrain.py
|   |       |   |   |   |   containers.py
|   |       |   |   |   |   control.py
|   |       |   |   |   |   default_styles.py
|   |       |   |   |   |   diagnose.py
|   |       |   |   |   |   emoji.py
|   |       |   |   |   |   errors.py
|   |       |   |   |   |   filesize.py
|   |       |   |   |   |   file_proxy.py
|   |       |   |   |   |   highlighter.py
|   |       |   |   |   |   json.py
|   |       |   |   |   |   jupyter.py
|   |       |   |   |   |   layout.py
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   live.py
|   |       |   |   |   |   live_render.py
|   |       |   |   |   |   logging.py
|   |       |   |   |   |   markup.py
|   |       |   |   |   |   measure.py
|   |       |   |   |   |   padding.py
|   |       |   |   |   |   pager.py
|   |       |   |   |   |   palette.py
|   |       |   |   |   |   panel.py
|   |       |   |   |   |   pretty.py
|   |       |   |   |   |   progress.py
|   |       |   |   |   |   progress_bar.py
|   |       |   |   |   |   prompt.py
|   |       |   |   |   |   protocol.py
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   region.py
|   |       |   |   |   |   repr.py
|   |       |   |   |   |   rule.py
|   |       |   |   |   |   scope.py
|   |       |   |   |   |   screen.py
|   |       |   |   |   |   segment.py
|   |       |   |   |   |   spinner.py
|   |       |   |   |   |   status.py
|   |       |   |   |   |   style.py
|   |       |   |   |   |   styled.py
|   |       |   |   |   |   syntax.py
|   |       |   |   |   |   table.py
|   |       |   |   |   |   terminal_theme.py
|   |       |   |   |   |   text.py
|   |       |   |   |   |   theme.py
|   |       |   |   |   |   themes.py
|   |       |   |   |   |   traceback.py
|   |       |   |   |   |   tree.py
|   |       |   |   |   |   _cell_widths.py
|   |       |   |   |   |   _emoji_codes.py
|   |       |   |   |   |   _emoji_replace.py
|   |       |   |   |   |   _export_format.py
|   |       |   |   |   |   _extension.py
|   |       |   |   |   |   _fileno.py
|   |       |   |   |   |   _inspect.py
|   |       |   |   |   |   _log_render.py
|   |       |   |   |   |   _loop.py
|   |       |   |   |   |   _null_file.py
|   |       |   |   |   |   _palettes.py
|   |       |   |   |   |   _pick.py
|   |       |   |   |   |   _ratio.py
|   |       |   |   |   |   _spinners.py
|   |       |   |   |   |   _stack.py
|   |       |   |   |   |   _timer.py
|   |       |   |   |   |   _win32_console.py
|   |       |   |   |   |   _windows.py
|   |       |   |   |   |   _windows_renderer.py
|   |       |   |   |   |   _wrap.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   __main__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           abc.cpython-314.pyc
|   |       |   |   |           align.cpython-314.pyc
|   |       |   |   |           ansi.cpython-314.pyc
|   |       |   |   |           bar.cpython-314.pyc
|   |       |   |   |           box.cpython-314.pyc
|   |       |   |   |           cells.cpython-314.pyc
|   |       |   |   |           color.cpython-314.pyc
|   |       |   |   |           color_triplet.cpython-314.pyc
|   |       |   |   |           columns.cpython-314.pyc
|   |       |   |   |           console.cpython-314.pyc
|   |       |   |   |           constrain.cpython-314.pyc
|   |       |   |   |           containers.cpython-314.pyc
|   |       |   |   |           control.cpython-314.pyc
|   |       |   |   |           default_styles.cpython-314.pyc
|   |       |   |   |           diagnose.cpython-314.pyc
|   |       |   |   |           emoji.cpython-314.pyc
|   |       |   |   |           errors.cpython-314.pyc
|   |       |   |   |           filesize.cpython-314.pyc
|   |       |   |   |           file_proxy.cpython-314.pyc
|   |       |   |   |           highlighter.cpython-314.pyc
|   |       |   |   |           json.cpython-314.pyc
|   |       |   |   |           jupyter.cpython-314.pyc
|   |       |   |   |           layout.cpython-314.pyc
|   |       |   |   |           live.cpython-314.pyc
|   |       |   |   |           live_render.cpython-314.pyc
|   |       |   |   |           logging.cpython-314.pyc
|   |       |   |   |           markup.cpython-314.pyc
|   |       |   |   |           measure.cpython-314.pyc
|   |       |   |   |           padding.cpython-314.pyc
|   |       |   |   |           pager.cpython-314.pyc
|   |       |   |   |           palette.cpython-314.pyc
|   |       |   |   |           panel.cpython-314.pyc
|   |       |   |   |           pretty.cpython-314.pyc
|   |       |   |   |           progress.cpython-314.pyc
|   |       |   |   |           progress_bar.cpython-314.pyc
|   |       |   |   |           prompt.cpython-314.pyc
|   |       |   |   |           protocol.cpython-314.pyc
|   |       |   |   |           region.cpython-314.pyc
|   |       |   |   |           repr.cpython-314.pyc
|   |       |   |   |           rule.cpython-314.pyc
|   |       |   |   |           scope.cpython-314.pyc
|   |       |   |   |           screen.cpython-314.pyc
|   |       |   |   |           segment.cpython-314.pyc
|   |       |   |   |           spinner.cpython-314.pyc
|   |       |   |   |           status.cpython-314.pyc
|   |       |   |   |           style.cpython-314.pyc
|   |       |   |   |           styled.cpython-314.pyc
|   |       |   |   |           syntax.cpython-314.pyc
|   |       |   |   |           table.cpython-314.pyc
|   |       |   |   |           terminal_theme.cpython-314.pyc
|   |       |   |   |           text.cpython-314.pyc
|   |       |   |   |           theme.cpython-314.pyc
|   |       |   |   |           themes.cpython-314.pyc
|   |       |   |   |           traceback.cpython-314.pyc
|   |       |   |   |           tree.cpython-314.pyc
|   |       |   |   |           _cell_widths.cpython-314.pyc
|   |       |   |   |           _emoji_codes.cpython-314.pyc
|   |       |   |   |           _emoji_replace.cpython-314.pyc
|   |       |   |   |           _export_format.cpython-314.pyc
|   |       |   |   |           _extension.cpython-314.pyc
|   |       |   |   |           _fileno.cpython-314.pyc
|   |       |   |   |           _inspect.cpython-314.pyc
|   |       |   |   |           _log_render.cpython-314.pyc
|   |       |   |   |           _loop.cpython-314.pyc
|   |       |   |   |           _null_file.cpython-314.pyc
|   |       |   |   |           _palettes.cpython-314.pyc
|   |       |   |   |           _pick.cpython-314.pyc
|   |       |   |   |           _ratio.cpython-314.pyc
|   |       |   |   |           _spinners.cpython-314.pyc
|   |       |   |   |           _stack.cpython-314.pyc
|   |       |   |   |           _timer.cpython-314.pyc
|   |       |   |   |           _win32_console.cpython-314.pyc
|   |       |   |   |           _windows.cpython-314.pyc
|   |       |   |   |           _windows_renderer.cpython-314.pyc
|   |       |   |   |           _wrap.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           __main__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---tomli
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   _parser.py
|   |       |   |   |   |   _re.py
|   |       |   |   |   |   _types.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _parser.cpython-314.pyc
|   |       |   |   |           _re.cpython-314.pyc
|   |       |   |   |           _types.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---tomli_w
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   _writer.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _writer.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---truststore
|   |       |   |   |   |   LICENSE
|   |       |   |   |   |   py.typed
|   |       |   |   |   |   _api.py
|   |       |   |   |   |   _macos.py
|   |       |   |   |   |   _openssl.py
|   |       |   |   |   |   _ssl_constants.py
|   |       |   |   |   |   _windows.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           _api.cpython-314.pyc
|   |       |   |   |           _macos.cpython-314.pyc
|   |       |   |   |           _openssl.cpython-314.pyc
|   |       |   |   |           _ssl_constants.cpython-314.pyc
|   |       |   |   |           _windows.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---urllib3
|   |       |   |   |   |   connection.py
|   |       |   |   |   |   connectionpool.py
|   |       |   |   |   |   exceptions.py
|   |       |   |   |   |   fields.py
|   |       |   |   |   |   filepost.py
|   |       |   |   |   |   LICENSE.txt
|   |       |   |   |   |   poolmanager.py
|   |       |   |   |   |   request.py
|   |       |   |   |   |   response.py
|   |       |   |   |   |   _collections.py
|   |       |   |   |   |   _version.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   +---contrib
|   |       |   |   |   |   |   appengine.py
|   |       |   |   |   |   |   ntlmpool.py
|   |       |   |   |   |   |   pyopenssl.py
|   |       |   |   |   |   |   securetransport.py
|   |       |   |   |   |   |   socks.py
|   |       |   |   |   |   |   _appengine_environ.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---_securetransport
|   |       |   |   |   |   |   |   bindings.py
|   |       |   |   |   |   |   |   low_level.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           bindings.cpython-314.pyc
|   |       |   |   |   |   |           low_level.cpython-314.pyc
|   |       |   |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           appengine.cpython-314.pyc
|   |       |   |   |   |           ntlmpool.cpython-314.pyc
|   |       |   |   |   |           pyopenssl.cpython-314.pyc
|   |       |   |   |   |           securetransport.cpython-314.pyc
|   |       |   |   |   |           socks.cpython-314.pyc
|   |       |   |   |   |           _appengine_environ.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---packages
|   |       |   |   |   |   |   six.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   +---backports
|   |       |   |   |   |   |   |   makefile.py
|   |       |   |   |   |   |   |   weakref_finalize.py
|   |       |   |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   |   
|   |       |   |   |   |   |   \---__pycache__
|   |       |   |   |   |   |           makefile.cpython-314.pyc
|   |       |   |   |   |   |           weakref_finalize.cpython-314.pyc
|   |       |   |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |   |           
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           six.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   +---util
|   |       |   |   |   |   |   connection.py
|   |       |   |   |   |   |   proxy.py
|   |       |   |   |   |   |   queue.py
|   |       |   |   |   |   |   request.py
|   |       |   |   |   |   |   response.py
|   |       |   |   |   |   |   retry.py
|   |       |   |   |   |   |   ssltransport.py
|   |       |   |   |   |   |   ssl_.py
|   |       |   |   |   |   |   ssl_match_hostname.py
|   |       |   |   |   |   |   timeout.py
|   |       |   |   |   |   |   url.py
|   |       |   |   |   |   |   wait.py
|   |       |   |   |   |   |   __init__.py
|   |       |   |   |   |   |   
|   |       |   |   |   |   \---__pycache__
|   |       |   |   |   |           connection.cpython-314.pyc
|   |       |   |   |   |           proxy.cpython-314.pyc
|   |       |   |   |   |           queue.cpython-314.pyc
|   |       |   |   |   |           request.cpython-314.pyc
|   |       |   |   |   |           response.cpython-314.pyc
|   |       |   |   |   |           retry.cpython-314.pyc
|   |       |   |   |   |           ssltransport.cpython-314.pyc
|   |       |   |   |   |           ssl_.cpython-314.pyc
|   |       |   |   |   |           ssl_match_hostname.cpython-314.pyc
|   |       |   |   |   |           timeout.cpython-314.pyc
|   |       |   |   |   |           url.cpython-314.pyc
|   |       |   |   |   |           wait.cpython-314.pyc
|   |       |   |   |   |           __init__.cpython-314.pyc
|   |       |   |   |   |           
|   |       |   |   |   \---__pycache__
|   |       |   |   |           connection.cpython-314.pyc
|   |       |   |   |           connectionpool.cpython-314.pyc
|   |       |   |   |           exceptions.cpython-314.pyc
|   |       |   |   |           fields.cpython-314.pyc
|   |       |   |   |           filepost.cpython-314.pyc
|   |       |   |   |           poolmanager.cpython-314.pyc
|   |       |   |   |           request.cpython-314.pyc
|   |       |   |   |           response.cpython-314.pyc
|   |       |   |   |           _collections.cpython-314.pyc
|   |       |   |   |           _version.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           __init__.cpython-314.pyc
|   |       |           __main__.cpython-314.pyc
|   |       |           __pip-runner__.cpython-314.pyc
|   |       |           
|   |       +---pip-25.3.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |       |   AUTHORS.txt
|   |       |       |   LICENSE.txt
|   |       |       |   
|   |       |       \---src
|   |       |           \---pip
|   |       |               \---_vendor
|   |       |                   +---cachecontrol
|   |       |                   |       LICENSE.txt
|   |       |                   |       
|   |       |                   +---certifi
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---dependency_groups
|   |       |                   |       LICENSE.txt
|   |       |                   |       
|   |       |                   +---distlib
|   |       |                   |       LICENSE.txt
|   |       |                   |       
|   |       |                   +---distro
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---idna
|   |       |                   |       LICENSE.md
|   |       |                   |       
|   |       |                   +---msgpack
|   |       |                   |       COPYING
|   |       |                   |       
|   |       |                   +---packaging
|   |       |                   |       LICENSE
|   |       |                   |       LICENSE.APACHE
|   |       |                   |       LICENSE.BSD
|   |       |                   |       
|   |       |                   +---pkg_resources
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---platformdirs
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---pygments
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---pyproject_hooks
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---requests
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---resolvelib
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---rich
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---tomli
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---tomli_w
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   +---truststore
|   |       |                   |       LICENSE
|   |       |                   |       
|   |       |                   \---urllib3
|   |       |                           LICENSE.txt
|   |       |                           
|   |       +---pydantic
|   |       |   |   aliases.py
|   |       |   |   alias_generators.py
|   |       |   |   annotated_handlers.py
|   |       |   |   class_validators.py
|   |       |   |   color.py
|   |       |   |   config.py
|   |       |   |   dataclasses.py
|   |       |   |   datetime_parse.py
|   |       |   |   decorator.py
|   |       |   |   env_settings.py
|   |       |   |   errors.py
|   |       |   |   error_wrappers.py
|   |       |   |   fields.py
|   |       |   |   functional_serializers.py
|   |       |   |   functional_validators.py
|   |       |   |   generics.py
|   |       |   |   json.py
|   |       |   |   json_schema.py
|   |       |   |   main.py
|   |       |   |   mypy.py
|   |       |   |   networks.py
|   |       |   |   parse.py
|   |       |   |   py.typed
|   |       |   |   root_model.py
|   |       |   |   schema.py
|   |       |   |   tools.py
|   |       |   |   types.py
|   |       |   |   type_adapter.py
|   |       |   |   typing.py
|   |       |   |   utils.py
|   |       |   |   validate_call_decorator.py
|   |       |   |   validators.py
|   |       |   |   version.py
|   |       |   |   warnings.py
|   |       |   |   _migration.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---deprecated
|   |       |   |   |   class_validators.py
|   |       |   |   |   config.py
|   |       |   |   |   copy_internals.py
|   |       |   |   |   decorator.py
|   |       |   |   |   json.py
|   |       |   |   |   parse.py
|   |       |   |   |   tools.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           class_validators.cpython-314.pyc
|   |       |   |           config.cpython-314.pyc
|   |       |   |           copy_internals.cpython-314.pyc
|   |       |   |           decorator.cpython-314.pyc
|   |       |   |           json.cpython-314.pyc
|   |       |   |           parse.cpython-314.pyc
|   |       |   |           tools.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---experimental
|   |       |   |   |   arguments_schema.py
|   |       |   |   |   missing_sentinel.py
|   |       |   |   |   pipeline.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           arguments_schema.cpython-314.pyc
|   |       |   |           missing_sentinel.cpython-314.pyc
|   |       |   |           pipeline.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---plugin
|   |       |   |   |   _loader.py
|   |       |   |   |   _schema_validator.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _loader.cpython-314.pyc
|   |       |   |           _schema_validator.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---v1
|   |       |   |   |   annotated_types.py
|   |       |   |   |   class_validators.py
|   |       |   |   |   color.py
|   |       |   |   |   config.py
|   |       |   |   |   dataclasses.py
|   |       |   |   |   datetime_parse.py
|   |       |   |   |   decorator.py
|   |       |   |   |   env_settings.py
|   |       |   |   |   errors.py
|   |       |   |   |   error_wrappers.py
|   |       |   |   |   fields.py
|   |       |   |   |   generics.py
|   |       |   |   |   json.py
|   |       |   |   |   main.py
|   |       |   |   |   mypy.py
|   |       |   |   |   networks.py
|   |       |   |   |   parse.py
|   |       |   |   |   py.typed
|   |       |   |   |   schema.py
|   |       |   |   |   tools.py
|   |       |   |   |   types.py
|   |       |   |   |   typing.py
|   |       |   |   |   utils.py
|   |       |   |   |   validators.py
|   |       |   |   |   version.py
|   |       |   |   |   _hypothesis_plugin.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           annotated_types.cpython-314.pyc
|   |       |   |           class_validators.cpython-314.pyc
|   |       |   |           color.cpython-314.pyc
|   |       |   |           config.cpython-314.pyc
|   |       |   |           dataclasses.cpython-314.pyc
|   |       |   |           datetime_parse.cpython-314.pyc
|   |       |   |           decorator.cpython-314.pyc
|   |       |   |           env_settings.cpython-314.pyc
|   |       |   |           errors.cpython-314.pyc
|   |       |   |           error_wrappers.cpython-314.pyc
|   |       |   |           fields.cpython-314.pyc
|   |       |   |           generics.cpython-314.pyc
|   |       |   |           json.cpython-314.pyc
|   |       |   |           main.cpython-314.pyc
|   |       |   |           mypy.cpython-314.pyc
|   |       |   |           networks.cpython-314.pyc
|   |       |   |           parse.cpython-314.pyc
|   |       |   |           schema.cpython-314.pyc
|   |       |   |           tools.cpython-314.pyc
|   |       |   |           types.cpython-314.pyc
|   |       |   |           typing.cpython-314.pyc
|   |       |   |           utils.cpython-314.pyc
|   |       |   |           validators.cpython-314.pyc
|   |       |   |           version.cpython-314.pyc
|   |       |   |           _hypothesis_plugin.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---_internal
|   |       |   |   |   _config.py
|   |       |   |   |   _core_metadata.py
|   |       |   |   |   _core_utils.py
|   |       |   |   |   _dataclasses.py
|   |       |   |   |   _decorators.py
|   |       |   |   |   _decorators_v1.py
|   |       |   |   |   _discriminated_union.py
|   |       |   |   |   _docs_extraction.py
|   |       |   |   |   _fields.py
|   |       |   |   |   _forward_ref.py
|   |       |   |   |   _generate_schema.py
|   |       |   |   |   _generics.py
|   |       |   |   |   _git.py
|   |       |   |   |   _import_utils.py
|   |       |   |   |   _internal_dataclass.py
|   |       |   |   |   _known_annotated_metadata.py
|   |       |   |   |   _mock_val_ser.py
|   |       |   |   |   _model_construction.py
|   |       |   |   |   _namespace_utils.py
|   |       |   |   |   _repr.py
|   |       |   |   |   _schema_gather.py
|   |       |   |   |   _schema_generation_shared.py
|   |       |   |   |   _serializers.py
|   |       |   |   |   _signature.py
|   |       |   |   |   _typing_extra.py
|   |       |   |   |   _utils.py
|   |       |   |   |   _validate_call.py
|   |       |   |   |   _validators.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           _config.cpython-314.pyc
|   |       |   |           _core_metadata.cpython-314.pyc
|   |       |   |           _core_utils.cpython-314.pyc
|   |       |   |           _dataclasses.cpython-314.pyc
|   |       |   |           _decorators.cpython-314.pyc
|   |       |   |           _decorators_v1.cpython-314.pyc
|   |       |   |           _discriminated_union.cpython-314.pyc
|   |       |   |           _docs_extraction.cpython-314.pyc
|   |       |   |           _fields.cpython-314.pyc
|   |       |   |           _forward_ref.cpython-314.pyc
|   |       |   |           _generate_schema.cpython-314.pyc
|   |       |   |           _generics.cpython-314.pyc
|   |       |   |           _git.cpython-314.pyc
|   |       |   |           _import_utils.cpython-314.pyc
|   |       |   |           _internal_dataclass.cpython-314.pyc
|   |       |   |           _known_annotated_metadata.cpython-314.pyc
|   |       |   |           _mock_val_ser.cpython-314.pyc
|   |       |   |           _model_construction.cpython-314.pyc
|   |       |   |           _namespace_utils.cpython-314.pyc
|   |       |   |           _repr.cpython-314.pyc
|   |       |   |           _schema_gather.cpython-314.pyc
|   |       |   |           _schema_generation_shared.cpython-314.pyc
|   |       |   |           _serializers.cpython-314.pyc
|   |       |   |           _signature.cpython-314.pyc
|   |       |   |           _typing_extra.cpython-314.pyc
|   |       |   |           _utils.cpython-314.pyc
|   |       |   |           _validate_call.cpython-314.pyc
|   |       |   |           _validators.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           aliases.cpython-314.pyc
|   |       |           alias_generators.cpython-314.pyc
|   |       |           annotated_handlers.cpython-314.pyc
|   |       |           class_validators.cpython-314.pyc
|   |       |           color.cpython-314.pyc
|   |       |           config.cpython-314.pyc
|   |       |           dataclasses.cpython-314.pyc
|   |       |           datetime_parse.cpython-314.pyc
|   |       |           decorator.cpython-314.pyc
|   |       |           env_settings.cpython-314.pyc
|   |       |           errors.cpython-314.pyc
|   |       |           error_wrappers.cpython-314.pyc
|   |       |           fields.cpython-314.pyc
|   |       |           functional_serializers.cpython-314.pyc
|   |       |           functional_validators.cpython-314.pyc
|   |       |           generics.cpython-314.pyc
|   |       |           json.cpython-314.pyc
|   |       |           json_schema.cpython-314.pyc
|   |       |           main.cpython-314.pyc
|   |       |           mypy.cpython-314.pyc
|   |       |           networks.cpython-314.pyc
|   |       |           parse.cpython-314.pyc
|   |       |           root_model.cpython-314.pyc
|   |       |           schema.cpython-314.pyc
|   |       |           tools.cpython-314.pyc
|   |       |           types.cpython-314.pyc
|   |       |           type_adapter.cpython-314.pyc
|   |       |           typing.cpython-314.pyc
|   |       |           utils.cpython-314.pyc
|   |       |           validate_call_decorator.cpython-314.pyc
|   |       |           validators.cpython-314.pyc
|   |       |           version.cpython-314.pyc
|   |       |           warnings.cpython-314.pyc
|   |       |           _migration.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---pydantic-2.12.5.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---pydantic_core
|   |       |   |   core_schema.py
|   |       |   |   py.typed
|   |       |   |   _pydantic_core.cp314-win_amd64.pyd
|   |       |   |   _pydantic_core.pyi
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           core_schema.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---pydantic_core-2.41.5.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---starlette
|   |       |   |   applications.py
|   |       |   |   authentication.py
|   |       |   |   background.py
|   |       |   |   concurrency.py
|   |       |   |   config.py
|   |       |   |   convertors.py
|   |       |   |   datastructures.py
|   |       |   |   endpoints.py
|   |       |   |   exceptions.py
|   |       |   |   formparsers.py
|   |       |   |   py.typed
|   |       |   |   requests.py
|   |       |   |   responses.py
|   |       |   |   routing.py
|   |       |   |   schemas.py
|   |       |   |   staticfiles.py
|   |       |   |   status.py
|   |       |   |   templating.py
|   |       |   |   testclient.py
|   |       |   |   types.py
|   |       |   |   websockets.py
|   |       |   |   _compat.py
|   |       |   |   _exception_handler.py
|   |       |   |   _utils.py
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   +---middleware
|   |       |   |   |   authentication.py
|   |       |   |   |   base.py
|   |       |   |   |   cors.py
|   |       |   |   |   errors.py
|   |       |   |   |   exceptions.py
|   |       |   |   |   gzip.py
|   |       |   |   |   httpsredirect.py
|   |       |   |   |   sessions.py
|   |       |   |   |   trustedhost.py
|   |       |   |   |   wsgi.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           authentication.cpython-314.pyc
|   |       |   |           base.cpython-314.pyc
|   |       |   |           cors.cpython-314.pyc
|   |       |   |           errors.cpython-314.pyc
|   |       |   |           exceptions.cpython-314.pyc
|   |       |   |           gzip.cpython-314.pyc
|   |       |   |           httpsredirect.cpython-314.pyc
|   |       |   |           sessions.cpython-314.pyc
|   |       |   |           trustedhost.cpython-314.pyc
|   |       |   |           wsgi.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           applications.cpython-314.pyc
|   |       |           authentication.cpython-314.pyc
|   |       |           background.cpython-314.pyc
|   |       |           concurrency.cpython-314.pyc
|   |       |           config.cpython-314.pyc
|   |       |           convertors.cpython-314.pyc
|   |       |           datastructures.cpython-314.pyc
|   |       |           endpoints.cpython-314.pyc
|   |       |           exceptions.cpython-314.pyc
|   |       |           formparsers.cpython-314.pyc
|   |       |           requests.cpython-314.pyc
|   |       |           responses.cpython-314.pyc
|   |       |           routing.cpython-314.pyc
|   |       |           schemas.cpython-314.pyc
|   |       |           staticfiles.cpython-314.pyc
|   |       |           status.cpython-314.pyc
|   |       |           templating.cpython-314.pyc
|   |       |           testclient.cpython-314.pyc
|   |       |           types.cpython-314.pyc
|   |       |           websockets.cpython-314.pyc
|   |       |           _compat.cpython-314.pyc
|   |       |           _exception_handler.cpython-314.pyc
|   |       |           _utils.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---starlette-0.41.3.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.md
|   |       |           
|   |       +---typing_extensions-4.15.0.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---typing_inspection
|   |       |   |   introspection.py
|   |       |   |   py.typed
|   |       |   |   typing_objects.py
|   |       |   |   typing_objects.pyi
|   |       |   |   __init__.py
|   |       |   |   
|   |       |   \---__pycache__
|   |       |           introspection.cpython-314.pyc
|   |       |           typing_objects.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           
|   |       +---typing_inspection-0.4.2.dist-info
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE
|   |       |           
|   |       +---uvicorn
|   |       |   |   config.py
|   |       |   |   importer.py
|   |       |   |   logging.py
|   |       |   |   main.py
|   |       |   |   py.typed
|   |       |   |   server.py
|   |       |   |   workers.py
|   |       |   |   _subprocess.py
|   |       |   |   _types.py
|   |       |   |   __init__.py
|   |       |   |   __main__.py
|   |       |   |   
|   |       |   +---lifespan
|   |       |   |   |   off.py
|   |       |   |   |   on.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           off.cpython-314.pyc
|   |       |   |           on.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---loops
|   |       |   |   |   asyncio.py
|   |       |   |   |   auto.py
|   |       |   |   |   uvloop.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           asyncio.cpython-314.pyc
|   |       |   |           auto.cpython-314.pyc
|   |       |   |           uvloop.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---middleware
|   |       |   |   |   asgi2.py
|   |       |   |   |   message_logger.py
|   |       |   |   |   proxy_headers.py
|   |       |   |   |   wsgi.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           asgi2.cpython-314.pyc
|   |       |   |           message_logger.cpython-314.pyc
|   |       |   |           proxy_headers.cpython-314.pyc
|   |       |   |           wsgi.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---protocols
|   |       |   |   |   utils.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   +---http
|   |       |   |   |   |   auto.py
|   |       |   |   |   |   flow_control.py
|   |       |   |   |   |   h11_impl.py
|   |       |   |   |   |   httptools_impl.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           auto.cpython-314.pyc
|   |       |   |   |           flow_control.cpython-314.pyc
|   |       |   |   |           h11_impl.cpython-314.pyc
|   |       |   |   |           httptools_impl.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   +---websockets
|   |       |   |   |   |   auto.py
|   |       |   |   |   |   websockets_impl.py
|   |       |   |   |   |   wsproto_impl.py
|   |       |   |   |   |   __init__.py
|   |       |   |   |   |   
|   |       |   |   |   \---__pycache__
|   |       |   |   |           auto.cpython-314.pyc
|   |       |   |   |           websockets_impl.cpython-314.pyc
|   |       |   |   |           wsproto_impl.cpython-314.pyc
|   |       |   |   |           __init__.cpython-314.pyc
|   |       |   |   |           
|   |       |   |   \---__pycache__
|   |       |   |           utils.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   +---supervisors
|   |       |   |   |   basereload.py
|   |       |   |   |   multiprocess.py
|   |       |   |   |   statreload.py
|   |       |   |   |   watchfilesreload.py
|   |       |   |   |   watchgodreload.py
|   |       |   |   |   __init__.py
|   |       |   |   |   
|   |       |   |   \---__pycache__
|   |       |   |           basereload.cpython-314.pyc
|   |       |   |           multiprocess.cpython-314.pyc
|   |       |   |           statreload.cpython-314.pyc
|   |       |   |           watchfilesreload.cpython-314.pyc
|   |       |   |           watchgodreload.cpython-314.pyc
|   |       |   |           __init__.cpython-314.pyc
|   |       |   |           
|   |       |   \---__pycache__
|   |       |           config.cpython-314.pyc
|   |       |           importer.cpython-314.pyc
|   |       |           logging.cpython-314.pyc
|   |       |           main.cpython-314.pyc
|   |       |           server.cpython-314.pyc
|   |       |           workers.cpython-314.pyc
|   |       |           _subprocess.cpython-314.pyc
|   |       |           _types.cpython-314.pyc
|   |       |           __init__.cpython-314.pyc
|   |       |           __main__.cpython-314.pyc
|   |       |           
|   |       +---uvicorn-0.32.1.dist-info
|   |       |   |   entry_points.txt
|   |       |   |   INSTALLER
|   |       |   |   METADATA
|   |       |   |   RECORD
|   |       |   |   REQUESTED
|   |       |   |   WHEEL
|   |       |   |   
|   |       |   \---licenses
|   |       |           LICENSE.md
|   |       |           
|   |       \---__pycache__
|   |               typing_extensions.cpython-314.pyc
|   |               
|   \---Scripts
|           activate
|           activate.bat
|           activate.fish
|           Activate.ps1
|           deactivate.bat
|           fastapi.exe
|           pip.exe
|           pip3.14.exe
|           pip3.exe
|           python.exe
|           pythonw.exe
|           uvicorn.exe
|           
+---APP
|   |   app.py
|   |   phase6_runner.py
|   |   requirements.txt
|   |   
|   \---__pycache__
|           app.cpython-314.pyc
|           phase6_runner.cpython-314.pyc
|           
+---ARCHIVE
|   +---checkpoints
|   |   |   PHASE6_SYSTEM_SNAPSHOT_2025-12-29_0943.md
|   |   |   PHASE_4_RUNTIME_READY.md
|   |   |   _repo_tree.txt
|   |   |   
|   |   \---PHASE6_LOCK_20251228_114844
|   |       |   bid_decision_v1.md
|   |       |   execution_risk_v1.json
|   |       |   executive_risk_summary_v1.md
|   |       |   phase6_build_manifest_v1.json
|   |       |   pricing_risk_v1.json
|   |       |   risk_scorecard_v1.json
|   |       |   
|   |       \---PHASE6
|   |               INPUT_CONTRACT.md
|   |               OUTPUT_TARGETS.md
|   |               PHASE6_LOCK.md
|   |               PHASE6_SCOPE.md
|   |               RISK_SCORING_PHILOSOPHY.md
|   |               SCORING_CONFIG_v1.json
|   |               
|   \---legacy_inputs
|       |   QuestionsBundle-Water-PIT-Inside.json
|       |   Scope Artifact - Inside Set (Indoor Meter) Questions v1.0.1 - Question ID correction (LOCKED).docx
|       |   Scope Artifact - Water PIT (Outside Meter) Questions (LOCKED).docx
|       |   
|       +---LOCKED_WATER_CORE_A1_B2A_v1.0
|       |       AnswerTokenRegistry-Core-A1-B2A-v1.0.json
|       |       LOCK_NOTES.md
|       |       QuestionsBundle-Water-Core-A1-B2A-v1.0.json
|       |       SMUS_AMI_Scope_Methodology_Core_v1.0.md
|       |       
|       +---LOCKED_WATER_CORE_B1_B9_v1.0
|       |       AnswerTokenRegistry-Core-B1-B9-v1.0.json
|       |       LOCK_NOTES_B1_B9_v1.0.md
|       |       QuestionsBundle-Water-Core-B1-B9-v1.0.json
|       |       SMUS_AMI_Scope_Methodology_Core_B1_B9_v1.0.md
|       |       
|       +---LOCKED_WATER_CORE_C1_C9_v1.0
|       |       AnswerTokenRegistry-Core-C1-C9-v1.0.json
|       |       QuestionsBundle-Water-Core-C1-C9-v1.0.json
|       |       SMUS_AMI_Scope_Methodology_Core_C1_C9_v1.0.md
|       |       
|       +---LOCKED_WATER_CORE_D1_D6_v1.0
|       |       AnswerTokenRegistry-Core-D1-D6-v1.0.json
|       |       LOCK_NOTES.md
|       |       QuestionsBundle-Water-Core-D1-D6-v1.0.json
|       |       SMUS_AMI_Scope_Methodology_Core_v1.0.md
|       |       
|       \---Master Combined
+---DOMAINS
|   +---ELECTRIC_AMI
|   +---GAS_AMI
|   \---WATER_AMI
|       +---methodology
|       +---questions
|       |       core.json
|       |       enrichment_map_v1.1.json
|       |       inside_extensions.json
|       |       pit_extensions.json
|       |       runtime_bundle_v1.1.json
|       |       
|       \---tokens
+---ENGINE
|   +---knowledge
|   +---methodology
|   \---schema
+---ENRICHMENT
|       enrichment_map_v1.1.json
|       
+---INGESTION
|   +---auto_answering
|   +---rfp_parsers
|   \---risk_extraction
+---LOCK_REPORTS
|       UNIVERSE_AUDIT_20251228_093724.txt
|       
+---MASTER_SPEC
|   +---CURRENT
|   |       MASTER_UNIVERSE_SPEC_v1.1.md
|   |       
|   \---DEPRECATED
|           MASTER_UNIVERSE_SPEC_v0.9.md
|           MASTER_UNIVERSE_SPEC_v1.0.md
|           
+---OUTPUT
|       bid_decision_v1.md
|       execution_risk_v1.json
|       executive_risk_summary_v1.md
|       gaps_v0.md
|       phase6_build_manifest_v1.json
|       pricing_risk_v1.json
|       risk_scorecard_v1.json
|       risk_summary_v1.md
|       scope_v0.md
|       validation_v0.json
|       
+---OUTPUTS
|   +---assumptions
|   +---risk_summaries
|   +---runs
|   |   +---20251228_221956_996c4774
|   |   |       bid_decision_v1.md
|   |   |       execution_risk_v1.json
|   |   |       executive_risk_summary_v1.md
|   |   |       phase6_build_manifest_v1.json
|   |   |       pricing_risk_v1.json
|   |   |       risk_scorecard_v1.json
|   |   |       stdout.txt
|   |   |       
|   |   \---20251229_152059_ab1c22a3
|   |           bid_decision_v1.md
|   |           execution_risk_v1.json
|   |           executive_risk_summary_v1.md
|   |           phase6_build_manifest_v1.json
|   |           pricing_risk_v1.json
|   |           risk_scorecard_v1.json
|   |           stderr.txt
|   |           stdout.txt
|   |           
|   \---scope_generation
+---PHASE6
|       INPUT_CONTRACT.md
|       NEXT_SESSION_PROMPT.md
|       OUTPUT_TARGETS.md
|       PHASE6_LOCK.md
|       PHASE6_SCOPE.md
|       RISK_SCORING_PHILOSOPHY.md
|       SCORING_CONFIG_v1.json
|       
\---RUNTIME
    |   build_phase6_bid_decision.ps1
    |   build_phase6_execution_risk.ps1
    |   build_phase6_executive_summary.ps1
    |   build_phase6_manifest.ps1
    |   build_phase6_pricing_risk.ps1
    |   build_phase6_risk_scorecard.ps1
    |   build_water_ami.ps1
    |   run_full_engine.ps1
    |   
    \---answers
            sample_answers_v1.json
            

\\\


---

## 12. Execution Wiring (Explicit)

### 12.1 Phase 6 — Deterministic Engine Run (Primary Path)

**Preferred execution path (platform-agnostic):**
- Python runner executes Phase 6 logic directly.
- Outputs written to OUTPUT/.

Entry points:
- APP/phase6_runner.py
- Consumes:
  - PHASE6/*.md (control + philosophy)
  - PHASE6/SCORING_CONFIG_v1.json
  - ENRICHMENT/enrichment_map_v1.1.json
  - OUTPUT/risk_summary_v1.md (Phase 5 output)

Produces:
- risk_scorecard_v1.json
- pricing_risk_v1.json
- execution_risk_v1.json
- bid_decision_v1.md
- executive_risk_summary_v1.md
- phase6_build_manifest_v1.json

---

### 12.2 Legacy / Utility Execution (Windows)

PowerShell scripts remain for:
- Validation
- Debugging
- Transitional support

Location:
- RUNTIME/build_phase6_*.ps1

These should not be relied on for production container runs.

---

### 12.3 FastAPI Layer (Local / Container)

Purpose:
- HTTP wrapper around deterministic Phase 6 execution
- No business logic
- No scoring logic

Location:
- APP/app.py

Endpoints:
- POST /run → triggers Phase 6 execution
- GET /runs/{id}/output/{file} → retrieves artifacts

---

### 12.4 Docker Execution Path

Dockerfile copies:
- APP/
- RUNTIME/
- PHASE6/
- ENRICHMENT/
- OUTPUT/

Container runs:
- FastAPI via Uvicorn
- Python-based execution only (no PowerShell dependency)

Result:
- Identical artifacts to local execution
- Suitable for future deployment (smartmeterus.com)

---

### 12.5 Non-Goals (Confirmed)

- PowerShell is NOT required in containers
- Docker is NOT authoritative for logic
- FastAPI does NOT contain business rules
- Canonical questions are NEVER modified at runtime


---

## 13. Verified Runtime Endpoints (Observed Working)

### Local FastAPI (Windows)
- Base URL: http://127.0.0.1:8000
- Swagger Docs: http://127.0.0.1:8000/docs
- OpenAPI Spec: http://127.0.0.1:8000/openapi.json
- Engine Execution: POST http://127.0.0.1:8000/run
- Run Artifact Fetch: GET http://127.0.0.1:8000/runs/{run_id}/output/{filename}

Notes:
- GET /favicon.ico may return 404 (expected, non-impacting).
- Outputs are written to OUTPUT/ and OUTPUTS/runs/{run_id}/ during local execution.

---

### Docker Runtime (Containerized)
- Host-mapped URL: http://127.0.0.1:8000  (via -p 8000:8000)
- Swagger Docs: http://127.0.0.1:8000/docs
- Engine Execution: POST http://127.0.0.1:8000/run

Notes:
- Container runtime executes Python-based Phase 6 logic only.
- No PowerShell dependency exists inside the container.
- Output artifacts match local deterministic outputs.

---

## 14. Runtime Dependency Boundary (Critical)

The following distinction is explicit and intentional:

### Development Environment
- Personal workstation
- Local filesystem used for outputs
- PowerShell + Python + Docker available
- Suitable for development and validation only

### Production Intent (Future State)
- No dependency on developer workstation
- API runs in hosted container environment
- Canonical knowledge baked into container image or mounted read-only
- RFP uploads and run outputs stored in cloud object storage
- Personal machine is NOT part of runtime execution

This boundary is mandatory for any public or multi-user deployment.


---

## 15. Roadmap and Next Milestones (Handoff Anchor)

A top-level project roadmap exists at:
- ROADMAP.md

Immediate focus:
1) **Local Product Mode** (prove repeatable operation)
2) **Phase 7-lite rails** (schemas + run ledger, no DB required)
3) **Reverse Mode ingestion** (RFP/addendums -> gaps + risk)
4) **Helper context layer** (separate from canonical universe)

Critical constraint:
- Phase 6 outputs and schemas remain **LOCKED**. Phase 7 adds adjacent artifacts only.

---

## Post-Phase-6 Structural Additions (Non-Breaking)

After Phase 6 was locked, validated, and tagged, the following folders were
added to the repository strictly as forward-looking scaffolding. These
additions do NOT modify, execute, or interfere with any Phase 6 logic,
runtime behavior, scoring, or output contracts.

The Phase 6 engine remains deterministic and unchanged.

### Added Folders

- PHASE7/
  Reserved for future development related to:
  - Knowledge-base ingestion
  - RFP parsing and normalization
  - Bid intelligence and comparative analytics

- ENGINE/schema/phase7/
  Placeholder schemas for structured knowledge storage.
  Not referenced by any Phase 6 runtime or scoring components.

No Phase 6 files were edited as part of this structural preparation.

---

