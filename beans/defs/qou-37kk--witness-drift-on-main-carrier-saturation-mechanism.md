---
# qou-37kk
title: 'Witness drift on main: carrier-saturation-mechanism flips 5 assertions pass->FAIL on a clean re-run'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T15:43:52Z
updated_at: 2026-10-04T15:14:25Z
parent: qou-5vkl
---

Found while draining the assertion_kwarg float64 casts (qou-l790). NOT caused by
that drain -- proved by construction, see below.

## The finding

`computations/deltalambda/carrier_saturation_mechanism_probe.py` re-run on a
CLEAN checkout of main (09e2be2b5), with NO source edit whatsoever, flips five
assertions from pass to FAIL and moves eight values by 5-35 %:

    anchor_kappaD_reproduced          True -> False    6.0427  -> 6.4161
    anchor_kappa4He_reproduced        True -> False   63.0515  -> 73.5943
    li6_amplification_reproduced      True -> False   79.8576  -> 107.8856
    carrier_flat_band_all_A           True -> False    1.2190  -> 1.8375
    erratum_T_me_S_matches_A_column   True -> False    0.4466  -> 0.4720
    lr_free_path_validated_at_4He     (no flip)      6.4e-06  -> 1.26e-48

`computations/dilog-archimedean-partB.witness.json` also drifts (2 values, no
flips).

So the committed witness does not reproduce, and the producer's own stated
result is now negative where the record says positive. Either an upstream it
consumes moved, or the producer changed without its witness being regenerated.
NOT diagnosed here -- this bean is the measurement.

## Why this is not the drain's doing

Three runs, and the isolation is the point:

  1. committed HEAD  vs  fresh run WITHOUT my edits  -> 5 flips, 8 moves
  2. committed HEAD  vs  fresh run WITH    my edits  -> 5 flips, 8 moves
  3. fresh WITHOUT   vs  fresh WITH                  -> 0 flips, 0 moves,
                                                        19 values gained digits,
                                                        110 byte-identical

Run 3 is the one that isolates the edit. Comparing against the committed
witness (runs 1 and 2) measures the edit AND the drift together, which is how
this nearly got attributed to the drain.

15 of the 17 witnesses in that batch are drift-free, so this is two producers,
not a corpus-wide problem.

CORRECTED (2026-08-26, prepare-merge for #5838). This read "12 of the 14",
low in both numerator and denominator by 3. Flagged by #5835 and then
re-measured here rather than taken on its word: the drain branch touches
17 producers and commits 15 witnesses
(`git diff --name-only origin/main...origin/claude/assertion-kwarg-float-drain-2026-08-26`),
and the 2 it does not commit are exactly this bean's two. Nothing downstream
moves -- the exclusions were always the right two -- but the bean is the
durable record and the next reader would take the tally at face value.

## What was done about it

The two drifted witnesses were RESTORED to HEAD and deliberately left OUT of
the drain PR. Committing them there would have landed five pass->FAIL flips
inside a precision-formatting change and attributed someone else's regression
to it. Their producers' sources ARE edited there, so both carry scriptHash
drift until this bean is worked -- the lesser of the two evils, and stated in
that PR rather than left to be discovered.


## DIAGNOSED 2026-08-26 — stale at BIRTH, not drift. And it hid a real regression.

NOT upstream drift, NOT non-determinism. The witness never matched the producer
it shipped with.

  commit cdb64587b CREATED both files (the producer did not exist before it --
  its parent hashes to e3b0c44298fc, the sha256 of empty).

    producer hash at cdb64587b : 501a19c13c1b
    witness records scriptHash : 0d25fcf48239   <- a DIFFERENT, unversioned draft

So the committed numbers come from a version of the producer that is not in git
at all, and cannot be reproduced. cdb64587b was a no-float64 sweep, and its own
message announces a stale witness -- but names `averaged-block-swap-binding`, a
DIFFERENT file. This one went unmentioned.

## What the stale witness concealed

The probe is a REGRESSION TEST against the published table in
docs/audits/2026-07-13-carrier-saturation-crossover-mechanism.md (rows 45-50).
Its `expected=` values are that table, hard-coded. On a clean re-run it fails
against all four, by large margins -- not marginal drift:

  anchor_kappaD_reproduced         6.0426    -> 6.4161      37x tolerance
  anchor_kappa4He_reproduced      63.05      -> 73.5943    105x tolerance
  li6_amplification_reproduced    79.86      -> 107.8856   560x tolerance
  erratum_T_me_S_matches_A_column  0.446636  -> 0.471969    25x tolerance
  carrier_flat_band_all_A          1.0       -> 1.8375       ~3x tolerance

dilog-archimedean-partB is BENIGN by comparison: same stale-at-birth cause, two
values moved, all 7 assertions still pass.

## The hypothesis I am NOT asserting

cdb64587b was a float64 fix, and fixing an f64 leak CHANGES numbers -- so the
audit table's values are plausibly the f64-contaminated ones and the new values
correct. That is a HYPOTHESIS, not a result. It cannot be tested by re-running
the old code: the version that produced them was never committed. Whoever takes
this decides whether the table is now wrong or the producer regressed; I am not
guessing, and I did NOT touch a tolerance or an expected value.

## Done

Both witnesses regenerated off main and committed with their TRUE verdicts,
including the five failures. Recording a real failure is the point; making it
pass by moving the goalposts would be laundering.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- **Round 93 (`litlfred/qou#8421`)**: Advanced in `feat/round93-strip-kindratio-kohnokz-resolvent-affinenorm-43c1` (Commit 1 `53341df5af4d7e77e4fbee34d9b0bead3b0b6187`, Commit 2 `2f40c0d2d071ec6bb42d20002fb53171245df01c`, probe sha256 `3d8255f15bbdfc2d9c41114f8ac21a1bec3996e0b1546ef080914210757c628c`).
