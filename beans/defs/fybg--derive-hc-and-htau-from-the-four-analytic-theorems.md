---
# fybg
title: Derive `hc` and `hτ` in OneLoopPrefactorInvariance from the four analytic theorems (the successor to qou-mlgp)
status: in-progress
type: task
priority: normal
tags:
    - c-sigma
    - one-loop
    - saddle-point
    - kashaev-invariant
    - formalization-gap
    - reorg-2026-10-04
    - lean
created_at: 2026-08-09T00:00:00Z
updated_at: 2026-10-04T15:26:45Z
parent: qou-n4nr
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

## Landed: the region BELOW the secant window. 2026-08-09

`kashaevProd_le_max_of_le`, `sum_kashaevProd_below_window_le`,
`sq_le_kashaevProd_argmax` -- all sorry-free.

    kashaevProd N k <= max 1 (kashaevProd N w)          for k <= w <= 5N/6
    sum_{k<w} kashaevProd N k <= w * max 1 (kashaevProd N w)
    N^2 <= kashaevProd N (5N/6)

**No analysis at all in this part.** Below `theta = 2pi/3` the secant is invalid,
but nothing analytic is needed there: the DOWN-UP-DOWN shape from
`KashaevArgmax` says every term is dominated by one of the two ENDS of that
stretch -- `kashaevProd N 0 = 1` on the falling part, `kashaevProd N w` on the
rising part -- and `max` of the two covers both cases in one statement. Pure
monotonicity runs.

`sq_le_kashaevProd_argmax` sharpens `one_le_kashaevProd_argmax` from `1` to
`N^2`, which is the same proof (fall from `k*` to `N-1`, where
`kashaevProd_endpoint` gives exactly `N^2`) read one line earlier. It is what
makes the `k <= N/6` terms, each `<= 1`, negligible against the peak.

### THE REGION DECOMPOSITION IS NOW COMPLETE; the bound is not

Four regions of `range N`, all with sorry-free bounds:

    k < w                sum_kashaevProd_below_window_le   w * max 1 g_w
    w <= k <= k*         sum_kashaevProd_left_window_le    g_{k*}(2 + sqrt(sqrt3 N)/2)
    k* <= k < N          sum_kashaevProd_right_le          g_{k*}(2 + sqrt(N/sqrt3)/2)

What is NOT proved is the arithmetic that turns the first line into `C g_{k*}`:

  * `w := ceil(2N/3)`, so `D := k* - w >= (N-9)/6`;
  * `g_w <= g_{k*} exp(-pi D(D-1)/(sqrt3 N))` (`kashaevProd_left_tail`);
  * `e^{-x} <= 1/x` (from `Real.add_one_le_exp`) turns that into
    `g_w <= g_{k*} sqrt3 N/(pi D(D-1))`;
  * so `w * g_w <= g_{k*} * 36 sqrt3 N^2/(pi (N-9)(N-15))`, which is `<= 32`
    for `N >= 62` (checked by hand: with `sqrt3 <= 1.8` and `pi >= 3.14` the
    inequality is `35.68 N^2 - 2411.5 N + 13564.8 >= 0`, larger root ~61.6);
  * and `w * 1 <= N <= g_{k*}/N` from `sq_le_kashaevProd_argmax`.

That is a numeric grind with an explicit threshold, not a missing idea. It is
deliberately NOT waved through here: `<4_1>_N <= C sqrt(N) g_{k*}` is still not
a theorem, and neither is any statement about `<4_1>_N` itself.

Also still missing, and more important: the matching LOWER bound. Only the
single largest term is available. An upper bound alone gives an inequality, not
a value for `c_sigma`. The lower bound needs the mirror-image pointwise
inequalities -- a SECANT above `theta*` (where the tangent is an upper bound)
and the TANGENT below it -- plus `AntitoneOn.integral_le_sum` for the Gaussian
sum in the other direction.

## Landed: the FIRST LOWER BOUND. The peak is not a spike. 2026-08-09

`QOU/Knot/KashaevTailBound.lean::kashaevProd_ge_left`, sorry-free:

    for every d <= k*:
      kashaevProd N k* * exp(-sqrt3 pi d(d+1)/N) <= kashaevProd N (k*-d)

Everything before this bounds terms from ABOVE, which yields an upper bound on
`<4_1>_N` and therefore an inequality, not a value. Laplace needs the other
side: the terms near the peak must stay LARGE over a `sqrt(N)`-wide stretch, or
the sum could be `g_{k*}` and nothing more.

**And it needs no new analysis.** Below `theta*` the terms are RISING, so a
LOWER bound on `g_{k*-d}` needs an UPPER bound on the accumulated
`log(2 sin)` -- which is exactly what the TANGENT gives. Concavity, which
pointed the wrong way for the upper bound on the left (forcing the secant and
its window), points the RIGHT way here. Consequence: **there is no window**.
The tangent is global on `(0,pi)`, so this holds for every `d <= k*`.

Note `d(d+1)`, not `d(d-1)`: bounding from below costs one step more, because
the `d`-th step back is at MOST `(d+1)h` from `theta*` rather than at LEAST
`(d-1)h`. The two directions are not symmetric and the exponents record it.

### The sum lower bound is now elementary, and does NOT need an integral

`sum_{d<m} exp(-a d(d+1)) >= m * exp(-a m(m-1))` -- every term is at least the
last, since the exponent is monotone. Taking `m ~ 1/sqrt(a)` gives
`>= m e^{-1} ~ e^{-1}/sqrt(a)`, i.e. `c sqrt(N)` at `a = sqrt3 pi/N`. No
`AntitoneOn.integral_le_sum`, no Gaussian integral: the earlier plan in this
bean (which called for the integral comparison in the other direction) was
overbuilt. NOT YET WRITTEN, but it is three lines of `Finset.card_nsmul_le_sum`
plus a choice of `m`.

### Lean gotcha: an inequality stated in the wrong direction

The first draft of the induction's key step read
`-(2 sqrt3)(theta_j - theta*) >= -(2 sqrt3)(n+1) pi/N`. That is TRUE but
vacuous -- LHS >= 0 >= RHS -- and `linarith` failed on it for a reason that
looked like a missing sign fact. The needed statement is the OTHER direction,
`2 sqrt3 (theta* - theta_j) <= 2 sqrt3 (n+1) h`, which is `hfrac` scaled by
`2 sqrt3` and is purely linear in the monomials, no sign knowledge required.
When `linarith` fails on something that "should be obvious", check whether the
hypothesis you are feeding it is the trivially-true version.

Also: `div_le_iff0` vs `le_div_iff0` -- the division was on the RIGHT here and
on the LEFT in the right-tail proof, and the two need different lemmas.

### What is left

  * the sum lower bound (above -- elementary, three lines);
  * the numeric constant for the below-window region (recorded last round);
  * then `hc`, which is `c^2 sqrt3 = 1`, and step 4.

## Landed: the sum lower bound. The sqrt(N) now has BOTH sides. 2026-08-09

`le_sum_kashaevProd_left` and `le_sum_kashaevProd_left_of_sq`, both sorry-free:

    kashaevProd N k* * (m * exp(-sqrt3 pi m(m-1)/N))
        <= sum_{d<m} kashaevProd N (k*-d)

    and, when sqrt3 pi m^2 <= N,

    kashaevProd N k* * (m * e^{-1}) <= sum_{d<m} kashaevProd N (k*-d)

Taking `m ~ sqrt(N/(sqrt3 pi))` makes the second `>= c sqrt(N) g_{k*}` -- the
matching side of `sum_kashaevProd_right_le`.

**The overbuilt plan, corrected.** The previous round of this bean said the
lower bound would need `AntitoneOn.integral_le_sum` and the Gaussian integral
in the reverse direction. It needs neither. The exponent `d(d+1)` is monotone
in `d`, so every term of `sum_{d<m}` is at least the LAST one, and
`Finset.card_nsmul_le_sum` gives `m` copies of it. Three lines. The integral
machinery was only ever needed for the UPPER bound, where the terms have to be
summed against something that converges.

The caller picks `m`; expressing it as an explicit floor-of-a-square-root is
Nat arithmetic that would bury the one inequality doing the work
(`sqrt3 pi m^2 <= N` makes the last term `>= e^{-1}`).

### Lean note

Two `nlinarith` failures, both the same shape: a hypothesis `X <= Y` needed to
be scaled by `sqrt3 * pi >= 0`, and nlinarith would not find the product on its
own. Passing `mul_le_mul_of_nonneg_left h (mul_nonneg hs3.le hpi.le)` as an
explicit hint fixed both. Pattern for this file: when the goal is a hypothesis
multiplied by a positive transcendental constant, hand nlinarith the product.

### The file header now says what the file does and does not do

`KashaevTailBound.lean` has grown to eight parts. Its header now lists them and
states explicitly that NO theorem in the file bounds `<4_1>_N` -- the regions
are all bounded, above and (near the peak) below, but the numeric constant for
the below-window region is not assembled and the recombination into a single
statement about the sum is not written.

### What is left

  1. the numeric constant for the below-window region (sketch recorded two
     rounds ago; explicit threshold `N >= 62`);
  2. recombination of the four regions into one statement about
     `sum_{k<N} kashaevProd N k` -- needs an order-reversing reindex to move
     the distance-indexed window sums onto `Finset.Ico`;
  3. then `hc`, which is `c^2 sqrt3 = 1`, and step 4.

## Landed: RECOMBINATION. A bound on `<4_1>_N` -- in three named pieces. 2026-08-09

`sum_kashaevProd_Icc_eq` and `sum_kashaevProd_le_split`, both sorry-free:

    sum_{k<N} kashaevProd N k
      <= w * max 1 (kashaevProd N w)
         + g_{k*} * (2 + sqrt(sqrt3 N)/2)
         + g_{k*} * (2 + sqrt(N/sqrt3)/2)

for `6w <= 5N`, `2N + 3 <= 3w`, `w <= k*`.

This is the FIRST statement in the arc whose subject is the whole Kashaev sum
rather than a region of it.

**The reindex.** The window sums are indexed by DISTANCE from the saddle --
which is what let the Gaussian bounds apply with no reindexing at all -- while
`<4_1>_N` is indexed by `k`. `sum_kashaevProd_Icc_eq` is the one
order-reversing bridge: `Icc w k* -> Ico w (k*+1) -> range (k*-w+1)` by
`Finset.sum_Ico_eq_sum_range`, then `Finset.sum_range_reflect` and an `omega`
on the index arithmetic. Four lines, and it only has to exist once.

**`hw2` is one step stricter than the secant window.** `2N + 3 <= 3w`, not
`2N <= 3w`: the middle region is the CLOSED `[w, k*]`, so the distance-indexed
sum runs to `d = k*-w`, which lands ON `w` -- and the window must hold there
too. `omega` caught this, with a counterexample, rather than my noticing it.

### What this does NOT say

The first summand is `O(N) * max 1 g_w`, not `O(sqrt N) * g_{k*}`. Collapsing
it needs the numeric constant recorded two rounds ago (`e^{-x} <= 1/x` against
`D = k* - w ~ N/6`, threshold `N >= 62`), which is still not assembled.

So `<4_1>_N <= C sqrt(N) g_{k*}` remains NOT A THEOREM. What is proved is a
bound in three named pieces, one of which is not yet in the right shape. The
file header says exactly this.

### What is left

  1. the numeric constant (item above) -- turns piece 1 into `O(1) g_{k*}`;
  2. the matching lower bound on the WHOLE sum -- `le_sum_kashaevProd_left_of_sq`
     bounds the window from below, and the full sum dominates the window
     (all terms nonneg), so this is nearly free once the reindex above is
     reused;
  3. then `hc`, which is `c^2 sqrt3 = 1`, and step 4.

## Landed: the LOWER bound on the whole sum, and both sides phrased for `<4_1>_N`. 2026-08-09

`le_sum_kashaevProd`, plus the two `kashaev`-phrased corollaries
`le_kashaev` and `kashaev_le_split`. All sorry-free.

    kashaevProd N k* * (m * e^{-1}) <= kashaev N        when sqrt3 pi m^2 <= N
    kashaev N <= w * max 1 (kashaevProd N w)
                 + g_{k*}(2 + sqrt(sqrt3 N)/2)
                 + g_{k*}(2 + sqrt(N/sqrt3)/2)

**The lower bound needed no decomposition at all.** Dropping terms only helps,
so the window sum is a sub-sum of the whole sum with every term nonnegative --
`Finset.sum_le_sum_of_subset_of_nonneg` and the reindex from Part 9. That is
the asymmetry between the two directions in one line: an UPPER bound must
account for every term, a LOWER bound may ignore as many as it likes.

**`kashaev N` is DEFINITIONALLY the sum**, so `le_kashaev` and
`kashaev_le_split` have no proof body -- they are the same theorems with the
subject named. Worth having anyway: they are the ones to cite, because they say
"the Kashaev invariant" rather than "a sum over `Finset.range N`".

### Lean gotcha

`congr 1` on `Finset.sum s f = Finset.sum t f` leaves a FINSET equation
`s = t`, which `omega` cannot touch even when the underlying arithmetic is
trivial. Rewrite the range's Nat argument first
(`have hr : ... = m := by omega; rw [hr]`) and let the sums close by rfl.

### Where the arc stands

`<4_1>_N` is now bounded on BOTH sides by explicit expressions in `g_{k*}`. The
lower bound is already `c sqrt(N) g_{k*}` in the right shape. The upper bound
is not: its first summand is `O(N) max 1 g_w`. ONE numeric collapse
(`e^{-x} <= 1/x` against `D = k*-w ~ N/6`, threshold `N >= 62`) stands between
the current state and `c1 sqrt(N) g_{k*} <= <4_1>_N <= c2 sqrt(N) g_{k*}`.

After that, `hc` still needs the VALUE of `g_{k*}` -- these bounds are relative
to it, and turning them into `c_sigma` needs
`log g_{k*} = 2 s_{k*}` fed through `kashaev_log_sum_asymptotic`. That join is
untouched.

## Landed: the numeric collapse. `<4_1>_N` vs its own largest term, both sides. 2026-08-09

`exp_neg_le_one_div`, `max_one_kashaevProd_le`,
`sum_kashaevProd_below_window_le_argmax`, `kashaev_le_argmax_mul` -- all
sorry-free.

    <4_1>_N <= g_{k*} * ( w/N^2 + w sqrt3 N/(pi D (D-1))
                          + (2 + sqrt(sqrt3 N)/2) + (2 + sqrt(N/sqrt3)/2) )

with `D = k* - w`. With `le_kashaev` on the other side, the invariant is now
bounded ABOVE and BELOW by explicit multiples of `g_{k*}`.

**No threshold on N.** The earlier sketch in this bean proposed collapsing the
below-window region to a numeral (`<= 32`, for `N >= 62`, via `sqrt3 <= 1.8` and
`pi >= 3.14`). Leaving `D` symbolic instead costs a longer statement and buys
the removal of the threshold entirely -- and the threshold was the ugliest thing
in the plan. `e^{-x} <= 1/x` (one line from `Real.add_one_le_exp`) is what makes
that possible: it converts an exponential into a rational function with no
"for N large enough" anywhere.

Every summand of the constant is `O(sqrt N)` or better: `w/N^2 <= 1/N`; the
`D`-term is `~ 36 sqrt3/pi ~ 20` at `D ~ N/6`; the two window terms carry the
`sqrt(N)`.

### Lean gotchas

  * A multi-line `nlinarith [a, b,\n c]` nested inside `by` inside `refine
    max_le (by ...) (by ...)` does not parse -- "unexpected identifier;
    expected ']'". Pull each branch out as its own `have`.
  * `congr 1` on `Finset.sum s f = Finset.sum t f` leaves a FINSET equation that
    `omega` cannot touch. Rewrite the range's Nat argument instead.

### What is left -- and it is not a constant

The bounds are RELATIVE to `g_{k*}`. Nothing in this file evaluates `g_{k*}`
itself. Turning them into `c_sigma` means feeding
`log g_{k*} = 2 s_{k*}` through `kashaev_log_sum_asymptotic` -- i.e. joining
this arc to `qou-mlgp`'s (A). THAT JOIN IS UNTOUCHED, and it is the whole of
what remains before `hc`.

Concretely: `log <4_1>_N = log g_{k*} + log(Theta(sqrt N))`, and
`log g_{k*} = 2 s_{k*}` expands via (A) to
`-(2N/pi)Lambda(theta*) + log(2N sin theta*) + O(1/N)`. Combining gives the
`N^{3/2}` and the `c_sigma`. Every ingredient exists; the combination does not.

---

## Step 6 -- the join (`QOU/Knot/KashaevPeakValue.lean`, sorry-free)

The join above is no longer untouched. Two theorems, both
`[propext, Classical.choice, Quot.sound]`.

**`log_kashaevProd_asymptotic`** -- for `1 <= k < N`, `4 <= N`:

    | log g_k - ( -(2N/pi) Lambda(theta_k) + log(2 N sin theta_k)
                  + (pi/6N) cot theta_k ) |
      <= 2*( 1/(144 k^2) + (7/12)(pi/N)^2 + (pi/N)^2/(12 sin^2 theta_k) )

with `theta_k = k pi / N`. This is `kashaev_log_sum_asymptotic` (bean
`qou-mlgp`, gap A) doubled through
`log_kashaevProd : log g_k = 2 sum_{j=1}^{k} log(2 sin(j pi/N))`.

The mathematical content is entirely in the two imported theorems; what this
one costs is bookkeeping, and it is worth recording that the bookkeeping was
the only thing standing between the two arcs for several sessions:

  * index sets: `Finset.Icc 1 k` on the `log_kashaevProd` side vs
    `Finset.Ico 1 (k+1)` on the Euler-Maclaurin side (`ext j; simp only
    [Finset.mem_Icc, Finset.mem_Ico]; omega` -- NOT the deprecated
    `Nat.Ico_succ_right`);
  * the angle: `(j:R) * (pi/N)` vs `(j:R) * pi / N` (`mul_div_assoc`);
  * the doubling itself: the target main term is EXACTLY twice (A)'s, term by
    term, including `pi/(6N) = 2 * pi/(12N)`. `field_simp; ring` after `set`ing
    the four big subterms opaque.

**`log_kashaevProd_saddle`** -- the same, re-centred on the exact saddle angle
`5pi/6` instead of `theta_k`, for any `k` with `|theta_k - 5pi/6| <= pi/N`
(which `floor(5N/6)` and `ceil(5N/6)` both satisfy). Extra cost:

    (2N/pi) * ( sqrt3 (pi/N)^2 / 2 + M (pi/N)^3 / 6 )

where `M` dominates `1/sin^2` between the two angles. Via
`abs_Lob_taylor_saddle`, whose linear term vanishes because
`Lambda'(5pi/6) = -log(2 sin(5pi/6)) = 0`.

**That penalty is `O(1/N)`, not `O(1/N^2)`, and that is not slack in the
argument.** The `N` in front of `Lambda` amplifies the quadratic Taylor term
`sqrt3 d^2/2 ~ 1/N^2` back up to `1/N`. Probe part (iii) pins it: at `N = 961`
the true re-centring cost is `3.92e-3` against a bound of `5.68e-3`, and
`penalty * N -> 5.455` against `sqrt3 pi = 5.441`. The bound is within 45% of
the truth and converging to the right constant, so nothing is being thrown away
here. It matters downstream: `c_sigma` is only visible after the `sqrt N` from
the Gaussian window is divided out, and an `O(1/N)` term in the exponent is not
smaller than that.

### Probe

`computations/probes/kashaev_peak_value_probe.py` -- all assertions pass.
Part (i) at the saddle index for `N` up to 960; part (ii) at nine indices
spread across `[1, N)` for `N in {60, 240}`; part (iii) the re-centring with
`N` NOT divisible by 6 so the offset is genuinely nonzero; part (iii-b) the
degenerate `6 | N` case, where `theta_{k*} = 5pi/6` to 35 digits and (II)
collapses back to (I); part (iv) the sanity check that
`-(2/pi) Lambda(5pi/6) = Vol(4_1)/(2 pi) = 0.323065947219`, i.e. that the
leading term really is the hyperbolic volume.

First draft of part (iii) used only `N` divisible by 6 -- every offset was
exactly 0, so the Taylor penalty was never exercised and the test was vacuous
while printing "ok". Caught by noticing the `true cost` column was all zeros.

### What is left

`log <4_1>_N = log g_{k*} + log(Theta(sqrt N))` now has BOTH halves:
step 5 bounds `<4_1>_N / g_{k*}` above and below, step 6 evaluates
`log g_{k*}`. Remaining before `hc`:

  1. combine them -- take `log` of the step-5 sandwich and add step 6;
  2. `hc : c^2 |cot theta| = (2 sin theta)^2`, which at `theta* = 5pi/6`
     reduces to `c^2 sqrt3 = 1`;
  3. `htau`.

---

## Step 7 -- `log <4_1>_N` absolutely (`QOU/Knot/KashaevLogAsymptotic.lean`)

Eight theorems, all `[propext, Classical.choice, Quot.sound]`. The sandwich
stops being relative to the peak.

**The saddle index, concretely.** `argmax_angle_eq` gives the exact identity

    theta_{k*} = 5pi/6 - r pi/(6N),   r = 5N mod 6 in [0, 5]

from `Nat.div_add_mod` and nothing else. Two corollaries feed
`log_kashaevProd_saddle`'s two hypotheses: `argmax_offset_le`
(`|theta_{k*} - 5pi/6| <= pi/N`, in fact <= 5pi/6N) and `argmax_angle_mem`
(`theta_{k*} in [pi/6, 5pi/6]`).

The DIRECTION matters and is worth stating: `floor` undershoots, so
`theta_{k*} <= 5pi/6` always -- the saddle index approaches the saddle angle
from below, never above. That is what puts the whole interval inside
`[pi/6, 5pi/6]`, where `half_le_sin` (step 1) already gives `sin >= 1/2`, hence
`M = 4`. And `M = 4` is SHARP for that interval, not an estimate: `1/sin^2` is
exactly 4 at both endpoints. `log_kashaevProd_argmax` is the peak value with
every constant explicit.

**Logging the sandwich.** `kashaevUpperConst N w` names the constant from
`kashaev_le_argmax_mul` so it can be logged; `four_le_kashaevUpperConst` gives
its positivity (the two window terms alone contribute 4). Then

    le_log_kashaev :  log g* + log m - 1     <= log <4_1>_N
    log_kashaev_le :  log <4_1>_N <= log g* + log C(N,w)

Pure monotonicity; the only content is positivity of both sides, from
`sq_le_kashaevProd_argmax` and `kashaev_pos`.

### The hypotheses are satisfiable only from N = 18

`log_kashaev_le` needs `2N+3 <= 3w` (secant window) AND `2 <= 5N/6 - w` (two
steps of gap). Those pull against each other, and below `N = 18` there is no
`w` at all -- at `N = 12` the constraints ask for `w >= 9` and `w <= 8`.
Probe part (v-a) pins the threshold at exactly 18 and asserts it, so that if a
future edit to the hypotheses moves it, the probe says so instead of silently
covering fewer `N`.

This is a real restriction, not slack I can argue away: the below-window
collapse (step 5, part 10) genuinely needs `D = k* - w >= 2` for
`1/(D(D-1))` to be finite.

### What the bracket delivers -- and what it does NOT

With `m ~ sqrt(N/(sqrt3 pi))` and `w = ceil((2N+3)/3)`, probe part (vi):

    N     log<4_1>_N - N Vol/(2pi) - (3/2)log N
    18    -0.2409
    96    -0.2688
    768   -0.2739          target  log(3^(-1/4)) = -0.274653

Monotone, gap `7.2e-4` at `N = 768`. **`c_sigma = 3^(-1/4)` is confirmed to
four digits by the assembled main term** -- the volume `N Vol/(2pi)`, the
`(3/2) log N`, and the constant all come out of the formalised pieces.

But the Lean sandwich only brackets `c_sigma` in `[0.146, 1.670]`. The width
does not shrink to 0, and no amount of tuning `m` and `w` will close it. The
reason is structural: step 5's Gaussian sums are one-sided-crude (peel the
first term, compare the rest to an integral), which is enough for
`Theta(sqrt N)` and loses the constant. **Pinning `c_sigma` needs a two-sided
Laplace with matching leading constant -- i.e. `qou-mlgp` gap (B), which is not
closed.** The Jacobi theta route (`hasSum_gaussian_theta`,
`hasSum_gaussian_theta_tilt`, already in-repo) is where I would go: it gives
`sum_{d in Z} e^{-a d^2} = sqrt(pi/a) * (1 + exponentially small)`, which is
the sharp constant rather than a bound.

So the honest state after step 7: **the growth ORDER
`<4_1>_N = Theta(N^{3/2} e^{N Vol/2pi})` is formalised with explicit
constants on both sides. The CONSTANT `c_sigma` is not.**

### Probe

`computations/probes/kashaev_log_asymptotic_probe.py` -- all assertions pass.
Parts (i)-(iv) check the four saddle-index theorems and `M = 4`'s sharpness;
(v-a) the `N >= 18` threshold; (v-b) the sandwich against the true
`<4_1>_N = sum_k g_k` for `N` up to 768; (vi) the residual against
`log(3^(-1/4))`, asserted both to be within `2e-3` and to be still
approaching (not sitting at some other constant).

### Remaining before `hc`

  1. gap (B) -- sharp two-sided Laplace, to pin `c_sigma` rather than bracket
     it. This is now the ONLY thing between step 7 and the constant.
  2. `hc : c^2 |cot theta| = (2 sin theta)^2`, at `theta* = 5pi/6` reducing to
     `c^2 sqrt3 = 1`.
  3. `htau`.

---

## Step 8 -- the sharp Laplace sum (`QOU/MathlibExt/GaussianThetaBound.lean`)

Five theorems, all `[propext, Classical.choice, Quot.sound]`. This is the
first half of `qou-mlgp` gap (B) -- the half that says the Gaussian sum IS its
integral, not merely `Theta` of it.

    abs_tsum_gaussian_sub_sqrt_le :
      | sum_{n in Z} e^{-a(n-c)^2}  -  sqrt(pi/a) |
          <=  sqrt(pi/a) * 2q/(1-q),    q = e^{-pi^2/a}

uniformly in the shift `c`. `GaussianThetaSum` already had the exact identity
`sum = sqrt(pi/a) Re theta_2(-c, i pi/a)`; what was missing was the one
estimate making it usable, `theta_2 = 1 + O(e^{-pi^2/a})`, which is
`norm_jacobiTheta₂_sub_one_le`.

The proof is Mathlib's own `norm_jacobiTheta₂_term_le` at `S = 0` -- the
argument `-c` is real, so the theta series has no growth from the `z`
direction, and THAT is what makes the bound uniform in `c` -- summed against a
two-sided geometric series via `n^2 >= |n|`.

Contrast with `GaussianSumBound`: `sum <= 1 + sqrt(pi/a)/2` is one-sided and
carries an additive `1`; it proves `Theta(1/sqrt a)` and cannot see the
constant. Step 8 has no additive slack at all and the relative error is
exponential, not polynomial.

### Where 3^(-1/4) comes from

At `a = sqrt3 pi/N` (the Kashaev tail's exponent, `sqrt3 = Lambda''(5pi/6)`):

    sqrt(pi/a) = sqrt(N/sqrt3) = N^(1/2) * 3^(-1/4)

So `c_sigma = 3^(-1/4)` is not a separate fact to be derived -- it is the
Gaussian width at the saddle, and the `3` is `Lambda''(5pi/6) = -cot(5pi/6)`.
And the theta correction there is `e^{-pi N/sqrt3}` (probe part (iv):
`1.1e-47` at N=60), so for the constant, replacing the sum by the integral is
free. Everything that is lost is lost elsewhere.

### Lean gotchas -- two, and both cost a cycle

  * `HasSum.of_nat_of_neg` MUST be given `f` explicitly. Left to unification,
    `?f (n:Z) =?= (if (n:Z) = 0 then 0 else q^(n:Z).natAbs)` is a higher-order
    problem Lean searches at length: the step alone blew a 1000000-heartbeat
    budget. With `(f := ...)` the whole theorem elaborates in 2.3s.
  * `jacobiTheta₂_term 0 z tau = 1` costs more than 200000 heartbeats under
    plain `simp`/`norm_num`, for no reason visible in the statement. Spelling
    out the lemma list makes it instant.

### A false "isolated success" -- worth recording

While debugging the first gotcha I extracted the lemma to a scratch file, and
`#print axioms` reported it CLEAN while the same text timed out in place. The
scratch file had a failing `example` above it. **When an earlier declaration
in a file errors, a later one can report clean axioms without having been
checked.** Re-testing with the failing example deleted showed the timeout.
Lesson: an axiom check is only evidence if the file it ran in is error-free.

### Probe

`computations/probes/gaussian_theta_bound_probe.py` -- all assertions pass.
(i) the theta bound at four `a` and four `c`, including the check that it is
NEAR-ATTAINED at `c = 0` (ratio 0.9999 at `a = 1`) so it cannot be dismissed as
loose; (ii) the Laplace sum against its integral; (iii) `c = 1/2`, the worst
shift, where the correction changes sign; (iv) the Kashaev regime.

Part (ii)'s `a = 0.05` rows report `noise`, not `ok`: there the true difference
is below mp roundoff at 60 digits, so the comparison against the bound is
vacuous and only the tolerance made it pass. They assert instead that the sum
is indistinguishable from the integral at working precision. Reporting `ok`
would have been reporting a check that did not happen.

### Remaining before `hc`

Gap (B)'s SECOND half, which step 8 does not touch: uniform two-sided control
of `g_{k*+d}/g_{k*}` against `e^{-a d^2}` for `|d| <~ N^{0.6}`, so that the
Kashaev sum can be replaced by the Gaussian sum in the first place. Step 6
(`log_kashaevProd_asymptotic`, error `O(1/N^2)` uniformly) is a much stronger
tool for this than step 5's one-sided tangent/secant bounds -- the ratio's
expansion is `-sqrt3 pi d^2/N + O(d^3/N^2) + O(1/N^2)` plus a linear term
`O(d/N)` from `Lambda'(theta_{k*}) != 0` (it vanishes only at exactly `5pi/6`).
Then `hc`, then `htau`.

---

## Step 9 -- the ratio against a Gaussian (`QOU/Knot/KashaevRatioExpansion.lean`)

Three theorems, all `[propext, Classical.choice, Quot.sound]`. Gap (B)'s
second half begins: step 8 says a Gaussian sum equals its integral, and to use
that on `<4_1>_N = sum_k g_k` one must first know the summand IS a Gaussian.

`logKashaevMain` / `logKashaevErr` name step 6's main and error terms.

  * `abs_log_kashaevProd_ratio_le` -- the triangle inequality on two instances
    of step 6. Trivial, but note what it buys: the bound on the RATIO is
    two-sided and uniform, which NO tail bound in `KashaevTailBound` is. Step
    5's bounds are a tangent line one way and a secant line the other; they
    cannot be sharp in the constant by construction.
  * `abs_log_kashaevProd_ratio_taylor` -- Taylor `Lambda` about `theta_k` and
    the Gaussian appears:

        log(g_k'/g_k) = 2u log(2 sin th_k) + (pi u^2/N) cot th_k
                        + [log(2N sin th_k') - log(2N sin th_k)]
                        + (pi/6N)[cot th_k' - cot th_k]
                        + err,    |err| <= Err_k + Err_k' + M pi^2 |u|^3/(3N^2)

    with `u = k' - k` REAL, so `k'` may sit on either side of `k`.

### The two coefficients, and why they are what they are

**Quadratic.** `a = pi |cot th_k|/N -> sqrt3 pi/N`, and `sqrt(pi/a) ->
sqrt(N) 3^(-1/4)`. Probe part (iii) checks the rate, not just a value: the
relative gap times `N` is `3.023` at every one of N = 241, 481, 961, 1921 --
constant to four digits. And `3.023` is not a fitted number:
`|cot th_k*|` misses `sqrt3` by `4 * 5pi/(6N) = 10pi/(3N)` (since
`d cot/d th = -1/sin^2 = -4` at `5pi/6` and `th_k*` undershoots by
`r pi/6N`, `r <= 5`), a relative `10pi/(3 sqrt3 N) = 6.046/N`, and `sqrt`
halves it. **So `c_sigma = 3^(-1/4)` is `Lambda''(5pi/6)^(-1/2)` and nothing
else.**

**Linear.** `2u log(2 sin th_k)` does NOT vanish. It is exactly zero when
`6 | N` and nonzero otherwise (probe part (iv) asserts BOTH directions), of
size `~4.52/N`. It is a tilt of the Gaussian -- a shift of the summation
centre -- not an error to be bounded away, which is what
`hasSum_gaussian_theta_tilt` exists for.

### A real restriction: the sqrt(N) window vs the endpoint singularity

Probe part (v). Going `u = sqrt(N)` steps RIGHT from `k*` lands at angle
`5pi/6 + pi/sqrt(N)`, whose distance to `pi` is `pi/6 - pi/sqrt(N)` -- small
when `N` is small. So `M = sup 1/sin^2` blows up at small `N`:

    N        60      240      960     3840    15360
    M      40.86     9.68     5.87     4.81     4.38     (-> 4)
    bound  12.84     1.87     0.57     0.24     0.11

The bound crosses 1 between N=240 and N=960. **Below that the sqrt(N) window
runs into the endpoint singularity and this expansion does not control it.**
The probe asserts the threshold (first below 1 at N=960) rather than claiming
smallness everywhere -- a first draft asserted `bound < 1` at every N and
failed honestly at N=60 and N=240.

Consequence for the eventual proof: the window must be stated as
`|u| <= c sqrt(N)` with a constant `c` small enough to keep the right edge
away from `pi`, or with a threshold on `N`. It is not free.

### Remaining before `hc`

  1. Exponentiate step 9: `g_{k*+u}/g_{k*} = e^{-a u^2 + tilt}(1 + O(eta))`
     with `eta -> 0` uniformly on the window.
  2. Sum over the window, apply step 8 (tilted form) to get
     `sqrt(pi/a)(1 + exponentially small)`.
  3. Cut the tail beyond the window with step 5's one-sided bounds (lossy
     there is fine -- the tail is exponentially small).
  4. Combine with step 7 to get `c_sigma`, then `hc`, then `htau`.

`hc` itself, once `c_sigma` is in hand, is the algebra already proved in
`OneLoopPrefactorInvariance.lean`: `hc : c^2 |cot th| = (2 sin th)^2` is
"Stirling factor squared over Gaussian width", and step 6 supplies the
`2N sin th*` while steps 8-9 supply the `sqrt(N/|cot th*|)`.

---

## Step 10 -- absorbing the two extras (same file, +3 theorems)

`abs_log_kashaevProd_ratio_taylor` left two pieces that are not part of the
Gaussian: the variation of `log(2N sin th)` and of `cot th` across the window.
Both are now bounded by mean value on the interval, via Mathlib's
`Convex.norm_image_sub_le_of_norm_hasDerivWithin_le`:

  * `abs_log_two_sin_sub_le` -- derivative `cot`, bound `K |b-a|`;
  * `abs_cot_sub_le` -- derivative `-1/sin^2`, bound `M |b-a|`;
  * `abs_log_kashaevProd_ratio_gaussian` -- the payoff:

        | log(g_k'/g_k) - [ 2u log(2 sin th_k) + (pi u^2/N) cot th_k ] |
          <= Err_k + Err_k' + M pi^2 |u|^3/(3N^2)
             + K pi |u| / N + M pi^2 |u| / (6 N^2)

`K` bounds `|cot|`, `M` bounds `1/sin^2`. They are not independent
(`cot^2 <= 1/sin^2`, so `K <= sqrt M` always works) but keeping them separate
avoids dragging a square root through the arithmetic for nothing.

The `N` inside `log(2N sin th)` cancels out of the difference -- one
`Real.log_mul` on each side -- so the mean-value bound is on `log(2 sin th)`,
whose derivative is exactly `cot`.

### Absorbing costs the RATE, and that is the number to remember

Probe part (vii). The ratio itself is pinned to `O(1/N^2)`. But the absorbed
`K pi |u| / N` term is `~ K pi / sqrt(N)` at `|u| ~ sqrt(N)`, so at the window
edge the total error is `Theta(1/sqrt N)`, not `O(1/N^2)`:

    N          960     3840    15360    61440
    bound     0.783    0.341    0.160    0.077
    x sqrt N  24.26    21.12    19.80    19.20   <- settling, so the rate is 1/sqrt(N)

Still `-> 0`, so the Laplace step is licensed; but the eventual `c_sigma`
statement will carry a relative error `O(1/sqrt N)` and no better unless the
`log(2N sin th)` variation is kept rather than absorbed. That is a real choice
made here, not an artefact: keeping it would mean carrying a `k`-dependent
prefactor through the summation, which is more machinery for a better rate that
the constant does not need (identifying `c_sigma` is a limit statement).

### Lean gotchas

  * `(convex_uIcc a b).norm_image_sub_le_of_norm_hasDerivWithin_le` -- dot
    notation already supplies the `Convex ℝ s` argument. Passing
    `convex_uIcc a b` again shifts `x`/`y` into the wrong slots and the error
    surfaces as "Function expected at ..." with a nonsense type, not as an
    arity complaint.
  * `simpa [Real.norm_eq_abs] using hK x hx` FAILS where
    `rw [Real.norm_eq_abs]; exact hK x hx` succeeds: simp rewrites
    `|cos x / sin x|` into `|cos x| / |sin x|` and then no longer matches.

### Remaining before `hc`

  1. Exponentiate: `g_{k*+u}/g_{k*} = e^{tilt + quadratic} (1 + O(1/sqrt N))`
     on `|u| <= c sqrt(N)`.
  2. Sum over the window and apply step 8 in its TILTED form
     (`hasSum_gaussian_theta_tilt`) -- the tilt is why that form exists.
  3. Cut the tail beyond the window with step 5 (lossy is fine there).
  4. Combine with step 7 for `c_sigma`, then `hc`, then `htau`.

---

## Step 11 -- pointwise Gaussian to Gaussian SUM (`QOU/Knot/KashaevWindowSum.lean`)

Five theorems, all `[propext, Classical.choice, Quot.sound]`. The two
mechanical steps between step 10 and Laplace.

  * `kashaevProd_eq_mul_exp` -- `g_k' = g_k exp(log g_k' - log g_k)`, the only
    place positivity of both terms is used (`kashaevProd_pos`).
  * `kashaevProd_bounds_of_log_bound` -- `|log(g_k'/g_k) - T| <= B` becomes
    `g_k e^{T-B} <= g_k' <= g_k e^{T+B}`, both directions from one hypothesis.
  * `sum_kashaevProd_le_of_log_bound` / `le_sum_kashaevProd_of_log_bound` --
    over any `Finset` window, `e^{+-B}` factors out of every term.
  * `sum_kashaevProd_window_sandwich` -- the two combined:
    `|sum_s g_k' - g_k sum_s e^T| <= g_k (e^B - 1) sum_s e^T`.

**`T : N -> R` and `B : R` are abstract.** Nothing in this file knows about
`Lambda`, the saddle, or `4_1`. That is deliberate: a sharper expansion than
step 10's can be dropped in without touching these proofs.

### No sign hypothesis on B -- a correction

A first draft carried `0 <= B`, reasoning that `e^B - 1` had better be
nonnegative. Lean's unused-variable linter flagged it, and the linter was
right: the lower half rests on `e^B + e^{-B} >= 2`, which holds for EVERY real
`B`, so no sign hypothesis is needed. (And a negative `B` forces the window
empty -- it would bound an absolute value below zero -- so both sides are 0 and
the statement is true there too.) The docstring now says this instead of the
wrong justification I had written.

### The sandwich is not vacuous

Probe part (iv). The sandwich is only worth anything if `e^B - 1 -> 0`:

    N        240      960     3840    15360
    B       2.449    0.783    0.341    0.160
    e^B-1  10.577    1.188    0.406    0.173
    true/model - 1   0.00533  0.00131  0.00033  0.00008

So model and true window sum agree to `1 + O(1/sqrt N)` -- the rate step 10
established. Note the bound is loose by ~2000x against the truth; that is the
price of a sup-over-the-window `B` and it does not matter, since only
`e^B - 1 -> 0` is needed.

### A display that lied, caught

Probe part (iii) first printed the raw window sums. `g_k ~ e^{0.323 N}`, so at
N = 3840 those are `~1e539` and `float()` renders them `inf`: the table read
`inf  inf  inf   ok`. The COMPARISON was genuine throughout (mpmath has
arbitrary exponent range) -- but a column of `inf` next to `ok` shows nothing,
so everything is now normalised by `g_k`.

Separately: a `python3 - <<'PY'` patch script of mine used `s.split('\\n')`
inside a quoted heredoc, which splits on a literal backslash-n and collapsed
the whole probe to one line. Rewrote the file rather than trying to unpick it.

### Remaining before `hc`

  1. Evaluate `sum_s e^{T(k')}` -- extend the window to `Z`, apply step 8 in
     its TILTED form, and subtract the tail. Step 8 gives
     `sqrt(pi/a)(1 + exp small)`; step 5 gives the tail.
  2. Combine with step 7 for `c_sigma`; then `hc`; then `htau`.

---

## Step 12 -- the tilted Gaussian sum (`QOU/MathlibExt/GaussianTiltedSum.lean`)

Five theorems, all `[propext, Classical.choice, Quot.sound]`.

Step 10's summand is `e^{-a u^2 + 2 L u}` -- a Gaussian with a linear tilt.
Completing the square is the whole idea: `-a u^2 + 2 L u = L^2/a - a(u - L/a)^2`,
so a TILT IS A SHIFT of the centre by `L/a` plus a factor `e^{L^2/a}`. And step
8 was proved uniformly in the shift, which is exactly why it was stated that
way. The tilt costs one line of algebra and an already-uniform estimate; no new
analysis.

    abs_tsum_tilted_gaussian_sub_le :
      | sum_{n in Z} e^{-a n^2 + 2 L n}  -  e^{L^2/a} sqrt(pi/a) |
        <= e^{L^2/a} sqrt(pi/a) * 2q/(1-q)

`e^{L^2/a} sqrt(pi/a)` is exactly `int_R e^{-a x^2 + 2 L x} dx`, so this says
the tilted Laplace sum is its tilted Laplace integral.

### THE PAYOFF -- `c_sigma = 3^(-1/4)` from the formalised ingredients

Probe part (iv) instantiates `a` and `L` with exactly what step 10 produces at
the Kashaev saddle (`a = pi |cot th_k*| / N`, `L = log(2 sin th_k*)`,
`k* = floor(5N/6)`) and divides the model sum by `sqrt(N)`:

    N          241      961     3841    15361    61441
    model/sqrtN  0.78153  0.76523  0.76118  0.76017  0.75992
    gap        2.17e-2  5.39e-3  1.35e-3  3.37e-4  8.41e-5
    gap x N      5.227    5.183    5.172    5.169    5.168

against `3^(-1/4) = 0.7598356857`. **Computed from the Lean statements' own
ingredients, not from the closed form.**

And the `O(1/N)` decomposes completely, which is the part I find convincing:

  * `sqrt(pi/(aN)) = |cot th_k*|^{-1/2}`, and `|cot th_k*| = sqrt3 - 10pi/(3N)`
    (step 9), so this contributes a relative `+3.023/N`;
  * `e^{L^2/a} = 1 + L^2/a + ...` with `L ~ 4.52/N` and `a ~ sqrt3 pi/N`, so
    `L^2/a ~ 3.755/N` -- the TILT's contribution.

`(3.023 + 3.755) * 3^(-1/4) = 5.15`, against the observed 5.168. Both halves of
the `1/N` are accounted for, and neither is an error term -- one is the
Hessian's offset from the saddle, the other is the tilt.

### Remaining before `hc`

Only the bookkeeping between "model sum over Z" and "the actual Kashaev sum":

  1. window -> Z. The easy half is `sum_le_tsum_tilted_gaussian` (any finite
     part <= the whole), already here. The other half needs a Gaussian tail
     bound beyond the window -- `GaussianSumBound` is enough there, since
     losing the constant on an exponentially small tail costs nothing.
  2. Assemble: step 11's sandwich + step 12's evaluation + step 7's peak value
     gives `<4_1>_N = c_sigma N^{3/2} e^{N Vol/2pi} (1 + o(1))`.
  3. `hc` (already algebraically proved in `OneLoopPrefactorInvariance.lean` --
     it is "Stirling factor squared over Gaussian width"), then `htau`.

---

## Step 13 -- the Gaussian tail outside the window (`QOU/MathlibExt/GaussianTailBound.lean`)

Two theorems, both `[propext, Classical.choice, Quot.sound]`. The last piece of
the window-vs-`Z` comparison; the easy half was already in step 12.

    tsum_gaussian_sub_sum_Icc_le :
      sum_{n in Z} e^{-a(n-c)^2} - sum_{|n|<=W} e^{-a(n-c)^2}
        <= e^{a c^2} e^{-a(W+1)^2/4} (1 + 2 sigma/(1-sigma)),  sigma = e^{-a/4}

plus `hasSum_int_geometric` (`sum_{n in Z} q^|n| = 1 + 2q/(1-q)`), which is
step 8's `hasSum_int_geometric_ne_zero` with the `n=0` term put back.

The bound is deliberately crude -- three give-aways in a row: `(n-c)^2 >=
n^2/2 - c^2` (costs the `e^{ac^2}`), `n^2 >= (W+1)^2/2 + n^2/2` for
`|n| >= W+1`, and `n^2 >= |n|` to reach a geometric series. A sharp bound would
keep `e^{-a(W+1)^2}` instead of `e^{-a(W+1)^2/4}`. Probe part (iii) MEASURES the
crudeness (overshoot 2.1e12 at a=1, c=0, W=5) rather than leaving "crude" as an
assertion.

### The window exponent is a real tradeoff, and my first guess was wrong

Writing `W = N^p`:

  * this tail is `~ 1.93 sqrt(N) exp(-1.36 N^{2p-1})` -- wants `p` large;
  * step 10's cubic is `~ N^{3p-2}` -- wants `p` small, and needs `p < 2/3`.

    N       p      tail/main    cubic
    1e4   0.55     6.22e+00    3.98e-02
    1e4   0.60     3.43e-02    1.58e-01
    1e4   0.65     7.65e-08    6.31e-01
    1e6   0.55     8.57e+00    7.94e-03
    1e6   0.60     8.30e-07    6.31e-02
    1e6   0.65     1.01e-34    5.01e-01

**`p = 0.6` is the balanced choice** (tail exponent `N^{0.2}` against cubic
`N^{-0.2}`), and NEITHER end of `(1/2, 2/3)` is comfortable:

  * at `p = 0.55` the tail bound is still 8.6x the main term at `N = 1e6` --
    `1.36 N^{0.1} = 5.4` has not yet beaten the `0.5 log N = 6.9` coming from
    the `sqrt(N)` prefactor. That crossover is near `N ~ 1e10`. Asymptotically
    valid, practically useless.
  * at `p = 0.65` the tail is nothing but the cubic decays only like
    `N^{-0.05}` -- WORSE overall.

I had written "the tail is much happier near the top of that range"; the
numbers say otherwise and the probe docstring now says so. The probe asserts
the `p=0.55` uselessness explicitly, so the claim cannot rot.

### Probe gotcha

Part (i) first summed the geometric series over a fixed `+-400`. At `q = 0.99`
that truncates at `0.99^400 = 0.018` and reported `195.45` against the correct
`199` -- a wrong sum, not a rounding artefact. Truncation is now adaptive in
`q`. (The `q = 0.9` case failed too, but only in the 18th digit; the `q = 0.99`
failure is the one that mattered.)

### Remaining before `hc`

All the pieces now exist. What is left is assembly, in one file:

  1. window `[k*-W, k*+W]` -> step 11 sandwich -> step 12 evaluation
     -> step 13 tail;
  2. everything outside the window -> step 5 (lossy there is free, the region
     is exponentially small);
  3. divide by `g_{k*}`, use step 7 for `log g_{k*}`, and read off
     `<4_1>_N = c_sigma N^{3/2} e^{N Vol/2pi} (1 + o(1))` with
     `c_sigma = 3^{-1/4}`;
  4. `hc` -- already algebraically proved in `OneLoopPrefactorInvariance.lean`;
     then `htau`.

---

## Step 14 -- the finite window, and the index bridge

Four theorems, all `[propext, Classical.choice, Quot.sound]`.

**`QOU/MathlibExt/GaussianWindowSum.lean`** -- steps 12 and 13 combined into the
statement the Kashaev assembly actually consumes:

    | sum_{|n|<=W} e^{-an^2+2Ln}  -  e^{L^2/a} sqrt(pi/a) |
      <= e^{L^2/a} ( sqrt(pi/a) * 2q/(1-q)  +  (tail beyond W) )

The two errors are kept SEPARATE on purpose: one is sum-versus-integral
(exponentially small in `1/a`, nothing to do with the window), the other is the
tail (exponentially small in `aW^2`, nothing to do with sum-versus-integral),
and they are optimised by opposite choices of `W`.

Numerically at the Kashaev parameters they are not close to comparable --
probe part (iii), `W = N^0.6`:

    N        log10(theta err)   log10(tail)   decades apart
    1e4          -7877.0             0.4          7877
    1e6        -787721.8            -3.2        787719

So the separation is about the STATEMENT, not the numbers; nobody should spend
effort sharpening the theta half.

**`QOU/Knot/KashaevWindowIndex.lean`** -- `sum_Icc_shift_int`, reindexing a
symmetric `N`-window around `k*` as a symmetric `Z`-window around `0`. Needed
twice with different `F` (on `kashaevProd` and on the model `e^{T}`), and both
must be reindexed the same way or the comparison compares different sums.

### `W <= k` is load-bearing, and its failure is SILENT

Without it, Nat subtraction truncates `k - W` to `0` and `Int.toNat` clamps
`(k+n).toNat` to `0`; the two sides then disagree and NEITHER errors. Probe
part (iv) exhibits concrete disagreements (`k=3, W=10`: 0.1048 vs 0.2476), so
the hypothesis is visibly not decorative.

### Lean gotcha

`Finset.sum_nbij'` leaves its five side goals with the maps un-beta-reduced, so
`omega` sees `(fun j => ↑j - ↑k) j` as an opaque atom and reports a
"counterexample" in terms of it. `simp only []` (or `simp only [Finset.mem_Icc]`,
which also beta-reduces) before `omega` in every branch.

### Probe gotcha -- the same display lie, caught again

Part (iii) first printed the theta error directly. It is about `e^{-pi N/sqrt3}`,
so `float()` underflows below 1e-308 and the column read a flat `0.0000e+00`
with a `0.0000e+00` ratio beside it. mpmath's comparison was exact throughout;
the display was not. Now printed as log10. (Same failure mode as step 11's raw
window sums -- worth watching for whenever a quantity is exponentially large or
small in `N`.)

### Remaining before `hc`

The assembly, now purely mechanical:

  1. instantiate step 11's sandwich on `s = Icc (k*-W) (k*+W)` with
     `T k = -a(k-k*)^2 + 2L(k-k*)`, `a = pi|cot th_k*|/N`;
  2. `sum_Icc_shift_int` to move both sides to the `Z`-window;
  3. `abs_sum_Icc_tilted_sub_le` to evaluate the model;
  4. step 5 for everything outside the window;
  5. step 7 for `log g_{k*}` -- and `c_sigma = 3^{-1/4}` follows.

---

## Step 15 -- THE ASSEMBLY (`QOU/Knot/KashaevWindowAssembly.lean`)

Three theorems, all `[propext, Classical.choice, Quot.sound]`. Steps 11 and 14
meet:

    | sum_{|k'-k|<=W} g_k'  -  g_k e^{L^2/a} sqrt(pi/a) |
      <= g_k ( (e^B - 1)(e^{L^2/a} sqrt(pi/a) + E) + E )

`a`, `L`, `B` are PARAMETERS, not the Kashaev values -- the hypothesis is
exactly what `abs_log_kashaevProd_ratio_gaussian` delivers, so specialising is
a matter of supplying `a = pi|cot th_k|/N` and `L = log(2 sin th_k)`. The
assembly itself has no knot in it.

`cast_toNat_shift_sub` and `sum_window_model_eq` do the reindexing; `B >= 0`
is DERIVED (the window contains `k`, so `h k` bounds an absolute value)
rather than assumed.

### `nlinarith` -> `linarith`: 6m19s -> 11s

The final combination is `h11 + hsecond + hfirst`, which is LINEAR in the
(large) atoms. `nlinarith` searched products it never needed and took 6m19s;
`linarith` closes it in 11s. Worth remembering whenever the atoms are big sums:
reach for `linarith` first and only escalate if it genuinely needs a product.

### THE PAYOFF, from the Kashaev sum itself

Probe part (iii), `W = N^0.6`, `N` not divisible by 6:

    N        window/(g_k sqrt N)     gap to 3^(-1/4)
    241          0.7620803696          2.24e-03
    961          0.7603947088          5.59e-04
    3841         0.7599753048          1.40e-04

against `3^(-1/4) = 0.7598356857`. Step 12 reached this from the Gaussian
MODEL; this is the Kashaev sum.

### The bound is proved and is NOT numerically sharp -- say so

Probe part (iv):

    N        bound/model
    241        2.50e+12
    961        5.83e+03
    3841       7.35e+01

Shrinking fast, still ~74x the main term at the largest N the probe reaches.
**What pins `c_sigma` is the limit, which part (iii) exhibits; the finite-N
bound does not.** The dominant cost is `B` (the sup over the window of step
10's bound, 4.22 at N=3841), and `e^B - 1` is brutal at `B ~ 4`. Sharpening
would mean a `k'`-dependent `B` instead of a sup -- more machinery for a better
finite-N constant that the limit statement does not need.

### Probe gotcha -- the 6 | N degeneracy, AGAIN

First draft used N = 240, 960, 3840. For `6 | N` the saddle index hits `5pi/6`
exactly, so `L = 0` and the model is `3^(-1/4) sqrt(N)` BY CONSTRUCTION -- the
tilt is never exercised and part (iii)'s model column is a tautology that
printed the target to 10 digits at every N. Same trap as the step-6 probe.
Now N = 241, 961, 3841.

### Remaining before `hc`

  1. specialise the assembly at the Kashaev values (supply `a`, `L`, `B` from
     step 10 and `hs`/`h` from `abs_log_kashaevProd_ratio_gaussian`);
  2. add the outside-window region via step 5 (exponentially small, lossy is
     free);
  3. divide by `g_{k*}` and feed step 7's `log g_{k*}` -- giving
     `<4_1>_N = c_sigma N^{3/2} e^{N Vol/2pi}(1 + o(1))`;
  4. `hc`, already algebraically proved in `OneLoopPrefactorInvariance.lean`;
     then `htau`.

---

## Step 16 -- the assembly specialised at the saddle (`QOU/Knot/KashaevSaddleWindow.lean`)

Three theorems, all `[propext, Classical.choice, Quot.sound]`. Step 15 was
stated for abstract `a`, `L`, `B`; this supplies them:

    kashaevGaussCoeff N k = -pi cot(th_k)/N      kashaevTilt N k = log(2 sin th_k)

`kashaevGaussCoeff_pos` -- `a > 0` exactly when `th_k > pi/2`, which is why the
summand is a Gaussian and not a growing exponential. `angle_mem_window` lets
ONE pair of angular bounds (`M` on `1/sin^2`, `K` on `|cot|`, both on
`[th_{k-W}, th_{k+W}]`) serve every `k'` in the window, via
`Set.uIcc_subset_Icc`. `B` stays abstract -- it need only dominate step 10's
per-pair bound, and computing an explicit maximum is caller-side arithmetic.

### The hypotheses ARE satisfiable, from N = 79

Probe part (i). Five Nat/real side conditions interact
(`W <= k`, `1 <= k-W`, `k+W < N`, `pi/2 < th_k < pi`) and with `k = floor(5N/6)`,
`W = floor(N^0.6)` the binding one is `k + W < N`: it needs `N^0.6 < N/6`,
i.e. `N^0.4 > 6`, i.e. `N > 6^2.5 = 88.2`. The probe finds the actual first N
by search (79 -- floor effects make it slightly under the continuous estimate)
and asserts every smaller N fails, so a later edit cannot move the threshold
silently.

### M and K converge to 4 and sqrt3 -- but only at rate N^-0.4

    N        M      (M-4) N^0.4     K     (K-sqrt3) N^0.4
    241   26.4907     201.75     5.0488       29.75
    3841   6.3241      63.10     2.3074       15.62
    61441  4.5922      48.74     1.8953       13.44

The window's angular half-width is `pi W/N ~ pi N^-0.4`, and
`1/sin^2(5pi/6 + eps) = 4(1 + 2 sqrt3 eps)`, so `(M-4) N^0.4 -> 8 sqrt3 pi =
43.53`. Observed 48.74 at N = 61441 and still descending. **This is slow**: M
is 5.13 at N = 15361. It does not threaten the limit, but it is why the
finite-N bound of step 15 is so far from sharp.

### Two thresholds I guessed wrong, both caught by the probe

`M < 5` at N=15361 (actual 5.13) and `K < 1.85` at N=61441 (actual 1.90). Both
were my invented tolerances, not the mathematics. Replaced by the rate check
against the derived constant `8 sqrt3 pi`, which cannot drift.

### Remaining before `hc`

  1. the region OUTSIDE the window, via step 5 (exponentially small there, so
     step 5's lossy constants are free);
  2. divide by `g_{k*}` and feed step 7's `log g_{k*}`, giving
     `<4_1>_N = c_sigma N^{3/2} e^{N Vol/2pi}(1 + o(1))`;
  3. `hc` -- already algebraically proved in `OneLoopPrefactorInvariance.lean`;
     then `htau`.

---

## Step 17 -- everything outside the window (`QOU/Knot/KashaevBeyondWindow.lean`)

Three theorems, all `[propext, Classical.choice, Quot.sound]`.

    sum_kashaevProd_right_beyond_le : sum_{k > k*+W} g_k
        <= N g_{k*} exp(-sqrt3 pi (W+1)W/N)
    sum_kashaevProd_left_beyond_le  : sum_{w <= k < k*-W} g_k
        <= N g_{k*} exp(-pi (W+1)W/(sqrt3 N)),   for 2N <= 3w

`mul_pred_le_of_le` (`d(d-1) >= (W+1)W` for `d >= W+1`) is what turns step 5's
per-index tail into a uniform one.

**card x largest term, not a geometric sum.** A geometric sum would give
`e^{-cW^2/N}/(1 - e^{-cW/N})` instead of `N e^{-cW^2/N}`; the exponential
crushes both, and `Finset.sum_le_card_nsmul` costs three lines where the
geometric series costs thirty. The region has to beat `sqrt(N)`, not `N`.

### The two directions are not symmetric, and the LEFT is the slow one

    exponent coefficient:  right  sqrt3 pi = 5.441
                           left   pi/sqrt3 = 1.814

A factor 3, because step 5's lower bound uses a SECANT chord where the upper
bound uses the TANGENT, and the secant is shallower. Probe part (iii), the
bounds relative to the main term `3^(-1/4) sqrt(N)`:

    N        right/sqrtN    left/sqrtN
    241        2.03e-06      7.88e-02
    3841       2.98e-11      4.85e-03
    1e6        3.45e-35      3.26e-10

Both vanish; the left one is the binding constraint at small N.

### The region below 2N/3 is not a problem at all

Neither tail bound covers `k < 2N/3` (the secant chord is invalid there), so
`KashaevTailBound`'s much cruder machinery has to. Probe part (iv) measures
what is actually there:

    N      sum_{k < 2N/3} g_k / (g_{k*} sqrt N)
    241            4.28e-13
    961            4.57e-47
    3841           4.63e-182

`g_k` collapses so fast below the saddle that this region is beyond
irrelevant. The crude constants there cost nothing -- I had expected `O(1)`
relative to `g_{k*}` and it is `1e-180`.

### Remaining before `hc`

  1. add the three regions to the window: `<4_1>_N = window + right + left +
     below`, giving `<4_1>_N / (g_{k*} sqrt N) -> 3^(-1/4)`;
  2. feed step 7's `log g_{k*}` to convert that into
     `<4_1>_N = c_sigma N^{3/2} e^{N Vol/2pi}(1 + o(1))`;
  3. `hc` -- already algebraically proved in `OneLoopPrefactorInvariance.lean`;
     then `htau`.

---

## Step 18 -- THE WHOLE SUM (`QOU/Knot/KashaevFullSum.lean`)

Two theorems, both `[propext, Classical.choice, Quot.sound]`.

    kashaev_split : range N = [0,w) + [w,k*-W) + [k*-W,k*+W] + (k*+W,N)

    abs_kashaev_sub_model_le :
      | <4_1>_N - g_{k*} e^{L^2/a} sqrt(pi/a) |
        <= g_{k*} ( window + below + left + right )

Only the window carries any of the constant; the other three are error terms.

### THE HEADLINE

Probe part (iii) -- the FULL invariant, every term of `sum_{k<N} g_k`:

    N        <4_1>_N/(g_{k*} sqrt N)   gap to 3^(-1/4)   gap x N
    241          0.762080560081          2.2449e-03       0.5410
    961          0.760394709201          5.5902e-04       0.5372
    3841         0.759975304786          1.3962e-04       0.5363
    15361        0.759870581895          3.4896e-05       0.5360

against `3^(-1/4) = 0.759835685652`. `gap x N` is constant to three digits, so
the convergence is clean `O(1/N)`.

Step 12 reached `3^(-1/4)` from the Gaussian model; step 15 from the window
sum; **this is the whole thing**.

### Which error binds -- and the answer is not the obvious one

Probe part (iv), relative to the main term (which GROWS like sqrt(N), so
absolute sizes mislead):

    N       window/model   below/model   left/model    right/model
    961       5.83e+03      5.70e-01      3.22e-02      2.03e-08
    3841      7.35e+01      2.82e-01      6.38e-03      3.91e-11

The window dominates at both, and asymptotically stays dominant:

    window/model ~ B ~ M pi^2 W^3/(3N^2) ~ 13.2 N^-0.2   (cubic-limited)
    below /model ~ (24 sqrt3/pi)/(3^-1/4 sqrt N) ~ 17.4 N^-0.5
    left, right  ~ sqrt(N) exp(-c N^0.2)

**The `below` bound is CONSTANT in N** -- `24 sqrt3/pi = 13.2` in absolute
terms. It vanishes only because the main term grows. Its TRUE size is `~1e-47`
(step 17 probe), so it is loose by about 48 orders of magnitude; that costs
nothing only because the window is looser still. If `B` were ever sharpened
past `N^-0.5`, this term would become the bottleneck and would have to be
redone.

### Where the whole theorem becomes usable

Probe part (i): every side condition first holds at **N = 81** (search, with
every smaller N asserted to fail). The binding one is again `k + W < N`.

### Remaining before `hc`

  1. feed step 7's `log g_{k*}` into step 18 to convert
     `<4_1>_N / g_{k*} -> 3^(-1/4) sqrt(N)` into
     `<4_1>_N = c_sigma N^{3/2} e^{N Vol/2pi}(1 + o(1))`;
  2. `hc` -- the algebra is already proved in
     `OneLoopPrefactorInvariance.lean` (`c^2 |cot th| = (2 sin th)^2` is
     "Stirling factor squared over Gaussian width"); what step 18 supplies is
     the Gaussian width, and step 7 the Stirling factor;
  3. `htau`.

---

## Step 19 -- `<4_1>_N` with no `g_{k*}` left in it (`QOU/Knot/KashaevAsymptoticBounds.lean`)

Three theorems, all `[propext, Classical.choice, Quot.sound]`. Step 18 gives
`<4_1>_N = g_{k*}(model +- err)`; step 7 gives `log g_{k*}`. Combined:

    e^{P-E}(model - err) <= <4_1>_N <= e^{P+E}(model + err)

with `P = peakLogMain N`, `E = peakLogErr N`. The peak term is gone.

`P` is where the volume enters: `-(2/pi)Lambda(5pi/6) = Vol(4_1)/2pi`, so `P`'s
first term is `N Vol/2pi`.

### The headline in final form

Probe part (ii):

    N       e^P model / (N^{3/2} e^{N Vol/2pi})    gap        gap x N
    241            0.793267141197              3.343e-02      8.057
    3841           0.761900986929              2.065e-03      7.933
    61441          0.759964672874              1.290e-04      7.925

against `3^(-1/4) = 0.759835685652`, `Vol/2pi = 0.323065947219`. Clean `O(1/N)`.
(Step 18's headline had constant 0.536; this one uses the MODEL and step 7's
MAIN term rather than the true values, so the constants differ.)

### WHERE THE LOWER BOUND ACQUIRES CONTENT -- and it is late

`err <= model` is a hypothesis of `kashaev_bounds_of_model`, and without it the
lower bound is negative and says nothing. Probe part (iii):

    N        W = N^0.6   err/model     best W   best err/model
    1e4         251        19.4346       213         7.3234
    1e5         999         3.6636       927         2.4511
    1e6        3981         1.4522      3001         0.4996

**With `W = N^0.6` the condition holds at no `N` tested.** Optimising `W` beats
it everywhere and brings the threshold to `N = 1e6`. The exponent 0.6 is
convenient for step 13's TAIL analysis; it is not the choice that makes the
lower bound usable soonest, because the cubic remainder wants a SMALLER window
than the tail does and the balance point moves with `N`. (`W = N^0.6` should
come good near `N ~ 1e7`.)

So the honest state: the UPPER bound is unconditional; the LOWER bound is a
theorem whose hypothesis is first satisfiable around `N = 1e6` with a tuned
window. The limit statement is untouched by this -- it is the finite-`N`
content that arrives late.

### Three guessed thresholds in a row, all wrong

`M < 5` (step 16), `K < 1.85` (step 16), `gap < 1e-4` and `threshold = 1e5`
(here). Every one was a tolerance I invented rather than derived, and every one
was caught by the probe failing. The fix each time was the same: assert the
RATE against a derived constant (`8 sqrt3 pi`, `gap x N` settling) instead of
an absolute number. Worth doing that first next time.

### Remaining before `hc`

Only `hc` and `htau` now.

`hc : c^2 |cot th| = (2 sin th)^2` is already proved as ALGEBRA in
`OneLoopPrefactorInvariance.lean`. What steps 7-19 supply is its two
ingredients at the Kashaev saddle: the Stirling factor `2 sin th_{k*}` (step 7,
inside `P`) and the Gaussian width `sqrt(pi/a) = sqrt(N/|cot th*|)` (steps
12-19, inside `model`). Writing `c_sigma = 2 sin th* |cot th*|^{-1/2}` and
squaring gives `hc` directly.

---

## Step 20 -- `hc` DERIVED (`QOU/Knot/KashaevCSigma.lean`)

Five theorems, all `[propext, Classical.choice, Quot.sound]`. **This bean's
first half is done.**

`OneLoopPrefactorInvariance` proved the algebra downstream of the saddle from a
HYPOTHESIS `hc : c^2 |cot th| = (2 sin th)^2`, and its header recorded that
nobody had derived it. It is now derived.

The whole content is that steps 7-19 produce the constant in a specific SHAPE:

    c_sigma(th) = (2 sin th) * |cot th|^{-1/2}
                     ^                ^
              Stirling factor   Gaussian width

the first from step 7's `log(2N sin th_{k*})`, the second from steps 12-19's
`sqrt(pi/a)` at `a = pi|cot th|/N`. Square it, multiply by `|cot th|`, and the
Hessian cancels. **`hc` is not a fact about `4_1`** -- probe part (i) checks it
at 199 angles across `(0, pi)`, worst relative error `4.8e-51`. It is the
statement that a Laplace constant is a Stirling factor over a square-rooted
Hessian, which is what every Laplace constant is.

`stirling_mul_gaussWidth` is the link back to the analysis:
`(2N sin th) sqrt(pi/a) = c_sigma(th) N^{3/2}` exactly.

`cSigma_saddle_pow_four` and `k_sq_eq_half` re-prove
`OneLoopPrefactorInvariance`'s conclusions with `hc` SUPPLIED rather than
assumed. So the chain from the Kashaev sum to `c_sigma = 3^{-1/4}` no longer
passes through an assumption.

### The loop closes

Probe part (iv) -- the DERIVED value against the MEASURED asymptotics:

    N        <4_1>_N/(N^{3/2} e^{N Vol/2pi})   c_sigma(5pi/6)      gap
    961            0.76027461955642           0.75983568565159   4.39e-04
    3841           0.75994536766618           0.75983568565159   1.10e-04
    15361          0.75986310295666           0.75983568565159   2.74e-05

and exactly:

    c_sigma(5pi/6) = 1/sqrt(sqrt 3) = 3^(-1/4) = 0.75983568565159
    c_sigma(5pi/6)^4 = 1/3
    k = c_sigma sqrt(|cot|/2) = 0.70710678118655,  k^2 = 1/2

### A stale header, corrected

`OneLoopPrefactorInvariance.lean` said "nobody has yet derived `hc` and `hτ`".
True when written, half out of date now. Updated in the same change, with the
old wording and the date recorded rather than silently replaced -- the same
discipline applied to that file's earlier "not formalised" claim.

### Remaining

**`htau` only.** `|tau_DG| = |cot th*|/2` is the other output of the saddle;
`k_sq_eq_half` already shows the Hessian cancels between `c_sigma` and `|tau|`
before it is evaluated, so what is missing is the identification of `tau` with
the Hessian, not any further analysis of the Kashaev sum.

---

## MERGED. 2026-08-09 — PR #4729, merge commit `25387e2a4`

The `hc` half of this bean is **on `main`**. 15 Lean files, 14 probes, all
sorry-free (`#print axioms` -> `[propext, Classical.choice, Quot.sound]`,
re-verified in an error-free file immediately before merge -- see the "false
isolated success" note above for why that qualifier is load-bearing).

`OneLoopPrefactorInvariance`'s `hc` is no longer a hypothesis anywhere in the
chain from the Kashaev sum to `c_sigma = 3^(-1/4)`:

    cSigma_sq_mul_abs_cot     c^2 |cot th| = (2 sin th)^2   -- ANY th with cot != 0
    cSigma_saddle_pow_four    c_sigma(5pi/6)^4 = 1/3        -- hc discharged
    k_sq_eq_half              k^2 = 1/2                     -- hc discharged

PR #4729's title and body were **rewritten before merging**. They claimed "the
raw-float64 ratchet goes green -- 0 NEW, 0 REGRESSED", true when written and
false against the main of 2026-08-09; and they did not mention this arc at all,
which by then was most of the branch. The old wording is recorded in the new
body rather than replaced. See `qou-mnrd` for the ratchet's live state.

## Bean stays OPEN — `htau` only

Nothing about `htau` changed. It is **not** one more step of this arc:
`tau_DG` has no Lean definition to bridge to, `QOU.OneLoopEdgeLattice`'s own
header says nothing there "proves that the multi-cusp construction computes the
adjoint torsion", and `|tau(4_1)| = sqrt3/2` is in this corpus a SnapPy
computation (`computations/one_loop_torsion.py`), DG's own worked example.
Whoever picks it up needs the 1-loop invariant formalised first; the target is
already pinned in Lean as `abs_cot_saddle_div_two` so the gap is a definite
claim rather than prose.



Also known as `qou-fybg` (its former front-matter header id; the beans CLI uses the filename id `fybg`). Recorded 2026-10-04.

### Progress (Round 74 — PR litlfred/qou#8322)
- Formalized in PR `litlfred/qou#8322` (`feat/round74-kashaev-stokes3-stokesamp-ohtsukinz-pauli-43c1`, Commit 1 `82ec77a3b69cc6d79a85c01e64b63d422fa51c45`, Head `d13ffedea3175ba61da12a5b2abf5cf08d471608`, `scriptHash: 79ed375a0246`).
