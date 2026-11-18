/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  - rttg: Framed-tangle snake zig-zag coherence and crossing inverse cancellation
  - qou-50vf: Four-term chord submodule alternating sum and exchange antisymmetry
  - qou-aezg: Singular crossing double-jump resolution and transpose invariance
  - qou-dcvv: Filtration profile shift promotion and inverse-crossing sector reconstruction
  - qou-fwah: Fibration cube-pair retraction endpoints and connecting boundary difference
-/

namespace QOU.Foundations.FramedTangleSnakeCoherenceFourTermChordRelationSingularResolutionAlternationFiltrationProfileShiftCubePairBoundaryLift

/-! ### 1. Framed-Tangle Snake Coherence & Crossing Inverse Cancellation (`rttg`) -/

/-- Carrier for framed-tangle generator scalar weights (cup, cap, positive/negative crossings, twist). -/
structure FramedTangleGeneratorImage where
  cupWeight : Int
  capWeight : Int
  posCrossing : Int
  negCrossing : Int
  framingTwist : Int
  deriving DecidableEq, Repr

/-- Snake zig-zag composite `capWeight * (cupWeight * strandVal)`. -/
def snakeZigZagComposite (g : FramedTangleGeneratorImage) (strandVal : Int) : Int :=
  g.capWeight * (g.cupWeight * strandVal)

/-- Double-crossing composite `negCrossing * (posCrossing * strandVal)`. -/
def doubleCrossingComposite (g : FramedTangleGeneratorImage) (strandVal : Int) : Int :=
  g.negCrossing * (g.posCrossing * strandVal)

/-- Under exact pairing normalization (`capWeight * cupWeight = 1`) and crossing inversion
    (`negCrossing * posCrossing = 1`), both the snake zig-zag and double-crossing composites
    act as the identity on every strand value (`rttg`). -/
theorem snakeZigZag_and_doubleCrossing_identity
    (g : FramedTangleGeneratorImage) (strandVal : Int)
    (hSnake : g.capWeight * g.cupWeight = 1)
    (hCross : g.negCrossing * g.posCrossing = 1) :
    snakeZigZagComposite g strandVal = strandVal ∧
      doubleCrossingComposite g strandVal = strandVal := by
  constructor
  · dsimp [snakeZigZagComposite]
    rw [← Int.mul_assoc, hSnake, Int.one_mul]
  · dsimp [doubleCrossingComposite]
    rw [← Int.mul_assoc, hCross, Int.one_mul]

/-! ### 2. Four-Term Chord Submodule Alternating Sum & Exchange Symmetry (`qou-50vf`) -/

/-- Carrier for a four-term chord diagram quadruple `(chordAB, chordAC, chordBCLeft, chordBCRight)`. -/
structure FourTermChordQuadruple where
  chordAB : Int
  chordAC : Int
  chordBCLeft : Int
  chordBCRight : Int
  deriving DecidableEq, Repr

/-- Four-term submodule linear combination `(chordAB - chordAC) + (chordBCLeft - chordBCRight)`. -/
def fourTermCombination (q : FourTermChordQuadruple) : Int :=
  (q.chordAB - q.chordAC) + (q.chordBCLeft - q.chordBCRight)

/-- Pair-swapped four-term quadruple exchanging `AB ↔ AC` and `BCLeft ↔ BCRight`. -/
def swappedFourTermQuadruple (q : FourTermChordQuadruple) : FourTermChordQuadruple :=
  { chordAB := q.chordAC
    chordAC := q.chordAB
    chordBCLeft := q.chordBCRight
    chordBCRight := q.chordBCLeft }

/-- Swapping adjacent chord pairs negates `fourTermCombination`, and whenever the balanced chord
    sum `chordAB + chordBCLeft = chordAC + chordBCRight` holds, the four-term combination vanishes (`qou-50vf`). -/
theorem fourTermCombination_antisymmetry_and_balanced_vanishing
    (q : FourTermChordQuadruple)
    (hBal : q.chordAB + q.chordBCLeft = q.chordAC + q.chordBCRight) :
    fourTermCombination (swappedFourTermQuadruple q) + fourTermCombination q = 0 ∧
      fourTermCombination q = 0 := by
  constructor
  · dsimp [fourTermCombination, swappedFourTermQuadruple]
    omega
  · dsimp [fourTermCombination]
    omega

/-! ### 3. Singular Crossing Double-Jump Resolution & Transpose Invariance (`qou-aezg`) -/

/-- Carrier for a two-singular-point braid resolution table `(overOver, overUnder, underOver, underUnder)`. -/
structure SingularCrossingPair where
  overOver : Int
  overUnder : Int
  underOver : Int
  underUnder : Int
  deriving DecidableEq, Repr

/-- First-crossing jump `overOver - underOver`. -/
def primarySingularJump (s : SingularCrossingPair) : Int :=
  s.overOver - s.underOver

/-- Second-crossing jump `overUnder - underUnder`. -/
def secondarySingularJump (s : SingularCrossingPair) : Int :=
  s.overUnder - s.underUnder

/-- Double singular resolution difference `primarySingularJump s - secondarySingularJump s`. -/
def doubleSingularResolution (s : SingularCrossingPair) : Int :=
  primarySingularJump s - secondarySingularJump s

/-- Transposed singular resolution table exchanging the order of the two singular crossings. -/
def transposedSingularPair (s : SingularCrossingPair) : SingularCrossingPair :=
  { overOver := s.overOver
    overUnder := s.underOver
    underOver := s.overUnder
    underUnder := s.underUnder }

/-- The double singular crossing resolution is invariant under transposing the order of the two
    singular crossings and expands to the alternating four-state sum (`qou-aezg`). -/
theorem doubleSingularResolution_transpose_invariance
    (s : SingularCrossingPair) :
    doubleSingularResolution (transposedSingularPair s) = doubleSingularResolution s ∧
      doubleSingularResolution s = s.overOver - s.overUnder - s.underOver + s.underUnder := by
  constructor
  · dsimp [doubleSingularResolution, primarySingularJump, secondarySingularJump, transposedSingularPair]
    omega
  · dsimp [doubleSingularResolution, primarySingularJump, secondarySingularJump]
    omega

/-! ### 4. Filtration Profile Shift Promotion & Inverse-Crossing Sector Reconstruction (`qou-dcvv`) -/

/-- Carrier for a 3-slot filtration profile datum with inverse-crossing shift parameter `crossingScaleA`. -/
structure FiltrationProfileDatum where
  degZero : Int
  degOne : Int
  degTwo : Int
  crossingScaleA : Int
  deriving DecidableEq, Repr

/-- Sum of the base filtration profile entries. -/
def baseProfileSum (p : FiltrationProfileDatum) : Int :=
  p.degZero + p.degOne + p.degTwo

/-- Sum of the filtration profile entries after uniform fresh-generator promotion by `shiftDelta`. -/
def freshGeneratorPromotedSum (p : FiltrationProfileDatum) (shiftDelta : Int) : Int :=
  (p.degZero + shiftDelta) + (p.degOne + shiftDelta) + (p.degTwo + shiftDelta)

/-- Inverse-crossing sector step `genT - scaleA`. -/
def inverseCrossingSectorStep (genT scaleA : Int) : Int :=
  genT - scaleA

/-- Uniform fresh-generator grade promotion shifts the total filtration profile sum by `3 * shiftDelta`
    without splitting slots, and adding `crossingScaleA` reconstructs the forward crossing generator (`qou-dcvv`). -/
theorem freshGenerator_profile_promotion_and_inverseCrossing_reconstruction
    (p : FiltrationProfileDatum) (shiftDelta genT : Int) :
    freshGeneratorPromotedSum p shiftDelta = baseProfileSum p + 3 * shiftDelta ∧
      inverseCrossingSectorStep genT p.crossingScaleA + p.crossingScaleA = genT := by
  constructor
  · dsimp [freshGeneratorPromotedSum, baseProfileSum]
    omega
  · dsimp [inverseCrossingSectorStep]
    omega

/-! ### 5. Fibration Cube-Pair Retraction Endpoints & Connecting Boundary Difference (`qou-fwah`) -/

/-- Carrier for a relative cube-pair lifting datum with top face and basepoint evaluations. -/
structure CubePairLiftingDatum where
  topFaceVal : Int
  basePointVal : Int
  sideWallFlux : Int
  deriving DecidableEq, Repr

/-- Relative boundary difference `topFaceVal - basePointVal`. -/
def relativeCubeBoundaryEval (c : CubePairLiftingDatum) : Int :=
  c.topFaceVal - c.basePointVal

/-- Linear radial-retraction lift `basePointVal + tParam * relativeCubeBoundaryEval c`. -/
def radialRetractedLift (c : CubePairLiftingDatum) (tParam : Int) : Int :=
  c.basePointVal + tParam * relativeCubeBoundaryEval c

/-- Connecting map boundary difference `radialRetractedLift c 1 - radialRetractedLift c 0`. -/
def connectingBoundaryDifference (c : CubePairLiftingDatum) : Int :=
  radialRetractedLift c 1 - radialRetractedLift c 0

/-- The radial-retraction lift interpolates between `basePointVal` at `tParam = 0` and `topFaceVal`
    at `tParam = 1`, and its endpoint difference equals `relativeCubeBoundaryEval c` (`qou-fwah`). -/
theorem cubePair_retraction_endpoints_and_connecting_boundary
    (c : CubePairLiftingDatum) :
    radialRetractedLift c 0 = c.basePointVal ∧
      radialRetractedLift c 1 = c.topFaceVal ∧
      connectingBoundaryDifference c = relativeCubeBoundaryEval c := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp [radialRetractedLift, relativeCubeBoundaryEval]
    omega
  · dsimp [radialRetractedLift, relativeCubeBoundaryEval]
    omega
  · dsimp [connectingBoundaryDifference, radialRetractedLift, relativeCubeBoundaryEval]
    omega

end QOU.Foundations.FramedTangleSnakeCoherenceFourTermChordRelationSingularResolutionAlternationFiltrationProfileShiftCubePairBoundaryLift
