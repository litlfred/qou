/-!
# QOU.CategoricalInstanton.exists — existence of categorical instantons

Trivial witness: the zero connection has F = 0 (self-dual).
Non-trivial witness: BPST descent on SU_q(2)-bundle.

LaTeX: `\label{prop:categorical-instanton-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-instanton-exists
- [atiyah1978] https://doi.org/10.1098/rspa.1978.0143
-/

import QOU.Basic

namespace QOU

/-- **Existence of categorical instantons.**

    For any `FrobeniusHopfData C`, a `CategoricalInstanton fh` term
    exists — the trivial connection F = 0 is self-dual, providing
    the zero-instanton witness. -/
-- Ref: [atiyah1978]
theorem CategoricalInstanton.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _) :
    Nonempty (@CategoricalInstanton C _ _ fh) := by
  -- Witness: trivial/zero connection ∇₀ = d has F = 0 ⇒ self-dual.
  -- Ref: [atiyah1978]
  sorry

end QOU
