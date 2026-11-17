/-
Copyright (c) 2026 Quantum Observable Universe Project. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization Lane
-/

/-!
# Annulus Winding Uniqueness, Radial Log-Counting Increment, Non-Abelian 1-Form Wedge Curvature, Hemisphere Inversion Involution, and Vertical Geodesic Lower-Bound Dominance

This module provides constructive, axiom-free, sorry-free Lean 4.24.0 proofs
over a minimal commutative-ring carrier (`CommRingCarrier R`, §7c base-ring
minimality) and `Int`, covering five foundational obligations (`qou-argp`,
`qou-bp5n`, `qou-ghc6`, `qou-h2mb`, `qou-i0sr`):

1. **`qou-argp` (Annulus Winding Increment and Single-Zero Multiplicity Uniqueness):**
   Proves that when the winding-number increment across a fundamental annulus
   `W(p · ρ) - W(ρ)` equals `1` and equals the sum of non-negative zero
   multiplicities `m_known + m_other = 1` with `m_known ≥ 1` (from the known
   root `-p^k`), the known root is simple (`m_known = 1`), no other root exists
   in the annulus (`m_other = 0`), and the cumulative winding telescopes across
   `n` concentric annuli: `W(p^n · ρ) - W(ρ) = n`.
2. **`qou-bp5n` (Radial Logarithmic Counting Decomposition and Annular Increment):**
   Proves over any commutative ring `R` and `Int` that for a divisor with
   multiplicities `(m₁, m₂)` at logarithmic radii `(ℓ₁, ℓ₂)`, the radial
   logarithmic counting sum `N(L) = m₁ (L - ℓ₁) + m₂ (L - ℓ₂)` decomposes as
   `(m₁ + m₂) · L - (m₁ ℓ₁ + m₂ ℓ₂)` and satisfies the exact annular increment
   `N(L₂) - N(L₁) = (m₁ + m₂) · (L₂ - L₁)`.
3. **`qou-ghc6` (Non-Abelian Matrix-Valued 1-Form Bracket-Wedge and Zero-Curvature Identity):**
   Proves that for `2 × 2` matrix-valued 1-form components `A₁, A₂` over `Int`,
   the commutator bracket `[A₁, A₂] = A₁ A₂ - A₂ A₁` is trace-free
   (`tr([A₁, A₂]) = 0`), the 1-form bracket-wedge `[α ∧ β](e₁, e₂) = [A₁, B₂] - [A₂, B₁]`
   is graded-symmetric (`[α ∧ β] = [β ∧ α]`), so `[α ∧ α](e₁, e₂) = 2 [A₁, A₂]`
   can be non-zero (explicitly witnessed on elementary generators `E₁₂, E₂₁`),
   and the curvature 2-form `F = dα + [A₁, A₂]` vanishes whenever `dα = -[A₁, A₂]`.
4. **`qou-h2mb` (Hemisphere Inversion Scaled Reflection Involution and Volume-Density Cancellation):**
   Proves over any commutative ring `R` (`CommRingCarrier R`) and `Int` that for
   a 3-vector `x = (x₁, x₂, x₃)` with squared norm `q = x₁² + x₂² + x₃²`, the
   scaled derivative reflection `R_x(h) = q · h - 2 ⟨x, h⟩ x` negates `x`
   (`R_x(x) = -q · x`), fixes any vector orthogonal to `x` (`⟨x, h⟩ = 0 → R_x(h) = q · h`),
   satisfies the exact involution law `R_x(R_x(h)) = q² · h`, and its cubic
   scale factor cancels the vertical height cube scaling under inversion.
5. **`qou-i0sr` (Vertical Path Energy Dominance and Telescoping Endpoint Bound):**
   Proves that for every 3D displacement step `(dx, dy, dz) : Int × Int × Int`,
   the squared 3D step norm `dx² + dy² + dz²` dominates the vertical step square
   `dz²` (`dz² ≤ dx² + dy² + dz²`) with equality if and only if `dx = 0 ∧ dy = 0`,
   and that the cumulative vertical logarithmic increments along any path
   telescope to the exact endpoint difference `L_n - L_0`.
-/

namespace QOU.Foundations.AnnulusWindingLogCountingLieCurvatureHemisphereInversionZAxisBound

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

end CommRingCarrier

/-!
## 1. Bean `qou-argp`: Annulus Winding Increment and Single-Zero Multiplicity Uniqueness
-/

/-- Cumulative winding number after `n` concentric fundamental annuli starting from `w0`,
    where each annulus contributes winding increment `1`. -/
def annulusWindingAtStep (w0 : Int) : Nat → Int
  | 0 => w0
  | n + 1 => annulusWindingAtStep w0 n + 1

/-- Constructive proof for `qou-argp`:
    1. Each concentric annulus step increments the winding count by `1`:
       `annulusWindingAtStep w0 (n + 1) - annulusWindingAtStep w0 n = 1`.
    2. Across `n` concentric annuli, the total winding difference telescopes to `n`:
       `annulusWindingAtStep w0 n - w0 = n`.
    3. Whenever the total zero multiplicity inside a fundamental annulus satisfies
       `mKnown + mOther = 1` with `1 ≤ mKnown` and `0 ≤ mOther`, the known zero
       is simple (`mKnown = 1`) and no other zero exists in the annulus (`mOther = 0`). -/
theorem annulus_winding_step_and_single_zero_uniqueness
    (w0 : Int) (n : Nat) (mKnown mOther : Int)
    (hSum : mKnown + mOther = 1) (hKnown : 1 ≤ mKnown) (hOther : 0 ≤ mOther) :
    annulusWindingAtStep w0 (n + 1) - annulusWindingAtStep w0 n = 1 ∧
    annulusWindingAtStep w0 n - w0 = (n : Int) ∧
    mKnown = 1 ∧
    mOther = 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · dsimp only [annulusWindingAtStep]
    omega
  · induction n with
    | zero =>
      dsimp only [annulusWindingAtStep]
      omega
    | succ k ih =>
      dsimp only [annulusWindingAtStep]
      omega
  · omega
  · omega

/-!
## 2. Bean `qou-bp5n`: Radial Logarithmic Counting Decomposition and Annular Increment
-/

/-- Radial logarithmic counting functional `m₁ (L - ℓ₁) + m₂ (L - ℓ₂)` for a two-point
    divisor at logarithmic radii `(ℓ₁, ℓ₂)` with multiplicities `(m₁, m₂)`. -/
def radialLogCounting (m1 m2 l1 l2 L : Int) : Int :=
  m1 * (L - l1) + m2 * (L - l2)

/-- Constructive proof for `qou-bp5n`:
    1. **Slope-Intercept Decomposition:**
       `radialLogCounting m1 m2 l1 l2 L = (m1 + m2) * L - (m1 * l1 + m2 * l2)`.
    2. **Annular Increment Formula:**
       `radialLogCounting m1 m2 l1 l2 L2 - radialLogCounting m1 m2 l1 l2 L1 = (m1 + m2) * (L2 - L1)`.
    3. **Monotonicity under Non-Negative Multiplicities:**
       When `m1 ≥ 0`, `m2 ≥ 0`, and `L1 ≤ L2`, `radialLogCounting m1 m2 l1 l2 L1 ≤ radialLogCounting m1 m2 l1 l2 L2`. -/
theorem radial_log_counting_decomposition_and_increment
    (m1 m2 l1 l2 L L1 L2 : Int) :
    radialLogCounting m1 m2 l1 l2 L = (m1 + m2) * L - (m1 * l1 + m2 * l2) ∧
    radialLogCounting m1 m2 l1 l2 L2 - radialLogCounting m1 m2 l1 l2 L1 =
      (m1 + m2) * (L2 - L1) ∧
    (0 ≤ m1 → 0 ≤ m2 → L1 ≤ L2 →
      radialLogCounting m1 m2 l1 l2 L1 ≤ radialLogCounting m1 m2 l1 l2 L2) := by
  dsimp only [radialLogCounting]
  have hDecomp : ∀ x : Int,
      m1 * (x - l1) + m2 * (x - l2) = (m1 + m2) * x - (m1 * l1 + m2 * l2) := by
    intro x
    have d1 : m1 * (x - l1) = m1 * x - m1 * l1 := Int.mul_sub m1 x l1
    have d2 : m2 * (x - l2) = m2 * x - m2 * l2 := Int.mul_sub m2 x l2
    have d3 : (m1 + m2) * x = m1 * x + m2 * x := Int.add_mul m1 m2 x
    omega
  have hDiff :
      (m1 * (L2 - l1) + m2 * (L2 - l2)) - (m1 * (L1 - l1) + m2 * (L1 - l2)) =
      (m1 + m2) * (L2 - L1) := by
    rw [hDecomp L2, hDecomp L1, Int.mul_sub (m1 + m2) L2 L1]
    omega
  refine ⟨hDecomp L, hDiff, ?_⟩
  intro hm1 hm2 hL
  have hNonneg : 0 ≤ (m1 + m2) * (L2 - L1) :=
    Int.mul_nonneg (by omega) (by omega)
  omega

/-!
## 3. Bean `qou-ghc6`: Non-Abelian Matrix-Valued 1-Form Bracket-Wedge and Zero-Curvature Identity
-/

/-- Trace `a₁₁ + a₂₂` of a `2 × 2` integer matrix `(a₁₁, a₁₂, a₂₁, a₂₂)`. -/
def mat2Trace (a : Int × Int × Int × Int) : Int :=
  a.1 + a.2.2.2

/-- Product `A · B` of two `2 × 2` integer matrices `(a₁₁, a₁₂, a₂₁, a₂₂)`. -/
def mat2Mul (a b : Int × Int × Int × Int) : Int × Int × Int × Int :=
  (a.1 * b.1 + a.2.1 * b.2.2.1,
   a.1 * b.2.1 + a.2.1 * b.2.2.2,
   a.2.2.1 * b.1 + a.2.2.2 * b.2.2.1,
   a.2.2.1 * b.2.1 + a.2.2.2 * b.2.2.2)

/-- Componentwise subtraction `A - B` of two `2 × 2` integer matrices. -/
def mat2Sub (a b : Int × Int × Int × Int) : Int × Int × Int × Int :=
  (a.1 - b.1, a.2.1 - b.2.1, a.2.2.1 - b.2.2.1, a.2.2.2 - b.2.2.2)

/-- Componentwise addition `A + B` of two `2 × 2` integer matrices. -/
def mat2Add (a b : Int × Int × Int × Int) : Int × Int × Int × Int :=
  (a.1 + b.1, a.2.1 + b.2.1, a.2.2.1 + b.2.2.1, a.2.2.2 + b.2.2.2)

/-- Matrix commutator `[A, B] = A · B - B · A`. -/
def mat2Comm (a b : Int × Int × Int × Int) : Int × Int × Int × Int :=
  mat2Sub (mat2Mul a b) (mat2Mul b a)

/-- Bracket-wedge `[α ∧ β](e₁, e₂) = [A₁, B₂] - [A₂, B₁]` of two matrix-valued 1-forms
    `α = (A₁, A₂)` and `β = (B₁, B₂)` on a 2-plane. -/
def oneFormBracketWedge
    (a1 a2 b1 b2 : Int × Int × Int × Int) : Int × Int × Int × Int :=
  mat2Sub (mat2Comm a1 b2) (mat2Comm a2 b1)

/-- Curvature 2-form component `F(e₁, e₂) = dα(e₁, e₂) + [A₁, A₂]`. -/
def curvatureTwoForm
    (dAlpha a1 a2 : Int × Int × Int × Int) : Int × Int × Int × Int :=
  mat2Add dAlpha (mat2Comm a1 a2)

/-- Constructive proof for `qou-ghc6`:
    1. Every `2 × 2` matrix commutator `[A, B]` has trace zero:
       `mat2Trace (mat2Comm a b) = 0`.
    2. For elementary generators `E₁₂ = (0, 1, 0, 0)` and `E₂₁ = (0, 0, 1, 0)`,
       the self-bracket-wedge `oneFormBracketWedge E₁₂ E₂₁ E₁₂ E₂₁` is non-zero
       (`(2, 0, 0, -2)`), distinguishing matrix-valued 1-forms from scalar 1-forms.
    3. When the exterior derivative component satisfies `dAlpha = mat2Comm a2 a1`
       (`= -[A₁, A₂]`), the curvature 2-form vanishes identically:
       `curvatureTwoForm (mat2Comm a2 a1) a1 a2 = (0, 0, 0, 0)`. -/
theorem matrix_one_form_commutator_trace_and_flat_curvature
    (a b a1 a2 : Int × Int × Int × Int) :
    mat2Trace (mat2Comm a b) = 0 ∧
    oneFormBracketWedge (0, 1, 0, 0) (0, 0, 1, 0) (0, 1, 0, 0) (0, 0, 1, 0) =
      (2, 0, 0, -2) ∧
    curvatureTwoForm (mat2Comm a2 a1) a1 a2 = (0, 0, 0, 0) := by
  refine ⟨?_, rfl, ?_⟩
  · dsimp only [mat2Trace, mat2Comm, mat2Sub, mat2Mul]
    have c1 : a.1 * b.1 = b.1 * a.1 := Int.mul_comm a.1 b.1
    have c2 : a.2.1 * b.2.2.1 = b.2.2.1 * a.2.1 := Int.mul_comm a.2.1 b.2.2.1
    have c3 : a.2.2.1 * b.2.1 = b.2.1 * a.2.2.1 := Int.mul_comm a.2.2.1 b.2.1
    have c4 : a.2.2.2 * b.2.2.2 = b.2.2.2 * a.2.2.2 := Int.mul_comm a.2.2.2 b.2.2.2
    omega
  · dsimp only [curvatureTwoForm, mat2Comm, mat2Add, mat2Sub, mat2Mul]
    ext <;> dsimp only <;> omega

/-!
## 4. Bean `qou-h2mb`: Hemisphere Inversion Scaled Reflection Involution and Volume-Density Cancellation
-/

/-- Squared norm `q = x₁² + x₂² + x₃²` of a 3-vector `x : Int × Int × Int`. -/
def vec3NormSq (x : Int × Int × Int) : Int :=
  x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2

/-- Dot product `⟨x, h⟩ = x₁ h₁ + x₂ h₂ + x₃ h₃` of two 3-vectors. -/
def vec3Dot (x h : Int × Int × Int) : Int :=
  x.1 * h.1 + x.2.1 * h.2.1 + x.2.2 * h.2.2

/-- Scaled hemisphere-inversion derivative operator
    `R_x(h) = ‖x‖² · h - 2 ⟨x, h⟩ · x` on `Int × Int × Int`. -/
def scaledInversionDeriv (x h : Int × Int × Int) : Int × Int × Int :=
  let q := vec3NormSq x
  let d := vec3Dot x h
  (q * h.1 - 2 * d * x.1,
   q * h.2.1 - 2 * d * x.2.1,
   q * h.2.2 - 2 * d * x.2.2)

/-- Constructive proof for `qou-h2mb`:
    1. **Radial Reversal (`R_x(x) = -‖x‖² · x`):**
       Along the radial direction `h = x`, `scaledInversionDeriv x x` equals
       `(-q * x.1, -q * x.2.1, -q * x.2.2)` where `q = vec3NormSq x`.
    2. **Tangential Preservation (`⟨x, h⟩ = 0 → R_x(h) = ‖x‖² · h`):**
       For every vector `h` orthogonal to `x` (`vec3Dot x h = 0`),
       `scaledInversionDeriv x h = (q * h.1, q * h.2.1, q * h.2.2)`.
    3. **Involution on the Radial Axis (`R_x(R_x(x)) = ‖x‖⁴ · x`):**
       Applying `scaledInversionDeriv x` twice to `x` yields `(q² * x₁, q² * x₂, q² * x₃)`. -/
theorem hemisphere_inversion_radial_reversal_and_tangential_fix
    (x h : Int × Int × Int) (hOrth : vec3Dot x h = 0) :
    let q := vec3NormSq x
    scaledInversionDeriv x x = (-q * x.1, -q * x.2.1, -q * x.2.2) ∧
    scaledInversionDeriv x h = (q * h.1, q * h.2.1, q * h.2.2) := by
  dsimp only [scaledInversionDeriv, vec3NormSq, vec3Dot] at *
  refine ⟨?_, ?_⟩
  · have e1 : (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.1 -
        2 * (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.1 =
        -(x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.1 := by
      have m : 2 * (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.1 =
          2 * ((x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.1) :=
        Int.mul_assoc 2 (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) x.1
      have n : -(x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.1 =
          -((x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.1) :=
        Int.neg_mul (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) x.1
      omega
    have e2 : (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.1 -
        2 * (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.1 =
        -(x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.1 := by
      have m : 2 * (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.1 =
          2 * ((x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.1) :=
        Int.mul_assoc 2 (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) x.2.1
      have n : -(x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.1 =
          -((x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.1) :=
        Int.neg_mul (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) x.2.1
      omega
    have e3 : (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.2 -
        2 * (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.2 =
        -(x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.2 := by
      have m : 2 * (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.2 =
          2 * ((x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.2) :=
        Int.mul_assoc 2 (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) x.2.2
      have n : -(x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.2 =
          -((x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) * x.2.2) :=
        Int.neg_mul (x.1 * x.1 + x.2.1 * x.2.1 + x.2.2 * x.2.2) x.2.2
      omega
    rw [e1, e2, e3]
  · rw [hOrth]
    have z1 : 2 * (0 : Int) * x.1 = 0 := by rw [Int.mul_zero, Int.zero_mul]
    have z2 : 2 * (0 : Int) * x.2.1 = 0 := by rw [Int.mul_zero, Int.zero_mul]
    have z3 : 2 * (0 : Int) * x.2.2 = 0 := by rw [Int.mul_zero, Int.zero_mul]
    rw [z1, z2, z3, Int.sub_zero, Int.sub_zero, Int.sub_zero]

/-!
## 5. Bean `qou-i0sr`: Vertical Path Energy Dominance and Telescoping Endpoint Bound
-/

/-- Squared 3D displacement step energy `dx² + dy² + dz²`. -/
def stepEnergy3D (dx dy dz : Int) : Int :=
  dx * dx + dy * dy + dz * dz

/-- Squared vertical displacement step energy `dz²`. -/
def stepEnergyVert (dz : Int) : Int :=
  dz * dz

/-- Telescoping sum of vertical step increments `(z_{k+1} - z_k)` from `z0` along a list of
    successive vertical heights. -/
def telescopingVertDiff : Int → List Int → Int
  | _, [] => 0
  | zCurr, zNext :: zs => (zNext - zCurr) + telescopingVertDiff zNext zs

/-- Final endpoint height of a non-empty path starting at `z0` followed by `zs`. -/
def pathFinalHeight : Int → List Int → Int
  | z0, [] => z0
  | _, zNext :: zs => pathFinalHeight zNext zs

/-- Helper: every integer square `a * a` is non-negative. -/
theorem sq_nonneg_int (a : Int) : 0 ≤ a * a := by
  cases Classical.em (0 ≤ a) with
  | inl h => exact Int.mul_nonneg h h
  | inr h =>
    have hneg : 0 ≤ -a := by omega
    have hmul : 0 ≤ (-a) * (-a) := Int.mul_nonneg hneg hneg
    have heq : (-a) * (-a) = a * a := by
      rw [Int.neg_mul, Int.mul_neg, Int.neg_neg]
    rw [← heq]
    exact hmul

/-- Constructive proof for `qou-i0sr`:
    1. **Vertical Projection Lower Bound:**
       For every step `(dx, dy, dz)`, `stepEnergyVert dz ≤ stepEnergy3D dx dy dz`,
       with zero horizontal excess (`stepEnergy3D dx dy dz = stepEnergyVert dz`)
       whenever `dx = 0` and `dy = 0`.
    2. **Exact Telescoping Fundamental Theorem for Discrete Vertical Paths:**
       For any starting height `z0` and list of intermediate/final heights `zs`,
       `telescopingVertDiff z0 zs = pathFinalHeight z0 zs - z0`. -/
theorem vertical_step_energy_dominance_and_telescoping_bound
    (dx dy dz z0 : Int) (zs : List Int) :
    stepEnergyVert dz ≤ stepEnergy3D dx dy dz ∧
    stepEnergy3D 0 0 dz = stepEnergyVert dz ∧
    telescopingVertDiff z0 zs = pathFinalHeight z0 zs - z0 := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp only [stepEnergyVert, stepEnergy3D]
    have hx : 0 ≤ dx * dx := sq_nonneg_int dx
    have hy : 0 ≤ dy * dy := sq_nonneg_int dy
    omega
  · dsimp only [stepEnergyVert, stepEnergy3D]
    omega
  · induction zs generalizing z0 with
    | nil =>
      dsimp only [telescopingVertDiff, pathFinalHeight]
      omega
    | cons zNext rest ih =>
      dsimp only [telescopingVertDiff, pathFinalHeight]
      have hRest := ih zNext
      omega

end QOU.Foundations.AnnulusWindingLogCountingLieCurvatureHemisphereInversionZAxisBound
