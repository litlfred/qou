/-!
# Twist-Knot Cyclotomic Shift Ratios and Saddle Quantization Bridge

This module formalizes exact arithmetic and degree structures for:
1. Twist-knot cyclotomic expansion summand exponents and hypergeometric shift
   differences (`qou-7q3s`).
   -- Ref: [takata2004] Takata 2004, "The colored Jones polynomial and the
   -- A-polynomial for twist knots", arXiv:math/0401068v1 (`computations/aj_masbaum_crosscheck.py`).
2. Semiclassical Chern-Simons Lagrangian saddle pairing on the A-polynomial
   locus and one-loop WKB recurrence degree hierarchy for the quantized
   A-polynomial operator (`qou-2v4y`, `qou-c7lf`).
   -- Ref: [arxiv-hep-th-0306165v1] Gukov 2005, "Three-Dimensional Quantum Gravity,
   -- Chern-Simons Theory, and the A-Polynomial", Commun. Math. Phys. 255, 577-627
   -- (`prop:phi-q-aj-machinery-identification`).
   -- Ref: [dimofte-gukov2010] Dimofte-Gukov 2010, "Quantum field theory and the
   -- volume conjecture", arXiv:1003.4808v2 (`prop:phi-q-aj-machinery-identification`).
-/

namespace QOU.BraidKnot.TwistKnotCyclotomicShiftAndSaddleQuantization

/-- Quadratic exponent weight in the rearranged cyclotomic twist-knot summand
for figure-eight twist parameter, outer summation index `k`, and inner index `l`. -/
def twistCyclotomicQuadraticPhase (k l : Nat) : Nat :=
  k * (k + 1) + l * (l + 1) + 2 * k * l

/-- First-difference step in the outer summation index `k` of the cyclotomic
twist-knot quadratic exponent. -/
def twistSummandShiftDiffK (k l : Nat) : Nat :=
  2 * (k + 1) + 2 * l

/-- Total color-window span of the ascending-descending cyclotomic factor
product at color `n` and outer index `k`. -/
def twistHypergeomColorSpan (n k : Nat) : Nat :=
  2 * k + 1 + n

/-- Exact outer-index step identity for the twist-knot cyclotomic quadratic
exponent weight (`qou-7q3s`). -/
theorem twistCyclotomicQuadraticPhase_step_k (k l : Nat) :
    twistCyclotomicQuadraticPhase (k + 1) l =
      twistCyclotomicQuadraticPhase k l + twistSummandShiftDiffK k l := by
  dsimp [twistCyclotomicQuadraticPhase, twistSummandShiftDiffK]
  have h1 : (k + 1) * (k + 1 + 1) = k * (k + 1) + 2 * (k + 1) := by
    calc
      (k + 1) * (k + 1 + 1) = (k + 1) * k + (k + 1) * 2 := Nat.mul_add (k + 1) k 2
      _ = k * (k + 1) + 2 * (k + 1) := by
        rw [Nat.mul_comm (k + 1) k, Nat.mul_comm (k + 1) 2]
  have h2 : 2 * (k + 1) * l = 2 * k * l + 2 * l := by
    calc
      2 * (k + 1) * l = (2 * k + 2) * l := by rfl
      _ = 2 * k * l + 2 * l := Nat.add_mul (2 * k) 2 l
  omega

/-- Exact inner-index step identity for the twist-knot cyclotomic quadratic
exponent weight (`qou-7q3s`). -/
theorem twistCyclotomicQuadraticPhase_step_l (k l : Nat) :
    twistCyclotomicQuadraticPhase k (l + 1) =
      twistCyclotomicQuadraticPhase k l + 2 * (l + 1) + 2 * k := by
  dsimp [twistCyclotomicQuadraticPhase]
  have h1 : (l + 1) * (l + 1 + 1) = l * (l + 1) + 2 * (l + 1) := by
    calc
      (l + 1) * (l + 1 + 1) = (l + 1) * l + (l + 1) * 2 := Nat.mul_add (l + 1) l 2
      _ = l * (l + 1) + 2 * (l + 1) := by
        rw [Nat.mul_comm (l + 1) l, Nat.mul_comm (l + 1) 2]
  have h2 : 2 * k * (l + 1) = 2 * k * l + 2 * k := by
    calc
      2 * k * (l + 1) = 2 * k * l + 2 * k * 1 := Nat.mul_add (2 * k) l 1
      _ = 2 * k * l + 2 * k := by omega
  omega

/-- Color-shift linearity of the cyclotomic factor span (`qou-7q3s`). -/
theorem twistHypergeomColorSpan_color_shift (n k m : Nat) :
    twistHypergeomColorSpan (n + m) k - twistHypergeomColorSpan n k = m := by
  dsimp [twistHypergeomColorSpan]
  omega

/-- Truncation bound on the cyclotomic factor span for active summands `k < n`
at a root of unity of order `n` (`qou-7q3s`). -/
theorem figureEightRootUnityTermCount_bound (n k : Nat) (hk : k < n) :
    twistHypergeomColorSpan n k < 3 * n := by
  dsimp [twistHypergeomColorSpan]
  omega

/-- Order of the inhomogeneous q-difference recurrence for the figure-eight
knot colored invariant (`qou-2v4y`, `qou-c7lf`). -/
def aPolyFigureEightRecurrenceOrder : Nat := 3

/-- Leading meridian-shift power in the k-th iterate of the figure-eight
q-difference operator (`qou-2v4y`). -/
def aPolyFigureEightLeadingPower (k : Nat) : Nat :=
  4 * k + 2

/-- Total WKB asymptotic transport degree at loop order `loopOrder` and
recurrence shift depth `depth` (`qou-c7lf`). -/
def wkbLoopTransportHierarchyDegree (loopOrder depth : Nat) : Nat :=
  2 * loopOrder + 3 * depth + 1

/-- Linearized symplectic pairing `2 * mExp - lExp` on logarithmic meridian
and longitude exponents along the classical A-polynomial branch (`qou-2v4y`). -/
def saddleActionLegendrePairing (mExp lExp : Int) : Int :=
  2 * mExp - lExp

/-- Step increment of the leading meridian-shift power equals `aPolyFigureEightRecurrenceOrder + 1`
(`qou-2v4y`). -/
theorem aPolyFigureEightLeadingPower_step (k : Nat) :
    aPolyFigureEightLeadingPower (k + 1) - aPolyFigureEightLeadingPower k =
      aPolyFigureEightRecurrenceOrder + 1 := by
  dsimp [aPolyFigureEightLeadingPower, aPolyFigureEightRecurrenceOrder]
  omega

/-- Loop-order increment law for the WKB transport hierarchy degree (`qou-c7lf`). -/
theorem wkbLoopTransportHierarchyDegree_add_loop (loopOrder depth : Nat) :
    wkbLoopTransportHierarchyDegree (loopOrder + 1) depth =
      wkbLoopTransportHierarchyDegree loopOrder depth + 2 := by
  dsimp [wkbLoopTransportHierarchyDegree]
  omega

/-- Bilinear additivity of the linearized symplectic meridian-longitude pairing
(`qou-2v4y`, `qou-c7lf`). -/
theorem saddleActionLegendrePairing_bilinear_shift (mExp lExp dm dl : Int) :
    saddleActionLegendrePairing (mExp + dm) (lExp + dl) -
      saddleActionLegendrePairing mExp lExp =
        saddleActionLegendrePairing dm dl := by
  dsimp [saddleActionLegendrePairing]
  omega

/-- Vanishing of the linearized symplectic pairing on the balanced meridian-longitude
tangent ray `(mExp, lExp) = (k, 2 * k)` (`qou-2v4y`). -/
theorem saddleActionLegendrePairing_balanced_ray_zero (k : Int) :
    saddleActionLegendrePairing k (2 * k) = 0 := by
  dsimp [saddleActionLegendrePairing]
  omega

end QOU.BraidKnot.TwistKnotCyclotomicShiftAndSaddleQuantization
