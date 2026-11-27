import QOU.Core.CategoricalLagrangianTwoTermBridge

/-!
# The concrete two-term bridge with Cartan-weighted matter traces

`CategoricalLagrangianTwoTermBridge.trace_lagrangian_diff_concrete_borromean_weight_space`
makes two choices that conflict with `MatterTraceWeightVector`:

* `hHoriz` sets the proton and neutron horizontal matter traces equal. When the states are
  `K`-weight vectors and the flip intertwines the connections, this forces the horizontal
  matrix element to `0` (`matrix_element_zero_of_equal_traces`).
* The matter-Reeb (Coulomb) traces carry no Cartan weight, while the bosonic Reeb² traces
  do. By `qtrace_rank_one`, a matter trace on a weight-`q` state carries weight `q`.

This file restates the theorem with both weights in place. The proton horizontal matter trace
is `q · c`, the neutron's `q⁻¹ · c` (one common matrix element `c`). The Coulomb traces are
`q · tr((Q₁₂ + Q₂₃)V³_A)` and `q⁻¹ · tr((Q₁₂ + Q₂₃)V³_B)`. The bosonic hypotheses are unchanged.

The result: the difference is the unchanged bosonic Reeb² term, plus `(q⁻² − 1)·c`, plus a
re-weighted Coulomb term. The weighted Coulomb term is a different rational function from the
bridge's unweighted one. At `q = 1` both are `−2/3`.

Nothing here fixes `c`.
-/

namespace QOU.MassTheory.WeightedTwoTermBridge

open CategoryTheory Matrix QOU.CategoricalLagrangianTwoTermBridge
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

universe u v

variable {F : Type*} [Field F]
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
  [Preadditive C] [Linear F C] {fh : FrobeniusHopfData C}

/-- The weighted Coulomb difference `q⁻¹·tr(Q V³_B) − q·tr(Q V³_A)`. -/
theorem weighted_QAdj_diff_borromeanV3 (q : F) (hq : q ≠ 0) (h3 : (3 : F) ≠ 0) :
    q⁻¹ * trace ((Q12n + Q23n) * borromeanV3B q) - q * trace ((Q12p + Q23p) * borromeanV3A q) =
      (2 * q ^ 14 - 2 * q ^ 12 - 9 * q ^ 10 + 20 * q ^ 8 - 26 * q ^ 6 + 18 * q ^ 4
        - 13 * q ^ 2 + 4) / (9 * q ^ 7) := by
  rw [trace_QAdjn_borromeanV3 q hq h3, trace_QAdjp_borromeanV3 q hq h3]
  have h9 : (9 : F) ≠ 0 := by
    have : (9 : F) = 3 * 3 := by norm_num
    rw [this]; exact mul_ne_zero h3 h3
  field_simp
  ring

/-- **The concrete bridge with Cartan-weighted matter traces.** -/
theorem trace_lagrangian_diff_weighted_borromean
    (τ : (fh.obj ⟶ fh.obj) →ₗ[F] F)
    (L_n L_p : CategoricalLagrangian F C fh)
    (q c : F) (hq : q ≠ 0) (h3 : (3 : F) ≠ 0)
    (hQn : L_n.dirac.qinv = q⁻¹)
    (hQp : L_p.dirac.qinv = q⁻¹)
    (hNabla : L_n.dirac.nablaEndo = L_p.dirac.nablaEndo)
    (hCross :
      τ (L_n.dirac.nablaEndo ≫ L_n.dirac.reeb + L_n.dirac.reeb ≫ L_n.dirac.nablaEndo) =
      τ (L_p.dirac.nablaEndo ≫ L_p.dirac.reeb + L_p.dirac.reeb ≫ L_p.dirac.nablaEndo))
    (hReebN : τ (L_n.dirac.reeb ≫ L_n.dirac.reeb) = q⁻¹ * trace (borromeanV3B q))
    (hReebP : τ (L_p.dirac.reeb ≫ L_p.dirac.reeb) = q * trace (borromeanV3A q))
    (hHorizP : τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo) = q * c)
    (hHorizN : τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) = q⁻¹ * c)
    (hMatReebN :
      τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb) =
      q⁻¹ * trace ((Q12n + Q23n) * borromeanV3B q))
    (hMatReebP :
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb) =
      q * trace ((Q12p + Q23p) * borromeanV3A q)) :
    τ L_n.lagrangian - τ L_p.lagrangian =
      (1 - q⁻¹) ^ 2 * (q⁻¹ - q) *
        (-(q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6) +
      (q⁻¹ ^ 2 - 1) * c +
      (1 - q⁻¹) *
        ((2 * q ^ 14 - 2 * q ^ 12 - 9 * q ^ 10 + 20 * q ^ 8 - 26 * q ^ 6 + 18 * q ^ 4
          - 13 * q ^ 2 + 4) / (9 * q ^ 7)) := by
  have hQinv : L_n.dirac.qinv = L_p.dirac.qinv := hQn.trans hQp.symm
  rw [trace_lagrangian_diff_shared_spatial_closure τ L_n L_p hQinv hNabla hCross,
    trace_matter_two_term_expansion τ L_n, trace_matter_two_term_expansion τ L_p,
    hQn, hQp, hHorizP, hHorizN, hReebN, hReebP, hMatReebN, hMatReebP,
    trace_borromeanV3B q hq, trace_borromeanV3A q hq]
  have hW := weighted_QAdj_diff_borromeanV3 q hq h3
  have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  linear_combination (1 - q⁻¹) * hW + (-c) * hqq

end QOU.MassTheory.WeightedTwoTermBridge
