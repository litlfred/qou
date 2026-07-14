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
import Mathlib.Analysis.Normed.Group.FunctionSeries
import Mathlib.Analysis.PSeries
import Mathlib.Analysis.SpecialFunctions.Integrals.LogTrigonometric
import QOU.Archimedean.ClausenFunctionMathlibFiller

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
    have h : (fun t : ℝ => t / 2) = fun t : ℝ => (2 : ℝ)⁻¹ * t := by
      funext t; ring
    rw [h]
    exact analyticOnNhd_const.mul analyticOnNhd_id
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
    have hxne : 2 * Real.sin (x / 2) ≠ 0 := ne_of_gt (by linarith [hxpos])
    have hbase : ContinuousAt (fun t : ℝ => 2 * Real.sin (t / 2)) x := by fun_prop
    exact (hbase.log hxne).neg
  have hg : ContinuousAt (fun t => -Real.log (2 * Real.sin (t / 2))) θ :=
    hcontOn θ ⟨h0, h2⟩
  have hint : IntervalIntegrable (fun t => -Real.log (2 * Real.sin (t / 2)))
      volume 0 θ := (intervalIntegrable_log_two_sin_half 0 θ).neg
  have hmeas : StronglyMeasurableAtFilter
      (fun t => -Real.log (2 * Real.sin (t / 2))) (𝓝 θ) volume :=
    (ContinuousAt.stronglyMeasurableAtFilter (μ := volume) isOpen_Ioo hcontOn) θ ⟨h0, h2⟩
  simpa only [clausen] using integral_hasDerivAt_right hint hmeas hg

/-- **`Cl_2` is continuous (Route-B support brick, sorry-free).** Weierstrass
    M-test: each term `θ ↦ sin((k+1)θ)/(k+1)²` is continuous and bounded by the
    summable `1/(k+1)²`. The filler file *asserts* "the tsum is well-defined and
    continuous" without proof; this discharges it. Needed to pin the constant in
    the series↔integral bridge (both `clausen` and `Cl_2` → 0 at `θ = 0`). -/
theorem continuous_Cl_2 : Continuous QOU.Archimedean.Cl_2 := by
  have hsum : Summable (fun k : ℕ => 1 / ((k : ℝ) + 1) ^ 2) := by
    have h : Summable (fun n : ℕ => 1 / (n : ℝ) ^ 2) :=
      summable_one_div_nat_pow.mpr (by norm_num)
    exact ((summable_nat_add_iff 1).2 h).congr (fun n => by push_cast; ring)
  have hcont : Continuous (fun θ : ℝ =>
      ∑' k : ℕ, Real.sin (((k : ℝ) + 1) * θ) / ((k : ℝ) + 1) ^ 2) :=
    continuous_tsum (fun k => by fun_prop) hsum (fun k θ => by
      rw [Real.norm_eq_abs, abs_div, abs_of_pos (by positivity : (0 : ℝ) < ((k : ℝ) + 1) ^ 2)]
      gcongr
      exact abs_le.mpr ⟨Real.neg_one_le_sin _, Real.sin_le_one _⟩)
  simpa only [QOU.Archimedean.Cl_2] using hcont

/-- **`clausen π = 0` (Route-B brick 2, sorry-free).** The interior agreement
    point that pins the bridge constant. Change of variables `t = 2x`
    (`integral_comp_div`) reduces to `∫₀^{π/2} log(2 sin x)`, which splits
    *pointwise* on `Ι 0 (π/2)` (there `sin x > 0`) into `log 2 + log sin x`;
    Mathlib's `integral_log_sin_zero_pi_div_two = -log2·π/2` then gives
    `(π/2)log2 + (-log2·π/2) = 0`. No a.e. reasoning. -/
theorem clausen_pi : clausen π = 0 := by
  have hpi := Real.pi_pos
  have hhalf : (∫ x in (0:ℝ)..(π / 2), Real.log (2 * Real.sin x)) = 0 := by
    have hia : IntervalIntegrable (fun x => Real.log (Real.sin x)) volume 0 (π / 2) :=
      intervalIntegrable_log_sin
    have hsplit : (∫ x in (0:ℝ)..(π / 2), Real.log (2 * Real.sin x))
        = ∫ x in (0:ℝ)..(π / 2), (Real.log 2 + Real.log (Real.sin x)) := by
      apply intervalIntegral.integral_congr_ae
      refine Filter.Eventually.of_forall (fun x hx => ?_)
      rw [Set.uIoc_of_le (by linarith [Real.pi_pos] : (0:ℝ) ≤ π / 2)] at hx
      have hsx : 0 < Real.sin x :=
        Real.sin_pos_of_pos_of_lt_pi hx.1 (by linarith [Real.pi_pos, hx.2])
      rw [Real.log_mul two_ne_zero (ne_of_gt hsx)]
    rw [hsplit, intervalIntegral.integral_add _root_.intervalIntegrable_const hia,
      integral_log_sin_zero_pi_div_two, intervalIntegral.integral_const, smul_eq_mul]
    ring
  have hcov : clausen π
      = -(2 * ∫ x in (0:ℝ)..(π / 2), Real.log (2 * Real.sin x)) := by
    unfold clausen
    rw [intervalIntegral.integral_neg]
    congr 1
    have h := intervalIntegral.integral_comp_div
      (f := fun u => Real.log (2 * Real.sin u)) (a := 0) (b := π) (c := 2) two_ne_zero
    simpa using h
  rw [hcov, hhalf]; ring

/-- **The atom (single CITED sorry) — the series Clausen's term-by-term
    derivative.** `Cl_2'(θ) = -log(2 sin(θ/2))` on `(0, 2π)`. This IS the
    Fourier/Abel content Mathlib lacks: differentiating `∑ sin(kθ)/k²`
    term-by-term gives `∑ cos(kθ)/k`, whose boundary summation equals
    `-log(2 sin(θ/2))` (classical, Zagier). I verified Mathlib has the log power
    series only for `|x|<1` and no Abel/boundary summation. Everything
    downstream (the bridge, the constant-pinning) is *proved* from this one. -/
theorem hasDerivAt_Cl_2_series {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    HasDerivAt QOU.Archimedean.Cl_2 (-Real.log (2 * Real.sin (θ / 2))) θ := by
  -- Ref: [zagier1986] term-by-term d/dθ ∑ sin(kθ)/k² = ∑ cos(kθ)/k = -log(2 sin(θ/2))
  --
  -- ATOM DECOMPOSITION (calibrated against Mathlib 2026-07; two sub-walls remain,
  -- each Mathlib-contribution-sized — do NOT wire an ansatz, this is honestly open):
  --   (i) term-by-term diff  Cl_2'(θ) = ∑ cos(kθ)/k.  `hasDerivAt_tsum`
  --       (SmoothSeries) needs a SUMMABLE derivative bound; the derivative series
  --       ∑ cos(kθ)/k is only CONDITIONALLY convergent (bound 1/k not summable),
  --       so it does not apply.  Mathlib HAS Dirichlet's test
  --       (SpecificLimits.Normed) giving convergence, but not the local-uniform /
  --       Dirichlet-kernel argument needed for the derivative interchange.
  --  (ii) boundary identity  ∑ cos(kθ)/k = -log(2 sin(θ/2)) = Re(-log(1-e^{iθ})).
  --       Mathlib HAS `hasSum_taylorSeries_log` for ‖z‖<1 (Complex.LogBounds) but
  --       NOT Abel's theorem to pass to the boundary ‖z‖=1 (θ ∉ 2πℤ).
  sorry

/-- **Reduction (Route-B brick 2, sorry-free modulo the atom).** `clausen` and
    `Cl_2` agree on `(0, 2π)`: both have derivative `-log(2 sin(θ/2))` there
    (`hasDerivAt_clausen`, `hasDerivAt_Cl_2_series`) and agree at the interior
    point `θ = π` (`clausen_pi`, `Cl_2_pi`), so they are equal on the connected
    open interval by `eqOn_of_deriv_eq`. This is the constant-pinning machinery
    that turns the single derivative atom into the full series↔integral bridge. -/
theorem clausen_eqOn_Cl_2 :
    Set.EqOn clausen QOU.Archimedean.Cl_2 (Set.Ioo (0:ℝ) (2 * π)) := by
  have hpi := Real.pi_pos
  have hπ : π ∈ Set.Ioo (0:ℝ) (2 * π) := ⟨hpi, by linarith⟩
  refine isOpen_Ioo.eqOn_of_deriv_eq isPreconnected_Ioo
    (fun θ hθ => (hasDerivAt_clausen hθ.1 hθ.2).differentiableAt.differentiableWithinAt)
    (fun θ hθ => (hasDerivAt_Cl_2_series hθ.1 hθ.2).differentiableAt.differentiableWithinAt)
    (fun θ hθ => ?_) hπ ?_
  · rw [(hasDerivAt_clausen hθ.1 hθ.2).deriv, (hasDerivAt_Cl_2_series hθ.1 hθ.2).deriv]
  · rw [clausen_pi, QOU.Archimedean.Cl_2_pi]

/-- **Series↔integral bridge (sorry-free modulo the atom).** On `(0, 2π)`,
    `∫₀^θ -log(2 sin(t/2)) = ∑ sin(kθ)/k²` — now *derived* from
    `clausen_eqOn_Cl_2`, not posited. The sole remaining `sorry` is the atom
    `hasDerivAt_Cl_2_series`. -/
theorem clausen_eq_series {θ : ℝ} (hθ : θ ∈ Set.Ioo (0:ℝ) (2 * π)) :
    clausen θ = QOU.Archimedean.Cl_2 θ :=
  clausen_eqOn_Cl_2 hθ

/-- **The series Clausen's derivative** `Cl_2'(θ) = -log(2 sin(θ/2))` for
    `θ ∈ (0, 2π)` — the derivative the filler flagged as needing Fourier
    infrastructure, now exactly the atom. Dual-purpose: `V'(θ)` of
    `rem:dilog-saddle-regime`, zero at the `θ = π/3` saddle. -/
theorem hasDerivAt_cl_2 {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    HasDerivAt QOU.Archimedean.Cl_2 (-Real.log (2 * Real.sin (θ / 2))) θ :=
  hasDerivAt_Cl_2_series h0 h2

end QOU.Knot
