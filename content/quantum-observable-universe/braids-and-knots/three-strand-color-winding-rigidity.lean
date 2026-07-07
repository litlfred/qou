/-
  Rigidity of the three-strand color winding.

  On the 2-dimensional (2,1) Hoefsmit block of H_3(q), the uniform
  three-strand rotation σ₁σ₂ has trace -1 and determinant 1 for EVERY q
  with q⁴ ≠ 1; by Cayley–Hamilton it satisfies the ζ₃ quadratic
  M² = -M - 1 and hence cubes to the identity — the compact ζ₃
  (color/triality) winding of the (3,k) torus-link tower is exact and
  q-independent (rigid: it does not flow with the substrate modulus).

  The square root in the Hoefsmit off-diagonal is avoided by carrying the
  binding amplitude β as a variable constrained by its defining quadratic
  β² = a₂·a₋₂ + 1 (the corpus Hoefsmit convention), so the statement is
  over a generic field (§7c: no ℝ, no ordering, no √). A minimal
  self-contained 2×2 matrix carrier `M2` is used (entry-level algebra);
  no Mathlib matrix API is required.

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

variable {R : Type*} [Field R]

/-- The (2,1) Hoefsmit block of the uniform three-strand rotation
    `σ₁σ₂`: `σ₁ = diag(q, -q⁻¹)` times the axial-distance-2 Hoefsmit
    block for `σ₂` with binding amplitude `β`. Entries written out
    (the product of the diagonal and the symmetric block). -/
def threeStrandRotation (q β : R) : M2 R :=
  ⟨q * ((q - q⁻¹) / (1 - q ^ 4)), q * β,
   -q⁻¹ * β, -q⁻¹ * ((q - q⁻¹) / (1 - (q ^ 4)⁻¹))⟩

/-- The rotation is honestly the product `σ₁ · σ₂` of the diagonal lepton
    channel matrix and the symmetric Hoefsmit block. -/
theorem threeStrandRotation_eq_product (q β : R) :
    M2.mul ⟨q, 0, 0, -q⁻¹⟩
      ⟨(q - q⁻¹) / (1 - q ^ 4), β, β, (q - q⁻¹) / (1 - (q ^ 4)⁻¹)⟩
      = threeStrandRotation q β := by
  simp only [M2.mul, threeStrandRotation, M2.mk.injEq]
  exact ⟨by ring, by ring, by ring, by ring⟩

section NonzeroFacts

variable (q : R) (hq : q ≠ 0) (h4 : q ^ 4 ≠ 1)

include hq h4 in
/-- **Trace is `-1`, q-independently** (no β involved). -/
theorem threeStrand_trace (β : R) :
    (threeStrandRotation q β).a + (threeStrandRotation q β).d = -1 := by
  have hq4 : q ^ 4 ≠ 0 := pow_ne_zero 4 hq
  have hden : (1 : R) - q ^ 4 ≠ 0 := sub_ne_zero.mpr (Ne.symm h4)
  have hden' : q ^ 4 - 1 ≠ 0 := sub_ne_zero.mpr h4
  simp only [threeStrandRotation]
  field_simp
  ring

include hq h4 in
/-- **Determinant is `1`** — exactly the Hoefsmit constraint on β. -/
theorem threeStrand_det (β : R)
    (hβ : β ^ 2 = (q - q⁻¹) / (1 - (q ^ 4)⁻¹) * ((q - q⁻¹) / (1 - q ^ 4)) + 1) :
    (threeStrandRotation q β).a * (threeStrandRotation q β).d
      - (threeStrandRotation q β).b * (threeStrandRotation q β).c = 1 := by
  have hq4 : q ^ 4 ≠ 0 := pow_ne_zero 4 hq
  have hden : (1 : R) - q ^ 4 ≠ 0 := sub_ne_zero.mpr (Ne.symm h4)
  have hden' : q ^ 4 - 1 ≠ 0 := sub_ne_zero.mpr h4
  have hdeninv : (1 : R) - (q ^ 4)⁻¹ ≠ 0 := by
    intro h
    have h1 : (1 : R) = (q ^ 4)⁻¹ := sub_eq_zero.mp h
    exact h4 (by rw [← inv_inv (q ^ 4), ← h1, inv_one])
  simp only [threeStrandRotation]
  field_simp at hβ ⊢
  linear_combination hβ

include hq h4 in
/-- **Rigidity of the color winding (the cube identity).** The uniform
    three-strand rotation on the (2,1) block cubes to the identity for
    every `q` with `q⁴ ≠ 1` — exactly and q-independently: the ζ₃ color
    winding of the (3,k) torus tower is topological. -/
theorem threeStrand_cubes_to_one (β : R)
    (hβ : β ^ 2 = (q - q⁻¹) / (1 - (q ^ 4)⁻¹) * ((q - q⁻¹) / (1 - q ^ 4)) + 1) :
    M2.mul (threeStrandRotation q β)
      (M2.mul (threeStrandRotation q β) (threeStrandRotation q β))
      = M2.one :=
  M2.cube_of_trace_det _ (threeStrand_trace q hq h4 β)
    (threeStrand_det q hq h4 β hβ)

end NonzeroFacts

end QOU.BraidsAndKnots
