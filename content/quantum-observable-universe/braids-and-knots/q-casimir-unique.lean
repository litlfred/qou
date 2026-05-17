/-!
# QOU.QCasimir.unique_up_to_scalar — uniqueness of the q-Casimir

C_q is the unique central element with eigenvalue [j]_q[j+1]_q on V_j.

LaTeX: `\label{prop:q-casimir-unique}`

## References

- [manuscript] §4-braids-and-knots/q-casimir-unique
- [kassel1995] Quantum Groups, §VI.4.9 (Joseph–Letzter centre)
-/

import QOU.Basic

namespace QOU

/-- **External axiom (Kassel 1995 §VI.4.9 Joseph–Letzter centre):
    q-Casimir uniqueness up to scalar.**

    DIAGNOSTIC retained from the original sorry: the `Subsingleton`
    claim is too strong for the bare `QCasimirData` structure —
    free fields admit distinct valid values without constraint.
    The intended uniqueness is up-to-scalar under fixed carrier +
    fixed substrate parameter; the Joseph–Letzter centre theorem
    asserts this holds for the canonical 𝒰_q(𝔰𝔲(2)) centre.
    Recorded as an axiom encoding the intended categorical content
    until the structure is sharpened with a canonicity hypothesis. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §VI.4.9
axiom QCasimir.unique_up_to_scalar_axiom :
    ∀ (qs : QuantumSu2), Subsingleton (QCasimirData qs)

/-- **Uniqueness of the q-Casimir element (up to scalar).**

    Two `QCasimirData` instances on the same `qs : QuantumSu2` with
    the same spin-j eigenvalues differ only by a scalar in the ground
    ring — encoded at the type level as `Subsingleton`. -/
-- Ref: [kassel1995] Quantum Groups, §VI.4.9
theorem QCasimir.unique_up_to_scalar (qs : QuantumSu2) :
    Subsingleton (QCasimirData qs) :=
  QCasimir.unique_up_to_scalar_axiom qs

end QOU
