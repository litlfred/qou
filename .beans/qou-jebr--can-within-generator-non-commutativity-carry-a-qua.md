---
# qou-jebr
title: Can within-generator non-commutativity carry a quadratic? Pin the transfer-matrix convention first
status: completed
type: task
priority: normal
created_at: 2026-09-04T20:43:03Z
updated_at: 2026-09-04T20:45:55Z
---


Opened 2026-09-04 to clean up after a retracted test, and **closed negative the
same day**. Probe: `no_within_generator_noncommutativity_probe` (6/6).

## The convention, pinned first this time

`ground_state_ordering_convention_independence_probe` states it:
`M = alpha*1 + beta*S` with `S = [[h,1],[1,0]]`, readout
`Vhat = z*M[1][0] + M[1][1] = z*beta + alpha`.

Checked against a known value **before** using it: a single crossing is
`M = S + d*1`, giving `Vhat = z + d` — exactly the bond factor `qou-m3sh` proved
and `ChainTraceFactor.twoStrandTrace_eq` formalises. The readout in my retracted
test, `z*M[0,0] + M[1,0]`, is the one in
`computations/_deprecated/transfer_matrix_symbolic.py`; it is deprecated and does
not reproduce `z + d`. That single line is what the earlier error cost.

## The answer: the question is empty

`S^2 = hS + 1` exactly, and every crossing at a generator is `S + d`, so

    [S + d1, S + d2] = 0   identically.

All crossings at one generator are polynomials in the same matrix and commute.
**There is no within-generator non-commutativity for anything to be carried
by.** Structural, not numerical.

## What is true instead, and it is a different property

The readout is **not multiplicative** within a generator:

    Vhat(AB) - Vhat(A)Vhat(B) = z*h - z^2 + 1 = (q^4+q^2+1)/(q^2+1)^2 != 0

independent of the offsets. That is the Hecke relation folding `S^2` back to
`alpha + beta S`. Non-multiplicative is easy to mistake for non-commutative; it
is not the same thing, and the distinction is what the original question got
wrong.

## And it still cannot make a quadratic

For a reason unrelated to either property: **every interface generator carries
exactly one crossing** (verified for 3He, 3H, 4He, 6Li), so no within-generator
combination happens on a bond at all. The multi-crossing generators are the
intra-nucleon ones (`3k`, `3k+1`), which sit inside ONE nucleon, so their factor
depends only on that nucleon's type. Summed that is
`Z*(p-factor) + N*(n-factor)` — linear in the counts, never bilinear. Nothing
within a generator mixes two different nucleons, and a quadratic in `N - Z`
needs exactly that.

So the type-two direction now closes for a **third** independent reason, on top
of the per-partition scales and the logarithm (`qou-eqwg`).

## Summary of Changes

- `computations/probes/no_within_generator_noncommutativity_probe.py` (6/6,
  float64-gate clean): convention pinned against the proved value, commutator
  shown zero identically, the non-multiplicativity defect computed in closed
  form, and the interface-generator crossing counts verified.
- Nothing wired, nothing fitted, no binding claim.

Not touched: `qou-bygw`, whose band generators DO span several generators and
genuinely fail to commute — still blocked on a modelling decision.
