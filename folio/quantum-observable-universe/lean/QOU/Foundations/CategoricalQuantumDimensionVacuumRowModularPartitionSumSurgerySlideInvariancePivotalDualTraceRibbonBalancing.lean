/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  - bwrt: Categorical quantum dimension unit normalization and vacuum row cross-product balance
  - bwse: Modular surgery partition sum factorization and vacuum sector isolation
  - rtkb: Surgery handle-slide bilinear linking discriminant invariance
  - rtqd: Pivotal dual-trace transport and swapped pairing conjugation symmetry
  - rtrb: Ribbon balancing twist tensor symmetry and double-mate shift invariance
-/

namespace QOU.Foundations.CategoricalQuantumDimensionVacuumRowModularPartitionSumSurgerySlideInvariancePivotalDualTraceRibbonBalancing

/-! ### 1. Categorical Quantum Dimension & Vacuum Row Proportionality (`bwrt`) -/

/-- Carrier for a braided right-rigid trace datum with coevaluation, braiding, evaluation, and total scale. -/
structure BraidedRigidTraceDatum where
  coevalWeight : Int
  braidingScale : Int
  evalWeight : Int
  totalQuantumScale : Int
  deriving DecidableEq, Repr

/-- Categorical quantum dimension `coevalWeight * braidingScale * evalWeight`. -/
def categoricalObjectDimension (d : BraidedRigidTraceDatum) : Int :=
  d.coevalWeight * d.braidingScale * d.evalWeight

/-- Cross-product residual `rowEntry * totalQuantumScale - categoricalObjectDimension d`. -/
def vacuumRowWeightCrossProduct (d : BraidedRigidTraceDatum) (rowEntry : Int) : Int :=
  rowEntry * d.totalQuantumScale - categoricalObjectDimension d

/-- Canonical monoidal unit trace datum with unit coevaluation, braiding, and evaluation weights. -/
def unitObjectTraceDatum (scale : Int) : BraidedRigidTraceDatum :=
  { coevalWeight := 1
    braidingScale := 1
    evalWeight := 1
    totalQuantumScale := scale }

/-- The categorical quantum dimension of the monoidal unit is `1` and evaluating the vacuum row
    cross-product at `categoricalObjectDimension d` factors as `d_X * (D - 1)` (`bwrt`). -/
theorem unitObjectDimension_eq_one_and_vacuumRow_balance
    (d : BraidedRigidTraceDatum) (scale : Int) :
    categoricalObjectDimension (unitObjectTraceDatum scale) = 1 ∧
      vacuumRowWeightCrossProduct d (categoricalObjectDimension d) =
        categoricalObjectDimension d * (d.totalQuantumScale - 1) := by
  constructor
  · rfl
  · dsimp [vacuumRowWeightCrossProduct]
    rw [Int.mul_sub, Int.mul_one]

/-! ### 2. Modular Surgery Partition Sum & Per-Label Weighted Decomposition (`bwse`) -/

/-- Carrier for a 3-label modular surgery sum with object dimensions, amplitudes, and common scale. -/
structure ThreeLabelModularDatum where
  dim0 : Int
  dim1 : Int
  dim2 : Int
  amp0 : Int
  amp1 : Int
  amp2 : Int
  commonFactor : Int
  deriving DecidableEq, Repr

/-- Unnormalized modular surgery sum `dim0 * amp0 + dim1 * amp1 + dim2 * amp2`. -/
def unnormalizedSurgerySum (m : ThreeLabelModularDatum) : Int :=
  m.dim0 * m.amp0 + m.dim1 * m.amp1 + m.dim2 * m.amp2

/-- Scaled modular partition sum with `commonFactor` distributed across each simple-object dimension. -/
def scaledModularPartitionSum (m : ThreeLabelModularDatum) : Int :=
  (m.commonFactor * m.dim0) * m.amp0 +
    (m.commonFactor * m.dim1) * m.amp1 +
    (m.commonFactor * m.dim2) * m.amp2

/-- Vacuum-projected datum with non-vacuum amplitudes zeroed. -/
def vacuumProjectedDatum (m : ThreeLabelModularDatum) : ThreeLabelModularDatum :=
  { dim0 := m.dim0
    dim1 := m.dim1
    dim2 := m.dim2
    amp0 := m.amp0
    amp1 := 0
    amp2 := 0
    commonFactor := m.commonFactor }

/-- Uniform scaling of simple-object dimensions factors out of the modular surgery partition sum,
    and projecting onto the vacuum channel isolates `dim0 * amp0` (`bwse`). -/
theorem modularPartitionSum_factorization_and_vacuum_isolation
    (m : ThreeLabelModularDatum) :
    scaledModularPartitionSum m = m.commonFactor * unnormalizedSurgerySum m ∧
      unnormalizedSurgerySum (vacuumProjectedDatum m) = m.dim0 * m.amp0 := by
  constructor
  · dsimp [scaledModularPartitionSum, unnormalizedSurgerySum]
    rw [Int.mul_add, Int.mul_add]
    rw [← Int.mul_assoc, ← Int.mul_assoc, ← Int.mul_assoc]
  · dsimp [unnormalizedSurgerySum, vacuumProjectedDatum]
    rw [Int.mul_zero, Int.mul_zero]
    omega

/-! ### 3. Surgery Handle-Slide Bilinear Linking Discriminant Invariance (`rtkb`) -/

/-- Two-component symmetric surgery linking matrix datum `(diagA, offDiagB, diagC)`. -/
structure SurgeryLinkingPair where
  diagA : Int
  offDiagB : Int
  diagC : Int
  deriving DecidableEq, Repr

/-- Handle-slide transformation `B' = B + k * A`, `C' = C + 2 * k * B + k^2 * A` along component 1. -/
def handleSlideTransformedPair (s : SurgeryLinkingPair) (kSlide : Int) : SurgeryLinkingPair :=
  { diagA := s.diagA
    offDiagB := s.offDiagB + kSlide * s.diagA
    diagC := s.diagC + 2 * kSlide * s.offDiagB + kSlide * kSlide * s.diagA }

/-- Bilinear linking determinant `diagA * diagC - offDiagB * offDiagB`. -/
def linkingDiscriminant (s : SurgeryLinkingPair) : Int :=
  s.diagA * s.diagC - s.offDiagB * s.offDiagB

/-- The two-component surgery linking discriminant is strictly invariant under any integer
    handle-slide move `kSlide` (`rtkb`). -/
theorem handleSlide_discriminant_invariance
    (s : SurgeryLinkingPair) (kSlide : Int) :
    linkingDiscriminant (handleSlideTransformedPair s kSlide) = linkingDiscriminant s := by
  dsimp [linkingDiscriminant, handleSlideTransformedPair]
  rw [Int.mul_add, Int.mul_add]
  rw [Int.add_mul, Int.mul_add, Int.mul_add]
  have hcross1 : s.offDiagB * (kSlide * s.diagA) = s.diagA * (kSlide * s.offDiagB) := by
    rw [← Int.mul_assoc s.offDiagB kSlide s.diagA, Int.mul_comm (s.offDiagB * kSlide) s.diagA]
    rw [Int.mul_comm s.offDiagB kSlide]
  have hcross2 : kSlide * s.diagA * s.offDiagB = s.diagA * (kSlide * s.offDiagB) := by
    rw [Int.mul_comm kSlide s.diagA, Int.mul_assoc s.diagA kSlide s.offDiagB]
  have htwo : s.diagA * (2 * kSlide * s.offDiagB) =
      s.diagA * (kSlide * s.offDiagB) + s.diagA * (kSlide * s.offDiagB) := by
    have h2 : (2 : Int) * kSlide * s.offDiagB = kSlide * s.offDiagB + kSlide * s.offDiagB := by
      rw [Int.mul_assoc (2 : Int) kSlide s.offDiagB]
      omega
    rw [h2, Int.mul_add]
  have hsq : kSlide * s.diagA * (kSlide * s.diagA) =
      s.diagA * (kSlide * kSlide * s.diagA) := by
    rw [← Int.mul_assoc (kSlide * s.diagA) kSlide s.diagA]
    rw [Int.mul_assoc kSlide s.diagA kSlide]
    rw [Int.mul_comm s.diagA kSlide]
    rw [← Int.mul_assoc kSlide kSlide s.diagA]
    rw [Int.mul_comm (kSlide * kSlide * s.diagA) s.diagA]
  rw [hcross1, hcross2, htwo, hsq]
  omega

/-! ### 4. Pivotal Dual-Trace Transport & Swapped Pairing Conjugation Symmetry (`rtqd`) -/

/-- Carrier for a swapped right-dual pairing trace datum with inverse and forward braidings. -/
structure SwappedDualPairingDatum where
  leftCoeval : Int
  braidingHom : Int
  braidingInv : Int
  rightEval : Int
  deriving DecidableEq, Repr

/-- Standard right quantum trace `leftCoeval * (braidingHom * rightEval)`. -/
def rightQuantumTrace (p : SwappedDualPairingDatum) : Int :=
  p.leftCoeval * (p.braidingHom * p.rightEval)

/-- Swapped-pairing dual quantum trace `leftCoeval * (braidingInv * (braidingHom * (braidingHom * rightEval)))`. -/
def swappedDualQuantumTrace (p : SwappedDualPairingDatum) : Int :=
  p.leftCoeval * (p.braidingInv * (p.braidingHom * (p.braidingHom * p.rightEval)))

/-- Whenever the inverse braiding cancels the forward braiding (`braidingInv * braidingHom = 1`),
    the swapped-pairing dual quantum trace equals the standard right quantum trace (`rtqd`). -/
theorem swappedDualQuantumTrace_eq_rightQuantumTrace
    (p : SwappedDualPairingDatum) (hCancel : p.braidingInv * p.braidingHom = 1) :
    swappedDualQuantumTrace p = rightQuantumTrace p := by
  dsimp [swappedDualQuantumTrace, rightQuantumTrace]
  rw [← Int.mul_assoc p.braidingInv p.braidingHom (p.braidingHom * p.rightEval)]
  rw [hCancel, Int.one_mul]

/-! ### 5. Ribbon Balancing Twist Multiplicativity & Double-Dual Mate Commutation (`rtrb`) -/

/-- Carrier for a ribbon balancing datum on a tensor product with component twists and double braiding. -/
structure RibbonBalancingDatum where
  twistX : Int
  twistY : Int
  doubleBraidingXY : Int
  deriving DecidableEq, Repr

/-- Ribbon twist `(twistX * twistY) * doubleBraidingXY` on `X ⊗ Y`. -/
def tensorRibbonTwist (r : RibbonBalancingDatum) : Int :=
  (r.twistX * r.twistY) * r.doubleBraidingXY

/-- Factor-swapped ribbon twist `(twistY * twistX) * doubleBraidingXY`. -/
def transposedRibbonTwist (r : RibbonBalancingDatum) : Int :=
  (r.twistY * r.twistX) * r.doubleBraidingXY

/-- Iterated adjoint-mate shift `mateStep + (mateStep + baseTwist) - 2 * mateStep`. -/
def iteratedMateShift (mateStep baseTwist : Int) : Int :=
  mateStep + (mateStep + baseTwist) - 2 * mateStep

/-- The composite tensor ribbon twist is invariant under swapping the component twist factors
    and applying two adjoint-mate shifts followed by double-dual normalization restores `baseTwist` (`rtrb`). -/
theorem ribbonTwist_tensor_symmetry_and_doubleMate_fixed
    (r : RibbonBalancingDatum) (mateStep baseTwist : Int) :
    tensorRibbonTwist r = transposedRibbonTwist r ∧
      iteratedMateShift mateStep baseTwist = baseTwist := by
  constructor
  · dsimp [tensorRibbonTwist, transposedRibbonTwist]
    rw [Int.mul_comm r.twistX r.twistY]
  · dsimp [iteratedMateShift]
    omega

end QOU.Foundations.CategoricalQuantumDimensionVacuumRowModularPartitionSumSurgerySlideInvariancePivotalDualTraceRibbonBalancing
