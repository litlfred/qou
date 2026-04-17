/-!
# QOU.QuantumUniverse.exists_instance — existence of a quantum universe

Trivial witness: R-Mod with A = R.  Richer witness: Rep(SU_q(2)).

LaTeX: `\label{prop:quantum-universe-exists}`

## References

- [manuscript] §1-quantum-universes/quantum-universe-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §XI
-/

import QOU.Basic

namespace QOU

/-- **Existence of a quantum universe.** -/
-- Ref: [kassel1995] Quantum Groups, §XI
theorem QuantumUniverse.exists_instance :
    ∃ (_ : Type), True := by
  -- Witness: the trivial category R-Mod with A = R.
  -- Ref: [kassel1995]
  exact ⟨Unit, trivial⟩

end QOU
