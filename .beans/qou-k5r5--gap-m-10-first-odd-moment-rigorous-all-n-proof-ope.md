---
# qou-k5r5
title: 'GAP: M_1>0 (first odd moment) — rigorous all-n proof OPEN; identity Lean-proved, Kerov-CLT gives asymptotic only'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:10:21Z
updated_at: 2026-08-21T16:16:10Z
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
