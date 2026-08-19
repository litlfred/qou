import QOU.QuantumObservableUniverse.CategoricalFoundations


/-!
# QOU.QuantumObservableUniverse.exists_axiom_3_chern

Axiom 3 of a quantum observable universe (categorical Chern-class
vanishing for the adjoint bundle): `Hom_C(𝟙, Ad(A))` is trivial,
ruling out non-trivial invariant adjoint morphisms.

The Lake module
[`lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean`](../../lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean)
encodes this directly as the `adjoint_vanishing` field of the
`QuantumObservableUniverse R` structure.  This sibling extracts
that field as the named lemma matching the URI's expected decl.

LaTeX label: `lem:qou-exists-axiom-3`

## References

- [manuscript] §1 Quantum Observable Universe, Axiom 3
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.QuantumObservableUniverse

/-- **Axiom 3 — Chern-class vanishing (categorical form).**

    Any `QuantumObservableUniverse R` carries the `adjoint_vanishing`
    field, asserting that all morphisms `𝟙 → Ad(A)` in `C` agree —
    the `Subsingleton` form of "no non-trivial invariant adjoint
    morphisms".  This is the categorical analogue of vanishing
    Chern classes for the adjoint bundle. -/
-- Ref: [manuscript] §1 Quantum Observable Universe, Axiom 3
theorem exists_axiom_3_chern
    {R : Type*} [CommRing R] (Q : QOU.QuantumObservableUniverse.{u, v} R) :
    letI := Q.catInst
    letI := Q.monInst
    Subsingleton ((𝟙_ Q.C) ⟶ Q.adjointObj) :=
  Q.adjoint_vanishing

end QOU.QuantumObservableUniverse
