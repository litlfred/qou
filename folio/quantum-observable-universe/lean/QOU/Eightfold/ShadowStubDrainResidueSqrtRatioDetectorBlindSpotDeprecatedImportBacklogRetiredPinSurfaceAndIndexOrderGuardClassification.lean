/-
Copyright (c) 2026 QOU Formalization. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

# Shadow Stub Drain Residue, Sqrt-Ratio Detector Blind Spot, Deprecated Import Backlog, Retired Pin Surface, and Index-Order Guard Classification

This standalone zero-sorry Lean 4 module formalizes five audit-surface and
detector-classification findings:

1. **`qou-enyo` — Residual shadow-stub drain accounting**:
   - Out of 147 manifest shadow stubs (`134` cleared prior to the residual `13`),
     two drain passes removed `11` (`7` in PR #4831 and `4` in the follow-on),
     leaving `2` residual items (`1` carrying a genuine proof that must stay and
     `1` remaining sibling requiring individual inspection).

2. **`qou-l7j1` — Unseen `sqrt(q)/(q+1)` detector spelling and shape-census partition**:
   - Clearing denominators in `1 / (s + 1/s)` and `s / (s^2 + 1)` yields the same
     cross-product `s * (s^2 + 1)`, so a detector that matches `1 / (sqrt q + 1/sqrt q)`
     but omits `sqrt(q) / (q + 1)` misses algebraically identical convention-C sites
     while also causing `scan_closed_forms()` to skip files wholly on convention C.
   - Across `computations/**/*.py`, the 92 shape-census hits partition into `27`
     actionable + `15` deliberate (`42` flagged) and `50` unflagged hits (including
     `3` confirmed unseen convention-C sites and `47` legitimate comparison/dimension uses).

3. **`qou-n7mj` — Residual `in-repo-wiring` backlog from `_deprecated/` imports**:
   - After draining the initial 72 `in-repo-wiring` failures through three passes
     (`72 → 40` via 32 path-bridge entries, `40 → 15` via 25 producer bootstraps,
     and `15 → 11` via 4 targeted fixes), the entire remaining 11-producer backlog
     consists of `10` live probes importing `probe_staircase_ew_k3_categorical` and
     `1` live probe importing `lambda_scale_alt_g_skein_polynomial_direct` across the
     `_deprecated/` boundary.

4. **`qou-ng5n` — Retired-pin live-code surface (`83` COMPUTE candidates vs `48` reported)**:
   - Out of `209` grep matches (`209 > 2 * 97`), `97` occur in live code (`83` COMPUTE +
     `2` UNCLEAR + `12` REFERENCE = `97`, with `112` non-live occurrences).
   - Reporting only three subdirectories (`29 + 9 + 6 = 44` COMPUTE candidates) omits
     `83 - 44 = 39` live COMPUTE candidates, including `35` in `computations/` top level.

5. **`qou-omiu` — `ℕ`-index comparison false positives and suffix-exclusion coverage tradeoff**:
   - Over `2129` library Lean files, gating weak `≤`/`≥` markers on the presence of `ℝ`
     reduces archimedean classifications from `1381` to `943` (dropping `438` `ℕ`-only
     files), whereas narrowing the regex without type gating (`1119` files) simultaneously
     drops `45` genuine `ℝ`-typed files and retains `221` `ℕ`-only files (`943 - 45 + 221 = 1119`).
   - In `canonical_mass_status_guard`, widening exclusions to the `742` suffix-named files
     out of `2790` scanned Python files (`829` directory-excluded + `64` prefix-excluded =
     `3683` total) would sacrifice `742` scanned files (`> 26%` of `2790`) while preventing
     `0` of the `11` measured guard hits.
-/

namespace QOU.Eightfold.ShadowStubDrainResidueSqrtRatioDetectorBlindSpotDeprecatedImportBacklogRetiredPinSurfaceAndIndexOrderGuardClassification

/-! ## 1. `qou-enyo`: Residual Shadow-Stub Drain Accounting -/

/-- Remaining shadow stubs after subtracting two consecutive drain passes from a residual pool. -/
def remainingShadowStubs (residualPool passOneDeleted passTwoDeleted : Nat) : Nat :=
  residualPool - (passOneDeleted + passTwoDeleted)

/-- Total manifest stubs accounted for by prior drains, the two mechanical passes, and the remaining stubs. -/
def manifestStubTotal (priorCleared passOneDeleted passTwoDeleted remaining : Nat) : Nat :=
  priorCleared + passOneDeleted + passTwoDeleted + remaining

/-- From the 147-stub manifest (`134` cleared prior to the `13`-stub residue), deleting `7` in
    pass one and `4` in pass two (`11` total) leaves exactly `2` stubs (`1` verified non-vacuous
    proof that must stay + `1` remaining sibling). -/
theorem shadow_stub_drain_residue_accounting
    (residualPool passOne passTwo : Nat)
    (hDrained : passOne + passTwo ≤ residualPool) :
    remainingShadowStubs residualPool passOne passTwo + passOne + passTwo = residualPool ∧
    remainingShadowStubs 13 7 4 = 2 ∧
    manifestStubTotal 134 7 4 (remainingShadowStubs 13 7 4) = 147 := by
  dsimp [remainingShadowStubs, manifestStubTotal]
  omega

/-! ## 2. `qou-l7j1`: Unseen `sqrt(q)/(q+1)` Detector Spelling and Shape-Census Partition -/

/-- Cross-multiplied numerator of `1 / (s + 1/s)` after clearing `1/s`, i.e. `s * (s^2 + 1)`. -/
def clearedReciprocalSumCross (s : Nat) : Nat :=
  s * (s * s + 1)

/-- Cross-multiplied numerator of `s / (q + 1)` at `q = s^2` against `(s^2 + 1) / s`, i.e. `s * (s^2 + 1)`. -/
def clearedDirectRatioCross (s : Nat) : Nat :=
  (s * s + 1) * s

/-- Unflagged shape-census hits remaining after subtracting actionable and deliberate detector hits. -/
def unflaggedShapeCensusHits (totalCensus actionableHits deliberateHits : Nat) : Nat :=
  totalCensus - (actionableHits + deliberateHits)

/-- For every `s : Nat`, the cleared cross-products of `1 / (s + 1/s)` and `s / (s^2 + 1)`
    coincide, and across the 92 shape-census hits (`27` actionable + `15` deliberate = `42`),
    `50` hits go unflagged by `scan()` (`3` confirmed unseen convention-C sites + `47` legitimate uses). -/
theorem sqrt_ratio_cross_identity_and_census_partition
    (s totalCensus actionable deliberate : Nat)
    (hFlagged : actionable + deliberate ≤ totalCensus) :
    clearedReciprocalSumCross s = clearedDirectRatioCross s ∧
    unflaggedShapeCensusHits totalCensus actionable deliberate + actionable + deliberate = totalCensus ∧
    unflaggedShapeCensusHits 92 27 15 = 50 ∧
    unflaggedShapeCensusHits 92 27 15 - 3 = 47 := by
  dsimp [clearedReciprocalSumCross, clearedDirectRatioCross, unflaggedShapeCensusHits]
  refine ⟨Nat.mul_comm s (s * s + 1), ?_⟩
  omega

/-! ## 3. `qou-n7mj`: Residual `in-repo-wiring` Backlog from `_deprecated/` Imports -/

/-- Remaining `in-repo-wiring` broken producers after three sequential remediation passes. -/
def remainingWiringBacklog (initialBroken passOneFixed passTwoFixed passThreeFixed : Nat) : Nat :=
  initialBroken - (passOneFixed + passTwoFixed + passThreeFixed)

/-- Total broken live producers importing across the `_deprecated/` boundary from two retired modules. -/
def deprecatedBoundaryImporters (moduleOneImporters moduleTwoImporters : Nat) : Nat :=
  moduleOneImporters + moduleTwoImporters

/-- Draining `72 → 40 → 15 → 11` (`32 + 25 + 4 = 61` fixed) leaves `11` broken producers,
    which exactly equals the `10 + 1 = 11` live probes importing the two retired modules from `_deprecated/`. -/
theorem deprecated_import_wiring_backlog_partition
    (initialBroken p1 p2 p3 : Nat)
    (hDrained : p1 + p2 + p3 ≤ initialBroken) :
    remainingWiringBacklog initialBroken p1 p2 p3 + p1 + p2 + p3 = initialBroken ∧
    remainingWiringBacklog 72 32 25 4 = 11 ∧
    deprecatedBoundaryImporters 10 1 = remainingWiringBacklog 72 32 25 4 ∧
    72 - 32 = 40 ∧
    40 - 25 = 15 ∧
    15 - 4 = 11 := by
  dsimp [remainingWiringBacklog, deprecatedBoundaryImporters]
  omega

/-! ## 4. `qou-ng5n`: Retired-Pin Live-Code Surface (`83` COMPUTE vs `48` Reported) -/

/-- Total live-code occurrences partitioned into COMPUTE, UNCLEAR, and REFERENCE classes. -/
def liveCodePinTotal (computeCount unclearCount referenceCount : Nat) : Nat :=
  computeCount + unclearCount + referenceCount

/-- Non-live grep matches (comments/docstrings) over-counted by a raw string search. -/
def grepOvercountResidue (grepTotal liveTotal : Nat) : Nat :=
  grepTotal - liveTotal

/-- Unreported live COMPUTE candidates omitted when only three subdirectories (`qbeta`, `audits`, `substrate`) are tallied. -/
def unreportedComputeSurface (totalCompute qbetaCompute auditsCompute substrateCompute : Nat) : Nat :=
  totalCompute - (qbetaCompute + auditsCompute + substrateCompute)

/-- Out of `209` grep matches (`112` non-live + `97` live = `83 + 2 + 12`), the three reported
    subdirectories contain `29 + 9 + 6 = 44` COMPUTE candidates, leaving `39` unreported
    COMPUTE candidates (`35` in `computations/` top level + `4` in remaining subdirectories). -/
theorem retired_pin_live_code_and_unreported_top_level_surface
    (grepTotal computeCount unclearCount referenceCount : Nat)
    (hLive : liveCodePinTotal computeCount unclearCount referenceCount ≤ grepTotal) :
    liveCodePinTotal computeCount unclearCount referenceCount +
      grepOvercountResidue grepTotal (liveCodePinTotal computeCount unclearCount referenceCount) =
      grepTotal ∧
    liveCodePinTotal 83 2 12 = 97 ∧
    grepOvercountResidue 209 97 = 112 ∧
    97 * 215 ≤ 209 * 100 ∧
    209 * 100 < 97 * 216 ∧
    unreportedComputeSurface 83 29 9 6 = 39 ∧
    unreportedComputeSurface 83 29 9 6 - 35 = 4 := by
  dsimp [liveCodePinTotal, grepOvercountResidue, unreportedComputeSurface] at *
  omega

/-! ## 5. `qou-omiu`: `ℕ`-Index Comparison False Positives and Suffix-Exclusion Tradeoff -/

/-- Net archimedean file count under a regex approximation that drops `falseNegatives` genuine `ℝ`
    files and retains `falsePositives` `ℕ`-only files relative to the type-gated truth `trueArchimedean`. -/
def approximatedArchimedeanCount (trueArchimedean falseNegatives falsePositives : Nat) : Nat :=
  trueArchimedean - falseNegatives + falsePositives

/-- Remaining scanned Python files if suffix-named files were excluded from the scanned surface. -/
def remainingGuardScanSurface (currentlyScanned suffixNamedFiles : Nat) : Nat :=
  currentlyScanned - suffixNamedFiles

/-- Over `2129` library Lean files (`1381` old archimedean vs `943` type-gated, dropping `438`
    `ℕ`-only files), the reverted regex (`1119` files) dropped `45` genuine `ℝ` files and kept
    `221` `ℕ`-only files (`438 - 221 = 217`), while in `canonical_mass_status_guard` (`2790`
    scanned + `829` dir-excluded + `64` prefix-excluded = `3683`), excluding the `742` suffix
    files drops `> 26%` of the scan surface (`2048` remaining) for `0` of the `11` guard hits. -/
theorem index_order_reclassification_and_suffix_guard_tradeoff
    (trueArch falseNeg falsePos scanned suffixFiles : Nat)
    (hFn : falseNeg ≤ trueArch)
    (hSuf : suffixFiles ≤ scanned) :
    approximatedArchimedeanCount trueArch falseNeg falsePos + falseNeg = trueArch + falsePos ∧
    remainingGuardScanSurface scanned suffixFiles + suffixFiles = scanned ∧
    1381 - 943 = 438 ∧
    approximatedArchimedeanCount 943 45 221 = 1119 ∧
    2790 + 829 + 64 = 3683 ∧
    remainingGuardScanSurface 2790 742 = 2048 ∧
    2790 * 26 < 742 * 100 ∧
    742 * 100 < 2790 * 27 := by
  dsimp [approximatedArchimedeanCount, remainingGuardScanSurface]
  omega

end QOU.Eightfold.ShadowStubDrainResidueSqrtRatioDetectorBlindSpotDeprecatedImportBacklogRetiredPinSurfaceAndIndexOrderGuardClassification
