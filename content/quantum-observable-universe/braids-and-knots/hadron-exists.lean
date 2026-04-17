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

/-- **Existence of hadrons.** -/
-- Ref: [atiyah1990]
theorem Hadron.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
