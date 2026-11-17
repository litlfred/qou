---
# qou-cyon
title: Fix UDeformFamilyPruning.lean — re-derive family kill-tests over the correct harmonic Im form (√3/4)(x²−y²); F1/F2/F3 all refuted, diagonal-crossing necessary
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-26T21:51:00Z
updated_at: 2026-11-17T08:05:00Z
parent: b9cj
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 77 Formalization Update (2026-11-17)

- **PR**: https://github.com/litlfred/qou/pull/8270 (`6053dcb4a4cd613867cf11286810e234a6e19f69`)
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/DeformedVolumeParityAndDiracReebConvexSplitBrick.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, verified with `lean -DautoImplicit=false -s 65536` exit 0, 0 `sorry`/`axiom`/`native_decide`, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/deformed_volume_parity_and_dirac_reeb_convex_split_brick_probe.py` (`scriptCommitSha: 9d5b1ea5cef1335474ac59e8528d4646769eddc6`) and `computations/probes/deformed-volume-parity-and-dirac-reeb-convex-split-brick.witness.json` (`allPassed: true`).

## Round 56 Update (PR #8271)
- Opened PR https://github.com/litlfred/qou/pull/8271 (`b2cbd4734e5f10beb2130e3555212a3d78a87989`, C1 `22c4bf632182163314cbb930ffed44b139fa5265`).
- Compiled under Lean 4.24.0 (`0` `sorry`, `0` `axiom`, `0` warnings) and verified `0` advisories across all 6 static vacuity & borrowed-name audits, with 80-dps `mpmath` witness `computations/probes/round56-devacuify-6qbv-b9cj.witness.json` (`scriptHash = c44bdf430d4f`).
