import QOU.QuantumObservableUniverse.Instanton


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

universe u v

namespace QOU

/-- **External axiom (§3b-cond pattern): existence of the categorical
    q-exterior derivative.**

    For every category `C` with monoidal structure, a
    `CategoricalQExtDeriv C` term exists via the formula
    `d_q = q⁻¹ d + (1 - q⁻¹) π_V ∘ d`.

    The substantive structure `CategoricalQExtDeriv` (Frobenius–Hopf
    data, the classical differential `d`, the vertical projection
    `proj_V` with idempotency, and the non-zero deformation parameter
    `q`) is defined in `QOU.QuantumObservableUniverse.Instanton`;
    its `dq` morphism and `dq_classical` reduction are proved there.
    Constructing such data for an *arbitrary* monoidal `C` requires
    Mathlib infrastructure not yet present, so existence is asserted
    as a named axiom pending that infrastructure. -/
-- Ref: [majid2002] A Quantum Groups Primer (Cambridge UP), §5
axiom CategoricalQExtDeriv.exists_axiom (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] :
    Nonempty (CategoricalQExtDeriv C)

/-- **Existence of the categorical q-exterior derivative** (conditional on
    `CategoricalQExtDeriv.exists_axiom`). -/
theorem CategoricalQExtDeriv.exists
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] :
    Nonempty (CategoricalQExtDeriv C) :=
  CategoricalQExtDeriv.exists_axiom C

end QOU
