# Tier-2 #3 closed: skew-Euclidean right-division sorry-free; Tier-2 #4 verdict

**Date:** 2026-07-20
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Bean:** qou-965j
**File:** `content/quantum-observable-universe/lean/QOU/Machinery/QuantumTorusDivision.lean`

## Summary

Both cited `sorry`s in `QuantumTorusDivision.lean` — the genuine v4.24.0
Ore-extension gap — are **closed sorry-free**. The reduction engine
(`reduction_leading_coeff_match`, `reduction_top_coeff_cancel`,
`coeffAt_sub`) was already proved; this work built the induction/termination
layer on top. File verified lean-direct (`lean QuantumTorusDivision.lean`,
exit 0, no live `sorry`); downstream `StrongAJFigureEight.lean` re-verified
exit 0.

## Tier-2 #3 — what was proved

1. **`topDeg_lt_of_forall_ge_eq_zero`** (new helper). The `WithBot ℤ` /
   `Finset.max` calculus: if every L-coefficient at exponent `≥ e` vanishes,
   then `topDeg f < e`. Proof by `Finset.max'`/`coe_max'` + `mem_expSupport_iff`
   (empty-support and nonempty branches).

2. **`skew_right_division_degree_drop`** (was sorry #1). One reduction step
   strictly drops `topDeg`. The `L^e` coefficient vanishes
   (`reduction_top_coeff_cancel`); every *higher* coefficient vanishes because
   `topDeg f = e` (`coeffAt_eq_zero_of_topDeg_lt f`) and the reduction monomial
   `L^{e-d}·g` contributes nothing above `e` — computed directly via
   `coeff_single_mul` (index `(ofAdd(e-d))⁻¹·ofAdd n = ofAdd(n-(e-d))`, and
   `n-(e-d) > d = topDeg g` for `n > e`). Then `topDeg_lt_of_forall_ge_eq_zero`
   upgrades the coefficient facts to the strict degree drop.

3. **`topDeg_eq_bot_iff`** (new helper): `topDeg f = ⊥ ↔ f = 0`
   (`Finset.max_eq_bot` + `image_eq_empty` + `support_eq_empty`).

4. **`exists_skew_right_division_fuel` + `exists_skew_right_division`**
   (was sorry #2). Existence of `f = q·g + r` with `r=0` or
   `topDeg r < topDeg g`. Rather than `WellFounded.fix` on `WithBot ℤ`
   (which is not downward-well-founded), a **ℕ-fuel induction**: prove
   `∀ k f, topDeg f < d+k → ∃ q r …` by `Nat.rec`. Each step invokes (2) to
   drop `topDeg` under the fuel budget; `k` steps terminate. The top-level
   theorem reads a fuel `k = (e-d).toNat + 1` off `f`'s finite top degree
   (`topDeg_eq_bot_iff` gives the exponent `e` when `f ≠ 0`). The assembled
   quotient is `Σ reductionQuotient`; correctness by `add_mul`/`add_assoc`/`abel`
   (noncommutative-safe — no `ring`).

No axioms introduced; no `native_decide`; no conditional class. The one lint
warning (`hde` unused in `skew_right_division_degree_drop`) is a deliberately
retained domain precondition (`d ≤ e`) that the fuel caller always supplies.

## Transitive win

`StrongAJFigureEight.lean`'s `TransferLemmas.division` field is now discharged
sorry-free by `exists_skew_right_division` (docstrings synced). The remaining
open inputs to strong-AJ for the figure-eight are `aj_mem` (torus module action
+ operator lift) and the `[Tr4]` `minimality` transfer — the B3 division wall
is removed.

## Tier-2 #4 verdict — the θ = ½·C(m,2) analytic bridge: GENUINE WALL

**Not buildable now.** #4 asks to identify the Newton-polygon slope of the
q-difference operator with the q-Gevrey growth order of its formal solutions —
the Ramis–Sauloy–Zhang (2013) index theorem for q-difference modules, the
q-analogue of the classical Ramis index theorem. Mathlib v4.24.0 contains
**none** of the required substrate (grep-verified empty): no q-difference
modules, no Newton polygon of an operator, no Gevrey / q-Gevrey asymptotic
scale, no formal-solution slope filtration, no index/index-theorem machinery.
Building the genuine analytic theorem would require all four layers from
scratch — a multi-file, realistically multi-month Mathlib development, not a
self-contained finite-algebra gap.

This is categorically unlike #3: #3's ingredients (a skew-monoid-algebra, its
`coeff_single_mul`, a finite support, ℕ-fuel termination) were *all present* in
Mathlib — only the assembly was missing. #4's ingredients are *absent as a
theory*. What the corpus *can* and *does* do (all proved sorry-free) is the
**arithmetic/combinatorial skeleton** that stands in for the analytic content
with an honest `-- Ref: [ramis-sauloy-zhang2013]` definitional bridge:
`ThetaSlopeArithmetic` (bar negates, product adds, ramified pullback scales —
RSZ Thm 2.2.1(iv), as ℚ-slope arithmetic), `BindingGevreyHalf` (the integer
sandwich `n! ≤ 4ⁿ·I(n)² ≤ 8ⁿ·n!` pinning the Gevrey-1/2 *class*), and
`QDifferenceConfluentObstruction` (the bounded-depth kernel exclusion). Those
are the correct current stopping point; the full RSZ slope = growth-order
*equality* is a genuine unbuilt-Mathlib wall and should stay a cited reference,
not be axiomatized as proved.
