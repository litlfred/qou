/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.Model.GLnTrace
import QOU.OrientedSkein.SkeinDatum
import Mathlib.LinearAlgebra.Matrix.Block
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse

/-!
# `QOU.OrientedSkein.Model.GLnDatum` — the `GL_n` vector representation is an oriented skein datum

Dispatch B of PR #7705 (bean `qou-slck`): the full oriented skein datum
(`QOU.OrientedSkein.OrientedSkeinDatum`, Brundan's relations (1)–(5)) on `E = R^n` in
`ModuleCat R`, for every `n`, over any commutative ring with `q * qi = 1`, with parameters

`t = q^n`,  `δ = ∑_i q^{n-1-i} qi^i = [n]_q`   (so `(q - qi) δ = q^n - qi^n = t - t⁻¹`).

The data:

* `E = F = R^n`.  `F` plays the dual: the exact pairing `F ⊣ E` (`pairing`) has cup
  `η(1) = ∑_c e_c ⊗ e_c` and cap `ε(e_a ⊗ e_b) = δ_{ab}`; the zigzags are checked on basis vectors.
* `S = Ř`, the `GL_n` R-matrix (`QOU.OrientedSkein.Model.GLnRMatrix.crossing`): relations (1), (2).
* The sideways crossing `sideways Ř : E ⊗ F ⟶ F ⊗ E` is computed on basis vectors
  (`sideways_apply`): it swaps `e_a ⊗ e_b ↦ e_b ⊗ e_a` for `a ≠ b`, and on the diagonal span
  `{e_a ⊗ e_a}` it acts by the upper-triangular matrix `A` with diagonal `q` and entries `q - qi`
  above the diagonal.
* `T` (relation (4)) is the inverse: the swap off the diagonal, and `A⁻¹` on the diagonal.  `A` is
  invertible because it is triangular with determinant `q^n`, a unit.
* Relation (5): `η ≫ T ≫ ε = ∑_c (A⁻¹ 1)_c`, and `A⁻¹ 1 = (qi^{2(n-1-c)+1})_c`, whose total times
  `q^n` is `[n]_q` (`dim_eq`).

Main definition: `datum`.  Composed with the universal property
(`QOU.OrientedSkein.OS.lift`) this gives a linear monoidal functor `OS(q - qi, q^n) ⥤ ModuleCat R`
sending the generating object to `R^n`.

## Nondegeneracy

For `n ≥ 2` the crossing is not a scalar (`S_ne_smul_id`), and the closed loop is `[n]_q`
(`GLnTrace.loop_mul`), invertible for generic `q`.  The Markov trace this datum's crossing produces
by closing strands is `GLnTrace.markovFamily`, with `z = q^n/[n]_q = t/δ`.

## Not proved here

That the left trace of `GLnTrace` *is* the closure computed in `OS(z, t)` through this datum's cups
and caps is not proved: the trace in `GLnTrace` is defined directly as a weighted partial trace in
`ModuleCat`, not as the image of an `OS` closure.

Sorry-free; no axioms beyond Lean/Mathlib's.

## References

* [brundan2017] J. Brundan, *Representations of the oriented skein category*, arXiv 1712.08953,
  Theorem 1.1.
* [turaev1989] V. Turaev, *Operator invariants of tangles and R-matrices*.
-/

namespace QOU.OrientedSkein.GLn

open CategoryTheory MonoidalCategory Module

universe u

variable {R : Type u} [CommRing R] {n : ℕ}

/-! ## The exact pairing `F ⊣ E` on `R^n` -/

/-- `∑_c e_c ⊗ e_c`. -/
noncomputable def casimir : XX R n := ∑ c, e c ⊗ₜ e c

/-- The cup `η : 𝟙 ⟶ F ⊗ E`, `1 ↦ ∑_c e_c ⊗ e_c`. -/
noncomputable def coev : 𝟙_ (ModuleCat.{u} R) ⟶ X R n ⊗ X R n :=
  ModuleCat.ofHom (LinearMap.toSpanSingleton R (XX R n) casimir)

/-- The cap on the raw tensor square, `e_a ⊗ e_b ↦ δ_{ab}`. -/
noncomputable def evLin : XX R n →ₗ[R] R :=
  (bas R n).constr R (fun p => if p.1 = p.2 then 1 else 0)

theorem evLin_ee (a b : Fin n) : evLin (e a ⊗ₜ e b : XX R n) = if a = b then (1 : R) else 0 := by
  rw [← bas_apply, evLin]
  exact Basis.constr_basis _ _ _ _

/-- The cap `ε : E ⊗ F ⟶ 𝟙`. -/
noncomputable def ev : X R n ⊗ X R n ⟶ 𝟙_ (ModuleCat.{u} R) := ModuleCat.ofHom evLin

section homs

variable {A B : ModuleCat.{u} R}

theorem hom_lu_apply (x) : (λ_ A).hom.hom x = TensorProduct.lid R A x := rfl
theorem hom_lu_inv_apply (x) : (λ_ A).inv.hom x = (TensorProduct.lid R A).symm x := rfl
theorem hom_ru_apply (x) : (ρ_ A).hom.hom x = TensorProduct.rid R A x := rfl
theorem hom_ru_inv_apply (x) : (ρ_ A).inv.hom x = (TensorProduct.rid R A).symm x := rfl

end homs

theorem coev_whiskerRight_apply (x : TensorProduct R R (X R n)) :
    (coev (R := R) (n := n) ▷ X R n).hom x =
      (LinearMap.toSpanSingleton R (XX R n) casimir).rTensor (X R n) x := rfl

theorem coev_whiskerLeft_apply (x : TensorProduct R (X R n) R) :
    (X R n ◁ coev (R := R) (n := n)).hom x =
      (LinearMap.toSpanSingleton R (XX R n) casimir).lTensor (X R n) x := rfl

theorem ev_whiskerLeft_apply (x : XXX R n) :
    (X R n ◁ ev (R := R) (n := n)).hom x = (evLin (R := R) (n := n)).lTensor (X R n) x := rfl

theorem ev_whiskerRight_apply (x : TensorProduct R (XX R n) (X R n)) :
    (ev (R := R) (n := n) ▷ X R n).hom x = (evLin (R := R) (n := n)).rTensor (X R n) x := rfl

theorem hom_ext_XU {W : ModuleCat.{u} R} {f g : X R n ⊗ 𝟙_ (ModuleCat.{u} R) ⟶ W}
    (h : ∀ a, f.hom (e a ⊗ₜ (1 : R) : TensorProduct R (X R n) R) =
      g.hom (e a ⊗ₜ (1 : R) : TensorProduct R (X R n) R)) : f = g := by
  ext1
  apply TensorProduct.ext
  apply (basX R n).ext
  intro a
  apply LinearMap.ext_ring
  simpa [basX_apply] using h a

theorem hom_ext_UX {W : ModuleCat.{u} R} {f g : 𝟙_ (ModuleCat.{u} R) ⊗ X R n ⟶ W}
    (h : ∀ a, f.hom ((1 : R) ⊗ₜ e a : TensorProduct R R (X R n)) =
      g.hom ((1 : R) ⊗ₜ e a : TensorProduct R R (X R n))) : f = g := by
  ext1
  apply TensorProduct.ext
  apply LinearMap.ext_ring
  apply (basX R n).ext
  intro a
  simpa [basX_apply] using h a

theorem zigzag_E : X R n ◁ coev ≫ (α_ (X R n) (X R n) (X R n)).inv ≫ ev ▷ X R n =
    (ρ_ (X R n)).hom ≫ (λ_ (X R n)).inv := by
  apply hom_ext_XU
  intro a
  simp only [ModuleCat.hom_comp, LinearMap.comp_apply, coev_whiskerLeft_apply,
    LinearMap.lTensor_tmul, LinearMap.toSpanSingleton_apply, one_smul, casimir,
    TensorProduct.tmul_sum, map_sum, hom_assoc_inv_apply, TensorProduct.assoc_symm_tmul,
    ev_whiskerRight_apply, LinearMap.rTensor_tmul, evLin_ee, hom_ru_apply, hom_lu_inv_apply,
    TensorProduct.rid_tmul, TensorProduct.lid_symm_apply]
  rw [Finset.sum_eq_single a (fun b _ hb => by simp [Ne.symm hb]) (by simp)]
  simp

theorem zigzag_F : coev ▷ X R n ≫ (α_ (X R n) (X R n) (X R n)).hom ≫ X R n ◁ ev =
    (λ_ (X R n)).hom ≫ (ρ_ (X R n)).inv := by
  apply hom_ext_UX
  intro a
  simp only [ModuleCat.hom_comp, LinearMap.comp_apply, coev_whiskerRight_apply,
    LinearMap.rTensor_tmul, LinearMap.toSpanSingleton_apply, one_smul, casimir,
    TensorProduct.sum_tmul, map_sum, hom_assoc_apply, TensorProduct.assoc_tmul,
    ev_whiskerLeft_apply, LinearMap.lTensor_tmul, evLin_ee, hom_lu_apply, hom_ru_inv_apply,
    TensorProduct.lid_tmul, TensorProduct.rid_symm_apply]
  rw [Finset.sum_eq_single a (fun b _ hb => by simp [hb]) (by simp)]
  simp

/-- **The exact pairing `F ⊣ E`** on `R^n` (with `F = R^n` playing the dual through the standard
pairing): Brundan's relation (3). -/
noncomputable instance pairing : ExactPairing (X R n) (X R n) where
  coevaluation' := coev
  evaluation' := ev
  coevaluation_evaluation' := zigzag_E
  evaluation_coevaluation' := zigzag_F

theorem coevaluation_eq : η_ (X R n) (X R n) = coev (R := R) (n := n) := rfl
theorem evaluation_eq : ε_ (X R n) (X R n) = ev (R := R) (n := n) := rfl

/-! ## The diagonal block and its inverse -/

variable (q qi : R)

variable (n) in
/-- The diagonal block of the sideways crossing, `A d c = diagCoef d c`: upper triangular with
`q` on the diagonal and `q - qi` above it. -/
def A : Matrix (Fin n) (Fin n) R := Matrix.of fun d c => diagCoef q qi d c

theorem A_apply (d c : Fin n) : A n q qi d c = diagCoef q qi d c := rfl

theorem A_blockTriangular : (A n q qi).BlockTriangular id := by
  intro i j hij
  simp only [id] at hij
  simp [A, diagCoef, hij.ne', not_lt.mpr hij.le]

theorem det_A : (A n q qi).det = q ^ n := by
  rw [Matrix.det_of_upperTriangular (A_blockTriangular q qi)]
  simp [A, diagCoef]

theorem isUnit_det_A (h : q * qi = 1) : IsUnit (A n q qi).det := by
  rw [det_A]
  exact (isUnit_of_mul_eq_one q qi h).pow n

variable (n) in
/-- `x_c = qi^{2(n-1-c)+1}`, the solution of `A x = 1`. -/
def xs (c : ℕ) : R := qi ^ (2 * (n - 1 - c) + 1)

/-- `∑_{d < c < n} x_c`, as a sum over `range n`. -/
def tail (d : ℕ) : R := ∑ c ∈ Finset.range n, if d < c then xs n qi c else 0

theorem tail_succ (d : ℕ) :
    tail (n := n) qi d = (if d + 1 < n then xs n qi (d + 1) else 0) + tail (n := n) qi (d + 1) := by
  have hpt : ∀ c, (if d < c then xs n qi c else 0) =
      (if d + 1 = c then xs n qi c else 0) + (if d + 1 < c then xs n qi c else 0) := by
    intro c
    by_cases h1 : d + 1 = c
    · subst h1
      simp
    · by_cases h2 : d < c
      · have : d + 1 < c := by omega
        simp [h1, h2, this]
      · have : ¬ d + 1 < c := by omega
        simp [h1, h2, this]
  simp only [tail, hpt, Finset.sum_add_distrib, Finset.sum_ite_eq, Finset.mem_range]

theorem tail_top (d : ℕ) (hd : n ≤ d + 1) : tail (n := n) qi d = 0 := by
  apply Finset.sum_eq_zero
  intro c hc
  simp only [Finset.mem_range] at hc
  simp [show ¬ d < c by omega]

/-- `q x_d + (q - qi) ∑_{d<c<n} x_c = 1`. -/
theorem row_eq (h : q * qi = 1) : ∀ k d : ℕ, d + k + 1 = n →
    q * xs n qi d + (q - qi) * tail (n := n) qi d = 1
  | 0, d, hk => by
      rw [tail_top qi d (by omega), xs, show n - 1 - d = 0 by omega]
      simp [h]
  | k + 1, d, hk => by
      have ih := row_eq h k (d + 1) (by omega)
      rw [tail_succ, if_pos (by omega)]
      have e1 : xs n qi d = qi ^ 2 * xs n qi (d + 1) := by
        simp only [xs]
        rw [show n - 1 - d = (n - 1 - (d + 1)) + 1 by omega, ← pow_add]
        congr 1
        ring
      rw [e1]
      have hq : q * qi ^ 2 = qi := by rw [pow_two, ← mul_assoc, h, one_mul]
      linear_combination ih + (xs n qi (d + 1)) * hq

variable (n) in
/-- `x` as a vector on `Fin n`. -/
def xv : Fin n → R := fun c => xs n qi c

theorem A_mulVec_xv (h : q * qi = 1) : (A n q qi).mulVec (xv n qi) = fun _ => 1 := by
  funext d
  have hsplit : ∀ c : Fin n, A n q qi d c * xv n qi c =
      (if d = c then q * xs n qi d else 0) + (q - qi) * (if (d : ℕ) < c then xs n qi c else 0) := by
    intro c
    rcases lt_trichotomy d c with hdc | rfl | hdc
    · simp [A, diagCoef, xv, hdc, hdc.ne, Fin.lt_iff_val_lt_val.mp hdc]
    · simp [A, diagCoef, xv]
    · simp [A, diagCoef, xv, hdc.ne', not_lt.mpr hdc.le,
        not_lt.mpr (Fin.le_iff_val_le_val.mp hdc.le)]
  simp only [Matrix.mulVec, dotProduct, hsplit, Finset.sum_add_distrib, Finset.sum_ite_eq,
    Finset.mem_univ, if_true, ← Finset.mul_sum]
  rw [Fin.sum_univ_eq_sum_range (fun c => if (d : ℕ) < c then xs n qi c else 0) n]
  exact row_eq q qi h (n - 1 - d) d (by omega)

/-- `A⁻¹ 1 = x`. -/
theorem Ainv_mulVec_one (h : q * qi = 1) : (A n q qi)⁻¹.mulVec (fun _ => (1 : R)) = xv n qi := by
  rw [← A_mulVec_xv q qi h, Matrix.mulVec_mulVec, Matrix.nonsing_inv_mul _ (isUnit_det_A q qi h),
    Matrix.one_mulVec]

/-- The total of `x`, rescaled by `q^n`, is the quantum integer `∑_i q^{n-1-i} qi^i`. -/
theorem sum_xv (h : q * qi = 1) : q ^ n * ∑ c, xv n qi c = ∑ i, wt n q qi i := by
  rw [Finset.mul_sum, show (∑ c : Fin n, q ^ n * xv n qi c) = ∑ c : Fin n, q ^ n * xs n qi c from rfl,
    Fin.sum_univ_eq_sum_range (fun c => q ^ n * xs n qi c) n,
    show (∑ i, wt n q qi i) = ∑ i : Fin n, q ^ (n - 1 - i) * qi ^ (i : ℕ) from rfl,
    Fin.sum_univ_eq_sum_range (fun i => q ^ (n - 1 - i) * qi ^ i) n,
    ← Finset.sum_range_reflect]
  refine Finset.sum_congr rfl fun c hc => ?_
  simp only [Finset.mem_range] at hc
  obtain ⟨m, rfl⟩ : ∃ m, n = c + 1 + m := ⟨n - (c + 1), by omega⟩
  simp only [xs]
  rw [show c + 1 + m - 1 - (c + 1 + m - 1 - c) = c by omega,
    show c + 1 + m - 1 - c = m by omega]
  have : q ^ (c + 1 + m) * qi ^ (2 * c + 1) = q ^ m * qi ^ c * (q * qi) ^ (c + 1) := by ring
  rw [this, h, one_pow, mul_one]

/-! ## The sideways crossing on basis vectors -/

/-- `sideways S` as an explicit composite of whiskered structure maps. -/
theorem sideways_eq (Sx : X R n ⊗ X R n ⟶ X R n ⊗ X R n) :
    sideways (E := X R n) (F := X R n) Sx =
      (λ_ (X R n)).inv ▷ X R n ≫ (coev ▷ X R n) ▷ X R n ≫ (α_ (X R n) (X R n) (X R n)).hom ▷ X R n ≫
        (X R n ◁ Sx) ▷ X R n ≫ (α_ (X R n) (X R n ⊗ X R n) (X R n)).hom ≫
        X R n ◁ (α_ (X R n) (X R n) (X R n)).hom ≫ X R n ◁ X R n ◁ ev ≫ X R n ◁ (ρ_ (X R n)).hom := by
  rw [sideways, coevaluation_eq, evaluation_eq]
  monoidal

section steps

theorem step1 (x : XX R n) : ((λ_ (X R n)).inv ▷ X R n).hom x =
    ((TensorProduct.lid R (X R n)).symm.toLinearMap.rTensor (X R n)) x := rfl
theorem step2 (x : TensorProduct R (TensorProduct R R (X R n)) (X R n)) :
    ((coev ▷ X R n) ▷ X R n).hom x =
      (((LinearMap.toSpanSingleton R (XX R n) casimir).rTensor (X R n)).rTensor (X R n)) x := rfl
theorem step3 (x : TensorProduct R (TensorProduct R (XX R n) (X R n)) (X R n)) :
    ((α_ (X R n) (X R n) (X R n)).hom ▷ X R n).hom x =
      ((TensorProduct.assoc R (X R n) (X R n) (X R n)).toLinearMap.rTensor (X R n)) x := rfl
theorem step4 (x : TensorProduct R (XXX R n) (X R n)) :
    ((X R n ◁ S q qi) ▷ X R n).hom x =
      (((rLin (n := n) q qi).lTensor (X R n)).rTensor (X R n)) x := rfl
theorem step5 (x : TensorProduct R (XXX R n) (X R n)) :
    (α_ (X R n) (X R n ⊗ X R n) (X R n)).hom.hom x =
      TensorProduct.assoc R (X R n) (XX R n) (X R n) x := rfl
theorem step6 (x : TensorProduct R (X R n) (TensorProduct R (XX R n) (X R n))) :
    (X R n ◁ (α_ (X R n) (X R n) (X R n)).hom).hom x =
      ((TensorProduct.assoc R (X R n) (X R n) (X R n)).toLinearMap.lTensor (X R n)) x := rfl
theorem step7 (x : TensorProduct R (X R n) (XXX R n)) :
    (X R n ◁ X R n ◁ ev).hom x = (((evLin (R := R) (n := n)).lTensor (X R n)).lTensor (X R n)) x :=
  rfl
theorem step8 (x : TensorProduct R (X R n) (TensorProduct R (X R n) R)) :
    (X R n ◁ (ρ_ (X R n)).hom).hom x =
      ((TensorProduct.rid R (X R n)).toLinearMap.lTensor (X R n)) x := rfl

end steps

set_option synthInstance.maxHeartbeats 200000 in
/-- **The sideways crossing on basis vectors.**
`sideways Ř (e_a ⊗ e_b) = ∑_c ∑_x ⟨e_x ⊗ e_b | Ř | e_c ⊗ e_a⟩ · e_c ⊗ e_x`. -/
theorem sideways_apply (a b : Fin n) :
    (sideways (E := X R n) (F := X R n) (S q qi)).hom (e a ⊗ₜ e b : XX R n) =
      ∑ c : Fin n, ∑ x : Fin n, coef q qi (x, b) (c, a) • (e c ⊗ₜ e x : XX R n) := by
  rw [sideways_eq]
  simp only [ModuleCat.hom_comp, LinearMap.comp_apply]
  rw [step1, LinearMap.rTensor_tmul, LinearEquiv.coe_coe, TensorProduct.lid_symm_apply, step2,
    LinearMap.rTensor_tmul, LinearMap.rTensor_tmul, LinearMap.toSpanSingleton_apply, one_smul,
    step3, LinearMap.rTensor_tmul, casimir, TensorProduct.sum_tmul, map_sum]
  simp only [LinearEquiv.coe_coe, TensorProduct.assoc_tmul, TensorProduct.sum_tmul, map_sum, step4,
    LinearMap.rTensor_tmul, LinearMap.lTensor_tmul, rLin_ee, step5, step6, step7, step8]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [show rv q qi c a = rv q qi (c, a).1 (c, a).2 from rfl, rv_eq_sum, TensorProduct.sum_tmul]
  simp only [map_sum, ← TensorProduct.smul_tmul', map_smul, TensorProduct.assoc_tmul,
    LinearMap.lTensor_tmul, evLin_ee, TensorProduct.rid_tmul, TensorProduct.tmul_sum,
    TensorProduct.tmul_smul, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun x _ => ?_
  rw [Finset.sum_eq_single b (fun y _ hy => by simp [hy]) (by simp)]
  simp

/-- The coefficients of `Ř`: `⟨e_x ⊗ e_y | Ř | e_c ⊗ e_a⟩` is the diagonal coefficient on
`(x, y) = (c, a)` plus `1` on the swap `(x, y) = (a, c)`, `c ≠ a`. -/
theorem coef_apply (x y c a : Fin n) :
    coef q qi (x, y) (c, a) =
      (if x = c ∧ y = a then diagCoef q qi c a else 0) + (if x = a ∧ y = c ∧ c ≠ a then 1 else 0) := by
  simp only [coef]
  rcases lt_trichotomy c a with h | rfl | h
  · rw [rv_lt q qi h, map_add, map_smul, repr_ee, repr_ee]
    by_cases h1 : x = c <;> by_cases h2 : y = a <;> by_cases h3 : x = a <;> by_cases h4 : y = c <;>
      simp_all [Finsupp.single_apply, diagCoef, h.ne, h.ne'] <;> omega
  · rw [rv_self, map_smul, repr_ee]
    by_cases h1 : x = c <;> by_cases h2 : y = c <;> simp_all [Finsupp.single_apply, diagCoef]
  · rw [rv_gt q qi h, repr_ee]
    by_cases h1 : x = c <;> by_cases h2 : y = a <;> by_cases h3 : x = a <;> by_cases h4 : y = c <;>
      simp_all [Finsupp.single_apply, diagCoef, h.ne, h.ne', not_lt.mpr h.le] <;> omega

theorem sideways_off {a b : Fin n} (hab : a ≠ b) :
    (sideways (E := X R n) (F := X R n) (S q qi)).hom (e a ⊗ₜ e b : XX R n) = e b ⊗ₜ e a := by
  rw [sideways_apply]
  simp only [coef_apply, add_smul, Finset.sum_add_distrib, ite_smul, zero_smul, one_smul]
  have h1 : ∀ c x : Fin n, (if x = c ∧ b = a then diagCoef q qi c a • (e c ⊗ₜ e x : XX R n) else 0) = 0 :=
    fun c x => by simp [Ne.symm hab]
  simp only [h1, Finset.sum_const_zero, zero_add]
  rw [Finset.sum_eq_single b (fun c _ hc => by simp [Ne.symm hc]) (by simp)]
  rw [Finset.sum_eq_single a (fun x _ hx => by simp [hx]) (by simp)]
  simp [Ne.symm hab]

theorem sideways_diag (a : Fin n) :
    (sideways (E := X R n) (F := X R n) (S q qi)).hom (e a ⊗ₜ e a : XX R n) =
      ∑ d : Fin n, A n q qi d a • (e d ⊗ₜ e d : XX R n) := by
  rw [sideways_apply]
  simp only [coef_apply, add_smul, Finset.sum_add_distrib, ite_smul, zero_smul, one_smul]
  have h2 : ∀ c x : Fin n, (if x = a ∧ a = c ∧ c ≠ a then (e c ⊗ₜ e x : XX R n) else 0) = 0 :=
    fun c x => by
      by_cases hc : a = c
      · simp [hc]
      · simp [hc]
  simp only [h2, Finset.sum_const_zero, add_zero]
  refine Finset.sum_congr rfl fun d _ => ?_
  rw [Finset.sum_eq_single d (fun x _ hx => by simp [hx]) (by simp)]
  simp [A_apply]

/-! ## The mixed crossing `T` -/

/-- `T (e_a ⊗ e_b)`: the swap off the diagonal, `A⁻¹` on the diagonal. -/
noncomputable def tv (a b : Fin n) : XX R n :=
  if a = b then ∑ c : Fin n, (A n q qi)⁻¹ c a • (e c ⊗ₜ e c : XX R n) else e b ⊗ₜ e a

/-- The mixed crossing `T : F ⊗ E ⟶ E ⊗ F`. -/
noncomputable def Tm : X R n ⊗ X R n ⟶ X R n ⊗ X R n :=
  ModuleCat.ofHom ((bas R n).constr R (fun p => tv q qi p.1 p.2))

theorem Tm_ee (a b : Fin n) : (Tm q qi).hom (e a ⊗ₜ e b : XX R n) = tv q qi a b := by
  rw [← bas_apply, Tm, ModuleCat.hom_ofHom]
  exact Basis.constr_basis _ _ _ _

/-- **Relation (4), first half**: `T ≫ sideways Ř = 1`. -/
theorem T_sideways (h : q * qi = 1) :
    Tm q qi ≫ sideways (E := X R n) (F := X R n) (S q qi) = 𝟙 _ := by
  apply hom_ext2
  intro a b
  rw [ModuleCat.hom_comp, LinearMap.comp_apply, Tm_ee, ModuleCat.hom_id, LinearMap.id_apply, tv]
  by_cases hab : a = b
  · subst hab
    rw [if_pos rfl, map_sum]
    simp only [map_smul, sideways_diag, Finset.smul_sum, smul_smul]
    rw [Finset.sum_comm]
    simp only [← Finset.sum_smul]
    have hm : ∀ d : Fin n, (∑ c, (A n q qi)⁻¹ c a * A n q qi d c) = (1 : Matrix (Fin n) (Fin n) R) d a := by
      intro d
      rw [← Matrix.mul_nonsing_inv _ (isUnit_det_A q qi h), Matrix.mul_apply]
      exact Finset.sum_congr rfl fun c _ => mul_comm _ _
    simp only [hm, Matrix.one_apply, ite_smul, one_smul, zero_smul, Finset.sum_ite_eq',
      Finset.mem_univ, if_true]
  · rw [if_neg hab, sideways_off q qi (Ne.symm hab)]

/-- **Relation (4), second half**: `sideways Ř ≫ T = 1`. -/
theorem sideways_T (h : q * qi = 1) :
    sideways (E := X R n) (F := X R n) (S q qi) ≫ Tm q qi = 𝟙 _ := by
  apply hom_ext2
  intro a b
  rw [ModuleCat.hom_comp, LinearMap.comp_apply, ModuleCat.hom_id, LinearMap.id_apply]
  by_cases hab : a = b
  · subst hab
    rw [sideways_diag, map_sum]
    simp only [map_smul, Tm_ee, tv, if_true, Finset.smul_sum, smul_smul]
    rw [Finset.sum_comm]
    simp only [← Finset.sum_smul]
    have hm : ∀ c : Fin n, (∑ d, A n q qi d a * (A n q qi)⁻¹ c d) = (1 : Matrix (Fin n) (Fin n) R) c a := by
      intro c
      rw [← Matrix.nonsing_inv_mul _ (isUnit_det_A q qi h), Matrix.mul_apply]
      exact Finset.sum_congr rfl fun d _ => mul_comm _ _
    simp only [hm, Matrix.one_apply, ite_smul, one_smul, zero_smul, Finset.sum_ite_eq',
      Finset.mem_univ, if_true]
  · rw [sideways_off q qi hab, Tm_ee, tv, if_neg (Ne.symm hab)]

/-- The closed loop with the mixed crossing: `ε ∘ T ∘ η = ∑_c (A⁻¹ 1)_c`. -/
theorem loopT_apply (h : q * qi = 1) :
    (coev ≫ Tm (n := n) q qi ≫ ev).hom (1 : R) = ∑ c, xv n qi c := by
  rw [← Ainv_mulVec_one q qi h]
  change evLin ((Tm q qi).hom (LinearMap.toSpanSingleton R (XX R n) casimir 1)) = _
  rw [LinearMap.toSpanSingleton_apply, one_smul, casimir, map_sum, map_sum]
  simp only [Tm_ee, tv, if_true, map_sum, map_smul, evLin_ee, smul_eq_mul, mul_one,
    Matrix.mulVec, dotProduct]
  rw [Finset.sum_comm]

/-- **Relation (5)**: `t · (ε ∘ T ∘ η) = δ · 1` with `t = q^n` and `δ = [n]_q = ∑_i q^{n-1-i} qi^i`. -/
theorem dim_eq (h : q * qi = 1) :
    (q ^ n) • (η_ (X R n) (X R n) ≫ Tm q qi ≫ ε_ (X R n) (X R n)) =
      (∑ i, wt n q qi i) • 𝟙 (𝟙_ (ModuleCat.{u} R)) := by
  ext1
  apply LinearMap.ext_ring
  rw [ModuleCat.hom_smul, LinearMap.smul_apply, coevaluation_eq, evaluation_eq]
  erw [loopT_apply q qi h]
  rw [ModuleCat.hom_smul, LinearMap.smul_apply, ModuleCat.hom_id, smul_eq_mul, sum_xv q qi h]
  exact (mul_one _).symm

/-! ## The datum -/

/-- **The `GL_n` vector representation is an oriented skein datum** in `ModuleCat R`, for every
`n`, with `t = q^n` and `δ = [n]_q`: Brundan's relations (1)–(5) for `E = F = R^n`,
`S = Ř`, `T` the inverse of the sideways crossing, and the standard cup and cap. -/
noncomputable def datum (h : q * qi = 1) :
    OrientedSkeinDatum q qi (q ^ n) (∑ i, wt n q qi i) (X R n) (X R n) where
  cross := crossing q qi h
  T := Tm q qi
  T_sideways := T_sideways q qi h
  sideways_T := sideways_T q qi h
  dim := dim_eq q qi h

@[simp] theorem datum_S (h : q * qi = 1) : (datum (n := n) q qi h).cross.S = S q qi := rfl

@[simp] theorem datum_T (h : q * qi = 1) : (datum (n := n) q qi h).T = Tm q qi := rfl

end QOU.OrientedSkein.GLn
