import QOU.MathlibExt.ComplexDilogarithmDeriv
import Mathlib.Analysis.SpecialFunctions.Integrability.Basic

/-!
# Toward `cLiTwoExt` at `x > 1`: the real-argument decomposition of `log`

Bean `qou-invr`, step (1), **partial**. This file contains one small proved
lemma and **no proof of the integrability statement itself** — see "What is
NOT here" below, which is the more useful half of this file.

## Why step (1) exists

Route 35 showed the inversion leg is not a boundary-value problem: `Re Li₂` is
continuous across `[1,∞)` because `Li₂`'s jump `2πi·log x` is purely imaginary.
What that left is concrete: `cLiTwoExt y = −∫₀¹ log(1 − y·t)/t dt`, and every
existing integrability lemma (`intervalIntegrable_log_one_sub_div_of_slitPlane`
and its `notCut` corollary) assumes the integrand avoids `log`'s cut on the
**whole** of `[0,1]`. For real `x > 1` that fails — `1 − x·t` changes sign at
`t = 1/x ∈ (0,1)`.

**This is not a technicality.** A Lean `∫` of a non-integrable function is the
junk value `0`, so until integrability is proved, every statement about
`cLiTwoExt x` for `x > 1` is a statement about `0`: vacuously true and useless.
Exactly the "true and about nothing" failure this lane has hit before.

## What IS proved here

`log_ofReal_eq` — for real `r ≠ 0`, the principal `Complex.log` splits as
`Real.log |r| + arg(r)·I`. Every route to step (1) starts by separating the
divergent real part from the bounded `arg`, so this is the first line of all of
them. Small, but it is a theorem rather than a plan.

## What is NOT here, and the recipe for it

The integrability statement itself. It is **not** stubbed — there is no `sorry`
in this file and no theorem asserting it. The recipe, with the hard step already
located in Mathlib:

1. **Split at `c = 1/(2x)`**, so `0 < c < 1/x` and `1 − x·t ≥ 1/2` on `[0,c]`.
   Combine the pieces with `IntervalIntegrable.trans`.
2. **On `[0,c]`** the slit hypothesis holds, so the *existing*
   `intervalIntegrable_log_one_sub_div_of_slitPlane` applies — modulo
   generalising its right endpoint from `1` to `c`, which its proof (a removable
   singularity at `0` via `hasDerivAt_iff_tendsto_slope`) should tolerate
   mechanically. The `t = 0` singularity is removable and this is where that is
   handled.
3. **On `[c,1]`**, `1/t` is continuous and bounded, so it suffices that
   `t ↦ log(1 − x·t)` is integrable. Split it with `log_ofReal_eq`:
   * the real part is `Real.log |1 − x·t| = Real.log (1 − x·t)` — `Real.log` is
     even, `Real.log_abs` — and **`Mathlib.intervalIntegrable_log'` gives this
     unconditionally, singularity included.** That is the crux, and it is
     already in Mathlib. `intervalIntegrable_log_norm_meromorphicOn` is a second
     route to the same thing, `1 − x·t` being a polynomial.
   * the `arg` part is bounded by `π` and measurable (`Complex.measurable_arg`),
     hence integrable on a compact interval.

Step 3's crux being a pre-existing unconditional Mathlib lemma is the reason
`qou-invr` was re-priced from "new analytic infrastructure" to "an integrability
lemma". Steps 1–2 are the remaining assembly and neither is deep.

**The 5₂ sum rule remains verified to 80 dps, unproved.**
-/

namespace QOU.MathlibExt

open Complex

/-- **The real-argument decomposition of the principal logarithm.**

For real `r`, `log r = log |r| + arg(r)·I`, with `arg(r) ∈ {0, π}` according to
the sign. Separating the divergent real part from the bounded `arg` is the first
step of every route to integrability on the cut. -/
theorem log_ofReal_eq (r : ℝ) :
    Complex.log ((r : ℝ) : ℂ) = ((Real.log |r| : ℝ) : ℂ)
      + ((Complex.arg ((r : ℝ) : ℂ) : ℝ) : ℂ) * Complex.I := by
  rw [Complex.log]
  congr 2
  rw [Complex.norm_real, Real.norm_eq_abs]

/-- The real part is a genuine real logarithm — and `Real.log` is even, so the
absolute value costs nothing. This is the form `intervalIntegrable_log'`
consumes. -/
theorem re_log_ofReal (r : ℝ) : (Complex.log ((r : ℝ) : ℂ)).re = Real.log r := by
  rw [Complex.log_re, Complex.norm_real, Real.norm_eq_abs, Real.log_abs]

/-- And the imaginary part is bounded by `π`, uniformly — the half that is
integrable for trivial reasons. -/
theorem abs_im_log_ofReal_le (r : ℝ) :
    |(Complex.log ((r : ℝ) : ℂ)).im| ≤ Real.pi := by
  rw [Complex.log_im]
  exact Complex.abs_arg_le_pi _

end QOU.MathlibExt
