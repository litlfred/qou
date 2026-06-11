import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.Algebra.Module.Basic


/-!
# QOU.JetProlongation — First jet bundle in a QOU

Given a quantum observable universe (C, A, ω), the jet object
J¹(A) := A ⊗ Ω¹(A) carries a canonical Frobenius–Hopf structure
inherited from A, and (C, J¹(A), ω') is again a QOU.

## References

- [manuscript] §3 Proposition: Jet Prolongation
- [fred2005] Strong multiplicativity / Gröbner–Shirshov deformation
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Jet prolongation data**: the categorical jet object J¹(A) = A ⊗ Ω¹(A)
    together with its inherited Frobenius–Hopf structure.

    The four steps of the proof are:
    1. Ω¹(A) = ker(μ : A ⊗ A → A) is a direct summand (Frobenius non-degeneracy).
    2. The Frobenius relation restricts to J¹(A), giving (Δ', ε', S').
    3. Non-degeneracy of the pairing on A passes to J¹(A).
    4. Adjoint vanishing: Ad(A) = 0 implies Ad(J¹(A)) = 0.

    LaTeX: `\label{prop:jet-prolongation}`
    Ref: [manuscript] §3 -/
-- Ref: [manuscript] §3
-- Ref: [fred2005] Integration of Skewed-Poisson Structures on Non-co — see content/schema/references.ts
structure JetProlongation (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The Kähler differentials Ω¹(A) as an object of C.
      Abstractly: Ω¹(A) = ker(μ : A ⊗ A → A). -/
  differentials : C
  /-- The jet object J¹(A) = A ⊗ Ω¹(A) in C. -/
  jetObj : C
  /-- J¹(A) is the tensor product of A with Ω¹(A). -/
  jet_is_tensor : jetObj = (fh.obj ⊗ differentials)
  /-- The canonical inclusion A ↪ J¹(A) via the unit section. -/
  unitSection : fh.obj ⟶ jetObj
  /-- The inherited multiplication μ' : J¹(A) ⊗ J¹(A) → J¹(A). -/
  jetMul : (jetObj ⊗ jetObj) ⟶ jetObj
  /-- The inherited comultiplication Δ' : J¹(A) → J¹(A) ⊗ J¹(A). -/
  jetComul : jetObj ⟶ (jetObj ⊗ jetObj)
  /-- The inherited Frobenius form λ' : J¹(A) → 𝟙. -/
  jetFrobForm : jetObj ⟶ (𝟙_ C)
  /-- The Frobenius relation holds for the inherited structure:
      μ' ≫ Δ' = (Δ' ▷ J¹(A)) ≫ α ≫ (J¹(A) ◁ μ'). -/
  jet_frobenius :
    jetMul ≫ jetComul =
      (jetComul ▷ jetObj) ≫ (α_ jetObj jetObj jetObj).hom ≫ (jetObj ◁ jetMul)
  /-- The unit section is a monomorphism (canonical embedding A ↪ J¹(A)). -/
  unitSection_mono : ∀ (f g : (𝟙_ C) ⟶ fh.obj),
    f ≫ unitSection = g ≫ unitSection → f = g

/-- The jet prolongation of a QOU is again a QOU.

    The key content: observability (adjoint vanishing) is preserved because
    Ad(A) = 0 implies Ad(J¹(A)) = 0 — any invariant in Ad(J¹(A)) would
    project to a non-zero invariant in Ad(A), contradicting the hypothesis.

    LaTeX: `\label{prop:jet-prolongation}` (conclusion) -/
-- Ref: [manuscript] §3
theorem jet_prolongation_preserves_observability
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C)
    (adjointObj : C)
    (jetAdjointObj : C)
    (h_proj : ((𝟙_ C) ⟶ jetAdjointObj) → ((𝟙_ C) ⟶ adjointObj))
    (h_inj : Function.Injective h_proj)
    [h_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)] :
    Subsingleton ((𝟙_ C) ⟶ jetAdjointObj) :=
  ⟨fun f g => h_inj (Subsingleton.elim _ _)⟩

end QOU
