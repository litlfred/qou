import QOU.OrientedSkein.OS.Syntax
import QOU.OrientedSkein.SkeinDatum

namespace QOU.OrientedSkein.OS

open CategoryTheory MonoidalCategory

universe v u

set_option linter.unusedSectionVars false

section Interp

variable {R : Type*} [CommRing R] {q qi t δ : R}
variable {𝒞 : Type u} [Category.{v} 𝒞] [Preadditive 𝒞] [Linear R 𝒞]
  [MonoidalCategory 𝒞] [MonoidalPreadditive 𝒞] [MonoidalLinear R 𝒞]
variable {E F : 𝒞} [ExactPairing F E]

variable (E F) in
/-- The object attached to an orientation: `true ↦ E`, `false ↦ F`. -/
def col : Bool → 𝒞
  | true => E
  | false => F

variable (E F) in
/-- The object attached to a word: the right-nested tensor product of its letters. -/
def obj : Word → 𝒞
  | [] => 𝟙_ 𝒞
  | b :: w => col E F b ⊗ obj w

@[simp] theorem obj_nil : obj E F [] = 𝟙_ 𝒞 := rfl
@[simp] theorem obj_cons (b : Bool) (w : Word) : obj E F (b :: w) = col E F b ⊗ obj E F w := rfl

variable (E F) in
/-- The canonical isomorphism `obj (a ++ b) ≅ obj a ⊗ obj b`. -/
def μ : (a b : Word) → (obj E F (a ++ b) ≅ obj E F a ⊗ obj E F b)
  | [], b => (λ_ (obj E F b)).symm
  | x :: a, b => whiskerLeftIso (col E F x) (μ a b) ≪≫ (α_ _ _ _).symm

theorem μ_nil (b : Word) : μ E F [] b = (λ_ (obj E F b)).symm := rfl
theorem μ_cons (x : Bool) (a b : Word) :
    μ E F (x :: a) b = whiskerLeftIso (col E F x) (μ E F a b) ≪≫ (α_ _ _ _).symm := rfl

theorem eqToHom_cons (x : Bool) {w w' : Word} (h : w = w')
    (h' : obj E F (x :: w) = obj E F (x :: w')) :
    eqToHom h' = col E F x ◁ eqToHom (congrArg (obj E F) h) := by
  subst h; simp

/-- Associativity of `μ`. -/
@[reassoc]
theorem μ_assoc (a b c : Word) :
    (μ E F a (b ++ c)).hom ≫ (obj E F a ◁ (μ E F b c).hom) =
      eqToHom (congrArg (obj E F) (List.append_assoc a b c).symm) ≫ (μ E F (a ++ b) c).hom ≫
        ((μ E F a b).hom ▷ obj E F c) ≫ (α_ _ _ _).hom := by
  induction a with
  | nil =>
      simp only [μ_nil, Iso.symm_hom, eqToHom_refl, Category.id_comp, List.nil_append]
      monoidal
  | cons x a ih =>
      rw [eqToHom_cons x (List.append_assoc a b c).symm]
      simp only [μ_cons, Iso.trans_hom, whiskerLeftIso_hom, Iso.symm_hom, comp_whiskerRight,
        Category.assoc, obj_cons]
      sorry

end Interp

end QOU.OrientedSkein.OS
