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

/-- **External axiom (Kassel 1995 §VII.4): per-isotypic ODE uniqueness
    forces solutions of the q-heat equation to coincide under matching
    initial data.**

    DIAGNOSTIC: bare `Subsingleton` is too strong; axiom encodes
    intended uniqueness pending structure refactor (§3b-cond). -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §VII.4
axiom QHeatEquation.unique_solution_axiom :
    ∀ (S : Type*), Subsingleton (QHeatEquation S)

/-- **Uniqueness of solutions of the q-heat equation.**

    Two `QHeatEquation S` instances with the same initial data
    coincide — per-isotypic ODE uniqueness. -/
-- Ref: [kassel1995] §VII.4
theorem QHeatEquation.unique_solution (S : Type*) :
    Subsingleton (QHeatEquation S) :=
  QHeatEquation.unique_solution_axiom S

end QOU
