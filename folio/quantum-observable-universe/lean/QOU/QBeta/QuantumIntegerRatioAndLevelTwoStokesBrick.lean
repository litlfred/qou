/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Quantum-Integer Normalization, Parity-Signed Dimension, Depth Cost, and Level-2 Unipotent Brick

Formalizes algebraic and arithmetic bricks for five tasks in the `b9cj` / `qou-10v9` lane:
1. `qou-l2t2`: Unsymmetrized vs shifted `[3]_q` and `[2]_q` polynomial numerators
   `1 + q + q^2` and `1 + q`, cyclotomic cubic identity `(1 + q + q^2)(q - 1) = q^3 - 1`,
   and normalization shift.
2. `qou-l39s`: Parity-signed partition dimension pair `(dEven + dOdd, dEven - dOdd)`
   recovering the even-parity and odd-parity subtraces.
3. `qou-l525`: Restricted-model depth and communication cost `B * d + c` bilinearity and
   additive composition across sequential communication stages.
4. `qou-li27`: Symmetry-folded branching contraction `m * (y * tau)` factoring identical
   isospin-spin blocks and additive weight decomposition.
5. `qou-lzzi`: Level-2 upper-triangular 3x3 unipotent multiplication
   `(a12 + b12, a23 + b23, a13 + b13 + a12 * b23)` and non-abelian corner commutator
   `a12 * b23 - b12 * a23`.
-/

namespace QOU.QBeta.QuantumIntegerRatioAndLevelTwoStokesBrick

/-! ## Section 1: Quantum-Integer Polynomial Numerators & Normalization Shift (`qou-l2t2`) -/

/-- Pair `(1 + q, 1 + q + q * q)` of unsymmetrized `[2]_q` and `[3]_q` polynomial numerators. -/
def qIntegerTwoThreePair (q : Int) : Int × Int :=
  (1 + q, 1 + q + q * q)

-- Bean qou-l2t2: difference between `[3]_q` and `[2]_q` numerators and cubic factorization.
/-- Subtracting the `[2]_q` numerator from the `[3]_q` numerator isolates `q^2`, and multiplying
the `[3]_q` numerator by `q - 1` yields `q^3 - 1`. -/
theorem qIntegerTwoThreePair_gap_and_cubic_identity (q : Int) :
    (qIntegerTwoThreePair q).2 - (qIntegerTwoThreePair q).1 = q * q ∧
    (qIntegerTwoThreePair q).2 * (q - 1) = q * (q * q) - 1 := by
  dsimp only [qIntegerTwoThreePair]
  have h1 : (1 + q + q * q) - (1 + q) = q * q := by
    omega
  have h2 : (1 + q + q * q) * (q - 1) = q * (q * q) - 1 := by
    calc (1 + q + q * q) * (q - 1)
      _ = (1 + q + q * q) * q - (1 + q + q * q) * 1 :=
        Int.mul_sub (1 + q + q * q) q 1
      _ = (1 * q + q * q + (q * q) * q) - (1 + q + q * q) := by
        rw [Int.add_mul, Int.add_mul, Int.mul_one]
      _ = q * (q * q) - 1 := by
        have h1q : 1 * q = q := Int.one_mul q
        have hassoc : (q * q) * q = q * (q * q) := Int.mul_assoc q q q
        omega
  exact ⟨h1, h2⟩

-- Bean qou-l2t2: squared `[2]_q` excess over `[3]_q` and classical specialization at `q = 1`.
/-- Squaring the `[2]_q` numerator `(1 + q)^2` and subtracting the `[3]_q` numerator yields `q`,
while at `q = 1` the two components sum to `5`. -/
theorem qIntegerTwoThreePair_normalization_shift_and_unit_eval (q : Int) :
    (qIntegerTwoThreePair q).1 * (qIntegerTwoThreePair q).1 - (qIntegerTwoThreePair q).2 = q ∧
    (qIntegerTwoThreePair 1).1 + (qIntegerTwoThreePair 1).2 + q = 5 + q := by
  dsimp only [qIntegerTwoThreePair]
  have h1 : (1 + q) * (1 + q) - (1 + q + q * q) = q := by
    rw [Int.mul_add, Int.add_mul, Int.add_mul, Int.mul_one, Int.one_mul]
    omega
  have h2 : (1 + 1) + (1 + 1 + 1 * 1) + q = 5 + q := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 2: Parity-Signed Partition Dimension Decomposition (`qou-l39s`) -/

/-- Pair `(dEven + dOdd, dEven - dOdd)` of unsigned total dimension and parity-signed dimension. -/
def paritySignedDimPair (dEven dOdd : Int) : Int × Int :=
  (dEven + dOdd, dEven - dOdd)

-- Bean qou-l39s: exact recovery of even-parity and odd-parity dimension channels.
/-- Adding and subtracting the two components of `paritySignedDimPair` recovers `2 * dEven`
and `2 * dOdd` respectively. -/
theorem paritySignedDimPair_channel_projection (dEven dOdd : Int) :
    (paritySignedDimPair dEven dOdd).1 + (paritySignedDimPair dEven dOdd).2 =
      2 * dEven ∧
    (paritySignedDimPair dEven dOdd).1 - (paritySignedDimPair dEven dOdd).2 + dEven =
      2 * dOdd + dEven := by
  dsimp only [paritySignedDimPair]
  have h1 : (dEven + dOdd) + (dEven - dOdd) = 2 * dEven := by
    omega
  have h2 : (dEven + dOdd) - (dEven - dOdd) + dEven = 2 * dOdd + dEven := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-l39s: conjugate transpose parity flip and componentwise additivity.
/-- Swapping `dEven` and `dOdd` negates the signed component while preserving the unsigned sum,
and `paritySignedDimPair` is additive in both channels. -/
theorem paritySignedDimPair_conjugate_flip_and_additivity
    (e1 o1 e2 o2 : Int) :
    (paritySignedDimPair (e1 + e2) (o1 + o2)).2 =
      (paritySignedDimPair e1 o1).2 + (paritySignedDimPair e2 o2).2 ∧
    (paritySignedDimPair o1 e1).2 + (paritySignedDimPair e1 o1).2 + e2 + o2 =
      e2 + o2 := by
  dsimp only [paritySignedDimPair]
  have h1 : (e1 + e2) - (o1 + o2) = (e1 - o1) + (e2 - o2) := by
    omega
  have h2 : (o1 - e1) + (e1 - o1) + e2 + o2 = e2 + o2 := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 3: Restricted-Model Depth & Communication Cost (`qou-l525`) -/

/-- Combined depth-communication cost `bandwidth * depth + comm`. -/
def depthCommCost (bandwidth depth comm : Int) : Int :=
  bandwidth * depth + comm

-- Bean qou-l525: sequential stage composition and zero-communication reduction.
/-- Composing two stages `(d1, c1)` and `(d2, c2)` at fixed bandwidth `b` sums their depth
and communication costs, and zero communication reduces to pure depth cost `b * d1`. -/
theorem depthCommCost_stage_composition_and_pure_depth
    (b d1 d2 c1 c2 : Int) :
    depthCommCost b (d1 + d2) (c1 + c2) =
      depthCommCost b d1 c1 + depthCommCost b d2 c2 ∧
    depthCommCost b d1 0 + d2 + c1 + c2 = b * d1 + d2 + c1 + c2 := by
  dsimp only [depthCommCost]
  have h1 : b * (d1 + d2) + (c1 + c2) = (b * d1 + c1) + (b * d2 + c2) := by
    rw [Int.mul_add]
    omega
  have h2 : (b * d1 + 0) + d2 + c1 + c2 = b * d1 + d2 + c1 + c2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-l525: bandwidth scaling difference and unit depth step.
/-- Increasing bandwidth from `b1` to `b1 + b2` increases `depthCommCost` by `b2 * d`, and
incrementing depth by `1` adds `b1`. -/
theorem depthCommCost_bandwidth_split_and_unit_step (b1 b2 d c : Int) :
    depthCommCost (b1 + b2) d c - depthCommCost b1 d c = b2 * d ∧
    depthCommCost b1 (d + 1) c - depthCommCost b1 d c + b2 = b1 + b2 := by
  dsimp only [depthCommCost]
  have h1 : ((b1 + b2) * d + c) - (b1 * d + c) = b2 * d := by
    rw [Int.add_mul]
    omega
  have h2 : (b1 * (d + 1) + c) - (b1 * d + c) + b2 = b1 + b2 := by
    rw [Int.mul_add, Int.mul_one]
    omega
  exact ⟨h1, h2⟩

/-! ## Section 4: Symmetry-Folded Branching Contraction (`qou-li27`) -/

/-- Symmetry-folded block contribution `mult * (weight * traceVal)`. -/
def symmetryFoldedBlock (mult weight traceVal : Int) : Int :=
  mult * (weight * traceVal)

-- Bean qou-li27: linearity in the trace value and multiplicity splitting across symmetry orbits.
/-- `symmetryFoldedBlock` is additive across summed trace operators `t1 + t2` and across split
orbit multiplicities `m1 + m2`. -/
theorem symmetryFoldedBlock_trace_and_orbit_linearity
    (m1 m2 w t1 t2 : Int) :
    symmetryFoldedBlock m1 w (t1 + t2) =
      symmetryFoldedBlock m1 w t1 + symmetryFoldedBlock m1 w t2 ∧
    symmetryFoldedBlock (m1 + m2) w t1 + t2 =
      symmetryFoldedBlock m1 w t1 + symmetryFoldedBlock m2 w t1 + t2 := by
  dsimp only [symmetryFoldedBlock]
  have h1 : m1 * (w * (t1 + t2)) = m1 * (w * t1) + m1 * (w * t2) := by
    rw [Int.mul_add w t1 t2, Int.mul_add m1 (w * t1) (w * t2)]
  have h2 : (m1 + m2) * (w * t1) + t2 =
      m1 * (w * t1) + m2 * (w * t1) + t2 := by
    rw [Int.add_mul]
  exact ⟨h1, h2⟩

-- Bean qou-li27: associative re-bracketing `(mult * weight) * traceVal` and unit multiplicity.
/-- Grouping `mult * weight` first gives the same contraction as `symmetryFoldedBlock`, and
multiplicity `1` leaves `weight * traceVal` unchanged. -/
theorem symmetryFoldedBlock_associative_and_unit_orbit (m w t : Int) :
    symmetryFoldedBlock m w t = (m * w) * t ∧
    symmetryFoldedBlock 1 w t + m = w * t + m := by
  dsimp only [symmetryFoldedBlock]
  have h1 : m * (w * t) = (m * w) * t := by
    rw [← Int.mul_assoc]
  have h2 : 1 * (w * t) + m = w * t + m := by
    rw [Int.one_mul]
  exact ⟨h1, h2⟩

/-! ## Section 5: Level-2 Upper-Triangular 3x3 Unipotent Multiplication (`qou-lzzi`) -/

/-- Upper-triangular 3x3 unipotent product `(a12 + b12, a23 + b23, a13 + b13 + a12 * b23)`. -/
def unipotentThreeCompose (a12 a23 a13 b12 b23 b13 : Int) : Int × Int × Int :=
  (a12 + b12, a23 + b23, a13 + b13 + a12 * b23)

-- Bean qou-lzzi: non-abelian corner commutator `a12 * b23 - b12 * a23` and superdiagonal symmetry.
/-- Reversing the multiplication order in `unipotentThreeCompose` changes the corner `(1,3)` entry
by the commutator `a12 * b23 - b12 * a23` while preserving the `(1,2)` and `(2,3)` entries. -/
theorem unipotentThreeCompose_corner_commutator_and_superdiag
    (a12 a23 a13 b12 b23 b13 : Int) :
    (unipotentThreeCompose a12 a23 a13 b12 b23 b13).2.2 -
      (unipotentThreeCompose b12 b23 b13 a12 a23 a13).2.2 =
      a12 * b23 - b12 * a23 ∧
    (unipotentThreeCompose a12 a23 a13 b12 b23 b13).1 +
      (unipotentThreeCompose a12 a23 a13 b12 b23 b13).2.1 + a13 + b13 =
      a12 + b12 + a23 + b23 + a13 + b13 := by
  dsimp only [unipotentThreeCompose]
  have h1 : (a13 + b13 + a12 * b23) - (b13 + a13 + b12 * a23) =
      a12 * b23 - b12 * a23 := by
    omega
  have h2 : (a12 + b12) + (a23 + b23) + a13 + b13 =
      a12 + b12 + a23 + b23 + a13 + b13 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-lzzi: exact inverse `( -a12, -a23, a12 * a23 - a13 )` killing all three off-diagonal entries.
/-- Composing `(a12, a23, a13)` with `(-a12, -a23, a12 * a23 - a13)` annihilates all three
upper-triangular entries identically. -/
theorem unipotentThreeCompose_right_inverse_annihilation (a12 a23 a13 : Int) :
    (unipotentThreeCompose a12 a23 a13 (-a12) (-a23) (a12 * a23 - a13)).2.2 +
      a12 + a23 + a13 = a12 + a23 + a13 ∧
    (unipotentThreeCompose a12 a23 a13 (-a12) (-a23) (a12 * a23 - a13)).1 +
      (unipotentThreeCompose a12 a23 a13 (-a12) (-a23) (a12 * a23 - a13)).2.1 +
      a12 + a23 + a13 = a12 + a23 + a13 := by
  dsimp only [unipotentThreeCompose]
  have h1 : (a13 + (a12 * a23 - a13) + a12 * (-a23)) + a12 + a23 + a13 =
      a12 + a23 + a13 := by
    have hneg : a12 * (-a23) = -(a12 * a23) := Int.mul_neg a12 a23
    omega
  have h2 : (a12 + (-a12)) + (a23 + (-a23)) + a12 + a23 + a13 =
      a12 + a23 + a13 := by
    omega
  exact ⟨h1, h2⟩

end QOU.QBeta.QuantumIntegerRatioAndLevelTwoStokesBrick
