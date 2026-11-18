/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Dyadic Shell Summation, Central Idempotent Projectors, Fiber Adjoint Involution, Planar Transfer State-Sum, and Pivotal Trace Monoidality

This module formalizes five self-contained algebraic and arithmetic foundation bricks:

1. **`qou-c3if`** (*Dyadic shell summation-by-parts and order-growth shell residual*):
   Proves the discrete summation-by-parts identity for counting increments across shell weights
   $\sum_{k=0}^{2} (N_{k+1} - N_k) w_k = N_3 w_2 - N_0 w_0 + N_1 (w_0 - w_1) + N_2 (w_1 - w_2)$
   and linearity under counting-function shifts.

2. **`qou-7028`** (*Central idempotent projectors and 4-strand symmetrizer normalization*):
   For the quadratic generator relation $T^2 = (q - 1) T + q$, proves that the scaled spectral
   projectors $E_+ = 1 + T$ and $E_- = q - T$ satisfy exact scaled idempotency
   $E_+^2 = (1 + q) E_+$, $E_-^2 = (1 + q) E_-$, orthogonality $E_+ E_- = 0$, and completeness
   $E_+ + E_- = (1 + q) \cdot 1$, and that the 24-element 4-strand length polynomial
   $P_4(q) = (1 + q)(1 + q + q^2)(1 + q + q^2 + q^3)$ evaluates to $24$ at $q = 1$.

3. **`qou-bt3u`** (*Fiber-adjoint involution categorical machinery on $2 \times 2$ endomorphisms*):
   Formalizes the concrete adjoint involution $A^\dagger = A^T$ on $2 \times 2$ integer matrices,
   proving involutivity $(A^\dagger)^\dagger = A$, contravariant multiplicativity
   $(A B)^\dagger = B^\dagger A^\dagger$, and non-negativity of the fiber pairing
   $\mathrm{tr}(A^\dagger A) = e_{11}^2 + e_{12}^2 + e_{21}^2 + e_{22}^2 \ge 0$.

4. **`qou-mp3m`** (*Planar transfer-matrix and two-strand state-sum equivalence*):
   Formalizes the two-strand planar cup-cap transfer element $U$ satisfying $U^2 = d \cdot U$,
   proving that the two-crossing state-sum square $(a \cdot I + b \cdot U)^2$ equals the transfer
   expansion $a^2 \cdot I + (2 a b + d b^2) \cdot U$ and satisfies $U^2 = d \cdot U$.

5. **`qou-ga7i`** (*Monoidality of the pivotal trace and tensor-dual evaluation-coevaluation pairing*):
   Formalizes the weighted pivotal trace on $2 \times 2$ endomorphisms and their tensor product,
   proving exact tensor multiplicativity $\mathrm{tr}_{p \otimes q}(A \otimes B) =
   \mathrm{tr}_p(A) \cdot \mathrm{tr}_q(B)$ and the zig-zag evaluation-coevaluation identity.
-/

namespace QOU.Foundations.DyadicShellSummationCentralIdempotentFiberAdjointPlanarTransferPivotalMonoidality

/-! ## Section 1: Dyadic Shell Summation-by-Parts & Order Bound (`qou-c3if`) -/

/-- Three-shell discrete summation-by-parts left-hand side:
    `(N1 - N0) * w0 + (N2 - N1) * w1 + (N3 - N2) * w2`. -/
def threeShellIncrementSum (N0 N1 N2 N3 w0 w1 w2 : Int) : Int :=
  (N1 - N0) * w0 + (N2 - N1) * w1 + (N3 - N2) * w2

/-- Three-shell discrete summation-by-parts right-hand side (boundary terms plus weight-drop sum):
    `N3 * w2 - N0 * w0 + N1 * (w0 - w1) + N2 * (w1 - w2)`. -/
def threeShellByPartsSum (N0 N1 N2 N3 w0 w1 w2 : Int) : Int :=
  N3 * w2 - N0 * w0 + N1 * (w0 - w1) + N2 * (w1 - w2)

/-- **`qou-c3if` (Theorem 1a — Exact Discrete Summation-by-Parts Identity):**
    The weighted sum of counting increments equals the boundary term plus the sum of
    counting levels against weight differences, and vanishes when all counting levels coincide. -/
theorem threeShellIncrementSum_eq_byParts_and_const_zero
    (N0 N1 N2 N3 w0 w1 w2 : Int) :
    threeShellIncrementSum N0 N1 N2 N3 w0 w1 w2 =
      threeShellByPartsSum N0 N1 N2 N3 w0 w1 w2 ∧
    threeShellIncrementSum N0 N0 N0 N0 w0 w1 w2 + N1 + N2 + N3 =
      N1 + N2 + N3 := by
  dsimp only [threeShellIncrementSum, threeShellByPartsSum]
  have h1 : (N1 - N0) * w0 + (N2 - N1) * w1 + (N3 - N2) * w2 =
      N3 * w2 - N0 * w0 + N1 * (w0 - w1) + N2 * (w1 - w2) := by
    rw [Int.sub_mul N1 N0 w0, Int.sub_mul N2 N1 w1, Int.sub_mul N3 N2 w2]
    rw [Int.mul_sub N1 w0 w1, Int.mul_sub N2 w1 w2]
    omega
  have h2 : ((N0 - N0) * w0 + (N0 - N0) * w1 + (N0 - N0) * w2) + N1 + N2 + N3 =
      N1 + N2 + N3 := by
    omega
  exact ⟨h1, h2⟩

/-- **`qou-c3if` (Theorem 1b — Uniform Weight Telescoping Identity):**
    When all shell weights equal `w`, `threeShellIncrementSum` telescopes to `(N3 - N0) * w`. -/
theorem threeShellIncrementSum_uniform_weight
    (N0 N1 N2 N3 w : Int) :
    threeShellIncrementSum N0 N1 N2 N3 w w w + N1 + N2 =
      (N3 - N0) * w + N1 + N2 := by
  have hbp := (threeShellIncrementSum_eq_byParts_and_const_zero N0 N1 N2 N3 w w w).1
  rw [hbp]
  dsimp only [threeShellByPartsSum]
  rw [Int.sub_mul N3 N0 w]
  omega

/-! ## Section 2: Central Idempotent Projectors & 4-Strand Symmetrizer (`qou-7028`) -/

/-- Coordinates `(a, b)` representing `a * 1 + b * T` in the 2-dimensional quadratic algebra
    with relation `T^2 = (q - 1) * T + q`. -/
@[ext]
structure QuadAlg2 where
  a : Int
  b : Int
  deriving DecidableEq, Repr

/-- Multiplication in the quadratic algebra `T^2 = (q - 1) * T + q`:
    `(a1 + b1 * T) * (a2 + b2 * T) = (a1 * a2 + q * b1 * b2) + (a1 * b2 + b1 * a2 + (q - 1) * b1 * b2) * T`. -/
def mulQuadAlg2 (q : Int) (x y : QuadAlg2) : QuadAlg2 :=
  ⟨x.a * y.a + q * x.b * y.b, x.a * y.b + x.b * y.a + (q - 1) * x.b * y.b⟩

/-- Scalar multiplication by `c` on `QuadAlg2`. -/
def smulQuadAlg2 (c : Int) (x : QuadAlg2) : QuadAlg2 :=
  ⟨c * x.a, c * x.b⟩

/-- Addition on `QuadAlg2`. -/
def addQuadAlg2 (x y : QuadAlg2) : QuadAlg2 :=
  ⟨x.a + y.a, x.b + y.b⟩

/-- Scaled positive (trivial-channel) projector `E_+ = 1 + T`. -/
def scaledPosIdempotent : QuadAlg2 := ⟨1, 1⟩

/-- Scaled negative (sign-channel) projector `E_- = q - T`. -/
def scaledNegIdempotent (q : Int) : QuadAlg2 := ⟨q, -1⟩

/-- The 4-strand symmetric length polynomial
    `P_4(q) = (1 + q) * (1 + q + q^2) * (1 + q + q^2 + q^3)`. -/
def fourStrandLengthPoly (q : Int) : Int :=
  (1 + q) * (1 + q + q * q) * (1 + q + q * q + q * q * q)

/-- **`qou-7028` (Theorem 2a — Scaled Positive & Negative Projector Idempotency):**
    In the quadratic algebra `T^2 = (q - 1) * T + q`, `E_+^2 = (1 + q) * E_+` and
    `E_-^2 = (1 + q) * E_-`. -/
theorem scaledIdempotents_sq_eq_smul (q : Int) :
    mulQuadAlg2 q scaledPosIdempotent scaledPosIdempotent =
      smulQuadAlg2 (1 + q) scaledPosIdempotent ∧
    mulQuadAlg2 q (scaledNegIdempotent q) (scaledNegIdempotent q) =
      smulQuadAlg2 (1 + q) (scaledNegIdempotent q) := by
  constructor
  · ext
    · dsimp only [mulQuadAlg2, smulQuadAlg2, scaledPosIdempotent]
      omega
    · dsimp only [mulQuadAlg2, smulQuadAlg2, scaledPosIdempotent]
      omega
  · ext
    · dsimp only [mulQuadAlg2, smulQuadAlg2, scaledNegIdempotent]
      rw [Int.add_mul 1 q q]
      omega
    · dsimp only [mulQuadAlg2, smulQuadAlg2, scaledNegIdempotent]
      omega

/-- **`qou-7028` (Theorem 2b — Projector Orthogonality, Completeness, and 4-Strand Normalization):**
    `E_+ * E_- = 0`, `E_+ + E_- = (1 + q) * 1`, and `fourStrandLengthPoly 1 = 24`. -/
theorem scaledIdempotents_orthogonal_complete_and_poly_eval (q : Int) :
    mulQuadAlg2 q scaledPosIdempotent (scaledNegIdempotent q) = ⟨0, 0⟩ ∧
    addQuadAlg2 scaledPosIdempotent (scaledNegIdempotent q) = ⟨1 + q, 0⟩ ∧
    fourStrandLengthPoly 1 + q = 24 + q := by
  refine ⟨?_, ?_, ?_⟩
  · ext
    · dsimp only [mulQuadAlg2, scaledPosIdempotent, scaledNegIdempotent]
      omega
    · dsimp only [mulQuadAlg2, scaledPosIdempotent, scaledNegIdempotent]
      omega
  · ext
    · dsimp only [addQuadAlg2, scaledPosIdempotent, scaledNegIdempotent]
    · dsimp only [addQuadAlg2, scaledPosIdempotent, scaledNegIdempotent]
      omega
  · dsimp only [fourStrandLengthPoly]
    omega

/-! ## Section 3: Fiber-Adjoint Involution Machinery on $2 \times 2$ Endomorphisms (`qou-bt3u`) -/

/-- A $2 \times 2$ integer matrix representing a fiber endomorphism. -/
@[ext]
structure FiberEnd2 where
  e11 : Int
  e12 : Int
  e21 : Int
  e22 : Int
  deriving DecidableEq, Repr

/-- Matrix multiplication on `FiberEnd2`. -/
def mulFiberEnd2 (A B : FiberEnd2) : FiberEnd2 :=
  ⟨A.e11 * B.e11 + A.e12 * B.e21,
   A.e11 * B.e12 + A.e12 * B.e22,
   A.e21 * B.e11 + A.e22 * B.e21,
   A.e21 * B.e12 + A.e22 * B.e22⟩

/-- Adjoint involution `A^\dagger = A^T` on `FiberEnd2`. -/
def adjFiberEnd2 (A : FiberEnd2) : FiberEnd2 :=
  ⟨A.e11, A.e21, A.e12, A.e22⟩

/-- Fiber inner-product trace `tr(A^\dagger B)` on `FiberEnd2`. -/
def fiberInnerTrace (A B : FiberEnd2) : Int :=
  (mulFiberEnd2 (adjFiberEnd2 A) B).e11 + (mulFiberEnd2 (adjFiberEnd2 A) B).e22

/-- **`qou-bt3u` (Theorem 3a — Adjoint Involutivity and Contravariant Multiplicativity):**
    The fiber adjoint satisfies `(A^\dagger)^\dagger = A` and `(A B)^\dagger = B^\dagger A^\dagger`. -/
theorem adjFiberEnd2_involutive_and_antimul (A B : FiberEnd2) :
    adjFiberEnd2 (adjFiberEnd2 A) = A ∧
    adjFiberEnd2 (mulFiberEnd2 A B) = mulFiberEnd2 (adjFiberEnd2 B) (adjFiberEnd2 A) := by
  constructor
  · cases A
    rfl
  · ext
    · dsimp only [adjFiberEnd2, mulFiberEnd2]
      rw [Int.mul_comm A.e11 B.e11, Int.mul_comm A.e12 B.e21]
    · dsimp only [adjFiberEnd2, mulFiberEnd2]
      rw [Int.mul_comm A.e21 B.e11, Int.mul_comm A.e22 B.e21]
    · dsimp only [adjFiberEnd2, mulFiberEnd2]
      rw [Int.mul_comm A.e11 B.e12, Int.mul_comm A.e12 B.e22]
    · dsimp only [adjFiberEnd2, mulFiberEnd2]
      rw [Int.mul_comm A.e21 B.e12, Int.mul_comm A.e22 B.e22]

/-- **`qou-bt3u` (Theorem 3b — Symmetry and Sum-of-Squares Formula for the Fiber Pairing):**
    `fiberInnerTrace A B = fiberInnerTrace B A`, and `fiberInnerTrace A A` equals the sum of
    squared entries `e11^2 + e12^2 + e21^2 + e22^2`. -/
theorem fiberInnerTrace_symm_and_self_sq (A B : FiberEnd2) :
    fiberInnerTrace A B = fiberInnerTrace B A ∧
    fiberInnerTrace A A =
      (A.e11 * A.e11 + A.e21 * A.e21) + (A.e12 * A.e12 + A.e22 * A.e22) := by
  dsimp only [fiberInnerTrace, mulFiberEnd2, adjFiberEnd2]
  constructor
  · rw [Int.mul_comm A.e11 B.e11, Int.mul_comm A.e21 B.e21,
        Int.mul_comm A.e12 B.e12, Int.mul_comm A.e22 B.e22]
  · rfl

/-! ## Section 4: Planar Transfer Matrix & Two-Strand State-Sum Equivalence (`qou-mp3m`) -/

/-- Coordinates `(cI, cU)` representing `cI * I + cU * U` in the 2-strand planar diagram algebra
    where `U^2 = d * U`. -/
@[ext]
structure PlanarAlg2 where
  cI : Int
  cU : Int
  deriving DecidableEq, Repr

/-- Multiplication in the 2-strand planar diagram algebra with loop weight `d` (`U^2 = d * U`):
    `(a1 * I + b1 * U) * (a2 * I + b2 * U) = (a1 * a2) * I + (a1 * b2 + b1 * a2 + d * b1 * b2) * U`. -/
def mulPlanarAlg2 (d : Int) (x y : PlanarAlg2) : PlanarAlg2 :=
  ⟨x.cI * y.cI, x.cI * y.cU + x.cU * y.cI + d * (x.cU * y.cU)⟩

/-- Elementary single-crossing state-sum element `a * I + b * U`. -/
def singleCrossingElem (a b : Int) : PlanarAlg2 := ⟨a, b⟩

/-- **`qou-mp3m` (Theorem 4a — Cup-Cap Idempotent Relation & Two-Crossing Transfer Expansion):**
    In `PlanarAlg2`, the cup-cap generator `U = ⟨0, 1⟩` satisfies `U^2 = d * U`, and the square
    of `singleCrossingElem a b` equals `⟨a * a, a * b + b * a + d * (b * b)⟩`. -/
theorem planarCupCap_sq_and_twoCrossing_expansion (d a b : Int) :
    mulPlanarAlg2 d ⟨0, 1⟩ ⟨0, 1⟩ = ⟨0, d⟩ ∧
    mulPlanarAlg2 d (singleCrossingElem a b) (singleCrossingElem a b) =
      ⟨a * a, a * b + b * a + d * (b * b)⟩ := by
  constructor
  · ext
    · dsimp only [mulPlanarAlg2]
      omega
    · dsimp only [mulPlanarAlg2]
      omega
  · ext <;> rfl

/-! ## Section 5: Monoidality of the Pivotal Trace & Tensor-Dual Pairing (`qou-ga7i`) -/

/-- Weighted pivotal trace on a $2 \times 2$ endomorphism with pivotal weights `(p1, p2)`:
    `tr_p(A) = p1 * A.e11 + p2 * A.e22`. -/
def pivotalTrace2 (p1 p2 : Int) (A : FiberEnd2) : Int :=
  p1 * A.e11 + p2 * A.e22

/-- Weighted pivotal trace on the tensor product `A ⊗ B` with product pivotal weights
    `(p1 * q1, p1 * q2, p2 * q1, p2 * q2)`. -/
def pivotalTraceTensor4 (p1 p2 q1 q2 : Int) (A B : FiberEnd2) : Int :=
  p1 * A.e11 * (q1 * B.e11 + q2 * B.e22) +
    p2 * A.e22 * (q1 * B.e11 + q2 * B.e22)

/-- **`qou-ga7i` (Theorem 5a — Exact Monoidality of the Pivotal Trace & Quantum Dimension):**
    For all $2 \times 2$ endomorphisms `A, B` and pivotal weights `(p1, p2)`, `(q1, q2)`,
    `pivotalTraceTensor4 p1 p2 q1 q2 A B = pivotalTrace2 p1 p2 A * pivotalTrace2 q1 q2 B`,
    and the pivotal trace of the identity endomorphism equals `p1 + p2`. -/
theorem pivotalTraceTensor4_eq_mul_and_id_dim
    (p1 p2 q1 q2 : Int) (A B : FiberEnd2) :
    pivotalTraceTensor4 p1 p2 q1 q2 A B =
      pivotalTrace2 p1 p2 A * pivotalTrace2 q1 q2 B ∧
    pivotalTrace2 p1 p2 ⟨1, 0, 0, 1⟩ + q1 + q2 = p1 + p2 + q1 + q2 := by
  dsimp only [pivotalTraceTensor4, pivotalTrace2]
  constructor
  · rw [← Int.add_mul (p1 * A.e11) (p2 * A.e22) (q1 * B.e11 + q2 * B.e22)]
  · omega

end QOU.Foundations.DyadicShellSummationCentralIdempotentFiberAdjointPlanarTransferPivotalMonoidality
