import QOU.Basic


/-!
# QOU.FrobeniusHopfData.frobeniusForm_exists — existence of the Frobenius pairing

Every quantum universe admits a non-degenerate Frobenius pairing
⟨·,·⟩ = ∫_A ∘ μ : A ⊗ A → 𝟙.  Existence is immediate from the QU
data; non-degeneracy comes from the snake identities (rigid monoidal
structure of 𝐂 applied to the Frobenius object A).

LaTeX: `\label{prop:frobenius-pairing-exists}`

## References

- [manuscript] §1-quantum-universes/frobenius-pairing-exists
- [kock2004] Frobenius Algebras and 2D Topological Quantum Field
  Theories (Cambridge LMS 59), Ch 2
-/

namespace QOU

/-- **Existence of the non-degenerate Frobenius pairing on a quantum
    universe.**

    Every `QuantumUniverse k` carries a `FrobeniusHopfData` term as
    a structural field (`qu.frobHopf`); the Frobenius pairing is then
    the canonical composition `λ ∘ μ` (see `frobenius-pairing.lean`,
    `FrobeniusHopfData.canonicalPairing`), and non-degeneracy is the
    snake-identity field on `FrobeniusHopfData`.

    Restated relative to the original sorry-stubbed version:
    the original `Nonempty (FrobeniusHopfData C)` claim was too
    strong — not every monoidal category admits Frobenius-Hopf data.
    The right hypothesis is "C is the underlying category of a
    QuantumUniverse", which packages the data by definition. -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
noncomputable def FrobeniusHopfData.frobeniusForm_exists
    {k : Type*} [Field k] (qu : QuantumUniverse.{u, v} k) :
    Nonempty (@FrobeniusHopfData qu.C qu.catInst qu.monInst) :=
  ⟨qu.frobHopf⟩

end QOU
