import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category


/-!
# QOU.categorical_irreducible — Irreducibility of categorical instantons

Any categorical instanton ∇ in a quantum observable universe is
irreducible: Hom_C(𝟙, Ad(A)) = 0.

This follows directly from condition (ii) of the QOU axioms:
`Subsingleton (𝟙_ C ⟶ adjointObj)`.

LaTeX label: `lem:categorical-irreducible`

## References

- [manuscript] §1-quantum-observable-universe/categorical-irreducible
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Irreducibility of categorical instantons**.

    In a quantum observable universe (C, A, ω), condition (ii) requires
    `Hom_C(𝟙, Ad(A))` to be trivial (a subsingleton). This means every
    categorical instanton is irreducible: there are no nontrivial
    gauge-invariant endomorphisms. -/
-- Ref: [manuscript] §1
theorem categorical_irreducible {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (qou : QuantumObservableUniverse C)
    (f g : (𝟙_ C) ⟶ qou.adjointObj) : f = g :=
  Subsingleton.elim f g

/-- The adjoint hom-space is either empty or a singleton. -/
-- Ref: [manuscript] §1
theorem adjoint_hom_subsingleton {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (qou : QuantumObservableUniverse C) :
    Subsingleton ((𝟙_ C) ⟶ qou.adjointObj) :=
  qou.adjoint_vanishing

end QOU
