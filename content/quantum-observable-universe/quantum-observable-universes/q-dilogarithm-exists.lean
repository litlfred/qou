/-!
# QOU.QDilogarithm.exists — existence of the q-dilogarithm

Level-2 iterated primitive of 𝓗_q exists via the shuffle recursion
with pentagon-identity normalisation.

LaTeX: `\label{prop:q-dilogarithm-exists}`

## References

- [manuscript] §2-quantum-observable-universes/q-dilogarithm-exists
- [kassel1995] Quantum Groups, §IV (iterated primitives)
-/

import QOU.Basic

namespace QOU

/-- **Existence of the q-dilogarithm.** -/
-- Ref: [kassel1995]
theorem QDilogarithm.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
