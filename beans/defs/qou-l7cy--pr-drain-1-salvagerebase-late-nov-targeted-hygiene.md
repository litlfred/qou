---
# qou-l7cy
title: 'PR-Drain-1: Salvage/Rebase Late-Nov Targeted Hygiene, Precision Gates, Library & Policy PRs (9 PRs, #8560..#9159)'
status: in-progress
type: task
priority: high
created_at: 2026-11-23T20:55:51Z
updated_at: 2026-11-24T00:50:03Z
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


## 2026-11-23 — Worker 31 PR-Drain-1 Audit & Consolidated Salvage PR #9237 (`claude/backlog-drain-batch1-20261123`, head `3328685b1ae`)

Audited all 9 legacy PRs in `PR-Drain-1` against `origin/main` (`e330ab6aa04`):
- **0/9 PRs were already 100% landed on `origin/main`** prior to salvage, so **0 legacy PRs were closed prematurely** and **0 branches were deleted** (per Rule 3: wait until consolidating PR **#9237** merges to `main` before closing superseded PRs `#9159, #9157, #9045, #8741, #8896, #8751`).
- **Salvaged cleanly into PR #9237 (7 of 9 PRs — 6 in full, 1 standalone Lean+probe+audit subset):**
  1. **`#9159`** (`9c43cb9a797`, 100% ported): `.claude/agents/corpus-grepper.md`, `AGENTS.md` Path 7 (`<block>.qa.json`), `docs/coordination/owner-rulings.md` (3 rows), and `fits_AME` comparison-point labels in `QOU/Interactions/QIntegerMassFormula.lean` & `mass-theory/q-integer-mass-formula.lean` (`lean -DautoImplicit=false -s 65536 -j 1` exit 0 on both). Supersedes `#9159` once #9237 merges.
  2. **`#9157`** (`dd9498d6e10`, 100% of remaining 3-file delta ported): `library/arxiv-0903.1376v1/` + `library/INDEX.md` (13/16 files) were already byte-identical on `origin/main` via `#9184` (`dc8919ec7a3`); ported `folio/references/bilson-thompson-hackett-kauffman2009.json`, `folio/schema/references.ts`, and `references.bib` (`check-references-bib.ts` exit 0). Supersedes `#9157` once #9237 merges.
  3. **`#9045`** (`82561735a60`, 100% ported): `.claude/agent-memory/merge-coordinator/MEMORY.md` linear 118-commit rebase-merge 405 note (#8804). Supersedes `#9045` once #9237 merges.
  4. **`#8741`** (`84311a62c23`, 100% ported): `computations/probes/gg_internucleon_bond/preregistration.md` (`qou-k54t`, ruled photon `1 + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1^{-1}`). Supersedes `#8741` once #9237 merges.
  5. **`#8896`** (`60124c9b7b0` + `3328685b1ae`, 100% of remaining 16-file delta ported & upgraded): `qbeta_markov_trace_steps_4_5` `Q0_FLIP` fix was already on `origin/main`; ported all 8 `c_3 = -2.0097` probes + 8 witnesses and upgraded their pasted 15-digit literals (which tripped `witness_value_copy_audit.py`) to full-dps `qbeta.qbeta_utils.c3_muon_extracted()` / `c3_extracted_at_q(...)` (+15 guard digits, `witness_value_copy_audit` `0 NEW`). Supersedes `#8896` once #9237 merges.
  6. **`#9105` + `#8751`** (`9f4ec266a1e` + `3328685b1ae`): Ported all 86 non-contended producer/witness/manifest/deprecated-move/owner-rulings fixes from `#9105` (which completely subsumes `#8751` via `q0_anchor_manifest.json` + re-runs, omitting the 9 contended tree-measuring audit witnesses per `qou-v0t8`), plus fixed `finite_rieffel_tl3_metric_probe.py:395` and `qbeta_{mixed_,}chain_closed_form_probe.py`. Flips **5 of 6** blocking precision-gate reds to **GREEN** (`q0-anchor flip`, `q0-value drift`, `never-raises-dps`, `reference-literal`, `witness-value copy`) and cuts `q0-anchor refill` `NEW: 63 -> 21`. Supersedes `#8751` completely once #9237 merges; `#9105` retains only the 7 unfinished cloud Leray / `two-row` jobs (`qou-q0rf`).
  7. **`#8560` Parts B & D** (`3305739d688`): Salvaged standalone `QOU/Mass/LinkingWeightWedderburn.lean` (10 sorry-free theorems over generic `[Field R]`, `lean-direct` exit 0, `0` self-assuming candidates), `lw_cusp_pole_is_classical_probe.py` (11/11 exact checks), `exposed_witness_identification.py`, and `q50_digit_cap_classify.py`.
- **Documented Blockers / Gated Holdouts (2 PRs kept open untouched):**
  - **`#9095`** (`claude/knots-particles-prior-art-2026-11-22`, `DRAFT=true`): Explicitly marked in PR body *"This is a proposal; do not merge without the owner's go"*; overlaps `finkelstein2008.json` / `references.ts` in active `needs-owner-ok` sibling bean `qou-cvu9` and adds 5 `library/` PDFs (`arxiv-2501.03260v1`, `1507.06276v2`, `1711.09011v1`, `1803.02202v2`, `math-0103228v2`). Hold until owner approves Ch. 9 proposal + `qou-cvu9`.
  - **`#8560` Part C** (`claude/uic-scoping-kjik-banner-reland-2026-11-20`): 961-file branch (588 Python files patched `mpf(Q_50_DIGIT_STR) -> Q_MP`, 14 files diverged with `origin/main`, and 47 witness re-runs still unfinished in-flight when its cloud session paused). Requires a dedicated witness-refresh sweep rather than blind cherry-pick.
