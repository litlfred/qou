---
# qou-izah
title: 'GAP-2 is bracketed: 3-cliques overshoot, its own proposed fix (mu-bar irreducible) gives ZERO at A>=5'
status: todo
pr: 8314
branch: feat/qou-izah-jc0e-wpr6-x5bv-zbgu
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T06:59:31Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`ThreeCliqueOvershootAndMuBarZeroAtFive.lean`, `AnalyticPositivityNonDiscriminationAndMultiplicityBlowup.lean`, `ClassicalisationCrossingShiftAndBondSetDisagreement.lean`) and verified at 50 dps in `computations/probes/three_clique_positivity_classicalisation_multiplicity_triton_probe.py` (`computations/probes/three-clique-positivity-classicalisation-multiplicity-triton-probe.witness.json`, `allPassed = true`). Opened PR #8314 (`ready: f962cb073826c603c1acca705a4ce4f581dfdcc6`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8314, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
