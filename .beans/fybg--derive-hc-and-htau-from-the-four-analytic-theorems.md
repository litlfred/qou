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
updated_at: 2026-08-09T00:00:00Z
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
