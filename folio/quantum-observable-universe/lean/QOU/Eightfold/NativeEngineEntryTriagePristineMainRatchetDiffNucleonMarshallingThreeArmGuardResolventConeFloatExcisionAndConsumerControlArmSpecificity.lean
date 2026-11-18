/-!
# Native Engine Entry Triage, Pristine-Main Ratchet Diff, Nucleon Marshalling Three-Arm Guard, Resolvent Cone Float64 Excision, and Consumer Control-Arm Specificity

Formalizes five numerical-precision and convention-audit theorems in the
`qou-10v9` subtree:

1. **qou-nmza — `F64_ENGINE_ENTRY` Disposition Partition and Zero Clean Propagators**:
   The initial AST census across both direct and wrapper hops flags `71`
   candidate sites across `46` files, which partition into `7` deliberate sites
   (`5` files), `46` harmless sites (`33` files), and `18` actionable sites
   (`13` files; `7 + 46 + 18 = 71`). On the 2026-09-13 re-measurement, the
   `63` candidate sites across `43` files partition into `9` deliberate sites
   (`6` files), `38` harmless sites (`26` files), and `16` actionable sites
   (`11` files; `9 + 38 + 16 = 63`, `6 + 26 + 11 = 43`). Of the `11` actionable
   files (`16` sites), `2` files (`2` sites) carry the `PROPAGATES` flag and
   `9` files (`14` sites) are `terminal` (`2 + 9 = 11`, `2 + 14 = 16`). Hand
   inspection of the `2` propagating files shows `1` is a deliberate internal
   cross-check and `1` is capped by float64 `dim_q`/`qfac`, leaving `2 - 2 = 0`
   clean propagators.

2. **qou-nwhg — Pristine-`main` `REGRESSED: 3` Ratchet False Stop and Branch-vs-`main` Diff**:
   Comparing a feature branch against the static committed baseline JSON flags
   `3` regressed witnesses inherited verbatim from pristine `main` (`3`
   `main`-inherited regressions, `0` branch-authored regressions). Evaluating
   the ratchet relative to live `origin/main` subtracts the `3` inherited
   regressions (`3 - 3 = 0` net branch regressions), eliminating the false stop
   while preserving sensitivity to any strictly positive branch-introduced
   dirty-field delta.

3. **qou-o0pa — Nucleon `H_3` Marshalling Divergence Three-Arm Guard Restoration**:
   The canonical `11`-crossing nucleon word decomposes into `6` positive + `2`
   averaged + `3` inverse crossings (`6 + 2 + 3 = 11`) for the proton and `5`
   positive + `2` averaged + `4` inverse crossings (`5 + 2 + 4 = 11`) for the
   neutron. Restoring the three-arm regression guard (`3 + 2 = 5` passing
   assertions) separates the `d`-preserving canonical arm (`0.6293284022`
   proton, `0.4751335172` neutron), the production routing arm, and the explicit
   lossy marshalled arm (`0.8070313949` proton, `0.5350618531` neutron, with
   proton ratio `> 1.28` and neutron ratio `> 1.12`).

4. **qou-oiz3 — UIC Resolvent Cone Float64 Excision (`9 + 1 = 10` Sites) and Residual Dominant Floor**:
   Excising float64 across `9` source sites and `1` ambient-dps cache site
   (`9 + 1 = 10` sites) at `mp.dps = 70` yields a worst per-atom gated shift of
   `8.44176e-16` and worst ungated shift of `6.65778e-15` at `(Z, N) = (4, 4)`,
   exceeding binary64 machine epsilon (`2.22045e-16`) by more than `3x` (gated)
   and `29x` (ungated) via cancellation. Across the `31` weighted blocks, the
   local excision removes at most `2.4946976e-16` while the shared float64
   `q_int` helper (`124` Python files, `243` witnesses) leaves a `1.0212424e-15`
   residual at `(2, 2)` (`> 4x` the locally removed error).

5. **qou-okkz — Consumer-Side Control-Arm Detector and Self-Poisoning Specificity Census**:
   Scanning `2938` witnesses and `3758` Python files (`1854` naming a witness)
   after dropping `371` self-written pairs yields `229` foreign READ edges
   across `122` consumers, including `15` foreign-transcription edges split into
   `1` specific control-arm edge (`5` transcribed weights) and `14`
   shared-constant edges (`1 + 14 = 15`; `229 - 1 = 228` unmeasured edges).
   Under the specificity bound `census <= 3`, the control arm's `5` weights sit
   at `census = 2`; counting the detector's own witness raises the count to
   `2 + 1 = 3` (zero margin below `3`), and `1` more transcribing artifact
   pushes it to `3 + 1 = 4 > 3`, silencing the control-arm verdict.
-/

namespace QOU.Eightfold.NativeEngineEntryTriagePristineMainRatchetDiffNucleonMarshallingThreeArmGuardResolventConeFloatExcisionAndConsumerControlArmSpecificity

/-! ## 1. `F64_ENGINE_ENTRY` Disposition Partition (`qou-nmza`) -/

/-- Initial AST candidate sites reaching the native f64 entry points. -/
def initialCandidateSites : Nat := 71

/-- Initial deliberate cross-check sites. -/
def initialDeliberateSites : Nat := 7

/-- Initial harmless sites (never serialized above 17 digits). -/
def initialHarmlessSites : Nat := 46

/-- Initial actionable sites (serialized wide from an f64 value). -/
def initialActionableSites : Nat := 18

/-- Re-measured (2026-09-13) AST candidate sites. -/
def remeasuredCandidateSites : Nat := 63

/-- Re-measured deliberate cross-check sites. -/
def remeasuredDeliberateSites : Nat := 9

/-- Re-measured harmless sites. -/
def remeasuredHarmlessSites : Nat := 38

/-- Re-measured actionable sites. -/
def remeasuredActionableSites : Nat := 16

/-- Re-measured candidate files. -/
def remeasuredCandidateFiles : Nat := 43

/-- Re-measured deliberate files. -/
def remeasuredDeliberateFiles : Nat := 6

/-- Re-measured harmless files. -/
def remeasuredHarmlessFiles : Nat := 26

/-- Re-measured actionable files. -/
def remeasuredActionableFiles : Nat := 11

/-- Actionable files flagged `PROPAGATES`. -/
def propagatingActionableFiles : Nat := 2

/-- Actionable files flagged `terminal`. -/
def terminalActionableFiles : Nat := 9

/-- Propagating sites among the 16 actionable sites. -/
def propagatingActionableSites : Nat := 2

/-- Terminal sites among the 16 actionable sites (`4 + 3 + 1 + 6 * 1 = 14`). -/
def terminalActionableSites : Nat := 14

/-- Propagating files that are false positives or half-fix blocked (`1 + 1 = 2`). -/
def blockedOrDeliberatePropagatingFiles : Nat := 2

/-- Exact partition of both `F64_ENGINE_ENTRY` censuses and proof that `0` clean
    propagating files remain after accounting for the 2 flagged propagators. -/
theorem native_engine_entry_disposition_partition :
    initialDeliberateSites + initialHarmlessSites + initialActionableSites =
      initialCandidateSites ∧
    remeasuredDeliberateSites + remeasuredHarmlessSites + remeasuredActionableSites =
      remeasuredCandidateSites ∧
    remeasuredDeliberateFiles + remeasuredHarmlessFiles + remeasuredActionableFiles =
      remeasuredCandidateFiles ∧
    propagatingActionableFiles + terminalActionableFiles = remeasuredActionableFiles ∧
    propagatingActionableSites + terminalActionableSites = remeasuredActionableSites ∧
    propagatingActionableFiles - blockedOrDeliberatePropagatingFiles = 0 := by
  decide

/-! ## 2. Pristine-`main` `REGRESSED: 3` Ratchet False Stop (`qou-nwhg`) -/

/-- Witness regressions reported on pristine `main` against the static baseline JSON. -/
def pristineMainStaticRegressions : Nat := 3

/-- Net regressions on a clean feature branch when diffed against live `origin/main`. -/
def cleanBranchNetRegressions : Nat := 0

/-- Stale-baseline witnesses identified across the full 69-entry baseline refresh (`qou-kn46`). -/
def fullRefreshStaleBaselineWitnesses : Nat := 5

/-- Additional stale-baseline witnesses uncovered only by full regeneration (`5 - 3 = 2`). -/
def regenerationOnlyStaleWitnesses : Nat := 2

/-- Diffing against live `origin/main` cancels the `3` pristine-`main` static regressions. -/
theorem pristine_main_ratchet_diff_cancellation :
    pristineMainStaticRegressions - pristineMainStaticRegressions =
      cleanBranchNetRegressions ∧
    pristineMainStaticRegressions + regenerationOnlyStaleWitnesses =
      fullRefreshStaleBaselineWitnesses ∧
    cleanBranchNetRegressions < pristineMainStaticRegressions := by
  decide

/-! ## 3. Nucleon `H_3` Marshalling Divergence Three-Arm Guard (`qou-o0pa`) -/

/-- Total crossings in the canonical 3-strand nucleon word. -/
def nucleonCanonicalCrossingCount : Nat := 11

/-- Proton positive-crossing count (`sigma`). -/
def protonPositiveCrossings : Nat := 6

/-- Proton averaged-crossing count. -/
def protonAveragedCrossings : Nat := 2

/-- Proton inverse-crossing count (`sigma_inv`). -/
def protonInverseCrossings : Nat := 3

/-- Neutron positive-crossing count (`sigma`). -/
def neutronPositiveCrossings : Nat := 5

/-- Neutron averaged-crossing count. -/
def neutronAveragedCrossings : Nat := 2

/-- Neutron inverse-crossing count (`sigma_inv`). -/
def neutronInverseCrossings : Nat := 4

/-- Assertions in the two-arm unmarshalled rebuild. -/
def twoArmRebuildAssertions : Nat := 3

/-- Additional explicit marshalled-loss assertions added by the third arm. -/
def explicitMarshalledArmAssertions : Nat := 2

/-- Total passing assertions in the restored three-arm probe. -/
def restoredThreeArmAssertions : Nat := 5

/-- Canonical `d`-preserving proton trace scaled by `10^10` (`0.6293284022 * 10^10`). -/
def protonCanonicalTraceScaled1e10 : Nat := 6293284022

/-- Explicit marshalled proton trace scaled by `10^10` (`0.8070313949 * 10^10`). -/
def protonMarshalledTraceScaled1e10 : Nat := 8070313949

/-- Canonical `d`-preserving neutron trace scaled by `10^10` (`0.4751335172 * 10^10`). -/
def neutronCanonicalTraceScaled1e10 : Nat := 4751335172

/-- Explicit marshalled neutron trace scaled by `10^10` (`0.5350618531 * 10^10`). -/
def neutronMarshalledTraceScaled1e10 : Nat := 5350618531

/-- Exact crossing-census partition (`6 + 2 + 3 = 11`, `5 + 2 + 4 = 11`), assertion
    count (`3 + 2 = 5`), and marshalling-divergence bounds (`> 28%` proton, `> 12%` neutron). -/
theorem nucleon_marshalling_three_arm_guard_bounds :
    protonPositiveCrossings + protonAveragedCrossings + protonInverseCrossings =
      nucleonCanonicalCrossingCount ∧
    neutronPositiveCrossings + neutronAveragedCrossings + neutronInverseCrossings =
      nucleonCanonicalCrossingCount ∧
    twoArmRebuildAssertions + explicitMarshalledArmAssertions =
      restoredThreeArmAssertions ∧
    protonMarshalledTraceScaled1e10 * 100 > 128 * protonCanonicalTraceScaled1e10 ∧
    neutronMarshalledTraceScaled1e10 * 100 > 112 * neutronCanonicalTraceScaled1e10 := by
  decide

/-! ## 4. UIC Resolvent Cone Float64 Excision and Residual Dominant Floor (`qou-oiz3`) -/

/-- Source-line float64 sites excised in `unified_iterative_correction.py`. -/
def excisedSourceLineSites : Nat := 9

/-- Ambient-dps cache site (`_partition_table`) wrapped in `workdps`. -/
def wrappedCacheSites : Nat := 1

/-- Total float64 surface sites addressed in the UIC resolvent cone excision. -/
def totalExcisedUicSurfaceSites : Nat := 10

/-- IEEE 754 binary64 machine epsilon in units of `10^-21` (`2.22045e-16 = 222045 * 10^-21`). -/
def binary64EpsScaled1e21 : Nat := 222045

/-- Worst per-atom gated shift at `(Z, N) = (4, 4)` in units of `10^-21` (`8.44176e-16 = 844176 * 10^-21`). -/
def worstGatedShiftScaled1e21 : Nat := 844176

/-- Worst per-atom ungated shift at `(Z, N) = (4, 4)` in units of `10^-21` (`6.65778e-15 = 6657780 * 10^-21`). -/
def worstUngatedShiftScaled1e21 : Nat := 6657780

/-- Maximum per-block error removed by the local excision in units of `10^-23` (`2.4946976e-16`). -/
def maxRemovedBlockErrorScaled1e23 : Nat := 24946976

/-- Remaining per-block error at `(2, 2)` from float64 `q_int` in units of `10^-23` (`1.0212424e-15`). -/
def remainingQIntBlockErrorScaled1e23 : Nat := 102124240

/-- Exact site sum (`9 + 1 = 10`), cancellation amplification above binary64 epsilon
    (`> 3x` gated, `> 29x` ungated), and proof that the unexcised `q_int` error exceeds
    `4x` the locally removed block error. -/
theorem uic_resolvent_cone_excision_and_qint_residual :
    excisedSourceLineSites + wrappedCacheSites = totalExcisedUicSurfaceSites ∧
    worstGatedShiftScaled1e21 > 3 * binary64EpsScaled1e21 ∧
    worstUngatedShiftScaled1e21 > 29 * binary64EpsScaled1e21 ∧
    remainingQIntBlockErrorScaled1e23 > 4 * maxRemovedBlockErrorScaled1e23 := by
  decide

/-! ## 5. Consumer-Side Control-Arm Detector and Self-Poisoning Census (`qou-okkz`) -/

/-- Total foreign READ edges of Convention C witnesses across `122` consumers. -/
def totalForeignReadEdges : Nat := 229

/-- Confirmed control-arm edges transcribing specific reference values (`>= 1` specific value). -/
def confirmedControlArmEdges : Nat := 1

/-- Unmeasured foreign READ edges (`229 - 1 = 228`). -/
def unmeasuredForeignReadEdges : Nat := 228

/-- Total foreign-transcription edges (`1` control arm + `14` shared-constant edges). -/
def totalForeignTranscriptionEdges : Nat := 15

/-- Foreign-transcription edges carrying shared constants only (`m_e`, `hbar*c`, `q_0`). -/
def sharedConstantTranscriptionEdges : Nat := 14

/-- Maximum witness occurrence count (`SPECIFICITY_MAX`) for a value to be classed as specific. -/
def specificityMaxThreshold : Nat := 3

/-- Corpus witness count for the control arm's 5 weights when self-exclusion is active. -/
def selfExcludedWeightCensus : Nat := 2

/-- Corpus witness count when the audit's own witness is included (`2 + 1 = 3`). -/
def unexcludedSelfWeightCensus : Nat := 3

/-- Corpus witness count if one additional artifact transcribes the weights (`3 + 1 = 4`). -/
def poisonedWeightCensus : Nat := 4

/-- Exact edge partition (`1 + 228 = 229`, `1 + 14 = 15`) and specificity threshold
    boundary (`2 <= 3`, `3 <= 3`, `4 > 3`) demonstrating the latent self-poisoning hazard. -/
theorem consumer_control_arm_edge_partition_and_specificity_threshold :
    confirmedControlArmEdges + unmeasuredForeignReadEdges = totalForeignReadEdges ∧
    confirmedControlArmEdges + sharedConstantTranscriptionEdges =
      totalForeignTranscriptionEdges ∧
    selfExcludedWeightCensus < specificityMaxThreshold ∧
    unexcludedSelfWeightCensus = specificityMaxThreshold ∧
    poisonedWeightCensus > specificityMaxThreshold := by
  decide

end QOU.Eightfold.NativeEngineEntryTriagePristineMainRatchetDiffNucleonMarshallingThreeArmGuardResolventConeFloatExcisionAndConsumerControlArmSpecificity
