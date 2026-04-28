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

/-- **Existence of the q-resolvent.**

    For any `QResolvent H` data (which packages `delta_q`, `s`, the
    inverse witness `R`, and the compatibility property), a term-level
    `QResolvent H` term exists whenever `(s + delta_q)` is invertible
    on `H`.  The existence claim records that such data exists; the
    Peter-Weyl construction over `SU_q(2)` provides a concrete witness
    on each isotypic summand.

    Stub: constructing the witness requires q-heat semigroup
    infrastructure not yet in Mathlib. -/
-- Ref: [kassel1995] Quantum Groups, §IV.4
theorem QResolvent.exists (H : Type*) [Nonempty H] :
    Nonempty (QResolvent H) := by
  -- Witness: R_q(s) = Laplace transform of exp(-t Δ̂_q).
  -- Ref: [kassel1995] §IV.4
  sorry

end QOU
