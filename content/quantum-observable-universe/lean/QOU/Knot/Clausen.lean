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
import Mathlib.Analysis.Calculus.SmoothSeries
import Mathlib.Analysis.SpecialFunctions.Integrals.LogTrigonometric
import Mathlib.Analysis.Complex.AbelLimit
import Mathlib.Analysis.SpecialFunctions.Complex.LogBounds
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

/-- **Abel-regularisation of `Cl_2` (assembly brick, sorry-free).** As `x → 1⁻`,
    `∑ₙ (sin(nθ)/n²) xⁿ → Cl_2 θ` — Abel's limit theorem
    (`Real.tendsto_tsum_powerSeries_nhdsWithin_lt`), valid because the
    `sin(nθ)/n²` series converges absolutely at `x = 1`. First brick of the Abel
    route discharging the atom `hasDerivAt_Cl_2_series`. -/
theorem tendsto_Cl_2_reg (θ : ℝ) :
    Filter.Tendsto (fun x : ℝ => ∑' n : ℕ, Real.sin (n * θ) / (n : ℝ) ^ 2 * x ^ n)
      (nhdsWithin 1 (Set.Iio 1)) (nhds (QOU.Archimedean.Cl_2 θ)) := by
  have hsum : Summable (fun n : ℕ => Real.sin (n * θ) / (n : ℝ) ^ 2) := by
    have hg : Summable (fun n : ℕ => 1 / (n : ℝ) ^ 2) :=
      summable_one_div_nat_pow.mpr (by norm_num)
    refine hg.of_norm_bounded (fun n => ?_)
    rw [Real.norm_eq_abs, abs_div, abs_of_nonneg (by positivity : (0:ℝ) ≤ (n : ℝ) ^ 2)]
    rcases Nat.eq_zero_or_pos n with hn | hn
    · simp [hn]
    · gcongr
      exact abs_le.mpr ⟨Real.neg_one_le_sin _, Real.sin_le_one _⟩
  have hCl : ∑' n : ℕ, Real.sin (n * θ) / (n : ℝ) ^ 2 = QOU.Archimedean.Cl_2 θ := by
    rw [tsum_eq_zero_add hsum, QOU.Archimedean.Cl_2]
    simp
  rw [← hCl]
  exact Real.tendsto_tsum_powerSeries_nhdsWithin_lt hsum.hasSum.tendsto_sum_nat

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

/-- **Assembly brick 2a (sorry-free)** — the complex log power series at the
    boundary interior: `∑ₙ wⁿ/n = -log(1-w)` for `‖w‖ < 1`. Derived from Mathlib's
    `Complex.hasSum_taylorSeries_log` (`∑ (-1)^{n+1} zⁿ/n = log(1+z)`) at `z = -w`,
    with the sign algebra `(-1)^{n+1}(-w)ⁿ = -wⁿ`. (bean qou-6r0y) -/
theorem hasSum_pow_div_neg_log {w : ℂ} (hw : ‖w‖ < 1) :
    HasSum (fun n : ℕ => w ^ n / n) (-Complex.log (1 - w)) := by
  have h := Complex.hasSum_taylorSeries_log (z := -w) (by rwa [norm_neg])
  rw [show (1 : ℂ) + -w = 1 - w by ring] at h
  have hfun : (fun n : ℕ => w ^ n / (n : ℂ))
      = fun n : ℕ => -((-1 : ℂ) ^ (n + 1) * (-w) ^ n / n) := by
    funext n
    have e3 : ((-1 : ℂ) ^ n) * ((-1) ^ n) = 1 := by
      rw [← pow_add, ← two_mul, pow_mul]; norm_num
    rw [neg_pow w n, pow_succ,
      show ((-1 : ℂ) ^ n * (-1)) * ((-1) ^ n * w ^ n)
        = ((-1) ^ n * (-1) ^ n) * (-(w ^ n)) by ring, e3]
    ring
  rw [hfun]
  exact h.neg

/-- **Assembly brick 2b (sorry-free)** — the real cos-series closed form. For
    `|r| < 1`, `∑ₙ rⁿ cos(nθ)/n = -log‖1 - r e^{iθ}‖`. Real part of brick 2a
    (`hasSum_pow_div_neg_log`) at `w = r e^{iθ}`, using Euler
    (`exp_ofReal_mul_I_re`) and `Complex.log_re`. (bean qou-smve) -/
theorem tsum_rpow_cos_div (θ : ℝ) {r : ℝ} (hr : |r| < 1) :
    ∑' n : ℕ, r ^ n * Real.cos ((n : ℝ) * θ) / n
      = -Real.log ‖1 - (r : ℂ) * Complex.exp ((θ : ℂ) * Complex.I)‖ := by
  have hnorm : ‖(r : ℂ) * Complex.exp ((θ : ℂ) * Complex.I)‖ < 1 := by
    rw [norm_mul, Complex.norm_exp_ofReal_mul_I, mul_one, Complex.norm_real, Real.norm_eq_abs]
    exact hr
  have hsummand : ∀ n : ℕ,
      (((r : ℂ) * Complex.exp ((θ : ℂ) * Complex.I)) ^ n / (n : ℂ)).re
        = r ^ n * Real.cos ((n : ℝ) * θ) / n := by
    intro n
    have heq : ((r : ℂ) * Complex.exp ((θ : ℂ) * Complex.I)) ^ n / (n : ℂ)
        = ((r ^ n / n : ℝ) : ℂ) * Complex.exp (((n : ℝ) * θ : ℝ) * Complex.I) := by
      rw [mul_pow, ← Complex.exp_nat_mul]
      push_cast
      ring
    rw [heq, Complex.re_ofReal_mul, Complex.exp_ofReal_mul_I_re]; ring
  have hs := Complex.hasSum_re (hasSum_pow_div_neg_log hnorm)
  simp only [hsummand] at hs
  rw [hs.tsum_eq, Complex.neg_re, Complex.log_re]

/-- **Assembly brick 3 (sorry-free)** — the boundary norm identity. For every θ,
    `‖1 - e^{iθ}‖ = 2 |sin(θ/2)|`. Hence the `r→1⁻` limit of brick 2b's closed
    form `-log‖1 - r e^{iθ}‖` is `-log(2 sin(θ/2))` on `(0,2π)` (where
    `sin(θ/2) > 0`) — the boundary log value the atom needs. (bean qou-cdxw) -/
theorem norm_one_sub_exp_ofReal_mul_I (θ : ℝ) :
    ‖1 - Complex.exp ((θ : ℂ) * Complex.I)‖ = 2 * |Real.sin (θ / 2)| := by
  have hc : Real.cos θ = 2 * Real.cos (θ / 2) ^ 2 - 1 := by
    have h := Real.cos_two_mul (θ / 2)
    rw [show 2 * (θ / 2) = θ by ring] at h; linarith
  have hnn : (0 : ℝ) ≤ 2 * |Real.sin (θ / 2)| := by positivity
  have hnormsq : ‖1 - Complex.exp ((θ : ℂ) * Complex.I)‖ ^ 2
      = (2 * |Real.sin (θ / 2)|) ^ 2 := by
    rw [Complex.sq_norm, Complex.normSq_apply, Complex.sub_re, Complex.sub_im,
      Complex.one_re, Complex.one_im, Complex.exp_ofReal_mul_I_re, Complex.exp_ofReal_mul_I_im,
      mul_pow, sq_abs]
    nlinarith [Real.sin_sq_add_cos_sq θ, Real.sin_sq_add_cos_sq (θ / 2), hc]
  rw [← Real.sqrt_sq (norm_nonneg _), hnormsq, Real.sqrt_sq hnn]

/-- **Assembly brick 4 (sorry-free)** — term-by-term derivative of the Abel-
    regularised `g_r`. For `|r| < 1`,
    `d/dθ ∑ₙ sin(nθ)/n² · rⁿ = ∑ₙ rⁿ cos(nθ)/n`. Absolute convergence at `r<1`
    (derivative bound `|r|ⁿ`, summable geometric) makes `hasDerivAt_tsum` apply —
    the conditional-convergence obstruction bites only at `r=1`. (bean qou-7lj2) -/
theorem hasDerivAt_g_r {r : ℝ} (hr : |r| < 1) (θ : ℝ) :
    HasDerivAt (fun t : ℝ => ∑' n : ℕ, Real.sin ((n : ℝ) * t) / (n : ℝ) ^ 2 * r ^ n)
      (∑' n : ℕ, r ^ n * Real.cos ((n : ℝ) * θ) / n) θ := by
  have hu : Summable (fun n : ℕ => |r| ^ n) :=
    summable_geometric_of_lt_one (abs_nonneg r) hr
  have hg : ∀ (n : ℕ) (t : ℝ),
      HasDerivAt (fun t : ℝ => Real.sin ((n : ℝ) * t) / (n : ℝ) ^ 2 * r ^ n)
        (r ^ n * Real.cos ((n : ℝ) * t) / n) t := by
    intro n t
    have hinner : HasDerivAt (fun t : ℝ => (n : ℝ) * t) ((n : ℝ) * 1) t :=
      (hasDerivAt_id t).const_mul (n : ℝ)
    have hsin : HasDerivAt (fun t : ℝ => Real.sin ((n : ℝ) * t))
        ((n : ℝ) * Real.cos ((n : ℝ) * t)) t := by
      have h := (Real.hasDerivAt_sin ((n : ℝ) * t)).comp t hinner
      simp only [Function.comp_def] at h
      convert h using 1
      ring
    have hmain := (hsin.div_const ((n : ℝ) ^ 2)).mul_const (r ^ n)
    convert hmain using 1
    rcases Nat.eq_zero_or_pos n with hn | hn
    · simp [hn]
    · have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn
      field_simp
  have hbound : ∀ (n : ℕ) (t : ℝ), ‖r ^ n * Real.cos ((n : ℝ) * t) / n‖ ≤ |r| ^ n := by
    intro n t
    rcases Nat.eq_zero_or_pos n with hn | hn
    · simp [hn]
    · have hnn : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
      rw [Real.norm_eq_abs, abs_div, abs_mul, abs_pow, abs_of_nonneg (by positivity : (0:ℝ) ≤ (n:ℝ))]
      have hcos : |Real.cos ((n : ℝ) * t)| ≤ 1 :=
        abs_le.mpr ⟨Real.neg_one_le_cos _, Real.cos_le_one _⟩
      calc |r| ^ n * |Real.cos ((n : ℝ) * t)| / (n : ℝ)
          ≤ |r| ^ n * 1 / 1 := by gcongr
        _ = |r| ^ n := by ring
  have hg0 : Summable (fun n : ℕ => Real.sin ((n : ℝ) * θ) / (n : ℝ) ^ 2 * r ^ n) := by
    refine hu.of_norm_bounded (fun n => ?_)
    rcases Nat.eq_zero_or_pos n with hn | hn
    · simp [hn]
    · have hnn : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
      have hn2 : (1 : ℝ) ≤ (n : ℝ) ^ 2 := by nlinarith [hnn]
      rw [Real.norm_eq_abs, abs_mul, abs_pow]
      have h1 : |Real.sin ((n : ℝ) * θ) / (n : ℝ) ^ 2| ≤ 1 := by
        rw [abs_div, abs_of_nonneg (by positivity : (0:ℝ) ≤ (n:ℝ) ^ 2), div_le_one (by positivity)]
        exact le_trans (abs_le.mpr ⟨Real.neg_one_le_sin _, Real.sin_le_one _⟩) hn2
      calc |Real.sin ((n : ℝ) * θ) / (n : ℝ) ^ 2| * |r| ^ n
          ≤ 1 * |r| ^ n := by gcongr
        _ = |r| ^ n := one_mul _
  exact hasDerivAt_tsum hu hg hbound hg0 θ

/-- **Assembly brick 5 — `hf'`, the local-uniform convergence (sorry-free).**
    As `r → 1⁻`, the regularised derivatives `g_r' = ∑ₙ rⁿ cos(n·)/n` converge
    locally uniformly on `(0, 2π)` to `-log(2 sin(·/2))`. The closing trick: the
    series equals its closed form `F(r,t) = -log‖1 - r e^{it}‖` (brick 2b), and
    `F` is jointly continuous THROUGH `r = 1` away from `t ∈ 2πℤ` (the only zeros
    of `1 - r e^{it}` for `r > 0`, via `Complex.exp_eq_one_iff`); on a compact
    `K ⊆ (0,2π)` the compact product `[½,3/2] ×ˢ K` gives uniform continuity
    (Heine–Cantor), hence uniform convergence as `r → 1` within `[½,3/2]`. The
    conditional-convergence "wall" was an artifact of the series representation —
    no Dirichlet-kernel estimate is needed. (bean qou-6fkd) -/
theorem tendstoLocallyUniformlyOn_tsum_rpow_cos :
    TendstoLocallyUniformlyOn
      (fun (r : ℝ) (t : ℝ) => ∑' n : ℕ, r ^ n * Real.cos ((n : ℝ) * t) / n)
      (fun t : ℝ => -Real.log (2 * Real.sin (t / 2)))
      (nhdsWithin 1 (Set.Iio 1)) (Set.Ioo (0 : ℝ) (2 * π)) := by
  have hpi := Real.pi_pos
  rw [tendstoLocallyUniformlyOn_iff_forall_isCompact isOpen_Ioo]
  intro K hKsub hKc
  -- nonvanishing of `1 - r e^{it}` on the product window
  have hne : ∀ p : ℝ × ℝ, p ∈ Set.Icc (1/2 : ℝ) (3/2) ×ˢ K →
      (1 : ℂ) - (p.1 : ℂ) * Complex.exp ((p.2 : ℂ) * Complex.I) ≠ 0 := by
    rintro ⟨r, t⟩ ⟨hrU, htK⟩ heq
    obtain ⟨ht0, ht2⟩ := hKsub htK
    have hr0 : 0 < r := lt_of_lt_of_le (by norm_num) hrU.1
    have hw : (r : ℂ) * Complex.exp ((t : ℂ) * Complex.I) = 1 :=
      (sub_eq_zero.mp heq).symm
    have hr1 : r = 1 := by
      have hnrm := congrArg norm hw
      rwa [norm_mul, Complex.norm_exp_ofReal_mul_I, mul_one, Complex.norm_real,
        Real.norm_eq_abs, norm_one, abs_of_pos hr0] at hnrm
    have hexp : Complex.exp ((t : ℂ) * Complex.I) = 1 := by
      rw [hr1, Complex.ofReal_one, one_mul] at hw
      exact hw
    obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.mp hexp
    have htn : t = (n : ℝ) * (2 * π) := by
      have him := congrArg Complex.im hn
      simpa using him
    rw [htn] at ht0 ht2
    have hn0 : (0 : ℤ) < n := by
      have : (0 : ℝ) < (n : ℝ) := by nlinarith
      exact_mod_cast this
    have hn1 : n < (1 : ℤ) := by
      have : (n : ℝ) < 1 := by nlinarith
      exact_mod_cast this
    omega
  -- joint continuity on the compact product ⇒ uniform continuity (Heine–Cantor)
  have hcont : ContinuousOn
      (Function.uncurry fun (r t : ℝ) =>
        -Real.log ‖1 - (r : ℂ) * Complex.exp ((t : ℂ) * Complex.I)‖)
      (Set.Icc (1/2 : ℝ) (3/2) ×ˢ K) := by
    have hbase : Continuous (fun p : ℝ × ℝ =>
        (1 : ℂ) - (p.1 : ℂ) * Complex.exp ((p.2 : ℂ) * Complex.I)) := by fun_prop
    exact ((hbase.norm.continuousOn).log fun p hp => norm_ne_zero_iff.mpr (hne p hp)).neg
  have hunif : UniformContinuousOn
      (Function.uncurry fun (r t : ℝ) =>
        -Real.log ‖1 - (r : ℂ) * Complex.exp ((t : ℂ) * Complex.I)‖)
      (Set.Icc (1/2 : ℝ) (3/2) ×ˢ K) :=
    (isCompact_Icc.prod hKc).uniformContinuousOn_of_continuous hcont
  -- uniform convergence of the closed form as r → 1 within the window
  have hFu : TendstoUniformlyOn
      (fun (r t : ℝ) => -Real.log ‖1 - (r : ℂ) * Complex.exp ((t : ℂ) * Complex.I)‖)
      (fun t : ℝ => -Real.log ‖1 - ((1 : ℝ) : ℂ) * Complex.exp ((t : ℂ) * Complex.I)‖)
      (nhdsWithin 1 (Set.Icc (1/2 : ℝ) (3/2))) K :=
    hunif.tendstoUniformlyOn (by norm_num [Set.mem_Icc])
  have hle : nhdsWithin (1 : ℝ) (Set.Iio 1) ≤ nhdsWithin 1 (Set.Icc (1/2 : ℝ) (3/2)) :=
    nhdsWithin_le_of_mem (nhdsWithin_le_nhds (Icc_mem_nhds (by norm_num) (by norm_num)))
  -- swap the limit (brick 3: `‖1-e^{it}‖ = 2 sin(t/2)` on K)
  have hlim : Set.EqOn
      (fun t : ℝ => -Real.log ‖1 - ((1 : ℝ) : ℂ) * Complex.exp ((t : ℂ) * Complex.I)‖)
      (fun t : ℝ => -Real.log (2 * Real.sin (t / 2))) K := by
    intro t htK
    obtain ⟨ht0, ht2⟩ := hKsub htK
    have hs : 0 < Real.sin (t / 2) :=
      Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
    simp only [Complex.ofReal_one, one_mul]
    rw [norm_one_sub_exp_ofReal_mul_I, abs_of_pos hs]
  -- swap the family (brick 2b), eventually `|r| < 1`
  have hev : ∀ᶠ (r : ℝ) in nhdsWithin (1 : ℝ) (Set.Iio 1), Set.EqOn
      (fun t : ℝ => -Real.log ‖1 - (r : ℂ) * Complex.exp ((t : ℂ) * Complex.I)‖)
      (fun t : ℝ => ∑' n : ℕ, r ^ n * Real.cos ((n : ℝ) * t) / n) K := by
    have h1 : ∀ᶠ r in nhdsWithin (1 : ℝ) (Set.Iio 1), r < 1 :=
      eventually_mem_nhdsWithin.mono fun r hr => hr
    have h2 : ∀ᶠ r in nhdsWithin (1 : ℝ) (Set.Iio 1), (-1 : ℝ) < r :=
      (isOpen_Ioi.eventually_mem (by norm_num : (1 : ℝ) ∈ Set.Ioi (-1 : ℝ))).filter_mono
        nhdsWithin_le_nhds
    filter_upwards [h1, h2] with r hr1 hr2 t _
    exact (tsum_rpow_cos_div t (abs_lt.mpr ⟨hr2, hr1⟩)).symm
  have hFu' : TendstoUniformlyOn
      (fun (r t : ℝ) => -Real.log ‖1 - (r : ℂ) * Complex.exp ((t : ℂ) * Complex.I)‖)
      (fun t : ℝ => -Real.log ‖1 - ((1 : ℝ) : ℂ) * Complex.exp ((t : ℂ) * Complex.I)‖)
      (nhdsWithin 1 (Set.Iio 1)) K :=
    fun u hu => (hFu u hu).filter_mono hle
  exact (hFu'.congr_right hlim).congr hev

/-- **The atom — CLOSED, sorry-free.** `Cl_2'(θ) = -log(2 sin(θ/2))` on
    `(0, 2π)`: the term-by-term derivative of the Fourier-series Clausen — the
    identity the filler file deferred to "Fourier-series infrastructure not in
    Mathlib". Proved by `hasDerivAt_of_tendstoLocallyUniformlyOn` from
    `hasDerivAt_g_r` (brick 4), `tendsto_Cl_2_reg` (brick 1), and
    `tendstoLocallyUniformlyOn_tsum_rpow_cos` (brick 5, the former `hf'`).
    With this the whole file is sorry-free: the Zagier series↔integral bridge
    (`clausen_eq_series`) and the `Cl_2` derivative are machine-proved. -/
theorem hasDerivAt_Cl_2_series {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    HasDerivAt QOU.Archimedean.Cl_2 (-Real.log (2 * Real.sin (θ / 2))) θ := by
  have hf' := tendstoLocallyUniformlyOn_tsum_rpow_cos
  have hf : ∀ᶠ r in nhdsWithin (1 : ℝ) (Set.Iio 1),
      ∀ x ∈ Set.Ioo (0 : ℝ) (2 * π),
        HasDerivAt (fun t : ℝ => ∑' n : ℕ, Real.sin ((n : ℝ) * t) / (n : ℝ) ^ 2 * r ^ n)
          ((fun (r : ℝ) (t : ℝ) => ∑' n : ℕ, r ^ n * Real.cos ((n : ℝ) * t) / n) r x) x := by
    have hmem : ∀ᶠ r in nhdsWithin (1 : ℝ) (Set.Iio 1), |r| < 1 := by
      have h1 : ∀ᶠ r in nhdsWithin (1 : ℝ) (Set.Iio 1), r < 1 :=
        eventually_mem_nhdsWithin.mono fun r hr => hr
      have h2 : ∀ᶠ r in nhdsWithin (1 : ℝ) (Set.Iio 1), (-1 : ℝ) < r :=
        (isOpen_Ioi.eventually_mem (by norm_num : (1 : ℝ) ∈ Set.Ioi (-1 : ℝ))).filter_mono
          nhdsWithin_le_nhds
      filter_upwards [h1, h2] with r hr1 hr2
      rw [abs_lt]; exact ⟨hr2, hr1⟩
    filter_upwards [hmem] with r hr x _
    exact hasDerivAt_g_r hr x
  have hfg : ∀ x ∈ Set.Ioo (0 : ℝ) (2 * π),
      Filter.Tendsto (fun r : ℝ => ∑' n : ℕ, Real.sin ((n : ℝ) * x) / (n : ℝ) ^ 2 * r ^ n)
        (nhdsWithin 1 (Set.Iio 1)) (nhds (QOU.Archimedean.Cl_2 x)) :=
    fun x _ => tendsto_Cl_2_reg x
  exact hasDerivAt_of_tendstoLocallyUniformlyOn isOpen_Ioo hf' hf hfg ⟨h0, h2⟩

/-- **Reduction (Route-B brick 2, sorry-free).** `clausen` and
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

/-- **Series↔integral bridge (sorry-free).** On `(0, 2π)`,
    `∫₀^θ -log(2 sin(t/2)) = ∑ sin(kθ)/k²` — the classical Zagier identity,
    fully machine-proved via `clausen_eqOn_Cl_2`. -/
theorem clausen_eq_series {θ : ℝ} (hθ : θ ∈ Set.Ioo (0:ℝ) (2 * π)) :
    clausen θ = QOU.Archimedean.Cl_2 θ :=
  clausen_eqOn_Cl_2 hθ

/-- **Antisymmetry of `Cl_2` about `π` (saddle brick E2, sorry-free).**
    `Cl_2(2π − θ) = −Cl_2(θ)`: termwise `sin((k+1)(2π−θ)) = −sin((k+1)θ)` by
    `2π`-periodicity (`Real.sin_int_mul_two_pi_sub`). Locates the minimum of
    `Cl_2` on `(0,2π)` at `θ = 5π/3` with value `−Cl_2(π/3)` — the value the
    Kashaev saddle max `−2Cl_2(2πx)` attains at `x = 5/6`, feeding the
    existence/value program for `VolumeConjecture41` (bean qou-yrog). -/
theorem Cl_2_two_pi_sub (θ : ℝ) :
    QOU.Archimedean.Cl_2 (2 * π - θ) = -QOU.Archimedean.Cl_2 θ := by
  unfold QOU.Archimedean.Cl_2
  rw [← tsum_neg]
  congr 1
  funext k
  have h : ((k : ℝ) + 1) * (2 * π - θ)
      = ((k + 1 : ℤ) : ℝ) * (2 * π) - ((k : ℝ) + 1) * θ := by push_cast; ring
  rw [h, Real.sin_int_mul_two_pi_sub, neg_div]

/-- **`clausen(π/3) > 0` (saddle brick E3b, integral side, sorry-free).** On
    `(0, π/3)` the integrand `-log(2 sin(t/2))` is strictly positive
    (`2 sin(t/2) < 2 sin(π/6) = 1` by strict monotonicity of `sin`), so the
    integral is positive. -/
theorem clausen_pi_div_three_pos : 0 < clausen (π / 3) := by
  have hpi := Real.pi_pos
  unfold clausen
  apply intervalIntegral_pos_of_pos_on
    ((intervalIntegrable_log_two_sin_half 0 (π / 3)).neg)
  · intro t ht
    have h1 : 0 < Real.sin (t / 2) :=
      Real.sin_pos_of_pos_of_lt_pi (by linarith [ht.1]) (by linarith [ht.2])
    have h2 : Real.sin (t / 2) < 1 / 2 := by
      have hmono := Real.strictMonoOn_sin
        (Set.mem_Icc.mpr ⟨by linarith [ht.1], by linarith [ht.2]⟩)
        (Set.mem_Icc.mpr ⟨by linarith, by linarith⟩)
        (by linarith [ht.2] : t / 2 < π / 6)
      rwa [Real.sin_pi_div_six] at hmono
    have hlog : Real.log (2 * Real.sin (t / 2)) < 0 :=
      Real.log_neg (by linarith) (by linarith)
    simp only [Pi.neg_apply]
    linarith
  · linarith

/-- **`Cl₂(π/3) > 0` (saddle brick E3b, sorry-free).** Transported from the
    integral side through the machine-proved bridge `clausen_eq_series`. This is
    the strict positivity that makes the Kashaev saddle value
    `2 Cl₂(π/3) = Vol(4₁)` a genuine maximum (the `θ = 5π/3` minimum of `Cl₂`
    equals `−Cl₂(π/3) < 0 <` the endpoint values `0`; bean qou-yzs2). -/
theorem Cl_2_pi_div_three_pos : 0 < QOU.Archimedean.Cl_2 (π / 3) := by
  have hpi := Real.pi_pos
  have h := clausen_eq_series (θ := π / 3) ⟨by linarith, by linarith⟩
  rw [← h]
  exact clausen_pi_div_three_pos

/-- **The series Clausen's derivative** `Cl_2'(θ) = -log(2 sin(θ/2))` for
    `θ ∈ (0, 2π)` — the derivative the filler flagged as needing Fourier
    infrastructure, now machine-proved (`hasDerivAt_Cl_2_series`). Dual-purpose: `V'(θ)` of
    `rem:dilog-saddle-regime`, zero at the `θ = π/3` saddle. -/
theorem hasDerivAt_cl_2 {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    HasDerivAt QOU.Archimedean.Cl_2 (-Real.log (2 * Real.sin (θ / 2))) θ :=
  hasDerivAt_Cl_2_series h0 h2

end QOU.Knot
