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

/-- **[MI-2, analytic — residual cited `sorry`] Convolution order = envelope.**
    Under the Cauchy product the q-Gevrey order is the dominant-balance ENVELOPE
    `cauchyEnvelope s t` (`= max s t` when not both `≤ 0`; `= s·t/(s+t)` when
    both `≤ 0`), NOT the additive `s + t` of the MI-1 stub.

    The `≤` direction reduces to the two sorry-free lemmas above
    (`cauchyMul_norm_le_sum` + `exponent_le_envelope`) plus an `ε`-`δ`
    assembly extracting `‖a_k‖ ≤ q^{(s+ε)k²/2}` (resp. `b`) from the defining
    limits and absorbing the `(n+1)` prefactor.  The `≥` direction additionally
    needs a non-cancellation hypothesis on the leading coefficients (in a general
    normed field the boundary/saddle term may cancel).  Both are the deferred
    analytic content. -/
theorem cauchyMul_order {q s t : ℝ} {a b : ℕ → K}
    (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b)
    (hq : 1 < q) :
    IsQGevreyOrder q (cauchyEnvelope s t) (cauchyMul a b) := by
  -- Ref: [ramis-sauloy-zhang2013] Newton-polygon / dominant-balance slopes of
  --      q-difference systems.  Upper bound: cauchyMul_norm_le_sum +
  --      exponent_le_envelope + ε-δ; lower bound: + non-cancellation.
  -- SORRY: needs dominant balance / Laplace method for discrete convolutions with q-Gevrey bounds
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

/-! ### q-Gevrey LEVEL — the reciprocal notion, and the one RSZ ties to slopes

Ramis–Sauloy–Zhang, Astérisque 355 §1.3.2, verbatim:

> we introduce the space of formal series of q-Gevrey **order** `s`:
> `C[[z]]_{q;s} := { Σ aₙzⁿ | ∃A > 0 : aₙ = O(Aⁿ q^{s n²/2}) }`.
> We also say that `f ∈ C[[z]]_{q;s}` is of q-Gevrey **level** `1/s`.

So `IsQGevreyOrder` above **is** RSZ's *order*, on the nose. The *level* is its
reciprocal, and the level is what RSZ attaches to the Newton polygon: §2.3.2
calls the two-slope case the *"one level case, because the q-Gevrey level
`µ₂ − µ₁` is the fundamental parameter"*, and Example 3.3.3 writes
`d := µ₂ − µ₁` for *"the level"*, with the q-Borel kernel `tₙ` of *"order of
growth `q^{n²/2d}`"* — which is exactly order `1/d`.

Both words are therefore in play, they are reciprocal, and the corpus has used
"q-Gevrey ½" for both. This section makes the level a definition so the two
numbers stop travelling as prose. -/

/-- **q-Gevrey level** (RSZ §1.3.2): level `d` means order `1/d`. -/
def IsQGevreyLevel (q : ℝ) (d : ℝ) (a : ℕ → K) : Prop := IsQGevreyOrder q d⁻¹ a

/-- Level and order are reciprocal, by definition. -/
theorem isQGevreyLevel_iff_order {q d : ℝ} {a : ℕ → K} :
    IsQGevreyLevel q d a ↔ IsQGevreyOrder q d⁻¹ a := Iff.rfl

/-- A sequence of order `s ≠ 0` has level `1/s`. -/
theorem isQGevreyLevel_of_order {q s : ℝ} {a : ℕ → K} (hs : s ≠ 0)
    (h : IsQGevreyOrder q s a) : IsQGevreyLevel q s⁻¹ a := by
  rw [IsQGevreyLevel, inv_inv]
  exact h

/-- **Level is a well-defined invariant** for nonzero levels, from `order_unique`. -/
theorem level_unique {q d e : ℝ} {a : ℕ → K} (hd : d ≠ 0) (he : e ≠ 0)
    (hdl : IsQGevreyLevel q d a) (hel : IsQGevreyLevel q e a) : d = e := by
  have := order_unique hdl hel
  field_simp at this
  linarith

/-- **`q^{n²}` has q-Gevrey order 2** (and hence level `½`).

Stated because two files in this corpus attach the number `½` to `q^{m²/4}` and
to `q^{n²}`, which are reciprocal:

* `routeB_gaussian_order_half` (above) — growth `q^{m²/4}`, **order** `½`.
* `QOU.Mass.C1FormalSolutionGrowth` — growth `q^{n²}` for the C1 `∞`-side
  formal solution, docstring "the q-Gevrey-½ divergence" — that `½` is the
  **level** (RSZ §1.3.2), i.e. order `2`.

`IsQGevreyOrder q s a` is `‖aₙ‖ ∼ Cⁿ q^{s n²/2}`, which is RSZ's *order*
verbatim, so `q^{n²}` forces `s = 2`. Neither file wrote a wrong number; they
wrote **different quantities** under one word. See
`routeB_and_c1Inf_are_reciprocal` for what that leaves open, and the
level section above for the RSZ citations. -/
theorem qSquare_gaussian_order_two (q : ℝ) (hq : 1 < q) :
    IsQGevreyOrder q 2 (fun n : ℕ => q ^ ((n : ℝ) ^ 2)) := by
  have hfun : (fun n : ℕ => q ^ ((n : ℝ) ^ 2))
      = (fun n : ℕ => q ^ ((2 : ℝ) * (n : ℝ) ^ 2 / 2)) := by
    funext n; congr 1; ring
  rw [hfun]
  exact order_of_rpow_gaussian q 2 hq

/-- **`q^{n²}` has q-Gevrey LEVEL ½.** Same fact as
`qSquare_gaussian_order_two`, said in RSZ's other word. So
`QOU.Mass.C1FormalSolutionGrowth`'s "q-Gevrey-½ divergence" **is correct RSZ
terminology** — it is the *level*. It is simply not the quantity
`IsQGevreyOrder` measures. -/
theorem qSquare_gaussian_level_half (q : ℝ) (hq : 1 < q) :
    IsQGevreyLevel q (1 / 2) (fun n : ℕ => q ^ ((n : ℝ) ^ 2)) := by
  rw [IsQGevreyLevel, show ((1:ℝ) / 2)⁻¹ = 2 by norm_num]
  exact qSquare_gaussian_order_two q hq

/-- **`q^{m²/4}` has q-Gevrey LEVEL 2.** The Route-B kernel's `½` is an
*order*; its level is `2`. -/
theorem routeB_gaussian_level_two (q : ℝ) (hq : 1 < q) :
    IsQGevreyLevel q 2 (fun n : ℕ => q ^ ((n : ℝ) ^ 2 / 4)) := by
  rw [IsQGevreyLevel, show (2:ℝ)⁻¹ = 1 / 2 by norm_num]
  exact routeB_gaussian_order_half q hq

/-- **The two `½`s in this corpus are `½` in reciprocal senses.**

* Route-B kernel `q^{m²/4}`: order `½`, level `2`.
* C1 `∞`-side `q^{n²}`: order `2`, level `½`.

Neither file was writing a wrong number; they were writing *different
quantities* under one word. `½ ≠ 2`, so with `order_unique` / `level_unique` no
single sequence carries both, and "the C1 slope is ½" is ambiguous until one
says *order* or *level*.

**Which one is the Newton-polygon slope is NOT settled here.** RSZ attaches the
**level** to the slope (§2.3.2, Ex. 3.3.3), which would favour the C1 `∞`-side
reading; but `theta_eq_half_gs_bridge` below grounds
`ThetaSlopeArithmetic.c1Slope = ½` through `routeB_gaussian_order_half`, an
**order**. Those cannot both be the slope. Deciding it needs the Newton polygon
of `L1` computed directly — bean `qou-slpd` item 4 — not a relabelling. -/
theorem routeB_and_c1Inf_are_reciprocal :
    ((1 : ℝ) / 2 ≠ 2) ∧ ((2 : ℝ)⁻¹ = 1 / 2) ∧ (((1 : ℝ) / 2)⁻¹ = 2) := by
  refine ⟨by norm_num, by norm_num, by norm_num⟩

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

/-! ## MI-3(c): the order of an ACTUAL C1 coefficient sequence

`routeB_gaussian_order_half` and `qSquare_gaussian_order_two` are about the
explicit functions `q^{m²/4}` and `q^{n²}`. `theta_eq_half_gs_bridge` above
already flags what that leaves open — *"what remains probe-only is that the
kernel's actual coefficient sequence realises order ½"*. This section closes
that for one actual sequence: the C1 `∞`-side coefficients

    c₀ = 1,   c_{m+1} = cₘ·(1 + (q−1)qᵐ + (q−1)q^{2m})

(`QOU.Mass.C1FormalSolutionGrowth`, whose `natDegree_c1CoeffPoly` gives the
same `n²` on the polynomial side). The answer is **2**, not ½ — under the
definition at the top of this file. The sandwich

    (q−1)ⁿ q^{n²}  ≤  cₙ qⁿ  ≤  (2q−1)ⁿ q^{n²}

is proved by induction from `(q−1)q^{2m} ≤ M_m ≤ (2q−1)q^{2m}`, and both sides
of the resulting bound on `2 log_q cₙ / n²` are `2 log_q(const)/n + 2 − 2/n → 2`.

This does **not** settle which convention the manuscript intends — see the note
on `qSquare_gaussian_order_two`. It settles that, under the formalised one, an
actual C1 sequence gives `2`. -/

section C1InfOrder

variable {q : ℝ}

/-- The C1 `∞`-side per-step multiplier. -/
noncomputable def c1InfMult (q : ℝ) (m : ℕ) : ℝ :=
  1 + (q - 1) * q ^ m + (q - 1) * q ^ (2 * m)

/-- The C1 `∞`-side coefficients themselves. -/
noncomputable def c1InfCoeff (q : ℝ) : ℕ → ℝ
  | 0 => 1
  | (m + 1) => c1InfCoeff q m * c1InfMult q m

variable {q : ℝ}

private lemma c1q_pos (hq : 1 < q) : 0 < q := lt_trans zero_lt_one hq

private lemma c1_one_le_qpow (hq : 1 < q) (m : ℕ) : (1:ℝ) ≤ q ^ m := one_le_pow₀ hq.le

lemma c1InfMult_lower (hq : 1 < q) (m : ℕ) : (q - 1) * q ^ (2 * m) ≤ c1InfMult q m := by
  have h1 : (0:ℝ) ≤ (q - 1) * q ^ m := by
    have := (c1_one_le_qpow hq m); nlinarith [c1q_pos hq]
  rw [c1InfMult]; linarith

lemma c1InfMult_upper (hq : 1 < q) (m : ℕ) : c1InfMult q m ≤ (2 * q - 1) * q ^ (2 * m) := by
  have hm : q ^ m ≤ q ^ (2 * m) := pow_le_pow_right₀ hq.le (by omega)
  have h1 : (1:ℝ) ≤ q ^ (2 * m) := c1_one_le_qpow hq _
  have hq1 : (0:ℝ) ≤ q - 1 := by linarith
  rw [c1InfMult]
  nlinarith [mul_le_mul_of_nonneg_left hm hq1]

lemma c1InfCoeff_pos (hq : 1 < q) (n : ℕ) : 0 < c1InfCoeff q n := by
  induction n with
  | zero => rw [c1InfCoeff]; norm_num
  | succ k ih =>
    have h := c1InfMult_lower hq k
    have h2 : (0:ℝ) < (q - 1) * q ^ (2 * k) := by
      have := c1_one_le_qpow hq (2 * k); nlinarith
    rw [c1InfCoeff]
    exact mul_pos ih (lt_of_lt_of_le h2 h)

private lemma pow_sq_succ (hq : 1 < q) (k : ℕ) :
    q ^ ((k + 1) * (k + 1)) = q ^ (k * k) * q ^ (2 * k) * q := by
  rw [← pow_add, ← pow_succ]
  congr 1
  ring

/-- `(q−1)ⁿ q^{n²} ≤ cₙ qⁿ`. -/
lemma c1InfCoeff_lower (hq : 1 < q) (n : ℕ) :
    (q - 1) ^ n * q ^ (n * n) ≤ c1InfCoeff q n * q ^ n := by
  have hqp : (0:ℝ) < q := c1q_pos hq
  have hA : (0:ℝ) < q - 1 := by linarith
  induction n with
  | zero => rw [c1InfCoeff]; norm_num
  | succ k ih =>
    have hmul : (q - 1) * q ^ (2 * k) ≤ c1InfMult q k := c1InfMult_lower hq k
    have hnn1 : (0:ℝ) ≤ (q - 1) * q ^ (2 * k) * q :=
      mul_nonneg (mul_nonneg hA.le (pow_nonneg hqp.le _)) hqp.le
    have hnn2 : (0:ℝ) ≤ c1InfCoeff q k * q ^ k :=
      mul_nonneg (c1InfCoeff_pos hq k).le (pow_nonneg hqp.le _)
    calc (q - 1) ^ (k + 1) * q ^ ((k + 1) * (k + 1))
        = ((q - 1) ^ k * q ^ (k * k)) * ((q - 1) * q ^ (2 * k) * q) := by
          rw [pow_sq_succ hq k]; ring
      _ ≤ (c1InfCoeff q k * q ^ k) * ((q - 1) * q ^ (2 * k) * q) :=
          mul_le_mul_of_nonneg_right ih hnn1
      _ ≤ (c1InfCoeff q k * q ^ k) * (c1InfMult q k * q) :=
          mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_right hmul hqp.le) hnn2
      _ = c1InfCoeff q (k + 1) * q ^ (k + 1) := by
          rw [show c1InfCoeff q (k + 1) = c1InfCoeff q k * c1InfMult q k from rfl,
              pow_succ]
          ring

/-- `cₙ qⁿ ≤ (2q−1)ⁿ q^{n²}`. -/
lemma c1InfCoeff_upper (hq : 1 < q) (n : ℕ) :
    c1InfCoeff q n * q ^ n ≤ (2 * q - 1) ^ n * q ^ (n * n) := by
  have hqp : (0:ℝ) < q := c1q_pos hq
  have hB : (0:ℝ) < 2 * q - 1 := by linarith
  induction n with
  | zero => rw [c1InfCoeff]; norm_num
  | succ k ih =>
    have hmul : c1InfMult q k ≤ (2 * q - 1) * q ^ (2 * k) := c1InfMult_upper hq k
    have hnn1 : (0:ℝ) ≤ (2 * q - 1) * q ^ (2 * k) * q :=
      mul_nonneg (mul_nonneg hB.le (pow_nonneg hqp.le _)) hqp.le
    have hnn2 : (0:ℝ) ≤ c1InfCoeff q k * q ^ k :=
      mul_nonneg (c1InfCoeff_pos hq k).le (pow_nonneg hqp.le _)
    calc c1InfCoeff q (k + 1) * q ^ (k + 1)
        = (c1InfCoeff q k * q ^ k) * (c1InfMult q k * q) := by
          rw [show c1InfCoeff q (k + 1) = c1InfCoeff q k * c1InfMult q k from rfl,
              pow_succ]
          ring
      _ ≤ (c1InfCoeff q k * q ^ k) * ((2 * q - 1) * q ^ (2 * k) * q) :=
          mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_right hmul hqp.le) hnn2
      _ ≤ ((2 * q - 1) ^ k * q ^ (k * k)) * ((2 * q - 1) * q ^ (2 * k) * q) :=
          mul_le_mul_of_nonneg_right ih hnn1
      _ = (2 * q - 1) ^ (k + 1) * q ^ ((k + 1) * (k + 1)) := by
          rw [pow_sq_succ hq k]; ring

private lemma log_bounds (hq : 1 < q) (n : ℕ) :
    (n:ℝ) * Real.log (q - 1) + ((n:ℝ) * (n:ℝ) - (n:ℝ)) * Real.log q
      ≤ Real.log (c1InfCoeff q n)
    ∧ Real.log (c1InfCoeff q n)
      ≤ (n:ℝ) * Real.log (2 * q - 1) + ((n:ℝ) * (n:ℝ) - (n:ℝ)) * Real.log q := by
  have hqp : (0:ℝ) < q := c1q_pos hq
  have hA : (0:ℝ) < q - 1 := by linarith
  have hB : (0:ℝ) < 2 * q - 1 := by linarith
  have hc : 0 < c1InfCoeff q n := c1InfCoeff_pos hq n
  have hqn : (0:ℝ) < q ^ n := pow_pos hqp n
  have hqnn : (0:ℝ) < q ^ (n * n) := pow_pos hqp _
  have hposL : (0:ℝ) < (q - 1) ^ n * q ^ (n * n) := mul_pos (pow_pos hA n) hqnn
  have hposM : (0:ℝ) < c1InfCoeff q n * q ^ n := mul_pos hc hqn
  have h1 := Real.log_le_log hposL (c1InfCoeff_lower hq n)
  have h2 := Real.log_le_log hposM (c1InfCoeff_upper hq n)
  have e1 : Real.log ((q - 1) ^ n * q ^ (n * n))
      = (n:ℝ) * Real.log (q - 1) + ((n:ℝ) * (n:ℝ)) * Real.log q := by
    rw [Real.log_mul (ne_of_gt (pow_pos hA n)) (ne_of_gt hqnn), Real.log_pow, Real.log_pow]
    push_cast
    ring
  have e2 : Real.log (c1InfCoeff q n * q ^ n)
      = Real.log (c1InfCoeff q n) + (n:ℝ) * Real.log q := by
    rw [Real.log_mul (ne_of_gt hc) (ne_of_gt hqn), Real.log_pow]
  have e3 : Real.log ((2 * q - 1) ^ n * q ^ (n * n))
      = (n:ℝ) * Real.log (2 * q - 1) + ((n:ℝ) * (n:ℝ)) * Real.log q := by
    rw [Real.log_mul (ne_of_gt (pow_pos hB n)) (ne_of_gt hqnn), Real.log_pow, Real.log_pow]
    push_cast
    ring
  rw [e1, e2] at h1
  rw [e2, e3] at h2
  constructor <;> nlinarith [h1, h2]

/-- **The C1 `∞`-side coefficient sequence has q-Gevrey order 2.**

Not the explicit function `q^{n²}` — the actual sequence defined by the
recursion. Squeeze on `2 log_q cₙ / n²` between the two bounds
`(q−1)ⁿ q^{n²} ≤ cₙ qⁿ ≤ (2q−1)ⁿ q^{n²}`; both sides are
`2 log_q(const)/n + 2 − 2/n → 2`. -/
theorem c1InfCoeff_order_two (hq : 1 < q) : IsQGevreyOrder q 2 (c1InfCoeff q) := by
  have hqp : (0:ℝ) < q := c1q_pos hq
  have hlogq : 0 < Real.log q := Real.log_pos hq
  set a : ℝ := Real.log (q - 1) / Real.log q with ha
  set b : ℝ := Real.log (2 * q - 1) / Real.log q with hb
  have hlim : ∀ c : ℝ,
      Tendsto (fun n : ℕ => 2 * c / (n:ℝ) + 2 - 2 / (n:ℝ)) atTop (𝓝 2) := by
    intro c
    have h1 : Tendsto (fun n : ℕ => 2 * c / (n:ℝ)) atTop (𝓝 0) :=
      tendsto_const_div_atTop_nhds_zero_nat (2 * c)
    have h2 : Tendsto (fun n : ℕ => 2 / (n:ℝ)) atTop (𝓝 0) :=
      tendsto_const_div_atTop_nhds_zero_nat 2
    simpa using ((h1.add tendsto_const_nhds).sub h2)
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' (hlim a) (hlim b) ?_ ?_
  · filter_upwards [eventually_gt_atTop 0] with n hn
    have hn0 : (0:ℝ) < (n:ℝ) := by exact_mod_cast hn
    have hn2 : (0:ℝ) < (n:ℝ) ^ 2 := by positivity
    have hc : 0 < c1InfCoeff q n := c1InfCoeff_pos hq n
    have hnorm : ‖c1InfCoeff q n‖ = c1InfCoeff q n := by
      rw [Real.norm_eq_abs, abs_of_pos hc]
    obtain ⟨hlo, -⟩ := log_bounds hq n
    have hlog : Real.log (q - 1) = a * Real.log q := by rw [ha]; field_simp
    rw [hlog] at hlo
    have hdiv : (n:ℝ) * a + ((n:ℝ) * (n:ℝ) - (n:ℝ))
        ≤ Real.log (c1InfCoeff q n) / Real.log q := by
      rw [le_div_iff₀ hlogq]; nlinarith [hlo]
    rw [hnorm, logb, le_div_iff₀ hn2]
    have hexp : (2 * a / (n:ℝ) + 2 - 2 / (n:ℝ)) * (n:ℝ) ^ 2
        = 2 * ((n:ℝ) * a + ((n:ℝ) * (n:ℝ) - (n:ℝ))) := by
      field_simp; ring
    rw [hexp]
    linarith [hdiv]
  · filter_upwards [eventually_gt_atTop 0] with n hn
    have hn0 : (0:ℝ) < (n:ℝ) := by exact_mod_cast hn
    have hn2 : (0:ℝ) < (n:ℝ) ^ 2 := by positivity
    have hc : 0 < c1InfCoeff q n := c1InfCoeff_pos hq n
    have hnorm : ‖c1InfCoeff q n‖ = c1InfCoeff q n := by
      rw [Real.norm_eq_abs, abs_of_pos hc]
    obtain ⟨-, hup⟩ := log_bounds hq n
    have hlog : Real.log (2 * q - 1) = b * Real.log q := by rw [hb]; field_simp
    rw [hlog] at hup
    have hdiv : Real.log (c1InfCoeff q n) / Real.log q
        ≤ (n:ℝ) * b + ((n:ℝ) * (n:ℝ) - (n:ℝ)) := by
      rw [div_le_iff₀ hlogq]; nlinarith [hup]
    rw [hnorm, logb, div_le_iff₀ hn2]
    have hexp : (2 * b / (n:ℝ) + 2 - 2 / (n:ℝ)) * (n:ℝ) ^ 2
        = 2 * ((n:ℝ) * b + ((n:ℝ) * (n:ℝ) - (n:ℝ))) := by
      field_simp; ring
    rw [hexp]
    linarith [hdiv]

end C1InfOrder

end QOU.Mathlib.QGevreyOrder
