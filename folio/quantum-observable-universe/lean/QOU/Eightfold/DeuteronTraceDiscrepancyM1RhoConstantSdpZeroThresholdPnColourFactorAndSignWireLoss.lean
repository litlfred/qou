/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Formalization for beans under qou-10v9:
  - qou-4e5k: Deuteron tr_M witness discrepancy (1.41e-4 on D vs ~7e-8 pin straddle on p, n)
  - qou-742w: M1 leading constant RHO_INF = 0.979796195657 vs 2*sqrt(6)/5 squared inequality
  - qou-9bei: He/Nu SDP saturation n=6 partition support (8 exact zeros vs 3 positive blocks) and threshold stability
  - qou-cblw: p-n interface factor colour-weighted z - h*(1/2 - delta/4) vs colour-blind z - h/2
  - qou-fv0s: Ternary sign wire format {-1, 0, +1} non-injectivity on 4 crossing kinds (R3 colour-weight loss)
-/

namespace QOU.Eightfold.DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss

/-!
## 1. Bean `qou-4e5k`: Deuteron `tr_M` Witness Discrepancy vs Single-Nucleon Pin Straddle
On `origin/main`, the two committed 50-dps witnesses (`atomic-tr-m-mpfr-50dps` vs
`low-isotope-mass-table`) differ on the proton and neutron only at the `~7e-8` pin straddle,
whereas on the deuteron (`D`) they differ by `0.575172243917771870827 - 0.575090958682446712092
= 0.000081285235325158735` (`~1.41e-4` relative), exceeding the proton discrepancy by more
than `900x` in absolute terms and `1800x` in relative terms.
-/

/-- Absolute difference `|a - b|` in `10^15`-scaled integer units between the two committed
    witnesses for proton, neutron, and deuteron. -/
def trMDiscrepancyScaled15 (valA15 valB15 : Int) : Int :=
  if valA15 ≥ valB15 then valA15 - valB15 else valB15 - valA15

/-- Verification that in `10^15`-scaled units:
    - Proton discrepancy is `1145759782287835 - 1145759692457300 = 89830535` (`~8.98e-8`);
    - Neutron discrepancy is `987743756687661 - 987743688115809 = 68571852` (`~6.86e-8`);
    - Deuteron discrepancy is `575172243917771 - 575090958682446 = 81285235325` (`~8.13e-5`),
      which strictly exceeds `900 * protonDiscrepancy`. -/
theorem deuteron_tr_m_discrepancy_exceeds_pin_straddle :
    trMDiscrepancyScaled15 1145759782287835 1145759692457300 = 89830535 ∧
    trMDiscrepancyScaled15 987743756687661 987743688115809 = 68571852 ∧
    trMDiscrepancyScaled15 575172243917771 575090958682446 = 81285235325 ∧
    900 * trMDiscrepancyScaled15 1145759782287835 1145759692457300 <
      trMDiscrepancyScaled15 575172243917771 575090958682446 := by
  decide

/-!
## 2. Bean `qou-742w`: M1 Leading Constant `RHO_INF` vs `2 * sqrt(6) / 5`
Twelve scripts hard-code `RHO_INF = 0.979796195657` (`979796195657 / 10^12`), while one
annotates it as `2 * sqrt(6) / 5`. Squaring both in `10^24` integer units proves they are
mathematically distinct (`(2 * sqrt(6) / 5)^2 = 24 / 25 = 0.96`).
-/

/-- `10^24 * RHO_INF^2` for the 12-digit literal `979796195657`. -/
def rhoInfLiteralSquared24 : Int :=
  979796195657 * 979796195657

/-- `10^24 * (2 * sqrt(6) / 5)^2 = 10^24 * 24 / 25`. -/
def twoSqrtSixOverFiveSquared24 : Int :=
  960000000000000000000000

/-- Exact integer proof that `RHO_INF^2 - (2 * sqrt(6) / 5)^2 = 585023930225661649 / 10^24 > 0`,
    confirming `0.979796195657 ≠ 2 * sqrt(6) / 5`. -/
theorem m1_rho_inf_literal_ne_two_sqrt_six_over_five :
    25 * twoSqrtSixOverFiveSquared24 = 24 * (1000000000000 : Int) ^ 2 ∧
    rhoInfLiteralSquared24 - twoSqrtSixOverFiveSquared24 = 585023930225661649 ∧
    twoSqrtSixOverFiveSquared24 < rhoInfLiteralSquared24 := by
  decide

/-!
## 3. Bean `qou-9bei`: `he_nu_sdp_saturation_obstruction` Zero-Block Threshold Stability
At `n = 6` strands, there are `p(6) = 11` partitions of `6`, of which `8` have mathematically
zero character weight (`|y_λ| <= 10^-52`) and `3` have positive physical weight (`y_λ >= 10^-2`).
-/

/-- Filtered negative-block count using a noise floor `tau > 0`: a block `y` is counted as
    genuinely negative iff `y < -tau`. -/
def countGenuineNegativeBlocks (tauFloor : Int) (blockWeights : List Int) : Nat :=
  (blockWeights.filter (fun y => decide (y < -tauFloor))).length

/-- Filtered indistinguishable-from-zero block count (`|y| <= tauFloor`). -/
def countZeroResidueBlocks (tauFloor : Int) (blockWeights : List Int) : Nat :=
  (blockWeights.filter (fun y => decide (-tauFloor ≤ y ∧ y ≤ tauFloor))).length

/-- Verification that for `8` arithmetic-residue zero blocks (`|r_i| <= 1`, modelling `10^-52`)
    and `3` positive physical blocks (`b_j >= 1000`, modelling `10^-2`) with threshold
    `tauFloor = 10` (modelling `10^-30`), `countGenuineNegativeBlocks = 0` and
    `countZeroResidueBlocks = 8` regardless of the signs of the sub-threshold residues. -/
theorem sdp_saturation_threshold_eliminates_pin_residue_false_negatives :
    countGenuineNegativeBlocks 10 [-1, -1, -1, 0, 0, 0, 1, 1, 1000, 2500, 5000] = 0 ∧
    countGenuineNegativeBlocks 10 [0, 0, 0, 0, 0, 0, 0, 0, 1000, 2500, 5000] = 0 ∧
    countZeroResidueBlocks 10 [-1, -1, -1, 0, 0, 0, 1, 1, 1000, 2500, 5000] = 8 := by
  decide

/-!
## 4. Bean `qou-cblw`: Colour-Weighted vs Colour-Blind `p-n` Interface Factor
The canonical colour-weighted p-n interface factor is `z - h * (1/2 - δ/4)`, whereas the
colour-blind factor is `z - h / 2`.
-/

/-- Four times the canonical colour-weighted p-n interface factor:
    `4 * (z - h * (1/2 - δ/4)) = 4 * z - 2 * h + h * δ`. -/
def fourTimesColourWeightedPnFactor (zVal hVal deltaVal : Int) : Int :=
  4 * zVal - 2 * hVal + hVal * deltaVal

/-- Four times the colour-blind p-n interface factor:
    `4 * (z - h / 2) = 4 * z - 2 * h`. -/
def fourTimesColourBlindPnFactor (zVal hVal : Int) : Int :=
  4 * zVal - 2 * hVal

/-- Exact difference `4 * w_canon - 4 * w_blind = h * δ`, which is strictly positive whenever
    `0 < hVal` and `0 < deltaVal`. -/
theorem pn_interface_colour_weighted_minus_blind_identity
    (zVal hVal deltaVal : Int) (hPosH : 0 < hVal) (hPosD : 0 < deltaVal) :
    fourTimesColourWeightedPnFactor zVal hVal deltaVal -
      fourTimesColourBlindPnFactor zVal hVal = hVal * deltaVal ∧
    0 < fourTimesColourWeightedPnFactor zVal hVal deltaVal -
      fourTimesColourBlindPnFactor zVal hVal := by
  dsimp [fourTimesColourWeightedPnFactor, fourTimesColourBlindPnFactor]
  have hProd : 0 < hVal * deltaVal := Int.mul_pos hPosH hPosD
  have hDiff : 4 * zVal - 2 * hVal + hVal * deltaVal - (4 * zVal - 2 * hVal) = hVal * deltaVal := by
    omega
  exact ⟨hDiff, by omega⟩

/-!
## 5. Bean `qou-fv0s`: Ternary Sign Wire Format Cannot Carry `R3` Colour Weight
`canonical_braid_crossings.sign_for_ctype` maps the 4 distinct crossing types
`(positive, negative, averaged, averaged_weighted)` into the 3-element sign alphabet `{-1, 0, +1}`,
sending both `averaged` and `averaged_weighted` to `0`.
-/

/-- The 4 crossing types in `canonical_braid_crossings`. -/
inductive CrossingType where
  | positive
  | negative
  | averaged
  | averagedWeighted
  deriving DecidableEq

/-- The ternary sign wire encoder `sign_for_ctype : CrossingType → Int` into `{-1, 0, +1}`. -/
def signForCtype : CrossingType → Int
  | .positive => 1
  | .negative => -1
  | .averaged => 0
  | .averagedWeighted => 0

/-- Reconstructed `4x`-scaled interface factor from the ternary wire sign `s ∈ {-1, 0, +1}`. -/
def fourTimesFactorFromWireSign (sWire zVal hVal : Int) : Int :=
  if sWire = 1 then 4 * zVal
  else if sWire = -1 then 4 * (zVal - hVal)
  else 4 * zVal - 2 * hVal

/-- Proof that `signForCtype` collapses `averaged` and `averagedWeighted` onto the same wire
    symbol `0`, so any downstream decoder reading only `signForCtype` returns the colour-blind
    factor `4 * z - 2 * h` for both, losing the `h * δ` colour-weight correction. -/
theorem sign_wire_format_collapses_averaged_and_averaged_weighted (zVal hVal : Int) :
    CrossingType.averaged ≠ CrossingType.averagedWeighted ∧
    signForCtype CrossingType.averaged = 0 ∧
    signForCtype CrossingType.averagedWeighted = 0 ∧
    fourTimesFactorFromWireSign (signForCtype CrossingType.averagedWeighted) zVal hVal =
      fourTimesColourBlindPnFactor zVal hVal := by
  dsimp [signForCtype, fourTimesFactorFromWireSign, fourTimesColourBlindPnFactor]
  refine ⟨by decide, rfl, rfl, rfl⟩

end QOU.Eightfold.DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss
