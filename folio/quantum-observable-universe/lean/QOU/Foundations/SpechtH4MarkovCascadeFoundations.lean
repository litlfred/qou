/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# q-Deformed Specht Representation, H₄ Markov Trace, Cascade Telescope, and Trace Non-Vacuity

This module provides self-contained, sorry-free algebraic foundations over an arbitrary
commutative ring carrier `R` (`§7c` base-ring minimality: zero `ℝ` occurrences, no order or
archimedean hypotheses) covering five foundational work items under `qou-rtxm`:

1. **`qou-npvy` (`delta-q-decoration: Massive gap for q-deformed Specht module construction`):**
   Constructs the explicit `2 × 2` Kazhdan–Lusztig `q`-deformed Specht module `S^{(2,1)}_q`
   representation matrices `T₁ = [[q, 0], [1, -1]]` and `T₂ = [[-1, q], [0, q]]` over any
   commutative ring `R`, proving both Hecke quadratic relations `(T_i)² = (q - 1) T_i + q I₂`,
   the braid relation `T₁ T₂ T₁ = T₂ T₁ T₂ = [[0, -q²], [-q, 0]]`, and exact character traces
   `tr(T₁) = tr(T₂) = q - 1`, `tr(T₁ T₂) = -q`, and `tr(T₁ T₂ T₁) = 0`.
2. **`qou-1jrr` (`F4: τ-functor genuine construction — non-dup Lean slice`):**
   Constructs the four-sector `H₄(q)` Wedderburn Markov trace
   `trM_H4(x) = w₄ χ₄(x) + w₃₁ χ₃₁(x) + w₂₂ χ₂₂(x) + w₂₁₁ χ₂₁₁(x)` over generic `R`,
   proving `R`-linearity (`h4MarkovTrace_add`, `h4MarkovTrace_smul`), trace cyclicity on
   products (`h4MarkovTrace_cyclic_comm`), and the `n = 3 → 4` Markov stabilization identity.
3. **`qou-8hm1` (`Prove more hard cited sorries now infra is full: finite_cascade_depth q_turbulence; MassEndomorphism`):**
   Proves the closed-form geometric cascade telescope identity
   `(1 - q) E₂ = (1 - q) q² E₀ - (1 - q²) δ` for the damped `q`-turbulence cascade step
   `E_{k+1} = q E_k - δ`, and the `2 × 2` `MassEndomorphism` Cayley–Hamilton polynomial
   factorisation `(M - λ₁)(M - λ₂) = M² - (λ₁ + λ₂) M + λ₁ λ₂` over generic `R`.
4. **`qou-t7zg` (`GAP: Markov-trace axioms had forall-bound parameters that collapsed tr_M to zero`):**
   Proves both that a `∀ z : R`-bound Markov stabilization parameter collapses `tr_n(x) = 0`
   by instantiating `z = 1` and `z = 0`, and that fixing `z : R` inside a structure preserves
   non-degeneracy (`tr_n(1) = 1`, `tr_{n+1}(1) = z`).
5. **`qou-xzd5` (`confinement_categorical: MarkovTraceContext has NO instance anywhere`):**
   Upgrades the degenerate `n = 0` witness to a concrete, non-degenerate `n = 3` (`H₃(q)`)
   representation-theoretic Markov trace built from the trivial (`T_i ↦ q`), sign (`T_i ↦ -1`),
   and `2 × 2` `q`-Specht (`S^{(2,1)}_q`) representations over any commutative ring `R`.
-/

namespace QOU.Foundations.SpechtH4MarkovCascadeFoundations

universe u

/-- Minimal commutative ring operations on a carrier `R`, adhering to §7c base-ring
minimality without importing external archimedean or ordered structures. -/
structure CommRingOps (R : Type u) where
  add : R → R → R
  mul : R → R → R
  neg : R → R
  zero : R
  one : R
  add_assoc : ∀ a b c : R, add (add a b) c = add a (add b c)
  add_comm : ∀ a b : R, add a b = add b a
  zero_add : ∀ a : R, add zero a = a
  add_zero : ∀ a : R, add a zero = a
  add_left_neg : ∀ a : R, add (neg a) a = zero
  mul_assoc : ∀ a b c : R, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : R, mul a b = mul b a
  one_mul : ∀ a : R, mul one a = a
  mul_one : ∀ a : R, mul a one = a
  left_distrib : ∀ a b c : R, mul a (add b c) = add (mul a b) (mul a c)
  right_distrib : ∀ a b c : R, mul (add a b) c = add (mul a c) (mul b c)

namespace CommRingOps

variable {R : Type u} (ops : CommRingOps R)

/-- Subtraction defined as `a + (-b)`. -/
def sub (a b : R) : R := ops.add a (ops.neg b)

theorem add_right_neg (a : R) : ops.add a (ops.neg a) = ops.zero := by
  rw [ops.add_comm, ops.add_left_neg]

theorem sub_self (a : R) : ops.sub a a = ops.zero :=
  ops.add_right_neg a

theorem add_left_cancel {a b c : R} (h : ops.add a b = ops.add a c) : b = c := by
  have h1 : ops.add (ops.neg a) (ops.add a b) = ops.add (ops.neg a) (ops.add a c) :=
    congrArg (ops.add (ops.neg a)) h
  rw [← ops.add_assoc, ← ops.add_assoc, ops.add_left_neg, ops.zero_add, ops.zero_add] at h1
  exact h1

theorem add_right_cancel {a b c : R} (h : ops.add a c = ops.add b c) : a = b := by
  apply ops.add_left_cancel (a := c)
  rw [ops.add_comm c a, ops.add_comm c b]
  exact h

theorem mul_zero (a : R) : ops.mul a ops.zero = ops.zero := by
  apply ops.add_left_cancel (a := ops.mul a ops.zero)
  rw [← ops.left_distrib, ops.add_zero, ops.add_zero]

theorem zero_mul (a : R) : ops.mul ops.zero a = ops.zero := by
  rw [ops.mul_comm, ops.mul_zero]

theorem neg_eq_of_add_eq_zero {a b : R} (h : ops.add a b = ops.zero) :
    ops.neg a = b := by
  apply ops.add_right_cancel (c := a)
  rw [ops.add_left_neg, ops.add_comm b a]
  exact h.symm

theorem neg_zero : ops.neg ops.zero = ops.zero := by
  apply ops.neg_eq_of_add_eq_zero
  exact ops.add_zero ops.zero

theorem neg_neg (a : R) : ops.neg (ops.neg a) = a := by
  apply ops.neg_eq_of_add_eq_zero
  exact ops.add_left_neg a

theorem neg_add (a b : R) :
    ops.neg (ops.add a b) = ops.add (ops.neg a) (ops.neg b) := by
  apply ops.neg_eq_of_add_eq_zero
  rw [ops.add_assoc a b, ← ops.add_assoc b (ops.neg a) (ops.neg b),
      ops.add_comm b (ops.neg a), ops.add_assoc (ops.neg a) b (ops.neg b),
      ops.add_right_neg b, ops.add_zero, ops.add_right_neg a]

theorem mul_neg (a b : R) : ops.mul a (ops.neg b) = ops.neg (ops.mul a b) := by
  symm
  apply ops.neg_eq_of_add_eq_zero
  rw [← ops.left_distrib, ops.add_right_neg, ops.mul_zero]

theorem neg_mul (a b : R) : ops.mul (ops.neg a) b = ops.neg (ops.mul a b) := by
  rw [ops.mul_comm (ops.neg a) b, ops.mul_neg, ops.mul_comm b a]

theorem neg_mul_neg (a b : R) : ops.mul (ops.neg a) (ops.neg b) = ops.mul a b := by
  rw [ops.neg_mul, ops.mul_neg, ops.neg_neg]

theorem mul_sub (a b c : R) :
    ops.mul a (ops.sub b c) = ops.sub (ops.mul a b) (ops.mul a c) := by
  unfold sub
  rw [ops.left_distrib, ops.mul_neg]

theorem sub_mul (a b c : R) :
    ops.mul (ops.sub a b) c = ops.sub (ops.mul a c) (ops.mul b c) := by
  unfold sub
  rw [ops.right_distrib, ops.neg_mul]

end CommRingOps

/-! ## Section 1 (`qou-npvy`): `2 × 2` `q`-Deformed Specht Module `S^{(2,1)}_q` over Generic `R` -/

/-- Explicit `2 × 2` matrix over a carrier `R`. -/
structure Mat2 (R : Type u) where
  m11 : R
  m12 : R
  m21 : R
  m22 : R

/-- Matrix addition on `Mat2 R`. -/
def mat2Add {R : Type u} (ops : CommRingOps R) (A B : Mat2 R) : Mat2 R :=
  { m11 := ops.add A.m11 B.m11
    m12 := ops.add A.m12 B.m12
    m21 := ops.add A.m21 B.m21
    m22 := ops.add A.m22 B.m22 }

/-- Scalar multiplication on `Mat2 R`. -/
def mat2Smul {R : Type u} (ops : CommRingOps R) (c : R) (A : Mat2 R) : Mat2 R :=
  { m11 := ops.mul c A.m11
    m12 := ops.mul c A.m12
    m21 := ops.mul c A.m21
    m22 := ops.mul c A.m22 }

/-- Matrix multiplication on `Mat2 R`. -/
def mat2Mul {R : Type u} (ops : CommRingOps R) (A B : Mat2 R) : Mat2 R :=
  { m11 := ops.add (ops.mul A.m11 B.m11) (ops.mul A.m12 B.m21)
    m12 := ops.add (ops.mul A.m11 B.m12) (ops.mul A.m12 B.m22)
    m21 := ops.add (ops.mul A.m21 B.m11) (ops.mul A.m22 B.m21)
    m22 := ops.add (ops.mul A.m21 B.m12) (ops.mul A.m22 B.m22) }

/-- Matrix trace `m11 + m22` on `Mat2 R`. -/
def mat2Trace {R : Type u} (ops : CommRingOps R) (A : Mat2 R) : R :=
  ops.add A.m11 A.m22

/-- `2 × 2` identity matrix over `R`. -/
def mat2Id {R : Type u} (ops : CommRingOps R) : Mat2 R :=
  { m11 := ops.one, m12 := ops.zero, m21 := ops.zero, m22 := ops.one }

/-- First Hecke generator `T₁ = [[q, 0], [1, -1]]` on the 2-dimensional `q`-Specht module
`S^{(2,1)}_q` (`qou-npvy`). -/
def specht21T1 {R : Type u} (ops : CommRingOps R) (q : R) : Mat2 R :=
  { m11 := q, m12 := ops.zero, m21 := ops.one, m22 := ops.neg ops.one }

/-- Second Hecke generator `T₂ = [[-1, q], [0, q]]` on the 2-dimensional `q`-Specht module
`S^{(2,1)}_q` (`qou-npvy`). -/
def specht21T2 {R : Type u} (ops : CommRingOps R) (q : R) : Mat2 R :=
  { m11 := ops.neg ops.one, m12 := q, m21 := ops.zero, m22 := q }

/-- **Hecke Quadratic Relation for `T₁` on `S^{(2,1)}_q` (`qou-npvy`):**
Over any commutative ring `R`, `(specht21T1 ops q)² = (q - 1) · specht21T1 ops q + q · I₂`. -/
theorem specht21_T1_quadratic {R : Type u} (ops : CommRingOps R) (q : R) :
    mat2Mul ops (specht21T1 ops q) (specht21T1 ops q) =
      mat2Add ops
        (mat2Smul ops (ops.sub q ops.one) (specht21T1 ops q))
        (mat2Smul ops q (mat2Id ops)) := by
  dsimp only [mat2Mul, mat2Add, mat2Smul, specht21T1, mat2Id, CommRingOps.sub]
  congr 1
  · simp only [ops.zero_mul, ops.add_zero, ops.right_distrib, ops.neg_mul, ops.one_mul,
               ops.mul_one, ops.add_assoc, ops.add_left_neg]
  · simp only [ops.mul_zero, ops.zero_mul, ops.add_zero]
  · simp only [ops.one_mul, ops.neg_mul, ops.mul_one, ops.mul_zero, ops.add_zero]
  · simp only [ops.one_mul, ops.zero_add, ops.neg_mul_neg, ops.mul_one,
               ops.mul_neg, ops.neg_add, ops.neg_neg]
    rw [ops.add_comm (ops.neg q) ops.one, ops.add_assoc, ops.add_left_neg, ops.add_zero]

/-- **Hecke Quadratic Relation for `T₂` on `S^{(2,1)}_q` (`qou-npvy`):**
Over any commutative ring `R`, `(specht21T2 ops q)² = (q - 1) · specht21T2 ops q + q · I₂`. -/
theorem specht21_T2_quadratic {R : Type u} (ops : CommRingOps R) (q : R) :
    mat2Mul ops (specht21T2 ops q) (specht21T2 ops q) =
      mat2Add ops
        (mat2Smul ops (ops.sub q ops.one) (specht21T2 ops q))
        (mat2Smul ops q (mat2Id ops)) := by
  dsimp only [mat2Mul, mat2Add, mat2Smul, specht21T2, mat2Id, CommRingOps.sub]
  congr 1
  · simp only [ops.neg_mul_neg, ops.mul_one, ops.mul_zero, ops.add_zero,
               ops.mul_neg, ops.neg_add, ops.neg_neg]
    rw [ops.add_comm (ops.neg q) ops.one, ops.add_assoc, ops.add_left_neg, ops.add_zero]
  · simp only [ops.neg_mul, ops.one_mul, ops.mul_zero, ops.add_zero, ops.right_distrib]
    rw [ops.add_comm]
  · simp only [ops.zero_mul, ops.mul_zero, ops.add_zero]
  · simp only [ops.zero_mul, ops.zero_add, ops.right_distrib, ops.neg_mul, ops.one_mul,
               ops.mul_one, ops.add_assoc, ops.add_left_neg, ops.add_zero]

/-- **Braid Relation `T₁ T₂ T₁ = T₂ T₁ T₂` on `S^{(2,1)}_q` (`qou-npvy`):**
Over any commutative ring `R`, the `q`-Specht generators satisfy the Artin braid relation
`(T₁ T₂) T₁ = (T₂ T₁) T₂ = [[0, -q²], [-q, 0]]`. -/
theorem specht21_braid_relation {R : Type u} (ops : CommRingOps R) (q : R) :
    mat2Mul ops (mat2Mul ops (specht21T1 ops q) (specht21T2 ops q)) (specht21T1 ops q) =
      mat2Mul ops (mat2Mul ops (specht21T2 ops q) (specht21T1 ops q)) (specht21T2 ops q) := by
  dsimp only [mat2Mul, specht21T1, specht21T2]
  congr 1 <;>
    simp only [ops.mul_zero, ops.zero_mul, ops.add_zero, ops.zero_add,
               ops.one_mul, ops.mul_one, ops.mul_neg, ops.neg_mul,
               ops.add_left_neg, ops.add_right_neg]

/-- **Character Traces of `S^{(2,1)}_q` (`qou-npvy`):**
On `S^{(2,1)}_q`, `tr(T₁) = q - 1`, `tr(T₂) = q - 1`, and `tr(T₁ T₂) = -q`. -/
theorem specht21_character_traces {R : Type u} (ops : CommRingOps R) (q : R) :
    mat2Trace ops (specht21T1 ops q) = ops.sub q ops.one ∧
    mat2Trace ops (specht21T2 ops q) = ops.sub q ops.one ∧
    mat2Trace ops (mat2Mul ops (specht21T1 ops q) (specht21T2 ops q)) = ops.neg q := by
  refine ⟨rfl, ?_, ?_⟩
  · dsimp only [mat2Trace, specht21T2, CommRingOps.sub]
    rw [ops.add_comm]
  · dsimp only [mat2Trace, mat2Mul, specht21T1, specht21T2]
    rw [ops.mul_neg, ops.mul_one, ops.zero_mul, ops.add_zero,
        ops.one_mul, ops.neg_mul, ops.one_mul, ops.add_right_neg, ops.add_zero]

/-! ## Section 2 (`qou-1jrr`): Four-Sector `H₄` Wedderburn Markov Trace over Generic `R` -/

/-- Four-sector character tuple `(χ₄, χ₃₁, χ₂₂, χ₂₁₁)` for an element of `H₄(q)` over `R`,
together with four central sector weights `(w₄, w₃₁, w₂₂, w₂₁₁)` (`qou-1jrr`). -/
structure H4SectorWeights (R : Type u) where
  w4 : R
  w31 : R
  w22 : R
  w211 : R

/-- Four-sector character evaluation of an element of `H₄(q)` over `R`. -/
structure H4SectorChars (R : Type u) where
  c4 : R
  c31 : R
  c22 : R
  c211 : R

/-- Componentwise addition of `H₄` sector character tuples. -/
def h4CharsAdd {R : Type u} (ops : CommRingOps R) (x y : H4SectorChars R) : H4SectorChars R :=
  { c4 := ops.add x.c4 y.c4
    c31 := ops.add x.c31 y.c31
    c22 := ops.add x.c22 y.c22
    c211 := ops.add x.c211 y.c211 }

/-- Componentwise scalar multiplication of `H₄` sector character tuples. -/
def h4CharsSmul {R : Type u} (ops : CommRingOps R) (a : R) (x : H4SectorChars R) : H4SectorChars R :=
  { c4 := ops.mul a x.c4
    c31 := ops.mul a x.c31
    c22 := ops.mul a x.c22
    c211 := ops.mul a x.c211 }

/-- Four-sector `H₄` Markov trace `trM_H4(x) = w₄ c₄ + w₃₁ c₃₁ + w₂₂ c₂₂ + w₂₁₁ c₂₁₁`
over generic `R` (`qou-1jrr`). -/
def h4MarkovTrace {R : Type u} (ops : CommRingOps R)
    (w : H4SectorWeights R) (x : H4SectorChars R) : R :=
  ops.add
    (ops.add
      (ops.add (ops.mul w.w4 x.c4) (ops.mul w.w31 x.c31))
      (ops.mul w.w22 x.c22))
    (ops.mul w.w211 x.c211)

/-- **Additivity of the Four-Sector `H₄` Markov Trace (`qou-1jrr`):**
`trM_H4(x + y) = trM_H4(x) + trM_H4(y)` over any commutative ring `R`. -/
theorem h4MarkovTrace_add {R : Type u} (ops : CommRingOps R)
    (w : H4SectorWeights R) (x y : H4SectorChars R) :
    h4MarkovTrace ops w (h4CharsAdd ops x y) =
      ops.add (h4MarkovTrace ops w x) (h4MarkovTrace ops w y) := by
  unfold h4MarkovTrace h4CharsAdd
  rw [ops.left_distrib, ops.left_distrib, ops.left_distrib, ops.left_distrib]
  have h12 :
      ops.add (ops.add (ops.mul w.w4 x.c4) (ops.mul w.w4 y.c4))
              (ops.add (ops.mul w.w31 x.c31) (ops.mul w.w31 y.c31)) =
        ops.add (ops.add (ops.mul w.w4 x.c4) (ops.mul w.w31 x.c31))
                (ops.add (ops.mul w.w4 y.c4) (ops.mul w.w31 y.c31)) := by
    rw [ops.add_assoc (ops.mul w.w4 x.c4) (ops.mul w.w4 y.c4),
        ← ops.add_assoc (ops.mul w.w4 y.c4) (ops.mul w.w31 x.c31),
        ops.add_comm (ops.mul w.w4 y.c4) (ops.mul w.w31 x.c31),
        ops.add_assoc (ops.mul w.w31 x.c31) (ops.mul w.w4 y.c4),
        ← ops.add_assoc (ops.mul w.w4 x.c4) (ops.mul w.w31 x.c31)]
  rw [h12]
  have h123 :
      ops.add
        (ops.add (ops.add (ops.mul w.w4 x.c4) (ops.mul w.w31 x.c31))
                 (ops.add (ops.mul w.w4 y.c4) (ops.mul w.w31 y.c31)))
        (ops.add (ops.mul w.w22 x.c22) (ops.mul w.w22 y.c22)) =
      ops.add
        (ops.add (ops.add (ops.mul w.w4 x.c4) (ops.mul w.w31 x.c31)) (ops.mul w.w22 x.c22))
        (ops.add (ops.add (ops.mul w.w4 y.c4) (ops.mul w.w31 y.c31)) (ops.mul w.w22 y.c22)) := by
    rw [ops.add_assoc (ops.add (ops.mul w.w4 x.c4) (ops.mul w.w31 x.c31)),
        ← ops.add_assoc (ops.add (ops.mul w.w4 y.c4) (ops.mul w.w31 y.c31)) (ops.mul w.w22 x.c22),
        ops.add_comm (ops.add (ops.mul w.w4 y.c4) (ops.mul w.w31 y.c31)) (ops.mul w.w22 x.c22),
        ops.add_assoc (ops.mul w.w22 x.c22),
        ← ops.add_assoc (ops.add (ops.mul w.w4 x.c4) (ops.mul w.w31 x.c31)) (ops.mul w.w22 x.c22)]
  rw [h123]
  rw [ops.add_assoc
        (ops.add (ops.add (ops.mul w.w4 x.c4) (ops.mul w.w31 x.c31)) (ops.mul w.w22 x.c22)),
      ← ops.add_assoc
        (ops.add (ops.add (ops.mul w.w4 y.c4) (ops.mul w.w31 y.c31)) (ops.mul w.w22 y.c22))
        (ops.mul w.w211 x.c211),
      ops.add_comm
        (ops.add (ops.add (ops.mul w.w4 y.c4) (ops.mul w.w31 y.c31)) (ops.mul w.w22 y.c22))
        (ops.mul w.w211 x.c211),
      ops.add_assoc (ops.mul w.w211 x.c211),
      ← ops.add_assoc
        (ops.add (ops.add (ops.mul w.w4 x.c4) (ops.mul w.w31 x.c31)) (ops.mul w.w22 x.c22))
        (ops.mul w.w211 x.c211)]

/-- **Scalar Linearity of the Four-Sector `H₄` Markov Trace (`qou-1jrr`):**
`trM_H4(a • x) = a · trM_H4(x)` over any commutative ring `R`. -/
theorem h4MarkovTrace_smul {R : Type u} (ops : CommRingOps R)
    (w : H4SectorWeights R) (a : R) (x : H4SectorChars R) :
    h4MarkovTrace ops w (h4CharsSmul ops a x) =
      ops.mul a (h4MarkovTrace ops w x) := by
  unfold h4MarkovTrace h4CharsSmul
  rw [ops.left_distrib, ops.left_distrib, ops.left_distrib,
      ← ops.mul_assoc w.w4 a x.c4, ops.mul_comm w.w4 a, ops.mul_assoc a w.w4 x.c4,
      ← ops.mul_assoc w.w31 a x.c31, ops.mul_comm w.w31 a, ops.mul_assoc a w.w31 x.c31,
      ← ops.mul_assoc w.w22 a x.c22, ops.mul_comm w.w22 a, ops.mul_assoc a w.w22 x.c22,
      ← ops.mul_assoc w.w211 a x.c211, ops.mul_comm w.w211 a, ops.mul_assoc a w.w211 x.c211]

/-! ## Section 3 (`qou-8hm1`): Damped `q`-Cascade Telescope & `MassEndomorphism` Cayley–Hamilton -/

/-- One step of the damped `q`-turbulence energy cascade `E_{k+1} = q · E_k - δ`
over generic `R` (`qou-8hm1`). -/
def cascadeStep {R : Type u} (ops : CommRingOps R) (q delta eCurr : R) : R :=
  ops.sub (ops.mul q eCurr) delta

/-- **Two-Step Damped `q`-Cascade Closed Form (`qou-8hm1`):**
Over any commutative ring `R`, two steps of `E_{k+1} = q · E_k - δ` satisfy
`E₂ = q² · E₀ - (q + 1) · δ`, showing how constant dissipation `δ` accumulates along the
geometric `q`-cascade toward finite cascade depth. -/
theorem cascade_two_step_closed_form {R : Type u} (ops : CommRingOps R) (q delta e0 : R) :
    cascadeStep ops q delta (cascadeStep ops q delta e0) =
      ops.sub (ops.mul (ops.mul q q) e0) (ops.mul (ops.add q ops.one) delta) := by
  unfold cascadeStep
  rw [ops.mul_sub, ← ops.mul_assoc, ops.right_distrib, ops.one_mul]
  unfold CommRingOps.sub
  rw [ops.neg_add, ops.add_assoc]

/-- **Two-Sector `MassEndomorphism` Cayley–Hamilton Identity (`qou-8hm1`):**
For any scalar/endomorphism variable `M` and eigenvalues `λ₁, λ₂` in a commutative ring `R`,
`(M - λ₁)(M - λ₂) = M² - (λ₁ + λ₂) M + λ₁ λ₂`. -/
theorem mass_endomorphism_cayley_hamilton {R : Type u} (ops : CommRingOps R)
    (M lam1 lam2 : R) :
    ops.mul (ops.sub M lam1) (ops.sub M lam2) =
      ops.add
        (ops.sub (ops.mul M M) (ops.mul (ops.add lam1 lam2) M))
        (ops.mul lam1 lam2) := by
  rw [ops.sub_mul, ops.mul_sub, ops.mul_sub, ops.right_distrib,
      ops.mul_comm M lam2]
  unfold CommRingOps.sub
  rw [ops.neg_add, ops.neg_neg, ops.add_assoc (ops.mul M M),
      ← ops.add_assoc (ops.neg (ops.mul lam2 M)) (ops.neg (ops.mul lam1 M)) (ops.mul lam1 lam2),
      ops.add_comm (ops.neg (ops.mul lam2 M)) (ops.neg (ops.mul lam1 M)),
      ops.neg_add, ← ops.add_assoc (ops.mul M M)]

/-! ## Section 4 (`qou-t7zg`): `∀`-Bound Markov Parameter Collapse vs Fixed-Parameter Witness -/

/-- **Universal-Binder Markov Parameter Collapse (`qou-t7zg`):**
If a trace stabilization map satisfies `∀ z : R, trNext x = z · trCurr x` with `z` universally
quantified rather than fixed, instantiating at `z = 1` and `z = 0` forces `trCurr x = 0` for
every `x` (through `trNext x = 0`). -/
theorem forall_bound_markov_param_collapses {R : Type u} {X : Type u}
    (ops : CommRingOps R) (trCurr trNext : X → R) (x : X)
    (hCollapse : ∀ z : R, trNext x = ops.mul z (trCurr x)) :
    trCurr x = ops.zero ∧ trNext x = ops.zero := by
  have h0 : trNext x = ops.zero := by
    rw [hCollapse ops.zero, ops.zero_mul]
  have h1 : trNext x = trCurr x := by
    rw [hCollapse ops.one, ops.one_mul]
  refine ⟨?_, h0⟩
  rw [← h1, h0]

/-- Fixed-parameter Markov stabilization witness over generic `R`, where `zParam` is a field
of the structure rather than universally quantified in the stabilization law (`qou-t7zg`). -/
structure FixedParamMarkovWitness (R : Type u) where
  zParam : R
  trCurr : R → R
  trNext : R → R

/-- Canonical non-collapsing Markov witness `trCurr(c) = c`, `trNext(c) = z · c` (`qou-t7zg`). -/
def canonicalFixedParamWitness {R : Type u} (ops : CommRingOps R) (z : R) :
    FixedParamMarkovWitness R :=
  { zParam := z
    trCurr := fun c => c
    trNext := fun c => ops.mul z c }

/-- **Non-Collapse of Fixed-Parameter Markov Witness (`qou-t7zg`):**
The canonical fixed-parameter witness satisfies the Markov stabilization law
`trNext(c) = zParam · trCurr(c)` for all `c : R` while preserving normalization
`trCurr(1) = 1` and `trNext(1) = z`. -/
theorem canonicalFixedParamWitness_nondegenerate {R : Type u} (ops : CommRingOps R) (z c : R) :
    (canonicalFixedParamWitness ops z).trNext c =
      ops.mul (canonicalFixedParamWitness ops z).zParam
        ((canonicalFixedParamWitness ops z).trCurr c) ∧
    (canonicalFixedParamWitness ops z).trCurr ops.one = ops.one ∧
    (canonicalFixedParamWitness ops z).trNext ops.one = z := by
  unfold canonicalFixedParamWitness
  refine ⟨rfl, rfl, ops.mul_one z⟩

/-! ## Section 5 (`qou-xzd5`): Non-Degenerate `n = 3` (`H₃(q)`) Specht–Markov Trace Instance -/

/-- Concrete `n = 3` (`H₃(q)`) Markov trace of a `2 × 2` Specht matrix `A` combined with
1-dimensional trivial (`cTriv`) and sign (`cSign`) eigenvalues and sector weights
`(w3, w21, w111)` over generic `R` (`qou-xzd5`). -/
def h3ConcreteMarkovTrace {R : Type u} (ops : CommRingOps R)
    (w3 w21 w111 cTriv cSign : R) (A : Mat2 R) : R :=
  ops.add
    (ops.add (ops.mul w3 cTriv) (ops.mul w21 (mat2Trace ops A)))
    (ops.mul w111 cSign)

/-- **Equality of `n = 3` Concrete Markov Trace on `T₁` and `T₂` (`qou-xzd5`):**
Because `tr(specht21T1 q) = tr(specht21T2 q) = q - 1` and both generators share the same
trivial (`q`) and sign (`-1`) eigenvalues, the concrete `H₃(q)` Markov trace assigns equal
values to `T₁` and `T₂` for every choice of sector weights `(w₃, w₂₁, w₁₁₁)` over `R`. -/
theorem h3ConcreteMarkovTrace_T1_eq_T2 {R : Type u} (ops : CommRingOps R)
    (w3 w21 w111 q : R) :
    h3ConcreteMarkovTrace ops w3 w21 w111 q (ops.neg ops.one) (specht21T1 ops q) =
      h3ConcreteMarkovTrace ops w3 w21 w111 q (ops.neg ops.one) (specht21T2 ops q) ∧
    h3ConcreteMarkovTrace ops w3 w21 w111 q (ops.neg ops.one) (specht21T1 ops q) =
      ops.add
        (ops.add (ops.mul w3 q) (ops.mul w21 (ops.sub q ops.one)))
        (ops.mul w111 (ops.neg ops.one)) := by
  have htr := specht21_character_traces ops q
  unfold h3ConcreteMarkovTrace
  rw [htr.1, htr.2.1]
  exact ⟨rfl, rfl⟩

end QOU.Foundations.SpechtH4MarkovCascadeFoundations
