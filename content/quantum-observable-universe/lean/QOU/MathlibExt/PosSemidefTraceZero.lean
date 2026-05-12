import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Spectrum
import Mathlib.Tactic
import QOU.MathlibExt.PosSemidefDiagZero
import QOU.MathlibExt.FrobeniusInnerProduct

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
  -- Square-root proof (cleaner than spectral-theorem unrolling).
  -- Let A^{1/2} := hA.sqrt (Mathlib: PSD has unique PSD square root).
  -- Define M := A^{1/2} · B · A^{1/2} (PSD by sandwich).
  -- tr(M) = tr(A^{1/2}·B·A^{1/2}) = tr(A^{1/2}·A^{1/2}·B) = tr(A·B) = 0.
  -- M PSD with tr 0 ⟹ M = 0 (Mathlib: PSD trace-zero ⟹ zero matrix).
  -- Then (A^{1/2}·B^{1/2}) · (A^{1/2}·B^{1/2})^T = A^{1/2}·B·A^{1/2} = M = 0.
  -- X · X^T = 0 ⟹ X = 0 (Frobenius norm zero).
  -- So A^{1/2}·B^{1/2} = 0.
  -- A·B = (A^{1/2})² · (B^{1/2})² = A^{1/2} · (A^{1/2}·B^{1/2}) · B^{1/2} = 0.
  set Asqrt := hA.sqrt with hAsqrt_def
  set Bsqrt := hB.sqrt with hBsqrt_def
  have hAsq : Asqrt * Asqrt = A := hA.sq_sqrt
  have hBsq : Bsqrt * Bsqrt = B := hB.sq_sqrt
  have hAsqrt_psd : Asqrt.PosSemidef := hA.posSemidef_sqrt
  have hBsqrt_psd : Bsqrt.PosSemidef := hB.posSemidef_sqrt
  have hAsqrt_herm : Asqrt.IsHermitian := hAsqrt_psd.1
  have hBsqrt_herm : Bsqrt.IsHermitian := hBsqrt_psd.1
  -- Define X := Asqrt · Bsqrt.  Then X · X^T = Asqrt · B · Asqrt.
  set X := Asqrt * Bsqrt with hX_def
  have hXX_T : X * X.transpose = Asqrt * B * Asqrt := by
    rw [hX_def, Matrix.transpose_mul,
        show Bsqrt.transpose = Bsqrt from hBsqrt_herm,
        show Asqrt.transpose = Asqrt from hAsqrt_herm,
        Matrix.mul_assoc, ← Matrix.mul_assoc Bsqrt Bsqrt _, hBsq]
  -- tr(X · X^T) = tr(Asqrt · B · Asqrt) = tr(Asqrt² · B) = tr(A · B) = 0
  have hXX_T_trace_zero : (X * X.transpose).trace = 0 := by
    rw [hXX_T, Matrix.trace_mul_comm, ← Matrix.mul_assoc, hAsq]
    exact h_trace
  -- Direct closure via Frobenius inner product (proven in batch 10):
  -- tr(X · X^T) = tr(X^T · X) = frobeniusInner X X (def + trace cyclicity).
  -- frobeniusInner X X = 0 ⟹ X = 0 (`frobeniusInner_self_eq_zero_iff`,
  -- proven in `QOU.MathlibExt.FrobeniusInnerProduct`, batch 10).
  -- This sidesteps the PSD detour entirely.
  have hX_zero : X = 0 := by
    have h_fro : QOU.MathlibExt.FrobeniusInnerProduct.Matrix.frobeniusInner X X = 0 := by
      -- frobeniusInner X X = tr(X^T · X) = tr(X · X^T) (cyclic) = 0.
      show (X.transpose * X).trace = 0
      rw [Matrix.trace_mul_comm]
      exact hXX_T_trace_zero
    exact (QOU.MathlibExt.FrobeniusInnerProduct.Matrix.frobeniusInner_self_eq_zero_iff X).mp h_fro
  -- A · B = Asqrt² · Bsqrt² = Asqrt · (Asqrt · Bsqrt) · Bsqrt = Asqrt · X · Bsqrt
  --      = Asqrt · 0 · Bsqrt = 0.
  calc A * B
      = (Asqrt * Asqrt) * (Bsqrt * Bsqrt) := by rw [hAsq, hBsq]
    _ = (Asqrt * Asqrt * Bsqrt) * Bsqrt := by rw [Matrix.mul_assoc]
    _ = (Asqrt * (Asqrt * Bsqrt)) * Bsqrt := by rw [Matrix.mul_assoc Asqrt Asqrt Bsqrt]
    _ = (Asqrt * X) * Bsqrt := rfl
    _ = (Asqrt * 0) * Bsqrt := by rw [hX_zero]
    _ = 0 * Bsqrt := by rw [Matrix.mul_zero]
    _ = 0 := Matrix.zero_mul _

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
