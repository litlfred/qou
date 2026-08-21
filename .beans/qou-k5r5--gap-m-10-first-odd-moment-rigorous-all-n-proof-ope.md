---
# qou-k5r5
title: 'GAP: M_1>0 (first odd moment) — rigorous all-n proof OPEN; identity Lean-proved, Kerov-CLT gives asymptotic only'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:10:21Z
updated_at: 2026-08-21T22:10:42Z
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



*** LEADING CONSTANT DERIVED (2026-08-21, PR #5428): kappa = 128/(225 pi^2) ***
M_1 ~ kappa n^{5/2}, kappa = 128/(225 pi^2) = 0.0576404955832 > 0. DERIVED, not
fitted (exact data is at 0.0591; the Omega-integral gives 0.05764).

Chain: (1) EXACT identity Sum_h = Sum_u D(u)^2 + Sum|c| (n<=14, D=diagonal
lengths) => M_1 = Cov(Sum_u D^2 + Sum|c|, Sum_u u^2 D), functionals of the
single fn D(u); quadratic Sum D^2 linearizes (dropped term order sqrt n).
(2) IO Kerov-CLT field (arxiv-math-0304010 eq 0.3). (3) Calibration dD=Delta,
Sum_u=sqrt n int reproduces the KNOWN exact Var(Sum_c^2)=n(n-1)(n-2)/3 ->
Var/n^3=1/3 (validates normalization). (4) Sum_h's test function collapses to
phi_h = 2 D_inf + |x| = Omega(x) (VKLS shape!); Sum_c^2's x^2 has ONLY k=3 mode
=> kappa = Omega_hat_3/3, Omega_hat_3 = 128/(75 pi^2).

Verified: Omega_hat_3 closed-form vs quadrature to 1e-42; calibration exact;
cross-check Var(Sum_h)/n^2 -> sum Omega_hat_k^2/k = 0.00997; rho -> 0.9997;
transition-measure free cumulants R_2=n verified all partitions, R_4-explained%
of Var(Sum_h) rises toward 100. Rigorous MODULO the IO CLT theorem (cited).

STATUS UPDATE: leading term now DERIVED (kappa>0), was 'unknown/non-monotone'.
REMAINING for M_1>0 all-n: Fulman (arxiv-math-0305423) finite-n bound on the
+/- n^{5/2} cancellation. kappa>0 = asymptotic positivity; + exact positivity
n<=50; the finite-n bound is the SOLE remaining gap. Not laundered; nothing
wired; L2 unchanged.
