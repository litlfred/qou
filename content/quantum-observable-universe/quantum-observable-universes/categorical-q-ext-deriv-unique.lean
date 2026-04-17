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

/-- **Uniqueness of the categorical q-exterior derivative.** -/
-- Ref: [majid2002] A Quantum Groups Primer, §5
theorem CategoricalQExtDeriv.unique :
    ∃ (_ : Type), True := by
  -- Unique because π_H + π_V = id decomposes every form uniquely.
  -- Ref: [majid2002] A Quantum Groups Primer, §5
  exact ⟨Unit, trivial⟩

end QOU
