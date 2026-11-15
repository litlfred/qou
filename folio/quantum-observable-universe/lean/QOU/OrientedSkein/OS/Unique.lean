/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.OS.Universal

/-!
# `QOU.OrientedSkein.OS.Unique` — uniqueness of the lift up to monoidal isomorphism

Stage 3e of the formalisation of the oriented skein category `OS(z, t)` (issue #7703).

`QOU.OrientedSkein.OS.Universal` builds, for every oriented skein datum `D` on `E, F` in an
`R`-linear monoidal category `𝒞`, a strong monoidal functor `lift D : OS(z, t) ⥤ 𝒞` sending the
universal datum to `D`, and proves it is the only linear functor agreeing with it on objects and
layers. This file proves the stronger, isomorphism-invariant form of uniqueness: **every**
`R`-linear monoidal functor `G : OS(z, t) ⥤ 𝒞` that sends the universal datum to `D` along chosen
isomorphisms `eE : G E ≅ E`, `eF : G F ≅ F` is isomorphic to `lift D` by a monoidal natural
isomorphism.

"Sends the universal datum to `D`" means four commuting squares, one per generator
(`SendsS`, `SendsT`, `SendsCoev`, `SendsEv`): the image under `G` of `S`, `T`, the coevaluation and
the evaluation, transported along the tensorator of `G` and `eE`, `eF`, is the corresponding
morphism of `D`.

## Main results

* `cmp G eE eF w : G ⟨w⟩ ≅ obj E F w` — the comparison, built letter by letter.
* `cmp_tensor` — the comparison intertwines the tensorator of `G` with the canonical
  `obj (a ++ b) ≅ obj a ⊗ obj b`.
* `cmp_natural` — the comparison is natural on every morphism of `OS` (generation by layers).
* `liftIso` — the natural isomorphism `G ≅ lift D`, and `liftIso_isMonoidal`: it is monoidal.

Sorry-free.

## References

* [brundan2017] J. Brundan, *Representations of the oriented skein category*, arXiv 1712.08953,
  Theorem 1.1.
-/

namespace QOU.OrientedSkein.OS

open CategoryTheory MonoidalCategory

universe v u

set_option linter.unusedSectionVars false

noncomputable section

variable {R : Type*} [CommRing R] {q qi t δ : R}
variable {𝒞 : Type u} [Category.{v} 𝒞] [Preadditive 𝒞] [Linear R 𝒞]
  [MonoidalCategory 𝒞] [MonoidalPreadditive 𝒞] [MonoidalLinear R 𝒞]
variable {E F : 𝒞} [ExactPairing F E]
variable (G : OSCat q qi t δ ⥤ 𝒞) [G.Monoidal]
variable (eE : G.obj (OSCat.E q qi t δ) ≅ E) (eF : G.obj (OSCat.F q qi t δ) ≅ F)

/-- The comparison on a single letter. -/
def colIso : (b : Bool) → G.obj (⟨[b]⟩ : OSCat q qi t δ) ≅ col E F b
  | true => eE
  | false => eF

/-- The comparison `G ⟨w⟩ ≅ obj E F w`, built letter by letter from the tensorator of `G`. -/
def cmp : (w : Word) → G.obj (⟨w⟩ : OSCat q qi t δ) ≅ obj E F w
  | [] => (Functor.Monoidal.εIso G).symm
  | b :: w => (Functor.Monoidal.μIso G ⟨[b]⟩ ⟨w⟩).symm ≪≫ tensorIso (colIso G eE eF b) (cmp w)

theorem cmp_nil : (cmp G eE eF []).hom = Functor.OplaxMonoidal.η G := rfl

theorem cmp_cons (b : Bool) (w : Word) : (cmp G eE eF (b :: w)).hom =
    Functor.OplaxMonoidal.δ G ⟨[b]⟩ ⟨w⟩ ≫ ((colIso G eE eF b).hom ⊗ₘ (cmp G eE eF w).hom) := rfl

theorem map_canon {X Y : OSCat q qi t δ} (h : X = Y) (h' : X.w = Y.w) :
    G.map (canon h') = eqToHom (congrArg G.obj h) := by
  subst h; exact G.map_id X

theorem cmp_single (b : Bool) :
    (cmp G eE eF [b]).hom = (colIso G eE eF b).hom ≫ (ρ_ _).inv := by
  have h := Functor.Monoidal.map_rightUnitor G (⟨[b]⟩ : OSCat q qi t δ)
  rw [rightUnitor_hom, map_canon G rfl] at h
  have h2 : Functor.OplaxMonoidal.δ G (⟨[b]⟩ : OSCat q qi t δ) ⟨[]⟩ ≫
      G.obj ⟨[b]⟩ ◁ Functor.OplaxMonoidal.η G = (ρ_ (G.obj ⟨[b]⟩)).inv :=
    calc _ = (Functor.OplaxMonoidal.δ G (⟨[b]⟩ : OSCat q qi t δ) (𝟙_ _) ≫
          G.obj ⟨[b]⟩ ◁ Functor.OplaxMonoidal.η G ≫ (ρ_ (G.obj ⟨[b]⟩)).hom) ≫
            (ρ_ (G.obj ⟨[b]⟩)).inv := by
          simp only [Category.assoc, Iso.hom_inv_id, Category.comp_id]; rfl
      _ = _ := by rw [← h, eqToHom_refl, Category.id_comp]
  rw [cmp_cons, cmp_nil, tensorHom_def', ← Category.assoc, h2]
  simp

/-- `cmp` is monoidal: it intertwines the tensorator of `G` with `μ`. -/
theorem cmp_tensor (a b : Word) : (cmp G eE eF (a ++ b)).hom =
    Functor.OplaxMonoidal.δ G ⟨a⟩ ⟨b⟩ ≫ ((cmp G eE eF a).hom ⊗ₘ (cmp G eE eF b).hom) ≫
      (μ E F a b).inv := by
  induction a with
  | nil =>
      have h := Functor.Monoidal.map_leftUnitor G (⟨b⟩ : OSCat q qi t δ)
      rw [leftUnitor_hom, map_canon G rfl, eqToHom_refl] at h
      simp only [List.nil_append, μ_nil, Iso.symm_inv, cmp_nil, tensorHom_def, Category.assoc]
      erw [leftUnitor_naturality]
      calc (cmp G eE eF b).hom = 𝟙 _ ≫ (cmp G eE eF b).hom := (Category.id_comp _).symm
        _ = _ := by erw [h]; simp only [Category.assoc]; rfl
  | cons x a ih =>
      have h := Functor.OplaxMonoidal.associativity G (⟨[x]⟩ : OSCat q qi t δ) ⟨a⟩ ⟨b⟩
      rw [associator_hom, map_canon G rfl, eqToHom_refl, Category.id_comp] at h
      simp only [List.cons_append, cmp_cons, ih, μ_cons, Iso.trans_inv, Iso.symm_inv,
        whiskerLeftIso_inv]
      have h' := h =≫ ((colIso G eE eF x).hom ⊗ₘ ((cmp G eE eF a).hom ⊗ₘ (cmp G eE eF b).hom)) ≫
        col E F x ◁ (μ E F a b).inv
      simp only [Category.assoc] at h'
      rw [← associator_naturality_assoc] at h'
      have hR : ∀ {A B C D' : 𝒞} {W : 𝒞} (f : A ⟶ B) (g : B ⟶ C) (k : W ⟶ D'),
          (f ≫ g) ⊗ₘ k = f ▷ W ≫ (g ⊗ₘ k) := by
        intros; rw [← tensorHom_id, tensorHom_comp_tensorHom, Category.id_comp]
      have hL : ∀ {A B C D' W V : 𝒞} (e : W ⟶ V) (f : A ⟶ B) (g : B ⟶ C) (k : C ⟶ D'),
          e ⊗ₘ (f ≫ g ≫ k) = W ◁ f ≫ (e ⊗ₘ g) ≫ V ◁ k := by
        intros; rw [← id_tensorHom, ← id_tensorHom, tensorHom_comp_tensorHom,
          tensorHom_comp_tensorHom, Category.id_comp, Category.comp_id]
      rw [hR, hL]
      simp only [Category.assoc]
      exact h'.symm

/-- Naturality of `cmp` survives whiskering on the left. -/
theorem cmp_whiskerLeft (l : Word) {x y : Word} (f : (⟨x⟩ : OSCat q qi t δ) ⟶ ⟨y⟩)
    (φ : obj E F x ⟶ obj E F y)
    (hf : G.map f ≫ (cmp G eE eF y).hom = (cmp G eE eF x).hom ≫ φ) :
    G.map ((⟨l⟩ : OSCat q qi t δ) ◁ f) ≫ (cmp G eE eF (l ++ y)).hom =
      (cmp G eE eF (l ++ x)).hom ≫ (μ E F l x).hom ≫ (obj E F l ◁ φ) ≫ (μ E F l y).inv := by
  rw [Functor.Monoidal.map_whiskerLeft, cmp_tensor, cmp_tensor]
  simp only [Category.assoc, Iso.inv_hom_id_assoc, Functor.Monoidal.μ_δ_assoc]
  rw [whiskerLeft_comp_tensorHom_assoc, hf, ← tensorHom_comp_whiskerLeft_assoc]

/-- Naturality of `cmp` survives whiskering on the right. -/
theorem cmp_whiskerRight (r : Word) {x y : Word} (f : (⟨x⟩ : OSCat q qi t δ) ⟶ ⟨y⟩)
    (φ : obj E F x ⟶ obj E F y)
    (hf : G.map f ≫ (cmp G eE eF y).hom = (cmp G eE eF x).hom ≫ φ) :
    G.map (f ▷ (⟨r⟩ : OSCat q qi t δ)) ≫ (cmp G eE eF (y ++ r)).hom =
      (cmp G eE eF (x ++ r)).hom ≫ (μ E F x r).hom ≫ (φ ▷ obj E F r) ≫ (μ E F y r).inv := by
  rw [Functor.Monoidal.map_whiskerRight, cmp_tensor, cmp_tensor]
  simp only [Category.assoc, Iso.inv_hom_id_assoc, Functor.Monoidal.μ_δ_assoc]
  rw [whiskerRight_comp_tensorHom_assoc, hf, ← tensorHom_comp_whiskerRight_assoc]

variable (D : OrientedSkeinDatum q qi t δ E F)

/-- `G` sends the universal crossing `S` to `D`'s, along `eE`. -/
def SendsS : Prop :=
  G.map (OSCat.cross q qi t δ).S ≫ Functor.OplaxMonoidal.δ G _ _ ≫ (eE.hom ⊗ₘ eE.hom) =
    Functor.OplaxMonoidal.δ G _ _ ≫ (eE.hom ⊗ₘ eE.hom) ≫ D.cross.S

/-- `G` sends the universal mixed crossing `T` to `D`'s, along `eE` and `eF`. -/
def SendsT : Prop :=
  G.map (OSCat.datum q qi t δ).T ≫ Functor.OplaxMonoidal.δ G _ _ ≫ (eE.hom ⊗ₘ eF.hom) =
    Functor.OplaxMonoidal.δ G _ _ ≫ (eF.hom ⊗ₘ eE.hom) ≫ D.T

/-- `G` sends the universal coevaluation to `η_ F E`, along `eE` and `eF`. -/
def SendsCoev : Prop :=
  G.map (η_ (OSCat.F q qi t δ) (OSCat.E q qi t δ)) ≫ Functor.OplaxMonoidal.δ G _ _ ≫
      (eF.hom ⊗ₘ eE.hom) = Functor.OplaxMonoidal.η G ≫ η_ F E

/-- `G` sends the universal evaluation to `ε_ F E`, along `eE` and `eF`. -/
def SendsEv : Prop :=
  G.map (ε_ (OSCat.F q qi t δ) (OSCat.E q qi t δ)) ≫ Functor.OplaxMonoidal.η G =
    Functor.OplaxMonoidal.δ G _ _ ≫ (eE.hom ⊗ₘ eF.hom) ≫ ε_ F E

variable {G eE eF D}

theorem cmp_pair (b b' : Bool) : (cmp G eE eF [b, b']).hom =
    Functor.OplaxMonoidal.δ G ⟨[b]⟩ ⟨[b']⟩ ≫ ((colIso G eE eF b).hom ⊗ₘ (colIso G eE eF b').hom) ≫
      col E F b ◁ (ρ_ _).inv := by
  rw [cmp_cons, cmp_single, tensorHom_comp_whiskerLeft]

/-- `cmp` is natural on every generator. -/
theorem cmp_gen (hS : SendsS G eE D) (hT : SendsT G eE eF D) (hC : SendsCoev G eE eF)
    (hD : SendsEv G eE eF) (g : Gen) :
    G.map (OSCat.gen g : (⟨g.src⟩ : OSCat q qi t δ) ⟶ _) ≫ (cmp G eE eF g.tgt).hom =
      (cmp G eE eF g.src).hom ≫ genHom D g := by
  cases g <;> simp only [Gen.src, Gen.tgt, cmp_pair, cmp_nil, genHom, colIso, col,
    Category.assoc, ← whiskerLeft_comp_assoc, Iso.inv_hom_id, whiskerLeft_id, Category.id_comp]
  · exact (reassoc_of% hS) _
  · exact (reassoc_of% hT) _
  · exact (reassoc_of% hC) _
  · exact hD

/-- `cmp` is natural on every layer. -/
theorem cmp_layer (hS : SendsS G eE D) (hT : SendsT G eE eF D) (hC : SendsCoev G eE eF)
    (hD : SendsEv G eE eF) (s : Step) :
    G.map (layer s : (⟨s.src⟩ : OSCat q qi t δ) ⟶ _) ≫ (cmp G eE eF s.tgt).hom =
      (cmp G eE eF s.src).hom ≫ (lift D).map (layer s) := by
  obtain ⟨l, g, r⟩ := s
  have h := cmp_whiskerLeft G eE eF l _ _
    (cmp_whiskerRight G eE eF r _ _ (cmp_gen hS hT hC hD g))
  rw [lift_layer, layer_eq]
  simpa only [Category.assoc] using h

/-- `cmp` is natural on every morphism of `OS`. -/
theorem cmp_natural [G.Additive] [G.Linear R] (hS : SendsS G eE D) (hT : SendsT G eE eF D)
    (hC : SendsCoev G eE eF) (hD : SendsEv G eE eF) {X Y : OSCat q qi t δ} (f : X ⟶ Y) :
    G.map f ≫ (cmp G eE eF Y.w).hom = (cmp G eE eF X.w).hom ≫ (lift D).map f := by
  refine hom_induction
    (P := fun {X Y} f => G.map f ≫ (cmp G eE eF Y.w).hom = (cmp G eE eF X.w).hom ≫ (lift D).map f)
    ?_ ?_ ?_ ?_ ?_ (cmp_layer hS hT hC hD) f
  · intro X Y
    simp only [CategoryTheory.Functor.map_zero, Limits.zero_comp, Limits.comp_zero]
  · intro X Y f g hf hg
    simp only [CategoryTheory.Functor.map_add, Preadditive.add_comp, Preadditive.comp_add, hf, hg]
  · intro X Y c f hf
    simp only [Functor.map_smul, Linear.smul_comp, Linear.comp_smul, hf]
  · intro X Y Z f g hf hg
    rw [G.map_comp, (lift D).map_comp, Category.assoc, hg, reassoc_of% hf]
  · intro X Y h
    subst h
    simp only [eqToHom_refl, CategoryTheory.Functor.map_id, Category.id_comp]
    exact (Category.comp_id _).symm

variable (G eE eF D) in
/-- **Uniqueness up to monoidal isomorphism.** An `R`-linear monoidal functor out of `OS(z, t)`
that sends the universal datum to `D` along `eE : G E ≅ E` and `eF : G F ≅ F` is isomorphic to
`lift D`, by the natural isomorphism built letter by letter from the tensorator of `G`. -/
def liftIso [G.Additive] [G.Linear R] (hS : SendsS G eE D) (hT : SendsT G eE eF D)
    (hC : SendsCoev G eE eF) (hD : SendsEv G eE eF) : G ≅ lift D :=
  NatIso.ofComponents (fun X => cmp G eE eF X.w) (fun f => cmp_natural hS hT hC hD f)

/-- The comparison `liftIso` is a monoidal natural transformation. -/
instance liftIso_isMonoidal [G.Additive] [G.Linear R] (hS : SendsS G eE D)
    (hT : SendsT G eE eF D) (hC : SendsCoev G eE eF) (hD : SendsEv G eE eF) :
    NatTrans.IsMonoidal (liftIso G eE eF D hS hT hC hD).hom where
  unit := by
    show Functor.LaxMonoidal.ε G ≫ (cmp G eE eF []).hom = 𝟙 _
    rw [cmp_nil, Functor.Monoidal.ε_η]
  tensor X Y := by
    show Functor.LaxMonoidal.μ G X Y ≫ (cmp G eE eF (X.w ++ Y.w)).hom =
      ((cmp G eE eF X.w).hom ⊗ₘ (cmp G eE eF Y.w).hom) ≫ (μ E F X.w Y.w).inv
    rw [cmp_tensor, Functor.Monoidal.μ_δ_assoc]

end

end QOU.OrientedSkein.OS
