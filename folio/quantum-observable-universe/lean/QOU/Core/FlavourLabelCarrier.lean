import QOU.Core.FlavourCentralPhase
import Mathlib.CategoryTheory.Monoidal.Discrete
import Mathlib.Data.ZMod.Basic

/-!
# QOU.Core.FlavourLabelCarrier — a `ℤ/3` fibre label as the carrier of the flavour phase

Bean `qou-x08k`, multi-fibre route.  Follows `QOU.Core.FlavourCentralPhase` and
`QOU.StandardModel.ColourTripletCommutant`.

`ColourTripletCommutant` shows that the order-3 phase of the octonionic colour triple is the
centre of **colour** `SU(3)`: on that carrier the commutant of colour is `ℚ[J]`, so a flavour
phase needs a different carrier.  The simplest one is a **fibre label**: the carrier
`C × Discrete (ZMod 3)`, an object of `C` together with a label in `ℤ/3`, labels adding under
`⊗` and no morphisms between different labels.

## Results (generic commutative ring `R`, sorry-free)

* `labelPhase` — for `ω : R` with `ω³ = 1`, `z_{(X,g)} = ω^g • 𝟙_X` is a **central phase**
  (`FlavourCentralPhase.CentralPhase`) on the labelled carrier.  The label supplies the
  phase; nothing about `C` is used beyond `R`-linearity.
* `labelPhase_app_flavour` — on `W := (V, 1)` the phase acts by `ω`.
* `flavour_hom_unit_tensor_empty` — **non-self-duality for free**: there is no morphism
  `𝟙 ⟶ W ⊗ W`, because `W ⊗ W` carries label `2 ≠ 0`.  This holds for **every** `V`,
  including self-dual ones and `V = 𝟙`.
* `flavourVolume` / `flavourVolume_epi` — a volume form `(V ⊗ V) ⊗ V ↠ L ≅ 𝟙` in `C`
  lifts to `(W ⊗ W) ⊗ W ↠ 𝟙` on the carrier, since `1 + 1 + 1 = 0` in `ℤ/3`.

## Honest label

The label is **put in by hand**.  This file shows the multi-fibre carrier does what the
flavour axioms ask, and it shows something less welcome: the axioms ask very little.  Taking
`V = 𝟙` gives a `W` with `Λ³W ≅ 𝟙` and `Hom(𝟙, W ⊗ W) = ∅` that is one-dimensional and has
no `SU(3)` in it.  So `Λ³W ≅ 𝟙` plus non-self-duality does **not** force `dim W = 3` or a
flavour `SU(3)`; those need further axioms.  Deriving the `ℤ/3` label from the aether
(rather than from colour, which `ColourTripletCommutant` excludes) is still open.  Pure
algebra, no analytic or empirical input.
-/

namespace QOU.FlavourLabelCarrier

open CategoryTheory MonoidalCategory QOU.FlavourCentralPhase

universe v u

variable {R : Type*} [CommRing R] {C : Type u} [Category.{v} C] [MonoidalCategory C]

attribute [local instance] Discrete.addMonoidal

/-- The labelled carrier: objects of `C` with a `ℤ/3` fibre label. -/
abbrev Labelled (C : Type u) [Category.{v} C] [MonoidalCategory C] :=
  C × Discrete (ZMod 3)

/-- The **flavour object**: `V` with label `1`. -/
abbrev flavourObj (V : C) : Labelled C := (V, Discrete.mk 1)

/-- Labels of a morphism agree. -/
theorem label_eq {X Y : Labelled C} (f : X ⟶ Y) : X.2.as = Y.2.as :=
  Discrete.eq_of_hom f.2

theorem pow_val_add {ω : R} (hω : ω ^ 3 = 1) (g h : ZMod 3) :
    ω ^ (g + h).val = ω ^ g.val * ω ^ h.val := by
  rw [ZMod.val_add, ← pow_eq_pow_mod _ hω, pow_add]

/-- **The label phase** `z_{(X,g)} = ω^g • 𝟙_X`, a central phase when `ω³ = 1`. -/
def labelPhase [Preadditive C] [Linear R C] [MonoidalPreadditive C] [MonoidalLinear R C]
    (ω : R) (hω : ω ^ 3 = 1) : CentralPhase (Labelled C) where
  app X := ((ω ^ X.2.as.val) • 𝟙 X.1, 𝟙 X.2)
  naturality {X Y} f := by
    have hl := label_eq f
    refine Prod.ext ?_ ?_
    · simp only [prod_comp_fst, Linear.smul_comp, Linear.comp_smul, Category.id_comp,
        Category.comp_id, hl]
    · simp
  app_unit := by
    refine Prod.ext ?_ ?_
    · show (ω ^ (0 : ZMod 3).val) • 𝟙 (𝟙_ C) = 𝟙 _
      simp
    · rfl
  app_tensor X Y := by
    refine Prod.ext ?_ ?_
    · show (ω ^ (X.2.as + Y.2.as).val) • 𝟙 (X.1 ⊗ Y.1) =
        ((ω ^ X.2.as.val) • 𝟙 X.1) ⊗ₘ ((ω ^ Y.2.as.val) • 𝟙 Y.1)
      rw [pow_val_add hω, smul_id_tensor_smul_id]
    · exact Subsingleton.elim _ _

/-- On `W = (V, 1)` the label phase acts by `ω`. -/
theorem labelPhase_app_flavour [Preadditive C] [Linear R C] [MonoidalPreadditive C]
    [MonoidalLinear R C] (ω : R) (hω : ω ^ 3 = 1) (V : C) :
    ((labelPhase ω hω).app (flavourObj V)).1 = ω • 𝟙 V := by
  show (ω ^ (1 : ZMod 3).val) • 𝟙 V = ω • 𝟙 V
  rw [show (1 : ZMod 3).val = 1 from rfl, pow_one]

/-- **No morphism `𝟙 ⟶ W ⊗ W`**: `W ⊗ W` has label `2 ≠ 0`.  Holds for every `V`. -/
theorem flavour_hom_unit_tensor_empty (V : C) :
    IsEmpty ((𝟙_ (Labelled C)) ⟶ flavourObj V ⊗ flavourObj V) :=
  ⟨fun f => absurd (label_eq f) (show (0 : ZMod 3) ≠ 1 + 1 by decide)⟩

/-- Consequently `Hom(𝟙, W ⊗ W)` is a subsingleton (the form the flavour axiom uses). -/
theorem flavour_not_selfDual (V : C) :
    Subsingleton ((𝟙_ (Labelled C)) ⟶ flavourObj V ⊗ flavourObj V) :=
  haveI := flavour_hom_unit_tensor_empty V; inferInstance

/-- **Lifted volume form.**  A map `(V ⊗ V) ⊗ V ⟶ L` in `C` lifts to
`(W ⊗ W) ⊗ W ⟶ (L, 0)`, since `1 + 1 + 1 = 0` in `ℤ/3`. -/
def flavourVolume (V L : C) (π : (V ⊗ V) ⊗ V ⟶ L) :
    (flavourObj V ⊗ flavourObj V) ⊗ flavourObj V ⟶ ((L, Discrete.mk 0) : Labelled C) :=
  (π, eqToHom (Discrete.ext (show (1 + 1 + 1 : ZMod 3) = 0 by decide)))

/-- The lifted volume form is epi when `π` is. -/
theorem flavourVolume_epi (V L : C) (π : (V ⊗ V) ⊗ V ⟶ L) [Epi π] :
    Epi (flavourVolume V L π) := by
  constructor
  intro Z g h e
  refine Prod.ext ?_ (Subsingleton.elim _ _)
  exact (cancel_epi π).1 (congrArg Prod.fst e)

/-- `(L, 0) ≅ 𝟙` on the carrier from `L ≅ 𝟙` in `C`. -/
def volumeIso {L : C} (vol : L ≅ 𝟙_ C) : ((L, Discrete.mk 0) : Labelled C) ≅ 𝟙_ (Labelled C) :=
  Iso.prod vol (Iso.refl _)

/-- **The axioms do not force dimension three.**  With `V = 𝟙` the volume form
`(𝟙 ⊗ 𝟙) ⊗ 𝟙 ≅ 𝟙` lifts to an epi `(W ⊗ W) ⊗ W ↠ (𝟙, 0)`, while `Hom(𝟙, W ⊗ W)` is still
empty: a one-dimensional `W` meets both flavour conditions. -/
theorem unit_flavour_meets_axioms :
    Epi (flavourVolume (𝟙_ C) (𝟙_ C) (((λ_ (𝟙_ C)).hom ▷ 𝟙_ C) ≫ (λ_ (𝟙_ C)).hom)) ∧
      IsEmpty ((𝟙_ (Labelled C)) ⟶ flavourObj (𝟙_ C) ⊗ flavourObj (𝟙_ C)) :=
  ⟨flavourVolume_epi _ _ _, flavour_hom_unit_tensor_empty _⟩

end QOU.FlavourLabelCarrier
