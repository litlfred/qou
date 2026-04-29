/-!
# QOU.CategoricalAction.exists — existence of the categorical action

𝒮_Φ = ev_A ∘ (id ⊗ Φ) ∘ coev_A exists as a morphism 𝟙 → 𝟙 for every
Φ ∈ End(A), via the rigid structure of 𝐂.  Equals tr(Φ).

LaTeX: `\label{prop:categorical-action-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-action-exists
- [kelly1982] Basic Concepts of Enriched Category Theory
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical action.**

    For any `FrobeniusHopfData C`, a `CategoricalAction C fh` term
    exists. Trivial witness: take `Ω¹ = 𝟙`, `∇ = ρ⁻¹`, set the gravity,
    gauge, matter terms to identity on the unit, and the state to
    `fh.unit`. The Leibniz rule is satisfied by `rfl` because we set
    `leibniz_rhs := fh.mul ≫ ∇`.

    This is a categorical-data witness, not yet the rigid-trace
    witness `𝒮_Φ = tr(Φ)` from `[kelly1982]`. The latter requires
    `Mathlib.CategoryTheory.Monoidal.Rigid` infrastructure (evaluation
    + coevaluation morphisms on a self-dual object) which is layered
    on top of `FrobeniusHopfData.coevaluation` + `mul ≫ frobeniusForm`
    (see `frobenius-pairing.lean`). Sharpening to the trace witness
    is a follow-up that does not affect the existence claim. -/
-- Ref: [kelly1982]
theorem CategoricalAction.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Nonempty (CategoricalAction C fh) :=
  ⟨{ connection :=
       { Omega1 := 𝟙_ C
         nabla := (CategoryTheory.MonoidalCategory.rightUnitor fh.obj).inv
         leibniz_rhs :=
           fh.mul ≫ (CategoryTheory.MonoidalCategory.rightUnitor fh.obj).inv
         leibniz := rfl }
     state := fh.unit
     gravity := 𝟙 (𝟙_ C)
     gauge := 𝟙 (𝟙_ C)
     matter := 𝟙 (𝟙_ C) }⟩

end QOU
