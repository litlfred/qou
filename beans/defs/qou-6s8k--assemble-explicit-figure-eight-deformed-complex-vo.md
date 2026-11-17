---
# qou-6s8k
title: Assemble explicit figure-eight deformed complex volume V_41(u)=Vol(u)+i*CS(u) from CuspShapeBarParity + NeumannZagierParity + Clausen; reduce SDeformedVolumeChannel.V from abstract field to concrete NZ function (formalize-first, no fit)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-26T20:31:56Z
updated_at: 2026-11-17T08:05:00Z
parent: b9cj
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 77 Formalization Update (2026-11-17)

- **PR**: https://github.com/litlfred/qou/pull/8270 (`6053dcb4a4cd613867cf11286810e234a6e19f69`)
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/DeformedVolumeParityAndDiracReebConvexSplitBrick.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, verified with `lean -DautoImplicit=false -s 65536` exit 0, 0 `sorry`/`axiom`/`native_decide`, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/deformed_volume_parity_and_dirac_reeb_convex_split_brick_probe.py` (`scriptCommitSha: 9d5b1ea5cef1335474ac59e8528d4646769eddc6`) and `computations/probes/deformed-volume-parity-and-dirac-reeb-convex-split-brick.witness.json` (`allPassed: true`).

