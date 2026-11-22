import QOU.KZ.Drinfeld.Pentagon
import QOU.KZ.Drinfeld.Natural
import Mathlib.CategoryTheory.Monoidal.Category

/-!
# `D_ℏ` is a monoidal category

Stage S2 of bean `qou-zoyv`. For transcendental `ℏ` (`[Fact (Transcendental ℚ ℏ)]`), the
category `DH ℏ` has:

* objects: tensor words in `V = ℂ²`;
* morphisms: `sl₂`-equivariant matrices;
* `⊗`: the Kronecker product;
* the KZ associator `α_{X,Y,Z} = reidx · Φ_KZ(ℏ t_{X,Y}, ℏ t_{Y,Z})`;
* trivial unitors.

It is a Mathlib `MonoidalCategory`. Pentagon: `pentagon_mat`. Naturality: `natural_mat`.
Triangle: `Φ(0, 0) = 1`.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open CategoryTheory MonoidalCategory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues
  QOU.KZ.DrinfeldAssociator Obj

/-! ### Unitors -/

/-- Legs of `𝟙 ⊗ X`. -/
def leftLegs (X : Obj) : Leaves (tensor unit X) ≃ Leaves X := Equiv.emptySum _ _
/-- Legs of `X ⊗ 𝟙`. -/
def rightLegs (X : Obj) : Leaves (tensor X unit) ≃ Leaves X := Equiv.sumEmpty _ _

theorem equivariant_reidx {X Y : Obj} (e : Leaves X ≃ Leaves Y) :
    Equivariant (X := X) (Y := Y) (reidx e) := by
  intro a _
  rw [ρ_eq_diag, ρ_eq_diag, reidx_diag]

/-- A reindexing as an isomorphism of `D_ℏ`. -/
def reidxIso {X Y : Obj} (e : Leaves X ≃ Leaves Y) : X ≅ Y where
  hom := ⟨reidx e, equivariant_reidx e⟩
  inv := ⟨reidx e.symm, equivariant_reidx e.symm⟩
  hom_inv_id := hom_ext (by
    show reidx e.symm * reidx e = 1
    rw [reidx_mul, Equiv.self_trans_symm, reidx_refl])
  inv_hom_id := hom_ext (by
    show reidx e * reidx e.symm = 1
    rw [reidx_mul, Equiv.symm_trans_self, reidx_refl])

theorem one_unit_apply (x y : Idx unit) : (1 : Matrix (Idx unit) (Idx unit) ℂ) x y = 1 := by
  rw [Matrix.one_apply, if_pos (Subsingleton.elim x y)]

/-- The tensor product of morphisms. -/
def tensHom {X₁ Y₁ X₂ Y₂ : Obj} (f : X₁ ⟶ Y₁) (g : X₂ ⟶ Y₂) : tensor X₁ X₂ ⟶ tensor Y₁ Y₂ :=
  ⟨kron f.1 g.1, equivariant_kron f.2 g.2⟩

theorem leftUnitor_natural {X Y : Obj} (f : X ⟶ Y) :
    reidx (leftLegs Y) * kron (1 : Matrix (Idx unit) (Idx unit) ℂ) f.1 =
      f.1 * reidx (leftLegs X) := by
  ext y x
  rw [reidx_mul_apply, mul_reidx_apply]
  rw [kron_apply, Matrix.one_apply, if_pos (Subsingleton.elim _ _), one_mul]
  rfl

theorem rightUnitor_natural {X Y : Obj} (f : X ⟶ Y) :
    reidx (rightLegs Y) * kron f.1 (1 : Matrix (Idx unit) (Idx unit) ℂ) =
      f.1 * reidx (rightLegs X) := by
  ext y x
  rw [reidx_mul_apply, mul_reidx_apply]
  rw [kron_apply, Matrix.one_apply, if_pos (Subsingleton.elim _ _), mul_one]
  rfl

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable (Ψ : Associator.{0}) {c : ℂ} (hc : Transcendental ℚ c)
include Ψ hc

theorem ΦB_unit (X Y : Obj) : ΦB Ψ hc (blkX X unit Y) (blkY X unit Y) (blkZ X unit Y) = 1 := by
  have h0 : blkY X unit Y = ∅ := by
    rw [blkY, Finset.univ_eq_empty, Finset.map_empty]
  have e₁ : c • tB ℂ 2 (blkX X unit Y) (blkY X unit Y) = 0 := by
    rw [h0, tB]; simp
  have e₂ : c • tB ℂ 2 (blkY X unit Y) (blkZ X unit Y) = 0 := by
    rw [h0, tB]; simp
  rw [ΦB, Ψ.ΦN_congr e₁ e₂ _ _ KZShiftPhi.nonResonant_zero KZShiftPhi.nonResonant_zero,
    Ψ.ΦN_zero_left]

/-- **The triangle** (matrix form). -/
theorem triangle_mat (X Y : Obj) :
    kron (1 : EndL (Leaves X)) (reidx (leftLegs Y)) * αmat Ψ hc X unit Y =
      kron (reidx (rightLegs X)) (1 : EndL (Leaves Y)) := by
  rw [αmat, ΦB_unit, Matrix.mul_one, one_kron_reidx, kron_reidx_one, reidx_mul]
  congr 1
  ext k; rcases k with (k | k) | k
  · rfl
  · exact k.elim
  · rfl

omit Ψ hc

/-! ### The monoidal category -/

/-- The Drinfeld category `D_ℏ` built from the associator `Ψ` (on tensor words in `V = ℂ²`).
With `Ψ = kz` this is the category built from `Φ_KZ`. -/
def DH (Ψ : Associator.{0}) (c : ℂ) : Type := Obj

instance (Ψ : Associator.{0}) (c : ℂ) : Category (DH Ψ c) := inferInstanceAs (Category Obj)

variable (Ψ : Associator.{0}) (c : ℂ) [hc : Fact (Transcendental ℚ c)]

instance : MonoidalCategoryStruct (DH Ψ c) where
  tensorObj X Y := Obj.tensor X Y
  whiskerLeft X _ _ f := tensHom (𝟙 (X : Obj)) f
  whiskerRight f Y := tensHom f (𝟙 (Y : Obj))
  tensorHom f g := tensHom f g
  tensorUnit := Obj.unit
  associator X Y Z :=
    { hom := ⟨αmat Ψ hc.out X Y Z, equivariant_αmat Ψ hc.out X Y Z⟩
      inv := ⟨αinv Ψ hc.out X Y Z, equivariant_αinv Ψ hc.out X Y Z⟩
      hom_inv_id := hom_ext (αinv_mul_αmat Ψ hc.out X Y Z)
      inv_hom_id := hom_ext (αmat_mul_αinv Ψ hc.out X Y Z) }
  leftUnitor X := reidxIso (leftLegs X)
  rightUnitor X := reidxIso (rightLegs X)

/-- **`D_ℏ` is a monoidal category** (`ℏ` transcendental). -/
instance : MonoidalCategory (DH Ψ c) :=
  MonoidalCategory.ofTensorHom
    (id_tensorHom_id := fun X Y => hom_ext (kron_one (α := Leaves X) (α' := Leaves Y)))
    (id_tensorHom := fun _ _ _ _ => rfl)
    (tensorHom_id := fun _ _ => rfl)
    (tensorHom_comp_tensorHom := fun f₁ f₂ g₁ g₂ => hom_ext (kron_mul g₁.1 g₂.1 f₁.1 f₂.1))
    (associator_naturality := fun f₁ f₂ f₃ => hom_ext (natural_mat Ψ hc.out f₁ f₂ f₃))
    (leftUnitor_naturality := fun f => hom_ext (leftUnitor_natural f))
    (rightUnitor_naturality := fun f => hom_ext (rightUnitor_natural f))
    (pentagon := fun W X Y Z => hom_ext (by
      show kron (1 : EndL (Leaves W)) (αmat Ψ hc.out X Y Z) * αmat Ψ hc.out W (tensor X Y) Z *
        kron (αmat Ψ hc.out W X Y) (1 : EndL (Leaves Z)) = _
      rw [Matrix.mul_assoc]
      exact pentagon_mat Ψ hc.out W X Y Z))
    (triangle := fun X Y => hom_ext (by
      show kron (1 : EndL (Leaves X)) (reidx (leftLegs Y)) * αmat Ψ hc.out X unit Y = _
      exact triangle_mat Ψ hc.out X Y))

end QOU.KZ.Drinfeld
