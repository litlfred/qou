import QOU.MassTheory.MagnusSumAbsEigBound
import Mathlib.Data.Real.Sqrt

/-!
# The bound on `Σ|eig(M_λ)|` at `ℝ` (Transcendental companion)

Split from `QOU.MassTheory.MagnusSumAbsEigBound` (bean `qou-dk7p`). That file states the
Cauchy–Schwarz step over an arbitrary ordered field with the square root as a ring symbol `s`,
`0 ≤ s`, `s² = x`. This file instantiates `s := Real.sqrt x` and keeps the original `ℝ` names.
-/

namespace QOU.MassTheory

open Finset BigOperators

variable {ι : Type*} [Fintype ι]

/-- Cauchy–Schwarz at `ℝ`: `Σ aᵢ ≤ √(card ι · Σ aᵢ²)`. -/
theorem sum_le_sqrt_card_mul_sum_sq (a : ι → ℝ) (ha : ∀ i, 0 ≤ a i) :
    ∑ i, a i ≤ Real.sqrt (Fintype.card ι * ∑ i, (a i) ^ 2) :=
  sum_le_of_sq_eq_card_mul_sum_sq a ha _ (Real.sqrt_nonneg _)
    (Real.sq_sqrt (by positivity))

/-- The composed bound `(B)` at `ℝ`. -/
theorem sum_le_sqrt_card_mul_of_sq_le (a : ι → ℝ) (ha : ∀ i, 0 ≤ a i) (F : ℝ)
    (hF : ∑ i, (a i) ^ 2 ≤ F) :
    ∑ i, a i ≤ Real.sqrt (Fintype.card ι * F) := by
  have hF0 : 0 ≤ F := le_trans (Finset.sum_nonneg fun i _ => sq_nonneg (a i)) hF
  exact sum_le_of_sq_eq_card_mul_of_sq_le a ha F hF _ (Real.sqrt_nonneg _)
    (Real.sq_sqrt (by positivity))

/-- Tightness at uniform modulus, at `ℝ`. -/
theorem sum_const_eq_sqrt_card_mul_sum_sq (c : ℝ) (hc : 0 ≤ c) :
    (∑ _i : ι, c) = Real.sqrt (Fintype.card ι * ∑ _i : ι, c ^ 2) :=
  sum_const_eq_of_sq_eq_card_mul_sum_sq c hc _ (Real.sqrt_nonneg _)
    (Real.sq_sqrt (by positivity))

end QOU.MassTheory
