---
# qou-08xc
title: Wire Lean-proved kappa=3/16 correction into Deuteron gap compute
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T02:21:41Z
updated_at: 2026-11-15T21:40:00Z
parent: qou-10v9
---

## 2026-11-15 — Unified 3-way reconciliation of `κ = 3/16` on the deuteron (`²H`, `pn`) (owner ruling `Q-10V9-2 = 1`, PR `litlfred/qou#7991`, commit `bb48975072`)

Added `QOU/MassTheory/DeuteronKappaThreeSixteenthsReconciliation.lean` (wired into `QOU.lean`, sorry-free) and companion probe `computations/probes/deuteron_kappa_three_sixteenths_reconciliation_probe.py` (33/33 assertions pass) reconciling all three appearances of `κ = 3/16` (and `±1/16`) across the deuteron and Borromean 3-strand binding corpus:

1. **Route 1 — Borromean 29-letter Laurent-trace coefficients on `H_{3A}` (`PairwiseChainLeadingOrder`, `LeadingOrderTraceCoefficient`, `qou-qqm4`):**
   - At first order in `ℏ_q`, `c₁(pp) = 1/8`, `c₁(pn) = 1/16`, `c₁(nn) = 0`, so the `³He` and `⁴He` pairwise chain sums equal `c₁(pp) + c₁(pn) = 3/16 = κ` (from `3(a+b)/16` at Borromean weights `(a,b) = (3,-2)` with `a+b = 1`), whereas the deuteron (`pn`) alone has `c₁(pn) = 1/16 = κ/3` (`route1_deuteron_c1_reconciliation`).
   - At second order in `ε = q - 1` (`|S| = 2` pair-class split, `qou-qqm4`), the `A = 3` intra-nucleon slope is `intra(Z,N) = (Z - N) · κ` with `κ(3) = 3/16` (`route1_intraA3_values`, vanishing at `Z = N = 1`), while the deuteron cross-nucleon term is `cross(pn) = -3/16 = -κ`, partially cancelled by the nucleon–interface term `n-if(pn) = +1/8 = +2/16` to give the net `|S| = 2` contribution `-1/16 = -c₁(pn)` and total `c₂(pn) = 25/32` (`route1_deuteron_S2_reconciliation`).
2. **Route 2 — Yekutieli / Family-A Borromean `h²` extraction (`κ_Yek = 3/16`) vs standard Kauffman–Jones (`κ_std = 0`) (`BorromeanMarkovTrace`, `qou-pi4m`):**
   - Under `[2]_q² = 4 + h²`, the `1 + h²/4` factor in `V(𝓑₃) = 4 + h² - 3h⁴ - h⁶` cancels (`κ_std = 0`, `route2_standard_h2_vanishes`).
   - Under `(√q + 1/√q)² = q + 2 + q⁻¹ = w² + 4` (`w = q^{1/2} - q^{-1/2}`, `h² = w²(w² + 4)`), the denominator slope shifts from `1/4` to `1/16`, producing `κ_Yek = 1/4 - 1/16 = 3/16` (`4 · κ_Yek = 3/4` in Family A) as an exact polynomial identity in `w` (`route2_yekutieli_h2_mul`, `route2_yekutieli_h2_is_three_sixteenths`, `route2_yekutieli_kappa_unique`).
3. **Route 3 — Discretized Yekutieli surface 2-form on the deuteron `pn` braid `σ₁³` (`YekutieliTrefoilDiscretization`, `qou-prjo`):**
   - The right-handed trefoil Seifert matrix `V = [[-1, 1], [0, -1]]` has unit skew intersection `V_{01} - V_{10} = 1` (`route3_trefoil_seifert_skew_unit`), supplying the framing- and color-dressing-invariant operator carrier `1 · ⁅A_0, A_1⁆` (`route3_trefoil_operator_carrier`).

