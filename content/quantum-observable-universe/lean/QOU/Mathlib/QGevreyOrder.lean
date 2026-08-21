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

/-- **[MI-2, sorry-free] Envelope shift bound.**  Raising both slopes by the same
    `δ ≥ 0` raises the envelope by at most `δ`.

    This is the algebraic core of the `ε`-`δ` step: passing from the limit form
    to a bound costs an `ε` in each slope, and this lemma says that costs at most
    `ε` in the envelope — so the two forms have the same envelope in the limit.
    Conceptually it is `sup_θ((s+δ)θ² + (t+δ)(1−θ)²) ≤ sup_θ(sθ² + t(1−θ)²) + δ`,
    since `θ² + (1−θ)² ≤ 1` on `[0,1]`; proved here directly from the closed
    form, which is why it is a four-way case split rather than one line. -/
theorem envelope_shift_le (s t δ : ℝ) (hδ : 0 ≤ δ) :
    cauchyEnvelope (s + δ) (t + δ) ≤ cauchyEnvelope s t + δ := by
  unfold cauchyEnvelope
  split_ifs with h1 h2 h2
  · -- both shifted ≤ 0 and both unshifted ≤ 0: harmonic vs harmonic
    obtain ⟨hu, hv⟩ := h1
    obtain ⟨hs, ht⟩ := h2
    rcases (add_nonpos hs ht).lt_or_eq with hd1 | hd1
    · -- s + t < 0
      rcases (by linarith : s + δ + (t + δ) ≤ 0).lt_or_eq with hd2 | hd2
      · have hne : s + t ≠ 0 := ne_of_lt hd1
        have hA : s * t / (s + t) * (s + t) = s * t := div_mul_cancel₀ _ hne
        rw [div_le_iff_of_neg (by linarith : s + δ + (t + δ) < 0)]
        nlinarith [mul_nonneg (neg_nonneg.mpr hv) (neg_nonneg.mpr hs),
                   mul_nonneg (neg_nonneg.mpr hu) (neg_nonneg.mpr ht), hA, hδ]
      · -- the shifted slopes sum to 0, so both are 0 and the LHS is 0/0 = 0
        have hu0 : s + δ = 0 := le_antisymm hu (by linarith)
        have hv0 : t + δ = 0 := le_antisymm hv (by linarith)
        have hδ0 : 0 < δ := by linarith
        have hst : s * t / (s + t) = -(δ / 2) := by
          have hs' : s = -δ := by linarith
          have ht' : t = -δ := by linarith
          rw [hs', ht', show (-δ) * (-δ) = δ * δ by ring,
            show (-δ) + (-δ) = -(2 * δ) by ring]
          field_simp
        rw [hu0, hv0, hst]
        norm_num
        linarith
    · -- s + t = 0 with s, t ≤ 0 forces s = t = 0, hence δ = 0
      have hs0 : s = 0 := by linarith
      have ht0 : t = 0 := by linarith
      have hδ0 : δ = 0 := by rw [hs0] at hu; linarith
      subst hs0; subst ht0; subst hδ0; simp
  · -- shifted both ≤ 0 but unshifted not: impossible, since δ ≥ 0
    exact absurd ⟨by linarith [h1.1], by linarith [h1.2]⟩ h2
  · -- shifted not both ≤ 0, unshifted both ≤ 0: max ≤ harmonic + δ
    obtain ⟨hs, ht⟩ := h2
    rcases (add_nonpos hs ht).lt_or_eq with hd1 | hd1
    · have hne : s + t ≠ 0 := ne_of_lt hd1
      have hA : s * t / (s + t) * (s + t) = s * t := div_mul_cancel₀ _ hne
      -- `s ≤ st/(s+t)`: multiplying by `s + t < 0` reduces it to `0 ≤ s²`.
      have hsA : s ≤ s * t / (s + t) := by nlinarith [hA, hd1, sq_nonneg s]
      have htA : t ≤ s * t / (s + t) := by nlinarith [hA, hd1, sq_nonneg t]
      rw [max_add_add_right]
      have := max_le hsA htA
      linarith
    · have hs0 : s = 0 := by linarith
      have ht0 : t = 0 := by linarith
      subst hs0; subst ht0; simp
  · -- neither both ≤ 0: max shifts by exactly δ
    rw [max_add_add_right]

/-- **Bound form of q-Gevrey growth.**  `‖a n‖ ≤ C·Aⁿ·q^{s n²/2}` — the
    "ALTERNATIVE (bound form)" of the header, made a definition.  Unlike
    `IsQGevreyOrder` this is finitary (no filter, no `log`), which is exactly why
    the `≤` half of the convolution law is provable outright in this form. -/
def QGevreyBound (q s : ℝ) (a : ℕ → K) : Prop :=
  ∃ C A : ℝ, 0 < C ∧ 0 < A ∧ ∀ n : ℕ, ‖a n‖ ≤ C * A ^ n * q ^ (s * (n : ℝ) ^ 2 / 2)

/-- **[MI-2, sorry-free] The `≤` direction of the convolution law.**  In bound
    form the upper half of `cauchyMul_order` holds **unconditionally** — no
    non-cancellation hypothesis, because bounding a sum of norms never needs to
    know that the terms fail to cancel.

    This is the half that survives the counterexample: only the `≥` direction
    was false. The proof is the docstring's own recipe with nothing deferred —
    `cauchyMul_norm_le_sum` for the triangle bound, `exponent_le_envelope` on
    each summand's Gaussian exponent, and the `(n+1)` term count absorbed into
    the geometric factor via `n + 1 ≤ 2ⁿ`. -/
theorem cauchyMul_bound {q s t : ℝ} {a b : ℕ → K} (hq : 1 < q)
    (ha : QGevreyBound q s a) (hb : QGevreyBound q t b) :
    QGevreyBound q (cauchyEnvelope s t) (cauchyMul a b) := by
  obtain ⟨Ca, Aa, hCa, hAa, ha⟩ := ha
  obtain ⟨Cb, Ab, hCb, hAb, hb⟩ := hb
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have hq1 : (1 : ℝ) ≤ q := le_of_lt hq
  set M := max Aa Ab with hMdef
  have hM0 : 0 < M := lt_of_lt_of_le hAa (le_max_left _ _)
  refine ⟨Ca * Cb, 2 * M, by positivity, by positivity, ?_⟩
  intro n
  -- Each summand is bounded by the same envelope-exponent expression.
  have hterm : ∀ k ∈ Finset.range (n + 1),
      ‖a k‖ * ‖b (n - k)‖
        ≤ Ca * Cb * M ^ n * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2) := by
    intro k hk
    have hkn : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
    have hcast : ((n - k : ℕ) : ℝ) = (n : ℝ) - (k : ℝ) := by
      rw [Nat.cast_sub hkn]
    -- Gaussian exponents: dominant balance.
    have hexp : s * (k : ℝ) ^ 2 / 2 + t * ((n - k : ℕ) : ℝ) ^ 2 / 2
        ≤ cauchyEnvelope s t * (n : ℝ) ^ 2 / 2 := by
      have hle := exponent_le_envelope s t (k := (k : ℝ)) (j := ((n - k : ℕ) : ℝ))
        (Nat.cast_nonneg k) (Nat.cast_nonneg _)
      have hsum : (k : ℝ) + ((n - k : ℕ) : ℝ) = (n : ℝ) := by rw [hcast]; ring
      rw [hsum] at hle
      linarith
    -- Geometric factors: both bounded by the common ratio M.
    have hgeo : Aa ^ k * Ab ^ (n - k) ≤ M ^ n := by
      calc Aa ^ k * Ab ^ (n - k)
          ≤ M ^ k * M ^ (n - k) :=
            mul_le_mul (pow_le_pow_left₀ hAa.le (le_max_left _ _) k)
              (pow_le_pow_left₀ hAb.le (le_max_right _ _) _) (by positivity) (by positivity)
        _ = M ^ n := by rw [← pow_add, Nat.add_sub_cancel' hkn]
    calc ‖a k‖ * ‖b (n - k)‖
        ≤ (Ca * Aa ^ k * q ^ (s * (k : ℝ) ^ 2 / 2))
            * (Cb * Ab ^ (n - k) * q ^ (t * ((n - k : ℕ) : ℝ) ^ 2 / 2)) :=
          mul_le_mul (ha k) (hb (n - k)) (norm_nonneg _) (by positivity)
      _ = (Ca * Cb) * (Aa ^ k * Ab ^ (n - k))
            * q ^ (s * (k : ℝ) ^ 2 / 2 + t * ((n - k : ℕ) : ℝ) ^ 2 / 2) := by
          rw [Real.rpow_add hq0]; ring
      _ ≤ (Ca * Cb) * M ^ n * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2) := by
          have h1 : q ^ (s * (k : ℝ) ^ 2 / 2 + t * ((n - k : ℕ) : ℝ) ^ 2 / 2)
              ≤ q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2) :=
            Real.rpow_le_rpow_of_exponent_le hq1 hexp
          have h2 : (0 : ℝ) ≤ Ca * Cb := by positivity
          have h3 : (0 : ℝ) ≤ q ^ (s * (k : ℝ) ^ 2 / 2 + t * ((n - k : ℕ) : ℝ) ^ 2 / 2) :=
            Real.rpow_nonneg hq0.le _
          exact mul_le_mul (mul_le_mul_of_nonneg_left hgeo h2) h1 h3 (by positivity)
  -- The term count `n + 1 ≤ 2ⁿ` is absorbed into the geometric factor.
  have hcount : ((n : ℝ) + 1) ≤ (2 : ℝ) ^ n := by
    have := Nat.lt_two_pow_self (n := n)
    have : (n : ℝ) + 1 ≤ ((2 ^ n : ℕ) : ℝ) := by exact_mod_cast this
    simpa using this
  calc ‖cauchyMul a b n‖
      ≤ ∑ k ∈ Finset.range (n + 1), ‖a k‖ * ‖b (n - k)‖ := cauchyMul_norm_le_sum a b n
    _ ≤ ∑ _k ∈ Finset.range (n + 1),
          Ca * Cb * M ^ n * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2) :=
        Finset.sum_le_sum hterm
    _ = ((n : ℝ) + 1) * (Ca * Cb * M ^ n * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2)) := by
        rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]; push_cast; ring
    _ ≤ Ca * Cb * (2 * M) ^ n * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2) := by
        have hbase : (0 : ℝ) ≤ Ca * Cb * M ^ n
            * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2) := by
          have := Real.rpow_nonneg hq0.le (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2)
          positivity
        rw [mul_pow]
        have hrw : Ca * Cb * ((2 : ℝ) ^ n * M ^ n)
            * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2)
            = (2 : ℝ) ^ n * (Ca * Cb * M ^ n
                * q ^ (cauchyEnvelope s t * (n : ℝ) ^ 2 / 2)) := by ring
        rw [hrw]
        exact mul_le_mul_of_nonneg_right hcount hbase

/-- **Non-cancellation of the dominant convolution term.**  There is a fixed
    `c > 0` such that, eventually, the convolution dominates *every* one of its
    own summands: `c·‖a_k‖·‖b_{n−k}‖ ≤ ‖(a⋆b)_n‖` for all `k ≤ n`.

    This is the hypothesis the `≥` direction of the order law needs, and it is a
    genuine hypothesis, not bookkeeping: it constrains only the *norm* of the
    product against the norms of its summands, saying nothing about the product's
    order, so assuming it does not assume the conclusion.  In a general normed
    field the summands can cancel; `not_noCancellation_of_cauchyMul_eventually_zero`
    below is the extreme case, and `q^{n²} ⋆ (q^{n²})⁻¹` realises it. -/
def NoCancellation (a b : ℕ → K) : Prop :=
  ∃ c > 0, ∀ᶠ n in atTop, ∀ k ∈ Finset.range (n + 1),
    c * (‖a k‖ * ‖b (n - k)‖) ≤ ‖cauchyMul a b n‖

/-- **The non-cancellation hypothesis has teeth.**  If the convolution
    eventually vanishes while some summand does not, `NoCancellation` fails —
    so it is not satisfied automatically, and the `≥` direction genuinely
    depends on it.

    This is the shape of the counterexample recorded in
    `computations/qbeta/cauchymul_order_cancellation_witness.py`: taking
    `a n = q^{n²}` (positive order) and `b` its formal inverse (the computation
    shows `log_q‖b n‖/n² → 1`, so `b` carries the SAME positive order), the
    Cauchy product is the unit sequence `(1,0,0,…)` — order `0`, while
    `cauchyEnvelope s t > 0` for `s, t > 0`.  Two factors of equal positive
    order whose product has order `0`. -/
theorem not_noCancellation_of_cauchyMul_eventually_zero {a b : ℕ → K}
    (hz : ∀ᶠ n in atTop, cauchyMul a b n = 0)
    (hne : ∀ᶠ n in atTop, ∃ k ∈ Finset.range (n + 1), a k * b (n - k) ≠ 0) :
    ¬ NoCancellation a b := by
  rintro ⟨c, hc, hbound⟩
  obtain ⟨n, ⟨hzn, hnen⟩, hbn⟩ := ((hz.and hne).and hbound).exists
  obtain ⟨k, hk, hkne⟩ := hnen
  have hpos : 0 < ‖a k‖ * ‖b (n - k)‖ := by
    rw [← norm_mul]; exact norm_pos_iff.mpr hkne
  have := hbn k hk
  rw [hzn, norm_zero] at this
  exact absurd this (not_le.mpr (mul_pos hc hpos))

/-- **[MI-2, analytic — residual cited `sorry`] Convolution order = envelope,
    given non-cancellation.**  Under the Cauchy product the q-Gevrey order is the
    dominant-balance ENVELOPE `cauchyEnvelope s t` (`= max s t` when not both
    `≤ 0`; `= s·t/(s+t)` when both `≤ 0`), NOT the additive `s + t` of the MI-1
    stub.

    **`hnc` is load-bearing and was added 2026-08-08 to repair a FALSE
    statement.**  This theorem previously carried no such hypothesis, and in that
    form it is refuted by `a n = q^{n²}` together with its formal inverse: both
    have the same positive order, yet `a ⋆ b` is the unit sequence, of order `0`.
    The refutation is normalization-robust — whatever positive order the
    convention assigns `a`, it assigns the same to `b`, and `cauchyEnvelope` is
    positive on `s, t > 0` — so no rescaling of the definition rescues it.
    Witness: `computations/qbeta/cauchymul_order_cancellation_witness.py`;
    the failure of `hnc` on that pair is
    `not_noCancellation_of_cauchyMul_eventually_zero`.

    What remains deferred is analytic, not a question of what is true.  The `≤`
    direction is unconditional and now proved sorry-free, in bound form, as
    `cauchyMul_bound` above; `envelope_shift_le` is the algebraic step that
    carries a bound back to the limit form.  The residual is the `≥` half: pick
    `k ≈ θ*·n` attaining the envelope, then apply `hnc` to transfer that single
    summand's growth to the convolution. -/
theorem cauchyMul_order {q s t : ℝ} {a b : ℕ → K}
    (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b)
    (hq : 1 < q) (hnc : NoCancellation a b) :
    IsQGevreyOrder q (cauchyEnvelope s t) (cauchyMul a b) := by
  -- Ref: [ramis-sauloy-zhang2013] Newton-polygon / dominant-balance slopes of
  --      q-difference systems.  Upper: cauchyMul_order_le (sorry-free).
  --      Lower: hnc applied at k ≈ θ*·n, where θ* attains the envelope.
  -- SORRY: needs the ≥ half — attainment of the sup at a near-optimal index,
  --        then hnc to transfer that summand's growth to the convolution.
  sorry

/-- **[MI-2, sorry-free] Endpoint `≥`-brick for the convolution order law.**
    The lower (`≥`) half of `cauchyMul_order`, discharged unconditionally at the
    **`k = n` endpoint** — the pick that attains the envelope `max s t` when `a`
    dominates (`t ≤ s`, so `cauchyEnvelope s t = s`).

    Given the non-cancellation hypothesis `hnc`, a nonzero constant term
    `b 0 ≠ 0`, and `a` eventually nonzero, the leading Gaussian coefficient of
    `a ⋆ b` is eventually `≥ s − ε`.  The single summand `a n · b 0` already
    grows like `q^{s n²/2}`, and `hnc` transfers that growth to the whole
    convolution: `‖(a⋆b)_n‖ ≥ c·‖a_n‖·‖b_0‖`, whence

    `2·log_q‖(a⋆b)_n‖/n² ≥ 2·log_q‖a_n‖/n² + 2(log_q c + log_q‖b_0‖)/n² → s`,

    the second term being `O(1/n²)`.  This closes the `θ* = 1` pick the general
    `cauchyMul_order` `sorry` cites, for the physically relevant `s`-dominant
    positive-order regime (e.g. a Route-B kernel of order `½` against a
    lower-order factor).  It does **not** close the general theorem: the
    interior-optimum case (both orders `≤ 0`, envelope `s t/(s+t)`) still needs a
    near-optimal `k ≈ θ*·n` argument.  Companion of `order_eventually_ge`. -/
theorem cauchyMul_leadingCoeff_ge_endpoint {q s : ℝ} {a b : ℕ → K}
    (ha : IsQGevreyOrder q s a) (hq : 1 < q) (hnc : NoCancellation a b)
    (hb0 : b 0 ≠ 0) (ha0 : ∀ᶠ n in atTop, a n ≠ 0) {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ n in atTop, s - ε ≤ 2 * logb q ‖cauchyMul a b n‖ / (n : ℝ) ^ 2 := by
  obtain ⟨c, hc, hbound⟩ := hnc
  have hlogq : 0 < Real.log q := Real.log_pos hq
  have hb0n : 0 < ‖b 0‖ := norm_pos_iff.mpr hb0
  -- The constant contribution `M/n² → 0`.
  set M : ℝ := 2 * (logb q c + logb q ‖b 0‖) with hM
  have hsq : Tendsto (fun n : ℕ => (n : ℝ) ^ 2) atTop atTop :=
    (tendsto_pow_atTop (by norm_num : (2 : ℕ) ≠ 0)).comp tendsto_natCast_atTop_atTop
  have hKtend : Tendsto (fun n : ℕ => M / (n : ℝ) ^ 2) atTop (𝓝 0) := by
    have hinv : Tendsto (fun n : ℕ => ((n : ℝ) ^ 2)⁻¹) atTop (𝓝 0) :=
      tendsto_inv_atTop_zero.comp hsq
    have := hinv.const_mul M
    simpa [div_eq_mul_inv] using this
  have hCsmall : ∀ᶠ n : ℕ in atTop, -(ε / 2) ≤ M / (n : ℝ) ^ 2 := by
    have hnhds : ∀ᶠ x : ℝ in 𝓝 (0 : ℝ), -(ε / 2) ≤ x := by
      filter_upwards [Ioi_mem_nhds (show -(ε / 2) < (0 : ℝ) by linarith)] with x hx
        using le_of_lt hx
    exact hKtend.eventually hnhds
  -- eventual lower bound on `a`'s leading coefficient (as in `order_eventually_ge`,
  -- inlined here since that lemma is stated below this one).
  have hA : ∀ᶠ n : ℕ in atTop, s - ε / 2 ≤ 2 * logb q ‖a n‖ / (n : ℝ) ^ 2 := by
    have hmem : ∀ᶠ y : ℝ in 𝓝 s, s - ε / 2 ≤ y := by
      filter_upwards [Ioi_mem_nhds (show s - ε / 2 < s by linarith)] with y hy
        using le_of_lt hy
    exact ha.eventually hmem
  filter_upwards [hA, hCsmall, ha0, hbound, eventually_ge_atTop 1]
    with n hAn hCn han hbn hn1
  have hnpos : (0 : ℝ) < (n : ℝ) := by
    have : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn1
    linarith
  have hn2 : (0 : ℝ) < (n : ℝ) ^ 2 := by positivity
  have han' : 0 < ‖a n‖ := norm_pos_iff.mpr han
  -- `hnc` at `k = n` transfers the endpoint summand's growth.
  have key : c * (‖a n‖ * ‖b 0‖) ≤ ‖cauchyMul a b n‖ := by
    have h := hbn n (Finset.self_mem_range_succ n)
    rwa [Nat.sub_self] at h
  have hpos : 0 < c * (‖a n‖ * ‖b 0‖) := by positivity
  -- `logb` is monotone (division by `Real.log q > 0`).
  have hlogmono : logb q (c * (‖a n‖ * ‖b 0‖)) ≤ logb q ‖cauchyMul a b n‖ := by
    unfold logb
    rw [div_eq_mul_inv, div_eq_mul_inv]
    exact mul_le_mul_of_nonneg_right (Real.log_le_log hpos key)
      (le_of_lt (inv_pos.mpr hlogq))
  -- `log` splits the positive product.
  have hsplit : logb q (c * (‖a n‖ * ‖b 0‖))
      = logb q c + logb q ‖a n‖ + logb q ‖b 0‖ := by
    unfold logb
    rw [Real.log_mul (ne_of_gt hc) (mul_pos han' hb0n).ne',
        Real.log_mul han'.ne' hb0n.ne']
    ring
  have hnum : 2 * logb q ‖a n‖ + M ≤ 2 * logb q ‖cauchyMul a b n‖ := by
    have heq : 2 * logb q ‖a n‖ + M = 2 * logb q (c * (‖a n‖ * ‖b 0‖)) := by
      rw [hM, hsplit]; ring
    rw [heq]; linarith [hlogmono]
  -- Combine over the common `n²` denominator.
  rw [le_div_iff₀ hn2] at hAn hCn ⊢
  nlinarith [hAn, hCn, hnum]

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
    order — the compiled half of the numerical probe.

    **CORRECTED 2026-08-08 (bean `qou-slpd` item 5).** This theorem's `s = ½` is
    the Route-B kernel's q-Gevrey **order**, and the docstring used to call the
    missing piece "the RSZ slope=order theorem". There is no such theorem: the
    Newton slope is the **level** (see §MI-3(d) below — the slope-`k` family
    separates order from level, and the level tracks the slope). So this bridge
    reaches the right *number* `½` by the wrong route. The correct grounding of
    `ThetaSlopeArithmetic.c1Slope = ½` is the C1 `∞`-side **level**, which is
    `c1InfCoeff_order_two` restated via `isQGevreyLevel_of_order`. Nothing
    downstream changes — Door-i needs only that the two slope multisets differ
    (`ThetaSlopeArithmetic.newtonSlopes_c1_ne_ggm`) — but the statement below
    should be read as a numerical coincidence of two `½`s, not as a slope
    identification. -/
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

/-! ## MI-3(d): the Newton slope is the q-Gevrey LEVEL, not the order

Bean `qou-slpd` item 5. `IsQGevreyOrder` and `IsQGevreyLevel` are reciprocal
(RSZ §1.3.2), and this corpus carries one `½` of each kind — the Route-B
kernel's *order* and the C1 `∞`-side's *level*. Which one the Newton polygon
attaches to was the last step in the C1 chain carried by prose.

**RSZ's own touchstone cannot settle it.** The q-Euler / Tshakaloff equation
`zσf = f` has Newton slope `1` and solution `c_m = q^{m(m-1)/2}`, i.e. order `1`
**and** level `1`. At slope 1 the two readings agree, which is exactly why a `½`
could sit unexamined here: the one example everyone checks against is the one
case that cannot tell them apart. `slopeKCoeff_order_one` below is that case.

**The slope-`k` family separates them.** `L_k = z^kσ − 1` has Newton points
`(0,0)`, `(1,k)`, hence slope `k`; recursion `c_m = q^{m−k}c_{m−k}`; nonzero
coefficients `c_{jk} = q^{k j(j−1)/2}`; and therefore order `1/k`, level `k`. It
is the **level** that tracks the slope, and `slopeKCoeff_order` proves this for
**every** `k ≥ 1`, not just for sampled instances. `slopeKCoeff_order_half`
(`k = 2`) is the first case where the two readings differ.
`computations/qbeta/c3_w2_newton_slope_is_qgevrey_level.py` (4/4) additionally
checks the polygon and the recursion symbolically for `k = 1, 2, 3` — the two
inputs the Lean takes as given.

**Consequence for C1, and it is forced rather than chosen.** The computed Newton
slope at `∞` is `½` (`ThetaSlopeArithmetic.newtonSlopes_c1`). Read as a *level*
it predicts order `2`, i.e. growth `q^{n²}` — which is exactly
`c1InfCoeff_order_two` and `C1FormalSolutionGrowth.natDegree_c1CoeffPoly`. Read
as an *order* it would predict `q^{n²/4}`, off by a factor 4 in the exponent and
inconsistent with the corpus's own measured growth. So
`theta_eq_half_gs_bridge` below reaches the right **number** by the wrong route:
it grounds `c1Slope = ½` in the Route-B *order*, where the correct grounding is
the `∞`-side *level*. The number, and every downstream conclusion, is unchanged
— Door-i needs only that the two slope multisets differ, which is
`ThetaSlopeArithmetic.newtonSlopes_c1_ne_ggm`. -/

/-- Solution coefficients of the slope-`k` model `z^k σ f = f`, on the indices
`m = jk` where they are nonzero: `d_j := c_{jk}`, from `c_m = q^{m-k}c_{m-k}`. -/
noncomputable def slopeKCoeff (q : ℝ) (k : ℕ) : ℕ → ℝ
  | 0 => 1
  | (j + 1) => q ^ (k * j) * slopeKCoeff q k j

theorem slopeKCoeff_sq_mul (q : ℝ) (k j : ℕ) :
    slopeKCoeff q k j * slopeKCoeff q k j * q ^ (k * j) = q ^ (k * (j * j)) := by
  induction j with
  | zero => simp [slopeKCoeff]
  | succ i ih =>
    have hexp : q ^ (k * ((i + 1) * (i + 1))) = q ^ (2 * (k * i)) * q ^ (k * (i * i)) * q ^ k := by
      rw [← pow_add, ← pow_add]; congr 1; ring
    calc slopeKCoeff q k (i + 1) * slopeKCoeff q k (i + 1) * q ^ (k * (i + 1))
        = q ^ (2 * (k * i)) * (slopeKCoeff q k i * slopeKCoeff q k i * q ^ (k * i)) * q ^ k := by
          rw [show slopeKCoeff q k (i + 1) = q ^ (k * i) * slopeKCoeff q k i from rfl,
              show k * (i + 1) = k * i + k by ring, pow_add, two_mul, pow_add]
          ring
      _ = q ^ (2 * (k * i)) * q ^ (k * (i * i)) * q ^ k := by rw [ih]
      _ = q ^ (k * ((i + 1) * (i + 1))) := hexp.symm

theorem slopeKCoeff_pos (q : ℝ) (hq : 0 < q) (k j : ℕ) : 0 < slopeKCoeff q k j := by
  induction j with
  | zero => rw [slopeKCoeff]; norm_num
  | succ i ih =>
    rw [show slopeKCoeff q k (i + 1) = q ^ (k * i) * slopeKCoeff q k i from rfl]
    exact mul_pos (pow_pos hq _) ih

theorem logb_slopeKCoeff (q : ℝ) (hq : 1 < q) (k j : ℕ) :
    logb q (slopeKCoeff q k j) = (k : ℝ) * ((j : ℝ) * j - j) / 2 := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have hlq : Real.log q ≠ 0 := ne_of_gt (Real.log_pos hq)
  have hd : 0 < slopeKCoeff q k j := slopeKCoeff_pos q hq0 k j
  have h := slopeKCoeff_sq_mul q k j
  have hlog : Real.log (slopeKCoeff q k j) + Real.log (slopeKCoeff q k j)
      + ((k : ℝ) * j) * Real.log q = ((k : ℝ) * ((j : ℝ) * j)) * Real.log q := by
    have := congrArg Real.log h
    rwa [Real.log_mul (mul_ne_zero (ne_of_gt hd) (ne_of_gt hd)) (ne_of_gt (pow_pos hq0 _)),
         Real.log_mul (ne_of_gt hd) (ne_of_gt hd), Real.log_pow, Real.log_pow,
         Nat.cast_mul, Nat.cast_mul, Nat.cast_mul] at this
  rw [logb, div_eq_iff hlq]
  linarith

/-- **The slope-`k` model has q-Gevrey order `1/k`, hence LEVEL `k` = its slope.**

`L_k = z^kσ − 1` has Newton points `(0,0)`, `(1,k)`, so slope `k`. Its formal
solution satisfies `c_m = q^{m−k}c_{m−k}`, so `c_{jk} = q^{k j(j−1)/2}` and along
the nonzero subsequence `m = jk`

    2·log_q c_m / m²  =  (j − 1)/(k j)  →  1/k.

Order `1/k`, level `k`. The slope is `k`. **The Newton slope is the LEVEL**, for
every `k ≥ 1` — not just the two instances checked before. At `k = 1` order and
level coincide, which is why RSZ's own touchstone cannot see the distinction. -/
theorem slopeKCoeff_order (q : ℝ) (hq : 1 < q) (k : ℕ) (hk : 1 ≤ k) :
    Tendsto (fun j : ℕ => 2 * logb q (slopeKCoeff q k j) / (((k : ℝ) * j) ^ 2))
      atTop (𝓝 (1 / (k : ℝ))) := by
  have hk0 : (0:ℝ) < (k : ℝ) := by exact_mod_cast hk
  have heq : ∀ j : ℕ, 1 ≤ j →
      2 * logb q (slopeKCoeff q k j) / (((k : ℝ) * j) ^ 2)
        = 1 / (k : ℝ) - 1 / ((k : ℝ) * j) := by
    intro j hj
    have hj0 : (0:ℝ) < (j : ℝ) := by exact_mod_cast hj
    rw [logb_slopeKCoeff q hq k j]
    field_simp
  have hlim : Tendsto (fun j : ℕ => 1 / (k : ℝ) - 1 / ((k : ℝ) * j)) atTop (𝓝 (1 / (k : ℝ))) := by
    have h : Tendsto (fun j : ℕ => ((k : ℝ))⁻¹ * (1 / (j : ℝ))) atTop (𝓝 0) := by
      simpa using (tendsto_const_div_atTop_nhds_zero_nat (1 : ℝ)).const_mul ((k : ℝ))⁻¹
    have h2 : Tendsto (fun j : ℕ => 1 / ((k : ℝ) * j)) atTop (𝓝 0) := by
      refine h.congr fun j => ?_
      rw [one_div, one_div, mul_inv_rev]
      ring
    simpa using (tendsto_const_nhds (x := (1 / (k : ℝ)))).sub h2
  refine hlim.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with j hj
  exact (heq j hj).symm

/-- **The slope-1 (q-Euler / Tshakaloff) case**, `k = 1`: order `1`, level `1`.
The two readings agree here — this is the degenerate touchstone. -/
theorem slopeKCoeff_order_one (q : ℝ) (hq : 1 < q) :
    Tendsto (fun j : ℕ => 2 * logb q (slopeKCoeff q 1 j) / (((1 : ℝ) * j) ^ 2))
      atTop (𝓝 1) := by
  simpa using slopeKCoeff_order q hq 1 le_rfl

/-- **The slope-2 case**, `k = 2`: order `½`, level `2`. The first `k` where the
two readings separate, and the level is the one that tracks the slope. -/
theorem slopeKCoeff_order_half (q : ℝ) (hq : 1 < q) :
    Tendsto (fun j : ℕ => 2 * logb q (slopeKCoeff q 2 j) / (((2 : ℝ) * j) ^ 2))
      atTop (𝓝 (1 / 2)) := by
  simpa using slopeKCoeff_order q hq 2 (by norm_num)

/-! ## MI-4 — the `≥` direction under positivity, and `cauchyMul_order` discharged there

`cauchyMul_order` above is stated for an arbitrary normed field and carries the
`NoCancellation` hypothesis its `≥` half genuinely needs; in that generality the
half is still open.  This section closes it in the **positive real** regime — the
one the MI-2 numerics were run in ("positive/no-cancel coefficients") — and on
the way shows `NoCancellation` is satisfiable at all.

* `noCancellation_of_pos` — for `0 < a n`, `0 < b n` the hypothesis holds with
  `c = 1`, because a sum of positive terms dominates each of its terms.  So
  `NoCancellation` is not vacuous and the general theorem has content.
* `cauchyMul_order_of_pos` — the full law, **proved**, for positive real
  coefficients.  Its conclusion is `cauchyMul_order`'s on exactly the instances
  `noCancellation_of_pos` supplies, so it is a partial discharge of that theorem,
  not a parallel statement.

Positivity makes the sum dominate each of its terms, so it is enough to name the
term at the maximiser of `θ ↦ sθ² + t(1−θ)²`; along `kₙ = ⌊θn⌋` the `≥` half is
then a composition of limits,

    2·log_q(a_{kₙ}·b_{n−kₙ}) / n²
      = (2·log_q a_{kₙ}/kₙ²)·(kₙ/n)² + (2·log_q b_{n−kₙ}/(n−kₙ)²)·((n−kₙ)/n)²
      → s·θ² + t·(1−θ)².

The maximiser reads off `cauchyEnvelope`'s closed form: an endpoint `θ ∈ {0,1}`
in the convex (`max`) branch, `θ = t/(s+t)` in the concave one, where
`sθ² + t(1−θ)² = st/(s+t)` exactly.  Degenerate concave sub-cases (`s = 0`,
`t = 0`, `s + t = 0`) all have envelope `0` and take an endpoint, so no `θ`
outside `[0,1]` is ever formed and `s + t = 0` is never divided by.

The `≤` half is not redone here: it is `cauchyMul_bound` above, consumed through
the two bridges `qGevreyBound_of_isQGevreyOrder` and `coeff_le_of_qGevreyBound`. -/

section Positive

/-! ### Bridges between the limit form and `QGevreyBound` -/

/-- **Limit form ⇒ bound form at an inflated slope.**  The finitely many indices
where the eventual bound has not yet kicked in are absorbed into `C`; no
geometric factor is needed, so `A = 1`. -/
theorem qGevreyBound_of_isQGevreyOrder {q s : ℝ} (hq : 1 < q) {a : ℕ → K}
    (ha : IsQGevreyOrder q s a) {ε : ℝ} (hε : 0 < ε) :
    QGevreyBound q (s + ε) a := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hlogq : 0 < Real.log q := Real.log_pos hq
  obtain ⟨N₀, hN₀⟩ := eventually_atTop.mp (order_eventually_le ha hε)
  have hnn : ∀ k : ℕ, (0 : ℝ) ≤ ‖a k‖ / q ^ ((s + ε) * (k : ℝ) ^ 2 / 2) := fun k =>
    div_nonneg (norm_nonneg _) (Real.rpow_pos_of_pos hq0 _).le
  refine ⟨1 + ∑ k ∈ Finset.range (max N₀ 1), ‖a k‖ / q ^ ((s + ε) * (k : ℝ) ^ 2 / 2), 1,
    by linarith [Finset.sum_nonneg (fun k (_ : k ∈ Finset.range (max N₀ 1)) => hnn k)],
    one_pos, fun n => ?_⟩
  rw [one_pow, mul_one]
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
    nlinarith [(Real.rpow_pos_of_pos hq0 ((s + ε) * (n : ℝ) ^ 2 / 2)),
      Finset.sum_nonneg (fun k (_ : k ∈ Finset.range (max N₀ 1)) => hnn k)]

/-- **Bound form ⇒ an eventual bound on the leading coefficient.**  The `C·Aⁿ`
prefactor contributes degree `≤ 1` in `n`, which the `n²` denominator washes
out. -/
theorem coeff_le_of_qGevreyBound {q u : ℝ} (hq : 1 < q) {c : ℕ → ℝ}
    (hc : QGevreyBound q u c) (hpos : ∀ n, 0 < c n) {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ n : ℕ in atTop, 2 * logb q (c n) / (n : ℝ) ^ 2 ≤ u + ε := by
  obtain ⟨C, A, hC, hA, hbd⟩ := hc
  have hq0 : (0 : ℝ) < q := by linarith
  have hlogq : 0 < Real.log q := Real.log_pos hq
  -- the majorant, which tends to `u`
  have hlim : Tendsto (fun n : ℕ =>
      2 * logb q C / (n : ℝ) ^ 2 + 2 * logb q A / (n : ℝ) + u) atTop (𝓝 (0 + 0 + u)) := by
    refine Tendsto.add (Tendsto.add ?_ ?_) tendsto_const_nhds
    · exact Tendsto.div_atTop tendsto_const_nhds
        ((tendsto_pow_atTop (by norm_num : 2 ≠ 0)).comp tendsto_natCast_atTop_atTop)
    · exact Tendsto.div_atTop tendsto_const_nhds tendsto_natCast_atTop_atTop
  have hev : ∀ᶠ n : ℕ in atTop,
      2 * logb q C / (n : ℝ) ^ 2 + 2 * logb q A / (n : ℝ) + u ≤ u + ε := by
    have hmem : ∀ᶠ z in 𝓝 (0 + 0 + u), z ≤ u + ε := by
      filter_upwards [Iio_mem_nhds (show (0 : ℝ) + 0 + u < u + ε by linarith)] with z hz
      exact le_of_lt hz
    exact hlim.eventually hmem
  filter_upwards [hev, eventually_ge_atTop 1] with n hn hn1
  have hnR : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn1
  have hn2 : (0 : ℝ) < (n : ℝ) ^ 2 := by positivity
  -- expand the logarithm of the majorant
  have hlogprod : Real.log (C * A ^ n * q ^ (u * (n : ℝ) ^ 2 / 2))
      = Real.log C + (n : ℝ) * Real.log A + (u * (n : ℝ) ^ 2 / 2) * Real.log q := by
    rw [Real.log_mul (by positivity) (ne_of_gt (Real.rpow_pos_of_pos hq0 _)),
      Real.log_mul (ne_of_gt hC) (by positivity), Real.log_pow, Real.log_rpow hq0]
  have hmono : Real.log (c n) ≤ Real.log (C * A ^ n * q ^ (u * (n : ℝ) ^ 2 / 2)) := by
    have := hbd n
    rw [Real.norm_of_nonneg (hpos n).le] at this
    exact Real.log_le_log (hpos n) this
  rw [hlogprod] at hmono
  -- divide through by `log q` and by `n²`
  unfold logb
  rw [div_le_iff₀ hn2]
  have hdiv : Real.log (c n) / Real.log q
      ≤ Real.log C / Real.log q + (n : ℝ) * (Real.log A / Real.log q)
        + u * (n : ℝ) ^ 2 / 2 := by
    rw [div_le_iff₀ hlogq]
    have : Real.log C / Real.log q * Real.log q = Real.log C := div_mul_cancel₀ _ (ne_of_gt hlogq)
    have hA' : Real.log A / Real.log q * Real.log q = Real.log A :=
      div_mul_cancel₀ _ (ne_of_gt hlogq)
    nlinarith [hmono, this, hA']
  have hn' : 2 * logb q C / (n : ℝ) ^ 2 * (n : ℝ) ^ 2 = 2 * logb q C :=
    div_mul_cancel₀ _ (ne_of_gt hn2)
  have hn'' : 2 * logb q A / (n : ℝ) * (n : ℝ) = 2 * logb q A :=
    div_mul_cancel₀ _ (ne_of_gt hnR)
  have hnn2 : (n : ℝ) * (n : ℝ) = (n : ℝ) ^ 2 := by ring
  unfold logb at hn' hn'' hn
  nlinarith [hdiv, hn, hn', hn'', hnn2, hn2, hnR]

/-! ### Positivity: `NoCancellation` holds, and the law is provable -/

/-- The Cauchy product of positive sequences is positive. -/
theorem cauchyMul_pos {a b : ℕ → ℝ} (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n) (n : ℕ) :
    0 < cauchyMul a b n :=
  Finset.sum_pos (fun i _ => mul_pos (ha0 i) (hb0 _))
    ⟨0, Finset.mem_range.mpr n.succ_pos⟩

/-- **The sum dominates each of its terms** — the one place positivity is used,
and the whole content of `noCancellation_of_pos`. -/
theorem term_le_cauchyMul {a b : ℕ → ℝ} (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n)
    {k n : ℕ} (hk : k ≤ n) : a k * b (n - k) ≤ cauchyMul a b n :=
  Finset.single_le_sum (f := fun i => a i * b (n - i))
    (fun i _ => (mul_pos (ha0 i) (hb0 _)).le) (Finset.mem_range.mpr (Nat.lt_succ_of_le hk))

/-- **`NoCancellation` is satisfiable** — it holds with `c = 1` for positive real
coefficients.  Together with `not_noCancellation_of_cauchyMul_eventually_zero`
(which shows it can fail) this pins the hypothesis as a genuine side condition:
neither vacuous nor automatic. -/
theorem noCancellation_of_pos {a b : ℕ → ℝ} (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n) :
    NoCancellation a b := by
  refine ⟨1, one_pos, ?_⟩
  filter_upwards with n
  intro k hk
  have hkn : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  rw [one_mul, Real.norm_of_nonneg (cauchyMul_pos ha0 hb0 n).le,
    Real.norm_of_nonneg (ha0 k).le, Real.norm_of_nonneg (hb0 (n - k)).le]
  exact term_le_cauchyMul ha0 hb0 hkn

/-- Over `ℝ` a **positive** sequence's order can be stated without the norm. -/
theorem isQGevreyOrder_pos {q s : ℝ} {a : ℕ → ℝ} (hpos : ∀ n, 0 < a n) :
    IsQGevreyOrder q s a ↔
      Tendsto (fun n : ℕ => 2 * logb q (a n) / (n : ℝ) ^ 2) atTop (𝓝 s) := by
  have hfun : (fun n : ℕ => 2 * logb q ‖a n‖ / (n : ℝ) ^ 2)
      = fun n : ℕ => 2 * logb q (a n) / (n : ℝ) ^ 2 := by
    funext n; rw [Real.norm_of_nonneg (hpos n).le]
  unfold IsQGevreyOrder
  rw [hfun]

private theorem logb_le_logb {q : ℝ} (hq : 1 < q) {x y : ℝ} (hx : 0 < x) (hxy : x ≤ y) :
    logb q x ≤ logb q y :=
  div_le_div_of_nonneg_right (Real.log_le_log hx hxy) (Real.log_pos hq).le

private theorem logb_mul' {q x y : ℝ} (hx : x ≠ 0) (hy : y ≠ 0) :
    logb q (x * y) = logb q x + logb q y := by
  unfold logb; rw [Real.log_mul hx hy, add_div]

/-- A frozen index contributes nothing to the leading coefficient — the `n²`
denominator washes a constant out.  This is what makes the endpoint cases
(`θ ∈ {0,1}`) work. -/
private theorem tendsto_logb_const {q : ℝ} (x : ℝ) :
    Tendsto (fun n : ℕ => 2 * logb q x / (n : ℝ) ^ 2) atTop (𝓝 0) :=
  Tendsto.div_atTop tendsto_const_nhds
    ((tendsto_pow_atTop (by norm_num : 2 ≠ 0)).comp tendsto_natCast_atTop_atTop)

/-- **Reindex an order limit along `u`, then rescale.**  If `uₙ → ∞` with
`uₙ/n → c`, the leading coefficient of `a` read at `uₙ` against `n²` converges to
`s·c²`.  This one computation is the whole interior (saddle) case. -/
private theorem tendsto_logb_comp {q s : ℝ} {a : ℕ → ℝ}
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
private theorem tendsto_term {q : ℝ} {a b : ℕ → ℝ} (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n)
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
private theorem term_coeff_le {q : ℝ} {a b : ℕ → ℝ} (hq : 1 < q)
    (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n)
    {k : ℕ → ℕ} (hk : ∀ n, k n ≤ n) (n : ℕ) :
    2 * logb q (a (k n) * b (n - k n)) / (n : ℝ) ^ 2
      ≤ 2 * logb q (cauchyMul a b n) / (n : ℝ) ^ 2 := by
  have h := logb_le_logb hq (mul_pos (ha0 (k n)) (hb0 (n - k n)))
    (term_le_cauchyMul ha0 hb0 (hk n))
  exact div_le_div_of_nonneg_right (by linarith) (sq_nonneg _)

/-- **[MI-2 — PROVED for positive real coefficients] Convolution order =
envelope.**  The conclusion of `cauchyMul_order` on exactly the instances
`noCancellation_of_pos` supplies, so this is a partial discharge of that
theorem's residual `sorry`, not a restatement of it.

`≤` is `cauchyMul_bound` through the two `QGevreyBound` bridges; `≥` is the
Laplace/saddle term selection described in the section header.  The two are glued
by `tendsto_order`.

Checked at the small instances the MI-2 numerics report: `(-1,-1) ↦ -0.5`,
`(-2,-1) ↦ -2/3`, `(2,1) ↦ 2`, `(-3,1) ↦ 1`. -/
theorem cauchyMul_order_of_pos {q s t : ℝ} {a b : ℕ → ℝ}
    (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b)
    (hq : 1 < q) (ha0 : ∀ n, 0 < a n) (hb0 : ∀ n, 0 < b n) :
    IsQGevreyOrder q (cauchyEnvelope s t) (cauchyMul a b) := by
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
  obtain ⟨k, hk, hterm⟩ :
      ∃ k : ℕ → ℕ, (∀ n, k n ≤ n) ∧
        Tendsto (fun n : ℕ => 2 * logb q (a (k n) * b (n - k n)) / (n : ℝ) ^ 2)
          atTop (𝓝 (cauchyEnvelope s t)) := by
    by_cases hcc : s ≤ 0 ∧ t ≤ 0
    · obtain ⟨hs, ht⟩ := hcc
      have hE : cauchyEnvelope s t = s * t / (s + t) := by
        unfold cauchyEnvelope; exact if_pos ⟨hs, ht⟩
      rw [hE]
      rcases eq_or_lt_of_le (add_nonpos hs ht) with hst0 | hstneg
      · have hs0 : s = 0 := by linarith
        have ht0 : t = 0 := by linarith
        subst hs0; subst ht0
        exact ⟨fun _ => 0, fun n => Nat.zero_le n, by simpa using hzero⟩
      · rcases eq_or_lt_of_le ht with ht0 | htneg
        · refine ⟨fun _ => 0, fun n => Nat.zero_le n, ?_⟩
          rw [show s * t / (s + t) = 0 + t by rw [ht0]; simp]
          exact hzero
        · rcases eq_or_lt_of_le hs with hs0 | hsneg
          · refine ⟨fun n => n, fun n => le_refl n, ?_⟩
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
            have hval : s * θ ^ 2 + t * (1 - θ) ^ 2 = s * t / (s + t) := by
              rw [hθdef]; field_simp; ring
            rw [← hval]
            exact tendsto_term ha0 hb0 _
              (tendsto_logb_comp haR huA hratioA) (tendsto_logb_comp hbR huB hratioB)
    · have hE : cauchyEnvelope s t = max s t := by
        unfold cauchyEnvelope; exact if_neg hcc
      rw [hE]
      rcases le_total t s with hts | hst
      · rw [max_eq_left hts]
        exact ⟨fun n => n, fun n => le_refl n, by simpa using hfull⟩
      · rw [max_eq_right hst]
        exact ⟨fun _ => 0, fun n => Nat.zero_le n, by simpa using hzero⟩
  -- squeeze: the selected term bounds below, `cauchyMul_bound` bounds above
  rw [isQGevreyOrder_pos (fun n => cauchyMul_pos ha0 hb0 n)]
  refine tendsto_order.2 ⟨fun c hc => ?_, fun c hc => ?_⟩
  · filter_upwards [hterm.eventually (Ioi_mem_nhds hc)] with n hn
    exact lt_of_lt_of_le hn (term_coeff_le hq ha0 hb0 hk n)
  · have hε : (0 : ℝ) < (c - cauchyEnvelope s t) / 4 := by linarith
    have hbA := qGevreyBound_of_isQGevreyOrder hq ha hε
    have hbB := qGevreyBound_of_isQGevreyOrder hq hb hε
    have hprod := cauchyMul_bound hq hbA hbB
    have hshift := envelope_shift_le s t ((c - cauchyEnvelope s t) / 4) hε.le
    filter_upwards [coeff_le_of_qGevreyBound hq hprod
      (fun n => cauchyMul_pos ha0 hb0 n) hε] with n hn
    linarith

end Positive

/-! ### The unhypothesised law, refuted inside Lean

`not_noCancellation_of_cauchyMul_eventually_zero` above shows `NoCancellation`
fails on the `q^{n²}` / formal-inverse pair — the mathematically strongest
witness, since both factors carry the *same positive order*.  Its Lean content is
that the hypothesis fails there; the pair itself lives in a Python witness.

The lemma below is the cheap complement: a fully machine-checked refutation of
the hypothesis-free statement, needing no external witness.  It exploits a
different mechanism — `Real.log 0 = 0`, so the zero sequence has order `0` — and
is therefore weaker as evidence but complete as a proof. -/

/-- **The identically-zero sequence has q-Gevrey order `0`**, for every base:
`‖0‖ = 0` and `Real.log 0 = 0`, so the defining ratio is identically `0`. -/
theorem isQGevreyOrder_zero (q : ℝ) : IsQGevreyOrder q 0 (fun _ : ℕ => (0 : K)) := by
  unfold IsQGevreyOrder
  refine Tendsto.congr' ?_ (tendsto_const_nhds (x := (0 : ℝ)))
  filter_upwards with n
  simp [logb]

/-- **The unhypothesised convolution law is FALSE** (machine-proved, no `sorry`,
no external witness).  Over `ℝ` with `q = 2`: `a n = 2^{n²}` has order `2`, the
zero sequence has order `0`, their Cauchy product is `0` and so has order `0`,
yet `cauchyEnvelope 2 0 = max 2 0 = 2`.  `order_unique` then gives `0 = 2`.

This is why `cauchyMul_order` carries `NoCancellation`.  Axioms
`[propext, Classical.choice, Quot.sound]`. -/
theorem cauchyMul_order_unhypothesised_false :
    ¬ ∀ (q s t : ℝ) (a b : ℕ → ℝ),
        IsQGevreyOrder q s a → IsQGevreyOrder q t b → 1 < q →
        IsQGevreyOrder q (cauchyEnvelope s t) (cauchyMul a b) := by
  intro h
  have hlog : Real.log 2 ≠ 0 := ne_of_gt (Real.log_pos one_lt_two)
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
  have hb : IsQGevreyOrder (2 : ℝ) 0 (fun _ : ℕ => (0 : ℝ)) := isQGevreyOrder_zero (K := ℝ) 2
  have hE : cauchyEnvelope 2 0 = 2 := by norm_num [cauchyEnvelope]
  have hprod : cauchyMul (fun n : ℕ => (2 : ℝ) ^ (n ^ 2)) (fun _ : ℕ => (0 : ℝ))
      = fun _ : ℕ => (0 : ℝ) := by
    funext n; simp [cauchyMul]
  have hc := h 2 2 0 _ _ ha hb one_lt_two
  rw [hE, hprod] at hc
  have : (2 : ℝ) = 0 := order_unique hc (isQGevreyOrder_zero (K := ℝ) 2)
  norm_num at this

end QOU.Mathlib.QGevreyOrder
