/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.MarkovClosure
import QOU.OrientedSkein.SkeinDatum

/-!
# `QOU.OrientedSkein.BraidedClosure` — closing strands in a braided category is a Markov trace

Stage 4b of the oriented-skein formalisation (Step 3 of
`docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`).

Let `C` be an `R`-linear braided monoidal category, `E, F` objects, `u : 𝟙 ⟶ F ⊗ E` a "cup" and
`c : F ⊗ E ⟶ 𝟙` a "cap".  Closing the leftmost strand of an endomorphism `f` of `E ⊗ Y` by

`ptr_Y (f) = λ⁻¹ ≫ (u ▷ Y) ≫ α ≫ (F ◁ f) ≫ α⁻¹ ≫ (c ▷ Y) ≫ λ`

satisfies every axiom of `QOU.OrientedSkein.LeftTrace` for the braiding crossing `S = β_{E,E}`,
provided `u ≫ c = d • 𝟙` and the curl `ptr_E (β_{E,E}) = w • 𝟙`.  Nothing else is assumed of `u`
and `c`: the double-closure rule (Markov's first move) holds for an *arbitrary* cup and cap, because
a crossing on the two right legs of a pair of nested cups (or caps) slides through them onto the two
left legs (`cup_cross_nested`, `cap_cross_nested`), and a crossing of the left legs commutes with
everything acting on the right legs.

The standard instance (`braidedLeftTrace`) takes `u = η_{F,E}` and `c = β_{F,E} ≫ ε_{F,E}` for an
exact pairing `F ⊣ E`, so that `d` is the braided quantum dimension
`QOU.MathlibExt.qDimWith F E = η ≫ β ≫ ε` and the closure of a braid is its (blackboard-framed)
closure.  With stage 4a (`QOU.OrientedSkein.MarkovClosure`) this gives:

**Theorem (`braided_closure_eq_markov`).**  If `β_{E,E}` satisfies the Hecke relation
`β² = (q - qi) β + q qi`, the loop is `d` (invertible), the curl is `w`, and `s : End 𝟙 → R` is
`R`-linear with `s 𝟙 = 1`, then for every `x ∈ H_{n+1}(q)`

`d^{-(n+1)} · s (closure of all strands of ρ(x)) = T.tr n x`

for **every** Markov trace family `T` on the Hecke tower with parameter `z = w d⁻¹`, e.g. the
Ocneanu trace.  This is the categorical half of the universal property of `OS(z, t)` used by Step 4
of the audit (traces of braids computed through any braided functor out of the skein category).

## Main statements

* `cup_cross_nested`, `cap_cross_nested` — a crossing slides through a nested pair of cups / caps.
* `closureLeftTrace` — an arbitrary cup and cap give a `LeftTrace` for `β_{E,E}`.
* `braidedLeftTrace` — the exact-pairing instance.
* `braided_closure_eq_markov` — the normalised closure is *the* Markov trace.

Sorry-free; no axioms beyond Lean/Mathlib's.

## References

* [turaev1988] V. Turaev, *The Yang–Baxter equation and invariants of links*, Invent. Math. 92
  (1988), §2 (enhanced Yang–Baxter operators and Markov traces).
* [brundan2017] J. Brundan, *Representations of the oriented skein category*, arXiv 1712.08953.
-/

namespace QOU.OrientedSkein

open CategoryTheory MonoidalCategory BraidedCategory QOU.SchurWeyl

universe v u

set_option linter.unusedSectionVars false

section Slides

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
variable {F E : C}

/-- A crossing of the right leg of a cup with a strand on its right moves to the left leg. -/
theorem cup_slide_right_leg (u : 𝟙_ C ⟶ F ⊗ E) :
    u ▷ E ≫ (α_ F E E).hom ≫ F ◁ (β_ E E).hom =
      (λ_ E).hom ≫ (ρ_ E).inv ≫ E ◁ u ≫ (α_ E F E).inv ≫ (β_ F E).inv ▷ E ≫ (α_ F E E).hom := by
  have h := braiding_naturality_left u E
  rw [braiding_tensor_left_hom, braiding_tensorUnit_left] at h
  have h2 := congrArg (· ≫ (α_ E F E).inv ≫ (β_ F E).inv ▷ E ≫ (α_ F E E).hom) h
  simp only [Category.assoc] at h2
  simpa using h2

/-- A strand crossing the left leg of a cup from the right moves to its other side. -/
theorem cup_slide_left_leg (u : 𝟙_ C ⟶ F ⊗ E) :
    u ▷ F ≫ (α_ F E F).hom ≫ F ◁ (β_ F E).inv =
      (λ_ F).hom ≫ (ρ_ F).inv ≫ F ◁ u ≫ (α_ F F E).inv ≫ (β_ F F).hom ▷ E ≫ (α_ F F E).hom := by
  have h := braiding_naturality_right F u
  rw [braiding_tensor_right_hom, braiding_tensorUnit_right] at h
  have h2 := congrArg (fun x => (λ_ F).hom ≫ (ρ_ F).inv ≫ x ≫ (α_ F E F).hom ≫
    F ◁ (β_ F E).inv) h
  simp only [Category.assoc] at h2
  simpa using h2.symm

/-- A crossing entering the right leg of a cap moves to a crossing past its left leg. -/
theorem cap_slide_right_leg (c : F ⊗ E ⟶ 𝟙_ C) :
    F ◁ (β_ E E).hom ≫ (α_ F E E).inv ≫ c ▷ E =
      (α_ F E E).inv ≫ (β_ E F).inv ▷ E ≫ (α_ E F E).hom ≫ E ◁ c ≫ (ρ_ E).hom ≫ (λ_ E).inv := by
  have h := braiding_naturality_right E c
  rw [braiding_tensor_right_hom, braiding_tensorUnit_right] at h
  have h2 := congrArg (fun x => (α_ F E E).inv ≫ (β_ E F).inv ▷ E ≫ (α_ E F E).hom ≫ x) h
  simp only [Category.assoc] at h2
  simpa using h2.symm

/-- A strand crossing into a cap from the right exits across its left leg. -/
theorem cap_slide_left_leg (c : F ⊗ E ⟶ 𝟙_ C) :
    F ◁ (β_ E F).inv ≫ (α_ F E F).inv ≫ c ▷ F =
      (α_ F F E).inv ≫ (β_ F F).hom ▷ E ≫ (α_ F F E).hom ≫ F ◁ c ≫ (ρ_ F).hom ≫ (λ_ F).inv := by
  have h := braiding_naturality_left c F
  rw [braiding_tensor_left_hom, braiding_tensorUnit_left] at h
  have h2 := congrArg (fun x => F ◁ (β_ E F).inv ≫ (α_ F E F).inv ≫ x ≫ (ρ_ F).hom ≫
    (λ_ F).inv) h
  simp only [Category.assoc] at h2
  simpa using h2

/-- A cup on the left of `Y`: `Y ⟶ F ⊗ (E ⊗ Y)`. -/
def cupOn (u : 𝟙_ C ⟶ F ⊗ E) (Y : C) : Y ⟶ F ⊗ (E ⊗ Y) :=
  (λ_ Y).inv ≫ u ▷ Y ≫ (α_ F E Y).hom

/-- A cap on the left of `Y`: `F ⊗ (E ⊗ Y) ⟶ Y`. -/
def capOn (c : F ⊗ E ⟶ 𝟙_ C) (Y : C) : F ⊗ (E ⊗ Y) ⟶ Y :=
  (α_ F E Y).inv ≫ c ▷ Y ≫ (λ_ Y).hom

@[reassoc]
theorem cupOn_naturality (u : 𝟙_ C ⟶ F ⊗ E) {Y Y' : C} (g : Y ⟶ Y') :
    g ≫ cupOn u Y' = cupOn u Y ≫ F ◁ E ◁ g := by
  unfold cupOn
  rw [leftUnitor_inv_naturality_assoc, whisker_exchange_assoc, Category.assoc, Category.assoc,
    associator_naturality_right]

theorem capOn_naturality (c : F ⊗ E ⟶ 𝟙_ C) {Y Y' : C} (g : Y ⟶ Y') :
    F ◁ E ◁ g ≫ capOn c Y' = capOn c Y ≫ g := by
  unfold capOn
  rw [associator_inv_naturality_right_assoc, whisker_exchange_assoc, leftUnitor_naturality]
  simp only [Category.assoc]

/-- **A crossing slides through a nested pair of cups**, from the right legs to the left legs. -/
theorem cup_cross_nested (u : 𝟙_ C ⟶ F ⊗ E) (Y : C) :
    cupOn u Y ≫ F ◁ cupOn u (E ⊗ Y) ≫ F ◁ F ◁ leftCross (β_ E E).hom Y =
      cupOn u Y ≫ F ◁ cupOn u (E ⊗ Y) ≫ leftCross (β_ F F).hom (E ⊗ (E ⊗ Y)) := by
  calc _ = 𝟙 Y ⊗≫ u ▷ Y ⊗≫
        F ◁ (u ▷ E ≫ (α_ F E E).hom ≫ F ◁ (β_ E E).hom) ▷ Y ⊗≫ 𝟙 _ := by
          unfold cupOn leftCross; monoidal
    _ = 𝟙 Y ⊗≫ (u ▷ Y ≫ (F ⊗ E) ◁ ((λ_ Y).inv ≫ u ▷ Y)) ⊗≫
        (F ◁ (β_ F E).inv ▷ E) ▷ Y ⊗≫ 𝟙 _ := by
          rw [cup_slide_right_leg]; monoidal
    _ = 𝟙 Y ⊗≫ u ▷ Y ⊗≫
        ((u ▷ F ≫ (α_ F E F).hom ≫ F ◁ (β_ F E).inv) ▷ E) ▷ Y ⊗≫ 𝟙 _ := by
          rw [← whisker_exchange]; monoidal
    _ = _ := by
          rw [cup_slide_left_leg]; unfold cupOn leftCross; monoidal

/-- **A crossing slides through a nested pair of caps**, from the right legs to the left legs. -/
theorem cap_cross_nested (c : F ⊗ E ⟶ 𝟙_ C) (Y : C) :
    F ◁ F ◁ leftCross (β_ E E).hom Y ≫ F ◁ capOn c (E ⊗ Y) ≫ capOn c Y =
      leftCross (β_ F F).hom (E ⊗ (E ⊗ Y)) ≫ F ◁ capOn c (E ⊗ Y) ≫ capOn c Y := by
  calc _ = 𝟙 _ ⊗≫ (F ◁ (F ◁ (β_ E E).hom ≫ (α_ F E E).inv ≫ c ▷ E)) ▷ Y ⊗≫
        c ▷ Y ⊗≫ 𝟙 Y := by
          unfold capOn leftCross; monoidal
    _ = 𝟙 _ ⊗≫ (F ◁ (β_ E F).inv ▷ E) ▷ Y ⊗≫
        ((F ⊗ E) ◁ (c ▷ Y ≫ (λ_ Y).hom) ≫ c ▷ Y) ⊗≫ 𝟙 Y := by
          rw [cap_slide_right_leg]; monoidal
    _ = 𝟙 _ ⊗≫ ((F ◁ (β_ E F).inv ≫ (α_ F E F).inv ≫ c ▷ F) ▷ E) ▷ Y ⊗≫
        c ▷ Y ⊗≫ 𝟙 Y := by
          rw [whisker_exchange]; monoidal
    _ = _ := by
          rw [cap_slide_left_leg]; unfold capOn leftCross; monoidal

/-- A crossing of the two left strands commutes with anything on the strands to their right. -/
@[reassoc]
theorem leftCross_comm_whisker' {X : C} (S : X ⊗ X ⟶ X ⊗ X) {P P' : C} (τ : P ⟶ P') :
    leftCross S P ≫ (X ◁ X ◁ τ) = (X ◁ X ◁ τ) ≫ leftCross S P' := by
  unfold leftCross
  rw [Category.assoc, Category.assoc, ← associator_naturality_right, ← whisker_exchange_assoc,
    ← associator_inv_naturality_right_assoc]

/-- The double closure with arbitrary cup and cap is invariant under moving the crossing. -/
theorem closure2_conj (u : 𝟙_ C ⟶ F ⊗ E) (c : F ⊗ E ⟶ 𝟙_ C) (Y : C)
    (f : E ⊗ (E ⊗ Y) ⟶ E ⊗ (E ⊗ Y)) :
    cupOn u Y ≫ F ◁ (cupOn u (E ⊗ Y) ≫ F ◁ (leftCross (β_ E E).hom Y ≫ f) ≫ capOn c (E ⊗ Y))
        ≫ capOn c Y =
      cupOn u Y ≫ F ◁ (cupOn u (E ⊗ Y) ≫ F ◁ (f ≫ leftCross (β_ E E).hom Y) ≫ capOn c (E ⊗ Y))
        ≫ capOn c Y := by
  simp only [whiskerLeft_comp, Category.assoc]
  rw [reassoc_of% (cup_cross_nested u Y), leftCross_comm_whisker'_assoc, cap_cross_nested]

end Slides

section LinearClosure

variable {R : Type*} [CommRing R]
variable {C : Type u} [Category.{v} C] [Preadditive C] [Linear R C]
  [MonoidalCategory C] [MonoidalPreadditive C] [MonoidalLinear R C] [BraidedCategory C]
variable {F E : C}

/-- Closing the leftmost strand with a cup `u` and a cap `c`, as an `R`-linear map. -/
def closeLeft (u : 𝟙_ C ⟶ F ⊗ E) (c : F ⊗ E ⟶ 𝟙_ C) (Y : C) :
    (E ⊗ Y ⟶ E ⊗ Y) →ₗ[R] (Y ⟶ Y) where
  toFun f := cupOn u Y ≫ F ◁ f ≫ capOn c Y
  map_add' f g := by
    rw [MonoidalPreadditive.whiskerLeft_add, Preadditive.add_comp, Preadditive.comp_add]
  map_smul' r f := by
    rw [MonoidalLinear.whiskerLeft_smul, Linear.smul_comp, Linear.comp_smul, RingHom.id_apply]

theorem closeLeft_apply (u : 𝟙_ C ⟶ F ⊗ E) (c : F ⊗ E ⟶ 𝟙_ C) (Y : C) (f : E ⊗ Y ⟶ E ⊗ Y) :
    closeLeft (R := R) u c Y f = cupOn u Y ≫ F ◁ f ≫ capOn c Y := rfl

theorem closeLeft_id (u : 𝟙_ C ⟶ F ⊗ E) (c : F ⊗ E ⟶ 𝟙_ C) {d : R}
    (hd : u ≫ c = d • 𝟙 (𝟙_ C)) (Y : C) :
    closeLeft (R := R) u c Y (𝟙 _) = d • 𝟙 Y := by
  rw [closeLeft_apply, whiskerLeft_id, Category.id_comp]
  unfold cupOn capOn
  simp only [Category.assoc, Iso.hom_inv_id_assoc]
  rw [← comp_whiskerRight_assoc, hd, MonoidalLinear.smul_whiskerRight, id_whiskerRight,
    Linear.smul_comp, Linear.comp_smul, Category.id_comp, Iso.inv_hom_id]

theorem closeLeft_leftCross (u : 𝟙_ C ⟶ F ⊗ E) (c : F ⊗ E ⟶ 𝟙_ C) (Y : C)
    (h : E ⊗ E ⟶ E ⊗ E) :
    closeLeft (R := R) u c (E ⊗ Y) (leftCross h Y) = closeLeft (R := R) u c E h ▷ Y := by
  simp only [closeLeft_apply]
  unfold cupOn capOn leftCross
  monoidal

/-- **An arbitrary cup and cap give a left trace** for the braiding crossing, given the loop value
`u ≫ c = d • 𝟙` and the curl value `closeLeft (β_{E,E}) = w • 𝟙`. -/
def closureLeftTrace {q qi : R} (H : HeckeCrossing q qi E) (hS : H.S = (β_ E E).hom)
    (u : 𝟙_ C ⟶ F ⊗ E) (c : F ⊗ E ⟶ 𝟙_ C) (d w : R) (hd : u ≫ c = d • 𝟙 (𝟙_ C))
    (hw : closeLeft (R := R) u c E (β_ E E).hom = w • 𝟙 E) : LeftTrace H where
  ptr := closeLeft u c
  ptr_whisker_comp g f := by
    simp only [closeLeft_apply, whiskerLeft_comp, Category.assoc]
    rw [cupOn_naturality_assoc]
  ptr_comp_whisker g f := by
    simp only [closeLeft_apply, whiskerLeft_comp, Category.assoc]
    rw [capOn_naturality]
  d := d
  w := w
  ptr_id Y := closeLeft_id u c hd Y
  ptr_cross Y := by
    rw [hS, closeLeft_leftCross, hw, MonoidalLinear.smul_whiskerRight, id_whiskerRight]
  ptr2_conj Y f := by
    rw [hS]
    simp only [closeLeft_apply]
    exact closure2_conj u c Y f

/-- The Hecke crossing given by the braiding, when it satisfies the Hecke quadratic relation. -/
def HeckeCrossing.ofBraiding {q qi : R} (E : C) (hquad : IsHeckeQuad q qi (β_ E E).hom) :
    HeckeCrossing q qi E :=
  ⟨(β_ E E).hom, hquad, braid_braiding E⟩

/-- **The exact-pairing instance**: close a strand by `η_{F,E}`, the braiding `β_{F,E}`, and
`ε_{F,E}`; the loop value is the braided quantum dimension `qDimWith F E`. -/
noncomputable def braidedLeftTrace {q qi : R} (E F : C) [ExactPairing F E]
    (hquad : IsHeckeQuad q qi (β_ E E).hom) (d w : R)
    (hd : QOU.MathlibExt.qDimWith F E = d • 𝟙 (𝟙_ C))
    (hw : closeLeft (R := R) (η_ F E) ((β_ F E).hom ≫ ε_ F E) E (β_ E E).hom = w • 𝟙 E) :
    LeftTrace (HeckeCrossing.ofBraiding (R := R) E hquad) :=
  closureLeftTrace _ rfl (η_ F E) ((β_ F E).hom ≫ ε_ F E) d w hd hw

/-- **The closure of a braid in a braided category is the Markov trace.**  If the braiding on `E`
is a Hecke crossing, the loop `d` is invertible and the curl is `w`, then the normalised closure
of all strands agrees with every Markov trace family of parameter `z = w d⁻¹` on the Hecke tower
(for instance the Ocneanu trace). -/
theorem braided_closure_eq_markov {q qi : R} (E F : C) [ExactPairing F E]
    (hquad : IsHeckeQuad q qi (β_ E E).hom) (d w dinv : R) (hdinv : d * dinv = 1)
    (hd : QOU.MathlibExt.qDimWith F E = d • 𝟙 (𝟙_ C))
    (hw : closeLeft (R := R) (η_ F E) ((β_ F E).hom ≫ ε_ F E) E (β_ E E).hom = w • 𝟙 E)
    (s : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (hs : s (𝟙 _) = 1)
    (T : HeckeCoset.MarkovTraceFamily R q qi (w * dinv)) (n : ℕ) (x : Hecke R q qi n) :
    dinv ^ (n + 1) * s ((braidedLeftTrace E F hquad d w hd hw).fullTr (n + 1)
        ((HeckeCrossing.ofBraiding (R := R) E hquad).revAction n x)) = T.tr n x :=
  (braidedLeftTrace E F hquad d w hd hw).markovFamily_eq s hs dinv hdinv T n x

end LinearClosure

end QOU.OrientedSkein
