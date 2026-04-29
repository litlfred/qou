/-!
# QOU.CategoricalInstanton.unique_up_to_gauge — uniqueness of instantons modulo gauge

Two categorical instantons of the same c₂ are related by a
categorical gauge transformation.

LaTeX: `\label{prop:categorical-instanton-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-instanton-unique
- [atiyah1978] https://doi.org/10.1098/rspa.1978.0143
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of categorical instantons (moduli).**

    For fixed `FrobeniusHopfData`, the moduli of self-dual instanton
    connections is a quotient by categorical gauge transformations;
    `Subsingleton` expresses the type-level uniqueness of the moduli
    point for a given topological charge. -/
-- Ref: [atiyah1978]
theorem CategoricalInstanton.unique_up_to_gauge
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _) :
    Subsingleton (@CategoricalInstanton C _ _ fh) := by
  -- DIAGNOSTIC: The `Subsingleton` claim is too strong. The underlying
  -- structure carries free fields (parameters / morphisms / opaque
  -- functions) that admit distinct valid values, so two instances
  -- need not coincide. To recover a meaningful uniqueness claim,
  -- sharpen with a constraining hypothesis (fixing the carrier
  -- object, fixing the substrate parameter, or quantifying over a
  -- quotient by structural equivalence) — see
  -- `frobenius-pairing-unique.lean` for the pattern. Sorry retained
  -- with this diagnosis rather than closed-as-stated.
  sorry

end QOU
