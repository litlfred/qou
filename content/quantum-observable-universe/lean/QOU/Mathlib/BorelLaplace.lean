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

end QOU.Mathlib.Borel
