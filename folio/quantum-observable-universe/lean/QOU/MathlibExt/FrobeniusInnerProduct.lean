import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

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
- `QOU.MathlibExt.FrobeniusInnerProduct.frobeniusInner_symm` — symmetry.
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

namespace QOU.MathlibExt.FrobeniusInnerProduct

open Matrix

variable {n : ℕ}

/-- **Frobenius inner product** on `Matrix (Fin n) (Fin n) ℝ`,
    defined as `tr(A^T · B) = Σ_{ij} A_ij B_ij`.  The standard
    choice in matrix analysis. -/
def Matrix.frobeniusInner (A B : Matrix (Fin n) (Fin n) ℝ) : ℝ :=
  (A.transpose * B).trace

/-- **Symmetry** of the Frobenius inner product. -/
theorem frobeniusInner_symm (A B : Matrix (Fin n) (Fin n) ℝ) :
    Matrix.frobeniusInner A B = Matrix.frobeniusInner B A := by
  unfold Matrix.frobeniusInner
  -- `tr M = tr Mᵀ`; apply to LHS, then expand the transpose of a
  -- product and collapse `Aᵀᵀ = A`.
  calc (A.transpose * B).trace
      = ((A.transpose * B).transpose).trace :=
        (Matrix.trace_transpose _).symm
    _ = (B.transpose * A.transpose.transpose).trace := by
        rw [Matrix.transpose_mul]
    _ = (B.transpose * A).trace := by
        rw [Matrix.transpose_transpose]

/-- **Non-negativity on the diagonal**: `⟨A, A⟩_F = Σ A_ij² ≥ 0`. -/
theorem Matrix.frobeniusInner_self_nonneg (A : Matrix (Fin n) (Fin n) ℝ) :
    0 ≤ Matrix.frobeniusInner A A := by
  unfold Matrix.frobeniusInner Matrix.trace
  apply Finset.sum_nonneg
  intro i _
  show 0 ≤ (A.transpose * A) i i
  rw [Matrix.mul_apply]
  apply Finset.sum_nonneg
  intro k _
  rw [Matrix.transpose_apply]
  exact mul_self_nonneg (A k i)

/-- **Non-degeneracy**: `⟨A, A⟩_F = 0` iff `A = 0`. -/
theorem Matrix.frobeniusInner_self_eq_zero_iff
    (A : Matrix (Fin n) (Fin n) ℝ) :
    Matrix.frobeniusInner A A = 0 ↔ A = 0 := by
  refine ⟨?_, ?_⟩
  · intro h
    -- Forward: `tr(Aᵀ · A) = Σ_{i'} Σ_k (A k i')² = 0` ⟹ each
    -- `A k i' = 0` for all (k, i') ⟹ `A = 0`.  The double-sum
    -- analysis specialises to the goal `A i j = 0` by setting
    -- `k := i`, `i' := j` in the universal "all entries zero".
    ext i j
    have h_unfold : (∑ i' : Fin n, ∑ k : Fin n, (A k i') * (A k i')) = 0 := by
      simpa [Matrix.frobeniusInner, Matrix.trace, Matrix.mul_apply,
             Matrix.transpose_apply] using h
    -- Specialise the outer sum at `i' := j`.
    have h_at_j : (∑ k : Fin n, (A k j) * (A k j)) = 0 := by
      apply (Finset.sum_eq_zero_iff_of_nonneg
        (fun i'' _ => Finset.sum_nonneg
          (fun k _ => mul_self_nonneg (A k i'')))).mp h_unfold j (Finset.mem_univ _)
    -- Specialise the inner sum at `k := i`.
    have h_entry : (A i j) * (A i j) = 0 :=
      (Finset.sum_eq_zero_iff_of_nonneg
        (fun k _ => mul_self_nonneg (A k j))).mp h_at_j i (Finset.mem_univ _)
    -- `x * x = 0 ⟹ x = 0` (over ℝ, no zero-divisors).
    show A i j = (0 : Matrix _ _ ℝ) i j
    simpa using mul_self_eq_zero.mp h_entry
  · intro h
    rw [h]
    unfold Matrix.frobeniusInner
    simp

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
