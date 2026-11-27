/-
  Archimedean `Real.sqrt` specialisation of the Geiger–Nuttall section of
  `QOU.Nuclear.ThomaeJacksonCoulombAndAlphaTunneling`.  Same namespace,
  original names kept.
-/
import QOU.Nuclear.ThomaeJacksonCoulombAndAlphaTunneling
import Mathlib.Data.Real.Sqrt

namespace QOU.Nuclear.ThomaeJacksonCoulombAndAlphaTunneling

section GeigerNuttall

/-- Archimedean `ℝ` specialization `G_leading(Z_d, Q)` using `Real.sqrt Q` and
`Real.sqrt (Z_d * R_touch)` (§7c `_real` pair for `geigerNuttallSubbarrier`). -/
noncomputable def geigerNuttallSubbarrier_real (C_GN D_GN Z_d Q R_touch : ℝ) : ℝ :=
  geigerNuttallSubbarrier C_GN D_GN Z_d (Real.sqrt Q) (Real.sqrt (Z_d * R_touch))

/-- **Affine Geiger–Nuttall Law & Monotonicity in `Q`:**
1. `2 * geigerNuttallSubbarrier_real C_GN D_GN Z_d Q R_touch = C_GN * Z_d / √Q - D_GN * √(Z_d * R_touch)`.
2. For `0 < C` and `0 < Q₁ < Q₂`, `C / √Q₂ < C / √Q₁` (hence larger `Q_α` strictly decreases
   the Gamow barrier integral `2 G`). -/
theorem geiger_nuttall_linear_in_inv_sqrt_Q (C_GN D_GN Z_d Q R_touch : ℝ) :
    2 * geigerNuttallSubbarrier_real C_GN D_GN Z_d Q R_touch =
      C_GN * Z_d / Real.sqrt Q - D_GN * Real.sqrt (Z_d * R_touch) := by
  unfold geigerNuttallSubbarrier_real
  exact geiger_nuttall_linear_generic C_GN D_GN Z_d (Real.sqrt Q) (Real.sqrt (Z_d * R_touch))

theorem geiger_nuttall_monotone_in_Q_real {C Q1 Q2 : ℝ}
    (hC : 0 < C) (hQ1 : 0 < Q1) (hQ12 : Q1 < Q2) :
    C / Real.sqrt Q2 < C / Real.sqrt Q1 := by
  have hQ2 : 0 < Q2 := lt_trans hQ1 hQ12
  have hs1 : 0 < Real.sqrt Q1 := Real.sqrt_pos.mpr hQ1
  have hs2 : 0 < Real.sqrt Q2 := Real.sqrt_pos.mpr hQ2
  have hslt : Real.sqrt Q1 < Real.sqrt Q2 := Real.sqrt_lt_sqrt (le_of_lt hQ1) hQ12
  have hprod_pos : 0 < Real.sqrt Q1 * Real.sqrt Q2 := mul_pos hs1 hs2
  have hdiff_pos : 0 < (C / Real.sqrt Q1 - C / Real.sqrt Q2) * (Real.sqrt Q1 * Real.sqrt Q2) := by
    have hsimp :
        (C / Real.sqrt Q1 - C / Real.sqrt Q2) * (Real.sqrt Q1 * Real.sqrt Q2) =
          C * (Real.sqrt Q2 - Real.sqrt Q1) := by
      have hs1_ne : Real.sqrt Q1 ≠ 0 := ne_of_gt hs1
      have hs2_ne : Real.sqrt Q2 ≠ 0 := ne_of_gt hs2
      field_simp
    rw [hsimp]
    exact mul_pos hC (sub_pos.mpr hslt)
  by_contra hle
  push_neg at hle
  have hnonpos : (C / Real.sqrt Q1 - C / Real.sqrt Q2) * (Real.sqrt Q1 * Real.sqrt Q2) ≤ 0 :=
    mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr hle) (le_of_lt hprod_pos)
  linarith

end GeigerNuttall

end QOU.Nuclear.ThomaeJacksonCoulombAndAlphaTunneling
