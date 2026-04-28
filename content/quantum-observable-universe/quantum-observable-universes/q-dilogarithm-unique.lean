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
  -- One-dim solution space + pentagon normalisation.
  -- Ref: [kassel1995]
  sorry

end QOU
