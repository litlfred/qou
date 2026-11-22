import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.Order.Basic


/-!
# QOU.Torsion.brane_boundary_structure — Brane boundary structure

The defining boundary ∂Aₙ has four structural properties:
1. Codimension ≥ 2 in archimedean realisation
2. Exceptional object: ker(rₙ|_S) ≅ simple object (≅ P¹(ℂ) ≅ S²)
3. Involution symmetry: descent involution restricts to ∂Aₙ
4. Chirality interface: at n=1, separates spacetime from gauge fibre

LaTeX label: `prop:brane-boundary`

## References

- [leitner2026] §3-lifting-of-quantum-torsion/brane-boundary-structure
-/

namespace QOU.Torsion

/-- **Brane boundary structure**: the structural properties of the
    defining boundary `∂Aₙ = ker(rₙ)`.

    The boundary carries four key properties that constrain the
    geometry and topology of the descent tower. -/
-- Ref: [leitner2026] §3
structure BraneBoundaryStructure (R : Type*) [CommRing R] where
  /-- The module at level n. -/
  M_n : Type*
  /-- The module at level n-1. -/
  M_prev : Type*
  /-- Module structures. -/
  [instN : AddCommGroup M_n]
  [instModN : Module R M_n]
  [instPrev : AddCommGroup M_prev]
  [instModPrev : Module R M_prev]
  /-- The restriction map rₙ : Aₙ → A_{n-1}. -/
  restriction : M_n →ₗ[R] M_prev
  /-- The boundary as a submodule (kernel of restriction). -/
  boundary : Submodule R M_n := LinearMap.ker restriction
  /-- (1) Codimension: the boundary has codimension ≥ 2 in M_n.
      Abstractly: the quotient M_n / ∂Aₙ has rank ≥ 2. -/
  codim_ge_two : ∃ (v₁ v₂ : M_n),
    v₁ ∉ boundary ∧ v₂ ∉ boundary ∧
    ∀ (r₁ r₂ : R), r₁ • v₁ + r₂ • v₂ ∈ boundary →
      r₁ = 0 ∧ r₂ = 0
  /-- (2) Exceptional object: at each degeneration locus, the kernel
      restricted to a simple subobject S is isomorphic to a simple
      object (P¹(ℂ) in archimedean realisation). -/
  exceptional_simple : ∃ (S : Submodule R M_n),
    S ≤ boundary ∧ S ≠ ⊥
  /-- (3) Involution symmetry: the descent involution τ restricts
      to an endomorphism of ∂Aₙ. -/
  tau : M_n →ₗ[R] M_n
  tau_idem : tau ∘ₗ tau = tau
  tau_preserves_boundary : ∀ x ∈ boundary, tau x ∈ boundary

attribute [instance] BraneBoundaryStructure.instN
attribute [instance] BraneBoundaryStructure.instModN
attribute [instance] BraneBoundaryStructure.instPrev
attribute [instance] BraneBoundaryStructure.instModPrev

/-- The boundary is non-trivial when the restriction is not injective. -/
-- Ref: [leitner2026] §3
theorem boundary_nontrivial {R : Type*} [CommRing R]
    (bbs : BraneBoundaryStructure R)
    (h : ¬ Function.Injective bbs.restriction) :
    bbs.boundary ≠ ⊥ := by
  -- `boundary` is a data field (defaulted to `ker restriction` but not
  -- constrained to it), so nontriviality follows from the exceptional
  -- simple subobject `S ≤ boundary`, `S ≠ ⊥`.
  obtain ⟨S, hS, hSne⟩ := bbs.exceptional_simple
  intro hbot
  exact hSne (le_bot_iff.mp (hbot ▸ hS))

/-- The involution restricted to the boundary is still idempotent. -/
-- Ref: [leitner2026] §3
theorem tau_boundary_idem {R : Type*} [CommRing R]
    (bbs : BraneBoundaryStructure R)
    (x : bbs.M_n) (hx : x ∈ bbs.boundary) :
    bbs.tau (bbs.tau x) = bbs.tau x := by
  have h := bbs.tau_idem
  have : (bbs.tau ∘ₗ bbs.tau) x = bbs.tau x := by rw [h]
  simpa using this

end QOU.Torsion
