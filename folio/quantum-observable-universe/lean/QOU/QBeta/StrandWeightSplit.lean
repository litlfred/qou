import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# The per-quark split μ_d − μ_u from the strand weight (prereg Addendum 10)

Premise (L): u carries `H = +1`, d carries `H = −1`, and a strand of weight `H` contributes `q ^ H`.
Premise (Q): the per-quark mass is the log-map energy of its own strand factor.

* `quark_split_eq_cell`: under (Q) the split is `−2 c log q`, the n–p cell.
* `pairSkein_diff`: under the convention-D pair-Skein map (issue #8923), over any field,
  `m_n − m_p = ((q² + q⁻²)/(q + q⁻¹)) (μ_d − μ_u)` for `p = (u,u,d)`, `n = (u,d,d)`.
* `pairSkein_factor_ne_one`: for real `q > 0`, `q ≠ 1`, that factor is not `1`, so the pair-Skein
  route and the whole-nucleon log map give different n–p differences when (Q) holds.

No measured value appears here.
-/

namespace QOU.QBeta.StrandWeightSplit

section Generic

variable {R : Type*} [Field R]

/-- Convention-D pair-Skein crossing mass (issue #8923): `(q² μ_a + q⁻² μ_b) / [2]_q`. -/
def pairSkein (q μa μb : R) : R := (q ^ 2 * μa + q⁻¹ ^ 2 * μb) / (q + q⁻¹)

/-- Nucleon mass as the sum over the three ordered pairs `(1,2), (1,3), (2,3)`. -/
def nucleon (q μ₁ μ₂ μ₃ : R) : R :=
  pairSkein q μ₁ μ₂ + pairSkein q μ₁ μ₃ + pairSkein q μ₂ μ₃

/-- `m_n − m_p` with `p = (u,u,d)`, `n = (u,d,d)`. -/
theorem pairSkein_diff (q μu μd : R) :
    nucleon q μu μd μd - nucleon q μu μu μd
      = ((q ^ 2 + q⁻¹ ^ 2) / (q + q⁻¹)) * (μd - μu) := by
  unfold nucleon pairSkein
  ring

end Generic

/-- Premise (Q): the split is the log-map image of the strand factors `q⁻¹` (d) and `q` (u). -/
theorem quark_split_eq_cell (c d₁ q : ℝ) :
    (c * Real.log (q ^ (-1 : ℤ)) + d₁) - (c * Real.log (q ^ (1 : ℤ)) + d₁) = -2 * c * Real.log q := by
  rw [zpow_neg_one, zpow_one, Real.log_inv]
  ring

/-- `q² + q⁻² − (q + q⁻¹) = (s − 2)(s + 1)` with `s = q + q⁻¹`. -/
theorem factor_sub_identity (q : ℝ) (hq : q ≠ 0) :
    q ^ 2 + q⁻¹ ^ 2 - (q + q⁻¹) = ((q + q⁻¹) - 2) * ((q + q⁻¹) + 1) := by
  field_simp
  ring

/-- For real `q > 0`, `q ≠ 1`, the pair-Skein factor `(q² + q⁻²)/(q + q⁻¹)` is not `1`. -/
theorem pairSkein_factor_ne_one (q : ℝ) (hq : 0 < q) (h1 : q ≠ 1) :
    (q ^ 2 + q⁻¹ ^ 2) / (q + q⁻¹) ≠ 1 := by
  have hs : 0 < q + q⁻¹ := by positivity
  have hgap : 0 < (q + q⁻¹) - 2 := by
    have : q + q⁻¹ - 2 = (q - 1) ^ 2 / q := by field_simp; ring
    rw [this]
    have : 0 < (q - 1) ^ 2 := by
      have : q - 1 ≠ 0 := sub_ne_zero.mpr h1
      positivity
    positivity
  intro h
  rw [div_eq_one_iff_eq hs.ne'] at h
  have := factor_sub_identity q hq.ne'
  rw [h, sub_self] at this
  have : 0 < ((q + q⁻¹) - 2) * ((q + q⁻¹) + 1) := by positivity
  linarith

section Symmetry

variable {R : Type*} [Field R]

/-- The pair-Skein nucleon mass is a weighted sum with position weights
`(2q², q² + q⁻², 2q⁻²)/[2]_q`. -/
theorem nucleon_weights (q μ₁ μ₂ μ₃ : R) :
    nucleon q μ₁ μ₂ μ₃
      = (2 * q ^ 2 * μ₁ + (q ^ 2 + q⁻¹ ^ 2) * μ₂ + 2 * q⁻¹ ^ 2 * μ₃) / (q + q⁻¹) := by
  unfold nucleon pairSkein
  ring

/-- **T2.** Cyclic relabelling of the three Borromean components changes the mass by
`(q − q⁻¹)(2μ₁ − μ₂ − μ₃)`. -/
theorem nucleon_cyclic_diff (q μ₁ μ₂ μ₃ : R) (hs : q + q⁻¹ ≠ 0) :
    nucleon q μ₁ μ₂ μ₃ - nucleon q μ₂ μ₃ μ₁ = (q - q⁻¹) * (2 * μ₁ - μ₂ - μ₃) := by
  rw [nucleon_weights, nucleon_weights, ← sub_div, div_eq_iff hs]
  ring

end Symmetry

/-- **T2 fails** for real `q > 0`, `q ≠ 1`, whenever `2μ₁ ≠ μ₂ + μ₃` (e.g. the proton `(u,u,d)`
with `μ_u ≠ μ_d`). -/
theorem nucleon_not_cyclic (q μ₁ μ₂ μ₃ : ℝ) (hq : 0 < q) (h1 : q ≠ 1)
    (hμ : 2 * μ₁ - μ₂ - μ₃ ≠ 0) :
    nucleon q μ₁ μ₂ μ₃ ≠ nucleon q μ₂ μ₃ μ₁ := by
  intro h
  have hs : q + q⁻¹ ≠ 0 := by positivity
  have hd := nucleon_cyclic_diff q μ₁ μ₂ μ₃ hs
  rw [h, sub_self] at hd
  have hh : q - q⁻¹ ≠ 0 := by
    intro h0
    have : q * q = 1 := by
      have := congrArg (· * q) h0
      simp only [sub_mul, inv_mul_cancel₀ hq.ne', zero_mul] at this
      linarith
    have : q = 1 := by nlinarith
    exact h1 this
  exact mul_ne_zero hh hμ hd.symm

/-- **T1 fails**: the first and last position weights differ for real `q > 0`, `q ≠ 1`, so the n–p
difference depends on where the flipped strand sits. -/
theorem weights_first_ne_last (q : ℝ) (hq : 0 < q) (h1 : q ≠ 1) :
    2 * q ^ 2 / (q + q⁻¹) ≠ 2 * q⁻¹ ^ 2 / (q + q⁻¹) := by
  have hs : 0 < q + q⁻¹ := by positivity
  intro h
  rw [div_left_inj' hs.ne'] at h
  have h2 : q ^ 2 = q⁻¹ ^ 2 := by linarith
  have hinv : q ^ 2 * q⁻¹ ^ 2 = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ hq.ne', one_pow]
  have h4 : q ^ 2 * q ^ 2 = 1 := by
    calc q ^ 2 * q ^ 2 = q ^ 2 * q⁻¹ ^ 2 := by rw [← h2]
      _ = 1 := hinv
  have hq2 : q ^ 2 = 1 := by nlinarith [sq_nonneg (q ^ 2 - 1), pow_pos hq 2]
  have : q = 1 := by nlinarith [sq_nonneg (q - 1)]
  exact h1 this

end QOU.QBeta.StrandWeightSplit
