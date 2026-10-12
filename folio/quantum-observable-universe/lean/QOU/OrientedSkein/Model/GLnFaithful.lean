/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.Model.GLnRMatrix
import QOU.OrientedSkein.Model.GLnTrace
import QOU.SchurWeyl.HeckeStandardBasis

/-!
# `QOU.OrientedSkein.Model.GLnFaithful` — the Hecke action on `(R^n)^{⊗(m+1)}` is faithful for `m < n`

Open item 2 of dispatch B (PR #7705, bean `qou-slck`).

For the `GL_n` R-matrix on `X = R^n` (`QOU.OrientedSkein.Model.GLnRMatrix`), the induced algebra map
`H_{m+1}(q) → End (X^{⊗(m+1)})` (`HeckeCrossing.heckeAction`) is **injective** whenever `m + 1 ≤ n`,
over **any** commutative ring `R` with `q * qi = 1` — no genericity of `q`, no field.

## Proof

* `tvec a = e_{a 0} ⊗ (e_{a 1} ⊗ ⋯)` is the basis tensor of a word `a : Fin k → Fin n`.
* On a descent `a i > a (i+1)` the crossing on strands `i, i+1` is a pure swap (`gen_tvec`):
  `Ř (e_a ⊗ e_b) = e_b ⊗ e_a` for `a > b`, with no correction term.
* Take the strictly decreasing word `d j = m - j` (this is where `m + 1 ≤ n` is used).  Along a
  reduced word every letter meets a descent, so `T_w (tvec d) = tvec (d ∘ w⁻¹)` exactly
  (`stdElt_tvec`).  Reducedness is measured by the inversion number `ninv` of
  `QOU.SchurWeyl.HeckeCoset`; we add `ninv_inv` (`ninv w⁻¹ = ninv w`) and the head-recursive bound
  `ninv_mul_word_le`.
* The `T_w` span `H_{m+1}(q)` (`HeckeCoset.span_cosetFam_eq_top`), and the vectors
  `tvec (d ∘ w⁻¹)` for distinct `w` are distinct basis tensors, separated by the coordinate
  functionals `coord` (`coord_tvec`).  So `ρ(x) = 0` forces every coefficient of `x` to vanish.

Sorry-free; no axioms beyond Lean/Mathlib's.

## References

* [jimbo1986] M. Jimbo, *A q-analogue of U(gl(N+1)), Hecke algebra, and the Yang–Baxter equation*.
* [mathas1999] A. Mathas, *Iwahori–Hecke algebras and Schur algebras of the symmetric group*,
  Ch. 1 (the `T_w` basis).
-/

namespace QOU.OrientedSkein.GLn

open CategoryTheory MonoidalCategory Equiv QOU.SchurWeyl QOU.SchurWeyl.HeckeCoset

universe u

variable {R : Type u} [CommRing R] {n : ℕ}

variable (R n) in
/-- `X^{⊗k}` as an object of `ModuleCat R`. -/
noncomputable abbrev P (k : ℕ) : ModuleCat.{u} R := tpow (X R n) k

/-! ## Basis tensors -/

/-- The basis tensor `e_{a 0} ⊗ (e_{a 1} ⊗ (⋯ ⊗ 1))` of `X^{⊗k}`. -/
noncomputable def tvec : (k : ℕ) → (Fin k → Fin n) → P R n k
  | 0, _ => (1 : R)
  | k + 1, a => (e (a 0) ⊗ₜ tvec k (Fin.tail a) : TensorProduct R (X R n) (P R n k))

theorem tvec_succ (k : ℕ) (a : Fin (k + 1) → Fin n) :
    tvec (R := R) (k + 1) a =
      (e (a 0) ⊗ₜ tvec k (Fin.tail a) : TensorProduct R (X R n) (P R n k)) := rfl

/-! ## A crossing on a descent is a pure swap -/

variable (q qi : R)

theorem whiskerLeft_X_apply {Y Z : ModuleCat.{u} R} (g : Y ⟶ Z) (x : TensorProduct R (X R n) Y) :
    (X R n ◁ g).hom x = g.hom.lTensor (X R n) x := rfl

theorem adjT_zero_zero (k : ℕ) : adjT (0 : Fin (k + 1)) 0 = 1 := by
  simp [adjT, swap_apply_def, Fin.ext_iff]

theorem adjT_zero_one (k : ℕ) : adjT (0 : Fin (k + 1)) 1 = 0 := by
  simp [adjT, swap_apply_def, Fin.ext_iff]

theorem adjT_zero_ss (k : ℕ) (j : Fin k) : adjT (0 : Fin (k + 1)) j.succ.succ = j.succ.succ := by
  simp only [adjT, swap_apply_def]
  split_ifs with h1 h2 <;> simp_all [Fin.ext_iff]

theorem adjT_succ_zero (k : ℕ) (j : Fin k) : adjT j.succ (0 : Fin (k + 2)) = 0 := by
  simp only [adjT, swap_apply_def]
  split_ifs with h1 h2 <;> simp_all [Fin.ext_iff]

theorem adjT_succ_succ (k : ℕ) (j : Fin k) (x : Fin (k + 1)) :
    adjT j.succ x.succ = (adjT j x).succ := by
  simp only [adjT, swap_apply_def, Fin.ext_iff, Fin.val_succ, Fin.coe_castSucc]
  split_ifs <;> simp_all [Fin.ext_iff] <;> omega

/-- **On a descent the crossing is a pure swap**: if `a (i+1) < a i` then the crossing on strands
`i, i+1` sends `tvec a` to `tvec (a ∘ (i i+1))`. -/
theorem gen_tvec (h : q * qi = 1) : ∀ (k : ℕ) (i : Fin (k + 1)) (a : Fin (k + 2) → Fin n),
    a i.succ < a i.castSucc →
      ((crossing (n := n) q qi h).gen (k + 1) i).hom (tvec (k + 2) a) = tvec (k + 2) (a ∘ adjT i)
  | k, ⟨0, h0⟩, a, hd => by
      rw [HeckeCrossing.gen_zero]
      change (α_ (X R n) (X R n) (P R n k)).hom.hom ((S q qi ▷ P R n k).hom
        ((α_ (X R n) (X R n) (P R n k)).inv.hom (e (a 0) ⊗ₜ (e (Fin.tail a 0) ⊗ₜ
          tvec k (Fin.tail (Fin.tail a)) : TensorProduct R (X R n) (P R n k)) :
            TensorProduct R (X R n) (TensorProduct R (X R n) (P R n k))))) = _
      rw [hom_assoc_inv_apply, TensorProduct.assoc_symm_tmul, S_whiskerRight_apply',
        LinearMap.rTensor_tmul, rLin_ee]
      have hd' : a 1 < a 0 := hd
      rw [show Fin.tail a 0 = a 1 from rfl, rv_gt q qi hd', hom_assoc_apply, TensorProduct.assoc_tmul]
      change _ = (e ((a ∘ adjT 0) 0) ⊗ₜ (e ((a ∘ adjT 0) 1) ⊗ₜ
          tvec k (Fin.tail (Fin.tail (a ∘ adjT 0))) : TensorProduct R (X R n) (P R n k)) :
            TensorProduct R (X R n) (TensorProduct R (X R n) (P R n k)))
      have htt : Fin.tail (Fin.tail (a ∘ adjT (0 : Fin (k + 1)))) = Fin.tail (Fin.tail a) := by
        funext j
        simp only [Fin.tail, Function.comp_apply, adjT_zero_ss]
      simp only [Function.comp_apply, adjT_zero_zero, adjT_zero_one, htt]
  | k + 1, ⟨j + 1, hj⟩, a, hd => by
      rw [HeckeCrossing.gen_succ]
      change (X R n ◁ (crossing (n := n) q qi h).gen (k + 1) ⟨j, _⟩).hom
        (e (a 0) ⊗ₜ tvec (k + 2) (Fin.tail a) : TensorProduct R (X R n) (P R n (k + 2))) = _
      rw [whiskerLeft_X_apply, LinearMap.lTensor_tmul]
      have hd' : Fin.tail a (⟨j, by omega⟩ : Fin (k + 1)).succ <
          Fin.tail a (⟨j, by omega⟩ : Fin (k + 1)).castSucc := hd
      rw [gen_tvec h k ⟨j, by omega⟩ (Fin.tail a) hd']
      change _ = (e ((a ∘ adjT ⟨j + 1, hj⟩) 0) ⊗ₜ tvec (k + 2) (Fin.tail (a ∘ adjT ⟨j + 1, hj⟩)) :
        TensorProduct R (X R n) (P R n (k + 2)))
      have e0 : (a ∘ adjT (⟨j + 1, hj⟩ : Fin (k + 2))) 0 = a 0 := by
        simpa using congrArg a (adjT_succ_zero (k + 1) ⟨j, by omega⟩)
      have et : Fin.tail (a ∘ adjT (⟨j + 1, hj⟩ : Fin (k + 2))) =
          Fin.tail a ∘ adjT (⟨j, by omega⟩ : Fin (k + 1)) := by
        funext x
        simp only [Fin.tail, Function.comp_apply]
        exact congrArg a (adjT_succ_succ (k + 1) ⟨j, by omega⟩ x)
      rw [e0, et]

theorem gen_tvec' (h : q * qi = 1) (m : ℕ) (i : Fin m) (a : Fin (m + 1) → Fin n)
    (hd : a i.succ < a i.castSucc) :
    ((crossing (n := n) q qi h).gen m i).hom (tvec (m + 1) a) = tvec (m + 1) (a ∘ adjT i) := by
  cases m with
  | zero => exact i.elim0
  | succ k => exact gen_tvec q qi h k i a hd

/-! ## Inversions along words -/

/-- `ninv w⁻¹ = ninv w`. -/
theorem ninv_inv {k : ℕ} (w : Perm (Fin k)) : ninv w⁻¹ = ninv w := by
  unfold ninv
  refine Finset.card_nbij' (fun p => (w⁻¹ p.2, w⁻¹ p.1)) (fun p => (w p.2, w p.1)) ?_ ?_ ?_ ?_
  · intro p hp
    simp only [Finset.coe_filter, Finset.mem_univ, true_and, Set.mem_setOf_eq] at hp ⊢
    refine ⟨hp.2, ?_⟩
    simpa using hp.1
  · intro p hp
    simp only [Finset.coe_filter, Finset.mem_univ, true_and, Set.mem_setOf_eq] at hp ⊢
    refine ⟨hp.2, ?_⟩
    simpa using hp.1
  · intro p _
    simp
  · intro p _
    simp

/-- Head-recursive bound: `ninv (π · s_{u₀} ⋯ s_{u_l}) ≤ ninv π + l`. -/
theorem ninv_mul_word_le {k : ℕ} : ∀ (u : List (Fin k)) (π : Perm (Fin (k + 1))),
    ninv (π * (u.map adjT).prod) ≤ ninv π + u.length
  | [], π => by simp
  | i :: u, π => by
      rw [List.map_cons, List.prod_cons, ← mul_assoc, List.length_cons]
      have := ninv_mul_word_le u (π * adjT i)
      have := ninv_mul_adjT_le π i
      omega

/-- At a descent of `π` at `i`, right multiplication by `s_i` removes an inversion. -/
theorem ninv_mul_adjT_of_gt {k : ℕ} (π : Perm (Fin (k + 1))) (i : Fin k)
    (hlt : π i.succ < π i.castSucc) : ninv (π * adjT i) + 1 = ninv π := by
  have h' : (π * adjT i) i.castSucc < (π * adjT i) i.succ := by
    simpa [adjT, Perm.mul_apply, swap_apply_left, swap_apply_right] using hlt
  have e := ninv_mul_adjT_of_lt (π * adjT i) i h'
  have hs : adjT i * adjT i = 1 := swap_mul_self _ _
  rw [mul_assoc, hs, mul_one] at e
  omega

/-! ## Reduced words act by permuting a strictly decreasing word -/

/-- **Along a reduced word, the Hecke action permutes a strictly decreasing basis tensor.** -/
theorem action_word (h : q * qi = 1) {m : ℕ} (d : Fin (m + 1) → Fin n) (hd : StrictAnti d) :
    ∀ (u : List (Fin m)) (π : Perm (Fin (m + 1))),
      ninv (π * (u.map adjT).prod) = ninv π + u.length →
      ((crossing (n := n) q qi h).heckeAction m ((u.reverse.map (Hecke.σ R q qi m)).prod)).hom
          (tvec (m + 1) (d ∘ ⇑π)) = tvec (m + 1) (d ∘ ⇑(π * (u.map adjT).prod))
  | [], π, _ => by
      rw [List.reverse_nil, List.map_nil, List.prod_nil, map_one, End.one_def, ModuleCat.hom_id,
        LinearMap.id_apply, List.map_nil, List.prod_nil, mul_one]
  | i :: u, π, hu => by
      rw [List.map_cons, List.prod_cons, ← mul_assoc, List.length_cons] at hu
      have hb1 := ninv_mul_word_le u (π * adjT i)
      have hb2 := ninv_mul_adjT_le π i
      have hasc : π i.castSucc < π i.succ := by
        rcases lt_or_gt_of_ne (π.injective.ne (Fin.castSucc_lt_succ i).ne) with hl | hl
        · exact hl
        · have := ninv_mul_adjT_of_gt π i hl
          omega
      have hih : ninv (π * adjT i * (u.map adjT).prod) = ninv (π * adjT i) + u.length := by omega
      rw [List.reverse_cons, List.map_append, List.prod_append, List.map_singleton,
        List.prod_singleton, map_mul ((crossing (n := n) q qi h).heckeAction m), End.mul_def, ModuleCat.hom_comp, LinearMap.comp_apply,
        HeckeCrossing.heckeAction_σ, gen_tvec' q qi h m i (d ∘ π) (hd hasc)]
      rw [show (d ∘ ⇑π) ∘ ⇑(adjT i) = d ∘ ⇑(π * adjT i) from rfl, action_word h d hd u (π * adjT i) hih,
        List.map_cons, List.prod_cons, mul_assoc]

theorem adjT_inv {k : ℕ} (i : Fin k) : (adjT i)⁻¹ = adjT i := swap_inv _ _

theorem prod_reverse_adjT {k : ℕ} : ∀ l : List (Fin k),
    (l.reverse.map adjT).prod = ((l.map adjT).prod)⁻¹
  | [] => by simp
  | i :: l => by
      rw [List.reverse_cons, List.map_append, List.prod_append, List.map_singleton,
        List.prod_singleton, prod_reverse_adjT l, List.map_cons, List.prod_cons, mul_inv_rev,
        adjT_inv]

/-- **`T_w` sends the strictly decreasing basis tensor `tvec d` to `tvec (d ∘ w⁻¹)`.** -/
theorem stdElt_tvec (h : q * qi = 1) {m : ℕ} (d : Fin (m + 1) → Fin n) (hd : StrictAnti d)
    (w : Perm (Fin (m + 1))) :
    ((crossing (n := n) q qi h).heckeAction m (stdElt (K := R) (q := q) (qi := qi) m w)).hom
        (tvec (m + 1) d) = tvec (m + 1) (d ∘ ⇑w⁻¹) := by
  have hw : ((stdWord m w).reverse.map adjT).prod = w⁻¹ := by
    rw [prod_reverse_adjT, stdWord_prod_eq]
  have key := action_word q qi h d hd (stdWord m w).reverse 1
    (by rw [one_mul, hw, ninv_inv, ninv_one, zero_add, List.length_reverse, stdWord_length])
  rw [List.reverse_reverse, one_mul, hw] at key
  rw [stdElt_eq_prod_word]
  exact key

/-! ## Coordinates of basis tensors -/

/-- The coordinate functional `tvec a ↦ δ_{a b}` on `X^{⊗k}`. -/
noncomputable def coord : (k : ℕ) → (Fin k → Fin n) → (P R n k →ₗ[R] R)
  | 0, _ => (LinearMap.id : R →ₗ[R] R)
  | k + 1, b => TensorProduct.lift ((LinearMap.mul R R).compl₁₂
      (LinearMap.proj (R := R) (φ := fun _ : Fin n => R) (b 0)) (coord k (Fin.tail b)))

theorem coord_tvec : ∀ (k : ℕ) (a b : Fin k → Fin n),
    coord k b (tvec (R := R) k a) = if a = b then 1 else 0
  | 0, a, b => by
      have : a = b := funext fun i => i.elim0
      rw [if_pos this]
      rfl
  | k + 1, a, b => by
      change TensorProduct.lift ((LinearMap.mul R R).compl₁₂
        (LinearMap.proj (R := R) (φ := fun _ : Fin n => R) (b 0)) (coord k (Fin.tail b)))
          (e (a 0) ⊗ₜ tvec k (Fin.tail a) : TensorProduct R (X R n) (P R n k)) = _
      erw [TensorProduct.lift.tmul]
      rw [LinearMap.compl₁₂_apply, LinearMap.mul_apply', coord_tvec k]
      change (e (a 0) : Fin n → R) (b 0) * _ = _
      rw [e_apply]
      by_cases h0 : a 0 = b 0
      · by_cases ht : Fin.tail a = Fin.tail b
        · have hab : a = b := by
            funext i
            refine Fin.cases h0 (fun j => congrFun ht j) i
          simp [h0, ht, hab]
        · have hab : a ≠ b := fun hab => ht (by rw [hab])
          simp [h0, ht, hab]
      · have hab : a ≠ b := fun hab => h0 (by rw [hab])
        simp [h0, hab]

/-! ## Faithfulness -/

/-- **The `GL_n` Hecke action on `(R^n)^{⊗(m+1)}` is faithful for `m + 1 ≤ n`**, over any
commutative ring with `q * qi = 1`. -/
theorem heckeAction_injective (h : q * qi = 1) {m : ℕ} (hm : m + 1 ≤ n) :
    Function.Injective ((crossing (n := n) q qi h).heckeAction m) := by
  rw [injective_iff_map_eq_zero]
  intro x hx
  set d : Fin (m + 1) → Fin n := fun j => ⟨m - j, by omega⟩ with hd_def
  have hd : StrictAnti d := by
    intro i j hij
    simp only [hd_def, Fin.lt_iff_val_lt_val] at hij ⊢
    have := j.2
    omega
  have hmem : x ∈ Submodule.span R (Set.range (cosetFam (K := R) (q := q) (qi := qi) m)) := by
    rw [span_cosetFam_eq_top]
    trivial
  obtain ⟨c, rfl⟩ := (Submodule.mem_span_range_iff_exists_fun R).mp hmem
  have hfam : ∀ p, cosetFam (K := R) (q := q) (qi := qi) m p =
      stdElt (K := R) (q := q) (qi := qi) m (permOf m p) := by
    intro p
    rw [stdElt]
    exact congrArg _ ((permOfEquiv m).symm_apply_apply p).symm
  let evalV : End (P R n (m + 1)) →ₗ[R] P R n (m + 1) :=
    { toFun := fun f => f.hom (tvec (m + 1) d)
      map_add' := fun _ _ => rfl
      map_smul' := fun _ _ => rfl }
  have hv := congrArg evalV hx
  rw [map_sum, map_sum, map_zero] at hv
  simp only [map_smul, hfam] at hv
  have hev : ∀ p, evalV ((crossing (n := n) q qi h).heckeAction m
      (stdElt (K := R) (q := q) (qi := qi) m (permOf m p))) = tvec (m + 1) (d ∘ ⇑(permOf m p)⁻¹) :=
    fun p => stdElt_tvec q qi h d hd _
  simp only [hev] at hv
  have hc : ∀ p0, c p0 = 0 := by
    intro p0
    have := congrArg (coord (m + 1) (d ∘ ⇑(permOf m p0)⁻¹)) hv
    rw [map_sum, map_zero] at this
    simp only [map_smul, coord_tvec, smul_eq_mul, mul_ite, mul_one, mul_zero] at this
    rw [Finset.sum_eq_single p0 (fun p _ hp => if_neg fun heq => hp ?_) (by simp)] at this
    · simpa using this
    · apply permOf_injective m
      have h1 := hd.injective.comp_left heq
      exact inv_injective (Equiv.ext fun x => congrFun h1 x)
  simp [hc]

end QOU.OrientedSkein.GLn
