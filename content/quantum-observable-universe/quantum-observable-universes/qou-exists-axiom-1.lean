import QOU.QuantumObservableUniverse.CategoricalFoundations


/-!
# QOU.QuantumObservableUniverse.exists_axiom_1_frobenius

Axiom 1 of a quantum observable universe (Haar state induces a
non-degenerate Frobenius pairing on `A`): equivalently, the
pairing `(a, b) ↦ h(a · b)` realises an isomorphism
`A → A^∨`.

The Lake module
[`lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean`](../../lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean)
defines `FrobeniusHopfData C`, the structure carrying the Hopf
multiplication, comultiplication, unit, counit, antipode, and the
snake identities that *already* realise non-degeneracy of the
Frobenius pairing (rigid duality `A ≅ A^∨`).  This sibling
records the structural existence claim: every
`QuantumObservableUniverse k` exhibits a `FrobeniusHopfData` on
its underlying category, so the Haar-state / Frobenius pairing is
intrinsic.

LaTeX label: `lem:qou-exists-axiom-1`

## References

- [manuscript] §1 Quantum Observable Universe, Axiom 1
- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*
-/

namespace QOU.QuantumObservableUniverse

/-- **Axiom 1 — Frobenius pairing (existence form).**

    Any `QuantumObservableUniverse k` carries `frobHopf` — the
    `FrobeniusHopfData` whose snake identities encode the
    non-degenerate Haar-state Frobenius pairing on `A`. -/
-- Ref: [manuscript] §1 Quantum Observable Universe, Axiom 1
-- Ref: [kock2004]
-- NOTE: `def`, not `theorem` — `FrobeniusHopfData` is a `Type _`
-- (data, not a proposition).  Per Copilot review on PR #794.
def exists_axiom_1_frobenius_data
    {k : Type*} [Field k] (Q : QOU.QuantumObservableUniverse.{u, v} k) :
    @QOU.FrobeniusHopfData Q.C Q.catInst Q.monInst :=
  Q.frobHopf

lemma exists_axiom_1_frobenius
    {k : Type*} [Field k] (Q : QOU.QuantumObservableUniverse.{u, v} k) :
    Nonempty (@QOU.FrobeniusHopfData Q.C Q.catInst Q.monInst) :=
  ⟨exists_axiom_1_frobenius_data Q⟩

end QOU.QuantumObservableUniverse
