/-!
# QOU.LocalizedKnot — Knot localized at a point on the projective line

A localized knot is a pair (p, K) where p is a categorical point of
the projective line P(V) = G/T and K is a knot type.  This is the
fundamental unit of matter in the QOU framework.

## References

- [manuscript] §3 Lifting of Quantum Torsion
-/

import Mathlib.Data.Real.Basic
import QOU.KnotTheory

namespace QOU

/-- A localized knot: a knot type placed at a point on the base manifold.
    The point is represented abstractly as an element of the projective line
    (in the archimedean case, a point on CP¹ ≅ S²). -/
structure LocalizedKnot where
  /-- Spherical coordinate θ ∈ [0, π] on CP¹ ≅ S². -/
  theta : ℝ
  /-- Spherical coordinate φ ∈ [0, 2π) on CP¹ ≅ S². -/
  phi : ℝ
  /-- The knot type at this point (given by its planar diagram). -/
  knot : KnotTheory.PlanarDiagram
  /-- θ is in valid range. -/
  theta_range : 0 ≤ theta ∧ theta ≤ Real.pi
  /-- φ is in valid range. -/
  -- Ref: [manuscript] §3, Definition: Localized knot
  phi_range : 0 ≤ phi ∧ phi < 2 * Real.pi

/-! ## Base point and crossing number -/

/-- The base point of a localized knot as a pair (θ, φ) on S². -/
def LocalizedKnot.basePoint (k : LocalizedKnot) : ℝ × ℝ :=
  (k.theta, k.phi)

/-- The crossing number of a localized knot is the crossing count of
    its underlying planar diagram. -/
def LocalizedKnot.crossingNumber (k : LocalizedKnot) : ℕ :=
  k.knot.crossingCount

/-- The writhe of a localized knot. -/
def LocalizedKnot.writhe (k : LocalizedKnot) : ℤ :=
  k.knot.writhe

/-! ## Knot-type equivalence

Two localized knots are *knot-equivalent* when they carry the same knot type
(identified by planar diagram name), regardless of base point.  This is the
combinatorial proxy for ambient isotopy equivalence of knot types. -/

/-- Two localized knots carry the same knot type (same PD name). -/
def LocalizedKnot.sameKnotType (k₁ k₂ : LocalizedKnot) : Prop :=
  k₁.knot.name = k₂.knot.name

/-- `sameKnotType` is reflexive. -/
theorem LocalizedKnot.sameKnotType_refl (k : LocalizedKnot) :
    k.sameKnotType k := rfl

/-- `sameKnotType` is symmetric. -/
theorem LocalizedKnot.sameKnotType_symm {k₁ k₂ : LocalizedKnot}
    (h : k₁.sameKnotType k₂) : k₂.sameKnotType k₁ :=
  h.symm

/-- `sameKnotType` is transitive. -/
theorem LocalizedKnot.sameKnotType_trans {k₁ k₂ k₃ : LocalizedKnot}
    (h₁ : k₁.sameKnotType k₂) (h₂ : k₂.sameKnotType k₃) :
    k₁.sameKnotType k₃ :=
  h₁.trans h₂

/-! ## Co-location

Two localized knots are *co-located* when they share the same base point.
Co-located knots at a common point form the constituents of a hadron. -/

/-- Two localized knots share the same base point on S². -/
def LocalizedKnot.colocated (k₁ k₂ : LocalizedKnot) : Prop :=
  k₁.basePoint = k₂.basePoint

/-- `colocated` is reflexive. -/
theorem LocalizedKnot.colocated_refl (k : LocalizedKnot) :
    k.colocated k := rfl

/-- `colocated` is symmetric. -/
theorem LocalizedKnot.colocated_symm {k₁ k₂ : LocalizedKnot}
    (h : k₁.colocated k₂) : k₂.colocated k₁ :=
  h.symm

/-- `colocated` is transitive. -/
theorem LocalizedKnot.colocated_trans {k₁ k₂ k₃ : LocalizedKnot}
    (h₁ : k₁.colocated k₂) (h₂ : k₂.colocated k₃) :
    k₁.colocated k₃ :=
  h₁.trans h₂

/-! ## Intrinsic angular momentum

The intrinsic angular momentum (spin) of a localized knot is proportional
to its crossing number. This gives knots their half-integer spin
classification in the QOU framework. -/

/-- Intrinsic angular momentum of a localized knot, proportional to
    crossing number: J = c(K) / 2 (in natural units). -/
-- Ref: [manuscript] §3, Proposition: Intrinsic angular momentum
noncomputable def LocalizedKnot.intrinsicAngularMomentum (k : LocalizedKnot) : ℝ :=
  (k.crossingNumber : ℝ) / 2

/-- The trefoil (3 crossings) has spin 3/2 — a fermion (baryon constituent). -/
-- Ref: [manuscript] §3, Example: Trefoil spin
theorem trefoil_spin_three_halves (k : LocalizedKnot)
    (hk : k.knot = KnotTheory.trefoil) :
    k.intrinsicAngularMomentum = 3 / 2 := by
  unfold LocalizedKnot.intrinsicAngularMomentum LocalizedKnot.crossingNumber
  rw [hk]
  simp [KnotTheory.PlanarDiagram.crossingCount, KnotTheory.trefoil]
  ring

/-- The unknot (0 crossings) has spin 0 — a scalar. -/
-- Ref: [manuscript] §3, Example: Unknot spin
theorem unknot_spin_zero (k : LocalizedKnot)
    (hk : k.knot = KnotTheory.unknot) :
    k.intrinsicAngularMomentum = 0 := by
  unfold LocalizedKnot.intrinsicAngularMomentum LocalizedKnot.crossingNumber
  rw [hk]
  simp [KnotTheory.PlanarDiagram.crossingCount, KnotTheory.unknot]

/-- Angular momentum is non-negative. -/
-- Ref: [manuscript] §3
theorem LocalizedKnot.angularMomentum_nonneg (k : LocalizedKnot) :
    0 ≤ k.intrinsicAngularMomentum := by
  unfold intrinsicAngularMomentum crossingNumber
  -- Ref: [manuscript] §3, crossing count is a natural number
  sorry

end QOU
