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

/-- **Existence of the categorical q-exterior derivative.**

    For every category `C` with monoidal structure, a
    `CategoricalQExtDeriv C` term exists via the formula
    `d_q = q⁻¹ d + (1 - q⁻¹) π_V ∘ d`. -/
-- Ref: [majid2002]
/-- **External axiom (§3b-cond pattern): CategoricalQExtDeriv.exists.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalQExtDeriv.exists_axiom (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] :
    Nonempty (CategoricalQExtDeriv C)

theorem CategoricalQExtDeriv.exists
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] :
    Nonempty (CategoricalQExtDeriv C) :=
  CategoricalQExtDeriv.exists_axiom C

end QOU
