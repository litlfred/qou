---
# qou-a5l8
title: 'Lean-prove Gap 3 & 4: Project Borromean V^3 Two-Term Trace onto Central Idempotents e_(3) and e_(2,1)'
status: completed
type: task
priority: high
created_at: 2026-11-18T20:58:52Z
updated_at: 2026-11-18T21:15:24Z
parent: qou-7xl8
---

Close Gaps 3 & 4 in the categorical mass derivation by welding Route 1 (`NucleonWeightSpaceTwoTerm.lean`) and Route 2 (`NucleonIdempotentModifiedTrace.lean`):
1. Prove that `e3p` and `e21p` commute with `A₁Inv`, `A₂Inv`, `borromeanVA`, and `borromeanV3A` (and `e3n`, `e21n` commute with `B₁Inv`, `B₂Inv`, `borromeanVB`, `borromeanV3B`).
2. Prove `trace_e3p_borromeanV3 : trace (e3p q * borromeanV3A q) = 1` and `trace_e3n_borromeanV3 : trace (e3n q * borromeanV3B q) = 1` (the `I=3/2` decuplet trace on the Borromean link is identically `1` for all `q`).
3. Prove `trace_e21p_borromeanV3` and `trace_e21n_borromeanV3`: on the pure 2D `I=1/2` nucleon sector `e_(2,1)`, `trace (e21p q * borromeanV3A q) = -(q^4 - q^2 + 1)*(q^8 - 2*q^6 - 2*q^2 + 1) / q^6` (`= 2` at `q=1`, so `(q - q⁻¹) * tr(e_(2,1) V³) = 2h + O(h³) ≈ 4 ln q`).
4. Prove the exact `e_(2,1)`-projected electromagnetic adjacent-crossing traces `trace_e21p_QAdjp_borromeanV3`, `trace_e21n_QAdjn_borromeanV3`, and `trace_e21_QAdj_diff_borromeanV3`.
5. Verify with `scripts/lean-verify.sh` and strict vacuity audits, then submit to adversarial review.



## Completion Record (2026-11-18)
- Formalized Section 7 (Central Idempotent Projections e_(3) and e_(2,1) on Borromean V^3) and Section 8 (Gröbner Normal-Form Channel Collapse L_- = L_+^T and c_{L_+} + c_{L_-} = h^4) in `NucleonWeightSpaceTwoTerm.lean` (774 lines, `0 sorry`, `0 warnings`).
- Adversarially verified (`qou-kyfx`, `lane-7b4f`): PASS (`0` vacuity defects).
