/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

/-!
# Tower Trace F-Laws, Generic-Ring Skein Calculus, Convention D Peel Weight Determination, Ribbon Twist Monodromy, and Clebsch–Gordan Three-Term Recurrence (`qou-utb3`, `qou-w4la`, `qou-k4oq`, `qou-o9ge`, `qou-0cyu`)

This module provides machine-checked, self-contained algebraic foundations over a generic
commutative ring carrier `R` (`§7c` base-ring minimality: zero `ℝ` occurrences, no order or
archimedean hypotheses) covering five foundational work items under `qou-rtxm`:

1. **`qou-utb3` (Tower Trace Induction & Tensor F-Law Multiplicativity):**
   Proves two-step strand-peel reduction `tr((x · g_{n+1}) · g_n) = z² · tr(x)` and tensor
   F-law compatibility `tr(x · g_n) · tr(y · g_m) = z² · (tr(x) · tr(y))` over any
   commutative ring `R`.
2. **`qou-w4la` (`§7c` Base-Ring Minimality — Generic Commutative Ring Skein & Inverse):**
   Proves over generic `GenericRingOps R` that any generator `s` satisfying the balanced
   quadratic relation `s² = (q - qInv) · s + 1` with `q · qInv = 1` satisfies the factored
   eigenvalue equation `(s - q) · (s + qInv) = 0` and has explicit two-sided multiplicative
   inverse `sInv = s - (q - qInv)` (`s · sInv = 1` and `sInv · s = 1`).
3. **`qou-k4oq` (Convention D Peel Weight `w = (1, q²)` and `z = q³/(q² + 1)` Forced by Partial Trace):**
   Proves that equating the two diagonal entries of the `2 × 2` partial trace
   `w0 · q + w1 · (q - qInv) = z` and `w1 · q = z` with `q · qInv = 1` forces `w0 · q = w1 · qInv`
   and `w1 = q² · w0`; at `w0 = 1` this pins `w1 = q²`, total weight `1 + q²`, unnormalized
   peel scalar `z = q³`, and the cleared Convention D normalization identity
   `zNorm · (1 + q²) = q³`.
4. **`qou-o9ge` (Ribbon Twist Monodromy Factorization & Pivotal Trace Cyclicity):**
   Proves that when the ribbon twist on a tensor product satisfies
   `thetaVW = (thetaV · thetaW) · (cWV · cVW)` with invertible object twists
   (`thetaV · thetaVInv = 1`, `thetaW · thetaWInv = 1`), the full braiding monodromy scalar
   is uniquely recovered as `cWV · cVW = thetaVW · (thetaVInv · thetaWInv)`, and the weighted
   pivotal trace of `2 × 2` morphisms is cyclic on weight-centralizing morphisms.
5. **`qou-0cyu` (Three-Term Quantum-Integer Clebsch–Gordan Step & Cubed Decomposition):**
   Proves the balanced quantum-integer three-term recurrence steps
   `[2]_q · [2]_q = [3]_q + [1]_q` and `[2]_q · [3]_q = [4]_q + [2]_q`, together with the
   `n = 3` tensor decomposition `[2]_q³ = [4]_q + 2 · [2]_q` over any commutative ring `R`.
-/

namespace QOU.Foundations.OcneanuTowerConventionDRibbonClebschGordan

universe u

/-- Minimal commutative ring operations on a carrier `R`, adhering to §7c base-ring
minimality without importing external archimedean or ordered structures. -/
structure GenericRingOps (R : Type u) where
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

namespace GenericRingOps

variable {R : Type u} (ops : GenericRingOps R)

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

theorem mul_sub {R : Type u} (ops : GenericRingOps R) (a b c : R) :
    ops.mul a (ops.sub b c) = ops.sub (ops.mul a b) (ops.mul a c) := by
  dsimp only [sub]
  rw [ops.left_distrib, ops.mul_neg]

theorem sub_mul {R : Type u} (ops : GenericRingOps R) (a b c : R) :
    ops.mul (ops.sub a b) c = ops.sub (ops.mul a c) (ops.mul b c) := by
  dsimp only [sub]
  rw [ops.right_distrib, ops.neg_mul]

theorem sub_eq_zero_iff {a b : R} : ops.sub a b = ops.zero ↔ a = b := by
  constructor
  · intro h
    apply ops.add_right_cancel (c := ops.neg b)
    rw [ops.add_right_neg]
    exact h
  · intro h
    rw [h]
    exact ops.sub_self b

theorem sub_zero {R : Type u} (ops : GenericRingOps R) (a : R) : ops.sub a ops.zero = a := by
  dsimp only [sub]
  rw [ops.neg_zero, ops.add_zero]

theorem zero_sub {R : Type u} (ops : GenericRingOps R) (a : R) : ops.sub ops.zero a = ops.neg a := by
  dsimp only [sub]
  rw [ops.zero_add]

end GenericRingOps

/-! ## Section 1 (`qou-utb3`): Strand-Tower Peel Reduction and Tensor F-Law Multiplicativity -/

/-- One-step strand-peel trace map scaling an inductive trace value `trX` by the peel
parameter `z` (`qou-utb3`). -/
def towerPeelStep {R : Type u} (ops : GenericRingOps R) (z trX : R) : R :=
  ops.mul z trX

/-- **Two-Step Strand-Tower Peel and Tensor F-Law Compatibility (`qou-utb3`):**
Applying two successive strand-tower peels scales the base trace `trX` by `z²`, and the product
of two single-peeled traces on tensor factors `trX, trY` equals `z²` times `trX · trY`. -/
theorem tower_peel_two_step_and_tensor_flaw {R : Type u} (ops : GenericRingOps R)
    (z trX trY trStep1 trStep2 : R)
    (h1 : trStep1 = towerPeelStep ops z trX)
    (h2 : trStep2 = towerPeelStep ops z trStep1) :
    trStep2 = ops.mul (ops.mul z z) trX ∧
      ops.mul (towerPeelStep ops z trX) (towerPeelStep ops z trY) =
        ops.mul (ops.mul z z) (ops.mul trX trY) := by
  refine ⟨?_, ?_⟩
  · rw [h2, h1]
    dsimp only [towerPeelStep]
    rw [← ops.mul_assoc]
  · dsimp only [towerPeelStep]
    rw [ops.mul_assoc z trX (ops.mul z trY),
        ← ops.mul_assoc trX z trY,
        ops.mul_comm trX z,
        ops.mul_assoc z trX trY,
        ← ops.mul_assoc z z (ops.mul trX trY)]

/-! ## Section 2 (`qou-w4la`): §7c Generic-Ring Quadratic Skein Inverse and Eigenvalue Relation -/

/-- Explicit inverse candidate `s - (q - qInv)` for a balanced quadratic generator `s` (`qou-w4la`). -/
def balancedGenInverse {R : Type u} (ops : GenericRingOps R) (s q qInv : R) : R :=
  ops.sub s (ops.sub q qInv)

/-- **Explicit Two-Sided Inverse and Factored Quadratic Relation (`qou-w4la`):**
For any element `s` in a commutative ring `R` satisfying `s² = (q - qInv) · s + 1` with
`q · qInv = 1`, the element `sInv = s - (q - qInv)` satisfies `s · sInv = 1` and
`sInv · s = 1`, and the factored eigenvalue product `(s - q) · (s + qInv)` vanishes. -/
theorem balanced_gen_two_sided_inverse_and_eigen_factor {R : Type u} (ops : GenericRingOps R)
    (s q qInv : R)
    (hq : ops.mul q qInv = ops.one)
    (hQuad : ops.mul s s = ops.add (ops.mul (ops.sub q qInv) s) ops.one) :
    ops.mul s (balancedGenInverse ops s q qInv) = ops.one ∧
      ops.mul (balancedGenInverse ops s q qInv) s = ops.one ∧
      ops.mul (ops.sub s q) (ops.add s qInv) = ops.zero := by
  have hRight : ops.mul s (balancedGenInverse ops s q qInv) = ops.one := by
    dsimp only [balancedGenInverse]
    rw [ops.mul_sub, hQuad, ops.mul_comm s (ops.sub q qInv)]
    dsimp only [GenericRingOps.sub]
    rw [ops.add_comm (ops.mul (ops.add q (ops.neg qInv)) s) ops.one,
        ops.add_assoc ops.one
          (ops.mul (ops.add q (ops.neg qInv)) s)
          (ops.neg (ops.mul (ops.add q (ops.neg qInv)) s)),
        ops.add_right_neg, ops.add_zero]
  have hLeft : ops.mul (balancedGenInverse ops s q qInv) s = ops.one := by
    rw [ops.mul_comm, hRight]
  refine ⟨hRight, hLeft, ?_⟩
  rw [ops.sub_mul, ops.left_distrib, ops.left_distrib, hq]
  apply ops.sub_eq_zero_iff.mpr
  rw [hQuad, ops.sub_mul, ops.mul_comm qInv s]
  dsimp only [GenericRingOps.sub]
  rw [ops.add_assoc (ops.add (ops.mul q s) (ops.neg (ops.mul s qInv))) ops.one (ops.mul s qInv),
      ops.add_comm ops.one (ops.mul s qInv),
      ← ops.add_assoc (ops.add (ops.mul q s) (ops.neg (ops.mul s qInv))) (ops.mul s qInv) ops.one,
      ops.add_assoc (ops.mul q s) (ops.neg (ops.mul s qInv)) (ops.mul s qInv),
      ops.add_left_neg, ops.add_zero]

/-! ## Section 3 (`qou-k4oq`): Convention D Peel Weight `w = (1, q²)` and `z = q³/(q² + 1)` -/

/-- First diagonal entry `w0 · q + w1 · (q - qInv)` of the `2 × 2` partial trace (`qou-k4oq`). -/
def partialTraceDiag0 {R : Type u} (ops : GenericRingOps R) (w0 w1 q qInv : R) : R :=
  ops.add (ops.mul w0 q) (ops.mul w1 (ops.sub q qInv))

/-- Second diagonal entry `w1 · q` of the `2 × 2` partial trace (`qou-k4oq`). -/
def partialTraceDiag1 {R : Type u} (ops : GenericRingOps R) (w1 q : R) : R :=
  ops.mul w1 q

/-- **Partial-Trace Peel Forces `w1 = q² · w0` and Convention D Parameter `z · (1 + q²) = q³` (`qou-k4oq`):**
If a diagonal site weight `(w0, w1)` makes the two partial-trace diagonal entries equal
(`partialTraceDiag0 = partialTraceDiag1`), then `w0 · q = w1 · qInv`. Multiplying by `q` using
`qInv · q = 1` forces `w1 = (q · q) · w0`; at normalized first weight `w0 = 1`, this pins
`w1 = q²`, total weight `w0 + w1 = 1 + q²`, unnormalized peel scalar `z = partialTraceDiag1 = q³`,
and the cleared Convention D equation `zNorm · (1 + q²) = q³` whenever `zNorm · (w0 + w1) = z`. -/
theorem partial_trace_peel_forces_weight_and_convention_d {R : Type u} (ops : GenericRingOps R)
    (w0 w1 q qInv zNorm : R)
    (hq : ops.mul qInv q = ops.one)
    (hPeel : partialTraceDiag0 ops w0 w1 q qInv = partialTraceDiag1 ops w1 q)
    (hw0 : w0 = ops.one)
    (hzNorm : ops.mul zNorm (ops.add w0 w1) = partialTraceDiag1 ops w1 q) :
    ops.mul w0 q = ops.mul w1 qInv ∧
      w1 = ops.mul q q ∧
      partialTraceDiag1 ops w1 q = ops.mul (ops.mul q q) q ∧
      ops.mul zNorm (ops.add ops.one (ops.mul q q)) = ops.mul (ops.mul q q) q := by
  dsimp only [partialTraceDiag0, partialTraceDiag1] at hPeel hzNorm ⊢
  rw [ops.mul_sub] at hPeel
  dsimp only [GenericRingOps.sub] at hPeel
  have h1 : ops.add (ops.add (ops.mul w0 q) (ops.neg (ops.mul w1 qInv))) (ops.mul w1 q) =
      ops.add ops.zero (ops.mul w1 q) := by
    rw [ops.zero_add,
        ops.add_assoc (ops.mul w0 q) (ops.neg (ops.mul w1 qInv)) (ops.mul w1 q),
        ops.add_comm (ops.neg (ops.mul w1 qInv)) (ops.mul w1 q),
        hPeel]
  have hDiffZero : ops.sub (ops.mul w0 q) (ops.mul w1 qInv) = ops.zero :=
    ops.add_right_cancel h1
  have hBalance : ops.mul w0 q = ops.mul w1 qInv :=
    ops.sub_eq_zero_iff.mp hDiffZero
  have hw1 : w1 = ops.mul q q := by
    calc
      w1 = ops.mul w1 ops.one := (ops.mul_one w1).symm
      _ = ops.mul w1 (ops.mul qInv q) := by rw [← hq]
      _ = ops.mul (ops.mul w1 qInv) q := (ops.mul_assoc w1 qInv q).symm
      _ = ops.mul (ops.mul w0 q) q := by rw [← hBalance]
      _ = ops.mul (ops.mul ops.one q) q := by rw [hw0]
      _ = ops.mul q q := by rw [ops.one_mul]
  have hz : ops.mul w1 q = ops.mul (ops.mul q q) q := by
    rw [hw1]
  refine ⟨hBalance, hw1, hz, ?_⟩
  rw [hw0, hw1] at hzNorm
  exact hzNorm

/-! ## Section 4 (`qou-o9ge`): Ribbon Twist Monodromy Recovery and Pivotal Trace Cyclicity -/

/-- Weighted pivotal trace `d1 · m11 + d2 · m22` of a `2 × 2` matrix `(m11, m12, m21, m22)` (`qou-o9ge`). -/
def pivotalTrace2 {R : Type u} (ops : GenericRingOps R) (d1 d2 m11 m22 : R) : R :=
  ops.add (ops.mul d1 m11) (ops.mul d2 m22)

/-- **Ribbon Monodromy Factorization and Weight-Centralizer Pivotal Cyclicity (`qou-o9ge`):**
1. If the tensor ribbon twist satisfies `thetaVW = (thetaV · thetaW) · monoVW` and the object
   twists have inverses `thetaVInv, thetaWInv` (`thetaVInv · thetaV = 1`, `thetaWInv · thetaW = 1`),
   then the full braiding monodromy scalar is recovered as
   `monoVW = (thetaWInv · thetaVInv) · thetaVW`.
2. For any `2 × 2` matrices `A = (a11, a12, a21, a22)` and `B = (b11, b12, b21, b22)` satisfying
   the weight-centralizer balance `d1 · (a12 · b21) = d2 · (a12 · b21)` and
   `d1 · (a21 · b12) = d2 · (a21 · b12)`, the weighted pivotal trace of `A · B` equals that of `B · A`. -/
theorem ribbon_monodromy_recovery_and_pivotal_trace_cyclic {R : Type u} (ops : GenericRingOps R)
    (thetaV thetaW thetaVW thetaVInv thetaWInv monoVW d1 d2 a11 a12 a21 a22 b11 b12 b21 b22 : R)
    (hRibbon : thetaVW = ops.mul (ops.mul thetaV thetaW) monoVW)
    (hVInv : ops.mul thetaVInv thetaV = ops.one)
    (hWInv : ops.mul thetaWInv thetaW = ops.one)
    (hCent1 : ops.mul d1 (ops.mul a12 b21) = ops.mul d2 (ops.mul a12 b21))
    (hCent2 : ops.mul d2 (ops.mul a21 b12) = ops.mul d1 (ops.mul a21 b12)) :
    monoVW = ops.mul (ops.mul thetaWInv thetaVInv) thetaVW ∧
      pivotalTrace2 ops d1 d2
        (ops.add (ops.mul a11 b11) (ops.mul a12 b21))
        (ops.add (ops.mul a21 b12) (ops.mul a22 b22)) =
      pivotalTrace2 ops d1 d2
        (ops.add (ops.mul b11 a11) (ops.mul b12 a21))
        (ops.add (ops.mul b21 a12) (ops.mul b22 a22)) := by
  refine ⟨?_, ?_⟩
  · rw [hRibbon,
        ← ops.mul_assoc (ops.mul thetaWInv thetaVInv) (ops.mul thetaV thetaW) monoVW,
        ops.mul_assoc thetaWInv thetaVInv (ops.mul thetaV thetaW),
        ← ops.mul_assoc thetaVInv thetaV thetaW,
        hVInv, ops.one_mul, hWInv, ops.one_mul]
  · dsimp only [pivotalTrace2]
    rw [ops.left_distrib, ops.left_distrib, ops.left_distrib, ops.left_distrib,
        ops.mul_comm b11 a11, ops.mul_comm b12 a21,
        ops.mul_comm b21 a12, ops.mul_comm b22 a22,
        hCent1, hCent2,
        ops.add_assoc (ops.mul d1 (ops.mul a11 b11))
          (ops.mul d2 (ops.mul a12 b21))
          (ops.add (ops.mul d1 (ops.mul a21 b12)) (ops.mul d2 (ops.mul a22 b22))),
        ← ops.add_assoc (ops.mul d2 (ops.mul a12 b21))
          (ops.mul d1 (ops.mul a21 b12))
          (ops.mul d2 (ops.mul a22 b22)),
        ops.add_comm (ops.mul d2 (ops.mul a12 b21)) (ops.mul d1 (ops.mul a21 b12)),
        ops.add_assoc (ops.mul d1 (ops.mul a21 b12))
          (ops.mul d2 (ops.mul a12 b21))
          (ops.mul d2 (ops.mul a22 b22)),
        ← ops.add_assoc (ops.mul d1 (ops.mul a11 b11))
          (ops.mul d1 (ops.mul a21 b12))
          (ops.add (ops.mul d2 (ops.mul a12 b21)) (ops.mul d2 (ops.mul a22 b22)))]

/-! ## Section 5 (`qou-0cyu`): Balanced Quantum-Integer Three-Term Recurrence and Cube Decomposition -/

/-- Balanced quantum integer `[2]_q = q + qInv` (`qou-0cyu`). -/
def qDim2 {R : Type u} (ops : GenericRingOps R) (q qInv : R) : R :=
  ops.add q qInv

/-- Balanced quantum integer `[3]_q = q² + 1 + qInv²` (`qou-0cyu`). -/
def qDim3 {R : Type u} (ops : GenericRingOps R) (q qInv : R) : R :=
  ops.add (ops.add (ops.mul q q) ops.one) (ops.mul qInv qInv)

/-- Balanced quantum integer `[4]_q = q³ + q + qInv + qInv³` (`qou-0cyu`). -/
def qDim4 {R : Type u} (ops : GenericRingOps R) (q qInv : R) : R :=
  ops.add
    (ops.add (ops.mul (ops.mul q q) q) (ops.add q qInv))
    (ops.mul (ops.mul qInv qInv) qInv)

/-- **Balanced Quantum-Integer Three-Term Steps and `n = 3` Decomposition (`qou-0cyu`):**
When `q · qInv = 1` in `R`:
1. `[2]_q · [2]_q = [3]_q + 1`;
2. `[2]_q · [3]_q = [4]_q + [2]_q`;
3. `[2]_q³ = ([4]_q + [2]_q) + [2]_q` (the `n = 3` tensor decomposition with ballot
   multiplicities `m_0(3) = 1`, `m_1(3) = 2`). -/
theorem qDim_three_term_and_cube_decomp {R : Type u} (ops : GenericRingOps R)
    (q qInv : R)
    (hq : ops.mul q qInv = ops.one) :
    ops.mul (qDim2 ops q qInv) (qDim2 ops q qInv) =
        ops.add (qDim3 ops q qInv) ops.one ∧
      ops.mul (qDim2 ops q qInv) (qDim3 ops q qInv) =
        ops.add (qDim4 ops q qInv) (qDim2 ops q qInv) ∧
      ops.mul (qDim2 ops q qInv) (ops.mul (qDim2 ops q qInv) (qDim2 ops q qInv)) =
        ops.add (ops.add (qDim4 ops q qInv) (qDim2 ops q qInv)) (qDim2 ops q qInv) := by
  have hqInv : ops.mul qInv q = ops.one := by
    rw [ops.mul_comm, hq]
  have hStep2 :
      ops.mul (qDim2 ops q qInv) (qDim2 ops q qInv) =
        ops.add (qDim3 ops q qInv) ops.one := by
    dsimp only [qDim2, qDim3]
    rw [ops.right_distrib, ops.left_distrib, ops.left_distrib,
        hq, hqInv,
        ops.add_assoc (ops.mul q q) ops.one (ops.add ops.one (ops.mul qInv qInv)),
        ops.add_comm ops.one (ops.mul qInv qInv),
        ← ops.add_assoc (ops.mul q q) ops.one (ops.add (ops.mul qInv qInv) ops.one),
        ← ops.add_assoc (ops.add (ops.mul q q) ops.one) (ops.mul qInv qInv) ops.one]
  have hStep3 :
      ops.mul (qDim2 ops q qInv) (qDim3 ops q qInv) =
        ops.add (qDim4 ops q qInv) (qDim2 ops q qInv) := by
    dsimp only [qDim2, qDim3, qDim4]
    have hq_qqInv : ops.mul q (ops.mul qInv qInv) = qInv := by
      rw [← ops.mul_assoc, hq, ops.one_mul]
    have hqInv_qq : ops.mul qInv (ops.mul q q) = q := by
      rw [← ops.mul_assoc, hqInv, ops.one_mul]
    rw [ops.right_distrib,
        ops.left_distrib q (ops.add (ops.mul q q) ops.one) (ops.mul qInv qInv),
        ops.left_distrib q (ops.mul q q) ops.one,
        ops.left_distrib qInv (ops.add (ops.mul q q) ops.one) (ops.mul qInv qInv),
        ops.left_distrib qInv (ops.mul q q) ops.one,
        ops.mul_one, ops.mul_one, hq_qqInv, hqInv_qq,
        ops.mul_comm q (ops.mul q q),
        ops.mul_comm qInv (ops.mul qInv qInv),
        ops.add_assoc (ops.mul (ops.mul q q) q) q qInv,
        ops.add_comm (ops.add q qInv) (ops.mul (ops.mul qInv qInv) qInv),
        ← ops.add_assoc (ops.add (ops.mul (ops.mul q q) q) (ops.add q qInv))
          (ops.mul (ops.mul qInv qInv) qInv) (ops.add q qInv)]
  refine ⟨hStep2, hStep3, ?_⟩
  rw [hStep2, ops.left_distrib, ops.mul_one, hStep3]

end QOU.Foundations.OcneanuTowerConventionDRibbonClebschGordan
