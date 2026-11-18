import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.Algebra.Category.ModuleCat.Monoidal.Symmetric
import Mathlib.CategoryTheory.Limits.Shapes.ZeroObjects

/-!
# Why a QOU witness cannot be a module category

`QOU.TrivialWitness` builds a `QuantumUniverse` on `ModuleCat R` with `A = 𝟙`.
The obvious next question is whether the same category can carry a
`QuantumObservableUniverse`.  **It cannot**, and this file proves why.

The obstruction is a *shape* argument about two of the QOU fields, not about
`R` or the choice of `A`:

* `adjoint_vanishing : Subsingleton (𝟙 ⟶ Ad(A))` — the observability axiom,
  "no hidden global symmetries".
* `adjoint_nontrivial : adjointIncl ≠ 0` — the field added under bean
  `qou-fav8` to stop `adjointObj := 0` satisfying the previous one vacuously.

In a category where `Hom(𝟙, −)` **reflects zero objects**, the first forces
`Ad(A)` to be a zero object, which forces every morphism out of it to be zero,
which contradicts the second.  `ModuleCat R` is such a category:
`Hom(R, W) ≅ W`, so a subsingleton hom-set means `W = 0` on the nose.

## What this buys

It is a *necessary condition on any QOU witness*, obtained without attempting
the construction: **the unit must not generate.** That is exactly the property
separating a representation category from a plain module category — in
`Rep(G)`, `Hom(𝟙, W) = W^G` can vanish for `W ≠ 0`, and it is what
`brings-qou-axiom-map.md` relies on when it says `Ad(A)` decomposes "with no
spin-0 summand".

So `[kassel1995]` §IX naming `Rep(SU_q(2))` is not an arbitrary choice of
convenience — no module category could have worked. The formalize-first
discipline applies: this prunes the search before running it.

## Scope

This is scope **(a)**: it rules out module categories as QOU witnesses. It does
**not** show a QOU exists anywhere, and it is not progress toward discharging
`QuantumObservableUniverse.exists_instance`, whose `sorry` is untouched.

-- Ref: [leitner2026] §2-quantum-observable-universes/quantum-observable-universe-exists
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IX (quantum SU(2))
-/

open CategoryTheory MonoidalCategory Limits

namespace QOU.WitnessObstruction

/-- **The two adjoint conditions are incompatible when the unit reflects zero
    objects.**

    Stated on bare data rather than on a `QuantumObservableUniverse` so that it
    is about the *shape* of the axioms and reusable: `hvanish` is the QOU
    observability axiom, `hnontrivial` is `adjoint_nontrivial`, and `hgen` says
    `Hom(𝟙, −)` reflects zero objects. -/
theorem qou_needs_nongenerating_unit
    {C : Type*} [Category C] [MonoidalCategory C] [Limits.HasZeroMorphisms C]
    {adjointObj A : C} (incl : adjointObj ⟶ A)
    (hvanish : Subsingleton ((𝟙_ C) ⟶ adjointObj))
    (hnontrivial : incl ≠ 0)
    (hgen : ∀ W : C, Subsingleton ((𝟙_ C) ⟶ W) → IsZero W) : False :=
  hnontrivial ((hgen _ hvanish).eq_zero_of_src _)

/-- **In `ModuleCat R` the unit reflects zero objects.**  `Hom(R, W) ≅ W` via
    evaluation at `1`, so a subsingleton hom-set forces `W` to be zero. -/
theorem moduleCat_unit_generates (R : Type) [CommRing R] (W : ModuleCat R)
    (h : Subsingleton ((𝟙_ (ModuleCat R)) ⟶ W)) : IsZero W := by
  rw [IsZero.iff_id_eq_zero]
  apply ModuleCat.hom_ext; apply LinearMap.ext; intro x
  have hzero : (ModuleCat.ofHom (LinearMap.toSpanSingleton R W x) :
      (𝟙_ (ModuleCat R)) ⟶ W) = 0 := h.elim _ _
  have hx := congrArg (fun f => (ModuleCat.Hom.hom f) (1 : R)) hzero
  simpa using hx

/-- **No module category carries a quantum observable universe.**

    The composite of the two results above: `ModuleCat R` satisfies the
    hypothesis that kills the adjoint conditions. -/
theorem no_qou_on_moduleCat (R : Type) [CommRing R]
    {adjointObj A : ModuleCat R} (incl : adjointObj ⟶ A)
    (hvanish : Subsingleton ((𝟙_ (ModuleCat R)) ⟶ adjointObj))
    (hnontrivial : incl ≠ 0) : False :=
  qou_needs_nongenerating_unit incl hvanish hnontrivial (moduleCat_unit_generates R)

/-- **Contrapositive form of the unit-generation obstruction.** When the monoidal
    unit reflects zero objects, any object admitting a nonzero outgoing morphism
    `incl : adjointObj ⟶ A` cannot have a subsingleton hom-set from `𝟙_ C`. -/
theorem not_subsingleton_unit_hom_of_nontrivial_incl
    {C : Type*} [Category C] [MonoidalCategory C] [Limits.HasZeroMorphisms C]
    {adjointObj A : C} (incl : adjointObj ⟶ A)
    (hnontrivial : incl ≠ 0)
    (hgen : ∀ W : C, Subsingleton ((𝟙_ C) ⟶ W) → IsZero W) :
    ¬ Subsingleton ((𝟙_ C) ⟶ adjointObj) :=
  fun hvanish => qou_needs_nongenerating_unit incl hvanish hnontrivial hgen

/-- **In `ModuleCat R`, any source of a nonzero morphism has a non-subsingleton
    hom-set from the monoidal unit.** -/
theorem moduleCat_not_subsingleton_unit_hom_of_ne_zero (R : Type) [CommRing R]
    {adjointObj A : ModuleCat R} (incl : adjointObj ⟶ A)
    (hnontrivial : incl ≠ 0) :
    ¬ Subsingleton ((𝟙_ (ModuleCat R)) ⟶ adjointObj) :=
  fun hvanish => no_qou_on_moduleCat R incl hvanish hnontrivial

end QOU.WitnessObstruction
