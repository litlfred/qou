---
# qou-zck8
title: sublemma_2_1_A_operator_extract is float64-by-construction — blocks the weighted H6 regeneration
status: todo
type: bug
created_at: 2026-08-21T21:46:44Z
updated_at: 2026-08-21T21:46:44Z
---

The `qou-cds4` A-operator regeneration is **correct and blocked**, and the
blocker is precision rather than convention.

## What happened

The two A-operator producers were fixed to derive the p-n interface from
`d_for_ctype` instead of hardcoding the colour-blind `-h/2` (landed). Running
`sublemma_2_1_A_operator_extract.py` with that fix does exactly what it should —
the deuteron moves onto the canonical frame, `0.5750908722902754 ->
0.5751722439177617`, matching `bring_color_weighted` to 1.8e-14, and the mass
table stops being mixed-frame.

But the regenerated witness trips the raw-float64 ratchet:

    REGRESSED — these witnesses gained raw float64:
         304 -> 493     computations/sublemma-2-1-A-operator-extract.witness.json

**That growth is real, not an artifact of the count.** The colour-weighted
interface makes more `(λ, ξν)` blocks operator-valued rather than scalar, so the
producer emits more matrix entries — and every one of them is float64, because
the producer is float64 by construction:

    grep numpy  -> np.zeros(..., dtype=complex), np.eye(..., dtype=complex)
    grep mpmath -> 0 occurrences

So this is not a serialization fix. Wrapping those values in `_precision.fmt`
would dress float64 as high precision, which is worse than leaving them — the
`mpf_mixed_arithmetic` gate exists for exactly that move.

## Why the witness was reverted rather than shipped

The ratchet's rule is that a baselined witness whose count increases fails, and
`AGENTS.md` forbids growing a baseline to clear it. Shipping the regeneration
would have meant either breaking that gate or widening its baseline — and the
gate in question is the one landed the same day, whose whole argument was that a
preflight red for reasons you did not cause is a preflight people learn to skip.
Doing that to somebody else's gate two hours after making the argument would be
indefensible.

**The producer fixes ARE landed.** They are correct and inert: nothing changes
until the extract is regenerated, so the tree is strictly better and no number
moved.

## The actual work

Port `sublemma_2_1_A_operator_extract.py` off float64. It is a seminormal-matrix
computation (`evaluate_word_matrix` -> `np.ndarray`, `chi_lambda_matrix_trace`),
so the port is real: mpmath matrices, or an exact route, not a wrapper. Note the
`numpy/mpmath dtype leak` gate guards the obvious half-measure — an `mpf`
reaching a numpy array silently demotes it to `dtype=object` and leaves BLAS,
measured at ~4000x elsewhere (`qou-5qwb`).

Related: `qou-840k` (excise float64 — 222 float casts of q-derived constants) is
the same class corpus-wide, though it does not name this file.

## What is NOT blocked

The mixed-frame finding stands and is recorded in `qou-cds4`: only the deuteron
was off-frame, T and up were already canonical, and the fix is one extract
(`(6,"pn")`) — not the five, and not the long-compute job I first scoped. All of
that was measured before this blocker appeared.
