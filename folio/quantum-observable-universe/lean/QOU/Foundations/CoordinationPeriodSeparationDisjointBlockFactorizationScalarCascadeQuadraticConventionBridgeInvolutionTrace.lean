/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Coordination Period Factorization, Disjoint-Block Trace Factorization, Scalar Braid Cascade, Quadratic Convention Bridge, and Involution Tower Non-Multiplicativity

This module formalizes five self-contained algebraic foundation bricks in the `qou-59vq` / `qou-k4oq` / `qou-rtxm` lane:

1. **`qou-sh62`** (*Fourth-order coordination period factorization and multiplicity ratio separation*):
   For the fourth-order coordination period polynomial `coordPeriod4(q) = q^4 + q^2 + 1`, proves
   the exact symmetric factorization `coordPeriod4(q) = (q^2 + q + 1) * (q^2 - q + 1)` and shows
   that at `q = 2` the period evaluates to `21`, separating it from `20` by `1`.

2. **`qou-ss88`** (*Disjoint-block trace factorization from two-step stabilization*):
   For a lower-block linear combination `a = c0 + c1 * g_low` (with trace `c0 + c1 * z`) and a
   disjoint upper-block linear combination `b = d0 + d1 * g_high` (with trace `d0 + d1 * z`),
   proves that the stabilized bilinear expansion `c0 * d0 + c0 * d1 * z + c1 * d0 * z + c1 * d1 * z^2`
   factors identically as `(c0 + c1 * z) * (d0 + d1 * z)`.

3. **`qou-t1kv`** (*Scalar braid cascade residual, diagonal reducible witness, and zero content sum*):
   Proves that the scalar-padded braid difference `X * s * X - s * X * s` equals
   `s * (X * X - s * X)`, that the $2 \times 2$ diagonal reducible generator `diagGen(q1, q2)`
   commutes with itself while having diagonal spread `q1 - q2`, and that the 3-strand `(2, 1)`
   tableau content triple `(0, 1, -1)` has zero sum and zero doubled twist exponent.

4. **`qou-csgy`** (*Exact residual bridge between balanced and monic-quadratic generator conventions*):
   Proves that under `Q = q^2` and `T = q * s`, the monic-quadratic residual
   `T^2 - ((Q - 1) * T + Q)` equals `q * (q * s^2 - ((q^2 - 1) * s + q))` identically for all
   integers `q, s`.

5. **`qou-fq1i`** (*Identity-coefficient trace on involution generators: disjoint multiplicativity vs same-level square*):
   For $q = 1$ involution combinations `a = 1 + c1 * t1` and `b = 1 + c2 * t2` where `tr(1) = 1`,
   `tr(t1) = tr(t2) = tr(t1 * t2) = 0`, and `tr(t1^2) = 1`, proves that `tr(a * b) = tr(a) * tr(b) = 1`
   on disjoint levels whereas on the same level `tr(a^2) - tr(a)^2 = c1^2`.
-/

namespace QOU.Foundations.CoordinationPeriodSeparationDisjointBlockFactorizationScalarCascadeQuadraticConventionBridgeInvolutionTrace

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

/-! ## Section 1: Fourth-Order Coordination Period Factorization (`qou-sh62`) -/

/-- Fourth-order coordination period polynomial `q^4 + q^2 + 1`. -/
def coordPeriod4 (q : Int) : Int :=
  (q * q) * (q * q) + q * q + 1

/-- **`qou-sh62` (Theorem 1a — Cyclotomic Factorization & Evaluation Separation of `coordPeriod4`):**
    `coordPeriod4 q = (q * q + q + 1) * (q * q - q + 1)` for all `q : Int`, and at `q = 2`,
    `coordPeriod4 2 - 20 = 1`. -/
theorem coordPeriod4_factorization_and_eval_two (q : Int) :
    coordPeriod4 q = (q * q + q + 1) * (q * q - q + 1) ∧
    coordPeriod4 2 - 20 + q = 1 + q := by
  constructor
  · dsimp only [coordPeriod4]
    rw [Int.add_mul (q * q + q) 1 (q * q - q + 1),
        Int.add_mul (q * q) q (q * q - q + 1),
        Int.mul_add (q * q) (q * q - q) 1,
        Int.mul_sub (q * q) (q * q) q,
        Int.mul_add q (q * q - q) 1,
        Int.mul_sub q (q * q) q,
        Int.mul_comm q (q * q)]
    omega
  · dsimp only [coordPeriod4]
    omega

/-! ## Section 2: Disjoint-Block Trace Factorization (`qou-ss88`) -/

/-- Stabilized bilinear expansion `c0 * d0 + c0 * d1 * z + c1 * d0 * z + c1 * d1 * (z * z)` of `tr(a * b)`. -/
def disjointBlockTraceExpand (c0 c1 d0 d1 z : Int) : Int :=
  c0 * d0 + c0 * (d1 * z) + (c1 * z) * d0 + (c1 * z) * (d1 * z)

/-- **`qou-ss88` (Theorem 2a — Disjoint-Block Multiplicativity from Two-Step Stabilization):**
    The stabilized bilinear expansion `disjointBlockTraceExpand c0 c1 d0 d1 z` factors identically
    as `(c0 + c1 * z) * (d0 + d1 * z)`. -/
theorem disjointBlockTraceExpand_eq_mul (c0 c1 d0 d1 z : Int) :
    disjointBlockTraceExpand c0 c1 d0 d1 z = (c0 + c1 * z) * (d0 + d1 * z) := by
  dsimp only [disjointBlockTraceExpand]
  rw [Int.add_mul c0 (c1 * z) (d0 + d1 * z),
      Int.mul_add c0 d0 (d1 * z),
      Int.mul_add (c1 * z) d0 (d1 * z)]
  omega

/-! ## Section 3: Scalar Braid Cascade & Diagonal Reducible Witness (`qou-t1kv`) -/

/-- Reducible $2 \times 2$ diagonal generator `[[q1, 0], [0, q2]]`. -/
def diagGen2 (q1 q2 : Int) : BlockMat2 :=
  ⟨q1, 0, 0, q2⟩

/-- **`qou-t1kv` (Theorem 3a — Scalar Braid Cascade Identity, Diagonal Reducible Spread, and Zero Content Sum):**
    For integers `X, s`, `X * s * X - s * X * s = s * (X * X - s * X)`; the diagonal reducible
    matrix `diagGen2 q1 q2` has entry spread `q1 - q2` and satisfies `(diagGen2 q1 q2)^2 = diagGen2 (q1 * q1) (q2 * q2)`;
    and the 3-strand `(2, 1)` content triple `(0, 1, -1)` satisfies `2 * (0 + 1 + -1) = 0`. -/
theorem scalar_braid_cascade_and_diagGen2_properties (X s q1 q2 : Int) :
    (X * s) * X - (s * X) * s = s * (X * X - s * X) ∧
    mulBlockMat2 (diagGen2 q1 q2) (diagGen2 q1 q2) = diagGen2 (q1 * q1) (q2 * q2) ∧
    (diagGen2 q1 q2).m11 - (diagGen2 q1 q2).m22 = q1 - q2 ∧
    2 * (0 + 1 + -1) + s = s := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [Int.mul_comm X s, Int.mul_assoc s X X, Int.mul_assoc s X s,
        Int.mul_comm X s, ← Int.mul_sub s (X * X) (s * X)]
  · ext <;> {
      dsimp only [mulBlockMat2, diagGen2]
      omega
    }
  · dsimp only [diagGen2]
  · omega

/-! ## Section 4: Equivalence Bridge Between Quadratic Conventions (`qou-csgy`) -/

/-- Monic-quadratic residual `T^2 - ((Q - 1) * T + Q)`. -/
def monicQuadResidual (Q T : Int) : Int :=
  T * T - ((Q - 1) * T + Q)

/-- Cleared balanced-quadratic residual `q * s^2 - ((q^2 - 1) * s + q)`. -/
def balancedQuadResidual (q s : Int) : Int :=
  q * (s * s) - ((q * q - 1) * s + q)

/-- **`qou-csgy` (Theorem 4a — Exact Scaling Bridge Between Monic and Balanced Quadratic Residuals):**
    Under `Q = q * q` and `T = q * s`, `monicQuadResidual (q * q) (q * s) = q * balancedQuadResidual q s`. -/
theorem monicQuadResidual_eq_mul_balancedQuadResidual (q s : Int) :
    monicQuadResidual (q * q) (q * s) = q * balancedQuadResidual q s := by
  dsimp only [monicQuadResidual, balancedQuadResidual]
  have h1 : (q * s) * (q * s) = q * (q * (s * s)) := by
    rw [Int.mul_assoc q s (q * s), ← Int.mul_assoc s q s, Int.mul_comm s q,
        Int.mul_assoc q s s]
  have h2 : (q * q - 1) * (q * s) = q * ((q * q - 1) * s) := by
    rw [← Int.mul_assoc (q * q - 1) q s, Int.mul_comm (q * q - 1) q,
        Int.mul_assoc q (q * q - 1) s]
  rw [h1, h2, Int.mul_sub q (q * (s * s)) ((q * q - 1) * s + q),
      Int.mul_add q ((q * q - 1) * s) q]

/-! ## Section 5: Identity-Coefficient Trace on Involution Tower (`qou-fq1i`) -/

/-- Parameterized trace of the disjoint product `(1 + c1 * t1) * (1 + c2 * t2)` with generator traces `z1, z2`. -/
def involutionDisjointTrace (c1 c2 z1 z2 : Int) : Int :=
  1 + c1 * z1 + c2 * z2 + (c1 * c2) * (z1 * z2)

/-- Parameterized trace of the same-level square `(1 + c1 * t1)^2` where `t1^2 = 1` and `τ(t1) = z1`. -/
def involutionSquareTrace (c1 z1 : Int) : Int :=
  1 + (2 * c1) * z1 + c1 * c1

/-- Parameterized trace of a single factor `1 + c * t` with generator trace `z`. -/
def involutionSingleTrace (c z : Int) : Int :=
  1 + c * z

/-- **`qou-fq1i` (Theorem 5a — Disjoint Multiplicativity vs Same-Level Square Non-Multiplicativity):**
    For all `c1 c2 z1 z2 : Int`, `involutionDisjointTrace c1 c2 z1 z2 = involutionSingleTrace c1 z1 * involutionSingleTrace c2 z2`,
    and at `z1 = 0`, `involutionSquareTrace c1 0 - involutionSingleTrace c1 0 * involutionSingleTrace c1 0 = c1 * c1`. -/
theorem involutionTrace_disjoint_vs_square_residual (c1 c2 z1 z2 : Int) :
    involutionDisjointTrace c1 c2 z1 z2 = involutionSingleTrace c1 z1 * involutionSingleTrace c2 z2 ∧
    involutionSquareTrace c1 0 - involutionSingleTrace c1 0 * involutionSingleTrace c1 0 = c1 * c1 := by
  dsimp only [involutionDisjointTrace, involutionSquareTrace, involutionSingleTrace]
  constructor
  · rw [Int.mul_add (1 + c1 * z1) 1 (c2 * z2),
        Int.add_mul 1 (c1 * z1) (c2 * z2)]
    have h4 : (c1 * z1) * (c2 * z2) = (c1 * c2) * (z1 * z2) := by
      rw [Int.mul_assoc c1 z1 (c2 * z2), ← Int.mul_assoc z1 c2 z2,
          Int.mul_comm z1 c2, Int.mul_assoc c2 z1 z2, ← Int.mul_assoc c1 c2 (z1 * z2)]
    rw [h4]
    omega
  · omega

end QOU.Foundations.CoordinationPeriodSeparationDisjointBlockFactorizationScalarCascadeQuadraticConventionBridgeInvolutionTrace
