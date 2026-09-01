---
# qou-gq2p
title: '_habiro_coefficient_extract: 26 vacuous-green witnesses, unblocked by qou-wc8f'
status: todo
type: task
priority: normal
created_at: 2026-08-31T07:33:40Z
updated_at: 2026-08-31T07:34:13Z
---

## Status

**Unblocked.** This family was held by `qou-wc8f` — whether a fresh run of the
Habiro cone produced right or wrong numbers. That is settled (#6381, #6385):
the post-R3 convention-D values are correct, the pre-R3 committed ones were the
stale artifact, and the `qou-wc8f` disposition was reversed accordingly.

## Measured on `main` `e8f5a64a81`

    habiro-coefficients-* witnesses (non-deprecated)   30
    still in the vacuous-green baseline               26

All 26 are written by one producer, `computations/_habiro_coefficient_extract.py`
(`invocation.reproduce`: `python3 -u computations/_habiro_coefficient_extract.py`,
no arguments). This is the **largest remaining single-owner family** in the
`qou-srvu` backlog — see `qou-5ax1`, where it is the second row and, now that
`canonical_isotope_witness` is a LEAVE-on-the-merits, the largest *open* one.

## Why it is one unit of work, not 26

Every witness in the family is all-or-nothing vacuous-green (26 of 26 in the
baseline), because they come off one batch run of one producer. One fix drains
all of them. That is the whole point of `qou-5ax1`'s finding that the backlog is
8 producer families rather than 423 independent problems.

## What the assertion probably is — NOT yet established

The witnesses carry `integral=True` and a `reconstruction_matches` flag (the
shared loader `habiro_coefficients_atomic.load_a_m` **refuses** a witness whose
`reconstruction_matches` is false, per bean `qou-s41x`). A reconstruction check
that the loader already trusts enough to refuse on is the obvious candidate for
promotion to a real assertion.

**Do not take that as a plan.** I have not read the producer's source, and the
whole lesson of `qou-5ax1` is that witness *shape* is evidence about the payload
and not about whether the producer computes anything falsifiable — the largest
family in that table turned out to be a read-many orchestrator whose every
available invariant is true by construction. Read `_habiro_coefficient_extract.py`
before writing an assertion.

## Two cautions carried from the arc that unblocked this

1. **The producer is the input to `topic2_mirror_pair_phi8_boundary_scan`.**
   Re-running it moves that scan's numbers — that is exactly the drift chased
   through `qou-wc8f`. The topic2 witness is now refreshed and asserted at the
   D-frame values (#6385), so a re-run should be a no-op there; **verify that it
   is** rather than assuming, and diff the topic2 witness alongside.

2. **`M_max_used` in the topic2 rows is this producer's Habiro depth.** If it
   moves on a re-run, the a_m depth changed and the downstream multiplicities
   will move with it. That is the signal that caught the R3 migration in the
   first place; treat any movement in it as a finding, not as noise.

## Cost

The 2026-08-25 batch that produced these ran 21:49:01 → 21:57:20 — **~8 minutes
for all 18 mirror-pair slugs**. Small. Log it per the long-compute discipline
anyway (`-u … | tee`), because the diff step is where this family's findings
have historically come from.
