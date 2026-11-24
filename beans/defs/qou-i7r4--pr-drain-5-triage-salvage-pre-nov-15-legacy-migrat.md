---
# qou-i7r4
title: 'PR-Drain-5: Triage & Salvage Pre-Nov-15 Legacy Migration, Molecular, TL/Hecke & Precision PRs (15 PRs, #5402..#7773)'
status: completed
type: task
priority: high
created_at: 2026-11-23T20:55:53Z
updated_at: 2026-11-24T09:44:28Z
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

## PR-Drain-5: Pre-Nov-15 Legacy Migration, Molecular, TL/Hecke & Precision Salvage PRs (#5402..#7817) (`15` PRs)
- **`#8161`** (`claude/round48-hygiene-and-gate-integrity`, files=30, lean_mod=0, lean_new=0, py=29): fix(qa): Round 48 hygiene & gate integrity (qou-myk3, qou-li9a, qou-ff4b, qou-ungx, qou-lz8f)
- **`#7817`** (`claude/pr-4928-convention-migration-fknylp`, files=14, lean_mod=0, lean_new=0, py=1): Convention C→D, five weeks on: the drain is finished, the accounting drifted, and the one open item is research
- **`#7773`** (`claude/molecular-word-corpus-lb-2026-10-12`, files=22, lean_mod=5, lean_new=0, py=6): Molecular word on the corpus L_b: factorisation, window depth, reading 3 (qou-a1hh)
- **`#7763`** (`claude/corpus-search-reachable-2026-10-12`, files=4, lean_mod=0, lean_new=0, py=0): corpus_search reachable from agent sessions: CLI wrapper + .mcp.json entry fix (qou-q261)
- **`#7590`** (`claude/rem-qstar-codata2022-figures-2026-10-10`, files=5, lean_mod=0, lean_new=0, py=1): rem-qstar: refresh figures to the CODATA-2022 muon pin
- **`#7481`** (`claude/two-row-count-eq-dimhlf-2026-09-27`, files=22, lean_mod=0, lean_new=10, py=7): The TL/Hecke arc after general-n semisimplicity: count↔formula, the carrier mismatch closed, WenzlTowerStep's zero consumers, and two drains — *TL-ideal carrier lemma ported (54802e02ba), vendor-mirror drain noted unported in qou-78bm (891264f2e0).*
- **`#7477`** (`claude/bk-crossing-coordination-woiqj3`, files=9, lean_mod=0, lean_new=0, py=1): precision-gate triage (1 laundered float64 fixed, 2 REDs triaged as non-defects) + two AGENTS.md figure corrections, one of which surfaced an unadjudicated duplicate of Neumann–Zagier 1985
- **`#7123`** (`claude/tl-gs-basis-citation-2026-09-07`, files=11, lean_mod=0, lean_new=1, py=3): probe(qou-cds1): the TL closure rule was in this corpus all along — a path-5 failure, corrected and then checked — *Tranche 1 ported in 35fab5703f; check remaining probe/doc files before closing.*
- **`#6361`** (`claude/qbeta-inversion-chain-audit-2026-08-31`, files=6, lean_mod=0, lean_new=1, py=2): qou-cds1: the negative (1³) weight is an INTERVAL fact — deflating two prior claims, one of them mine
- **`#6350`** (`claude/mkmpi-conditionality-measure-2026-08-31`, files=2, lean_mod=0, lean_new=0, py=1): L2 option 3: the "0/5 unconditional" headline rests on two claims — one stale, one conflated
- **`#6342`** (`claude/convention-migration-validation-77exfa`, files=11, lean_mod=0, lean_new=0, py=4): qou-cds1 entries 9 + 15 + 16: the |c_4| threshold, a clean pinning/non-D sweep, two gates that rejected their own output, and three retractions of my own claims
- **`#6307`** (`claude/symbolic-nf-bottleneck-2026-08-30`, files=2, lean_mod=0, lean_new=0, py=2): perf(hecke_core_symbolic): the symbolic NF fold was exponential — LaurentQ kernel takes A=2 from &gt;240 s to 0.024 s
- **`#6025`** (`claude/joint-tower-f64-declaration-2026-08-29`, files=12, lean_mod=0, lean_new=0, py=2): Add witness truncation and provenance stamping for joint-tower-sdp
- **`#5861`** (`claude/diagram-calculus-sphere-transition-ei9rdz`, files=4, lean_mod=0, lean_new=1, py=0): docs(glossary,lean): cite barrett1993 for spherical terminology; close the Barrett–Westbury referee hole
- **`#5402`** (`claude/jet-algebraic-dependence-2026-08-21`, files=9, lean_mod=0, lean_new=0, py=1): bean qou-j4mn: jet dependence is forced (holds), but "min degree 7" is convention-C-frame — under D it is 3

Batch 5 15-PR ledger committed at 75acb71b14a: 5 100%-superseded (#7763, #7481, #7477, #7123, #6025), 1 immediate clean merge candidate (#8161), 9 conflicting/draft.
