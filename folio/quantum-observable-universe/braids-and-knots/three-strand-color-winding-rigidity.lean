/-
  Rigidity of the three-strand color winding.

  On the 2-dimensional (2,1) Hoefsmit block of H_3(q), the uniform
  three-strand rotation σ₁σ₂ has trace -1 and determinant 1 for EVERY q
  with 1 - q² invertible; by Cayley–Hamilton it satisfies the ζ₃ quadratic
  M² = -M - 1 and hence cubes to the identity — the compact ζ₃
  (color/triality) winding of the (3,k) torus-link tower is exact and
  q-independent (rigid: it does not flow with the substrate modulus).

  Base ring (CLAUDE.md §7c). Everything is stated over a generic
  `{R : Type*} [CommRing R]` with the substrate modulus carried as a
  **unit** `q : Rˣ`, so `↑q⁻¹` is a `Units` coercion and no ring inverse
  or division appears. Two square roots / quotients are avoided:

  * the square root in the Hoefsmit off-diagonal, by carrying the
    binding amplitude β as a variable constrained by its defining
    quadratic `β² = a₋₂ · a₂ + 1` (the corpus Hoefsmit convention);
  * the axial-distance quotient `a₂ = h / (1 − q⁴)`, by carrying `a₂`
    as a variable constrained by its defining *relation*
    `a₂ · (1 − q⁴) = h` (`hoefsmitAxial_rel`-style hypothesis). The
    axial-distance −2 entry is then *derived*, `a₋₂ = −q⁴ · a₂`
    (`axialNeg`), and `axialNeg_rel` proves it satisfies its own
    defining relation `a₋₂ · (1 − q⁻⁴) = h` with no hypothesis beyond
    `↑q · ↑q⁻¹ = 1`. `axial_eq_div` records that over a field with
    `1 − q⁴ ≠ 0` the relation form is literally the old quotient.

  So the statement needs no ℝ, no ordering, no √ and no field. The only
  invertibility actually used is `1 − q²`, and only for the trace: at
  `q² = 1` the defining relation degenerates to `0 = 0` and constrains
  nothing, so the hypothesis is genuine, not an artefact. The
  determinant identity needs no hypothesis at all.

  A minimal self-contained 2×2 matrix carrier `M2` is used
  (entry-level algebra); no Mathlib matrix API is required.

  Machine-verified counterpart of the sympy probe
  computations/substrate/toroidal-level-selection-three-strand-probe.witness.json.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
-/

import Mathlib.Tactic

namespace QOU.BraidsAndKnots

/-- Minimal 2×2 matrix carrier (row-major entries). -/
structure M2 (R : Type*) where
  a : R
  b : R
  c : R
  d : R

namespace M2

variable {R : Type*} [CommRing R]

/-- 2×2 matrix product. -/
def mul (x y : M2 R) : M2 R :=
  ⟨x.a * y.a + x.b * y.c, x.a * y.b + x.b * y.d,
   x.c * y.a + x.d * y.c, x.c * y.b + x.d * y.d⟩

/-- Identity. -/
def one : M2 R := ⟨1, 0, 0, 1⟩

/-- **Cayley–Hamilton, ζ₃ case (quadratic).** A 2×2 matrix with trace
    `-1` and determinant `1` satisfies `M² = -M - 1` entrywise. Pure
    commutative-ring algebra. -/
theorem quadratic_of_trace_det (A : M2 R)
    (htr : A.a + A.d = -1) (hdet : A.a * A.d - A.b * A.c = 1) :
    mul A A = ⟨-A.a - 1, -A.b, -A.c, -A.d - 1⟩ := by
  simp only [mul, mk.injEq]
  exact ⟨by linear_combination A.a * htr - hdet,
         by linear_combination A.b * htr,
         by linear_combination A.c * htr,
         by linear_combination A.d * htr - hdet⟩

/-- **Cayley–Hamilton, ζ₃ case (cube).** A 2×2 matrix satisfying the ζ₃
    quadratic cubes to the identity. -/
theorem cube_of_quadratic (A : M2 R)
    (hquad : mul A A = ⟨-A.a - 1, -A.b, -A.c, -A.d - 1⟩) :
    mul A (mul A A) = one := by
  have ha := congrArg M2.a hquad
  have hb := congrArg M2.b hquad
  have hc := congrArg M2.c hquad
  have hd := congrArg M2.d hquad
  simp only [mul] at ha hb hc hd
  rw [hquad]
  simp only [mul, one, mk.injEq]
  exact ⟨by linear_combination -ha, by linear_combination -hb,
         by linear_combination -hc, by linear_combination -hd⟩

/-- ζ₃ rigidity, packaged: trace `-1` and determinant `1` force `M³ = 1`. -/
theorem cube_of_trace_det (A : M2 R)
    (htr : A.a + A.d = -1) (hdet : A.a * A.d - A.b * A.c = 1) :
    mul A (mul A A) = one :=
  cube_of_quadratic A (quadratic_of_trace_det A htr hdet)

end M2

variable {R : Type*} [CommRing R]

/-- Hecke amplitude `h = q − q⁻¹`. -/
def heckeH (q : Rˣ) : R := (q : R) - (↑q⁻¹ : R)

/-- The Hoefsmit axial-distance `−2` entry, derived from the `+2` entry:
    `a₋₂ = −q⁴ · a₂`. (Over a field this is
    `h/(1 − q⁻⁴) = −q⁴ · h/(1 − q⁴)`.) -/
def axialNeg (q : Rˣ) (a : R) : R := -((q : R) ^ 4) * a

/-- The derived entry satisfies its own Hoefsmit defining relation
    `a₋₂ · (1 − q⁻⁴) = h`, given only `a₂ · (1 − q⁴) = h`. No
    invertibility, no division. -/
theorem axialNeg_rel (q : Rˣ) (a : R)
    (ha : a * (1 - (q : R) ^ 4) = heckeH q) :
    axialNeg q a * (1 - (↑q⁻¹ : R) ^ 4) = heckeH q := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  unfold axialNeg
  linear_combination ha
    + (a * ((q : R) * (↑q⁻¹ : R) + 1) * (((q : R) * (↑q⁻¹ : R)) ^ 2 + 1)) * h

/-- The (2,1) Hoefsmit block of the uniform three-strand rotation
    `σ₁σ₂`: `σ₁ = diag(q, -q⁻¹)` times the axial-distance-2 Hoefsmit
    block for `σ₂` with axial entry `a` and binding amplitude `β`.
    Entries written out (the product of the diagonal and the symmetric
    block). -/
def threeStrandRotation (q : Rˣ) (a β : R) : M2 R :=
  ⟨(q : R) * a, (q : R) * β,
   -(↑q⁻¹ : R) * β, -(↑q⁻¹ : R) * axialNeg q a⟩

/-- The rotation is honestly the product `σ₁ · σ₂` of the diagonal lepton
    channel matrix and the symmetric Hoefsmit block. -/
theorem threeStrandRotation_eq_product (q : Rˣ) (a β : R) :
    M2.mul ⟨(q : R), 0, 0, -(↑q⁻¹ : R)⟩ ⟨a, β, β, axialNeg q a⟩
      = threeStrandRotation q a β := by
  simp only [M2.mul, threeStrandRotation, M2.mk.injEq]
  exact ⟨by ring, by ring, by ring, by ring⟩

section HoefsmitFacts

variable (q : Rˣ) (a β : R)

/-- **Trace is `-1`, q-independently** (no β involved).

    The only hypothesis is that `1 - q²` is invertible. It is genuine
    rather than technical: at `q² = 1` the Hoefsmit defining relation
    `a · (1 - q⁴) = h` degenerates to `0 = 0` and constrains `a` not at
    all, so the trace really is unconstrained there. -/
theorem threeStrand_trace
    (ha : a * (1 - (q : R) ^ 4) = heckeH q)
    (hu : IsUnit ((1 : R) - (q : R) ^ 2)) :
    (threeStrandRotation q a β).a + (threeStrandRotation q a β).d = -1 := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  obtain ⟨w, hw⟩ := hu
  rw [← Units.mul_right_inj w, hw]
  simp only [threeStrandRotation, axialNeg, heckeH] at *
  linear_combination (q : R) * ha
    - (a * (q : R) ^ 5 - a * (q : R) ^ 3 + 1) * h

/-- **Determinant is `1`** — exactly the Hoefsmit constraint on β.
    Needs no invertibility hypothesis at all: it is an identity in
    `ℤ[q, q⁻¹][a, β]` modulo the amplitude's defining quadratic. -/
theorem threeStrand_det
    (hβ : β ^ 2 = axialNeg q a * a + 1) :
    (threeStrandRotation q a β).a * (threeStrandRotation q a β).d
      - (threeStrandRotation q a β).b * (threeStrandRotation q a β).c = 1 := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  simp only [threeStrandRotation, axialNeg] at *
  linear_combination ((q : R) * (↑q⁻¹ : R)) * hβ + h

/-- **Rigidity of the color winding (the cube identity).** The uniform
    three-strand rotation on the (2,1) block cubes to the identity for
    every `q` with `1 - q²` invertible — exactly and q-independently:
    the ζ₃ color winding of the (3,k) torus tower is topological. -/
theorem threeStrand_cubes_to_one
    (ha : a * (1 - (q : R) ^ 4) = heckeH q)
    (hu : IsUnit ((1 : R) - (q : R) ^ 2))
    (hβ : β ^ 2 = axialNeg q a * a + 1) :
    M2.mul (threeStrandRotation q a β)
      (M2.mul (threeStrandRotation q a β) (threeStrandRotation q a β))
      = M2.one :=
  M2.cube_of_trace_det _ (threeStrand_trace q a β ha hu)
    (threeStrand_det q a β hβ)

end HoefsmitFacts

/-! ## Quotient presentation of the axial entry (a field only to divide)

The Hoefsmit seminormal form is usually written with the axial distance
in a denominator. That presentation — and only that presentation —
needs division. -/

section RatioForm

variable {K : Type*} [Field K]

/-- Over a field with `1 - q⁴ ≠ 0`, the relation `a · (1 − q⁴) = h`
    used above is literally the classical Hoefsmit quotient
    `a₂ = h / (1 − q⁴)`. Nothing is lost by carrying the relation. -/
theorem axial_eq_div (q : Kˣ) (a : K) (h4 : (1 : K) - (q : K) ^ 4 ≠ 0)
    (ha : a * (1 - (q : K) ^ 4) = heckeH q) :
    a = heckeH q / (1 - (q : K) ^ 4) := by
  rw [eq_div_iff h4]
  exact ha

end RatioForm

/-! ## Explicit Hoefsmit `H₃(q)` Generators (`σ₁`, `σ₂`), Hecke + Braid Relations, and Primitive `ζ₃` Eigenvalues -/

section HoefsmitGeneratorsAndEigenvalues

variable {R : Type*} [CommRing R]

/-- Scalar multiplication on `2 × 2` matrices `M2 R`. -/
def M2.smul (c : R) (A : M2 R) : M2 R :=
  ⟨c * A.a, c * A.b, c * A.c, c * A.d⟩

/-- Matrix addition on `2 × 2` matrices `M2 R`. -/
def M2.add (A B : M2 R) : M2 R :=
  ⟨A.a + B.a, A.b + B.b, A.c + B.c, A.d + B.d⟩

/-- Explicit Hoefsmit `(2,1)` generator `σ₁ = diag(q, -q⁻¹)`. -/
def hoefsmitSigma1 (q : Rˣ) : M2 R :=
  ⟨(q : R), 0, 0, -(↑q⁻¹ : R)⟩

/-- Explicit Hoefsmit `(2,1)` generator `σ₂ = !![a, β; β, a₋₂]`. -/
def hoefsmitSigma2 (q : Rˣ) (a β : R) : M2 R :=
  ⟨a, β, β, axialNeg q a⟩

/-- `threeStrandRotation q a β` is literally the matrix product
`hoefsmitSigma1 q * hoefsmitSigma2 q a β`. -/
theorem hoefsmitSigma1_mul_hoefsmitSigma2 (q : Rˣ) (a β : R) :
    M2.mul (hoefsmitSigma1 q) (hoefsmitSigma2 q a β) =
      threeStrandRotation q a β :=
  threeStrandRotation_eq_product q a β

/-- `hoefsmitSigma1 q` satisfies the Hecke quadratic relation `σ₁² = h · σ₁ + I₂`. -/
theorem hoefsmitSigma1_hecke_sq (q : Rˣ) :
    M2.mul (hoefsmitSigma1 q) (hoefsmitSigma1 q) =
      M2.add (M2.smul (heckeH q) (hoefsmitSigma1 q)) M2.one := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  simp only [hoefsmitSigma1, M2.mul, M2.add, M2.smul, M2.one, heckeH, M2.mk.injEq]
  exact ⟨by linear_combination h, by ring, by ring, by linear_combination h⟩

/-- `hoefsmitSigma2 q a β` satisfies the Hecke quadratic relation `σ₂² = h · σ₂ + I₂`
whenever `a + a₋₂ = h` (`htr2`) and `β² = a₋₂ · a + 1` (`hβ`). -/
theorem hoefsmitSigma2_hecke_sq (q : Rˣ) (a β : R)
    (htr2 : a + axialNeg q a = heckeH q)
    (hβ : β ^ 2 = axialNeg q a * a + 1) :
    M2.mul (hoefsmitSigma2 q a β) (hoefsmitSigma2 q a β) =
      M2.add (M2.smul (heckeH q) (hoefsmitSigma2 q a β)) M2.one := by
  simp only [hoefsmitSigma2, M2.mul, M2.add, M2.smul, M2.one, M2.mk.injEq]
  exact ⟨by linear_combination a * htr2 + hβ,
         by linear_combination β * htr2,
         by linear_combination β * htr2,
         by linear_combination (axialNeg q a) * htr2 + hβ⟩

/-- `hoefsmitSigma1 q` and `hoefsmitSigma2 q a β` satisfy the 3-strand Artin braid
relation `σ₁ σ₂ σ₁ = σ₂ σ₁ σ₂` whenever `(q : R) * a - (↑q⁻¹ : R) * axialNeg q a = -1`,
`(q : R) * a ^ 2 - (↑q⁻¹ : R) * β ^ 2 = (q : R) ^ 2 * a`, and
`(q : R) * β ^ 2 - (↑q⁻¹ : R) * (axialNeg q a) ^ 2 = (↑q⁻¹ : R) ^ 2 * axialNeg q a`. -/
theorem hoefsmitSigma_braid_relation (q : Rˣ) (a β : R)
    (htr12 : (q : R) * a - (↑q⁻¹ : R) * axialNeg q a = -1)
    (hdiag1 : (q : R) * a ^ 2 - (↑q⁻¹ : R) * β ^ 2 = (q : R) ^ 2 * a)
    (hdiag2 : (q : R) * β ^ 2 - (↑q⁻¹ : R) * (axialNeg q a) ^ 2 =
      (↑q⁻¹ : R) ^ 2 * axialNeg q a) :
    M2.mul (M2.mul (hoefsmitSigma1 q) (hoefsmitSigma2 q a β)) (hoefsmitSigma1 q) =
      M2.mul (M2.mul (hoefsmitSigma2 q a β) (hoefsmitSigma1 q)) (hoefsmitSigma2 q a β) := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  simp only [hoefsmitSigma1, hoefsmitSigma2, M2.mul, M2.mk.injEq]
  refine ⟨?_, ?_, ?_, ?_⟩
  · linear_combination -hdiag1
  · linear_combination -β * htr12 - β * h
  · linear_combination -β * htr12 - β * h
  · linear_combination -hdiag2

/-- **Primitive cube root of unity eigenvalues (`λ = e^{±2πi/3}`):**
Any eigenvalue `lam : R` satisfying the characteristic equation `lam² + lam + 1 = 0`
of `M = σ₁ σ₂` satisfies `lam³ = 1`, and over any domain with `(3 : R) ≠ 0` is a
*primitive* cube root of unity (`lam ≠ 1`). -/
theorem threeStrand_eigenvalue_primitive_cube_root (lam : R)
    (hchar : lam ^ 2 + lam + 1 = 0) :
    lam ^ 3 = 1 ∧ ([IsDomain R] → (3 : R) ≠ 0 → lam ≠ 1) := by
  refine ⟨by linear_combination (lam - 1) * hchar, ?_⟩
  intro _ h3 h1
  subst h1
  have h0 : (3 : R) = 0 := by linear_combination hchar
  exact h3 h0

end HoefsmitGeneratorsAndEigenvalues

end QOU.BraidsAndKnots
