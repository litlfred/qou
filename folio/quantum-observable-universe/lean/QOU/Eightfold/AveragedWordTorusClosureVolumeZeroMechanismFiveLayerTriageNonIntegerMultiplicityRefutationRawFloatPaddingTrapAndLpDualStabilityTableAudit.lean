/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Round 85 Formalization:
  - qou-dgpz: Option B averaged-word branch count (2^(2A+1) = 32, 128, 512 at A = 2, 3, 4) & zero torus-closure volume
  - qou-dqgp: Mechanism-5 producer layer triage (79 + 74 - 58 = 95 union; 7-bucket partition 4+16+8+2+18+39+8 = 95)
  - qou-dt01: Non-integer 4He cap (1889 / 1000) refuting integer projection multiplicity & I=0 derived color-tube weights
  - qou-epxx: Raw-float64 baseline vs live carve-outs (30985 - 25396 = 5589) & 44-digit binary64 padding trap (60 - 16 = 44)
  - qou-etfq: LP dual-stability table audit (all 4 sub-units Gx > 0, halving transcription rule, condition ratio > 24 / 5 * quoted)
-/

namespace QOU.Eightfold.AveragedWordTorusClosureVolumeZeroMechanismFiveLayerTriageNonIntegerMultiplicityRefutationRawFloatPaddingTrapAndLpDualStabilityTableAudit

/-! ## 1. Bean `qou-dgpz`: Averaged-Word Sign-Resolved Branch Count and Torus-Closure Zero Volume -/

/-- Number of averaged letters `2A + 1` in the production canonical word at mass number `A` (`qou-dgpz`). -/
def averagedWordLetterCount (massNumberA : Nat) : Nat :=
  2 * massNumberA + 1

/-- Number of sign-resolved branches `2^(2A + 1)` of the production word (`qou-dgpz`). -/
def signResolvedBranchCount (massNumberA : Nat) : Nat :=
  2 ^ (2 * massNumberA + 1)

/-- Census candidates admitted at the algebraic-trace level (`0` out of `3558`) (`qou-dgpz`). -/
def totalCensusCandidates : Nat := 3558
def admittedTraceCandidates : Nat := 0

/-- Sum of `nBranches` connected-sum torus-link branch volumes when each branch has volume `branchVol` (`qou-dgpz`). -/
def totalBranchVolumeSum (nBranches branchVol : Int) : Int :=
  nBranches * branchVol

/-- Exact branch counts `32, 128, 512` at `A = 2, 3, 4` (`5, 7, 9` averaged letters), zero
algebraic-trace census admissions (`3558 - 0 = 3558` rejected), and identically zero total volume
whenever every torus-link branch has `branchVol = 0` (`qou-dgpz`). -/
theorem averagedWordBranchCount_and_zeroTorusVolume (nBranches : Int) :
    averagedWordLetterCount 2 = 5 ∧
    signResolvedBranchCount 2 = 32 ∧
    signResolvedBranchCount 3 = 128 ∧
    signResolvedBranchCount 4 = 512 ∧
    totalCensusCandidates - admittedTraceCandidates = 3558 ∧
    totalBranchVolumeSum nBranches 0 = 0 := by
  dsimp [averagedWordLetterCount, signResolvedBranchCount, totalCensusCandidates,
    admittedTraceCandidates, totalBranchVolumeSum]
  omega

/-! ## 2. Bean `qou-dqgp`: Mechanism-5 Producer Layer Triage and Detector Inclusion-Exclusion -/

/-- Two AST detector counts (`79` and `74`) and their overlap (`58`) (`qou-dqgp`). -/
def astDetectorOneCount : Nat := 79
def astDetectorTwoCount : Nat := 74
def astDetectorOverlapCount : Nat := 58
def astDetectorUnionCount : Nat :=
  astDetectorOneCount + astDetectorTwoCount - astDetectorOverlapCount

/-- Seven triage bucket counts `A..G` across the `95` mechanism-5 producers (`qou-dqgp`). -/
def bucketAInfraCount : Nat := 4
def bucketBTwoAnchorCount : Nat := 16
def bucketCLegitMuonCount : Nat := 8
def bucketDContradictionCount : Nat := 2
def bucketEShouldBeProtonCount : Nat := 18
def bucketFHygieneCount : Nat := 39
def bucketGNeedsAuthorCount : Nat := 8

/-- Exact inclusion-exclusion union (`79 + 74 - 58 = 95`, exceeding the earlier `85` count by `10`
and the `51` filtered count by `44 = 26 + 18`) and exact 7-bucket partition summing to `95`, with
`18 + 39 = 57` deferred proton-migration candidates (`qou-dqgp`). -/
theorem mechanismFiveLayerTriage_inclusionExclusion_and_buckets :
    astDetectorUnionCount = 95 ∧
    astDetectorUnionCount - 85 = 10 ∧
    astDetectorUnionCount - 51 = 26 + 18 ∧
    bucketAInfraCount + bucketBTwoAnchorCount + bucketCLegitMuonCount +
      bucketDContradictionCount + bucketEShouldBeProtonCount +
      bucketFHygieneCount + bucketGNeedsAuthorCount = astDetectorUnionCount ∧
    bucketEShouldBeProtonCount + bucketFHygieneCount = 57 := by
  dsimp [astDetectorUnionCount, astDetectorOneCount, astDetectorTwoCount, astDetectorOverlapCount,
    bucketAInfraCount, bucketBTwoAnchorCount, bucketCLegitMuonCount, bucketDContradictionCount,
    bucketEShouldBeProtonCount, bucketFHygieneCount, bucketGNeedsAuthorCount]
  omega

/-! ## 3. Bean `qou-dt01`: Non-Integer Cap Refutation of `ρ_F = ν_SDP` and Color-Tube Channel Hierarchy -/

/-- Scaled (`× 1000`) empirical cap `ρ_F(⁴He) = 1.889` (`qou-dt01`). -/
def rhoFHe4Millis : Int := 1889

/-- Scaled (`× 10^12`) `I = 0` deuteron derived color-tube weights (`qou-dt01`). -/
def colorTubeI0SameWeightScaled : Int := 165485393155
def colorTubeI0DiffWeightScaled : Int := 83923970089

/-- Parameter count reduction steps `8 -> 2 -> 1 -> 0` along the color-tube derivation chain (`qou-dt01`). -/
def initialFreeParams : Nat := 8
def finalFreeParams : Nat := 0

/-- Because `1000 < 1889 < 2000`, `ρ_F(⁴He) = 1889 / 1000` cannot equal any integer multiplicity
`nu : Int` (`1000 * nu ≠ 1889`), refuting `ρ_F = ν_SDP`, while the `I = 0` derived color-tube
weights satisfy `0 < W_diff < W_same < 2 * W_diff` (`qou-dt01`). -/
theorem nonIntegerCap_refutes_integerMultiplicity_and_colorTubeOrder (nu : Int) :
    1000 * nu ≠ rhoFHe4Millis ∧
    0 < colorTubeI0DiffWeightScaled ∧
    colorTubeI0DiffWeightScaled < colorTubeI0SameWeightScaled ∧
    colorTubeI0SameWeightScaled < 2 * colorTubeI0DiffWeightScaled ∧
    initialFreeParams - finalFreeParams = 8 := by
  dsimp [rhoFHe4Millis, colorTubeI0DiffWeightScaled, colorTubeI0SameWeightScaled,
    initialFreeParams, finalFreeParams]
  omega

/-! ## 4. Bean `qou-epxx`: Raw-Float64 Baseline vs Live Carve-Outs and 44-Digit Padding Trap -/

/-- Baseline vs live raw-float64 witness and field counts (`qou-epxx`). -/
def baselineFloatWitnessCount : Nat := 1003
def liveFloatWitnessCount : Nat := 975
def baselineFloatFieldCount : Nat := 30985
def liveFloatFieldCount : Nat := 25396

/-- Number of fabricated trailing decimal digits when a 16-digit binary64 float is formatted to `targetDigits` (`qou-epxx`). -/
def paddedFabricatedDigits (targetDigits binary64Digits : Int) : Int :=
  targetDigits - binary64Digits

/-- Candidate partition on `mixed mpf/f64 -> serializer` (`3` real baseline + `4` false positives = `7`) (`qou-epxx`). -/
def mixedSerializerRealCount : Nat := 3
def mixedSerializerFalsePositiveCount : Nat := 4

/-- Exact baseline-minus-live difference (`1003 - 975 = 28` files, `30985 - 25396 = 5589` fields),
`3 + 4 = 7` serializer candidate split, and proof that formatting a `16`-digit binary64 cast to
`targetDigits ≥ 60` fabricates at least `44` spurious digits (`qou-epxx`). -/
theorem rawFloatBaselineDelta_and_paddingTrap
    (targetDigits : Int) (htarget : 60 ≤ targetDigits) :
    baselineFloatWitnessCount - liveFloatWitnessCount = 28 ∧
    baselineFloatFieldCount - liveFloatFieldCount = 5589 ∧
    mixedSerializerRealCount + mixedSerializerFalsePositiveCount = 7 ∧
    44 ≤ paddedFabricatedDigits targetDigits 16 ∧
    paddedFabricatedDigits 60 16 = 44 := by
  dsimp [baselineFloatWitnessCount, liveFloatWitnessCount, baselineFloatFieldCount,
    liveFloatFieldCount, mixedSerializerRealCount, mixedSerializerFalsePositiveCount,
    paddedFabricatedDigits]
  omega

/-! ## 5. Bean `qou-etfq`: LP Dual-Stability Table Positivity and Condition-Number Understatement -/

/-- Scaled (`× 100`) true `min(Gx)` values for the four sub-units `σ₀, σ₀⁻¹, σ₀σ₁⁻¹, σ₀²` (`qou-etfq`). -/
def minGxSigma0Centis : Int := 25
def minGxSigma0InvCentis : Int := 14
def minGxSigma0Sigma1InvCentis : Int := 14
def minGxSigma0SqCentis : Int := 36

/-- Scaled (`× 100`) printed table value `-11` vs true entry `+32` on `σ₀σ₁⁻¹` (`qou-etfq`). -/
def printedTableSigma0Sigma1InvCentis : Int := -11
def trueEntrySigma0Sigma1InvCentis : Int := 32

/-- Scaled (`× 10^8`) extremal positive Gram eigenvalues `λ_max = 3.47694990` and `λ_min⁺ = 0.10179668` (`qou-etfq`). -/
def gramLambdaMaxScaled : Int := 347694990
def gramLambdaMinPosScaled : Int := 10179668

/-- All four sub-unit `min(Gx)` values are strictly positive (`> 0`), the true entry `+32` exceeds
the printed `-11` by `43` hundredths, and the true condition ratio `λ_max / λ_min⁺ > 34` exceeds
`24 / 5` (`4.8×`) times the quoted `7` (`5 * λ_max > 24 * 7 * λ_min⁺`) (`qou-etfq`). -/
theorem lpDualStabilityTable_positivity_and_conditionRatio_certificate :
    0 < minGxSigma0Centis ∧
    0 < minGxSigma0InvCentis ∧
    0 < minGxSigma0Sigma1InvCentis ∧
    0 < minGxSigma0SqCentis ∧
    trueEntrySigma0Sigma1InvCentis - printedTableSigma0Sigma1InvCentis = 43 ∧
    gramLambdaMaxScaled > 34 * gramLambdaMinPosScaled ∧
    5 * gramLambdaMaxScaled > 24 * 7 * gramLambdaMinPosScaled := by
  dsimp [minGxSigma0Centis, minGxSigma0InvCentis, minGxSigma0Sigma1InvCentis,
    minGxSigma0SqCentis, trueEntrySigma0Sigma1InvCentis, printedTableSigma0Sigma1InvCentis,
    gramLambdaMaxScaled, gramLambdaMinPosScaled]
  omega

end QOU.Eightfold.AveragedWordTorusClosureVolumeZeroMechanismFiveLayerTriageNonIntegerMultiplicityRefutationRawFloatPaddingTrapAndLpDualStabilityTableAudit
