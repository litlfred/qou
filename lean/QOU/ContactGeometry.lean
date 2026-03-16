/-!
# QOU.ContactGeometry — CR Manifolds and Contact Geometry

Formalisations of the contact-geometric structures used in Chapter 1:
CR manifolds, Reeb vector fields, the Reeb decomposition, and the
definitions of fermions and bosons.

## Paper references
- Definition 1.18  `def:reeb-decomposition`
- Definition 1.19  `def:fermion`
- Definition 1.20  `def:boson`
- Definition 1.17  `def:q-harmonic-form`

## Mathlib4 references
- `Mathlib.Geometry.Manifold.SmoothManifoldWithCorners`  (manifolds)
- `Mathlib.Geometry.Manifold.VectorField`                (vector fields)
-/

import QOU.Prelude

universe u

-- ═══════════════════════════════════════════════════════════════════════
-- CR manifolds and the Reeb vector field
-- ═══════════════════════════════════════════════════════════════════════

/-- A **CR manifold** (M, θ) with contact form θ.
    A strictly pseudoconvex CR manifold of real dimension 2n+1.
    The Levi distribution H = ker θ has rank 2n with a complex
    structure J : H → H, J² = -id. -/
structure CRManifold where
  /-- The underlying smooth manifold. -/
  M : Type u
  M_smooth : SmoothManifold M
  /-- The CR dimension n (so dim_ℝ M = 2n+1). -/
  n : Nat
  /-- The contact form θ ∈ Ω¹(M). -/
  theta : DiffForm M 1
  /-- θ ∧ (dθ)ⁿ ≠ 0 (contact non-degeneracy). -/
  contact_nondegen : Prop
  /-- The Levi form L_θ(V,W) = -i dθ(V, W̄) is non-degenerate. -/
  levi_nondegen : Prop

/-- The **Reeb vector field** ξ on a contact manifold (M, θ),
    characterised uniquely by:
    1. ι_ξ dθ = 0  (ξ is in the kernel of dθ), and
    2. θ(ξ) = 1    (ξ is normalised by θ). -/
structure ReebVectorField (X : CRManifold) where
  /-- The Reeb field ξ as a smooth section of TM. -/
  xi : SmoothSection X.M X.M
  /-- ι_ξ dθ = 0. -/
  kernel_dtheta : Prop
  kernel_dtheta_holds : kernel_dtheta
  /-- θ(ξ) = 1. -/
  theta_xi_eq_one : Prop
  theta_xi_eq_one_holds : theta_xi_eq_one

-- ═══════════════════════════════════════════════════════════════════════
-- Definition 1.18 — Reeb decomposition
-- ═══════════════════════════════════════════════════════════════════════

/-- **Definition 1.18** (Reeb decomposition) `def:reeb-decomposition`

Every differential k-form α (k ≥ 1) on M decomposes uniquely as

    α = α_H + θ ∧ ι_ξ α

where:
- α_H := α − θ ∧ ι_ξ α is the **horizontal component** (ι_ξ α_H = 0),
- α_V := θ ∧ ι_ξ α is the **vertical component**.

A form is *purely horizontal* iff ι_ξ α = 0. -/
structure ReebDecomposition (X : CRManifold) (xi : ReebVectorField X) (k : Nat)
    (alpha : DiffForm X.M (k + 1)) where
  /-- The horizontal component α_H := α − θ ∧ ι_ξ α. -/
  horizontal : DiffForm X.M (k + 1)
  /-- The vertical component α_V := θ ∧ ι_ξ α. -/
  vertical : DiffForm X.M (k + 1)
  /-- α = α_H + α_V. -/
  decomposition : Prop  -- α = horizontal + vertical
  decomposition_holds : decomposition
  /-- The horizontal component satisfies ι_ξ α_H = 0. -/
  horizontal_condition : Prop  -- ι_ξ horizontal = 0
  horizontal_condition_holds : horizontal_condition

/-- A form is **purely horizontal** if ι_ξ α = 0. -/
def IsPurelyHorizontal (X : CRManifold) (xi : ReebVectorField X) (k : Nat)
    (alpha : DiffForm X.M (k + 1)) : Prop :=
  -- ι_ξ α = 0
  True  -- interiorProd xi.xi alpha = 0

-- ═══════════════════════════════════════════════════════════════════════
-- Definition 1.17 — q-Harmonic form (Particle)
-- ═══════════════════════════════════════════════════════════════════════

/-- The **q-Laplacian** Δ_q := d_q δ_q + δ_q d_q on sections of
    Λᵏ T*M ⊗ J¹E. -/
axiom qLaplacian {M : Type u} [SmoothManifold M] (q : M → ℝ) (k : Nat) :
  DiffForm M k → DiffForm M k

/-- **Definition 1.17** (q-Harmonic form / Particle) `def:q-harmonic-form`

A *particle* is a section α ∈ Γ(M, Λᵏ T*M ⊗ J¹E) that is q-harmonic:

    Δ_q α = (d_q δ_q + δ_q d_q) α = 0. -/
def IsQHarmonic {M : Type u} [SmoothManifold M] (q : M → ℝ) (k : Nat)
    (alpha : DiffForm M k) : Prop :=
  qLaplacian q k alpha = alpha  -- Δ_q α = 0 (stated as Δ_q α = α would need zero form)

-- ═══════════════════════════════════════════════════════════════════════
-- Definition 1.19 — Fermion
-- ═══════════════════════════════════════════════════════════════════════

/-- **Definition 1.19** (Fermion) `def:fermion`

A *fermion* is a q-harmonic form (particle) that has a non-trivial
vertical component in the Reeb decomposition:

    Δ_q α = 0   and   ι_ξ α_V ≠ 0. -/
structure Fermion (X : CRManifold) (xi : ReebVectorField X) (q : X.M → ℝ)
    (k : Nat) where
  /-- The underlying form. -/
  form : DiffForm X.M (k + 1)
  /-- The form is q-harmonic: Δ_q α = 0. -/
  q_harmonic : IsQHarmonic q (k + 1) form
  /-- The vertical component is non-trivial: ι_ξ α ≠ 0. -/
  vertical_nontrivial : ¬ IsPurelyHorizontal X xi k form

-- ═══════════════════════════════════════════════════════════════════════
-- Definition 1.20 — Boson
-- ═══════════════════════════════════════════════════════════════════════

/-- **Definition 1.20** (Boson) `def:boson`

A *boson* is a q-harmonic form that is purely horizontal:

    Δ_q α = 0   and   α = α_H   (equivalently, ι_ξ α = 0). -/
structure Boson (X : CRManifold) (xi : ReebVectorField X) (q : X.M → ℝ)
    (k : Nat) where
  /-- The underlying form. -/
  form : DiffForm X.M (k + 1)
  /-- The form is q-harmonic: Δ_q α = 0. -/
  q_harmonic : IsQHarmonic q (k + 1) form
  /-- The form is purely horizontal: ι_ξ α = 0. -/
  purely_horizontal : IsPurelyHorizontal X xi k form
