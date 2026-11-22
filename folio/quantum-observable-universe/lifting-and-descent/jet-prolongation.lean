import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.Algebra.Module.Basic


/-!
# QOU.JetProlongation — First jet bundle in a QOU

Given a quantum observable universe (C, A, ω), the prolongation object is the
tangent algebra T(A) = Sym_A(Ω¹(A)) (owner ruling 2026-11-22), with A as a direct
summand. Its Hopf data are fields of the structure below: for A = 𝒪(G) they
are cited (T(A) = 𝒪(TG)). No Frobenius form on T(A) is required (owner ruling
2026-11-22); a Haar-type one is excluded in characteristic zero
(`QOU.LiftingDescent.additive_no_integral`).

## References

- [leitner2026] §3 Proposition: Jet Prolongation
- [fred2005] Strong multiplicativity / Gröbner–Shirshov deformation
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Jet prolongation data**: the prolongation object T(A) = Sym_A(Ω¹(A)),
    split over A, together with Hopf data carried as fields
    (they are hypotheses here, not derived).

    LaTeX: `\label{prop:jet-prolongation}`
    Ref: [leitner2026] §3 -/
-- Ref: [leitner2026] §3
-- Ref: [fred2005] Integration of Skewed-Poisson Structures on Non-co — see folio/schema/references.ts
structure JetProlongation (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The Kähler differentials Ω¹(A) as an object of C.
      Abstractly: Ω¹(A) = ker(μ : A ⊗ A → A). -/
  differentials : C
  /-- The prolongation object (owner ruling 2026-11-22: the tangent algebra
      `T(A) = Sym_A(Ω¹(A))`; its degree-≤1 part is `J¹(A) = (A ⊗ A)/I²`). -/
  jetObj : C
  /-- The structure map `ℓ : A → T(A)`. -/
  unitSection : fh.obj ⟶ jetObj
  /-- The augmentation `r : T(A) → A`. -/
  jetRetract : jetObj ⟶ fh.obj
  /-- `A` is a direct summand: `ℓ ≫ r = 𝟙_A`
      (commutative case: `QOU.LiftingDescent.tangentRetract_comp_tangentSection`). -/
  section_retract : unitSection ≫ jetRetract = 𝟙 fh.obj
  /-- The inherited multiplication μ' : J¹(A) ⊗ J¹(A) → J¹(A). -/
  jetMul : (jetObj ⊗ jetObj) ⟶ jetObj
  /-- The inherited comultiplication Δ' : J¹(A) → J¹(A) ⊗ J¹(A). -/
  jetComul : jetObj ⟶ (jetObj ⊗ jetObj)
  /-- The unit section is a monomorphism (canonical embedding A ↪ J¹(A)). -/
  unitSection_mono : ∀ (f g : (𝟙_ C) ⟶ fh.obj),
    f ≫ unitSection = g ≫ unitSection → f = g

/-- Adjoint vanishing transfers to the prolongation object, given an injective
    projection of invariants `Hom(𝟙, Ad(T(A))) → Hom(𝟙, Ad(A))` (a hypothesis,
    not derived). This does not make `T(A)` a QOU: no Frobenius form on it is
    required or supplied.

    LaTeX: `\label{prop:jet-prolongation}` (conclusion) -/
-- Ref: [leitner2026] §3
theorem jet_prolongation_preserves_observability
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C)
    (adjointObj : C)
    (jetAdjointObj : C)
    (h_proj : ((𝟙_ C) ⟶ jetAdjointObj) → ((𝟙_ C) ⟶ adjointObj))
    (h_inj : Function.Injective h_proj)
    [h_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)] :
    Subsingleton ((𝟙_ C) ⟶ jetAdjointObj) :=
  ⟨fun f g => h_inj (Subsingleton.elim _ _)⟩

end QOU
