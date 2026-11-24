import Mathlib.Tactic

/-!
# Stacked-Crossing Writhe Framing Flip (`qou-pjx4`)

This module formalizes the two-way bound/unbound verdict reversal (`qou-pjx4`) between raw
and writhe-normalised Markov scalars for stacked `σ²` (`e = +2`) and `σ⁻²` (`e = -2`)
crossings:

1. For `σ² = h σ + 1`, the raw scalar is `μ_raw(+2) = h z + 1` and the writhe-normalised
   scalar (`(1 - h)^{2/2} = 1 - h`) is `μ_eff(+2) = (h z + 1)(1 - h) = 1 - h((1 - z) + h z)`.
2. For `σ⁻² = (σ - h)² = (1 + h²) - h σ`, the raw scalar is `μ_raw(-2) = 1 + h² - h z = 1 - h(z - h)`
   and the writhe-normalised scalar (`(1 - h)^{-2/2} = (1 - h)⁻¹`) is
   `μ_eff(-2) = (1 + h² - h z) / (1 - h) = 1 + h(1 - z + h) / (1 - h)`.
3. Consequently, throughout the physical regime `0 < h < z < 1`:
   - `μ_raw(+2) > 1` (unbound raw) flips to `μ_eff(+2) < 1` (bound after writhe normalisation);
   - `μ_raw(-2) < 1` (bound raw) flips to `μ_eff(-2) > 1` (unbound after writhe normalisation).
-/

namespace QOU.MassTheory

/-- Raw Markov scalar `h z + 1` of `σ²` (`qou-pjx4`). -/
def muRawPos2 (z h : ℚ) : ℚ :=
  h * z + 1

/-- Writhe-normalised Markov scalar `(h z + 1)(1 - h)` of `σ²` (`qou-pjx4`). -/
def muEffPos2 (z h : ℚ) : ℚ :=
  (h * z + 1) * (1 - h)

/-- Raw Markov scalar `1 + h² - h z` of `σ⁻² = (σ - h)²` (`qou-pjx4`). -/
def muRawNeg2 (z h : ℚ) : ℚ :=
  1 + h ^ 2 - h * z

/-- Writhe-normalised Markov scalar `(1 + h² - h z) / (1 - h)` of `σ⁻²` (`qou-pjx4`). -/
def muEffNeg2 (z h : ℚ) : ℚ :=
  (1 + h ^ 2 - h * z) / (1 - h)

/-- Exact algebraic decompositions of `μ_eff(+2) - 1`, `μ_raw(-2) - 1`, and `μ_eff(-2) - 1` (`qou-pjx4`). -/
theorem stacked_writhe_decompositions (z h : ℚ) (h1 : 1 - h ≠ 0) :
    muEffPos2 z h - 1 = -h * ((1 - z) + h * z) ∧
    muRawNeg2 z h - 1 = -h * (z - h) ∧
    muEffNeg2 z h - 1 = h * (1 - z + h) / (1 - h) := by
  unfold muEffPos2 muRawNeg2 muEffNeg2
  refine ⟨by ring, by ring, ?_⟩
  field_simp [h1]
  ring

/-- For `0 < h < z < 1`, writhe normalisation reverses the unbinding verdict of both
`σ²` (`μ_raw(+2) > 1` vs `μ_eff(+2) < 1`) and `σ⁻²` (`μ_raw(-2) < 1` vs `μ_eff(-2) > 1`) (`qou-pjx4`). -/
theorem framing_flips_pos2_and_neg2_unbinding
    (z h : ℚ) (hh_pos : 0 < h) (hh_lt_z : h < z) (hz_lt_one : z < 1) :
    1 < muRawPos2 z h ∧
    muEffPos2 z h < 1 ∧
    muRawNeg2 z h < 1 ∧
    1 < muEffNeg2 z h := by
  have hz_pos : 0 < z := lt_trans hh_pos hh_lt_z
  have hh_lt_one : h < 1 := lt_trans hh_lt_z hz_lt_one
  have h1_pos : 0 < 1 - h := by linarith
  have h1_ne : 1 - h ≠ 0 := ne_of_gt h1_pos
  obtain ⟨hd_pos2, hd_raw_neg2, hd_eff_neg2⟩ := stacked_writhe_decompositions z h h1_ne
  have hz_h : 0 < h * z := mul_pos hh_pos hz_pos
  have h_pos2_factor : 0 < (1 - z) + h * z := by linarith
  have h_pos2_neg : -h * ((1 - z) + h * z) < 0 := by nlinarith
  have h_raw_neg2 : -h * (z - h) < 0 := by nlinarith
  have h_num_neg2 : 0 < h * (1 - z + h) := mul_pos hh_pos (by linarith)
  have h_eff_neg2 : 0 < h * (1 - z + h) / (1 - h) := div_pos h_num_neg2 h1_pos
  unfold muRawPos2
  refine ⟨by linarith, by linarith, by linarith, by linarith⟩

end QOU.MassTheory
