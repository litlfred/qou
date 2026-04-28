/-!
# QOU.Organic.BondOrderEnergyFormula — Linear BDE(k) ≈ k · BDE_1

The first-order linear approximation for the bond dissociation
energy as a function of the bond order k.

## References

- [manuscript] Ch. 10, Proposition `prop:bond-order-energy-formula`
- [luo2007] Y.-R. Luo, Comprehensive Handbook of Chemical Bond Energies, CRC Press 2007
-/

namespace QOU.Organic

/-- Linear bond-order energy: BDE(k) = k · BDE_1. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:bond-order-energy-formula
def bondOrderEnergyLinear (k bde_1 : ℝ) : ℝ := k * bde_1

/-- Bond-order-energy with explicit resonance correction. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:bond-order-energy-formula
def bondOrderEnergyFormula (k bde_1 res : ℝ) : ℝ :=
  bondOrderEnergyLinear k bde_1 + res

/-- The exact formula equals the linear approximation when the
    resonance correction vanishes. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:bond-order-energy-formula
theorem bondOrderEnergyFormula_zero_resonance (k bde_1 : ℝ) :
    bondOrderEnergyFormula k bde_1 0 = bondOrderEnergyLinear k bde_1 := by
  unfold bondOrderEnergyFormula
  ring

/-- For positive k and BDE_1, the linear prediction is positive. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:bond-order-energy-formula
theorem bondOrderEnergyLinear_pos
    (k bde_1 : ℝ) (h_k : 0 < k) (h_b : 0 < bde_1) :
    0 < bondOrderEnergyLinear k bde_1 := by
  unfold bondOrderEnergyLinear
  exact mul_pos h_k h_b

/-- Linearity in BDE_1: doubling the single-bond reference doubles
    the predicted energy. -/
-- Ref: [manuscript] Ch. 10, Proposition prop:bond-order-energy-formula
theorem bondOrderEnergyLinear_scale (k bde_1 c : ℝ) :
    bondOrderEnergyLinear k (c * bde_1) = c * bondOrderEnergyLinear k bde_1 := by
  unfold bondOrderEnergyLinear
  ring

end QOU.Organic
