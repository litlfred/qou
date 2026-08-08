import QOU.MathlibExt.ComplexDilogarithmDeriv
import Mathlib.Analysis.SpecialFunctions.Integrability.Basic
import Mathlib.Analysis.SpecialFunctions.Integrability.LogMeromorphic

/-!
# `cLiTwoExt`'s integrand is integrable at real `x > 0` — `qou-invr` step (1), DONE

Bean `qou-invr`, **step (1) complete**:

    intervalIntegrable_clog_one_sub_div_ofReal {x : ℝ} (hx : 0 < x) :
      IntervalIntegrable (fun t => log (1 − x·t) / t) volume 0 1

Both singularities handled — the **logarithmic** one at `t = 1/x` (in range
exactly when `x > 1`, which is the whole difficulty) and the **removable** one
at `t = 0`. Verified at `x = 2.24698`, i.e. at `w₁` itself.

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

## What IS proved

`intervalIntegrable_clog_one_sub_mul (x a b : ℝ)` — the full complex statement,
on any interval. It is assembled from:

* `log_ofReal_eq` — for real `r`, `log r = log |r| + arg(r)·I`. Separating the
  divergent real part from the bounded `arg` is the first line of the argument.
* `arg_one_sub_mul_ofReal` — `arg (1 − x·t)` is an explicit **two-valued step
  function**, `0` before the sign change and `π` after. So the branch jump is
  not an obstacle at all; it is a bounded measurable function.
* `intervalIntegrable_real_log_one_sub_mul` — the real half, **unconditional**.
  `1 − x·t` is affine, hence analytic, hence meromorphic, so Mathlib's
  `intervalIntegrable_log_norm_meromorphicOn` applies directly; `Real.log` is
  even (`Real.log_abs`) so the `‖·‖` costs nothing.

That last step is why this closed. The hard part — integrating `log` *through*
its own singularity — was already in Mathlib, twice over
(`intervalIntegrable_log'` unconditionally, and the meromorphic version used
here). `qou-invr` had priced this leg as "new analytic infrastructure"; it was
API archaeology.

## The `1/t` assembly, as built

`1/t` is a **second, independent** singularity at `t = 0` — removable
(`log(1 − x·t) ~ −x·t`), and unrelated to the logarithmic one.

1. Split at `c = 1/(2x)` (`IntervalIntegrable.trans`), so `1 − x·t ≥ 1/2` on `[0,c]`.
2. `intervalIntegrable_integrand_right` — on `[c,1]`, `1/t` is continuous
   (`t ≥ c > 0`), so it peels off with `IntervalIntegrable.mul_continuousOn`
   against the theorem above.
3. `intervalIntegrable_integrand_left` — on `[0,c]`, **rescale to the existing
   `intervalIntegrable_log_one_sub_div_of_slitPlane`** rather than reprove the
   removable singularity. The substitution `t = c·u` sends the integrand to
   `log(1 − u/2)/u`, whose slit hypothesis holds outright (`Re(1 − u/2) ≥ 1/2`),
   and `comp_mul_left` transports `0..1` to `0..c`. The removable singularity at
   `0` is thereby handled by the proof that already existed.

⚠ **A performance note worth keeping.** Step 3 first appeared to be a
*mathematical* obstruction: it timed out at 63s even with a 10× heartbeat
budget. The cause was neither the analysis nor `comp_mul_left`'s side
conditions — it was a `rw [one_div]` in the goal that `hcomp` did not carry, so
`exact` had to unify `(2x)⁻¹` against `1/(2x)` under a pile of casts. Deleting
that one rewrite made it instant. **An elaboration timeout is not evidence that
a step is hard.**

## What remains for `qou-invr`

Step (2) only: the real identity `Re Li₂(x) + Li₂(1/x) = π²/3 − ½·log²x` for
`x > 1` (Route 35 G3, measured at 1e-25). Step (1) no longer blocks it — and
because of it, `cLiTwoExt x` for `x > 1` is now a **provably real object** in
Lean rather than an integral that might be the junk value `0`.

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

/-! ## The crux: `log (1 − x·t)` is integrable across its own singularity -/

/-- `arg (1 − x·t)` for real `x, t` is an explicit two-valued step function. -/
theorem arg_one_sub_mul_ofReal (x t : ℝ) :
    Complex.arg (((1 - x * t : ℝ)) : ℂ) = if 1 - x * t < 0 then Real.pi else 0 := by
  by_cases h : 1 - x * t < 0
  · rw [if_pos h, Complex.arg_ofReal_of_neg h]
  · rw [if_neg h, Complex.arg_ofReal_of_nonneg (not_lt.mp h)]

/-- **`t ↦ Real.log (1 − x·t)` is interval-integrable on ANY interval**, the
logarithmic singularity at `t = 1/x` included.

Via `intervalIntegrable_log_norm_meromorphicOn`: `1 − x·t` is affine, hence
analytic, hence meromorphic, and `Real.log` is even so `‖·‖` costs nothing. -/
theorem intervalIntegrable_real_log_one_sub_mul (x a b : ℝ) :
    IntervalIntegrable (fun t : ℝ => Real.log (1 - x * t))
      MeasureTheory.volume a b := by
  have hmero : MeromorphicOn (fun t : ℝ => (1 - x * t : ℝ)) (Set.uIcc a b) := by
    intro t _
    exact (analyticAt_const.sub (analyticAt_const.mul analyticAt_id)).meromorphicAt
  have h := intervalIntegrable_log_norm_meromorphicOn hmero
  simpa [Real.norm_eq_abs, Real.log_abs] using h

/-- The bounded `arg` half: a two-valued step function is interval-integrable. -/
theorem intervalIntegrable_arg_step (x a b : ℝ) :
    IntervalIntegrable (fun t : ℝ => if 1 - x * t < 0 then Real.pi else 0)
      MeasureTheory.volume a b := by
  have hmeas : Measurable (fun t : ℝ => if 1 - x * t < 0 then Real.pi else 0) := by
    refine Measurable.ite ?_ measurable_const measurable_const
    exact measurableSet_lt (by fun_prop) measurable_const
  refine ⟨?_, ?_⟩ <;>
  · refine MeasureTheory.Measure.integrableOn_of_bounded (M := Real.pi) ?_
      hmeas.aestronglyMeasurable ?_
    · exact (measure_Ioc_lt_top).ne
    · filter_upwards with t
      by_cases h : 1 - x * t < 0 <;> simp [h, Real.pi_nonneg, abs_of_nonneg]

/-- **`t ↦ Complex.log (1 − x·t)` is interval-integrable on any interval**, for
real `x` — across the cut, singularity and branch jump included. -/
theorem intervalIntegrable_clog_one_sub_mul (x a b : ℝ) :
    IntervalIntegrable (fun t : ℝ => Complex.log ((1 : ℂ) - (x : ℂ) * (t : ℂ)))
      MeasureTheory.volume a b := by
  have hsplit : (fun t : ℝ => Complex.log ((1 : ℂ) - (x : ℂ) * (t : ℂ)))
      = fun t : ℝ => ((Real.log (1 - x * t) : ℝ) : ℂ)
          + ((if 1 - x * t < 0 then Real.pi else 0 : ℝ) : ℂ) * Complex.I := by
    funext t
    have hcast : (1 : ℂ) - (x : ℂ) * (t : ℂ) = (((1 - x * t : ℝ)) : ℂ) := by
      push_cast; ring
    rw [hcast, log_ofReal_eq, arg_one_sub_mul_ofReal, Real.log_abs]
  rw [hsplit]
  refine IntervalIntegrable.add ?_ ?_
  · -- `IntervalIntegrable` is a conjunction of `IntegrableOn`, and
    -- `Integrable.ofReal` lifts each half from ℝ to ℂ
    obtain ⟨h1, h2⟩ := intervalIntegrable_real_log_one_sub_mul x a b
    exact ⟨h1.ofReal, h2.ofReal⟩
  · have hstep : IntervalIntegrable
        (fun t : ℝ => ((if 1 - x * t < 0 then Real.pi else 0 : ℝ) : ℂ))
        MeasureTheory.volume a b := by
      obtain ⟨h1, h2⟩ := intervalIntegrable_arg_step x a b
      exact ⟨h1.ofReal, h2.ofReal⟩
    exact hstep.mul_const _

/-! ## The `1/t` assembly: the second, removable singularity -/

/-- **Away from `0` the integrand is integrable**: `1/t` is continuous there, so
it peels off against `intervalIntegrable_clog_one_sub_mul`. -/
theorem intervalIntegrable_integrand_right {x c : ℝ} (hc : 0 < c) :
    IntervalIntegrable (fun t : ℝ => Complex.log ((1 : ℂ) - (x : ℂ) * (t : ℂ)) / (t : ℂ))
      MeasureTheory.volume c 1 := by
  have hcont : ContinuousOn (fun t : ℝ => ((t : ℂ))⁻¹) (Set.uIcc c 1) := by
    refine ContinuousOn.inv₀ (Complex.continuous_ofReal.continuousOn) ?_
    intro t ht
    have ht0 : t ≠ 0 := by
      rcases Set.mem_uIcc.mp ht with h | h
      · exact ne_of_gt (lt_of_lt_of_le hc h.1)
      · exact ne_of_gt (lt_of_lt_of_le zero_lt_one h.1)
    simpa using ht0
  have h := (intervalIntegrable_clog_one_sub_mul x c 1).mul_continuousOn hcont
  simpa [div_eq_mul_inv] using h

set_option maxHeartbeats 1000000 in
/-- **Near `0` the integrand is integrable**, by rescaling to the existing
`slitPlane` lemma. With `c = 1/(2x)` the substitution `t = c·u` turns the
integrand into `log(1 − u/2)/u`, whose slit hypothesis holds outright. -/
theorem intervalIntegrable_integrand_left {x : ℝ} (hx : 0 < x) :
    IntervalIntegrable (fun t : ℝ => Complex.log ((1 : ℂ) - (x : ℂ) * (t : ℂ)) / (t : ℂ))
      MeasureTheory.volume 0 (1 / (2 * x)) := by
  have h2x : (0 : ℝ) < 2 * x := by linarith
  -- the rescaled integrand, with `y = 1/2`, is covered by the existing lemma
  have hF : IntervalIntegrable
      (fun u : ℝ => Complex.log ((1 : ℂ) - (1 / 2 : ℂ) * (u : ℂ)) / (u : ℂ))
      MeasureTheory.volume 0 1 := by
    refine intervalIntegrable_log_one_sub_div (fun u h0 h1 => ?_)
    have : ((1 : ℂ) - (1 / 2 : ℂ) * (u : ℂ)).re = 1 - u / 2 := by
      simp [Complex.sub_re, Complex.mul_re]
      ring
    rw [this]
    linarith
  have hcomp := hF.comp_mul_left (c := 2 * x) (by simp) (by simp)
  rw [zero_div] at hcomp
  -- `F (2x · t) = (1/(2x)) · f t`, so `f = (2x) · (F ∘ (2x · ·))`
  have hfun : (fun t : ℝ =>
      Complex.log ((1 : ℂ) - (x : ℂ) * (t : ℂ)) / (t : ℂ))
      = fun t : ℝ => ((2 * x : ℝ) : ℂ) *
          (Complex.log ((1 : ℂ) - (1 / 2 : ℂ) * (((2 * x) * t : ℝ) : ℂ))
            / ((((2 * x) * t : ℝ)) : ℂ)) := by
    funext t
    have harg : ((1 : ℂ) - (1 / 2 : ℂ) * (((2 * x) * t : ℝ) : ℂ))
        = (1 : ℂ) - (x : ℂ) * (t : ℂ) := by push_cast; ring
    rw [harg]
    by_cases ht : t = 0
    · simp [ht]
    · have htc : ((t : ℝ) : ℂ) ≠ 0 := by simpa using ht
      have hxc : ((x : ℝ) : ℂ) ≠ 0 := by
        simpa using (ne_of_gt hx)
      push_cast
      field_simp
  rw [hfun]
  exact hcomp.const_mul _

/-- **`cLiTwoExt`'s integrand is integrable at real `x > 0`** — both
singularities handled: the logarithmic one at `t = 1/x` (if it is in range) and
the removable one at `t = 0`. This is `qou-invr` step (1). -/
theorem intervalIntegrable_clog_one_sub_div_ofReal {x : ℝ} (hx : 0 < x) :
    IntervalIntegrable (fun t : ℝ => Complex.log ((1 : ℂ) - (x : ℂ) * (t : ℂ)) / (t : ℂ))
      MeasureTheory.volume 0 1 :=
  (intervalIntegrable_integrand_left hx).trans
    (intervalIntegrable_integrand_right (by positivity))

end QOU.MathlibExt
