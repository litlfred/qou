import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity


/-!
# QOU.Archimedean.bar_self_dual_confinement_band — Maximal bar-invariant band

The open interval ℬ = (1/φ², φ²) is the maximal connected open
sub-interval of ℝ_{>0} that is invariant under the bar involution
q ↦ q⁻¹ and avoids both golden nodes {1/φ², φ²}.

This file is self-contained: it redefines φ, 1/φ, q_gold, q* locally
(in a private subnamespace) so that it can be checked independently
of the GoldenSkewDualNode sibling.

LaTeX label: `prop:bar-self-dual-confinement-band`

## References

- [leitner2026] §6/bar-self-dual-confinement-band
- [leitner2026] §6/golden-skew-dual-node
- [leitner2026] §7/deconfinement-golden-threshold
-/

namespace QOU.Archimedean.BarSelfDualConfBand

/-- The golden ratio φ = (1 + √5)/2. -/
noncomputable def phi : ℝ := (1 + Real.sqrt 5) / 2

/-- The reciprocal of the golden ratio, 1/φ = (√5 − 1)/2. -/
noncomputable def phiInv : ℝ := (Real.sqrt 5 - 1) / 2

/-- The sub-classical golden node q_gold = 1/φ². -/
noncomputable def qGold : ℝ := phiInv ^ 2

/-- The skew-dual golden node q* = φ². -/
noncomputable def qGoldDual : ℝ := phi ^ 2

/-- The bar involution on the positive reals: q ↦ q⁻¹. -/
noncomputable def bar (q : ℝ) : ℝ := q⁻¹

/-- The bar-self-dual confinement band ℬ = (1/φ², φ²). -/
noncomputable def confBand : Set ℝ := Set.Ioo qGold qGoldDual

private theorem sqrt5_sq : Real.sqrt 5 ^ 2 = 5 :=
  Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)

private theorem sqrt5_nonneg : (0 : ℝ) ≤ Real.sqrt 5 := Real.sqrt_nonneg _

/-- 1 < √5. -/
private theorem one_lt_sqrt5 : 1 < Real.sqrt 5 := by
  nlinarith [sqrt5_sq, sqrt5_nonneg]

/-- √5 < 3. -/
private theorem sqrt5_lt_three : Real.sqrt 5 < 3 := by
  nlinarith [sqrt5_sq, sqrt5_nonneg]

/-- φ > 1. -/
theorem phi_gt_one : 1 < phi := by
  unfold phi
  linarith [one_lt_sqrt5]

/-- 1/φ < 1. -/
theorem phiInv_lt_one : phiInv < 1 := by
  unfold phiInv
  linarith [sqrt5_lt_three]

/-- 1/φ > 0. -/
theorem phiInv_pos : 0 < phiInv := by
  unfold phiInv
  linarith [one_lt_sqrt5]

/-- φ > 0. -/
theorem phi_pos : 0 < phi := by
  unfold phi
  linarith [sqrt5_nonneg]

/-- φ · (1/φ) = 1. -/
theorem phi_mul_phiInv : phi * phiInv = 1 := by
  unfold phi phiInv
  field_simp
  nlinarith [sqrt5_sq]

/-- q_gold · q* = 1. -/
theorem qGold_mul_qGoldDual : qGold * qGoldDual = 1 := by
  unfold qGold qGoldDual
  have h : phi * phiInv = 1 := phi_mul_phiInv
  nlinarith [h]

/-- 1/φ² > 0. -/
theorem qGold_pos : 0 < qGold := by
  unfold qGold
  have h : 0 < phiInv := phiInv_pos
  positivity

/-- φ² > 0. -/
theorem qGoldDual_pos : 0 < qGoldDual := by
  unfold qGoldDual
  have h : 0 < phi := phi_pos
  positivity

/-- 1/φ² < 1. -/
theorem qGold_lt_one : qGold < 1 := by
  unfold qGold
  have h1 : 0 < phiInv := phiInv_pos
  have h2 : phiInv < 1 := phiInv_lt_one
  nlinarith

/-- 1 < φ². -/
theorem one_lt_qGoldDual : 1 < qGoldDual := by
  unfold qGoldDual
  have h1 : 0 < phi := phi_pos
  have h2 : 1 < phi := phi_gt_one
  nlinarith

/-- 1/φ² < φ². -/
theorem qGold_lt_qGoldDual : qGold < qGoldDual := by
  linarith [qGold_lt_one, one_lt_qGoldDual]

/-- The band ℬ is non-empty: 1 ∈ ℬ. -/
theorem one_mem_confBand : (1 : ℝ) ∈ confBand := by
  unfold confBand
  exact ⟨qGold_lt_one, one_lt_qGoldDual⟩

/-- φ² is the multiplicative inverse of 1/φ². -/
theorem qGoldDual_eq_inv_qGold : qGoldDual = qGold⁻¹ := by
  have hg_ne : qGold ≠ 0 := ne_of_gt qGold_pos
  rw [inv_eq_one_div, eq_div_iff hg_ne]
  have h := qGold_mul_qGoldDual
  linarith [mul_comm qGold qGoldDual]

/-- 1/φ² is the multiplicative inverse of φ². -/
theorem qGold_eq_inv_qGoldDual : qGold = qGoldDual⁻¹ := by
  rw [qGoldDual_eq_inv_qGold, inv_inv]

/-- The bar involution is an involution on nonzero reals. -/
theorem bar_bar (q : ℝ) (_ : q ≠ 0) : bar (bar q) = q := by
  unfold bar
  exact inv_inv q

/-- **Bar-invariance of the confinement band**: q ∈ ℬ iff q⁻¹ ∈ ℬ. -/
theorem bar_invariant_confBand (q : ℝ) (hq : 0 < q) :
    q ∈ confBand ↔ q⁻¹ ∈ confBand := by
  unfold confBand
  simp only [Set.mem_Ioo]
  have hg : 0 < qGold := qGold_pos
  have hd : 0 < qGoldDual := qGoldDual_pos
  have hd_eq : qGoldDual = qGold⁻¹ := qGoldDual_eq_inv_qGold
  have hg_eq : qGold = qGoldDual⁻¹ := qGold_eq_inv_qGoldDual
  have hqi : 0 < q⁻¹ := inv_pos.mpr hq
  refine ⟨fun ⟨h1, h2⟩ => ⟨?_, ?_⟩, fun ⟨h1, h2⟩ => ⟨?_, ?_⟩⟩
  · rw [hg_eq]; exact (inv_lt_inv₀ hd hq).mpr h2
  · rw [hd_eq]; exact (inv_lt_inv₀ hq hg).mpr h1
  · rw [show q = q⁻¹⁻¹ from (inv_inv q).symm, hg_eq]
    exact (inv_lt_inv₀ hd hqi).mpr h2
  · rw [show q = q⁻¹⁻¹ from (inv_inv q).symm, hd_eq]
    exact (inv_lt_inv₀ hqi hg).mpr h1

/-- **Bar-self-dual confinement band** (Proposition):

    ℬ = (1/φ², φ²) is invariant under the bar involution q ↦ q⁻¹,
    contains q = 1, and the two endpoints are bar-paired
    (qGold · qGoldDual = 1). -/
theorem bar_self_dual_confinement_band :
    qGold * qGoldDual = 1 ∧
    qGold < qGoldDual ∧
    (1 : ℝ) ∈ confBand ∧
    ∀ q : ℝ, 0 < q → (q ∈ confBand ↔ bar q ∈ confBand) :=
  ⟨qGold_mul_qGoldDual, qGold_lt_qGoldDual, one_mem_confBand,
   fun q hq => bar_invariant_confBand q hq⟩

end QOU.Archimedean.BarSelfDualConfBand
