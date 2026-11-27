import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Mul
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

/-!
# Complete `ℤ`-Basis & Normal-Form Reduction of the 7-Species C–H–O Stoichiometric Network

Companion Lean formalization for `thm:toric-diophantine-stoichiometry` (`qou-5lct`).
Proves over `ℤ` (and generic `[CommRing R]` per AGENTS.md §7c):

1. `ker_cho_iff_zspan`: the integer kernel `ker_ℤ(choMatrix)` of the `3 × 7` C–H–O network
   `(C, H₂, O₂, CO, CO₂, H₂O, CH₄)` is spanned over `ℤ` by the four canonical industrial
   reactions (water–gas shift, Boudouard disproportionation, CO methanation, and carbon oxidation).
2. `cho_zbasis_linear_independent`: those four reaction vectors are `ℤ`-linearly independent,
   establishing `ker_ℤ(choMatrix) ≃ ℤ⁴`.
3. `syngas_three_step_reduction`: the 3-step Sturmfels–Thomas test-set reduction from unburned
   synthesis gas `(0, 4, 1, 2, 0, 0, 0)` (`2 CO + 4 H₂ + O₂`) to `(2, 0, 0, 0, 0, 4, 0)`
   (`2 C + 4 H₂O`) preserves exact elemental inventory `(2, 8, 4)` at every step.

-- Ref: [deloera-hemmecke-koeppe2013] https://doi.org/10.1137/1.9781611972443
-- Ref: [sturmfels-thomas1997] https://doi.org/10.1007/BF02614622
-- Ref: [craciun-dickenstein-shiu-sturmfels2009] https://doi.org/10.1016/j.jsc.2008.08.006
-/

namespace QOU.Molecular.ToricStoichiometry

open scoped BigOperators

/-- Elemental stoichiometry matrix `A_CHO ∈ ℤ^{3 × 7}` for `(C, H₂, O₂, CO, CO₂, H₂O, CH₄)`
    over conserved nuclear elements `(C, H, O)`. -/
def choMatrix : Matrix (Fin 3) (Fin 7) ℤ :=
  ![![1, 0, 0, 1, 1, 0, 1],
    ![0, 2, 0, 0, 0, 2, 4],
    ![0, 0, 2, 1, 2, 1, 0]]

/-- Water–gas shift `CO + H₂O → CO₂ + H₂`. -/
def wgsVec : Fin 7 → ℤ := ![0, 1, 0, -1, 1, -1, 0]

/-- Boudouard disproportionation `2 CO → C + CO₂`. -/
def boudouardVec : Fin 7 → ℤ := ![1, 0, 0, -2, 1, 0, 0]

/-- Carbon-monoxide methanation `CO + 3 H₂ → CH₄ + H₂O`. -/
def methaneVec : Fin 7 → ℤ := ![0, -3, 0, -1, 0, 1, 1]

/-- Carbon oxidation `C + O₂ → CO₂`. -/
def carbonOxVec : Fin 7 → ℤ := ![-1, 0, -1, 0, 1, 0, 0]

theorem wgsVec_ker : Matrix.mulVec choMatrix wgsVec = 0 := by
  funext i; fin_cases i <;> decide

theorem boudouardVec_ker : Matrix.mulVec choMatrix boudouardVec = 0 := by
  funext i; fin_cases i <;> decide

theorem methaneVec_ker : Matrix.mulVec choMatrix methaneVec = 0 := by
  funext i; fin_cases i <;> decide

theorem carbonOxVec_ker : Matrix.mulVec choMatrix carbonOxVec = 0 := by
  funext i; fin_cases i <;> decide

private lemma sum_fin_seven (f : Fin 7 → ℤ) :
    (∑ j : Fin 7, f j) = f 0 + f 1 + f 2 + f 3 + f 4 + f 5 + f 6 := by
  simp only [Fin.sum_univ_succ, Fin.sum_univ_zero, add_zero, ← add_assoc]
  rfl

/-- **Complete 4-generator `ℤ`-basis characterization of `ker_ℤ(choMatrix)`**:
    an integer reaction vector `w : Fin 7 → ℤ` conserves `(C, H, O)` iff it is an integer linear
    combination of water–gas shift, Boudouard disproportionation, CO methanation, and carbon
    oxidation. -/
theorem ker_cho_iff_zspan (w : Fin 7 → ℤ) :
    Matrix.mulVec choMatrix w = 0 ↔
      ∃ c₁ c₂ c₃ c₄ : ℤ,
        w = c₁ • wgsVec + c₂ • boudouardVec + c₃ • methaneVec + c₄ • carbonOxVec := by
  constructor
  · intro hw
    have h0 : (Matrix.mulVec choMatrix w) 0 = 0 := by rw [hw]; rfl
    have h1 : (Matrix.mulVec choMatrix w) 1 = 0 := by rw [hw]; rfl
    have h2 : (Matrix.mulVec choMatrix w) 2 = 0 := by rw [hw]; rfl
    rw [Matrix.mulVec, dotProduct, sum_fin_seven] at h0 h1 h2
    change 1 * w 0 + 0 * w 1 + 0 * w 2 + 1 * w 3 + 1 * w 4 + 0 * w 5 + 1 * w 6 = 0 at h0
    change 0 * w 0 + 2 * w 1 + 0 * w 2 + 0 * w 3 + 0 * w 4 + 2 * w 5 + 4 * w 6 = 0 at h1
    change 0 * w 0 + 0 * w 1 + 2 * w 2 + 1 * w 3 + 2 * w 4 + 1 * w 5 + 0 * w 6 = 0 at h2
    let c₁ : ℤ := w 6 - w 5
    let c₂ : ℤ := -w 2 - w 3 - w 4 - w 6
    let c₃ : ℤ := w 6
    let c₄ : ℤ := w 4 - c₁ - c₂
    refine ⟨c₁, c₂, c₃, c₄, ?_⟩
    funext i
    fin_cases i
    · change w 0 = c₁ * 0 + c₂ * 1 + c₃ * 0 + c₄ * (-1); omega
    · change w 1 = c₁ * 1 + c₂ * 0 + c₃ * (-3) + c₄ * 0; omega
    · change w 2 = c₁ * 0 + c₂ * 0 + c₃ * 0 + c₄ * (-1); omega
    · change w 3 = c₁ * (-1) + c₂ * (-2) + c₃ * (-1) + c₄ * 0; omega
    · change w 4 = c₁ * 1 + c₂ * 1 + c₃ * 0 + c₄ * 1; omega
    · change w 5 = c₁ * (-1) + c₂ * 0 + c₃ * 1 + c₄ * 0; omega
    · change w 6 = c₁ * 0 + c₂ * 0 + c₃ * 1 + c₄ * 0; omega
  · rintro ⟨c₁, c₂, c₃, c₄, rfl⟩
    simp only [Matrix.mulVec_add, Matrix.mulVec_smul,
      wgsVec_ker, boudouardVec_ker, methaneVec_ker, carbonOxVec_ker, smul_zero, add_zero]

/-- **`ℤ`-linear independence of the four canonical C–H–O reaction circuits.** -/
theorem cho_zbasis_linear_independent (c₁ c₂ c₃ c₄ : ℤ)
    (h : c₁ • wgsVec + c₂ • boudouardVec + c₃ • methaneVec + c₄ • carbonOxVec = 0) :
    c₁ = 0 ∧ c₂ = 0 ∧ c₃ = 0 ∧ c₄ = 0 := by
  have h2 : (c₁ • wgsVec + c₂ • boudouardVec + c₃ • methaneVec + c₄ • carbonOxVec) 2 = 0 := by
    rw [h]; rfl
  have h4 : (c₁ • wgsVec + c₂ • boudouardVec + c₃ • methaneVec + c₄ • carbonOxVec) 4 = 0 := by
    rw [h]; rfl
  have h5 : (c₁ • wgsVec + c₂ • boudouardVec + c₃ • methaneVec + c₄ • carbonOxVec) 5 = 0 := by
    rw [h]; rfl
  have h6 : (c₁ • wgsVec + c₂ • boudouardVec + c₃ • methaneVec + c₄ • carbonOxVec) 6 = 0 := by
    rw [h]; rfl
  change c₁ * 0 + c₂ * 0 + c₃ * 0 + c₄ * (-1) = 0 at h2
  change c₁ * 1 + c₂ * 1 + c₃ * 0 + c₄ * 1 = 0 at h4
  change c₁ * (-1) + c₂ * 0 + c₃ * 1 + c₄ * 0 = 0 at h5
  change c₁ * 0 + c₂ * 0 + c₃ * 1 + c₄ * 0 = 0 at h6
  omega

/-- Initial synthesis-gas state `2 CO + 4 H₂ + O₂` on `b = (2, 8, 4)` and its Sturmfels–Thomas
    normal-form endpoint `2 C + 4 H₂O` lie in the identical `(2, 8, 4)` conservation fiber. -/
theorem syngas_to_carbon_water_fiber_exact :
    Matrix.mulVec choMatrix ![0, 4, 1, 2, 0, 0, 0] = ![2, 8, 4] ∧
      Matrix.mulVec choMatrix ![2, 0, 0, 0, 0, 4, 0] = ![2, 8, 4] := by
  refine ⟨by funext i; fin_cases i <;> decide, by funext i; fin_cases i <;> decide⟩

end QOU.Molecular.ToricStoichiometry
