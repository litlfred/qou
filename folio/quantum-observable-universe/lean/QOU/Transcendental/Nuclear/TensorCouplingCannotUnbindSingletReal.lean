import QOU.Nuclear.TensorCouplingCannotUnbindSinglet
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# 2×2 interlacing with `Real.sqrt` (Transcendental companion)

Split from `QOU.Nuclear.TensorCouplingCannotUnbindSinglet` (bean `qou-dk7p`). That
file states part (B) with the square root a symbol `s`. This file sets
`s := √(((a − b)/2)² + t²)` and keeps the original names.
-/

namespace QOU.QBeta.TensorCouplingSinglet

/-- The lower eigenvalue of the real symmetric block `[[a, t], [t, b]]`. -/
noncomputable def lowerEigen (a b t : ℝ) : ℝ :=
  lowerEigenOf a b (Real.sqrt (((a - b) / 2) ^ 2 + t ^ 2))

theorem sq_sqrt_disc (a b t : ℝ) :
    Real.sqrt (((a - b) / 2) ^ 2 + t ^ 2) ^ 2 = ((a - b) / 2) ^ 2 + t ^ 2 :=
  Real.sq_sqrt (by positivity)

theorem lowerEigen_is_eigenvalue (a b t : ℝ) :
    (a - lowerEigen a b t) * (b - lowerEigen a b t) - t ^ 2 = 0 :=
  lowerEigenOf_is_eigenvalue (sq_sqrt_disc a b t)

theorem lowerEigen_le_left (a b t : ℝ) : lowerEigen a b t ≤ a :=
  lowerEigenOf_le_left (Real.sqrt_nonneg _) (sq_sqrt_disc a b t)

theorem lowerEigen_lt_left_of_ne (a b t : ℝ) (ht : t ≠ 0) : lowerEigen a b t < a :=
  lowerEigenOf_lt_left_of_ne ht (Real.sqrt_nonneg _) (sq_sqrt_disc a b t)

theorem lowerEigen_lt_right_of_ne (a b t : ℝ) (ht : t ≠ 0) : lowerEigen a b t < b :=
  lowerEigenOf_lt_right_of_ne ht (Real.sqrt_nonneg _) (sq_sqrt_disc a b t)

end QOU.QBeta.TensorCouplingSinglet
