---
# qou-9ohz
title: 'PERF: per_generator_V_hat_3A -- one mpf coefficient forces an object-dtype O(dim^3) matmul; the word collapses to alpha*sigma+beta'
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T18:57:13Z
updated_at: 2026-08-24T18:58:31Z
---

MEASURED 2026-08-24, branch claude/excise-convention-c-2026-08-24.

## Symptom
`computations/binding_via_interface_knot.py` appears to hang. It does not:
`py-spy dump` on the live PID and on an independent probe caught BOTH at the
same line, in mpmath scalar arithmetic:

    per_generator_V_hat_3A (computations/mass_at_3A_proper.py:757)
        __mul__ (mpmath/ctx_mp_python.py:275)

Line 757 is `M = M @ (c * sigmas[i] + d * I_lam)`.
CPU-bound, 89 MB RSS of 16 GB, no swap. The `>12 GB RAM` comment in the file
is a 4He concern and is NOT what is happening here.

## Root cause -- dtype contamination, not algorithmic cost
The seminormal matrices are float64 and cheap: all 30 partitions of 9 build in
0.08 s, dims <= 216. The braid word coefficients are NOT uniformly typed:

    type histogram (c,d): {(int,mpf): 17, (int,int): 16, (mpf,mpf): 2}
      gen 0: steps=7 first_mpf_at=4   gen 1: steps=4 first_mpf_at=0
      gen 2: steps=1 first_mpf_at=0   gen 3: steps=7 first_mpf_at=3   ...

19 of 35 steps carry an mpf and every generator hits one by step 0-4, so
`mpf * float64_array` promotes to dtype=object and the rest of the chain is a
Python-level triple loop instead of BLAS: ~60M mpf mul+add per word-step sweep
over lambda |- 9.

Scaling check: D (n=6, sum dim^3 ~ 2e4) = 0.58 s; T (n=9, sum dim^3 ~ 6e7) is
~3000x that ~ 29 min. Observed: 20+ min and still running. Consistent.

## Fix -- exact scalar collapse, NOT a float64 cast
Within one generator every factor is a polynomial in the SAME sigma_i, so they
commute, and sigma_i obeys the Hecke quadratic relation. VERIFIED, not assumed:

    (3,2,1)     sigma^2 = (q-1/q) sigma + 1 : max|diff| = 6.661e-16   OK
    (4,3,1,1)   sigma^2 = (q-1) sigma + q   : max|diff| = 1.992e-01   NO
                eigenvalues [-0.90091828, 1.10997858] = [-1/q, q]

So the product collapses to W_i = alpha*sigma_i + beta*1 by a scalar mpf
recursion, and chi_lambda(W_i) = alpha * tr(sigma_i^lambda) + beta * dim.
tr(sigma_i^lambda) is a diagonal sum of ONE matrix, O(dim), computed once.
No matmul, no precision given up.

    (alpha,beta) * (c,d):  alpha` = alpha*c*(q-1/q) + alpha*d + beta*c
                           beta`  = alpha*c + beta*d

## Verification
    D: matmul 0.611s   reduced 0.001s   max|diff| = 9.107e-16
       matmul : +0.671385824 +1.055110319 +0.000071902 +0.551656055 +1.088367533
       reduced: +0.671385824 +1.055110319 +0.000071902 +0.551656055 +1.088367533
    T: reduced 0.099s   (vs the 20+ min matmul run)

Caveats, stated because they are not yet closed:
  * T / 3He equality is still verifying against the slow path in the
    background. D is confirmed; T is NOT yet.
  * 9.1e-16 is float64 round-off because `_cached_seminormal` returns float64
    on this path. The reduction is exact; it does not by itself make this path
    high-precision, and it must not be reported as if it did.
  * Whether this unblocks 4He (n=12) is NOT established. The reduction removes
    the matmul but still asks for sigma_i per lambda; a closed-form axial-
    distance diagonal would remove that too, and has not been checked.

## Overlap
Main`s qou-fmoi sparse-chi_lambda work (97-186x) does not touch
mass_at_3A_proper.py. Commit 6b21956c23 hit the same mpf-contamination class in
chi_lambda_of_word. Adjacent, not duplicate.

## Next
Patch mass_at_3A_proper.py:746-763 once the T/3He confirmation lands. Worth
doing before the qou-37xc baseline campaign resumes -- that campaign is itself
paying this cost.
