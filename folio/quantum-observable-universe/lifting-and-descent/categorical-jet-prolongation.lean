import QOU.Basic
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Category


/-!
# QOU.categorical_jet_prolongation — Jet prolongation preserves QU structure

For a quantum universe (C, A, τ) with connection ∇, the first jet
J¹(A) inherits a Frobenius–Hopf structure and becomes a quantum
universe itself.

LaTeX label: `prop:categorical-jet-prolongation`

## References

- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [leitner2026] §1-quantum-observable-universe/categorical-jet-prolongation
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Prolonged connection data**: the jet prolongation J¹(A)
    inherits a connection ∇' from the original connection ∇. -/
-- Ref: [kock2004], [leitner2026] §1
structure ProlongedConnection (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C] where
  /-- The original Frobenius–Hopf object A. -/
  fh : FrobeniusHopfData C
  /-- The jet object J¹(A) = A ⊗ Ω¹(A). -/
  jetObj : C
  /-- Kähler differentials Ω¹(A). -/
  differentials : C
  /-- J¹(A) is the tensor product. -/
  jet_is_tensor : jetObj = fh.obj ⊗ differentials
  /-- The jet evaluation map j¹ : J¹(A) → A. -/
  jetEval : jetObj ⟶ fh.obj
  /-- The prolonged connection ∇' : J¹(A) → J¹(A) ⊗ Ω¹. -/
  prolongedNabla : jetObj ⟶ (jetObj ⊗ differentials)
  /-- The original connection ∇ : A → A ⊗ Ω¹. -/
  originalNabla : fh.obj ⟶ (fh.obj ⊗ differentials)
  /-- The prolonged connection restricts to the original via jet evaluation:
      ∇ ∘ j¹ = (j¹ ⊗ id) ∘ ∇'. -/
  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  restriction_compatible :
    prolongedNabla ≫ (jetEval ▷ differentials) = jetEval ≫ originalNabla

/-- **Jet prolongation preserves quantum universe structure**.

    J¹(A) inherits multiplication, comultiplication, antipode, and
    Frobenius form from A, making it a Frobenius–Hopf object. -/
-- Ref: [kock2004], [leitner2026] §1
structure JetPreservesQU (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C] where
  /-- The original Frobenius–Hopf object. -/
  original : FrobeniusHopfData C
  /-- The jet Frobenius–Hopf object J¹(A). -/
  jet : FrobeniusHopfData C
  /-- The jet evaluation map. -/
  jetEval : jet.obj ⟶ original.obj
  /-- The jet evaluation is compatible with multiplication:
      j¹ ∘ μ_jet = μ_A ∘ (j¹ ⊗ j¹).
      Expressed as: jetEval composed with the jet multiplication
      equals the original multiplication composed with jetEval on each factor. -/
  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  eval_preserves_mul :
    jet.mul ≫ jetEval = MonoidalCategory.tensorHom jetEval jetEval ≫ original.mul
  /-- The unit section embeds A into J¹(A) as a subalgebra. -/
  unitSection : original.obj ⟶ jet.obj
  /-- The unit section is a monomorphism. -/
  unitSection_mono : Mono unitSection

/-- **Jet prolongation preserves the QU structure -- and the statement is
    vacuous, so this is now a theorem rather than an axiom.**

    It stood as an `axiom` for

        ∃ jet : JetPreservesQU C, jet.original = fh

    Taking `jet := fh` with `jetEval` and `unitSection` both the identity
    discharges it: `eval_preserves_mul` closes by `tensor_id`, and the
    identity is a monomorphism.  So the existential says only that the
    trivial prolongation exists.

    `JetPreservesQU` has no field distinguishing `jet` from `original` --
    no first-order structure, no requirement that `jetEval` be a genuine
    evaluation rather than the identity, and `unitSection_mono` is
    satisfied by the identity.  The prolongation content the proposition
    describes is therefore nowhere in the type, and adding it is a
    structure refactor that is deliberately not guessed at here. -/
-- Ref: [leitner2026] prop:categorical-jet-prolongation
theorem categorical_jet_prolongation (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) : ∃ (jet : JetPreservesQU C), jet.original = fh :=
  ⟨{ original := fh
     jet := fh
     jetEval := CategoryTheory.CategoryStruct.id fh.obj
     eval_preserves_mul := by simp
     unitSection := CategoryTheory.CategoryStruct.id fh.obj
     unitSection_mono := inferInstance }, rfl⟩

end QOU
