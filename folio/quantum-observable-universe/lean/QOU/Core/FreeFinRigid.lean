import Mathlib.Algebra.Category.ModuleCat.Monoidal.Symmetric
import Mathlib.CategoryTheory.Monoidal.Subcategory
import Mathlib.CategoryTheory.Monoidal.Rigid.Braided
import Mathlib.LinearAlgebra.Contraction
import Mathlib.RingTheory.TensorProduct.Finite
import Mathlib.LinearAlgebra.FreeModule.Finite.Basic

/-!
# Free finite modules over a commutative ring form a rigid category

`FreeFinModuleCat R` is the full monoidal subcategory of `ModuleCat R` on the
modules that are free of finite rank.  Mathlib's `FGModuleCat` is rigid only over
a field (its coevaluation is built from `Basis.ofVectorSpace`); this file
repeats that construction over an arbitrary commutative ring, using
`Module.Free.chooseBasis` in place of a vector-space basis.  Duals are
`Module.Dual R V`, evaluation is `contractLeft`, coevaluation is
`1 ↦ Σ bᵢ ⊗ bᵢ*`.  The left-rigid half comes from the symmetric braiding.

Pure algebra over `R`: no field, no ordering, no analytic input.  Built for the
QOU witness programme (bean `qou-aawz`): a QOU needs a *rigid* `R`-linear
category, and `ModuleCat R` is not rigid.
-/

open CategoryTheory MonoidalCategory TensorProduct Module

universe w

namespace QOU.FreeFin

variable (R : Type w) [CommRing R]

/-- Free and finite `R`-modules. -/
def isFreeFin : ObjectProperty (ModuleCat.{w} R) :=
  fun M => Module.Free R M ∧ Module.Finite R M

instance : (isFreeFin R).IsMonoidal where
  prop_unit := ⟨inferInstanceAs (Module.Free R R), inferInstanceAs (Module.Finite R R)⟩
  prop_tensor X Y hX hY := by
    obtain ⟨h1, h2⟩ := hX; obtain ⟨h3, h4⟩ := hY
    exact ⟨inferInstanceAs (Module.Free R (X ⊗[R] Y)), inferInstanceAs (Module.Finite R (X ⊗[R] Y))⟩

abbrev FreeFinModuleCat := (isFreeFin R).FullSubcategory

variable {R}

section coev
variable (V : Type w) [AddCommGroup V] [Module R V] [Module.Free R V] [Module.Finite R V]

/-- Coevaluation over a commutative ring, for a free finite module. -/
noncomputable def coevalFree : R →ₗ[R] V ⊗[R] Module.Dual R V :=
  LinearMap.toSpanSingleton R _
    (∑ i, (Module.Free.chooseBasis R V) i ⊗ₜ[R] (Module.Free.chooseBasis R V).coord i)

theorem coevalFree_one : coevalFree V 1 =
    ∑ i, (Module.Free.chooseBasis R V) i ⊗ₜ[R] (Module.Free.chooseBasis R V).coord i := by
  simp [coevalFree]

theorem contractLeft_assoc_coevalFree :
    (contractLeft R V).rTensor _ ∘ₗ
        (TensorProduct.assoc R _ _ _).symm.toLinearMap ∘ₗ
          (coevalFree V).lTensor (Module.Dual R V) =
      (TensorProduct.lid R _).symm.toLinearMap ∘ₗ (TensorProduct.rid R _).toLinearMap := by
  classical
  apply TensorProduct.ext
  apply (Module.Free.chooseBasis R V).dualBasis.ext; intro j; apply LinearMap.ext_ring
  rw [LinearMap.compr₂_apply, LinearMap.compr₂_apply, TensorProduct.mk_apply]
  simp only [LinearMap.coe_comp, Function.comp_apply, LinearEquiv.coe_toLinearMap]
  rw [rid_tmul, one_smul, lid_symm_apply]
  simp only [LinearMap.lTensor_tmul, coevalFree_one]
  rw [TensorProduct.tmul_sum, map_sum]; simp only [assoc_symm_tmul]
  rw [map_sum]; simp only [LinearMap.rTensor_tmul, contractLeft_apply]
  simp only [Basis.coe_dualBasis, Basis.coord_apply, Basis.repr_self_apply, TensorProduct.ite_tmul]
  rw [Finset.sum_ite_eq']; simp only [Finset.mem_univ, if_true]

theorem contractLeft_assoc_coevalFree' :
    (contractLeft R V).lTensor _ ∘ₗ
        (TensorProduct.assoc R _ _ _).toLinearMap ∘ₗ (coevalFree V).rTensor V =
      (TensorProduct.rid R _).symm.toLinearMap ∘ₗ (TensorProduct.lid R _).toLinearMap := by
  classical
  apply TensorProduct.ext
  apply LinearMap.ext_ring; apply (Module.Free.chooseBasis R V).ext; intro j
  rw [LinearMap.compr₂_apply, LinearMap.compr₂_apply, TensorProduct.mk_apply]
  simp only [LinearMap.coe_comp, Function.comp_apply, LinearEquiv.coe_toLinearMap]
  rw [lid_tmul, one_smul, rid_symm_apply]
  simp only [LinearMap.rTensor_tmul, coevalFree_one]
  rw [TensorProduct.sum_tmul, map_sum]; simp only [assoc_tmul]
  rw [map_sum]; simp only [LinearMap.lTensor_tmul, contractLeft_apply]
  simp only [Basis.coord_apply, Basis.repr_self_apply, TensorProduct.tmul_ite]
  rw [Finset.sum_ite_eq]; simp only [Finset.mem_univ, if_true]

end coev

variable (V : FreeFinModuleCat R)

instance : Module.Free R V.obj := V.2.1
instance : Module.Finite R V.obj := V.2.2

noncomputable def dual : FreeFinModuleCat R :=
  ⟨ModuleCat.of R (Module.Dual R V.obj), inferInstanceAs (Module.Free R (Module.Dual R V.obj)),
    inferInstanceAs (Module.Finite R (Module.Dual R V.obj))⟩

noncomputable def coeval : 𝟙_ (FreeFinModuleCat R) ⟶ V ⊗ dual V :=
  ModuleCat.ofHom <| coevalFree V.obj

noncomputable def eval : dual V ⊗ V ⟶ 𝟙_ (FreeFinModuleCat R) :=
  ModuleCat.ofHom <| contractLeft R V.obj

private theorem coevaluation_evaluation :
    letI V' : FreeFinModuleCat R := dual V
    V' ◁ coeval V ≫ (α_ V' V V').inv ≫ eval V ▷ V' =
      (ρ_ V').hom ≫ (λ_ V').inv := by
  ext : 1
  apply contractLeft_assoc_coevalFree V.obj

private theorem evaluation_coevaluation :
    coeval V ▷ V ≫ (α_ V (dual V) V).hom ≫ V ◁ eval V =
      (λ_ V).hom ≫ (ρ_ V).inv := by
  ext : 1
  apply contractLeft_assoc_coevalFree' V.obj

noncomputable instance exactPairing : ExactPairing V (dual V) where
  coevaluation' := coeval V
  evaluation' := eval V
  coevaluation_evaluation' := coevaluation_evaluation V
  evaluation_coevaluation' := evaluation_coevaluation V

noncomputable instance rightDual : HasRightDual V := ⟨dual V⟩

noncomputable instance rightRigidCategory : RightRigidCategory (FreeFinModuleCat R) where

noncomputable example : RigidCategory (FreeFinModuleCat R) := inferInstance


section lin
variable {X Y Z X' Y' : FreeFinModuleCat R}

/-- A linear map as a morphism of `FreeFinModuleCat`. -/
def fh (f : X.obj →ₗ[R] Y.obj) : X ⟶ Y := ModuleCat.ofHom f

lemma fh_comp (f : X.obj →ₗ[R] Y.obj) (g : Y.obj →ₗ[R] Z.obj) :
    fh f ≫ fh g = fh (g ∘ₗ f) := rfl

lemma fh_tensorHom (f : X.obj →ₗ[R] X'.obj) (g : Y.obj →ₗ[R] Y'.obj) :
    (fh f ⊗ₘ fh g) = (fh (TensorProduct.map f g) : X ⊗ Y ⟶ X' ⊗ Y') := rfl

lemma fh_whiskerLeft (f : Y.obj →ₗ[R] Y'.obj) :
    X ◁ fh f = (fh (LinearMap.lTensor X.obj f) : X ⊗ Y ⟶ X ⊗ Y') := rfl

lemma fh_whiskerRight (f : X.obj →ₗ[R] X'.obj) :
    fh f ▷ Y = (fh (LinearMap.rTensor Y.obj f) : X ⊗ Y ⟶ X' ⊗ Y) := rfl

lemma assoc_hom_eq : (α_ X Y Z).hom =
    fh (X := (X ⊗ Y) ⊗ Z) (Y := X ⊗ (Y ⊗ Z))
      (TensorProduct.assoc R X.obj Y.obj Z.obj).toLinearMap := rfl
lemma assoc_inv_eq : (α_ X Y Z).inv =
    fh (X := X ⊗ (Y ⊗ Z)) (Y := (X ⊗ Y) ⊗ Z)
      (TensorProduct.assoc R X.obj Y.obj Z.obj).symm.toLinearMap := rfl
lemma leftUnitor_hom_eq : (λ_ X).hom =
    fh (X := 𝟙_ _ ⊗ X) (Y := X) (TensorProduct.lid R X.obj).toLinearMap := rfl
lemma leftUnitor_inv_eq : (λ_ X).inv =
    fh (X := X) (Y := 𝟙_ _ ⊗ X) (TensorProduct.lid R X.obj).symm.toLinearMap := rfl
lemma rightUnitor_hom_eq : (ρ_ X).hom =
    fh (X := X ⊗ 𝟙_ _) (Y := X) (TensorProduct.rid R X.obj).toLinearMap := rfl
lemma rightUnitor_inv_eq : (ρ_ X).inv =
    fh (X := X) (Y := X ⊗ 𝟙_ _) (TensorProduct.rid R X.obj).symm.toLinearMap := rfl
lemma braiding_hom_eq : (β_ X Y).hom =
    fh (X := X ⊗ Y) (Y := Y ⊗ X) (TensorProduct.comm R X.obj Y.obj).toLinearMap := rfl
lemma id_eq : 𝟙 X = fh LinearMap.id := rfl

lemma fh_inj {f g : X.obj →ₗ[R] Y.obj} (h : f = g) : fh f = fh g := by rw [h]

end lin

end QOU.FreeFin
