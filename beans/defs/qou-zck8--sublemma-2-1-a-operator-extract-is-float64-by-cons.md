---
# qou-zck8
title: sublemma_2_1_A_operator_extract is float64-by-construction — blocks the weighted H6 regeneration
status: completed
type: bug
priority: normal
created_at: 2026-08-21T21:46:44Z
updated_at: 2026-08-22T09:44:42Z
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

## SCOPING CORRECTED 2026-08-21 — the part I called hard is already built

I wrote above that "the port is real: mpmath matrices, or an exact route, not a
wrapper", assuming the seminormal-matrix source would have to be rebuilt. It does
not. Measured:

    char_fast._compiled_sigmas(shape, "mpmath50")   ->  mpmath matrix, mpf entries
    char_fast.chi_lambda_fast_mp(...)               ->  mpmath.mpc

    (2,1) sigma_0 [0,0]:
      double     float64  1.10997858275138
      mpmath50   mpf      1.109978582751381059879

So the high-precision backend exists, is wired, and is already used elsewhere in
the corpus. `evaluate_word_matrix` simply asks for `"double"`.

### What the work actually is

16 numpy sites, concentrated in two places. In order of difficulty:

**Easy — mechanical:**
- `evaluate_word_matrix` (l.64-79): request `"mpmath50"`, build with `mp.eye` /
  `mp.matrix`, multiply with `*`. The word loop is unchanged in shape.
- `chi_lambda_matrix_trace` (l.128): `complex(np.trace(M))` -> mpmath trace.
- Reporting (l.249-254): `np.linalg.norm`, `np.max(np.abs(...))`, the
  scalar-vs-operator test at `< 1e-9`. Straight substitutions.

**The real work — the least-squares solve (l.204-237):**
- `np.linalg.lstsq(M, rhs, rcond=None)` on a **complex** system, `n_eq = K²`
  equations by `n_unknowns` entries. mpmath's counterpart is `mp.qr_solve`, and
  **the rank semantics differ**: `rcond=None` is rank-revealing and silently
  truncates small singular values; `qr_solve` does not. If this system is ever
  rank-deficient — and an over-determined fit across LR multiplicity copies
  plausibly is — the two do not compute the same thing, and the difference will
  not announce itself. Establish rank first (the existing call already returns
  `rank` and `sv`; log them before porting).
- `np.kron(B_mu, B_nu)` (l.217) has no mpmath built-in. Writing one is easy;
  getting the index order right matters, because the code depends on
  `X.T.flatten()` matching the `A_kk` layout, and there is an in-file comment
  recording an earlier bug here that produced 4e-3 relative residual on
  λ = (3,2,1).

### Validation path — cheap and decisive

The current committed witness is the float64 answer for the SAME system. Port,
re-run, and compare the per-pair `A_diag^{μν}` coefficients against it. Agreement
at ~1e-12 confirms the port; disagreement beyond that means the rank-truncation
question above was answered wrong, not that mpmath is "more accurate".

Do NOT accept a large disagreement as "higher precision revealing the truth"
without first checking rank — that is the shape of a rationalisation, and
`qou-4e5k` is the worked example of where that leads.

### Why it was not done in the same session

The lstsq/rank question is the one part that can silently produce wrong
A-operator coefficients, and those feed the canonical mass table. Porting it at
the tail of a long session, with no reviewer, against a gate I had just argued
should be respected, is how a plausible-looking wrong number lands. The producer
fixes are landed and inert; this is the piece that wants a fresh pass.
