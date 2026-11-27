import CompactQuantumMetrics.FrobeniusInnerProduct
import Mathlib.Data.Real.Sqrt

/-!
# QOU.Transcendental.FrobeniusNorm

The Frobenius norm `‖A‖_F := √⟨A, A⟩_F`. It sits behind the transcendental boundary
(owner ruling 2026-11-27, bean `qou-dk7p`) because it takes a real square root, which is a
completion of `ℚ` and not an algebraic operation. The inner product, its symmetry,
non-negativity and non-degeneracy stay algebraic in
`CompactQuantumMetrics.FrobeniusInnerProduct`; a consumer that needs only
`⟨A, A⟩_F` should import that module and not this one.

No empirical value enters this file.
-/

namespace QOU.MathlibExt.FrobeniusInnerProduct

open Matrix

variable {n : ℕ}

/-- **Frobenius norm** on matrices, `‖A‖_F := √(tr A^T · A)`. -/
noncomputable def Matrix.frobeniusNorm (A : Matrix (Fin n) (Fin n) ℝ) : ℝ :=
  Real.sqrt (Matrix.frobeniusInner A A)

/-- **Frobenius norm is non-negative.** -/
theorem frobeniusNorm_nonneg (A : Matrix (Fin n) (Fin n) ℝ) :
    0 ≤ Matrix.frobeniusNorm A :=
  Real.sqrt_nonneg _

/-- **Frobenius norm is zero iff matrix is zero.** -/
theorem frobeniusNorm_eq_zero_iff
    (A : Matrix (Fin n) (Fin n) ℝ) :
    Matrix.frobeniusNorm A = 0 ↔ A = 0 := by
  unfold Matrix.frobeniusNorm
  rw [Real.sqrt_eq_zero (Matrix.frobeniusInner_self_nonneg A)]
  exact Matrix.frobeniusInner_self_eq_zero_iff A

end QOU.MathlibExt.FrobeniusInnerProduct
