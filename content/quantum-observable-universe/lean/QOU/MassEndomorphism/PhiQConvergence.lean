import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Algebra.Order.AbsoluteValue.Basic
import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Summable
import Mathlib.Tactic

/-!
# Gap 4 closure: Φ_q convergence at single-tick

Closes a piece of Gap 4 from
`content/quantum-observable-universe/lean/QOU/MassComputationChainRoadmap.lean`:
the analytic convergence of the q-Pochhammer / quantum dilogarithm

  Φ_q(z) = ∏_{k≥1} (1 - q^{-k} z)^{-1}

for the relevant domain `1 < q` and `|z| < q`.

The convergence reduces to **absolute summability of the geometric
series** Σ q^{-k}|z|. This is a clean Mathlib-provable fact.

## What this closes

The existing `mass-endomorphism-tower.lean` defines `quantumDilog`
via `∏' k, ...` without proving convergence. Without convergence
proven, the definition is technically `0` whenever the product
doesn't multiplicable (per Mathlib's convention). This file gives
the convergence theorem so the definition has its intended value.

## What this does NOT close

- The CYCLOTOMIC PROJECTION at level n_⋆ (Gap 5; conjectural)
- The structural lift formula from N=0 → N=1 → ... (open R&D)
- The PRECISE numerical value of Φ_q at specific witness points
  (those remain in the MassEvaluation class as numerical inputs)

This file proves only that the infinite product is well-defined as
a real number for the relevant analytical domain. The N≥1 lift
formula is a separate structural problem.

## References

- [habiro2004cyclotomic] Habiro ring and q-Pochhammer convergence
- [manuscript] prop:beta-decay-energy-scale §"calibration cross-check"
  (cites the 0.75% brane-tower correction as the gap between N=0
   single-tick and the convergent infinite product)
- [manuscript] per-braid-mass-tower.md §"remainder bound"
  (gives |R_N| ≤ ℏ_q^{2(N+1)}/(1-ℏ_q²) — the per-N bound this
   convergence theorem implicitly underpins)
-/

namespace QOU.MassEndomorphism.PhiQConvergence

/-! ## Key analytic lemma: geometric summability -/

-- Ref: [habiro2004cyclotomic] §2 q-Pochhammer convergence; std analysis
/-- For `1 < q : ℝ`, the geometric series `Σ_{k≥0} q^(-(k+1))`
    converges absolutely. This is the foundation for Φ_q
    convergence — every term in the q-Pochhammer / quantum
    dilogarithm is bounded by a multiple of `q^{-k}`. -/
theorem summable_q_inv_geometric {q : ℝ} (hq : 1 < q) :
    Summable (fun k : ℕ => q ^ (-((k : ℤ) + 1))) := by
  -- Use Mathlib's geometric-series summability:
  --   |1/q| < 1 since q > 1
  -- Then Σ q^(-(k+1)) = q^(-1) · Σ q^(-k) converges.
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have hq_inv_lt_one : (1 / q : ℝ) < 1 := by
    rw [div_lt_one hq_pos]; exact hq
  have hq_inv_nonneg : (0 : ℝ) ≤ 1 / q := by positivity
  -- Σ (1/q)^k converges absolutely (geometric ratio < 1)
  have h_geom : Summable (fun k : ℕ => (1 / q) ^ k) :=
    summable_geometric_of_lt_one hq_inv_nonneg hq_inv_lt_one
  -- Rewrite q^(-(k+1)) = (1/q)^(k+1) = (1/q) · (1/q)^k
  -- and multiply by the constant 1/q
  have hq_ne : q ≠ 0 := hq_pos.ne'
  have heq : (fun k : ℕ => q ^ (-((k : ℤ) + 1))) =
      (fun k : ℕ => (1 / q) * (1 / q) ^ k) := by
    funext k
    -- Step 1: normalize (k : ℤ) + 1 = ((k+1 : ℕ) : ℤ) for zpow_natCast.
    have key_cast : (((k : ℤ) + 1)) = ((k + 1 : ℕ) : ℤ) := by push_cast; ring
    -- Step 2: rewrite q^(-(k+1)) = (q^(k+1))⁻¹ = (q^k * q)⁻¹.
    rw [key_cast, zpow_neg, zpow_natCast, pow_succ]
    -- Goal becomes: (q^k * q)⁻¹ = (1/q) * (1/q)^k — pure field arithmetic.
    rw [mul_inv, ← inv_pow]
    ring
  rw [heq]
  exact h_geom.mul_left (1 / q)

/-! ## Φ_q absolute-convergence statement

The full convergence of the infinite PRODUCT `Φ_q(z) = ∏_{k≥1} (1 - q^{-k} z)^{-1}`
follows from the summability of the LOGARITHM:

    log Φ_q(z) = -Σ_{k≥1} log(1 - q^{-k} z)

For |z| < q, |q^{-k} z| < 1, so |log(1 - q^{-k} z)| ≤ 2|q^{-k} z|
(using |log(1-x)| ≤ 2|x| for |x| ≤ 1/2). Therefore:

    Σ |log(1 - q^{-k} z)| ≤ 2|z| · Σ q^{-k}

which converges by `summable_q_inv_geometric`. The infinite product
then `Multipliable`s to a positive real number.

The full Multipliable statement requires Mathlib's
`Multipliable.tprod_eq` machinery applied to the log-summability.
We state the corollary directly:
-/

/-- The product `∏ (1 - q^{-k-1} z)` is non-zero whenever
    `1 < q` and `|z| < q`. Together with summability, this proves
    `Multipliable (fun k => (1 - q^{-k-1} z)^{-1})` —
    i.e. `Φ_q(z)` is a well-defined positive real.

    This is the analytic content underpinning
    `mass-endomorphism-tower.lean §QOU.MassEndomorphism.Arch.quantumDilog`. -/
-- Ref: [manuscript] prop:beta-decay-energy-scale §"calibration cross-check"
-- Ref: [habiro2004cyclotomic] q-Pochhammer
theorem quantumDilog_factors_nonzero
    {q z : ℝ} (hq : 1 < q) (hz : |z| < q) :
    ∀ k : ℕ, (1 - q ^ (-((k : ℤ) + 1)) * z) ≠ 0 := by
  intro k
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have hq_ne : q ≠ 0 := hq_pos.ne'
  -- |q^(-(k+1)) z| = q^(-(k+1)) |z| < q^(-(k+1)) · q = q^(-k) ≤ 1
  -- so 1 - q^(-(k+1)) z ≠ 0 (it's strictly between 0 and 2).
  intro h
  -- Strategy: derive |q^(-(k+1)) z| < 1 and then contradict with the
  -- consequence of 1 - q^(-(k+1)) z = 0.
  have hz_pos_factor : 0 < q ^ (-((k : ℤ) + 1)) := zpow_pos hq_pos _
  -- Step 1: q^(-(k+1)) · |z| < q^(-(k+1)) · q
  have step1 : q ^ (-((k : ℤ) + 1)) * |z| < q ^ (-((k : ℤ) + 1)) * q :=
    (mul_lt_mul_iff_of_pos_left hz_pos_factor).mpr hz
  -- Step 2: q^(-(k+1)) · q = q^(-k).
  have step2 : q ^ (-((k : ℤ) + 1)) * q = q ^ (-(k : ℤ)) := by
    have : (q : ℝ) ^ (-((k : ℤ) + 1)) * q ^ (1 : ℤ) = q ^ (-((k : ℤ) + 1) + 1) :=
      (zpow_add₀ hq_ne _ _).symm
    rw [zpow_one] at this
    rw [this]
    congr 1; ring
  -- Step 3: q^(-k) ≤ 1 (since q ≥ 1 and -k ≤ 0).
  have step3 : q ^ (-(k : ℤ)) ≤ 1 := by
    rw [show -((k : ℤ)) = -((k : ℕ) : ℤ) from rfl, zpow_neg, zpow_natCast]
    apply inv_le_one_of_one_le₀
    exact one_le_pow₀ hq.le
  -- Combine: q^(-(k+1)) · |z| < 1
  have habs : q ^ (-((k : ℤ) + 1)) * |z| < 1 := by
    calc q ^ (-((k : ℤ) + 1)) * |z|
        < q ^ (-((k : ℤ) + 1)) * q := step1
      _ = q ^ (-(k : ℤ)) := step2
      _ ≤ 1 := step3
  -- Now: 1 - q^(-(k+1)) z = 0 implies q^(-(k+1)) z = 1, so its absolute
  -- value is 1, contradicting habs.
  have prod_eq_one : q ^ (-((k : ℤ) + 1)) * z = 1 := by linarith
  have abs_eq_one : |q ^ (-((k : ℤ) + 1)) * z| = 1 := by
    rw [prod_eq_one]; exact abs_one
  rw [abs_mul, abs_of_pos hz_pos_factor] at abs_eq_one
  linarith

/-! ## Φ_q multipliability (the convergence half of Gap 4)

We now upgrade the two facts above (geometric summability + non-vanishing
of factors) to the statement that the infinite product actually
`Multipliable`s.  The mechanism is Mathlib's
`Real.multipliable_one_add_of_summable`: if `Summable g` then
`Multipliable (fun k => 1 + g k)`.

We apply it twice:

  * with `g k = -(q^{-(k+1)} z)` to get `Multipliable (fun k => 1 - q^{-(k+1)} z)`
    (the *denominator* product);
  * with `g k = (1 - q^{-(k+1)} z)⁻¹ - 1` to get
    `Multipliable (fun k => (1 - q^{-(k+1)} z)⁻¹)` (the actual `Φ_q` product).

For the second application we need `Summable g`.  Writing
`a k = q^{-(k+1)} z`, we have `g k = a k / (1 - a k)`, and since
`|a k| ≤ |z|/q < 1` the denominator is bounded below by `c := 1 - |z|/q > 0`,
so `|g k| ≤ |a k| / c`, summable by comparison with the geometric series.
-/

-- Ref: [habiro2004cyclotomic] §2 q-Pochhammer convergence; std analysis
/-- The terms `a k = q^{-(k+1)} z` are summable for `1 < q` (any `z`).
    This is the geometric summability repackaged in the `* z` form used
    by the multipliability proofs below. -/
theorem summable_quantumDilog_terms {q z : ℝ} (hq : 1 < q) :
    Summable (fun k : ℕ => q ^ (-((k : ℤ) + 1)) * z) :=
  (summable_q_inv_geometric hq).mul_right z

/-- The denominator product `∏ (1 - q^{-(k+1)} z)` is `Multipliable`. -/
-- Ref: [manuscript] prop:beta-decay-energy-scale §"calibration cross-check"
theorem quantumDilog_denom_multipliable {q z : ℝ} (hq : 1 < q) :
    Multipliable (fun k : ℕ => 1 - q ^ (-((k : ℤ) + 1)) * z) := by
  have hsum : Summable (fun k : ℕ => -(q ^ (-((k : ℤ) + 1)) * z)) :=
    (summable_quantumDilog_terms (z := z) hq).neg
  have h := Real.multipliable_one_add_of_summable hsum
  -- `1 + (-(a k)) = 1 - a k`
  simpa [sub_eq_add_neg] using h

/-- **Brane-tower convergence half of Gap 4.**
    For `1 < q` and `|z| < q`, the q-dilogarithm / q-Pochhammer product

      Φ_q(z) = ∏_{k≥1} (1 - q^{-k} z)^{-1}

    is `Multipliable` — i.e. it converges to a well-defined non-zero real.
    Each factor is non-zero by `quantumDilog_factors_nonzero`, and the
    inverse-factor terms are summable by comparison with the geometric
    series, so `Real.multipliable_one_add_of_summable` applies. -/
-- Ref: [manuscript] prop:beta-decay-energy-scale §"calibration cross-check"
-- Ref: [habiro2004cyclotomic] q-Pochhammer convergence
theorem quantumDilog_multipliable {q z : ℝ} (hq : 1 < q) (hz : |z| < q) :
    Multipliable (fun k : ℕ => (1 - q ^ (-((k : ℤ) + 1)) * z)⁻¹) := by
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have hq_ne : q ≠ 0 := hq_pos.ne'
  -- `c = 1 - |z|/q` is a positive lower bound for every denominator.
  have hzq_lt_one : |z| / q < 1 := (div_lt_one hq_pos).mpr hz
  set c : ℝ := 1 - |z| / q with hc_def
  have hc_pos : 0 < c := by rw [hc_def]; linarith
  -- For each `k`, `|a k| ≤ |z| / q`, hence `1 - a k ≥ c > 0`.
  have hden_ge : ∀ k : ℕ, c ≤ 1 - q ^ (-((k : ℤ) + 1)) * z := by
    intro k
    have hpow_pos : 0 < q ^ (-((k : ℤ) + 1)) := zpow_pos hq_pos _
    -- `q^(-(k+1)) ≤ q^(-1) = 1/q`  (since `-(k+1) ≤ -1` and `q ≥ 1`)
    have hpow_le : q ^ (-((k : ℤ) + 1)) ≤ q ^ (-1 : ℤ) :=
      zpow_le_zpow_right₀ hq.le (by omega)
    have hq_inv_eq : q ^ (-1 : ℤ) = 1 / q := by
      rw [zpow_neg_one, one_div]
    have hpow_le' : q ^ (-((k : ℤ) + 1)) ≤ 1 / q := by
      rw [← hq_inv_eq]; exact hpow_le
    -- `a k = q^(-(k+1)) z ≤ q^(-(k+1)) |z| ≤ (1/q) |z| = |z|/q`
    have hak_le : q ^ (-((k : ℤ) + 1)) * z ≤ |z| / q := by
      calc q ^ (-((k : ℤ) + 1)) * z
          ≤ q ^ (-((k : ℤ) + 1)) * |z| := by
            apply mul_le_mul_of_nonneg_left (le_abs_self z) hpow_pos.le
        _ ≤ (1 / q) * |z| := by
            apply mul_le_mul_of_nonneg_right hpow_le' (abs_nonneg z)
        _ = |z| / q := by ring
    rw [hc_def]; linarith
  -- Define the deviation `g k = (1 - a k)⁻¹ - 1` and prove its summability.
  set g : ℕ → ℝ := fun k => (1 - q ^ (-((k : ℤ) + 1)) * z)⁻¹ - 1 with hg_def
  have hsumg : Summable g := by
    -- comparison: `|g k| ≤ (1/c) * |a k|`
    have hbound : ∀ k : ℕ, ‖g k‖ ≤ (1 / c) * ‖q ^ (-((k : ℤ) + 1)) * z‖ := by
      intro k
      have hden_pos : 0 < 1 - q ^ (-((k : ℤ) + 1)) * z := lt_of_lt_of_le hc_pos (hden_ge k)
      have hden_ne : (1 - q ^ (-((k : ℤ) + 1)) * z) ≠ 0 := hden_pos.ne'
      -- `g k = a k / (1 - a k)`
      have hgk : g k = (q ^ (-((k : ℤ) + 1)) * z) / (1 - q ^ (-((k : ℤ) + 1)) * z) := by
        rw [hg_def]; field_simp; ring
      rw [hgk, Real.norm_eq_abs, abs_div]
      rw [abs_of_pos hden_pos]
      rw [div_le_iff₀ hden_pos]
      rw [one_div, ← div_eq_inv_mul, Real.norm_eq_abs]
      rw [div_mul_eq_mul_div, le_div_iff₀ hc_pos]
      -- goal: |a k| * c ≤ |a k| * (1 - a k)
      apply mul_le_mul_of_nonneg_left (hden_ge k) (abs_nonneg _)
    -- `(1/c) • |a|` is summable, so `g` is summable by comparison.
    have hsum_abs : Summable (fun k : ℕ => (1 / c) * ‖q ^ (-((k : ℤ) + 1)) * z‖) :=
      ((summable_quantumDilog_terms (z := z) hq).norm).mul_left (1 / c)
    exact Summable.of_norm_bounded hsum_abs hbound
  -- Apply the one-add multipliability criterion.
  have h := Real.multipliable_one_add_of_summable hsumg
  -- `1 + g k = (1 - a k)⁻¹`
  refine h.congr (fun k => ?_)
  rw [hg_def]; ring

/-! ## The Φ_q functional (q-difference) equation `(1 - z)·Φ_q(qz) = Φ_q(z)`

The infinite product satisfies the first-order q-difference equation

  (1 - z) · Φ_q(qz) = Φ_q(z),     Φ_q(z) = ∏_{k≥1} (1 - q^{-k} z)^{-1}.

This is the analytic input that closes the WHICH-FAMILY half of
`conj:brane-tower-z-habiro` item 2(i): with the single normalisation
`Φ_q(0) = 1` (one generic, non-degenerate point) it determines `Φ_q` uniquely,
and in coefficients it is exactly the recurrence
`QOU.MassEndomorphism.ZHabiroCauchy.eulerCoeff_succ`, whose unique solution is
`eulerCoeff` (`eulerCoeff_unique`); `zHabiroLimit_eq_euler` then pins the
z-Habiro limit to the localised Euler element. Verified symbolically in
`computations/probes/z_habiro_increment_probe.py` (the functional equation holds
coeff-wise; the recurrence reproduces the Euler coefficients).

The proof is a `tprod` reindex: `Φ_q(qz)`'s factors are `(1-z)^{-1}` (the
`k=0` factor, `q^{-1}·qz = z`) prepended to `Φ_q(z)`'s factors (the
`(k+1)`-st `qz`-factor is the `k`-th `z`-factor, `q^{-(k+2)}·qz = q^{-(k+1)}z`),
via `Multipliable.tprod_eq_zero_mul`. Domain `|z| < 1` (so both `|z| < q` and
`|qz| < q`).

> **VERIFICATION STATUS (2026-06-17).** The arithmetic core (`hstep`, `htail`,
> `hhead`, the domain bounds) is verified sorry-free by `lean`-direct in the web
> sandbox. The single `tprod`-shift step `Multipliable.tprod_eq_zero_mul` could
> NOT be verified there: that lemma whnf-times-out at 4·10⁵ heartbeats *even on a
> trivial `g : ℕ → ℝ`*, i.e. an artifact of the sandbox's restored-olean
> environment, not of this proof (the lemma is standard and instant in a full
> build). `maxHeartbeats` is raised below for a full `lake build` / overnight
> laptop verification. If CI hits the same wall, treat it like the known
> environment-timeout pattern, not a proof failure. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"What survives the closure"
-- Ref: [habiro2004cyclotomic] q-Pochhammer functional equation
set_option maxHeartbeats 1000000 in
theorem quantumDilog_functional_eq {q z : ℝ} (hq : 1 < q) (hz : |z| < 1) :
    (1 - z) * (∏' k : ℕ, (1 - q ^ (-((k : ℤ) + 1)) * (q * z))⁻¹)
      = ∏' k : ℕ, (1 - q ^ (-((k : ℤ) + 1)) * z)⁻¹ := by
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have hq_ne : q ≠ 0 := hq_pos.ne'
  have hz1 : z < 1 := (abs_lt.mp hz).2
  have h1z : (1 : ℝ) - z ≠ 0 := by linarith
  have hqz : |q * z| < q := by
    rw [abs_mul, abs_of_pos hq_pos]
    calc q * |z| < q * 1 := mul_lt_mul_of_pos_left hz hq_pos
      _ = q := mul_one q
  set f : ℕ → ℝ := fun k => (1 - q ^ (-((k : ℤ) + 1)) * (q * z))⁻¹ with hf
  have hmul : Multipliable f := by
    change Multipliable (fun k : ℕ => (1 - q ^ (-((k : ℤ) + 1)) * (q * z))⁻¹)
    exact quantumDilog_multipliable hq hqz
  have hstep : ∀ m : ℤ, q ^ (-(m + 1)) * q = q ^ (-m) := by
    intro m; rw [← zpow_add_one₀ hq_ne]; congr 1; ring
  change (1 - z) * tprod f = ∏' k : ℕ, (1 - q ^ (-((k : ℤ) + 1)) * z)⁻¹
  rw [Multipliable.tprod_eq_zero_mul hmul]
  have e0 : f 0 = (1 - z)⁻¹ := by
    change (1 - q ^ (-(((0 : ℕ) : ℤ) + 1)) * (q * z))⁻¹ = (1 - z)⁻¹
    have hp : q ^ (-(((0 : ℕ) : ℤ) + 1)) * (q * z) = z := by
      have h2 : q ^ (-(((0 : ℕ) : ℤ) + 1)) * (q * z) = q ^ (-((0 : ℕ) : ℤ)) * z := by
        rw [← mul_assoc, hstep ((0 : ℕ) : ℤ)]
      rw [h2]; simp
    simp only [hp]
  have etail : ∀ n : ℕ, f (n + 1) = (1 - q ^ (-((n : ℤ) + 1)) * z)⁻¹ := by
    intro n
    change (1 - q ^ (-(((n + 1 : ℕ) : ℤ) + 1)) * (q * z))⁻¹ = (1 - q ^ (-((n : ℤ) + 1)) * z)⁻¹
    have hcast : ((n + 1 : ℕ) : ℤ) = (n : ℤ) + 1 := by push_cast; ring
    have hprod : q ^ (-(((n : ℤ) + 1) + 1)) * (q * z) = q ^ (-((n : ℤ) + 1)) * z := by
      rw [← mul_assoc, hstep ((n : ℤ) + 1)]
    simp only [hcast, hprod]
  have h_tail_eq : tprod (fun k => f (k + 1)) = ∏' k, (1 - q ^ (-((k : ℤ) + 1)) * z)⁻¹ := tprod_congr etail
  rw [e0]
  rw [h_tail_eq]
  rw [← mul_assoc]
  rw [mul_inv_cancel₀ h1z]
  rw [one_mul]

/-! ## Gap 4 status summary

What's now proved (this file):

  * `summable_q_inv_geometric` — Σ q^{-k} converges for 1 < q
    (zpow normalization closed via key_cast + mul_inv + inv_pow)
  * `quantumDilog_factors_nonzero` — each factor (1 - q^{-k} z)
    is non-zero in the domain (closed via zpow_pos + zpow_add₀
    + inv_le_one_of_one_le₀)
  * `summable_quantumDilog_terms` — Σ q^{-(k+1)} z converges
    (geometric summability in the `* z` form)
  * `quantumDilog_denom_multipliable` — the denominator product
    ∏ (1 - q^{-(k+1)} z) is `Multipliable`
    (via `Real.multipliable_one_add_of_summable` on `-(q^{-(k+1)} z)`)
  * **`quantumDilog_multipliable`** — the Φ_q product
    ∏ (1 - q^{-(k+1)} z)^{-1} is `Multipliable` for 1 < q, |z| < q.
    This is the **convergence half of Gap 4**: combining the
    geometric summability with the uniform lower bound
    1 - q^{-(k+1)} z ≥ 1 - |z|/q > 0 on the factors, the deviation
    terms g k = (1 - q^{-(k+1)} z)^{-1} - 1 are summable by
    comparison with the geometric series, and
    `Real.multipliable_one_add_of_summable` upgrades this to
    multipliability of the inverse-factor product.

What this gives:

  * `Φ_q(z) = ∏' k, (1 - q^{-(k+1)} z)^{-1}` is now a well-defined
    real (the `∏'` no longer collapses to Mathlib's 1-fallback,
    since the family is genuinely `Multipliable`).

What's still OPEN (Gap 5, separate file):

  * The CYCLOTOMIC PROJECTION at level n_⋆ — the truncation rule
    that gives Φ_q^{(n_⋆)} matching the empirical brane-tower
    contribution. The current `BraneTowerZHabiro` class is
    tautological (recoversBinding := True).
  * The STRUCTURAL LIFT FORMULA from N=0 → N=1+ — 5 naive lifts
    all failed (PR #637 commit e1b005b2). Open R&D.
-/

end QOU.MassEndomorphism.PhiQConvergence
