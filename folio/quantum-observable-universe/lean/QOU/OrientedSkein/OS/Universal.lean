/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.OS.Datum
import QOU.OrientedSkein.OS.Interpret
import Mathlib.CategoryTheory.Linear.LinearFunctor

/-!
# `QOU.OrientedSkein.OS.Universal` — the universal property of `OS(z, t)`

Stage 3d of the formalisation of the oriented skein category (issue #7703).
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

end

end QOU.OrientedSkein.OS
