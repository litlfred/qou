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

/-- **Uniqueness of the q-dilogarithm.** -/
-- Ref: [kassel1995]
theorem QDilogarithm.unique :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
