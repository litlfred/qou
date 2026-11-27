import QOU.MassTheory.ReebLinkingCWF
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# The CWF linking functional at `ℝ` (Transcendental companion)

Split from `QOU.MassTheory.ReebLinkingCWF` (bean `qou-dk7p`). That file works with
the norm as a symbol `r`, `r² = 1 + z²`. This file sets `r := √(1+z²)` and keeps
the original names `ell`, `ellDirect` and their theorems.
-/

namespace QOU.MassTheory.ReebLinkingCWF

/-- `ℓ(z) = z/√(1+z²)`. -/
noncomputable def ell (z : ℝ) : ℝ := ellOf (Real.sqrt (1 + z ^ 2)) z

/-- `cos θ = 1/√(1+z²)`. -/
noncomputable def ellDirect (z : ℝ) : ℝ := ellDirectOf (Real.sqrt (1 + z ^ 2))

theorem sq_sqrt_one_add_sq (z : ℝ) : Real.sqrt (1 + z ^ 2) ^ 2 = 1 + z ^ 2 :=
  Real.sq_sqrt (by positivity)

theorem ellDirect_sq_add_ell_sq (z : ℝ) : ellDirect z ^ 2 + ell z ^ 2 = 1 :=
  ellDirectOf_sq_add_ellOf_sq (sq_sqrt_one_add_sq z)

theorem ell_sq_normalization (z : ℝ) : ell z ^ 2 * (1 + z ^ 2) = z ^ 2 :=
  ellOf_sq_normalization (sq_sqrt_one_add_sq z)

theorem ell_criticality (w : ℝ) (hw : w ≠ 0) :
    ell (1 / w) ^ 2 * (1 + w ^ 2) = 1 :=
  ellOf_criticality hw (sq_sqrt_one_add_sq (1 / w))

theorem ell_eq_exchange_unit_component (z : ℝ) :
    ell z = z * (Real.sqrt (1 + z ^ 2))⁻¹ :=
  ellOf_eq_exchange_unit_component _ z

end QOU.MassTheory.ReebLinkingCWF
