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

  SCOPE (updated 2026-07-26). Originally this file discharged only the
  DERIVATIVE claim of the dilog-saddle block. The E4/E5 brick program appended
  below (Riemann-sum sandwiches, the all-k uniform deviation bound
  `abs_deviation_le`, and the vanishing master error `tendsto_master_error`)
  now feeds the E5d squeeze in `FigureEightVolumeSqueeze.lean`, which
  DISCHARGES the figure-eight volume-conjecture `sorry` outright
  (`tendsto_log_kashaev_vol`, milestone qou-cpfn). Bean qou-reab (brick 3);
  the Clausen VALUE (no elementary closed form; transcendental) remains
  tracked in bean qou-44ma.

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
import Mathlib.Analysis.SumIntegralComparisons
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

/-- **Saddle brick E4a (sorry-free).** The log-sine integral is the Clausen
    primitive under `t = 2u`: `∫₀^a log(2 sin u) du = −clausen(2a)/2` — the
    continuum limit the Kashaev Riemann sums converge to (bean qou-x5mg). -/
theorem integral_log_two_sin (a : ℝ) :
    ∫ u in (0:ℝ)..a, Real.log (2 * Real.sin u) = -clausen (2 * a) / 2 := by
  have h := intervalIntegral.integral_comp_div
    (f := fun u => Real.log (2 * Real.sin u)) (a := (0:ℝ)) (b := 2 * a)
    (c := 2) two_ne_zero
  simp only [zero_div, smul_eq_mul] at h
  rw [show (2 * a) / 2 = a by ring] at h
  have hcl : clausen (2 * a)
      = -∫ t in (0:ℝ)..(2 * a), Real.log (2 * Real.sin (t / 2)) := by
    unfold clausen
    rw [intervalIntegral.integral_neg]
  rw [hcl, h]
  ring

/-- **Saddle brick E4b, rising half (sorry-free).** `log(2 sin)` is monotone on
    `(0, π/2]` (strict monotonicity of `sin` + monotonicity of `log` on
    positives). The point `0` is excluded: `log(2 sin 0) = log 0 = 0` exceeds
    nearby negative values under Mathlib's `log 0 = 0` convention. -/
theorem monotoneOn_log_two_sin :
    MonotoneOn (fun u => Real.log (2 * Real.sin u)) (Set.Ioc 0 (π / 2)) := by
  have hpi := Real.pi_pos
  intro u hu v hv huv
  have hsu : 0 < Real.sin u :=
    Real.sin_pos_of_pos_of_lt_pi hu.1 (by linarith [hu.2])
  have hsv : Real.sin u ≤ Real.sin v := by
    rcases eq_or_lt_of_le huv with h | h
    · rw [h]
    · exact le_of_lt (Real.strictMonoOn_sin
        (Set.mem_Icc.mpr ⟨by linarith [hu.1], hu.2⟩)
        (Set.mem_Icc.mpr ⟨by linarith [hv.1], hv.2⟩) h)
  exact Real.log_le_log (by linarith) (by linarith)

/-- **Saddle brick E4b, falling half (sorry-free).** `log(2 sin)` is antitone on
    `[π/2, π)` — by the reflection `sin u = sin(π − u)` and the rising half. -/
theorem antitoneOn_log_two_sin :
    AntitoneOn (fun u => Real.log (2 * Real.sin u)) (Set.Ico (π / 2) π) := by
  have hpi := Real.pi_pos
  intro u hu v hv huv
  have hsv : 0 < Real.sin v :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith [hv.1]) hv.2
  have hsvu : Real.sin v ≤ Real.sin u := by
    rw [← Real.sin_pi_sub u, ← Real.sin_pi_sub v]
    rcases eq_or_lt_of_le huv with h | h
    · rw [h]
    · exact le_of_lt (Real.strictMonoOn_sin
        (Set.mem_Icc.mpr ⟨by linarith [hv.2], by linarith [hv.1]⟩)
        (Set.mem_Icc.mpr ⟨by linarith [hu.2], by linarith [hu.1]⟩)
        (by linarith))
  exact Real.log_le_log (by linarith) (by linarith)

/-- **E4c helper (sorry-free).** On the unit grid `[1, c]`, the rescaled
    `v ↦ log(2 sin(v·h))` inherits E4b's monotonicity when `c·h ≤ π/2`. -/
theorem monotoneOn_log_two_sin_mul {h : ℝ} (hh : 0 < h) {c : ℝ}
    (hc : c * h ≤ π / 2) :
    MonotoneOn (fun v : ℝ => Real.log (2 * Real.sin (v * h))) (Set.Icc 1 c) := by
  intro u hu v hv huv
  have h1 : u * h ∈ Set.Ioc 0 (π / 2) :=
    ⟨by nlinarith [hu.1], by nlinarith [hu.2]⟩
  have h2 : v * h ∈ Set.Ioc 0 (π / 2) :=
    ⟨by nlinarith [hv.1], by nlinarith [hv.2]⟩
  exact monotoneOn_log_two_sin h1 h2 (by nlinarith)

/-- **Saddle brick E4c, rising-half lower bound (sorry-free).** On the shifted
    window `[π/N, kπ/N]` inside the rising half, the integral is dominated by
    `π/N` times the right-endpoint log-sine sum — library
    `MonotoneOn.integral_le_sum_Ico` on the unit grid, transported by the
    change of variables `u = v·π/N`. (bean qou-x5mg) -/
theorem integral_le_sum_log_sin {N k : ℕ} (hN : 1 ≤ N) (hk : 1 ≤ k)
    (hhalf : (k : ℝ) * (π / N) ≤ π / 2) :
    (∫ u in ((π : ℝ) / N)..((k : ℝ) * (π / N)), Real.log (2 * Real.sin u))
      ≤ (π / N) * ∑ i ∈ Finset.Ico 1 k,
          Real.log (2 * Real.sin (((i : ℝ) + 1) * (π / N))) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hh : (0 : ℝ) < π / N := by positivity
  have hmono : MonotoneOn (fun v : ℝ => Real.log (2 * Real.sin (v * (π / N))))
      (Set.Icc ((1 : ℕ) : ℝ) ((k : ℕ) : ℝ)) := by
    simpa using monotoneOn_log_two_sin_mul hh (c := (k : ℝ)) hhalf
  have hlib := MonotoneOn.integral_le_sum_Ico (a := 1) (b := k) hk hmono
  have hcov : (∫ v in ((1 : ℕ) : ℝ)..((k : ℕ) : ℝ),
        Real.log (2 * Real.sin (v * (π / N))))
      = (π / N)⁻¹ * ∫ u in ((π : ℝ) / N)..((k : ℝ) * (π / N)),
          Real.log (2 * Real.sin u) := by
    rw [intervalIntegral.integral_comp_mul_right
      (f := fun u => Real.log (2 * Real.sin u)) (ne_of_gt hh)]
    norm_num
  have hsum : (∑ i ∈ Finset.Ico 1 k,
        (fun v : ℝ => Real.log (2 * Real.sin (v * (π / N)))) ((i + 1 : ℕ) : ℝ))
      = ∑ i ∈ Finset.Ico 1 k,
          Real.log (2 * Real.sin (((i : ℝ) + 1) * (π / N))) := by
    refine Finset.sum_congr rfl (fun i _ => ?_)
    push_cast
    ring_nf
  rw [hcov, hsum] at hlib
  calc (∫ u in ((π : ℝ) / N)..((k : ℝ) * (π / N)), Real.log (2 * Real.sin u))
      = (π / N) * ((π / N)⁻¹ * ∫ u in ((π : ℝ) / N)..((k : ℝ) * (π / N)),
          Real.log (2 * Real.sin u)) := by
        field_simp
    _ ≤ (π / N) * ∑ i ∈ Finset.Ico 1 k,
          Real.log (2 * Real.sin (((i : ℝ) + 1) * (π / N))) :=
        mul_le_mul_of_nonneg_left hlib (le_of_lt hh)

/-- **Saddle brick E4c, rising-half upper bound (sorry-free).** `π/N` times the
    left-endpoint log-sine sum `Σ_{j=1}^{k}` is dominated by the integral over
    the widened window `[π/N, (k+1)π/N]` — library
    `MonotoneOn.sum_le_integral_Ico`, same transport. (bean qou-x5mg) -/
theorem sum_log_sin_le_integral {N k : ℕ} (hN : 1 ≤ N) (hk : 1 ≤ k)
    (hhalf : ((k : ℝ) + 1) * (π / N) ≤ π / 2) :
    (π / N) * ∑ i ∈ Finset.Ico 1 (k + 1),
        Real.log (2 * Real.sin ((i : ℝ) * (π / N)))
      ≤ ∫ u in ((π : ℝ) / N)..(((k : ℝ) + 1) * (π / N)),
          Real.log (2 * Real.sin u) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hh : (0 : ℝ) < π / N := by positivity
  have hmono : MonotoneOn (fun v : ℝ => Real.log (2 * Real.sin (v * (π / N))))
      (Set.Icc ((1 : ℕ) : ℝ) (((k + 1 : ℕ)) : ℝ)) := by
    have := monotoneOn_log_two_sin_mul hh (c := (k : ℝ) + 1) hhalf
    have hcast : (((k + 1 : ℕ)) : ℝ) = (k : ℝ) + 1 := by push_cast; ring
    simpa [hcast] using this
  have hlib := MonotoneOn.sum_le_integral_Ico (a := 1) (b := k + 1)
    (by omega) hmono
  have hcov : (∫ v in ((1 : ℕ) : ℝ)..(((k + 1 : ℕ)) : ℝ),
        Real.log (2 * Real.sin (v * (π / N))))
      = (π / N)⁻¹ * ∫ u in ((π : ℝ) / N)..(((k : ℝ) + 1) * (π / N)),
          Real.log (2 * Real.sin u) := by
    rw [intervalIntegral.integral_comp_mul_right
      (f := fun u => Real.log (2 * Real.sin u)) (ne_of_gt hh)]
    push_cast
    norm_num
  have hsum : (∑ x ∈ Finset.Ico 1 (k + 1),
        (fun v : ℝ => Real.log (2 * Real.sin (v * (π / N)))) ((x : ℕ) : ℝ))
      = ∑ i ∈ Finset.Ico 1 (k + 1),
          Real.log (2 * Real.sin ((i : ℝ) * (π / N))) := by
    refine Finset.sum_congr rfl (fun i _ => rfl)
  rw [hcov, hsum] at hlib
  calc (π / N) * ∑ i ∈ Finset.Ico 1 (k + 1),
        Real.log (2 * Real.sin ((i : ℝ) * (π / N)))
      ≤ (π / N) * ((π / N)⁻¹ * ∫ u in ((π : ℝ) / N)..(((k : ℝ) + 1) * (π / N)),
          Real.log (2 * Real.sin u)) :=
        mul_le_mul_of_nonneg_left hlib (le_of_lt hh)
    _ = ∫ u in ((π : ℝ) / N)..(((k : ℝ) + 1) * (π / N)),
          Real.log (2 * Real.sin u) := by
        field_simp

/-- **E4c helper, falling half (sorry-free).** On the unit grid `[c₁, c₂]`, the
    rescaled `v ↦ log(2 sin(v·h))` inherits E4b's antitonicity when
    `π/2 ≤ c₁·h` and `c₂·h < π`. -/
theorem antitoneOn_log_two_sin_mul {h : ℝ} (hh : 0 < h) {c₁ c₂ : ℝ}
    (hc1 : π / 2 ≤ c₁ * h) (hc2 : c₂ * h < π) :
    AntitoneOn (fun v : ℝ => Real.log (2 * Real.sin (v * h))) (Set.Icc c₁ c₂) := by
  intro u hu v hv huv
  have h1 : u * h ∈ Set.Ico (π / 2) π :=
    ⟨by nlinarith [hu.1], by nlinarith [hu.2]⟩
  have h2 : v * h ∈ Set.Ico (π / 2) π :=
    ⟨by nlinarith [hv.1], by nlinarith [hv.2]⟩
  exact antitoneOn_log_two_sin h1 h2 (by nlinarith)

/-- **Saddle brick E4c, falling-half lower bound (sorry-free).** On a window
    `[k₁π/N, k₂π/N] ⊆ [π/2, π)`, the right-endpoint log-sine sum is dominated
    by the integral — library `AntitoneOn.sum_le_integral_Ico`, transported by
    `u = v·π/N`. (bean qou-x5mg) -/
theorem sum_log_sin_le_integral_falling {N k₁ k₂ : ℕ} (hN : 1 ≤ N) (h12 : k₁ ≤ k₂)
    (hlo : π / 2 ≤ (k₁ : ℝ) * (π / N)) (hhi : (k₂ : ℝ) * (π / N) < π) :
    (π / N) * ∑ i ∈ Finset.Ico k₁ k₂,
        Real.log (2 * Real.sin (((i : ℝ) + 1) * (π / N)))
      ≤ ∫ u in ((k₁ : ℝ) * (π / N))..((k₂ : ℝ) * (π / N)),
          Real.log (2 * Real.sin u) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hh : (0 : ℝ) < π / N := by positivity
  have hanti : AntitoneOn (fun v : ℝ => Real.log (2 * Real.sin (v * (π / N))))
      (Set.Icc ((k₁ : ℕ) : ℝ) ((k₂ : ℕ) : ℝ)) := by
    simpa using antitoneOn_log_two_sin_mul hh (c₁ := (k₁ : ℝ)) (c₂ := (k₂ : ℝ)) hlo hhi
  have hlib := AntitoneOn.sum_le_integral_Ico (a := k₁) (b := k₂) h12 hanti
  have hcov : (∫ v in ((k₁ : ℕ) : ℝ)..((k₂ : ℕ) : ℝ),
        Real.log (2 * Real.sin (v * (π / N))))
      = (π / N)⁻¹ * ∫ u in ((k₁ : ℝ) * (π / N))..((k₂ : ℝ) * (π / N)),
          Real.log (2 * Real.sin u) := by
    rw [intervalIntegral.integral_comp_mul_right
      (f := fun u => Real.log (2 * Real.sin u)) (ne_of_gt hh)]
    norm_num
  have hsum : (∑ i ∈ Finset.Ico k₁ k₂,
        (fun v : ℝ => Real.log (2 * Real.sin (v * (π / N)))) ((i + 1 : ℕ) : ℝ))
      = ∑ i ∈ Finset.Ico k₁ k₂,
          Real.log (2 * Real.sin (((i : ℝ) + 1) * (π / N))) := by
    refine Finset.sum_congr rfl (fun i _ => ?_)
    push_cast
    ring_nf
  rw [hcov, hsum] at hlib
  calc (π / N) * ∑ i ∈ Finset.Ico k₁ k₂,
        Real.log (2 * Real.sin (((i : ℝ) + 1) * (π / N)))
      ≤ (π / N) * ((π / N)⁻¹ * ∫ u in ((k₁ : ℝ) * (π / N))..((k₂ : ℝ) * (π / N)),
          Real.log (2 * Real.sin u)) :=
        mul_le_mul_of_nonneg_left hlib (le_of_lt hh)
    _ = ∫ u in ((k₁ : ℝ) * (π / N))..((k₂ : ℝ) * (π / N)),
          Real.log (2 * Real.sin u) := by
        field_simp

/-- **Saddle brick E4c, falling-half upper bound (sorry-free).** On a window
    `[k₁π/N, k₂π/N] ⊆ [π/2, π)`, the integral is dominated by `π/N` times the
    left-endpoint log-sine sum — library `AntitoneOn.integral_le_sum_Ico`,
    same transport. (bean qou-x5mg) -/
theorem integral_le_sum_log_sin_falling {N k₁ k₂ : ℕ} (hN : 1 ≤ N) (h12 : k₁ ≤ k₂)
    (hlo : π / 2 ≤ (k₁ : ℝ) * (π / N)) (hhi : (k₂ : ℝ) * (π / N) < π) :
    (∫ u in ((k₁ : ℝ) * (π / N))..((k₂ : ℝ) * (π / N)), Real.log (2 * Real.sin u))
      ≤ (π / N) * ∑ i ∈ Finset.Ico k₁ k₂,
          Real.log (2 * Real.sin ((i : ℝ) * (π / N))) := by
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hh : (0 : ℝ) < π / N := by positivity
  have hanti : AntitoneOn (fun v : ℝ => Real.log (2 * Real.sin (v * (π / N))))
      (Set.Icc ((k₁ : ℕ) : ℝ) ((k₂ : ℕ) : ℝ)) := by
    simpa using antitoneOn_log_two_sin_mul hh (c₁ := (k₁ : ℝ)) (c₂ := (k₂ : ℝ)) hlo hhi
  have hlib := AntitoneOn.integral_le_sum_Ico (a := k₁) (b := k₂) h12 hanti
  have hcov : (∫ v in ((k₁ : ℕ) : ℝ)..((k₂ : ℕ) : ℝ),
        Real.log (2 * Real.sin (v * (π / N))))
      = (π / N)⁻¹ * ∫ u in ((k₁ : ℝ) * (π / N))..((k₂ : ℝ) * (π / N)),
          Real.log (2 * Real.sin u) := by
    rw [intervalIntegral.integral_comp_mul_right
      (f := fun u => Real.log (2 * Real.sin u)) (ne_of_gt hh)]
    norm_num
  have hsum : (∑ x ∈ Finset.Ico k₁ k₂,
        (fun v : ℝ => Real.log (2 * Real.sin (v * (π / N)))) ((x : ℕ) : ℝ))
      = ∑ i ∈ Finset.Ico k₁ k₂,
          Real.log (2 * Real.sin ((i : ℝ) * (π / N))) :=
    Finset.sum_congr rfl (fun i _ => rfl)
  rw [hcov, hsum] at hlib
  calc (∫ u in ((k₁ : ℝ) * (π / N))..((k₂ : ℝ) * (π / N)), Real.log (2 * Real.sin u))
      = (π / N) * ((π / N)⁻¹ * ∫ u in ((k₁ : ℝ) * (π / N))..((k₂ : ℝ) * (π / N)),
          Real.log (2 * Real.sin u)) := by
        field_simp
    _ ≤ (π / N) * ∑ i ∈ Finset.Ico k₁ k₂,
          Real.log (2 * Real.sin ((i : ℝ) * (π / N))) :=
        mul_le_mul_of_nonneg_left hlib (le_of_lt hh)

/-- The unhalved log-sine integrand is interval-integrable (transport of the
    halved version through `t = 2u`). -/
theorem intervalIntegrable_log_two_sin (a b : ℝ) :
    IntervalIntegrable (fun u => Real.log (2 * Real.sin u)) volume a b := by
  have h := (intervalIntegrable_log_two_sin_half (2 * a) (2 * b)).comp_mul_left (c := 2)
  have hfun : (fun x : ℝ => Real.log (2 * Real.sin (2 * x / 2)))
      = fun u : ℝ => Real.log (2 * Real.sin u) := by
    funext x; norm_num
  rw [hfun] at h
  simpa using h

/-- **`clausen` is continuous (E4d support, sorry-free).** The primitive of an
    everywhere interval-integrable function is continuous
    (`intervalIntegral.continuous_primitive`). -/
theorem continuous_clausen : Continuous clausen := by
  unfold clausen
  exact intervalIntegral.continuous_primitive
    (fun a b => (intervalIntegrable_log_two_sin_half a b).neg) 0

@[simp] theorem clausen_zero : clausen 0 = 0 := by
  unfold clausen
  simp

/-- The series↔integral bridge extends to the CLOSED interval `[0, 2π]` by
    continuity of both sides (`Set.EqOn.closure`). -/
theorem clausen_eqOn_Icc :
    Set.EqOn clausen QOU.Archimedean.Cl_2 (Set.Icc (0:ℝ) (2 * π)) := by
  have hpi := Real.pi_pos
  have h := clausen_eqOn_Cl_2.closure continuous_clausen continuous_Cl_2
  rwa [closure_Ioo (by linarith : (0:ℝ) ≠ 2 * π)] at h

/-- `clausen(2π) = 0` — the right endpoint, by the closed-interval bridge and
    `Cl₂(2π) = 0`. Equivalently `∫₀^π log(2 sin u) du = 0`. -/
@[simp] theorem clausen_two_pi : clausen (2 * π) = 0 := by
  have hpi := Real.pi_pos
  rw [clausen_eqOn_Icc ⟨by linarith, le_refl _⟩, QOU.Archimedean.Cl_2_two_pi]

/-- **Saddle brick E4d-1 (sorry-free).** The cell integral `∫₀^{C·π/N}` of the
    log-sine vanishes as `N → ∞` — the singular first cell contributes nothing
    in the limit. Via E4a + continuity of `clausen` at `0`. (bean qou-x5mg) -/
theorem tendsto_integral_cell (C : ℝ) :
    Filter.Tendsto (fun N : ℕ => ∫ u in (0:ℝ)..(C * (π / N)), Real.log (2 * Real.sin u))
      Filter.atTop (nhds 0) := by
  have hrw : ∀ N : ℕ, (∫ u in (0:ℝ)..(C * (π / N)), Real.log (2 * Real.sin u))
      = -clausen (2 * (C * (π / N))) / 2 := fun N => integral_log_two_sin _
  simp only [hrw]
  have h1 : Filter.Tendsto (fun N : ℕ => 2 * C * π / N) Filter.atTop (nhds 0) :=
    tendsto_const_div_atTop_nhds_zero_nat (2 * C * π)
  have h2 : Filter.Tendsto (fun N : ℕ => clausen (2 * (C * (π / N))))
      Filter.atTop (nhds 0) := by
    have hcomp := (continuous_clausen.tendsto 0).comp
      (by simpa [mul_div_assoc, mul_assoc] using h1)
    simpa [clausen_zero, Function.comp_def, mul_div_assoc, mul_assoc] using hcomp
  simpa using (h2.neg).div_const 2

/-- **Saddle brick E4d-2 (sorry-free).** The scaled first grid term
    `(π/N)·log(2 sin(π/N)) → 0`: squeezed between the primitive differences
    `∫₀^{π/N} ≤ (π/N)·f(π/N) ≤ ∫_{π/N}^{2π/N}` (monotonicity of the integrand
    near `0`), both of which vanish by E4d-1 — no `x·log x` special-function
    limit needed. (bean qou-x5mg) -/
theorem tendsto_first_term :
    Filter.Tendsto (fun N : ℕ => (π / N) * Real.log (2 * Real.sin (π / N)))
      Filter.atTop (nhds 0) := by
  have hpi := Real.pi_pos
  have hlow : Filter.Tendsto (fun N : ℕ => ∫ u in (0:ℝ)..(1 * (π / N)),
      Real.log (2 * Real.sin u)) Filter.atTop (nhds 0) := tendsto_integral_cell 1
  have hupp0 := tendsto_integral_cell 2
  have hupp : Filter.Tendsto (fun N : ℕ =>
      (∫ u in (0:ℝ)..(2 * (π / N)), Real.log (2 * Real.sin u))
        - ∫ u in (0:ℝ)..(1 * (π / N)), Real.log (2 * Real.sin u))
      Filter.atTop (nhds 0) := by
    simpa using hupp0.sub hlow
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' (by simpa using hlow)
    (by simpa using hupp) ?_ ?_
  · -- ∫₀^{π/N} f ≤ (π/N)·f(π/N)  (f ≤ f(π/N) a.e. on [0, π/N])
    filter_upwards [Filter.eventually_ge_atTop 2] with N hN
    have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have hh : (0:ℝ) < π / N := by positivity
    have h2N : (2:ℝ) ≤ N := by exact_mod_cast hN
    have hhalf : π / (N:ℝ) ≤ π / 2 := by gcongr <;> linarith
    have hmono : (∫ u in (0:ℝ)..(π / N), Real.log (2 * Real.sin u))
        ≤ ∫ _u in (0:ℝ)..(π / N), Real.log (2 * Real.sin (π / N)) := by
      apply intervalIntegral.integral_mono_ae_restrict (le_of_lt hh)
        (intervalIntegrable_log_two_sin _ _) intervalIntegrable_const
      have hvol : ∀ᵐ x ∂(volume : MeasureTheory.Measure ℝ), x ≠ 0 := by
        rw [MeasureTheory.ae_iff]
        simpa [Set.setOf_eq_eq_singleton] using Real.volume_singleton (x := 0)
      have hne : ∀ᵐ x ∂(volume.restrict (Set.Icc (0:ℝ) (π / N))), x ≠ 0 :=
        hvol.filter_mono (MeasureTheory.ae_mono MeasureTheory.Measure.restrict_le_self)
      have hmem : ∀ᵐ x ∂(volume.restrict (Set.Icc (0:ℝ) (π / N))),
          x ∈ Set.Icc (0:ℝ) (π / N) :=
        MeasureTheory.ae_restrict_mem measurableSet_Icc
      filter_upwards [hne, hmem] with x hx hxmem
      exact monotoneOn_log_two_sin
        ⟨lt_of_le_of_ne hxmem.1 (Ne.symm hx), le_trans hxmem.2 hhalf⟩
        ⟨hh, hhalf⟩ hxmem.2
    rw [intervalIntegral.integral_const, smul_eq_mul, sub_zero] at hmono
    simpa using hmono
  · -- (π/N)·f(π/N) ≤ ∫_{π/N}^{2π/N} f  (f(π/N) ≤ f on [π/N, 2π/N])
    filter_upwards [Filter.eventually_ge_atTop 4] with N hN
    have hNpos : (0:ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have hh : (0:ℝ) < π / N := by positivity
    have h4N : (4:ℝ) ≤ N := by exact_mod_cast hN
    have hquarter : 2 * (π / (N:ℝ)) ≤ π / 2 := by
      have hstep : π / (N:ℝ) ≤ π / 4 := by gcongr <;> linarith
      calc 2 * (π / (N:ℝ)) ≤ 2 * (π / 4) := by linarith
        _ = π / 2 := by ring
    have hsplit : (∫ u in ((π:ℝ) / N)..(2 * (π / N)), Real.log (2 * Real.sin u))
        = (∫ u in (0:ℝ)..(2 * (π / N)), Real.log (2 * Real.sin u))
          - ∫ u in (0:ℝ)..(π / N), Real.log (2 * Real.sin u) := by
      rw [eq_sub_iff_add_eq]
      rw [add_comm]
      exact intervalIntegral.integral_add_adjacent_intervals
        (intervalIntegrable_log_two_sin _ _) (intervalIntegrable_log_two_sin _ _)
    have hmono : (∫ _u in ((π:ℝ) / N)..(2 * (π / N)), Real.log (2 * Real.sin (π / N)))
        ≤ ∫ u in ((π:ℝ) / N)..(2 * (π / N)), Real.log (2 * Real.sin u) := by
      refine intervalIntegral.integral_mono_on ?_ _root_.intervalIntegrable_const
        (intervalIntegrable_log_two_sin _ _) ?_
      · nlinarith
      intro x hxmem
      exact monotoneOn_log_two_sin ⟨hh, by nlinarith⟩
        ⟨lt_of_lt_of_le hh hxmem.1, le_trans hxmem.2 hquarter⟩ hxmem.1
    rw [intervalIntegral.integral_const, smul_eq_mul] at hmono
    have harith : (2 * (π / N) - π / N) * Real.log (2 * Real.sin (π / N))
        = (π / N) * Real.log (2 * Real.sin (π / N)) := by ring
    rw [harith] at hmono
    calc (π / N) * Real.log (2 * Real.sin (π / N))
        ≤ ∫ u in ((π:ℝ) / N)..(2 * (π / N)), Real.log (2 * Real.sin u) := hmono
      _ = _ := hsplit

/-- **Saddle brick E4e-i, upper (sorry-free).** The Kashaev-indexed rising-half
    upper bound: `(π/N)·Σ_{j∈Icc 1 k} log(2sin(jπ/N)) ≤ ∫_{π/N}^{(k+1)π/N}` —
    E4c-upper with the grid `Ico 1 (k+1)` rewritten to the Kashaev index set
    `Icc 1 k`. (bean qou-x5mg) -/
theorem sum_log_sin_le_integral_Icc {N k : ℕ} (hN : 1 ≤ N) (hk : 1 ≤ k)
    (hhalf : ((k : ℝ) + 1) * (π / N) ≤ π / 2) :
    (π / N) * ∑ j ∈ Finset.Icc 1 k, Real.log (2 * Real.sin ((j : ℝ) * (π / N)))
      ≤ ∫ u in ((π : ℝ) / N)..(((k : ℝ) + 1) * (π / N)),
          Real.log (2 * Real.sin u) := by
  have h := sum_log_sin_le_integral hN hk hhalf
  rwa [Nat.Ico_succ_right] at h

/-- **Saddle brick E4e-i, lower (sorry-free).** The Kashaev-indexed rising-half
    lower bound: `∫_{π/N}^{kπ/N} + (π/N)·log(2sin(π/N)) ≤ (π/N)·Σ_{j∈Icc 1 k}` —
    E4c-lower plus the split-off first grid term (whose scaled value vanishes
    by E4d-2). (bean qou-x5mg) -/
theorem integral_le_sum_log_sin_Icc {N k : ℕ} (hN : 1 ≤ N) (hk : 1 ≤ k)
    (hhalf : (k : ℝ) * (π / N) ≤ π / 2) :
    (∫ u in ((π : ℝ) / N)..((k : ℝ) * (π / N)), Real.log (2 * Real.sin u))
        + (π / N) * Real.log (2 * Real.sin (π / N))
      ≤ (π / N) * ∑ j ∈ Finset.Icc 1 k,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
  have h := integral_le_sum_log_sin hN hk hhalf
  have hsplit : (∑ j ∈ Finset.Icc 1 k, Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      = Real.log (2 * Real.sin (π / N))
        + ∑ i ∈ Finset.Ico 1 k, Real.log (2 * Real.sin (((i : ℝ) + 1) * (π / N))) := by
    have h1 : Finset.Icc 1 k = insert 1 (Finset.Icc 2 k) := by
      ext x
      simp only [Finset.mem_Icc, Finset.mem_insert]
      omega
    rw [h1, Finset.sum_insert (by simp [Finset.mem_Icc])]
    congr 1
    · norm_num
    · rw [← Nat.Ico_succ_right,
        show Finset.Ico 2 (k + 1)
          = Finset.map ⟨fun i => i + 1, fun a b h => by simpa using h⟩ (Finset.Ico 1 k) from ?_,
        Finset.sum_map]
      · refine Finset.sum_congr rfl (fun i _ => ?_)
        simp only [Function.Embedding.coeFn_mk]
        push_cast
        ring_nf
      · ext x
        simp only [Finset.mem_Ico, Finset.mem_map, Function.Embedding.coeFn_mk]
        constructor
        · intro hx
          exact ⟨x - 1, by omega, by omega⟩
        · rintro ⟨y, hy, rfl⟩
          omega
  rw [hsplit, mul_add]
  linarith

/-- **E4e reindex helper (sorry-free).** Shifting a sum from the Kashaev index
    set `Icc (m+1) k` to right-endpoint form over `Ico m k`. -/
theorem sum_Icc_succ_eq_sum_Ico (g : ℕ → ℝ) (m k : ℕ) :
    ∑ j ∈ Finset.Icc (m + 1) k, g j = ∑ i ∈ Finset.Ico m k, g (i + 1) := by
  rw [← Nat.Ico_succ_right,
    show Finset.Ico (m + 1) (k + 1)
      = Finset.map ⟨fun i => i + 1, fun a b h => by simpa using h⟩ (Finset.Ico m k)
      from ?_,
    Finset.sum_map]
  · rfl
  · ext x
    simp only [Finset.mem_Ico, Finset.mem_map, Function.Embedding.coeFn_mk]
    constructor
    · intro hx
      exact ⟨x - 1, by omega, by omega⟩
    · rintro ⟨y, hy, rfl⟩
      omega

/-- **E4e decomposition helper (sorry-free).** The left-endpoint sum over
    `Ico m k` in terms of the Kashaev index set: for `m ≤ k`,
    `Σ_{Ico m k} g = g(m) + Σ_{Icc (m+1) k} g − g(k)`. -/
theorem sum_Ico_eq_add_sum_Icc_sub (g : ℕ → ℝ) {m k : ℕ} (hmk : m ≤ k) :
    ∑ i ∈ Finset.Ico m k, g i
      = g m + (∑ j ∈ Finset.Icc (m + 1) k, g j) - g k := by
  rcases eq_or_lt_of_le hmk with rfl | hlt
  · simp
  · have h1 : Finset.Ico m k = insert m (Finset.Ico (m + 1) k) := by
      ext x
      simp only [Finset.mem_Ico, Finset.mem_insert]
      omega
    have h2 : Finset.Icc (m + 1) k = insert k (Finset.Ico (m + 1) k) := by
      rw [← Nat.Ico_succ_right, Nat.Ico_succ_right_eq_insert_Ico (by omega)]
    rw [h1, Finset.sum_insert (by simp), h2, Finset.sum_insert (by simp)]
    ring

/-- **Saddle brick E4e-ii, upper (sorry-free).** Falling-half Kashaev-indexed
    upper bound: on `[mπ/N, kπ/N] ⊆ [π/2, π)`,
    `(π/N)·Σ_{j∈Icc (m+1) k} log(2sin(jπ/N)) ≤ ∫_{mπ/N}^{kπ/N}` — the falling
    sums are right-endpoint sums of an antitone integrand. (bean qou-x5mg) -/
theorem sum_log_sin_le_integral_falling_Icc {N m k : ℕ} (hN : 1 ≤ N) (hmk : m ≤ k)
    (hlo : π / 2 ≤ (m : ℝ) * (π / N)) (hhi : (k : ℝ) * (π / N) < π) :
    (π / N) * ∑ j ∈ Finset.Icc (m + 1) k,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N)))
      ≤ ∫ u in ((m : ℝ) * (π / N))..((k : ℝ) * (π / N)),
          Real.log (2 * Real.sin u) := by
  have h := sum_log_sin_le_integral_falling hN hmk hlo hhi
  have hre := sum_Icc_succ_eq_sum_Ico
    (fun j => Real.log (2 * Real.sin ((j : ℝ) * (π / N)))) m k
  have hcast : (∑ i ∈ Finset.Ico m k,
        (fun j : ℕ => Real.log (2 * Real.sin ((j : ℝ) * (π / N)))) (i + 1))
      = ∑ i ∈ Finset.Ico m k,
          Real.log (2 * Real.sin (((i : ℝ) + 1) * (π / N))) := by
    refine Finset.sum_congr rfl (fun i _ => ?_)
    push_cast
    ring_nf
  rw [hre, hcast]
  exact h

/-- **Saddle brick E4e-ii, lower (sorry-free).** Falling-half Kashaev-indexed
    lower bound with explicit boundary terms: on `[mπ/N, kπ/N] ⊆ [π/2, π)`,
    `∫_{mπ/N}^{kπ/N} ≤ (π/N)·Σ_{j∈Icc (m+1) k} + (π/N)·f(mπ/N) − (π/N)·f(kπ/N)`
    — the E5 assembly bounds the two boundary terms (near `π/2` the integrand is
    at most `log 2`; near `π` it mirrors the E4d singular cell by
    `sin(π−u) = sin u`). (bean qou-x5mg) -/
theorem integral_le_sum_log_sin_falling_Icc {N m k : ℕ} (hN : 1 ≤ N) (hmk : m ≤ k)
    (hlo : π / 2 ≤ (m : ℝ) * (π / N)) (hhi : (k : ℝ) * (π / N) < π) :
    (∫ u in ((m : ℝ) * (π / N))..((k : ℝ) * (π / N)), Real.log (2 * Real.sin u))
      ≤ (π / N) * (∑ j ∈ Finset.Icc (m + 1) k,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        + (π / N) * Real.log (2 * Real.sin ((m : ℝ) * (π / N)))
        - (π / N) * Real.log (2 * Real.sin ((k : ℝ) * (π / N))) := by
  have h := integral_le_sum_log_sin_falling hN hmk hlo hhi
  have hdec := sum_Ico_eq_add_sum_Icc_sub
    (fun j : ℕ => Real.log (2 * Real.sin ((j : ℝ) * (π / N)))) hmk
  rw [hdec] at h
  calc (∫ u in ((m : ℝ) * (π / N))..((k : ℝ) * (π / N)), Real.log (2 * Real.sin u))
      ≤ (π / N) * (Real.log (2 * Real.sin ((m : ℝ) * (π / N)))
          + (∑ j ∈ Finset.Icc (m + 1) k, Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
          - Real.log (2 * Real.sin ((k : ℝ) * (π / N)))) := h
    _ = (π / N) * (∑ j ∈ Finset.Icc (m + 1) k,
            Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        + (π / N) * Real.log (2 * Real.sin ((m : ℝ) * (π / N)))
        - (π / N) * Real.log (2 * Real.sin ((k : ℝ) * (π / N))) := by ring

/-- **E5b ceiling (sorry-free).** The log-sine integrand never exceeds `log 2`
    on `(0, π)`. -/
theorem log_two_sin_le_log_two {u : ℝ} (h0 : 0 < u) (hπ : u < π) :
    Real.log (2 * Real.sin u) ≤ Real.log 2 := by
  have hs : 0 < Real.sin u := Real.sin_pos_of_pos_of_lt_pi h0 hπ
  exact Real.log_le_log (by linarith)
    (by nlinarith [Real.sin_le_one u])

/-- **E5b floor (sorry-free).** On the mirror-symmetric window `[h, π−h]`
    (with `0 < h ≤ π/2`), the unimodal log-sine integrand is at least its
    common boundary value `f(h)`: by monotonicity up to `π/2` and the
    reflection `sin(π−u) = sin u` beyond. -/
theorem log_two_sin_ge_boundary {h u : ℝ} (hh : 0 < h) (hhalf : h ≤ π / 2)
    (hu1 : h ≤ u) (hu2 : u ≤ π - h) :
    Real.log (2 * Real.sin h) ≤ Real.log (2 * Real.sin u) := by
  have hpi := Real.pi_pos
  rcases le_or_gt u (π / 2) with hcase | hcase
  · exact monotoneOn_log_two_sin ⟨hh, hhalf⟩ ⟨lt_of_lt_of_le hh hu1, hcase⟩ hu1
  · have hmirror : Real.log (2 * Real.sin u) = Real.log (2 * Real.sin (π - u)) := by
      rw [Real.sin_pi_sub]
    have hmirror' : Real.log (2 * Real.sin h) = Real.log (2 * Real.sin h) := rfl
    rw [hmirror]
    exact monotoneOn_log_two_sin ⟨hh, hhalf⟩
      ⟨by linarith, by linarith⟩ (by linarith)

/-- **E5b crude cell bound (sorry-free).** For any window `[a, b] ⊆ [h, π−h]`,
    the log-sine integral is at most `(b−a)·(|f(h)| + log 2)` in absolute value —
    the boundary-cell control the E5 stitch charges to the master error term.
    (bean qou-sho7) -/
theorem abs_integral_log_sin_cell_le {h a b : ℝ} (hh : 0 < h) (hhalf : h ≤ π / 2)
    (hab : a ≤ b) (ha : h ≤ a) (hb : b ≤ π - h) :
    |∫ u in a..b, Real.log (2 * Real.sin u)|
      ≤ (b - a) * (|Real.log (2 * Real.sin h)| + Real.log 2) := by
  have hpi := Real.pi_pos
  have hbound : ∀ x ∈ Set.uIoc a b,
      ‖Real.log (2 * Real.sin x)‖ ≤ |Real.log (2 * Real.sin h)| + Real.log 2 := by
    intro x hx
    rw [Set.uIoc_of_le hab] at hx
    have hx1 : h ≤ x := le_trans ha (le_of_lt hx.1)
    have hx2 : x ≤ π - h := le_trans hx.2 hb
    have hceil : Real.log (2 * Real.sin x) ≤ Real.log 2 :=
      log_two_sin_le_log_two (by linarith) (by linarith)
    have hfloor : Real.log (2 * Real.sin h) ≤ Real.log (2 * Real.sin x) :=
      log_two_sin_ge_boundary hh hhalf hx1 hx2
    rw [Real.norm_eq_abs, abs_le]
    constructor
    · have : -|Real.log (2 * Real.sin h)| ≤ Real.log (2 * Real.sin h) :=
        neg_abs_le _
      nlinarith [Real.log_nonneg (by norm_num : (1:ℝ) ≤ 2)]
    · nlinarith [abs_nonneg (Real.log (2 * Real.sin h))]
  have := intervalIntegral.norm_integral_le_of_norm_le_const hbound
  rw [Real.norm_eq_abs, abs_of_nonneg (by linarith : (0:ℝ) ≤ b - a)] at this
  calc |∫ u in a..b, Real.log (2 * Real.sin u)|
      ≤ (|Real.log (2 * Real.sin h)| + Real.log 2) * (b - a) := this
    _ = (b - a) * (|Real.log (2 * Real.sin h)| + Real.log 2) := by ring

/-- **E5c-2 — pointwise integrand bound (sorry-free).** On the mirror window
    `[h, π−h]`, `|log(2 sin u)| ≤ |log(2 sin h)| + log 2` — ceiling + floor
    combined. (bean qou-n8d0) -/
theorem abs_log_two_sin_le {h u : ℝ} (hh : 0 < h) (hhalf : h ≤ π / 2)
    (hu1 : h ≤ u) (hu2 : u ≤ π - h) :
    |Real.log (2 * Real.sin u)| ≤ |Real.log (2 * Real.sin h)| + Real.log 2 := by
  have hpi := Real.pi_pos
  have hceil : Real.log (2 * Real.sin u) ≤ Real.log 2 :=
    log_two_sin_le_log_two (by linarith) (by linarith)
  have hfloor : Real.log (2 * Real.sin h) ≤ Real.log (2 * Real.sin u) :=
    log_two_sin_ge_boundary hh hhalf hu1 hu2
  rw [abs_le]
  constructor
  · have := neg_abs_le (Real.log (2 * Real.sin h))
    nlinarith [Real.log_nonneg (by norm_num : (1:ℝ) ≤ 2)]
  · nlinarith [abs_nonneg (Real.log (2 * Real.sin h))]

/-- **E5 F-bridge (sorry-free).** The log-sine integral over any window as a
    Clausen-primitive difference: `∫_a^b = F(b) − F(a)` with
    `F(x) = −clausen(2x)/2`. -/
theorem integral_log_sin_window (a b : ℝ) :
    (∫ u in a..b, Real.log (2 * Real.sin u))
      = (-clausen (2 * b) / 2) - (-clausen (2 * a) / 2) := by
  have hadd := intervalIntegral.integral_add_adjacent_intervals
    (intervalIntegrable_log_two_sin 0 a) (intervalIntegrable_log_two_sin a b)
  have h1 := integral_log_two_sin a
  have h2 := integral_log_two_sin b
  linarith

/-- **Saddle brick E5c-1 — rising uniform deviation (sorry-free).** For every
    `k` in the rising range `(k+1)π/N ≤ π/2`, the scaled Kashaev log-sum
    deviates from the Clausen primitive `F(kπ/N) = −clausen(2kπ/N)/2` by at most
    the k-INDEPENDENT master error
    `E₁(N) = |F(π/N)| + (π/N)|f(π/N)| + (π/N)(|f(π/N)| + log 2)`
    — assembled from the E4e-i sandwich, the F-bridge, and the crude bound on
    the single overshoot cell `[kπ/N, (k+1)π/N]`. Every E₁ summand → 0 by E4d.
    (bean qou-bnge) -/
theorem abs_rising_deviation_le {N k : ℕ} (hN : 1 ≤ N) (hk : 1 ≤ k)
    (hhalf : ((k : ℝ) + 1) * (π / N) ≤ π / 2) :
    |(π / N) * (∑ j ∈ Finset.Icc 1 k, Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)|
      ≤ |(-clausen (2 * (π / N)) / 2)|
        + (π / N) * |Real.log (2 * Real.sin (π / N))|
        + (π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hh : (0 : ℝ) < π / N := by positivity
  have hk1 : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hkhalf : (k : ℝ) * (π / N) ≤ π / 2 := by nlinarith
  have hhπ : π / N ≤ π / 2 := by nlinarith
  -- upper: h·S(k) ≤ F((k+1)h) − F(h)  (E4e-i upper + F-bridge)
  have hup := sum_log_sin_le_integral_Icc hN hk hhalf
  rw [integral_log_sin_window] at hup
  -- lower: F(kh) − F(h) + h·f(h) ≤ h·S(k)  (E4e-i lower + F-bridge)
  have hlo := integral_le_sum_log_sin_Icc hN hk hkhalf
  rw [integral_log_sin_window] at hlo
  -- the overshoot cell [kh, (k+1)h] ⊆ [h, π−h]
  have hcell : |(-clausen (2 * (((k : ℝ) + 1) * (π / N))) / 2)
        - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)|
      ≤ (π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) := by
    have := abs_integral_log_sin_cell_le hh hhπ
      (a := (k : ℝ) * (π / N)) (b := ((k : ℝ) + 1) * (π / N))
      (by nlinarith) (by nlinarith) (by nlinarith)
    rw [integral_log_sin_window] at this
    calc |(-clausen (2 * (((k : ℝ) + 1) * (π / N))) / 2)
          - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)|
        ≤ (((k : ℝ) + 1) * (π / N) - (k : ℝ) * (π / N))
            * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) := this
      _ = (π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) := by ring
  -- assemble the two-sided bound
  rw [abs_le]
  rw [abs_le] at hcell
  constructor
  · -- lower side: from hlo
    have h1 := abs_nonneg (Real.log (2 * Real.sin (π / N)))
    have h2 := le_abs_self (-clausen (2 * (π / N)) / 2)
    have h3 := neg_abs_le (-clausen (2 * (π / N)) / 2)
    have h4 := neg_abs_le (Real.log (2 * Real.sin (π / N)))
    have h5 := le_abs_self (Real.log (2 * Real.sin (π / N)))
    have h6 := Real.log_nonneg (by norm_num : (1:ℝ) ≤ 2)
    nlinarith [hlo, mul_le_mul_of_nonneg_left h5 (le_of_lt hh),
      mul_le_mul_of_nonneg_left h4 (le_of_lt hh)]
  · -- upper side: from hup + hcell
    have h2 := le_abs_self (-clausen (2 * (π / N)) / 2)
    have h3 := neg_abs_le (-clausen (2 * (π / N)) / 2)
    nlinarith [hup, hcell.2, mul_le_mul_of_nonneg_left
      (le_abs_self (Real.log (2 * Real.sin (π / N)))) (le_of_lt hh),
      mul_nonneg (le_of_lt hh) (abs_nonneg (Real.log (2 * Real.sin (π / N))))]

/-- **Saddle brick E5c-3 — falling uniform deviation (sorry-free).** For any
    falling window `[mπ/N, kπ/N] ⊆ [π/2, π−π/N]`, the scaled block log-sum
    deviates from the Clausen-primitive difference by at most the
    (m,k)-INDEPENDENT error `2·(π/N)(|f(π/N)| + log 2)` — E4e-ii sandwich +
    F-bridge, boundary terms charged to E5c-2. (bean qou-emex) -/
theorem abs_falling_deviation_le {N m k : ℕ} (hN : 1 ≤ N) (hmk : m ≤ k)
    (hlo : π / 2 ≤ (m : ℝ) * (π / N)) (hkN : k ≤ N - 1) :
    |(π / N) * (∑ j ∈ Finset.Icc (m + 1) k,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - ((-clausen (2 * ((k : ℝ) * (π / N))) / 2)
            - (-clausen (2 * ((m : ℝ) * (π / N))) / 2))|
      ≤ 2 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2)) := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have hh : (0 : ℝ) < π / N := by positivity
  have hm1 : 1 ≤ m := by
    by_contra hm0
    push_neg at hm0
    have hmz : m = 0 := by omega
    rw [hmz] at hlo
    push_cast at hlo
    nlinarith
  have hN2 : 2 ≤ N := by omega
  have h2N : (2 : ℝ) ≤ N := by exact_mod_cast hN2
  have hhπ : π / N ≤ π / 2 := by gcongr <;> linarith
  have hm1' : (1 : ℝ) ≤ (m : ℝ) := by exact_mod_cast hm1
  have hmk' : (m : ℝ) ≤ (k : ℝ) := by exact_mod_cast hmk
  have hkN' : (k : ℝ) ≤ (N : ℝ) - 1 := by
    have h : ((k : ℕ) : ℝ) ≤ ((N - 1 : ℕ) : ℝ) := by exact_mod_cast hkN
    rwa [Nat.cast_sub hN, Nat.cast_one] at h
  have hNh : ((N : ℝ) - 1) * (π / N) = π - π / N := by
    field_simp
  have hhi : (k : ℝ) * (π / N) < π := by nlinarith
  have hup := sum_log_sin_le_integral_falling_Icc hN hmk hlo hhi
  have hlow := integral_le_sum_log_sin_falling_Icc hN hmk hlo hhi
  rw [integral_log_sin_window] at hup hlow
  have hfm : |Real.log (2 * Real.sin ((m : ℝ) * (π / N)))|
      ≤ |Real.log (2 * Real.sin (π / N))| + Real.log 2 :=
    abs_log_two_sin_le hh hhπ (by nlinarith) (by nlinarith)
  have hfk : |Real.log (2 * Real.sin ((k : ℝ) * (π / N)))|
      ≤ |Real.log (2 * Real.sin (π / N))| + Real.log 2 :=
    abs_log_two_sin_le hh hhπ (by nlinarith) (by nlinarith)
  rw [abs_le]
  constructor
  · nlinarith [hlow,
      mul_le_mul_of_nonneg_left
        (le_abs_self (Real.log (2 * Real.sin ((m : ℝ) * (π / N))))) (le_of_lt hh),
      mul_le_mul_of_nonneg_left
        (neg_abs_le (Real.log (2 * Real.sin ((k : ℝ) * (π / N))))) (le_of_lt hh),
      mul_le_mul_of_nonneg_left hfm (le_of_lt hh),
      mul_le_mul_of_nonneg_left hfk (le_of_lt hh)]
  · nlinarith [hup,
      mul_nonneg (le_of_lt hh)
        (abs_nonneg (Real.log (2 * Real.sin (π / N)))),
      mul_nonneg (le_of_lt hh) (Real.log_nonneg (by norm_num : (1:ℝ) ≤ 2))]

/-- **Saddle brick E5c-4a — one-cell extension step (sorry-free).** If the
    scaled Kashaev log-sum deviates from the Clausen primitive by at most `B`
    at index `k`, it deviates by at most `B + 2c` at `k + 1`, where
    `c = (π/N)(|f(π/N)| + log 2)`: the new summand is charged one `c` via
    E5c-2 and the new cell `[kπ/N, (k+1)π/N]` one `c` via the crude cell
    bound. Works anywhere in the mirror window (`k + 1 ≤ N − 1`) — this is
    the step that stitches the rising (E5c-1) and falling (E5c-3) halves
    across `π/2`. (bean qou-xqae) -/
theorem abs_deviation_succ {N k : ℕ} (hk : 1 ≤ k) (hk1N : k + 1 ≤ N - 1) {B : ℝ}
    (hB : |(π / N) * (∑ j ∈ Finset.Icc 1 k,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)| ≤ B) :
    |(π / N) * (∑ j ∈ Finset.Icc 1 (k + 1),
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - (-clausen (2 * (((k : ℝ) + 1) * (π / N))) / 2)|
      ≤ B + 2 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2)) := by
  have hpi := Real.pi_pos
  have hN3 : 3 ≤ N := by omega
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 1 ≤ N)
  have hh : (0 : ℝ) < π / N := by positivity
  have hfield : (N : ℝ) * (π / N) = π := by field_simp
  have hk' : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hk2N' : (k : ℝ) + 2 ≤ (N : ℝ) := by exact_mod_cast (by omega : k + 2 ≤ N)
  have h3N : (3 : ℝ) ≤ (N : ℝ) := by exact_mod_cast hN3
  have hhπ : π / N ≤ π / 2 := by gcongr <;> linarith
  rw [Finset.sum_Icc_succ_top (by omega : 1 ≤ k + 1)]
  push_cast
  -- the new summand, bounded by E5c-2 on the mirror window
  have hterm : |Real.log (2 * Real.sin (((k : ℝ) + 1) * (π / N)))|
      ≤ |Real.log (2 * Real.sin (π / N))| + Real.log 2 := by
    refine abs_log_two_sin_le hh hhπ
      (by nlinarith [mul_nonneg (by linarith : (0:ℝ) ≤ (k : ℝ)) (le_of_lt hh)]) ?_
    nlinarith [mul_le_mul_of_nonneg_right hk2N' (le_of_lt hh), hfield]
  -- the new cell, bounded crudely
  have hcell : |(-clausen (2 * (((k : ℝ) + 1) * (π / N))) / 2)
        - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)|
      ≤ (π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) := by
    have hcb := abs_integral_log_sin_cell_le hh hhπ
      (a := (k : ℝ) * (π / N)) (b := ((k : ℝ) + 1) * (π / N))
      (by nlinarith)
      (by nlinarith [mul_nonneg (by linarith : (0:ℝ) ≤ (k : ℝ) - 1) (le_of_lt hh)])
      (by nlinarith [mul_le_mul_of_nonneg_right hk2N' (le_of_lt hh), hfield])
    rw [integral_log_sin_window] at hcb
    calc |(-clausen (2 * (((k : ℝ) + 1) * (π / N))) / 2)
          - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)|
        ≤ (((k : ℝ) + 1) * (π / N) - (k : ℝ) * (π / N))
            * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) := hcb
      _ = (π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) := by ring
  rw [abs_le] at hB hterm hcell ⊢
  constructor
  · nlinarith [hB.1, hcell.2,
      mul_le_mul_of_nonneg_left hterm.1 (le_of_lt hh),
      mul_le_mul_of_nonneg_left hterm.2 (le_of_lt hh)]
  · nlinarith [hB.2, hcell.1,
      mul_le_mul_of_nonneg_left hterm.1 (le_of_lt hh),
      mul_le_mul_of_nonneg_left hterm.2 (le_of_lt hh)]

/-- **Saddle brick E5c-4 — the `π/2`-stitch: all-`k` uniform deviation
    (sorry-free).** For `N ≥ 4` and every `1 ≤ k ≤ N − 1`, the scaled Kashaev
    log-sum deviates from the Clausen primitive `F(kπ/N) = −clausen(2kπ/N)/2`
    by at most the k-INDEPENDENT master error
    `E(N) = |F(π/N)| + (π/N)|f(π/N)| + 7c`, `c = (π/N)(|f(π/N)| + log 2)`:
    the rising range `k + 1 ≤ ⌊N/2⌋` by E5c-1 (cost `E₁ = |F| + h|f| + c`),
    the two mid indices `k = ⌊N/2⌋, ⌊N/2⌋+1` straddling `π/2` by one E5c-4a
    step each (`+2c` per step), and the falling range `k ≥ ⌊N/2⌋+2` by gluing
    the prefix at `⌊N/2⌋+1` to E5c-3 (`+2c`). Every summand of `E(N)` tends
    to `0` as `N → ∞` — the E5c-5 brick. (bean qou-xqae) -/
theorem abs_deviation_le {N k : ℕ} (hN : 4 ≤ N) (hk : 1 ≤ k) (hkN : k ≤ N - 1) :
    |(π / N) * (∑ j ∈ Finset.Icc 1 k,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
        - (-clausen (2 * ((k : ℝ) * (π / N))) / 2)|
      ≤ |(-clausen (2 * (π / N)) / 2)|
        + (π / N) * |Real.log (2 * Real.sin (π / N))|
        + 7 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2)) := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by exact_mod_cast (by omega : 1 ≤ N)
  have hh : (0 : ℝ) < π / N := by positivity
  have hfield : (N : ℝ) * (π / N) = π := by field_simp
  have hc0 : 0 ≤ (π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2) :=
    mul_nonneg (le_of_lt hh)
      (add_nonneg (abs_nonneg _) (Real.log_nonneg (by norm_num)))
  -- the ℕ midpoint m₀ = ⌊N/2⌋: last index with m₀·π/N ≤ π/2
  set m₀ := N / 2 with hm₀def
  have hm₀2 : 2 ≤ m₀ := by omega
  have h2m₀N : 2 * m₀ ≤ N := by omega
  have hhalf_of : ∀ j : ℕ, 2 * j ≤ N → (j : ℝ) * (π / N) ≤ π / 2 := by
    intro j hj
    have hj' : ((2 * j : ℕ) : ℝ) ≤ (N : ℝ) := by exact_mod_cast hj
    push_cast at hj'
    nlinarith [mul_le_mul_of_nonneg_right hj' (le_of_lt hh), hfield]
  -- deviation at m₀: one E5c-4a step from the rising bound at m₀ − 1
  have hdev_m₀ : |(π / N) * (∑ j ∈ Finset.Icc 1 m₀,
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      - (-clausen (2 * ((m₀ : ℝ) * (π / N))) / 2)|
      ≤ |(-clausen (2 * (π / N)) / 2)|
        + (π / N) * |Real.log (2 * Real.sin (π / N))|
        + 3 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2)) := by
    have hcast : ((m₀ - 1 : ℕ) : ℝ) + 1 = (m₀ : ℝ) := by
      rw [Nat.cast_sub (by omega : 1 ≤ m₀), Nat.cast_one]
      ring
    have hhalf : (((m₀ - 1 : ℕ) : ℝ) + 1) * (π / N) ≤ π / 2 := by
      rw [hcast]
      exact hhalf_of m₀ h2m₀N
    have hrise := abs_rising_deviation_le (N := N) (k := m₀ - 1)
      (by omega : 1 ≤ N) (by omega : 1 ≤ m₀ - 1) hhalf
    have hstep := abs_deviation_succ (N := N) (k := m₀ - 1)
      (by omega : 1 ≤ m₀ - 1) (by omega : (m₀ - 1) + 1 ≤ N - 1) hrise
    have hidx : m₀ - 1 + 1 = m₀ := by omega
    rw [hidx, hcast] at hstep
    linarith [hstep]
  -- deviation at m₀ + 1: a second E5c-4a step
  have hdev_m₀1 : |(π / N) * (∑ j ∈ Finset.Icc 1 (m₀ + 1),
        Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
      - (-clausen (2 * (((m₀ : ℝ) + 1) * (π / N))) / 2)|
      ≤ |(-clausen (2 * (π / N)) / 2)|
        + (π / N) * |Real.log (2 * Real.sin (π / N))|
        + 5 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2)) := by
    have hstep := abs_deviation_succ (N := N) (k := m₀)
      (by omega : 1 ≤ m₀) (by omega : m₀ + 1 ≤ N - 1) hdev_m₀
    linarith [hstep]
  rcases le_or_lt (k + 1) m₀ with hA | hA
  · -- rising range: E5c-1 directly
    have hhalf : ((k : ℝ) + 1) * (π / N) ≤ π / 2 := by
      have h := hhalf_of (k + 1) (by omega)
      push_cast at h
      linarith [h]
    have hb := abs_rising_deviation_le (by omega : 1 ≤ N) hk hhalf
    linarith [hb, hc0]
  · have hm₀k : m₀ ≤ k := by omega
    rcases eq_or_lt_of_le hm₀k with heq | hgt
    · -- k = m₀
      rw [← heq]
      linarith [hdev_m₀, hc0]
    · have hm₀1k : m₀ + 1 ≤ k := by omega
      rcases eq_or_lt_of_le hm₀1k with heq1 | hgt2
      · -- k = m₀ + 1
        rw [← heq1]
        push_cast
        linarith [hdev_m₀1, hc0]
      · -- k ≥ m₀ + 2: glue the prefix at m₀ + 1 to the falling tail (E5c-3)
        have hlo : π / 2 ≤ ((m₀ + 1 : ℕ) : ℝ) * (π / N) := by
          have hNle : (N : ℝ) ≤ 2 * ((m₀ + 1 : ℕ) : ℝ) := by
            exact_mod_cast (by omega : N ≤ 2 * (m₀ + 1))
          nlinarith [mul_le_mul_of_nonneg_right hNle (le_of_lt hh), hfield]
        have hfall := abs_falling_deviation_le (N := N) (m := m₀ + 1) (k := k)
          (by omega : 1 ≤ N) (by omega : m₀ + 1 ≤ k) hlo hkN
        have hcast : ((m₀ + 1 : ℕ) : ℝ) = (m₀ : ℝ) + 1 := by push_cast; ring
        rw [hcast] at hfall
        have hsplit : (∑ j ∈ Finset.Icc 1 k,
              Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
            = (∑ j ∈ Finset.Icc 1 (m₀ + 1),
                Real.log (2 * Real.sin ((j : ℝ) * (π / N))))
              + ∑ j ∈ Finset.Icc (m₀ + 1 + 1) k,
                  Real.log (2 * Real.sin ((j : ℝ) * (π / N))) := by
          rw [← Nat.Ico_succ_right 1 k, ← Nat.Ico_succ_right 1 (m₀ + 1),
            ← Nat.Ico_succ_right (m₀ + 1 + 1) k]
          exact (Finset.sum_Ico_consecutive _
            (by omega : 1 ≤ m₀ + 1 + 1) (by omega : m₀ + 1 + 1 ≤ k + 1)).symm
        rw [hsplit, mul_add]
        set S₁ := ∑ j ∈ Finset.Icc 1 (m₀ + 1),
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))) with hS₁
        set S₂ := ∑ j ∈ Finset.Icc (m₀ + 1 + 1) k,
          Real.log (2 * Real.sin ((j : ℝ) * (π / N))) with hS₂
        set F₁ := -clausen (2 * (((m₀ : ℝ) + 1) * (π / N))) / 2 with hF₁
        set Fk := -clausen (2 * ((k : ℝ) * (π / N))) / 2 with hFk
        calc |(π / N) * S₁ + (π / N) * S₂ - Fk|
            = |((π / N) * S₁ - F₁) + ((π / N) * S₂ - (Fk - F₁))| := by
              congr 1
              ring
          _ ≤ |(π / N) * S₁ - F₁| + |(π / N) * S₂ - (Fk - F₁)| := abs_add_le _ _
          _ ≤ _ := add_le_add hdev_m₀1 hfall
          _ ≤ _ := by linarith [hc0]

/-- **Saddle brick E5c-5 — the master error vanishes (sorry-free).** The
    k-independent E5c-4 master error
    `E(N) = |F(π/N)| + (π/N)|f(π/N)| + 7·(π/N)(|f(π/N)| + log 2)` tends to
    `0` as `N → ∞`: the Clausen-primitive term by continuity of `clausen` at
    `0` (the E4d-1 route), the first-grid term by E4d-2, and the `log 2` cell
    term by `π/N → 0`. Together with E5c-4 this squeezes the scaled Kashaev
    log-sum onto the Clausen primitive uniformly in `k`. (bean qou-2cmk) -/
theorem tendsto_master_error :
    Filter.Tendsto (fun N : ℕ =>
      |(-clausen (2 * (π / N)) / 2)|
        + (π / N) * |Real.log (2 * Real.sin (π / N))|
        + 7 * ((π / N) * (|Real.log (2 * Real.sin (π / N))| + Real.log 2)))
      Filter.atTop (nhds 0) := by
  -- the Clausen-primitive term |F(π/N)| → 0
  have hdiv : Filter.Tendsto (fun N : ℕ => 2 * π / N) Filter.atTop (nhds 0) :=
    tendsto_const_div_atTop_nhds_zero_nat (2 * π)
  have hcl : Filter.Tendsto (fun N : ℕ => clausen (2 * (π / N)))
      Filter.atTop (nhds 0) := by
    have hcomp := (continuous_clausen.tendsto 0).comp
      (by simpa [mul_div_assoc] using hdiv)
    simpa [clausen_zero, Function.comp_def, mul_div_assoc] using hcomp
  have h1 : Filter.Tendsto (fun N : ℕ => |(-clausen (2 * (π / N)) / 2)|)
      Filter.atTop (nhds 0) := by
    have := ((hcl.neg).div_const 2).abs
    simpa using this
  -- the first-grid term (π/N)·|f(π/N)| → 0 (E4d-2 + abs)
  have h2 : Filter.Tendsto
      (fun N : ℕ => (π / N) * |Real.log (2 * Real.sin (π / N))|)
      Filter.atTop (nhds 0) := by
    have habs := tendsto_first_term.abs
    rw [abs_zero] at habs
    refine habs.congr (fun N => ?_)
    rw [abs_mul, abs_of_nonneg (by positivity : (0:ℝ) ≤ π / N)]
  -- the log 2 cell term (π/N)·log 2 → 0
  have h3 : Filter.Tendsto (fun N : ℕ => (π / N) * Real.log 2)
      Filter.atTop (nhds 0) := by
    have := (tendsto_const_div_atTop_nhds_zero_nat π).mul_const (Real.log 2)
    simpa using this
  have hsum := (h1.add h2).add ((h2.add h3).const_mul 7)
  norm_num at hsum
  refine hsum.congr (fun N => ?_)
  ring

/-- **Borromean brick B1 — the Clausen duplication formula (sorry-free).**
    `clausen(2θ) = 2·clausen(θ) − 2·clausen(π − θ)` on `(0, π)`: both sides
    have derivative `−2·log(2 sin θ)` (the sine duplication
    `2 sin θ = (2 sin(θ/2))·(2 sin((π−θ)/2))`), and agree at `θ = π/2`
    (`clausen π = 0`). Closes the functional-equation gap the Clausen filler
    listed as requiring Fourier infrastructure; needed by the Borromean
    squeeze to evaluate the continuum functional at `x = 3/4` as
    `8·Cl₂(π/2)`. (bean qou-jor3) -/
theorem clausen_duplication {θ : ℝ} (h0 : 0 < θ) (hπ : θ < π) :
    clausen (2 * θ) = 2 * clausen θ - 2 * clausen (π - θ) := by
  have hpi := Real.pi_pos
  have hf : ∀ t ∈ Set.Ioo (0:ℝ) π, HasDerivAt (fun t => clausen (2 * t))
      (-Real.log (2 * Real.sin (2 * t / 2)) * 2) t := by
    intro t ht
    have h1 := hasDerivAt_clausen (θ := 2 * t)
      (by linarith [ht.1]) (by linarith [ht.2])
    have h2 : HasDerivAt (fun t : ℝ => 2 * t) 2 t := by
      simpa using (hasDerivAt_id t).const_mul 2
    exact h1.comp t h2
  have hg : ∀ t ∈ Set.Ioo (0:ℝ) π, HasDerivAt
      (fun t => 2 * clausen t - 2 * clausen (π - t))
      (2 * -Real.log (2 * Real.sin (t / 2))
        - 2 * (-Real.log (2 * Real.sin ((π - t) / 2)) * -1)) t := by
    intro t ht
    have h1 := (hasDerivAt_clausen (θ := t) ht.1
      (by linarith [ht.2])).const_mul 2
    have hsub : HasDerivAt (fun t : ℝ => π - t) (-1) t := by
      simpa using (hasDerivAt_id t).const_sub π
    have h2 := ((hasDerivAt_clausen (θ := π - t)
      (by linarith [ht.2]) (by linarith [ht.1])).comp t hsub).const_mul 2
    exact h1.sub h2
  have key : Set.EqOn (fun t => clausen (2 * t))
      (fun t => 2 * clausen t - 2 * clausen (π - t)) (Set.Ioo (0:ℝ) π) := by
    have hmid : (π / 2 : ℝ) ∈ Set.Ioo (0:ℝ) π := ⟨by linarith, by linarith⟩
    refine isOpen_Ioo.eqOn_of_deriv_eq isPreconnected_Ioo
      (fun t ht => (hf t ht).differentiableAt.differentiableWithinAt)
      (fun t ht => (hg t ht).differentiableAt.differentiableWithinAt)
      (fun t ht => ?_) hmid ?_
    · rw [(hf t ht).deriv, (hg t ht).deriv]
      have hs1 : 0 < Real.sin (t / 2) :=
        Real.sin_pos_of_pos_of_lt_pi (by linarith [ht.1]) (by linarith [ht.2])
      have hs2 : 0 < Real.sin ((π - t) / 2) :=
        Real.sin_pos_of_pos_of_lt_pi (by linarith [ht.2]) (by linarith [ht.1])
      have hprod : (2 * Real.sin (t / 2)) * (2 * Real.sin ((π - t) / 2))
          = 2 * Real.sin (2 * t / 2) := by
        have hc : Real.sin ((π - t) / 2) = Real.cos (t / 2) := by
          rw [show (π - t) / 2 = π / 2 - t / 2 by ring, Real.sin_pi_div_two_sub]
        have hd := Real.sin_two_mul (t / 2)
        rw [hc, show (2:ℝ) * t / 2 = 2 * (t / 2) by ring, hd]
        ring
      have hlm : Real.log (2 * Real.sin (2 * t / 2))
          = Real.log (2 * Real.sin (t / 2))
            + Real.log (2 * Real.sin ((π - t) / 2)) := by
        rw [← hprod]
        exact Real.log_mul (mul_pos two_pos hs1).ne' (mul_pos two_pos hs2).ne'
      rw [hlm]
      ring
    · show clausen (2 * (π / 2)) = 2 * clausen (π / 2) - 2 * clausen (π - π / 2)
      rw [show 2 * (π / 2 : ℝ) = π by ring, clausen_pi,
        show π - π / 2 = π / 2 by ring]
      ring
  exact key ⟨h0, hπ⟩

/-- **B1, series side (sorry-free).** `Cl₂(2θ) = 2·Cl₂(θ) − 2·Cl₂(π − θ)` on
    `(0, π)`, via the series↔integral bridge. -/
theorem Cl_2_duplication {θ : ℝ} (h0 : 0 < θ) (hπ : θ < π) :
    QOU.Archimedean.Cl_2 (2 * θ)
      = 2 * QOU.Archimedean.Cl_2 θ - 2 * QOU.Archimedean.Cl_2 (π - θ) := by
  have hpi := Real.pi_pos
  have h1 := clausen_duplication h0 hπ
  rw [clausen_eq_series (θ := 2 * θ) ⟨by linarith, by linarith⟩,
    clausen_eq_series (θ := θ) ⟨h0, by linarith⟩,
    clausen_eq_series (θ := π - θ) ⟨by linarith, by linarith⟩] at h1
  exact h1

/-- **The series Clausen's derivative** `Cl_2'(θ) = -log(2 sin(θ/2))` for
    `θ ∈ (0, 2π)` — the derivative the filler flagged as needing Fourier
    infrastructure, now machine-proved (`hasDerivAt_Cl_2_series`). Dual-purpose: `V'(θ)` of
    `rem:dilog-saddle-regime`, zero at the `θ = π/3` saddle. -/
theorem hasDerivAt_cl_2 {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    HasDerivAt QOU.Archimedean.Cl_2 (-Real.log (2 * Real.sin (θ / 2))) θ :=
  hasDerivAt_Cl_2_series h0 h2

end QOU.Knot
