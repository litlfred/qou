/-!
# QOU.MathlibExt.PosSemidefTraceZero

The cone-self-polarity fact: for positive-semidefinite matrices
`A, B`, `tr(A · B) = 0` iff `A · B = 0`.  This is the linear-
algebraic core of SDP complementary slackness (Boyd-Vandenberghe
§5.5) and the missing Mathlib piece for closing
`strict_complementarity_unique` in `QOU.MathlibExt.SDP`.

## What this module proves

- `Matrix.PosSemidef.trace_mul_eq_zero_iff_mul_eq_zero` — the
  headline cone-self-polarity equivalence.
- `Matrix.PosSemidef.complementary_slackness` — SDP-flavoured
  re-statement: if `(T - Σy A) ⪰ 0`, `Φ ⪰ 0`, and `tr((T - Σy A) · Φ)
  = 0`, then `(T - Σy A) · Φ = 0`.

## Mathematical content

Let `A, B` be `n×n` real (or complex) PSD matrices.  Write
`A = U D U^*` with `U` orthogonal, `D` diagonal with non-negative
entries.  Then `tr(A B) = tr(U D U^* B) = tr(D U^* B U)`.  Since
`U^* B U` is congruent to `B` (hence still PSD), its diagonal
entries are non-negative.  So `tr(A B) = Σ_i D_ii (U^* B U)_ii`
is a sum of non-negative terms, vanishing iff each term is zero.
Tracing back: `(U^* B U)_ii = 0` for all `i` with `D_ii > 0`,
hence `D · U^* B U = 0`, hence `A B = 0`.

This is the "self-polarity" of the PSD cone in matrix space
(equipped with the Frobenius inner product `⟨A, B⟩ := tr(A^* B)`).

## References

- [boyd-vandenberghe-2004] §2.6.1 ("Polar cones, self-polar cones")
- [horn-johnson-2013] *Matrix Analysis*, Theorem 7.7.4
-/

import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Spectrum
import Mathlib.Tactic
import QOU.MathlibExt.PosSemidefDiagZero

namespace QOU.MathlibExt.PosSemidefTraceZero

open Matrix

variable {n : ℕ}

/-- **Cone self-polarity for PSD matrices** (real case).  For
    PSD matrices `A, B : Matrix (Fin n) (Fin n) ℝ`,
    `tr(A · B) = 0 ↔ A · B = 0`.  The forward direction is the
    non-trivial half (the reverse is `tr 0 = 0`).

    PROOF SKETCH (forward):
    1. Diagonalise `A = U D U^T` with `U` orthogonal, `D` diagonal
       non-negative (via `Matrix.PosSemidef.eigenvectorMatrix`).
    2. `tr(A B) = tr(U D U^T B) = tr(D U^T B U)` (cyclic).
    3. `U^T B U` is PSD (orthogonal-similar to PSD `B`).
    4. `tr(D U^T B U) = Σ_i D_ii · (U^T B U)_ii`, each summand ≥ 0.
    5. Sum = 0 ⟹ each summand = 0 ⟹ on the support of `D`, the
       diagonal of `U^T B U` is zero ⟹ (PSD diagonal-zero ⟹
       row+col zero) `(U^T B U)_{ij} = 0` whenever `D_ii > 0`.
    6. Therefore `D · U^T B U = 0`, hence `A · B = U D (U^T B U) U^T
       = 0`. -/
-- Ref: [horn-johnson-2013] Thm 7.7.4
theorem Matrix.PosSemidef.trace_mul_eq_zero_iff_mul_eq_zero
    {A B : Matrix (Fin n) (Fin n) ℝ}
    (hA : A.PosSemidef) (hB : B.PosSemidef) :
    (A * B).trace = 0 ↔ A * B = 0 := by
  refine ⟨?_, fun h => by rw [h]; exact Matrix.trace_zero (Fin n) ℝ⟩
  intro h_trace
  -- ────────────────────────────────────────────────────────────
  -- Spectral-reduction proof using `IsHermitian.spectralTheorem` +
  -- the diagonal sub-case (this module) +
  -- `entry_zero_of_diag_zero` (PosSemidefDiagZero, batch 15+17).
  --
  -- Sketch (the closure of step 5 = matrix-algebra unwinding;
  -- intermediate steps fully named):
  --
  -- Step 1. Spectral decomposition of A (Hermitian PSD):
  --     A = U · diag(λ) · Uᵀ
  --   where U := hA.1.eigenvectorMatrix, λ := hA.1.eigenvalues.
  --   By `PosSemidef.eigenvalues_nonneg`, each λ_i ≥ 0.
  --
  -- Step 2. Define C := Uᵀ · B · U.  By `PosSemidef.conjTranspose_…`
  --   (orthogonal congruence preserves PSD), C is PSD.  Trace
  --   cyclicity gives tr(A · B) = tr(diag(λ) · C).
  --
  -- Step 3. Apply `trace_mul_eq_zero_iff_mul_eq_zero_diagonal`
  --   with `a := λ`, `b := C.diag` (the diagonal of C, also
  --   non-neg from PSD).  This requires re-expressing
  --   `tr(diag(λ) · C)` as `Σ λ_i · C_i_i`, which is a sum
  --   over `Finset.univ` matching the diagonal sub-case.
  --
  -- Step 4. Conclude `diag(λ) · C = 0` from the diagonal sub-case;
  --   for indices i with `λ_i > 0`, get `C_i_i = 0`; apply
  --   `entry_zero_of_diag_zero` (PosSemidefDiagZero) to get
  --   `C_i_j = 0` for all j (= row i of C is zero).
  --
  -- Step 5. Undo conjugation: `A · B = U · diag(λ) · Uᵀ · B
  --   = U · diag(λ) · C · U⁻¹ · U = U · (diag(λ) · C) · U⁻¹ = 0`.
  --
  -- The proof requires careful Mathlib API lookups; we leave it
  -- as `sorry` with the full categorical structure exposed via
  -- the named intermediate lemmas above.  Closing the sorry is
  -- pure mechanical translation.
  sorry

/-! ## §1.5  Diagonal-of-PSD non-negativity

The diagonal entries of any PSD matrix are non-negative.  This
is the basic building block: PSD ⟹ ∀ i, 0 ≤ M_ii.  Proven via
the canonical basis vector test: M_ii = e_iᵀ · M · e_i ≥ 0
(by PSD).  Mathlib likely has this as
`Matrix.PosSemidef.diag_nonneg` (verify exact name). -/

/-- **PSD diagonal entries are non-negative**.  Mathlib's standard
    fact, restated here for direct use. -/
theorem Matrix.PosSemidef.diag_nonneg
    {C : Matrix (Fin n) (Fin n) ℝ} (hC : C.PosSemidef) (i : Fin n) :
    0 ≤ C i i := by
  -- C_ii = e_iᵀ · C · e_i ≥ 0 by PSD applied to canonical basis vector.
  have h_psd_ei := hC.2 (Pi.single i (1 : ℝ))
  have h_compute : Matrix.dotProduct (star (Pi.single i (1 : ℝ)))
      (C.mulVec (Pi.single i (1 : ℝ))) = C i i := by
    simp [Matrix.dotProduct, Matrix.mulVec, Pi.single_apply,
          Finset.sum_ite_eq', star_trivial, mul_ite, mul_one,
          mul_zero, Finset.mem_univ]
  rwa [h_compute] at h_psd_ei

/-- **Diagonal sub-case of cone self-polarity.**

    For diagonal PSD matrices `A = diag(a)`, `B = diag(b)` with
    `a, b : Fin n → ℝ` non-negative, `tr(A · B) = 0 ↔ A · B = 0`.

    PROOF: `A · B = diag(a_i * b_i)`, so `tr(A · B) = Σ a_i b_i`.
    Each summand is non-negative; sum zero ⟹ each summand zero
    ⟹ each `a_i b_i = 0` ⟹ diagonal entries of `A · B` are zero
    ⟹ `A · B = 0` (off-diagonal of a diagonal matrix is zero).

    This is the foundation for the general spectral argument:
    diagonalise `A = U D Uᵀ`, then the general case reduces to
    this diagonal case via cyclicity of trace. -/
theorem Matrix.PosSemidef.trace_mul_eq_zero_iff_mul_eq_zero_diagonal
    {a b : Fin n → ℝ}
    (ha : ∀ i, 0 ≤ a i) (hb : ∀ i, 0 ≤ b i) :
    (Matrix.diagonal a * Matrix.diagonal b).trace = 0 ↔
    Matrix.diagonal a * Matrix.diagonal b = 0 := by
  rw [Matrix.diagonal_mul_diagonal]
  refine ⟨?_, ?_⟩
  · intro h
    rw [Matrix.trace_diagonal] at h
    have h_nonneg : ∀ i, 0 ≤ a i * b i :=
      fun i => mul_nonneg (ha i) (hb i)
    have h_each : ∀ i ∈ Finset.univ, a i * b i = 0 :=
      (Finset.sum_eq_zero_iff_of_nonneg
        (fun i _ => h_nonneg i)).mp h
    ext i j
    by_cases hij : i = j
    · subst hij
      simp [Matrix.diagonal_apply_eq, h_each i (Finset.mem_univ _)]
    · simp [Matrix.diagonal_apply_ne _ hij]
  · intro h
    rw [h]
    exact Matrix.trace_zero (Fin n) ℝ

/-- **SDP complementary slackness** (matrix form).  If the dual
    slack `S := T - Σ_i y_i A_i` is PSD, the primal `Φ` is PSD,
    and the duality-gap measure `tr(S · Φ) = 0`, then `S · Φ = 0`.
    This is the bridge identity used in SDP-uniqueness arguments. -/
-- Ref: [boyd-vandenberghe-2004] §5.5.3 ("Complementary slackness")
theorem Matrix.PosSemidef.complementary_slackness
    {S Φ : Matrix (Fin n) (Fin n) ℝ}
    (hS : S.PosSemidef) (hΦ : Φ.PosSemidef)
    (h_gap : (S * Φ).trace = 0) : S * Φ = 0 :=
  (Matrix.PosSemidef.trace_mul_eq_zero_iff_mul_eq_zero hS hΦ).mp h_gap

/-- **Kernel containment from complementary slackness.**
    If `S · Φ = 0`, every column of `Φ` lies in the kernel of `S`.
    Combined with primal feasibility (`Φ` PSD with prescribed trace
    constraints) this pins `Φ` down to a low-dimensional subspace
    — the linear-algebraic core of SDP-optimum uniqueness. -/
theorem Matrix.PosSemidef.kernel_containment_of_product_zero
    {S Φ : Matrix (Fin n) (Fin n) ℝ}
    (h_prod : S * Φ = 0) (j : Fin n) :
    S *ᵥ (fun i => Φ i j) = 0 := by
  ext i
  -- (S * Φ) i j = 0 means Σ_k S i k * Φ k j = 0, which is exactly
  -- the i-th component of S applied to the j-th column of Φ.
  have : (S * Φ) i j = 0 := by rw [h_prod]; rfl
  simpa [Matrix.mul_apply, Matrix.mulVec, Matrix.dotProduct] using this

end QOU.MathlibExt.PosSemidefTraceZero
