---
# qou-kwza
title: 'Branch gate state at HEAD, measured clean: 4 blocking reds, two of them main''s'
status: todo
type: task
created_at: 2026-08-24T00:30:00Z
updated_at: 2026-08-24T00:30:00Z
---

Measured on a **clean worktree at branch HEAD** (`bbf717a26`), not on the
working tree — the drain agent is concurrently writing witnesses, and a gate
run against that measures the drain, not the branch.

    PRECISION GATES   exit 1     RED: raw-float64 ratchet
    STALENESS GATES   exit 1     RED: scriptHash + upstream drift
                                      q0 constant staleness
                                      qou-mass vendor mirror

## Attribution — two of the four are documented as main's

`scripts/staleness-gates.sh`'s own preamble records that `origin/main` is red
on **scriptHash + upstream drift** and **q0 constant staleness**, and warns that
"A RED MEASURED ONCE ON MAIN MAY BE MID-ARC, NOT PERSISTENT". Neither is this
branch's to clear.

**`qou-mass vendor mirror` is actionable and deferred on purpose.** It needs
`python3 scripts/sync-qou-mass-vendor.py --apply`, and running it now would
capture the drain's intermediate state and immediately re-stale. **This is a
required pre-merge step**, to be done after the drain's last batch lands.

## The raw-float64 ratchet — measured, and it is a refresh, not a leak

    NEW dirty witnesses   1
    REGRESSED             3

and all four trace to this session's regenerations:

    NEW   20  habiro/habiro-coefficients-extended
    25 -> 42  beta-decay-matrix
     5 -> 20  bar-pairing-binding-observable-extension
     5 ->  7  markov/markov-substrate-realization

**None of it is float64 this session introduced.** Verified by diffing the
float64 field PATHS against the pre-session copy (`93e24e23d`):

    beta-decay-matrix        17 added, of which provenance fields: 0
    markov-substrate-real.    2 added, of which provenance fields: 0

Every added field is producer output — `crossing_coefficients.*`,
`decay_matrices.*`, `transfer_matrices.*`, `tr_M_at_q0`, `u_0`. The stamp added
`scriptFile` / `scriptHash` / `commitSha` / `computedAt` / `engine` /
`q0Anchor`, all strings. So these are stale witnesses refreshed to what their
producers actually emit — the same "corpus ceasing to lie" pattern as the
assertion flips, in the float64 axis.

Two of the four deserve separating:

- **`habiro-coefficients-extended` — all 20 fields are `timings_sec.*`**, wall
  clock measurements of the run itself. Serialising a timing at float64 is
  correct; it is the same category as `durationMs`, which nothing objects to.
  This is a carve-out candidate, not a drain target.
- **`bar-pairing-binding-observable-extension` 5 -> 20** is a direct consequence
  of `ee3ed1a09`: that producer used to TIME OUT at 900 s and now completes in
  1 s, so for the first time it writes its full output. The count rose because
  the producer started working.

The genuine leaks in the set are the pin itself serialized at float64 —
`beta-decay-matrix.parameters.q = 1.1099785827513808` and
`markov-substrate-realization.parameters.q_0` — and clearing those means
converting float64 producers to mpmath end to end, which is bean qou-gqt5's
scope, not a one-line fix.

## What WAS fixed here

The advisory `f64-into-mpmath` gate's LAUNDERED class — `mpf(str(<f64>))`,
which recovers a float64's 17 digits and discards the other 32 while LOOKING
like arbitrary precision. **8 sites -> 1.**

The clearest of them, `gram-matrix-dual.py:205`, had a comment directly above
it saying the mpmath form "is exact, so the witness carries the exact value
rather than a 16-digit shadow of it" — and `mpf(str(q0))` produced exactly that
16-digit shadow. The code defeated its own stated purpose.

`docs/coordination/trace_convention_registry_validate.py` did it twice inside
`workdps(50)`: `mpf(str(trM_borromean(mpf(str(Q0)))))` and
`sp.Float(str(Q0), 50)` — asking for 50 digits from a 17-digit source, so 33
were padding. That module already imported `Q_50_DIGIT_STR` elsewhere.

The one remaining site is NOT a defect: `wlambda_normalisation_census.py:65` is
the middle tier of a deliberate three-tier fallback (`Q_50_DIGIT_STR` -> `Q` ->
string literal) whose last tier carries a comment showing the author was
careful. The audit cannot see the intent. Worth a suppression marker if the
audit ever gains one.

## The F64_CAST class is untouched and much larger

    F64_CAST — float(<f64>) in a value position: 118 file(s), 211 site(s)

Also declared "These are defects" by the same audit, and not addressed here.
Both classes belong to qou-gqt5's drain.
