/-!
# Proximity Detector False Positives, Matrix-M Migration Blast Radius, Import-Dps Call-Chain Safety, Direct JSON-Dump Pin Decay, and Anchor Refill Arrival Rate

Formalizes five numerical-precision and convention-audit theorems in the
`qou-10v9` subtree:

1. **qou-p6sj — `qou-00c5` Laundering-Sweep Proximity Detector Contraction**:
   Three heuristic text-proximity detectors for uninhabited Lean `class`
   declarations reported as proved in prose fail via false positives:
   Detector 1 (`+-2`-line window) flags `22` candidates including `2` freshly
   fixed files (`22 - 2 = 20`); Detector 2 (substring and filename matching)
   flags `296` candidates across `956` uninhabited classes; Detector 3
   (whole-word class names, no filename matching, widened instance detection)
   contracts the list to `67` candidates across `778` uninhabited classes
   (`296 - 67 = 229` false positives removed, `956 - 778 = 178` classes filtered),
   where `3` sites on the twist-eigenvalue class are the `qou-00c5` fix itself
   stating `"AXIOMATIZED, not proved"`.

2. **qou-pb4c — Downstream `chi-*-at-q0-50dps-matrix-m` Convention D Migration Blast Radius**:
   Migrating `8` `chi-*-at-q0-50dps-matrix-m` witnesses from Convention C to
   Convention D collapses the 3-row weight `y_lambda(1,1,1)` from `0.0227449425`
   to `3.50e-72` and shifts proton `tr_M(q_0)` from `1.6331535901` to
   `1.8843194673` (`+15.3792%`, `> 15.3%`). The downstream blast radius spans
   `23` live producers emitting `14` witnesses (`23 - 14 = 9` excess producer
   scripts), and on the `qou-lt8x` 4-flag sample `3` of `4` flags (`4 - 1 = 3`)
   were non-Convention-C artifacts.

3. **qou-pgr1 — Import-Time `mp.dps` Call-Chain Safety (`20 = 15 + 5`) and `qou-wlaf` Blind-Spot Closure (`256 / 356`)**:
   All `20` position-risky import-time `mp.dps` sites across `11` files are
   safe (`0` proven-lossy): `15` follow an import-time `mp.dps` raise and `5`
   reside inside deferred `lambda`/`def` bodies (`15 + 5 = 20`). Across `2966`
   witnesses scanned by `witness_provenance_attribution_audit.py`, `2610` record
   a producer and `356` record none (`2610 + 356 = 2966`). Source-verified
   attribution resolves `256` of the `356` blind-spot witnesses, leaving
   `9` stem-only + `91` stemless = `100` unverified witnesses (`356 - 256 = 100`,
   closing `256 / 356 > 71.9%` of the blind spot).

4. **qou-pin5 — Direct `json.dump` Witness Writers (`436`) and Unmaintained Backfilled `q0Anchor` Pins (`15 = 1 + 14`)**:
   Across `780` witness producers, `184` invoke `stamp_staleness_metadata`
   (`780 - 184 = 596` do not), and `436` write witnesses via raw `json.dump`
   without `WitnessBuilder.save()`. Of those `436` direct-dump producers, `15`
   carried a backfilled `q0Anchor` pin (`436 - 15 = 421` unpinned direct-dump
   producers); repairing `1` (`t25_cinquefoil_deltalambda_sign_probe`, restoring
   `Q0_OK` from `565` to `566`) leaves `15 - 1 = 14` pinned witnesses one
   regeneration away from losing their pin.

5. **qou-q0rf — `q0-anchor` Refill Ratchet Five-Day Arrival Trajectory (`147`) and Within-Session `1:1` Replacement**:
   Over the 5-day window (2026-08-29 to 2026-09-02), daily unstamped arrivals of
   `[4, 74, 48, 16, 5]` sum to `147` new unstamped witnesses (`147 + 3 = 150`
   that afternoon), while the missing-anchor baseline shrank by `1`
   (`1678 - 1677 = 1`) and live unstamped witnesses grew by `1742 - 1627 = 115`.
   During a single session draining `4` witnesses (`86 + 4 = 90` drained, live
   unstamped `1605 - 4 = 1601`), `3` new unstamped files plus `1` stripped bare
   witness arrived via rebase (`3 + 1 = 4`), leaving `NEW` invariant at
   `14 - 4 + 4 = 14`.
-/

namespace QOU.Eightfold.ProximityDetectorFalsePositivesMatrixMMigrationBlastRadiusImportDpsCallChainSafetyDirectJsonDumpPinDecayAndAnchorRefillArrivalRate

/-! ## 1. `qou-00c5` Laundering-Sweep Proximity Detector Contraction (`qou-p6sj`) -/

/-- Candidates flagged by Detector 1 (`+-2`-line twist-name vs exponent window). -/
def detector1CandidateCount : Nat := 22

/-- Freshly fixed files falsely flagged by Detector 1. -/
def detector1FixedFileFalsePositives : Nat := 2

/-- Candidates flagged by Detector 2 (substring and filename matching). -/
def detector2CandidateCount : Nat := 296

/-- Uninhabited Lean classes scanned by Detector 2. -/
def detector2UninhabitedClassCount : Nat := 956

/-- Candidates flagged by Detector 3 (whole-word class names, no filename matching). -/
def detector3CandidateCount : Nat := 67

/-- Uninhabited Lean classes remaining in Detector 3 after widened instance detection. -/
def detector3UninhabitedClassCount : Nat := 778

/-- Candidate reduction from Detector 2 to Detector 3 (`296 - 67 = 229`). -/
def detector2To3CandidateReduction : Nat := 229

/-- Uninhabited-class reduction from Detector 2 to Detector 3 (`956 - 778 = 178`). -/
def detector2To3ClassReduction : Nat := 178

/-- Exact contraction counts across the three heuristic laundering-sweep detectors. -/
theorem proximity_detector_contraction_accounting :
    detector1CandidateCount - detector1FixedFileFalsePositives = 20 ∧
    detector2CandidateCount - detector3CandidateCount =
      detector2To3CandidateReduction ∧
    detector2UninhabitedClassCount - detector3UninhabitedClassCount =
      detector2To3ClassReduction ∧
    detector1CandidateCount < detector3CandidateCount ∧
    detector3CandidateCount < detector2CandidateCount := by
  decide

/-! ## 2. Downstream `chi-*-at-q0-50dps-matrix-m` Migration Blast Radius (`qou-pb4c`) -/

/-- Upstream `chi-*-at-q0-50dps-matrix-m` witnesses migrated from Convention C to D. -/
def migratedUpstreamMatrixMWitnesses : Nat := 8

/-- Live downstream producers referencing `matrix-m` / `at-q0-50dps-matrix`. -/
def downstreamMatrixMProducers : Nat := 23

/-- Downstream witnesses emitted by the 23 producers. -/
def downstreamMatrixMWitnesses : Nat := 14

/-- Proton `tr_M(q_0)` under Convention C scaled by `10^10` (`1.6331535901 * 10^10`). -/
def protonTrMConventionCScaled1e10 : Nat := 16331535901

/-- Proton `tr_M(q_0)` under Convention D scaled by `10^10` (`1.8843194673 * 10^10`). -/
def protonTrMConventionDScaled1e10 : Nat := 18843194673

/-- Sampled flags in `qou-lt8x` that were non-Convention-C artifacts (`3` of `4`). -/
def sampleNonConventionCFlags : Nat := 3

/-- Total sampled flags in `qou-lt8x`. -/
def sampleTotalFlags : Nat := 4

/-- Exact blast-radius counts (`23 - 14 = 9`, `4 - 3 = 1`) and cross-multiplied
    inequality proving `(tr_M_D - tr_M_C) / tr_M_C > 15.3%`. -/
theorem matrix_m_migration_blast_radius_and_trm_shift :
    downstreamMatrixMProducers - downstreamMatrixMWitnesses = 9 ∧
    sampleTotalFlags - sampleNonConventionCFlags = 1 ∧
    migratedUpstreamMatrixMWitnesses < downstreamMatrixMWitnesses ∧
    (protonTrMConventionDScaled1e10 - protonTrMConventionCScaled1e10) * 1000 >
      153 * protonTrMConventionCScaled1e10 := by
  decide

/-! ## 3. Import-Time `mp.dps` Call-Chain Safety and Blind-Spot Closure (`qou-pgr1`) -/

/-- Total position-risky import-time `mp.dps` sites baselined across 11 files. -/
def totalPositionRiskyDpsSites : Nat := 20

/-- Sites preceded by an import-time `mp.dps` raise. -/
def importRaisePrecededSites : Nat := 15

/-- Sites inside deferred `lambda` or `def` bodies. -/
def deferredBodyDpsSites : Nat := 5

/-- Proven-lossy sites among the 20 position-risky sites. -/
def provenLossyDpsSites : Nat := 0

/-- Total witnesses scanned by `witness_provenance_attribution_audit.py`. -/
def totalAttributionScannedWitnesses : Nat := 2966

/-- Witnesses recording a producer directly. -/
def directProducerRecordedWitnesses : Nat := 2610

/-- Blind-spot witnesses recording no producer (`2966 - 2610 = 356`). -/
def unrecordedProducerBlindSpot : Nat := 356

/-- Blind-spot witnesses recovered by source-verified attribution. -/
def sourceVerifiedAttributedWitnesses : Nat := 256

/-- Blind-spot witnesses with a stem-only match (unverified guess). -/
def stemOnlyGuessWitnesses : Nat := 9

/-- Blind-spot witnesses with no matching producer stem at all. -/
def noProducerStemWitnesses : Nat := 91

/-- Residual unverified invisible witness set (`9 + 91 = 100`). -/
def residualInvisibleWitnesses : Nat := 100

/-- Exact partition of the `20` safe `mp.dps` sites (`15 + 5 = 20`) and the `356`
    provenance blind-spot witnesses (`256 + 9 + 91 = 356`, closing `> 71.9%`). -/
theorem import_dps_safety_and_provenance_blind_spot_closure :
    importRaisePrecededSites + deferredBodyDpsSites = totalPositionRiskyDpsSites ∧
    provenLossyDpsSites = 0 ∧
    directProducerRecordedWitnesses + unrecordedProducerBlindSpot =
      totalAttributionScannedWitnesses ∧
    stemOnlyGuessWitnesses + noProducerStemWitnesses = residualInvisibleWitnesses ∧
    sourceVerifiedAttributedWitnesses + residualInvisibleWitnesses =
      unrecordedProducerBlindSpot ∧
    sourceVerifiedAttributedWitnesses * 1000 > 719 * unrecordedProducerBlindSpot := by
  decide

/-! ## 4. Direct `json.dump` Witness Writers and Backfilled Pin Decay (`qou-pin5`) -/

/-- Approximate total witness producers in corpus. -/
def totalCorpusProducers : Nat := 780

/-- Producers calling `stamp_staleness_metadata`. -/
def stalenessStampingProducers : Nat := 184

/-- Producers not calling `stamp_staleness_metadata` (`780 - 184 = 596`). -/
def nonStampingProducers : Nat := 596

/-- Producers writing witnesses via raw `json.dump` (no `WitnessBuilder`). -/
def rawJsonDumpProducers : Nat := 436

/-- Initial backfilled pinned witnesses written by raw `json.dump` producers (`1 + 14 = 15`). -/
def initialBackfilledPinnedDumpWitnesses : Nat := 15

/-- Pinned witness repaired via `WitnessBuilder.stamp_staleness_metadata` (`t25_cinquefoil`). -/
def repairedPinnedDumpWitnesses : Nat := 1

/-- Remaining pinned witnesses one regeneration away from losing `q0Anchor`. -/
def remainingVulnerablePinnedWitnesses : Nat := 14

/-- Unpinned raw `json.dump` producers (`436 - 15 = 421`). -/
def unpinnedRawJsonDumpProducers : Nat := 421

/-- `Q0_OK` count before and after the `t25_cinquefoil` pin drop/restoration (`565 + 1 = 566`). -/
def q0OkDroppedCount : Nat := 565
def q0OkRestoredCount : Nat := 566

/-- Exact partition of the `780` corpus producers and the `436` raw `json.dump` writers. -/
theorem direct_json_dump_pin_decay_accounting :
    stalenessStampingProducers + nonStampingProducers = totalCorpusProducers ∧
    repairedPinnedDumpWitnesses + remainingVulnerablePinnedWitnesses =
      initialBackfilledPinnedDumpWitnesses ∧
    initialBackfilledPinnedDumpWitnesses + unpinnedRawJsonDumpProducers =
      rawJsonDumpProducers ∧
    q0OkDroppedCount + repairedPinnedDumpWitnesses = q0OkRestoredCount := by
  decide

/-! ## 5. `q0-anchor` Refill Ratchet Five-Day Arrival Trajectory (`qou-q0rf`) -/

/-- Daily unstamped witness arrivals across 2026-08-29..2026-09-02 `[4, 74, 48, 16, 5]`. -/
def fiveDayUnstampedArrivals : List Nat := [4, 74, 48, 16, 5]

/-- Total new unstamped witnesses across the 5-day window. -/
def fiveDayTotalNewUnstamped : Nat := 147

/-- Same-afternoon re-measured NEW unstamped witness count (`147 + 3 = 150`). -/
def afternoonRemeasuredNewUnstamped : Nat := 150

/-- Previous and current `q0-anchor-missing-baseline.json` counts (`1678 -> 1677`). -/
def priorMissingBaselineCount : Nat := 1678
def currentMissingBaselineCount : Nat := 1677

/-- Previous and current live unstamped witness counts (`1627 -> 1742`). -/
def priorLiveUnstampedCount : Nat := 1627
def currentLiveUnstampedCount : Nat := 1742

/-- Within-session witnesses drained and replaced (`4` drained, `3` new + `1` stripped = `4` arrived). -/
def sessionDrainedWitnesses : Nat := 4
def sessionNewFileArrivals : Nat := 3
def sessionStrippedStampArrivals : Nat := 1
def sessionNetNewCount : Nat := 14

/-- Exact 5-day arrival sum (`147`), baseline drain (`1`), and within-session `1:1`
    replacement invariance (`14 - 4 + (3 + 1) = 14`). -/
theorem q0_anchor_refill_arrival_and_session_replacement :
    fiveDayUnstampedArrivals.length = 5 ∧
    fiveDayUnstampedArrivals.sum = fiveDayTotalNewUnstamped ∧
    fiveDayTotalNewUnstamped + 3 = afternoonRemeasuredNewUnstamped ∧
    priorMissingBaselineCount - currentMissingBaselineCount = 1 ∧
    currentLiveUnstampedCount - priorLiveUnstampedCount = 115 ∧
    sessionNewFileArrivals + sessionStrippedStampArrivals = sessionDrainedWitnesses ∧
    sessionNetNewCount - sessionDrainedWitnesses +
      (sessionNewFileArrivals + sessionStrippedStampArrivals) = sessionNetNewCount := by
  decide

end QOU.Eightfold.ProximityDetectorFalsePositivesMatrixMMigrationBlastRadiusImportDpsCallChainSafetyDirectJsonDumpPinDecayAndAnchorRefillArrivalRate
