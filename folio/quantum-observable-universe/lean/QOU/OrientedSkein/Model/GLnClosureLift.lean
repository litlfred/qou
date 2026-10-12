/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.Model.GLnClosure
import QOU.OrientedSkein.Model.GLnLift

/-!
# `QOU.OrientedSkein.Model.GLnClosureLift` — the closure in `OS(z, t)`, mapped to `R^n`

Open item 1 of dispatch B (PR #7705, bean `qou-slck`), completed.

* `map_cupL`, `map_capL`, `map_closeL` — for any monoidal functor `G`, the image of a
  cup–whisker–cap closure is the closure of the images, with the cup, cap and endomorphism
  conjugated by the tensorator `μ`/`δ` and unitor `ε`/`η` of `G`.  General; no braiding.
* `glnFunctor_closeD` — the vector-representation functor `glnFunctor : OS(q, qi, q^n, [n]_q) ⥤
  ModuleCat R` sends the closure of the leftmost strand computed **inside `OS`** with the universal
  datum (cup `η`, leftward cap `T ≫ ε`) to the closure computed in `ModuleCat` with the `GL_n`
  datum.  Here `glnFunctor.obj (E ⊗ Y) = R^n ⊗ glnFunctor.obj Y` definitionally, so the two sides
  have the same type.  After expanding the lift's tensorator (`OS.μ`) and the images of the
  generators (`lift_coevaluation`, `lift_T`, `lift_evaluation`), the remaining identity is pure
  coherence, discharged by `monoidal`.
* `glnFunctor_closeD_eq_ptr` — combined with `GLnClosure.closeD_datum_eq`: the image of an `OS`
  closure is `qi^n` times the weighted quantum partial trace of `GLnTrace`.

Sorry-free; no axioms beyond Lean/Mathlib's.
-/

namespace QOU.OrientedSkein

open CategoryTheory MonoidalCategory Functor.LaxMonoidal Functor.OplaxMonoidal

universe v₁ v₂ u₁ u₂
variable {C : Type u₁} [Category.{v₁} C] [MonoidalCategory C]
variable {D : Type u₂} [Category.{v₂} D] [MonoidalCategory D]
variable (G : C ⥤ D) [G.Monoidal] {E F : C}

/-- A monoidal functor carries a cup on the left of `Y` to the cup of the image. -/
theorem map_cupL (u : 𝟙_ C ⟶ F ⊗ E) (Y : C) :
    G.map (cupL u Y) = cupL (ε G ≫ G.map u ≫ δ G F E) (G.obj Y) ≫ G.obj F ◁ μ G E Y ≫ μ G F (E ⊗ Y) := by
  simp only [cupL, Functor.map_comp, Functor.Monoidal.map_leftUnitor_inv, Functor.Monoidal.map_whiskerRight,
    Functor.Monoidal.map_associator, comp_whiskerRight, Category.assoc]
  simp only [Functor.Monoidal.μ_δ_assoc, ← comp_whiskerRight_assoc, Functor.Monoidal.μ_δ, id_whiskerRight, Category.id_comp]

/-- A monoidal functor carries a cap on the left of `Y` to the cap of the image. -/
theorem map_capL (c : F ⊗ E ⟶ 𝟙_ C) (Y : C) :
    G.map (capL c Y) = δ G F (E ⊗ Y) ≫ G.obj F ◁ δ G E Y ≫ capL (μ G F E ≫ G.map c ≫ η G) (G.obj Y) := by
  simp only [capL, Functor.map_comp, Functor.Monoidal.map_leftUnitor, Functor.Monoidal.map_whiskerRight,
    Functor.Monoidal.map_associator_inv, comp_whiskerRight, Category.assoc]
  simp only [Functor.Monoidal.μ_δ_assoc, ← comp_whiskerRight_assoc, Functor.Monoidal.μ_δ,
    id_whiskerRight, Category.id_comp, ← whiskerLeft_comp_assoc, whiskerLeft_id]

/-- A monoidal functor carries a cup–whisker–cap closure to the closure of the images. -/
theorem map_closeL (u : 𝟙_ C ⟶ F ⊗ E) (c : F ⊗ E ⟶ 𝟙_ C) (Y : C) (f : E ⊗ Y ⟶ E ⊗ Y) :
    G.map (cupL u Y ≫ F ◁ f ≫ capL c Y) =
      cupL (ε G ≫ G.map u ≫ δ G F E) (G.obj Y) ≫ G.obj F ◁ (μ G E Y ≫ G.map f ≫ δ G E Y) ≫
        capL (μ G F E ≫ G.map c ≫ η G) (G.obj Y) := by
  rw [Functor.map_comp, Functor.map_comp, map_cupL, map_capL, Functor.Monoidal.map_whiskerLeft]
  simp only [Category.assoc, Functor.Monoidal.μ_δ_assoc, whiskerLeft_comp]

end QOU.OrientedSkein

namespace QOU.OrientedSkein.GLn

open CategoryTheory MonoidalCategory Functor.LaxMonoidal Functor.OplaxMonoidal QOU.OrientedSkein.OS

universe u

variable {R : Type u} [CommRing R] {n : ℕ} (q qi : R)
/-- The tensorator of `glnFunctor` is the canonical `OS.μ`. -/
theorem G_μ (h : q * qi = 1) (X0 Y0 : OSCat q qi (q ^ n) (∑ i, wt n q qi i)) :
    μ (glnFunctor (n := n) q qi h) X0 Y0 = (OS.μ (X R n) (X R n) X0.w Y0.w).inv := rfl
theorem G_δ (h : q * qi = 1) (X0 Y0 : OSCat q qi (q ^ n) (∑ i, wt n q qi i)) :
    δ (glnFunctor (n := n) q qi h) X0 Y0 = (OS.μ (X R n) (X R n) X0.w Y0.w).hom := rfl
theorem G_ε (h : q * qi = 1) : ε (glnFunctor (n := n) q qi h) = 𝟙 _ := rfl
theorem G_η (h : q * qi = 1) : η (glnFunctor (n := n) q qi h) = 𝟙 _ := rfl

/-- **The lift carries the `OS` closure to the `GL_n` datum's closure.** -/
theorem glnFunctor_closeD (h : q * qi = 1) (Y : OSCat q qi (q ^ n) (∑ i, wt n q qi i))
    (g : OSCat.E q qi (q ^ n) (∑ i, wt n q qi i) ⊗ Y ⟶ OSCat.E q qi (q ^ n) (∑ i, wt n q qi i) ⊗ Y) :
    (glnFunctor (n := n) q qi h).map (closeD (OSCat.datum q qi (q ^ n) (∑ i, wt n q qi i)) Y g) =
      closeD (datum (n := n) q qi h) (obj (X R n) (X R n) Y.w) ((glnFunctor (n := n) q qi h).map g) := by
  rw [closeD_apply, closeD_apply, map_closeL, G_μ, G_δ, G_ε, G_η, Functor.map_comp]
  rw [lift_coevaluation, lift_T, lift_evaluation]
  simp only [G_μ, G_δ, OS.μ_cons, OS.μ_nil, Iso.trans_hom, Iso.trans_inv, Iso.symm_hom,
    Iso.symm_inv, whiskerLeftIso_hom, whiskerLeftIso_inv, cupL, capL, datum_T, lift_obj,
    OSCat.E, OSCat.F, OS.obj_cons, OS.obj_nil, OS.col, tensorUnit_w]
  monoidal

/-- **Trace compatibility of the lift.**  The image under `glnFunctor` of the closure of the
leftmost strand computed in `OS(q, qi, q^n, [n]_q)` is `qi^n` times the weighted quantum partial
trace `ptr` of `GLnTrace`, applied to the image of the morphism. -/
theorem glnFunctor_closeD_eq_ptr (h : q * qi = 1) (Y : OSCat q qi (q ^ n) (∑ i, wt n q qi i))
    (g : OSCat.E q qi (q ^ n) (∑ i, wt n q qi i) ⊗ Y ⟶ OSCat.E q qi (q ^ n) (∑ i, wt n q qi i) ⊗ Y) :
    (glnFunctor (n := n) q qi h).map (closeD (OSCat.datum q qi (q ^ n) (∑ i, wt n q qi i)) Y g) =
      qi ^ n • ptr (wt n q qi) (obj (X R n) (X R n) Y.w) ((glnFunctor (n := n) q qi h).map g) := by
  rw [glnFunctor_closeD, closeD_datum_eq]

end QOU.OrientedSkein.GLn
