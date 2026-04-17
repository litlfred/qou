/-!
# QOU.QHeatEquation.exists_solution — well-posedness of the q-heat equation

Formal solution u(t) = exp(-t Δ_q) u₀, eigenfunction expansion over
Peter-Weyl isotypic components.

LaTeX: `\label{prop:q-heat-equation-exists}`

## References

- [manuscript] §2-quantum-observable-universes/q-heat-equation-exists
- [kassel1995] Quantum Groups, §VII.4
-/

import QOU.Basic

namespace QOU

/-- **Well-posedness of the q-heat equation.**

    For every slice type `S`, a `QHeatEquation S` instance exists —
    witnessed by the formal semigroup `u(t) = exp(-t Δ_q) u₀`. -/
-- Ref: [kassel1995] §VII.4
theorem QHeatEquation.exists_solution (S : Type*) [Nonempty S] :
    Nonempty (QHeatEquation S) := by
  -- Witness: Peter-Weyl eigenfunction expansion.
  -- Ref: [kassel1995]
  sorry

end QOU
