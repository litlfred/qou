---
# qou-myk3
title: 'Corpus audits rglob into .claude/worktrees: 40 of 41 scanners lack the exclusion; counts inflate ~2x when an agent worktree exists'
status: todo
type: bug
priority: normal
created_at: 2026-08-22T12:38:06Z
updated_at: 2026-08-22T12:38:38Z
---

## What

Agent worktrees live at `.claude/worktrees/<agent-id>/` and are a **full
second checkout of the repo** — gitignored (`.gitignore:120`), 0 tracked
files. Corpus scanners that walk `ROOT.rglob("*.py")` without excluding
`.claude` therefore see **every file twice**.

Measured 2026-08-22 in a container with one agent worktree present
(`agent-afca082fc401776c5`, on `claude/color-channel-weighting-audit-qcaqfm`,
4215 `.py` files):

    in-scope .py files:            7321
      of which under .claude/:     3648   (49.8%)
      real source:                 3673

`computations/f64_into_mpmath_audit.py` before vs after adding the
exclusion — an almost exact halving of every tier:

| tier | with worktree | correctly scoped |
|---|---|---|
| LAUNDERED | 16 files / 16 sites | **8 / 8** |
| F64_CAST | 246 files / 448 sites | **122 / 222** |
| NUMPY_ON_Q | 30 files / 120 ops | **15 / 60** |
| F64_IMPORT | 211 files | **105** |
| F64_DISPLAY | 2 files / 36 sites | **1 / 17** |

## Why this is worse than a wrong number

The inflation is **environment-dependent**. The same commit audits
differently depending on whether an agent worktree happens to be checked
out, so the counts are not reproducible across machines and **cannot
support a baseline or a ratchet**. A gate keyed on them would flip
red/green on worktree lifecycle, not on code.

## Evidence the corrected numbers are the intended ones

Bean `qou-840k` records "**222** float()-casts of q-derived constants
across 129 files". The worktree-excluded run reports **222 sites** —
an exact match on the site count (files 122 vs 129, plausibly fixes since
landed). So the recorded corpus figures were taken without a worktree
present, and the exclusion restores the intended scope rather than
changing it. Stated as evidence, not proof — I did not verify when that
measurement was taken.

## Scope

**Fixed here (measured):** `computations/f64_into_mpmath_audit.py` only.
Its sibling `witness_raw_float64_audit.py` is already correctly scoped
(0 worktree hits; `dirty_witnesses 1535` reproduces), so the family is
inconsistent rather than uniformly broken.

**Candidates, NOT a work order: 40 of 41 files that `rglob("*.py")`
under `computations/` + `scripts/` contain no `.claude` mention.** That
is a crude proxy — a scanner may scope correctly via a shared helper, via
`git ls-files`, or by rooting at a subdirectory that never contains
`.claude`. Each needs confirming individually before editing; do not bulk
-edit off this count. Sample of the candidate list:

    computations/audits/float64_leak_audit.py
    computations/audits/hardcoded_literal_audit.py
    computations/audits/q0_consistency_audit.py
    computations/audits/ghost_value_sweep.py
    computations/cal4_disguise_hunt.py
    computations/canonical_mass_status_guard.py
    ...

Worth checking first: any scanner whose output feeds a **baseline**, since
that is where an environment-dependent count does real damage.

## How it surfaced

Scoping `qou-v6vp` (the `char_fast` constant-function defect) on PR #5427.
Running `f64_into_mpmath_audit` to see whether that defect was already a
tracked class, I noticed its listing was dominated by
`.claude/worktrees/...` paths.
