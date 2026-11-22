---
# qou-amvt
title: Missing AngleStructureFeasibility file in Optimization
status: completed
pr: 8240
updated_at: 2026-11-22T22:50:00Z
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T18:19:09Z
updated_at: 2026-11-22T22:50:00Z
parent: qou-r9ih
---

## Progress Update (PR #8240)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8240` at `cb076a625e5995208490115a8926f02d958314a7`).
- **Lean Formalization**: `QOU.QBeta.AnglePolytopeFeasibilityAndClausenUnitCircleBrick.angle_structure_interior_simplex_feasibility_and_volume_witness` (Interior feasibility witness around the equilateral ideal tetrahedron centre (pi/3, pi/3, pi/3) preserving angle sum pi and strict positivity.)
- **80-dps Witness**: `computations/probes/angle-polytope-feasibility-and-clausen-unit-circle-brick.witness.json` (`scriptHash: 2cbc25827af3`, `scriptCommitSha: ec2c1b177f9eff729f315a26ddbb5ea7edbf540d`).

## 2026-11-22 — wave-2 review of the claiming PR (thread "Work dilogarithm and Bloch beans")

The claim on this bean comes from PR #8240 (`QOU/QBeta/AnglePolytopeFeasibilityAndClausenUnitCircleBrick.lean`, opened 2026-11-16/17, still open, `mergeable_state: dirty`). I read every theorem in that file. Each one is an identity in scalar variables over `ℚ` or `ℝ` (`ring` / `linarith` / `field_simp`), and where the bean's claim appears it appears as a hypothesis (for example `#8224` proves `A_ω = 3` from the hypothesis `a_omega_phi = 3`). No theorem touches the bean's actual objects (no `LiTwo`, `blochD`, `Φ_b`, state integral, measure or limit). **So PR #8240 does not discharge this bean.** The W4 triage (PR #8531, `docs/coordination/2026-11-20-batch-pr-triage.md` on that branch) listed it as NEEDS-REWORK for conflicts only, because its scan deliberately does not flag real- or rational-typed one-liners.

Status left unchanged: resetting the claim and closing the PR are the owner's call, and the recommendation went to the coordinator. The work this bean describes is still open, as stated above this note.

## 2026-11-22 — applicability verdict (STRICT review, wave-2 brief)

**ALREADY-DONE.** QOU/Optimization/AngleStructureFeasibility.lean is tracked on main and wired in QOU.lean; lean-verify exit 0 (2026-11-22). Status set to completed.
