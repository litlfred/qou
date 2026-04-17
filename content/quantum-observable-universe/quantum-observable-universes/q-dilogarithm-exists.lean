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

/-- **Existence of the q-dilogarithm.**

    For any type `H` (representing 𝓗_q), a `QDilogarithm H` term
    exists — the level-2 iterated primitive with pentagon-identity
    normalisation. -/
-- Ref: [kassel1995]
theorem QDilogarithm.exists (H : Type*) [Nonempty H] :
    Nonempty (QDilogarithm H) := by
  -- Witness: shuffle recursion + pentagon normalisation.
  -- Ref: [kassel1995]
  sorry

end QOU
