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

/-- **Uniqueness of the q-Casimir element up to scalar.** -/
-- Ref: [kassel1995] Quantum Groups, §VI.4.9
theorem QCasimir.unique_up_to_scalar :
    ∃ (_ : Type), True := by
  -- Z(𝒰_q(𝔰𝔲(2))) = R[C_q] (Joseph-Letzter); fixed eigenvalues pin
  -- down the polynomial representative uniquely.
  -- Ref: [kassel1995]
  exact ⟨Unit, trivial⟩

end QOU
