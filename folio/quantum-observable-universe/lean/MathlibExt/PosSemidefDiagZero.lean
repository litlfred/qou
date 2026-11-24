import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Tactic

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

- [horn-johnson-2013] *Matrix Analysis*, §7.7 (Schur complements +
  PSD det inequalities — the canonical authority for the
  PSD-has-nonneg-principal-minors lemma used here).
- [boyd-vandenberghe-2004] §A.5.5 (Schur complement; PSD block
  structure). Note: §A.5.3 in Boyd is "Generalized eigenvalue
  decomposition" — that section was previously cited here in error.
-/

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
      exact (div_nonpos_iff.mp this).resolve_left
        (fun ⟨_, hb_le⟩ => absurd hb_le (not_le.mpr hb_pos))
        |>.1
    have h_a2_eq : a ^ 2 = 0 := le_antisymm h_a2_le (sq_nonneg a)
    exact (pow_eq_zero_iff two_ne_zero).mp h_a2_eq

/-- **2-index quadratic form expansion (Horn–Johnson 2013 §7.7).**

    For a Hermitian matrix `C` and a two-support test vector
    `α · e_i + β · e_j`, the quadratic form expands to
    `α² C_ii + 2αβ C_ij + β² C_jj`.

    Proved directly: distribute `mulVec`/`dotProduct` over the two
    `Pi.single` summands (`mulVec_add`, `add_dotProduct`,
    `dotProduct_add`), collapse each `single` term (`mulVec_single`,
    `single_dotProduct`, `col_apply`, `op_smul_eq_mul`), identify
    `C j i = C i j` by Hermitian symmetry, and close with `ring`.
    (The identity in fact holds for all `i, j`; the `i ≠ j`
    hypothesis is retained for the call sites and is unused in the
    proof.)  Previously an `axiom` "pending Mathlib API
    stabilisation"; now discharged with the current API. -/
-- Ref: [horn-johnson-2013] *Matrix Analysis*, §7.7
private theorem quadratic_form_two_index
    {C : Matrix (Fin n) (Fin n) ℝ} (hH : C.IsHermitian)
    (α β : ℝ) {i j : Fin n} (_hij : i ≠ j) :
    dotProduct (star (Pi.single i α + Pi.single j β))
      (C.mulVec (Pi.single i α + Pi.single j β)) =
    α ^ 2 * C i i + 2 * α * β * C i j + β ^ 2 * C j j := by
  have hsymm : C j i = C i j := by simpa using hH.apply i j
  simp only [star_trivial, mulVec_add, dotProduct_add, add_dotProduct,
             mulVec_single, single_dotProduct, Pi.smul_apply, col_apply,
             op_smul_eq_mul]
  rw [hsymm]
  ring

/-- **Cauchy–Schwarz inequality for PSD entries** (Horn–Johnson 2013
    §7.7): for any real PSD matrix `C` and indices `i, j`,
    `(C_ij)² ≤ C_ii · C_jj`.

    Proved directly from the test-vector quadratic form: for `i ≠ j`,
    `v = x·e_i + e_j` gives `0 ≤ C_ii x² + 2 C_ij x + C_jj` for all
    `x` (PSD positivity + `quadratic_form_two_index`); a nonnegative
    real quadratic has nonpositive discriminant (`discrim_le_zero`),
    i.e. `(2 C_ij)² − 4 C_ii C_jj ≤ 0`, whence the bound.  The
    `i = j` case is `C_ii² ≤ C_ii²`.  Previously an `axiom` pending
    the Mathlib principal-submatrix-PSD API; now discharged. -/
-- Ref: [horn-johnson-2013] *Matrix Analysis*, §7.7
theorem Matrix.PosSemidef.entry_sq_le_diag_mul
    {C : Matrix (Fin n) (Fin n) ℝ} (hC : C.PosSemidef)
    (i j : Fin n) :
    (C i j) ^ 2 ≤ C i i * C j j := by
  rcases eq_or_ne i j with rfl | hij
  · nlinarith [sq_nonneg (C i i)]
  · have key : ∀ x : ℝ, 0 ≤ C i i * (x * x) + 2 * C i j * x + C j j := by
      intro x
      have h := hC.2 (Pi.single i x + Pi.single j 1)
      rw [quadratic_form_two_index hC.1 x 1 hij] at h
      nlinarith [h]
    have hd : discrim (C i i) (2 * C i j) (C j j) ≤ 0 := discrim_le_zero key
    simp only [discrim] at hd
    nlinarith [hd]

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
  -- ALTERNATIVE PROOF (cleaner): use the entry-wise Cauchy-Schwarz
  -- inequality for PSD matrices: `|C_ij|² ≤ C_ii · C_jj`.
  -- With `C_ii = 0`, this forces `C_ij² ≤ 0` ⟹ `C_ij = 0`.
  --
  -- Mathlib provides this either as:
  --   `Matrix.PosSemidef.entry_sq_le_diag_mul` (direct), or
  --   composed from `Matrix.PosSemidef.principalSubmatrix_posSemidef`
  --   + `Matrix.posSemidef_iff_self_inner_nonneg` + 2x2 det ≥ 0.
  --
  -- For now, provide both proof skeletons; commit the cleaner one
  -- using the test-vector approach at the bottom.

  -- Method 1: Cauchy-Schwarz on PSD entries.
  have h_cs : (C i j) ^ 2 ≤ C i i * C j j :=
    Matrix.PosSemidef.entry_sq_le_diag_mul hC i j
  rw [h_diag, zero_mul] at h_cs
  -- (C i j)² ≤ 0 AND ≥ 0 ⟹ = 0 ⟹ C i j = 0.
  have h_sq_eq : (C i j) ^ 2 = 0 :=
    le_antisymm h_cs (sq_nonneg _)
  exact (pow_eq_zero_iff two_ne_zero).mp h_sq_eq

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
