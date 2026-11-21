import QOU.BraidKnot.SeminormalDiagonalPoleOrder

/-!
# prop:crystal-r-matrix-sub-lemma — pole order of the seminormal diagonal entry

**Statement.** Let `ρ = ρ_T(i) = c(cell of i+1 in T) − c(cell of i in T)`
be the axial distance (`c = col − row`). In Hoefsmit's seminormal form the
boundary generator `σ_i` acts on the basis vector `v_T` with diagonal entry

    a_T(i) = (q − q⁻¹) / (1 − q^{−2ρ}).

(Check of the orientation: a column tableau has `ρ = −1` and the entry is
`−q⁻¹`, the sign-representation eigenvalue; a row tableau has `ρ = +1` and the
entry is `q`.)

The pole order of `a_T(i)` at `q = 0` is the indicator `𝟙[ρ ≤ −1]`:

* `ρ = −(m+1)`: `a_T(i) = q⁻¹ · (q² − 1)/(1 − q^{2(m+1)})`, and the second
  factor has numerator `−1` and denominator `1` at `q = 0`: a simple pole;
* `ρ = m + 1`: `a_T(i) = q^{2m+1} · (q² − 1)/(q^{2(m+1)} − 1)`, and the second
  factor has numerator `−1` and denominator `−1` at `q = 0`: no pole.

No crystal hypothesis is used. Until 2026-11-21 this block was stated
conditional on `conj:crystal-graph-realization`, carried as a class whose field
was the boxed identity itself.

**Scope.** This is the diagonal entry. That the `(μ, ν)`-block of `σ_i` in
the Wenzl decomposition acts on `v_T` with this diagonal entry is Hoefsmit's
seminormal form (cited, not formalised here). Off-diagonal entries are not
covered.

Ref: [hoefsmit1974] seminormal form; [wenzl1988] branching.
-/

namespace QOU.BraidKnot.CrystalRMatrix

open QOU.BraidKnot.SeminormalDiagonalPoleOrder

variable {K : Type*} [Field K]

/-- The seminormal diagonal entry at axial distance `ρ`. -/
noncomputable def seminormalDiag (q : K) (ρ : ℤ) : K :=
  (q - q⁻¹) / (1 - q ^ (-2 * ρ))

/-- **`ρ ≤ −1`: simple pole.** The entry is `q⁻¹` times a factor whose
numerator `q² − 1` and denominator `1 − q^{2(m+1)}` are `−1` and `1` at
`q = 0`. -/
theorem seminormalDiag_of_le_neg_one {q : K} (hq : q ≠ 0) (m : ℕ)
    (hd : 1 - q ^ (2 * (m + 1)) ≠ 0) :
    seminormalDiag q (-((m : ℤ) + 1)) =
      q⁻¹ * ((q ^ 2 - 1) / (1 - q ^ (2 * (m + 1)))) := by
  unfold seminormalDiag
  have e : (-2 : ℤ) * -((m : ℤ) + 1) = ((2 * (m + 1) : ℕ) : ℤ) := by push_cast; ring
  rw [e, zpow_natCast]
  exact diag_pos_axial hq m hd

/-- **`ρ ≥ 1`: no pole.** The entry is `q^{2m+1}` times a factor whose
numerator `q² − 1` and denominator `q^{2(m+1)} − 1` are both `−1` at
`q = 0`. -/
theorem seminormalDiag_of_ge_one {q : K} (hq : q ≠ 0) (m : ℕ)
    (hd : q ^ (2 * (m + 1)) - 1 ≠ 0) :
    seminormalDiag q ((m : ℤ) + 1) =
      q ^ (2 * m + 1) * ((q ^ 2 - 1) / (q ^ (2 * (m + 1)) - 1)) := by
  unfold seminormalDiag
  have e : (-2 : ℤ) * ((m : ℤ) + 1) = -(((2 * (m + 1) : ℕ) : ℤ)) := by push_cast; ring
  rw [e, zpow_neg, zpow_natCast]
  exact diag_neg_axial hq m hd

/-- **Orientation check.** At `ρ = −1` the entry is `−q⁻¹` and at `ρ = 1` it
is `q`: the sign and trivial eigenvalues of `σ_i`. -/
theorem seminormalDiag_neg_one_and_one {q : K} (hq : q ≠ 0) (h2 : q ^ 2 ≠ 1) :
    seminormalDiag q (-1) = -q⁻¹ ∧ seminormalDiag q 1 = q := by
  have h2' : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr h2
  have h2'' : 1 - q ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm h2)
  unfold seminormalDiag
  constructor
  · norm_num
    field_simp
    ring
  · norm_num
    field_simp

end QOU.BraidKnot.CrystalRMatrix
