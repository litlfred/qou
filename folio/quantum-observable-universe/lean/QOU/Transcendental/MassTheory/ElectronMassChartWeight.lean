/-
# The mass formula's own rule fixes the electron's weight: `w_e = q ∂_q log τ_e → 3`

Thread "Derive the electron's categorical weight", second part (2026-11-27). Algebraic half:
`QOU.Observations.ElectronMassChartWeight`. Builds on #9692
(`QOU.Transcendental.MuonCarrierHeckeObstruction`) and #9718
(`QOU.Transcendental.MassTheory.ElectronCategoricalEnergy`). Audit:
`docs/audits/2026-11-27-electron-categorical-weight.md` §7.

**Which additive reading the mass formula uses.** #9718 shows that among functions of the trace
*value*, additivity forces `c·log`. The mass formula is not a value function: the muon's weight
`G = q ∂_q log P` (#9692) is a derivative. Derivatives of `log` are additive too
(`energyReading_mul`, Leibniz). So the additive local readings are `(q ∂_q)^k log Z`, and `k`
is fixed by the pole order:

* `hbar_pole_raise`: `q ∂_q ℏ_q⁻ⁿ = −n q⁻¹ ℏ_q^{−(n+1)}`. Each `q ∂_q` raises the pole at
  `q = 1` by exactly one.
* The quantum dilogarithm has `log P ~ −Li₂/ℏ_q` (pole order 1, #9692 §10.2). The mass
  formula's carrier is `Vol/ℏ_q²` (order 2). So `k = 1`: the weight is the energy reading.

**The electron, by the same rule.** `electron_energy_reading`: for `q > 0`,
`q·τ_e'(q)/τ_e(q) = w_e(q) = 3 + 4q²(q²−1)/((q⁴+1)(q²+1))`, and `w_e(1) = 3`. This replaces the
hand-placed weight `1` of the unit `m_e/ℏ_q²`. With CAL-1 the derived mass-chart unit is
`m_e/w_e(q)`.

**n–p cell in this chart.** `np_cell_energy_reading`: for `ε_n = q⁻²·ε_p` (the K-weights
`q^{∓1}` of `SpectatorEnergyMap`), the readings differ by exactly `−2`, for every differentiable
`ε_p`. So the cell is `2/w_e(q)` electron masses, `2/3` at `q = 1`.

Consequence, stated in the audit and not used here: at the current q₀ the derived chart gives
`m_μ/m_e = W_μ/w_e = 64.69`, which is #9692's "Vol/3". CAL-2 defines q₀ through the carrier
with the hand-placed weight, so adopting `w_e` would re-solve q₀. That is an owner decision.
No measured value enters.
-/
import QOU.Observations.ElectronMassChartWeight
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Tactic

namespace QOU.Transcendental.MassTheory.ElectronMassChartWeight

open QOU.Observations.ElectronWeightAdditivity QOU.Observations.ElectronMassChartWeight

/-- **Leibniz: the energy reading is additive on products.** -/
theorem energyReading_mul (q f g f' g' : ℝ) (hf : f ≠ 0) (hg : g ≠ 0) :
    q * (f' * g + f * g') / (f * g) = q * f' / f + q * g' / g := by
  field_simp

/-- **Each `q ∂_q` raises the pole of `ℏ_q⁻ⁿ` by one:**
`q · d/dq (1 − q⁻¹)⁻ⁿ = −n q⁻¹ (1 − q⁻¹)^{−(n+1)}`. -/
theorem hbar_pole_raise (n : ℕ) (q : ℝ) (hq : q ≠ 0) (hq1 : q ≠ 1) :
    HasDerivAt (fun x : ℝ => ((1 - x⁻¹) ^ n)⁻¹)
      (-(n * (1 - q⁻¹) ^ (n - 1) * (q ^ 2)⁻¹) / ((1 - q⁻¹) ^ n) ^ 2) q ∧
    q * (-(n * (1 - q⁻¹) ^ (n - 1) * (q ^ 2)⁻¹) / ((1 - q⁻¹) ^ n) ^ 2) =
      -(n : ℝ) * q⁻¹ * ((1 - q⁻¹) ^ (n + 1))⁻¹ := by
  have hh : 1 - q⁻¹ ≠ 0 := by
    intro h; apply hq1
    have : q⁻¹ = 1 := by linarith
    simpa using congrArg (·⁻¹) this
  have hinv : HasDerivAt (fun x : ℝ => 1 - x⁻¹) ((q ^ 2)⁻¹) q := by
    have := (hasDerivAt_inv hq).const_sub 1
    simpa using this
  have hpow := hinv.pow n
  refine ⟨?_, ?_⟩
  · have := hpow.inv (pow_ne_zero n hh)
    convert this using 1
  · rcases Nat.eq_zero_or_pos n with rfl | hn
    · simp
    · obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
      simp only [Nat.add_sub_cancel]
      generalize 1 - q⁻¹ = h at hh ⊢
      field_simp
      ring

/-- `τ_e` has derivative `dTauE` everywhere on `ℝ`. -/
theorem hasDerivAt_tauE (q : ℝ) : HasDerivAt tauE (dTauE q) q := by
  have hnum : HasDerivAt (fun x : ℝ => x ^ 3 * (x ^ 4 + 1))
      (3 * q ^ 2 * (q ^ 4 + 1) + q ^ 3 * (4 * q ^ 3)) q := by
    have h3 : HasDerivAt (fun x : ℝ => x ^ 3) (3 * q ^ 2) q := by
      simpa using hasDerivAt_pow 3 q
    have h4 : HasDerivAt (fun x : ℝ => x ^ 4 + 1) (4 * q ^ 3) q := by
      simpa using (hasDerivAt_pow 4 q).add_const 1
    exact h3.mul h4
  have hden : HasDerivAt (fun x : ℝ => (x ^ 2 + 1) ^ 2) (2 * (q ^ 2 + 1) * (2 * q)) q := by
    have h2 : HasDerivAt (fun x : ℝ => x ^ 2 + 1) (2 * q) q := by
      simpa using (hasDerivAt_pow 2 q).add_const 1
    have := h2.pow 2
    simpa [mul_comm, mul_assoc, mul_left_comm] using this
  have hd : (q ^ 2 + 1) ^ 2 ≠ 0 := by positivity
  have := hnum.div hden hd
  unfold tauE dTauE
  convert this using 1
  field_simp

/-- **The electron's energy reading is `w_e`:** `q·τ_e'/τ_e = w_e` for `q > 0`. -/
theorem electron_energy_reading (q : ℝ) (hq : 0 < q) :
    q * deriv tauE q / tauE q = wE q := by
  rw [(hasDerivAt_tauE q).deriv, q_mul_dTauE q (by positivity) (by positivity)]
  have := (tauE_pos q hq).ne'
  field_simp

/-- **At `q = 1` the electron's mass-chart weight is the writhe, `3`.** -/
theorem electron_energy_reading_one : (1 : ℝ) * deriv tauE 1 / tauE 1 = 3 := by
  rw [electron_energy_reading 1 one_pos, wE_one]

/-- **n–p cell in the mass chart.** If `ε_n = q⁻²·ε_p` near `q`, the energy readings differ by
exactly `−2`, whatever `ε_p` is. -/
theorem np_cell_energy_reading (q e e' : ℝ) (hq : q ≠ 0) (he : e ≠ 0) :
    q * (-(2 * q⁻¹ ^ 3) * e + q⁻¹ ^ 2 * e') / (q⁻¹ ^ 2 * e) - q * e' / e = -2 := by
  field_simp
  ring

/-- The `q⁻²` factor has derivative `−2q⁻³`, so the `np_cell_energy_reading` numerator is the
true derivative of `q⁻²·ε_p` (product rule). -/
theorem hasDerivAt_inv_sq_mul (q e e' : ℝ) (hq : q ≠ 0) (εp : ℝ → ℝ)
    (hε : HasDerivAt εp e' q) (hv : εp q = e) :
    HasDerivAt (fun x => x⁻¹ ^ 2 * εp x) (-(2 * q⁻¹ ^ 3) * e + q⁻¹ ^ 2 * e') q := by
  have hi : HasDerivAt (fun x : ℝ => x⁻¹ ^ 2) (2 * q⁻¹ * (-(q ^ 2)⁻¹)) q :=
    ((hasDerivAt_inv hq).pow 2).congr_deriv (by norm_num)
  have := hi.mul hε
  rw [hv] at this
  convert this using 1
  field_simp

end QOU.Transcendental.MassTheory.ElectronMassChartWeight
