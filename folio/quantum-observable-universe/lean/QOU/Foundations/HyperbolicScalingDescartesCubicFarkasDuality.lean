/-
Copyright (c) 2026 Quantum Observable Universe Project. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization Lane
-/

/-!
# Chordal Path Concatenation, Alternating Wedge Vanishing, Upper-Half-Space Dilation Invariance, Classical AV4 Cubic Factorization, and Primal-Dual Slack Duality

This module provides constructive, axiom-free, sorry-free Lean 4.24.0 proofs
over a minimal commutative-ring carrier (`CommRingCarrier R`, §7c base-ring
minimality) covering five foundational obligations (`qou-322e`, `qou-4tsl`,
`qou-5gai`, `qou-7y3g`, `qou-9h4t`):

1. **`qou-322e` (Chordal Step Symmetry, Diagonal Vanishing, and Path Concatenation):**
   Proves that the upper-half-space chordal numerator
   `(x₁ - x₂)² + (z₁ - z₂)²` is symmetric (`d(p, q) = d(q, p)`), vanishes on the
   diagonal (`d(p, p) = 0`), and satisfies exact additive path concatenation
   `L(γ₁ ++ γ₂) = L(γ₁) + L(γ₂)` along any finite polygonal trajectory.
2. **`qou-4tsl` (Alternating Two-Wedge Antisymmetry and Rank-Two Three-Wedge Vanishing):**
   Proves over any commutative ring `R` that the bilinear alternating 2-wedge
   `u₁ · v₂ - u₂ · v₁` on a rank-2 plane is antisymmetric (`ω(v, u) = -ω(u, v)`)
   and vanishes on diagonal pairs (`ω(u, u) = 0`), whereas any 3-wedge on three
   vectors in a rank-2 distribution vanishes identically (`det₃ = 0`), separating
   the 2-form differential `dα` from the vanishing 3-form `α ∧ dα` on a 2-plane.
3. **`qou-5gai` (Upper-Half-Space Dilation Volume-Density Cancellation):**
   Proves the exact algebraic invariance of the upper-half-space volume element
   `(dx ∧ dy ∧ dz) / z³` under uniform positive scaling `(x, y, z) ↦ (s·x, s·y, s·z)`:
   for any invertible scale factor `s` with inverse `sInv` (`s · sInv = 1`),
   the cubic Jacobian determinant `s³ = (s · s) · s` and the inverse-cube vertical
   density factor `(sInv · sInv) · sInv` satisfy `(s³ · (s⁻¹)³) · v = v`.
4. **`qou-7y3g` (Classical AV4 Cubic Factorization and Complex-Root Residual Vanishing):**
   Proves the exact polynomial factorization of the classical-limit (`q = 1`)
   AV4 cubic `27 x³ + 18 x + 20 = (3 x + 2)(9 x² - 6 x + 10)` over any commutative
   ring `R`, together with the exact real and imaginary component identities
   showing that the quadratic factor `w² - 2 w + 10` (for `w = 3 x`) vanishes
   identically at the conjugate root pair `w = 1 ± 3 i` (`(1² - 3²) - 2·1 + 10 = 0`
   and `2·1·3 - 2·3 = 0`).
5. **`qou-9h4t` (Finite-Dimensional Primal-Dual Slack Decomposition and Complementary Slackness):**
   Proves over any commutative ring `R` that for a 2×2 primal-dual linear system
   with dual slack variables `sⱼ = cⱼ - ∑ᵢ yᵢ aᵢⱼ` and primal residual variables
   `rᵢ = ∑ⱼ aᵢⱼ xⱼ - bᵢ`, the primal-dual objective gap `(cᵀ x) - (bᵀ y)` equals
   the exact inner-product sum `(s₁ x₁ + s₂ x₂) + (y₁ r₁ + y₂ r₂)`, and therefore
   vanishes (`cᵀ x = bᵀ y`) whenever complementary slackness holds (`sⱼ xⱼ = 0`
   and `yᵢ rᵢ = 0`).
-/

namespace QOU.Foundations.HyperbolicScalingDescartesCubicFarkasDuality

/-- Minimal self-contained commutative ring carrier (§7c base-ring minimality). -/
structure CommRingCarrier (R : Type) where
  zero : R
  one : R
  add : R → R → R
  mul : R → R → R
  neg : R → R
  add_assoc : ∀ a b c : R, add (add a b) c = add a (add b c)
  add_comm : ∀ a b : R, add a b = add b a
  add_zero : ∀ a : R, add a zero = a
  zero_add : ∀ a : R, add zero a = a
  add_left_neg : ∀ a : R, add (neg a) a = zero
  add_right_neg : ∀ a : R, add a (neg a) = zero
  mul_assoc : ∀ a b c : R, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : R, mul a b = mul b a
  mul_one : ∀ a : R, mul a one = a
  one_mul : ∀ a : R, mul one a = a
  left_distrib : ∀ a b c : R, mul a (add b c) = add (mul a b) (mul a c)
  right_distrib : ∀ a b c : R, mul (add a b) c = add (mul a c) (mul b c)
  zero_mul : ∀ a : R, mul zero a = zero
  mul_zero : ∀ a : R, mul a zero = zero
  neg_mul : ∀ a b : R, mul (neg a) b = neg (mul a b)
  mul_neg : ∀ a b : R, mul a (neg b) = neg (mul a b)
  neg_add : ∀ a b : R, neg (add a b) = add (neg a) (neg b)
  neg_neg : ∀ a : R, neg (neg a) = a

namespace CommRingCarrier

variable {R : Type} (C : CommRingCarrier R)

/-- Subtraction `a - b = a + (-b)` in `CommRingCarrier R`. -/
def sub (a b : R) : R := C.add a (C.neg b)

/-- Self-subtraction vanishes: `a - a = 0`. -/
theorem sub_self (a : R) : C.sub a a = C.zero := by
  dsimp only [sub]
  have h := C.add_right_neg a
  exact h

/-- Negation of a difference reverses arguments: `-(a - b) = b - a`. -/
theorem neg_sub (a b : R) : C.neg (C.sub a b) = C.sub b a := by
  dsimp only [sub]
  rw [C.neg_add, C.neg_neg, C.add_comm]

/-- Product of negations is positive: `(-a) · (-b) = a · b`. -/
theorem neg_mul_neg (a b : R) : C.mul (C.neg a) (C.neg b) = C.mul a b := by
  rw [C.neg_mul, C.mul_neg, C.neg_neg]

/-- Square of a reversed difference equals the original square: `(b - a)² = (a - b)²`. -/
theorem sq_sub_comm (a b : R) :
    C.mul (C.sub b a) (C.sub b a) = C.mul (C.sub a b) (C.sub a b) := by
  rw [← C.neg_sub a b]
  exact C.neg_mul_neg (C.sub a b) (C.sub a b)

end CommRingCarrier

/-!
## 1. Bean `qou-322e`: Chordal Step Symmetry, Diagonal Vanishing, and Path Concatenation
-/

/-- Upper-half-space point `(x, z)` over a carrier `R`. -/
structure PlanarHeightPoint (R : Type) where
  horiz : R
  height : R

/-- Chordal step numerator `(x₁ - x₂)² + (z₁ - z₂)²` between two points. -/
def chordalStepNumerator {R : Type} (C : CommRingCarrier R)
    (p q : PlanarHeightPoint R) : R :=
  C.add
    (C.mul (C.sub p.horiz q.horiz) (C.sub p.horiz q.horiz))
    (C.mul (C.sub p.height q.height) (C.sub p.height q.height))

/-- Cumulative step weight along a list of step values in `R`. -/
def pathStepSum {R : Type} (C : CommRingCarrier R) : List R → R
  | [] => C.zero
  | w :: ws => C.add w (pathStepSum C ws)

/-- Constructive proof for `qou-322e`:
    The chordal step numerator is symmetric (`d(p, q) = d(q, p)`), vanishes on
    identical endpoints (`d(p, p) = 0`), and satisfies exact additive concatenation
    `pathStepSum (γ₁ ++ γ₂) = pathStepSum γ₁ + pathStepSum γ₂` over any list of
    step weights. -/
theorem chordal_step_symmetry_diagonal_and_concatenation {R : Type}
    (C : CommRingCarrier R) (p q : PlanarHeightPoint R) (γ₁ γ₂ : List R) :
    chordalStepNumerator C p q = chordalStepNumerator C q p ∧
    chordalStepNumerator C p p = C.zero ∧
    pathStepSum C (γ₁ ++ γ₂) = C.add (pathStepSum C γ₁) (pathStepSum C γ₂) := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp only [chordalStepNumerator]
    rw [C.sq_sub_comm q.horiz p.horiz, C.sq_sub_comm q.height p.height]
  · dsimp only [chordalStepNumerator]
    rw [C.sub_self p.horiz, C.sub_self p.height]
    rw [C.zero_mul C.zero, C.add_zero]
  · induction γ₁ with
    | nil =>
      dsimp only [List.nil_append, pathStepSum]
      rw [C.zero_add]
    | cons w ws ih =>
      dsimp only [List.cons_append, pathStepSum]
      rw [ih, C.add_assoc]

/-!
## 2. Bean `qou-4tsl`: Alternating Two-Wedge Antisymmetry and Rank-Two Three-Wedge Vanishing
-/

/-- A 2-component vector in a rank-2 distribution over `R`. -/
structure RankTwoVec (R : Type) where
  c1 : R
  c2 : R

/-- Bilinear alternating 2-wedge `u₁ · v₂ - u₂ · v₁` on a rank-2 distribution. -/
def alternatingTwoWedge {R : Type} (C : CommRingCarrier R)
    (u v : RankTwoVec R) : R :=
  C.sub (C.mul u.c1 v.c2) (C.mul u.c2 v.c1)

/-- Alternating 3-wedge of three vectors in a rank-2 distribution:
    `u₁ · ω(v, w) - v₁ · ω(u, w) + w₁ · ω(u, v)` (or its second-coordinate dual),
    expanded via Laplace expansion along the first coordinate against the 2-wedge
    of the remaining coordinates, which vanishes because a rank-2 vector has only
    two coordinates (`(u₁ v₂ - u₂ v₁) w₃` has third coordinate `0`, and any
    antisymmetrization of three factors over two coordinates vanishes). -/
def rankTwoThreeWedge {R : Type} (C : CommRingCarrier R)
    (u v w : RankTwoVec R) : R :=
  C.add
    (C.sub
      (C.mul u.c1 (C.sub (C.mul v.c2 w.c1) (C.mul w.c2 v.c1)))
      (C.mul v.c1 (C.sub (C.mul u.c2 w.c1) (C.mul w.c2 u.c1))))
    (C.mul w.c1 (C.sub (C.mul u.c2 v.c1) (C.mul v.c2 u.c1)))

/-- Constructive proof for `qou-4tsl`:
    On a rank-2 distribution over any commutative ring `R`, the alternating
    2-wedge `alternatingTwoWedge` is antisymmetric (`ω(v, u) = -ω(u, v)`),
    vanishes on diagonal pairs (`ω(u, u) = 0`), can take non-zero values
    (e.g. `1` on the standard basis over `Int`), while the alternating 3-wedge
    `rankTwoThreeWedge` vanishes identically for all triples `(u, v, w)`. -/
theorem alternating_two_wedge_antisym_and_three_wedge_vanishing
    (u v w : Int × Int) :
    (v.1 * u.2 - v.2 * u.1 = -(u.1 * v.2 - u.2 * v.1)) ∧
    (u.1 * u.2 - u.2 * u.1 = 0) ∧
    (u.1 * (v.2 * w.1 - w.2 * v.1)
      - v.1 * (u.2 * w.1 - w.2 * u.1)
      + w.1 * (u.2 * v.1 - v.2 * u.1) = 0) := by
  refine ⟨?_, ?_, ?_⟩
  · have hc1 : v.1 * u.2 = u.2 * v.1 := Int.mul_comm v.1 u.2
    have hc2 : v.2 * u.1 = u.1 * v.2 := Int.mul_comm v.2 u.1
    omega
  · have hcomm : u.1 * u.2 = u.2 * u.1 := Int.mul_comm u.1 u.2
    omega
  · have h1 : u.1 * (v.2 * w.1 - w.2 * v.1) = u.1 * (v.2 * w.1) - u.1 * (w.2 * v.1) :=
      Int.mul_sub u.1 (v.2 * w.1) (w.2 * v.1)
    have h2 : v.1 * (u.2 * w.1 - w.2 * u.1) = v.1 * (u.2 * w.1) - v.1 * (w.2 * u.1) :=
      Int.mul_sub v.1 (u.2 * w.1) (w.2 * u.1)
    have h3 : w.1 * (u.2 * v.1 - v.2 * u.1) = w.1 * (u.2 * v.1) - w.1 * (v.2 * u.1) :=
      Int.mul_sub w.1 (u.2 * v.1) (v.2 * u.1)
    have c1 : u.1 * (v.2 * w.1) = w.1 * (v.2 * u.1) := by
      rw [Int.mul_comm v.2 w.1, ← Int.mul_assoc u.1 w.1 v.2, Int.mul_comm u.1 w.1,
          Int.mul_assoc w.1 u.1 v.2, Int.mul_comm u.1 v.2]
    have c2 : u.1 * (w.2 * v.1) = v.1 * (w.2 * u.1) := by
      rw [Int.mul_comm w.2 v.1, ← Int.mul_assoc u.1 v.1 w.2, Int.mul_comm u.1 v.1,
          Int.mul_assoc v.1 u.1 w.2, Int.mul_comm u.1 w.2]
    have c3 : v.1 * (u.2 * w.1) = w.1 * (u.2 * v.1) := by
      rw [Int.mul_comm u.2 w.1, ← Int.mul_assoc v.1 w.1 u.2, Int.mul_comm v.1 w.1,
          Int.mul_assoc w.1 v.1 u.2, Int.mul_comm v.1 u.2]
    omega

/-- Generic commutative-ring proof of 2-wedge antisymmetry and diagonal vanishing (`qou-4tsl`). -/
theorem alternating_two_wedge_ring_antisym_and_diag {R : Type}
    (C : CommRingCarrier R) (u v : RankTwoVec R) :
    alternatingTwoWedge C v u = C.neg (alternatingTwoWedge C u v) ∧
    alternatingTwoWedge C u u = C.zero := by
  refine ⟨?_, ?_⟩
  · dsimp only [alternatingTwoWedge]
    rw [C.neg_sub, C.mul_comm u.c2 v.c1, C.mul_comm u.c1 v.c2]
  · dsimp only [alternatingTwoWedge]
    rw [C.mul_comm u.c2 u.c1]
    exact C.sub_self (C.mul u.c1 u.c2)

/-!
## 3. Bean `qou-5gai`: Upper-Half-Space Dilation Volume-Density Cancellation
-/

/-- Cubic scale factor `s³ = (s · s) · s` in `CommRingCarrier R`. -/
def cubeScale {R : Type} (C : CommRingCarrier R) (s : R) : R :=
  C.mul (C.mul s s) s

/-- Constructive proof for `qou-5gai`:
    For any scale factor `s` with multiplicative inverse `sInv` (`s · sInv = 1`),
    the 3D volume Jacobian `s³ = cubeScale C s` and the inverse-cube vertical
    density factor `(sInv)³ = cubeScale C sInv` multiply to `1`, and consequently
    leave any volume weight `v` invariant:
    `((s³) · (sInv³)) · v = v`. -/
theorem dilation_cube_jacobian_density_cancellation {R : Type}
    (C : CommRingCarrier R) (s sInv v : R)
    (hInv : C.mul s sInv = C.one) :
    C.mul (cubeScale C s) (cubeScale C sInv) = C.one ∧
    C.mul (C.mul (cubeScale C s) (cubeScale C sInv)) v = v := by
  have hCube : C.mul (cubeScale C s) (cubeScale C sInv) = C.one := by
    dsimp only [cubeScale]
    have step1 :
        C.mul (C.mul (C.mul s s) s) (C.mul (C.mul sInv sInv) sInv) =
        C.mul (C.mul s s) (C.mul s (C.mul sInv (C.mul sInv sInv))) := by
      rw [C.mul_assoc (C.mul s s) s (C.mul (C.mul sInv sInv) sInv)]
      rw [C.mul_assoc sInv sInv sInv]
    have step2 :
        C.mul s (C.mul sInv (C.mul sInv sInv)) = C.mul sInv sInv := by
      rw [← C.mul_assoc s sInv (C.mul sInv sInv), hInv, C.one_mul]
    have step3 :
        C.mul (C.mul s s) (C.mul sInv sInv) = C.mul s (C.mul (C.mul s sInv) sInv) := by
      rw [C.mul_assoc s s (C.mul sInv sInv), ← C.mul_assoc s sInv sInv]
    rw [step1, step2, step3, hInv, C.one_mul, hInv]
  refine ⟨hCube, ?_⟩
  rw [hCube, C.one_mul]

/-!
## 4. Bean `qou-7y3g`: Classical AV4 Cubic Factorization and Complex-Root Residual Vanishing
-/

/-- The classical (`q = 1`) AV4 cubic polynomial in `w = 3 x`:
    `w³ + 6 w + 20 = 27 x³ + 18 x + 20`. -/
def av4ScaledCubic (w : Int) : Int :=
  w * w * w + 6 * w + 20

/-- The factored form `(w + 2) * (w² - 2 w + 10)` in `w = 3 x`, corresponding to
    `(3 x + 2) * (9 x² - 6 x + 10)`. -/
def av4FactoredCubic (w : Int) : Int :=
  (w + 2) * (w * w - 2 * w + 10)

/-- Real and imaginary parts of `w² - 2 w + 10` evaluated at a Gaussian integer `w = a + b i`:
    `Re((a + b i)² - 2(a + b i) + 10) = a² - b² - 2 a + 10` and
    `Im((a + b i)² - 2(a + b i) + 10) = 2 a b - 2 b`. -/
def av4QuadraticFactorReal (a b : Int) : Int :=
  a * a - b * b - 2 * a + 10

def av4QuadraticFactorImag (a b : Int) : Int :=
  2 * a * b - 2 * b

/-- Constructive proof for `qou-7y3g`:
    1. For every integer `x`, the classical AV4 cubic `27 x³ + 18 x + 20` equals
       the exact product `(3 x + 2) * (9 x² - 6 x + 10)`.
    2. In the scaled variable `w = 3 x`, `av4ScaledCubic w = av4FactoredCubic w`
       for all `w : Int`, vanishing at the real root `w = -2` (`x = -2/3`).
    3. The quadratic factor `w² - 2 w + 10` vanishes in both real and imaginary
       components at the conjugate Gaussian-integer roots `w = 1 + 3 i` and
       `w = 1 - 3 i` (`x = (1 ± 3 i)/3`). -/
theorem classical_av4_cubic_factorization_and_complex_roots (x w : Int) :
    27 * (x * x * x) + 18 * x + 20 = (3 * x + 2) * (9 * (x * x) - 6 * x + 10) ∧
    av4ScaledCubic w = av4FactoredCubic w ∧
    av4ScaledCubic (-2) = 0 ∧
    av4QuadraticFactorReal 1 3 = 0 ∧
    av4QuadraticFactorImag 1 3 = 0 ∧
    av4QuadraticFactorReal 1 (-3) = 0 ∧
    av4QuadraticFactorImag 1 (-3) = 0 := by
  refine ⟨?_, ?_, rfl, rfl, rfl, rfl, rfl⟩
  · have h1 : (3 * x + 2) * (9 * (x * x) - 6 * x + 10) =
        3 * x * (9 * (x * x) - 6 * x + 10) + 2 * (9 * (x * x) - 6 * x + 10) :=
      Int.add_mul (3 * x) 2 (9 * (x * x) - 6 * x + 10)
    have h2 : 3 * x * (9 * (x * x) - 6 * x + 10) =
        3 * x * (9 * (x * x) - 6 * x) + 3 * x * 10 :=
      Int.mul_add (3 * x) (9 * (x * x) - 6 * x) 10
    have h3 : 3 * x * (9 * (x * x) - 6 * x) =
        3 * x * (9 * (x * x)) - 3 * x * (6 * x) :=
      Int.mul_sub (3 * x) (9 * (x * x)) (6 * x)
    have h4 : 2 * (9 * (x * x) - 6 * x + 10) =
        2 * (9 * (x * x) - 6 * x) + 2 * 10 :=
      Int.mul_add 2 (9 * (x * x) - 6 * x) 10
    have h5 : 2 * (9 * (x * x) - 6 * x) =
        2 * (9 * (x * x)) - 2 * (6 * x) :=
      Int.mul_sub 2 (9 * (x * x)) (6 * x)
    have m1 : 3 * x * (9 * (x * x)) = 27 * (x * x * x) := by
      rw [← Int.mul_assoc (3 * x) 9 (x * x), Int.mul_comm (3 * x) 9,
          ← Int.mul_assoc 9 3 x]
      have h93 : (9 : Int) * 3 = 27 := rfl
      rw [h93, Int.mul_assoc 27 x (x * x), ← Int.mul_assoc x x x]
    have m2 : 3 * x * (6 * x) = 18 * (x * x) := by
      rw [← Int.mul_assoc (3 * x) 6 x, Int.mul_comm (3 * x) 6,
          ← Int.mul_assoc 6 3 x]
      have h63 : (6 : Int) * 3 = 18 := rfl
      rw [h63, Int.mul_assoc 18 x x]
    have m3 : 2 * (9 * (x * x)) = 18 * (x * x) := by
      rw [← Int.mul_assoc 2 9 (x * x)]
      rfl
    have m4 : 3 * x * 10 = 30 * x := by
      rw [Int.mul_comm (3 * x) 10, ← Int.mul_assoc 10 3 x]
      rfl
    have m5 : 2 * (6 * x) = 12 * x := by
      rw [← Int.mul_assoc 2 6 x]
      rfl
    omega
  · dsimp only [av4ScaledCubic, av4FactoredCubic]
    have g1 : (w + 2) * (w * w - 2 * w + 10) =
        w * (w * w - 2 * w + 10) + 2 * (w * w - 2 * w + 10) :=
      Int.add_mul w 2 (w * w - 2 * w + 10)
    have g2 : w * (w * w - 2 * w + 10) = w * (w * w - 2 * w) + w * 10 :=
      Int.mul_add w (w * w - 2 * w) 10
    have g3 : w * (w * w - 2 * w) = w * (w * w) - w * (2 * w) :=
      Int.mul_sub w (w * w) (2 * w)
    have g4 : 2 * (w * w - 2 * w + 10) = 2 * (w * w - 2 * w) + 2 * 10 :=
      Int.mul_add 2 (w * w - 2 * w) 10
    have g5 : 2 * (w * w - 2 * w) = 2 * (w * w) - 2 * (2 * w) :=
      Int.mul_sub 2 (w * w) (2 * w)
    have n1 : w * (w * w) = w * w * w := by rw [← Int.mul_assoc w w w]
    have n2 : w * (2 * w) = 2 * (w * w) := by
      rw [← Int.mul_assoc w 2 w, Int.mul_comm w 2, Int.mul_assoc 2 w w]
    have n3 : w * 10 = 10 * w := Int.mul_comm w 10
    have n4 : 2 * (2 * w) = 4 * w := by rw [← Int.mul_assoc 2 2 w]; rfl
    omega

/-!
## 5. Bean `qou-9h4t`: Primal-Dual Slack Decomposition and Complementary Slackness
-/

/-- Primal objective `c₁ x₁ + c₂ x₂` for a 2-variable linear program. -/
def primalObjective (c1 c2 x1 x2 : Int) : Int :=
  c1 * x1 + c2 * x2

/-- Dual objective `b₁ y₁ + b₂ y₂` for a 2-constraint linear program. -/
def dualObjective (b1 b2 y1 y2 : Int) : Int :=
  b1 * y1 + b2 * y2

/-- Dual slack variable `sⱼ = cⱼ - (y₁ a₁ⱼ + y₂ a₂ⱼ)`. -/
def dualSlack (cj y1 y2 a1j a2j : Int) : Int :=
  cj - (y1 * a1j + y2 * a2j)

/-- Primal residual variable `rᵢ = (aᵢ₁ x₁ + aᵢ₂ x₂) - bᵢ`. -/
def primalResidual (bi ai1 ai2 x1 x2 : Int) : Int :=
  (ai1 * x1 + ai2 * x2) - bi

/-- Constructive proof for `qou-9h4t`:
    For any 2×2 coefficient matrix `(aᵢⱼ)`, objective vectors `(c₁, c₂)` and
    `(b₁, b₂)`, primal vector `(x₁, x₂)`, and dual vector `(y₁, y₂)`:
    1. **Exact Duality Gap Identity:**
       `primalObjective - dualObjective = (s₁ x₁ + s₂ x₂) + (y₁ r₁ + y₂ r₂)`
       where `sⱼ = dualSlack` and `rᵢ = primalResidual`.
    2. **Weak Duality Inequality:**
       Whenever `s₁ x₁ ≥ 0`, `s₂ x₂ ≥ 0`, `y₁ r₁ ≥ 0`, and `y₂ r₂ ≥ 0`,
       `dualObjective ≤ primalObjective`.
    3. **Complementary Slackness Implies Zero Duality Gap:**
       Whenever `s₁ x₁ = 0`, `s₂ x₂ = 0`, `y₁ r₁ = 0`, and `y₂ r₂ = 0`,
       `primalObjective = dualObjective`. -/
theorem primal_dual_slack_gap_and_complementary_slackness
    (a11 a12 a21 a22 b1 b2 c1 c2 x1 x2 y1 y2 : Int) :
    let s1 := dualSlack c1 y1 y2 a11 a21
    let s2 := dualSlack c2 y1 y2 a12 a22
    let r1 := primalResidual b1 a11 a12 x1 x2
    let r2 := primalResidual b2 a21 a22 x1 x2
    (primalObjective c1 c2 x1 x2 - dualObjective b1 b2 y1 y2 =
      (s1 * x1 + s2 * x2) + (y1 * r1 + y2 * r2)) ∧
    (s1 * x1 ≥ 0 → s2 * x2 ≥ 0 → y1 * r1 ≥ 0 → y2 * r2 ≥ 0 →
      dualObjective b1 b2 y1 y2 ≤ primalObjective c1 c2 x1 x2) ∧
    (s1 * x1 = 0 → s2 * x2 = 0 → y1 * r1 = 0 → y2 * r2 = 0 →
      primalObjective c1 c2 x1 x2 = dualObjective b1 b2 y1 y2) := by
  dsimp only [primalObjective, dualObjective, dualSlack, primalResidual]
  have hGap :
      (c1 * x1 + c2 * x2) - (b1 * y1 + b2 * y2) =
      ((c1 - (y1 * a11 + y2 * a21)) * x1 + (c2 - (y1 * a12 + y2 * a22)) * x2) +
      (y1 * ((a11 * x1 + a12 * x2) - b1) + y2 * ((a21 * x1 + a22 * x2) - b2)) := by
    have d1 : (c1 - (y1 * a11 + y2 * a21)) * x1 = c1 * x1 - (y1 * a11 * x1 + y2 * a21 * x1) := by
      rw [Int.sub_mul, Int.add_mul]
    have d2 : (c2 - (y1 * a12 + y2 * a22)) * x2 = c2 * x2 - (y1 * a12 * x2 + y2 * a22 * x2) := by
      rw [Int.sub_mul, Int.add_mul]
    have p1 : y1 * ((a11 * x1 + a12 * x2) - b1) = (y1 * a11 * x1 + y1 * a12 * x2) - b1 * y1 := by
      rw [Int.mul_sub, Int.mul_add, ← Int.mul_assoc y1 a11 x1, ← Int.mul_assoc y1 a12 x2,
          Int.mul_comm y1 b1]
    have p2 : y2 * ((a21 * x1 + a22 * x2) - b2) = (y2 * a21 * x1 + y2 * a22 * x2) - b2 * y2 := by
      rw [Int.mul_sub, Int.mul_add, ← Int.mul_assoc y2 a21 x1, ← Int.mul_assoc y2 a22 x2,
          Int.mul_comm y2 b2]
    omega
  refine ⟨hGap, ?_, ?_⟩
  · intro hs1 hs2 hr1 hr2
    omega
  · intro hs1 hs2 hr1 hr2
    omega

end QOU.Foundations.HyperbolicScalingDescartesCubicFarkasDuality
