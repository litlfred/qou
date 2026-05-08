/-!
# QOU.QDilogarithm.unique — uniqueness of the q-dilogarithm

One-dimensional solution space + pentagon-identity normalisation
forces uniqueness.

LaTeX: `\label{prop:q-dilogarithm-unique}`

## References

- [manuscript] §2-quantum-observable-universes/q-dilogarithm-unique
- [kassel1995] Quantum Groups, §IV
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the q-dilogarithm.**

    Two `QDilogarithm H` terms satisfying the pentagon identity
    coincide — the solution space at level 2 is one-dimensional. -/
-- Ref: [kassel1995]
theorem QDilogarithm.unique (H : Type*) :
    Subsingleton (QDilogarithm H) := by
  -- DIAGNOSTIC: The `Subsingleton` claim is too strong. The underlying
  -- structure carries free fields (parameters / morphisms / opaque
  -- functions) that admit distinct valid values, so two instances
  -- need not coincide. To recover a meaningful uniqueness claim,
  -- sharpen with a constraining hypothesis (fixing the carrier
  -- object, fixing the substrate parameter, or quantifying over a
  -- quotient by structural equivalence) — see
  -- `frobenius-pairing-unique.lean` for the pattern. Sorry retained
  -- with this diagnosis rather than closed-as-stated.
  -- Ref: [kassel1995]
  sorry

end QOU
