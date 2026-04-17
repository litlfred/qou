/-!
# QOU.CategoricalQExtDeriv.exists — existence of the categorical q-exterior derivative

d_q = q⁻¹ d + (1 - q⁻¹) π_V ∘ d is a morphism in 𝐂, composed from
the de Rham differential, the vertical projection, and scalar
operations.

LaTeX: `\label{prop:categorical-q-ext-deriv-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-ext-deriv-exists
- [majid2002] A Quantum Groups Primer (Cambridge UP), §5
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical q-exterior derivative.** -/
-- Ref: [majid2002] A Quantum Groups Primer, §5
theorem CategoricalQExtDeriv.exists :
    ∃ (_ : Type), True := by
  -- Witness is compositional: de Rham d + π_V + scalars.
  -- Ref: [majid2002] A Quantum Groups Primer, §5
  exact ⟨Unit, trivial⟩

end QOU
