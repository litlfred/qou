/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Formalization for Round 114 beans:
- `qou-cc4t`: Belted-sum hyperbolic volume additivity `beltedSumVolumeScaled numBelts beltVol = numBelts * beltVol`
  and zero volume difference `mutationPairDiff` between distinct mutation / gluing choices at equal belt count.
- `qou-cjkt`: Perturbative one-loop invariant scaling `firstLoopFromInvariant invScaled = 6 * invScaled`
  and Seifert surgery sine-product denominator degree balance `(numFibres - 1) + 1 = numFibres`.
- `qou-cmjv`: Weight-3 level-5 cyclotomic distribution relation factor `1 - 5^2 = -24` over `5^2 = 25`
  and conjugate-pair real-part reduction `2 * (reOne + reTwo) - 2 * reOne = 2 * reTwo`.
- `qou-d8up`: Genus-`g` symmetric period-matrix dimension `g * (g + 1) / 2` (cleared `g * (g + 1)`)
  vs skew-symmetric dimension `g * (g - 1) / 2` and symplectic dimension `g * (2 * g + 1)` at `g = 4`.
- `qou-f0qa`: Neutron-proton mass-energy difference revision shift (`129333251 - 129333210 = 41`
  in units of `10^{-8}` MeV), strictly bounded by the `1σ` uncertainty `50`, and exact shift of
  `predictionResidualScaled`.
-/

namespace QOU.Eightfold.Qou10v9Cc4tCjktCmjvD8upF0qa

/-! ### 1. `qou-cc4t`: Belted-Sum Volume Additivity and Mutation Volume Degeneracy -/

/-- Total scaled volume `numBelts * beltVol` of a belted sum of `numBelts` link pieces. -/
def beltedSumVolumeScaled (numBelts beltVol : Int) : Int :=
  numBelts * beltVol

/-- Volume difference `volChoiceA - volChoiceB` between two mutation-related link complements. -/
def mutationPairDiff (volChoiceA volChoiceB : Int) : Int :=
  volChoiceA - volChoiceB

/-- Adding one belt increases the total volume by `beltVol`, while any two mutation-related links
with the same belt count and per-belt volume have zero volume difference. -/
theorem belted_sum_volume_additivity_and_mutation_degeneracy (numBelts beltVol : Int) :
    beltedSumVolumeScaled (numBelts + 1) beltVol - beltedSumVolumeScaled numBelts beltVol =
      beltVol ∧
    mutationPairDiff (beltedSumVolumeScaled numBelts beltVol)
      (beltedSumVolumeScaled numBelts beltVol) = 0 ∧
    beltedSumVolumeScaled 2 4 = 8 ∧
    beltedSumVolumeScaled 3 4 = 12 := by
  refine ⟨?_, ?_, by decide, by decide⟩
  · dsimp [beltedSumVolumeScaled]
    rw [Int.add_mul, Int.one_mul]
    omega
  · dsimp [mutationPairDiff, beltedSumVolumeScaled]
    omega

/-! ### 2. `qou-cjkt`: Perturbative One-Loop Scaling and Surgery Sine-Denominator Degree -/

/-- One-loop perturbative coefficient `6 * invScaled` proportional to the rational homology sphere invariant. -/
def firstLoopFromInvariant (invScaled : Int) : Int :=
  6 * invScaled

/-- Total sine-factor degree `(numFibres - 1) + 1` in the denominator of the `numFibres`-fibre surgery formula. -/
def surgerySineDenomDegree (numFibres : Int) : Int :=
  (numFibres - 1) + 1

/-- The one-loop coefficient increments by `6` per unit invariant step, and the denominator sine
degree `(numFibres - 1) + 1` equals `numFibres` for every fibre count (in particular `3` for `Σ(2,3,5)`). -/
theorem first_loop_scaling_and_sine_denom_balance (invScaled numFibres : Int) :
    firstLoopFromInvariant (invScaled + 1) - firstLoopFromInvariant invScaled = 6 ∧
    surgerySineDenomDegree numFibres = numFibres ∧
    surgerySineDenomDegree 3 = 3 := by
  refine ⟨?_, ?_, by decide⟩
  · dsimp [firstLoopFromInvariant]
    omega
  · dsimp [surgerySineDenomDegree]
    omega

/-! ### 3. `qou-cmjv`: Weight-3 Level-5 Distribution Factor and Conjugate-Pair Reduction -/

/-- Numerator `1 - primeLevel * primeLevel` of the weight-3 distribution factor `primeLevel^(1-3) - 1`. -/
def distributionFactorNumer (primeLevel : Int) : Int :=
  1 - primeLevel * primeLevel

/-- Denominator `primeLevel * primeLevel` of the weight-3 distribution factor. -/
def distributionFactorDenom (primeLevel : Int) : Int :=
  primeLevel * primeLevel

/-- Sum `2 * (reOne + reTwo)` of the real parts over the four primitive fifth roots of unity paired by conjugation. -/
def realPairSumScaled (reOne reTwo : Int) : Int :=
  2 * (reOne + reTwo)

/-- At level `5`, the weight-3 distribution factor is `-24 / 25`, its numerator and denominator sum
to `1`, and subtracting `2 * reOne` from the four-root conjugate sum isolates `2 * reTwo`. -/
theorem fifth_root_distribution_and_real_pair_reduction (reOne reTwo : Int) :
    distributionFactorNumer 5 = -24 ∧
    distributionFactorDenom 5 = 25 ∧
    distributionFactorNumer 5 + distributionFactorDenom 5 = 1 ∧
    realPairSumScaled reOne reTwo - 2 * reOne = 2 * reTwo := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  dsimp [realPairSumScaled]
  omega

/-! ### 4. `qou-d8up`: Period-Matrix Symmetric Dimension and Symplectic Dimension at Genus 4 -/

/-- Cleared symmetric period-matrix dimension `g * (g + 1)` (twice `g * (g + 1) / 2`). -/
def periodSymmetricDoubleDim (g : Int) : Int :=
  g * (g + 1)

/-- Cleared skew-symmetric dimension `g * (g - 1)` (twice `g * (g - 1) / 2`). -/
def skewDoubleDim (g : Int) : Int :=
  g * (g - 1)

/-- Dimension `g * (2 * g + 1)` of the symplectic modular group `Sp(2g)` at genus `g`. -/
def symplecticGroupDim (g : Int) : Int :=
  g * (2 * g + 1)

/-- At genus `g = 4`, twice the symmetric period dimension is `20` (so `dim = 10`), twice the skew
dimension is `12` (`dim = 6`), their sum is `32 = 2 * 4^2`, and `dim Sp(8) = 36`. -/
theorem period_symmetric_and_symplectic_dimension_identities :
    periodSymmetricDoubleDim 4 = 20 ∧
    skewDoubleDim 4 = 12 ∧
    periodSymmetricDoubleDim 4 + skewDoubleDim 4 = 32 ∧
    periodSymmetricDoubleDim 4 - skewDoubleDim 4 = 8 ∧
    symplecticGroupDim 4 = 36 := by
  decide

/-! ### 5. `qou-f0qa`: Neutron-Proton Mass-Energy Difference Revision Shift -/

/-- Neutron-proton mass-energy difference in units of `10^{-8}` MeV (2022 vs 2018 adjustments). -/
def massDiffScaled2022 : Int := 129333251
def massDiffScaled2018 : Int := 129333210

/-- Standard uncertainties in units of `10^{-8}` MeV (`38` in 2022 vs `50` in 2018). -/
def sigmaScaled2022 : Int := 38
def sigmaScaled2018 : Int := 50

/-- Signed residual `predScaled - refScaled` of a predicted mass difference against a reference target. -/
def predictionResidualScaled (predScaled refScaled : Int) : Int :=
  predScaled - refScaled

/-- The 2022-vs-2018 shift is `+41` (in units of `10^{-8}` MeV), lies strictly within the 2018
`1σ` band (`41 < 50`), and shifts every prediction residual by `-41`. -/
theorem neutron_proton_mass_diff_revision_shift (predScaled : Int) :
    massDiffScaled2022 - massDiffScaled2018 = 41 ∧
    massDiffScaled2022 - massDiffScaled2018 < sigmaScaled2018 ∧
    sigmaScaled2022 < sigmaScaled2018 ∧
    predictionResidualScaled predScaled massDiffScaled2018 -
      predictionResidualScaled predScaled massDiffScaled2022 = 41 := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  dsimp [predictionResidualScaled, massDiffScaled2022, massDiffScaled2018]
  omega

end QOU.Eightfold.Qou10v9Cc4tCjktCmjvD8upF0qa
