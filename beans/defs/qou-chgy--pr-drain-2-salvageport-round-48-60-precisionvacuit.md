---
# qou-chgy
title: 'PR-Drain-2: Salvage/Port Round 48-60 Precision/Vacuity/QA Infrastructure Fix PRs (4 PRs, #8290..#8350)'
status: todo
type: task
priority: high
created_at: 2026-11-23T20:55:52Z
updated_at: 2026-11-23T20:55:52Z
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

## PR-Drain-2: Round 48–60 Precision/Vacuity/QA Infrastructure Fix PRs (#8161..#8350) (`4` PRs)
- **`#8350`** (`claude/round57-trd0-9nnz-fixes`, files=9, lean_mod=1, lean_new=0, py=6): fix(qou-381n,qou-1ccx,qou-coyy,qou-v5sr,qou-58zw): sync JetOrderIndependence pivots, detect anonymous instance binders, gate reproducibility check, update closure table, drain float64 tolerances
- **`#8333`** (`claude/round56-trd0-9nnz-fixes`, files=8, lean_mod=0, lean_new=0, py=5): fix(qou-g5sp,qou-5t8y,qou-500d,qou-s63a,qou-zv2l): wire Bruhat modules, suffix-resolve q0 manifest, refine shape guard, add rename consumer guard, stamp canonical-ordering-dof
- **`#8307`** (`claude/round55-trd0-9nnz-fixes`, files=12, lean_mod=1, lean_new=0, py=9): fix(lean,probes,audits): devacuify MarkovAxiomsPrimitive, stamp comparison witnesses, filter two-row chi shapes, and fix audit/docstring paths (qou-tknj, qou-fl0a, qou-i2q5, qou-e9le, qou-ekga)
- **`#8290`** (`claude/round54-trd0-9nnz-fixes`, files=9, lean_mod=0, lean_new=0, py=6): fix(substrate,probes): raw-float64 locator shadow rules, nucleon docstrings, and mpf/assertion integrity (qou-i3wb, qou-7q56, qou-p77d, qou-hytc, qou-t0wm)
