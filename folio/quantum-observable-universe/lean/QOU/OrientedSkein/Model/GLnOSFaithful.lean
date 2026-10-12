/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.Model.GLnFaithful
import QOU.OrientedSkein.Model.GLnClosureLift

/-!
# `QOU.OrientedSkein.Model.GLnOSFaithful` — the Hecke algebra embeds in `End_{OS}(E^{⊗r})`, `r ≤ n`

Dispatch B follow-up (PR #7705, bean `qou-slck`): faithfulness inside the oriented skein category.

Brundan's `ι_r : H_r(q) → End_{OS(z,t)}(E^{⊗r})` (`HeckeCrossing.heckeAction` of the universal
crossing `OSCat.cross`) is **injective** for `r ≤ n` in `OS(q, qi, q^n, [n]_q)`, over any commutative
ring with `q * qi = 1` (`OS_heckeAction_injective`).  So `OS` is nondegenerate in every degree
`r ≤ n`: `End(E^{⊗r})` contains a copy of `H_r(q)`.

## Proof

* `Φ k : glnFunctor (E^{⊗k}) ≅ (R^n)^{⊗k}` is built by whiskering the identity: the lift sends the
  word `[true, …, true]` to `R^n ⊗ (⋯ ⊗ 𝟙)` definitionally, but not syntactically for variable `k`.
* `map_gen`: the lift of the OS crossing on strands `i, i+1` is `Φ ≫ (GL_n crossing on strands
  i, i+1) ≫ Φ⁻¹`, by induction on the strand index: the left-whisker step (`map_gen_succ`) and the
  base step (`map_gen_zero`) reduce, after expanding the lift's tensorator `OS.μ` and `lift_S`
  and one naturality square, to coherence (`monoidal`).
* `lift_heckeAction`: hence `glnFunctor ∘ ι_{m+1} = conj_Φ ∘ ρ_{m+1}` as algebra maps
  (`Hecke.hom_ext`), where `ρ` is the `GL_n` action.
* `ρ_{m+1}` is injective for `m + 1 ≤ n` (`GLnFaithful.heckeAction_injective`) and `conj_Φ` is
  injective, so `ι_{m+1}` is.

Sorry-free; no axioms beyond Lean/Mathlib's.

## References

* [brundan2017] J. Brundan, *Representations of the oriented skein category*, arXiv 1712.08953,
  §1.4 (the map `ι_r`).
-/

open CategoryTheory MonoidalCategory Functor.LaxMonoidal Functor.OplaxMonoidal QOU.OrientedSkein.OS
namespace QOU.OrientedSkein.GLn
universe u
variable {R : Type u} [CommRing R] {n : ℕ} (q qi : R) (h : q * qi = 1)

local notation "𝒪" => OSCat q qi (q ^ n) (∑ i, wt n q qi i)
local notation "EO" => OSCat.E q qi (q ^ n) (∑ i, wt n q qi i)

/-- `G (E^{⊗k}) ≅ X^{⊗k}`, componentwise identity up to the definitional unfolding of words. -/
noncomputable def Φ : (k : ℕ) → ((glnFunctor (n := n) q qi h).obj (tpow EO k) ≅ tpow (X R n) k)
  | 0 => Iso.refl (𝟙_ (ModuleCat.{u} R))
  | k + 1 => whiskerLeftIso (X R n) (Φ k)

theorem Φ_succ_hom (k : ℕ) : (Φ q qi h (k + 1)).hom = X R n ◁ (Φ q qi h k).hom := rfl
theorem Φ_succ_inv (k : ℕ) : (Φ q qi h (k + 1)).inv = X R n ◁ (Φ q qi h k).inv := rfl

theorem map_gen_succ (k : ℕ) (j : Fin k) (g : tpow EO (k + 1) ⟶ tpow EO (k + 1))
    (ih : (glnFunctor (n := n) q qi h).map g =
      (Φ q qi h (k + 1)).hom ≫ (crossing (n := n) q qi h).gen k j ≫ (Φ q qi h (k + 1)).inv) :
    (glnFunctor (n := n) q qi h).map (EO ◁ g) =
      (Φ q qi h (k + 2)).hom ≫ X R n ◁ (crossing (n := n) q qi h).gen k j ≫ (Φ q qi h (k + 2)).inv := by
  rw [Functor.Monoidal.map_whiskerLeft, G_μ, G_δ, ih]
  simp only [OS.μ_cons, OS.μ_nil, Iso.trans_hom, Iso.trans_inv, Iso.symm_hom, Iso.symm_inv,
    whiskerLeftIso_hom, whiskerLeftIso_inv, OSCat.E, OS.obj_cons, OS.obj_nil, OS.col, lift_obj,
    Φ_succ_hom, Φ_succ_inv]
  monoidal

theorem map_gen_zero (k : ℕ) :
    (glnFunctor (n := n) q qi h).map (leftCross (OSCat.cross q qi (q ^ n) (∑ i, wt n q qi i)).S (tpow EO k)) =
      (Φ q qi h (k + 2)).hom ≫ leftCross (S q qi) (tpow (X R n) k) ≫ (Φ q qi h (k + 2)).inv := by
  have hnat : (Φ q qi h (k + 2)).hom ≫ leftCross (S q qi) (tpow (X R n) k) ≫ (Φ q qi h (k + 2)).inv =
      leftCross (S q qi) ((glnFunctor (n := n) q qi h).obj (tpow EO k)) := by
    rw [Φ_succ_hom, Φ_succ_hom, Φ_succ_inv, Φ_succ_inv, ← Category.assoc, ← cancel_mono
      (X R n ◁ X R n ◁ (Φ q qi h k).hom)]
    simp only [Category.assoc, ← whiskerLeft_comp, Iso.inv_hom_id, whiskerLeft_id, Category.comp_id]
    unfold leftCross
    simp only [Category.assoc]
    rw [← associator_naturality_right, ← whisker_exchange_assoc, ← associator_inv_naturality_right_assoc]
    erw [MonoidalCategory.whiskerLeft_id, Category.comp_id]
  rw [hnat]
  rw [leftCross, Functor.map_comp, Functor.map_comp, Functor.Monoidal.map_associator_inv,
    Functor.Monoidal.map_associator, Functor.Monoidal.map_whiskerRight, lift_S]
  simp only [G_μ, G_δ, OS.μ_cons, OS.μ_nil, Iso.trans_hom, Iso.trans_inv, Iso.symm_hom, Iso.symm_inv,
    whiskerLeftIso_hom, whiskerLeftIso_inv, OSCat.E, OS.obj_cons, OS.obj_nil, OS.col, lift_obj,
    datum_S, tensorObj_w, List.cons_append, List.nil_append, leftCross]
  monoidal

/-- **The lift carries the OS crossing on strands `i, i+1` to the `GL_n` crossing**, up to `Φ`. -/
theorem map_gen : ∀ (k : ℕ) (i : Fin k),
    (glnFunctor (n := n) q qi h).map ((OSCat.cross q qi (q ^ n) (∑ i, wt n q qi i)).gen k i) =
      (Φ q qi h (k + 1)).hom ≫ (crossing (n := n) q qi h).gen k i ≫ (Φ q qi h (k + 1)).inv
  | 0, i => i.elim0
  | k + 1, ⟨0, h0⟩ => by
      rw [HeckeCrossing.gen_zero, HeckeCrossing.gen_zero, map_gen_zero]
      rfl
  | k + 1, ⟨j + 1, hj⟩ => by
      rw [HeckeCrossing.gen_succ, HeckeCrossing.gen_succ]
      exact map_gen_succ q qi h k ⟨j, by omega⟩ _ (map_gen k ⟨j, by omega⟩)

variable (R) in
/-- An `R`-linear functor induces an algebra map on endomorphism algebras. -/
noncomputable def mapEndAlg {𝒞 𝒟 : Type*} [Category 𝒞] [Preadditive 𝒞] [Linear R 𝒞]
    [Category 𝒟] [Preadditive 𝒟] [Linear R 𝒟] (G : 𝒞 ⥤ 𝒟) [G.Additive] [G.Linear R] (A : 𝒞) :
    End A →ₐ[R] End (G.obj A) where
  toFun f := G.map f
  map_one' := G.map_id A
  map_mul' f g := G.map_comp g f
  map_zero' := G.map_zero A A
  map_add' f g := G.map_add
  commutes' r := by
    simp only [Algebra.algebraMap_eq_smul_one, End.one_def]
    rw [CategoryTheory.Functor.map_smul, CategoryTheory.Functor.map_id]

variable (R) in
/-- Conjugation by an isomorphism, as an algebra map on endomorphism algebras. -/
def conjAlg {𝒟 : Type*} [Category 𝒟] [Preadditive 𝒟] [Linear R 𝒟] {A B : 𝒟} (e : A ≅ B) :
    End B →ₐ[R] End A where
  toFun f := e.hom ≫ f ≫ e.inv
  map_one' := by simp [End.one_def]
  map_mul' f g := by simp [End.mul_def]
  map_zero' := by simp
  map_add' f g := by rw [Preadditive.add_comp, Preadditive.comp_add]
  commutes' r := by
    simp only [Algebra.algebraMap_eq_smul_one, End.one_def]
    rw [Linear.smul_comp, Category.id_comp, Linear.comp_smul, Iso.hom_inv_id]

theorem conjAlg_injective {𝒟 : Type*} [Category 𝒟] [Preadditive 𝒟] [Linear R 𝒟] {A B : 𝒟}
    (e : A ≅ B) : Function.Injective (conjAlg R e) := by
  intro f g hfg
  have := congrArg (fun x => e.inv ≫ x ≫ e.hom) hfg
  change e.inv ≫ (e.hom ≫ f ≫ e.inv) ≫ e.hom = e.inv ≫ (e.hom ≫ g ≫ e.inv) ≫ e.hom at this
  simpa using this

/-- **The lift of Brundan's `ι_r` is the `GL_n` Hecke action, conjugated by `Φ`.** -/
theorem lift_heckeAction (m : ℕ) :
    (mapEndAlg R (glnFunctor (n := n) q qi h) (tpow EO (m + 1))).comp
        ((OSCat.cross q qi (q ^ n) (∑ i, wt n q qi i)).heckeAction m) =
      (conjAlg R (Φ q qi h (m + 1))).comp ((crossing (n := n) q qi h).heckeAction m) := by
  apply QOU.SchurWeyl.Hecke.hom_ext
  intro i
  simp only [AlgHom.comp_apply, HeckeCrossing.heckeAction_σ]
  exact map_gen q qi h m i

/-- **Faithfulness inside `OS`.**  For `m + 1 ≤ n`, Brundan's
`ι_{m+1} : H_{m+1}(q) → End_{OS(q, qi, q^n, [n]_q)}(E^{⊗(m+1)})` is injective, over any
commutative ring with `q * qi = 1`: the Hecke algebra embeds in the endomorphisms of every tensor
power `E^{⊗r}`, `r ≤ n`. -/
theorem OS_heckeAction_injective (h : q * qi = 1) {m : ℕ} (hm : m + 1 ≤ n) :
    Function.Injective ((OSCat.cross q qi (q ^ n) (∑ i, wt n q qi i)).heckeAction m) := by
  intro x y hxy
  apply heckeAction_injective q qi h hm
  apply conjAlg_injective (R := R) (Φ q qi h (m + 1))
  have hx := AlgHom.congr_fun (lift_heckeAction (n := n) q qi h m) x
  have hy := AlgHom.congr_fun (lift_heckeAction (n := n) q qi h m) y
  simp only [AlgHom.comp_apply] at hx hy
  rw [← hx, ← hy, hxy]
end QOU.OrientedSkein.GLn
