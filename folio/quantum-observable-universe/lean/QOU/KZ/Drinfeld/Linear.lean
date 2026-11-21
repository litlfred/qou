import QOU.KZ.Drinfeld.Monoidal
import Mathlib.CategoryTheory.Monoidal.Linear

/-!
# `D_ℏ` is `ℂ`-linear

Stage S5 of bean `qou-zoyv`. Hom-sets of `D_ℏ` are the `sl₂`-equivariant matrices, a `ℂ`-subspace;
composition is matrix multiplication and `⊗` is the Kronecker product, both bilinear. So `D_ℏ` is
preadditive, `ℂ`-linear, and monoidal-linear. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S5)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory MonoidalCategory QOU.KZ.DrinfeldAssociator Obj

/-- The equivariant matrices `X → Y` as a `ℂ`-subspace. -/
def equivSub (X Y : Obj) : Submodule ℂ (Matrix (Idx Y) (Idx X) ℂ) where
  carrier := {f | Equivariant f}
  add_mem' {f g} hf hg a ha := by
    rw [Matrix.mul_add, Matrix.add_mul, hf a ha, hg a ha]
  zero_mem' a _ := by rw [Matrix.mul_zero, Matrix.zero_mul]
  smul_mem' r f hf a ha := by rw [Matrix.mul_smul, Matrix.smul_mul, hf a ha]

instance (X Y : Obj) : AddCommGroup (X ⟶ Y) := inferInstanceAs (AddCommGroup (equivSub X Y))
instance (X Y : Obj) : Module ℂ (X ⟶ Y) := inferInstanceAs (Module ℂ (equivSub X Y))

@[simp] theorem add_val {X Y : Obj} (f g : X ⟶ Y) : (f + g).1 = f.1 + g.1 := rfl
@[simp] theorem smul_val {X Y : Obj} (r : ℂ) (f : X ⟶ Y) : (r • f).1 = r • f.1 := rfl
@[simp] theorem zero_val {X Y : Obj} : (0 : X ⟶ Y).1 = 0 := rfl
@[simp] theorem neg_val {X Y : Obj} (f : X ⟶ Y) : (-f).1 = -f.1 := rfl
@[simp] theorem sub_val {X Y : Obj} (f g : X ⟶ Y) : (f - g).1 = f.1 - g.1 := rfl

instance : Preadditive Obj where
  add_comp _ _ _ f f' g := hom_ext (by simp [comp_val, Matrix.mul_add])
  comp_add _ _ _ f g g' := hom_ext (by simp [comp_val, Matrix.add_mul])

instance : Linear ℂ Obj where
  smul_comp _ _ _ r f g := hom_ext (by simp [comp_val, Matrix.mul_smul])
  comp_smul _ _ _ f r g := hom_ext (by simp [comp_val, Matrix.smul_mul])

variable (Ψ : Associator.{0}) (c : ℂ) [hc : Fact (Transcendental ℚ c)]

instance : Preadditive (DH Ψ c) := inferInstanceAs (Preadditive Obj)
instance : Linear ℂ (DH Ψ c) := inferInstanceAs (Linear ℂ Obj)

instance : MonoidalPreadditive (DH Ψ c) where
  whiskerLeft_zero := hom_ext (by
    show kron (1 : Matrix _ _ ℂ) (0 : Matrix _ _ ℂ) = 0
    ext y x; simp [kron_apply])
  zero_whiskerRight := hom_ext (by
    show kron (0 : Matrix _ _ ℂ) (1 : Matrix _ _ ℂ) = 0
    ext y x; simp [kron_apply])
  whiskerLeft_add f g := hom_ext (kron_add_right _ f.1 g.1)
  add_whiskerRight f g := hom_ext (kron_add_left f.1 g.1 _)

instance : MonoidalLinear ℂ (DH Ψ c) where
  whiskerLeft_smul _ _ _ r f := hom_ext (kron_smul_right r _ f.1)
  smul_whiskerRight r _ _ f _ := hom_ext (kron_smul_left r f.1 _)

end QOU.KZ.Drinfeld
