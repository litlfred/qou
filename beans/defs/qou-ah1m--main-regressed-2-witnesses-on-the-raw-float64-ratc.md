---
# qou-ah1m
title: main regressed 2 witnesses on the raw-float64 ratchet (phase-transition-q-ideal-gas, seifert-volume-meson-n7-extension)
status: in-progress
pr: 8186
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:54:37Z
updated_at: 2026-10-04T15:21:25Z
parent: qou-9nnz
---

## Measured 2026-08-30 on `origin/main`

`computations/witness_raw_float64_audit.py` full sweep:

    NEW dirty witnesses : 0
    REGRESSED           : 2
         6 -> 11    computations/phase-transition-q-ideal-gas.witness.json
        51 -> 55    computations/seifert-volume-meson-n7-extension.witness.json

## Attribution — this is main's, not a branch's

Established without re-running on a clean checkout, which is unnecessary here:
the ratchet's verdict is a function of exactly three things — the two witnesses,
and `computations/raw-float64-baseline.json`. **None of the three is touched by
the branch that found it** (`claude/library-intake-6-uploads-2026-08-30`,
a library-intake PR), and the auditor itself is untouched too. So the verdict is
deterministic from main's own content.

Last commits on the two witnesses, both ancestors of `origin/main`
(`git merge-base --is-ancestor 13483c9b48 origin/main` -> true):

    13483c9b48  QOU(26f2): drain 2 - and the first one where the drained claim turned out false
    5a9bbf3350  QOU(26f2): drain 11 more - and two claims whose subjects have vanished

So a **draining** pass is what regressed them. Worth noting for its own sake: a
sweep whose purpose is to reduce raw float64 raised it on two files, and its own
commit messages record that it was already finding its claims turning out false.
Read those two commits before draining these — the fix may be a partial revert
rather than new work.

## Why it is not fixed in the PR that found it

Fixing it means re-running two producers and committing their witnesses, which
is unrelated to a library intake and would bury the finding where no reviewer
would look. The regenerated audit witnesses were deliberately **not** committed
either: their diffs carry an environment change (`sympy 1.12 -> 1.14.0`) and a
different invocation (`--strict`), so committing this container's copies would
replace main's environment stamp — exactly what `precision-gates.sh` warns
against for the drift-only cases it auto-reverts.

## Next

Diff each witness against the two named commits to see which fields gained raw
float64, then fix **at the producer** — never by widening
`raw-float64-baseline.json`. Baselines drain, never grow.



---

## Re-checked 2026-08-30 11:0x — the attribution stands, and the CHECK exposed a trap

I re-opened this because two ratchet runs in the same session disagreed:
**REGRESSED 0** on `claude/onepb-last3-float64-upstream-2026-08-30` (PR #6147)
and **REGRESSED 2** on `claude/library-intake-6-uploads-2026-08-30` (PR #6152).
One of the two had to be wrong, and if the float64 branch had silenced it by
widening the baseline that would have been a defect I opened and endorsed.

**Neither was wrong, and no baseline was widened.** #6147's baseline diff is a
pure drain -- `files_count` 1098 -> 1097, `fields_count` 35398 -> 35361,
`onepb-status-dashboard` 3 -> 1, and the `rho-f-volume-binding-gap` entry
removed outright. Both regressed witnesses carry the **same** baseline values
(6 and 51) on both branches.

## 🛑 TRAP — a REGRESSED count is a property of your MERGE BASE, not of your change

The two branches hold **different versions of the witnesses**:

    computations/phase-transition-q-ideal-gas.witness.json
      float64 branch f15e483118   ->  6 raw float leaves
      main / intake  becb7df60a   -> 11
    computations/seifert-volume-meson-n7-extension.witness.json
      float64 branch d3e2cdb7f3   -> 51
      main / intake  1cade4e51b   -> 55

`13483c9b488f7fe9c8abbf6fa9b2b376d8d3a035` and
`5a9bbf3350ffb169964cbea3086145b5e993b821` landed in main **after the float64
branch diverged**, so that branch's tree still has the pre-regression witnesses
and honestly reports 0. The intake branch is newer and honestly reports 2.

**So the attribution in this bean is correct as written** -- both commits are
ancestors of `origin/main`, neither branch touches those witnesses, the
baseline and the auditor are untouched, and the drift is main's.

**Two measurement traps recorded, both of which cost me a false alarm here:**

1. **A ratchet REGRESSED count is not comparable across branches.** Two branches
   of the same session can report 0 and 2 with neither being wrong. Always say
   which merge base a count was measured at. #6147's PR body says
   "REGRESSED: 0" and that is **correct for its base** -- do not "fix" it; a
   reviewer re-running on an updated base will see 2 and it will not be that
   PR's doing.
2. **A PR's GitHub `base.sha` is NOT necessarily on the branch.** Measured:
   `git merge-base --is-ancestor 0b423be625 <#6147 branch>` exits **1**. The real
   merge base is `c1412d907c`. So `--is-ancestor <commit> <PR base.sha>` answers
   a different question from `git log <branch>..main`, and I got opposite
   answers from the two before noticing. **Test ancestry against the BRANCH TIP,
   or use `git merge-base A B` explicitly** -- never against the API-reported
   base.sha.


## Round 51 Progress
- [x] PR https://github.com/litlfred/qou/pull/8186 (`fb4f6926d3f96fd99209ef3cb58128ff0ce2701b`): updated `computations/phase_transition_q_ideal_gas.py` and `computations/seifert_volume_meson_n7_extension.py` to use `set_compute_dps()`, explicit `_precision.fmt` serialization, and `mpf` `R_gas`, and regenerated both witnesses (0 raw float64).
