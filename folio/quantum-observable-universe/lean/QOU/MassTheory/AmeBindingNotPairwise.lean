import Mathlib.Tactic
import QOU.Mass.PairwiseCumulantVanishing

/-!
# The AME binding is not pairwise-additive — the instantiation, discharged

`QOU.Mass.PairwiseCumulantVanishing` (landed in #6101) proves the general fact:
a pairwise-additive binding map has identically vanishing connected three- and
four-body cumulants, for **every** bond functional. Its falsifiable form,
`not_isPairwise_of_b3_ne_zero`, says a binding map with any nonzero connected
`b₃` is not of that shape.

Its docstring then instantiates that against measurement — *"Since AME2020 gives
`b₃ = +1.426222 ≠ 0`, the physical binding is not of this shape"* — but **in
prose**. No `BindingMap` is constructed from AME numbers anywhere on `main`, so
the step from the general theorem to the physical conclusion is asserted rather
than checked. This file supplies exactly that step and nothing else.

## What is added

* `ameMap` — a `BindingMap ℚ` built from AME2020: every pair is the deuteron
  binding `2.224566`, every triple the isospin average of ³H and ³He,
  `(8.481798 + 7.718043)/2`.
* `ame_b3_eq` — its connected three-body cumulant is exactly `2852445/2000000
  = 1.4262225`, the figure the Ursell inversion reports as `+1.426222`.
* `ame_b3_ne_zero`, `ame_not_isPairwise` — hence, via the merged general
  theorem, the AME binding **is not pairwise-additive**. Machine-checked, not
  quoted.

## Why this and not the rest

An earlier revision of this branch carried two further files. Both are now
**redundant against `main`** and were deleted rather than merged:

* `PairwiseAdditiveCumulants.lean` — its `pairwise_b3_eq_zero` assumed a *common
  bond value*; `b3_eq_zero_ofBondFunctional` covers every bond functional, so
  the merged version strictly subsumes it.
* `FixedDepthGrowthBound.lean` — its `abs_le_geometric` / `not_factorial_growth`
  are subsumed by `ConstantKernelGrowthBound.exists_exponential_bound` and
  `not_isConstKernelRec_of_superExponential`, which quantify over a
  `SuperExponential` predicate instead of the factorial instance and prove both
  directions.

Landing either would have put a second copy of a general result into the corpus
behind a weaker hypothesis — the duplication class `#3594` records.

## Scope

This changes nothing about the magnitude gate, which stays **OPEN**. It closes a
prose-vs-proof seam in an argument already made. The `b₄` leg is deliberately
not instantiated: the ⁴He literal is recorded as `28.295673` in
`he4_body_order_shortfall_location_probe.py` and as `28.2956624` in #6101's
writeup, and `b₃` does not depend on it. That discrepancy is noted in bean
`qou-edt7` rather than silently resolved here.

Base ring: `ℚ` — the AME data are exact decimal literals and no archimedean
construct is needed (AGENTS.md §7c).
-/

namespace QOU.MassTheory.AmeBindingNotPairwise

open QOU.Mass.PairwiseCumulantVanishing

/-- AME2020 as a four-body binding map: pairs at the deuteron value, triples at
the isospin average of ³H and ³He. `quad` is set to the ⁴He binding but plays no
part in the `b₃` statements below. -/
def ameMap : BindingMap ℚ where
  pair _ _ := 2224566 / 1000000
  triple _ _ _ := (8481798 + 7718043) / 2000000
  quad := 28295673 / 1000000

/-- The connected three-body cumulant of the AME map, exactly. -/
theorem ame_b3_eq (i j k : Fin 4) :
    ameMap.b3 i j k = 2852445 / 2000000 := by
  simp [BindingMap.b3, ameMap]
  norm_num

theorem ame_b3_ne_zero (i j k : Fin 4) : ameMap.b3 i j k ≠ 0 := by
  rw [ame_b3_eq]
  norm_num

/-- **The instantiation the merged docstring asserts in prose.** The AME binding
is not pairwise-additive — so no bond functional, the Cauchy-forced logarithm
included, assembles it. -/
theorem ame_not_isPairwise : ¬ ameMap.IsPairwise :=
  not_isPairwise_of_b3_ne_zero (ame_b3_ne_zero 0 1 2)

end QOU.MassTheory.AmeBindingNotPairwise
