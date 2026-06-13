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

/-- **External lemma (Horn–Johnson 2013 §7.7): 2-index quadratic
    form expansion.**

    For a Hermitian matrix `C` and a two-support test vector
    `α · e_i + β · e_j` (with `i ≠ j`), the quadratic form expands
    to `α² C_ii + 2αβ C_ij + β² C_jj`.

    Proof: expand `dotProduct` as a `Finset.sum`, collapse the four
    cross-terms via `Finset.sum_ite_eq'`, use Hermitian symmetry to
    identify `C j i = C i j`.  The mechanical unfolding involves
    Mathlib API names that have shifted between versions
    (`Matrix.dotProduct` → top-level `dotProduct`, `Pi.single`
    elaboration changes); recorded as an axiom pending the next
    Mathlib API stabilisation. -/
-- Ref: [horn-johnson-2013] *Matrix Analysis*, §7.7
theorem quadratic_form_two_index_axiom :
    ∀ {n : ℕ} {C : Matrix (Fin n) (Fin n) ℝ} (_hH : C.IsHermitian)
      (α β : ℝ) {i j : Fin n} (_hij : i ≠ j),
        dotProduct (star (Pi.single i α + Pi.single j β))
          (C.mulVec (Pi.single i α + Pi.single j β)) =
        α ^ 2 * C i i + 2 * α * β * C i j + β ^ 2 * C j j := by
  intro n C hH α β i j hij
  have hsymm : C j i = C i j := (hH j i).symm
  simp only [Matrix.dotProduct, Matrix.mulVec, Pi.single, starRingEnd_apply]
  simp only [star_add, star_trivial]
  simp only [mul_add, add_mul, Finset.sum_add_distrib, Finset.mul_sum, Finset.sum_mul]
  simp only [Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  have h_ne : (j = i) = False := eq_false_iff.mpr hij.symm
  have h_ne' : (i = j) = False := eq_false_iff.mpr hij
  simp only [h_ne, h_ne', if_false, mul_zero, zero_mul, add_zero, zero_add]
  calc
    α * (C i i * α) + α * (C i j * β) + (β * (C j i * α) + β * (C j j * β))
      = α ^ 2 * C i i + α * β * C i j + β * α * C j i + β ^ 2 * C j j := by ring
    _ = α ^ 2 * C i i + α * β * C i j + β * α * C i j + β ^ 2 * C j j := by rw [hsymm]
    _ = α ^ 2 * C i i + 2 * α * β * C i j + β ^ 2 * C j j := by ring

private theorem quadratic_form_two_index
    {C : Matrix (Fin n) (Fin n) ℝ} (hH : C.IsHermitian)
    (α β : ℝ) {i j : Fin n} (hij : i ≠ j) :
    dotProduct (star (Pi.single i α + Pi.single j β))
      (C.mulVec (Pi.single i α + Pi.single j β)) =
    α ^ 2 * C i i + 2 * α * β * C i j + β ^ 2 * C j j :=
  quadratic_form_two_index_axiom hH α β hij

/-- **External axiom (Horn–Johnson 2013 §7.7; Boyd–Vandenberghe
    2004 §A.5.3): Cauchy–Schwarz inequality for PSD entries.**

    For any real PSD matrix `C` and indices `i, j`, the entry-wise
    Cauchy–Schwarz bound holds: `(C_ij)² ≤ C_ii · C_jj`.

    Proof: 2x2 principal submatrix of PSD is PSD; PSD ⟹ det ≥ 0;
    det of the 2x2 submatrix is `C_ii · C_jj − C_ij²` (using
    `C_ji = C_ij` from Hermitian symmetry).  Axiomatised here
    pending the Mathlib API for principal-submatrix-PSD; the test-
    vector proof (`quadratic_form_two_index`) gives an alternative
    route. -/
-- Ref: [horn-johnson-2013] *Matrix Analysis*, §7.7 (Schur complements
--      + PSD det inequalities — primary authority for the
--      principal-submatrix lemma used here)
-- Ref: [boyd-vandenberghe-2004] §A.5.5 (Schur complement; PSD block
--      structure). Note: §A.5.3 (which was previously cited here) is
--      "Generalized eigenvalue decomposition" — irrelevant to this
--      diagonal-zero PSD lemma. Fixed during local-PDF verification.
theorem entry_sq_le_diag_mul_axiom :
    ∀ {n : ℕ} {C : Matrix (Fin n) (Fin n) ℝ} (_hC : C.PosSemidef)
      (i j : Fin n),
        (C i j) ^ 2 ≤ C i i * C j j := by
  intro n C hC i j
  by_cases hij : i = j
  · subst hij
    exact le_rfl
  have h_quad : ∀ α β : ℝ, 0 ≤ α ^ 2 * C i i + 2 * α * β * C i j + β ^ 2 * C j j := by
    intro α β
    have h_pos := hC.2 (Pi.single i α + Pi.single j β)
    have h_eq := quadratic_form_two_index_axiom hC.1 α β hij
    rw [h_eq] at h_pos
    exact h_pos
  by_cases h_diag : C i i = 0
  · have h_zero_ij : C i j = 0 := by
      have h_nonneg : ∀ t : ℝ, 0 ≤ 2 * t * C i j + t ^ 2 * C j j := by
        intro t
        have h_spec := h_quad 1 t
        rw [h_diag] at h_spec
        linarith
      have h_cjj : 0 ≤ C j j := by
        have h_spec2 := h_quad 0 1
        linarith
      exact quadratic_nonneg_implies_linear_zero (C i j) (C j j) h_cjj h_nonneg
    rw [h_zero_ij, h_diag]
    linarith
  · have h_cii_pos : 0 < C i i := by
      have h_spec := h_quad 1 0
      have : 0 ≤ C i i := by linarith
      exact lt_of_le_of_ne this (Ne.symm h_diag)
    have h_spec3 := h_quad (-C i j) (C i i)
    have h_ineq : 0 ≤ C i i * (C i i * C j j - (C i j) ^ 2) := by
      calc 0 ≤ (- C i j) ^ 2 * C i i + 2 * (- C i j) * C i i * C i j + C i i ^ 2 * C j j := h_spec3
           _ = C i i * (C i i * C j j - (C i j) ^ 2) := by ring
    have h_ineq2 : 0 ≤ C i i * C j j - (C i j) ^ 2 := nonneg_of_mul_nonneg_left h_ineq h_cii_pos
    linarith

/-- **Cauchy-Schwarz inequality for PSD entries**: for any PSD
    matrix `C : Matrix (Fin n) (Fin n) ℝ` and indices `i, j`,
    `(C i j)² ≤ C i i · C j j`.  Discharged via the cited external
    axiom. -/
theorem Matrix.PosSemidef.entry_sq_le_diag_mul
    {C : Matrix (Fin n) (Fin n) ℝ} (hC : C.PosSemidef)
    (i j : Fin n) :
    (C i j) ^ 2 ≤ C i i * C j j :=
  entry_sq_le_diag_mul_axiom hC i j

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
