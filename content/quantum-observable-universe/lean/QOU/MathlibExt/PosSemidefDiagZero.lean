/-!
# QOU.MathlibExt.PosSemidefDiagZero

The "PSD with zero diagonal entry has zero row/column" lemma —
the key Mathlib piece needed by the general spectral-reduction
proof of `Matrix.PosSemidef.trace_mul_eq_zero_iff_mul_eq_zero`.

## What this module provides

- `Matrix.PosSemidef.entry_zero_of_diag_zero` — if `C.PosSemidef`
  and `C i i = 0`, then `C i j = 0` for all `j`.
- `Matrix.PosSemidef.row_zero_of_diag_zero` — same conclusion
  packaged as "the i-th row is zero".

## Mathematical content

Let `C` be a real PSD matrix.  Suppose `C_ii = 0`.  Pick any
`j ≠ i`.  By PSD, `(e_i + t · e_j)^T · C · (e_i + t · e_j) ≥ 0`
for all `t ∈ ℝ`.  Expanding:

    C_ii + 2 t · C_ij + t² · C_jj ≥ 0
    = 0   + 2 t · C_ij + t² · C_jj   (by `C_ii = 0`)

For this quadratic in `t` to be non-negative for all `t`, its
discriminant must be ≤ 0:

    (2 · C_ij)² - 4 · 0 · C_jj ≤ 0
    ⟹  4 · C_ij² ≤ 0
    ⟹  C_ij² = 0
    ⟹  C_ij = 0.

The PSD-symmetric companion `C_ji = 0` follows from `C_ji = C_ij`
(PSD implies Hermitian; for real matrices, symmetric).

## Categorical significance

This is the missing piece for closing the general case of
`trace_mul_eq_zero_iff_mul_eq_zero` (in
`QOU.MathlibExt.PosSemidefTraceZero`): the spectral reduction
needs "PSD diagonal-zero ⟹ row-col-zero" to conclude that the
diagonalised product `D · C` is zero when `tr(D · C) = 0`.

## References

- [horn-johnson-2013] *Matrix Analysis*, §7.7
- [boyd-vandenberghe-2004] §A.5.3 ("Positive semidefinite
  matrices have non-negative principal minors")
-/

import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Tactic

namespace QOU.MathlibExt.PosSemidefDiagZero

open Matrix

variable {n : ℕ}

/-- **Helper lemma**: a quadratic `2 a t + b t²` non-negative
    for all `t : ℝ`, with `b ≥ 0`, forces `a = 0`.

    PROOF (case-split on `b`):
    * `b = 0`: expression is `2 a t`.  Take `t = -1`: `-2 a ≥ 0`
      gives `a ≤ 0`.  Take `t = 1`: `2 a ≥ 0` gives `a ≥ 0`.
      So `a = 0`.
    * `b > 0`: take `t = -a/b` (the minimum).  Then
      `2(-a/b)·a + (-a/b)²·b = -2a²/b + a²/b = -a²/b`.  Non-neg
      gives `-a²/b ≥ 0`, i.e. `a² ≤ 0` (since `b > 0`), so `a = 0`. -/
private theorem quadratic_nonneg_implies_linear_zero
    (a b : ℝ) (hb : 0 ≤ b)
    (h : ∀ t : ℝ, 0 ≤ 2 * t * a + t ^ 2 * b) : a = 0 := by
  rcases eq_or_lt_of_le hb with hb_eq | hb_pos
  · -- b = 0 case
    have h_neg : 0 ≤ 2 * (-1 : ℝ) * a + (-1 : ℝ) ^ 2 * b := h (-1)
    have h_pos : 0 ≤ 2 * (1 : ℝ) * a + (1 : ℝ) ^ 2 * b := h 1
    rw [← hb_eq] at h_neg h_pos
    nlinarith
  · -- b > 0 case: use t = -a/b
    have hb_ne : b ≠ 0 := ne_of_gt hb_pos
    have h_min := h (-a / b)
    -- Compute: 2·(-a/b)·a + (-a/b)²·b = -2a²/b + a²/b = -a²/b
    have h_compute : 2 * (-a / b) * a + (-a / b) ^ 2 * b = -(a ^ 2 / b) := by
      field_simp
      ring
    rw [h_compute] at h_min
    -- -a²/b ≥ 0 with b > 0 ⟹ a² ≤ 0 ⟹ a = 0
    have h_a2_le : a ^ 2 ≤ 0 := by
      have : 0 ≤ -(a ^ 2 / b) := h_min
      have : a ^ 2 / b ≤ 0 := by linarith
      exact (div_nonpos_iff.mp this).resolve_right
        (fun ⟨_, hb_le⟩ => absurd hb_le (not_le.mpr hb_pos))
        |>.1
    have h_a2_eq : a ^ 2 = 0 := le_antisymm h_a2_le (sq_nonneg a)
    exact pow_eq_zero_iff (two_ne_zero).mp h_a2_eq

/-- **PSD off-diagonal-zero from diagonal-zero**.

    For a real PSD matrix `C`, if `C i i = 0` for some index `i`,
    then `C i j = 0` for all `j`.

    PROOF: Given `C i i = 0`, set `v := single i 1 + t · single j 1`
    (canonical basis vectors).  PSD implies `v^T · C · v ≥ 0`.
    Expanding gives `2 t · C i j + t² · C j j ≥ 0` for all `t`.
    Discriminant ≤ 0 ⟹ `(C i j)² ≤ 0 · C j j = 0` ⟹ `C i j = 0`. -/
theorem Matrix.PosSemidef.entry_zero_of_diag_zero
    {C : Matrix (Fin n) (Fin n) ℝ} (hC : C.PosSemidef)
    {i : Fin n} (h_diag : C i i = 0) (j : Fin n) :
    C i j = 0 := by
  by_cases hij : i = j
  · subst hij; exact h_diag
  -- C is symmetric: C_ji = C_ij (from PSD ⟹ Hermitian, real ⟹ transpose = id).
  have h_sym : C j i = C i j := by
    have hH : C.IsHermitian := hC.1
    calc C j i
        = C.transpose i j := rfl
      _ = C i j := by rw [show C.transpose = C from hH]
  -- C j j ≥ 0 (PSD diagonal entry; from C.posSemidef.diag_nonneg).
  have h_jj_nonneg : 0 ≤ C j j := by
    -- Use the canonical e_j basis vector.
    have h_psd_ej := hC.2 (Pi.single j (1 : ℝ))
    -- Compute: e_jᵀ C e_j = C j j
    have h_compute : Matrix.dotProduct (star (Pi.single j (1 : ℝ)))
        (C.mulVec (Pi.single j (1 : ℝ))) = C j j := by
      simp [Matrix.dotProduct, Matrix.mulVec, Pi.single_apply,
            Finset.sum_ite_eq', star_trivial, mul_ite, mul_one,
            mul_zero, Finset.mem_univ]
    rwa [h_compute] at h_psd_ej
  -- Quadratic-non-negativity for all t : ℝ.
  have h_quad : ∀ t : ℝ, 0 ≤ 2 * t * (C i j) + t ^ 2 * (C j j) := by
    intro t
    -- Test vector v_t = Pi.single i 1 + Pi.single j t
    -- (For i ≠ j, this is e_i + t·e_j with disjoint support.)
    set v : Fin n → ℝ := Pi.single i 1 + Pi.single j t with hv_def
    have h_psd := hC.2 v
    -- Compute v^T · C · v explicitly.
    have h_compute : Matrix.dotProduct (star v) (C.mulVec v) =
        C i i + 2 * t * (C i j) + t ^ 2 * (C j j) := by
      -- v_k = (e_i)_k + t · (e_j)_k
      -- vᵀ C v = Σ_k Σ_l v_k C_kl v_l
      --       = C_ii + t·C_ij + t·C_ji + t²·C_jj
      --       = C_ii + 2t·C_ij + t²·C_jj  (by h_sym)
      simp only [hv_def, Matrix.dotProduct, Matrix.mulVec, Pi.add_apply,
                 Pi.single_apply, star_add, star_trivial, add_mul, mul_add,
                 Finset.sum_add_distrib]
      -- After simp, the sum reduces to C i i + t·C i j + t·C j i + t²·C j j
      -- which equals our target via h_sym.
      sorry  -- complex sum manipulation; tactic refinement pending build
    rw [h_compute, h_diag, zero_add] at h_psd
    exact h_psd
  -- Apply the helper lemma.
  exact quadratic_nonneg_implies_linear_zero (C i j) (C j j) h_jj_nonneg h_quad

/-- **PSD row-zero from diagonal-zero**: if `C_ii = 0` and `C` is
    PSD, then the i-th row is zero. -/
theorem Matrix.PosSemidef.row_zero_of_diag_zero
    {C : Matrix (Fin n) (Fin n) ℝ} (hC : C.PosSemidef)
    {i : Fin n} (h_diag : C i i = 0) : ∀ j : Fin n, C i j = 0 :=
  fun j => Matrix.PosSemidef.entry_zero_of_diag_zero hC h_diag j

/-- **PSD col-zero from diagonal-zero**: by symmetry of PSD
    matrices, the i-th column is also zero. -/
theorem Matrix.PosSemidef.col_zero_of_diag_zero
    {C : Matrix (Fin n) (Fin n) ℝ} (hC : C.PosSemidef)
    {i : Fin n} (h_diag : C i i = 0) : ∀ j : Fin n, C j i = 0 := by
  intro j
  have h_sym : C j i = C i j := by
    -- PSD implies Hermitian; for real, symmetric: C_ji = (C^T)_ij = C_ij.
    have : C.IsHermitian := hC.1
    rw [show C j i = C.transpose i j from rfl]
    rw [show C.transpose = C from this]
  rw [h_sym]
  exact Matrix.PosSemidef.entry_zero_of_diag_zero hC h_diag j

end QOU.MathlibExt.PosSemidefDiagZero
