---
# qou-h315
title: 'EPIC: analytic machinery to discharge the M1>0 (CS)-margin input (hCS)'
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T01:33:54Z
updated_at: 2026-10-04T15:15:15Z
parent: qou-m6dn
---

Machinery to discharge the M1>0 (CS)-margin input hCS (sigma_D < rho_P*sigma_A for n>=N0<=79).
Reduction skeleton PROVED: YoungDiagramKernelCSMargin.m1_pos_all_of_cs_inputs (sorry-free).

ACCURATE INVENTORY (corrects earlier 'Mathlib lacks it' over-claim): Euler-Maclaurin with explicit
remainder EXISTS sorry-free (QOU/MathlibExt/CompositeEulerMaclaurin, |R|<=k h^5 M/720; CorrectedTrapezoid);
Gaussian tail/sum bounds EXIST (GaussianTailBound/GaussianSumBound/...); Lobachevsky/Clausen EXIST.
Shared with c_sigma arc bean qou-mlgp.

ROUTE DECISION = Route 1 (Kerov limit-shape + EM, reuses CompositeEulerMaclaurin), since the kink
cancels (c_{1/2}=0, PR #5939) => smooth integrand => order-2 EM remainder applies. Route 2 (discrete
Bessel-J Olver/Debye asymptotics) is a larger new build with no other corpus consumer.

Tasks: qou-2toh (route: DONE=Route1), qou-8quz (c_{1/2}=0 symmetry proof), qou-tvok (C_A via EM),
qou-po72 (C_W/C_P/C_D), qou-xs2c (de-poissonization const), qou-jh3m (ratio prop -> C -> N0<=78).
Audit: docs/audits/2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md

CORRECTION (2026-08-29): the Route-1 rationale 'kink cancels (c_{1/2}=0, PR #5939) => smooth
integrand' is RETRACTED. The transpose-symmetry argument is invalid (reflection automatic) and the
sub-leading exponent is numerically indeterminate (theta^{-1/2}/-2/3/-5/6/-1 all fit; best single
power ~0.94; a theta^{-5/6} Airy-edge term is plausible). Route 1 still stands (reuses the most infra:
CompositeEulerMaclaurin bulk + Gaussian-bound edge), but qou-tvok must handle the EDGE term explicitly.
qou-8quz (symmetry proof) SCRAPPED/refuted. Robust: correction small => any rate >= theta^{-1/2}
closes (CS) (30-300x headroom).
