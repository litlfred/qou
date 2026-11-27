import QOU.Nuclear.NucleonDownStrandSelfEnergy
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The Weyl-odd self term against the Gibbs cell (archimedean)

Split off `QOU.Nuclear.NucleonDownStrandSelfEnergy` at the transcendental boundary (bean
`qou-gfsr`); name and namespace unchanged. The algebraic self-sum, Legendre and canonical
results stay in that module; only the comparison with `log q` lives here.
-/

namespace QOU.Nuclear.NucleonDownStrandSelfEnergy

/-- **The Weyl-odd self term is strictly below the Gibbs cell**: `2(1 − q⁻¹) < 2 log q` for
`1 < q`. -/
theorem self_cartan_lt_gibbs_cell (q : ℝ) (hq : 1 < q) : 2 * (1 - q⁻¹) < 2 * Real.log q := by
  have hq0 : 0 < q := by linarith
  have hi0 : 0 < q⁻¹ := inv_pos.mpr hq0
  have hi1 : q⁻¹ ≠ 1 := by
    intro h
    have : q = 1 := by rw [← inv_inv q, h, inv_one]
    linarith
  have hlt := Real.log_lt_sub_one_of_pos hi0 hi1
  rw [Real.log_inv] at hlt
  linarith

end QOU.Nuclear.NucleonDownStrandSelfEnergy
