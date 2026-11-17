---
# qou-j6mp
title: 'Cleanup: ensure co-equational caveat present wherever bridge equation Δ_ω f = A_ω df/dz is stated for the binding/entire-EGF side'
status: in-progress
pr: 8240
updated_at: 2026-11-17T07:03:07Z
type: bug
priority: normal
tags:
    - alien-habiro
    - reorg-2026-10-04
created_at: 2026-07-18T17:09:31Z
updated_at: 2026-10-04T15:15:37Z
parent: qou-frzo
---

For binding EGF e^{x+x²/2} (entire at q=1) there is NO equational Stokes phenomenon; the literal one-parameter-ODE bridge form does NOT apply verbatim — A_ω is a CO-EQUATIONAL (coefficient-plane) Stokes constant. Grep content/ + witnesses for any statement of the ODE bridge Δ_ω f = A_ω ∂f/∂z applied to the binding/entire side without the co-equational qualifier; add the caveat. Does NOT apply to the Q_β odd channel or genuinely divergent-equational objects — scope carefully. Ref: W5, Addendum 2 of 2026-07-12-alien-calculus-review-binding-gevrey-half.md.

## Progress Update (PR #8240)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8240` at `cb076a625e5995208490115a8926f02d958314a7`).
- **Lean Formalization**: `QOU.QBeta.AnglePolytopeFeasibilityAndClausenUnitCircleBrick.coequational_bridge_vs_entire_egf_stokes_defect_dichotomy` (Two-channel alien bridge equation reduction when the equational Stokes multiplier vanishes (S_eq = 0) on the entire binding EGF side.)
- **80-dps Witness**: `computations/probes/angle-polytope-feasibility-and-clausen-unit-circle-brick.witness.json` (`scriptHash: 2cbc25827af3`, `scriptCommitSha: ec2c1b177f9eff729f315a26ddbb5ea7edbf540d`).
