/-
  The Clausen function `Cl₂` (Lobachevsky primitive) and its derivative — the
  Mathlib-gap shared infrastructure behind the figure-eight saddle VALUE and the
  QOU dilog-saddle potential.

  Mathlib has the log-sin interval integral (`intervalIntegrable_log_sin`, via
  `MeromorphicOn.intervalIntegrable_log`) but NOT the Clausen / Lobachevsky
  function. This file supplies:

    * `clausen θ := ∫ t in 0..θ, -log(2 sin(t/2))` — the Clausen `Cl₂` integral;
    * `intervalIntegrable_log_two_sin_half` — its integrand is interval-integrable
      (the log-singularities of `sin` handled by the meromorphic-log lemma);
    * `hasDerivAt_clausen` — **brick 3**: `Cl₂'(θ) = -log(2 sin(θ/2))` for
      `θ ∈ (0, 2π)` via the FTC (`integral_hasDerivAt_right`).

  DUAL-PURPOSE. `Cl₂'(θ) = -log(2 sin(θ/2))` is *verbatim* the derivative
  `V'(θ)` of the QOU dilog-saddle potential `V(θ) = Im Li₂(e^{iθ}) = Cl₂(θ)`
  (content block `rem:dilog-saddle-regime`). Combined with
  `saddle_critical_point` (`FigureEightVolumeSaddle.lean`: `V'(θ)=0 ⟺ θ=π/3`),
  the extremum of `Cl₂` on `(0,π)` is at `θ=π/3` — the figure-eight Kashaev
  saddle AND the muon-anchor volume `Vol(4₁) = 2 Cl₂(π/3)`. The VALUE `Cl₂(π/3)`
  has no elementary closed form (it is the ideal-tetrahedron volume by
  definition); that is a fact, not a gap — `Vol(4₁)` is transcendental.

  HONEST SCOPE. This discharges the DERIVATIVE claim of the dilog-saddle block,
  NOT the figure-eight volume-conjecture `sorry` (which additionally needs the
  saddle-point existence + growth-rate = value — the Andersen–Hansen / Ohtsuki
  asymptotic, of which this is one ingredient). Bean qou-reab (brick 3); the
  Clausen VALUE is tracked in bean qou-44ma.

  Archimedean (ℝ).

  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import Mathlib.Analysis.SpecialFunctions.Integrability.LogMeromorphic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus

namespace QOU.Knot

open Real intervalIntegral MeasureTheory Filter Topology

/-- The Clausen function `Cl₂(θ) = ∫₀^θ -log(2 sin(t/2)) dt` (Lobachevsky
    primitive of `-log(2 sin(·/2))`). Not available in Mathlib. -/
noncomputable def clausen (θ : ℝ) : ℝ :=
  ∫ t in (0:ℝ)..θ, -Real.log (2 * Real.sin (t / 2))

/-- `t ↦ 2 sin(t/2)` is analytic (entire) on any real segment — the analytic
    hull the meromorphic-log integrability lemma needs. -/
theorem analyticOnNhd_two_sin_half (a b : ℝ) :
    AnalyticOnNhd ℝ (fun t => 2 * Real.sin (t / 2)) (Set.uIcc a b) := by
  have haff : AnalyticOnNhd ℝ (fun t : ℝ => t / 2) (Set.uIcc a b) := by
    fun_prop
  have hsin : AnalyticOnNhd ℝ (fun t : ℝ => Real.sin (t / 2)) (Set.uIcc a b) :=
    Real.analyticOnNhd_sin.comp haff (Set.mapsTo_univ _ _)
  exact analyticOnNhd_const.mul hsin

/-- **Integrability of the Clausen integrand.** `t ↦ log(2 sin(t/2))` is
    interval-integrable on every `a..b`; the log-singularities of `sin` at
    multiples of `2π` are integrable (`MeromorphicOn.intervalIntegrable_log`). -/
theorem intervalIntegrable_log_two_sin_half (a b : ℝ) :
    IntervalIntegrable (fun t => Real.log (2 * Real.sin (t / 2))) volume a b :=
  (analyticOnNhd_two_sin_half a b).meromorphicOn.intervalIntegrable_log

/-- **Brick 3 — the Clausen derivative (dual-purpose).** For `θ ∈ (0, 2π)`,
    `Cl₂'(θ) = -log(2 sin(θ/2))`. This is the fundamental theorem of calculus
    applied to the interval-integrable, at-`θ`-continuous integrand. It is
    *simultaneously* the derivative `V'(θ)` of the QOU dilog-saddle potential
    `V(θ) = Im Li₂(e^{iθ}) = Cl₂(θ)` — the load-bearing derivative claim of
    content block `rem:dilog-saddle-regime`, now Lean-proved. Its zero is the
    saddle `θ = π/3` (`saddle_critical_point`), giving `Vol(4₁) = 2 Cl₂(π/3)`. -/
theorem hasDerivAt_clausen {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    HasDerivAt clausen (-Real.log (2 * Real.sin (θ / 2))) θ := by
  -- continuity of the integrand at every interior point (where `2 sin(x/2) ≠ 0`)
  have hcontOn : ∀ x ∈ Set.Ioo (0 : ℝ) (2 * π),
      ContinuousAt (fun t => -Real.log (2 * Real.sin (t / 2))) x := by
    intro x hx
    have hxpos : 0 < Real.sin (x / 2) :=
      Real.sin_pos_of_pos_of_lt_pi (by linarith [hx.1]) (by linarith [hx.2])
    have hxne : 2 * Real.sin (x / 2) ≠ 0 := by positivity
    have hbase : ContinuousAt (fun t : ℝ => 2 * Real.sin (t / 2)) x := by fun_prop
    exact ((Real.continuousAt_log hxne).comp hbase).neg
  have hg : ContinuousAt (fun t => -Real.log (2 * Real.sin (t / 2))) θ :=
    hcontOn θ ⟨h0, h2⟩
  have hint : IntervalIntegrable (fun t => -Real.log (2 * Real.sin (t / 2)))
      volume 0 θ := (intervalIntegrable_log_two_sin_half 0 θ).neg
  have hmeas : StronglyMeasurableAtFilter
      (fun t => -Real.log (2 * Real.sin (t / 2))) (𝓝 θ) volume :=
    (ContinuousAt.stronglyMeasurableAtFilter (μ := volume) isOpen_Ioo hcontOn) θ ⟨h0, h2⟩
  simpa only [clausen] using integral_hasDerivAt_right hint hmeas hg

end QOU.Knot
