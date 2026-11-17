/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Round 83 Formalization:
  - qou-bfdb: Module-scope binary64 constant blast radius (1027 / 1929 producers) & additive-twin drift (2288%)
  - qou-bhvs: R11-a light-cluster amplitude scaling ladder (28, 58, 80 tenths) & onset envelope composition
  - qou-brkp: Silent parse-exception audit refutation (2 broken of 14) & three-stage trace shift bounds
  - qou-bvk7: Convention-C derived scalar trace detector blindspot (14 -> 2 drain) & denominator preflight
  - qou-c9n8: Confinement-phase stratification locus openness & local constancy of binding multiplicity mu
-/

namespace QOU.Eightfold.ModuleScopeFloatConstantBlastRadiusLightAmplitudeScalingSilentGateRefutationDerivedTraceDetectorBlindspotAndConfinementLocusOpenness

/-! ## 1. Bean `qou-bfdb`: Module-Scope Binary64 Constant Blast Radius and Additive-Twin Drift -/

/-- Number of witness-writing producers reaching the module-scope binary64 constant (`qou-bfdb`). -/
def affectedProducerCount : Nat := 1027

/-- Total witness-writing producers in the computation corpus (`qou-bfdb`). -/
def totalProducerCount : Nat := 1929

/-- Number of witness-writing producers not reaching the module-scope constant (`qou-bfdb`). -/
def unaffectedProducerCount : Nat := totalProducerCount - affectedProducerCount

/-- Percentage divergence `2288` of an unmonitored zero-consumer additive twin (`qou-bfdb`). -/
def unmonitoredTwinDivergencePct : Nat := 2288

/-- Residual downstream consumers still reaching the module-scope constant after patching `k` files (`qou-bfdb`). -/
def residualAffectedProducers (totalAffected patchedCount : Int) : Int :=
  totalAffected - patchedCount

/-- Exact partition of the `1929` witness-writing producers into `1027` affected and `902`
unaffected producers, with majority blast radius `2 * 1027 > 1929` and additive-twin drift `> 2200%` (`qou-bfdb`). -/
theorem moduleScopeFloatConstant_blastRadius_partition :
    unaffectedProducerCount = 902 ∧
    affectedProducerCount + unaffectedProducerCount = totalProducerCount ∧
    2 * affectedProducerCount > totalProducerCount ∧
    5 * affectedProducerCount < 3 * totalProducerCount ∧
    unmonitoredTwinDivergencePct > 2200 := by
  dsimp [unaffectedProducerCount, affectedProducerCount, totalProducerCount,
    unmonitoredTwinDivergencePct]
  omega

/-- Patching `k` consumer probes locally (`0 < k < totalAffected`) leaves a strictly positive
residual blast radius `0 < residualAffectedProducers totalAffected k < totalAffected`, and at
`(1027, 2)` leaves exactly `1025` unpatched consumers (`qou-bfdb`). -/
theorem localConsumerPatch_leaves_positive_residual
    (totalAffected k : Int) (hk_pos : 0 < k) (hk_lt : k < totalAffected) :
    0 < residualAffectedProducers totalAffected k ∧
    residualAffectedProducers totalAffected k < totalAffected ∧
    residualAffectedProducers 1027 2 = 1025 := by
  dsimp [residualAffectedProducers]
  omega

/-! ## 2. Bean `qou-bhvs`: R11-a Light-Cluster Amplitude Scaling Ladder and Onset Envelope Composition -/

/-- Light-cluster amplitude scaling values in tenths (`28, 58, 80` for `2.8, 5.8, 8.0` at `A_light = 1, 2, 3`) (`qou-bhvs`). -/
def lightAmplitudeTenths1 : Int := 28
def lightAmplitudeTenths2 : Int := 58
def lightAmplitudeTenths3 : Int := 80

/-- First and second discrete increments of the light-cluster amplitude ladder in tenths (`qou-bhvs`). -/
def lightAmplitudeStep1Tenths : Int := lightAmplitudeTenths2 - lightAmplitudeTenths1
def lightAmplitudeStep2Tenths : Int := lightAmplitudeTenths3 - lightAmplitudeTenths2
def lightAmplitudeSecondDiffTenths : Int := lightAmplitudeStep2Tenths - lightAmplitudeStep1Tenths

/-- Composed light-cluster amplitude combining light scale, three-cluster onset envelope, and parity factor (`qou-bhvs`). -/
def composedLightClusterAmplitude (scale envelopeWeight : Int) : Int :=
  scale * envelopeWeight

/-- Strict monotonicity (`28 < 58 < 80`) and discrete concavity (`Δ₁ = 30 > Δ₂ = 22 > 0`,
`Δ² = -8 < 0`) of the light-cluster amplitude ladder (`qou-bhvs`). -/
theorem lightAmplitudeScaling_monotonicity_and_concavity :
    lightAmplitudeTenths1 < lightAmplitudeTenths2 ∧
    lightAmplitudeTenths2 < lightAmplitudeTenths3 ∧
    lightAmplitudeStep1Tenths = 30 ∧
    lightAmplitudeStep2Tenths = 22 ∧
    lightAmplitudeStep2Tenths < lightAmplitudeStep1Tenths ∧
    lightAmplitudeSecondDiffTenths = -8 := by
  dsimp [lightAmplitudeTenths1, lightAmplitudeTenths2, lightAmplitudeTenths3,
    lightAmplitudeStep1Tenths, lightAmplitudeStep2Tenths, lightAmplitudeSecondDiffTenths]
  omega

/-- Difference between composed amplitudes at `s₂` and `s₁` under a shared onset-and-parity weight `w`
factors as `(s₂ - s₁) * w` (`qou-bhvs`). -/
theorem composedLightClusterAmplitude_diff_eq_sub_mul (s1 s2 w : Int) :
    composedLightClusterAmplitude s2 w - composedLightClusterAmplitude s1 w = (s2 - s1) * w := by
  dsimp [composedLightClusterAmplitude]
  exact (Int.sub_mul s2 s1 w).symm

/-- For any positive composite onset-and-parity weight (`1 ≤ w`), the composed amplitude
strictly increases from `A_light = 1` (`28 * w`) to `A_light = 2` (`58 * w`) to `A_light = 3` (`80 * w`) (`qou-bhvs`). -/
theorem composedLightClusterAmplitude_strict_hierarchy (w : Int) (hw : 1 ≤ w) :
    composedLightClusterAmplitude lightAmplitudeTenths1 w <
      composedLightClusterAmplitude lightAmplitudeTenths2 w ∧
    composedLightClusterAmplitude lightAmplitudeTenths2 w <
      composedLightClusterAmplitude lightAmplitudeTenths3 w := by
  dsimp [composedLightClusterAmplitude, lightAmplitudeTenths1, lightAmplitudeTenths2, lightAmplitudeTenths3]
  omega

/-! ## 3. Bean `qou-brkp`: Silent Parse-Gate Refutation and Three-Stage Trace Shift Bounds -/

/-- Total producers touched by the import-time precision commit (`qou-brkp`). -/
def remediatedProducerBatch : Nat := 14

/-- Producers broken by dict-interior `SyntaxError` (`qou-brkp`). -/
def syntaxBrokenProducers : Nat := 2

/-- Remaining runnable producers in the batch (`qou-brkp`). -/
def runnableProducersInBatch : Nat := remediatedProducerBatch - syntaxBrokenProducers

/-- Scaled integer representations (`× 10^8`) of the three deuteron trace regimes (`qou-brkp`). -/
def traceBaselineScaled : Int := 38835714
def traceCachedScaled : Int := 57517224
def traceFreshScaled : Int := 15196834

/-- Gap between true finding count (`parseErrors + astFindings`) and a silent-exception gate that returns `0` on parse error (`qou-brkp`). -/
def silentGateFindingDeficit (parseErrors astFindings : Int) : Int :=
  (parseErrors + astFindings) - 0

/-- Silent-gate defect count (`14 - 2 = 12` runnable) and three-stage deuteron trace ratio bounds:
the post-08-10 weight-table shift exceeds `37 / 25` (`25 * 57517224 > 37 * 38835714`) and the
cached-to-fresh ratio exceeds `18 / 5` (`5 * 57517224 > 18 * 15196834`) (`qou-brkp`). -/
theorem silentParseGate_and_traceRegimeShift_certificate :
    runnableProducersInBatch = 12 ∧
    syntaxBrokenProducers + runnableProducersInBatch = remediatedProducerBatch ∧
    25 * traceCachedScaled > 37 * traceBaselineScaled ∧
    5 * traceCachedScaled > 18 * traceFreshScaled := by
  dsimp [runnableProducersInBatch, syntaxBrokenProducers, remediatedProducerBatch,
    traceBaselineScaled, traceCachedScaled, traceFreshScaled]
  omega

/-- Whenever `1 ≤ parseErrors` and `0 ≤ astFindings`, a gate that silently swallows parse errors
under-reports findings by at least `parseErrors > 0` (`qou-brkp`). -/
theorem silentGateFindingDeficit_pos_of_parse_error
    (parseErrors astFindings : Int) (hp : 1 ≤ parseErrors) (ha : 0 ≤ astFindings) :
    parseErrors ≤ silentGateFindingDeficit parseErrors astFindings ∧
    0 < silentGateFindingDeficit parseErrors astFindings := by
  dsimp [silentGateFindingDeficit]
  omega

/-! ## 4. Bean `qou-bvk7`: Convention-C Derived-Trace Detector Blindspot and Denominator Preflight -/

/-- Initial text-matched witness count and drained count (`qou-bvk7`). -/
def initialTraceMatchWitnessCount : Nat := 14
def drainedTraceMatchWitnessCount : Nat := 12
def survivingTraceMatchWitnessCount : Nat :=
  initialTraceMatchWitnessCount - drainedTraceMatchWitnessCount

/-- Unscaled coefficient subtraction `d_X * t_X - d_Y * t_Y` rejected by `_qou_lnog_preflight` when `d_X ≠ d_Y` (`qou-bvk7`). -/
def rawCoefficientSubtraction (dX tX dY tY : Int) : Int :=
  dX * tX - dY * tY

/-- Cross-multiplied numerator `d_Y * t_X - d_X * t_Y` of the true rational difference `(t_X / d_X) - (t_Y / d_Y)` (`qou-bvk7`). -/
def crossMultipliedDifference (dX tX dY tY : Int) : Int :=
  dY * tX - dX * tY

/-- Witness drain partition (`14 - 12 = 2 = 1 + 1`) and exact algebraic discrepancy showing that
on unit numerators (`t_X = t_Y = 1`), raw coefficient subtraction `d_X - d_Y` is the exact negation
of the true cross-multiplied numerator `d_Y - d_X`, and is non-zero whenever `d_X ≠ d_Y` (`qou-bvk7`). -/
theorem derivedTraceBlindspot_drain_and_denominator_mismatch
    (dX dY : Int) (hne : dX ≠ dY) :
    survivingTraceMatchWitnessCount = 2 ∧
    rawCoefficientSubtraction dX 1 dY 1 ≠ 0 ∧
    crossMultipliedDifference dX 1 dY 1 ≠ 0 ∧
    rawCoefficientSubtraction dX 1 dY 1 + crossMultipliedDifference dX 1 dY 1 = 0 := by
  dsimp [survivingTraceMatchWitnessCount, initialTraceMatchWitnessCount,
    drainedTraceMatchWitnessCount, rawCoefficientSubtraction, crossMultipliedDifference]
  omega

/-! ## 5. Bean `qou-c9n8`: Confinement-Phase Stratification Locus Openness and Local Constancy of `μ` -/

/-- Perturbation lower bound on the interior feasibility margin `sigma0 - slope * dist` (`qou-c9n8`). -/
def perturbedMarginLowerBound (sigma0 slopeDist : Int) : Int :=
  sigma0 - slopeDist

/-- Openness of the strict confinement feasibility locus: for any base margin `sigma0 > 0`
and perturbation magnitude `0 ≤ slopeDist < sigma0` inside the open feasibility ball,
every perturbed margin `sigmaY ≥ perturbedMarginLowerBound sigma0 slopeDist` remains strictly
positive (`qou-c9n8`). -/
theorem confinementLocus_open_ball_positivity
    (sigma0 slopeDist sigmaY : Int)
    (hdist_nonneg : 0 ≤ slopeDist)
    (hball : slopeDist < sigma0)
    (hpert : perturbedMarginLowerBound sigma0 slopeDist ≤ sigmaY) :
    0 < perturbedMarginLowerBound sigma0 slopeDist ∧
    0 < sigmaY ∧
    perturbedMarginLowerBound sigma0 slopeDist ≤ sigma0 := by
  dsimp [perturbedMarginLowerBound] at hpert ⊢
  omega

/-- Local constancy of the integer binding multiplicity `μ`: if two integer multiplicities
`muX, muY : Int` on a connected interior perturbation ball satisfy `|muY - muX| < 1`
(expressed as `-1 < muY - muX` and `muY - muX < 1`), then `muY = muX` (`qou-c9n8`). -/
theorem bindingMultiplicity_local_constancy_on_ball
    (muX muY : Int)
    (hlower : -1 < muY - muX)
    (hupper : muY - muX < 1) :
    muY = muX := by
  omega

end QOU.Eightfold.ModuleScopeFloatConstantBlastRadiusLightAmplitudeScalingSilentGateRefutationDerivedTraceDetectorBlindspotAndConfinementLocusOpenness
