import QOU.QuantumObservableUniverse.Instanton
import QOU.QuantumObservableUniverse.TrivialWitness


/-!
# QOU.CategoricalQExtDeriv.exists — existence of the categorical q-exterior derivative

d_q = q⁻¹ d + (1 - q⁻¹) π_V ∘ d is a morphism in 𝐂, composed from
the de Rham differential, the vertical projection, and scalar
operations.

LaTeX: `\label{prop:categorical-q-ext-deriv-exists}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-q-ext-deriv-exists
- [majid2002] A Quantum Groups Primer (Cambridge UP), §5
-/

universe u v

namespace QOU

/-- **Existence of the categorical q-exterior derivative.** Was the axiom
    `CategoricalQExtDeriv.exists_axiom`; proved 2026-11-15 (bean `qou-n2un`).

    Witness: the Frobenius–Hopf object at the tensor unit
    (`QOU.TrivialWitness.unitFrobHopf`, which exists in every braided monoidal
    category), with `d = π_V = 𝟙` and `q = q⁻¹ = 1`.

    **Scope.** This shows the structure is inhabited in every braided monoidal
    category, so the former axiom was consistent. It also shows existence is
    cheap: `CategoricalQExtDeriv` places no law on `d` (no `d ≫ d = 0`, no
    Leibniz rule) and no compatibility between `π_V` and `d`, so it does not
    pin down a q-exterior derivative. A non-trivial `d_q` needs those laws in
    the structure. -/
theorem CategoricalQExtDeriv.exists
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] :
    Nonempty (CategoricalQExtDeriv C) :=
  ⟨{ frobHopf := QOU.TrivialWitness.unitFrobHopf C
     d_classical := CategoryTheory.CategoryStruct.id _
     proj_V := CategoryTheory.CategoryStruct.id _
     q := 1
     qinv := 1
     q_mul_qinv := mul_one 1
     proj_V_idem := CategoryTheory.Category.comp_id _ }⟩

end QOU
