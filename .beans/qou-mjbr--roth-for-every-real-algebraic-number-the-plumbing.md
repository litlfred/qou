---
# qou-mjbr
title: 'Roth for every real algebraic number: the plumbing from IsAlgebraic to psi alpha_0'
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:28:55Z
updated_at: 2026-08-30T14:28:55Z
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
