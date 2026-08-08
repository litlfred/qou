---
# qou-lz235
title: 'The sqrt5 slot is Sigma(2,3,5): read Lawrence-Zagier and place the Bring constant'
status: todo
type: task
priority: high
tags:
    - one-loop
    - c-sigma
    - brings-surface
    - poincare-sphere
    - quantum-modular
    - branched-cover
    - lawrence-zagier
created_at: 2026-08-08T19:55:00Z
updated_at: 2026-08-08T21:10:00Z
---

## The ask

`qou-vdvS` and `qou-vdvK` derived `c_sigma` in closed form wherever the Laplace
saddle sits at a regular ideal polyhedron, and identified the obstruction to
going further as ARITHMETIC: `det(Hessian) = tau_DG` is an algebraic number in
the trace field, and radical expressions appear only for the two exceptional
imaginary quadratic fields `Q(sqrt-3)` and `Q(i)`. On that reading a `sqrt5`
is unavailable, because `Q(zeta_5)` is degree 4.

**That reading answers the wrong question.** The corpus's `sqrt5` was never
going to come from a hyperbolic trace field. It comes from a CYCLIC BRANCHED
COVER, and the arithmetic is the same shape:

    |H_1(Sigma_d(K))| = |Res(Delta_K, (t^d-1)/(t-1))|   -- a norm from Z[zeta_d]

Computed (sympy, this session):

    T_{2,3} trefoil     d=5:  |H_1| = 1   Poincare homology sphere Sigma(2,3,5)
    T_{2,5} cinquefoil  d=2:  |H_1| = 5   lens space L(5,q)
    sum_k zeta_5^{k^2} = sqrt5            the Bring constant, as a Gauss sum

Both knots are the ones `bring-trefoil-cinquefoil-channel` names, and
`klein-bring-icosahedral-bridge` already places `S^3/2I -> S^2(2,3,5)`. The
missing sentence is that the trefoil is the BRANCH LOCUS of that cover, and
`|2I| = 120 = |S_5| = |Aut(Bring)|`.

## What to do

1. **Get and read `lawrence-zagier-1999`** (Asian J. Math 3 (1999) 93-107),
   registered but NOT YET READ — the author's page is egress-blocked here, and
   no arXiv copy was found. It computes the asymptotic expansion of the WRT
   invariant of `Sigma(2,3,5)` as the radial limit of an Eichler integral of a
   half-integral-weight modular form. That is the non-hyperbolic analogue of
   `Q_inf`, and it is where the `sqrt5` in a one-loop constant actually lives.
   `zagier2010` (already registered, full text) is its follow-up.
2. Extract the one-loop constant of `Sigma(2,3,5)` in their normalisation and
   compare it to the `2^{-1/2}` that `k_sq_eq_half_of_saddle` shows is forced in
   the hyperbolic case. **They need not agree** — `Sigma(2,3,5)` is Seifert-
   fibred, `Vol = 0`, and there is no Lobachevsky saddle at all. Establishing
   that they are DIFFERENT constants, arrived at by different mechanisms, is a
   perfectly good outcome and is the more likely one.
3. Only then decide whether anything connects the Bring `sqrt5` to `c_sigma`.

## The trap, stated in advance

`Sigma(2,3,5)` is spherical and the torus knots `T_{2,3}`, `T_{2,5}` have zero
simplicial volume. The colored Jones grows POLYNOMIALLY there, not
exponentially; `c_sigma` as this corpus defines it (`lim |J'_N| N^{-3/2}
e^{-Vol N/2pi}`) is not the same object and the volume conjecture is vacuous.
Writing the Bring `sqrt5` and a hyperbolic `sqrt5` into the paper as one thing
would be a category error. Two `sqrt5`s of cyclotomic origin are not
automatically the same `sqrt5`.

## Definition of done

Lawrence-Zagier read at full text, its `Sigma(2,3,5)` constant recorded in a
witness, and a written verdict on whether it relates to `c_sigma` or is a
separate mechanism that merely shares the field `Q(zeta_5)`.

## Progress 2026-08-08 — two of the three mechanisms are now identified, one is BLOCKED

**Mechanism (3), quantum dimension, is done and it identifies with (1).** The
user supplied Jones, Bull. AMS 12 (1985) 103-111 (now full text at
`uploads/S0273-0979-1985-15304-2.pdf`; `jones1985` was already registered). At
`r = 5` the Markov trace's quantum dimension is the golden ratio directly,
`[2] = [3] = 2 cos(pi/5) = phi`, and the Bring torus knots evaluate to
golden-ratio algebraic integers:

                       |V(zeta_10)|^2         |V(zeta_5)|^2
    3_1 trefoil        phi^2                  3 - 1/phi
    T_{2,5} cinquefoil 2 + phi  = D^2_{Fib}   phi^{-4}

`2 + phi = 1 + phi^2` is the GLOBAL DIMENSION of the Fibonacci category. So the
Gauss-sum `sqrt5` of `bring-trefoil-cinquefoil-channel` and the Markov-trace
`sqrt5` of Jones are the same `sqrt5` — both `Q(sqrt5) = Q(zeta_5)^+`, entering
through `2 cos(pi/5)`. Probe: `bring_golden_jones_probe.py`, exact radicals,
closed forms asserted before evaluation.

**Mechanism (2) is BLOCKED ON READING in this environment — do not re-attempt
the same way.** `lawrence-zagier-1999` is unavailable:

  * `www.math.huji.ac.il` (the author's own page)  -> EGRESS_BLOCKED
  * `arxiv.org` (for the papers that restate it)   -> EGRESS_BLOCKED

Both are network-policy denials of the remote execution environment, not
transient failures, and must not be routed around. Either run from an
environment whose network policy permits them, or have the PDF uploaded to
`uploads/` the way `jones1985` was.

**If it stays blocked, compute instead of reading.** `Sigma(2,3,5)` is `-1`
surgery on the trefoil, so its WRT invariant is reachable from the trefoil's
colored Jones by the Reshetikhin-Turaev surgery formula, and its asymptotics can
be extracted numerically exactly as `Q_inf` and `c_sigma(4_1)` were. **Do not
implement a surgery formula from memory** — that is the same failure mode as the
retracted van der Veen premise. Implement it, then SELF-TEST against cases with
known answers (`tau_r(S^3) = 1`; lens-space values are Gauss sums) BEFORE
trusting any Poincare-sphere number. One hook worth checking on arrival: the
Lawrence-Zagier modulus is `q^{n^2/120}` and `4 * 2 * 3 * 5 = 120 = |2I| =
|S_5| = |Aut(Bring)|`.

**The trap in the original ask still stands** and is now sharper: the `c_sigma`
closed forms live in `Q(i)` and `Q(sqrt-3)`, the two exceptional IMAGINARY
quadratic fields. `Q(sqrt5)` is REAL. So a `sqrt5` cannot enter `c_sigma` by the
polyhedral route at all, and any connection would have to be of a different
kind. Expect a separation, not a unification.
