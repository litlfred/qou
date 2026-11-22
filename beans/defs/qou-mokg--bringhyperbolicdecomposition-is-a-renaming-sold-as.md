---
# qou-mokg
title: BringHyperbolicDecomposition is a renaming sold as a decomposition — identical field to BringZeroModeBlochClass, and its docstring promises three things the field does not encode
status: in-progress
pr: 8240
updated_at: 2026-11-22T22:50:00Z
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T02:22:51Z
updated_at: 2026-11-22T22:50:00Z
parent: qou-r9ih
---

MEASURED 2026-09-04 during the qou-08zf Lean gap assessment.

`predicted-spectra/bring-hyperbolic-knot-bloch-decomposition.lean:150` proves
`BringZeroModeBlochClass` from `BringHyperbolicDecomposition` by

    bring_zero_mode_realised := hD.bw_sum_realised

The two classes carry the IDENTICAL field, so the "conditional theorem" is a
pure projection -- §3b-cond rule 5's degenerate shape.

NOT LAUNDERED, and the distinction matters: it is a `theorem`, not an
`instance`, so nothing auto-fires and no downstream conditional is silently
discharged. This is a naming/exposition defect, not a soundness one.

Two things to fix:

1. The docstring promises a knot MULTI-SET, MULTIPLICITIES and a NORMALISATION
   that the single field does not encode -- the `proof-claims-unencoded`
   criterion (severity major) in the vacuity audit.
2. It describes the field as `exists z, z = 2/(3*pi)` -- the CLOSED pre-Phase-2
   loophole form, not the live one. So the docstring documents a state the
   corpus moved past.

Either encode what the docstring promises, or say plainly that the class is a
named alias for the one field it carries and let the theorem read as the
projection it is.

## Progress Update (PR #8240)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8240` at `cb076a625e5995208490115a8926f02d958314a7`).
- **Lean Formalization**: `QOU.QBeta.AnglePolytopeFeasibilityAndClausenUnitCircleBrick.bring_hyperbolic_five_fold_tetrahedron_sum_decomposition` (C_5-orbit five-tetrahedron Bring volume decomposition V_Bring = 5 * D_tet and orbit mean V_Bring / 5 = D_tet under zero-sum cyclic perturbations.)
- **80-dps Witness**: `computations/probes/angle-polytope-feasibility-and-clausen-unit-circle-brick.witness.json` (`scriptHash: 2cbc25827af3`, `scriptCommitSha: ec2c1b177f9eff729f315a26ddbb5ea7edbf540d`).

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8240 (`QOU/QBeta/AnglePolytopeFeasibilityAndClausenUnitCircleBrick.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8240 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.

## 2026-11-22 — applicability verdict (STRICT review, wave-2 brief)

**APPLIES.** pure mathematics; no retired premise found (grep for photon/trefoil/convention C/census/muon pin/virtual photon: none); claim is hollow (vacuous brick PR, see note above), the open work stands.
