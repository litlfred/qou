/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

namespace QOU.Foundations.NormedDifferentialFormGaussianLogNormalCanonicalProductContactReebZAxisUniqueness

/-!
# Normed-Space Differential Forms, Shifted Quadratic Moment Exponents, Genus-One Canonical Factors, Contact Characteristic Pairing, and Vertical Geodesic Uniqueness

This module provides self-contained, zero-`sorry` Lean 4 formalizations for five
foundational mathematical infrastructure items under `qou-c8p8` / `qou-rtxm`:

1. **`qou-ipsl`**: Second-order plane jet exterior derivative nilpotence (`d ∘ d = 0`)
   under mixed-partial symmetry and non-abelian curvature 2-form antisymmetry /
   abelian additivity.
2. **`qou-jbo8`**: Shifted quadratic moment exponent completion of the square and
   triangular exponent second-difference identity (`k(k - 1)L`).
3. **`qou-n4pv`**: Genus-one truncated canonical factor cubic deficit decomposition
   and strict positivity for nonzero arguments, together with two-point pinning of
   linear exponential factors.
4. **`qou-vspi`**: Three-dimensional contact 1-form characteristic vector normalization,
   kernel plane nondegeneracy, and horizontal lift pinning.
5. **`qou-xidi`**: Upper-half-space vertical speed saturation horizontal-velocity
   collapse (`vx = 0 ∧ vy = 0`) and constant-speed vertical log-height interpolation
   uniqueness.
-/

-- ============================================================================
-- Section 1 (qou-ipsl): Exterior Derivative Nilpotence and Curvature 2-Form
-- ============================================================================

/-- Second-order jet of a vector-valued 0-form on a plane with mixed partial
derivatives `fxy` and `fyx`. -/
structure PlaneSecondJet where
  f0 : Int
  fx : Int
  fy : Int
  fxx : Int
  fxy : Int
  fyx : Int
  fyy : Int
  deriving Repr, DecidableEq

/-- Exterior 2-form coefficient of `d(df)` on a plane jet: `∂_x ∂_y f - ∂_y ∂_x f`. -/
def planeExteriorTwoFormCoeff (J : PlaneSecondJet) : Int :=
  J.fxy - J.fyx

/-- Curvature 2-form component `F_{xy} = ∂_x A_y - ∂_y A_x + [A_x, A_y]` on a normed plane. -/
def planeCurvatureTwoForm (dxAy dyAx bracketAxAy : Int) : Int :=
  dxAy - dyAx + bracketAxAy

/-- **Theorem 1a (`qou-ipsl`)**: For any second-order plane jet with symmetric mixed
partials (`fxy = fyx`), the iterated exterior derivative `d(df)` vanishes identically,
and the difference between two jets' `d(df)` coefficients equals the difference of
their mixed-partial asymmetries. -/
theorem symmetric_mixed_partials_exterior_dd_zero
    (J K : PlaneSecondJet) (hSym : J.fxy = J.fyx) :
    planeExteriorTwoFormCoeff J = 0 ∧
      planeExteriorTwoFormCoeff K - planeExteriorTwoFormCoeff J = K.fxy - K.fyx := by
  dsimp only [planeExteriorTwoFormCoeff]
  omega

/-- **Theorem 1b (`qou-ipsl`)**: The non-abelian plane curvature 2-form is antisymmetric
under exchanging `x ↔ y` and negating the commutator bracket (`[A_y, A_x] = -[A_x, A_y]`),
and restricts to an additive linear operator when the commutator vanishes. -/
theorem plane_curvature_two_form_antisymmetry_and_additive_reduction
    (dxAy dyAx dxBy dyBx bracketAxAy : Int) :
    planeCurvatureTwoForm dxAy dyAx bracketAxAy +
        planeCurvatureTwoForm dyAx dxAy (-bracketAxAy) = 0 ∧
      planeCurvatureTwoForm (dxAy + dxBy) (dyAx + dyBx) 0 =
        planeCurvatureTwoForm dxAy dyAx 0 + planeCurvatureTwoForm dxBy dyBx 0 := by
  dsimp only [planeCurvatureTwoForm]
  omega

-- ============================================================================
-- Section 2 (qou-jbo8): Shifted Quadratic Moment Exponents & Completion of Square
-- ============================================================================

/-- Twice the quadratic moment generating exponent `2 * (k * μ + k² * σ² / 2)`
evaluated at mean `μ = -L / 2` and variance `σ² = L`: `k * (-L) + k² * L`. -/
def shiftedMomentExponentTwice (L k : Int) : Int :=
  k * (-L) + k * k * L

/-- Twice the triangular moment exponent `L * k * (k - 1)`. -/
def triangularMomentExponentTwice (L k : Int) : Int :=
  L * (k * (k - 1))

/-- **Theorem 2a (`qou-jbo8`)**: At mean `-L/2` and variance `L`, the quadratic moment
generating exponent equals the triangular exponent `L * k * (k - 1)`, whose second
central difference in `k` is the constant curvature `2 * L`. -/
theorem shifted_moment_exponent_eq_triangular_and_second_diff
    (L k : Int) :
    shiftedMomentExponentTwice L k = triangularMomentExponentTwice L k ∧
      triangularMomentExponentTwice L (k + 1) +
        triangularMomentExponentTwice L (k - 1) -
        2 * triangularMomentExponentTwice L k = 2 * L := by
  dsimp only [shiftedMomentExponentTwice, triangularMomentExponentTwice]
  refine ⟨?_, ?_⟩
  · calc
      k * (-L) + k * k * L = -(k * L) + k * (k * L) := by
        rw [Int.mul_neg, Int.mul_assoc k k L]
      _ = (k - 1) * (k * L) := by
        rw [Int.sub_mul, Int.one_mul]
        omega
      _ = L * (k * (k - 1)) := by
        rw [← Int.mul_assoc (k - 1) k L, Int.mul_comm (k - 1) k, Int.mul_comm (k * (k - 1)) L]
  · have h1 : (k + 1) * (k + 1 - 1) = k * k + k := by
      have s1 : k + 1 - 1 = k := by omega
      rw [s1, Int.add_mul, Int.one_mul]
    have h2 : (k - 1) * (k - 1 - 1) = k * k - 3 * k + 2 := by
      have s2 : k - 1 - 1 = k - 2 := by omega
      rw [s2, Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.one_mul]
      omega
    have h3 : k * (k - 1) = k * k - k := by
      rw [Int.mul_sub, Int.mul_one]
    rw [h1, h2, h3]
    rw [Int.mul_add L (k * k) k, Int.mul_add L (k * k - 3 * k) 2,
        Int.mul_sub L (k * k) (3 * k), Int.mul_sub L (k * k) k,
        ← Int.mul_assoc L 3 k, Int.mul_comm L 3, Int.mul_assoc 3 L k,
        Int.mul_comm L (k * k), Int.mul_comm L k, Int.mul_comm L 2]
    omega

/-- **Theorem 2b (`qou-jbo8`)**: Completion of the square for the shifted quadratic
density exponent: `(x - (μ + k σ²))² + 2 k σ² (x - μ) - k² σ⁴ = (x - μ)²`. -/
theorem shifted_quadratic_density_completion_of_square
    (x mu k sigma2 : Int) :
    (x - (mu + k * sigma2)) * (x - (mu + k * sigma2)) +
      (2 * k * sigma2 * (x - mu) - (k * sigma2) * (k * sigma2)) =
      (x - mu) * (x - mu) := by
  have hSub : x - (mu + k * sigma2) = (x - mu) - k * sigma2 := by omega
  rw [hSub]
  have e1 : ((x - mu) - k * sigma2) * ((x - mu) - k * sigma2) =
      (x - mu) * ((x - mu) - k * sigma2) - (k * sigma2) * ((x - mu) - k * sigma2) :=
    Int.sub_mul (x - mu) (k * sigma2) ((x - mu) - k * sigma2)
  have e2 : (x - mu) * ((x - mu) - k * sigma2) =
      (x - mu) * (x - mu) - (x - mu) * (k * sigma2) :=
    Int.mul_sub (x - mu) (x - mu) (k * sigma2)
  have e3 : (k * sigma2) * ((x - mu) - k * sigma2) =
      (k * sigma2) * (x - mu) - (k * sigma2) * (k * sigma2) :=
    Int.mul_sub (k * sigma2) (x - mu) (k * sigma2)
  have e4 : (x - mu) * (k * sigma2) = (k * sigma2) * (x - mu) :=
    Int.mul_comm (x - mu) (k * sigma2)
  have e5 : 2 * k * sigma2 * (x - mu) = 2 * ((k * sigma2) * (x - mu)) := by
    rw [Int.mul_assoc 2 k sigma2, Int.mul_assoc 2 (k * sigma2) (x - mu)]
  rw [e1, e2, e3, e4, e5]
  omega

-- ============================================================================
-- Section 3 (qou-n4pv): Genus-One Truncated Primary Factor & Linear Exponent Pinning
-- ============================================================================

/-- Six times the cubic Taylor truncation of the genus-one primary factor
`(1 - u) * (1 + u + u²/2 + u³/6)`: `(1 - u) * (6 + 6u + 3u² + u³)`. -/
def genusOneClearedTruncatedFactor (u : Int) : Int :=
  (1 - u) * (6 + 6 * u + 3 * (u * u) + u * (u * u))

private theorem sq_nonneg_int_r63 (x : Int) : 0 ≤ x * x := by
  rcases Int.lt_trichotomy x 0 with hlt | rfl | hgt
  · have hpos : 0 < -x := by omega
    have hmul : 0 ≤ (-x) * (-x) := Int.mul_nonneg (Int.le_of_lt hpos) (Int.le_of_lt hpos)
    rw [Int.neg_mul_neg] at hmul
    exact hmul
  · omega
  · exact Int.mul_nonneg (Int.le_of_lt hgt) (Int.le_of_lt hgt)

/-- **Theorem 3a (`qou-n4pv`)**: The deficit `6 - genusOneClearedTruncatedFactor u`
factors as `u² * (2 + (u + 1)²)`, is non-negative for all `u : Int`, and vanishes
if and only if `u = 0`. -/
theorem genus_one_truncated_factor_deficit_positivity (u : Int) :
    6 - genusOneClearedTruncatedFactor u = (u * u) * (2 + (u + 1) * (u + 1)) ∧
      0 ≤ 6 - genusOneClearedTruncatedFactor u ∧
      (6 - genusOneClearedTruncatedFactor u = 0 → u = 0) := by
  dsimp only [genusOneClearedTruncatedFactor]
  have hFactor :
      6 - (1 - u) * (6 + 6 * u + 3 * (u * u) + u * (u * u)) =
        (u * u) * (2 + (u + 1) * (u + 1)) := by
    have e1 : (1 - u) * (6 + 6 * u + 3 * (u * u) + u * (u * u)) =
        1 * (6 + 6 * u + 3 * (u * u) + u * (u * u)) -
          u * (6 + 6 * u + 3 * (u * u) + u * (u * u)) :=
      Int.sub_mul 1 u (6 + 6 * u + 3 * (u * u) + u * (u * u))
    have e2 : u * (6 + 6 * u + 3 * (u * u) + u * (u * u)) =
        u * (6 + 6 * u + 3 * (u * u)) + u * (u * (u * u)) :=
      Int.mul_add u (6 + 6 * u + 3 * (u * u)) (u * (u * u))
    have e3 : u * (6 + 6 * u + 3 * (u * u)) = u * (6 + 6 * u) + u * (3 * (u * u)) :=
      Int.mul_add u (6 + 6 * u) (3 * (u * u))
    have e4 : u * (6 + 6 * u) = u * 6 + u * (6 * u) :=
      Int.mul_add u 6 (6 * u)
    have e5 : u * (6 * u) = 6 * (u * u) := by
      rw [← Int.mul_assoc u 6 u, Int.mul_comm u 6, Int.mul_assoc 6 u u]
    have e6 : u * (3 * (u * u)) = 3 * (u * (u * u)) := by
      rw [← Int.mul_assoc u 3 (u * u), Int.mul_comm u 3, Int.mul_assoc 3 u (u * u)]
    have e7 : u * (u * (u * u)) = (u * u) * (u * u) := by
      rw [← Int.mul_assoc u u (u * u)]
    have e8 : (u + 1) * (u + 1) = (u * u) + 2 * u + 1 := by
      rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.one_mul, Int.mul_one]
      omega
    have e9 : (u * u) * (2 + ((u * u) + 2 * u + 1)) = (u * u) * (3 + 2 * u + (u * u)) := by
      have s9 : 2 + ((u * u) + 2 * u + 1) = 3 + 2 * u + (u * u) := by omega
      rw [s9]
    have e10 : (u * u) * (3 + 2 * u + (u * u)) =
        (u * u) * (3 + 2 * u) + (u * u) * (u * u) :=
      Int.mul_add (u * u) (3 + 2 * u) (u * u)
    have e11 : (u * u) * (3 + 2 * u) = (u * u) * 3 + (u * u) * (2 * u) :=
      Int.mul_add (u * u) 3 (2 * u)
    have e12 : (u * u) * (2 * u) = 2 * (u * (u * u)) := by
      rw [← Int.mul_assoc (u * u) 2 u, Int.mul_comm (u * u) 2,
          Int.mul_assoc 2 (u * u) u, Int.mul_comm (u * u) u]
    have e13 : u * 6 = 6 * u := Int.mul_comm u 6
    have e14 : (u * u) * 3 = 3 * (u * u) := Int.mul_comm (u * u) 3
    rw [e1, Int.one_mul, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]
    omega
  have hSqU : 0 ≤ u * u := sq_nonneg_int_r63 u
  have hSqU1 : 0 ≤ (u + 1) * (u + 1) := sq_nonneg_int_r63 (u + 1)
  have hPosFactor : 0 < 2 + (u + 1) * (u + 1) := by omega
  refine ⟨hFactor, ?_, ?_⟩
  · rw [hFactor]
    exact Int.mul_nonneg hSqU (Int.le_of_lt hPosFactor)
  · intro hZero
    rw [hFactor] at hZero
    rcases Int.mul_eq_zero.mp hZero with hU2 | hRight
    · rcases Int.mul_eq_zero.mp hU2 with hU | hU
      · exact hU
      · exact hU
    · omega

/-- **Theorem 3b (`qou-n4pv`)**: Two order-one linear exponential factors `a₁ z + b₁`
and `a₂ z + b₂` that agree at `z = 0` and `z = 1` have identical coefficients
`a₁ = a₂` and `b₁ = b₂`. -/
theorem order_one_linear_exponent_two_point_pinning
    (a1 b1 a2 b2 : Int)
    (hZero : a1 * 0 + b1 = a2 * 0 + b2)
    (hOne : a1 * 1 + b1 = a2 * 1 + b2) :
    a1 = a2 ∧ b1 = b2 := by
  omega

-- ============================================================================
-- Section 4 (qou-vspi): Contact 1-Form Characteristic Pairing & Kernel Plane
-- ============================================================================

/-- Standard 3D contact 1-form `α_y(dx, dz) = dz - y * dx`. -/
def contactOneForm3 (y dx dz : Int) : Int :=
  dz - y * dx

/-- Exterior 2-form `dα((dx₁, dy₁), (dx₂, dy₂)) = dx₁ * dy₂ - dy₁ * dx₂`. -/
def contactTwoForm3 (dx1 dy1 dx2 dy2 : Int) : Int :=
  dx1 * dy2 - dy1 * dx2

/-- **Theorem 4a (`qou-vspi`)**: The characteristic vector `(0, 0, 1)` satisfies
`α(0, 1) = 1` and annihilates `dα`, while the contact hyperplane basis vectors
`(1, 0, y)` and `(0, 1, 0)` lie in `ker α` and pair to `1` under `dα`. -/
theorem contact_characteristic_vector_and_kernel_symplectic_pairing
    (y dx dy : Int) :
    contactOneForm3 y 0 1 = 1 ∧
      contactTwoForm3 0 0 dx dy = 0 ∧
      contactOneForm3 y 1 y = 0 ∧
      contactOneForm3 y 0 0 = 0 ∧
      contactTwoForm3 1 0 0 1 = 1 := by
  dsimp only [contactOneForm3, contactTwoForm3]
  omega

/-- **Theorem 4b (`qou-vspi`)**: Every vertical displacement `dz` decomposes uniquely
into its characteristic component `α_y(dx, dz)` plus the horizontal lift height
`dx * y` in the contact kernel hyperplane `ker α_y`. -/
theorem contact_tangent_splitting_into_characteristic_and_kernel
    (y dx dz : Int) :
    dz = contactOneForm3 y dx dz + dx * y ∧
      (contactOneForm3 y dx dz = 0 ↔ dz = y * dx) := by
  dsimp only [contactOneForm3]
  refine ⟨?_, ?_⟩
  · rw [Int.mul_comm dx y]
    omega
  · constructor <;> intro h <;> omega

-- ============================================================================
-- Section 5 (qou-xidi): Vertical Speed Saturation & Constant-Speed Uniqueness
-- ============================================================================

/-- Squared tangent speed `vx² + vy² + vz²` in 3D upper half-space. -/
def upperHalfSpaceSquaredSpeed (vx vy vz : Int) : Int :=
  vx * vx + vy * vy + vz * vz

/-- **Theorem 5a (`qou-xidi`)**: Saturation of the vertical speed lower bound
`vx² + vy² + vz² = vz²` forces both horizontal velocity components to vanish (`vx = 0 ∧ vy = 0`). -/
theorem vertical_speed_saturation_collapses_horizontal_velocity
    (vx vy vz : Int)
    (hSat : upperHalfSpaceSquaredSpeed vx vy vz = vz * vz) :
    vx = 0 ∧ vy = 0 := by
  dsimp only [upperHalfSpaceSquaredSpeed] at hSat
  have hSumZero : vx * vx + vy * vy = 0 := by omega
  have hVx2 : 0 ≤ vx * vx := sq_nonneg_int_r63 vx
  have hVy2 : 0 ≤ vy * vy := sq_nonneg_int_r63 vy
  have hVxZero : vx * vx = 0 := by omega
  have hVyZero : vy * vy = 0 := by omega
  refine ⟨?_, ?_⟩
  · rcases Int.mul_eq_zero.mp hVxZero with h | h <;> exact h
  · rcases Int.mul_eq_zero.mp hVyZero with h | h <;> exact h

/-- **Theorem 5b (`qou-xidi`)**: Any two 3-step constant-speed vertical log-height
profiles `(a, u₁, u₂, b)` and `(a, v₁, v₂, b)` between endpoints `a` and `b`
satisfy `3 * u₁ = 2 * a + b`, `3 * u₂ = a + 2 * b`, and coincide pointwise (`u₁ = v₁ ∧ u₂ = v₂`). -/
theorem constant_speed_vertical_profile_three_step_uniqueness
    (a b u1 u2 v1 v2 : Int)
    (hu1 : u1 - a = u2 - u1)
    (hu2 : u2 - u1 = b - u2)
    (hv1 : v1 - a = v2 - v1)
    (hv2 : v2 - v1 = b - v2) :
    3 * u1 = 2 * a + b ∧
      3 * u2 = a + 2 * b ∧
      u1 = v1 ∧
      u2 = v2 := by
  omega

end QOU.Foundations.NormedDifferentialFormGaussianLogNormalCanonicalProductContactReebZAxisUniqueness
