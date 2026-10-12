/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.Model.GLnRMatrix
import QOU.OrientedSkein.MarkovClosure

/-!
# `QOU.OrientedSkein.Model.GLnTrace` — the quantum trace of the `GL_n` model is a Markov trace

Dispatch B of PR #7705, "go to the trace" (bean `qou-slck`).

`QOU.OrientedSkein.MarkovClosure` showed that a *left trace* for a Hecke crossing (a natural way of
closing the leftmost strand, with a loop value `d`, a curl value `w`, and invariance of the double
closure under the crossing) makes the normalised full closure a Markov trace with parameter
`z = w/d`.  This file constructs the left trace for the `GL_n` R-matrix on `X = R^n`
(`QOU.OrientedSkein.Model.GLnRMatrix`):

`ptr_Y (f) = ∑_i w_i · (ι_i ≫ f ≫ π_i)`,  `ι_i y = e_i ⊗ y`,  `π_i (x ⊗ y) = x_i · y`,

the **weighted (quantum) partial trace** over the left factor, with weights
`w_i = q^{n-1-i} qi^i` — the eigenvalues of the pivotal element `K_{2ρ}` on `e_i`, normalised
symmetrically.  We prove:

* the loop value is `d = ∑_i q^{n-1-i} qi^i`, the quantum integer `[n]_q` (`loop_eq`);
* the curl value is `q^n` (`ptr_cross`): closing the left strand of `Ř` on `e_j ⊗ y` gives
  `(q w_j + (q - qi) ∑_{i<j} w_i) · e_j ⊗ y`, and the weights are exactly the ones making this
  independent of `j` (`curl_sum`);
* the double closure is invariant under the crossing (`ptr2_conj`), because `Ř` only permutes the
  two tensor indices, so it preserves `w_a w_b` (`coef_weight`); this holds for **any** weights;
* hence (`markovFamily`) the normalised closure
  `tr_m (x) = [n]_q^{-(m+1)} · (closure of ρ_m (x))` is a `MarkovTraceFamily` on the Hecke tower
  with Markov parameter `z = q^n / [n]_q`, and by `markovTrace_unique` it is **the** Markov trace
  with that parameter (`markov_eq`).  In Brundan's variables `t = q^n` and
  `δ = (t - t⁻¹)/(q - q⁻¹) = [n]_q`, so this is the HOMFLYPT normalisation `z = t/δ`.
* **Cross-check at `n = 2`** (`markov_eq_wtrace_two`): over a field, `z = q²/(q + q⁻¹) =
  q³/(q² + 1) = z_D`, and the closure equals the Ocneanu-weighted seminormal trace `wtrace` of
  `QOU.SchurWeyl.MarkovTraceInstance` at every level.

## Nondegeneracy

* `loop_eq`: the closed loop is `[n]_q`, a unit whenever `[n]_q` is invertible (e.g. generic `q`
  over a field).  For `n = 2` it is `q + qi`.
* `S_ne_smul_id` (in `GLnRMatrix`): for `n ≥ 2` the crossing is not a scalar.

## What is not here

* The `OrientedSkeinDatum` itself (the exact pairing `X* ⊣ X` and the mixed crossing `T`) is built
  in `QOU.OrientedSkein.Model.GLnDatum`.  That this weighted partial trace coincides with the
  closure computed in `OS(z, t)` through the datum's cups and caps is not proved.
* The direct comparison with the matrix model `QOU.IwahoriHecke.TensorMarkovModel` is not made: that
  model's trace lives on the presented algebra `Pres N (q - q⁻¹) 1`, and no map between `Pres` and
  `QOU.SchurWeyl.Hecke` is in the tree.  The cross-check is made instead against `wtrace`, which is
  the convention-`D` Markov trace on `QOU.SchurWeyl.Hecke`.

Sorry-free; no axioms beyond Lean/Mathlib's.

## References

* [turaev1988] V. Turaev, *The Yang–Baxter equation and invariants of links*, Invent. Math. 92
  (1988), §2–3 (enhanced Yang–Baxter operators; the weights `μ = diag(q^{n-1-2i})`).
* [jones1987] V. F. R. Jones, *Hecke algebra representations of braid groups and link
  polynomials*, Ann. of Math. 126 (1987), §5.
-/

namespace QOU.OrientedSkein.GLn

open CategoryTheory MonoidalCategory Module QOU.SchurWeyl

universe u

variable {R : Type u} [CommRing R] {n : ℕ}

/-! ## Inserting and removing a basis vector on the left -/

/-- `ι_i : Y ⟶ X ⊗ Y`, `y ↦ e_i ⊗ y`. -/
noncomputable def ins (i : Fin n) (Y : ModuleCat.{u} R) : Y ⟶ X R n ⊗ Y :=
  ModuleCat.ofHom (TensorProduct.mk R (X R n) Y (e i))

/-- `π_i : X ⊗ Y ⟶ Y`, `x ⊗ y ↦ x_i · y`. -/
noncomputable def rem (i : Fin n) (Y : ModuleCat.{u} R) : X R n ⊗ Y ⟶ Y :=
  ModuleCat.ofHom (TensorProduct.lift ((LinearMap.lsmul R Y).comp
    (LinearMap.proj (R := R) (φ := fun _ : Fin n => R) i)))

theorem ins_apply (i : Fin n) (Y : ModuleCat.{u} R) (y : Y) :
    (ins i Y).hom y = (e i ⊗ₜ y : TensorProduct R (X R n) Y) := rfl

theorem rem_apply (i : Fin n) (Y : ModuleCat.{u} R) (x : X R n) (y : Y) :
    (rem i Y).hom (x ⊗ₜ y : TensorProduct R (X R n) Y) = (x : Fin n → R) i • y := by
  rw [rem, ModuleCat.hom_ofHom]; erw [TensorProduct.lift.tmul]; rfl

theorem e_apply (i j : Fin n) : (e i : Fin n → R) j = if i = j then 1 else 0 := by
  simp [e, Pi.single_apply, eq_comm]

/-- Morphisms out of `X ⊗ Z` agree if they agree on `e_a ⊗ z`. -/
theorem hom_ext_left {Z W : ModuleCat.{u} R} {f g : X R n ⊗ Z ⟶ W}
    (h : ∀ a (z : Z), f.hom (e a ⊗ₜ z : TensorProduct R (X R n) Z) =
      g.hom (e a ⊗ₜ z : TensorProduct R (X R n) Z)) : f = g := by
  ext1
  apply TensorProduct.ext
  apply (basX R n).ext
  intro a
  ext z
  simpa [basX_apply] using h a z

theorem ins_rem (i : Fin n) (Y : ModuleCat.{u} R) : ins i Y ≫ rem i Y = 𝟙 Y := by
  ext y
  simp [ins_apply, rem_apply, e_apply]

theorem ins_whisker (i : Fin n) {Y Y' : ModuleCat.{u} R} (g : Y ⟶ Y') :
    ins i Y ≫ (X R n ◁ g) = g ≫ ins i Y' := by
  ext y
  rfl

theorem whisker_rem (i : Fin n) {Y Y' : ModuleCat.{u} R} (g : Y ⟶ Y') :
    (X R n ◁ g) ≫ rem i Y' = rem i Y ≫ g := by
  apply hom_ext_left
  intro a y
  change (rem i Y').hom (e a ⊗ₜ g.hom y : TensorProduct R (X R n) Y') = g.hom ((rem i Y).hom _)
  rw [rem_apply, rem_apply, map_smul]

/-! ## The weighted partial trace -/

/-- The weighted partial trace over the leftmost factor, `f ↦ ∑_i w_i · (ι_i ≫ f ≫ π_i)`. -/
noncomputable def ptr (w : Fin n → R) (Y : ModuleCat.{u} R) :
    (X R n ⊗ Y ⟶ X R n ⊗ Y) →ₗ[R] (Y ⟶ Y) where
  toFun f := ∑ i, w i • (ins i Y ≫ f ≫ rem i Y)
  map_add' f g := by
    simp only [Preadditive.add_comp, Preadditive.comp_add, smul_add, Finset.sum_add_distrib]
  map_smul' r f := by
    simp only [Linear.smul_comp, Linear.comp_smul, smul_comm (w _) r, Finset.smul_sum,
      RingHom.id_apply]

theorem ptr_apply (w : Fin n → R) (Y : ModuleCat.{u} R) (f : X R n ⊗ Y ⟶ X R n ⊗ Y) :
    ptr w Y f = ∑ i, w i • (ins i Y ≫ f ≫ rem i Y) := rfl

theorem ptr_whisker_comp (w : Fin n → R) {Y : ModuleCat.{u} R} (g : Y ⟶ Y)
    (f : X R n ⊗ Y ⟶ X R n ⊗ Y) : ptr w Y ((X R n ◁ g) ≫ f) = g ≫ ptr w Y f := by
  simp only [ptr_apply, Preadditive.comp_sum, Linear.comp_smul, ← Category.assoc, ins_whisker]

theorem ptr_comp_whisker (w : Fin n → R) {Y : ModuleCat.{u} R} (g : Y ⟶ Y)
    (f : X R n ⊗ Y ⟶ X R n ⊗ Y) : ptr w Y (f ≫ (X R n ◁ g)) = ptr w Y f ≫ g := by
  simp only [ptr_apply, Preadditive.sum_comp, Linear.smul_comp, Category.assoc, whisker_rem]

theorem ptr_id (w : Fin n → R) (Y : ModuleCat.{u} R) : ptr w Y (𝟙 _) = (∑ i, w i) • 𝟙 Y := by
  simp only [ptr_apply, Category.id_comp, ins_rem, Finset.sum_smul]

/-! ## The curl -/

variable (q qi : R)

theorem S_whiskerRight_apply' (Y : ModuleCat.{u} R) (x : TensorProduct R (XX R n) Y) :
    (S q qi ▷ Y).hom x = (rLin (n := n) q qi).rTensor Y x := rfl

/-- The diagonal coefficient of `Ř`: the `e_i ⊗ e_j` component of `Ř (e_i ⊗ e_j)`. -/
def diagCoef (i j : Fin n) : R := if i = j then q else if i < j then q - qi else 0

/-- Closing the left strand of `Ř` against `e_i`, on `e_j ⊗ y`. -/
theorem ins_leftCross_rem (i j : Fin n) (Y : ModuleCat.{u} R) (y : Y) :
    (ins i (X R n ⊗ Y) ≫ leftCross (S q qi) Y ≫ rem i (X R n ⊗ Y)).hom
        (e j ⊗ₜ y : TensorProduct R (X R n) Y) =
      diagCoef q qi i j • (e j ⊗ₜ y : TensorProduct R (X R n) Y) := by
  change (rem i (X R n ⊗ Y)).hom ((α_ (X R n) (X R n) Y).hom.hom ((S q qi ▷ Y).hom
    ((α_ (X R n) (X R n) Y).inv.hom (e i ⊗ₜ (e j ⊗ₜ y : TensorProduct R (X R n) Y) :
      TensorProduct R (X R n) (TensorProduct R (X R n) Y))))) = _
  rw [hom_assoc_inv_apply, TensorProduct.assoc_symm_tmul, S_whiskerRight_apply',
    LinearMap.rTensor_tmul, rLin_ee, hom_assoc_apply]
  rcases lt_trichotomy i j with h | rfl | h
  · rw [rv_lt q qi h]
    simp only [TensorProduct.add_tmul, ← TensorProduct.smul_tmul', map_add, map_smul,
      TensorProduct.assoc_tmul]
    erw [rem_apply, rem_apply]
    simp [e_apply, h.ne', diagCoef, h, h.ne]
  · rw [rv_self]
    simp only [← TensorProduct.smul_tmul', map_smul, TensorProduct.assoc_tmul]
    erw [rem_apply]
    simp [e_apply, diagCoef]
  · rw [rv_gt q qi h]
    simp only [TensorProduct.assoc_tmul]
    erw [rem_apply]
    simp [e_apply, diagCoef, h.ne, h.ne', not_lt.mpr h.le]

variable (n) in
/-- The ℕ-indexed weights `W_m = q^{n-1-m} qi^m`. -/
def W (m : ℕ) : R := q ^ (n - 1 - m) * qi ^ m

variable (n) in
/-- The quantum weights `w_i = q^{n-1-i} qi^i` on the basis vectors of `X = R^n`. -/
def wt (i : Fin n) : R := W n q qi i

theorem curl_nat : ∀ j : ℕ, j < n →
    q * W n q qi j + (q - qi) * ∑ i ∈ Finset.range j, W n q qi i = q ^ n
  | 0, h => by
      obtain ⟨k, rfl⟩ : ∃ k, n = k + 1 := ⟨n - 1, by omega⟩
      simp [W, pow_succ]
      ring
  | j + 1, h => by
      have ih := curl_nat j (by omega)
      obtain ⟨k, rfl⟩ : ∃ k, n = j + 2 + k := ⟨n - (j + 2), by omega⟩
      rw [Finset.sum_range_succ]
      have e1 : j + 2 + k - 1 - (j + 1) = k := by omega
      have e2 : j + 2 + k - 1 - j = k + 1 := by omega
      simp only [W, e1, e2] at ih ⊢
      linear_combination ih

/-- **The curl sum.**  `∑_i w_i · ⟨e_i ⊗ e_j | Ř | e_i ⊗ e_j⟩ = q^n` for every `j`: the weights
are exactly those that make the closed curl a scalar. -/
theorem curl_sum (j : Fin n) : ∑ i, wt n q qi i * diagCoef q qi i j = q ^ n := by
  have hsplit : ∀ i : Fin n, wt n q qi i * diagCoef q qi i j =
      (if i = j then q * wt n q qi i else 0) + (q - qi) * (if (i : ℕ) < j then W n q qi i else 0) := by
    intro i
    rcases lt_trichotomy i j with h | rfl | h
    · simp [diagCoef, h, h.ne, Fin.lt_iff_val_lt_val.mp h, wt]; ring
    · simp [diagCoef]; ring
    · simp [diagCoef, h.ne', not_lt.mpr h.le, not_lt.mpr (Fin.le_iff_val_le_val.mp h.le)]
  simp only [hsplit, Finset.sum_add_distrib, Finset.sum_ite_eq', Finset.mem_univ, if_true,
    ← Finset.mul_sum]
  rw [Fin.sum_univ_eq_sum_range (fun i => if i < (j : ℕ) then W n q qi i else 0) n,
    ← Finset.sum_filter]
  have hf : (Finset.range n).filter (· < (j : ℕ)) = Finset.range j := by
    ext m; simp only [Finset.mem_filter, Finset.mem_range]; omega
  rw [hf]
  exact curl_nat q qi j j.2

/-- **The curl.**  Closing the left strand of the crossing gives `q^n`. -/
theorem ptr_cross (Y : ModuleCat.{u} R) :
    ptr (wt n q qi) (X R n ⊗ Y) (leftCross (S q qi) Y) = q ^ n • 𝟙 (X R n ⊗ Y) := by
  apply hom_ext_left
  intro j y
  rw [ptr_apply, ModuleCat.hom_sum, LinearMap.coeFn_sum, Finset.sum_apply]
  simp only [ModuleCat.hom_smul, LinearMap.smul_apply, ins_leftCross_rem, smul_smul,
    ← Finset.sum_smul, curl_sum, ModuleCat.hom_id, LinearMap.id_apply]

/-! ## The double closure is invariant under the crossing -/

/-- Morphisms out of `X ⊗ (X ⊗ Y)` agree if they agree on `e_a ⊗ (e_b ⊗ y)`. -/
theorem hom_ext_left2 {Y W : ModuleCat.{u} R} {f g : X R n ⊗ (X R n ⊗ Y) ⟶ W}
    (h : ∀ a b (y : Y),
      f.hom (e a ⊗ₜ (e b ⊗ₜ y : TensorProduct R (X R n) Y) :
        TensorProduct R (X R n) (TensorProduct R (X R n) Y)) =
      g.hom (e a ⊗ₜ (e b ⊗ₜ y : TensorProduct R (X R n) Y) :
        TensorProduct R (X R n) (TensorProduct R (X R n) Y))) : f = g := by
  ext1
  apply TensorProduct.ext
  apply (basX R n).ext
  intro a
  apply TensorProduct.ext
  apply (basX R n).ext
  intro b
  ext y
  simpa [basX_apply] using h a b y

/-- Insert `e_a ⊗ e_b` on the left: `y ↦ e_a ⊗ (e_b ⊗ y)`. -/
noncomputable def ins2 (p : Fin n × Fin n) (Y : ModuleCat.{u} R) : Y ⟶ X R n ⊗ (X R n ⊗ Y) :=
  ins p.2 Y ≫ ins p.1 (X R n ⊗ Y)

/-- Remove `e_a ⊗ e_b` on the left: `x₁ ⊗ (x₂ ⊗ y) ↦ x₁_a x₂_b · y`. -/
noncomputable def rem2 (p : Fin n × Fin n) (Y : ModuleCat.{u} R) : X R n ⊗ (X R n ⊗ Y) ⟶ Y :=
  rem p.1 (X R n ⊗ Y) ≫ rem p.2 Y

/-- The double closure as a single sum over pairs of basis indices. -/
theorem ptr_ptr (w : Fin n → R) (Y : ModuleCat.{u} R) (h : X R n ⊗ (X R n ⊗ Y) ⟶ X R n ⊗ (X R n ⊗ Y)) :
    ptr w Y (ptr w (X R n ⊗ Y) h) = ∑ p : Fin n × Fin n, (w p.2 * w p.1) • (ins2 p Y ≫ h ≫ rem2 p Y) := by
  simp only [ptr_apply, Preadditive.comp_sum, Preadditive.sum_comp, Linear.comp_smul,
    Linear.smul_comp, Finset.smul_sum, smul_smul, ins2, rem2, Category.assoc]
  rw [Fintype.sum_prod_type, Finset.sum_comm]

/-- The coefficient of `e_c ⊗ e_d` in `Ř (e_a ⊗ e_b)`. -/
noncomputable def coef (c p : Fin n × Fin n) : R := (bas R n).repr (rv q qi p.1 p.2) c

theorem rv_eq_sum (p : Fin n × Fin n) :
    rv q qi p.1 p.2 = ∑ c : Fin n × Fin n, coef q qi c p • (e c.1 ⊗ₜ e c.2 : XX R n) := by
  conv_lhs => rw [← (bas R n).sum_repr (rv q qi p.1 p.2)]
  refine Finset.sum_congr rfl fun c _ => ?_
  obtain ⟨a, b⟩ := c
  rw [bas_apply, coef]

theorem ins2_apply (p : Fin n × Fin n) (Y : ModuleCat.{u} R) (y : Y) :
    (ins2 p Y).hom y = (e p.1 ⊗ₜ (e p.2 ⊗ₜ y : TensorProduct R (X R n) Y) :
      TensorProduct R (X R n) (TensorProduct R (X R n) Y)) := rfl

set_option synthInstance.maxHeartbeats 200000 in
theorem leftCross_apply (Y : ModuleCat.{u} R) (a b : Fin n) (y : Y) :
    (leftCross (S q qi) Y).hom (e a ⊗ₜ (e b ⊗ₜ y : TensorProduct R (X R n) Y) :
      TensorProduct R (X R n) (TensorProduct R (X R n) Y)) =
      ∑ c : Fin n × Fin n, coef q qi c (a, b) •
        (e c.1 ⊗ₜ (e c.2 ⊗ₜ y : TensorProduct R (X R n) Y) :
          TensorProduct R (X R n) (TensorProduct R (X R n) Y)) := by
  change (α_ (X R n) (X R n) Y).hom.hom ((S q qi ▷ Y).hom ((α_ (X R n) (X R n) Y).inv.hom
    (e a ⊗ₜ (e b ⊗ₜ y : TensorProduct R (X R n) Y) :
      TensorProduct R (X R n) (TensorProduct R (X R n) Y)))) = _
  rw [hom_assoc_inv_apply, TensorProduct.assoc_symm_tmul, S_whiskerRight_apply',
    LinearMap.rTensor_tmul, rLin_ee, hom_assoc_apply]
  rw [show rv q qi a b = rv q qi (a, b).1 (a, b).2 from rfl, rv_eq_sum, TensorProduct.sum_tmul,
    map_sum]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [← TensorProduct.smul_tmul', map_smul, TensorProduct.assoc_tmul]

/-- Moving the crossing into the inserted pair. -/
theorem ins2_cross (p : Fin n × Fin n) (Y : ModuleCat.{u} R) :
    ins2 p Y ≫ leftCross (S q qi) Y = ∑ c : Fin n × Fin n, coef q qi c p • ins2 c Y := by
  ext y
  rw [ModuleCat.hom_comp, LinearMap.comp_apply, ins2_apply, leftCross_apply, ModuleCat.hom_sum,
    LinearMap.coeFn_sum, Finset.sum_apply]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [ModuleCat.hom_smul, LinearMap.smul_apply, ins2_apply]

theorem rem2_apply (p : Fin n × Fin n) (Y : ModuleCat.{u} R) (a b : Fin n) (y : Y) :
    (rem2 p Y).hom (e a ⊗ₜ (e b ⊗ₜ y : TensorProduct R (X R n) Y) :
      TensorProduct R (X R n) (TensorProduct R (X R n) Y)) =
      if (a, b) = p then y else 0 := by
  change (rem p.2 Y).hom ((rem p.1 (X R n ⊗ Y)).hom (e a ⊗ₜ (e b ⊗ₜ y : TensorProduct R (X R n) Y) :
      TensorProduct R (X R n) (TensorProduct R (X R n) Y))) = _
  rw [show (rem p.1 (X R n ⊗ Y)).hom (e a ⊗ₜ (e b ⊗ₜ y : TensorProduct R (X R n) Y) :
      TensorProduct R (X R n) (TensorProduct R (X R n) Y)) =
      (e a : Fin n → R) p.1 • (e b ⊗ₜ y : TensorProduct R (X R n) Y) from rem_apply _ _ _ _,
    map_smul, rem_apply]
  obtain ⟨c, d⟩ := p
  by_cases h1 : a = c <;> by_cases h2 : b = d <;> simp [e_apply, h1, h2]

/-- Moving the crossing into the removed pair. -/
theorem cross_rem2 (p : Fin n × Fin n) (Y : ModuleCat.{u} R) :
    leftCross (S q qi) Y ≫ rem2 p Y = ∑ c : Fin n × Fin n, coef q qi p c • rem2 c Y := by
  apply hom_ext_left2
  intro a b y
  rw [ModuleCat.hom_comp, LinearMap.comp_apply, leftCross_apply, map_sum, ModuleCat.hom_sum,
    LinearMap.coeFn_sum, Finset.sum_apply]
  simp only [map_smul, rem2_apply, ModuleCat.hom_smul, LinearMap.smul_apply, smul_ite, smul_zero,
    Finset.sum_ite_eq', Finset.mem_univ, if_true]
  rw [Finset.sum_ite_eq]
  simp

theorem repr_ee (a b : Fin n) : (bas R n).repr (e a ⊗ₜ e b : XX R n) = Finsupp.single (a, b) 1 := by
  rw [← bas_apply, Basis.repr_self]

/-- `Ř` only permutes the two tensor indices: `Ř (e_a ⊗ e_b)` has no component outside
`{e_a ⊗ e_b, e_b ⊗ e_a}`. -/
theorem coef_eq_zero {c p : Fin n × Fin n} (h1 : c ≠ p) (h2 : c ≠ p.swap) : coef q qi c p = 0 := by
  obtain ⟨a, b⟩ := p
  have h1' : (a, b) ≠ c := Ne.symm h1
  have h2' : (b, a) ≠ c := Ne.symm h2
  rcases lt_trichotomy a b with h | rfl | h
  · simp [coef, rv_lt q qi h, repr_ee, Finsupp.single_apply, h1', h2']
  · simp [coef, rv_self, repr_ee, Finsupp.single_apply, h1']
  · simp [coef, rv_gt q qi h, repr_ee, Finsupp.single_apply, h2']

/-- **Weight conservation.**  For any weights, `w_a w_b = w_c w_d` wherever `e_c ⊗ e_d` occurs in
`Ř (e_a ⊗ e_b)`. -/
theorem coef_weight (w : Fin n → R) (c p : Fin n × Fin n) :
    coef q qi c p * (w p.2 * w p.1) = coef q qi c p * (w c.2 * w c.1) := by
  by_cases h1 : c = p
  · rw [h1]
  by_cases h2 : c = p.swap
  · rw [h2, Prod.fst_swap, Prod.snd_swap, mul_comm (w p.1)]
  · rw [coef_eq_zero q qi h1 h2, zero_mul, zero_mul]

/-- **Markov's first move on the two closed strands.**  The double weighted closure of `Ř ≫ f`
equals that of `f ≫ Ř`, for any weights. -/
theorem ptr2_conj (w : Fin n → R) (Y : ModuleCat.{u} R) (f : X R n ⊗ (X R n ⊗ Y) ⟶ X R n ⊗ (X R n ⊗ Y)) :
    ptr w Y (ptr w (X R n ⊗ Y) (leftCross (S q qi) Y ≫ f)) =
      ptr w Y (ptr w (X R n ⊗ Y) (f ≫ leftCross (S q qi) Y)) := by
  rw [ptr_ptr, ptr_ptr]
  simp only [← Category.assoc, ins2_cross]
  simp only [Category.assoc, cross_rem2, Preadditive.sum_comp, Preadditive.comp_sum,
    Linear.smul_comp, Linear.comp_smul, Finset.smul_sum, smul_smul]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun p _ => ?_
  rw [mul_comm (w p.2 * w p.1), coef_weight q qi w c p, mul_comm]

/-! ## The left trace and the Markov trace -/

/-- **The quantum partial trace of the `GL_n` model is a left trace**, with loop value
`d = ∑_i q^{n-1-i} qi^i` and curl value `q^n`. -/
noncomputable def leftTrace (h : q * qi = 1) : LeftTrace (crossing (n := n) q qi h) where
  ptr := ptr (wt n q qi)
  ptr_whisker_comp := ptr_whisker_comp _
  ptr_comp_whisker := ptr_comp_whisker _
  d := ∑ i, wt n q qi i
  w := q ^ n
  ptr_id := ptr_id _
  ptr_cross := ptr_cross q qi
  ptr2_conj := ptr2_conj q qi _

@[simp] theorem leftTrace_d (h : q * qi = 1) :
    (leftTrace (n := n) q qi h).d = ∑ i, wt n q qi i := rfl

@[simp] theorem leftTrace_w (h : q * qi = 1) : (leftTrace (n := n) q qi h).w = q ^ n := rfl

/-- **The loop value is the quantum integer.**  `(q - qi) · d = q^n - qi^n`, i.e. `d = [n]_q`;
in Brundan's variables (`t = q^n`, `z = q - qi`) this is `z δ = t - t⁻¹`. -/
theorem loop_mul (h : q * qi = 1) :
    (leftTrace (n := n) q qi h).d * (q - qi) = q ^ n - qi ^ n := by
  have hs : (∑ i, wt n q qi i) = ∑ i ∈ Finset.range n, qi ^ i * q ^ (n - 1 - i) := by
    rw [show (∑ i, wt n q qi i) = ∑ i : Fin n, W n q qi i from rfl,
      Fin.sum_univ_eq_sum_range (fun i => W n q qi i) n]
    exact Finset.sum_congr rfl fun i _ => by rw [W, mul_comm]
  rw [leftTrace_d, hs]
  have := Commute.geom_sum₂_mul (Commute.all qi q) n
  linear_combination -this

variable (R) in
/-- The scalar of an endomorphism of the unit object `R` of `ModuleCat R`: `f ↦ f 1`. -/
noncomputable def unitScalar : (𝟙_ (ModuleCat.{u} R) ⟶ 𝟙_ (ModuleCat.{u} R)) →ₗ[R] R where
  toFun f := f.hom (1 : R)
  map_add' f g := rfl
  map_smul' r f := rfl

theorem unitScalar_id : unitScalar R (𝟙 _) = 1 := rfl

/-- **The normalised closure of the `GL_n` model is a Markov trace** on the Hecke tower, with
Markov parameter `z = q^n / [n]_q` (here `dinv` is an inverse of `[n]_q`). -/
noncomputable def markovFamily (h : q * qi = 1) (dinv : R)
    (hd : (∑ i, wt n q qi i) * dinv = 1) :
    HeckeCoset.MarkovTraceFamily R q qi (q ^ n * dinv) :=
  (leftTrace (n := n) q qi h).markovFamily (unitScalar R) (unitScalar_id) dinv hd

/-- The value of the closure trace: `tr_m (x) = d^{-(m+1)} · (closure of ρ_m(x))`. -/
theorem markovFamily_tr (h : q * qi = 1) (dinv : R) (hd : (∑ i, wt n q qi i) * dinv = 1)
    (m : ℕ) (x : Hecke R q qi m) :
    (markovFamily q qi h dinv hd).tr m x =
      dinv ^ (m + 1) * unitScalar R ((leftTrace (n := n) q qi h).fullTr (m + 1)
        ((crossing (n := n) q qi h).revAction m x)) := rfl

/-- **The closure is THE Markov trace with parameter `q^n/[n]_q`.**  It agrees with every Markov
trace family on the Hecke tower with that parameter. -/
theorem markov_eq (h : q * qi = 1) (dinv : R) (hd : (∑ i, wt n q qi i) * dinv = 1)
    (T : HeckeCoset.MarkovTraceFamily R q qi (q ^ n * dinv)) (m : ℕ) (x : Hecke R q qi m) :
    (markovFamily q qi h dinv hd).tr m x = T.tr m x :=
  HeckeCoset.markovTrace_unique _ T m x

/-- The trace of the single crossing `σ_0 ∈ H_2` is the Markov parameter `q^n/[n]_q`. -/
theorem markovFamily_sigma (h : q * qi = 1) (dinv : R) (hd : (∑ i, wt n q qi i) * dinv = 1) :
    (markovFamily q qi h dinv hd).tr 1 (Hecke.σ R q qi 1 (Fin.last 0)) = q ^ n * dinv :=
  HeckeCoset.MarkovTraceFamily.param_eq _

end QOU.OrientedSkein.GLn
