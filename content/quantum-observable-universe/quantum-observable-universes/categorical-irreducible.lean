import QOU.QuantumObservableUniverse.CategoricalFoundations
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

/-- The adjoint hom-space is either empty or a singleton.

    In a quantum observable universe over a field `k`, condition (ii)
    requires `Hom_C(𝟙, Ad(A))` to be trivial (a subsingleton). This is
    exactly the bundled `adjoint_vanishing` field. -/
-- Ref: [manuscript] §1
theorem adjoint_hom_subsingleton {k : Type*} [Field k]
    (qou : QuantumObservableUniverse.{u, v} k) :
    letI := qou.catInst
    letI := qou.monInst
    Subsingleton ((𝟙_ qou.C) ⟶ qou.adjointObj) :=
  qou.adjoint_vanishing

/-- **Irreducibility of categorical instantons**.

    In a quantum observable universe `(C, A, ω)` over a field `k`,
    condition (ii) makes `Hom_C(𝟙, Ad(A))` a subsingleton. Hence every
    categorical instanton is irreducible: there are no nontrivial
    gauge-invariant endomorphisms `𝟙 → Ad(A)`. -/
-- Ref: [manuscript] §1
theorem categorical_irreducible {k : Type*} [Field k]
    (qou : QuantumObservableUniverse.{u, v} k)
    (f g : (letI := qou.catInst; letI := qou.monInst; (𝟙_ qou.C) ⟶ qou.adjointObj)) :
    f = g :=
  letI := qou.catInst
  letI := qou.monInst
  @Subsingleton.elim _ qou.adjoint_vanishing f g

end QOU
