import Mathlib.Tactic

/-!
# Third-Order Ursell Alternating-Sign Identity and Corpus `b₃` Inversion (`qou-rwhv`)

This module formalizes the exact algebraic relationship (`qou-rwhv`) between the classical
grand-canonical Ursell functions `φ^T_n` in Mayer variables `g_{ij} = f_{ij} - 1` and the
corpus inclusion-exclusion cumulants `b_n`:

1. At `n = 2` and `n = 3`, the corpus cumulants satisfy the uniform minus relation
   `b₂(f₁₂) = -φ^T₂(f₁₂ - 1)` and `b₃(f₁₂, f₁₃, f₂₃) = -φ^T₃(f₁₂ - 1, f₁₃ - 1, f₂₃ - 1)`.
2. The third Ursell function factors as
   `φ^T₃(g₁₂, g₁₃, g₂₃) = g₁₂ g₁₃ (1 + g₂₃) + g₁₂ g₂₃ + g₁₃ g₂₃`.
3. Consequently, for every triple of bond factors `f₁₂, f₁₃, f₂₃ ∈ (0, 1)`
   (`g_{ij} ∈ (-1, 0)`), the classical alternating-sign law `(-1)^{3-1} φ^T₃ = +φ^T₃ > 0`
   holds unconditionally, whereas the corpus's uniform minus sign inverts `b₃ = -φ^T₃ < 0`.
-/

namespace QOU.MassTheory

/-- Second Ursell function `φ^T₂(g₁₂) = g₁₂` in Mayer variable `g₁₂ = f₁₂ - 1`. -/
def ursellPhi2 (g12 : ℚ) : ℚ := g12

/-- Corpus two-body cumulant `b₂(f₁₂) = 1 - f₁₂`. -/
def corpusB2 (f12 : ℚ) : ℚ := 1 - f12

/-- Third Ursell function `φ^T₃(g₁₂, g₁₃, g₂₃) = g₁₂ g₁₃ + g₁₂ g₂₃ + g₁₃ g₂₃ + g₁₂ g₁₃ g₂₃`
summed over the 3 spanning trees and 1 triangle on 3 labelled vertices (`qou-rwhv`). -/
def ursellPhi3 (g12 g13 g23 : ℚ) : ℚ :=
  g12 * g13 + g12 * g23 + g13 * g23 + g12 * g13 * g23

/-- Corpus three-body inclusion-exclusion cumulant
`b₃(f₁₂, f₁₃, f₂₃) = (1 - f₁₂ f₁₃ f₂₃) - (1 - f₁₂) - (1 - f₁₃) - (1 - f₂₃)` (`qou-rwhv`). -/
def corpusB3 (f12 f13 f23 : ℚ) : ℚ :=
  1 - f12 * f13 * f23 - (1 - f12) - (1 - f13) - (1 - f23)

/-- Exact identity `b_n = -φ^T_n(f - 1)` at both `n = 2` and `n = 3` (`qou-rwhv`). -/
theorem corpusB2_and_B3_eq_neg_ursell (f12 f13 f23 : ℚ) :
    corpusB2 f12 = -ursellPhi2 (f12 - 1) ∧
    corpusB3 f12 f13 f23 = -ursellPhi3 (f12 - 1) (f13 - 1) (f23 - 1) := by
  unfold corpusB2 ursellPhi2 corpusB3 ursellPhi3
  constructor <;> ring

/-- Factored decomposition `φ^T₃(g₁₂, g₁₃, g₂₃) = g₁₂ g₁₃ (1 + g₂₃) + g₁₂ g₂₃ + g₁₃ g₂₃`
isolating three manifestly positive summands when `g_{ij} ∈ (-1, 0)` (`qou-rwhv`). -/
theorem ursellPhi3_factored_decomp (g12 g13 g23 : ℚ) :
    ursellPhi3 g12 g13 g23 = g12 * g13 * (1 + g23) + g12 * g23 + g13 * g23 := by
  unfold ursellPhi3
  ring

/-- For every triple of bond factors `f₁₂, f₁₃, f₂₃ ∈ (0, 1)`, the third Ursell function
is strictly positive (`φ^T₃ > 0`, obeying `(-1)^{3-1} φ^T₃ > 0`), while the corpus's
uniform minus sign forces `corpusB3 < 0` (`qou-rwhv`). -/
theorem repulsive_bonds_force_ursellPhi3_pos_and_corpusB3_neg
    (f12 f13 f23 : ℚ)
    (hf12_lo : 0 < f12) (hf12_hi : f12 < 1)
    (hf13_lo : 0 < f13) (hf13_hi : f13 < 1)
    (hf23_lo : 0 < f23) (hf23_hi : f23 < 1) :
    0 < ursellPhi3 (f12 - 1) (f13 - 1) (f23 - 1) ∧
    corpusB3 f12 f13 f23 < 0 := by
  have hg12 : f12 - 1 < 0 := by linarith
  have hg13 : f13 - 1 < 0 := by linarith
  have hg23 : f23 - 1 < 0 := by linarith
  have h1g23 : 0 < 1 + (f23 - 1) := by linarith
  have hp1213 : 0 < (f12 - 1) * (f13 - 1) := mul_pos_of_neg_of_neg hg12 hg13
  have hp_tri : 0 < (f12 - 1) * (f13 - 1) * (1 + (f23 - 1)) := mul_pos hp1213 h1g23
  have hp1223 : 0 < (f12 - 1) * (f23 - 1) := mul_pos_of_neg_of_neg hg12 hg23
  have hp1323 : 0 < (f13 - 1) * (f23 - 1) := mul_pos_of_neg_of_neg hg13 hg23
  have hdecomp := ursellPhi3_factored_decomp (f12 - 1) (f13 - 1) (f23 - 1)
  have hpos : 0 < ursellPhi3 (f12 - 1) (f13 - 1) (f23 - 1) := by linarith
  have hneg_id := (corpusB2_and_B3_eq_neg_ursell f12 f13 f23).2
  refine ⟨hpos, by linarith⟩

end QOU.MassTheory
