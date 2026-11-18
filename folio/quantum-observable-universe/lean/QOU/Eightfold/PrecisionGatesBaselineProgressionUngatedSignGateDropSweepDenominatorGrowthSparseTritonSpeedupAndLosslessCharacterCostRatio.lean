/-
Copyright (c) 2026 QOU Formalization. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

# Precision Gates Baseline Progression, Ungated Sign-Gate Drop, Sweep Denominator Growth, Sparse Triton Speedup, and Lossless Character Cost Ratio

This standalone zero-sorry Lean 4 module formalizes five measurement-instrumentation
and partition-cost audits:

1. **`qou-z23u` — Precision-gates baseline progression and inherited debt**:
   - The 18 reported `Q0_FLIP` failures partition into 1 genuine anchor flip
     (`hadron-knot-table`) and 17 unmappable prose labels (`Q0_ANCHOR_UNRECOGNISED`
     drained `17 → 0`).
   - `tower_walk_magic_replication_probe` aggregated 77 traces at default
     `mp.dps = 15` (`60 - 15 = 45` digits of padding across 22 fields), and
     draining the 58 new padding hits reduced the ratchet count `70 → 12`.
   - `magnus_sign_row_truncation_probe` and `magnus_tr_decay_perpair_cluster_probe`
     upgraded 34 constructions from `mp.dps = 15` to `mp.dps = 140` (`140 - 15 = 125`
     digits gained, self-test cases `9 → 13`), while baseline blocking red gates
     progressed `10 → 9 → 10 → 11` across `683` commits between baselines.

2. **`qou-21oc` — Dropping the Pass-2 sign gate leaves the ungated total wrong-signed**:
   - Dropping the `final_tr_sign <= 0` gate shifts every admitted partition block into
     the total (`4/10 → 10/10` for `²H` and `2/10 → 10/10` for `⁴He` at `k_exact = 4`;
     `15/28 → 28/28` for `²H` and `10/28 → 28/28` for `⁴He` at `k_exact = 6`;
     `94/193 → 193/193` for `²H` and `90/193 → 193/193` for `⁴He` at production
     default `k = 11`).
   - Because all blocks have negative energy contribution, adding the previously
     excluded positive-trace blocks (`193 - 94 = 99` blocks for `²H`, `193 - 90 = 103`
     blocks for `⁴He`) drives the ungated term-1 contribution further negative, so the
     three-term `binding_energy(1, 1)` total moves from `-7.27110212487674490878` MeV
     to `-15.8141948959354083735877911366312919667669572902108415800038` MeV against
     the empirical `+2.2245662` MeV reference.

3. **`qou-6q7q` — Post-rebase re-measurement and dynamic sweep denominator growth**:
   - Out of 111 audited paths (`55` producers + witnesses), 108 were byte-identical
     to `origin/main` and 3 moved (`1` witness + `2` non-sweep producers), leaving
     1 real producer (`q0_anchor_consistency_audit.py`).
   - Meanwhile, a 229-witness labelling commit on `main` (`79` commits ahead of the
     pre-rebase base) enlarged the dynamic muon target denominator from `47` to `142`
     (`142 - 47 = 95` newly tagged targets), with `--resume` retaining `46` entries
     and measuring `9` new before `55 / 142` (`46 + 9 = 55`) and `7` more before
     `62 / 142` (`55 + 7 = 62`).

4. **`qou-bimg` — Dense vs sparse triton Magnus evaluation across 30 partitions**:
   - Both routes evaluate all `30/30` partitions of `n = 9`, agreeing to `9.08e-60`,
     while the dense route takes `~2400 s` (`40 min`, or `24000` tenths of a second)
     versus `27.5 s` (`275` tenths of a second) on the sparse route (`275 * 87 = 23925 ≤ 24000 < 275 * 88`),
     and a prior unpatched cache served `14/30` stale rows (`30 - 14 = 16` remaining).

5. **`qou-d9wf` — Lossless character cost model underestimation on `⁵Li` and `⁶Li`**:
   - The docstring cost model estimates `2 s` for `⁴He` (`n = 12`, `77` partitions),
     `4 s` (`~20 ms`/partition) for `⁵Li` (`n = 15`, `176` partitions), and `8 s` for
     `⁶Li` (`n = 18`, `385` partitions, combined `176 + 385 = 561` partitions), whereas
     measured `⁵Li` runtime exceeded `600 s` (`150 × 4 s`) and `1800 s` (`450 × 4 s`,
     `> 10000 ms` vs `20 ms` per partition = `500×`), with RSS climbing `198 → 247 → 310 MB`
     (`310 - 198 = 112 MB` growth).
-/

namespace QOU.Eightfold.PrecisionGatesBaselineProgressionUngatedSignGateDropSweepDenominatorGrowthSparseTritonSpeedupAndLosslessCharacterCostRatio

/-! ## 1. `qou-z23u`: Precision-Gates Baseline Progression and Inherited Debt -/

/-- Total initial `Q0_FLIP` count split into genuine anchor flips and unmappable prose labels. -/
def totalQ0FlipCount (realFlips unrecognisedAnchors : Nat) : Nat :=
  realFlips + unrecognisedAnchors

/-- Remaining `float64`-padding ratchet entries after draining newly introduced hits. -/
def remainingPaddingRatchet (initialTotal drainedNewHits : Nat) : Nat :=
  initialTotal - drainedNewHits

/-- Net decimal-precision gain when upgrading a probe from inherited default `dps` to explicit `dps`. -/
def precisionDigitsGain (inheritedDps explicitDps : Nat) : Nat :=
  explicitDps - inheritedDps

/-- Net change in blocking red gates between baseline measurements after fixing `fixedGates`
    and uncovering `newlyExposedGates`. -/
def blockingGatesProgression (initialRed fixedGates newlyExposedGates : Nat) : Nat :=
  initialRed - fixedGates + newlyExposedGates

/-- For any `realFlips`, `unrecognisedAnchors`, `initialRatchet`, and `drainedNewHits` with
    `drainedNewHits ≤ initialRatchet`, the split `totalQ0FlipCount` and `remainingPaddingRatchet`
    recover their respective totals, and at `(1, 17, 70, 58)` yield `18` total flips and `12`
    remaining baseline ratchet entries. -/
theorem q0_flip_partition_and_padding_ratchet_drain
    (realFlips unrecognisedAnchors initialRatchet drainedNewHits : Nat)
    (hDrain : drainedNewHits ≤ initialRatchet) :
    totalQ0FlipCount realFlips unrecognisedAnchors - unrecognisedAnchors = realFlips ∧
    remainingPaddingRatchet initialRatchet drainedNewHits + drainedNewHits = initialRatchet ∧
    totalQ0FlipCount 1 17 = 18 ∧
    remainingPaddingRatchet 70 58 = 12 := by
  dsimp [totalQ0FlipCount, remainingPaddingRatchet]
  omega

/-- Upgrading from `inheritedDps` to `explicitDps` (`inheritedDps ≤ explicitDps`) increases precision
    by `precisionDigitsGain inheritedDps explicitDps`, and the baseline red-gate sequence
    `10 → 9 → 10 → 11` follows `blockingGatesProgression`. -/
theorem precision_upgrade_and_blocking_gate_progression
    (inheritedDps explicitDps : Nat)
    (hDps : inheritedDps ≤ explicitDps) :
    inheritedDps + precisionDigitsGain inheritedDps explicitDps = explicitDps ∧
    precisionDigitsGain 15 60 = 45 ∧
    precisionDigitsGain 15 140 = 125 ∧
    blockingGatesProgression 10 1 0 = 9 ∧
    blockingGatesProgression 9 0 1 = 10 ∧
    blockingGatesProgression 10 0 1 = 11 := by
  dsimp [precisionDigitsGain, blockingGatesProgression]
  omega

/-! ## 2. `qou-21oc`: Ungated Sign-Gate Drop and Wrong-Signed Binding Total -/

/-- Number of positive-trace partition blocks newly admitted when the `final_tr_sign <= 0`
    sign gate is dropped. -/
def newlyAdmittedBlocks (totalPartitions gatedAdmittedBlocks : Nat) : Nat :=
  totalPartitions - gatedAdmittedBlocks

/-- Ungated term-1 energy (scaled integer magnitude) obtained by combining the gated negative
    magnitude with the newly admitted blocks' negative magnitude. -/
def ungatedNegativeMagnitude (gatedMagnitude newlyAdmittedMagnitude : Nat) : Nat :=
  gatedMagnitude + newlyAdmittedMagnitude

/-- Signed three-term binding energy (in scaled integer units) from a negative term-1 magnitude
    `-term1Mag`, zero term-2, and positive pairing term `+term3Mag`. -/
def threeTermSignedBinding (term1Mag term3Mag : Int) : Int :=
  -term1Mag + 0 + term3Mag

/-- Across `k_exact = 4` (`10` partitions), `k_exact = 6` (`28` partitions), and production
    default `k = 11` (`193` partitions), dropping the sign gate admits `totalPartitions - gatedAdmitted`
    additional negative-energy blocks (`6`, `8`, `13`, `18`, `99`, and `103` blocks respectively). -/
theorem sign_gate_drop_admitted_block_complements
    (totalPartitions gatedAdmitted : Nat)
    (hGated : gatedAdmitted ≤ totalPartitions) :
    gatedAdmitted + newlyAdmittedBlocks totalPartitions gatedAdmitted = totalPartitions ∧
    newlyAdmittedBlocks 10 4 = 6 ∧
    newlyAdmittedBlocks 10 2 = 8 ∧
    newlyAdmittedBlocks 28 15 = 13 ∧
    newlyAdmittedBlocks 28 10 = 18 ∧
    newlyAdmittedBlocks 193 94 = 99 ∧
    newlyAdmittedBlocks 193 90 = 103 := by
  dsimp [newlyAdmittedBlocks]
  omega

/-- Whenever newly admitted blocks contribute a positive magnitude `newlyAdmittedMag > 0`
    to the negative term-1 sum (`gatedMag > term3Mag ≥ 0`), the ungated three-term binding
    energy is strictly more negative than the gated binding energy and remains strictly negative. -/
theorem ungated_three_term_binding_strictly_more_negative
    (gatedMag newlyAdmittedMag term3Mag : Int)
    (hGatedDom : term3Mag < gatedMag)
    (hNewPos : 0 < newlyAdmittedMag) :
    threeTermSignedBinding (gatedMag + newlyAdmittedMag) term3Mag <
      threeTermSignedBinding gatedMag term3Mag ∧
    threeTermSignedBinding (gatedMag + newlyAdmittedMag) term3Mag < 0 ∧
    ungatedNegativeMagnitude 9147736 8543093 = 17690829 := by
  dsimp [threeTermSignedBinding, ungatedNegativeMagnitude]
  omega

/-! ## 3. `qou-6q7q`: Post-Rebase Path Audit and Dynamic Sweep Denominator Growth -/

/-- Number of moved paths in an in-scope file audit after subtracting byte-identical paths. -/
def movedPathCount (totalAuditedPaths byteIdenticalPaths : Nat) : Nat :=
  totalAuditedPaths - byteIdenticalPaths

/-- Growth in the dynamic muon target sweep denominator after a witness-labelling commit on `main`. -/
def sweepDenominatorGrowth (preRebaseTotal postRebaseTotal : Nat) : Nat :=
  postRebaseTotal - preRebaseTotal

/-- Cumulative measured entries in a `--resume` sweep after retaining `retainedEntries`
    and completing `newlyMeasuredEntries` before timeout. -/
def resumedMeasuredCount (retainedEntries newlyMeasuredEntries : Nat) : Nat :=
  retainedEntries + newlyMeasuredEntries

/-- Remaining unmeasured targets after a resumed sweep reaches `resumedMeasuredCount`. -/
def remainingSweepTargets (postRebaseTotal retainedEntries newlyMeasuredEntries : Nat) : Nat :=
  postRebaseTotal - resumedMeasuredCount retainedEntries newlyMeasuredEntries

/-- In the 111-path post-rebase check (`108` byte-identical, `3` moved), the dynamic sweep
    denominator grew from `47` to `142` (`+95` targets), and resuming from `46` retained entries
    through `9` then `7` additional measurements leaves `87` then `80` targets remaining. -/
theorem post_rebase_path_audit_and_sweep_denominator_growth
    (postRebaseTotal retainedEntries batchOne batchTwo : Nat)
    (hFit : retainedEntries + batchOne + batchTwo ≤ postRebaseTotal) :
    resumedMeasuredCount (resumedMeasuredCount retainedEntries batchOne) batchTwo +
      remainingSweepTargets postRebaseTotal (resumedMeasuredCount retainedEntries batchOne) batchTwo =
      postRebaseTotal ∧
    movedPathCount 111 108 = 3 ∧
    sweepDenominatorGrowth 47 142 = 95 ∧
    resumedMeasuredCount 46 9 = 55 ∧
    resumedMeasuredCount 55 7 = 62 ∧
    remainingSweepTargets 142 46 9 = 87 ∧
    remainingSweepTargets 142 55 7 = 80 := by
  dsimp [movedPathCount, sweepDenominatorGrowth, resumedMeasuredCount, remainingSweepTargets]
  omega

/-! ## 4. `qou-bimg`: Dense vs Sparse Triton Magnus Speedup and Stale Cache Drain -/

/-- Integer floor speedup factor of a dense route over a sparse route (in tenths of a second). -/
def denseToSparseSpeedupFloor (denseTenthsSec sparseTenthsSec : Nat) : Nat :=
  denseTenthsSec / sparseTenthsSec

/-- Number of remaining partitions that must be recomputed when a stale cache only serves
    `staleCachedRows` out of `totalPartitions`. -/
def uncachedPartitionRows (totalPartitions staleCachedRows : Nat) : Nat :=
  totalPartitions - staleCachedRows

/-- Total wall-clock time (in minutes) wasted by `rerunCount` full dense reruns of duration
    `minutesPerRun`. -/
def denseRerunWallMinutes (rerunCount minutesPerRun : Nat) : Nat :=
  rerunCount * minutesPerRun

/-- On the 30 partitions of `n = 9`, the `2400.0 s` (`24000` tenths-of-s) dense route vs the
    `27.5 s` (`275` tenths-of-s) sparse route yields an `87×` integer floor speedup, `14` stale
    cached rows leave `16` rows, and `2` docstring-triggered reruns cost `80` minutes. -/
theorem dense_vs_sparse_triton_speedup_and_cache_complement
    (totalPartitions staleRows reruns minutesPerRun : Nat)
    (hStale : staleRows ≤ totalPartitions) :
    staleRows + uncachedPartitionRows totalPartitions staleRows = totalPartitions ∧
    denseRerunWallMinutes reruns minutesPerRun = reruns * minutesPerRun ∧
    denseToSparseSpeedupFloor 24000 275 = 87 ∧
    275 * 87 ≤ 24000 ∧
    24000 < 275 * 88 ∧
    uncachedPartitionRows 30 14 = 16 ∧
    denseRerunWallMinutes 2 40 = 80 := by
  dsimp [denseToSparseSpeedupFloor, uncachedPartitionRows, denseRerunWallMinutes]
  omega

/-! ## 5. `qou-d9wf`: Lossless Character Cost Ratio and RSS Growth on `⁵Li` and `⁶Li` -/

/-- Underestimation factor between measured elapsed time and documented cost-model time. -/
def costModelUnderestimationFactor (measuredSeconds documentedSeconds : Nat) : Nat :=
  measuredSeconds / documentedSeconds

/-- Combined partition count across two consecutive nuclear character targets (`⁵Li` and `⁶Li`). -/
def combinedTargetPartitions (li5Partitions li6Partitions : Nat) : Nat :=
  li5Partitions + li6Partitions

/-- Net resident-set-size (RSS) memory growth in megabytes between two checkpoints. -/
def rssGrowthMegabytes (initialRssMb currentRssMb : Nat) : Nat :=
  currentRssMb - initialRssMb

/-- For `⁵Li` (`176` partitions, documented `4 s`, `20 ms`/partition) and `⁶Li` (`385` partitions,
    documented `8 s`), the combined sweep covers `561` partitions, measured `⁵Li` runtimes of
    `600 s` and `1800 s` exceed the `4 s` estimate by `150×` and `450×` (`10000 ms / 20 ms = 500×`
    per partition), and RSS grows `198 → 247 → 310 MB` (`+49 MB` then `+63 MB`, total `+112 MB`). -/
theorem lossless_character_cost_ratio_and_rss_growth
    (r0 r1 r2 : Nat)
    (h01 : r0 ≤ r1)
    (h12 : r1 ≤ r2) :
    rssGrowthMegabytes r0 r1 + rssGrowthMegabytes r1 r2 = rssGrowthMegabytes r0 r2 ∧
    combinedTargetPartitions 176 385 = 561 ∧
    costModelUnderestimationFactor 600 4 = 150 ∧
    costModelUnderestimationFactor 1800 4 = 450 ∧
    costModelUnderestimationFactor 10000 20 = 500 ∧
    rssGrowthMegabytes 198 247 = 49 ∧
    rssGrowthMegabytes 247 310 = 63 ∧
    rssGrowthMegabytes 198 310 = 112 := by
  dsimp [rssGrowthMegabytes, combinedTargetPartitions, costModelUnderestimationFactor]
  omega

end QOU.Eightfold.PrecisionGatesBaselineProgressionUngatedSignGateDropSweepDenominatorGrowthSparseTritonSpeedupAndLosslessCharacterCostRatio
