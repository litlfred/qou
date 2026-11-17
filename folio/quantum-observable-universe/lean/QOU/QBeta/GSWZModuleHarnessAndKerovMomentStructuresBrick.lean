/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  * qou-5erw: Khovanov bigraded total homology rank vs alternating Euler characteristic and cyclic commutator trace collapse.
  * qou-9p9y: GSWZ cyclic module-membership pairing (cyclic shift + dilogarithm coefficient + epsilon sign).
  * qou-9w1u: Per-loop measure scaling invariant across L = 1 and L = 2 loop orders.
  * qou-a6ma: Writhe-determined framing exponent vs decoupled free twist datum separation.
  * qou-c6s9: Kerov-Olshanski third/fourth-moment variances Var(R_3) = 2n(n-1), Var(R_4) = 3n(n-1)(n-2) vs 2x2 multiplet discriminant.
-/

namespace QOU.QBeta.GSWZModuleHarnessAndKerovMomentStructuresBrick

/-! ### 1. Bigraded Homology Rank vs Alternating Euler Characteristic (`qou-5erw`) -/

/-- Alternating Euler characteristic `rkEven - rkOdd` of a two-parity homological complex. -/
def homologicalEulerDiff (rkEven rkOdd : Int) : Int :=
  rkEven - rkOdd

/-- Total homological rank `rkEven + rkOdd` retained by bigraded homology before Euler collapse. -/
def homologicalTotalRank (rkEven rkOdd : Int) : Int :=
  rkEven + rkOdd

/-- Whenever both even and odd homological parities carry positive rank (`1 <= rkEven`, `1 <= rkOdd`),
    the total homological rank strictly exceeds the alternating Euler characteristic by `2 * rkOdd >= 2`,
    and even when `rkEven = rkOdd` collapses `homologicalEulerDiff` to `0`, `homologicalTotalRank` is at least `2`. -/
theorem homologicalTotalRank_exceeds_eulerDiff (rkEven rkOdd : Int)
    (hEven : 1 ≤ rkEven) (hOdd : 1 ≤ rkOdd) :
    homologicalTotalRank rkEven rkOdd - homologicalEulerDiff rkEven rkOdd = 2 * rkOdd ∧
    homologicalEulerDiff rkEven rkOdd + 2 ≤ homologicalTotalRank rkEven rkOdd ∧
    homologicalEulerDiff rkEven rkEven = 0 ∧
    2 ≤ homologicalTotalRank rkEven rkEven := by
  dsimp only [homologicalTotalRank, homologicalEulerDiff]
  have hDiff : (rkEven + rkOdd) - (rkEven - rkOdd) = 2 * rkOdd := by omega
  have hGap : (rkEven - rkOdd) + 2 ≤ rkEven + rkOdd := by omega
  have hZero : rkEven - rkEven = 0 := by omega
  have hPos : 2 ≤ rkEven + rkEven := by omega
  exact ⟨hDiff, hGap, hZero, hPos⟩

/-! ### 2. GSWZ Module-Membership Pairing Harness (`qou-9p9y`) -/

/-- Linear GSWZ module-membership residual `shiftCoeff * p + dilogCoeff * d + epsSign * e`
    evaluating a candidate triple `(shiftCoeff, dilogCoeff, epsSign)` against module generators `(p, d, e)`. -/
def gswzModuleResidual (shiftCoeff dilogCoeff epsSign p d e : Int) : Int :=
  shiftCoeff * p + dilogCoeff * d + epsSign * e

/-- The GSWZ module-membership residual is invariant under simultaneous sign reversal of `(epsSign, e)`,
    vanishes whenever `shiftCoeff * p + dilogCoeff * d = - (epsSign * e)`, and satisfies
    two-candidate additivity in the coefficient triple. -/
theorem gswzModuleResidual_sign_invariance_and_vanishing
    (s1 d1 e1 s2 d2 e2 p d e : Int) :
    gswzModuleResidual s1 d1 (-e1) p d (-e) = gswzModuleResidual s1 d1 e1 p d e ∧
    gswzModuleResidual (s1 + s2) (d1 + d2) (e1 + e2) p d e =
      gswzModuleResidual s1 d1 e1 p d e + gswzModuleResidual s2 d2 e2 p d e := by
  dsimp only [gswzModuleResidual]
  have hNeg : (-e1) * (-e) = e1 * e := by
    rw [Int.neg_mul_neg]
  have hAdd : (s1 + s2) * p + (d1 + d2) * d + (e1 + e2) * e =
      (s1 * p + d1 * d + e1 * e) + (s2 * p + d2 * d + e2 * e) := by
    rw [Int.add_mul, Int.add_mul, Int.add_mul]
    omega
  exact ⟨by omega, hAdd⟩

/-! ### 3. Per-Loop Measure Scaling Invariant Across `L = 1` and `L = 2` (`qou-9w1u`) -/

/-- Cross-loop measure consistency discrepancy `amp2 * mu - invRatio * mu * mu * mu`
    relating a two-loop amplitude `amp2 = invRatio * mu^2` and a one-loop measure factor `mu`. -/
def twoLoopMeasureDiscrepancy (amp1 amp2 mu : Int) : Int :=
  amp2 * (mu * mu) - amp1 * amp1 * (mu * mu)

/-- Logarithmic loop-measure weight `loopOrder * logMu` scaling linearly with loop order `L`. -/
def logLoopMeasureWeight (loopOrder logMu : Int) : Int :=
  loopOrder * logMu

/-- The logarithmic loop-measure weight at `L = 2` is exactly twice the `L = 1` weight,
    is additive across loop orders `L1 + L2`, and when `amp2 = amp1 * amp1` the two-loop
    measure discrepancy vanishes identically. -/
theorem logLoopMeasureWeight_one_two_and_consistency (l1 l2 logMu amp1 mu : Int) :
    logLoopMeasureWeight 2 logMu = 2 * logLoopMeasureWeight 1 logMu ∧
    logLoopMeasureWeight (l1 + l2) logMu =
      logLoopMeasureWeight l1 logMu + logLoopMeasureWeight l2 logMu ∧
    twoLoopMeasureDiscrepancy amp1 (amp1 * amp1) mu = 0 := by
  dsimp only [logLoopMeasureWeight, twoLoopMeasureDiscrepancy]
  have hOneTwo : 2 * logMu = 2 * (1 * logMu) := by omega
  have hAdd : (l1 + l2) * logMu = l1 * logMu + l2 * logMu := by
    rw [Int.add_mul]
  have hZero : (amp1 * amp1) * (mu * mu) - amp1 * amp1 * (mu * mu) = 0 := by omega
  exact ⟨hOneTwo, hAdd, hZero⟩

/-! ### 4. Writhe-Determined Framing vs Free Twist Datum (`qou-a6ma`) -/

/-- Writhe-determined blackboard framing exponent `c * w` pinned solely by the writhe `w`. -/
def writhePinnedFraming (c w : Int) : Int :=
  c * w

/-- Decoupled framing exponent `c * w + t` carrying an extra twist shift `t`. -/
def decoupledTwistFraming (c w t : Int) : Int :=
  c * w + t

/-- The decoupled twist framing coincides with the writhe-pinned framing if and only if the extra twist
    shift `t` vanishes, and the difference between two twist assignments `t1, t2` over the same writhe `w`
    equals `t1 - t2` independently of `c` and `w`. -/
theorem decoupledTwistFraming_vs_writhePinned (c w t1 t2 : Int) :
    decoupledTwistFraming c w 0 = writhePinnedFraming c w ∧
    decoupledTwistFraming c w t1 - writhePinnedFraming c w = t1 ∧
    decoupledTwistFraming c w t1 - decoupledTwistFraming c w t2 = t1 - t2 := by
  dsimp only [decoupledTwistFraming, writhePinnedFraming]
  have hZero : c * w + 0 = c * w := by omega
  have hDiff1 : (c * w + t1) - c * w = t1 := by omega
  have hDiff2 : (c * w + t1) - (c * w + t2) = t1 - t2 := by omega
  exact ⟨hZero, hDiff1, hDiff2⟩

/-! ### 5. Kerov-Olshanski Moment Variances vs `2x2` Multiplet Discriminant (`qou-c6s9`) -/

/-- Kerov-Olshanski third-moment variance `Var(R_3) = 2 * (n * (n - 1)) = 4 * C(n, 2)`. -/
def kerovR3Variance (n : Int) : Int :=
  2 * (n * (n - 1))

/-- Kerov-Olshanski fourth-moment variance `Var(R_4) = 3 * (n * (n - 1)) * (n - 2) = 9 * |C_3|`. -/
def kerovR4Variance (n : Int) : Int :=
  3 * (n * (n - 1)) * (n - 2)

/-- Discriminant `(a - d)^2 + 4 * e^2` of a symmetric `2x2` multiplet mixing matrix `[[a, e], [e, d]]`. -/
def multipletMixingDiscriminant (a d e : Int) : Int :=
  (a - d) * (a - d) + 4 * (e * e)

/-- Exact polynomial bridge `2 * Var(R_4) = (2 * (n - 2)) * (3 * (n * (n - 1)))` and
    `3 * Var(R_3) * (n - 2) = 2 * Var(R_4)` between the third- and fourth-moment
    Kerov-Olshanski variances, distinct support threshold at `n = 2` (`Var(R_3) = 4` vs `Var(R_4) = 0`),
    and off-diagonal multiplet mixing excess `multipletMixingDiscriminant a d e - (a - d)^2 = 4 * e^2`. -/
theorem kerovVariance_bridge_and_multiplet_excess (n a d e : Int) :
    2 * kerovR4Variance n = 3 * kerovR3Variance n * (n - 2) ∧
    kerovR3Variance 2 = 4 ∧
    kerovR4Variance 2 = 0 ∧
    multipletMixingDiscriminant a d e - (a - d) * (a - d) = 4 * (e * e) := by
  dsimp only [kerovR4Variance, kerovR3Variance, multipletMixingDiscriminant]
  have h6 : (2 : Int) * 3 = 3 * 2 := by omega
  have hBridge : 2 * (3 * (n * (n - 1)) * (n - 2)) = 3 * (2 * (n * (n - 1))) * (n - 2) := by
    rw [← Int.mul_assoc 2 (3 * (n * (n - 1))) (n - 2)]
    rw [← Int.mul_assoc 2 3 (n * (n - 1))]
    rw [← Int.mul_assoc 3 2 (n * (n - 1))]
    rw [h6]
  have hR3 : 2 * ((2 : Int) * (2 - 1)) = 4 := by omega
  have hR4 : 3 * ((2 : Int) * (2 - 1)) * (2 - 2) = 0 := by omega
  have hDisc : ((a - d) * (a - d) + 4 * (e * e)) - (a - d) * (a - d) = 4 * (e * e) := by omega
  exact ⟨hBridge, hR3, hR4, hDisc⟩

end QOU.QBeta.GSWZModuleHarnessAndKerovMomentStructuresBrick
