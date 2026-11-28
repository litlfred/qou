/-
# One scale for masses: the Euler derivative bridges the log chart and the mass chart

Thread "Unify the log and mass-formula energy scales" (2026-11-27). Analytic half:
`QOU.Transcendental.MassTheory.EnergyScaleBridge`. Audit:
`docs/audits/2026-11-27-energy-scale-bridge.md`.

Two CAL-1 charts are on record. For a trace weight `τ_X` write `L_X = log τ_X` and
`w_X = q ∂_q log τ_X`.

* **Log chart** (`k = 0`, #9718): `E₀(X) = m_e · L_X · L_e⁻¹`.
* **Mass chart** (`k = 1`, #9692, #9733): `E₁(X) = m_e · w_X · w_e⁻¹`.

With `β = ln q` the Euler operator `δ = q ∂_q` is `∂_β`, and `w = δ L`. So the mass chart is
the derivative of the log chart, and the two are tied by the quotient rule. This file proves the
algebraic content over a generic (strict ordered) commutative ring using invertible unit readings
`Le, we : Rˣ` (§7c base-ring discipline). The derivative facts it takes as data (`w = δL`, the
quotient rule) are proved for real functions in the analytic half.

* `chart_gap`: `E₁(X) − E₀(X) = m_e · (L_e · w_e⁻¹) · δ(L_X · L_e⁻¹)`.
* `charts_agree_iff`: the charts agree on `X` iff `L_X · L_e⁻¹` is stationary.
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
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.Observations.EnergyScaleBridge

section Ring

variable {R : Type*} [CommRing R]

/-- The Euler derivative of the ratio `L_X · L_e⁻¹` by the quotient rule over a commutative ring,
given `δ L_X = w_X` and `δ L_e = w_e` for an invertible electron log reading `Le : Rˣ`. -/
def ratioFlow (LX : R) (Le : Rˣ) (wX we : R) : R :=
  (wX * (Le : R) - LX * we) * ((↑Le⁻¹ : R) ^ 2)

/-- **Chart gap.** `m·w_X·w_e⁻¹ − m·L_X·L_e⁻¹ = m·(L_e·w_e⁻¹)·δ(L_X·L_e⁻¹)`. -/
theorem chart_gap (m LX : R) (Le : Rˣ) (wX : R) (we : Rˣ) :
    m * wX * (↑we⁻¹ : R) - m * LX * (↑Le⁻¹ : R) =
      m * ((Le : R) * (↑we⁻¹ : R)) * ratioFlow LX Le wX (we : R) := by
  unfold ratioFlow
  have hLe : (Le : R) * (↑Le⁻¹ : R) = 1 := Units.mul_inv Le
  have hwe : (we : R) * (↑we⁻¹ : R) = 1 := Units.mul_inv we
  calc
    m * wX * (↑we⁻¹ : R) - m * LX * (↑Le⁻¹ : R)
        = m * wX * (↑we⁻¹ : R) * ((Le : R) * (↑Le⁻¹ : R)) ^ 2 -
            m * LX * ((we : R) * (↑we⁻¹ : R)) * ((Le : R) * (↑Le⁻¹ : R)) * (↑Le⁻¹ : R) := by
          rw [hLe, hwe]; ring
    _ = m * ((Le : R) * (↑we⁻¹ : R)) *
          ((wX * (Le : R) - LX * (we : R)) * ((↑Le⁻¹ : R) ^ 2)) := by
          ring

/-- **The charts agree on `X` iff the log-chart ratio is stationary.** -/
theorem charts_agree_iff [NoZeroDivisors R] [Nontrivial R]
    (m LX : R) (Le : Rˣ) (wX : R) (we : Rˣ) (hm : m ≠ 0) :
    m * wX * (↑we⁻¹ : R) = m * LX * (↑Le⁻¹ : R) ↔ ratioFlow LX Le wX (we : R) = 0 := by
  have hLe0 : (Le : R) ≠ 0 := Le.ne_zero
  have hwe0 : (↑we⁻¹ : R) ≠ 0 := (we⁻¹).ne_zero
  rw [← sub_eq_zero, chart_gap m LX Le wX we]
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h1
    · rcases mul_eq_zero.mp h1 with h2 | h2
      · exact absurd h2 hm
      · exact absurd h2 (mul_ne_zero hLe0 hwe0)
    · exact h1
  · intro h; rw [h, mul_zero]

/-- **Legendre partner.** `S = L − β·w` is additive whenever `L` and `w` are. -/
theorem legendre_additive (β L₁ L₂ w₁ w₂ : R) :
    (L₁ + L₂) - β * (w₁ + w₂) = (L₁ - β * w₁) + (L₂ - β * w₂) := by ring

/-- On a pure power `q^k` (`L = k·β`, `w = k`), the mass-chart reading equals the log-chart
reading multiplied by the universal factor `L_e · β⁻¹ · w_e⁻¹`, independent of `k` and `m`. -/
theorem pure_power_ratio (m k : R) (β Le we : Rˣ) :
    m * k * (↑we⁻¹ : R) =
      (m * (k * (β : R)) * (↑Le⁻¹ : R)) * ((Le : R) * (↑β⁻¹ : R) * (↑we⁻¹ : R)) := by
  have hβ : (β : R) * (↑β⁻¹ : R) = 1 := Units.mul_inv β
  have hLe : (Le : R) * (↑Le⁻¹ : R) = 1 := Units.mul_inv Le
  calc
    m * k * (↑we⁻¹ : R)
        = m * k * ((β : R) * (↑β⁻¹ : R)) * ((Le : R) * (↑Le⁻¹ : R)) * (↑we⁻¹ : R) := by
          rw [hβ, hLe]; ring
    _ = (m * (k * (β : R)) * (↑Le⁻¹ : R)) * ((Le : R) * (↑β⁻¹ : R) * (↑we⁻¹ : R)) := by
          ring

end Ring

section Ordered

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- In a strict ordered commutative ring, the inverse of a positive unit is positive. -/
theorem unit_inv_pos (u : Rˣ) (hu : 0 < (u : R)) : 0 < (↑u⁻¹ : R) := by
  by_contra h
  push_neg at h
  have hmul : (u : R) * (↑u⁻¹ : R) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hu.le h
  rw [Units.mul_inv u] at hmul
  linarith [zero_lt_one (α := R)]

/-- In a strict ordered commutative ring, the inverse of a negative unit is negative. -/
theorem unit_inv_neg (u : Rˣ) (hu : (u : R) < 0) : (↑u⁻¹ : R) < 0 := by
  by_contra h
  push_neg at h
  have hmul : (u : R) * (↑u⁻¹ : R) ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hu.le h
  rw [Units.mul_inv u] at hmul
  linarith [zero_lt_one (α := R)]

/-- **Sign flip on pure powers.** If `β > 0` and `L_e < 0 < w_e`, the log chart and the mass
chart give a pure power `q^k`, `k ≠ 0`, readings of opposite sign. -/
theorem pure_power_sign_flip (m k β : R) (Le we : Rˣ) (hm : 0 < m) (hk : k ≠ 0) (hβ : 0 < β)
    (hLe : (Le : R) < 0) (hwe : 0 < (we : R)) :
    (m * k * (↑we⁻¹ : R)) * (m * (k * β) * (↑Le⁻¹ : R)) < 0 := by
  have hk2 : 0 < k ^ 2 := sq_pos_of_ne_zero hk
  have hm2 : 0 < m ^ 2 := sq_pos_of_ne_zero hm.ne'
  have hiLe : (↑Le⁻¹ : R) < 0 := unit_inv_neg Le hLe
  have hiwe : 0 < (↑we⁻¹ : R) := unit_inv_pos we hwe
  have hpos : 0 < m ^ 2 * k ^ 2 * β * (↑we⁻¹ : R) :=
    mul_pos (mul_pos (mul_pos hm2 hk2) hβ) hiwe
  have heq : (m * k * (↑we⁻¹ : R)) * (m * (k * β) * (↑Le⁻¹ : R)) =
      (m ^ 2 * k ^ 2 * β * (↑we⁻¹ : R)) * (↑Le⁻¹ : R) := by ring
  rw [heq]
  exact mul_neg_of_pos_of_neg hpos hiLe

/-- **When do the two charts agree in sign?** With the electron oriented as it is
(`L_e < 0 < w_e`), the readings `E₀(X)` and `E₁(X)` have the same sign iff `L_X` and `w_X`
have opposite signs, that is, iff `X` is "like the electron" (weight below 1 and rising, or
above 1 and falling). -/
theorem sign_agree_iff (m LX : R) (Le : Rˣ) (wX : R) (we : Rˣ)
    (hm : 0 < m) (hLe : (Le : R) < 0) (hwe : 0 < (we : R)) :
    0 < (m * wX * (↑we⁻¹ : R)) * (m * LX * (↑Le⁻¹ : R)) ↔ LX * wX < 0 := by
  have hm2 : 0 < m ^ 2 := sq_pos_of_ne_zero hm.ne'
  have hiLe : (↑Le⁻¹ : R) < 0 := unit_inv_neg Le hLe
  have hiwe : 0 < (↑we⁻¹ : R) := unit_inv_pos we hwe
  have hd : (↑we⁻¹ : R) * (↑Le⁻¹ : R) < 0 := mul_neg_of_pos_of_neg hiwe hiLe
  have hc : 0 < m ^ 2 * (-((↑we⁻¹ : R) * (↑Le⁻¹ : R))) := mul_pos hm2 (neg_pos.mpr hd)
  have heq : (m * wX * (↑we⁻¹ : R)) * (m * LX * (↑Le⁻¹ : R)) =
      (-(LX * wX)) * (m ^ 2 * (-((↑we⁻¹ : R) * (↑Le⁻¹ : R)))) := by ring
  rw [heq]
  constructor
  · intro h
    by_contra hge
    push_neg at hge
    have hle : (-(LX * wX)) * (m ^ 2 * (-((↑we⁻¹ : R) * (↑Le⁻¹ : R)))) ≤ 0 :=
      mul_nonpos_of_nonpos_of_nonneg (by linarith) hc.le
    linarith
  · intro h
    exact mul_pos (neg_pos.mpr h) hc

/-- **n−p cell, log chart.** `L_n − L_p = −2β`: the neutron lies above the proton. -/
theorem np_cell_log_pos (m β : R) (Le : Rˣ) (hm : 0 < m) (hβ : 0 < β) (hLe : (Le : R) < 0) :
    0 < m * (-2 * β) * (↑Le⁻¹ : R) := by
  have hiLe : (↑Le⁻¹ : R) < 0 := unit_inv_neg Le hLe
  have hneg : m * (-2 * β) < 0 := by
    have : 0 < m * (2 * β) := mul_pos hm (by linarith)
    linarith [show m * (-2 * β) = -(m * (2 * β)) by ring]
  exact mul_pos_of_neg_of_neg hneg hiLe

/-- **n−p cell, mass chart.** `w_n − w_p = −2`: the neutron lies below the proton. -/
theorem np_cell_mass_neg (m : R) (we : Rˣ) (hm : 0 < m) (hwe : 0 < (we : R)) :
    m * (-2) * (↑we⁻¹ : R) < 0 :=
  mul_neg_of_neg_of_pos (by linarith) (unit_inv_pos we hwe)

/-- **A shrinking bond letter adds mass in the log chart.** If `L_f < 0` (`f < 1`) then, with
the CAL-1 orientation `L_e < 0`, `B = −E₀(f) < 0`. -/
theorem bond_unbinds_log_chart (m Lf : R) (Le : Rˣ)
    (hm : 0 < m) (hLf : Lf < 0) (hLe : (Le : R) < 0) :
    -(m * Lf * (↑Le⁻¹ : R)) < 0 := by
  have : 0 < m * Lf * (↑Le⁻¹ : R) :=
    mul_pos_of_neg_of_neg (mul_neg_of_pos_of_neg hm hLf) (unit_inv_neg Le hLe)
  linarith

/-- **A growing bond letter adds mass in the mass chart.** If `w_f > 0` then, with `w_e > 0`,
`B = −E₁(f) < 0`. -/
theorem bond_unbinds_mass_chart (m wf : R) (we : Rˣ)
    (hm : 0 < m) (hwf : 0 < wf) (hwe : 0 < (we : R)) :
    -(m * wf * (↑we⁻¹ : R)) < 0 := by
  have : 0 < m * wf * (↑we⁻¹ : R) := mul_pos (mul_pos hm hwf) (unit_inv_pos we hwe)
  linarith

/-- **The ruled log law runs against the CAL-1 log chart.** The law
`B = T·log(tr_free/tr_atom) = T·(−L_f)` with `T > 0` and the CAL-1 reading
`B = −m·L_f·L_e⁻¹` have opposite signs on every letter with `L_f < 0`. -/
theorem ruled_law_opposite (T m Lf : R) (Le : Rˣ) (hT : 0 < T) (hm : 0 < m) (hLf : Lf < 0)
    (hLe : (Le : R) < 0) :
    (T * -Lf) * (-(m * Lf * (↑Le⁻¹ : R))) < 0 := by
  have h1 : 0 < T * -Lf := mul_pos hT (by linarith)
  exact mul_neg_of_pos_of_neg h1 (bond_unbinds_log_chart m Lf Le hm hLf hLe)

end Ordered

end QOU.Observations.EnergyScaleBridge
