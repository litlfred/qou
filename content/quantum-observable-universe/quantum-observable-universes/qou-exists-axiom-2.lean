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
`QuantumObservableUniverse R` exhibits a fibre functor — the
carrier of the Peter–Weyl decomposition.

LaTeX label: `lem:qou-exists-axiom-2`

## References

- [manuscript] §1 Quantum Observable Universe, Axiom 2
- Peter–Weyl theorem for compact quantum groups (Woronowicz)
-/

namespace QOU.QuantumObservableUniverse

-- Universe pinning (§7d): `QuantumObservableUniverse` is universe-carrying
-- via its `C : Type cObj` and `fibreFunctor : C ⥤ Type fib` fields.  The
-- application order is `.{cObj, cHom, k, fib}`.  Both the data def and the
-- existence lemma pin the same `fib` so the fibre-codomain universe of
-- `Q.fibreFunctor` ties at the use site (the respelled `Type _` otherwise
-- elaborates to a distinct rigid universe — the §7d trap).
universe cObj cHom uk fib

/-- **Axiom 2 — fibre functor / Peter–Weyl carrier (existence form).**

    Any `QuantumObservableUniverse R` exhibits a `fibreFunctor : C →
    Type*` (inherited from its `QuantumUniverse` base).  This is the
    carrier of the Peter–Weyl decomposition — the structural input
    for axiom 2's observability conditions. -/
-- Ref: [manuscript] §1 Quantum Observable Universe, Axiom 2
-- NOTE: `def`, not `theorem` — `Functor` is a `Type _` (data,
-- not a proposition).  Per Copilot review on PR #794.
def exists_axiom_2_observability_data
    {R : Type uk} [CommRing R]
    (Q : QOU.QuantumObservableUniverse.{cObj, cHom, uk, fib} R) :
    @CategoryTheory.Functor Q.C Q.catInst (Type fib) inferInstance :=
  Q.fibreFunctor

lemma exists_axiom_2_observability
    {R : Type uk} [CommRing R]
    (Q : QOU.QuantumObservableUniverse.{cObj, cHom, uk, fib} R) :
    Nonempty (@CategoryTheory.Functor Q.C Q.catInst (Type fib) inferInstance) :=
  ⟨exists_axiom_2_observability_data Q⟩

end QOU.QuantumObservableUniverse
