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

end QOU.QBeta.StrandWeightSplit
