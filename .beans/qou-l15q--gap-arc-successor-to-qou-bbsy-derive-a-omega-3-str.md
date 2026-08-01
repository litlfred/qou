---
# qou-l15q
title: 'GAP (arc successor to qou-bbsy): derive A_omega = 3 structurally. W3 certified A_omega is the Stokes SYMMETRY CONSTANT (S12+S21 = 3*S11, exact q-series identity, Lean StokesSymmetryConstant). Deriving the integer 3 from the categorical drivers is open. TWO competing structural candidates, both fitting 4_1, SHARPLY SPLIT on 5_2 -- a clean discriminating test: (A) |disc(trace field)|: 4_1 -> |-3| = 3 (Lean-proved in CuspShapeBarParity: (barOdd omega)^2 = -3); 5_2 -> |-23| = 23 (Lean-proved in FiveTwoSaddleCurve: cubic y^3-2y^2+3y-1, disc -23). (B) |middle coefficient of the Alexander polynomial|: Delta_41 = -t + 3 - 1/t -> 3; Delta_52 = 2t - 3 + 2/t -> 3. So A predicts 23 for 5_2 and B predicts 3. TEST: compute the 5_2 Stokes symmetry constant c in S12 + S21 = c*S11 from GGM 2012.00062 section 6 (corpus already has 5_2 Stokes work: qbeta-5two-stokes-barodd-index, qbeta-5two-stokes-population-bridge, fivetwo_saddle_values). c = 23 confirms A; c = 3 confirms B; anything else kills both. NOTE the guard discipline: 5_2 entry series are pre-asymptotic below ~q-order 1200 at the substrate -- use a multi-cut ladder, diff >= 1 means ZERO digits. Anti-fit: this is a structural identification test with a falsifiable prediction, NOT a fit; if neither matches, report the negative.'
status: todo
type: task
created_at: 2026-08-01T20:20:55Z
updated_at: 2026-08-01T20:20:55Z
---


## 2026-08-01 TEST RE-SCOPED before running (corpus read first)

The 4_1 -> 5_2 test as designed is ILL-POSED. The corpus already carries
the 5_2 Stokes machinery (qbeta_5two_stokes_barodd_index_probe.py, GGM
section 6): the 5_2 Stokes matrix is **3x3**, q->0 limit
[[1,4,0],[0,1,0],[-3,-9,1]] (eq 100a), with THREE off-diagonal integers
(4, -3, -9) -- versus 4_1s 2x2 [[1,3],[0,1]] with ONE (3). Rank tracks the
trace-field degree (4_1 quadratic, 5_2 cubic). So:

  * there is no single 5_2 Stokes constant to compare against 23 or 3;
  * the symmetry eq (65) that gave the 4_1 identity is a rank-2 statement
    with no 3x3 analogue -- GGMs 5_2 structural relation is the inversion
    S+^T S- = 1, which constrains a matrix PAIR, not an integer.

23 does not appear among {4,-3,-9}, but that is NOT a refutation of
candidate A (the predicted quantity is undefined here). 3 does appear as
|-3|, but that is NOT support for candidate B -- picking one of three
integers post hoc is numerology. Both candidates remain UNTESTED.

NEXT (recommended, route 3 of the scope note): re-run the same falsifiable
test on a different RANK-2 knot -- quadratic trace field, so the Stokes
constant is well-defined exactly as for 4_1 -- chosen so that
|disc| != |Alexander middle coeff| and the candidates still separate.
Cheapest well-posed route; does not require closing the rank>2 channel gap.

Scope note: docs/scope/2026-08-01-aomega-three-test-illposed.md
