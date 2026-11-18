/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  - qou-ix9e: Monic rewriting rule orientation and leading-monomial reduction decomposition
  - qou-lncp: Overlap critical-pair difference vanishing and two-term context linearity
  - qou-ulfe: Multiplicative formal group law associativity and unit-scale factorization
  - qou-znz5: Distribution algebra divided-power normal-form additivity and exchange reduction
  - qou-pso0: Specialization flatness and parameter-difference torsion-free factorization
-/

namespace QOU.Foundations.MonicRewritingRuleOrientationOverlapCriticalPairResolutionFormalGroupLawDistributionConfluenceSpecializationFlatness

/-! ### 1. Monic Rewriting Rule Orientation & Leading-Monomial Decomposition (`qou-ix9e`) -/

/-- Carrier for a two-letter rewriting rule with generator ranks, leading coefficient, and tail scale. -/
structure MonicTwoLetterRule where
  leftRank : Int
  rightRank : Int
  leadCoeff : Int
  rhsScale : Int
  deriving DecidableEq, Repr

/-- Orientation margin `leftRank - rightRank` witnessing strict degree-lexicographic orientation. -/
def ruleOrientationMargin (r : MonicTwoLetterRule) : Int :=
  r.leftRank - r.rightRank

/-- Leading reduction step `leadCoeff * u - rhsScale * u` eliminating the leading monomial. -/
def ruleMonicLeadingStep (r : MonicTwoLetterRule) (u : Int) : Int :=
  r.leadCoeff * u - r.rhsScale * u

/-- Rewritten normal-form remainder `rhsScale * u`. -/
def ruleRewrittenRemainder (r : MonicTwoLetterRule) (u : Int) : Int :=
  r.rhsScale * u

/-- Reversed-rank rule swapping `leftRank` and `rightRank`. -/
def reverseRuleOrientation (r : MonicTwoLetterRule) : MonicTwoLetterRule :=
  { leftRank := r.rightRank
    rightRank := r.leftRank
    leadCoeff := r.leadCoeff
    rhsScale := r.rhsScale }

/-- Under monicity (`leadCoeff = 1`), the leading step and rewritten remainder sum identically to `u`,
    and reversing generator ranks negates the orientation margin (`qou-ix9e`). -/
theorem monicRule_decomposition_and_orientation_antisymmetry
    (r : MonicTwoLetterRule) (u : Int) (hMonic : r.leadCoeff = 1) :
    ruleMonicLeadingStep r u + ruleRewrittenRemainder r u = u ∧
      ruleOrientationMargin (reverseRuleOrientation r) + ruleOrientationMargin r = 0 := by
  constructor
  · dsimp [ruleMonicLeadingStep, ruleRewrittenRemainder]
    rw [hMonic]
    omega
  · dsimp [ruleOrientationMargin, reverseRuleOrientation]
    omega

/-! ### 2. Overlap Critical-Pair Resolution & Context Linearity (`qou-lncp`) -/

/-- Carrier for a length-1 overlap critical pair with scaling parameters and ambient word weight. -/
structure OverlapCriticalPair where
  scaleA : Int
  scaleB : Int
  wordWeight : Int
  deriving DecidableEq, Repr

/-- Left overlap reduction branch `scaleA * (scaleB * wordWeight)`. -/
def overlapLeftBranch (p : OverlapCriticalPair) : Int :=
  p.scaleA * (p.scaleB * p.wordWeight)

/-- Right overlap reduction branch `scaleB * (scaleA * wordWeight)`. -/
def overlapRightBranch (p : OverlapCriticalPair) : Int :=
  p.scaleB * (p.scaleA * p.wordWeight)

/-- Critical-pair difference polynomial `overlapLeftBranch p - overlapRightBranch p`. -/
def overlapDifferencePolynomial (p : OverlapCriticalPair) : Int :=
  overlapLeftBranch p - overlapRightBranch p

/-- Two-term context multiplication `ctxLeft * (c1 * m1 + c2 * m2) * ctxRight`. -/
def contextTwoTermLift (ctxLeft ctxRight c1 m1 c2 m2 : Int) : Int :=
  ctxLeft * (c1 * m1 + c2 * m2) * ctxRight

/-- Every bi-scaled overlap critical pair resolves to zero and two-term context multiplication
    distributes linearly over the two summands (`qou-lncp`). -/
theorem overlap_critical_pair_vanishing_and_context_linearity
    (p : OverlapCriticalPair) (ctxLeft ctxRight c1 m1 c2 m2 : Int) :
    overlapDifferencePolynomial p = 0 ∧
      contextTwoTermLift ctxLeft ctxRight c1 m1 c2 m2 =
        c1 * (ctxLeft * m1 * ctxRight) + c2 * (ctxLeft * m2 * ctxRight) := by
  constructor
  · dsimp [overlapDifferencePolynomial, overlapLeftBranch, overlapRightBranch]
    rw [← Int.mul_assoc, Int.mul_comm p.scaleA p.scaleB, Int.mul_assoc]
    omega
  · dsimp [contextTwoTermLift]
    rw [Int.mul_add, Int.add_mul]
    rw [← Int.mul_assoc ctxLeft c1 m1, Int.mul_comm ctxLeft c1, Int.mul_assoc c1 ctxLeft m1,
        ← Int.mul_assoc c1 (ctxLeft * m1) ctxRight]
    rw [← Int.mul_assoc ctxLeft c2 m2, Int.mul_comm ctxLeft c2, Int.mul_assoc c2 ctxLeft m2,
        ← Int.mul_assoc c2 (ctxLeft * m2) ctxRight]

/-! ### 3. Multiplicative Formal Group Law Associativity & Unit Factorization (`qou-ulfe`) -/

/-- One-dimensional formal group law `F_lam(x, y) = x + y + lam * x * y`. -/
def multiplicativeFormalGroupLaw (lam x y : Int) : Int :=
  x + y + lam * x * y

/-- Unit-shifted group homomorphism `U_lam(x) = 1 + lam * x`. -/
def formalGroupUnitScale (lam x : Int) : Int :=
  1 + lam * x

/-- The formal group law `x + y + lam * x * y` is strictly associative and its unit-shifted scale
    factors multiplicatively as `(1 + lam * x) * (1 + lam * y)` (`qou-ulfe`). -/
theorem multiplicativeFormalGroupLaw_associativity_and_unit_factorization
    (lam x y z : Int) :
    multiplicativeFormalGroupLaw lam (multiplicativeFormalGroupLaw lam x y) z =
      multiplicativeFormalGroupLaw lam x (multiplicativeFormalGroupLaw lam y z) ∧
    formalGroupUnitScale lam (multiplicativeFormalGroupLaw lam x y) =
      formalGroupUnitScale lam x * formalGroupUnitScale lam y := by
  constructor
  · dsimp [multiplicativeFormalGroupLaw]
    rw [Int.mul_add, Int.mul_add, Int.add_mul, Int.add_mul]
    rw [Int.mul_add, Int.mul_add]
    rw [← Int.mul_assoc, ← Int.mul_assoc, ← Int.mul_assoc]
    have hcomm : lam * x * (lam * y) * z = lam * lam * x * y * z := by
      rw [← Int.mul_assoc (lam * x) lam y]
      rw [Int.mul_assoc lam x lam, Int.mul_comm x lam, ← Int.mul_assoc lam lam x]
    rw [hcomm]
    omega
  · dsimp [formalGroupUnitScale, multiplicativeFormalGroupLaw]
    rw [Int.mul_add, Int.mul_add, Int.add_mul, Int.mul_add]
    rw [Int.one_mul, Int.mul_add (lam * x), Int.mul_one]
    have hlam : lam * (lam * x * y) = lam * x * (lam * y) := by
      rw [← Int.mul_assoc lam (lam * x) y, ← Int.mul_assoc lam lam x]
      rw [← Int.mul_assoc (lam * x) lam y]
      rw [Int.mul_assoc lam x lam, Int.mul_comm x lam, ← Int.mul_assoc lam lam x]
    rw [hlam]
    omega

/-! ### 4. Distribution Algebra Divided-Power Normal-Form Confluence (`qou-znz5`) -/

/-- Divided-power exponent triple `(negExp, cartanExp, posExp)` for normal-form basis words. -/
structure DividedPowerTriple where
  negExp : Int
  cartanExp : Int
  posExp : Int
  deriving DecidableEq, Repr

/-- Componentwise sum of two divided-power exponent triples. -/
def addDividedPowerTriple (t1 t2 : DividedPowerTriple) : DividedPowerTriple :=
  { negExp := t1.negExp + t2.negExp
    cartanExp := t1.cartanExp + t2.cartanExp
    posExp := t1.posExp + t2.posExp }

/-- Linear normal-form filtration weight of a divided-power basis word. -/
def dividedPowerNormalWeight (t : DividedPowerTriple) (wNeg wCartan wPos : Int) : Int :=
  t.negExp * wNeg + t.cartanExp * wCartan + t.posExp * wPos

/-- Single-step exchange reduction `qScale * (eVal * fVal + kVal) - (qScale * eVal) * fVal`. -/
def dividedPowerStepExchange (qScale eVal fVal kVal : Int) : Int :=
  qScale * (eVal * fVal + kVal) - (qScale * eVal) * fVal

/-- Divided-power normal-form filtration weight is strictly additive under exponent composition
    and the single-step exchange reduction isolates the diagonal term `qScale * kVal` (`qou-znz5`). -/
theorem dividedPower_normal_weight_additivity_and_exchange_reduction
    (t1 t2 : DividedPowerTriple) (wNeg wCartan wPos qScale eVal fVal kVal : Int) :
    dividedPowerNormalWeight (addDividedPowerTriple t1 t2) wNeg wCartan wPos =
      dividedPowerNormalWeight t1 wNeg wCartan wPos + dividedPowerNormalWeight t2 wNeg wCartan wPos ∧
    dividedPowerStepExchange qScale eVal fVal kVal = qScale * kVal := by
  constructor
  · dsimp [dividedPowerNormalWeight, addDividedPowerTriple]
    rw [Int.add_mul, Int.add_mul, Int.add_mul]
    omega
  · dsimp [dividedPowerStepExchange]
    rw [Int.mul_add, ← Int.mul_assoc]
    omega

/-! ### 5. Specialization Flatness & Difference Factorization (`qou-pso0`) -/

/-- Evaluation of a 3-term deformed normal-form basis combination at parameter `tVal`. -/
def deformedCombinationEval (c0 c1 c2 tVal b0 b1 b2 : Int) : Int :=
  c0 * b0 + (c1 * tVal) * b1 + (c2 * tVal * tVal) * b2

/-- Divided difference quotient of `deformedCombinationEval` across parameters `tVal` and `sVal`. -/
def specializationDifferenceQuotient (c1 c2 tVal sVal b1 b2 : Int) : Int :=
  c1 * b1 + c2 * (tVal + sVal) * b2

/-- Specializing the deformed normal-form combination at `tVal = 1` recovers the undeformed basis
    combination and the two-point difference factors cleanly through `(tVal - sVal)` (`qou-pso0`). -/
theorem specializationAtOne_and_difference_factorization
    (c0 c1 c2 tVal sVal b0 b1 b2 : Int) :
    deformedCombinationEval c0 c1 c2 1 b0 b1 b2 = c0 * b0 + c1 * b1 + c2 * b2 ∧
      deformedCombinationEval c0 c1 c2 tVal b0 b1 b2 -
          deformedCombinationEval c0 c1 c2 sVal b0 b1 b2 =
        (tVal - sVal) * specializationDifferenceQuotient c1 c2 tVal sVal b1 b2 := by
  constructor
  · dsimp [deformedCombinationEval]
    rw [Int.mul_one, Int.mul_one, Int.mul_one]
  · dsimp [deformedCombinationEval, specializationDifferenceQuotient]
    have h1 : (c1 * tVal) * b1 - (c1 * sVal) * b1 = (tVal - sVal) * (c1 * b1) := by
      rw [Int.sub_mul, ← Int.mul_assoc tVal c1 b1, ← Int.mul_assoc sVal c1 b1]
      rw [Int.mul_comm tVal c1, Int.mul_comm sVal c1]
    have h2 : (c2 * tVal * tVal) * b2 - (c2 * sVal * sVal) * b2 =
        (tVal - sVal) * (c2 * (tVal + sVal) * b2) := by
      have hsq : tVal * tVal - sVal * sVal = (tVal - sVal) * (tVal + sVal) := by
        rw [Int.sub_mul, Int.mul_add, Int.mul_add, Int.mul_comm sVal tVal]
        omega
      calc
        (c2 * tVal * tVal) * b2 - (c2 * sVal * sVal) * b2
            = c2 * ((tVal * tVal - sVal * sVal) * b2) := by
              rw [Int.sub_mul, Int.mul_sub]
              rw [← Int.mul_assoc c2 (tVal * tVal) b2, ← Int.mul_assoc c2 tVal tVal]
              rw [← Int.mul_assoc c2 (sVal * sVal) b2, ← Int.mul_assoc c2 sVal sVal]
        _ = c2 * (((tVal - sVal) * (tVal + sVal)) * b2) := by rw [hsq]
        _ = (tVal - sVal) * (c2 * (tVal + sVal) * b2) := by
              rw [← Int.mul_assoc c2 ((tVal - sVal) * (tVal + sVal)) b2]
              rw [← Int.mul_assoc c2 (tVal - sVal) (tVal + sVal)]
              rw [Int.mul_comm c2 (tVal - sVal)]
              rw [Int.mul_assoc (tVal - sVal) c2 (tVal + sVal)]
              rw [Int.mul_assoc (tVal - sVal) (c2 * (tVal + sVal)) b2]
    rw [Int.mul_add, ← h1, ← h2]
    omega

end QOU.Foundations.MonicRewritingRuleOrientationOverlapCriticalPairResolutionFormalGroupLawDistributionConfluenceSpecializationFlatness
