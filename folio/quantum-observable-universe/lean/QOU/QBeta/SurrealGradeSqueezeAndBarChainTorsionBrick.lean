/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  * qou-034l: Surreal bound-management ord_omega cost/budget squeeze and polynomial grade closure.
  * qou-b55d: Squared normalization discrepancy between integer SDP multiplicity and figure-eight adjoint torsion norm 3.
  * qou-b7vr: Crossing-chain bar-involution consistency vs half-barred recurrence evaluation discrepancy.
  * qou-cwdx: Ternary skein 3^3 = 27 branching multiplier and per-block leaf growth excess.
  * qou-dilv: Cocenter-to-HH^1 outer derivation weight additivity and identity-class vanishing.
-/

namespace QOU.QBeta.SurrealGradeSqueezeAndBarChainTorsionBrick

/-! ### 1. Surreal `ord_omega` Cost/Budget Squeeze and Grade Closure (`qou-034l`) -/

/-- Super-polynomial `ord_omega` excess `wCost - wBudget` comparing cost and budget omega-grades. -/
def omegaGradeExcess (wCost wBudget : Int) : Int :=
  wCost - wBudget

/-- Combined omega-grade `w1 * d2 + w2 * d1` under grade multiplication of `(w1, d1)` and `(w2, d2)`. -/
def omegaProductGrade (w1 d1 w2 d2 : Int) : Int :=
  w1 * d2 + w2 * d1

/-- Whenever a super-polynomial cost has `1 <= wCost` and a polynomial budget has `wBudget = 0`,
    the omega-grade excess is at least `1`, and two pure polynomial grades (`w1 = 0`, `w2 = 0`)
    remain pure polynomial (`omegaProductGrade 0 d1 0 d2 = 0`) under grade multiplication. -/
theorem omegaGrade_squeeze_and_poly_closure (wCost d1 d2 : Int) (hSuper : 1 ≤ wCost) :
    1 ≤ omegaGradeExcess wCost 0 ∧
    omegaGradeExcess wCost 0 = wCost ∧
    omegaProductGrade 0 d1 0 d2 = 0 := by
  dsimp only [omegaGradeExcess, omegaProductGrade]
  have hEx : 1 ≤ wCost - 0 := by omega
  have hId : wCost - 0 = wCost := by omega
  have hProd : 0 * d2 + 0 * d1 = 0 := by
    rw [Int.zero_mul, Int.zero_mul]
    omega
  exact ⟨hEx, hId, hProd⟩

/-! ### 2. Integer Multiplicity vs Adjoint Torsion Squared Norm Squeeze (`qou-b55d`) -/

/-- Squared normalization discrepancy `nu * nu - torsionNormSq` comparing an integer SDP
    multiplicity `nu` against a squared adjoint torsion norm `torsionNormSq = tau_adj^2`. -/
def squaredTorsionDiscrepancy (nu torsionNormSq : Int) : Int :=
  nu * nu - torsionNormSq

/-- For the figure-eight adjoint torsion squared norm `torsionNormSq = 3` (`tau_adj = sqrt(3)`),
    `squaredTorsionDiscrepancy 1 3 = -2` and `squaredTorsionDiscrepancy 2 3 = 1`, squeezing `3`
    strictly between `1^2` and `2^2`, with `squaredTorsionDiscrepancy (-nu) t = squaredTorsionDiscrepancy nu t`. -/
theorem squaredTorsionDiscrepancy_figure_eight_squeeze (nu t : Int) :
    squaredTorsionDiscrepancy 1 3 = -2 ∧
    squaredTorsionDiscrepancy 2 3 = 1 ∧
    squaredTorsionDiscrepancy 2 3 - squaredTorsionDiscrepancy 1 3 = 3 ∧
    squaredTorsionDiscrepancy (-nu) t = squaredTorsionDiscrepancy nu t := by
  dsimp only [squaredTorsionDiscrepancy]
  have h1 : (1 : Int) * 1 - 3 = -2 := by omega
  have h2 : (2 : Int) * 2 - 3 = 1 := by omega
  have hDiff : ((2 : Int) * 2 - 3) - ((1 : Int) * 1 - 3) = 3 := by omega
  have hNeg : (-nu) * (-nu) - t = nu * nu - t := by
    rw [Int.neg_mul_neg]
  exact ⟨h1, h2, hDiff, hNeg⟩

/-! ### 3. Crossing-Chain Bar-Involution vs Half-Barred Evaluation (`qou-b7vr`) -/

/-- Bilinear model `c0 + c1 * hChain + c2 * hRec` of a crossing-chain recurrence evaluated at
    chain parameter `hChain` and recurrence parameter `hRec`. -/
def chainRecurrenceEval (c0 c1 c2 hChain hRec : Int) : Int :=
  c0 + c1 * hChain + c2 * hRec

/-- Evaluating the crossing chain at unbarred `h` while passing `-h` to the recurrence (`chainRecurrenceEval c0 c1 c2 h (-h)`)
    differs from the true bar image (`chainRecurrenceEval c0 c1 c2 (-h) (-h)`) by `2 * c1 * h`,
    whereas consistent bar-negation of both arguments matches the simultaneous `-h` specialization. -/
theorem chainRecurrenceEval_half_bar_discrepancy (c0 c1 c2 h : Int) :
    chainRecurrenceEval c0 c1 c2 h (-h) - chainRecurrenceEval c0 c1 c2 (-h) (-h) = 2 * (c1 * h) ∧
    chainRecurrenceEval c0 c1 c2 (-h) (-h) + chainRecurrenceEval c0 c1 c2 h h = 2 * c0 := by
  dsimp only [chainRecurrenceEval]
  have hNeg1 : c1 * (-h) = -(c1 * h) := by
    rw [Int.mul_neg]
  have hNeg2 : c2 * (-h) = -(c2 * h) := by
    rw [Int.mul_neg]
  have hDiff : (c0 + c1 * h + c2 * (-h)) - (c0 + c1 * (-h) + c2 * (-h)) = 2 * (c1 * h) := by
    omega
  have hSum : (c0 + c1 * (-h) + c2 * (-h)) + (c0 + c1 * h + c2 * h) = 2 * c0 := by
    omega
  exact ⟨hDiff, hSum⟩

/-! ### 4. Ternary Skein `3^3 = 27` Branching Multiplier (`qou-cwdx`) -/

/-- Single-crossing ternary skein leaf multiplier `3 * leaves`. -/
def ternarySkeinStep (leaves : Int) : Int :=
  3 * leaves

/-- Three-crossing block ternary skein multiplier `27 * leaves` (`3^3 = 27`). -/
def ternarySkeinCubeBlock (leaves : Int) : Int :=
  27 * leaves

/-- Three successive ternary skein steps equal `ternarySkeinCubeBlock`, producing a net leaf
    increase of `26 * leaves` per 3-crossing block, with `27` leaves from a single root (`leaves = 1`). -/
theorem ternarySkeinStep_three_fold_and_excess (leaves : Int) :
    ternarySkeinStep (ternarySkeinStep (ternarySkeinStep leaves)) = ternarySkeinCubeBlock leaves ∧
    ternarySkeinCubeBlock leaves - leaves = 26 * leaves ∧
    ternarySkeinCubeBlock 1 = 27 := by
  dsimp only [ternarySkeinStep, ternarySkeinCubeBlock]
  have hCube : 3 * (3 * (3 * leaves)) = 27 * leaves := by omega
  have hEx : 27 * leaves - leaves = 26 * leaves := by omega
  have hOne : 27 * (1 : Int) = 27 := by omega
  exact ⟨hCube, hEx, hOne⟩

/-! ### 5. Cocenter-to-`HH^1` Class-Polynomial Derivation Weight (`qou-dilv`) -/

/-- Degree-1 outer-derivation weight `wordLen * qWeight` on a minimal-length cocenter representative. -/
def cocenterDerivationWeight (wordLen qWeight : Int) : Int :=
  wordLen * qWeight

/-- Difference `cocenterDerivationWeight wordLen qWeight - hh0Rank` between the degree-1 derivation
    weight and the degree-0 cocenter rank contribution `hh0Rank`. -/
def cocenterDegreeOneExcess (wordLen qWeight hh0Rank : Int) : Int :=
  wordLen * qWeight - hh0Rank

/-- The cocenter derivation weight vanishes on the identity conjugacy class (`wordLen = 0`),
    is additive across minimal-length word concatenation `m1 + m2`, and reconstructs the
    degree-1 weight from `cocenterDegreeOneExcess`. -/
theorem cocenterDerivationWeight_additivity_and_excess (m1 m2 qWeight hh0Rank : Int) :
    cocenterDerivationWeight 0 qWeight = 0 ∧
    cocenterDerivationWeight (m1 + m2) qWeight =
      cocenterDerivationWeight m1 qWeight + cocenterDerivationWeight m2 qWeight ∧
    cocenterDegreeOneExcess m1 qWeight hh0Rank + hh0Rank = cocenterDerivationWeight m1 qWeight := by
  dsimp only [cocenterDerivationWeight, cocenterDegreeOneExcess]
  have hZero : 0 * qWeight = 0 := by
    rw [Int.zero_mul]
  have hAdd : (m1 + m2) * qWeight = m1 * qWeight + m2 * qWeight := by
    rw [Int.add_mul]
  have hRec : (m1 * qWeight - hh0Rank) + hh0Rank = m1 * qWeight := by omega
  exact ⟨hZero, hAdd, hRec⟩

end QOU.QBeta.SurrealGradeSqueezeAndBarChainTorsionBrick
