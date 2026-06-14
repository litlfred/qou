import QOU.QuantumObservableUniverse.CategoricalFoundations


/-!
# QOU.QuantumObservableUniverse.exists_axiom_2_observability

Axiom 2 of a quantum observable universe (observability via
Peter–Weyl decomposition): the fibre functor `ω : C → Type*` is
exact and faithful, so observables decompose into a direct sum
over the simple subobjects of `A`.

The Lake module
[`lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean`](../../lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean)
encodes the fibre functor via the `fibreFunctor` field of the
`QuantumUniverse` structure (inherited by
`QuantumObservableUniverse` through `extends`).  This sibling
records the structural existence claim that every
`QuantumObservableUniverse k` exhibits a fibre functor — the
carrier of the Peter–Weyl decomposition.

LaTeX label: `lem:qou-exists-axiom-2`

## References

- [manuscript] §1 Quantum Observable Universe, Axiom 2
- Peter–Weyl theorem for compact quantum groups (Woronowicz)
-/

namespace QOU.QuantumObservableUniverse

/-- **Axiom 2 — fibre functor / Peter–Weyl carrier (existence form).**

    Any `QuantumObservableUniverse k` exhibits a `fibreFunctor : C →
    Type*` (inherited from its `QuantumUniverse` base).  This is the
    carrier of the Peter–Weyl decomposition — the structural input
    for axiom 2's observability conditions. -/
-- Ref: [manuscript] §1 Quantum Observable Universe, Axiom 2
-- NOTE: `def`, not `theorem` — `Functor` is a `Type _` (data,
-- not a proposition).  Per Copilot review on PR #794.
def exists_axiom_2_observability_data
    {k : Type*} [Field k] (Q : QOU.QuantumObservableUniverse.{u, v} k) :
    @CategoryTheory.Functor Q.C Q.catInst (Type _) inferInstance :=
  Q.fibreFunctor

lemma exists_axiom_2_observability
    {k : Type*} [Field k] (Q : QOU.QuantumObservableUniverse.{u, v} k) :
    Nonempty (@CategoryTheory.Functor Q.C Q.catInst (Type _) inferInstance) :=
  ⟨exists_axiom_2_observability_data Q⟩

end QOU.QuantumObservableUniverse
