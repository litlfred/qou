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
updated_at: 2026-08-09T02:00:00Z
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
