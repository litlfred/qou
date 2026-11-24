---
# qou-l7cy
title: 'PR-Drain-1: Salvage/Rebase Late-Nov Targeted Hygiene, Precision Gates, Library & Policy PRs (9 PRs, #8560..#9159)'
status: in-progress
type: task
priority: high
created_at: 2026-11-23T20:55:51Z
updated_at: 2026-11-24T00:12:28Z
parent: qou-xip2
---

### Salvage, Rebase & Supersede Workflow (STRICT)
1. Fetch the target branch explicitly: `nice -n 15 git fetch origin <headRefName>` (NEVER bare `git fetch origin`, NEVER `lake build`).
2. Diff against `origin/main` (`git diff origin/main...origin/<headRefName> --stat`):
   - Check every claim against `docs/coordination/owner-rulings.md` (no retired `z_C`, no trefoil primary electron, no `L±` or virtual photons, no float64 in probes, zero fitting).
   - Verify Lean files with single-thread `lean -DautoImplicit=false -s 65536` (`LEAN_NUM_THREADS=1`, `nice -n 15`) and static vacuity/axiom guards (`0 sorryAx`, `0` self-assuming projections).
3. Port clean net-new value into a fresh consolidated PR onto `main`, wait until that consolidating PR is `MERGED`, and then close superseded legacy PRs with:
   `gh pr close <num> --repo litlfred/qou --comment "Consolidated onto main in #<new_pr> (<sha>); closing superseded PR while preserving branch <headRefName> intact."`
4. **CRITICAL BRANCH GUARD:** NEVER pass `--delete-branch` or `-d`! Preserve all remote and local branches intact.

## PR-Drain-1: Late-Nov Targeted Hygiene, Precision Gates, Library & Policy PRs (#8560..#9159) (`9` PRs)
- **`#9159`** (`claude/project-thread-ipc33x`, files=5, lean_mod=2, lean_new=0, py=0): Corpus-grep path 7 (block QA sidecar); fits_AME labelled as comparison
- **`#9157`** (`claude/library-ingest-helon-2026-11-22`, files=16, lean_mod=0, lean_new=0, py=0 | queue_overlap: `[9180, 9207]`): library: ingest Bilson-Thompson–Hackett–Kauffman 2009 (helon braided belts) — *15/16 files (library/arxiv-0903.1376v1/*) ALREADY on main via #9184; ONLY 1-line references.ts + bilson-thompson-hackett-kauffman2009.json delta remains!*
- **`#9105`** (`claude/precision-gate-reds-2026-11-22`, files=96, lean_mod=0, lean_new=0, py=34): Precision gates: fix the six reds on main at their producers (#9104)
- **`#9095`** (`claude/knots-particles-prior-art-2026-11-22`, files=100, lean_mod=0, lean_new=0, py=0 | queue_overlap: `[9180, 9207]`): Ch. 9 opener: braid-preon prior art; ingest five uploads — *7 sources already ingested in #9112; inspect remaining knotted-particles-history.md + Chester 2025 PDF delta.*
- **`#9045`** (`claude/merge-coordinator-memory-2026-11-22`, files=1, lean_mod=0, lean_new=0, py=0): merge-coordinator memory: rebase-merge 405 with no merge commit
- **`#8896`** (`claude/precision-muon-c3-retired-2026-11-15`, files=18, lean_mod=0, lean_new=0, py=9): Retire muon c₃ = −2.0097 in 8 probes, each paired with its own pin
- **`#8751`** (`claude/q0-anchor-refill-drain-2026-11-21`, files=20, lean_mod=0, lean_new=0, py=5): Drain the q0-anchor refill ratchet (30 → in progress)
- **`#8741`** (`claude/gg-internucleon-bond-2026-11-21`, files=1, lean_mod=0, lean_new=0, py=0): γγ inter-nucleon bond: which bond words does reading 3 admit in a nucleus? (qou-k54t)
- **`#8560`** (`claude/uic-scoping-kjik-banner-reland-2026-11-20`, files=100, lean_mod=0, lean_new=0, py=55): Re-land #7439's three items, then close the q-precision input ceiling (owner options 1 and 3)
