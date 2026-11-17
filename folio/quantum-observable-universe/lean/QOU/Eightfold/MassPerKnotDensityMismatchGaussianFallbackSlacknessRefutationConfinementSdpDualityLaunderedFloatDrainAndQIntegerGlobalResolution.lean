/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Round 82 Formalization:
  - qou-afjl: Mass-per-knot density rename vs normalization discrepancy (|Δ| = 1139.0)
  - qou-ai7v: Gaussian fallback tier delta_g zeroing & complementary-slackness refutation
  - qou-apcl: Confinement semidefinite program (SDP) strict interior duality & complementarity
  - qou-b7cf: Laundered mpf(str(f64)) precision deficit & 34-file / 68-site drain
  - qou-b8vx: Global-symbol q-integer convention resolution coverage across 366 definitions
-/

namespace QOU.Eightfold.MassPerKnotDensityMismatchGaussianFallbackSlacknessRefutationConfinementSdpDualityLaunderedFloatDrainAndQIntegerGlobalResolution

/-! ## 1. Bean `qou-afjl`: Mass-Per-Knot Density Equivalence Discrepancy -/

/-- Discrepancy between the unnormalized multi-cell knot mass `nCells * dCell`
    and the per-cell normalized knot mass `dCell`. -/
def scaledKnotDensityGap (nCells dCell : Int) : Int :=
  nCells * dCell - dCell

/-- Difference between two density conventions `dLegacy` and `dRenamed`. -/
def perKnotDensityDelta (dLegacy dRenamed : Int) : Int :=
  dLegacy - dRenamed

/-- The gap between `nCells * dCell` and `dCell` factors as `(nCells - 1) * dCell`. -/
theorem scaledKnotDensityGap_eq_pred_mul (nCells dCell : Int) :
    scaledKnotDensityGap nCells dCell = (nCells - 1) * dCell := by
  dsimp [scaledKnotDensityGap]
  calc nCells * dCell - dCell
    _ = nCells * dCell - 1 * dCell := by omega
    _ = (nCells - 1) * dCell := (Int.sub_mul nCells 1 dCell).symm

/-- On a single-cell carrier (`nCells = 1`), the two density conventions coincide (`gap = 0`). -/
theorem scaledKnotDensityGap_at_one_cell (dCell : Int) :
    scaledKnotDensityGap 1 dCell = 0 := by
  dsimp [scaledKnotDensityGap]
  omega

/-- For any multi-cell carrier (`2 ≤ nCells`) with positive per-cell density (`0 < dCell`),
    the discrepancy is strictly positive, and at `(2, 1139)` reproduces the `1139` witness gap. -/
theorem massPerKnot_discrepancy_pos_and_witness (nCells dCell : Int)
    (hCells : 2 ≤ nCells) (hPos : 0 < dCell) :
    0 < scaledKnotDensityGap nCells dCell ∧
      scaledKnotDensityGap 2 1139 = 1139 ∧
      perKnotDensityDelta 2278 1139 = 1139 := by
  have hFac := scaledKnotDensityGap_eq_pred_mul nCells dCell
  have hProd : 0 < (nCells - 1) * dCell :=
    Int.mul_pos (by omega) hPos
  dsimp [scaledKnotDensityGap, perKnotDensityDelta] at *
  omega

/-! ## 2. Bean `qou-ai7v`: Gaussian Fallback Tier `delta_g` Complementary-Slackness Refutation -/

/-- Non-zero fallback tier contribution `logTraceApprox * dualMultiplier` in window `k_exact < k ≤ k_max`. -/
def fallbackTierContribution (logTraceApprox dualMultiplier : Int) : Int :=
  logTraceApprox * dualMultiplier

/-- Complementary-slackness product `constraintSlack * dualMultiplier`. -/
def complementarySlacknessProduct (constraintSlack dualMultiplier : Int) : Int :=
  constraintSlack * dualMultiplier

/-- When a primal constraint is tight (`constraintSlack = 0`), the complementary-slackness product
    `constraintSlack * dualMultiplier` vanishes for ANY `dualMultiplier`, refuting the claim that
    `complementarySlacknessProduct = 0` forces `dualMultiplier = 0`. -/
theorem tightConstraint_allows_positive_dual (dualMultiplier : Int)
    (hDualPos : 0 < dualMultiplier) :
    complementarySlacknessProduct 0 dualMultiplier = 0 ∧ 0 < dualMultiplier := by
  dsimp [complementarySlacknessProduct]
  omega

/-- When both `logTraceApprox > 0` and `dualMultiplier > 0`, the true fallback tier contribution
    is strictly positive, so zeroing `delta_g := 0` introduces a strictly positive truncation error. -/
theorem fallbackTierContribution_pos_of_pos (logTraceApprox dualMultiplier : Int)
    (hTracePos : 0 < logTraceApprox) (hDualPos : 0 < dualMultiplier) :
    0 < fallbackTierContribution logTraceApprox dualMultiplier := by
  dsimp [fallbackTierContribution]
  exact Int.mul_pos hTracePos hDualPos

/-! ## 3. Bean `qou-apcl`: Confinement Semidefinite Program (SDP) Strict Interior Duality -/

/-- Two-block primal-dual inner product gap `x0 * z0 + x1 * z1` for diagonal SDP certificates. -/
def sdpPrimalDualGap (x0 z0 x1 z1 : Int) : Int :=
  x0 * z0 + x1 * z1

/-- Strict interior feasibility margin `xMin - barrierFloor` above a positive spectral floor. -/
def sdpStrictInteriorMargin (xMin barrierFloor : Int) : Int :=
  xMin - barrierFloor

/-- Non-negativity of the primal-dual gap over positive-semidefinite diagonal blocks (`x_i, z_i ≥ 0`). -/
theorem sdpPrimalDualGap_nonneg (x0 z0 x1 z1 : Int)
    (hx0 : 0 ≤ x0) (hz0 : 0 ≤ z0) (hx1 : 0 ≤ x1) (hz1 : 0 ≤ z1) :
    0 ≤ sdpPrimalDualGap x0 z0 x1 z1 := by
  dsimp [sdpPrimalDualGap]
  have h0 : 0 ≤ x0 * z0 := Int.mul_nonneg hx0 hz0
  have h1 : 0 ≤ x1 * z1 := Int.mul_nonneg hx1 hz1
  omega

/-- Under strict primal interior feasibility (`x0 > 0, x1 > 0`) and dual non-negativity (`z0 ≥ 0, z1 ≥ 0`),
    zero duality gap forces exact dual slack vanishing (`z0 = 0 ∧ z1 = 0`). -/
theorem confinementSdp_zero_gap_forces_zero_dualSlack (x0 z0 x1 z1 : Int)
    (hx0 : 0 < x0) (hz0 : 0 ≤ z0) (hx1 : 0 < x1) (hz1 : 0 ≤ z1)
    (hZeroGap : sdpPrimalDualGap x0 z0 x1 z1 = 0) :
    z0 = 0 ∧ z1 = 0 := by
  dsimp [sdpPrimalDualGap] at hZeroGap
  have h0Nonneg : 0 ≤ x0 * z0 := Int.mul_nonneg (by omega) hz0
  have h1Nonneg : 0 ≤ x1 * z1 := Int.mul_nonneg (by omega) hz1
  have h0Zero : x0 * z0 = 0 := by omega
  have h1Zero : x1 * z1 = 0 := by omega
  have hz0Zero : z0 = 0 := by
    cases Int.mul_eq_zero.mp h0Zero with
    | inl h => omega
    | inr h => exact h
  have hz1Zero : z1 = 0 := by
    cases Int.mul_eq_zero.mp h1Zero with
    | inl h => omega
    | inr h => exact h
  exact ⟨hz0Zero, hz1Zero⟩

/-- Strict interior feasibility margin is positive whenever `barrierFloor < xMin`. -/
theorem sdpStrictInteriorMargin_pos (xMin barrierFloor : Int)
    (hStrict : barrierFloor < xMin) :
    0 < sdpStrictInteriorMargin xMin barrierFloor := by
  dsimp [sdpStrictInteriorMargin]
  omega

/-! ## 4. Bean `qou-b7cf`: Laundered `mpf(str(f64))` Precision Deficit & Site Drain -/

/-- Unrecovered decimal digit deficit `targetDps - f64StringDigits` when laundering a float64 via `str()`. -/
def launderedDigitDeficit (targetDps f64StringDigits : Int) : Int :=
  targetDps - f64StringDigits

/-- Remaining laundered expression sites after draining `drainedSites` from `initialSites`. -/
def remainingLaunderedSites (initialSites drainedSites : Int) : Int :=
  initialSites - drainedSites

/-- Raising ambient working precision from `dps1` to `dps2` increases the laundered digit deficit by `dps2 - dps1`. -/
theorem launderedDigitDeficit_step (dps1 dps2 f64StringDigits : Int) :
    launderedDigitDeficit dps2 f64StringDigits -
      launderedDigitDeficit dps1 f64StringDigits = dps2 - dps1 := by
  dsimp [launderedDigitDeficit]
  omega

/-- At 80-dps (`targetDps = 80`) and 17-digit float64 string conversion (`f64StringDigits = 17`),
    63 decimal digits are lost per laundered cast, and draining all `38 + 30 = 68` sites leaves `0`. -/
theorem launderedDrain_68sites_complete :
    launderedDigitDeficit 80 17 = 63 ∧
      0 < launderedDigitDeficit 80 17 ∧
      remainingLaunderedSites (38 + 30) 68 = 0 := by
  dsimp [launderedDigitDeficit, remainingLaunderedSites]
  omega

/-! ## 5. Bean `qou-b8vx`: Global-Symbol `q`-Integer Convention Resolution Coverage -/

/-- Total measured `q`-integer definitions combining local and global-symbol resolution passes. -/
def measuredQIntDefs (localMeasured globalResolved : Int) : Int :=
  localMeasured + globalResolved

/-- Unmeasured `q`-integer definitions remaining out of `totalDefs`. -/
def unmeasuredQIntDefs (totalDefs localMeasured globalResolved : Int) : Int :=
  totalDefs - measuredQIntDefs localMeasured globalResolved

/-- Adding the global-symbol resolution pass reduces the unmeasured definition count by `globalResolved`. -/
theorem globalResolution_reduces_unmeasured_count
    (totalDefs localMeasured globalResolved : Int) :
    unmeasuredQIntDefs totalDefs localMeasured 0 -
      unmeasuredQIntDefs totalDefs localMeasured globalResolved =
      globalResolved := by
  dsimp [unmeasuredQIntDefs, measuredQIntDefs]
  omega

/-- Exact partition of the 366 corpus `q`-integer definitions: `158` locally evaluable + `63` globally
    resolved (`53` symmetric + `5` classical + `3` two-step symmetric + `2` affine) = `221` measured
    and `145` remaining unmeasured. -/
theorem qIntGlobalResolution_corpus_partition :
    measuredQIntDefs 158 (53 + 5 + 3 + 2) = 221 ∧
      unmeasuredQIntDefs 366 158 (53 + 5 + 3 + 2) = 145 ∧
      unmeasuredQIntDefs 366 158 0 = 208 := by
  dsimp [measuredQIntDefs, unmeasuredQIntDefs]
  omega

end QOU.Eightfold.MassPerKnotDensityMismatchGaussianFallbackSlacknessRefutationConfinementSdpDualityLaunderedFloatDrainAndQIntegerGlobalResolution
