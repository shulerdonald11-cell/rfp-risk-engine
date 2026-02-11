# SYSTEM SNAPSHOT — Phase 6 Locked + Phase 7-lite Rails + Phase 8 MVP Alignment
Generated: 2026-02-11 08:19:32 -06:00
Repo Root: C:\Users\shule\Documents\Shuler LLC\RFP_RISK_ENGINE

## Git
- HEAD: d3b15fd8f0f03fb09e701264cba085f0d686ad7a
- Last Commit: d3b15fd MVP: Answers->Enrichment->Phase6 in single run folder
- Tags: see tags_top15.txt
- Status: see git_status.txt

## Canonical vs Runtime
- Canonical baseline outputs live in: OUTPUT/ (locked baseline; do not overwrite)
- Runtime executions live in: OUTPUTS/runs/<run_id>/
- Phase 7 stores adjacent artifacts only (snapshots, ledgers, metadata). No Phase 6 mutation.

## MVP Reverse Flow (current)
answers_snapshot.json
  -> Phase 7 stub produces enrichment_map_run_v1.1.json
  -> Phase 6 runner produces phase6/* outputs under the same run folder

## Files captured in this snapshot
See hashes_sha256.tsv and ARTIFACTS/ folder.
