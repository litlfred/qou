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

/-- **Uniqueness of solutions of the q-heat equation.**

    Two `QHeatEquation S` instances with the same initial data
    coincide — per-isotypic ODE uniqueness. -/
-- Ref: [kassel1995] §VII.4
theorem QHeatEquation.unique_solution (S : Type*) :
    Subsingleton (QHeatEquation S) := by
  -- DIAGNOSTIC: The `Subsingleton` claim is too strong. The underlying
  -- structure carries free fields (parameters / morphisms / opaque
  -- functions) that admit distinct valid values, so two instances
  -- need not coincide. To recover a meaningful uniqueness claim,
  -- sharpen with a constraining hypothesis (fixing the carrier
  -- object, fixing the substrate parameter, or quantifying over a
  -- quotient by structural equivalence) — see
  -- `frobenius-pairing-unique.lean` for the pattern. Sorry retained
  -- with this diagnosis rather than closed-as-stated.
  -- Ref: [kassel1995] §VII.4
  sorry

end QOU
