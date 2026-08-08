---
# qou-mlgp
title: 'The Mathlib gap that blocks formalising the analytic half of the c_sigma derivation'
status: todo
type: task
priority: normal
tags:
    - lean
    - mathlib
    - c-sigma
    - one-loop
    - formalization-gap
created_at: 2026-08-08T22:20:00Z
updated_at: 2026-08-08T22:20:00Z
---

## What is and is not formalised

`QOU.OneLoopPrefactorInvariance` proves the ALGEBRA of the `c_sigma`
derivation sorry-free: `k_sq_eq_half_of_saddle`, `c_pow_four_eq_third`,
`saddle_forces_cot`, `vdv_c_sigma_iff_tau`, `vdv_tau_sq`,
`vdv_radical_is_gaussian_norm`, plus the `Sigma(2,3,5)` keystone tower.

The ANALYTIC input is assumed, as hypotheses `hc` and `hτ`, and is the whole of
what remains open on this arc:

  (A) the Euler-Maclaurin expansion
      `s_n = (N/pi) Lambda(n pi/N) - (1/2) log(2 N sin(r pi)) + O(1/N)`
      with the CONSTANT, not merely the leading order;
  (B) Laplace's method for a SUM,
      `sum_k e^{phi(k)} ~ e^{phi(k*)} sqrt(2 pi / |phi''(k*)|)`;
  (C) the Lobachevsky function `Lambda(theta) = -int_0^theta log|2 sin x| dx`
      with `Lambda' = -log|2 sin|` and `Lambda'' = -cot`;
  (D) the multivariate Gaussian with complex covariance,
      `int_{R^{n+1}} exp(-pi[A u^2/2 + 2 sum (v_j + u/2)^2]) = 2^{-n/2} sqrt(2/A)`.

## What Mathlib actually has — CHECKED, not assumed

The mathlib package in this repo is cache-only (build artifacts, no `.lean`
source), so this was determined by enumerating the compiled module tree:
`.lake/packages/mathlib/.lake/build/lib/lean/Mathlib`, 6990 modules.

  HAVE     Analysis/SpecialFunctions/Gaussian/GaussianIntegral.olean   -> (D) reachable
  HAVE     Real.cos_pi_div_five                                        -> used already,
           in `golden_quantum_dimension`
  MISSING  polylog / dilogarithm            0 modules
  MISSING  Lobachevsky                      0 modules      -> blocks (C)
  MISSING  Clausen                          0 modules      -> blocks (C)
  MISSING  Euler-Maclaurin                  0 modules      -> blocks (A)
  MISSING  Laplace method / stationary phase 0 modules     -> blocks (B)

So (D) is the only one of the four that Mathlib can currently support, and it is
the one the derivation needs least — it is a two-line change of variables. The
three that carry the actual content, (A), (B) and (C), have no Mathlib basis at
all.

## Why this is a real blocker and not laziness

(C) is the tractable entry point and is worth doing on its own merits:
`Lambda` is an elementary integral, `Lambda' = -log|2 sin|` is FTC, and
`Lambda'' = -cot` follows. It would also be reusable far beyond this corpus —
every hyperbolic-volume computation wants it.

(A) is the hard one. The `s_n` constant is what makes Lemma 3 true, what makes
`c_sigma(4_1) = 3^{-1/4}` come out rather than `3^{-1/4}` times an unknown, and
what the retracted van der Veen premise turned on. A leading-order
Euler-Maclaurin is not enough; the constant term is the entire content.

(B) is where the `sqrt(2 pi / |phi''|)` and hence the `|cot theta*|^{-1/2}` comes
from, i.e. the Hessian that cancels in `k`. Without it, `k_sq_eq_half_of_saddle`
is a theorem about a hypothesis rather than about the colored Jones polynomial.

## Definition of done

Either (C) contributed upstream and (A) stated as a Lean hypothesis with a
citation rather than an inline assumption, or a written decision that the
analytic half stays informal — recorded here, with the reason. Do NOT quietly
leave the Lean reading as though it covers more than it does; the file header and
`prop:one-loop-prefactor-provenance` both say explicitly what is assumed, and
that must stay true.
