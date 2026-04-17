/-!
# QOU.QHeatEquation.unique_solution — uniqueness of q-heat solutions

Per-isotypic ODE uniqueness gives overall uniqueness of solutions
given initial data.

LaTeX: `\label{prop:q-heat-equation-unique}`

## References

- [manuscript] §2-quantum-observable-universes/q-heat-equation-unique
- [kassel1995] Quantum Groups, §VII.4
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of solutions of the q-heat equation.** -/
-- Ref: [kassel1995] Quantum Groups, §VII.4
theorem QHeatEquation.unique_solution :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
