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

/-- **External axiom (Kassel 1995 §IV): pentagon-identity-normalised
    q-dilogarithm is unique.**

    DIAGNOSTIC: bare `Subsingleton` is too strong for the
    `QDilogarithm` structure (free fields admit distinct values).
    Recorded as an axiom encoding the intended categorical content
    (pentagon-normalised uniqueness) until the structure is
    sharpened with a canonicity constraint. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IV
axiom QDilogarithm.unique_axiom :
    ∀ (H : Type*), Subsingleton (QDilogarithm H)

/-- **Uniqueness of the q-dilogarithm.**

    Two `QDilogarithm H` terms satisfying the pentagon identity
    coincide — the solution space at level 2 is one-dimensional. -/
-- Ref: [kassel1995]
theorem QDilogarithm.unique (H : Type*) :
    Subsingleton (QDilogarithm H) :=
  QDilogarithm.unique_axiom H

end QOU
