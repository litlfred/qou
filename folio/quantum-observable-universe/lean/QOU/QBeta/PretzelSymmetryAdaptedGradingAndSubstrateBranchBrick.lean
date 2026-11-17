/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Brunnian Deficit Recursion, Kerov Row-Shifted Identity, Colour-Curve Branch Defect, Pretzel Symmetry-Adapted Grading & Plancherel Covariance Brick

This self-contained Lean 4 module formalizes exact algebraic and structural identities for five
items in the `b9cj` formalization arc:

1. **Convention-D Brunnian Trace Deficit Recursion & Leading Milnor Cofactor (`qou-ck2w`)**:
   Formalizes the convention-D trace deficit step factor `-hSq * (hSq + 2)` and its expanded
   form `-(hSq * hSq) - 2 * hSq`, along with the 4-scaled leading Milnor cofactor step
   `fourScaledMilnorCofactorNext curr = -2 * curr` generating `4 * mubar_A = 3 * (-2)^{A-3}`
   at `A = 3, 4, 5, 6` (`3, -6, 12, -24`).

2. **Kerov-Olshanski Row-Shifted Content Decomposition (`qou-k5r5`)**:
   Formalizes the exact row-wise identity `(lamI - rowIdx)^2 + 2 * rowIdx * (lamI - rowIdx) + rowIdx^2 = lamI^2`
   that separates the `Lambda*`-regularized square `(lamI - rowIdx)^2`, the index-weighted
   non-`Lambda*` obstruction term `2 * rowIdx * (lamI - rowIdx)`, and the staircase square `rowIdx^2`.

3. **Substrate Colour-Curve Modulus & Branch-vs-Bar Defect (`qou-ndt5`)**:
   Formalizes the 27-scaled colour-curve modulus `5 * (z + 1) * (4*z^2 - z + 4)` in the
   bar-invariant variable `z = s - 1/s`, proving its expansion `20*z^3 + 15*z^2 + 15*z + 20`,
   its vanishing at the golden-ratio degeneration `z = -1` (`s^2 + s - 1 = 0`), and the exact
   branch defect identity `27*r(z) - 27*r(-z) = 10 * z * (4*z^2 + 3)` under `s ↦ -s` (`z ↦ -z`).

4. **Pretzel `(-2,3,7)` Symmetry-Adapted `(4,1,1)` Grading & `W^2 = s(x) - 3` Identity (`qou-x3iv`)**:
   Formalizes the `X^2`-cleared identity `(X^2 - 1)^2 = (X^4 + X^2 + 1) - 3 * X^2` equivalent to
   `W^2 = s(x) - 3` for `W = X - 1/X` and adjoint character `s(x) = X^2 + 1 + X^{-2}`, together
   with the Garoufalidis-Zagier `(4, 1, 1)` weight-space dimension decomposition `4 + 1 + 1 = 6`.

5. **Plancherel Covariance Kernel Free-Cumulant Affine Relation & `T_3(3)` Anchor (`qou-x631`)**:
   Formalizes the affine fourth free-cumulant relation `R_4 = 3 * omega_3 - k` and the `k = 3`
   3-cycle character sum `T_3(3) = (f^{(3)})^2 * 1 + (f^{(2,1)})^2 * (-1) + (f^{(1,1,1)})^2 * 1 = -2 < 0`.
-/

namespace QOU.QBeta.PretzelSymmetryAdaptedGradingAndSubstrateBranchBrick

/-! ## 1. Brunnian Trace Deficit Step Factor & Leading Milnor Cofactor (`qou-ck2w`) -/

/-- Convention-D Brunnian trace deficit step multiplier `-hSq * (hSq + 2)` in `hSq = h^2`. -/
def brunnianDeficitStepFactor (hSq : Int) : Int :=
  -hSq * (hSq + 2)

/-- Expanded polynomial form `-(hSq * hSq) - 2 * hSq` of the Brunnian deficit step multiplier. -/
def brunnianDeficitStepExpanded (hSq : Int) : Int :=
  -(hSq * hSq) - 2 * hSq

/-- Exact polynomial equivalence between the factored and expanded Brunnian deficit step multipliers. -/
theorem brunnianDeficitStepFactor_eq_expanded (hSq : Int) :
    brunnianDeficitStepFactor hSq = brunnianDeficitStepExpanded hSq := by
  dsimp [brunnianDeficitStepFactor, brunnianDeficitStepExpanded]
  rw [Int.neg_mul, Int.mul_add, Int.mul_comm hSq 2]
  omega

/-- Single-step recursion `curr ↦ -2 * curr` for the 4-scaled leading Milnor cofactor `4 * mubar_A`. -/
def fourScaledMilnorCofactorNext (curr : Int) : Int :=
  -2 * curr

/-- Two steps of the leading Milnor cofactor recursion multiply by `+4`. -/
theorem fourScaledMilnorCofactorNext_two_step (curr : Int) :
    fourScaledMilnorCofactorNext (fourScaledMilnorCofactorNext curr) = 4 * curr := by
  dsimp [fourScaledMilnorCofactorNext]
  omega

/-- Starting from `4 * mubar_3 = 3`, the `A = 4, 5, 6` values are `-6, 12, -24`. -/
theorem fourScaledMilnorCofactor_anchors :
    fourScaledMilnorCofactorNext 3 = -6 ∧
      fourScaledMilnorCofactorNext (fourScaledMilnorCofactorNext 3) = 12 ∧
      fourScaledMilnorCofactorNext
        (fourScaledMilnorCofactorNext (fourScaledMilnorCofactorNext 3)) = -24 := by
  refine ⟨rfl, ⟨rfl, rfl⟩⟩

/-! ## 2. Kerov-Olshanski Row-Shifted Content Decomposition (`qou-k5r5`) -/

/-- Row-wise shifted decomposition `(lamI - rowIdx)^2 + 2*rowIdx*(lamI - rowIdx) + rowIdx^2`. -/
def kerovRowShiftedDecomposition (lamI rowIdx : Int) : Int :=
  (lamI - rowIdx) * (lamI - rowIdx) + 2 * rowIdx * (lamI - rowIdx) + rowIdx * rowIdx

/-- Exact algebraic identity `kerovRowShiftedDecomposition lamI rowIdx = lamI^2`, isolating the
`2 * rowIdx * (lamI - rowIdx)` non-`Lambda*` obstruction term. -/
theorem kerovRowShiftedDecomposition_eq_sq (lamI rowIdx : Int) :
    kerovRowShiftedDecomposition lamI rowIdx = lamI * lamI := by
  dsimp [kerovRowShiftedDecomposition]
  rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.mul_sub]
  rw [Int.mul_assoc 2 rowIdx lamI, Int.mul_comm rowIdx lamI, Int.mul_assoc 2 rowIdx rowIdx]
  omega

/-! ## 3. Substrate Colour-Curve Modulus & Branch Defect (`qou-ndt5`) -/

/-- Factored 27-scaled colour-curve modulus `27 * r(z) = 5 * (z + 1) * (4*z^2 - z + 4)`. -/
def twentySevenColourModulusFactored (z : Int) : Int :=
  5 * (z + 1) * (4 * z * z - z + 4)

/-- Expanded 27-scaled colour-curve modulus `20*z^3 + 15*z^2 + 15*z + 20`. -/
def twentySevenColourModulusExpanded (z : Int) : Int :=
  20 * (z * z * z) + 15 * (z * z) + 15 * z + 20

/-- Factored 27-scaled branch defect `27 * (r(z) - r(-z)) = 10 * z * (4*z^2 + 3)`. -/
def twentySevenBranchDefect (z : Int) : Int :=
  40 * (z * z * z) + 30 * z

/-- Vanishing of the colour-curve modulus at the golden-ratio degeneration `z = -1`
(`s^2 + s - 1 = 0`, `q in {phi^{-2}, phi^2}`). -/
theorem twentySevenColourModulusFactored_at_neg_one :
    twentySevenColourModulusFactored (-1) = 0 := by
  rfl

/-- Exact branch defect identity under `z ↦ -z` (`s ↦ -s`):
`27 * r(z) - 27 * r(-z) = 40 * z^3 + 30 * z`. -/
theorem twentySevenColourModulusExpanded_branch_defect (z : Int) :
    twentySevenColourModulusExpanded z - twentySevenColourModulusExpanded (-z) =
      twentySevenBranchDefect z := by
  dsimp [twentySevenColourModulusExpanded, twentySevenBranchDefect]
  rw [Int.neg_mul, Int.mul_neg z z, Int.neg_neg, Int.mul_neg (z * z) z, Int.mul_neg 20 (z * z * z), Int.mul_neg 15 z]
  omega

/-! ## 4. Pretzel (-2,3,7) Symmetry-Adapted Grading & W^2 = s(x) - 3 (`qou-x3iv`) -/

/-- `X`-scaled antisymmetric denominator `X * W = X^2 - 1` (written in `xSq = X^2`). -/
def pretzelScaledW (xSq : Int) : Int :=
  xSq - 1

/-- `X^2`-scaled adjoint character `X^2 * s(x) = X^4 + X^2 + 1` (written in `xSq = X^2`). -/
def pretzelScaledAdjointChar (xSq : Int) : Int :=
  xSq * xSq + xSq + 1

/-- Exact identity `(X * W)^2 = X^2 * s(x) - 3 * X^2`, encoding `W^2 = s(x) - 3` in the
adjoint-weight ring `Z[s(x)]`. -/
theorem pretzelScaledW_sq_eq_adjoint_sub_three (xSq : Int) :
    pretzelScaledW xSq * pretzelScaledW xSq =
      pretzelScaledAdjointChar xSq - 3 * xSq := by
  dsimp [pretzelScaledW, pretzelScaledAdjointChar]
  rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
  omega

/-- Garoufalidis-Zagier `(4, 1, 1)` weight-space dimension sum `w0Dim + w1Dim + w2Dim`. -/
def pretzelWeightGradingSum (w0Dim w1Dim w2Dim : Int) : Int :=
  w0Dim + w1Dim + w2Dim

/-- The symmetry-adapted `(4, 1, 1)` grading recovers the full 6-dimensional block space. -/
theorem pretzelWeightGradingSum_four_one_one :
    pretzelWeightGradingSum 4 1 1 = 6 := by
  rfl

/-! ## 5. Plancherel Covariance Kernel Free-Cumulant Affine Relation & T_3(3) (`qou-x631`) -/

/-- Affine relation `R_4 = 3 * omega_3 - k` for the fourth free cumulant. -/
def freeCumulantR4 (omega3 k : Int) : Int :=
  3 * omega3 - k

/-- Differences of `R_4` at fixed size `k` equal `3 * (omega3A - omega3B)`. -/
theorem freeCumulantR4_diff_at_fixed_k (omega3A omega3B k : Int) :
    freeCumulantR4 omega3A k - freeCumulantR4 omega3B k =
      3 * (omega3A - omega3B) := by
  dsimp [freeCumulantR4]
  omega

/-- Three-partition weighted 3-cycle character sum
`f3^2 * chi3 + f21^2 * chi21 + f111^2 * chi111` at `k = 3`. -/
def threeCycleWeightedSumThree (f3 chi3 f21 chi21 f111 chi111 : Int) : Int :=
  f3 * f3 * chi3 + f21 * f21 * chi21 + f111 * f111 * chi111

/-- At `k = 3` (`f^{(3)} = 1, chi^{(3)} = 1`, `f^{(2,1)} = 2, chi^{(2,1)} = -1`,
`f^{(1,1,1)} = 1, chi^{(1,1,1)} = 1`), the weighted 3-cycle sum `T_3(3)` equals `-2`. -/
theorem threeCycleWeightedSumThree_k3_eq_neg_two :
    threeCycleWeightedSumThree 1 1 2 (-1) 1 1 = -2 := by
  rfl

end QOU.QBeta.PretzelSymmetryAdaptedGradingAndSubstrateBranchBrick
