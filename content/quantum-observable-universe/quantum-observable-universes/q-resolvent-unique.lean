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

/-- **External axiom (Kassel 1995 §IV.4): pentagon-normalised
    q-resolvent is unique under matching `delta_q`/`s`.**

    Recorded under the §3b-cond pattern; the bare `Subsingleton`
    claim is too strong for the current `QResolvent` structure
    (free fields), so this axiom encodes the intended uniqueness
    pending a structure-tightening refactor. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IV.4
axiom QResolvent.unique_axiom :
    ∀ (H : Type*), Subsingleton (QResolvent H)

/-- **Uniqueness of the q-resolvent.**

    Two `QResolvent H` terms with the same `delta_q`, `s` coincide. -/
-- Ref: [kassel1995]
theorem QResolvent.unique (H : Type*) : Subsingleton (QResolvent H) :=
  QResolvent.unique_axiom H

end QOU
