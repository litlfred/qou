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

/-- **Uniqueness of the q-Casimir element (up to scalar).**

    Two `QCasimirData` instances on the same `qs : QuantumSu2` with
    the same spin-j eigenvalues differ only by a scalar in the ground
    ring — encoded at the type level as `Subsingleton`. -/
-- Ref: [kassel1995] Quantum Groups, §VI.4.9
theorem QCasimir.unique_up_to_scalar (qs : QuantumSu2) :
    Subsingleton (QCasimirData qs) := by
  -- Joseph–Letzter: Z(𝒰_q(𝔰𝔲(2))) = R[C_q]; eigenvalues pin C_q.
  -- Ref: [kassel1995] §VI.4.9
  sorry

end QOU
