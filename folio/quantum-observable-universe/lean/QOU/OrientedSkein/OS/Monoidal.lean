/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.OS.Category
import Mathlib.CategoryTheory.Monoidal.Linear
import Mathlib.Tactic.NoncommRing

/-!
# `QOU.OrientedSkein.OS.Monoidal` — the monoidal structure on the oriented skein category

Stage 3b (continued) of the formalisation of the oriented skein category `OS(z, t)`
(issue #7703).

Tensor product of objects is concatenation of words, whiskering is `whiskA` on representatives,
and the associator and unitors are the empty string `1 : PA R` viewed as a morphism between two
words that are equal (`(x y) z = x (y z)`, `[] x = x`, `x [] = x`).  Because validity of a
string is a proposition about words, the empty string is a morphism between *any* two equal
words, so no `eqToHom` appears.

All the axioms of a monoidal category except the interchange law hold already in the path algebra.
The interchange law is the one place where relations are needed: it is proved for single layers
from the defining relation `Rel.ichg g g' m` and propagated to strings and then to linear
combinations (`ichg_step`, `ichg_path`, `ichg_supp`).

## Main statements

* `ichg_supp` — the interchange law holds modulo the relations.
* `OSCat.instMonoidalCategory`, with `MonoidalPreadditive` and `MonoidalLinear R`.

Sorry-free.

## References

* [brundan2017] J. Brundan, *Representations of the oriented skein category*, arXiv 1712.08953,
  Theorem 1.1.
-/

namespace QOU.OrientedSkein.OS

open CategoryTheory MonoidalCategory

noncomputable section

variable {R : Type*} [CommRing R] {q qi t δ : R}

/-! ## Interchange in the path algebra -/

theorem pth_cons (s : Step) (π : List Step) : (pth (s :: π) : PA R) = pth [s] * pth π := by
  rw [pth_mul]; rfl

theorem pth_mem_supp' {x y : Word} {π : List Step} {x' y' : Word} (h : Valid x' π y')
    (hx : x = x') (hy : y = y') : (pth π : PA R) ∈ supp R x y := by
  subst hx hy; exact pth_mem_supp h

theorem sub_mul_mem_rels {x y z : Word} {u v p : PA R} (h : u - v ∈ rels q qi t δ x y)
    (hp : p ∈ supp R y z) : u * p - v * p ∈ rels q qi t δ x z := by
  rw [← sub_mul]; exact mul_mem_rels_left h hp

theorem mul_sub_mem_rels {w x y : Word} {u v p : PA R} (hp : p ∈ supp R w x)
    (h : u - v ∈ rels q qi t δ x y) : p * u - p * v ∈ rels q qi t δ w y := by
  rw [← mul_sub]; exact mul_mem_rels_right hp h

/-- Interchange of two single layers side by side, from the relation `Rel.ichg`. -/
theorem ichg_layer (s s' : Step) :
    (pth [s.whisk [] s'.src] * pth [s'.whisk s.tgt []] -
      pth [s'.whisk s.src []] * pth [s.whisk [] s'.tgt] : PA R) ∈
      rels q qi t δ (s.src ++ s'.src) (s.tgt ++ s'.tgt) := by
  have h := whiskA_rel_mem_rels (q := q) (qi := qi) (t := t) (δ := δ) (Rel.ichg s.g s'.g (s.r ++ s'.l))
    s.l s'.r (x := s.src ++ s'.src) (y := s.tgt ++ s'.tgt)
    (by simp [Rel.src, Step.src]) (by simp [Rel.tgt, Step.tgt])
  convert h using 1
  simp only [Rel.rel, Rel.lhs, Rel.rhs, map_sub, whiskA_pth, pth_mul]
  congr 2 <;> simp [Step.whisk, Step.src, Step.tgt]

/-- Interchange of one layer past a string. -/
theorem ichg_step (s : Step) : ∀ (π' : List Step) {b1 b2 : Word}, Valid b1 π' b2 →
    (pth [s.whisk [] b1] * pth (π'.map (Step.whisk s.tgt [])) -
      pth (π'.map (Step.whisk s.src [])) * pth [s.whisk [] b2] : PA R) ∈
      rels q qi t δ (s.src ++ b1) (s.tgt ++ b2)
  | [], b1, b2, h => by
      subst h; simp only [List.map_nil, pth_nil, mul_one, one_mul, sub_self]; exact zero_mem _
  | s' :: ρ, b1, b2, h => by
      obtain ⟨rfl, hρ⟩ := h
      have key := ichg_layer (q := q) (qi := qi) (t := t) (δ := δ) s s'
      have ih := ichg_step s ρ hρ
      have hP : (pth (ρ.map (Step.whisk s.tgt [])) : PA R) ∈ supp R (s.tgt ++ s'.tgt) (s.tgt ++ b2) :=
        pth_mem_supp' (hρ.whisk s.tgt []) (by simp) (by simp)
      have hc : (pth [s'.whisk s.src []] : PA R) ∈ supp R (s.src ++ s'.src) (s.src ++ s'.tgt) :=
        pth_mem_supp' (x' := s.src ++ (s'.src ++ [])) (y' := s.src ++ (s'.tgt ++ []))
          (Valid.whisk s.src [] (π := [s']) ⟨rfl, rfl⟩) (by simp) (by simp)
      have := Submodule.add_mem _ (sub_mul_mem_rels key hP) (mul_sub_mem_rels hc ih)
      convert this using 1
      rw [List.map_cons, List.map_cons, pth_cons _ (ρ.map (Step.whisk s.tgt [])),
        pth_cons _ (ρ.map (Step.whisk s.src []))]
      noncomm_ring

/-- Interchange of two strings side by side. -/
theorem ichg_path : ∀ (π : List Step) {a1 a2 : Word}, Valid a1 π a2 →
    ∀ (π' : List Step) {b1 b2 : Word}, Valid b1 π' b2 →
    (pth (π.map (Step.whisk [] b1)) * pth (π'.map (Step.whisk a2 [])) -
      pth (π'.map (Step.whisk a1 [])) * pth (π.map (Step.whisk [] b2)) : PA R) ∈
      rels q qi t δ (a1 ++ b1) (a2 ++ b2)
  | [], a1, a2, h, π', b1, b2, h' => by
      subst h; simp only [List.map_nil, pth_nil, mul_one, one_mul, sub_self]; exact zero_mem _
  | s :: ρ, a1, a2, h, π', b1, b2, h' => by
      obtain ⟨rfl, hρ⟩ := h
      have ih := ichg_path ρ hρ π' h'
      have st := ichg_step (q := q) (qi := qi) (t := t) (δ := δ) s π' h'
      have hx : (pth [s.whisk [] b1] : PA R) ∈ supp R (s.src ++ b1) (s.tgt ++ b1) :=
        pth_mem_supp' (x' := [] ++ (s.src ++ b1)) (y' := [] ++ (s.tgt ++ b1))
          (Valid.whisk [] b1 (π := [s]) ⟨rfl, rfl⟩) rfl rfl
      have hw : (pth (ρ.map (Step.whisk [] b2)) : PA R) ∈ supp R (s.tgt ++ b2) (a2 ++ b2) :=
        pth_mem_supp' (hρ.whisk [] b2) rfl rfl
      have := Submodule.add_mem _ (mul_sub_mem_rels hx ih) (sub_mul_mem_rels st hw)
      convert this using 1
      rw [List.map_cons, List.map_cons, pth_cons _ (ρ.map (Step.whisk [] b1)),
        pth_cons _ (ρ.map (Step.whisk [] b2))]
      noncomm_ring

/-- **The interchange law** in the path algebra, modulo the relations. -/
theorem ichg_supp {a1 a2 b1 b2 : Word} {g h : PA R} (hg : g ∈ supp R a1 a2)
    (hh : h ∈ supp R b1 b2) :
    whiskA [] b1 g * whiskA a2 [] h - whiskA a1 [] h * whiskA [] b2 g ∈
      rels q qi t δ (a1 ++ b1) (a2 ++ b2) := by
  refine supp_induction (P := fun g => whiskA [] b1 g * whiskA a2 [] h -
    whiskA a1 [] h * whiskA [] b2 g ∈ rels q qi t δ (a1 ++ b1) (a2 ++ b2)) (by simp)
    (fun g g' hg hg' => ?_) (fun c g hg => ?_) (fun π hπ => ?_) hg
  · beta_reduce at *
    convert Submodule.add_mem _ hg hg' using 1
    simp only [map_add, add_mul, mul_add]; abel
  · beta_reduce at *
    convert Submodule.smul_mem _ c hg using 1
    simp only [map_smul, smul_mul_assoc, mul_smul_comm, smul_sub]
  refine supp_induction (P := fun h => whiskA [] b1 (pth π) * whiskA a2 [] h -
    whiskA a1 [] h * whiskA [] b2 (pth π) ∈ rels q qi t δ (a1 ++ b1) (a2 ++ b2)) (by simp)
    (fun h h' hh hh' => ?_) (fun c h hh => ?_) (fun π' hπ' => ?_) hh
  · beta_reduce at *
    convert Submodule.add_mem _ hh hh' using 1
    simp only [map_add, add_mul, mul_add]; abel
  · beta_reduce at *
    convert Submodule.smul_mem _ c hh using 1
    simp only [map_smul, smul_mul_assoc, mul_smul_comm, smul_sub]
  · beta_reduce
    rw [whiskA_pth, whiskA_pth, whiskA_pth, whiskA_pth]
    exact ichg_path π hπ π' hπ'

/-! ## Whiskering on hom-modules -/

/-- Whiskering on representatives, as a linear map `supp x y →ₗ supp x' y'`. -/
def whiskS (a b : Word) {x y x' y' : Word} (hx : x' = a ++ (x ++ b)) (hy : y' = a ++ (y ++ b)) :
    supp R x y →ₗ[R] supp R x' y' :=
  ((whiskA a b).comp (supp R x y).subtype).codRestrict _
    fun f => whiskA_mem_supp' a b hx hy f.2

@[simp] theorem whiskS_apply (a b : Word) {x y x' y' : Word} (hx : x' = a ++ (x ++ b))
    (hy : y' = a ++ (y ++ b)) (f : supp R x y) :
    ((whiskS a b hx hy f : supp R x' y') : PA R) = whiskA a b f.1 := rfl

@[simp] theorem mulS_apply {x y z : Word} (f : supp R x y) (g : supp R y z) :
    ((mulS x y z f g : supp R x z) : PA R) = f.1 * g.1 := rfl

variable (q qi t δ) in
/-- Whiskering on hom-modules. -/
def whiskQ (a b : Word) {x y x' y' : Word} (hx : x' = a ++ (x ++ b)) (hy : y' = a ++ (y ++ b)) :
    HomQ q qi t δ x y →ₗ[R] HomQ q qi t δ x' y' :=
  Submodule.mapQ _ _ (whiskS a b hx hy) fun _ hf => whiskA_mem_rels' a b hx hy hf

theorem whiskQ_mk (a b : Word) {x y x' y' : Word} (hx : x' = a ++ (x ++ b))
    (hy : y' = a ++ (y ++ b)) {f : PA R} (hf : f ∈ supp R x y) :
    whiskQ q qi t δ a b hx hy (mk f hf) = mk (whiskA a b f) (whiskA_mem_supp' a b hx hy hf) := rfl

/-! ## The monoidal structure -/

/-- The empty string, as a morphism between two equal words. -/
abbrev canon {X Y : OSCat q qi t δ} (h : X.w = Y.w) : X ⟶ Y := homMk 1 (one_mem_supp h)

/-- The empty string, as an isomorphism between two equal words. -/
def canonIso {X Y : OSCat q qi t δ} (h : X.w = Y.w) : X ≅ Y where
  hom := canon h
  inv := canon h.symm
  hom_inv_id := mk_congr (one_mul 1) _ _
  inv_hom_id := mk_congr (one_mul 1) _ _

instance : MonoidalCategoryStruct (OSCat q qi t δ) where
  tensorObj X Y := ⟨X.w ++ Y.w⟩
  whiskerLeft X {_ _} f := whiskQ q qi t δ X.w [] (by simp) (by simp) f
  whiskerRight {_ _} f Y := whiskQ q qi t δ [] Y.w rfl rfl f
  tensorUnit := ⟨[]⟩
  associator X Y Z := canonIso (List.append_assoc X.w Y.w Z.w)
  leftUnitor X := canonIso (List.nil_append X.w)
  rightUnitor X := canonIso (List.append_nil X.w)

@[simp] theorem tensorObj_w (X Y : OSCat q qi t δ) : (X ⊗ Y).w = X.w ++ Y.w := rfl

@[simp] theorem tensorUnit_w : (𝟙_ (OSCat q qi t δ)).w = [] := rfl

theorem whiskerLeft_homMk (X : OSCat q qi t δ) {Y Z : OSCat q qi t δ} {f : PA R}
    (hf : f ∈ supp R Y.w Z.w) :
    X ◁ (homMk f hf : Y ⟶ Z) =
      homMk (whiskA X.w [] f) (whiskA_mem_supp' X.w [] (by simp) (by simp) hf) := rfl

theorem homMk_whiskerRight {X Y : OSCat q qi t δ} (Z : OSCat q qi t δ) {f : PA R}
    (hf : f ∈ supp R X.w Y.w) :
    (homMk f hf : X ⟶ Y) ▷ Z = homMk (whiskA [] Z.w f) (whiskA_mem_supp' [] Z.w rfl rfl hf) := rfl

theorem associator_hom (X Y Z : OSCat q qi t δ) :
    (α_ X Y Z).hom = canon (List.append_assoc X.w Y.w Z.w) := rfl

theorem associator_inv (X Y Z : OSCat q qi t δ) :
    (α_ X Y Z).inv = canon (List.append_assoc X.w Y.w Z.w).symm := rfl

theorem leftUnitor_hom (X : OSCat q qi t δ) : (λ_ X).hom = canon (List.nil_append X.w) := rfl
theorem leftUnitor_inv (X : OSCat q qi t δ) : (λ_ X).inv = canon (List.nil_append X.w).symm := rfl
theorem rightUnitor_hom (X : OSCat q qi t δ) : (ρ_ X).hom = canon (List.append_nil X.w) := rfl
theorem rightUnitor_inv (X : OSCat q qi t δ) :
    (ρ_ X).inv = canon (List.append_nil X.w).symm := rfl

/-- Two morphisms given by equal representatives are equal. -/
theorem homMk_congr {X Y : OSCat q qi t δ} {f g : PA R} (hfg : f = g) (hf : f ∈ supp R X.w Y.w)
    (hg : g ∈ supp R X.w Y.w) : (homMk f hf : X ⟶ Y) = homMk g hg :=
  mk_congr hfg hf hg

/-- The interchange law in `OS`. -/
theorem whisker_exchange' {W X Y Z : OSCat q qi t δ} (f : W ⟶ X) (g : Y ⟶ Z) :
    W ◁ g ≫ f ▷ Z = f ▷ Y ≫ X ◁ g := by
  obtain ⟨f, hf, rfl⟩ := homMk_surjective f
  obtain ⟨g, hg, rfl⟩ := homMk_surjective g
  simp only [whiskerLeft_homMk, homMk_whiskerRight, homMk_comp]
  refine (homMk_eq_homMk _ _ ?_).symm
  exact ichg_supp hf hg

theorem whiskerLeft_comp' (X : OSCat q qi t δ) {Y Z W : OSCat q qi t δ} (f : Y ⟶ Z) (g : Z ⟶ W) :
    X ◁ (f ≫ g) = X ◁ f ≫ X ◁ g := by
  obtain ⟨f, hf, rfl⟩ := homMk_surjective f
  obtain ⟨g, hg, rfl⟩ := homMk_surjective g
  exact homMk_congr (whiskA_mul _ _ _ _) _ _

theorem comp_whiskerRight' {X Y Z : OSCat q qi t δ} (f : X ⟶ Y) (g : Y ⟶ Z) (W : OSCat q qi t δ) :
    (f ≫ g) ▷ W = f ▷ W ≫ g ▷ W := by
  obtain ⟨f, hf, rfl⟩ := homMk_surjective f
  obtain ⟨g, hg, rfl⟩ := homMk_surjective g
  exact homMk_congr (whiskA_mul _ _ _ _) _ _

/-- Normalise a goal about whiskered representatives in the path algebra. -/
macro "pa_simp" : tactic =>
  `(tactic| simp only [whiskS_apply, mulS_apply, LinearMap.comp_apply, Submodule.coe_subtype,
      LinearMap.codRestrict_apply, tensorObj_w, tensorUnit_w, whiskA_mul, whiskA_whiskA, whiskA_one, whiskA_nil, List.append_nil,
      List.nil_append, List.append_assoc, mul_one, one_mul, mul_assoc])

instance instMonoidalCategory : MonoidalCategory (OSCat q qi t δ) where
  tensorHom_def _ _ := rfl
  id_tensorHom_id X₁ X₂ := homMk_congr (by pa_simp) _ _
  tensorHom_comp_tensorHom {X₁ Y₁ Z₁ X₂ Y₂ Z₂} f₁ f₂ g₁ g₂ := by
    change (f₁ ▷ X₂ ≫ Y₁ ◁ f₂) ≫ (g₁ ▷ Y₂ ≫ Z₁ ◁ g₂) = (f₁ ≫ g₁) ▷ X₂ ≫ Z₁ ◁ (f₂ ≫ g₂)
    rw [comp_whiskerRight', whiskerLeft_comp', Category.assoc, ← Category.assoc (Y₁ ◁ f₂),
      whisker_exchange' g₁ f₂]
    simp only [Category.assoc]
  whiskerLeft_id X Y := homMk_congr (by pa_simp) _ _
  id_whiskerRight X Y := homMk_congr (by pa_simp) _ _
  associator_naturality {X₁ X₂ X₃ Y₁ Y₂ Y₃} f₁ f₂ f₃ := by
    obtain ⟨f₁, hf₁, rfl⟩ := homMk_surjective f₁
    obtain ⟨f₂, hf₂, rfl⟩ := homMk_surjective f₂
    obtain ⟨f₃, hf₃, rfl⟩ := homMk_surjective f₃
    exact homMk_congr (by pa_simp) _ _
  leftUnitor_naturality {X Y} f := by
    obtain ⟨f, hf, rfl⟩ := homMk_surjective f
    exact homMk_congr (by pa_simp) _ _
  rightUnitor_naturality {X Y} f := by
    obtain ⟨f, hf, rfl⟩ := homMk_surjective f
    exact homMk_congr (by pa_simp) _ _
  pentagon W X Y Z := homMk_congr (by pa_simp) _ _
  triangle X Y := homMk_congr (by pa_simp) _ _

instance : MonoidalPreadditive (OSCat q qi t δ) where
  whiskerLeft_zero {X Y Z} := (whiskQ q qi t δ X.w [] (by simp) (by simp)).map_zero
  zero_whiskerRight {X Y Z} := (whiskQ q qi t δ [] X.w (x := Y.w) (y := Z.w) rfl rfl).map_zero
  whiskerLeft_add {X Y Z} f g := (whiskQ q qi t δ X.w [] (by simp) (by simp)).map_add f g
  add_whiskerRight {X Y Z} f g := (whiskQ q qi t δ [] X.w rfl rfl).map_add f g

instance : MonoidalLinear R (OSCat q qi t δ) where
  whiskerLeft_smul X {Y Z} c f := (whiskQ q qi t δ X.w [] (by simp) (by simp)).map_smul c f
  smul_whiskerRight c {X Y} f Z := (whiskQ q qi t δ [] Z.w rfl rfl).map_smul c f

end

end QOU.OrientedSkein.OS
