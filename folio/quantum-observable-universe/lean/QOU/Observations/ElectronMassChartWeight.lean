/-
# The electron's weight on the mass-formula scale: closed form of its energy reading

Thread "Derive the electron's categorical weight", second part (2026-11-27). Analytic half:
`QOU.Transcendental.MassTheory.ElectronMassChartWeight`. Audit:
`docs/audits/2026-11-27-electron-categorical-weight.md` §7.

The mass formula `m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²` gives the electron the weight `1` by hand: its
own rule gives `0` (`ElectronUnitSplit.product_weight_ne`). Its rule, made canonical in #9692,
is the energy reading `w = q ∂_q log Z` (the muon's q-volume `G` is this reading of the quantum
dilogarithm). This file gives the same reading of the electron trace `τ_e` in closed form,
over a generic field:

* `dTauE`: the derivative of `τ_e = q³(q⁴+1)/(q²+1)²`, written out.
* `q_mul_dTauE`: `q·τ_e' = τ_e·w_e`, with
  `w_e = 3 + 4q²(q²−1)/((q⁴+1)(q²+1))` (`wE`).
* `wE_one`: `w_e(1) = 3`, the writhe of `σ₀σ₁σ₀`.
* `wE_bar`: `w_e(q⁻¹) = 6 − w_e(q)`. The non-writhe part is odd under bar.

No measured value enters.
-/
import QOU.Observations.ElectronWeightAdditivity

namespace QOU.Observations.ElectronMassChartWeight

open QOU.Observations.ElectronWeightAdditivity

variable {R : Type*} [Field R]

/-- The electron's energy-reading weight `w_e = q ∂_q log τ_e`, in closed form. -/
def wE (q : R) : R := 3 + 4 * q ^ 2 * (q ^ 2 - 1) / ((q ^ 4 + 1) * (q ^ 2 + 1))

/-- The derivative of `τ_e`, written out (quotient rule). -/
def dTauE (q : R) : R :=
  (3 * q ^ 2 * (q ^ 4 + 1) + q ^ 3 * (4 * q ^ 3)) / (q ^ 2 + 1) ^ 2 -
    q ^ 3 * (q ^ 4 + 1) * (2 * (q ^ 2 + 1) * (2 * q)) / ((q ^ 2 + 1) ^ 2) ^ 2

/-- **`q·τ_e' = τ_e·w_e`.** -/
theorem q_mul_dTauE (q : R) (h4 : q ^ 4 + 1 ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    q * dTauE q = tauE q * wE q := by
  unfold dTauE tauE wE
  field_simp
  ring

/-- **`w_e(1) = 3`**: the writhe. -/
theorem wE_one [CharZero R] : wE (1 : R) = 3 := by
  unfold wE; norm_num

/-- **Bar symmetry:** `w_e(q⁻¹) = 6 − w_e(q)`. -/
theorem wE_bar (q : R) (hq : q ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    wE q⁻¹ = 6 - wE q := by
  have hp : (q ^ 4 + 1) * (q ^ 2 + 1) ≠ 0 := mul_ne_zero h4 h2
  have key : 4 * q⁻¹ ^ 2 * (q⁻¹ ^ 2 - 1) / ((q⁻¹ ^ 4 + 1) * (q⁻¹ ^ 2 + 1)) =
      -(4 * q ^ 2 * (q ^ 2 - 1) / ((q ^ 4 + 1) * (q ^ 2 + 1))) := by
    have e1 : 4 * q⁻¹ ^ 2 * (q⁻¹ ^ 2 - 1) = 4 * (1 - q ^ 2) / q ^ 4 := by
      field_simp
    have e2 : (q⁻¹ ^ 4 + 1) * (q⁻¹ ^ 2 + 1) = (q ^ 4 + 1) * (q ^ 2 + 1) / q ^ 6 := by
      field_simp; ring
    rw [e1, e2, div_div_eq_mul_div]
    field_simp
    ring
  unfold wE
  rw [key]
  ring

end QOU.Observations.ElectronMassChartWeight
