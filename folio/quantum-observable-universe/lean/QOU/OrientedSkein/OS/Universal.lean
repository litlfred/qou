/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.OS.Datum
import QOU.OrientedSkein.OS.Interpret
import Mathlib.CategoryTheory.Linear.LinearFunctor

/-!
# `QOU.OrientedSkein.OS.Universal` — the universal property of `OS(z, t)`

Stage 3d of the formalisation of the oriented skein category (issue #7703).

Let `𝒞` be an `R`-linear monoidal category and `D` an oriented skein datum on objects `E`, `F`
of `𝒞` (a Hecke crossing `S` on `E`, an exact pairing `F ⊣ E`, a mixed crossing `T` inverse to the
sideways crossing, and the dimension relation).  Then:

* **Existence.** `lift D : OS(z, t) ⥤ 𝒞` is an additive, `R`-linear, monoidal functor
  (`liftCoreMonoidal`), sending the word `w` to the right-nested tensor product `obj E F w`.
* **It sends the universal datum to `D`.** `lift_S`, `lift_T`, `lift_coevaluation`,
  `lift_evaluation`: the images of the generators of `OS` are `S`, `T`, `η`, `ε` of `D`, up to the
  right unitors `col x ⊗ 𝟙 ≅ col x`.
* **Uniqueness.** `hom_induction`: every morphism of `OS` is generated, under sums, scalars and
  composition, by layers, and `layer_eq` identifies a layer with a generator whiskered by
  identities.  Hence (`lift_unique`) an `R`-linear functor that agrees with `lift D` on objects and
  on layers is `lift D`, and `lift_layer` computes the layers from the four generators.

The strictly stronger statement — that any linear monoidal functor sending the universal datum
to `D` is monoidally isomorphic to `lift D` — is `liftIso` in `QOU.OrientedSkein.OS.Unique`.

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
variable {E F : 𝒞} [ExactPairing F E] (D : OrientedSkeinDatum q qi t δ E F)

/-- The interpretation kills the relation submodule. -/
theorem interp_rels {x y : Word} {f : PA R} (hf : f ∈ rels q qi t δ x y) :
    interp D x y f = 0 := by
  induction hf using Submodule.span_induction with
  | mem f hf =>
      obtain ⟨ρ, a, b, π, π', h, h', rfl⟩ := hf
      have hρ := whiskA_mem_supp a b (ρ.rel_mem q qi t δ)
      rw [interp_mul D (mul_mem_supp (pth_mem_supp h) hρ) (pth_mem_supp h'),
        interp_mul D (pth_mem_supp h) hρ, interp_whiskA D a b (ρ.rel_mem q qi t δ), interp_rel]
      simp
  | zero => simp
  | add f g _ _ hf hg => simp [hf, hg]
  | smul c f _ hf => simp [hf]

/-- The interpretation on hom-modules of `OS`. -/
def liftHom (x y : Word) : HomQ q qi t δ x y →ₗ[R] (obj E F x ⟶ obj E F y) :=
  (relsIn q qi t δ x y).liftQ (interp D x y ∘ₗ (supp R x y).subtype)
    (fun f hf => by
      rw [LinearMap.mem_ker, LinearMap.comp_apply, Submodule.coe_subtype]
      exact interp_rels D (Submodule.mem_comap.mp hf))

/-- **The lift** of an oriented skein datum `D` to a functor out of `OS(z, t)`. -/
def lift : OSCat q qi t δ ⥤ 𝒞 where
  obj X := obj E F X.w
  map {X Y} f := liftHom D X.w Y.w f
  map_id X := interp_one D X.w
  map_comp {X Y Z} f g := by
    obtain ⟨f, hf, rfl⟩ := homMk_surjective f
    obtain ⟨g, hg, rfl⟩ := homMk_surjective g
    exact interp_mul D hf hg

theorem lift_obj (X : OSCat q qi t δ) : (lift D).obj X = obj E F X.w := rfl

theorem lift_homMk {X Y : OSCat q qi t δ} {f : PA R} (hf : f ∈ supp R X.w Y.w) :
    (lift D).map (homMk f hf) = interp D X.w Y.w f := rfl

instance : (lift D).Additive where
  map_add {X Y f g} := (liftHom D X.w Y.w).map_add f g

instance : (lift D).Linear R where
  map_smul {X Y} f r := (liftHom D X.w Y.w).map_smul r f

/-- Transport of the interpretation along equalities of words. -/
theorem interp_congr {x x' y y' : Word} (hx : x = x') (hy : y = y') (f : PA R) :
    interp D x' y' f = eqToHom (congrArg (obj E F) hx.symm) ≫ interp D x y f ≫
      eqToHom (congrArg (obj E F) hy) := by
  subst hx hy; simp

/-- The lift of a canonical morphism is the transport along the equality of words. -/
theorem lift_canon {X Y : OSCat q qi t δ} (h : X.w = Y.w) :
    (lift D).map (canon h) = eqToHom (congrArg (obj E F) h) := by
  rw [lift_homMk, ← pth_nil, interp_pth D (show Valid X.w [] Y.w from h)]
  rfl

/-- The lift of a right whiskering. -/
theorem lift_whiskerRight {X Y : OSCat q qi t δ} (f : X ⟶ Y) (Z : OSCat q qi t δ) :
    (lift D).map (f ▷ Z) = (μ E F X.w Z.w).hom ≫ ((lift D).map f ▷ obj E F Z.w) ≫
      (μ E F Y.w Z.w).inv := by
  obtain ⟨f, hf, rfl⟩ := homMk_surjective f
  rw [homMk_whiskerRight, lift_homMk, lift_homMk]
  erw [interp_whiskA D [] Z.w hf]
  simp [μ_nil]

/-- The lift of a left whiskering. -/
theorem lift_whiskerLeft (Z : OSCat q qi t δ) {X Y : OSCat q qi t δ} (f : X ⟶ Y) :
    (lift D).map (Z ◁ f) = (μ E F Z.w X.w).hom ≫ (obj E F Z.w ◁ (lift D).map f) ≫
      (μ E F Z.w Y.w).inv := by
  obtain ⟨f, hf, rfl⟩ := homMk_surjective f
  rw [whiskerLeft_homMk, lift_homMk, lift_homMk]
  show interp D (Z.w ++ X.w) (Z.w ++ Y.w) (whiskA Z.w [] f) = _
  rw [interp_congr D (congrArg (Z.w ++ ·) (List.append_nil X.w))
      (congrArg (Z.w ++ ·) (List.append_nil Y.w)),
    interp_whiskA D Z.w [] hf]
  change eqToHom _ ≫ wl E F Z.w (wr E F [] (interp D X.w Y.w f)) ≫ eqToHom _ =
    wl E F Z.w (interp D X.w Y.w f)
  rw [wr_nil, wl_comp, wl_comp, wl_eqToHom _ (List.append_nil X.w),
    wl_eqToHom _ (List.append_nil Y.w).symm]
  simp

/-- The lift is a monoidal functor, with tensorator the canonical isomorphism
`obj a ⊗ obj b ≅ obj (a ++ b)` and identity unitor. -/
def liftCoreMonoidal : (lift D).CoreMonoidal where
  εIso := Iso.refl _
  μIso X Y := (μ E F X.w Y.w).symm
  μIso_hom_natural_left {X Y} f Z := by
    simp [lift_whiskerRight, lift_obj]
  μIso_hom_natural_right Z {X Y} f := by
    simp [lift_whiskerLeft, lift_obj]
  associativity X Y Z := by
    rw [associator_hom, lift_canon]
    simp only [Iso.symm_hom, lift_obj, tensorObj_w]
    rw [← Category.assoc, μ_assoc_inv']
    simp
  left_unitality X := by
    rw [leftUnitor_hom, lift_canon]
    simp [μ_nil, lift_obj]
  right_unitality X := by
    rw [rightUnitor_hom, lift_canon]
    simp [μ_nil_right_inv, lift_obj]

instance : (lift D).Monoidal := (liftCoreMonoidal D).toMonoidal

/-! ## The lift sends the universal datum to `D` -/

/-- The lift of a generator is its interpretation `genHom D g`: `S`, `T`, the cup and the cap of
`D`, conjugated by the right unitors `obj [x] = col x ⊗ 𝟙 ≅ col x`. -/
theorem lift_gen (g : Gen) : (lift D).map (OSCat.gen g : (⟨g.src⟩ : OSCat q qi t δ) ⟶ _) =
    genHom D g := by
  rw [OSCat.gen, lift_homMk, interp_pth D (OSCat.valid_lone g)]
  simp [stepHom, OSCat.lone, wl_nil, wr_nil]

theorem lift_S : (lift D).map (OSCat.cross q qi t δ).S =
    (E ◁ (ρ_ E).hom) ≫ D.cross.S ≫ (E ◁ (ρ_ E).inv) := lift_gen D .S

theorem lift_T : (lift D).map (OSCat.datum q qi t δ).T =
    (F ◁ (ρ_ E).hom) ≫ D.T ≫ (E ◁ (ρ_ F).inv) := lift_gen D .T

theorem lift_coevaluation :
    (lift D).map (η_ (OSCat.F q qi t δ) (OSCat.E q qi t δ)) = η_ F E ≫ (F ◁ (ρ_ E).inv) :=
  lift_gen D .C

theorem lift_evaluation :
    (lift D).map (ε_ (OSCat.F q qi t δ) (OSCat.E q qi t δ)) = (E ◁ (ρ_ F).hom) ≫ ε_ F E :=
  lift_gen D .D

/-! ## Generation by layers, and uniqueness -/

/-- The layer `s` as a morphism of `OS`. -/
def layer (s : Step) : (⟨s.src⟩ : OSCat q qi t δ) ⟶ ⟨s.tgt⟩ :=
  homMk (pth [s]) (pth_mem_supp ⟨rfl, rfl⟩)

/-- A layer is a generator whiskered by identities. -/
theorem layer_eq (l : Word) (g : Gen) (r : Word) :
    (layer ⟨l, g, r⟩ : (⟨Step.src ⟨l, g, r⟩⟩ : OSCat q qi t δ) ⟶ _) =
      (⟨l⟩ : OSCat q qi t δ) ◁ (OSCat.gen g ▷ (⟨r⟩ : OSCat q qi t δ)) := by
  simp only [layer, OSCat.gen, whiskerLeft_homMk, homMk_whiskerRight]
  refine homMk_congr ?_ _ _
  simp [whiskA_pth, OSCat.lone, Step.whisk]

theorem homMk_one_eq_eqToHom {X Y : OSCat q qi t δ} (h : X.w = Y.w) :
    (homMk 1 (one_mem_supp h) : X ⟶ Y) = eqToHom (OSCat.ext h) := by
  cases X; cases Y; cases h; rfl

/-- **Generation.** A property of morphisms of `OS` closed under zero, sums, scalars, composition
and transport along equalities of objects, and holding on every layer, holds on every morphism. -/
theorem hom_induction (P : ∀ {X Y : OSCat q qi t δ}, (X ⟶ Y) → Prop)
    (hzero : ∀ {X Y : OSCat q qi t δ}, P (0 : X ⟶ Y))
    (hadd : ∀ {X Y : OSCat q qi t δ} (f g : X ⟶ Y), P f → P g → P (f + g))
    (hsmul : ∀ {X Y : OSCat q qi t δ} (c : R) (f : X ⟶ Y), P f → P (c • f))
    (hcomp : ∀ {X Y Z : OSCat q qi t δ} (f : X ⟶ Y) (g : Y ⟶ Z), P f → P g → P (f ≫ g))
    (heq : ∀ {X Y : OSCat q qi t δ} (h : X = Y), P (eqToHom h))
    (hlayer : ∀ s : Step, P (layer s : (⟨s.src⟩ : OSCat q qi t δ) ⟶ _))
    {X Y : OSCat q qi t δ} (f : X ⟶ Y) : P f := by
  obtain ⟨f, hf, rfl⟩ := homMk_surjective f
  suffices H : ∃ hf' : f ∈ supp R X.w Y.w, P (homMk f hf' : X ⟶ Y) from H.2
  refine supp_induction (P := fun f => ∃ hf : f ∈ supp R X.w Y.w, P (homMk f hf : X ⟶ Y))
    ⟨zero_mem _, hzero⟩ (fun f g ⟨hf, pf⟩ ⟨hg, pg⟩ => ⟨add_mem hf hg, hadd _ _ pf pg⟩)
    (fun c f ⟨hf, pf⟩ => ⟨Submodule.smul_mem _ c hf, hsmul c _ pf⟩) (fun π hπ => ?_) hf
  refine ⟨pth_mem_supp hπ, ?_⟩
  clear hf
  induction π generalizing X with
  | nil => rw [homMk_congr pth_nil _ (one_mem_supp hπ), homMk_one_eq_eqToHom hπ]; exact heq _
  | cons s π ih =>
      obtain ⟨h1, h2⟩ := hπ
      cases X with
      | mk w =>
        simp only at h1
        subst h1
        rw [homMk_congr (pth_cons s π) _ (mul_mem_supp
          (pth_mem_supp (show Valid s.src [s] s.tgt from ⟨rfl, rfl⟩)) (pth_mem_supp h2)),
          ← homMk_comp (Y := ⟨s.tgt⟩) (pth_mem_supp (show Valid s.src [s] s.tgt from ⟨rfl, rfl⟩))
            (pth_mem_supp h2)]
        exact hcomp _ _ (hlayer s) (ih h2)

/-- The lift of a layer: the interpreted generator, whiskered through the canonical
isomorphisms `μ`. -/
theorem lift_layer (l : Word) (g : Gen) (r : Word) :
    (lift D).map (layer ⟨l, g, r⟩ : (⟨Step.src ⟨l, g, r⟩⟩ : OSCat q qi t δ) ⟶ _) =
      (μ E F l (g.src ++ r)).hom ≫ (obj E F l ◁ ((μ E F g.src r).hom ≫
        (genHom D g ▷ obj E F r) ≫ (μ E F g.tgt r).inv)) ≫ (μ E F l (g.tgt ++ r)).inv := by
  rw [layer_eq, lift_whiskerLeft, lift_whiskerRight, lift_gen]
  rfl

/-- **Uniqueness.** An `R`-linear functor out of `OS(z, t)` that agrees with `lift D` on objects
and on every layer is `lift D`. Together with `lift_layer`, the lift is determined by the images
`genHom D g` of the four generators. -/
theorem lift_unique (G : OSCat q qi t δ ⥤ 𝒞) [G.Additive] [G.Linear R]
    (hobj : ∀ X, G.obj X = (lift D).obj X)
    (hlayer : ∀ s : Step, G.map (layer s : (⟨s.src⟩ : OSCat q qi t δ) ⟶ _) =
      eqToHom (hobj _) ≫ (lift D).map (layer s) ≫ eqToHom (hobj _).symm) :
    G = lift D := by
  refine CategoryTheory.Functor.ext hobj (fun X Y f => ?_)
  refine hom_induction
    (P := fun {X Y} f => G.map f = eqToHom (hobj X) ≫ (lift D).map f ≫ eqToHom (hobj Y).symm)
    ?_ ?_ ?_ ?_ ?_ hlayer f
  · intro X Y; simp
  · intro X Y f g hf hg; simp [hf, hg]
  · intro X Y c f hf; simp [hf, Functor.map_smul]
  · intro X Y Z f g hf hg; simp [hf, hg]
  · intro X Y h; subst h; simp

end

end QOU.OrientedSkein.OS
