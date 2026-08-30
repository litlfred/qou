---
# qou-mjbr
title: 'Roth for every real algebraic number: the plumbing from IsAlgebraic to psi alpha_0'
status: completed
type: task
priority: normal
created_at: 2026-08-30T14:28:55Z
updated_at: 2026-08-30T14:52:21Z
---

Child of `qou-br3w`. The only gap between `not_approximable_of_algebraic` and the classical
statement that needs Lean work rather than prose. NO NEW ESTIMATE IS INVOLVED -- the analytic half
is already done by `not_approximable_of_nsmul_eq` (QOU/Mathlib/RothFinalAssembly.lean), which takes
`(n:R) * x = psi (algebraMap (O K) K alpha_0)` and concludes `x` is not approximable to order
2+delta.

What is left is construction:

1. `IsAlgebraic Q x` for `x : R`  ->  `IsAlgebraic.exists_integral_multiple` gives `n != 0` with
   `IsIntegral Z (n * x)`.
2. `K := Q(n*x)` as a subfield of `R` -- IntermediateField.adjoin, plus the `NumberField K`
   instance (finite-dimensional over Q because n*x is algebraic).
3. `psi : K ->+* R` is the inclusion.
4. `alpha_0 : O K` from step 1's integrality, with `psi (algebraMap (O K) K alpha_0) = n * x`.

Then feed `not_approximable_of_nsmul_eq`.

SECOND, SMALLER ITEM, worth doing at the same time because a reader will ask: the statement is in
HEIGHT form, `max(|num|, den)`, not the classical denominator form. |alpha| <= B gives H <= (B+1)q,
so q^{-(2+eps)} <= (B+1)^{2+eps} H^{-(2+eps)} <= H^{-(2+delta)} for large H and any delta < eps.
Benign, one lemma, and currently unwritten -- flagged as R0 in
docs/audits/2026-08-30-roth-arc-ROAST.md.

## Summary of Changes

DONE. Roth's theorem in its classical form, axiom-clean:

    #print axioms MvPolynomial.finite_approximations_of_isAlgebraic
      -> [propext, Classical.choice, Quot.sound]

For a real algebraic x and any eps > 0, |x - p/q| <= q^{-(2+eps)} has only FINITELY MANY rational
solutions.

THREE ITEMS, and the third was not in this bean's original scope.

1. HEIGHT -> DENOMINATOR (approximable_height_of_den). The gap runs in the HARDER direction and I
   had not noticed until the roast: H >= q, so q^{-(2+eps)} >= H^{-(2+eps)}, i.e. the height form
   is the STRONGER hypothesis and does not follow from the denominator form for free. What bridges
   them is that a rational close to a bounded x has a bounded numerator, |p| <= (B+1)q.

2. THE PLUMBING (not_approximable_of_isAlgebraic). As predicted, construction with no new estimate.
   IsFractionRing.isAlgebraic_iff Z Q R is the bridge from IsAlgebraic Q x to IsAlgebraic Z x --
   clearing denominators, packaged. Q(y) for y = |c|x is a number field: finite-dimensional because
   y is integral over Q, characteristic zero because it sits in R. y need not be primitive; Q(y) is
   used only as SOME number field containing y, never as Q(x). The one step that does not go the
   obvious way is integrality descending from R to Q(y), which needs IsIntegral.tower_bot and the
   injectivity of the embedding.

3. THE CLASSICAL FORM (finite_approximations_of_isAlgebraic, finite_den_le). Added because the PR
   listed it as a distance from the classical statement and leaving it would have been the same
   defect the roast caught: a named gap nobody wrote down. THE STEP IS NOT BOOKKEEPING -- "no family
   of unbounded denominator" and "finitely many solutions" differ by the DISCRETENESS OF Q, and
   nothing earlier in the arc supplies it: every estimate in Roth is about how GOOD an approximation
   is, none about how MANY there are. finite_den_le supplies it. What makes the two meet is that a
   solution is automatically within 1 of x, since q^{-(2+eps)} <= 1.

All three verified with `lake env lean` on the whole module (zero errors, zero warnings) and
`#print axioms` by name.
