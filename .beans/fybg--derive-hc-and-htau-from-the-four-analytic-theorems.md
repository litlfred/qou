---
# qou-fybg
title: 'Derive `hc` and `hτ` in OneLoopPrefactorInvariance from the four analytic theorems (the successor to qou-mlgp)'
status: todo
type: task
priority: normal
tags:
    - lean
    - c-sigma
    - one-loop
    - saddle-point
    - kashaev-invariant
    - formalization-gap
created_at: 2026-08-09T00:00:00Z
updated_at: 2026-08-09T07:00:00Z
---

## Why this bean exists

`qou-mlgp` closed all four analytic gaps behind `c_sigma(4_1) = 3^{-1/4}`:

    (A) Euler-Maclaurin for s_k WITH the constant   kashaev_log_sum_asymptotic
    (B) Laplace's method for a sum                  hasSum_gaussian_theta{,_tilt}
    (C) Lobachevsky function and derivatives        (was already in-repo)
    (D) multivariate Gaussian, complex covariance   integral_vdv_step4

all sorry-free on `[propext, Classical.choice, Quot.sound]`. What it did NOT do
is connect them. `QOU.OneLoopPrefactorInvariance` still takes the saddle as
hypotheses:

    hc : c ^ 2 * |cos theta / sin theta| = (2 * sin theta) ^ 2
    htau : ...

and proves the algebra downstream. Nobody has derived `hc`/`htau` from (A)-(D).

**This is a different KIND of task from `qou-mlgp`, which is why it is a
separate bean.** `qou-mlgp` was a search for missing analysis -- Mathlib had no
Euler-Maclaurin, no Lobachevsky, no Clausen, and the constant in (A) was an open
question in this corpus. This one is assembly of formalised pieces. Do not
reopen `qou-mlgp` for it.

## What the step actually is

    log g_k = -(2N/pi) Lambda(theta) + log(2N sin theta) + (pi/6N) cot theta
              + O(1/N^2)                                    (A), doubled via
                                                            kashaev_factor_eq_sin_sq

  1. maximise the leading term in `theta`: `d/dtheta [-(2N/pi)Lambda] = 0` is
     `log(2 sin theta) = 0`, i.e. `2 sin theta* = 1`. `Lambda' = -log(2 sin)` is
     in-repo (`hasDerivAt_Lob`); `saddle_forces_cot` already turns that plus
     `theta in (pi/2, pi)` into `cot theta* = -sqrt 3`.
  2. expand to second order around `theta*`: the Hessian is
     `-(2N/pi) Lambda''(theta*) = (2N/pi) cot theta*`.
  3. sum the Gaussian: this is exactly the shape `hasSum_gaussian_theta_tilt`
     handles, with `a = pi |cot theta*| / N` -- an EXACT theta identity, so the
     sum/integral ratio is `1 + O(e^{-pi^2/a})` and no separate Laplace error
     analysis is needed.
  4. read off `c_sigma = 2 sin theta* |cot theta*|^{-1/2}` and
     `|tau_DG| = |cot theta*|/2`, which is `hc` and `htau`.

Step 2 is the only one with real work left: it needs the remainder of the
`theta`-expansion controlled uniformly in `k`, not just pointwise, and (A)'s
bound `1/(144k^2) + (7/12)h^2 + h^2/(12 sin^2 theta)` degrades near
`theta -> 0, pi`. The saddle sits at `theta* = 5pi/6`, comfortably interior, so
restricting the sum to `|theta - theta*| < delta` and bounding the tail
separately is the expected shape.

## Definition of done

`c_pow_four_eq_third` (or a named successor) holding with `hc` DISCHARGED
rather than assumed, or a recorded decision that the link stays informal with
the reason. Whichever it is, `OneLoopPrefactorInvariance.lean`'s header and
`content/.../mass-theory/one-loop-prefactor-provenance.md` must keep saying
exactly what is assumed -- they were both wrong in the understating direction
on 2026-08-09 and were corrected then; do not let them drift the other way.

## Do not overclaim

"The analytic gaps are closed" is true. "`c_sigma(4_1) = 3^{-1/4}` is
formalised end to end" is NOT, and will not be until this bean is done.

## Landed: the saddle LOCATION, exactly and discretely. 2026-08-09

`QOU/Knot/KashaevArgmax.lean::kashaevProd_le_argmax`, sorry-free on
`[propext, Classical.choice, Quot.sound]`:

    for 6 <= N and every k < N:   kashaevProd N k <= kashaevProd N (5*N/6)

The largest term of `<4_1>_N = sum_k kashaevProd N k` sits at
`k* = floor(5N/6)`, i.e. `theta* = k* pi/N` within `pi/N` of `5pi/6`.

**Step 1 of this bean's plan needs no analysis at all.** The plan above said
"maximise the leading term in theta: d/dtheta[-(2N/pi)Lambda] = 0 is
log(2 sin theta) = 0" -- differentiating an asymptotic expansion, so needing
the expansion, its remainder, and uniformity in k. None of that is required.
The ratio of successive terms is EXACT:

    kashaevProd N (k+1) / kashaevProd N k = (2 sin((k+1) pi/N))^2

(`kashaevProd_succ`, one line from `Finset.prod_Icc_succ_top` +
`kashaev_factor_eq_sin_sq`). So the sequence rises precisely while `2 sin > 1`
and falls precisely while `2 sin < 1`. `2 sin theta = 1` is not an asymptotic
stationarity condition here -- it is the exact crossover of a ratio, and
`saddle_forces_cot` already turns it plus `theta in (pi/2, pi)` into
`cot theta* = -sqrt3`.

### Two things the shape forces, both easy to get wrong

**It is DOWN-UP-DOWN, not unimodal.** `2 sin(j pi/N) < 1` also holds near
`j = 0`, so the sequence FALLS on `[0, floor(N/6)]` before it rises. Calling it
unimodal would be false. That region is handled separately: there
`kashaevProd N k <= kashaevProd N 0 = 1`, and `1 <= kashaevProd N k*` because
the sequence falls from `k*` to `N-1` where `kashaevProd N (N-1) = N^2`
exactly (`kashaevProd_endpoint`, already in the corpus). The endpoint theorem
earns its keep here.

**The ties are real, so `<=` is sharp.** When `6 | N` the increment at
`j = N/6` and at `j = 5N/6` is exactly `1`, so `kashaevProd N k* =
kashaevProd N (k*-1)` and a strict `<` would be FALSE. Checked at N = 12, 30,
60 in `computations/probes/kashaev_argmax_probe.py`.

### A probe artifact worth recording, because it looked like a counterexample

The probe first reported "argmax mismatch at N=6: floor(5N/6)=5, argmaxes=[4]".
It is not a counterexample. `sin(5 pi/6)` is exactly `1/2`, but mpmath computes
it from a truncated `pi`, so an increment that is exactly `0` in closed form
lands at `+-1e-40` -- here negative, making `vals[5]` lose to `vals[4]` by
1e-40. Every comparison in the probe now carries a tolerance far above that
noise and far below any real gap. The lesson generalises: an exact tie in a
trig identity is exactly where a high-precision float probe will manufacture a
fake strict inequality, and the sign it picks is arbitrary.

### What is left of this bean

Steps 2-4 of the plan, unchanged: the second-order expansion around `theta*`
(the Hessian `(2N/pi)|cot theta*|`), the Gaussian sum via
`hasSum_gaussian_theta_tilt`, and reading off `hc`/`htau`. Step 1 is done and
was cheaper than the plan assumed. Step 2 remains the one with real work: the
remainder of the `theta`-expansion has to be controlled uniformly in `k`, and
(A)'s bound `1/(144k^2) + (7/12)h^2 + h^2/(12 sin^2 theta)` degrades near
`theta -> 0, pi`. The argmax theorem helps: it confines the terms that matter
to a neighbourhood of `k*`, where that bound is uniformly good.

## Landed: step 2, the HESSIAN. 2026-08-09

`QOU/Knot/LobTaylorSaddle.lean::abs_Lob_taylor_saddle`, sorry-free:

    | Lambda(theta) - ( Lambda(th*) + (sqrt3/2)(theta - th*)^2 ) |
        <= M |theta - th*|^3 / 6,      th* = 5 pi / 6

for any `M` bounding `1/sin^2` between the two points.

**The linear term is absent, not dropped.** `Lambda'(th*) = -log(2 sin th*) =
-log 1 = 0` exactly -- the saddle condition again, and the same one
`KashaevArgmax` locates discretely. The quadratic coefficient is
`Lambda''(th*)/2 = -cot(th*)/2 = sqrt3/2`, so the Hessian of the Kashaev
exponent `-(2N/pi)Lambda` at the saddle is `-(2N/pi)sqrt3` -- the `|cot th*|`
that `c_sigma = 2 sin th* |cot th*|^{-1/2}` and `|tau_DG| = |cot th*|/2` are
built from. `cot_five_pi_div_six : cos(5pi/6)/sin(5pi/6) = -sqrt3` is now a
named lemma, matching `saddle_forces_cot`'s conclusion from the other side.

### New Mathlib-gap infrastructure: `QOU/MathlibExt/TaylorRemainder.lean`

Mathlib's `taylor_mean_remainder_lagrange` is stated through `ContDiffOn` and
`iteratedDerivWithin`. Every function in this corpus arrives instead as an
explicit chain of `HasDerivAt`s (`hasDerivAt_Lob`, `hasDerivAt_log_two_sin`,
`hasDerivAt_cos_div_sin`), and restating those as a `ContDiffOn` is more work
than the theorem. So:

    taylor_two_integral_remainder
        f b = f a + f1 a (b-a) + f2 a (b-a)^2/2 + int_a^b f3 t (b-t)^2/2 dt
    abs_taylor_two_le
        |f b - (quadratic model at a)| <= M |b-a|^3 / 6
    integral_sq_weight
        int_a^b (b-t)^2/2 dt = (b-a)^3/6

ONE application of the FTC, against `F t = f t + f1 t (b-t) + f2 t (b-t)^2/2`,
whose derivative is `f3 t (b-t)^2/2` because the two `f1` terms and the two
`f2` terms cancel in pairs. Same trick as `TrapezoidRule.lean`'s
`F := w f' - w' f`, and it works for the same reason: choose the primitive so
the telescoping is visible and a three-step induction becomes a single FTC.
`b` may be on either side of `a`; both orders are proved.

### The constant 1/6 is sharp, and the probe shows it

`computations/probes/lob_taylor_saddle_probe.py`: the bound holds at every
offset tested, and `residual/|d|^3` converges to `0.6712 -> 2/3`, which is
exactly `|Lambda'''(th*)|/6 = (1/sin^2 th*)/6 = 4/6`. The bound/residual ratio
falls to 1.04x as `d` shrinks. So `1/6` is the true constant, not a slack
estimate -- worth stating because the `O(1/N^2)` bound in (A) is loose by
50x-20000x and it would be easy to assume every constant here is.

### Lean gotcha recorded

`have h : |b - a| = a - b := abs_of_nonpos (by linarith)` FAILS. `abs_of_nonpos`
produces `-(b-a)`, which is not defeq to `a-b`, so unification never determines
the implicit argument and the `by linarith` side goal is left with a
metavariable -- the error surfaces as "linarith failed" on a goal it could
prove in one step, with no goal shown. Write
`by rw [abs_of_nonpos (by linarith : b - a <= 0)]; ring`.

Also: rewrite `cot_five_pi_div_six` BEFORE `sin_five_pi_div_six`. Rewriting the
sine first turns `cos th*/sin th*` into `cos th*/(1/2)` and the cot lemma no
longer matches.

### What is left

Step 3 (the Gaussian sum, via `hasSum_gaussian_theta_tilt`) and step 4 (reading
off `hc`/`htau`). Steps 1 and 2 are done. The join is the remaining work: (A)'s
sum-to-integral bound and this expansion have independent error terms, and
combining them needs the `theta`-remainder controlled uniformly over the `k`
that matter. `KashaevArgmax` confines those to a neighbourhood of `k*`, where
both bounds are uniformly good -- that is the shape of step 3's setup.

## Landed: the RIGHT tail is Gaussian. 2026-08-09

`QOU/Knot/KashaevTailBound.lean::kashaevProd_right_tail`, sorry-free:

    kashaevProd N (k*+d) <= kashaevProd N k* * exp(-sqrt3 pi d(d-1)/N)

with `k* = floor(5N/6)`. This is `e^{-c d^2/N}` -- the Gaussian of width
`sqrt(N)` that `hasSum_gaussian_theta` is waiting for.

All of it comes from ONE fact: `f(theta) = log(2 sin theta)` is CONCAVE on
`(0, pi)` (`f'' = -csc^2 < 0`) and vanishes at `theta*` with
`f'(theta*) = cot theta* = -sqrt3`. Concavity puts `f` below its tangent there:

    log(2 sin theta) <= -sqrt3 (theta - 5pi/6)      for all theta in (0, pi)

`log_two_sin_le_tangent`, proved by the derivative-sign argument (`u' =
cot + sqrt3` changes sign exactly at `theta*`, so `u` peaks there at 0) on top
of a new `cot_antitoneOn`.

### Why the naive bound is not enough -- and the probe measures the gap

Each ratio `(2 sin theta_{k*+i})^2` is `< 1` and they decrease, so the obvious
bound is `prod <= (first factor)^d`. That is `e^{-c d/N}`, exponential in
`d/N`, and it does NOT confine the sum to a `sqrt(N)` window. The `d^2` comes
from the factors continuing to shrink -- i.e. from the LINEAR bound on `f`, not
from the first factor alone. At `N=480, d=60`:

    true ratio            5.5e-28
    quadratic bound       3.7e-18       <- proved here
    first-factor^d        2.5e-1        <- the naive bound

Seventeen orders. And the window scales right: the bound crosses `1e-6` at
`d/sqrt(N) = 1.68, 1.68, 1.61, 1.61` for `N = 60, 240, 960, 3840`.

### ONLY the right tail. Read the file header before citing it.

On the left the terms are RISING towards the saddle, so what is needed is a
LOWER bound on `f` -- and the tangent gives an upper one. Concavity is the
wrong way round there. The left tail needs a secant/chord bound instead
(`f(theta) >= (theta* - theta)/sqrt3` on `[2pi/3, theta*]`, from
`cot <= cot(2pi/3) = -1/sqrt3`). NOT DONE. `kashaevProd_right_tail` does not
confine the sum on both sides, and the file says so in as many words.

### Lean gotcha: `linarith` after a division-heavy multiplication

`linarith [mul_le_mul_of_nonneg_left hfrac hpos]` FAILED on a goal that is
literally `hfrac` scaled by `2 sqrt3`, where both sides carry `pi / N`. Its own
preprocessing did not bring the two into a common normal form. `ring_nf at h2
ok` first, THEN `linarith`, works. Two prior attempts (`nlinarith` with a
`mul_nonneg` hint; splitting `(X+1-n)*pi/N` into `(X+1)*pi/N - n*pi/N`) both
failed -- the split was necessary but not sufficient.

### What is left

The left tail (above), then the Gaussian sum itself via
`hasSum_gaussian_theta_tilt`, then `hc`/`htau`. Steps 1 and 2 are done, step 3
is half done.

## Landed: the LEFT tail too. Step 3's tail half is complete. 2026-08-09

`QOU/Knot/KashaevTailBound.lean::kashaevProd_left_tail`, sorry-free:

    for 6b <= 5N, d <= b, and 2N <= 3(b-d):
      kashaevProd N (b-d) <= kashaevProd N b * exp(-pi d(d-1)/(sqrt3 N))

Same Gaussian, run backwards. Two things differ from the right tail and both
are forced:

  * the constant is `1/sqrt3`, not `sqrt3`, because a SECANT is shallower than
    the tangent;
  * there is a WINDOW, `theta >= 2pi/3`, because a secant is only valid across
    the interval it was drawn over.

`le_log_two_sin_secant : (5pi/6 - theta)/sqrt3 <= log(2 sin theta)` on
`[2pi/3, 5pi/6]`, from `cot <= cot(2pi/3) = -1/sqrt3` there (`cot_antitoneOn`
again) integrated back from `theta*`, where `f` vanishes.

**Why a secant and not the tangent.** On the left the terms are RISING toward
the saddle, so the bound needed is a LOWER bound on `f = log(2 sin)` -- and
concavity supplies upper bounds. Concavity is the wrong way round there. This
is the one place in the tail argument where the two sides are genuinely not
symmetric, and getting it wrong would have produced a plausible-looking proof
of nothing.

The window is not tight, and the probe says so: the secant survives to
`theta = 1.5` (below `2pi/3 = 2.094`) and fails by `theta = 1.0`. `2pi/3` is a
convenient endpoint with a closed-form cotangent, not a boundary of validity.

### Header discipline, again

The file previously said "ONLY THE RIGHT TAIL IS PROVED HERE ... this file does
not contain it". That was true when written and is now false. Corrected in the
same commit that made it false. The pattern is worth naming: a header that
honestly records a gap becomes a lie the moment the gap closes, so closing a
gap means editing the place that named it.

### What is left of this bean

Step 3's remaining half: the Gaussian SUM itself, via
`hasSum_gaussian_theta_tilt` -- the tails now confine it to a `sqrt(N)` window
around `k*`, where (A)'s `O(1/N^2)` bound and `abs_Lob_taylor_saddle`'s cubic
remainder are both uniformly good. Then step 4, reading off `hc`/`htau`.

## Landed: the sqrt(N). The N^{3/2} power's exponent, machine-checked. 2026-08-09

`QOU/Knot/KashaevTailBound.lean::sum_kashaevProd_right_le`, sorry-free:

    sum_{k = k*}^{N-1} kashaevProd N k
        <= kashaevProd N k* * (2 + sqrt(N / sqrt3) / 2)

The corpus already had `log_kashaev_le_log_add`: `<4_1>_N <= N * g_{k*}`. That
is enough for the exponential growth RATE and nothing finer. This replaces the
`N` by `2 + (1/2) sqrt(N/sqrt3)` on the upper half -- and `sqrt(N/sqrt3)` is
EXACTLY the Laplace factor `one_loop_c_sigma_tetrahedral_probe.py` measures.
The `1/2` in `N^{3/2}` is this lemma's `1/sqrt(a)` at `a = sqrt3 pi/N`.

### New Mathlib-gap infra: `QOU/MathlibExt/GaussianSumBound.lean`

    sum_exp_neg_mul_sq_le        sum_{d<m} exp(-a d^2) <= 1 + sqrt(pi/a)/2
    sum_exp_neg_mul_mul_pred_le  sum_{d<m} exp(-a d(d-1)) <= 2 + sqrt(pi/a)/2
    integral_exp_neg_mul_sq_le   int_0^M exp(-a x^2) <= sqrt(pi/a)/2
    antitoneOn_exp_neg_mul_sq

uniform in `m`. Mathlib has BOTH halves and not the combination:
`AntitoneOn.sum_le_integral` compares a decreasing sum to its integral, and
`integral_gaussian_Ioi b : int_{(0,inf)} exp(-b x^2) = sqrt(pi/b)/2` evaluates
it. Joining them needs the `d = 0` term peeled off by hand -- no integral
comparison can see it. That peel is the whole content of the `1` in the bound.

The `d(d-1)` form costs one EXTRA unit (`2`, not `1`) because `d(d-1) >= (d-1)^2`
fails at `d = 0`. That form is not an artifact: a per-step tail bound with a
linear penalty accumulates `1 + 2 + ... + (d-1) = d(d-1)/2`, so `d(d-1)` is what
the tails actually hand you, and pretending it is `d^2` would be wrong at the
first two terms.

### Scope, stated plainly

UPPER HALF ONLY -- `k` from `k*` to `N-1`. The lower half needs a region
decomposition the right half does not: `kashaevProd_left_tail` carries a window
(`theta >= 2pi/3`), and below it the terms have to be handled separately
(`g_k <= 1` for `k <= N/6`, against `g_{k*} >= N^2` from `kashaevProd_endpoint`;
and the rising stretch in between). Not done. This does NOT yet bound
`<4_1>_N`.

### What is left

  * the lower half-sum, with the region decomposition above;
  * a matching LOWER bound on the sum (only the largest term, `g_{k*}`, is
    available so far) -- Laplace needs both sides to pin `c_sigma`;
  * then `hc`, which is `c^2 sqrt3 = 1`, and step 4.

## Landed: the left window too. Both sides of the peak are O(sqrt N). 2026-08-09

`sum_kashaevProd_left_window_le`, sorry-free:

    for m <= k* with 2N <= 3(k* - m):
      sum_{d<m} kashaevProd N (k*-d)
          <= kashaevProd N k* * (2 + sqrt(sqrt3 * N)/2)

Note the constant: `sqrt(sqrt3 N)` here versus `sqrt(N/sqrt3)` on the right.
They differ by a factor `sqrt3` because the secant's slope is `1/sqrt3` where
the tangent's is `sqrt3` -- the left window is WIDER in `k` for the same decay,
which is exactly what a shallower bound should give.

**Indexed by DISTANCE, not by index.** The statement sums over `d` with terms
`kashaevProd N (k*-d)`, which is how `kashaevProd_left_tail` is indexed, so the
Gaussian sum bound applies with no reindexing at all. Stating it over
`Ico (k*-m+1) (k*+1)` instead would have forced a `Finset.sum_range_reflect`
dance for no gain. Worth remembering: match the summation variable to the
lemma you are going to apply, not to the interval you are thinking about.

### What is still missing from the bound on `<4_1>_N`

Two things, and neither is the `sqrt(N)`:

  1. the FAR-LEFT region `3k < 2N` -- outside the secant window. Sketch (not
     done): `g_k <= 1` for `k <= N/6` against `g_{k*} >= N^2` from
     `kashaevProd_endpoint` handles the bottom; the rising stretch in between
     needs `g_k <= g_w` where `w = ceil(2N/3)`, and `g_w <= g_{k*} e^{-c N}`
     from the left tail at `D = k*-w ~ N/6`. To avoid a transcendental
     threshold use `e^{-x} <= 1/x` (from `Real.add_one_le_exp`), giving a bound
     with no exponential in it. This region contributes `O(1) * g_{k*}`, not
     `O(sqrt N)`, so it does not change the rate -- but it is not proved.
  2. a matching LOWER bound on the sum. Only the single largest term is
     available (`log_sup_le_log_kashaev`). Laplace needs both sides to pin
     `c_sigma`; an upper bound alone gives an inequality, not a value.

So: `<4_1>_N <= C sqrt(N) g_{k*}` is NOT yet a theorem. Both windows are, and
they are the part that carries the `sqrt(N)`.
