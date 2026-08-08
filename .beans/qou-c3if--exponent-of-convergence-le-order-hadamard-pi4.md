---
# qou-c3if
title: 'PROVE(lean): exponent of convergence <= order (Hadamard PI-4), from Mathlib Jensen + counting'
status: todo
type: task
priority: normal
tags:
    - lean
    - hadamard
    - mathlib-gap
    - paper-qou
created_at: 2026-08-08T03:30:00Z
updated_at: 2026-08-08T03:30:00Z
parent: qou-v4if
---

## Why

For `f` entire of order `rho` with zeros `a_n`, Hadamard needs
`sum_n 1/|a_n|^{rho+eps} < infinity` for every eps > 0 — the exponent of
convergence is at most the order. That is what makes the genus `p <= rho` and
the canonical product converge (PI-3, already proved).

The route is Jensen's formula: `N(r) <= T(r) + O(1)` and the growth bound gives
`T(r) = O(r^rho)`, so the zero-counting function grows at most like `r^rho`, and
a summation-by-parts turns that into summability of `1/|a_n|^{rho+eps}`.

Jensen and the counting function are ALREADY IN MATHLIB (bean qou-bp5n), so this
is a derivation, not a build.

## Do

1. Settle qou-bp5n step 1 first — what `ValueDistribution.logCounting` unfolds to.
2. State `exponentOfConvergence_le_order` against
   `QOU.Mathlib.HadamardFactorization.IsEntireOfOrderLE`.
3. Prove, or reduce to a precisely-named missing lemma.

## ROAST

**"Closing this closes PI-5."** FALSE, and this is the trap. PI-5 needs at least
three things: (a) this bound, (b) the canonical product itself has order <= rho,
(c) the quotient `f / (exp(g)·prod)` is zero-free of finite order, hence
`exp(polynomial)` — which needs Borel-Carathéodory (qou-8cwi, done) plus a
Liouville-type argument. Closing (a) closes one of three. Do not report PI-5 as
"nearly done" on the strength of it.

**"`IsEntireOfOrderLE` is the standard order-of-growth hypothesis."** NO — and
this is the sharpest hit against the whole PI chain. The definition in
HadamardFactorization.lean is

    Differentiable C f  AND  exists A C, 0 < C AND forall z, ‖f z‖ <= A exp(C ‖z‖^rho)

That is **finite type with respect to order rho**, which is STRICTLY STRONGER
than "order <= rho". The classical Hadamard theorem hypothesises order <= rho,
i.e. for every eps > 0, `‖f z‖ <= exp(‖z‖^{rho+eps})` for large `‖z‖`. A
function of order exactly rho and infinite type (e.g. maximal type) satisfies
the classical hypothesis and NOT this one.

Consequences, both real:
  * the theorem as stated is TRUE but WEAKER than Hadamard;
  * the intended application (`phiBProd`, epic qou-lbth) must be checked against
    the STRONGER hypothesis. Nobody has done that. If phiBProd is of maximal
    type at its order, the whole chain proves something that does not apply.

Also loose: no `0 < A` is required, so `A <= 0` forces `f == 0`. Harmless where
`f 0 /= 0` is assumed, but the definition is not clean.

**Action item promoted from this roast:** before investing in PI-4/PI-5, verify
that `phiBProd` satisfies `IsEntireOfOrderLE` and not merely "order <= rho". If
it does not, the definition must be relaxed to the eps-form FIRST, and every
downstream statement re-checked.
