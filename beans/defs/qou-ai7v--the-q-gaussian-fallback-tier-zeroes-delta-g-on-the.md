---
# qou-ai7v
title: The q-Gaussian fallback tier zeroes delta_g on the SAME disproved complementary-slackness argument
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T22:56:19Z
updated_at: 2026-10-04T15:24:59Z
parent: qou-v2om
---


## The finding

`hecke_core_legacy._unified_iterative_correction_exact`, q-Gaussian fallback
block: for every partition in the window `k_exact < k <= k_max` it computes
`log_trace_approx` and then sets `delta_g = 0.0`, justified in-comment by the
SAME complementary-slackness argument the Pass-2 sign gate used —

> "positive trace => SLACK Frobenius constraint => y_λ* = 0 by complementary
> slackness ... this is the categorically correct outcome"

That argument is **refuted sorry-free** in
`QOU.MassTheory.UICGateNotFromComplementarySlackness` (PR #7251; see bean
`qou-21oc` for the four mismatches and the scope-(b) invariant). So the zeroing
has no derivation behind it and is now an **asserted modelling choice**.

## Why it was NOT changed in #7253

Two reasons, both deliberate:

1. **There is no derived replacement rule.** The tier is a Perron-Frobenius
   ASYMPTOTIC approximation supplying a `log_trace` and no matrix, so nothing in
   the corpus says what its contribution should be. Inventing one would move a
   number by selection, which AGENTS.md §"NO FITTING" forbids.
2. **It is unreachable on every default run.** `k_exact` defaults to `k_max`
   (`K_PARTITION_MAX = 11`), which empties the window: measured 0 partitions at
   the default against 169 at `k_exact = 4`, 164 at 5, 155 at 6 (finding 6 of
   `qou-sv7h`, re-confirmed). So the choice is latent on the production path.

Marked asserted-not-derived at the code site, with a banner saying plainly that
the fallback tier contributes exactly zero at every `k` in `(k_exact, k_max]`
and that this zero must NOT be read as a derived prediction that high-k
partitions are negligible.

## What would close this

A derived rule for the tier's contribution, or a measurement showing the tier is
genuinely negligible at some `k_exact < k_max` a caller actually uses. Note the
second is weaker: it would justify the number, not the reasoning.

Related: `qou-px38` (the jet variant, same disproved argument, also unchanged),
`qou-sv7h` (the tier's unreachability), `qou-21oc` (the gate drop itself).


## Progress 2026-11-17 (lane-e925)

Formalized in Lean 4 (`v4.24.0`, zero `sorry`) under `QOU.MassTheory` (`FallbackTierWindowZeroingAndPerGeneratorGroupedVolume.lean`, `CanonicalBraidLinkingNonUniformityAndMirrorSlopeFlip.lean`, `SymmetryEnergyBarBranchContinuumAndBetaBlindness.lean`) and verified at 50 dps in `computations/probes/fallback_tier_grouped_volume_braid_linking_mirror_slope_symmetry_branch_probe.py` (`computations/probes/fallback-tier-grouped-volume-braid-linking-mirror-slope-symmetry-branch-probe.witness.json`, `allPassed = true`). Opened PR #8321 (`ready: cde173d67efbd687c4f51cce6847a870b6c300f4`).
