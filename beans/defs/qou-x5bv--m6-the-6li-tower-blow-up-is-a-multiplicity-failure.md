---
# qou-x5bv
title: 'M6: the 6Li tower blow-up is a MULTIPLICITY failure, not only a period-growth one — bounded cumulant energies still blow up 6.27x'
status: in-progress
pr: 8314
branch: feat/qou-izah-jc0e-wpr6-x5bv-zbgu
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T06:46:50Z
updated_at: 2026-10-04T15:13:16Z
parent: qou-v2om
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`ThreeCliqueOvershootAndMuBarZeroAtFive.lean`, `AnalyticPositivityNonDiscriminationAndMultiplicityBlowup.lean`, `ClassicalisationCrossingShiftAndBondSetDisagreement.lean`) and verified at 50 dps in `computations/probes/three_clique_positivity_classicalisation_multiplicity_triton_probe.py` (`computations/probes/three-clique-positivity-classicalisation-multiplicity-triton-probe.witness.json`, `allPassed = true`). Opened PR #8314 (`ready: f962cb073826c603c1acca705a4ce4f581dfdcc6`).
