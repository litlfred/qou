-- Trigger CI
import Lean

/-!
# Witnessed-Values Pin Spread, Second Laundering Surface, Short-Decimal 60-dps Record, Raw-Float64 Backlog Triage, and Three-Path Bridge/Peel Disagreement (`qou-q2xx`, `qou-q5pf`, `qou-rj7d`, `qou-sa14`, `qou-tfj0`)

This standalone core Lean 4.24.0 module formalizes five quantitative measurement and
audit accounting beans from the `qou-9nnz` sub-tree:

1. **`qou-q2xx` (Witnessed-Values Hardcoded Pin Spread & Stale `q0` Occurrences):**
   Hardcoded `hbar_q` values scaled at `10^5` (`9905`, `9908`, `9889`) have adjacent spreads
   `9908 - 9905 = 3` and `9908 - 9889 = 19`; `q|_U` central values scaled at `10^5`
   (`110998` vs `110970`) differ by `28`; muon ratios scaled at `10^1` (`2076` vs `2068`)
   differ by `8`; `c_q^2` values scaled at `10^1` (`832` vs `827`) differ by `5`; and the
   stale `q0` literal appears `43` times across the corpus.

2. **`qou-q5pf` (Second Laundering Surface — Pasted Decimal Literals in High-DPS Files):**
   An AST scan for `mp.mpf("<decimal>")` whose significant-digit count is at least `8`
   below the file's working `mp.mp.dps` identifies `153` candidate files and `309` candidate
   sites, alongside `35` drained `LAUNDERED`-tier sites, while the `4` sampled input/literature
   constants (`(12, 60)`, `(10, 80)`, `(48, 60)`, `(13, 110)`) all satisfy `dps - digits >= 8`.

3. **`qou-rj7d` (60-DPS Record of a Short Decimal — Two-Pass Witness Reconstruction):**
   Across `3745` committed witnesses, Pass 1 heuristic flags `1489` fields in `144` witnesses,
   whereas Pass 2 exact character-for-character reconstruction over `4` build precisions
   `{50, 53, 60, 70}` and `4` output precisions `{60, 65, 67, 70}` (`16` precision pairs)
   confirms `734` fields across `94` witnesses and leaves `745` unconfirmed fields across
   `59` witnesses, with the top `11` carriers accounting for `496` of the `734` confirmed fields.

4. **`qou-sa14` (Raw-Float64 Backlog Triage & Corrected On-Disk Queue Accounting):**
   Across `1003` baseline entries (`30985` baseline fields), first-pass bucketing over `980`
   dirty files partitions `29023` fields into scalar (`827` files, `20781` fields), matrix
   (`102` files, `4237` fields), LP-solver (`46` files, `3819` fields), and mixed (`5` files,
   `186` fields); corrected on-disk accounting partitions `1003 = 24 + 979` entries and
   `30985 = 5094 + 25891` baseline fields, with `25725` live on-disk dirty fields minus `21`
   orphan entries (`1550 = 615 + 935` fields) leaving `958` drainable entries and `24175`
   drainable fields.

5. **`qou-tfj0` (Three-Path Comparison Bridge vs Peel Disagreement Under Vacuous Assertion):**
   For the `4` light nuclides (`D`, `T`, `3He`, `4He`), the recorded `bridge_canonical` and
   `peel_path` values scaled at `10^4` (`(5752, 3883)`, `(2293, 1041)`, `(4038, 2065)`,
   `(0, 553)`) all violate the `10^-3` relative agreement criterion
   (`1000 * |bridge - peel| < bridge` with `bridge > 0`), while `0` recorded assertions make
   the vacuous conjunction pass.
-/

namespace QOU.Eightfold.WitnessedValuesPinSpreadSecondLaunderingSurfaceShortDecimalRecordRawFloat64BacklogTriageAndThreePathBridgePeelDisagreement

/-! ## 1. `qou-q2xx`: Witnessed-Values Hardcoded Pin Spread & Stale `q0` Occurrences -/

/-- Hardcoded `hbar_q` values scaled by `10^5` across observation blocks (`qou-q2xx`). -/
def hbarQTableScaled : Nat := 9905
def hbarQProofScaled : Nat := 9908
def hbarQTerminalScaled : Nat := 9889

/-- Hardcoded `q|_U` central values scaled by `10^5` (`1.10970` vs `1.10998`, `qou-q2xx`). -/
def qCentralLowScaled : Nat := 110970
def qCentralHighScaled : Nat := 110998

/-- Hardcoded muon mass ratios scaled by `10^1` (`207.6` vs `206.8`, `qou-q2xx`). -/
def muonTerminalScaled : Nat := 2076
def muonCanonicalScaled : Nat := 2068

/-- Hardcoded `c_q^2` values scaled by `10^1` (`83.2` vs `82.7`, `qou-q2xx`). -/
def cqSqHighScaled : Nat := 832
def cqSqLowScaled : Nat := 827

/-- Corpus-wide count of the stale `q0` literal string (`qou-q2xx`). -/
def staleQ0CorpusOccurrences : Nat := 43

/-- Exact pin spread and stale-occurrence accounting for `qou-q2xx`. -/
theorem witnessed_values_pin_spread_exact :
    hbarQProofScaled - hbarQTableScaled = 3 ∧
    hbarQProofScaled - hbarQTerminalScaled = 19 ∧
    hbarQTableScaled - hbarQTerminalScaled = 16 ∧
    qCentralHighScaled - qCentralLowScaled = 28 ∧
    muonTerminalScaled - muonCanonicalScaled = 8 ∧
    cqSqHighScaled - cqSqLowScaled = 5 ∧
    staleQ0CorpusOccurrences = 43 := by
  decide

/-! ## 2. `qou-q5pf`: Second Laundering Surface — Pasted Decimal Literals in High-DPS Files -/

/-- Candidate file and site counts from the AST digit-gap scan (`qou-q5pf`). -/
def secondSurfaceCandidateFiles : Nat := 153
def secondSurfaceCandidateSites : Nat := 309
def drainedFirstSurfaceSites : Nat := 35
def minDigitGapThreshold : Nat := 8

/-- Sampled `(significant_digits, file_working_dps)` pairs from `qou-q5pf`. -/
def sampledLiteralDigitDpsPairs : List (Nat × Nat) :=
  [(12, 60), (10, 80), (48, 60), (13, 110)]

/-- Predicate testing whether a `(digits, dps)` site triggers the `>= 8` digit-gap scan. -/
def triggersDigitGapScan (p : Nat × Nat) : Bool :=
  decide (p.1 + minDigitGapThreshold ≤ p.2)

/-- Exact candidate-surface and sampled-site digit-gap verification for `qou-q5pf`. -/
theorem second_laundering_surface_candidates_exact :
    secondSurfaceCandidateFiles = 153 ∧
    secondSurfaceCandidateSites = 309 ∧
    secondSurfaceCandidateSites - secondSurfaceCandidateFiles = 156 ∧
    drainedFirstSurfaceSites = 35 ∧
    sampledLiteralDigitDpsPairs.length = 4 ∧
    sampledLiteralDigitDpsPairs.all triggersDigitGapScan = true ∧
    (sampledLiteralDigitDpsPairs.map (fun p => p.2 - p.1)).sum = 227 := by
  decide

/-! ## 3. `qou-rj7d`: 60-DPS Record of a Short Decimal — Two-Pass Witness Reconstruction -/

/-- Total committed witnesses scanned and Pass 1 / Pass 2 counts (`qou-rj7d`). -/
def committedWitnessesScanned : Nat := 3745
def pass1HeuristicFields : Nat := 1489
def pass1HeuristicWitnesses : Nat := 144
def pass2ConfirmedFields : Nat := 734
def pass2ConfirmedWitnesses : Nat := 94
def pass2UnconfirmedFields : Nat := 745
def pass2UnconfirmedWitnesses : Nat := 59

/-- Build precisions `B` and output precisions `O` tested in Pass 2 (`qou-rj7d`). -/
def pass2BuildPrecisions : List Nat := [50, 53, 60, 70]
def pass2OutputPrecisions : List Nat := [60, 65, 67, 70]

/-- Confirmed field counts in the top `11` carrier witnesses (`qou-rj7d`). -/
def top11ConfirmedCarrierCounts : List Nat :=
  [108, 105, 104, 35, 28, 28, 24, 18, 18, 14, 14]

/-- Exact two-pass reconstruction and carrier-concentration identities for `qou-rj7d`. -/
theorem short_decimal_60dps_record_exact :
    committedWitnessesScanned = 3745 ∧
    pass2BuildPrecisions.length * pass2OutputPrecisions.length = 16 ∧
    pass2ConfirmedFields + pass2UnconfirmedFields = 1479 ∧
    pass1HeuristicFields - pass2ConfirmedFields = 755 ∧
    top11ConfirmedCarrierCounts.length = 11 ∧
    top11ConfirmedCarrierCounts.sum = 496 ∧
    pass2ConfirmedFields - top11ConfirmedCarrierCounts.sum = 238 ∧
    pass2ConfirmedWitnesses - top11ConfirmedCarrierCounts.length = 83 := by
  decide

/-! ## 4. `qou-sa14`: Raw-Float64 Backlog Triage & Corrected On-Disk Queue Accounting -/

/-- First-pass `(files, fields)` buckets across the `980` dirty entries (`qou-sa14`). -/
def firstPassTriageBuckets : List (Nat × Nat) :=
  [(827, 20781), (102, 4237), (46, 3819), (5, 186)]

/-- Baseline and corrected on-disk queue figures (`qou-sa14`). -/
def baselineTotalEntries : Nat := 1003
def baselineTotalFields : Nat := 30985
def correctedCleanEntriesOnDisk : Nat := 24
def correctedCleanBaselineFields : Nat := 5094
def correctedDirtyEntriesOnDisk : Nat := 979
def correctedDirtyBaselineFields : Nat := 25891
def correctedDirtyOnDiskFields : Nat := 25725
def orphanEntriesTotal : Nat := 21
def orphanEntriesCleanTwinDetected : Nat := 4
def orphanEntriesDirtyTwinMissed : Nat := 17
def orphanFieldsTotal : Nat := 1550
def orphanFieldsCleanTwinDetected : Nat := 615
def orphanFieldsDirtyTwinMissed : Nat := 935

/-- Exact bucket partition, on-disk correction, and orphan subtraction for `qou-sa14`. -/
theorem raw_float64_backlog_triage_exact :
    (firstPassTriageBuckets.map Prod.fst).sum = 980 ∧
    (firstPassTriageBuckets.map Prod.snd).sum = 29023 ∧
    20781 * 100 / 29023 = 71 ∧
    correctedCleanEntriesOnDisk + correctedDirtyEntriesOnDisk = baselineTotalEntries ∧
    correctedCleanBaselineFields + correctedDirtyBaselineFields = baselineTotalFields ∧
    correctedDirtyBaselineFields - correctedDirtyOnDiskFields = 166 ∧
    orphanEntriesCleanTwinDetected + orphanEntriesDirtyTwinMissed = orphanEntriesTotal ∧
    orphanFieldsCleanTwinDetected + orphanFieldsDirtyTwinMissed = orphanFieldsTotal ∧
    correctedDirtyEntriesOnDisk - orphanEntriesTotal = 958 ∧
    correctedDirtyOnDiskFields - orphanFieldsTotal = 24175 := by
  decide

/-! ## 5. `qou-tfj0`: Three-Path Bridge vs Peel Disagreement Under Vacuous Assertion -/

/-- Recorded `(bridge_canonical, peel_path)` values scaled at `10^4` for `D, T, 3He, 4He` (`qou-tfj0`). -/
def threePathBridgePeelScaled : List (Nat × Nat) :=
  [(5752, 3883), (2293, 1041), (4038, 2065), (0, 553)]

/-- Absolute difference `|a - b|` on natural numbers. -/
def natAbsDiff (a b : Nat) : Nat :=
  if a ≥ b then a - b else b - a

/-- Test whether a `(bridge, peel)` pair passes the `10^-3` relative agreement check. -/
def passesOnePerMilleRelativeBar (bp : Nat × Nat) : Bool :=
  decide (bp.1 > 0 ∧ 1000 * natAbsDiff bp.1 bp.2 < bp.1)

/-- Exact verification that all four nuclides fail the `10^-3` bar while the empty assertion list passes (`qou-tfj0`). -/
theorem three_path_bridge_peel_disagreement_exact :
    threePathBridgePeelScaled.length = 4 ∧
    (threePathBridgePeelScaled.map (fun bp => natAbsDiff bp.1 bp.2)) = [1869, 1252, 1973, 553] ∧
    threePathBridgePeelScaled.all (fun bp => !passesOnePerMilleRelativeBar bp) = true ∧
    ([] : List Bool).all id = true := by
  decide

end QOU.Eightfold.WitnessedValuesPinSpreadSecondLaunderingSurfaceShortDecimalRecordRawFloat64BacklogTriageAndThreePathBridgePeelDisagreement
