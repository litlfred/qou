/-
  Certified rational bounds on the Clausen value `Cl₂(π/3)` — the 4₁
  volume-value brick (bean qou-44ma).

  `Vol(4₁) = 2·Cl₂(π/3)` is transcendental (no elementary closed form); the
  repo carries its 30-digit decimal only as the APPROXIMATION carrier
  `VOL_4_1_decimal` with no formal link to the exact `VOL_4_1` (the qou-yf47
  statement repair). This file supplies the first machine-checked link:

    * `abs_Cl_2_pi_div_three_sub_le` — the series partial sum over the first
      24 terms (an exact rational multiple of `√3`, by the period-6 pattern
      `sin(kπ/3) ∈ {±√3/2, 0}`) approximates `Cl₂(π/3)` within `1/24`
      (crude tail: `|sin| ≤ 1` + the telescoping bound
      `Σ_{k>24} 1/k² ≤ 1/24`).
    * `abs_VOL_4_1_sub_decimal_lt` — hence `|VOL_4_1 − VOL_4_1_decimal| <
      1/10`, the first certified interval connecting the exact volume to its
      decimal carrier. (Tightening to more digits is a longer partial sum
      plus a sharper tail — same skeleton.)

  Archimedean (ℝ).

  -- Ref: [thurston1978] The geometry and topology of three-manifolds
  -- Ref: [zagier1986] DOI 10.1007/BFb0084581
-/

import Mathlib.Analysis.PSeries
import Mathlib.Analysis.SpecificLimits.Basic
import QOU.Knot.FigureEightVolume

namespace QOU.Knot

open Real

/-- The `k`-th term of the `Cl₂(π/3)` Fourier series. -/
noncomputable def cl2Term (k : ℕ) : ℝ :=
  Real.sin (((k : ℝ) + 1) * (π / 3)) / ((k : ℝ) + 1) ^ 2

theorem cl2_pi3_eq_tsum :
    QOU.Archimedean.Cl_2 (π / 3) = ∑' k, cl2Term k := rfl

/-- Shifted inverse squares are summable. -/
theorem summable_one_div_add_one_sq :
    Summable (fun k : ℕ => 1 / ((k : ℝ) + 1) ^ 2) := by
  have h0 : Summable (fun n : ℕ => 1 / (n : ℝ) ^ 2) :=
    (Real.summable_one_div_nat_pow (p := 2)).mpr one_lt_two
  have h := (summable_nat_add_iff 1).mpr h0
  refine h.congr fun k => ?_
  push_cast
  ring

theorem norm_cl2Term_le (k : ℕ) : ‖cl2Term k‖ ≤ 1 / ((k : ℝ) + 1) ^ 2 := by
  have hk : (0 : ℝ) < ((k : ℝ) + 1) ^ 2 := by positivity
  unfold cl2Term
  rw [norm_div, Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos hk]
  gcongr
  exact abs_le.mpr ⟨Real.neg_one_le_sin _, Real.sin_le_one _⟩

theorem summable_cl2Term : Summable cl2Term :=
  Summable.of_norm (Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
    norm_cl2Term_le summable_one_div_add_one_sq)

/-- The telescoping tail series `Σ (1/(i+24) − 1/(i+25))` sums to `1/24`. -/
theorem hasSum_telescope :
    HasSum (fun i : ℕ => 1 / ((i : ℝ) + 24) - 1 / ((i : ℝ) + 25))
      (1 / 24) := by
  have hpos : ∀ i : ℕ, 0 ≤ 1 / ((i : ℝ) + 24) - 1 / ((i : ℝ) + 25) := by
    intro i
    have h1 : (0 : ℝ) < (i : ℝ) + 24 := by positivity
    have h3 : 1 / ((i : ℝ) + 25) ≤ 1 / ((i : ℝ) + 24) := by
      gcongr
      linarith
    linarith
  refine (hasSum_iff_tendsto_nat_of_nonneg hpos _).mpr ?_
  have htel : ∀ n : ℕ,
      (∑ i ∈ Finset.range n, (1 / ((i : ℝ) + 24) - 1 / ((i : ℝ) + 25)))
        = 1 / 24 - 1 / ((n : ℝ) + 24) := by
    intro n
    have h := Finset.sum_range_sub' (f := fun i : ℕ => 1 / ((i : ℝ) + 24)) n
    calc (∑ i ∈ Finset.range n, (1 / ((i : ℝ) + 24) - 1 / ((i : ℝ) + 25)))
        = ∑ i ∈ Finset.range n,
            ((fun i : ℕ => 1 / ((i : ℝ) + 24)) i
              - (fun i : ℕ => 1 / ((i : ℝ) + 24)) (i + 1)) := by
          refine Finset.sum_congr rfl fun i _ => ?_
          push_cast
          ring
      _ = 1 / (((0 : ℕ) : ℝ) + 24) - 1 / ((n : ℝ) + 24) := h
      _ = 1 / 24 - 1 / ((n : ℝ) + 24) := by norm_num
  simp only [htel]
  have hx : Filter.Tendsto (fun n : ℕ => (n : ℝ) + 24)
      Filter.atTop Filter.atTop :=
    Filter.tendsto_atTop_add_const_right _ 24 tendsto_natCast_atTop_atTop
  have h0 : Filter.Tendsto (fun n : ℕ => 1 / ((n : ℝ) + 24))
      Filter.atTop (nhds 0) := by
    have := tendsto_inv_atTop_zero.comp hx
    simpa [Function.comp_def, one_div] using this
  have h1 := Filter.Tendsto.const_sub (1 / 24 : ℝ) h0
  simpa using h1

/-- Crude but certified tail bound: the series tail past 24 terms is at most
    `1/24` in absolute value. -/
theorem tail_le : |∑' i : ℕ, cl2Term (i + 24)| ≤ 1 / 24 := by
  have hb : ∀ i : ℕ,
      ‖cl2Term (i + 24)‖ ≤ 1 / ((i : ℝ) + 24) - 1 / ((i : ℝ) + 25) := by
    intro i
    have h1 := norm_cl2Term_le (i + 24)
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
  have hnorm : Summable (fun i : ℕ => ‖cl2Term (i + 24)‖) :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _) hb
      hasSum_telescope.summable
  calc |∑' i : ℕ, cl2Term (i + 24)|
      = ‖∑' i : ℕ, cl2Term (i + 24)‖ := (Real.norm_eq_abs _).symm
    _ ≤ ∑' i : ℕ, ‖cl2Term (i + 24)‖ := norm_tsum_le_tsum_norm hnorm
    _ ≤ ∑' i : ℕ, (1 / ((i : ℝ) + 24) - 1 / ((i : ℝ) + 25)) :=
        tsum_le_tsum hb hnorm hasSum_telescope.summable
    _ = 1 / 24 := hasSum_telescope.tsum_eq

/-- The 24-term partial sum, exactly: a rational multiple of `√3` by the
    period-6 sine pattern `sin(kπ/3) ∈ {√3/2, √3/2, 0, −√3/2, −√3/2, 0}`. -/
theorem S24_eq : (∑ i ∈ Finset.range 24, cl2Term i)
    = (414173156523019011 / 707846096282124800 : ℝ) * Real.sqrt 3 := by
  have s1 : Real.sin (π / 3) = Real.sqrt 3 / 2 := Real.sin_pi_div_three
  have s2 : Real.sin (2 * (π / 3)) = Real.sqrt 3 / 2 := by
    rw [show 2 * (π / 3) = π - π / 3 by ring, Real.sin_pi_sub, s1]
  have s3 : Real.sin (3 * (π / 3)) = 0 := by
    rw [show 3 * (π / 3) = π by ring, Real.sin_pi]
  have s4 : Real.sin (4 * (π / 3)) = -(Real.sqrt 3 / 2) := by
    rw [show 4 * (π / 3) = 2 * π - 2 * (π / 3) by ring, Real.sin_two_pi_sub, s2]
  have s5 : Real.sin (5 * (π / 3)) = -(Real.sqrt 3 / 2) := by
    rw [show 5 * (π / 3) = 2 * π - π / 3 by ring, Real.sin_two_pi_sub, s1]
  have s6 : Real.sin (6 * (π / 3)) = 0 := by
    rw [show 6 * (π / 3) = 2 * π by ring, Real.sin_two_pi]
  have s7 : Real.sin (7 * (π / 3)) = Real.sqrt 3 / 2 := by
    rw [show 7 * (π / 3) = π / 3 + 2 * π by ring, Real.sin_add_two_pi, s1]
  have s8 : Real.sin (8 * (π / 3)) = Real.sqrt 3 / 2 := by
    rw [show 8 * (π / 3) = 2 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s2]
  have s9 : Real.sin (9 * (π / 3)) = 0 := by
    rw [show 9 * (π / 3) = 3 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s3]
  have s10 : Real.sin (10 * (π / 3)) = -(Real.sqrt 3 / 2) := by
    rw [show 10 * (π / 3) = 4 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s4]
  have s11 : Real.sin (11 * (π / 3)) = -(Real.sqrt 3 / 2) := by
    rw [show 11 * (π / 3) = 5 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s5]
  have s12 : Real.sin (12 * (π / 3)) = 0 := by
    rw [show 12 * (π / 3) = 6 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s6]
  have s13 : Real.sin (13 * (π / 3)) = Real.sqrt 3 / 2 := by
    rw [show 13 * (π / 3) = 7 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s7]
  have s14 : Real.sin (14 * (π / 3)) = Real.sqrt 3 / 2 := by
    rw [show 14 * (π / 3) = 8 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s8]
  have s15 : Real.sin (15 * (π / 3)) = 0 := by
    rw [show 15 * (π / 3) = 9 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s9]
  have s16 : Real.sin (16 * (π / 3)) = -(Real.sqrt 3 / 2) := by
    rw [show 16 * (π / 3) = 10 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s10]
  have s17 : Real.sin (17 * (π / 3)) = -(Real.sqrt 3 / 2) := by
    rw [show 17 * (π / 3) = 11 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s11]
  have s18 : Real.sin (18 * (π / 3)) = 0 := by
    rw [show 18 * (π / 3) = 12 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s12]
  have s19 : Real.sin (19 * (π / 3)) = Real.sqrt 3 / 2 := by
    rw [show 19 * (π / 3) = 13 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s13]
  have s20 : Real.sin (20 * (π / 3)) = Real.sqrt 3 / 2 := by
    rw [show 20 * (π / 3) = 14 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s14]
  have s21 : Real.sin (21 * (π / 3)) = 0 := by
    rw [show 21 * (π / 3) = 15 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s15]
  have s22 : Real.sin (22 * (π / 3)) = -(Real.sqrt 3 / 2) := by
    rw [show 22 * (π / 3) = 16 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s16]
  have s23 : Real.sin (23 * (π / 3)) = -(Real.sqrt 3 / 2) := by
    rw [show 23 * (π / 3) = 17 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s17]
  have s24 : Real.sin (24 * (π / 3)) = 0 := by
    rw [show 24 * (π / 3) = 18 * (π / 3) + 2 * π by ring, Real.sin_add_two_pi, s18]
  simp only [cl2Term, Finset.sum_range_succ, Finset.sum_range_zero,
    Nat.cast_ofNat, Nat.cast_zero, Nat.cast_one]
  norm_num
  rw [s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16,
    s17, s18, s19, s20, s21, s22, s23, s24]
  field_simp
  ring

theorem sqrt_three_gt : (1.7320508 : ℝ) < Real.sqrt 3 := by
  nlinarith [Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 3), Real.sqrt_nonneg 3]

theorem sqrt_three_lt : Real.sqrt 3 < 1.7320509 := by
  nlinarith [Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 3), Real.sqrt_nonneg 3]

/-- **Certified bound on the Clausen value.** The exact rational-times-`√3`
    24-term partial sum approximates `Cl₂(π/3)` within `1/24`. -/
theorem abs_Cl_2_pi_div_three_sub_le :
    |QOU.Archimedean.Cl_2 (π / 3)
      - (414173156523019011 / 707846096282124800 : ℝ) * Real.sqrt 3|
      ≤ 1 / 24 := by
  have hsplit := summable_cl2Term.sum_add_tsum_nat_add 24
  rw [cl2_pi3_eq_tsum, ← hsplit, S24_eq, add_sub_cancel_left]
  exact tail_le

/-- **The exact volume meets its decimal carrier**: the transcendental
    `VOL_4_1 = 2·Cl₂(π/3)` and the 30-digit approximation carrier
    `VOL_4_1_decimal` agree within `1/10` — machine-certified, closing the
    "no formal identity is claimed" gap at the first decimal.
    (bean qou-44ma) -/
theorem abs_VOL_4_1_sub_decimal_lt :
    |FigureEightVolume.VOL_4_1 - FigureEightVolume.VOL_4_1_decimal|
      < 1 / 10 := by
  have h := abs_Cl_2_pi_div_three_sub_le
  have h1 := sqrt_three_gt
  have h2 := sqrt_three_lt
  rw [abs_le] at h
  have hV : FigureEightVolume.VOL_4_1
      = 2 * QOU.Archimedean.Cl_2 (π / 3) := rfl
  have hD : FigureEightVolume.VOL_4_1_decimal
      = 2.029883212819307250042405108549 := rfl
  rw [hV, hD, abs_lt]
  constructor <;> nlinarith [h.1, h.2]

end QOU.Knot
