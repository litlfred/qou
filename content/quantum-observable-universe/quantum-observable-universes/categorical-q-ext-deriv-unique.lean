/-!
# QOU.CategoricalQExtDeriv.unique — uniqueness of the categorical q-exterior derivative

Any morphism satisfying the three characterising properties agrees
with d_q = q⁻¹ d + (1 - q⁻¹) π_V ∘ d.

LaTeX: `\label{prop:categorical-q-ext-deriv-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-ext-deriv-unique
- [majid2002] A Quantum Groups Primer (Cambridge UP), §5
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical q-exterior derivative.**

    Given fixed `d`, `π_V`, and `q`, a `CategoricalQExtDeriv C` is
    uniquely determined (any two agree on horizontal and vertical
    components by the weight decomposition). -/
-- Ref: [majid2002]
theorem CategoricalQExtDeriv.unique
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] :
    Subsingleton (CategoricalQExtDeriv C) := by
  -- Weight decomposition π_H + π_V = id forces uniqueness.
  -- Ref: [majid2002]
  sorry

end QOU
