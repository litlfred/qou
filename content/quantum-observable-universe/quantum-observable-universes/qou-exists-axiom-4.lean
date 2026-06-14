import QOU.QuantumObservableUniverse.CategoricalFoundations


/-!
# QOU.QuantumObservableUniverse.exists_axiom_4_volume

Axiom 4 of a quantum observable universe (categorical volume
constraint via the quantum determinant): the fundamental object
`V` of categorical dimension 2 admits a non-degenerate epimorphism
`ε : Λ²V → 𝟙` preserved by the rigid dualities, which forces
`det(g_V) = 1` for all `g ∈ Aut⊗(ω)` — i.e., restricts the gauge
group from `GL(2)` to `SL(2)`.

The Lake module
[`lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean`](../../lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean)
encodes this as the `volumeForm` field of the
`QuantumObservableUniverse k` structure.  This sibling extracts
that field as the named lemma matching the URI's expected decl.

LaTeX label: `lem:qou-exists-axiom-4`

## References

- [manuscript] §1 Quantum Observable Universe, Axiom 4
-/

namespace QOU.QuantumObservableUniverse

/-- **Axiom 4 — categorical volume constraint.**

    Any `QuantumObservableUniverse k` carries the `volumeForm`
    field — a morphism `Λ²V → 𝟙` realising the non-degenerate
    epimorphism that pins the categorical determinant.  This is
    the categorical formulation of the `SL(2)` gauge restriction. -/
-- Ref: [manuscript] §1 Quantum Observable Universe, Axiom 4
-- NOTE: `def`, not `theorem` — a Hom-set `Q.exteriorSquare ⟶ (𝟙_ Q.C)`
-- is a `Type _` (morphisms are data, not propositions).  Per Copilot
-- review on PR #794.
def exists_axiom_4_volume_data
    {k : Type*} [Field k] (Q : QOU.QuantumObservableUniverse.{u, v} k) :
    Q.exteriorSquare ⟶ (𝟙_ Q.C) :=
  Q.volumeForm

lemma exists_axiom_4_volume
    {k : Type*} [Field k] (Q : QOU.QuantumObservableUniverse.{u, v} k) :
    Nonempty (Q.exteriorSquare ⟶ (𝟙_ Q.C)) :=
  ⟨exists_axiom_4_volume_data Q⟩

end QOU.QuantumObservableUniverse
