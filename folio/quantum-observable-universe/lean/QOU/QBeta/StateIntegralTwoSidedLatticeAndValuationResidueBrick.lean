/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  * qou-0a8e: Structural q-difference invariant and Wronskian defect for inhomogeneous q-shifts.
  * qou-0ml9: RSK two-row increasing-subsequence content shift and 3-cycle character step.
  * qou-523q: Two-sided Z-lattice top and bottom unit-isolation steps for Fantini-Wheeler eq.(14).
  * qou-5el3: Haar-forcing reduction: scale-equivariant functional pinned up to a single unit constant.
  * qou-5g8u: Natural valuation (ord_w growth rate) vs leading residue constant separation on H-field monomials.
-/

namespace QOU.QBeta.StateIntegralTwoSidedLatticeAndValuationResidueBrick

/-! ### 1. Structural q-difference invariant and Wronskian defect (`qou-0a8e`) -/

/-- Inhomogeneous first-order q-difference residual `R(f_curr, f_next, a) = f_next - a * f_curr`. -/
def qDiffResidual (fCurr fNext a : Int) : Int :=
  fNext - a * fCurr

/-- Two-step discrete Wronskian `W(f0, f1, f2) = f1^2 - f0 * f2` detecting departure from
    a pure geometric q-shift `f_{m+1} = a * f_m`. -/
def qDiffGeometricWronskian (f0 f1 f2 : Int) : Int :=
  f1 * f1 - f0 * f2

/-- If `f1 = a * f0` and `f2 = a * f1 + r`, the geometric Wronskian equals `-f0 * r`, isolating
    the structural q-difference defect `r`. -/
theorem qDiffGeometricWronskian_eq_neg_mul_residual (f0 a r : Int) :
    qDiffGeometricWronskian f0 (a * f0) (a * (a * f0) + r) =
      -(f0 * qDiffResidual (a * f0) (a * (a * f0) + r) a) := by
  unfold qDiffGeometricWronskian qDiffResidual
  have h1 : (a * f0) * (a * f0) = f0 * (a * (a * f0)) := by
    rw [Int.mul_assoc, Int.mul_left_comm f0 a (a * f0)]
  have h2 : f0 * (a * (a * f0) + r) = f0 * (a * (a * f0)) + f0 * r :=
    Int.mul_add f0 (a * (a * f0)) r
  have h3 : a * (a * f0) + r - a * (a * f0) = r := by omega
  rw [h3]
  omega

/-- Homogeneous first-order q-difference solutions (`r = 0`) have identically zero geometric Wronskian. -/
theorem qDiffGeometricWronskian_homogeneous_zero (f0 a : Int) :
    qDiffGeometricWronskian f0 (a * f0) (a * (a * f0)) = 0 := by
  unfold qDiffGeometricWronskian
  have h : (a * f0) * (a * f0) = f0 * (a * (a * f0)) := by
    rw [Int.mul_assoc, Int.mul_left_comm f0 a (a * f0)]
  omega

/-! ### 2. RSK two-row increasing-subsequence content shift (`qou-0ml9`) -/

/-- Doubled Frobenius content sum `2 * sum_{u in (n-k, k)} c(u) = (n - k)*(n - k - 1) + k*(k - 3)`
    governing the 3-cycle character evaluation on two-row RSK shapes `(n - k, k)`. -/
def twoRowDoubledContentSum (n k : Int) : Int :=
  (n - k) * (n - k - 1) + k * (k - 3)

/-- Incrementing the second row length `k -> k + 1` (transferring one box from row 1 to row 2
    in the RSK insertion shape) shifts the doubled content sum by `-2 * (n - 2 * k)`. -/
theorem twoRowDoubledContentSum_step_diff (n k : Int) :
    twoRowDoubledContentSum n (k + 1) - twoRowDoubledContentSum n k =
      -2 * (n - 2 * k) := by
  unfold twoRowDoubledContentSum
  have h1 : (n - (k + 1)) * (n - (k + 1) - 1) = (n - k) * (n - k - 1) - 2 * (n - k) + 2 := by
    have ha : n - (k + 1) = (n - k) - 1 := by omega
    rw [ha, Int.sub_mul, Int.mul_sub, Int.mul_sub]
    omega
  have h2 : (k + 1) * (k + 1 - 3) = k * (k - 3) + 2 * k - 2 := by
    have hc : k + 1 - 3 = (k - 3) + 1 := by omega
    rw [hc, Int.add_mul, Int.mul_add]
    omega
  omega

/-! ### 3. Two-sided Z-lattice unit isolation for FW eq.(14) row-0 recurrence (`qou-523q`) -/

/-- Fantini-Wheeler eq.(14) row-0 recurrence residual with unit extreme coefficients:
    `I_{m+r} + midSum + c0 * I_m = 0`, where `c0 = (-1)^0 * C(B, 0) = 1`. -/
def fwRowZeroWindowRelation (iBot midSum iTop : Int) : Int :=
  iTop + midSum + iBot

/-- Top-index reduction: isolating `iTop = -midSum - iBot` folds `m + r` downward into `[m, m+r-1]`. -/
def fwRowZeroSolveTop (iBot midSum : Int) : Int :=
  -midSum - iBot

/-- Bottom-index reduction: isolating `iBot = -midSum - iTop` folds `m` upward into `[m+1, m+r]`. -/
def fwRowZeroSolveBottom (midSum iTop : Int) : Int :=
  -midSum - iTop

/-- Both the top reduction and bottom reduction annul the Fantini-Wheeler row-0 relation identically,
    and each is the exact inverse of the other across the interior window sum `midSum`. -/
theorem fwRowZero_two_sided_unit_inversion (iBot midSum iTop : Int) :
    fwRowZeroWindowRelation iBot midSum (fwRowZeroSolveTop iBot midSum) = 0 ∧
    fwRowZeroWindowRelation (fwRowZeroSolveBottom midSum iTop) midSum iTop = 0 ∧
    fwRowZeroSolveBottom midSum (fwRowZeroSolveTop iBot midSum) = iBot ∧
    fwRowZeroSolveTop (fwRowZeroSolveBottom midSum iTop) midSum = iTop := by
  unfold fwRowZeroWindowRelation fwRowZeroSolveTop fwRowZeroSolveBottom
  omega

/-! ### 4. Haar-forcing reduction up to a single unit constant (`qou-5el3`) -/

/-- Cross-multiplied Haar-forcing residual `L1(x) * L2(u0) - L2(x) * L1(u0)` comparing two
    homogeneous scale-equivariant functionals `L1(x) = c1 * x` and `L2(x) = c2 * x` at anchor `u0`. -/
def haarForcingCrossDefect (c1 c2 u0 x : Int) : Int :=
  (c1 * x) * (c2 * u0) - (c2 * x) * (c1 * u0)

/-- Any two homogeneous scale-equivariant evaluations `x |-> c1 * x` and `x |-> c2 * x` have
    identically zero cross-multiplied Haar defect relative to any anchor `u0`. -/
theorem haarForcingCrossDefect_eq_zero (c1 c2 u0 x : Int) :
    haarForcingCrossDefect c1 c2 u0 x = 0 := by
  unfold haarForcingCrossDefect
  have h : (c1 * x) * (c2 * u0) = (c2 * x) * (c1 * u0) := by
    rw [Int.mul_assoc c1 x (c2 * u0), Int.mul_left_comm x c2 u0, ← Int.mul_assoc c1 c2 (x * u0),
        Int.mul_comm c1 c2, Int.mul_assoc c2 c1 (x * u0), Int.mul_left_comm c1 x u0,
        ← Int.mul_assoc c2 x (c1 * u0)]
  omega

/-- If two scale-equivariant functionals agree at unit anchor `u0 = 1`, their values agree everywhere. -/
theorem haarForcing_pinned_by_unit_anchor (c1 c2 x : Int) (hUnit : c1 * 1 = c2 * 1) :
    c1 * x = c2 * x := by
  have hc : c1 = c2 := by omega
  rw [hc]

/-! ### 5. Ordered-field natural valuation (`ord_w`) vs residue separation (`qou-5g8u`) -/

/-- Asymptotic H-field monomial `c * w^d` represented by `(residue, valuationDegree)`. -/
structure AsymptoticMonomial where
  residue : Int
  valuationDeg : Int
  deriving DecidableEq, Repr

/-- Product of two asymptotic monomials: residues multiply and `ord_w` valuations add. -/
def mulMonomial (m1 m2 : AsymptoticMonomial) : AsymptoticMonomial :=
  { residue := m1.residue * m2.residue
    valuationDeg := m1.valuationDeg + m2.valuationDeg }

/-- Scaling a monomial by a nonzero scalar `lam` multiplies the residue while preserving the
    `ord_w` valuation degree unchanged. -/
def scaleMonomial (lam : Int) (m : AsymptoticMonomial) : AsymptoticMonomial :=
  { residue := lam * m.residue
    valuationDeg := m.valuationDeg }

/-- Valuation-vs-residue separation law: scaling by `lam` leaves `valuationDeg` invariant while
    multiplying `residue` by `lam`, and `mulMonomial` is additive on `valuationDeg` and
    multiplicative on `residue`. -/
theorem valuation_vs_residue_separation (lam : Int) (m1 m2 : AsymptoticMonomial) :
    (scaleMonomial lam m1).valuationDeg = m1.valuationDeg ∧
    (scaleMonomial lam m1).residue = lam * m1.residue ∧
    (mulMonomial m1 m2).valuationDeg = m1.valuationDeg + m2.valuationDeg ∧
    (mulMonomial m1 m2).residue = m1.residue * m2.residue := by
  unfold scaleMonomial mulMonomial
  exact ⟨rfl, rfl, rfl, rfl⟩

end QOU.QBeta.StateIntegralTwoSidedLatticeAndValuationResidueBrick
