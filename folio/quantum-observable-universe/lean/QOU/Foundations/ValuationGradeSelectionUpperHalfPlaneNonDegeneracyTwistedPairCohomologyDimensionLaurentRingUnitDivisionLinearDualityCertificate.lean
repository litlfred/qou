/-
Copyright (c) 2026 Quantum Observable Universe Project. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Valuation Grade Selection, Upper-Half-Plane Non-Degeneracy, Twisted Pair Cohomology Dimension, Laurent Ring Unit Division, and Linear Duality Certificate

Formalizes five structural foundations in a zero-import integer-arithmetic module:

1. **Jet-Order Valuation Grade-Value vs Single-Degree Coinvariant Selection (`qou-71ma`)**:
   Models a two-component graded coinvariant carrier `GradedValuationCarrier` with lower and
   upper grades (`lowerGrade`, `upperGrade`), multiplicities (`lowerWeight`, `upperWeight`),
   and an equivariant driver shift (`driverShift`). Proves that the weighted grade moment
   decomposes into the minimum-grade baseline plus the single-degree selection defect
   `(upperGrade - lowerGrade) * upperWeight`, so promoting a valuation from a grade-value bound
   to single-degree selection holds if and only if the upper-grade selection defect vanishes,
   and proves the equivariant driver-shift covariance law.

2. **Upper-Half-Plane Complex Lattice Point Non-Degeneracy (`qou-n226`)**:
   Models a complex lattice coordinate `UpperHalfLatticePoint` with real and imaginary parts
   (`rePart`, `imPart`) and unit scale (`unitScale`). Proves that strict positivity of the
   imaginary part (`1 ≤ imPart`) unconditionally forces non-vanishing of `originImaginaryDist`,
   non-coincidence with the origin `(0, 0)`, and non-coincidence with the unit point
   `(unitScale, 0)`, while establishing the exact linear holonomy shift identity between origin
   and unit-centered coordinates.

3. **Twisted Pair Long Exact Sequence Dimension vs Real-Embedding Remainder (`qou-oilr`)**:
   Models the cohomological dimension profile `AdjointPairCohomologyData` of a 3-manifold pair
   `(M, dM)` with adjoint local coefficients alongside a knot-indexed real-embedding remainder.
   Proves that vanishing pair Euler characteristic together with vanishing degree-0 and degree-3
   cohomology forces `dimH1 = dimH2`, and that under unit boundary rank (`dimH2 = 1`) the
   cohomological degree-1 dimension is pinned to `1` while the arity discrepancy measure
   `realEmbeddingRemainder - dimH1` separates the knot-indexed real-embedding remainder from the
   degree-indexed cohomological dimension vector.

4. **Ground-Ring Localization vs Laurent Unit Division Obstruction (`qou-omuz`)**:
   Models quantum-dimension trace normalization `QuantumDimensionNormalizationData` over an
   integral Laurent ring versus its fraction field. Proves that a non-unit quantum dimension
   numerator (`quantumDimNumerator = 2`) admits no integer multiplicative inverse (`2 * k - 1 ≠ 0`
   for all `k : Int`), whereas clearing denominators over the fraction field satisfies an exact
   universal bilinear identity.

5. **Primal-Dual Linear Program Strong Duality & Zero-Gap Certificate (`qou-wxmm`)**:
   Models a primal-dual linear optimization certificate `PrimalDualLinearCertificate` with dual
   multipliers, right-hand sides, and primal slacks. Proves that the duality gap
   `dualObjective - primalObjective` equals the complementary slackness inner product, so
   non-negative slackness products enforce weak duality (`primalObjective ≤ dualObjective`) and
   strong zero-gap optimality holds if and only if the complementary slackness sum vanishes.
-/

namespace QOU.Foundations.ValuationGradeSelectionUpperHalfPlaneNonDegeneracyTwistedPairCohomologyDimensionLaurentRingUnitDivisionLinearDualityCertificate

/-! ## 1. Jet-Order Valuation Grade-Value vs Single-Degree Coinvariant Selection (`qou-71ma`) -/

/-- Two-component graded coinvariant carrier with lower/upper grades, weights, and driver shift. -/
structure GradedValuationCarrier where
  lowerGrade : Int
  upperGrade : Int
  lowerWeight : Int
  upperWeight : Int
  driverShift : Int
  deriving DecidableEq, Repr

/-- Baseline valuation given by the minimum (leading) jet-order grade. -/
def minimumGradeValuation (g : GradedValuationCarrier) : Int :=
  g.lowerGrade

/-- Total multiplicity across the lower and upper graded components. -/
def totalGradeWeight (g : GradedValuationCarrier) : Int :=
  g.lowerWeight + g.upperWeight

/-- Weighted grade moment across both graded coinvariant components. -/
def weightedGradeMoment (g : GradedValuationCarrier) : Int :=
  g.lowerGrade * g.lowerWeight + g.upperGrade * g.upperWeight

/-- Obstruction defect measuring deviation from single-degree concentration at `lowerGrade`. -/
def singleDegreeDefect (g : GradedValuationCarrier) : Int :=
  (g.upperGrade - g.lowerGrade) * g.upperWeight

/-- Driver-shifted weighted grade moment after translating both grades by `driverShift`. -/
def driverShiftedMoment (g : GradedValuationCarrier) : Int :=
  (g.lowerGrade + g.driverShift) * g.lowerWeight +
    (g.upperGrade + g.driverShift) * g.upperWeight

/-- Concrete inhabitant of `GradedValuationCarrier`. -/
def sampleGradedValuationCarrier : GradedValuationCarrier :=
  { lowerGrade := 3
    upperGrade := 5
    lowerWeight := 4
    upperWeight := 2
    driverShift := 7 }

/-- The weighted grade moment decomposes into the baseline valuation times total weight plus the
    single-degree selection defect, and single-degree concentration holds iff the defect vanishes. -/
theorem weightedGradeMoment_decomposition_and_singleDegreeSelection
    (g : GradedValuationCarrier) :
    weightedGradeMoment g =
      minimumGradeValuation g * totalGradeWeight g + singleDegreeDefect g ∧
    (weightedGradeMoment g = minimumGradeValuation g * totalGradeWeight g ↔
      singleDegreeDefect g = 0) := by
  dsimp [weightedGradeMoment, minimumGradeValuation, totalGradeWeight, singleDegreeDefect]
  rw [Int.mul_add, Int.sub_mul]
  omega

/-- Translating grades by `driverShift` shifts the weighted grade moment by
    `driverShift * totalGradeWeight g`. -/
theorem driverShiftedMoment_covariance
    (g : GradedValuationCarrier) :
    driverShiftedMoment g =
      weightedGradeMoment g + g.driverShift * totalGradeWeight g := by
  dsimp [driverShiftedMoment, weightedGradeMoment, totalGradeWeight]
  rw [Int.add_mul, Int.add_mul, Int.mul_add]
  omega

/-- Concrete evaluation of `sampleGradedValuationCarrier`. -/
theorem sampleGradedValuationCarrier_eval :
    weightedGradeMoment sampleGradedValuationCarrier = 22 ∧
    singleDegreeDefect sampleGradedValuationCarrier = 4 ∧
    driverShiftedMoment sampleGradedValuationCarrier = 64 := by
  decide

/-! ## 2. Upper-Half-Plane Complex Lattice Point Non-Degeneracy (`qou-n226`) -/

/-- Complex lattice coordinate `(rePart, imPart)` with unit reference `(unitScale, 0)`. -/
structure UpperHalfLatticePoint where
  rePart : Int
  imPart : Int
  unitScale : Int
  deriving DecidableEq, Repr

/-- Vertical displacement above the real axis. -/
def originImaginaryDist (z : UpperHalfLatticePoint) : Int :=
  z.imPart

/-- Horizontal offset relative to the unit point `(unitScale, 0)`. -/
def unitRealOffset (z : UpperHalfLatticePoint) : Int :=
  z.rePart - z.unitScale

/-- Linear holonomy functional centered at the origin `(0, 0)`. -/
def originHolonomyFunctional (z : UpperHalfLatticePoint) (a b : Int) : Int :=
  a * z.rePart + b * z.imPart

/-- Linear holonomy functional centered at the unit degeneracy point `(unitScale, 0)`. -/
def unitHolonomyFunctional (z : UpperHalfLatticePoint) (a b : Int) : Int :=
  a * unitRealOffset z + b * originImaginaryDist z

/-- Concrete inhabitant of `UpperHalfLatticePoint`. -/
def sampleUpperHalfLatticePoint : UpperHalfLatticePoint :=
  { rePart := 1
    imPart := 3
    unitScale := 2 }

/-- Positive imaginary part (`1 ≤ imPart`) alone forces non-vanishing imaginary distance and
    eliminates both the origin `(0, 0)` and unit `(unitScale, 0)` degeneracies, while the
    origin-centered and unit-centered holonomy functionals differ by `a * unitScale`. -/
theorem im_pos_eliminates_degeneracies_and_holonomy_shift
    (z : UpperHalfLatticePoint) (a b : Int)
    (hIm : 1 ≤ z.imPart) :
    originImaginaryDist z ≠ 0 ∧
    (z.rePart ≠ 0 ∨ z.imPart ≠ 0) ∧
    (unitRealOffset z ≠ 0 ∨ originImaginaryDist z ≠ 0) ∧
    originHolonomyFunctional z a b - unitHolonomyFunctional z a b = a * z.unitScale := by
  dsimp [originImaginaryDist, unitRealOffset, originHolonomyFunctional, unitHolonomyFunctional]
  rw [Int.mul_sub]
  omega

/-- Concrete evaluation of `sampleUpperHalfLatticePoint`. -/
theorem sampleUpperHalfLatticePoint_eval :
    originImaginaryDist sampleUpperHalfLatticePoint = 3 ∧
    unitRealOffset sampleUpperHalfLatticePoint = -1 ∧
    originHolonomyFunctional sampleUpperHalfLatticePoint 5 4 = 17 ∧
    unitHolonomyFunctional sampleUpperHalfLatticePoint 5 4 = 7 := by
  decide

/-! ## 3. Twisted Pair Long Exact Sequence Dimension vs Real-Embedding Remainder (`qou-oilr`) -/

/-- Cohomological dimension profile of a 3-manifold pair `(M, dM)` with adjoint coefficients
    together with a knot-indexed real-embedding remainder. -/
structure AdjointPairCohomologyData where
  dimH0 : Int
  dimH1 : Int
  dimH2 : Int
  dimH3 : Int
  realEmbeddingRemainder : Int
  deriving DecidableEq, Repr

/-- Euler characteristic of the twisted cochain complex in degrees `0 .. 3`. -/
def pairEulerCharacteristic (c : AdjointPairCohomologyData) : Int :=
  c.dimH0 - c.dimH1 + c.dimH2 - c.dimH3

/-- Adjoint representation core base count (`dim sl_2 = 3`). -/
def adjointCoreBaseCount : Int := 3

/-- Knot-indexed total state count obtained by adding `realEmbeddingRemainder` to the adjoint core. -/
def knotIndexedTotalCount (c : AdjointPairCohomologyData) : Int :=
  adjointCoreBaseCount + c.realEmbeddingRemainder

/-- Signed arity discrepancy between the knot-indexed remainder and degree-1 cohomology dimension. -/
def arityDiscrepancyMeasure (c : AdjointPairCohomologyData) : Int :=
  c.realEmbeddingRemainder - c.dimH1

/-- Concrete inhabitant representing the figure-eight complement (`realEmbeddingRemainder = 0`,
    `dimH1 = 1`). -/
def sampleAdjointPairCohomologyData : AdjointPairCohomologyData :=
  { dimH0 := 0
    dimH1 := 1
    dimH2 := 1
    dimH3 := 0
    realEmbeddingRemainder := 0 }

/-- Vanishing Euler characteristic with trivial degree-0 and degree-3 cohomology forces
    `dimH1 = dimH2`, and unit degree-2 boundary image (`dimH2 = 1`) pins `dimH1 = 1` while
    separating the knot-indexed remainder from the cohomological dimension via
    `arityDiscrepancyMeasure c = c.realEmbeddingRemainder - 1`. -/
theorem pair_cohomology_h1_pinning_and_arity_separation
    (c : AdjointPairCohomologyData)
    (hEuler : pairEulerCharacteristic c = 0)
    (h0 : c.dimH0 = 0)
    (h3 : c.dimH3 = 0)
    (h2 : c.dimH2 = 1) :
    c.dimH1 = 1 ∧
    knotIndexedTotalCount c - adjointCoreBaseCount = c.realEmbeddingRemainder ∧
    arityDiscrepancyMeasure c = c.realEmbeddingRemainder - 1 := by
  dsimp [pairEulerCharacteristic, knotIndexedTotalCount, adjointCoreBaseCount,
    arityDiscrepancyMeasure] at *
  omega

/-- Concrete evaluation of `sampleAdjointPairCohomologyData` witnessing `arityDiscrepancyMeasure = -1`. -/
theorem sampleAdjointPairCohomologyData_eval :
    pairEulerCharacteristic sampleAdjointPairCohomologyData = 0 ∧
    knotIndexedTotalCount sampleAdjointPairCohomologyData = 3 ∧
    arityDiscrepancyMeasure sampleAdjointPairCohomologyData = -1 := by
  decide

/-! ## 4. Ground-Ring Localization vs Laurent Unit Division Obstruction (`qou-omuz`) -/

/-- Quantum-dimension trace normalization carrier over a Laurent ring vs its fraction field. -/
structure QuantumDimensionNormalizationData where
  laurentUnitExponent : Int
  quantumDimNumerator : Int
  traceWeightFactor : Int
  commonScale : Int
  deriving DecidableEq, Repr

/-- Residual `quantumDimNumerator * candidateInverse - 1` testing invertibility in `Int`. -/
def nonUnitDivisionResidual (d : QuantumDimensionNormalizationData) (candidateInverse : Int) : Int :=
  d.quantumDimNumerator * candidateInverse - 1

/-- Cleared-denominator normalized trace weight in the fraction field. -/
def clearedDenominatorLHS (d : QuantumDimensionNormalizationData) : Int :=
  d.commonScale * d.traceWeightFactor

/-- Unnormalized product prior to dividing by `quantumDimNumerator`. -/
def clearedDenominatorRHS (d : QuantumDimensionNormalizationData) : Int :=
  d.quantumDimNumerator * d.commonScale * d.traceWeightFactor

/-- Concrete inhabitant of `QuantumDimensionNormalizationData`. -/
def sampleQuantumDimensionNormalizationData : QuantumDimensionNormalizationData :=
  { laurentUnitExponent := 2
    quantumDimNumerator := 2
    traceWeightFactor := 5
    commonScale := 3 }

/-- When `quantumDimNumerator = 2`, no integer inverse exists (`nonUnitDivisionResidual d k ≠ 0`
    for every `k : Int`), whereas clearing denominators over the fraction field satisfies the
    universal bilinear identity `clearedDenominatorRHS d = d.quantumDimNumerator * clearedDenominatorLHS d`. -/
theorem nonUnit_quantumDim_obstruction_and_cleared_normalization
    (d : QuantumDimensionNormalizationData) (k : Int)
    (hDim : d.quantumDimNumerator = 2) :
    nonUnitDivisionResidual d k ≠ 0 ∧
    clearedDenominatorRHS d - d.quantumDimNumerator * clearedDenominatorLHS d = 0 := by
  dsimp [nonUnitDivisionResidual, clearedDenominatorLHS, clearedDenominatorRHS]
  rw [← Int.mul_assoc d.quantumDimNumerator d.commonScale d.traceWeightFactor, hDim]
  omega

/-- Concrete evaluation of `sampleQuantumDimensionNormalizationData`. -/
theorem sampleQuantumDimensionNormalizationData_eval :
    nonUnitDivisionResidual sampleQuantumDimensionNormalizationData 1 = 1 ∧
    clearedDenominatorLHS sampleQuantumDimensionNormalizationData = 15 ∧
    clearedDenominatorRHS sampleQuantumDimensionNormalizationData = 30 := by
  decide

/-! ## 5. Primal-Dual Linear Program Strong Duality & Zero-Gap Certificate (`qou-wxmm`) -/

/-- Primal-dual linear optimization certificate with dual multipliers, RHS bounds, and primal slacks. -/
structure PrimalDualLinearCertificate where
  dualMultiplier1 : Int
  dualMultiplier2 : Int
  rhs1 : Int
  rhs2 : Int
  slack1 : Int
  slack2 : Int
  deriving DecidableEq, Repr

/-- Dual objective value `y_1 * b_1 + y_2 * b_2`. -/
def dualObjective (p : PrimalDualLinearCertificate) : Int :=
  p.dualMultiplier1 * p.rhs1 + p.dualMultiplier2 * p.rhs2

/-- Complementary slackness inner product `y_1 * s_1 + y_2 * s_2`. -/
def complementarySlacknessSum (p : PrimalDualLinearCertificate) : Int :=
  p.dualMultiplier1 * p.slack1 + p.dualMultiplier2 * p.slack2

/-- Primal objective value expressed via dual feasibility and primal slack equations. -/
def primalObjective (p : PrimalDualLinearCertificate) : Int :=
  p.dualMultiplier1 * p.rhs1 + p.dualMultiplier2 * p.rhs2 -
    (p.dualMultiplier1 * p.slack1 + p.dualMultiplier2 * p.slack2)

/-- Primal-dual duality gap `dualObjective p - primalObjective p`. -/
def dualityGap (p : PrimalDualLinearCertificate) : Int :=
  dualObjective p - primalObjective p

/-- Concrete inhabitant of `PrimalDualLinearCertificate`. -/
def samplePrimalDualLinearCertificate : PrimalDualLinearCertificate :=
  { dualMultiplier1 := 4
    dualMultiplier2 := 3
    rhs1 := 6
    rhs2 := 5
    slack1 := 0
    slack2 := 0 }

/-- The duality gap equals the complementary slackness sum; non-negative complementary slackness
    implies weak duality (`primalObjective p ≤ dualObjective p`), and strong zero-gap optimality
    holds if and only if the complementary slackness sum vanishes. -/
theorem primalDual_weakDuality_and_strongZeroGap_iff
    (p : PrimalDualLinearCertificate)
    (hNonneg : 0 ≤ complementarySlacknessSum p) :
    dualityGap p = complementarySlacknessSum p ∧
    primalObjective p ≤ dualObjective p ∧
    (dualityGap p = 0 ↔ complementarySlacknessSum p = 0) := by
  dsimp [dualityGap, dualObjective, primalObjective, complementarySlacknessSum] at *
  omega

/-- Concrete evaluation of `samplePrimalDualLinearCertificate`. -/
theorem samplePrimalDualLinearCertificate_eval :
    dualObjective samplePrimalDualLinearCertificate = 39 ∧
    primalObjective samplePrimalDualLinearCertificate = 39 ∧
    complementarySlacknessSum samplePrimalDualLinearCertificate = 0 ∧
    dualityGap samplePrimalDualLinearCertificate = 0 := by
  decide

end QOU.Foundations.ValuationGradeSelectionUpperHalfPlaneNonDegeneracyTwistedPairCohomologyDimensionLaurentRingUnitDivisionLinearDualityCertificate
