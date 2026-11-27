import QOU.Nuclear.SilverRatioCounitExclusion
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# The silver-ratio evaluations at `ℝ` (Transcendental companion)

Split from `QOU.Nuclear.SilverRatioCounitExclusion` (bean `qou-dk7p`). That file
states the evaluations over an ordered field with `√2` a symbol `r`, `r² = 2`.
This file sets `r := Real.sqrt 2` and keeps the original names.
-/

namespace QOU.QBeta

/-- The silver ratio `1 + √2`, the positive root of `q² − 2q − 1`. -/
noncomputable def silver : ℝ := silverOf (Real.sqrt 2)

/-- `√2 > 0`, used throughout. -/
theorem sqrt_two_pos : (0 : ℝ) < Real.sqrt 2 :=
  Real.sqrt_pos.mpr (by norm_num)

/-- `(√2)² = 2`. -/
@[simp] theorem sq_sqrt_two : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)

theorem silver_root : silver ^ 2 - 2 * silver - 1 = 0 := silverOf_root sq_sqrt_two

theorem one_lt_silver : (1 : ℝ) < silver := one_lt_silverOf sqrt_two_pos

theorem silver_ne_zero : silver ≠ 0 := silverOf_ne_zero sqrt_two_pos

theorem epsNP_silver : epsNP silver = 0 := epsNP_silverOf sq_sqrt_two

theorem bracket2half_silver : bracket2half silver = Real.sqrt 2 :=
  bracket2half_silverOf sqrt_two_pos sq_sqrt_two

theorem chiBlock3_silver_ne_zero : chiBlock3 silver ≠ 0 :=
  chiBlock3_silverOf_ne_zero sqrt_two_pos sq_sqrt_two

theorem silver_separates_target_from_control :
    epsNP silver = 0 ∧ chiBlock3 silver ≠ 0 :=
  silverOf_separates_target_from_control sqrt_two_pos sq_sqrt_two

end QOU.QBeta
