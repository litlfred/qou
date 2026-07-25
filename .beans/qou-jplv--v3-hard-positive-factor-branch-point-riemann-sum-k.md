---
# qou-jplv
title: 'V3 (hard): positive-factor branch-point Riemann sum (k<=k*) -> Li2(x)-pi^2/6 for q>1 partition u:1->1/x hitting branch point x=1; adapt DilogPartAConvergence h(u) machinery (integral_zero_one_eq_LiTwo, riemann_error_bound, tail_bound) to the u>1 side with integrable log singularity'
status: in-progress
type: task
priority: normal
created_at: 2026-07-25T03:17:08Z
updated_at: 2026-07-25T11:29:12Z
---


## 2026-07-25 V3 sub-obstacle breakdown (formalize-first scoping)

W-P1: `-(1-q)Sum_{k<=k*} log(1-x q^k) -> Li2(x) - pi^2/6` for the q>1 side, where
the u=q^k partition runs u: 1 -> 1/x hitting the branch point x*u=1. Decomposition
(each a distinct Lean sub-brick):

1. **Proper target integral (interior).** `int_1^b -log(1-xu)/u du = Li2(xb)-Li2(x)`
   for `b < 1/x` (so `xb<1`, no branch point). Change of variables t=xu (pattern of
   `integral_zero_one_eq_LiTwo`) + `LiTwo_eq_integral` (DilogReflection:377) +
   `integral_add_adjacent_intervals`. **Sub-obstacle:** interval-integrability of
   `-log(1-t)/t` across the removable t=0 point on [0,x] and [x,xb] — Part A's
   DilogReflection proof establishes this internally; check if it is exposed as a
   reusable `intervalIntegrable` lemma, else port it.
2. **Improper limit b -> 1/x^-.** `Li2(xb)-Li2(x) -> Li2(1)-Li2(x) = pi^2/6-Li2(x)`
   as b->1/x (i.e. xb->1^-). Needs continuity/limit of `LiTwo` at 1 from below
   (LiTwo is a tsum; `LiTwo_one` gives the value, need left-continuity or Abel).
3. **Variable-term Riemann sum.** The positive-factor sum has k*=floor(log_q(1/x))
   terms; the count jumps with q. Adapt Part A's `riemann_error_bound` telescoping
   squeeze to the q>1 "going up" partition [q^k, q^{k+1}] with widths q^k(1-q)<0
   (sign flip) and the growing integrand near 1/x. This is the genuine analytic
   core; the survey (2026-07-25) mapped the ~8 reusable Part-A lemmas with the
   flipped positivity hypothesis `b < 1/x`.
4. **Assembly -> W-P1** then **V4** (combine W-P1 + W-P2 (#4191, DONE) + #4173
   per-factor split into reg_n -> Li2(x)-pi^2/3).

Unlike W-P2 (closed via Tannery, no improper integral), V3's improper branch-point
integral + variable term count is irreducible analytic work — a focused session.
