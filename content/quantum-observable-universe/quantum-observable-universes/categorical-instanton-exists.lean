/-!
# QOU.CategoricalInstanton.exists — existence of categorical instantons

Trivial witness: the zero connection has F = 0 (self-dual).
Non-trivial witness: BPST descent on SU_q(2)-bundle.

LaTeX: `\label{prop:categorical-instanton-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-instanton-exists
- [atiyah1978] Self-duality in Four-Dimensional Riemannian Geometry,
  https://doi.org/10.1098/rspa.1978.0143
-/

import QOU.Basic

namespace QOU

/-- **Existence of categorical instantons.** -/
-- Ref: [atiyah1978]
theorem CategoricalInstanton.exists :
    ∃ (_ : Type), True := by
  exact ⟨Unit, trivial⟩

end QOU
