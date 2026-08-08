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
  0. §7c: the growth is archimedean, so `ℝ` for the base and target is genuine
  (`Real.log`).

  The genuinely-analytic Cauchy-CONVOLUTION law (Newton-polygon / dominant
  balance) is MI-2, and it is now **proved** — `cauchyMul_order`, no `sorry`
  anywhere in this file. The `≤` half (MI-3(c)) holds over an arbitrary normed
  field; the `≥` half (MI-4) is the Laplace/saddle term selection and needs the
  non-cancellation hypothesis carried by the statement. It genuinely needs one:
  the earlier hypothesis-free statement over an arbitrary normed field was FALSE,
  and `cauchyMul_order_unhypothesised_false` proves so.

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

    **SCOPE (honest).**  The `≤` (upper) direction is **fully proved**, over an
    arbitrary normed field and with no non-cancellation hypothesis, in four
    sorry-free steps: (i) `cauchyMul_norm_le_sum`, the triangle bound
    `‖(a⋆b)_n‖ ≤ ∑ ‖a_k‖‖b_{n-k}‖`; (ii) `exponent_le_envelope`, the exact
    dominant-balance inequality `s k² + t j² ≤ E(s,t)·(k+j)²` (`k,j ≥ 0`) — the
    mathematical heart, an identity-plus-sign completing-the-square argument in
    each regime; (iii) `cauchyMul_norm_le_envelope`, their assembly into the
    bound form; (iv) `cauchyMul_norm_eventually_le` (MI-3(c)), the `ε`-`δ`
    passage to the limit form, using `exists_global_gaussian_bound`,
    `cauchyEnvelope_add_le` and `eventually_linear_le_rpow_sq`.

    The `≥` (lower) direction is **also proved**, in MI-4 at the end of the file:
    the Laplace/saddle *term selection*, which is where the non-cancellation
    hypothesis is genuinely load-bearing.  That hypothesis is part of the
    statement (positive real coefficients, the regime the numerics above were run
    in): without it the law is **false**, and
    `cauchyMul_order_unhypothesised_false` proves it.

    So MI-2 carries **no `sorry`** — neither does anything else in this file. -/

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

/-! ### MI-2 — the law, corrected

**The previous statement of `cauchyMul_order` was false, not merely open.**  It
quantified over an arbitrary normed field `K` and assumed nothing beyond the two
orders, but `IsQGevreyOrder` is a *limit* statement and nothing stopped the
convolution from cancelling.  `cauchyMul_order_unhypothesised_false` below proves
the refutation from the file's own definitions: take `b = 0`, which has order `0`
(`‖0‖ = 0` and `Real.log 0 = 0`, so every ratio is `0`), against an `a` of order
`2`; then `a ⋆ b = 0` again has order `0`, while `cauchyEnvelope 2 0 = max 2 0 =
2`, and `order_unique` gives `0 = 2`.

A `sorry` in front of a false proposition is strictly worse than an open gap —
discharging it would discharge `False`, and every consumer would be unsound — so
the statement below is the **true** law: over `ℝ`, with strictly positive
coefficients.  That is exactly the regime this section's numerics were run in
("positive/no-cancel coefficients"), and positivity is precisely what kills every
cancellation counterexample: each summand of `(a ⋆ b)_n = ∑ a_k b_{n-k}` is then
positive, so the sum is squeezed between its own largest term (the saddle /
boundary term the Laplace argument selects) and `(n+1)` times it.

Nothing here is cited any more.  The `≤` half is discharged sorry-free — for an
arbitrary normed field and with no positivity — by `cauchyMul_norm_le_envelope`
just below and `cauchyMul_norm_eventually_le` in MI-3(c); the `≥` half, where
non-cancellation is load-bearing, is discharged in MI-4 at the end of the file.
The law itself is stated and proved there, as `cauchyMul_order`.

(This mirrors the in-repo `SnWedderburnPartitionBridge.freeProjClaim_false`
disposition: refute the over-general form by machine proof, then state the true
one, rather than leaving a `sorry` on a falsehood.) -/

/-- **The identically-zero sequence has q-Gevrey order `0`**, for every base.
`‖0‖ = 0` and `Real.log 0 = 0`, so the defining ratio is identically `0`.

This junk-value convention is what makes the unhypothesised convolution law
false, so it is recorded as a named lemma rather than left as a surprise. -/
theorem isQGevreyOrder_zero (q : ℝ) : IsQGevreyOrder q 0 (fun _ : ℕ => (0 : K)) := by
  unfold IsQGevreyOrder
  refine Tendsto.congr' ?_ (tendsto_const_nhds (x := (0 : ℝ)))
  filter_upwards with n
  simp [logb]

/-- **The unhypothesised convolution law is FALSE** (machine-proved, no `sorry`).

Concretely, over `ℝ` with `q = 2`: `a n = 2^{n²}` has order `2`, the zero
sequence has order `0`, their Cauchy product is `0` and so has order `0`, yet
`cauchyEnvelope 2 0 = max 2 0 = 2`.  By `order_unique` the law would give
`0 = 2`.

Hence `cauchyMul_order` **must** carry a non-cancellation hypothesis; the version
stated below carries strict positivity of the coefficients.  Axioms
`[propext, Classical.choice, Quot.sound]`. -/
theorem cauchyMul_order_unhypothesised_false :
    ¬ ∀ (q s t : ℝ) (a b : ℕ → ℝ),
        IsQGevreyOrder q s a → IsQGevreyOrder q t b → 1 < q →
        IsQGevreyOrder q (cauchyEnvelope s t) (cauchyMul a b) := by
  intro h
  have hlog : Real.log 2 ≠ 0 := ne_of_gt (Real.log_pos one_lt_two)
  -- an explicit order-2 sequence
  have ha : IsQGevreyOrder (2 : ℝ) 2 (fun n : ℕ => (2 : ℝ) ^ (n ^ 2)) := by
    unfold IsQGevreyOrder
    refine Tendsto.congr' ?_ (tendsto_const_nhds (x := (2 : ℝ)))
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hn0 : ((n : ℝ)) ^ 2 ≠ 0 := by
      have : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn
      positivity
    show (2 : ℝ) = 2 * logb 2 ‖(2 : ℝ) ^ (n ^ 2)‖ / (n : ℝ) ^ 2
    rw [Real.norm_of_nonneg (by positivity)]
    unfold logb
    rw [Real.log_pow]
    push_cast
    field_simp
  -- the zero sequence has order 0, and kills the convolution
  have hb : IsQGevreyOrder (2 : ℝ) 0 (fun _ : ℕ => (0 : ℝ)) := isQGevreyOrder_zero (K := ℝ) 2
  have hE : cauchyEnvelope 2 0 = 2 := by norm_num [cauchyEnvelope]
  have hprod : cauchyMul (fun n : ℕ => (2 : ℝ) ^ (n ^ 2)) (fun _ : ℕ => (0 : ℝ))
      = fun _ : ℕ => (0 : ℝ) := by
    funext n; simp [cauchyMul]
  have hc := h 2 2 0 _ _ ha hb one_lt_two
  rw [hE, hprod] at hc
  have : (2 : ℝ) = 0 := order_unique hc (isQGevreyOrder_zero (K := ℝ) 2)
  norm_num at this

/-- **[MI-2 ingredient, sorry-free] The envelope is `ε`-Lipschitz along the
diagonal**: `E(s+ε, t+ε) ≤ E(s,t) + ε` for `ε ≥ 0`.

Conceptually this is immediate from `E(s,t) = sup_{θ∈[0,1]}(sθ² + t(1−θ)²)` and
`θ² + (1−θ)² ≤ 1` on `[0,1]`; proved here directly from the closed form, which
costs a four-way case split (the `ε`-shifted point can leave the concave branch
but never enter it, so one of the four cases is vacuous).

This is the step that lets the `ε` in `cauchyMul_norm_eventually_le` be pushed
through the envelope instead of requiring continuity of `cauchyEnvelope`. -/
theorem cauchyEnvelope_add_le (s t : ℝ) {ε : ℝ} (hε : 0 ≤ ε) :
    cauchyEnvelope (s + ε) (t + ε) ≤ cauchyEnvelope s t + ε := by
  unfold cauchyEnvelope
  split_ifs with h1 h2 h2
  · -- both branches concave
    obtain ⟨hu, hv⟩ := h1
    obtain ⟨hs, ht⟩ := h2
    rcases eq_or_lt_of_le (add_nonpos hu hv) with hD1 | hD1
    · -- (s+ε) + (t+ε) = 0 forces s = t = -ε
      have hs' : s = -ε := by linarith
      have ht' : t = -ε := by linarith
      subst hs'; subst ht'
      rcases eq_or_lt_of_le hε with hε0 | hε0
      · simp [← hε0]
      · have hεne : ε ≠ 0 := ne_of_gt hε0
        have hL : (-ε + ε) * (-ε + ε) / ((-ε + ε) + (-ε + ε)) = (0 : ℝ) := by simp
        have hR : (-ε) * (-ε) / ((-ε) + (-ε)) = -(ε / 2) := by
          rw [div_eq_iff (by intro hcon; exact hεne (by linarith))]
          ring
        rw [hL, hR]
        linarith
    · -- both denominators strictly negative: clear them
      have hD2 : s + t < 0 := by linarith
      have hD1' : (s + ε) + (t + ε) ≠ 0 := ne_of_lt hD1
      have hD2' : s + t ≠ 0 := ne_of_lt hD2
      have hkey : s * t / (s + t) + ε - (s + ε) * (t + ε) / ((s + ε) + (t + ε))
          = (ε * (2 * (s * t) + ε * (s + t))) / ((s + t) * ((s + ε) + (t + ε))) := by
        field_simp
        ring
      -- `(s+ε)(t+ε) ≥ 0` and `ε² ≤ s·t` make the numerator nonnegative
      have hprod : (0 : ℝ) ≤ (s + ε) * (t + ε) := by
        nlinarith [mul_nonneg (neg_nonneg.mpr hu) (neg_nonneg.mpr hv)]
      have hst : ε * ε ≤ s * t := by
        have h1 : ε ≤ -s := by linarith
        have h2 : ε ≤ -t := by linarith
        nlinarith [mul_le_mul h1 h2 hε (by linarith : (0 : ℝ) ≤ -s)]
      have hnum : 0 ≤ ε * (2 * (s * t) + ε * (s + t)) :=
        mul_nonneg hε (by nlinarith [hprod, hst])
      have hden : 0 < (s + t) * ((s + ε) + (t + ε)) := mul_pos_of_neg_of_neg hD2 hD1
      have hpos : 0 ≤ s * t / (s + t) + ε
          - (s + ε) * (t + ε) / ((s + ε) + (t + ε)) := by
        rw [hkey]; exact div_nonneg hnum hden.le
      linarith
  · -- vacuous: `ε ≥ 0` and `s + ε ≤ 0` force `s ≤ 0` (same for `t`)
    exact absurd ⟨by linarith [h1.1], by linarith [h1.2]⟩ h2
  · -- convex on the left, concave on the right: `max s t ≤ s·t/(s+t)`
    obtain ⟨hs, ht⟩ := h2
    have hmax : max (s + ε) (t + ε) ≤ max s t + ε := by
      exact max_le (by linarith [le_max_left s t]) (by linarith [le_max_right s t])
    refine hmax.trans (add_le_add_right ?_ ε)
    rcases eq_or_lt_of_le (add_nonpos hs ht) with hD | hD
    · have hs' : s = 0 := by linarith
      have ht' : t = 0 := by linarith
      subst hs'; subst ht'; simp
    · rw [le_div_iff_of_neg hD]
      rcases max_cases s t with ⟨hm, _⟩ | ⟨hm, _⟩ <;> rw [hm] <;> nlinarith [sq_nonneg s, sq_nonneg t]
  · -- both branches convex
    exact max_le (by linarith [le_max_left s t]) (by linarith [le_max_right s t])

/-- **[MI-2, sorry-free] The `≤` direction in bound form.**  Global Gaussian
bounds on the two coefficient sequences give the ENVELOPE bound on their Cauchy
product, with only a linear `(n+1)` loss:

    ‖a k‖ ≤ Ca·q^{s k²/2},  ‖b k‖ ≤ Cb·q^{t k²/2}
      ⟹  ‖(a⋆b)_n‖ ≤ Ca·Cb·(n+1)·q^{E(s,t) n²/2}.

This is the assembly of the two ingredients above — `cauchyMul_norm_le_sum` for
the triangle inequality, `exponent_le_envelope` for the dominant balance — and it
holds over an arbitrary normed field with no positivity and no non-cancellation
hypothesis, because it is an upper bound. -/
theorem cauchyMul_norm_le_envelope {q s t : ℝ} (hq : 1 < q) {a b : ℕ → K}
    {Ca Cb : ℝ} (hCa : 0 ≤ Ca) (hCb : 0 ≤ Cb)
    (hA : ∀ k : ℕ, ‖a k‖ ≤ Ca * q ^ (s * (k : ℝ) ^ 2 / 2))
    (hB : ∀ k : ℕ, ‖b k‖ ≤ Cb * q ^ (t * (k : ℝ) ^ 2 / 2)) (n : ℕ) :
    ‖cauchyMul a b n‖
      ≤ Ca * Cb * ((n : ℝ) + 1) * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2) := by
  have hq0 : (0 : ℝ) < q := by linarith
  refine (cauchyMul_norm_le_sum a b n).trans ?_
  have hterm : ∀ k ∈ Finset.range (n + 1),
      ‖a k‖ * ‖b (n - k)‖ ≤ Ca * Cb * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2) := by
    intro k hk
    have hkn : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
    have hcast : ((n - k : ℕ) : ℝ) = (n : ℝ) - (k : ℝ) := Nat.cast_sub hkn
    have hj : (0 : ℝ) ≤ (n : ℝ) - (k : ℝ) := by
      have : (k : ℝ) ≤ (n : ℝ) := by exact_mod_cast hkn
      linarith
    calc ‖a k‖ * ‖b (n - k)‖
        ≤ (Ca * q ^ (s * (k : ℝ) ^ 2 / 2)) * (Cb * q ^ (t * ((n - k : ℕ) : ℝ) ^ 2 / 2)) :=
          mul_le_mul (hA k) (hB (n - k)) (norm_nonneg _)
            (by positivity)
      _ = Ca * Cb * (q ^ (s * (k : ℝ) ^ 2 / 2) * q ^ (t * ((n : ℝ) - (k : ℝ)) ^ 2 / 2)) := by
          rw [hcast]; ring
      _ = Ca * Cb * q ^ (s * (k : ℝ) ^ 2 / 2 + t * ((n : ℝ) - (k : ℝ)) ^ 2 / 2) := by
          rw [← Real.rpow_add hq0]
      _ ≤ Ca * Cb * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2) := by
          refine mul_le_mul_of_nonneg_left ?_ (by positivity)
          refine Real.rpow_le_rpow_of_exponent_le hq.le ?_
          have hbal := exponent_le_envelope s t (k := (k : ℝ)) (j := (n : ℝ) - (k : ℝ))
            (by positivity) hj
          have hsum : (k : ℝ) + ((n : ℝ) - (k : ℝ)) = (n : ℝ) := by ring
          rw [hsum] at hbal
          linarith
  refine (Finset.sum_le_sum hterm).trans (le_of_eq ?_)
  rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  push_cast
  ring

/-! The full law `cauchyMul_order` — both directions, for positive real
coefficients — is **proved** in MI-4 at the end of this file, once MI-3(c) has
supplied the `≤` half.  It is stated there rather than here only because its `≥`
half consumes the index-composition machinery of §MI-4. -/

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

/-! ### MI-3(c) — the `≤` direction of MI-2, discharged sorry-free

MI-3(a) above is exactly the `ε`-`δ` extraction that the `≤` direction of
`cauchyMul_order` cites.  Feeding it into `cauchyMul_norm_le_envelope` closes
that direction outright — arbitrary normed field, no positivity, no
non-cancellation.

Two steps.  `exists_global_gaussian_bound` upgrades MI-3(a)'s *eventual* bound to
a *global* one, absorbing the finite initial segment into the constant: the
convolution `∑_{k≤n} a_k b_{n−k}` runs over every index, so an eventual bound on
its own is not usable.  `cauchyMul_norm_eventually_le` then assembles — envelope
bound at the shifted slopes, `cauchyEnvelope_add_le` to push the two `ε/2`'s
through the envelope, and `eventually_linear_le_rpow_sq` to let the
super-exponential swallow the constants and the `(n+1)`.

Everything here is stated on **norms**, never on `logb`.  `Real.log 0 = 0` makes
`logb q ‖x‖` return `0` at `x = 0` — the junk value that
`cauchyMul_order_unhypothesised_false` exploits — and it would silently break a
`logb`-shaped upper bound whenever the envelope is negative, i.e. exactly in the
convergent q-Gevrey regime. -/

/-- **[MI-3(c), sorry-free] A Gaussian eventually swallows any linear function.**
`M·(n+1) ≤ q^{δn²/2}` eventually, for `q > 1` and `δ > 0`.

Elementary and Archimedean: for `n ≥ N` we have `δn²/2 ≥ (δN/2)·n`, so the
right-hand side dominates `r^n` with `r = q^{δN/2}`; `N` is chosen so that
`r − 1` exceeds twice the constant, and Bernoulli finishes. -/
theorem eventually_linear_le_rpow_sq {q δ M : ℝ} (hq : 1 < q) (hδ : 0 < δ) :
    ∀ᶠ n : ℕ in atTop, M * ((n : ℝ) + 1) ≤ q ^ (δ * (n : ℝ) ^ 2 / 2) := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hM'1 : (1 : ℝ) ≤ max M 1 := le_max_right _ _
  have hMM' : M ≤ max M 1 := le_max_left _ _
  have hr1 : (1 : ℝ) < q ^ (δ / 2) := by
    have := Real.rpow_lt_rpow_of_exponent_lt hq (show (0 : ℝ) < δ / 2 by linarith)
    simpa using this
  obtain ⟨N, hN⟩ := pow_unbounded_of_one_lt (2 * max M 1 + 1) hr1
  have hrN : (q ^ (δ / 2)) ^ N = q ^ (δ * (N : ℝ) / 2) := by
    rw [← Real.rpow_natCast (q ^ (δ / 2)) N, ← Real.rpow_mul hq0.le]
    congr 1
    ring
  rw [hrN] at hN
  have hrpos : (0 : ℝ) < q ^ (δ * (N : ℝ) / 2) := Real.rpow_pos_of_pos hq0 _
  filter_upwards [eventually_ge_atTop (max N 1)] with n hn
  have hnN : (N : ℝ) ≤ (n : ℝ) := by exact_mod_cast le_trans (le_max_left N 1) hn
  have hn1 : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast le_trans (le_max_right N 1) hn
  -- Bernoulli on the base `q^{δN/2}`
  have hbern : 1 + (n : ℝ) * (q ^ (δ * (N : ℝ) / 2) - 1)
      ≤ (q ^ (δ * (N : ℝ) / 2)) ^ n := by
    have h := one_add_mul_le_pow (a := q ^ (δ * (N : ℝ) / 2) - 1) (by linarith) n
    rwa [show (1 : ℝ) + (q ^ (δ * (N : ℝ) / 2) - 1) = q ^ (δ * (N : ℝ) / 2) by ring] at h
  -- the `n`-th power is an `rpow` with the smaller exponent `(δN/2)·n ≤ δn²/2`
  have hpow : (q ^ (δ * (N : ℝ) / 2)) ^ n ≤ q ^ (δ * (n : ℝ) ^ 2 / 2) := by
    rw [← Real.rpow_natCast (q ^ (δ * (N : ℝ) / 2)) n, ← Real.rpow_mul hq0.le]
    refine Real.rpow_le_rpow_of_exponent_le hq.le ?_
    nlinarith [mul_nonneg hδ.le
      (by nlinarith : (0 : ℝ) ≤ (n : ℝ) ^ 2 - (N : ℝ) * (n : ℝ))]
  -- arithmetic: `M(n+1) ≤ M'(n+1) ≤ 2M'n ≤ n(r−1) ≤ 1 + n(r−1)`
  have h1 : max M 1 ≤ max M 1 * (n : ℝ) := le_mul_of_one_le_right (by linarith) hn1
  have h2 : 2 * max M 1 * (n : ℝ) ≤ (n : ℝ) * (q ^ (δ * (N : ℝ) / 2) - 1) := by
    nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ (n : ℝ))
      (by linarith : (0 : ℝ) ≤ q ^ (δ * (N : ℝ) / 2) - 1 - 2 * max M 1)]
  have h3 : M * ((n : ℝ) + 1) ≤ max M 1 * ((n : ℝ) + 1) :=
    mul_le_mul_of_nonneg_right hMM' (by linarith)
  nlinarith

/-- **[MI-3(c), sorry-free] Limit form ⟹ GLOBAL Gaussian bound.**  MI-3(a) gives
the bound `‖a n‖ ≤ q^{(s+ε)n²/2}` only for large `n`; the Cauchy product needs it
for *every* `n`.  The upgrade is free: the finitely many exceptional indices are
absorbed into a constant `C` (here `1` plus the sum of the offending ratios,
which avoids a nonemptiness side-condition on a `Finset.sup'`).

`C > 0` and `1 ≤ C`, so the bound is also usable as a plain `q^{(s+ε)n²/2}`
majorant in the tail. -/
theorem exists_global_gaussian_bound {q s : ℝ} (hq : 1 < q) {a : ℕ → K}
    (ha : IsQGevreyOrder q s a) {ε : ℝ} (hε : 0 < ε) :
    ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, ‖a n‖ ≤ C * q ^ ((s + ε) * (n : ℝ) ^ 2 / 2) := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hlogq : 0 < Real.log q := Real.log_pos hq
  obtain ⟨N₀, hN₀⟩ := eventually_atTop.mp (order_eventually_le ha hε)
  have hnn : ∀ k : ℕ, (0 : ℝ) ≤ ‖a k‖ / q ^ ((s + ε) * (k : ℝ) ^ 2 / 2) := fun k =>
    div_nonneg (norm_nonneg _) (Real.rpow_pos_of_pos hq0 _).le
  refine ⟨1 + ∑ k ∈ Finset.range (max N₀ 1), ‖a k‖ / q ^ ((s + ε) * (k : ℝ) ^ 2 / 2),
    by linarith [Finset.sum_nonneg (fun k (_ : k ∈ Finset.range (max N₀ 1)) => hnn k)],
    fun n => ?_⟩
  have hsum := Finset.sum_nonneg (fun k (_ : k ∈ Finset.range (max N₀ 1)) => hnn k)
  rcases lt_or_ge n (max N₀ 1) with hlt | hge
  · -- initial segment: the constant already contains this very ratio
    have hsingle := Finset.single_le_sum (f := fun k : ℕ =>
      ‖a k‖ / q ^ ((s + ε) * (k : ℝ) ^ 2 / 2)) (fun k _ => hnn k) (Finset.mem_range.mpr hlt)
    rw [div_le_iff₀ (Real.rpow_pos_of_pos hq0 _)] at hsingle
    nlinarith [(Real.rpow_pos_of_pos hq0 ((s + ε) * (n : ℝ) ^ 2 / 2))]
  · -- tail: the defining limit gives the bound outright, with constant `1`
    have hn1 : 1 ≤ n := le_trans (le_max_right N₀ 1) hge
    have hn2 : (0 : ℝ) < (n : ℝ) ^ 2 := by
      have : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn1
      positivity
    have hbound := hN₀ n (le_trans (le_max_left N₀ 1) hge)
    unfold logb at hbound
    rw [div_le_iff₀ hn2] at hbound
    have hhalf : Real.log ‖a n‖ / Real.log q ≤ (s + ε) * (n : ℝ) ^ 2 / 2 := by linarith
    rw [div_le_iff₀ hlogq] at hhalf
    have hkey : ‖a n‖ ≤ q ^ ((s + ε) * (n : ℝ) ^ 2 / 2) := Real.le_rpow_of_log_le hq0 hhalf
    nlinarith [(Real.rpow_pos_of_pos hq0 ((s + ε) * (n : ℝ) ^ 2 / 2))]

/-- **[MI-3(c), sorry-free] THE `≤` DIRECTION OF MI-2.**  For every `ε > 0`,
eventually

    ‖(a ⋆ b)_n‖ ≤ q^{(E(s,t) + ε)·n²/2},        E = cauchyEnvelope.

This is the whole upper half of `cauchyMul_order`, over an arbitrary normed
field, with no positivity and no non-cancellation hypothesis — those are needed
only for the matching lower bound (MI-4). -/
theorem cauchyMul_norm_eventually_le {q s t : ℝ} (hq : 1 < q) {a b : ℕ → K}
    (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b) {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ n : ℕ in atTop,
      ‖cauchyMul a b n‖ ≤ q ^ ((cauchyEnvelope s t + ε) * (n : ℝ) ^ 2 / 2) := by
  have hq0 : (0 : ℝ) < q := by linarith
  obtain ⟨Ca, hCa, hA⟩ := exists_global_gaussian_bound hq ha (half_pos hε)
  obtain ⟨Cb, hCb, hB⟩ := exists_global_gaussian_bound hq hb (half_pos hε)
  filter_upwards [eventually_linear_le_rpow_sq (q := q) (δ := ε / 2) (M := Ca * Cb)
    hq (half_pos hε)] with n hn
  have hCC : (0 : ℝ) ≤ Ca * Cb * ((n : ℝ) + 1) :=
    mul_nonneg (mul_nonneg hCa.le hCb.le) (by positivity)
  have hshift : cauchyEnvelope (s + ε / 2) (t + ε / 2) ≤ cauchyEnvelope s t + ε / 2 :=
    cauchyEnvelope_add_le s t (by linarith)
  calc ‖cauchyMul a b n‖
      ≤ Ca * Cb * ((n : ℝ) + 1)
          * q ^ (cauchyEnvelope (s + ε / 2) (t + ε / 2) * (n : ℝ) ^ 2 / 2) :=
        cauchyMul_norm_le_envelope hq hCa.le hCb.le hA hB n
    _ ≤ Ca * Cb * ((n : ℝ) + 1)
          * q ^ ((cauchyEnvelope s t + ε / 2) * (n : ℝ) ^ 2 / 2) := by
        refine mul_le_mul_of_nonneg_left (Real.rpow_le_rpow_of_exponent_le hq.le ?_) hCC
        nlinarith [sq_nonneg ((n : ℝ))]
    _ ≤ q ^ (ε / 2 * (n : ℝ) ^ 2 / 2)
          * q ^ ((cauchyEnvelope s t + ε / 2) * (n : ℝ) ^ 2 / 2) :=
        mul_le_mul_of_nonneg_right hn (Real.rpow_pos_of_pos hq0 _).le
    _ = q ^ ((cauchyEnvelope s t + ε) * (n : ℝ) ^ 2 / 2) := by
        rw [← Real.rpow_add hq0]; congr 1; ring

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

/-! ## MI-4 — the `≥` direction, and the full convolution law

The `≤` direction (MI-3(c)) needed no positivity: it is an upper bound on a sum
of norms, so the triangle inequality does all the work.  The `≥` direction is
where positivity earns its place.  With `0 < a n` and `0 < b n` every summand of
`(a ⋆ b)_n = ∑_{k ≤ n} a_k b_{n−k}` is positive, so the sum **dominates each
individual term** — and it is then enough to name the term sitting at the
maximiser of `θ ↦ s θ² + t (1−θ)²`.

That collapses the Laplace/saddle argument into a composition of limits.  Along
`kₙ = ⌊θn⌋`,

    2·log_q(a_{kₙ}·b_{n−kₙ}) / n²
      = (2·log_q a_{kₙ} / kₙ²)·(kₙ/n)² + (2·log_q b_{n−kₙ} / (n−kₙ)²)·((n−kₙ)/n)²
      → s·θ² + t·(1−θ)²,

each factor by a limit already in hand: `tendsto_nat_floor_mul_div_atTop` for the
index ratios, the defining order limits reindexed along `kₙ → ∞` for the rest.

The maximiser is read straight off `cauchyEnvelope`'s closed form: an endpoint
`θ ∈ {0,1}` in the convex (`max`) branch, and `θ = t/(s+t)` in the concave
(harmonic) branch, where `s θ² + t (1−θ)² = st/(s+t)` exactly.  The degenerate
sub-cases of the concave branch (`s = 0`, `t = 0`, `s + t = 0`) all have envelope
`0` and are served by an endpoint choice, so no `θ` outside `[0,1]` is ever
formed and no division by `s + t = 0` is ever performed. -/

section LowerBound

variable {q s t : ℝ} {a b : ℕ → ℝ}

/-- Over `ℝ` a **positive** sequence's order can be stated without the norm. -/
theorem isQGevreyOrder_pos (hpos : ∀ n, 0 < a n) :
    IsQGevreyOrder q s a ↔
      Tendsto (fun n : ℕ => 2 * logb q (a n) / (n : ℝ) ^ 2) atTop (𝓝 s) := by
  have hfun : (fun n : ℕ => 2 * logb q ‖a n‖ / (n : ℝ) ^ 2)
      = fun n : ℕ => 2 * logb q (a n) / (n : ℝ) ^ 2 := by
    funext n; rw [Real.norm_of_nonneg (hpos n).le]
  unfold IsQGevreyOrder
  rw [hfun]

/-- The Cauchy product of positive sequences is positive. -/
theorem cauchyMul_pos (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n) (n : ℕ) :
    0 < cauchyMul a b n :=
  Finset.sum_pos (fun i _ => mul_pos (ha0 i) (hb0 _))
    ⟨0, Finset.mem_range.mpr n.succ_pos⟩

/-- **The sum dominates each of its terms.**  This is the *only* place positivity
is used, and it is what the whole `≥` direction rests on. -/
theorem term_le_cauchyMul (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n)
    {k n : ℕ} (hk : k ≤ n) : a k * b (n - k) ≤ cauchyMul a b n :=
  Finset.single_le_sum (f := fun i => a i * b (n - i))
    (fun i _ => (mul_pos (ha0 i) (hb0 _)).le) (Finset.mem_range.mpr (Nat.lt_succ_of_le hk))

private theorem logb_le_logb (hq : 1 < q) {x y : ℝ} (hx : 0 < x) (hxy : x ≤ y) :
    logb q x ≤ logb q y :=
  div_le_div_of_nonneg_right (Real.log_le_log hx hxy) (Real.log_pos hq).le

private theorem logb_mul' {x y : ℝ} (hx : x ≠ 0) (hy : y ≠ 0) :
    logb q (x * y) = logb q x + logb q y := by
  unfold logb; rw [Real.log_mul hx hy, add_div]

/-- A constant contributes nothing to the leading Gaussian coefficient — the
`n²` denominator washes it out.  This is what makes the endpoint cases
(`θ ∈ {0,1}`, where one index is frozen at `0`) work. -/
private theorem tendsto_logb_const (x : ℝ) :
    Tendsto (fun n : ℕ => 2 * logb q x / (n : ℝ) ^ 2) atTop (𝓝 0) :=
  Tendsto.div_atTop tendsto_const_nhds
    ((tendsto_pow_atTop (by norm_num : 2 ≠ 0)).comp tendsto_natCast_atTop_atTop)

/-- **Reindex an order limit along `u`, then rescale.**  If `uₙ → ∞` with
`uₙ/n → c`, the leading coefficient of `a` read at `uₙ` against `n²` converges to
`s·c²`.  This single computation is the whole interior (saddle) case. -/
private theorem tendsto_logb_comp
    (ha : Tendsto (fun n : ℕ => 2 * logb q (a n) / (n : ℝ) ^ 2) atTop (𝓝 s))
    {u : ℕ → ℕ} {c : ℝ} (hu : Tendsto u atTop atTop)
    (hratio : Tendsto (fun n : ℕ => ((u n : ℕ) : ℝ) / (n : ℝ)) atTop (𝓝 c)) :
    Tendsto (fun n : ℕ => 2 * logb q (a (u n)) / (n : ℝ) ^ 2) atTop (𝓝 (s * c ^ 2)) := by
  have h1 : Tendsto (fun n : ℕ => 2 * logb q (a (u n)) / ((u n : ℕ) : ℝ) ^ 2)
      atTop (𝓝 s) := ha.comp hu
  have h2 : Tendsto (fun n : ℕ => (((u n : ℕ) : ℝ) / (n : ℝ)) ^ 2) atTop (𝓝 (c ^ 2)) :=
    hratio.pow 2
  refine Tendsto.congr' ?_ (h1.mul h2)
  filter_upwards [hu.eventually_ge_atTop 1, eventually_ge_atTop 1] with n hun hn
  have hu0 : ((u n : ℕ) : ℝ) ≠ 0 := by
    have : (0 : ℝ) < ((u n : ℕ) : ℝ) := by exact_mod_cast hun
    exact ne_of_gt this
  have hn0 : ((n : ℝ)) ≠ 0 := by
    have : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn
    exact ne_of_gt this
  field_simp

/-- The two index contributions add, because `log` turns the selected term's
product into a sum (both factors are positive). -/
private theorem tendsto_term (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n)
    (k : ℕ → ℕ) {ca cb : ℝ}
    (hA : Tendsto (fun n : ℕ => 2 * logb q (a (k n)) / (n : ℝ) ^ 2) atTop (𝓝 ca))
    (hB : Tendsto (fun n : ℕ => 2 * logb q (b (n - k n)) / (n : ℝ) ^ 2) atTop (𝓝 cb)) :
    Tendsto (fun n : ℕ => 2 * logb q (a (k n) * b (n - k n)) / (n : ℝ) ^ 2)
      atTop (𝓝 (ca + cb)) := by
  refine Tendsto.congr' ?_ (hA.add hB)
  filter_upwards with n
  rw [logb_mul' (ne_of_gt (ha0 _)) (ne_of_gt (hb0 _))]
  ring

/-- Monotonicity of `log_q` transports "the sum dominates the term" to the
leading coefficients. -/
private theorem term_coeff_le (hq : 1 < q) (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n)
    {k : ℕ → ℕ} (hk : ∀ n, k n ≤ n) (n : ℕ) :
    2 * logb q (a (k n) * b (n - k n)) / (n : ℝ) ^ 2
      ≤ 2 * logb q (cauchyMul a b n) / (n : ℝ) ^ 2 := by
  have h := logb_le_logb hq (mul_pos (ha0 (k n)) (hb0 (n - k n)))
    (term_le_cauchyMul ha0 hb0 (hk n))
  exact div_le_div_of_nonneg_right (by linarith) (sq_nonneg _)

/-- MI-3(c) restated on the leading coefficient rather than the norm — legitimate
here because the convolution of positive sequences is positive, so no `log 0`
junk value can intervene. -/
private theorem cauchyMul_coeff_le (hq : 1 < q) (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n)
    (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b) {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ n : ℕ in atTop,
      2 * logb q (cauchyMul a b n) / (n : ℝ) ^ 2 ≤ cauchyEnvelope s t + ε := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hlogq : 0 < Real.log q := Real.log_pos hq
  filter_upwards [cauchyMul_norm_eventually_le hq ha hb hε, eventually_ge_atTop 1] with n hn hn1
  have hpos := cauchyMul_pos ha0 hb0 n
  rw [Real.norm_of_nonneg hpos.le] at hn
  have hlog : Real.log (cauchyMul a b n)
      ≤ ((cauchyEnvelope s t + ε) * (n : ℝ) ^ 2 / 2) * Real.log q := by
    have h := Real.log_le_log hpos hn
    rwa [Real.log_rpow hq0] at h
  have hn2 : (0 : ℝ) < (n : ℝ) ^ 2 := by
    have : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn1
    positivity
  unfold logb
  rw [div_le_iff₀ hn2]
  have := (div_le_iff₀ hlogq).mpr hlog
  linarith

end LowerBound

/-- **[MI-2 — PROVED] Convolution order = envelope, for positive real
coefficients.**  Under the Cauchy product the q-Gevrey order is the
dominant-balance ENVELOPE `cauchyEnvelope s t` (`= max s t` when not both `≤ 0`;
`= s·t/(s+t)` when both `≤ 0`), NOT the additive `s + t` of the MI-1 stub.

**Positivity is not decoration.**  Without it the statement is false — see
`cauchyMul_order_unhypothesised_false` — and `0 < a n`, `0 < b n` is the exact
regime the MI-2 numerics were run in.  It makes every summand of
`(a ⋆ b)_n = ∑_k a_k b_{n-k}` positive, which is what both halves need: no
cancellation, and a sum that dominates each of its own terms.

**Proof shape.**  `≤` is MI-3(c) (`cauchyMul_norm_eventually_le`), which needs
neither positivity nor `ℝ`.  `≥` selects the single term at the envelope's
maximiser and reads off its leading coefficient by composition of limits (§MI-4).
The two are glued by `tendsto_order`.

Checked at the small instances the MI-2 numerics report: `(-1,-1) ↦ -0.5`,
`(-2,-1) ↦ -2/3`, `(2,1) ↦ 2`, `(-3,1) ↦ 1`. -/
theorem cauchyMul_order {q s t : ℝ} {a b : ℕ → ℝ}
    (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b)
    (hq : 1 < q) (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n) :
    IsQGevreyOrder q (cauchyEnvelope s t) (cauchyMul a b) := by
  -- Ref: [ramis-sauloy-zhang2013] Newton-polygon / dominant-balance slopes of
  --      q-difference systems.
  have haR := (isQGevreyOrder_pos ha0).mp ha
  have hbR := (isQGevreyOrder_pos hb0).mp hb
  -- the endpoint selections, used by every degenerate branch
  have hzero : Tendsto
      (fun n : ℕ => 2 * logb q (a ((fun _ : ℕ => 0) n) * b (n - (fun _ : ℕ => 0) n))
        / (n : ℝ) ^ 2) atTop (𝓝 (0 + t)) :=
    tendsto_term ha0 hb0 (fun _ => 0) (tendsto_logb_const (a 0)) (by simpa using hbR)
  have hfull : Tendsto
      (fun n : ℕ => 2 * logb q (a ((fun n : ℕ => n) n) * b (n - (fun n : ℕ => n) n))
        / (n : ℝ) ^ 2) atTop (𝓝 (s + 0)) :=
    tendsto_term ha0 hb0 (fun n => n) haR (by simpa using tendsto_logb_const (q := q) (b 0))
  -- the selected term, and the limit of its leading coefficient
  obtain ⟨k, hk, hterm⟩ :
      ∃ k : ℕ → ℕ, (∀ n, k n ≤ n) ∧
        Tendsto (fun n : ℕ => 2 * logb q (a (k n) * b (n - k n)) / (n : ℝ) ^ 2)
          atTop (𝓝 (cauchyEnvelope s t)) := by
    by_cases hcc : s ≤ 0 ∧ t ≤ 0
    · -- concave branch: envelope is the harmonic combination `s·t/(s+t)`
      obtain ⟨hs, ht⟩ := hcc
      have hE : cauchyEnvelope s t = s * t / (s + t) := by
        unfold cauchyEnvelope; exact if_pos ⟨hs, ht⟩
      rw [hE]
      rcases eq_or_lt_of_le (add_nonpos hs ht) with hst0 | hstneg
      · -- `s + t = 0` with both `≤ 0` forces `s = t = 0`, envelope `0/0 = 0`
        have hs0 : s = 0 := by linarith
        have ht0 : t = 0 := by linarith
        subst hs0; subst ht0
        exact ⟨fun _ => 0, fun n => Nat.zero_le n, by simpa using hzero⟩
      · rcases eq_or_lt_of_le ht with ht0 | htneg
        · -- `t = 0`: envelope `= 0`, frozen index `0` (contributes `0 + t = 0`)
          refine ⟨fun _ => 0, fun n => Nat.zero_le n, ?_⟩
          rw [show s * t / (s + t) = 0 + t by rw [ht0]; simp]
          exact hzero
        · rcases eq_or_lt_of_le hs with hs0 | hsneg
          · -- `s = 0`: envelope `= 0`, frozen index `n` (contributes `s + 0 = 0`)
            refine ⟨fun n => n, fun n => le_refl n, ?_⟩
            rw [show s * t / (s + t) = s + 0 by rw [hs0]; simp]
            exact hfull
          · -- the genuine interior saddle: `θ = t/(s+t) ∈ (0,1)`
            set θ : ℝ := t / (s + t) with hθdef
            have hstne : s + t ≠ 0 := ne_of_lt hstneg
            have hθ0 : 0 < θ := div_pos_of_neg_of_neg htneg hstneg
            have hθ1 : θ < 1 := by
              rw [hθdef, div_lt_one_iff]
              exact Or.inr (Or.inr ⟨hstneg, by linarith⟩)
            have hfloor_le : ∀ n : ℕ, ⌊θ * (n : ℝ)⌋₊ ≤ n := by
              intro n
              have hle : θ * (n : ℝ) ≤ (n : ℝ) := by
                nlinarith [Nat.cast_nonneg (α := ℝ) n]
              calc ⌊θ * (n : ℝ)⌋₊ ≤ ⌊((n : ℕ) : ℝ)⌋₊ := Nat.floor_le_floor hle
                _ = n := Nat.floor_natCast n
            refine ⟨fun n => ⌊θ * (n : ℝ)⌋₊, hfloor_le, ?_⟩
            -- index ratios
            have hratioA : Tendsto (fun n : ℕ => ((⌊θ * (n : ℝ)⌋₊ : ℕ) : ℝ) / (n : ℝ))
                atTop (𝓝 θ) :=
              (tendsto_nat_floor_mul_div_atTop (R := ℝ) hθ0.le).comp
                tendsto_natCast_atTop_atTop
            have hratioB : Tendsto
                (fun n : ℕ => ((n - ⌊θ * (n : ℝ)⌋₊ : ℕ) : ℝ) / (n : ℝ))
                atTop (𝓝 (1 - θ)) := by
              refine Tendsto.congr' ?_ ((tendsto_const_nhds (x := (1 : ℝ))).sub hratioA)
              filter_upwards [eventually_ge_atTop 1] with n hn
              have hn0 : ((n : ℝ)) ≠ 0 := by
                have : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn
                exact ne_of_gt this
              rw [Nat.cast_sub (hfloor_le n)]
              field_simp
            -- both indices tend to infinity
            have huA : Tendsto (fun n : ℕ => ⌊θ * (n : ℝ)⌋₊) atTop atTop :=
              tendsto_nat_floor_atTop.comp
                (Tendsto.const_mul_atTop hθ0 tendsto_natCast_atTop_atTop)
            have huB : Tendsto (fun n : ℕ => n - ⌊θ * (n : ℝ)⌋₊) atTop atTop := by
              refine (tendsto_natCast_atTop_iff (R := ℝ)).mp ?_
              refine tendsto_atTop_mono (f := fun n : ℕ => (1 - θ) * (n : ℝ)) (fun n => ?_)
                (Tendsto.const_mul_atTop (by linarith) tendsto_natCast_atTop_atTop)
              rw [Nat.cast_sub (hfloor_le n)]
              have := Nat.floor_le (mul_nonneg hθ0.le (Nat.cast_nonneg (α := ℝ) n))
              nlinarith
            -- the saddle value is exactly the harmonic envelope
            have hval : s * θ ^ 2 + t * (1 - θ) ^ 2 = s * t / (s + t) := by
              rw [hθdef]; field_simp; ring
            rw [← hval]
            exact tendsto_term ha0 hb0 _
              (tendsto_logb_comp haR huA hratioA) (tendsto_logb_comp hbR huB hratioB)
    · -- convex branch: envelope is `max s t`, maximised at an endpoint
      have hE : cauchyEnvelope s t = max s t := by
        unfold cauchyEnvelope; exact if_neg hcc
      rw [hE]
      rcases le_total t s with hts | hst
      · rw [max_eq_left hts]
        exact ⟨fun n => n, fun n => le_refl n, by simpa using hfull⟩
      · rw [max_eq_right hst]
        exact ⟨fun _ => 0, fun n => Nat.zero_le n, by simpa using hzero⟩
  -- squeeze: the term bounds below, MI-3(c) bounds above
  rw [isQGevreyOrder_pos (fun n => cauchyMul_pos ha0 hb0 n)]
  refine tendsto_order.2 ⟨fun c hc => ?_, fun c hc => ?_⟩
  · filter_upwards [hterm.eventually (Ioi_mem_nhds hc)] with n hn
    exact lt_of_lt_of_le hn (term_coeff_le hq ha0 hb0 hk n)
  · filter_upwards [cauchyMul_coeff_le hq ha0 hb0 ha hb
      (show (0 : ℝ) < (c - cauchyEnvelope s t) / 2 by linarith)] with n hn
    linarith

end QOU.Mathlib.QGevreyOrder
