---
# qou-myk3
title: 'Corpus audits rglob into .claude/worktrees: 40 of 41 scanners lack the exclusion; counts inflate ~2x when an agent worktree exists'
status: todo
type: bug
priority: normal
created_at: 2026-08-22T12:38:06Z
updated_at: 2026-09-08T08:40:36Z
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


## 2026-09-08 — re-measured: the population GREW faster than the fix. 40 lacking -> 78

Pulled off the `qou-bstl` completion-candidate queue, flagged by
`14f27bb4d22` ("f64_into_mpmath_audit was scanning agent worktrees"). That
commit fixed **one** scanner, which this bean already says in its own Scope
section — so it is a false positive of the partial-completion class and the
bean stays `todo`.

The reason to record rather than just re-file it: the naive read of "8 more
scanners got the exclusion since" is *progress*, and the measurement says the
opposite.

Re-run with this bean's own methodology — files under `computations/` +
`scripts/` containing `rglob("*.py")`, split on whether the file mentions
`.claude` at all:

| | 2026-08-22 | 2026-09-08 |
|---|---|---|
| scanners matching `rglob("*.py")` | 41 | **87** |
| with the exclusion | 1 | **9** |
| **lacking it** | 40 | **78** |

So the exclusion spread to 8 more scanners in 17 days while the scanner
population more than doubled. The absolute gap nearly doubled with it. This is
not a backlog being drained; it is a backlog being outrun, and the cause is
that new corpus scanners are written without the exclusion by default.

The nine correctly-scoped ones, for whoever picks this up — note they are
overwhelmingly recent `computations/audits/*` files, i.e. the convention IS
being learned, just not retrofitted:

    computations/audits/anchor_flip_straddle_audit.py
    computations/audits/cached_accessor_shape_audit.py
    computations/audits/consumer_control_arm_audit.py
    computations/audits/inherited_q0_pin_audit.py
    computations/audits/local_qint_shim_audit.py
    computations/audits/ylambda_threerow_frame_audit.py
    computations/f64_into_mpmath_audit.py
    computations/mpf_context_dps_audit.py
    computations/witness_upstream_declaration_audit.py

**Same caveat as the original count, and it still binds: 78 is a CANDIDATE
figure, not a work order.** `.claude` absent from a file's text does not mean
that file is mis-scoped — it may scope via a shared helper, via `git
ls-files`, or by rooting at a subdirectory that never contains `.claude`. Do
not bulk-edit off it.

**What this suggests is a different fix from the one the bean implies.**
Retrofitting 78 files one at a time loses to the growth rate. The shape that
would actually close it is a single shared helper — an `iter_repo_py()` in a
module the audits already import — so a new scanner gets the exclusion by
using the corpus's own walker rather than by remembering a rule. That is a
change to ~78 files' import lines rather than to their logic, and under the
2026-09-07 ask-first directive it is neither a precision fix nor
corpus-derived, so it is the owner's call, not an agent's. Recorded here
rather than started.
