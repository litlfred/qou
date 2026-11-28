import QOU.StandardModel.ElectroweakVevGaps

/-!
# QOU.Transcendental.StandardModel.ElectroweakVevGapsReal

The `π`-valued part of `QOU.StandardModel.ElectroweakVevGaps`: the per-carrier zero-mode
rule evaluated at the EM and EW carriers on `Σ₄` (`2/(3π)` and `1/π`, through the
Gauss–Bonnet area `4π(g − 1)`), and the reduced decomposition that rewrites through the EW
value. Names and namespace are unchanged (transcendental-boundary strangler, bean
`qou-dk7p`).
-/

namespace QOU.StandardModel.EwVevGaps

open QOU.Archimedean (gaussBonnetArea bringZeroModeValue)
open QOU.StandardModel.EwVevDecomposition
  (EwVevHypotheses carrierRuleZeroMode carrierRule_ew)

/-- At the two EM carriers on `Σ₄` the per-carrier rule gives `2/(3π)`. -/
theorem perCarrier_em : perCarrierZeroMode 2 4 = bringZeroModeValue := by
  unfold perCarrierZeroMode gaussBonnetArea bringZeroModeValue
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

/-- At the three EW carriers on `Σ₄` the per-carrier rule gives `1/π`. -/
theorem perCarrier_ew : perCarrierZeroMode 3 4 = ewBringZeroMode := by
  rw [ewBringZeroMode_eq_one_div_pi]
  unfold perCarrierZeroMode gaussBonnetArea
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

/-! ## Section 6: reduced decomposition -/

/-- **Reduced hypotheses (§3b-cond, NO instance).** Compared with `EwVevHypotheses`:
the zero mode is the uniform per-carrier rule at three carriers (which also gives the EM
value, `perCarrier_em`); the sign is the `b₀` rule applied to the sector's group, with the
assignment of the `SU(2)_L` content made an explicit field; the dressing exponent `k` is an
explicit field (`k = 1` is a per-sector dispatch, no rule found). `tree`, `c_loop` and
`self_consistency` are unchanged. -/
class EwVevReducedHypotheses (q Nv treeTerm zeroMode s c αloop b0 : ℝ) (k : ℕ) : Prop where
  Nv_pos : 0 < Nv
  assembly : Nv = treeTerm + zeroMode + s * αloop * ewHabiroNorm q * (1 - c * αloop)
  /-- Tree term in the exponent family. -/
  tree : treeTerm = treeK q k
  /-- Dressing exponent: open dispatch (`qou-rpt1`). -/
  dressing_exponent : k = 1
  /-- Uniform per-carrier zero-mode rule, three carriers on `Σ₄`. -/
  zero_mode : zeroMode = perCarrierZeroMode 3 4
  /-- Sector assignment: the loop dressing the vev sector is the SM `SU(2)_L` loop. -/
  sector_group : b0 = oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2)
  /-- Sign rule `s = −sgn b₀`. -/
  sign_rule : s = signRule b0
  c_loop : c = (ewHbarQ q) ^ 2
  self_consistency : αloop * Nv = 1

/-- **The reduced hypotheses imply `EwVevHypotheses`.** -/
theorem ewVevReduced_imp_hypotheses (q Nv treeTerm zeroMode s c αloop b0 : ℝ) (k : ℕ)
    [hyp : EwVevReducedHypotheses q Nv treeTerm zeroMode s c αloop b0 k] :
    EwVevHypotheses q Nv treeTerm zeroMode s c αloop := by
  refine ⟨hyp.Nv_pos, hyp.assembly, ?_, ?_, ?_, hyp.c_loop, hyp.self_consistency⟩
  · rw [hyp.tree, hyp.dressing_exponent, treeK_one]
  · rw [hyp.zero_mode, perCarrier_ew, carrierRule_ew]
  · rw [hyp.sign_rule, hyp.sector_group, signRule_su2]

end QOU.StandardModel.EwVevGaps
