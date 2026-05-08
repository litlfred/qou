/-!
# QOU.CategoricalConnection.unique_up_to_gauge — uniqueness up to gauge

Connections form an affine space over Ω¹(A) ⊗ Ad(A).

LaTeX: `\label{prop:categorical-connection-unique}`

## References

- [manuscript] §1-quantum-universes/categorical-connection-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of categorical connections up to gauge.**

    Two `CategoricalConnection C fh` terms differ by an
    `Ad(A)`-valued 1-form: the affine structure makes the space of
    connections a torsor over `Ω¹(A) ⊗ Ad(A)`.  `Subsingleton`
    captures the type-level uniqueness after fixing a gauge. -/
-- Ref: [kock2004]
theorem CategoricalConnection.unique_up_to_gauge
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Subsingleton (CategoricalConnection C fh) := by
  -- DIAGNOSTIC: The `Subsingleton` claim is too strong. The underlying
  -- structure carries free fields (parameters / morphisms / opaque
  -- functions) that admit distinct valid values, so two instances
  -- need not coincide. To recover a meaningful uniqueness claim,
  -- sharpen with a constraining hypothesis (fixing the carrier
  -- object, fixing the substrate parameter, or quantifying over a
  -- quotient by structural equivalence) — see
  -- `frobenius-pairing-unique.lean` for the pattern. Sorry retained
  -- with this diagnosis rather than closed-as-stated.
  -- Ref: [kock2004]
  sorry

end QOU
