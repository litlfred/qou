/-
  Certified rational bounds on the Catalan constant `G = Cl₂(π/2)` — the
  Borromean volume-value companion of `ClausenValueBounds` (bean qou-8gv9,
  milestone qou-jpwy).

  The Borromean binding scale rides on `Vol(𝓑₃) = 8G = 8·Cl₂(π/2)`
  (`Catalan_constant` / `Vol_Borromean` carriers in the Clausen filler;
  `binding-scale-catalan`). Same skeleton as `ClausenValueBounds`, at `π/2`
  instead of `π/3`: the period-4 pattern `sin(kπ/2) ∈ {1, 0, −1, 0}` makes
  the 24-term partial sum an EXACT rational (no `√3` here), the crude
  telescoping tail gives `≤ 1/24`, and the certified intervals follow:

    * `abs_Catalan_sub_le`      — `|G − 102476291858462752/111983464450883025| ≤ 1/24`
    * `abs_Catalan_sub_decimal_lt` — `|Catalan_constant − 0.9159655942| < 1/20`
    * `abs_Vol_Borromean_sub_lt`   — `|Vol_Borromean − 7.3277247534| < 2/5`

  Tightening: longer partial sum + alternating-series tail (the `π/2` series
  is genuinely alternating, so the tail is first-omitted-term small) — same
  skeleton, follow-up material.

  Archimedean (ℝ).

  -- Ref: [zagier1986] DOI 10.1007/BFb0084581
  -- Ref: [leitner2026] binding-scale-catalan
-/

import Mathlib.Analysis.PSeries
import Mathlib.Analysis.SpecificLimits.Basic
import QOU.Knot.ClausenValueBounds

namespace QOU.Knot

open Real

/-- The `k`-th term of the `Cl₂(π/2)` (Catalan) Fourier series. -/
noncomputable def catTerm (k : ℕ) : ℝ :=
  Real.sin (((k : ℝ) + 1) * (π / 2)) / ((k : ℝ) + 1) ^ 2

theorem catalan_eq_tsum :
    QOU.Archimedean.Catalan_constant = ∑' k, catTerm k := rfl

theorem norm_catTerm_le (k : ℕ) : ‖catTerm k‖ ≤ 1 / ((k : ℝ) + 1) ^ 2 := by
  have hk : (0 : ℝ) < ((k : ℝ) + 1) ^ 2 := by positivity
  unfold catTerm
  rw [norm_div, Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos hk]
  gcongr
  exact abs_le.mpr ⟨Real.neg_one_le_sin _, Real.sin_le_one _⟩

theorem summable_catTerm : Summable catTerm :=
  Summable.of_norm (Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
    norm_catTerm_le summable_one_div_add_one_sq)

/-- Crude certified tail bound past 24 terms, via the `ClausenValueBounds`
    telescoping series. -/
theorem cat_tail_le : |∑' i : ℕ, catTerm (i + 24)| ≤ 1 / 24 := by
  have hb : ∀ i : ℕ,
      ‖catTerm (i + 24)‖ ≤ 1 / ((i : ℝ) + 24) - 1 / ((i : ℝ) + 25) := by
    intro i
    have h1 := norm_catTerm_le (i + 24)
    have hcast : ((i + 24 : ℕ) : ℝ) + 1 = (i : ℝ) + 25 := by push_cast; ring
    rw [hcast] at h1
    have h24 : (0 : ℝ) < (i : ℝ) + 24 := by positivity
    have h25 : (0 : ℝ) < (i : ℝ) + 25 := by positivity
    have key : 1 / ((i : ℝ) + 24) - 1 / ((i : ℝ) + 25)
        = 1 / (((i : ℝ) + 24) * ((i : ℝ) + 25)) := by
      field_simp
      ring
    refine le_trans h1 ?_
    rw [key]
    gcongr
    nlinarith
  have hnorm : Summable (fun i : ℕ => ‖catTerm (i + 24)‖) :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hb
      hasSum_telescope.summable
  calc |∑' i : ℕ, catTerm (i + 24)|
      = ‖∑' i : ℕ, catTerm (i + 24)‖ := (Real.norm_eq_abs _).symm
    _ ≤ ∑' i : ℕ, ‖catTerm (i + 24)‖ := norm_tsum_le_tsum_norm hnorm
    _ ≤ ∑' i : ℕ, (1 / ((i : ℝ) + 24) - 1 / ((i : ℝ) + 25)) :=
        tsum_le_tsum hb hnorm hasSum_telescope.summable
    _ = 1 / 24 := hasSum_telescope.tsum_eq

/-- The 24-term partial sum, exactly: a pure rational (the alternating odd
    inverse squares `1 − 1/9 + 1/25 − … − 1/529`), by the period-4 sine
    pattern `sin(kπ/2) ∈ {1, 0, −1, 0}`. -/
theorem catS24_eq : (∑ i ∈ Finset.range 24, catTerm i)
    = (102476291858462752 / 111983464450883025 : ℝ) := by
  have t1 : Real.sin (π / 2) = 1 := Real.sin_pi_div_two
  have t2 : Real.sin (2 * (π / 2)) = 0 := by
    rw [show 2 * (π / 2) = π by ring, Real.sin_pi]
  have t3 : Real.sin (3 * (π / 2)) = -1 := by
    rw [show 3 * (π / 2) = 2 * π - π / 2 by ring, Real.sin_two_pi_sub, t1]
  have t4 : Real.sin (4 * (π / 2)) = 0 := by
    rw [show 4 * (π / 2) = 2 * π by ring, Real.sin_two_pi]
  have t5 : Real.sin (5 * (π / 2)) = 1 := by
    rw [show 5 * (π / 2) = π / 2 + 2 * π by ring, Real.sin_add_two_pi, t1]
  have t6 : Real.sin (6 * (π / 2)) = 0 := by
    rw [show 6 * (π / 2) = 2 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t2]
  have t7 : Real.sin (7 * (π / 2)) = -1 := by
    rw [show 7 * (π / 2) = 3 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t3]
  have t8 : Real.sin (8 * (π / 2)) = 0 := by
    rw [show 8 * (π / 2) = 4 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t4]
  have t9 : Real.sin (9 * (π / 2)) = 1 := by
    rw [show 9 * (π / 2) = 5 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t5]
  have t10 : Real.sin (10 * (π / 2)) = 0 := by
    rw [show 10 * (π / 2) = 6 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t6]
  have t11 : Real.sin (11 * (π / 2)) = -1 := by
    rw [show 11 * (π / 2) = 7 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t7]
  have t12 : Real.sin (12 * (π / 2)) = 0 := by
    rw [show 12 * (π / 2) = 8 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t8]
  have t13 : Real.sin (13 * (π / 2)) = 1 := by
    rw [show 13 * (π / 2) = 9 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t9]
  have t14 : Real.sin (14 * (π / 2)) = 0 := by
    rw [show 14 * (π / 2) = 10 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t10]
  have t15 : Real.sin (15 * (π / 2)) = -1 := by
    rw [show 15 * (π / 2) = 11 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t11]
  have t16 : Real.sin (16 * (π / 2)) = 0 := by
    rw [show 16 * (π / 2) = 12 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t12]
  have t17 : Real.sin (17 * (π / 2)) = 1 := by
    rw [show 17 * (π / 2) = 13 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t13]
  have t18 : Real.sin (18 * (π / 2)) = 0 := by
    rw [show 18 * (π / 2) = 14 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t14]
  have t19 : Real.sin (19 * (π / 2)) = -1 := by
    rw [show 19 * (π / 2) = 15 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t15]
  have t20 : Real.sin (20 * (π / 2)) = 0 := by
    rw [show 20 * (π / 2) = 16 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t16]
  have t21 : Real.sin (21 * (π / 2)) = 1 := by
    rw [show 21 * (π / 2) = 17 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t17]
  have t22 : Real.sin (22 * (π / 2)) = 0 := by
    rw [show 22 * (π / 2) = 18 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t18]
  have t23 : Real.sin (23 * (π / 2)) = -1 := by
    rw [show 23 * (π / 2) = 19 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t19]
  have t24 : Real.sin (24 * (π / 2)) = 0 := by
    rw [show 24 * (π / 2) = 20 * (π / 2) + 2 * π by ring, Real.sin_add_two_pi, t20]
  simp only [catTerm, Finset.sum_range_succ, Finset.sum_range_zero,
    Nat.cast_ofNat, Nat.cast_zero, Nat.cast_one]
  norm_num
  rw [t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16,
    t17, t18, t19, t20, t21, t22, t23, t24]
  norm_num

/-- **Certified bound on the Catalan constant.** The exact rational 24-term
    partial sum approximates `G = Cl₂(π/2)` within `1/24`. -/
theorem abs_Catalan_sub_le :
    |QOU.Archimedean.Catalan_constant
      - (102476291858462752 / 111983464450883025 : ℝ)| ≤ 1 / 24 := by
  have hsplit := summable_catTerm.sum_add_tsum_nat_add 24
  rw [catalan_eq_tsum, ← hsplit, catS24_eq, add_sub_cancel_left]
  exact cat_tail_le

/-- `|G − 0.9159655942| < 1/20` — the Catalan carrier meets its standard
    decimal. -/
theorem abs_Catalan_sub_decimal_lt :
    |QOU.Archimedean.Catalan_constant - 0.9159655942| < 1 / 20 := by
  have h := abs_Catalan_sub_le
  rw [abs_le] at h
  rw [abs_lt]
  constructor <;> linarith [h.1, h.2]

/-- `Cl₂(π/2) > 0` — the Catalan constant is positive, straight from the
    certified interval (`RAT − 1/24 > 0`). The boundary-exclusion input the
    Borromean B4 extremum analysis needs. -/
theorem Cl_2_pi_div_two_pos : 0 < QOU.Archimedean.Cl_2 (π / 2) := by
  have h := abs_Catalan_sub_le
  rw [abs_le] at h
  have hC : QOU.Archimedean.Catalan_constant
      = QOU.Archimedean.Cl_2 (π / 2) := rfl
  rw [hC] at h
  linarith [h.1]

/-- `|Vol(𝓑₃) − 7.3277247534| < 2/5` — the Borromean-volume carrier
    `Vol_Borromean = 8·Cl₂(π/2)` meets the `8G` binding-scale decimal.
    (bean qou-8gv9) -/
theorem abs_Vol_Borromean_sub_lt :
    |QOU.Archimedean.Vol_Borromean - 7.3277247534| < 2 / 5 := by
  have h := abs_Catalan_sub_le
  rw [abs_le] at h
  have hV : QOU.Archimedean.Vol_Borromean
      = 8 * QOU.Archimedean.Cl_2 (π / 2) := rfl
  have hC : QOU.Archimedean.Catalan_constant
      = QOU.Archimedean.Cl_2 (π / 2) := rfl
  rw [hC] at h
  rw [hV, abs_lt]
  constructor <;> linarith [h.1, h.2]

end QOU.Knot
