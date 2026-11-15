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

/-- **PSD diagonal entries are non-negative**.  Mathlib's standard
    fact, restated here for direct use. -/
theorem Matrix.PosSemidef.diag_nonneg
    {C : Matrix (Fin n) (Fin n) ℝ} (hC : C.PosSemidef) (i : Fin n) :
    0 ≤ C i i := by
  -- C_ii = e_iᵀ · C · e_i ≥ 0 by PSD applied to canonical basis vector.
  have h_psd_ei := hC.2 (Pi.single i (1 : ℝ))
  have h_compute : dotProduct (star (Pi.single i (1 : ℝ)))
      (C.mulVec (Pi.single i (1 : ℝ))) = C i i := by
    simp [dotProduct, Matrix.mulVec, Pi.single_apply,
          Finset.sum_ite_eq', star_trivial, mul_ite, mul_one,
          mul_zero, Finset.mem_univ]
  rwa [h_compute] at h_psd_ei

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
  classical
  refine ⟨?_, fun h => by rw [h]; exact Matrix.trace_zero (Fin n) ℝ⟩
  intro h_trace
  -- LIGHTWEIGHT spectral-theorem proof (no continuous-functional-calculus,
  -- no `Mathlib.Analysis.Matrix.Order` import — that import pulls a ~2300-
  -- module analysis cone that is unbuildable in CI budget).  We diagonalise
  -- `A = U · D · Uᴴ` and reduce the claim to the diagonal-zero ⟹ row/col-zero
  -- lemma already proven in `QOU.MathlibExt.PosSemidefDiagZero`.
  --
  -- Strategy:
  --   A = U D Uᴴ  (spectral theorem, U unitary, D = diag(eigenvalues) ≥ 0).
  --   Set C := Uᴴ · B · U  (PSD, by congruence of PSD `B`).
  --   tr(A · B) = tr(U D Uᴴ B) = tr(D · (Uᴴ B U)) = tr(D · C) = Σ ev_i · C_ii.
  --   Each summand ≥ 0 (ev_i ≥ 0, C_ii ≥ 0); sum 0 ⟹ each ev_i · C_ii = 0.
  --   D · C = 0:  entry (i,j) is ev_i · C_ij.  Where ev_i = 0 the row is 0;
  --     where ev_i > 0, ev_i · C_ii = 0 ⟹ C_ii = 0 ⟹ (PSD diag-zero ⟹
  --     row-zero) C_ij = 0.  So every entry vanishes.
  --   A · B = U · D · Uᴴ · B = U · (D · C) · Uᴴ = U · 0 · Uᴴ = 0.
  set hAh := hA.1 with hAh_def
  set U : Matrix (Fin n) (Fin n) ℝ :=
    ((hAh.eigenvectorUnitary : Matrix.unitaryGroup (Fin n) ℝ) : Matrix (Fin n) (Fin n) ℝ)
    with hU_def
  set ev : Fin n → ℝ := hAh.eigenvalues with hev_def
  set D : Matrix (Fin n) (Fin n) ℝ := Matrix.diagonal (RCLike.ofReal ∘ ev) with hD_def
  -- Over `ℝ`, `RCLike.ofReal = id`, so `D = diagonal ev`.
  have hD_ev : D = Matrix.diagonal ev := by
    simp only [hD_def, Function.comp_def, RCLike.ofReal_real_eq_id, id_eq]
  -- Spectral theorem: `A = U * D * Uᴴ`.
  have hspec : A = U * D * Uᴴ := by
    rw [hU_def, hD_def, hev_def]
    exact hAh.spectral_theorem
  -- `U` is unitary: `Uᴴ * U = 1` and `U * Uᴴ = 1`.
  have hUstar : star (hAh.eigenvectorUnitary : Matrix (Fin n) (Fin n) ℝ) = Uᴴ := rfl
  have hUU : Uᴴ * U = 1 := by
    have := (hAh.eigenvectorUnitary).2
    rw [Matrix.mem_unitaryGroup_iff'] at this
    rw [hU_def]; simpa [hUstar] using this
  have hUUstar : U * Uᴴ = 1 := by
    have := (hAh.eigenvectorUnitary).2
    rw [Matrix.mem_unitaryGroup_iff] at this
    rw [hU_def]; simpa [hUstar] using this
  -- Congruence: `C := Uᴴ * B * U` is PSD.
  set C : Matrix (Fin n) (Fin n) ℝ := Uᴴ * B * U with hC_def
  have hC_psd : C.PosSemidef := by
    have := hB.conjTranspose_mul_mul_same U
    simpa [hC_def] using this
  -- Eigenvalues are non-negative (PSD).
  have hev_nonneg : ∀ i, 0 ≤ ev i := fun i => hA.eigenvalues_nonneg i
  -- Diagonal of `C` is non-negative (PSD).
  have hCdiag_nonneg : ∀ i, 0 ≤ C i i :=
    fun i => Matrix.PosSemidef.diag_nonneg hC_psd i
  -- `tr(A * B) = tr(D * C) = Σ_i ev_i * C_ii`.
  have htrace_eq : (A * B).trace = ∑ i, ev i * C i i := by
    have h1 : (A * B).trace = (D * C).trace := by
      rw [hspec, hC_def]
      -- tr((U*D*Uᴴ)*B) = tr(U*(D*Uᴴ*B)) = tr((D*Uᴴ*B)*U) = tr(D*(Uᴴ*B*U)) = tr(D*C)
      have e1 : U * D * Uᴴ * B = U * (D * Uᴴ * B) := by
        simp only [Matrix.mul_assoc]
      have e2 : D * Uᴴ * B * U = D * (Uᴴ * B * U) := by
        simp only [Matrix.mul_assoc]
      rw [e1, Matrix.trace_mul_comm U (D * Uᴴ * B), e2]
    rw [h1]
    -- (D * C).trace = ∑ i, ev i * C i i, with D = diagonal ev.
    rw [hD_ev, Matrix.trace]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Matrix.diag_apply, Matrix.mul_apply]
    -- ∑ k, diagonal ev i k * C k i = ev i * C i i
    rw [Finset.sum_eq_single i]
    · rw [Matrix.diagonal_apply_eq]
    · intro k _ hki
      rw [Matrix.diagonal_apply_ne ev (Ne.symm hki), zero_mul]
    · intro h; exact absurd (Finset.mem_univ i) h
  -- Each summand is non-negative.
  have hsummand_nonneg : ∀ i ∈ Finset.univ, 0 ≤ ev i * C i i :=
    fun i _ => mul_nonneg (hev_nonneg i) (hCdiag_nonneg i)
  -- Sum is zero ⟹ each summand is zero.
  have hsummand_zero : ∀ i, ev i * C i i = 0 := by
    have hsum_zero : ∑ i, ev i * C i i = 0 := htrace_eq ▸ h_trace
    intro i
    exact (Finset.sum_eq_zero_iff_of_nonneg hsummand_nonneg).mp hsum_zero i (Finset.mem_univ i)
  -- `D * C = 0`.
  have hDC_zero : D * C = 0 := by
    rw [hD_ev]
    ext i j
    rw [Matrix.diagonal_mul]
    simp only [Matrix.zero_apply]
    by_cases hev0 : ev i = 0
    · rw [hev0, zero_mul]
    · -- ev i ≠ 0 ⟹ C i i = 0 (from ev_i · C_ii = 0) ⟹ C i j = 0 (PSD row-zero).
      have hCii : C i i = 0 := by
        rcases mul_eq_zero.mp (hsummand_zero i) with h | h
        · exact absurd h hev0
        · exact h
      have hCij : C i j = 0 :=
        QOU.MathlibExt.PosSemidefDiagZero.Matrix.PosSemidef.row_zero_of_diag_zero
          hC_psd hCii j
      rw [hCij, mul_zero]
  -- `A * B = U * (D * C) * Uᴴ = 0`.
  calc A * B
      = (U * D * Uᴴ) * B := by rw [← hspec]
    _ = U * D * (Uᴴ * B) := by rw [Matrix.mul_assoc]
    _ = U * D * (Uᴴ * B * (U * Uᴴ)) := by rw [hUUstar, Matrix.mul_one]
    _ = U * (D * (Uᴴ * B * U)) * Uᴴ := by
          simp only [← Matrix.mul_assoc]
    _ = U * (D * C) * Uᴴ := by rw [hC_def]
    _ = U * 0 * Uᴴ := by rw [hDC_zero]
    _ = 0 := by rw [Matrix.mul_zero, Matrix.zero_mul]

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
-- Ref: [boyd-vandenberghe-2004] §5.5.2 ("Complementary slackness")
--      — Verified against the local PDF (library/boyd-vandenberghe-2004-…):
--      §5.5.2 is Complementary slackness; §5.5.3 is KKT optimality. The
--      `tr(S·Φ)=0 ⟹ S·Φ=0` bridge identity is the complementary-slackness
--      formulation specialised to the SDP cone.
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
  simpa [Matrix.mul_apply, Matrix.mulVec, dotProduct] using this

end QOU.MathlibExt.PosSemidefTraceZero
