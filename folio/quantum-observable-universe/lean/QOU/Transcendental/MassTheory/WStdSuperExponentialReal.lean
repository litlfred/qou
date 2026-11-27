import QOU.MassTheory.WStdSuperExponential
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# `w_std` geometric bound at ratio `√2` (Transcendental companion)

Split from `QOU.MassTheory.WStdSuperExponential` (bean `qou-dk7p`). That file proves
the bound for every `r ≥ 0` with `r² ≤ 2` and inhabits the class at `r = 7/5`. This
file keeps the original `√2` statement and instance.
-/

namespace QOU.Mass.WStd

/-- **The geometric bound: `(1/30)·(√2)^k ≤ w_std(k)` for `k ≥ 3`.** -/
theorem wStd_geometric_from_three (k : ℕ) (hk : 3 ≤ k) :
    (1/30 : ℝ) * Real.sqrt 2 ^ k ≤ wStd k :=
  wStd_geometric_from_three_of_sq_le (Real.sqrt_nonneg 2)
    (le_of_eq (Real.sq_sqrt (by norm_num))) k hk

/-- **The class is inhabited at `k₀ = 3`, ratio `√2`.** -/
instance towerGeometricLowerBound_wStd :
    QOU.Mass.LevelSelection.TowerGeometricLowerBound wStd (Real.sqrt 2) (1/30) 3 where
  one_lt_r := by nlinarith [Real.sq_sqrt (show (0:ℝ) ≤ 2 by norm_num), Real.sqrt_nonneg 2]
  c_pos := by norm_num
  lower_bound := wStd_geometric_from_three

end QOU.Mass.WStd
