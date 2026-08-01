---
# qou-l15q
title: 'GAP (arc successor to qou-bbsy): derive A_omega = 3 structurally. W3 certified A_omega is the Stokes SYMMETRY CONSTANT (S12+S21 = 3*S11, exact q-series identity, Lean StokesSymmetryConstant). Deriving the integer 3 from the categorical drivers is open. TWO competing structural candidates, both fitting 4_1, SHARPLY SPLIT on 5_2 -- a clean discriminating test: (A) |disc(trace field)|: 4_1 -> |-3| = 3 (Lean-proved in CuspShapeBarParity: (barOdd omega)^2 = -3); 5_2 -> |-23| = 23 (Lean-proved in FiveTwoSaddleCurve: cubic y^3-2y^2+3y-1, disc -23). (B) |middle coefficient of the Alexander polynomial|: Delta_41 = -t + 3 - 1/t -> 3; Delta_52 = 2t - 3 + 2/t -> 3. So A predicts 23 for 5_2 and B predicts 3. TEST: compute the 5_2 Stokes symmetry constant c in S12 + S21 = c*S11 from GGM 2012.00062 section 6 (corpus already has 5_2 Stokes work: qbeta-5two-stokes-barodd-index, qbeta-5two-stokes-population-bridge, fivetwo_saddle_values). c = 23 confirms A; c = 3 confirms B; anything else kills both. NOTE the guard discipline: 5_2 entry series are pre-asymptotic below ~q-order 1200 at the substrate -- use a multi-cut ladder, diff >= 1 means ZERO digits. Anti-fit: this is a structural identification test with a falsifiable prediction, NOT a fit; if neither matches, report the negative.'
status: todo
type: task
created_at: 2026-08-01T20:20:55Z
updated_at: 2026-08-01T20:20:55Z
---

