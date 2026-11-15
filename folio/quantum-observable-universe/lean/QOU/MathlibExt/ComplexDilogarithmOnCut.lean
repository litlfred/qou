import QOU.MathlibExt.ComplexDilogarithmDeriv
import Mathlib.Analysis.SpecialFunctions.Integrability.Basic
import Mathlib.Analysis.SpecialFunctions.Integrability.LogMeromorphic
import QOU.MathlibExt.ComplexDilogarithmBoundary
import QOU.Archimedean.ConstantOffOnePoint

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

## And the derivative ON the cut, which step (2) turns on

    hasDerivAt_cLiTwoExt_ofReal (hx : 0 < x) (hx1 : x ≠ 1) :
      HasDerivAt (fun s : ℝ => cLiTwoExt s) (−log(1 − x)/x) x

Verified at `x = 2.24698`, i.e. **strictly on the cut**.

`qou-invr` recorded a subtlety here: `hasDerivAt_cLiTwoExt_radial` differentiates
in the **parameter `s` along a fixed ray**, while the constancy argument needs the
derivative in **`x`, which moves the ray** — and converting one to the other
seemed to presuppose the differentiability being established.

**That dissolves.** The cap `t ≤ 1` in the original existed only because
integrability was known on `[0,1]`; `intervalIntegrable_clog_one_sub_div_ofReal'`
removes it. With the cap gone, take the **ray direction to be `1`** — then the
radial parameter *is* `x`, and the radial derivative *is* the `x`-derivative. No
chain rule run backwards, no circularity.

⚠ `x ≠ 1` is load-bearing and is what replaces `notCut`: at `x = 1` the kernel
genuinely diverges. A version admitting it would be false.

## What remains for `qou-invr`

Step (2)'s constancy argument, now with all three derivatives available:

| term | derivative on `x > 1` | source |
|---|---|---|
| `Re cLiTwoExt(x)` | `−log(x−1)/x` | **`hasDerivAt_cLiTwoExt_ofReal` + `re_log_ofReal`** |
| `LiTwo(1/x)` | `(log(x−1) − log x)/x` | off the cut, routine |
| `½·log²x` | `log x / x` | routine |

They cancel identically. **`hasDerivAt_inversionCombo` proves `G' = 0` on
`(1,∞)`** — the analytic core of step (2), done.

### ✅ AND THE CONSTANT IS PINNED — step (2) is closed

    re_inversion_identity (hx : 1 ≤ x) :
      Re cLiTwoExt(x) + Re cLiTwoExt(1/x) + ½·log²x = π²/3

The value came from `cLiTwoExt_one : cLiTwoExt 1 = π²/6`, which needed a route
around **both** existing boundary lemmas — see below. The exceptional point
`x = 1`, where the derivative does not exist, costs nothing:
`constant_of_hasDerivWithinAt_zero_off_point` is built for exactly that shape,
and was already in the tree for the transport lane.

### How `cLiTwoExt 1 = π²/6` was obtained

`1` is **the excluded point of both** existing lemmas — `cLiTwoExt_eq_cLiTwo`
needs `‖y‖ < 1`, `cLiTwoExt_eq_cLiTwo_of_norm_le_one` needs `y ∈ notCut`. The
route around:

* `cLiTwo 1 = π²/6` is immediate — the **series converges at `1`**, so this is
  just `hasSum_one_div_succ_sq`. No boundary theory.
* `cLiTwoExt` along the reals **is a primitive** (`cLiTwoExt_ofReal_eq_primitive`,
  from `cLiTwoExt_ofReal_mul` at `y = 1`), and primitives of integrable functions
  are continuous — **integrability at `x = 1` being step (1)**.
* So both are continuous along `[0,1]` and agree on `[0,1)`; the value at the
  branch point follows by uniqueness of limits.

Step (1) is therefore not merely a prerequisite of step (2) — it is what makes
the branch point reachable at all.

### The earlier framing, kept because the contrast still holds

`G' = 0` gives the identity only up to a constant, and Route 35 G3 measures
`G ≡ π²/3`. Pinning it needs one value, and the only available base point is
`x → 1⁺`, where `½·log²x → 0` and both dilogarithm terms tend to
`Re cLiTwoExt(1)`. So the constant is `2·Re cLiTwoExt(1)`, and the identity is
equivalent to

    Re cLiTwoExt(1) = π²/6.

**Contrast with the Landen leg, which is the instructive part.** There the base
point could be taken at `z → 0⁻`, where *every term vanishes outright* — so no
special value was needed and the leg closed. Here the base point is forced to
the **branch point** `x = 1`, where the value is `π²/6` rather than `0`. The two
legs differ not in their derivative arguments, which are equally routine, but in
whether the natural base point is a zero or a special value.

Two things are needed, and neither is free:

1. `Re cLiTwoExt(1) = π²/6`. `cLiTwoExt_eq_cLiTwo` needs `‖y‖ < 1` and
   `cLiTwoExt_eq_cLiTwo_of_norm_le_one` needs `y ∈ notCut`; **`1` satisfies
   neither** — it is exactly the excluded point of both. So this is an Abel /
   boundary-limit statement about the series, not a corollary of what exists.
2. Continuity of `x ↦ Re cLiTwoExt(x)` at `1`, to take the limit at all.

Note (2) is plausible precisely because Route 35 G1 measured the `Re` jump
across the cut to be **zero** — but measured is not proved, and `x = 1` is the
branch point rather than an interior point of the cut, so G1 does not cover it.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
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

/-! ## Continuity on the cut, along the real ray

`continuousAt_liTwoKernel` asks for `1 − y·t ∈ slitPlane`, which real `x > 1`
fails for `t > 1/x`. That hypothesis is **sufficient, not necessary**: along the
real ray `1 − x·u` stays on the real axis, so it *leaves* the slit plane but
never *crosses* the cut, and `log(1 − x·u) = log|1 − x·u| + iπ` is continuous
there for every `u ≠ 1/x`.

Same phenomenon as `hasDerivAt_log_neg_ofReal` in the transport lane: smooth
along a real path though the complex derivative does not exist. -/

/-- The `arg` step is **locally constant** away from the sign change. -/
theorem continuousAt_arg_step {x u : ℝ} (hxu : 1 - x * u ≠ 0) :
    ContinuousAt (fun v : ℝ => if 1 - x * v < 0 then Real.pi else 0) u := by
  have hc : ContinuousAt (fun v : ℝ => 1 - x * v) u := by fun_prop
  rcases lt_or_gt_of_ne hxu with h | h
  · have hev : (fun v : ℝ => if 1 - x * v < 0 then Real.pi else 0)
        =ᶠ[nhds u] (fun _ : ℝ => Real.pi) := by
      filter_upwards [hc.eventually (eventually_lt_nhds h)] with v hv
      rw [if_pos hv]
    exact continuousAt_const.congr hev.symm
  · have hev : (fun v : ℝ => if 1 - x * v < 0 then Real.pi else 0)
        =ᶠ[nhds u] (fun _ : ℝ => (0 : ℝ)) := by
      filter_upwards [hc.eventually (eventually_gt_nhds h)] with v hv
      rw [if_neg (not_lt.mpr hv.le)]
    exact continuousAt_const.congr hev.symm

/-- **The kernel is continuous at real `u`, on the cut**, provided only
`u ≠ 0` and `1 − x·u ≠ 0`. No `slitPlane` hypothesis. -/
theorem continuousAt_liTwoKernel_ofReal {x u : ℝ} (hu : u ≠ 0) (hxu : 1 - x * u ≠ 0) :
    ContinuousAt (liTwoKernel ((x : ℝ) : ℂ)) u := by
  have heq : (fun v : ℝ => Complex.log ((1 : ℂ) - ((x : ℝ) : ℂ) * (v : ℂ)))
      = fun v : ℝ => ((Real.log (1 - x * v) : ℝ) : ℂ)
          + ((if 1 - x * v < 0 then Real.pi else 0 : ℝ) : ℂ) * Complex.I := by
    funext v
    have hcast : (1 : ℂ) - ((x : ℝ) : ℂ) * (v : ℂ) = (((1 - x * v : ℝ)) : ℂ) := by
      push_cast; ring
    rw [hcast, log_ofReal_eq, arg_one_sub_mul_ofReal, Real.log_abs]
  have hlog : ContinuousAt
      (fun v : ℝ => Complex.log ((1 : ℂ) - ((x : ℝ) : ℂ) * (v : ℂ))) u := by
    rw [heq]
    refine ContinuousAt.add ?_ ?_
    · refine ContinuousAt.comp (g := fun r : ℝ => ((r : ℝ) : ℂ))
        (f := fun v : ℝ => Real.log (1 - x * v)) Complex.continuous_ofReal.continuousAt ?_
      exact ContinuousAt.comp (g := Real.log) (f := fun v : ℝ => 1 - x * v)
        (Real.continuousAt_log hxu) (by fun_prop)
    · refine ContinuousAt.mul ?_ continuousAt_const
      exact ContinuousAt.comp (g := fun r : ℝ => ((r : ℝ) : ℂ))
        (f := fun v : ℝ => if 1 - x * v < 0 then Real.pi else 0)
        Complex.continuous_ofReal.continuousAt (continuousAt_arg_step hxu)
  exact hlog.div Complex.continuous_ofReal.continuousAt (Complex.ofReal_ne_zero.mpr hu)

/-- **The radial derivative, generalised to real `x > 0` — including on the cut.**

`hasDerivAt_cLiTwoExt_radial` requires `y ∈ notCut`, which real `x > 1` fails.
That hypothesis was doing three jobs: integrability on `[0,t]`, continuity of the
kernel at `t`, and measurability near `t`. All three now hold for real `x`
without it — the first by `intervalIntegrable_clog_one_sub_div_ofReal`, the other
two by `continuousAt_liTwoKernel_ofReal`.

⚠ `hxt : 1 − x·t ≠ 0` is **load-bearing and replaces `notCut`**: at `t = 1/x` the
kernel genuinely diverges. The original excluded that point implicitly via
`slitPlane`; a version admitting it would be false. -/
theorem hasDerivAt_cLiTwoExt_radial_ofReal {x : ℝ} (hx : 0 < x) {t : ℝ}
    (ht0 : 0 < t) (ht1 : t ≤ 1) (hxt : 1 - x * t ≠ 0) :
    HasDerivAt (fun s : ℝ => cLiTwoExt ((s : ℂ) * ((x : ℝ) : ℂ)))
      (-(Complex.log (1 - ((x : ℝ) : ℂ) * (t : ℂ)) / (t : ℂ))) t := by
  have htne : t ≠ 0 := ne_of_gt ht0
  -- integrability: step (1), restricted from `[0,1]` to `[0,t]`
  have hint : IntervalIntegrable (liTwoKernel ((x : ℝ) : ℂ)) MeasureTheory.volume 0 t := by
    have h1 : IntervalIntegrable (liTwoKernel ((x : ℝ) : ℂ)) MeasureTheory.volume 0 1 := by
      have := intervalIntegrable_clog_one_sub_div_ofReal hx
      simpa [liTwoKernel] using this
    exact h1.mono_set (by
      rw [Set.uIcc_of_le ht0.le, Set.uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)]
      exact Set.Icc_subset_Icc le_rfl ht1)
  -- continuity at `t`, with NO slitPlane hypothesis
  have hcont : ContinuousAt (liTwoKernel ((x : ℝ) : ℂ)) t :=
    continuousAt_liTwoKernel_ofReal htne hxt
  -- measurability near `t`: the kernel is continuous on the open set off `0`
  -- and off the single bad point `1/x`
  have hUopen : IsOpen ({u : ℝ | u ≠ 0} ∩ {u : ℝ | 1 - x * u ≠ 0}) := by
    refine isOpen_ne.inter ?_
    exact isOpen_ne.preimage (by fun_prop)
  have htU : t ∈ ({u : ℝ | u ≠ 0} ∩ {u : ℝ | 1 - x * u ≠ 0}) := ⟨htne, hxt⟩
  have hUcont : ContinuousOn (liTwoKernel ((x : ℝ) : ℂ))
      ({u : ℝ | u ≠ 0} ∩ {u : ℝ | 1 - x * u ≠ 0}) :=
    fun u hu => (continuousAt_liTwoKernel_ofReal hu.1 hu.2).continuousWithinAt
  have hmeas : StronglyMeasurableAtFilter (liTwoKernel ((x : ℝ) : ℂ)) (nhds t) :=
    hUcont.stronglyMeasurableAtFilter hUopen t htU
  -- FTC-1, then transport across the substitution
  have hftc : HasDerivAt (fun u : ℝ => ∫ z in (0 : ℝ)..u, liTwoKernel ((x : ℝ) : ℂ) z)
      (liTwoKernel ((x : ℝ) : ℂ) t) t := intervalIntegral.integral_hasDerivAt_right hint hmeas hcont
  have hneg := hftc.neg
  refine hneg.congr_of_eventuallyEq ?_
  filter_upwards [eventually_ne_nhds htne] with s hs
  exact (cLiTwoExt_ofReal_mul (y := ((x : ℝ) : ℂ)) hs)

/-! ## Dropping the right-endpoint cap, and the `x`-derivative that follows

The radial lemma caps `t ≤ 1` only because integrability was established on
`[0,1]`. Generalising the right endpoint removes the cap — and then taking the
**ray direction to be `1`** makes the parameter `s` *be* `x`, so the radial
derivative becomes the `x`-derivative the constancy argument needs. That is what
resolves the "s-derivative vs x-derivative" subtlety recorded in `qou-invr`. -/

/-- Integrability on `0..b` for any `b > 0`, not just `b = 1`. -/
theorem intervalIntegrable_clog_one_sub_div_ofReal' {x b : ℝ} (hx : 0 < x) (hb : 0 < b) :
    IntervalIntegrable (fun t : ℝ => Complex.log ((1 : ℂ) - (x : ℂ) * (t : ℂ)) / (t : ℂ))
      MeasureTheory.volume 0 b := by
  set c : ℝ := min (1 / (2 * x)) (b / 2) with hc
  have h2x : (0 : ℝ) < 2 * x := by linarith
  have hcpos : 0 < c := lt_min (by positivity) (by positivity)
  have hcb : c < b := lt_of_le_of_lt (min_le_right _ _) (by linarith)
  -- near 0: the existing slitPlane lemma, rescaled (as before)
  have hleft : IntervalIntegrable
      (fun t : ℝ => Complex.log ((1 : ℂ) - (x : ℂ) * (t : ℂ)) / (t : ℂ))
      MeasureTheory.volume 0 c := by
    refine (intervalIntegrable_integrand_left hx).mono_set ?_
    rw [Set.uIcc_of_le hcpos.le, Set.uIcc_of_le (by positivity : (0:ℝ) ≤ 1 / (2 * x))]
    exact Set.Icc_subset_Icc le_rfl (by rw [hc]; exact min_le_left _ _)
  -- away from 0: `1/t` is continuous, so it peels off
  have hright : IntervalIntegrable
      (fun t : ℝ => Complex.log ((1 : ℂ) - (x : ℂ) * (t : ℂ)) / (t : ℂ))
      MeasureTheory.volume c b := by
    have hcont : ContinuousOn (fun t : ℝ => ((t : ℂ))⁻¹) (Set.uIcc c b) := by
      refine ContinuousOn.inv₀ (Complex.continuous_ofReal.continuousOn) ?_
      intro t ht
      have ht0 : t ≠ 0 := by
        rcases Set.mem_uIcc.mp ht with h | h
        · exact ne_of_gt (lt_of_lt_of_le hcpos h.1)
        · exact ne_of_gt (lt_of_lt_of_le hcpos (le_trans (le_of_lt hcb) h.1))
      simpa using ht0
    have h := (intervalIntegrable_clog_one_sub_mul x c b).mul_continuousOn hcont
    simpa [div_eq_mul_inv] using h
  exact hleft.trans hright

/-- The radial derivative with the right-endpoint cap removed. -/
theorem hasDerivAt_cLiTwoExt_radial_ofReal' {x : ℝ} (hx : 0 < x) {t : ℝ}
    (ht0 : 0 < t) (hxt : 1 - x * t ≠ 0) :
    HasDerivAt (fun s : ℝ => cLiTwoExt ((s : ℂ) * ((x : ℝ) : ℂ)))
      (-(Complex.log (1 - ((x : ℝ) : ℂ) * (t : ℂ)) / (t : ℂ))) t := by
  have htne : t ≠ 0 := ne_of_gt ht0
  have hint : IntervalIntegrable (liTwoKernel ((x : ℝ) : ℂ)) MeasureTheory.volume 0 t := by
    have := intervalIntegrable_clog_one_sub_div_ofReal' hx ht0
    simpa [liTwoKernel] using this
  have hcont : ContinuousAt (liTwoKernel ((x : ℝ) : ℂ)) t :=
    continuousAt_liTwoKernel_ofReal htne hxt
  have hUopen : IsOpen ({u : ℝ | u ≠ 0} ∩ {u : ℝ | 1 - x * u ≠ 0}) := by
    refine isOpen_ne.inter ?_
    exact isOpen_ne.preimage (by fun_prop)
  have htU : t ∈ ({u : ℝ | u ≠ 0} ∩ {u : ℝ | 1 - x * u ≠ 0}) := ⟨htne, hxt⟩
  have hUcont : ContinuousOn (liTwoKernel ((x : ℝ) : ℂ))
      ({u : ℝ | u ≠ 0} ∩ {u : ℝ | 1 - x * u ≠ 0}) :=
    fun u hu => (continuousAt_liTwoKernel_ofReal hu.1 hu.2).continuousWithinAt
  have hmeas : StronglyMeasurableAtFilter (liTwoKernel ((x : ℝ) : ℂ)) (nhds t) :=
    hUcont.stronglyMeasurableAtFilter hUopen t htU
  have hftc : HasDerivAt (fun u : ℝ => ∫ z in (0 : ℝ)..u, liTwoKernel ((x : ℝ) : ℂ) z)
      (liTwoKernel ((x : ℝ) : ℂ) t) t := intervalIntegral.integral_hasDerivAt_right hint hmeas hcont
  have hneg := hftc.neg
  refine hneg.congr_of_eventuallyEq ?_
  filter_upwards [eventually_ne_nhds htne] with s hs
  exact (cLiTwoExt_ofReal_mul (y := ((x : ℝ) : ℂ)) hs)

/-- **`d/dx cLiTwoExt(x) = −log(1−x)/x` for real `x > 0`, `x ≠ 1` — including on
the cut.** Ray direction `1`, so the radial parameter *is* `x`. -/
theorem hasDerivAt_cLiTwoExt_ofReal {x : ℝ} (hx : 0 < x) (hx1 : x ≠ 1) :
    HasDerivAt (fun s : ℝ => cLiTwoExt ((s : ℝ) : ℂ))
      (-(Complex.log (1 - ((x : ℝ) : ℂ)) / ((x : ℝ) : ℂ))) x := by
  have h := hasDerivAt_cLiTwoExt_radial_ofReal' (x := 1) one_pos (t := x) hx
    (by simpa using sub_ne_zero.mpr (Ne.symm hx1))
  simpa using h

/-! ## Step (2): the inversion combination has vanishing derivative on `(1,∞)` -/

/-- `d/dx Re cLiTwoExt(x) = −log|1−x|/x`, real `x > 0`, `x ≠ 1`. `Real.log` is
even, so this reads `−log(x−1)/x` on `x > 1`. -/
theorem hasDerivAt_re_cLiTwoExt_ofReal {x : ℝ} (hx : 0 < x) (hx1 : x ≠ 1) :
    HasDerivAt (fun s : ℝ => (cLiTwoExt ((s : ℝ) : ℂ)).re)
      (-(Real.log (1 - x) / x)) x := by
  have h := hasDerivAt_cLiTwoExt_ofReal hx hx1
  have hre := Complex.reCLM.hasFDerivAt.comp_hasDerivAt x h
  refine hre.congr_deriv ?_
  have hcast : (1 : ℂ) - ((x : ℝ) : ℂ) = (((1 - x : ℝ)) : ℂ) := by push_cast; ring
  simp only [Complex.reCLM_apply, Complex.neg_re, Complex.div_re, hcast,
    re_log_ofReal, Complex.ofReal_re, Complex.ofReal_im, Complex.normSq_ofReal]
  have hxne : x ≠ 0 := ne_of_gt hx
  field_simp
  ring

/-- **The inversion combination is locally constant on `(1,∞)`.**

    G(x) := Re cLiTwoExt(x) + Re cLiTwoExt(1/x) + ½·log²x

has `G' = 0`. The three derivatives are `−log(x−1)/x`, `(log(x−1) − log x)/x` and
`log x / x`, and they cancel identically. Route 35 G3 measures `G ≡ π²/3`. -/
theorem hasDerivAt_inversionCombo {x : ℝ} (hx : 1 < x) :
    HasDerivAt (fun s : ℝ => (cLiTwoExt ((s : ℝ) : ℂ)).re
        + (cLiTwoExt (((1 / s : ℝ)) : ℂ)).re + Real.log s ^ 2 / 2) 0 x := by
  have hx0 : 0 < x := lt_trans zero_lt_one hx
  have hxne : x ≠ 0 := ne_of_gt hx0
  have hx1 : x ≠ 1 := ne_of_gt hx
  -- first term
  have h1 := hasDerivAt_re_cLiTwoExt_ofReal hx0 hx1
  -- second term, through `s ↦ 1/s`
  have hinv : HasDerivAt (fun s : ℝ => 1 / s) (-(x ^ 2)⁻¹) x := by
    simpa [one_div] using hasDerivAt_inv hxne
  have hinvpos : (0 : ℝ) < 1 / x := by positivity
  have hinvne : (1 / x) ≠ 1 := by
    intro h
    have : x = 1 := by field_simp at h; linarith
    exact hx1 this
  have h2raw := (hasDerivAt_re_cLiTwoExt_ofReal hinvpos hinvne).comp x hinv
  -- third term
  have hlog : HasDerivAt Real.log x⁻¹ x := Real.hasDerivAt_log hxne
  have h3 : HasDerivAt (fun s : ℝ => Real.log s ^ 2 / 2) (Real.log x / x) x := by
    have := (hlog.pow 2).div_const 2
    refine this.congr_deriv ?_
    field_simp
    ring
  -- the three cancel
  have hsum := (h1.add h2raw).add h3
  refine hsum.congr_deriv ?_
  have hx1' : (0 : ℝ) < x - 1 := by linarith
  have hlog1x : Real.log (1 - x) = Real.log (x - 1) := by
    rw [← Real.log_neg_eq_log]
    congr 1
    ring
  have hloginv : Real.log (1 - 1 / x) = Real.log (x - 1) - Real.log x := by
    have : (1 : ℝ) - 1 / x = (x - 1) / x := by field_simp
    rw [this, Real.log_div (ne_of_gt hx1') hxne]
  rw [hlog1x, hloginv]
  field_simp
  ring

/-! ## Pinning the constant: `cLiTwoExt 1 = π²/6` -/

/-- `cLiTwo 1 = π²/6` — the series converges *at* `1`, so this is immediate from
`hasSum_one_div_succ_sq`; no boundary theory is involved. -/
theorem cLiTwo_one : cLiTwo 1 = ((Real.pi ^ 2 / 6 : ℝ) : ℂ) := by
  unfold cLiTwo
  have hr := hasSum_one_div_succ_sq
  have hc := Complex.ofRealCLM.hasSum hr
  refine HasSum.tsum_eq ?_
  refine hc.congr_fun ?_
  intro k
  simp only [Complex.ofRealCLM_apply]
  push_cast
  ring

/-- `cLiTwoExt` along the reals **is** the primitive of the `y = 1` kernel.
Holds at `0` too, where both sides are `0`. -/
theorem cLiTwoExt_ofReal_eq_primitive (x : ℝ) :
    cLiTwoExt ((x : ℝ) : ℂ) = -∫ u in (0 : ℝ)..x, liTwoKernel (1 : ℂ) u := by
  rcases eq_or_ne x 0 with rfl | hx
  · simp
  · simpa using cLiTwoExt_ofReal_mul (y := (1 : ℂ)) hx

/-- **`cLiTwoExt` is continuous along `[0,1]`, up to and including the branch
point.** Because it is a primitive of an integrable function — integrability at
`x = 1` being step (1) with `x = 1`. -/
theorem continuousOn_cLiTwoExt_ofReal_Icc :
    ContinuousOn (fun x : ℝ => cLiTwoExt ((x : ℝ) : ℂ)) (Set.Icc 0 1) := by
  have hint : IntervalIntegrable (liTwoKernel (1 : ℂ)) MeasureTheory.volume 0 1 := by
    have h := intervalIntegrable_clog_one_sub_div_ofReal (x := 1) one_pos
    have hfun : (fun t : ℝ => Complex.log ((1 : ℂ) - ((1 : ℝ) : ℂ) * (t : ℂ)) / (t : ℂ))
        = liTwoKernel (1 : ℂ) := by
      funext t
      simp [liTwoKernel]
    rwa [hfun] at h
  have hprim := intervalIntegral.continuousOn_primitive_interval' hint
    (by simp : (0 : ℝ) ∈ Set.uIcc (0 : ℝ) 1)
  have huIcc : Set.uIcc (0 : ℝ) 1 = Set.Icc 0 1 :=
    Set.uIcc_of_le (by norm_num)
  rw [huIcc] at hprim
  have : (fun x : ℝ => cLiTwoExt ((x : ℝ) : ℂ))
      = fun x : ℝ => -∫ u in (0 : ℝ)..x, liTwoKernel (1 : ℂ) u := by
    funext x; exact cLiTwoExt_ofReal_eq_primitive x
  rw [this]
  exact hprim.neg

/-- **`cLiTwoExt 1 = π²/6`.** Both `cLiTwoExt` and `cLiTwo` are continuous along
`[0,1]` and agree on `[0,1)`; the value at the branch point follows.

⚠ Neither `cLiTwoExt_eq_cLiTwo` (needs `‖y‖ < 1`) nor
`cLiTwoExt_eq_cLiTwo_of_norm_le_one` (needs `y ∈ notCut`) reaches `1` — it is
exactly the excluded point of both. The continuity above is what closes the gap,
and it exists only because step (1) supplied integrability at `x = 1`. -/
theorem cLiTwoExt_one : cLiTwoExt 1 = ((Real.pi ^ 2 / 6 : ℝ) : ℂ) := by
  have hne : (nhdsWithin (1 : ℝ) (Set.Ico 0 1)).NeBot := by
    rw [← mem_closure_iff_nhdsWithin_neBot]
    rw [closure_Ico (by norm_num : (0:ℝ) ≠ 1)]
    exact ⟨by norm_num, le_rfl⟩
  have hsub : Set.Ico (0:ℝ) 1 ⊆ Set.Icc 0 1 := Set.Ico_subset_Icc_self
  -- `cLiTwoExt` along the reals, restricted
  have h1 : ContinuousWithinAt (fun x : ℝ => cLiTwoExt ((x : ℝ) : ℂ)) (Set.Ico 0 1) 1 :=
    (continuousOn_cLiTwoExt_ofReal_Icc 1 ⟨by norm_num, le_rfl⟩).mono hsub
  -- `cLiTwo` along the reals, from continuity on the CLOSED ball
  have hmaps : Set.Icc (0:ℝ) 1 ⊆ (fun x : ℝ => ((x : ℝ) : ℂ)) ⁻¹' Metric.closedBall (0 : ℂ) 1 := by
    intro x hx
    simp only [Set.mem_preimage, Metric.mem_closedBall, dist_zero_right]
    rw [Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hx.1]
    exact hx.2
  have h2on : ContinuousOn (fun x : ℝ => cLiTwo ((x : ℝ) : ℂ)) (Set.Icc 0 1) :=
    ContinuousOn.comp continuousOn_cLiTwo_closedBall
      Complex.continuous_ofReal.continuousOn hmaps
  have h2 : ContinuousWithinAt (fun x : ℝ => cLiTwo ((x : ℝ) : ℂ)) (Set.Ico 0 1) 1 :=
    (h2on 1 ⟨by norm_num, le_rfl⟩).mono hsub
  -- they agree on `[0,1)`, where the series converges
  have heqf : (fun x : ℝ => cLiTwo ((x : ℝ) : ℂ))
      =ᶠ[nhdsWithin (1:ℝ) (Set.Ico 0 1)] (fun x : ℝ => cLiTwoExt ((x : ℝ) : ℂ)) := by
    refine eventually_mem_nhdsWithin.mono fun x hx => ?_
    have hnorm : ‖((x : ℝ) : ℂ)‖ < 1 := by
      rw [Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hx.1]
      exact hx.2
    exact (cLiTwoExt_eq_cLiTwo hnorm).symm
  have hb := tendsto_nhds_unique h1 (h2.congr' heqf)
  simp only [Complex.ofReal_one] at hb
  rw [hb, cLiTwo_one]

/-! ## Step (2), closed: the inversion identity on `[1,∞)` -/

/-- Continuity of `cLiTwoExt` along `[0,b]` for **any** `b > 0` — the primitive
argument again, now that integrability holds on `0..b`. -/
theorem continuousOn_cLiTwoExt_ofReal_Icc' {b : ℝ} (hb : 0 < b) :
    ContinuousOn (fun x : ℝ => cLiTwoExt ((x : ℝ) : ℂ)) (Set.Icc 0 b) := by
  have hint : IntervalIntegrable (liTwoKernel (1 : ℂ)) MeasureTheory.volume 0 b := by
    have h := intervalIntegrable_clog_one_sub_div_ofReal' (x := 1) one_pos hb
    have hfun : (fun t : ℝ => Complex.log ((1 : ℂ) - ((1 : ℝ) : ℂ) * (t : ℂ)) / (t : ℂ))
        = liTwoKernel (1 : ℂ) := by
      funext t; simp [liTwoKernel]
    rwa [hfun] at h
  have hprim := intervalIntegral.continuousOn_primitive_interval' hint
    (by simp : (0 : ℝ) ∈ Set.uIcc (0 : ℝ) b)
  rw [Set.uIcc_of_le hb.le] at hprim
  have hEq : (fun x : ℝ => cLiTwoExt ((x : ℝ) : ℂ))
      = fun x : ℝ => -∫ u in (0 : ℝ)..x, liTwoKernel (1 : ℂ) u := by
    funext x; exact cLiTwoExt_ofReal_eq_primitive x
  rw [hEq]
  exact hprim.neg

/-- `Re cLiTwoExt(1) = π²/6`. -/
theorem re_cLiTwoExt_one : (cLiTwoExt 1).re = Real.pi ^ 2 / 6 := by
  rw [cLiTwoExt_one, Complex.ofReal_re]

/-- **The inversion identity, `x ≥ 1`.**

    Re cLiTwoExt(x) + Re cLiTwoExt(1/x) + ½·log²x = π²/3

`G' = 0` on `(1,∞)` (`hasDerivAt_inversionCombo`), `G` is continuous up to and
including the branch point, and `G(1) = 2·Re cLiTwoExt(1) = π²/3`
(`re_cLiTwoExt_one`). The exceptional point `x = 1`, where the derivative does
not exist, costs nothing — `constant_of_hasDerivWithinAt_zero_off_point` is
built for exactly that. -/
theorem re_inversion_identity {x : ℝ} (hx : 1 ≤ x) :
    (cLiTwoExt ((x : ℝ) : ℂ)).re + (cLiTwoExt (((1 / x : ℝ)) : ℂ)).re
      + Real.log x ^ 2 / 2 = Real.pi ^ 2 / 3 := by
  set G : ℝ → ℝ := fun s : ℝ => (cLiTwoExt ((s : ℝ) : ℂ)).re
      + (cLiTwoExt (((1 / s : ℝ)) : ℂ)).re + Real.log s ^ 2 / 2 with hG
  have hb : (0 : ℝ) < x + 1 := by linarith
  -- continuity of `G` on `[1, x+1]`
  have hcont : ContinuousOn G (Set.Icc 1 (x + 1)) := by
    have hsub : Set.Icc (1 : ℝ) (x + 1) ⊆ Set.Icc 0 (x + 1) :=
      Set.Icc_subset_Icc (by norm_num) le_rfl
    refine ContinuousOn.add (ContinuousOn.add ?_ ?_) ?_
    · exact Complex.continuous_re.comp_continuousOn
        ((continuousOn_cLiTwoExt_ofReal_Icc' hb).mono hsub)
    · refine Complex.continuous_re.comp_continuousOn ?_
      -- pin `g` and `f`: `cLiTwoExt` unfolds to `-∫ …`, so bare `.comp` lets
      -- higher-order unification pick `Neg.neg` as the outer function
      refine ContinuousOn.comp (g := fun u : ℝ => cLiTwoExt ((u : ℝ) : ℂ))
        (f := fun s : ℝ => 1 / s) (continuousOn_cLiTwoExt_ofReal_Icc' hb) ?_ ?_
      · exact ContinuousOn.div continuousOn_const continuousOn_id
          (fun s hs => by intro h; rw [h] at hs; exact absurd hs.1 (by norm_num))
      · intro s hs
        have hs1 : (1 : ℝ) ≤ s := hs.1
        have hspos : (0 : ℝ) < s := lt_of_lt_of_le zero_lt_one hs1
        refine ⟨by positivity, ?_⟩
        have : 1 / s ≤ 1 := by rw [div_le_one hspos]; exact hs1
        linarith
    · refine ContinuousOn.div_const (ContinuousOn.pow ?_ 2) 2
      exact Real.continuousOn_log.mono (fun s hs => by
        have : (0:ℝ) < s := lt_of_lt_of_le zero_lt_one hs.1
        simpa using ne_of_gt this)
  -- derivative zero off the single point `1`
  have hderiv : ∀ s ∈ Set.Ico (1 : ℝ) (x + 1), s ≠ 1 →
      HasDerivWithinAt G 0 (Set.Ici s) s := by
    intro s hs hs1
    have hs' : 1 < s := lt_of_le_of_ne hs.1 (Ne.symm hs1)
    exact (hasDerivAt_inversionCombo hs').hasDerivWithinAt
  have hconst := QOU.Archimedean.constant_of_hasDerivWithinAt_zero_off_point
    (c := 1) hcont hderiv x ⟨hx, by linarith⟩
  have hG1 : G 1 = Real.pi ^ 2 / 3 := by
    simp only [hG, one_div_one, Complex.ofReal_one, re_cLiTwoExt_one, Real.log_one]
    ring
  exact hconst.trans hG1

/-! ## The Li₂ integrand, approached from below — Route 36 G11

`hcont` in the transport wants `cLiTwoExt` continuous at a point of the cut
`[1,∞)`, reached along a path with `Im < 0`. That splits into a pointwise part
and a dominated-convergence part; this section closes the pointwise one, and it
turns out to cost nothing.

The reason is a Mathlib theorem that is exactly the right shape:
`Complex.continuousWithinAt_log_of_re_neg_of_im_zero` gives `log` continuous at a
**negative real** when restricted to the **upper** half plane `{0 ≤ z.im}`. And
`w ↦ 1 − w·t` carries `{Im w ≤ 0}` into `{0 ≤ Im z}` for `t > 0`, because
`Im(1 − w·t) = −t·Im w`. So approaching the cut *from below in `w`* is
approaching `log`'s cut *from above in `1 − w·t`* — the two conventions agree,
and Lean's principal branch already sits on that side (`arg_one_sub_mul_ofReal`).

⚠ The value of this section is mostly negative information: it says the branch
analysis is **not** where the remaining difficulty is. What is left of G11 is a
dominated-convergence argument on `∫₀¹ log(1−wt)/t dt`, not anything about which
side of the cut Lean picks. -/

/-- **`w ↦ log(1 − w·t)` is continuous at a cut crossing, restricted to
`Im w ≤ 0`.** -/
theorem continuousWithinAt_clog_one_sub_mul {w₀ : ℂ} {t : ℝ} (ht : 0 < t)
    (hre : ((1 : ℂ) - w₀ * (t : ℂ)).re < 0) (him : ((1 : ℂ) - w₀ * (t : ℂ)).im = 0) :
    ContinuousWithinAt (fun w : ℂ => Complex.log (1 - w * (t : ℂ)))
      {w : ℂ | w.im ≤ 0} w₀ := by
  have hmaps : Set.MapsTo (fun w : ℂ => (1 : ℂ) - w * (t : ℂ))
      {w : ℂ | w.im ≤ 0} {z : ℂ | 0 ≤ z.im} := by
    intro w hw
    simp only [Set.mem_setOf_eq] at hw ⊢
    have hz : ((1 : ℂ) - w * (t : ℂ)).im = -(w.im * t) := by
      simp [Complex.sub_im, Complex.mul_im]
    rw [hz]
    nlinarith
  have hf : ContinuousWithinAt (fun w : ℂ => (1 : ℂ) - w * (t : ℂ))
      {w : ℂ | w.im ≤ 0} w₀ :=
    (continuous_const.sub (continuous_id.mul continuous_const)).continuousWithinAt
  -- pin `g` and `f`: bare `.comp` lets unification pick `HSub.hSub 1` as the outer map
  exact ContinuousWithinAt.comp (g := Complex.log)
    (f := fun w : ℂ => (1 : ℂ) - w * (t : ℂ))
    (Complex.continuousWithinAt_log_of_re_neg_of_im_zero hre him) hf hmaps

end QOU.MathlibExt
