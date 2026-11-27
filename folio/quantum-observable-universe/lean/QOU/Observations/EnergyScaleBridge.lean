/-
# One scale for masses: the Euler derivative bridges the log chart and the mass chart

Thread "Unify the log and mass-formula energy scales" (2026-11-27). Analytic half:
`QOU.Transcendental.MassTheory.EnergyScaleBridge`. Audit:
`docs/audits/2026-11-27-energy-scale-bridge.md`.

Two CAL-1 charts are on record. For a trace weight `τ_X` write `L_X = log τ_X` and
`w_X = q ∂_q log τ_X`.

* **Log chart** (`k = 0`, #9718): `E₀(X) = m_e · L_X / L_e`.
* **Mass chart** (`k = 1`, #9692, #9733): `E₁(X) = m_e · w_X / w_e`.

With `β = ln q` the Euler operator `δ = q ∂_q` is `∂_β`, and `w = δ L`. So the mass chart is
the derivative of the log chart, and the two are tied by the quotient rule. This file proves the
algebraic content over a generic (ordered) field. The derivative facts it takes as data
(`w = δL`, the quotient rule) are proved for real functions in the analytic half.

* `chart_gap`: `E₁(X) − E₀(X) = m_e · (L_e/w_e) · δ(L_X/L_e)`.
* `charts_agree_iff`: the charts agree on `X` iff `L_X / L_e` is stationary.
* `legendre_additive`: `S = L − β w` (the Legendre partner, an entropy) is additive too.
* `sign_agree_iff`: given `L_e < 0 < w_e`, the charts agree in sign on `X` iff
  `L_X · w_X < 0`.
* `pure_power_sign_flip`: on a pure power `q^k` the two charts give opposite signs
  whenever `L_e < 0 < w_e`. The electron is such a case (`τ_e < 1`, `w_e > 0`).
* `np_cell_log_pos`, `np_cell_mass_neg`: so the n−p cell `τ_n = q⁻² τ_p` puts the neutron
  above the proton in the log chart and below it in the mass chart.
* `bond_unbinds_log_chart`, `bond_unbinds_mass_chart`: a bond letter with `f < 1` that grows
  with `q` adds mass in both charts, so `B = −E(f) < 0`.
* `ruled_law_opposite`: the ruled law `B = T · log(tr_free/tr_atom)`, `T > 0`, has the
  opposite sign to the CAL-1 log-chart reading of the same letter.

No measured value enters.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.Observations.EnergyScaleBridge

section Field

variable {R : Type*} [Field R]

/-- The Euler derivative of the ratio `L_X / L_e` by the quotient rule, given
`δ L_X = w_X` and `δ L_e = w_e`. -/
def ratioFlow (LX Le wX we : R) : R := (wX * Le - LX * we) / Le ^ 2

/-- **Chart gap.** `m·w_X/w_e − m·L_X/L_e = m·(L_e/w_e)·δ(L_X/L_e)`. -/
theorem chart_gap (m LX Le wX we : R) (hLe : Le ≠ 0) (hwe : we ≠ 0) :
    m * wX / we - m * LX / Le = m * (Le / we) * ratioFlow LX Le wX we := by
  unfold ratioFlow
  field_simp

/-- **The charts agree on `X` iff the log-chart ratio is stationary.** -/
theorem charts_agree_iff (m LX Le wX we : R) (hm : m ≠ 0) (hLe : Le ≠ 0) (hwe : we ≠ 0) :
    m * wX / we = m * LX / Le ↔ ratioFlow LX Le wX we = 0 := by
  rw [← sub_eq_zero, chart_gap m LX Le wX we hLe hwe]
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h1
    · rcases mul_eq_zero.mp h1 with h2 | h2
      · exact absurd h2 hm
      · exact absurd h2 (div_ne_zero hLe hwe)
    · exact h1
  · intro h; rw [h, mul_zero]

/-- **Legendre partner.** `S = L − β·w` is additive whenever `L` and `w` are. -/
theorem legendre_additive (β L₁ L₂ w₁ w₂ : R) :
    (L₁ + L₂) - β * (w₁ + w₂) = (L₁ - β * w₁) + (L₂ - β * w₂) := by ring

/-- On a pure power `q^k` (`L = k·β`, `w = k`) the ratio of the two charts' readings is
`L_e / (β·w_e)`, independent of `k` and of `m`. -/
theorem pure_power_ratio (m k β Le we : R) (hm : m ≠ 0) (hk : k ≠ 0) (hβ : β ≠ 0)
    (hLe : Le ≠ 0) (hwe : we ≠ 0) :
    (m * k / we) / (m * (k * β) / Le) = Le / (β * we) := by
  field_simp

end Field

section Ordered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Sign flip on pure powers.** If `β > 0` and `L_e < 0 < w_e`, the log chart and the mass
chart give a pure power `q^k`, `k ≠ 0`, readings of opposite sign. -/
theorem pure_power_sign_flip (m k β Le we : R) (hm : 0 < m) (hk : k ≠ 0) (hβ : 0 < β)
    (hLe : Le < 0) (hwe : 0 < we) :
    (m * k / we) * (m * (k * β) / Le) < 0 := by
  have hk2 : 0 < k ^ 2 := by positivity
  have e : (m * k / we) * (m * (k * β) / Le) = (m ^ 2 * k ^ 2 * β) / (we * Le) := by
    field_simp
  rw [e]
  apply div_neg_of_pos_of_neg
  · positivity
  · exact mul_neg_of_pos_of_neg hwe hLe

/-- **When do the two charts agree in sign?** With the electron oriented as it is
(`L_e < 0 < w_e`), the readings `E₀(X)` and `E₁(X)` have the same sign iff `L_X` and `w_X`
have opposite signs, that is, iff `X` is "like the electron" (weight below 1 and rising, or
above 1 and falling). -/
theorem sign_agree_iff (m LX Le wX we : R) (hm : 0 < m) (hLe : Le < 0) (hwe : 0 < we) :
    0 < (m * wX / we) * (m * LX / Le) ↔ LX * wX < 0 := by
  have hd : we * Le < 0 := mul_neg_of_pos_of_neg hwe hLe
  have e : (m * wX / we) * (m * LX / Le) = (m ^ 2 * (LX * wX)) / (we * Le) := by
    field_simp
  rw [e]
  have hm2 : 0 < m ^ 2 := by positivity
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    have : (m ^ 2 * (LX * wX)) / (we * Le) ≤ 0 :=
      div_nonpos_of_nonneg_of_nonpos (mul_nonneg hm2.le hc) hd.le
    linarith
  · intro h
    exact div_pos_of_neg_of_neg (mul_neg_of_pos_of_neg hm2 h) hd

/-- **n−p cell, log chart.** `L_n − L_p = −2β`: the neutron lies above the proton. -/
theorem np_cell_log_pos (m β Le : R) (hm : 0 < m) (hβ : 0 < β) (hLe : Le < 0) :
    0 < m * (-2 * β) / Le := by
  apply div_pos_of_neg_of_neg _ hLe
  have : 0 < m * (2 * β) := by positivity
  linarith [show m * (-2 * β) = -(m * (2 * β)) by ring]

/-- **n−p cell, mass chart.** `w_n − w_p = −2`: the neutron lies below the proton. -/
theorem np_cell_mass_neg (m we : R) (hm : 0 < m) (hwe : 0 < we) :
    m * (-2) / we < 0 := by
  apply div_neg_of_neg_of_pos _ hwe
  linarith

/-- **A shrinking bond letter adds mass in the log chart.** If `L_f < 0` (`f < 1`) then, with
the CAL-1 orientation `L_e < 0`, `B = −E₀(f) < 0`. -/
theorem bond_unbinds_log_chart (m Lf Le : R) (hm : 0 < m) (hLf : Lf < 0) (hLe : Le < 0) :
    -(m * Lf / Le) < 0 := by
  have : 0 < m * Lf / Le := div_pos_of_neg_of_neg (mul_neg_of_pos_of_neg hm hLf) hLe
  linarith

/-- **A growing bond letter adds mass in the mass chart.** If `w_f > 0` then, with `w_e > 0`,
`B = −E₁(f) < 0`. -/
theorem bond_unbinds_mass_chart (m wf we : R) (hm : 0 < m) (hwf : 0 < wf) (hwe : 0 < we) :
    -(m * wf / we) < 0 := by
  have : 0 < m * wf / we := by positivity
  linarith

/-- **The ruled log law runs against the CAL-1 log chart.** The law
`B = T·log(tr_free/tr_atom) = T·(−L_f)` with `T > 0` and the CAL-1 reading
`B = −m·L_f/L_e` have opposite signs on every letter with `L_f < 0`. -/
theorem ruled_law_opposite (T m Lf Le : R) (hT : 0 < T) (hm : 0 < m) (hLf : Lf < 0)
    (hLe : Le < 0) :
    (T * -Lf) * (-(m * Lf / Le)) < 0 := by
  have h1 : 0 < T * -Lf := mul_pos hT (by linarith)
  exact mul_neg_of_pos_of_neg h1 (bond_unbinds_log_chart m Lf Le hm hLf hLe)

end Ordered

end QOU.Observations.EnergyScaleBridge
