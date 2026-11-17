---
# qou-k12x
title: 'DERIVED: the canonical braid fixes the bonded-pair linking number — non-uniformly, and undefined for p-n'
status: in-progress
pr: 8321
branch: feat/qou-ai7v-cgyn-k12x-u8ji-y2np
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T07:31:08Z
updated_at: 2026-10-04T15:12:21Z
parent: qou-v2om
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`FallbackTierWindowZeroingAndPerGeneratorGroupedVolume.lean`, `CanonicalBraidLinkingNonUniformityAndMirrorSlopeFlip.lean`, `SymmetryEnergyBarBranchContinuumAndBetaBlindness.lean`) and verified at 50 dps in `computations/probes/fallback_tier_grouped_volume_braid_linking_mirror_slope_symmetry_branch_probe.py` (`computations/probes/fallback-tier-grouped-volume-braid-linking-mirror-slope-symmetry-branch-probe.witness.json`, `allPassed = true`). Opened PR #8321 (`ready: cde173d67efbd687c4f51cce6847a870b6c300f4`).
