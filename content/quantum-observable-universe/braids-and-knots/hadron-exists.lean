/-!
# QOU.Hadron.exists — existence of hadrons

Proton witnesses the existence of stable hadrons; Borromean braid +
Hopf gluon gives E_cross < 0.

LaTeX: `\label{prop:hadron-exists}`

## References

- [manuscript] §4-braids-and-knots/hadron-exists
- [atiyah1990] Geometry and Physics of Knots
-/

import QOU.Basic

namespace QOU

/-- **Existence of hadrons.**

    A `Hadron` term exists (the proton 𝔭 = B₃(u,u,d) is a concrete
    witness satisfying the stability condition E_cross < 0). -/
-- Ref: [atiyah1990] Geometry and Physics of Knots
theorem Hadron.exists : Nonempty Hadron := by
  -- Witness: the proton construction via Borromean braid + Hopf gluon.
  -- Ref: [atiyah1990]
  sorry

end QOU
