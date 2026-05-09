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

/-- **Uniqueness of the q-resolvent.**

    Two `QResolvent H` terms with the same `delta_q`, `s` coincide —
    the inverse of `s + delta_q` is unique. -/
-- Ref: [kassel1995]
theorem QResolvent.unique (H : Type*) : Subsingleton (QResolvent H) := by
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
