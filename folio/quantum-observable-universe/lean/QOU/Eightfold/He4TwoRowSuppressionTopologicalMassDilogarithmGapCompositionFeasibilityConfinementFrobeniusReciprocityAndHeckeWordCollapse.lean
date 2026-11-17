/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Round 80 Formalization:
  - qou-8mmq: He4 two-row signed sum 29,000x suppression & near-cancellation bound
  - qou-8p6w: Topological mass dilogarithm Euler-reflection gap
  - qou-8r6b: Composition feasibility program on the affine interface letter (1-e)σ + eσ⁻¹
  - qou-9gpo: Confinement Frobenius reciprocity intertwining duality
  - qou-9ohz: Hecke generator word collapse to α·σ + β
-/

namespace QOU.Eightfold.He4TwoRowSuppressionTopologicalMassDilogarithmGapCompositionFeasibilityConfinementFrobeniusReciprocityAndHeckeWordCollapse

/-! ## 1. Bean `qou-8mmq`: He4 Two-Row Signed Sum Suppression -/

/-- L1 norm of a two-row Young stratum split into positive and negative channel weights. -/
def twoRowL1Mass (wPos wNeg : Int) : Int :=
  wPos + wNeg

/-- Signed sum of a two-row Young stratum. -/
def twoRowSignedSum (wPos wNeg : Int) : Int :=
  wPos - wNeg

/-- Adding the L1 mass and signed sum isolates twice the positive channel weight. -/
theorem twoRowL1_add_signed_eq_two_pos (wPos wNeg : Int) :
    twoRowL1Mass wPos wNeg + twoRowSignedSum wPos wNeg = 2 * wPos := by
  unfold twoRowL1Mass twoRowSignedSum
  omega

/-- Subtracting the signed sum from the L1 mass isolates twice the negative channel weight. -/
theorem twoRowL1_sub_signed_eq_two_neg (wPos wNeg : Int) :
    twoRowL1Mass wPos wNeg - twoRowSignedSum wPos wNeg = 2 * wNeg := by
  unfold twoRowL1Mass twoRowSignedSum
  omega

/-- Near-cancellation suppression bound: when `wPos - wNeg ≤ eps` and `2 * wNeg ≥ (M - 1) * eps`,
    the L1 mass dominates `M` times the signed sum. -/
theorem he4Singlet_nearCancellation_bound (wPos wNeg eps M : Int)
    (hDiffBound : wPos - wNeg ≤ eps)
    (hBulk : (M - 1) * eps ≤ 2 * wNeg)
    (hMPos : 1 ≤ M) :
    M * twoRowSignedSum wPos wNeg ≤ twoRowL1Mass wPos wNeg := by
  unfold twoRowSignedSum twoRowL1Mass
  have h1 : (M - 1) * (wPos - wNeg) ≤ (M - 1) * eps :=
    Int.mul_le_mul_of_nonneg_left hDiffBound (by omega)
  have h2 : M * (wPos - wNeg) - (wPos - wNeg) = (M - 1) * (wPos - wNeg) := by
    calc M * (wPos - wNeg) - (wPos - wNeg)
      _ = M * (wPos - wNeg) - 1 * (wPos - wNeg) := by omega
      _ = (M - 1) * (wPos - wNeg) := (Int.sub_mul M 1 (wPos - wNeg)).symm
  omega

/-- Scaled integer witness for the `⁴He` two-row stratum (`l1 = 4.3196 MeV`, `|signed| = 0.000149 MeV`),
    exhibiting > 28,990x suppression while remaining strictly non-zero (not an exact identity). -/
theorem he4TwoRow_29000x_suppression_witness :
    0 < twoRowSignedSum 21598745 21597255 ∧
    28990 * twoRowSignedSum 21598745 21597255 < twoRowL1Mass 21598745 21597255 := by
  unfold twoRowSignedSum twoRowL1Mass
  omega

/-! ## 2. Bean `qou-8p6w`: Topological Mass Dilogarithm Gap -/

/-- Discretized Euler reflection defect for the topological mass dilogarithm:
    `B2 - (Lx + L1mx + logProd)` where `B2` represents `π²/6` and `logProd` represents `ln(x)ln(1-x)`. -/
def topologicalMassDilogGap (Lx L1mx logProd B2 : Int) : Int :=
  B2 - (Lx + L1mx + logProd)

/-- The Euler reflection defect is symmetric under `x ↔ 1 - x`. -/
theorem topologicalMassDilogGap_symm (Lx L1mx logProd B2 : Int) :
    topologicalMassDilogGap Lx L1mx logProd B2 =
      topologicalMassDilogGap L1mx Lx logProd B2 := by
  unfold topologicalMassDilogGap
  omega

/-- Vanishing of the topological mass dilogarithm gap is equivalent to the Euler reflection identity. -/
theorem topologicalMassDilogGap_eq_zero_iff (Lx L1mx logProd B2 : Int) :
    topologicalMassDilogGap Lx L1mx logProd B2 = 0 ↔
      Lx + L1mx + logProd = B2 := by
  unfold topologicalMassDilogGap
  omega

/-- At the self-dual point `x = 1/2` (`Lx = L1mx = Lhalf`), the gap decomposition recovers `2*Lhalf + logProd`. -/
theorem topologicalMassDilogGap_selfDual_half (Lhalf logProd B2 : Int) :
    B2 - topologicalMassDilogGap Lhalf Lhalf logProd B2 = 2 * Lhalf + logProd := by
  unfold topologicalMassDilogGap
  omega

/-! ## 3. Bean `qou-8r6b`: Composition Feasibility Program on `(1 - e)σ + eσ⁻¹` -/

/-- Scaled affine interface braid letter `(s - e) * sigma + e * sigmaInv` for `e ∈ [0, s]`. -/
def interfaceBraidLetter (s e sigma sigmaInv : Int) : Int :=
  (s - e) * sigma + e * sigmaInv

/-- Deviation of the affine interface letter from the pure braid generator `s * sigma`. -/
def interfaceLetterDeviation (s e sigma sigmaInv : Int) : Int :=
  interfaceBraidLetter s e sigma sigmaInv - s * sigma

/-- At `e = 0`, the interface letter reduces to the pure forward generator `s * sigma`. -/
theorem interfaceBraidLetter_at_zero (s sigma sigmaInv : Int) :
    interfaceBraidLetter s 0 sigma sigmaInv = s * sigma := by
  unfold interfaceBraidLetter
  have h : s - 0 = s := by omega
  rw [h]
  omega

/-- At `e = s`, the interface letter reduces to the inverse generator `s * sigmaInv`. -/
theorem interfaceBraidLetter_at_unit (s sigma sigmaInv : Int) :
    interfaceBraidLetter s s sigma sigmaInv = s * sigmaInv := by
  unfold interfaceBraidLetter
  have h : s - s = 0 := by omega
  rw [h]
  omega

/-- The deviation from `s * sigma` is linear in the mixing parameter `e`. -/
theorem interfaceLetterDeviation_eq_mul_diff (s e sigma sigmaInv : Int) :
    interfaceLetterDeviation s e sigma sigmaInv = e * (sigmaInv - sigma) := by
  unfold interfaceLetterDeviation interfaceBraidLetter
  calc (s - e) * sigma + e * sigmaInv - s * sigma
    _ = s * sigma - e * sigma + e * sigmaInv - s * sigma := by
        rw [Int.sub_mul s e sigma]
    _ = e * sigmaInv - e * sigma := by omega
    _ = e * (sigmaInv - sigma) := (Int.mul_sub e sigmaInv sigma).symm

/-- For `0 ≤ e ≤ s` and `sigmaInv ≤ sigma`, the interface letter lies inside `[s * sigmaInv, s * sigma]`. -/
theorem interfaceBraidLetter_convex_bounds (s e sigma sigmaInv : Int)
    (heNonneg : 0 ≤ e) (heLeS : e ≤ s) (hOrd : sigmaInv ≤ sigma) :
    s * sigmaInv ≤ interfaceBraidLetter s e sigma sigmaInv ∧
      interfaceBraidLetter s e sigma sigmaInv ≤ s * sigma := by
  have hDev := interfaceLetterDeviation_eq_mul_diff s e sigma sigmaInv
  unfold interfaceLetterDeviation at hDev
  have hDiffNonpos : sigmaInv - sigma ≤ 0 := by omega
  have hUpperMul : e * (sigmaInv - sigma) ≤ 0 :=
    Int.mul_nonpos_of_nonneg_of_nonpos heNonneg hDiffNonpos
  have hLowerSub : (s - e) * (sigma - sigmaInv) ≥ 0 :=
    Int.mul_nonneg (by omega) (by omega)
  have hLowerId : interfaceBraidLetter s e sigma sigmaInv - s * sigmaInv =
      (s - e) * (sigma - sigmaInv) := by
    unfold interfaceBraidLetter
    calc (s - e) * sigma + e * sigmaInv - s * sigmaInv
      _ = (s - e) * sigma - (s - e) * sigmaInv := by
          have hs : s * sigmaInv - e * sigmaInv = (s - e) * sigmaInv :=
            (Int.sub_mul s e sigmaInv).symm
          omega
      _ = (s - e) * (sigma - sigmaInv) := (Int.mul_sub (s - e) sigma sigmaInv).symm
  omega

/-! ## 4. Bean `qou-9gpo`: Confinement Frobenius Reciprocity -/

/-- Induced character pairing `<Ind(w), v>_G` on a 2-channel (singlet/octet) branching block. -/
def frobeniusInducedPairing (w0 w1 m00 m01 m10 m11 v0 v1 : Int) : Int :=
  (w0 * m00 + w1 * m10) * v0 + (w0 * m01 + w1 * m11) * v1

/-- Restricted character pairing `<w, Res(v)>_H` on a 2-channel (singlet/octet) branching block. -/
def frobeniusRestrictedPairing (w0 w1 m00 m01 m10 m11 v0 v1 : Int) : Int :=
  w0 * (m00 * v0 + m01 * v1) + w1 * (m10 * v0 + m11 * v1)

/-- Exact Frobenius reciprocity adjoint identity `<Ind(w), v>_G = <w, Res(v)>_H`. -/
theorem confinement_frobenius_reciprocity_adjoint
    (w0 w1 m00 m01 m10 m11 v0 v1 : Int) :
    frobeniusInducedPairing w0 w1 m00 m01 m10 m11 v0 v1 =
      frobeniusRestrictedPairing w0 w1 m00 m01 m10 m11 v0 v1 := by
  unfold frobeniusInducedPairing frobeniusRestrictedPairing
  rw [Int.add_mul (w0 * m00) (w1 * m10) v0,
      Int.add_mul (w0 * m01) (w1 * m11) v1,
      Int.mul_add w0 (m00 * v0) (m01 * v1),
      Int.mul_add w1 (m10 * v0) (m11 * v1),
      Int.mul_assoc w0 m00 v0,
      Int.mul_assoc w1 m10 v0,
      Int.mul_assoc w0 m01 v1,
      Int.mul_assoc w1 m11 v1]
  omega

/-- Under color confinement (`m01 = m10 = m11 = 0`), the Frobenius pairing isolates the singlet channel `w0 * m00 * v0 > 0`. -/
theorem confinement_singlet_channel_isolation (w0 w1 m00 v0 v1 : Int)
    (hw0 : 0 < w0) (hm00 : 0 < m00) (hv0 : 0 < v0) :
    frobeniusInducedPairing w0 w1 m00 0 0 0 v0 v1 = w0 * m00 * v0 ∧
      0 < frobeniusInducedPairing w0 w1 m00 0 0 0 v0 v1 := by
  have hEq : frobeniusInducedPairing w0 w1 m00 0 0 0 v0 v1 = w0 * m00 * v0 := by
    unfold frobeniusInducedPairing
    simp [Int.mul_zero, Int.add_zero]
  have h1 : 0 < w0 * m00 := Int.mul_pos hw0 hm00
  have h2 : 0 < w0 * m00 * v0 := Int.mul_pos h1 hv0
  exact ⟨hEq, hEq.symm ▸ h2⟩

/-! ## 5. Bean `qou-9ohz`: Hecke Generator Word Collapse to `α·σ + β` -/

/-- Collapsed linear coefficient `α₁₂` of `(α₁·σ + β₁)(α₂·σ + β₂)` under `σ² = δ·σ + ι`. -/
def heckeCollapsedAlpha (delta a1 b1 a2 b2 : Int) : Int :=
  a1 * b2 + b1 * a2 + delta * (a1 * a2)

/-- Collapsed scalar coefficient `β₁₂` of `(α₁·σ + β₁)(α₂·σ + β₂)` under `σ² = δ·σ + ι`. -/
def heckeCollapsedBeta (iota a1 b1 a2 b2 : Int) : Int :=
  b1 * b2 + iota * (a1 * a2)

/-- Commutativity of the collapsed `σ`-coefficient for words in the same generator `σ`. -/
theorem heckeCollapsedAlpha_comm (delta a1 b1 a2 b2 : Int) :
    heckeCollapsedAlpha delta a1 b1 a2 b2 =
      heckeCollapsedAlpha delta a2 b2 a1 b1 := by
  unfold heckeCollapsedAlpha
  rw [Int.mul_comm a1 b2, Int.mul_comm b1 a2, Int.mul_comm a1 a2]
  omega

/-- Commutativity of the collapsed scalar coefficient for words in the same generator `σ`. -/
theorem heckeCollapsedBeta_comm (iota a1 b1 a2 b2 : Int) :
    heckeCollapsedBeta iota a1 b1 a2 b2 =
      heckeCollapsedBeta iota a2 b2 a1 b1 := by
  unfold heckeCollapsedBeta
  rw [Int.mul_comm b1 b2, Int.mul_comm a1 a2]

/-- Any scalar `sigma` satisfying the quadratic Hecke relation `sigma * sigma = delta * sigma + iota`
    evaluates the product of two affine generator words via `heckeCollapsedAlpha` and `heckeCollapsedBeta`. -/
theorem heckeWordCollapse_eval_eq (delta iota sigma a1 b1 a2 b2 : Int)
    (hHecke : sigma * sigma = delta * sigma + iota) :
    (a1 * sigma + b1) * (a2 * sigma + b2) =
      heckeCollapsedAlpha delta a1 b1 a2 b2 * sigma +
        heckeCollapsedBeta iota a1 b1 a2 b2 := by
  unfold heckeCollapsedAlpha heckeCollapsedBeta
  calc (a1 * sigma + b1) * (a2 * sigma + b2)
    _ = (a1 * sigma) * (a2 * sigma) + (a1 * sigma) * b2 + b1 * (a2 * sigma) + b1 * b2 := by
        rw [Int.add_mul (a1 * sigma) b1 (a2 * sigma + b2),
            Int.mul_add (a1 * sigma) (a2 * sigma) b2,
            Int.mul_add b1 (a2 * sigma) b2]
        omega
    _ = (a1 * a2) * (sigma * sigma) + (a1 * b2) * sigma + (b1 * a2) * sigma + b1 * b2 := by
        have hsq : (a1 * sigma) * (a2 * sigma) = (a1 * a2) * (sigma * sigma) := by
          rw [Int.mul_assoc a1 sigma (a2 * sigma),
              ← Int.mul_assoc sigma a2 sigma,
              Int.mul_comm sigma a2,
              Int.mul_assoc a2 sigma sigma,
              ← Int.mul_assoc a1 a2 (sigma * sigma)]
        have hb2 : (a1 * sigma) * b2 = (a1 * b2) * sigma := by
          rw [Int.mul_assoc a1 sigma b2, Int.mul_comm sigma b2, ← Int.mul_assoc a1 b2 sigma]
        have ha2 : b1 * (a2 * sigma) = (b1 * a2) * sigma := by
          rw [← Int.mul_assoc b1 a2 sigma]
        rw [hsq, hb2, ha2]
    _ = (a1 * a2) * (delta * sigma + iota) + (a1 * b2) * sigma + (b1 * a2) * sigma + b1 * b2 := by
        rw [hHecke]
    _ = (a1 * b2 + b1 * a2 + delta * (a1 * a2)) * sigma + (b1 * b2 + iota * (a1 * a2)) := by
        have hd : (a1 * a2) * (delta * sigma + iota) =
            (delta * (a1 * a2)) * sigma + iota * (a1 * a2) := by
          rw [Int.mul_add (a1 * a2) (delta * sigma) iota,
              ← Int.mul_assoc (a1 * a2) delta sigma,
              Int.mul_comm (a1 * a2) delta,
              Int.mul_comm (a1 * a2) iota]
        rw [hd,
            Int.add_mul (a1 * b2 + b1 * a2) (delta * (a1 * a2)) sigma,
            Int.add_mul (a1 * b2) (b1 * a2) sigma]
        omega

end QOU.Eightfold.He4TwoRowSuppressionTopologicalMassDilogarithmGapCompositionFeasibilityConfinementFrobeniusReciprocityAndHeckeWordCollapse
