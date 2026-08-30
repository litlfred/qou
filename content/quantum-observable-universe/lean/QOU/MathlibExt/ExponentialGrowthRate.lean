import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.Analysis.Complex.Trigonometric
import Mathlib.Topology.Algebra.Order.Field

/-!
# QOU.MathlibExt.ExponentialGrowthRate — asymptotics that survive `(1/N)·log‖·‖`

Bean `qou-mlgp` **Gap 5**.

## Why this is the right first brick

Every volume-conjecture instance has the same shape. Some hard analysis — steepest
descent, Poisson summation — produces an asymptotic expansion

    `⟨K⟩_N = e^{Nζ} · N^{p} · ω · (1 + o(1))`,

and the conjecture is then read off its **exponential growth rate**,

    `(2π/N) · log‖⟨K⟩_N‖ → 2π · Re ζ = Vol(K)`.

The second step is not the hard analysis, and it should not be re-done per knot. It is
one fact — *a sub-exponential factor cannot change an exponential growth rate* — and
Mathlib does not have it in usable form.

That separation is what makes the "shrink the axiom" strategy pay: it moves everything
except the expansion itself out of the assumed input. See
`QOU.Archimedean.FiveTwoOhtsukiBridge`, where the entire content of part (C) is
`tendsto_log_norm_div_of_tendsto_one` below.

## What is here, and what is deliberately not

* `tendsto_log_norm_sub_div_atTop` — asymptotic equivalence preserves the growth rate.
* `tendsto_log_norm_model` — the growth rate of `e^{Nζ}·N^p·ω` is `Re ζ`, for any `p`
  and any `ω ≠ 0`. This is where `N^p` is shown not to matter, via
  `Real.isLittleO_log_id_atTop`.
* `tendsto_log_norm_div_of_tendsto_one` — the two composed, which is the statement a
  volume-conjecture bridge actually consumes.

**Not** here: anything that would *produce* such an expansion. Steepest descent and
stationary phase are absent from Mathlib entirely (measured: `grep -ril "steepest
descent\|stationary phase\|Laplace"` over the pinned rev `f897ebcf` returns nothing),
and building them is the expensive part of Gap 5. This file is the part that does not
need them, isolated so the cost of the part that does is visible.

Archimedean (ℝ, ℂ).
-/

namespace QOU.MathlibExt

open Filter Topology

/-- `log N / N → 0` along `ℕ`. The one place `N^p` is shown to be sub-exponential. -/
theorem tendsto_log_natCast_div_atTop :
    Tendsto (fun N : ℕ => Real.log (N : ℝ) / (N : ℝ)) atTop (𝓝 0) :=
  Real.isLittleO_log_id_atTop.tendsto_div_nhds_zero.comp tendsto_natCast_atTop_atTop

/-- `c / N → 0` along `ℕ`, for a constant `c`. -/
theorem tendsto_const_div_natCast_atTop (c : ℝ) :
    Tendsto (fun N : ℕ => c / (N : ℝ)) atTop (𝓝 0) :=
  tendsto_const_nhds.div_atTop tendsto_natCast_atTop_atTop

/-- **Asymptotic equivalence preserves the exponential growth rate.**

If `f N / g N → 1` then `(log‖f N‖ − log‖g N‖)/N → 0`. The `(1 + o(1))` factor of an
asymptotic expansion is invisible at this resolution — which is the entire reason a
volume conjecture can be read off an expansion whose subleading terms nobody has
computed. -/
theorem tendsto_log_norm_sub_div_atTop {f g : ℕ → ℂ}
    (hf : ∀ᶠ N in atTop, f N ≠ 0) (hg : ∀ᶠ N in atTop, g N ≠ 0)
    (h : Tendsto (fun N => f N / g N) atTop (𝓝 1)) :
    Tendsto (fun N : ℕ => (Real.log ‖f N‖ - Real.log ‖g N‖) / (N : ℝ)) atTop (𝓝 0) := by
  have hnorm : Tendsto (fun N : ℕ => ‖f N / g N‖) atTop (𝓝 1) := by
    simpa using h.norm
  have hlog : Tendsto (fun N : ℕ => Real.log ‖f N / g N‖) atTop (𝓝 0) := by
    have := (Real.continuousAt_log (one_ne_zero)).tendsto.comp hnorm
    simpa using this
  refine Tendsto.congr' ?_ (hlog.div_atTop tendsto_natCast_atTop_atTop)
  filter_upwards [hf, hg] with N hfN hgN
  rw [norm_div, Real.log_div (norm_ne_zero_iff.mpr hfN) (norm_ne_zero_iff.mpr hgN)]

/-- **The model's growth rate is `Re ζ`.**

`‖e^{Nζ}·N^p·ω‖ = e^{N·Re ζ}·N^p·‖ω‖`, so its log over `N` is
`Re ζ + p·(log N)/N + log‖ω‖/N`, and both correction terms vanish. The exponent `p` is
arbitrary — `3/2` for Ohtsuki's `5₂`, `1/2` for the deformed torus-knot expansions —
and never enters the limit. -/
theorem tendsto_log_norm_model (ζ ω : ℂ) (hω : ω ≠ 0) (p : ℝ) :
    Tendsto
      (fun N : ℕ =>
        Real.log ‖Complex.exp ((N : ℂ) * ζ) * (((N : ℝ) ^ p : ℝ) : ℂ) * ω‖ / (N : ℝ))
      atTop (𝓝 ζ.re) := by
  have heq : ∀ᶠ N : ℕ in atTop,
      Real.log ‖Complex.exp ((N : ℂ) * ζ) * (((N : ℝ) ^ p : ℝ) : ℂ) * ω‖ / (N : ℝ)
        = ζ.re + (p * Real.log (N : ℝ) + Real.log ‖ω‖) / (N : ℝ) := by
    filter_upwards [eventually_gt_atTop 0] with N hN
    have hNpos : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hN
    have h1 : ‖Complex.exp ((N : ℂ) * ζ)‖ = Real.exp ((N : ℝ) * ζ.re) := by
      rw [Complex.norm_exp]
      congr 1
      simp [Complex.mul_re]
    have h2 : ‖((((N : ℝ)) ^ p : ℝ) : ℂ)‖ = (N : ℝ) ^ p := by
      rw [Complex.norm_real, Real.norm_eq_abs, abs_of_pos (Real.rpow_pos_of_pos hNpos p)]
    rw [norm_mul, norm_mul, h1, h2,
      Real.log_mul (by positivity) (norm_ne_zero_iff.mpr hω),
      Real.log_mul (Real.exp_ne_zero _) (by positivity),
      Real.log_exp, Real.log_rpow hNpos]
    field_simp
    ring
  -- `heq` is an `Eventually` of an equation; `.symm` needs it seen as `EventuallyEq`,
  -- which is the same proposition but not the same head symbol for dot notation.
  refine Tendsto.congr' (Filter.EventuallyEq.symm heq) ?_
  have hcorr : Tendsto
      (fun N : ℕ => (p * Real.log (N : ℝ) + Real.log ‖ω‖) / (N : ℝ)) atTop (𝓝 0) := by
    have hsplit : ∀ N : ℕ, (p * Real.log (N : ℝ) + Real.log ‖ω‖) / (N : ℝ)
        = p * (Real.log (N : ℝ) / (N : ℝ)) + Real.log ‖ω‖ / (N : ℝ) := by
      intro N; ring
    simp only [hsplit]
    simpa using
      ((tendsto_log_natCast_div_atTop.const_mul p).add
        (tendsto_const_div_natCast_atTop (Real.log ‖ω‖)))
  simpa using tendsto_const_nhds.add hcorr

/-- **The statement a volume-conjecture bridge consumes.**

From the asymptotic expansion alone — no steepest descent, no geometry — the
exponential growth rate of `f` is `Re ζ`.

This is part (C) of `QOU.Archimedean.FiveTwoOhtsukiBridge`, stated once, for any knot
whose Kashaev invariant has such an expansion. -/
theorem tendsto_log_norm_div_of_tendsto_one {f : ℕ → ℂ} {ζ ω : ℂ} (hω : ω ≠ 0) (p : ℝ)
    (hf : ∀ᶠ N in atTop, f N ≠ 0)
    (h : Tendsto
      (fun N : ℕ => f N / (Complex.exp ((N : ℂ) * ζ) * (((N : ℝ) ^ p : ℝ) : ℂ) * ω))
      atTop (𝓝 1)) :
    Tendsto (fun N : ℕ => Real.log ‖f N‖ / (N : ℝ)) atTop (𝓝 ζ.re) := by
  set g : ℕ → ℂ := fun N => Complex.exp ((N : ℂ) * ζ) * (((N : ℝ) ^ p : ℝ) : ℂ) * ω with hg
  have hgne : ∀ᶠ N : ℕ in atTop, g N ≠ 0 := by
    filter_upwards [eventually_gt_atTop 0] with N hN
    have hNpos : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hN
    refine mul_ne_zero (mul_ne_zero (Complex.exp_ne_zero _) ?_) hω
    simpa using (Real.rpow_pos_of_pos hNpos p).ne'
  have hdiff := tendsto_log_norm_sub_div_atTop hf hgne h
  have hmodel := tendsto_log_norm_model ζ ω hω p
  have := hdiff.add hmodel
  simp only [zero_add] at this
  refine this.congr fun N => ?_
  by_cases hN : (N : ℝ) = 0
  · simp [hN]
  · -- unfold `g`, so that `‖g N‖` and the model's norm are syntactically one term;
    -- what remains is `a - b + b = a`.
    simp only [hg]
    field_simp
    ring

end QOU.MathlibExt
