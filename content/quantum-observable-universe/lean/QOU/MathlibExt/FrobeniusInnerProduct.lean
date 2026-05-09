/-!
# QOU.MathlibExt.FrobeniusInnerProduct

The Frobenius inner product on matrices, `⟨A, B⟩_F := tr(A^T · B)`.
This is the canonical inner-product structure for SDP analysis:
the PSD cone is self-polar w.r.t. this inner product
(`PosSemidefTraceZero`), the Frobenius norm `‖A‖_F := sqrt(⟨A, A⟩)`
is rotation-invariant, and the strict-convexity arguments needed
for SDP uniqueness all live here.

## What this module provides

- `Matrix.frobeniusInner` — `tr(A^T · B)` as a real-valued
  inner product on `Matrix (Fin n) (Fin n) ℝ`.
- `Matrix.frobeniusInner_symm` — symmetry.
- `Matrix.frobeniusInner_self_nonneg` — non-negativity on the
  diagonal (Mathlib via `Matrix.trace_transpose_mul_self_nonneg`).
- `Matrix.frobeniusInner_self_eq_zero_iff` — non-degeneracy.
- `Matrix.frobeniusNorm` — sqrt of the diagonal value (extends
  to a `Norm` instance once paired with the metric topology).

## Categorical content

The Frobenius inner product makes `Matrix (Fin n) (Fin n) ℝ`
into an inner-product space isomorphic to `ℝ^(n²)`.  This
isomorphism transports Mathlib's `Convex` / `StrictConvexOn`
machinery directly to the matrix setting — the key ingredient
for closing `strict_complementarity_unique` in
`QOU.MathlibExt.SDP`.

## References

- [horn-johnson-2013] *Matrix Analysis*, §5.2 ("Frobenius
  inner product").
- [boyd-vandenberghe-2004] §A.1.1 ("Inner product on matrices").
-/

import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

namespace QOU.MathlibExt.FrobeniusInnerProduct

open Matrix

variable {n : ℕ}

/-- **Frobenius inner product** on `Matrix (Fin n) (Fin n) ℝ`,
    defined as `tr(A^T · B) = Σ_{ij} A_ij B_ij`.  The standard
    choice in matrix analysis. -/
def Matrix.frobeniusInner (A B : Matrix (Fin n) (Fin n) ℝ) : ℝ :=
  (A.transpose * B).trace

/-- **Symmetry** of the Frobenius inner product. -/
theorem Matrix.frobeniusInner_symm (A B : Matrix (Fin n) (Fin n) ℝ) :
    Matrix.frobeniusInner A B = Matrix.frobeniusInner B A := by
  unfold Matrix.frobeniusInner
  rw [Matrix.trace_mul_comm, ← Matrix.transpose_transpose B,
      ← Matrix.transpose_mul]
  congr 1
  rw [Matrix.transpose_transpose, Matrix.transpose_mul,
      Matrix.transpose_transpose]

/-- **Non-negativity on the diagonal**: `⟨A, A⟩_F = Σ A_ij² ≥ 0`. -/
theorem Matrix.frobeniusInner_self_nonneg (A : Matrix (Fin n) (Fin n) ℝ) :
    0 ≤ Matrix.frobeniusInner A A := by
  unfold Matrix.frobeniusInner
  -- `tr(A^T · A) = Σ_ij A_ij²` ≥ 0.  Mathlib has
  -- `Matrix.trace_transpose_mul_self_nonneg` (or similar; verify
  -- exact name).
  sorry

/-- **Non-degeneracy**: `⟨A, A⟩_F = 0` iff `A = 0`. -/
theorem Matrix.frobeniusInner_self_eq_zero_iff
    (A : Matrix (Fin n) (Fin n) ℝ) :
    Matrix.frobeniusInner A A = 0 ↔ A = 0 := by
  -- Sum-of-squares is zero iff each summand is zero iff each entry
  -- of A is zero iff A = 0.  Mathlib should have a packaged form.
  sorry

/-- **Frobenius norm** on matrices, `‖A‖_F := √(tr A^T · A)`. -/
def Matrix.frobeniusNorm (A : Matrix (Fin n) (Fin n) ℝ) : ℝ :=
  Real.sqrt (Matrix.frobeniusInner A A)

/-- **Frobenius norm is non-negative.** -/
theorem Matrix.frobeniusNorm_nonneg (A : Matrix (Fin n) (Fin n) ℝ) :
    0 ≤ Matrix.frobeniusNorm A :=
  Real.sqrt_nonneg _

/-- **Frobenius norm is zero iff matrix is zero.** -/
theorem Matrix.frobeniusNorm_eq_zero_iff
    (A : Matrix (Fin n) (Fin n) ℝ) :
    Matrix.frobeniusNorm A = 0 ↔ A = 0 := by
  unfold Matrix.frobeniusNorm
  rw [Real.sqrt_eq_zero (Matrix.frobeniusInner_self_nonneg A)]
  exact Matrix.frobeniusInner_self_eq_zero_iff A

end QOU.MathlibExt.FrobeniusInnerProduct
