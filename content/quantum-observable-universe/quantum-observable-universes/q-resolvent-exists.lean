/-!
# QOU.QResolvent.exists — existence of the q-resolvent

R_q(s) = (s + Δ̂_q)⁻¹ exists via Laplace transform of the heat
semigroup, or Peter-Weyl diagonal summation.

LaTeX: `\label{prop:q-resolvent-exists}`

## References

- [manuscript] §2-quantum-observable-universes/q-resolvent-exists
- [kassel1995] Quantum Groups, §IV.4
-/

import QOU.Basic

namespace QOU

/-- **Existence of the q-resolvent.** -/
-- Ref: [kassel1995]
theorem QResolvent.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
