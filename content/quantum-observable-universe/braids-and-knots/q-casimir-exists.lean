/-!
# QOU.QCasimir.exists — existence of the q-Casimir element

C_q = FE + (qK + q⁻¹K⁻¹ - (q + q⁻¹))/(q - q⁻¹)² is central in
𝒰_q(𝔰𝔲(2)) and acts as [j]_q[j+1]_q on V_j.

LaTeX: `\label{prop:q-casimir-exists}`

## References

- [manuscript] §4-braids-and-knots/q-casimir-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §VI.4
- [lusztig1993] Introduction to Quantum Groups (Birkhäuser)
-/

import QOU.Basic

namespace QOU

/-- **Existence of the q-Casimir element.**

    For any `qs : QuantumSu2`, the q-Casimir data `QCasimirData qs`
    is inhabited by the element
    `C_q = FE + (qK + q⁻¹K⁻¹ - (q + q⁻¹))/(q - q⁻¹)²`. -/
-- Ref: [kassel1995] Quantum Groups, §VI.4
theorem QCasimir.exists (qs : QuantumSu2) : Nonempty (QCasimirData qs) := by
  -- Witness: the explicit formula above; centrality via Hecke + Serre.
  -- Ref: [kassel1995]
  sorry

end QOU
