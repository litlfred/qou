import QOU.MassTheory.GrowingWidthCutShapeExclusion
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# Growing-width cut: the `Real.sqrt` forms (Transcendental companion)

Split from `QOU.MassTheory.GrowingWidthCutShapeExclusion` (bean `qou-dk7p`). That
file states the bounds with the square root as a symbol `s`, `0 ≤ s`, `s² = x`.
This file instantiates `s := Real.sqrt x` and keeps the original names.
-/

set_option autoImplicit false

namespace QOU.MassTheory

/-- The geometric mean never exceeds the max, at `ℝ`. -/
theorem sqrt_mul_le_max {x y : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) :
    Real.sqrt (x * y) ≤ max x y :=
  le_max_of_sq_eq_mul hx hy (Real.sqrt_nonneg _) (Real.sq_sqrt (mul_nonneg hx hy))

/-- The quantitative form at `ℝ`: the worst multiplicative error is at least
`√(rmax / rmin)`. -/
theorem best_constant_error_lower_bound
    {rmin rmax c : ℝ} (hmin : 0 < rmin) (hle : rmin ≤ rmax) (hc : 0 < c) :
    Real.sqrt (rmax / rmin) ≤ max (rmax / c) (c / rmin) :=
  best_constant_error_lower_bound_of_sq hmin hle hc (Real.sqrt_nonneg _)
    (Real.sq_sqrt (div_nonneg (le_trans hmin.le hle) hmin.le))

end QOU.MassTheory
