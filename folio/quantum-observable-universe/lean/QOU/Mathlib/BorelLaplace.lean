/-
  Borel resummation — the Laplace term-wise engine (bean el8w tranche 3).

  This is the "second half" the header of `QOU/Mathlib/BorelResummation.lean`
  names as the genuine Mathlib gap: the Laplace resummation
  `∫₀^∞ e^{−t} φ(z t) dt` that recovers `Σ aₙ zⁿ` from its Borel transform
  `φ`. Tranche 2 (`BorelResummation.lean`) proved the hypothesis half —
  Gevrey-1 ⇒ Borel-disc convergence, sorry-free. This file proves the
  TERM-WISE ENGINE of the resummation, now that the Gamma / measure-theory
  olean cone is available:

    * `laplace_pow_eq_factorial`:  `∫₀^∞ e^{−t} tⁿ dt = n!`  — the atomic
      identity the whole resummation rests on (Euler's Gamma integral at a
      natural argument), transcribed from `Real.Gamma_eq_integral` +
      `Real.Gamma_nat_eq_factorial`.
    * `laplace_borel_term`:  `∫₀^∞ e^{−t} (aₙ/n!)(z t)ⁿ dt = aₙ zⁿ`  — the
      n-th Borel-transform term Laplace-integrates back EXACTLY to the n-th
      term of the original series. This is the mechanism by which the Laplace
      transform of the Borel sum reproduces the divergent series term by term.

  What is STILL the documented gap (not in this file, honestly not faked): the
  interchange of `∑` and `∫₀^∞` under a Gevrey-1 dominating bound (dominated
  convergence over the Borel disc) and the Watson / Nevanlinna–Sokal
  UNIQUENESS theorem. Those upgrade the per-term engine to the full
  resummation-recovers-the-function statement; next el8w tranche.

  Archimedean (ℝ): genuinely archimedean — Euler's integral, `Real.exp`,
  measure theory on `Set.Ioi 0` (§7c).

  -- Ref: [sokal1980] https://doi.org/10.1063/1.524408
-/

import QOU.Mathlib.BorelResummation
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.MeasureTheory.Integral.DominatedConvergence

namespace QOU.Mathlib.Borel

open scoped Nat
open MeasureTheory Set

/-- **The Laplace term-wise engine**: `∫₀^∞ e^{−t} tⁿ dt = n!`. Euler's Gamma
    integral at the natural argument `s = n + 1`, with `Real.rpow` collapsed to
    the monoid power on `t`. This is the single analytic fact underneath Borel
    resummation — every `n!` that Borel division removed is restored by this
    Laplace integral. -/
theorem laplace_pow_eq_factorial (n : ℕ) :
    ∫ t in Ioi (0 : ℝ), Real.exp (-t) * t ^ n = (n ! : ℝ) := by
  have hs : (0 : ℝ) < (n : ℝ) + 1 := by positivity
  have h := Real.Gamma_eq_integral hs
  rw [Real.Gamma_nat_eq_factorial] at h
  rw [h]
  refine setIntegral_congr_fun measurableSet_Ioi (fun x _ => ?_)
  rw [add_sub_cancel_right, Real.rpow_natCast]

/-- **Per-term Borel recovery**: the `n`-th term of the Borel transform,
    `(aₙ/n!)(z t)ⁿ`, Laplace-integrates back to the `n`-th term `aₙ zⁿ` of the
    original series. The Borel division by `n!` and the Laplace multiplication
    by `n!` (from `laplace_pow_eq_factorial`) cancel exactly — the mechanism of
    Borel resummation, term by term. -/
theorem laplace_borel_term (a : ℕ → ℝ) (z : ℝ) (n : ℕ) :
    ∫ t in Ioi (0 : ℝ), Real.exp (-t) * (borelCoeff a n * (z * t) ^ n)
      = a n * z ^ n := by
  have key : ∀ t : ℝ,
      Real.exp (-t) * (borelCoeff a n * (z * t) ^ n)
        = (borelCoeff a n * z ^ n) * (Real.exp (-t) * t ^ n) := by
    intro t; rw [mul_pow]; ring
  rw [setIntegral_congr_fun measurableSet_Ioi (fun t _ => key t),
    integral_const_mul, laplace_pow_eq_factorial]
  have hn : (n ! : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero n)
  unfold borelCoeff
  field_simp

/-- The factorial series `Σ n! zⁿ` recovers its `n`-th term `n! zⁿ` under the
    Laplace engine — the concrete example: its unit Borel coefficients times
    `(z t)ⁿ` Laplace-integrate to `n! zⁿ`. -/
example (z : ℝ) (n : ℕ) :
    ∫ t in Ioi (0 : ℝ), Real.exp (-t) * (borelCoeff (fun k => (k ! : ℝ)) n * (z * t) ^ n)
      = (n ! : ℝ) * z ^ n :=
  laplace_borel_term (fun k => (k ! : ℝ)) z n

/-!
### The ∑ ↔ ∫ interchange — Borel-summation REGULARITY on the disc of convergence

The full resummation `∫₀^∞ e^{−t} φ(z t) dt = Σ aₙ zⁿ` (φ = Borel transform)
holds by exchanging `Σ` and `∫₀^∞`. Contrary to a naive "Gevrey-1 dominating
bound" reading, that interchange does **NOT** hold for a divergent Gevrey-1
series: there `∑ₙ ∫₀^∞ |e^{−t}(aₙ/n!)(z t)ⁿ| dt = ∑ₙ |aₙ||z|ⁿ = ∞`, which is
precisely *why* Borel summation of a divergent series is nontrivial (the
Borel-plane singularity on the ray is the alien-calculus/Stokes obstruction —
Watson / Nevanlinna–Sokal territory, still the open el8w gap).

The interchange DOES hold on the **disc of convergence**: when `∑ₙ |aₙ||z|ⁿ < ∞`
the dominating series is finite, `MeasureTheory.integral_tsum` applies, and each
term Laplace-integrates back by `laplace_borel_term`. The result is the
**regularity** (consistency) property: *where the series already converges,
Borel summation reproduces its ordinary sum.* This is the singularity-free base
layer of resurgence — proved sorry-free below.
-/

open scoped ENNReal

/-- Integrability of the `n`-th Borel integrand `e^{−t}·(borelCoeff a n)(z t)ⁿ`
    on `Ioi 0`: it is the constant `borelCoeff a n · zⁿ` times Euler's
    convergent `e^{−t} tⁿ`. -/
theorem integrableOn_borelIntegrand (a : ℕ → ℝ) (z : ℝ) (n : ℕ) :
    IntegrableOn (fun t => Real.exp (-t) * (borelCoeff a n * (z * t) ^ n)) (Ioi 0) := by
  have hg : IntegrableOn (fun t => Real.exp (-t) * t ^ n) (Ioi 0) := by
    have h := Real.GammaIntegral_convergent (s := (n : ℝ) + 1) (by positivity)
    refine h.congr_fun (fun x _ => ?_) measurableSet_Ioi
    rw [add_sub_cancel_right, Real.rpow_natCast]
  refine IntegrableOn.congr_fun (hg.const_mul (borelCoeff a n * z ^ n))
    (fun t _ => ?_) measurableSet_Ioi
  rw [mul_pow]; ring

/-- `∫₀^∞ ‖e^{−t}(borelCoeff a n)(z t)ⁿ‖ dt = |aₙ| |z|ⁿ`. The `|borelCoeff a n|`
    and the `n!` from `laplace_pow_eq_factorial` cancel to `|aₙ|`. -/
theorem integral_norm_borelIntegrand (a : ℕ → ℝ) (z : ℝ) (n : ℕ) :
    ∫ t in Ioi (0 : ℝ), ‖Real.exp (-t) * (borelCoeff a n * (z * t) ^ n)‖
      = |a n| * |z| ^ n := by
  have key : EqOn (fun t => ‖Real.exp (-t) * (borelCoeff a n * (z * t) ^ n)‖)
      (fun t => (|borelCoeff a n| * |z| ^ n) * (Real.exp (-t) * t ^ n)) (Ioi 0) := by
    intro t ht
    have h1 : |Real.exp (-t)| = Real.exp (-t) := abs_of_pos (Real.exp_pos _)
    have h2 : |t| = t := abs_of_pos ht
    simp only [Real.norm_eq_abs]
    rw [abs_mul, h1, abs_mul, abs_pow, abs_mul, h2, mul_pow]
    ring
  rw [setIntegral_congr_fun measurableSet_Ioi key, integral_const_mul,
    laplace_pow_eq_factorial]
  unfold borelCoeff
  rw [abs_div, abs_of_pos (show (0 : ℝ) < (n ! : ℝ) by positivity)]
  field_simp

/-- `∫⁻₀^∞ ‖e^{−t}(borelCoeff a n)(z t)ⁿ‖ₑ dt = ENNReal.ofReal (|aₙ| |z|ⁿ)`. -/
theorem lintegral_enorm_borelIntegrand (a : ℕ → ℝ) (z : ℝ) (n : ℕ) :
    ∫⁻ t in Ioi (0 : ℝ), ‖Real.exp (-t) * (borelCoeff a n * (z * t) ^ n)‖ₑ
      = ENNReal.ofReal (|a n| * |z| ^ n) := by
  rw [← ofReal_integral_norm_eq_lintegral_enorm (integrableOn_borelIntegrand a z n),
    integral_norm_borelIntegrand]

/-- The **Borel sum** of `a` at `z`: the Laplace transform of the pointwise Borel
    transform `φ(w) = ∑' n, borelCoeff a n · wⁿ` along `ℝ₊`,
    `∫₀^∞ e^{−t} φ(z t) dt`. -/
noncomputable def borelSum (a : ℕ → ℝ) (z : ℝ) : ℝ :=
  ∫ t in Ioi (0 : ℝ), Real.exp (-t) * ∑' n, borelCoeff a n * (z * t) ^ n

/-- **Borel-summation regularity / consistency.** When the series converges
    absolutely at `z` (`∑ₙ |aₙ||z|ⁿ < ∞`), the Borel sum equals the ordinary
    sum: `∫₀^∞ e^{−t} φ(z t) dt = ∑' n, aₙ zⁿ`. Proved by `integral_tsum` — the
    absolute-convergence hypothesis is exactly the finiteness of the dominating
    `∑ₙ ∫ ‖·‖` — with each term recovered by `laplace_borel_term`. Sorry-free;
    the divergent (Gevrey-1) case, where this fails, is the open Watson gap. -/
theorem borelSum_eq_tsum (a : ℕ → ℝ) (z : ℝ)
    (hconv : Summable (fun n => |a n| * |z| ^ n)) :
    borelSum a z = ∑' n, a n * z ^ n := by
  have hmeas : ∀ n, AEStronglyMeasurable
      (fun t => Real.exp (-t) * (borelCoeff a n * (z * t) ^ n))
      (volume.restrict (Ioi (0 : ℝ))) :=
    fun n => (integrableOn_borelIntegrand a z n).aestronglyMeasurable
  have hfin : (∑' n, ∫⁻ t in Ioi (0 : ℝ),
      ‖Real.exp (-t) * (borelCoeff a n * (z * t) ^ n)‖ₑ) ≠ ∞ := by
    rw [tsum_congr (lintegral_enorm_borelIntegrand a z),
      ← ENNReal.ofReal_tsum_of_nonneg (fun n => by positivity) hconv]
    exact ENNReal.ofReal_ne_top
  unfold borelSum
  have hpush : (fun t => Real.exp (-t) * ∑' n, borelCoeff a n * (z * t) ^ n)
      = (fun t => ∑' n, Real.exp (-t) * (borelCoeff a n * (z * t) ^ n)) := by
    funext t; exact tsum_mul_left.symm
  rw [hpush, integral_tsum hmeas hfin]
  exact tsum_congr (laplace_borel_term a z)

end QOU.Mathlib.Borel
