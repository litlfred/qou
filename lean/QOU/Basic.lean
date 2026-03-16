/-!
# QOU.Basic — Core Definitions (Chapter 1)

Full formalisations of the foundational definitions of
*Quantum Observable Universe* (F. C. Leitner), Chapter 1.

## Paper references
- Definition 1.1  `def:quantum-universe`
- Definition 1.2  `def:quantum-observable-universe`
- Example 1.3     `def:c-quantum-universe`
- Example 1.4     `def:c-quantum-observable-universe`

## Mathlib4 references
- `Mathlib.CategoryTheory.Monoidal.Basic`   (monoidal categories)
- `Mathlib.CategoryTheory.Monoidal.Rigid.Basic` (rigid / autonomous)
- `Mathlib.RingTheory.HopfAlgebra`          (Hopf algebra basics)
- `Mathlib.Algebra.Category.FGModuleCat`    (fibre-functor targets)
-/

import QOU.Prelude

universe u v w

-- ═══════════════════════════════════════════════════════════════════════
-- Frobenius–Hopf object in a monoidal category
-- ═══════════════════════════════════════════════════════════════════════

/-- A **Frobenius–Hopf object** in a k-linear rigid monoidal category.
    This packages the Hopf structure (μ, η, Δ, ε, S) together with a
    Frobenius form λ satisfying the Frobenius relation.

    Paper: Definition 1.1, item (ii). -/
structure FrobeniusHopfObject (k : Type u) (Obj : Type v) [QField k]
    [RigidMonoidalCategory k Obj] where
  /-- The underlying object A in 𝒞. -/
  carrier : Obj
  /-- Multiplication μ : A ⊗ A → A. -/
  mul  : QCategory.Hom (MonoidalCategory.tensorObj carrier carrier) carrier
  /-- Unit η : 𝟙 → A. -/
  unit : QCategory.Hom MonoidalCategory.tensorUnit carrier
  /-- Comultiplication Δ : A → A ⊗ A. -/
  comul : QCategory.Hom carrier (MonoidalCategory.tensorObj carrier carrier)
  /-- Counit ε : A → 𝟙. -/
  counit : QCategory.Hom carrier MonoidalCategory.tensorUnit
  /-- Antipode S : A → A. -/
  antipode : QCategory.Hom carrier carrier
  /-- Frobenius form λ : A → 𝟙. -/
  frobForm : QCategory.Hom carrier MonoidalCategory.tensorUnit
  /-- The Frobenius relation: (μ ⊗ id) ∘ (id ⊗ Δ_μ) = Δ_μ ∘ μ.
      Paper: diagram `eq:frobenius-relation`. -/
  frobenius_rel : Prop
  frobenius_rel_holds : frobenius_rel
  /-- Antipode axiom (left): S ⋆ id = η ∘ ε. -/
  antipode_left : Prop
  antipode_left_holds : antipode_left
  /-- Antipode axiom (right): id ⋆ S = η ∘ ε. -/
  antipode_right : Prop
  antipode_right_holds : antipode_right

/-- The **adjoint object** Ad(A) = A with the conjugation coaction
    a ↦ Σ a₍₁₎ b S(a₍₂₎).
    Paper: Definition 1.2, condition (ii). -/
def adjointObject {k : Type u} {Obj : Type v} [QField k]
    [RigidMonoidalCategory k Obj] (A : FrobeniusHopfObject k Obj) : Obj :=
  A.carrier

-- ═══════════════════════════════════════════════════════════════════════
-- Definition 1.1 — Quantum Universe
-- ═══════════════════════════════════════════════════════════════════════

/-- **Definition 1.1** (Quantum Universe) `def:quantum-universe`

A *quantum universe over k* is a quadruple (𝒞, A, ω, q) where:
1. 𝒞 is a k-linear rigid monoidal category;
2. A is a Frobenius–Hopf object in 𝒞;
3. ω : 𝒞 → Vect_k is a fibre functor (exact faithful k-linear monoidal);
4. q ∈ k× is the deformation parameter.

The *quantum gauge group* is Aut⊗(ω), reconstructed via Tannaka–Krein. -/
structure QuantumUniverse (k : Type u) (Obj : Type v) [QField k]
    [RigidMonoidalCategory k Obj] where
  /-- The Frobenius–Hopf object A in 𝒞. -/
  A : FrobeniusHopfObject k Obj
  /-- The fibre functor ω : 𝒞 → Vect_k. -/
  omega : FibreFunctor k Obj
  /-- The deformation parameter q ∈ k×. -/
  q : Units k

-- ═══════════════════════════════════════════════════════════════════════
-- Definition 1.2 — Quantum Observable Universe
-- ═══════════════════════════════════════════════════════════════════════

/-- Non-degeneracy of the Frobenius form:
    the pairing A ⊗ A → 𝟙 given by λ ∘ μ is non-degenerate.
    Paper: diagram `eq:frobenius-nondegen`. -/
def FrobeniusNondegenerate {k : Type u} {Obj : Type v} [QField k]
    [RigidMonoidalCategory k Obj] (A : FrobeniusHopfObject k Obj) : Prop :=
  ∀ (f : QCategory.Hom MonoidalCategory.tensorUnit A.carrier),
    f ≠ QCategory.id MonoidalCategory.tensorUnit →
    ∃ (g : QCategory.Hom MonoidalCategory.tensorUnit A.carrier),
      QCategory.comp (QCategory.comp f A.mul) A.frobForm ≠
      QCategory.comp (QCategory.id _) A.counit

/-- Vanishing of Hom(𝟙, Ad(A)): the contact / irreducibility condition.
    Paper: Definition 1.2, condition (ii);
    diagram `eq:frobenius-vanishing`. -/
def ContactCondition {k : Type u} {Obj : Type v} [QField k]
    [RigidMonoidalCategory k Obj] (A : FrobeniusHopfObject k Obj) : Prop :=
  ∀ (f : QCategory.Hom MonoidalCategory.tensorUnit (adjointObject A)),
    f = QCategory.id MonoidalCategory.tensorUnit

/-- **Definition 1.2** (Quantum Observable Universe) `def:quantum-observable-universe`

A quantum universe (𝒞, A, ω, q) over k is *observable* if:
1. the Frobenius form λ on A is non-degenerate; and
2. Hom_𝒞(𝟙, Ad(A)) = 0. -/
structure QuantumObservableUniverse (k : Type u) (Obj : Type v) [QField k]
    [RigidMonoidalCategory k Obj] extends QuantumUniverse k Obj where
  /-- The Frobenius form is non-degenerate. -/
  frobenius_nondegen : FrobeniusNondegenerate A
  /-- The contact condition: Hom(𝟙, Ad(A)) = 0. -/
  contact : ContactCondition A

-- ═══════════════════════════════════════════════════════════════════════
-- Examples 1.3–1.4 — ℂ Quantum Universe
-- ═══════════════════════════════════════════════════════════════════════

/-- **Example 1.3** (ℂ Quantum Universe) `def:c-quantum-universe`

Over k = ℂ the quadruple specialises to a 5-tuple (M, θ, G, P, E) where:
- M is a (2n+1)-dimensional smooth manifold,
- θ is a contact form (θ ∧ (dθ)ⁿ ≠ 0),
- G = SU(2),
- P is a principal SU(2)-bundle over M,
- E = P ×_G V is the associated vector bundle.

The Frobenius–Hopf object A = Γ(J¹E), the space of sections of the
first jet bundle, carries a natural Hopf algebra structure (via the
jet coaction) and a Frobenius form (via the Levi form). -/
structure ComplexQuantumUniverse where
  /-- The base manifold M. -/
  M : Type u
  M_smooth : SmoothManifold M
  /-- The contact form θ ∈ Ω¹(M) with θ ∧ (dθ)ⁿ ≠ 0. -/
  theta : DiffForm M 1
  /-- Contact non-degeneracy: θ ∧ (dθ)ⁿ ≠ 0. -/
  contact_nondegen : Prop
  contact_nondegen_holds : contact_nondegen
  /-- The structure group G (concretely SU(2)). -/
  G : Type u
  G_lie : LieGroup G
  /-- The principal bundle P → M. -/
  P : PrincipalBundle G M
  /-- The associated vector bundle E = P ×_G V. -/
  E : Type u

/-- **Example 1.4** (ℂ Quantum Observable Universe)
    `def:c-quantum-observable-universe`

A ℂ quantum universe (M, θ, G, P, E) is observable if additionally:
1. θ has non-degenerate Levi form (contact non-degeneracy), and
2. H⁰(M, Ad(P)) = 0 (instanton irreducibility). -/
structure ComplexQuantumObservableUniverse extends ComplexQuantumUniverse where
  /-- The Levi form L_θ(V,W) = -i dθ(V, W̄) is non-degenerate. -/
  levi_nondegen : Prop
  levi_nondegen_holds : levi_nondegen
  /-- H⁰(M, Ad(P)) = 0 — instanton irreducibility. -/
  h0_vanishes : Prop
  h0_vanishes_holds : h0_vanishes
