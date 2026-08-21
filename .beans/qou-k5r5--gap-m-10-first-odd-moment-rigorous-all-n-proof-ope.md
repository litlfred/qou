---
# qou-k5r5
title: 'GAP: M_1>0 (first odd moment) — rigorous all-n proof OPEN; identity Lean-proved, Kerov-CLT gives asymptotic only'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:10:21Z
updated_at: 2026-08-21T21:50:31Z
---


DULL ANALYSIS EXHAUSTED (2026-08-21). Confirmed exact routes closed:
- M_1 = Cov(Sum lambda_i^2, Sum c^2) [Lean-formalized identity, decide]; Cov(p2*,Sum c^2)=0 exact.
- NO simple closed form: M_1 != poly(n) + {E[ell],E[ell^2],E[lam1],ell*poly} (all exact fits fail n<=19).
- Asymptotic: Cov(Sum h,Sum c^2)/n^{5/2} converges to kappa ~ 0.0591 (exact data n<=28, monotone).
  Close to sqrt(2)/24=0.058926 but data trends slightly above; Richardson float-unstable, exact
  kappa NOT pinned. rho(Sum b,Sum c^2) -> ~0.93.
- Obstruction: M_1 = Cov(S|c|,Sc2)[+] + Cov(S_c h^2,Sc2)[-], partial cancellation of two ~n^{5/2}
  terms, ratio -> -0.62; need ratio > -1 uniformly.
STATUS: asymptotic positivity (kappa>0) numerically overwhelming but NOT rigorously derived. A full
all-n proof needs the Kerov-CLT covariance constant DERIVED (rigorous) + a finite-n error bound
controlling the +/- cancellation -- a genuine analysis project (free-cumulant/transition-measure
machinery), NOT closeable by probe-driven exact computation. No elementary exact route exists.
Recommend: dedicated Kerov-CLT/free-probability effort, or accept asymptotic+exact-finite-check status.
Not resolved; not laundered.



EXACT-ARITHMETIC UPDATE (2026-08-21, PR #5428). Recomputed Cov(Sum_h,Sum_c^2)
in exact Fraction (prior kappa~0.0591 'above sqrt2/24' was a float64
cancellation artifact):
  - leading exponent 5/2 CONFIRMED (a_n -> 2.500).
  - Cov > 0 EXACTLY for all 3<=n<=50.
  - kappa_n NON-MONOTONE: peaks 0.0591961 at n=32, then descends (0.0590862 at
    n=50, still drifting ~-7e-6/step). kappa NOT numerically pinned; sqrt(2)/24
    WITHDRAWN as confirmed (data falls toward it from above but does not settle).
  - Exact identities (Lean-formalizable): 2*Sum_h=p2(lam)+p2(lam');
    p2=Sum(lam_i-i)^2 + 2 Sum i(lam_i-i) + Sum i^2. The middle i-weighted term
    is the non-Lambda* obstruction (why Sum_h not in Lambda*). Leading
    fluctuation bulk-Gaussian (sd~n); edge/TW subleading (~n^{2/3}) = candidate
    source of the non-monotone corrections.
NEXT: kappa is a covariance of two profile linear statistics (Sum_c^2 in
Lambda* <-> R4; Sum_h OUTSIDE Lambda*), needs the IO Gaussian-field kernel
(Sniady 4.5 bulk term + Fulman finite-n bound), NOT more n. Any analytic kappa
must reproduce a NON-MONOTONE approach. Still OPEN; not laundered.
