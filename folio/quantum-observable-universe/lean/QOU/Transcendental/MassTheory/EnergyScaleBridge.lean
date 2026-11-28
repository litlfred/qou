/-
# The Euler derivative as the bridge between the two CAL-1 charts (analytic half)

Algebraic half: `QOU.Observations.EnergyScaleBridge`. Audit:
`docs/audits/2026-11-27-energy-scale-bridge.md`.

This file supplies the calculus that the algebraic half takes as data.

* `euler_reading_of_log`: for `f > 0` differentiable at `q`, `q · d/dq log f = q f'/f`.
  The mass-chart reading is the Euler derivative of the log-chart reading.
* `ratio_flow_eq`: `q · d/dq (L_X/L_e) = ratioFlow (L_X) (Units.mk0 L_e _) (q L_X') (q L_e')`.
* `chart_gap_real`: so `E₁ − E₀ = m · (L_e/w_e) · q·d/dq (L_X/L_e)`.
* `electron_log_neg`: `log τ_e < 0` on `1 ≤ q ≤ 6/5`, the hypothesis `L_e < 0` of the
  sign results.
* `beta_pos`: `log q > 0` for `q > 1`.

No measured value enters.
-/
import QOU.Observations.EnergyScaleBridge
import QOU.Observations.ElectronWeightAdditivity
import Mathlib.Analysis.SpecialFunctions.Log.Deriv

namespace QOU.Transcendental.MassTheory.EnergyScaleBridge

open QOU.Observations.EnergyScaleBridge QOU.Observations.ElectronWeightAdditivity

/-- **The mass-chart reading is the Euler derivative of the log-chart reading.** -/
theorem euler_reading_of_log (f : ℝ → ℝ) (f' q : ℝ) (hf : HasDerivAt f f' q) (hpos : 0 < f q) :
    HasDerivAt (fun x => Real.log (f x)) (f' / f q) q ∧ q * (f' / f q) = q * f' / f q := by
  refine ⟨hf.log hpos.ne', by ring⟩

/-- The Euler derivative of the ratio of two log readings is `ratioFlow`. -/
theorem ratio_flow_eq (LX Le : ℝ → ℝ) (lX le q : ℝ) (hX : HasDerivAt LX lX q)
    (he : HasDerivAt Le le q) (hne : Le q ≠ 0) :
    HasDerivAt (fun x => LX x / Le x) ((lX * Le q - LX q * le) / Le q ^ 2) q ∧
      q * ((lX * Le q - LX q * le) / Le q ^ 2) =
        ratioFlow (LX q) (Units.mk0 (Le q) hne) (q * lX) (q * le) := by
  refine ⟨hX.div he hne, ?_⟩
  unfold ratioFlow
  simp [div_eq_mul_inv]
  ring

/-- **Chart gap, real form.** With `w_X = q L_X'`, `w_e = q L_e'`:
`m·w_X/w_e − m·L_X/L_e = m·(L_e/w_e)·(q · d/dq (L_X/L_e))`. -/
theorem chart_gap_real (m : ℝ) (LX Le : ℝ → ℝ) (lX le q : ℝ) (hX : HasDerivAt LX lX q)
    (he : HasDerivAt Le le q) (hne : Le q ≠ 0) (hwe : q * le ≠ 0) :
    m * (q * lX) / (q * le) - m * LX q / Le q =
      m * (Le q / (q * le)) * (q * ((lX * Le q - LX q * le) / Le q ^ 2)) := by
  rw [(ratio_flow_eq LX Le lX le q hX he hne).2]
  have h := chart_gap m (LX q) (Units.mk0 (Le q) hne) (q * lX) (Units.mk0 (q * le) hwe)
  simpa [div_eq_mul_inv] using h

/-- `L_e = log τ_e < 0` on `1 ≤ q ≤ 6/5`. -/
theorem electron_log_neg (q : ℝ) (h1 : 1 ≤ q) (h2 : q ≤ 6 / 5) : Real.log (tauE q) < 0 :=
  Real.log_neg (tauE_pos q (by linarith)) (tauE_lt_one q h1 h2)

/-- `β = log q > 0` for `q > 1`. -/
theorem beta_pos (q : ℝ) (h : 1 < q) : 0 < Real.log q := Real.log_pos h

/-- **n−p, both charts, at the electron.** On `1 < q ≤ 6/5`, for any `w_e > 0`, the log chart
puts the neutron (`τ_n = q⁻²τ_p`) above the proton and the mass chart puts it below. -/
theorem np_cell_charts_disagree (m q we : ℝ) (hm : 0 < m) (h1 : 1 < q) (h2 : q ≤ 6 / 5)
    (hwe : 0 < we) :
    0 < m * (-2 * Real.log q) / Real.log (tauE q) ∧ m * (-2) / we < 0 := by
  have hLe : Real.log (tauE q) < 0 := electron_log_neg q h1.le h2
  have hlog := np_cell_log_pos m (Real.log q) (Units.mk0 (Real.log (tauE q)) hLe.ne)
    hm (beta_pos q h1) hLe
  have hmass := np_cell_mass_neg m (Units.mk0 we hwe.ne') hm hwe
  simpa [div_eq_mul_inv] using And.intro hlog hmass

end QOU.Transcendental.MassTheory.EnergyScaleBridge
