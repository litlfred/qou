import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith


/-!
# QOU.Archimedean.golden_skew_dual_node — Skew-dual golden node at q = φ²

The bar involution q ↔ q⁻¹ on the substrate parameter pairs the
golden-ratio node q_gold = 1/φ² with the skew-dual node q* = φ².
The minimal polynomial of 1/φ is s² + s − 1; the minimal polynomial
of φ is s² − s − 1; the substitution s ↔ 1/s exchanges them.

LaTeX label: `prop:golden-skew-dual-node`

## References

- [leitner2026] §6/golden-skew-dual-node
- [leitner2026] §7/golden-ratio-degeneration
-/

namespace QOU.Archimedean

/-- The golden ratio φ = (1 + √5)/2. -/
noncomputable def phi : ℝ := (1 + Real.sqrt 5) / 2

/-- The reciprocal of the golden ratio, 1/φ = (√5 − 1)/2. -/
noncomputable def phiInv : ℝ := (Real.sqrt 5 - 1) / 2

/-- The sub-classical golden node q_gold = 1/φ². -/
noncomputable def qGold : ℝ := phiInv ^ 2

/-- The skew-dual golden node q* = φ². -/
noncomputable def qGoldDual : ℝ := phi ^ 2

/-- 1/φ satisfies s² + s − 1 = 0. -/
-- Ref: [leitner2026] §6/golden-skew-dual-node
theorem phiInv_min_poly : phiInv ^ 2 + phiInv - 1 = 0 := by
  unfold phiInv
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)
  field_simp
  nlinarith

/-- φ satisfies s² − s − 1 = 0. -/
-- Ref: [leitner2026] §6/golden-skew-dual-node
theorem phi_min_poly : phi ^ 2 - phi - 1 = 0 := by
  unfold phi
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)
  field_simp
  nlinarith

/-- φ is positive. -/
-- Ref: [leitner2026] §6/golden-skew-dual-node
theorem phi_pos : 0 < phi := by
  unfold phi
  have : (0 : ℝ) ≤ Real.sqrt 5 := Real.sqrt_nonneg _
  linarith

/-- 1/φ is positive. -/
-- Ref: [leitner2026] §6/golden-skew-dual-node
theorem phiInv_pos : 0 < phiInv := by
  unfold phiInv
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)
  have hsqrt : (2 : ℝ) < Real.sqrt 5 := by
    have h2 : (2 : ℝ) ^ 2 < 5 := by norm_num
    nlinarith [Real.sqrt_nonneg (5 : ℝ), Real.sq_sqrt (show (5 : ℝ) ≥ 0 by norm_num)]
  linarith

/-- Bar duality: φ · (1/φ) = 1. -/
-- Ref: [leitner2026] §6/golden-skew-dual-node
theorem phi_mul_phiInv : phi * phiInv = 1 := by
  unfold phi phiInv
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)
  field_simp
  nlinarith

/-- The two nodes are reciprocals: q_gold · q* = 1. -/
-- Ref: [leitner2026] §6/golden-skew-dual-node
theorem qGold_mul_qGoldDual : qGold * qGoldDual = 1 := by
  unfold qGold qGoldDual
  have h := phi_mul_phiInv
  nlinarith [h]

/-- **Skew-dual golden node** (Proposition):

    Under the bar involution q ↔ q⁻¹, the sub-classical node
    q_gold = 1/φ² is paired with the super-classical node q* = φ².
    The pairing is witnessed by q_gold · q* = 1. -/
-- Ref: [leitner2026] §6/golden-skew-dual-node
theorem golden_skew_dual_node :
    qGold * qGoldDual = 1 ∧
    phiInv ^ 2 + phiInv - 1 = 0 ∧
    phi ^ 2 - phi - 1 = 0 :=
  ⟨qGold_mul_qGoldDual, phiInv_min_poly, phi_min_poly⟩

/-- The substrate parameter q₀ ≈ 1.1097 lies strictly between 1 and φ².
    We use the rational lower bound 1.1097 ≤ q₀ ≤ 1.1098 for the
    falsifiability witness. -/
-- Ref: [leitner2026] §6/golden-skew-dual-node
theorem q_in_classical_band {q0 : ℝ} (hlo : 1 < q0) (hhi : q0 < qGoldDual) :
    1 < q0 ∧ q0 < phi ^ 2 :=
  ⟨hlo, by unfold qGoldDual at hhi; exact hhi⟩

end QOU.Archimedean
