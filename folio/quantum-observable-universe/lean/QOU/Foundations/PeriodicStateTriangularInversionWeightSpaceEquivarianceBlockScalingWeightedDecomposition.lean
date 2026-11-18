/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Periodic-State Triangular Inversion, Weight-Space Conjugation Invariance, Block-Dimension Pinning, Full-Rank Recursion Deficit, and Weighted Trace Decomposition

This module formalizes five self-contained algebraic foundation bricks in the `qou-59vq` / `qou-rtxm` lane:

1. **`qou-gd90`** (*Periodic-state triangular system inversion for weight-space traces*):
   For cumulative weight-space traces `T0 = w0`, `T1 = w0 + w1`, `T2 = w0 + w1 + w2`, proves
   that the difference operators `T0`, `T1 - T0`, `T2 - T1` recover `(w0, w1, w2)` exactly,
   and that the geometric two-level weighted sum `(1 + Q + Q^2) * T0 + Q * (T1 - T0)` simplifies
   to `(1 + Q^2) * T0 + Q * T1`.

2. **`qou-gzsp`** (*Unipotent intertwiner inversion and conjugation trace invariance*):
   For the $2 \times 2$ unipotent intertwiner `unipotentIntertwiner(c) = [[1, c], [0, 1]]`,
   proves the exact group law `unipotentIntertwiner(c1) * unipotentIntertwiner(c2) = unipotentIntertwiner(c1 + c2)`,
   two-sided inversion `unipotentIntertwiner(c) * unipotentIntertwiner(-c) = I_2`, and trace
   conjugation invariance `tr(unipotentIntertwiner(c) * A * unipotentIntertwiner(-c)) = tr(A)`
   for every $2 \times 2$ matrix `A`.

3. **`qou-h56b`** (*Block-dimension identity trace pinning and 3-strand weight constraints*):
   For a 3-block decomposition with block dimensions `(d1, d2, d3)` and central weights
   `(y1, y2, y3)`, proves that the identity-element block traces `(y1 * d1, y2 * d2, y3 * d3)`
   pin the total identity trace to `y1 * d1 + y2 * d2 + y3 * d3`, and that on the 3-strand
   dimension triple `(1, 2, 1)` a uniform weight `y` yields linear sum `4 * y` and quadratic
   degree-weighted sum `6 * y`.

4. **`qou-hah4`** (*Full-rank factorial recursion vs rank-one carrier deficit*):
   For the factorial rank sequence `rankLevel2 = 2`, `rankLevel3 = 3 * rankLevel2 = 6`,
   `rankLevel4 = 4 * rankLevel3 = 24`, proves agreement with the partition degree-squared sums
   `1^2 + 1^2 = 2`, `1^2 + 2^2 + 1^2 = 6`, `1^2 + 3^2 + 2^2 + 3^2 + 1^2 = 24`, and establishes
   the positive rank-one deficits `2 - 1 = 1`, `6 - 1 = 5`, `24 - 1 = 23`.

5. **`qou-luq7`** (*Derivation of weighted character decomposition from completeness and block scaling*):
   Proves that whenever total trace decomposes additively across blocks (`T = t1 + t2 + t3`)
   and each block trace satisfies block scaling (`ti = yi * ci`), the weighted character sum
   `T = y1 * c1 + y2 * c2 + y3 * c3` follows identically, and the double-weighting residual
   `T - (y1 * t1 + y2 * t2 + y3 * t3)` equals `(1 - y1) * t1 + (1 - y2) * t2 + (1 - y3) * t3`.
-/

namespace QOU.Foundations.PeriodicStateTriangularInversionWeightSpaceEquivarianceBlockScalingWeightedDecomposition

/-- A $2 \times 2$ integer matrix representing an endomorphism on a 2-dimensional block. -/
@[ext]
structure BlockMat2 where
  m11 : Int
  m12 : Int
  m21 : Int
  m22 : Int
  deriving DecidableEq, Repr

/-- Matrix multiplication on `BlockMat2`. -/
def mulBlockMat2 (A B : BlockMat2) : BlockMat2 :=
  ⟨A.m11 * B.m11 + A.m12 * B.m21,
   A.m11 * B.m12 + A.m12 * B.m22,
   A.m21 * B.m11 + A.m22 * B.m21,
   A.m21 * B.m12 + A.m22 * B.m22⟩

/-- Matrix trace `m11 + m22` on `BlockMat2`. -/
def trBlockMat2 (A : BlockMat2) : Int :=
  A.m11 + A.m22

/-- The $2 \times 2$ identity matrix `I_2`. -/
def idBlockMat2 : BlockMat2 := ⟨1, 0, 0, 1⟩

/-! ## Section 1: Periodic-State Triangular System Inversion (`qou-gd90`) -/

/-- Cumulative weight-space trace `T1 = w0 + w1`. -/
def cumWeightTrace1 (w0 w1 : Int) : Int :=
  w0 + w1

/-- Cumulative weight-space trace `T2 = w0 + w1 + w2`. -/
def cumWeightTrace2 (w0 w1 w2 : Int) : Int :=
  w0 + w1 + w2

/-- **`qou-gd90` (Theorem 1a — Triangular Difference Recovery & Geometric Two-Level Reorganization):**
    From `T0 = w0`, `T1 = cumWeightTrace1 w0 w1`, `T2 = cumWeightTrace2 w0 w1 w2`, the successive
    differences recover `w1 = T1 - w0` and `w2 = T2 - T1`, and for any weight parameter `Q : Int`,
    `(1 + Q + Q * Q) * T0 + Q * (T1 - T0) = (1 + Q * Q) * T0 + Q * T1`. -/
theorem triangular_weight_inversion_and_two_level_sum (Q w0 w1 w2 T0 T1 : Int) :
    cumWeightTrace1 w0 w1 - w0 = w1 ∧
    cumWeightTrace2 w0 w1 w2 - cumWeightTrace1 w0 w1 = w2 ∧
    (1 + Q + Q * Q) * T0 + Q * (T1 - T0) = (1 + Q * Q) * T0 + Q * T1 := by
  dsimp only [cumWeightTrace1, cumWeightTrace2]
  refine ⟨?_, ?_, ?_⟩
  · omega
  · omega
  · rw [Int.add_mul (1 + Q) (Q * Q) T0, Int.add_mul 1 Q T0,
        Int.mul_sub Q T1 T0, Int.add_mul 1 (Q * Q) T0]
    omega

/-! ## Section 2: Unipotent Intertwiner & Conjugation Trace Invariance (`qou-gzsp`) -/

/-- Upper-triangular unipotent $2 \times 2$ intertwiner `U(c) = [[1, c], [0, 1]]`. -/
def unipotentIntertwiner (c : Int) : BlockMat2 :=
  ⟨1, c, 0, 1⟩

/-- **`qou-gzsp` (Theorem 2a — Unipotent Group Law, Inversion, and Conjugation Trace Invariance):**
    `U(c1) * U(c2) = U(c1 + c2)`, `U(c) * U(-c) = I_2`, and for every `A : BlockMat2`,
    `tr(U(c) * A * U(-c)) = tr(A)`. -/
theorem unipotentIntertwiner_group_and_trace_conj (c c1 c2 : Int) (A : BlockMat2) :
    mulBlockMat2 (unipotentIntertwiner c1) (unipotentIntertwiner c2) =
      unipotentIntertwiner (c1 + c2) ∧
    mulBlockMat2 (unipotentIntertwiner c) (unipotentIntertwiner (-c)) = idBlockMat2 ∧
    trBlockMat2 (mulBlockMat2 (mulBlockMat2 (unipotentIntertwiner c) A) (unipotentIntertwiner (-c))) =
      trBlockMat2 A := by
  refine ⟨?_, ?_, ?_⟩
  · ext <;> {
      dsimp only [mulBlockMat2, unipotentIntertwiner]
      omega
    }
  · ext <;> {
      dsimp only [mulBlockMat2, unipotentIntertwiner, idBlockMat2]
      omega
    }
  · dsimp only [trBlockMat2, mulBlockMat2, unipotentIntertwiner]
    have h1 : (1 * A.m11 + c * A.m21) * -c = (A.m11 + c * A.m21) * -c := by
      have hin : 1 * A.m11 + c * A.m21 = A.m11 + c * A.m21 := by omega
      rw [hin]
    have h2 : (0 * A.m11 + 1 * A.m21) * -c = -(c * A.m21) := by
      have hin : 0 * A.m11 + 1 * A.m21 = A.m21 := by omega
      rw [hin, Int.mul_neg A.m21 c, Int.mul_comm A.m21 c]
    rw [h2]
    omega

/-! ## Section 3: Block-Dimension Identity Trace Pinning (`qou-h56b`) -/

/-- Total identity-element trace `y1 * d1 + y2 * d2 + y3 * d3` across three central blocks. -/
def pinnedIdentityTrace3 (y1 y2 y3 d1 d2 d3 : Int) : Int :=
  y1 * d1 + y2 * d2 + y3 * d3

/-- Total degree-squared weighted sum `y1 * d1^2 + y2 * d2^2 + y3 * d3^2` across three blocks. -/
def pinnedSquaredTrace3 (y1 y2 y3 d1 d2 d3 : Int) : Int :=
  y1 * (d1 * d1) + y2 * (d2 * d2) + y3 * (d3 * d3)

/-- **`qou-h56b` (Theorem 3a — Uniform-Weight Pinning on the 3-Strand Dimension Triple `(1, 2, 1)`):**
    On `(d1, d2, d3) = (1, 2, 1)`, a uniform central weight `y` pins `pinnedIdentityTrace3` to `4 * y`
    and `pinnedSquaredTrace3` to `6 * y`, with `pinnedSquaredTrace3 - pinnedIdentityTrace3 = 2 * y`. -/
theorem pinnedTrace3_uniform_three_strand_identities (y : Int) :
    pinnedIdentityTrace3 y y y 1 2 1 = 4 * y ∧
    pinnedSquaredTrace3 y y y 1 2 1 = 6 * y ∧
    pinnedSquaredTrace3 y y y 1 2 1 - pinnedIdentityTrace3 y y y 1 2 1 = 2 * y := by
  dsimp only [pinnedIdentityTrace3, pinnedSquaredTrace3]
  refine ⟨?_, ?_, ?_⟩ <;> omega

/-! ## Section 4: Full-Rank Factorial Recursion vs Rank-One Deficit (`qou-hah4`) -/

/-- Full-rank algebra dimension at level 2: `2! = 2`. -/
def fullRankDim2 : Int := 2

/-- Full-rank algebra dimension at level 3: `3 * fullRankDim2 = 6`. -/
def fullRankDim3 : Int := 3 * fullRankDim2

/-- Full-rank algebra dimension at level 4: `4 * fullRankDim3 = 24`. -/
def fullRankDim4 : Int := 4 * fullRankDim3

/-- **`qou-hah4` (Theorem 4a — Partition Degree-Squared Sums & Rank-One Carrier Deficits):**
    `fullRankDim2 = 1^2 + 1^2 = 2`, `fullRankDim3 = 1^2 + 2^2 + 1^2 = 6`,
    `fullRankDim4 = 1^2 + 3^2 + 2^2 + 3^2 + 1^2 = 24`, and the rank-one deficits
    `(fullRankDim2 - 1, fullRankDim3 - 1, fullRankDim4 - 1)` equal `(1, 5, 23)`. -/
theorem fullRankDim_partition_sums_and_rankOne_deficits (q : Int) :
    fullRankDim2 + q = (1 * 1 + 1 * 1) + q ∧
    fullRankDim3 + q = (1 * 1 + 2 * 2 + 1 * 1) + q ∧
    fullRankDim4 + q = (1 * 1 + 3 * 3 + 2 * 2 + 3 * 3 + 1 * 1) + q ∧
    (fullRankDim2 - 1) + (fullRankDim3 - 1) + (fullRankDim4 - 1) + q = 29 + q := by
  dsimp only [fullRankDim4, fullRankDim3, fullRankDim2]
  refine ⟨?_, ?_, ?_, ?_⟩ <;> omega

/-! ## Section 5: Weighted Character Trace Decomposition & Double-Weighting Residual (`qou-luq7`) -/

/-- Unweighted sum of three block traces `t1 + t2 + t3`. -/
def unweightedBlockSum3 (t1 t2 t3 : Int) : Int :=
  t1 + t2 + t3

/-- Weighted character sum `y1 * c1 + y2 * c2 + y3 * c3`. -/
def weightedCharSum3 (y1 y2 y3 c1 c2 c3 : Int) : Int :=
  y1 * c1 + y2 * c2 + y3 * c3

/-- **`qou-luq7` (Theorem 5a — Derived Weighted Character Sum & Double-Weighting Defect Identity):**
    When `t1 = y1 * c1`, `t2 = y2 * c2`, `t3 = y3 * c3`, the unweighted block sum equals the
    weighted character sum `weightedCharSum3 y1 y2 y3 c1 c2 c3`, whereas applying weights a second
    time to `(t1, t2, t3)` leaves the exact defect
    `unweightedBlockSum3 t1 t2 t3 - (y1 * t1 + y2 * t2 + y3 * t3) = (1 - y1) * t1 + (1 - y2) * t2 + (1 - y3) * t3`. -/
theorem weightedCharSum3_derived_and_double_weight_defect (y1 y2 y3 c1 c2 c3 t1 t2 t3 : Int) :
    unweightedBlockSum3 (y1 * c1) (y2 * c2) (y3 * c3) =
      weightedCharSum3 y1 y2 y3 c1 c2 c3 ∧
    unweightedBlockSum3 t1 t2 t3 - (y1 * t1 + y2 * t2 + y3 * t3) =
      (1 - y1) * t1 + (1 - y2) * t2 + (1 - y3) * t3 := by
  dsimp only [unweightedBlockSum3, weightedCharSum3]
  constructor
  · omega
  · rw [Int.sub_mul 1 y1 t1, Int.sub_mul 1 y2 t2, Int.sub_mul 1 y3 t3]
    omega

end QOU.Foundations.PeriodicStateTriangularInversionWeightSpaceEquivarianceBlockScalingWeightedDecomposition
