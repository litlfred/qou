/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.Model.GLnDatum

/-!
# `QOU.OrientedSkein.Model.GLnClosure` — the skein closure of the `GL_n` datum is the quantum trace

Open item 1 of dispatch B (PR #7705, bean `qou-slck`): trace compatibility.

For an oriented skein datum `D` on `E, F` in any `R`-linear monoidal category, closing the
leftmost (upward) strand of `f : E ⊗ Y ⟶ E ⊗ Y` uses only the datum's own cup and cap:

`closeD D Y f = cupL η Y ≫ F ◁ f ≫ capL (T ≫ ε) Y`,

with `η : 𝟙 ⟶ F ⊗ E` the cup (Brundan's `C`), and `T ≫ ε : F ⊗ E ⟶ 𝟙` the leftward cap (Brundan's
`D ∘ T`).  This is the same picture as `QOU.OrientedSkein.BraidedClosure.closeLeft`, but without a
braiding: the cap is built from the datum's `T`.

For the `GL_n` datum on `R^n` (`QOU.OrientedSkein.Model.GLnDatum.datum`) we prove

`closeD (datum q qi h) Y f = qi^n • ptr (wt n q qi) Y f`   (`closeD_datum_eq`),

i.e. the skein closure **is** the weighted quantum partial trace of `GLnTrace`, up to the global
scalar `qi^n = t⁻¹`.  The computation:

* the cup is `∑_c (y ↦ e_c ⊗ (e_c ⊗ y))` (`cupL_coev`);
* the leftward cap `T ≫ ε` sends `e_a ⊗ e_b` to `δ_{ab}` times the column sum
  `∑_c (A⁻¹)_{c a}` (`capT_ee`); and the column sums of `A⁻¹` are `qi^n w_a` (`colsum_eq`), because
  `∑_d w_d A_{d a} = q^n` is exactly the curl identity `GLnTrace.curl_sum`;
* hence the closure is `∑_c qi^n w_c (ι_c ≫ f ≫ π_c)`.

Consequently (`closeLeftTrace`) the datum's closure is itself a left trace for the crossing, with
loop value `qi^n [n]_q` and curl value `1`, and its normalised full closure is the Markov trace with
the same parameter `z = q^n/[n]_q`.

## Transport through the lift

That `glnFunctor` (the lift `OS(z, t) ⥤ ModuleCat R`) carries the closure computed *inside `OS`*
to `closeD datum` is `QOU.OrientedSkein.Model.GLnClosureLift.glnFunctor_closeD`.

Sorry-free; no axioms beyond Lean/Mathlib's.
-/

namespace QOU.OrientedSkein

open CategoryTheory MonoidalCategory

universe v u

section General

variable {R : Type*} [CommRing R]
variable {C : Type u} [Category.{v} C] [Preadditive C] [Linear R C]
  [MonoidalCategory C] [MonoidalPreadditive C] [MonoidalLinear R C]
variable {E F : C}

/-- A cup on the left of `Y`: `Y ⟶ F ⊗ (E ⊗ Y)`. -/
def cupL (u : 𝟙_ C ⟶ F ⊗ E) (Y : C) : Y ⟶ F ⊗ (E ⊗ Y) :=
  (λ_ Y).inv ≫ u ▷ Y ≫ (α_ F E Y).hom

/-- A cap on the left of `Y`: `F ⊗ (E ⊗ Y) ⟶ Y`. -/
def capL (c : F ⊗ E ⟶ 𝟙_ C) (Y : C) : F ⊗ (E ⊗ Y) ⟶ Y :=
  (α_ F E Y).inv ≫ c ▷ Y ≫ (λ_ Y).hom

/-- **The skein closure of the leftmost strand** for an oriented skein datum: cup `η`, then `f` on
the right of `F`, then the leftward cap `T ≫ ε`. -/
def closeD {q qi t δ : R} [ExactPairing F E] (D : OrientedSkeinDatum q qi t δ E F) (Y : C) :
    (E ⊗ Y ⟶ E ⊗ Y) →ₗ[R] (Y ⟶ Y) where
  toFun f := cupL (η_ F E) Y ≫ F ◁ f ≫ capL (D.T ≫ ε_ F E) Y
  map_add' f g := by
    rw [MonoidalPreadditive.whiskerLeft_add, Preadditive.add_comp, Preadditive.comp_add]
  map_smul' r f := by
    rw [MonoidalLinear.whiskerLeft_smul, Linear.smul_comp, Linear.comp_smul, RingHom.id_apply]

theorem closeD_apply {q qi t δ : R} [ExactPairing F E] (D : OrientedSkeinDatum q qi t δ E F)
    (Y : C) (f : E ⊗ Y ⟶ E ⊗ Y) :
    closeD D Y f = cupL (η_ F E) Y ≫ F ◁ f ≫ capL (D.T ≫ ε_ F E) Y := rfl

end General

namespace GLn

variable {R : Type u} [CommRing R] {n : ℕ} (q qi : R)

/-! ## The cup and the cap on `R^n` -/

theorem ins_rem_ne {i j : Fin n} (hij : i ≠ j) (Y : ModuleCat.{u} R) : ins i Y ≫ rem j Y = 0 := by
  ext y
  simp [ins_apply, rem_apply, e_apply, hij]

theorem coev_whiskerRight_apply' (Y : ModuleCat.{u} R) (x : TensorProduct R R Y) :
    (coev (R := R) (n := n) ▷ Y).hom x =
      (LinearMap.toSpanSingleton R (XX R n) casimir).rTensor Y x := rfl

set_option synthInstance.maxHeartbeats 200000 in
/-- The cup on the left of `Y` is `∑_c (y ↦ e_c ⊗ (e_c ⊗ y))`. -/
theorem cupL_coev (Y : ModuleCat.{u} R) :
    cupL (η_ (X R n) (X R n)) Y = ∑ c : Fin n, ins2 (c, c) Y := by
  ext y
  rw [ModuleCat.hom_sum, LinearMap.coeFn_sum, Finset.sum_apply]
  change (α_ (X R n) (X R n) Y).hom.hom ((coev (R := R) (n := n) ▷ Y).hom
    ((λ_ Y).inv.hom y)) = _
  rw [hom_lu_inv_apply, TensorProduct.lid_symm_apply, coev_whiskerRight_apply',
    LinearMap.rTensor_tmul, LinearMap.toSpanSingleton_apply, one_smul, casimir,
    TensorProduct.sum_tmul, hom_assoc_apply, map_sum]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [TensorProduct.assoc_tmul, ins2_apply]

/-- The column sums of `A⁻¹`. -/
noncomputable def colsum (a : Fin n) : R := ∑ c : Fin n, (A n q qi)⁻¹ c a

/-- **The column sums of `A⁻¹` are the quantum weights**, rescaled: `∑_c (A⁻¹)_{c a} = qi^n w_a`.
This is the curl identity `∑_d w_d A_{d a} = q^n` read as `w^T A = q^n 1^T`. -/
theorem colsum_eq (h : q * qi = 1) (a : Fin n) : colsum q qi a = qi ^ n * wt n q qi a := by
  have hv : Matrix.vecMul (fun d => qi ^ n * wt n q qi d) (A n q qi) = fun _ => 1 := by
    funext a
    simp only [Matrix.vecMul, dotProduct, A_apply, mul_assoc, ← Finset.mul_sum, curl_sum]
    rw [← mul_pow, mul_comm qi q, h, one_pow]
  have key : Matrix.vecMul (fun _ => (1 : R)) (A n q qi)⁻¹ = fun d => qi ^ n * wt n q qi d := by
    rw [← hv, Matrix.vecMul_vecMul, Matrix.mul_nonsing_inv _ (isUnit_det_A q qi h),
      Matrix.vecMul_one]
  have := congrFun key a
  simpa [Matrix.vecMul, dotProduct, colsum] using this

/-- The leftward cap `T ≫ ε` on basis vectors. -/
theorem capT_ee (a b : Fin n) :
    (Tm q qi ≫ ev).hom (e a ⊗ₜ e b : XX R n) = if a = b then colsum q qi a else 0 := by
  rw [ModuleCat.hom_comp, LinearMap.comp_apply, Tm_ee, tv]
  by_cases hab : a = b
  · subst hab
    simp only [if_true, map_sum, map_smul]
    change ∑ c, (A n q qi)⁻¹ c a • evLin (e c ⊗ₜ e c : XX R n) = _
    simp [evLin_ee, colsum]
  · rw [if_neg hab, if_neg hab]
    change evLin (e b ⊗ₜ e a : XX R n) = _
    rw [evLin_ee, if_neg (Ne.symm hab)]

theorem capT_whiskerRight_apply (Y : ModuleCat.{u} R) (x : TensorProduct R (XX R n) Y) :
    ((Tm q qi ≫ ev) ▷ Y).hom x = ((Tm q qi ≫ ev).hom.rTensor Y) x := rfl

/-- The leftward cap on the left of `Y` is `∑_a colsum_a · (x₁ ⊗ (x₂ ⊗ y) ↦ x₁_a x₂_a y)`. -/
theorem capL_capT (Y : ModuleCat.{u} R) :
    capL (Tm q qi ≫ ev) Y = ∑ a : Fin n, colsum q qi a • rem2 (a, a) Y := by
  apply hom_ext_left2
  intro a b y
  rw [ModuleCat.hom_sum, LinearMap.coeFn_sum, Finset.sum_apply]
  simp only [ModuleCat.hom_smul, LinearMap.smul_apply, rem2_apply]
  change (λ_ Y).hom.hom (((Tm q qi ≫ ev) ▷ Y).hom ((α_ (X R n) (X R n) Y).inv.hom
    (e a ⊗ₜ (e b ⊗ₜ y : TensorProduct R (X R n) Y) :
      TensorProduct R (X R n) (TensorProduct R (X R n) Y)))) = _
  rw [hom_assoc_inv_apply, TensorProduct.assoc_symm_tmul, capT_whiskerRight_apply,
    LinearMap.rTensor_tmul]
  erw [capT_ee]
  rw [hom_lu_apply]
  by_cases hab : a = b
  · subst hab
    rw [Finset.sum_eq_single a (fun c _ hc => by simp [Ne.symm hc]) (by simp)]
    simp
  · rw [if_neg hab, TensorProduct.zero_tmul, map_zero]
    refine (Finset.sum_eq_zero fun x _ => ?_).symm
    rw [if_neg (fun hx => hab ((Prod.ext_iff.mp hx).1.trans (Prod.ext_iff.mp hx).2.symm)),
      smul_zero]

/-! ## The closure is the weighted partial trace -/

/-- **Trace compatibility.**  The skein closure of the `GL_n` datum (cup `η`, leftward cap
`T ≫ ε`) is `qi^n` times the weighted quantum partial trace of `GLnTrace`. -/
theorem closeD_datum_eq (h : q * qi = 1) (Y : ModuleCat.{u} R) (f : X R n ⊗ Y ⟶ X R n ⊗ Y) :
    closeD (datum (n := n) q qi h) Y f = qi ^ n • ptr (wt n q qi) Y f := by
  rw [closeD_apply, datum_T, evaluation_eq, cupL_coev, capL_capT q qi]
  simp only [Preadditive.sum_comp, Preadditive.comp_sum, Linear.comp_smul, ins2, rem2,
    Category.assoc]
  have hw : ∀ c d : Fin n, ins c Y ≫ ins c (X R n ⊗ Y) ≫ X R n ◁ f ≫ rem d (X R n ⊗ Y) ≫
      rem d Y = if c = d then ins c Y ≫ f ≫ rem c Y else 0 := by
    intro c d
    rw [← Category.assoc (ins c (X R n ⊗ Y)), ins_whisker, Category.assoc,
      ← Category.assoc (ins c (X R n ⊗ Y)) _ _]
    by_cases hcd : c = d
    · subst hcd
      rw [ins_rem, Category.id_comp, if_pos rfl]
    · rw [if_neg hcd]
      simp [ins_rem_ne hcd]
  simp only [hw, smul_ite, smul_zero, Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.mem_univ,
    if_true, ptr_apply, Finset.smul_sum, smul_smul, colsum_eq q qi h]

/-- **The datum's own closure is a left trace** for the crossing, with loop value `qi^n [n]_q`
and curl `1`; its Markov parameter is again `q^n / [n]_q`. -/
noncomputable def closeLeftTrace (h : q * qi = 1) : LeftTrace (crossing (n := n) q qi h) where
  ptr := closeD (datum (n := n) q qi h)
  ptr_whisker_comp g f := by
    rw [closeD_datum_eq, closeD_datum_eq, ptr_whisker_comp, Linear.comp_smul]
  ptr_comp_whisker g f := by
    rw [closeD_datum_eq, closeD_datum_eq, ptr_comp_whisker, Linear.smul_comp]
  d := qi ^ n * ∑ i, wt n q qi i
  w := 1
  ptr_id Y := by
    rw [closeD_datum_eq, ptr_id, smul_smul]
  ptr_cross Y := by
    rw [closeD_datum_eq, show (crossing (n := n) q qi h).S = S q qi from rfl, ptr_cross,
      smul_smul, ← mul_pow, mul_comm qi q, h, one_pow]
  ptr2_conj Y f := by
    simp only [closeD_datum_eq, map_smul, crossing_S, ptr2_conj]

end GLn

end QOU.OrientedSkein
