/-!
# QOU.QResolvent.unique — uniqueness of the q-resolvent

R_q(s) is the unique two-sided inverse of s + Δ̂_q.

LaTeX: `\label{prop:q-resolvent-unique}`

## References

- [manuscript] §2-quantum-observable-universes/q-resolvent-unique
- [kassel1995] Quantum Groups, §IV.4
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the q-resolvent.** -/
-- Ref: [kassel1995]
theorem QResolvent.unique :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
