/-!
# QOU.CategoricalConnection.exists — existence of categorical connections

Trivial witness ∇₀ = d; non-trivial via ∇ = ∇₀ + ω with ω ∈ Ω¹(A) ⊗ Ad(A).

LaTeX: `\label{prop:categorical-connection-exists}`

## References

- [manuscript] §1-quantum-universes/categorical-connection-exists
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Existence of categorical connections.**

    For every `FrobeniusHopfData C`, a `CategoricalConnection C fh`
    term exists — the trivial witness being the de Rham differential
    `∇₀ = d`; non-trivial witnesses add an `Ad(A)`-valued 1-form. -/
-- Ref: [kock2004]
theorem CategoricalConnection.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Nonempty (CategoricalConnection C fh) := by
  -- Witness: ∇₀ = d via the QU differential-calculus axiom.
  -- Ref: [kock2004]
  sorry

end QOU
