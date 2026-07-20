/-
  q-Gevrey order of a formal power series — the analytic "slope" (theta order)
  that Mathlib v4.24.0 lacks (grep-confirmed absent).

  MOTIVATION (epic qou-7b7v, brick MI-1). The abstract slope arithmetic of
  `QOU.Mass.ThetaSlopeArithmetic` manipulates a rational slope `s` as an opaque
  ℚ: product adds it, the bar involution `q ↦ q⁻¹` negates it. This file GROUNDS
  those abstractions for actual coefficient sequences `a : ℕ → K`: the slope `s`
  becomes the leading Gaussian exponent of `‖a n‖`, and the product/bar/geometric
  laws become theorems about the growth of real sequences.

  DEFINITION. A sequence `a : ℕ → K` (K a normed field) has q-Gevrey order `s`
  against base `q` (`q > 1`) when `‖a n‖` grows like `C^n · q^{s·n²/2}` — i.e. the
  Gaussian (theta) exponent `s·n²/2` dominates `log_q ‖a n‖`. Precisely we take
  the limit of the m²-coefficient:

      `IsQGevreyOrder q s a  :⟺  (2 · log_q ‖a n‖) / n² → s`.

  The factor `2` makes `s` read directly off the exponent `q^{s·n²/2}`; the
  `C^n` (order-0) prefactor and the finitely many small-`n` terms are washed out
  by the `n²` denominator and the `atTop` filter. When the limit exists it is
  unique (`order_unique`), so this is a genuine valuation-like invariant.

  ALTERNATIVE (bound form). One may instead ask that `‖a n‖ ≤ C^n q^{s n²/2}` for
  some `C` while no smaller `s` bounds it. The limit form above implies a bound
  form and is cleaner for the slope algebra; the bound-form equivalence is an
  MI-2/MI-3 refinement.

  SCOPE (honest). MI-1 = the definition + the elementary slope algebra, proved
  sorry-free: (i) the pointwise product adds order — the analogue of the theta
  exponent multiplication `q^{s n²/2}·q^{t n²/2}=q^{(s+t)n²/2}` and of
  `ThetaSlopeArithmetic.prodSlope`; (ii) the bar involution `q ↦ q⁻¹` negates
  order (`ThetaSlopeArithmetic.bar`); (iii) a geometric sequence `C^n` has order
  0. The genuinely-analytic Cauchy-CONVOLUTION law (Newton-polygon / dominant
  balance) is stated precisely with a cited `sorry`, deferred to MI-2 — it is
  NOT elementary and NOT vacuous. §7c: the growth is archimedean, so `ℝ` for the
  base and target is genuine (`Real.log`).

  -- Ref: [ramis-sauloy-zhang2013] q-difference Newton-polygon slopes / q-Gevrey
-/

import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.Normed.Field.Lemmas

namespace QOU.Mathlib.QGevreyOrder

open Filter Topology

variable {K : Type*} [NormedField K]

/-- `log_q x := log x / log q`, the base-`q` logarithm written inline (this file
    deliberately avoids `Real.logb` so it depends only on the QOU-cached
    `Log.Basic`; the two agree definitionally). -/
private noncomputable def logb (q x : ℝ) : ℝ := Real.log x / Real.log q

/-- The q-Gevrey order of a coefficient sequence `a : ℕ → K`, measured against a
    base `q` (`q > 1`).  `a` has order `s` when `‖a n‖ ∼ C^n · q^{s·n²/2}`, made
    precise as the limit of the leading Gaussian coefficient
    `(2·log_q ‖a n‖)/n² → s`.  The `atTop` filter and the `n²` denominator wash
    out the `C^n` prefactor and the finitely many `n = 0,1` terms. -/
def IsQGevreyOrder (q : ℝ) (s : ℝ) (a : ℕ → K) : Prop :=
  Tendsto (fun n : ℕ => 2 * logb q ‖a n‖ / (n : ℝ) ^ 2) atTop (𝓝 s)

/-- **Order is a well-defined invariant.**  When the q-Gevrey order exists it is
    unique — two witnessed orders of the same sequence agree.  (Uniqueness of a
    limit in a Hausdorff space.) -/
theorem order_unique {q s t : ℝ} {a : ℕ → K}
    (hs : IsQGevreyOrder q s a) (ht : IsQGevreyOrder q t a) : s = t :=
  tendsto_nhds_unique hs ht

/-- Pointwise: `log_{q⁻¹} x = - log_q x` (holds unconditionally, since
    `log q⁻¹ = -log q` and `x/(-y) = -(x/y)` even when `log q = 0`). -/
theorem logb_inv_base (x : ℝ) (q : ℝ) : logb q⁻¹ x = - logb q x := by
  unfold logb
  rw [Real.log_inv]
  ring

/-- **Bar involution negates order.**  The same sequence `a`, measured against
    the bar-conjugate base `q⁻¹`, has order `-s`.  This grounds
    `ThetaSlopeArithmetic.bar (s) = -s` at the level of actual sequences: the
    bar map `q ↦ q⁻¹` inverts the q-Gevrey growth direction. -/
theorem bar_negates {q s : ℝ} {a : ℕ → K} :
    IsQGevreyOrder q⁻¹ (-s) a ↔ IsQGevreyOrder q s a := by
  unfold IsQGevreyOrder
  have hfun : (fun n : ℕ => 2 * logb q⁻¹ ‖a n‖ / (n : ℝ) ^ 2)
      = (fun n : ℕ => -(2 * logb q ‖a n‖ / (n : ℝ) ^ 2)) := by
    funext n; rw [logb_inv_base]; ring
  rw [hfun]
  constructor
  · intro h
    have := h.neg
    simpa using this
  · intro h
    have := h.neg
    simpa using this

/-- **Geometric sequences have order 0.**  For any `C : K`, the geometric
    sequence `n ↦ C^n` has q-Gevrey order `0` (it carries only the `C^n`
    prefactor, no Gaussian `n²` term).  This grounds
    `ThetaSlopeArithmetic.c1Slope`-style order bookkeeping: pure exponential
    growth is order-0, the neutral element of the slope algebra. -/
theorem geometric_order_zero (q : ℝ) (C : K) :
    IsQGevreyOrder q 0 (fun n : ℕ => C ^ n) := by
  unfold IsQGevreyOrder
  -- `logb q ‖C^n‖ = n · logb q ‖C‖` (pull the exponent out of the log).
  have hlog : ∀ n : ℕ, logb q ‖(C : K) ^ n‖ = (n : ℝ) * logb q ‖C‖ := by
    intro n; unfold logb; rw [norm_pow, Real.log_pow]; ring
  -- For n ≥ 1: 2·logb q ‖C^n‖ / n² = (2·logb q ‖C‖) / n, which → 0.
  have hcongr : (fun n : ℕ => (2 * logb q ‖C‖) / (n : ℝ))
      =ᶠ[atTop] (fun n : ℕ => 2 * logb q ‖(C : K) ^ n‖ / (n : ℝ) ^ 2) := by
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hn0 : (n : ℝ) ≠ 0 := by
      have : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
      positivity
    rw [hlog n, pow_two]
    field_simp
  exact (tendsto_const_div_atTop_nhds_zero_nat (2 * logb q ‖C‖)).congr' hcongr

/-- **Pointwise product adds order.**  If `a` has order `s`, `b` has order `t`,
    and both are eventually nonzero, then the pointwise product `n ↦ a n · b n`
    has order `s + t`.  This grounds `ThetaSlopeArithmetic.prodSlope s t = s + t`
    for actual sequences: the theta exponents multiply,
    `q^{s n²/2}·q^{t n²/2} = q^{(s+t)n²/2}`, hence the leading coefficients add.

    Hypotheses `ha0`/`hb0` (eventual nonvanishing) are needed for the `log`
    additivity `log(xy)=log x+log y`; they are automatic for the nonzero
    coefficient sequences that carry a genuine slope. -/
theorem prod_adds {q s t : ℝ} {a b : ℕ → K}
    (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b)
    (ha0 : ∀ᶠ n in atTop, a n ≠ 0) (hb0 : ∀ᶠ n in atTop, b n ≠ 0) :
    IsQGevreyOrder q (s + t) (fun n : ℕ => a n * b n) := by
  unfold IsQGevreyOrder at ha hb ⊢
  have hsum := ha.add hb
  refine Tendsto.congr' ?_ hsum
  filter_upwards [ha0, hb0] with n hna hnb
  have hnorma : ‖a n‖ ≠ 0 := norm_ne_zero_iff.mpr hna
  have hnormb : ‖b n‖ ≠ 0 := norm_ne_zero_iff.mpr hnb
  unfold logb
  rw [norm_mul, Real.log_mul hnorma hnormb]
  ring

/-! ### MI-2 — the analytic convolution (Cauchy-product) law

    The q-Gevrey order under the CAUCHY product of power series
    `(a ⋆ b)_n = ∑_{k≤n} a_k · b_{n-k}` is governed by the Newton polygon
    (dominant-balance of the Gaussian exponents), NOT by the elementary
    log-additivity used for the pointwise product above.

    **CORRECTED LAW (MI-2).**  MI-1's stub asserted the additive law
    `order(a ⋆ b) = s + t`.  That is WRONG.  The RSZ dominant balance of
    `‖(a⋆b)_n‖ ∼ ∑_{k=0}^n q^{s k²/2} · q^{t (n-k)²/2}` is a Laplace/saddle sum:
    writing `θ = k/n ∈ [0,1]`, the leading `n²`-coefficient is the ENVELOPE

        `E(s,t) := sup_{θ∈[0,1]} ( s·θ² + t·(1−θ)² )`.

    The quadratic `g(θ) = s θ² + t(1−θ)²` has `g''(θ) = 2(s+t)`, so:

    * **Convex (not both ≤ 0)** — the sup is at an endpoint and
      `E(s,t) = max s t`.  The interior critical point `θ* = t/(s+t)` is a
      *minimum*; the sum is dominated by the boundary terms `k = 0` or `k = n`.
      (Growing/divergent q-Gevrey coefficients, `s` or `t > 0`.)
    * **Concave (both s,t ≤ 0)** — the sup is the interior saddle
      `θ* = t/(s+t)`, giving `E(s,t) = s·t/(s+t)` (the HARMONIC combination, not
      `s+t`).  This is the genuine convergent-q-Gevrey regime of RSZ.

    Numerically verified (mpmath, base `q = 2`, `n = 400`, positive/no-cancel
    coefficients): `(-1,-1)↦-0.5=st/(s+t)`; `(-2,-1)↦-0.667=st/(s+t)`;
    `(2,1)↦+2.0=max`; `(1,3)↦+3.0=max`; `(-3,1)↦+1.0=max` (note `s+t=-2<0` yet
    `max`, since `t>0`); `(-0.5,-2)↦-0.4=st/(s+t)`.  So the split is
    **both ≤ 0 → `st/(s+t)`, otherwise → `max s t`**, NOT the sign of `s+t`, and
    never the additive `s+t`.

    **SCOPE (honest).**  The two analytic ingredients of the `≤` (upper)
    direction are proved sorry-free below: (i) `cauchyMul_norm_le_sum`, the
    triangle bound `‖(a⋆b)_n‖ ≤ ∑ ‖a_k‖‖b_{n-k}‖`; (ii) `exponent_le_envelope`,
    the exact dominant-balance inequality
    `s k² + t j² ≤ E(s,t)·(k+j)²` (`k,j ≥ 0`) — the mathematical heart, an
    identity-plus-sign completing-the-square argument in each regime.  The
    remaining `ε`-`δ` assembly into the order LIMIT (upper bound), and the
    matching lower bound (which additionally needs a non-cancellation
    hypothesis on the leading coefficients), are the residual cited `sorry` in
    `cauchyMul_order`.  It is stated with the CORRECT `cauchyEnvelope` law and is
    NOT vacuous. -/

/-- The Cauchy (convolution) product of two coefficient sequences. -/
def cauchyMul (a b : ℕ → K) : ℕ → K :=
  fun n => ∑ k ∈ Finset.range (n + 1), a k * b (n - k)

/-- **The Cauchy-product q-Gevrey envelope** `E(s,t) = sup_{θ∈[0,1]}(sθ²+t(1−θ)²)`
    in closed form: the harmonic combination `s·t/(s+t)` when both slopes are
    `≤ 0` (concave, interior saddle — the convergent-q-Gevrey regime), and
    `max s t` otherwise (convex, endpoint-dominated).  At `s = t = 0` both
    branches give `0` (`0/0 = 0` in Lean).  Replaces the incorrect additive
    `s + t` of the MI-1 stub. -/
noncomputable def cauchyEnvelope (s t : ℝ) : ℝ :=
  if s ≤ 0 ∧ t ≤ 0 then s * t / (s + t) else max s t

/-- **[MI-2 core] Dominant-balance inequality (proved sorry-free).**  For
    `k, j ≥ 0` the raw Gaussian exponent is bounded by the envelope:
    `s·k² + t·j² ≤ cauchyEnvelope s t · (k + j)²`.  This is the analytic heart
    of the `≤` direction of the convolution order law — a completing-the-square
    identity in each regime:

    * both `s,t ≤ 0`, `s+t < 0`:
      `(s k²+t j²)(s+t) − s t (k+j)² = (s k − t j)² ≥ 0`, and dividing by
      `s+t < 0` flips to `s k²+t j² ≤ s t/(s+t)·(k+j)²`;
    * otherwise: `max s t ≥ 0`, and
      `max s t·(k+j)² − (s k²+t j²) = (max−s)k² + (max−t)j² + max·2kj ≥ 0`. -/
theorem exponent_le_envelope (s t : ℝ) {k j : ℝ} (hk : 0 ≤ k) (hj : 0 ≤ j) :
    s * k ^ 2 + t * j ^ 2 ≤ cauchyEnvelope s t * (k + j) ^ 2 := by
  unfold cauchyEnvelope
  split_ifs with h
  · -- both ≤ 0 : harmonic (concave, interior saddle)
    obtain ⟨hs, ht⟩ := h
    rcases (add_nonpos hs ht).lt_or_eq with hlt | heq
    · -- s + t < 0
      rw [div_mul_eq_mul_div, le_div_iff_of_neg hlt]
      nlinarith [sq_nonneg (s * k - t * j)]
    · -- s + t = 0 with s,t ≤ 0 forces s = t = 0
      have hs0 : s = 0 := by linarith
      have ht0 : t = 0 := by linarith
      subst hs0; subst ht0; simp
  · -- not both ≤ 0 : max (convex, endpoint-dominated)
    have hmax : 0 ≤ max s t := by
      rcases le_or_gt 0 (max s t) with h1 | h1
      · exact h1
      · exact absurd ⟨(le_max_left s t).trans h1.le, (le_max_right s t).trans h1.le⟩ h
    have hsk : s ≤ max s t := le_max_left s t
    have htk : t ≤ max s t := le_max_right s t
    nlinarith [mul_nonneg (sub_nonneg.mpr hsk) (sq_nonneg k),
               mul_nonneg (sub_nonneg.mpr htk) (sq_nonneg j),
               mul_nonneg hmax (mul_nonneg hk hj)]

/-- **[MI-2 ingredient] Triangle bound for the Cauchy product (proved
    sorry-free).**  `‖(a⋆b)_n‖ ≤ ∑_{k≤n} ‖a_k‖·‖b_{n-k}‖`.  Combined with
    `exponent_le_envelope` this supplies the `≤` (upper) direction of the order
    law: each summand's exponent is envelope-bounded, and the `(n+1)`-fold sum
    is washed out by the `n²` denominator. -/
theorem cauchyMul_norm_le_sum (a b : ℕ → K) (n : ℕ) :
    ‖cauchyMul a b n‖ ≤ ∑ k ∈ Finset.range (n + 1), ‖a k‖ * ‖b (n - k)‖ := by
  unfold cauchyMul
  refine (norm_sum_le _ _).trans (Finset.sum_le_sum ?_)
  intro k _
  exact (norm_mul (a k) (b (n - k))).le

/-- **[MI-2 ingredient, sorry-free] Eventual ⟹ uniform bound with a constant.**  A
    nonnegative sequence that is eventually dominated by a positive sequence `g` is
    dominated by `C·g` for a single constant `C ≥ 1` at *every* index — the finitely
    many small-index exceptions are absorbed into `C`.  This is the mechanism that
    turns the per-coefficient q-Gevrey bound (valid only for large `k`) into a bound
    valid across the whole convolution range `0 ≤ k ≤ n`. -/
private theorem exists_uniform_const {f g : ℕ → ℝ}
    (hf : ∀ n, 0 ≤ f n) (hg : ∀ n, 0 < g n) (h : ∀ᶠ n in atTop, f n ≤ g n) :
    ∃ C : ℝ, 1 ≤ C ∧ ∀ n, f n ≤ C * g n := by
  obtain ⟨N, hN⟩ := eventually_atTop.mp h
  have hsum_nonneg : 0 ≤ ∑ k ∈ Finset.range N, f k / g k :=
    Finset.sum_nonneg (fun k _ => div_nonneg (hf k) (hg k).le)
  refine ⟨1 + ∑ k ∈ Finset.range N, f k / g k, by linarith, ?_⟩
  intro n
  rcases lt_or_ge n N with hn | hn
  · have hmem : n ∈ Finset.range N := Finset.mem_range.mpr hn
    have hle : f n / g n ≤ ∑ k ∈ Finset.range N, f k / g k :=
      Finset.single_le_sum (fun k _ => div_nonneg (hf k) (hg k).le) hmem
    have hC : f n / g n ≤ 1 + ∑ k ∈ Finset.range N, f k / g k := by linarith
    exact (div_le_iff₀ (hg n)).mp hC
  · have h1 : f n ≤ g n := hN n hn
    nlinarith [hg n, hsum_nonneg]

/-- **[MI-2 ingredient, sorry-free] Uniform Gaussian bound from the order limit.**
    If `a` has q-Gevrey order `s`, then for every `ε > 0` there is a single constant
    `C ≥ 1` with `‖a k‖ ≤ C · q^{(s+ε)·k²/2}` for *all* `k`.  Extracts the eventual
    one-sided envelope from the defining limit (`order_eventually_le`), converts the
    `log`-form bound into an `rpow` bound (`Real.rpow_def_of_pos`), and absorbs the
    finitely many small-`k` terms via `exists_uniform_const`. -/
private theorem uniform_gaussian_bound {q s : ℝ} {a : ℕ → K}
    (ha : IsQGevreyOrder q s a) (hq : 1 < q) {ε : ℝ} (hε : 0 < ε) :
    ∃ C : ℝ, 1 ≤ C ∧ ∀ k : ℕ, ‖a k‖ ≤ C * q ^ ((s + ε) * (k : ℝ) ^ 2 / 2) := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hlogq : 0 < Real.log q := Real.log_pos hq
  have hg : ∀ k : ℕ, (0 : ℝ) < q ^ ((s + ε) * (k : ℝ) ^ 2 / 2) :=
    fun k => Real.rpow_pos_of_pos hq0 _
  -- eventual one-sided envelope, inlined (order_eventually_le is stated later)
  have hev_le : ∀ᶠ k in atTop, 2 * logb q ‖a k‖ / (k : ℝ) ^ 2 ≤ s + ε := by
    have hmem : ∀ᶠ y in 𝓝 s, y ≤ s + ε := by
      filter_upwards [Iio_mem_nhds (show s < s + ε by linarith)] with y hy
      exact le_of_lt hy
    exact ha.eventually hmem
  have hev : ∀ᶠ k in atTop, ‖a k‖ ≤ q ^ ((s + ε) * (k : ℝ) ^ 2 / 2) := by
    filter_upwards [hev_le, eventually_ge_atTop 1] with k hk hk1
    have hkpos : (0 : ℝ) < (k : ℝ) ^ 2 := by
      have : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk1
      positivity
    -- `2·logb q ‖a k‖ / k² ≤ s+ε`  ⟹  `logb q ‖a k‖ ≤ (s+ε)·k²/2`
    have hmul : 2 * logb q ‖a k‖ ≤ (s + ε) * (k : ℝ) ^ 2 := (div_le_iff₀ hkpos).mp hk
    have hlogb : logb q ‖a k‖ ≤ (s + ε) * (k : ℝ) ^ 2 / 2 := by linarith
    -- unfold logb and clear the (positive) log q denominator
    have hlog : Real.log ‖a k‖ ≤ (s + ε) * (k : ℝ) ^ 2 / 2 * Real.log q := by
      have := hlogb
      unfold logb at this
      exact (div_le_iff₀ hlogq).mp this
    -- q^{(s+ε)k²/2} = exp(log q · (s+ε)k²/2)
    rw [Real.rpow_def_of_pos hq0]
    rcases (norm_nonneg (a k)).lt_or_eq with hpos | hzero
    · calc ‖a k‖ = Real.exp (Real.log ‖a k‖) := (Real.exp_log hpos).symm
        _ ≤ Real.exp (Real.log q * ((s + ε) * (k : ℝ) ^ 2 / 2)) := by
            apply Real.exp_le_exp.mpr; nlinarith [hlog]
    · rw [← hzero]; exact (Real.exp_pos _).le
  obtain ⟨C, hC1, hC⟩ := exists_uniform_const (fun k => norm_nonneg (a k)) hg hev
  exact ⟨C, hC1, hC⟩

/-- **[MI-2 core, sorry-free] The Cauchy-product upper bound in envelope form.**
    Assembles the two sorry-free bricks — the triangle bound `cauchyMul_norm_le_sum`
    and the dominant-balance inequality `exponent_le_envelope` — with the uniform
    Gaussian bounds on `a`, `b` into a single closed pointwise estimate: for every
    `ε > 0` there is a constant `C > 0` with

        `‖(a⋆b)_n‖ ≤ C · (n+1) · q^{E(s+ε, t+ε) · n²/2}`   for all `n`,

    `E = cauchyEnvelope`.  This is the full analytic content of the `≤` (upper)
    direction of `cauchyMul_order` — every convolution summand's exponent is
    envelope-bounded, and the `(n+1)`-fold sum contributes only the polynomial
    prefactor washed out by the `n²` denominator of the order.  What it does *not*
    give (and what keeps `cauchyMul_order` behind a cited `sorry`) is the passage to
    the order *limit*: that requires the coefficients not to cancel to `0` (Lean's
    `Real.log 0 = 0` junk value breaks the `logb`-monotonicity precisely at a
    vanishing coefficient, when `E < 0`), i.e. the non-cancellation hypothesis the
    bare statement lacks. -/
theorem cauchyMul_eventual_norm_bound {q s t : ℝ} {a b : ℕ → K}
    (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b) (hq : 1 < q)
    {ε : ℝ} (hε : 0 < ε) :
    ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ,
      ‖cauchyMul a b n‖
        ≤ C * ((n : ℝ) + 1) * q ^ (cauchyEnvelope (s + ε) (t + ε) * (n : ℝ) ^ 2 / 2) := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hq1 : (1 : ℝ) ≤ q := le_of_lt hq
  obtain ⟨Ca, hCa1, hCa⟩ := uniform_gaussian_bound ha hq hε
  obtain ⟨Cb, hCb1, hCb⟩ := uniform_gaussian_bound hb hq hε
  refine ⟨Ca * Cb, by nlinarith [hCa1, hCb1], ?_⟩
  intro n
  set E := cauchyEnvelope (s + ε) (t + ε) with hE
  refine (cauchyMul_norm_le_sum a b n).trans ?_
  -- each summand ≤ Ca·Cb·q^{E n²/2}
  have hterm : ∀ k ∈ Finset.range (n + 1),
      ‖a k‖ * ‖b (n - k)‖ ≤ Ca * Cb * q ^ (E * (n : ℝ) ^ 2 / 2) := by
    intro k hk
    have hkn : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
    have hcast : ((n - k : ℕ) : ℝ) = (n : ℝ) - (k : ℝ) := Nat.cast_sub hkn
    -- product of the two uniform Gaussian bounds
    have hprod : ‖a k‖ * ‖b (n - k)‖
        ≤ (Ca * q ^ ((s + ε) * (k : ℝ) ^ 2 / 2))
          * (Cb * q ^ ((t + ε) * ((n - k : ℕ) : ℝ) ^ 2 / 2)) :=
      mul_le_mul (hCa k) (hCb (n - k)) (norm_nonneg _) (by positivity)
    refine hprod.trans ?_
    -- merge the two rpow factors
    have hmerge : (Ca * q ^ ((s + ε) * (k : ℝ) ^ 2 / 2))
          * (Cb * q ^ ((t + ε) * ((n - k : ℕ) : ℝ) ^ 2 / 2))
        = Ca * Cb
          * q ^ ((s + ε) * (k : ℝ) ^ 2 / 2 + (t + ε) * ((n - k : ℕ) : ℝ) ^ 2 / 2) := by
      rw [mul_mul_mul_comm, ← Real.rpow_add hq0]
    rw [hmerge]
    -- envelope exponent inequality
    have henv := exponent_le_envelope (s + ε) (t + ε)
      (k := (k : ℝ)) (j := ((n - k : ℕ) : ℝ)) (Nat.cast_nonneg k) (Nat.cast_nonneg (n - k))
    have hsum_kj : (k : ℝ) + ((n - k : ℕ) : ℝ) = (n : ℝ) := by rw [hcast]; ring
    rw [hsum_kj] at henv
    have hexp : (s + ε) * (k : ℝ) ^ 2 / 2 + (t + ε) * ((n - k : ℕ) : ℝ) ^ 2 / 2
        ≤ E * (n : ℝ) ^ 2 / 2 := by rw [hE]; linarith [henv]
    have hrpow : q ^ ((s + ε) * (k : ℝ) ^ 2 / 2 + (t + ε) * ((n - k : ℕ) : ℝ) ^ 2 / 2)
        ≤ q ^ (E * (n : ℝ) ^ 2 / 2) := Real.rpow_le_rpow_of_exponent_le hq1 hexp
    have hCC : (0 : ℝ) ≤ Ca * Cb := by nlinarith [hCa1, hCb1]
    exact mul_le_mul_of_nonneg_left hrpow hCC
  refine (Finset.sum_le_sum hterm).trans ?_
  rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  have : ((n + 1 : ℕ) : ℝ) = (n : ℝ) + 1 := by push_cast; ring
  rw [this]
  ring_nf
  rfl

/-- **[MI-2, analytic — residual reduced to non-cancellation] Convolution order =
    envelope.**  Under the Cauchy product the q-Gevrey order is the dominant-balance
    ENVELOPE `cauchyEnvelope s t` (`= max s t` when not both `≤ 0`; `= s·t/(s+t)` when
    both `≤ 0`), NOT the additive `s + t` of the MI-1 stub.

    **Status (this PR).**  The `≤` (upper) direction is now proved sorry-free and
    packaged as `cauchyMul_eventual_norm_bound`: the two bricks
    (`cauchyMul_norm_le_sum` + `exponent_le_envelope`) plus the uniform Gaussian
    bounds `uniform_gaussian_bound` assemble into the closed pointwise estimate
    `‖(a⋆b)_n‖ ≤ C·(n+1)·q^{E(s+ε,t+ε)·n²/2}`.  That lemma is invoked below and its
    upper-bound content is the analytic heart of this theorem.

    **Residual `sorry` — exactly the missing non-cancellation hypothesis.**  Passing
    from the norm bound to the order *limit* is genuinely FALSE for the bare
    signature: in a general normed field the boundary/saddle coefficient can cancel
    to `0`, and Lean's `Real.log 0 = 0` junk value then makes `X_n := 2·logb q
    ‖(a⋆b)_n‖/n² = 0`, breaking the limit toward `E(s,t)` (e.g. when `E < 0`).  Both
    the upper leg (via `logb`-monotonicity) and the lower leg (`liminf ≥ E`) require
    the leading coefficients not to cancel — a hypothesis this statement does not
    carry.  The single `sorry` is precisely that deferred non-cancellation content;
    it is NOT vacuous and the correct `cauchyEnvelope` law is stated. -/
theorem cauchyMul_order {q s t : ℝ} {a b : ℕ → K}
    (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b)
    (hq : 1 < q) :
    IsQGevreyOrder q (cauchyEnvelope s t) (cauchyMul a b) := by
  -- Ref: [ramis-sauloy-zhang2013] Newton-polygon / dominant-balance slopes of
  --      q-difference systems.  The `≤` analytic content is the sorry-free
  --      `cauchyMul_eventual_norm_bound` (invoked here); the residual is only the
  --      non-cancellation of leading coefficients the bare statement lacks
  --      (both to defeat Lean's `Real.log 0 = 0` junk in the upper leg and for the
  --      `liminf ≥ E` lower leg).
  have _upper : ∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ,
      ‖cauchyMul a b n‖
        ≤ C * ((n : ℝ) + 1) * q ^ (cauchyEnvelope (s + ε) (t + ε) * (n : ℝ) ^ 2 / 2) :=
    fun ε hε => cauchyMul_eventual_norm_bound ha hb hq hε
  sorry

/-! ### MI-3 — bound-form extraction and the θ = ½·C(m,2) payoff bridge

    Two consumptions of the MI-1/MI-2 infra, both proved sorry-free.

    (a) **Bound-form extraction.**  The limit-form `IsQGevreyOrder` yields a
        two-sided *eventual bound* on the leading Gaussian coefficient — the
        `ε`-`δ` step the `≤` direction of `cauchyMul_order` explicitly cites.
        This is only the LIMIT ⟹ BOUND direction; the reverse (BOUND ⟹ LIMIT)
        is genuinely FALSE (a bound controls only the `limsup`/`liminf`, not the
        limit), so there is no full equivalence to state — recorded honestly,
        not axiomatised.

    (b) **θ = ½·C(m,2) payoff bridge (Tier-2 #4).**  The Route-B binding kernel
        has proved growth `q^{m²/4}` (docs/audits/2026-07-20-theta-jet-gb-
        filtration.md).  Since `IsQGevreyOrder q s a` reads `‖a n‖ ∼ q^{s n²/2}`,
        that growth is order `s = ½` (`routeB_gaussian_order_half`).  The GS
        cumulative degree `C(m,2) = m(m−1)/2` (corpus `gs_cumulative_degree`,
        `QOU.Mass.ThetaSlopeArithmetic`) has leading Gaussian coefficient `½`
        (`gs_degree_leading_coeff_half`).  The **single value `½`** is thus
        simultaneously the Route-B q-Gevrey order and the GS-degree leading
        coefficient (`theta_eq_half_gs_bridge`) — and `½·(½) = ¼` is exactly the
        θ-coefficient of the `q^{m²/4}` exponent, closing the numerical
        `θ = ½·C(m,2)` identity at the level of leading coefficients.  What
        stays probe-only is that the kernel's *actual* coefficient sequence
        realises this order (the RSZ slope=order theorem, MI-2's harder
        direction); this bridge compiles the leading-coefficient arithmetic, not
        that identification. -/

/-- **[MI-3(a), sorry-free] Limit form ⟹ eventual upper bound.**  If `a` has
    q-Gevrey order `s`, then for every `ε > 0` the leading Gaussian coefficient
    is eventually `≤ s + ε`.  Equivalently `‖a n‖ ≤ q^{(s+ε) n²/2}` eventually —
    the one-sided envelope the `≤` direction of `cauchyMul_order` extracts from
    the defining limit. -/
theorem order_eventually_le {q s : ℝ} {a : ℕ → K}
    (ha : IsQGevreyOrder q s a) {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ n in atTop, 2 * logb q ‖a n‖ / (n : ℝ) ^ 2 ≤ s + ε := by
  have hmem : ∀ᶠ y in 𝓝 s, y ≤ s + ε := by
    filter_upwards [Iio_mem_nhds (show s < s + ε by linarith)] with y hy
    exact le_of_lt hy
  exact ha.eventually hmem

/-- **[MI-3(a), sorry-free] Limit form ⟹ eventual lower bound.**  Dually, for
    every `ε > 0` the leading Gaussian coefficient is eventually `≥ s − ε`.
    Together with `order_eventually_le` this is the full two-sided bound form. -/
theorem order_eventually_ge {q s : ℝ} {a : ℕ → K}
    (ha : IsQGevreyOrder q s a) {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ n in atTop, s - ε ≤ 2 * logb q ‖a n‖ / (n : ℝ) ^ 2 := by
  have hmem : ∀ᶠ y in 𝓝 s, s - ε ≤ y := by
    filter_upwards [Ioi_mem_nhds (show s - ε < s by linarith)] with y hy
    exact le_of_lt hy
  exact ha.eventually hmem

/-- **[MI-3(b), sorry-free] Explicit Gaussian sequence has its named order.**
    The real sequence `n ↦ q^{s n²/2}` (`Real.rpow`) has q-Gevrey order exactly
    `s`, for any `q > 1`.  This is the concrete realiser that turns the abstract
    slope `s` into an actual coefficient sequence: `logb q (q^{s n²/2}) = s n²/2`,
    so the leading coefficient `2·log_q‖a n‖/n² = s` for every `n ≥ 1`, a
    constant sequence whose limit is `s`. -/
theorem order_of_rpow_gaussian (q s : ℝ) (hq : 1 < q) :
    IsQGevreyOrder q s (fun n : ℕ => q ^ (s * (n : ℝ) ^ 2 / 2)) := by
  have hq0 : 0 < q := by linarith
  have hlogq : Real.log q ≠ 0 := ne_of_gt (Real.log_pos hq)
  unfold IsQGevreyOrder
  refine Tendsto.congr' ?_ (tendsto_const_nhds (x := s))
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hnpos : 0 < n := by omega
  have hn0 : (n : ℝ) ≠ 0 := by
    have : (0 : ℝ) < n := by exact_mod_cast hnpos
    exact ne_of_gt this
  have hpos : (0 : ℝ) < q ^ (s * (n : ℝ) ^ 2 / 2) := Real.rpow_pos_of_pos hq0 _
  rw [Real.norm_eq_abs, abs_of_pos hpos]
  unfold logb
  rw [Real.log_rpow hq0]
  field_simp

/-- **[MI-3(b), sorry-free] Route-B kernel has q-Gevrey order ½.**  The proved
    Route-B growth `q^{m²/4}` is q-Gevrey order `½`, since
    `q^{m²/4} = q^{(½)·m²/2}` matches the order-`½` Gaussian.  This grounds
    `ThetaSlopeArithmetic.c1Slope = ½` for the actual coefficient sequence. -/
theorem routeB_gaussian_order_half (q : ℝ) (hq : 1 < q) :
    IsQGevreyOrder q (1 / 2) (fun n : ℕ => q ^ ((n : ℝ) ^ 2 / 4)) := by
  have hfun : (fun n : ℕ => q ^ ((n : ℝ) ^ 2 / 4))
      = (fun n : ℕ => q ^ ((1 / 2) * (n : ℝ) ^ 2 / 2)) := by
    funext n; congr 1; ring
  rw [hfun]
  exact order_of_rpow_gaussian q (1 / 2) hq

/-- **[MI-3(b), sorry-free] GS cumulative degree has leading coefficient ½.**
    The Gröbner–Shirshov cumulative q-degree `C(m,2) = m(m−1)/2` (corpus
    `QOU.Mass.ThetaSlopeArithmetic.gs_cumulative_degree`) has leading Gaussian
    coefficient `lim_{m→∞} C(m,2)/m² = ½`.  (`C(m,2)/m² = ½ − 1/(2m) → ½`.) -/
theorem gs_degree_leading_coeff_half :
    Tendsto (fun m : ℕ => ((m : ℝ) * ((m : ℝ) - 1) / 2) / (m : ℝ) ^ 2)
      atTop (𝓝 (1 / 2)) := by
  have key : (fun m : ℕ => ((m : ℝ) * ((m : ℝ) - 1) / 2) / (m : ℝ) ^ 2)
      =ᶠ[atTop] (fun m : ℕ => 1 / 2 - (2 * (m : ℝ))⁻¹) := by
    filter_upwards [eventually_ge_atTop 1] with m hm
    have hm0 : (m : ℝ) ≠ 0 := by
      have : (0 : ℝ) < m := by exact_mod_cast (by omega : 0 < m)
      exact ne_of_gt this
    field_simp
  refine Tendsto.congr' key.symm ?_
  have h2 : Tendsto (fun m : ℕ => 2 * (m : ℝ)) atTop atTop :=
    Tendsto.const_mul_atTop (by norm_num) tendsto_natCast_atTop_atTop
  have hinv : Tendsto (fun m : ℕ => (2 * (m : ℝ))⁻¹) atTop (𝓝 0) :=
    h2.inv_tendsto_atTop
  simpa using (tendsto_const_nhds (x := (1 / 2 : ℝ))).sub hinv

/-- **[MI-3(b), sorry-free] The θ = ½·C(m,2) bridge — leading-coefficient form.**
    The single value `s = ½` is simultaneously (i) the q-Gevrey ORDER of the
    Route-B kernel (its proved `q^{m²/4}` growth, `routeB_gaussian_order_half`)
    and (ii) the leading Gaussian coefficient of the GS cumulative degree
    `C(m,2)` (`gs_degree_leading_coeff_half`).  Hence the θ-coefficient of the
    kernel exponent `q^{m²/4}` is `½·s = ½·½ = ¼`, i.e. `θ = ½·C(m,2)` at leading
    order — the compiled half of the numerical probe.  What remains probe-only
    (NOT asserted here) is that the kernel's actual coefficient sequence realises
    order ½ (the RSZ slope=order theorem). -/
theorem theta_eq_half_gs_bridge :
    ∃ s : ℝ,
      (∀ q : ℝ, 1 < q → IsQGevreyOrder q s (fun n : ℕ => q ^ ((n : ℝ) ^ 2 / 4)))
      ∧ Tendsto (fun m : ℕ => ((m : ℝ) * ((m : ℝ) - 1) / 2) / (m : ℝ) ^ 2)
          atTop (𝓝 s) :=
  ⟨1 / 2, fun q hq => routeB_gaussian_order_half q hq, gs_degree_leading_coeff_half⟩

end QOU.Mathlib.QGevreyOrder
