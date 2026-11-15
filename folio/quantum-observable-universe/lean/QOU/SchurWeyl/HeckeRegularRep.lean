import QOU.SchurWeyl.HeckeMultiplicationRule

/-!
# QOU.SchurWeyl.HeckeRegularRep — the `T_w` are linearly independent over any ring

Over an arbitrary commutative ring `K`, with `q, qi : K` free, the elements
`T_w = stdElt m w` (`w ∈ S_{m+1}`) are **linearly independent** in `H_{m+1}(q)`, so they form a
basis (`stdBasisAny`).  `HeckeStandardBasisIndep` proves the same only at generic `q` over a
characteristic-zero field, by counting dimensions.

## Proof: the regular representation

Let `E` be the free `K`-module on `S_{m+1}`, with basis `e_w`.  Put `c = q − qi`, `d = q·qi`, and
let `L_i, R_j : E → E` be

```
L_i e_w = e_{s_i w}                  if w⁻¹(i) < w⁻¹(i+1),   else  c e_w + d e_{s_i w},
R_j e_w = e_{w s_j}                  if w(j) < w(j+1),       else  c e_w + d e_{w s_j}.
```

1. `L_i` and `R_j` commute (`Lop_comm_Rop`).  If `{w(j), w(j+1)} ≠ {i, i+1}`, then left-
   multiplying by `s_i` does not change the right test at `j`, and right-multiplying by `s_j`
   does not change the left test at `i`, so the two orders agree by direct expansion.  Otherwise
   `s_i w = w s_j`, and the four expansions are checked by hand.
2. Any operator commuting with every `R_j` is determined by its value on `e_1`
   (`eq_of_comm_Rop`): `e_w` is `e_1` pushed through the `R_j` along a reduced word for `w`.
3. So the Hecke relations hold for the `L_i`: the quadratic relation by direct expansion, and
   the braid and commutation relations because both sides commute with all `R_j` and agree on
   `e_1`.  This gives `ρ : H_{m+1}(q) → End_K E` with `σ_i ↦ L_i` (`regRep`).
4. `ρ(T_w) e_1 = e_w` (`regRep_stdElt_one`), so a linear relation among the `T_w` becomes one
   among the `e_w`, which are independent.

## Base ring (§7c)

Generic `[CommRing K]`, no hypotheses on `q, qi`.  Nothing archimedean.

LaTeX label: `thm:hecke-standard-basis`

-- Ref: [humphreys1990] https://doi.org/10.1017/CBO9780511623646 (§7.3: the regular representation of the generic algebra)
-/

namespace QOU.SchurWeyl
namespace HeckeCoset

open Hecke Equiv Finsupp

variable {K : Type*} [CommRing K] (q qi : K)

/-- The free module on `S_{m+1}`. -/
abbrev RegMod (K : Type*) [CommRing K] (m : ℕ) := Perm (Fin (m + 1)) →₀ K

/-- The left operator `L_i`. -/
noncomputable def Lop (m : ℕ) (i : Fin m) : Module.End K (RegMod K m) :=
  Finsupp.linearCombination K fun w =>
    if w⁻¹ i.castSucc < w⁻¹ i.succ then single (adjT i * w) 1
    else (q - qi) • single w 1 + (q * qi) • single (adjT i * w) 1

/-- The right operator `R_j`. -/
noncomputable def Rop (m : ℕ) (j : Fin m) : Module.End K (RegMod K m) :=
  Finsupp.linearCombination K fun w =>
    if w j.castSucc < w j.succ then single (w * adjT j) 1
    else (q - qi) • single w 1 + (q * qi) • single (w * adjT j) 1

theorem Lop_single (m : ℕ) (i : Fin m) (w : Perm (Fin (m + 1))) :
    Lop q qi m i (single w 1) =
      if w⁻¹ i.castSucc < w⁻¹ i.succ then single (adjT i * w) 1
      else (q - qi) • single w 1 + (q * qi) • single (adjT i * w) 1 := by
  rw [Lop, linearCombination_single, one_smul]

theorem Rop_single (m : ℕ) (j : Fin m) (w : Perm (Fin (m + 1))) :
    Rop q qi m j (single w 1) =
      if w j.castSucc < w j.succ then single (w * adjT j) 1
      else (q - qi) • single w 1 + (q * qi) • single (w * adjT j) 1 := by
  rw [Rop, linearCombination_single, one_smul]

/-- Two endomorphisms of `E` agreeing on every `e_w` are equal. -/
theorem regMod_ext {m : ℕ} {φ ψ : Module.End K (RegMod K m)}
    (h : ∀ w, φ (single w 1) = ψ (single w 1)) : φ = ψ :=
  Finsupp.lhom_ext fun w b => by rw [← smul_single_one, map_smul, map_smul, h]

theorem adjT_inv {n : ℕ} (i : Fin n) : (adjT i)⁻¹ = adjT i := swap_inv _ _

/-! ## The left and right operators commute -/

/-- If `s_i w = w s_j` fails to be forced, the right test is unchanged by `s_i`. -/
theorem rightTest_adjT_mul {n : ℕ} (i j : Fin n) (w : Perm (Fin (n + 1)))
    (h1 : ¬(w j.castSucc = i.castSucc ∧ w j.succ = i.succ))
    (h2 : ¬(w j.castSucc = i.succ ∧ w j.succ = i.castSucc)) :
    (adjT i * w) j.castSucc < (adjT i * w) j.succ ↔ w j.castSucc < w j.succ := by
  rw [Perm.mul_apply, Perm.mul_apply]
  exact (adjT_lt_iff i _ _ h1 h2).symm

theorem leftTest_mul_adjT {n : ℕ} (i j : Fin n) (w : Perm (Fin (n + 1)))
    (h1 : ¬(w j.castSucc = i.castSucc ∧ w j.succ = i.succ))
    (h2 : ¬(w j.castSucc = i.succ ∧ w j.succ = i.castSucc)) :
    (w * adjT j)⁻¹ i.castSucc < (w * adjT j)⁻¹ i.succ ↔ w⁻¹ i.castSucc < w⁻¹ i.succ := by
  rw [mul_inv_rev, adjT_inv, Perm.mul_apply, Perm.mul_apply]
  refine (adjT_lt_iff j _ _ ?_ ?_).symm
  · rintro ⟨e1, e2⟩
    exact h1 ⟨(Perm.inv_eq_iff_eq.mp e1).symm, (Perm.inv_eq_iff_eq.mp e2).symm⟩
  · rintro ⟨e1, e2⟩
    exact h2 ⟨(Perm.inv_eq_iff_eq.mp e2).symm, (Perm.inv_eq_iff_eq.mp e1).symm⟩

/-- In the special case, `s_i w = w s_j`. -/
theorem adjT_mul_eq_mul_adjT {n : ℕ} (i j : Fin n) (w : Perm (Fin (n + 1)))
    (h : (w j.castSucc = i.castSucc ∧ w j.succ = i.succ) ∨
      (w j.castSucc = i.succ ∧ w j.succ = i.castSucc)) :
    adjT i * w = w * adjT j := by
  have hc : adjT i = w * adjT j * w⁻¹ := by
    show swap i.castSucc i.succ = w * swap j.castSucc j.succ * w⁻¹
    rw [← swap_apply_apply]
    rcases h with ⟨e1, e2⟩ | ⟨e1, e2⟩
    · simp only [e1, e2]
    · simp only [e1, e2, swap_comm]
  rw [hc, inv_mul_cancel_right]

theorem Lop_comm_Rop (m : ℕ) (i j : Fin m) :
    Lop q qi m i * Rop q qi m j = Rop q qi m j * Lop q qi m i := by
  refine regMod_ext fun w => ?_
  simp only [Module.End.mul_apply, Lop_single, Rop_single]
  by_cases hs : (w j.castSucc = i.castSucc ∧ w j.succ = i.succ) ∨
      (w j.castSucc = i.succ ∧ w j.succ = i.castSucc)
  · have he := adjT_mul_eq_mul_adjT i j w hs
    have hw : adjT i * (w * adjT j) = w := by rw [← he, ← mul_assoc, adjT_mul_self, one_mul]
    have hw' : adjT i * w * adjT j = w := by rw [mul_assoc, hw]
    rcases hs with ⟨e1, e2⟩ | ⟨e1, e2⟩
    · have hR : w j.castSucc < w j.succ := by rw [e1, e2]; exact Fin.castSucc_lt_succ i
      have hL : w⁻¹ i.castSucc < w⁻¹ i.succ := by
        rw [← e1, ← e2, Perm.inv_apply_self, Perm.inv_apply_self]; exact Fin.castSucc_lt_succ j
      have hR' : ¬ (adjT i * w) j.castSucc < (adjT i * w) j.succ := by
        rw [he, Perm.mul_apply, Perm.mul_apply]
        simp only [adjT, swap_apply_left, swap_apply_right, e1, e2, not_lt]
        exact (Fin.castSucc_lt_succ i).le
      have hL' : ¬ (w * adjT j)⁻¹ i.castSucc < (w * adjT j)⁻¹ i.succ := by
        rw [mul_inv_rev, adjT_inv, Perm.mul_apply, Perm.mul_apply, ← e1, ← e2,
          Perm.inv_apply_self, Perm.inv_apply_self]
        simp only [adjT, swap_apply_left, swap_apply_right, not_lt]
        exact (Fin.castSucc_lt_succ j).le
      simp only [hR, hL, hR', hL', if_true, if_false, Lop_single, Rop_single, hw, hw']
      simp only [he]
    · have hR : ¬ w j.castSucc < w j.succ := by rw [e1, e2, not_lt]; exact (Fin.castSucc_lt_succ i).le
      have hL : ¬ w⁻¹ i.castSucc < w⁻¹ i.succ := by
        rw [← e1, ← e2, Perm.inv_apply_self, Perm.inv_apply_self, not_lt]
        exact (Fin.castSucc_lt_succ j).le
      have hR' : (adjT i * w) j.castSucc < (adjT i * w) j.succ := by
        rw [he, Perm.mul_apply, Perm.mul_apply]
        simp only [adjT, swap_apply_left, swap_apply_right, e1, e2]
        exact Fin.castSucc_lt_succ i
      have hL' : (w * adjT j)⁻¹ i.castSucc < (w * adjT j)⁻¹ i.succ := by
        rw [mul_inv_rev, adjT_inv, Perm.mul_apply, Perm.mul_apply, ← e1, ← e2,
          Perm.inv_apply_self, Perm.inv_apply_self]
        simp only [adjT, swap_apply_left, swap_apply_right]
        exact Fin.castSucc_lt_succ j
      simp only [hR, hL, hR', hL', if_true, if_false, map_add, map_smul, Lop_single, Rop_single,
        hw, hw']
      simp only [he]
  · rw [not_or] at hs
    have hR := rightTest_adjT_mul i j w hs.1 hs.2
    have hL := leftTest_mul_adjT i j w hs.1 hs.2
    by_cases ha : w⁻¹ i.castSucc < w⁻¹ i.succ <;> by_cases hb : w j.castSucc < w j.succ <;>
      (simp only [ha, hb, hR, hL, if_true, if_false, map_add, map_smul, Lop_single, Rop_single,
        mul_assoc]; try module)

/-- The `T_w` span `H_{m+1}(q)`. -/
theorem span_stdElt_eq_top' (m : ℕ) :
    Submodule.span K (Set.range (stdElt (K := K) (q := q) (qi := qi) m)) = ⊤ := by
  have h : stdElt (K := K) (q := q) (qi := qi) m = cosetFam m ∘ (permOfEquiv m).symm := rfl
  rw [h, (permOfEquiv m).symm.surjective.range_comp]
  exact span_cosetFam_eq_top m

/-! ## Operators commuting with every `R_j` are determined on `e_1` -/

/-- `R` along a word, applied letter by letter from the left of the word. -/
noncomputable def Rword (m : ℕ) (u : List (Fin m)) : Module.End K (RegMod K m) :=
  ((u.map (Rop q qi m)).reverse).prod

theorem Rop_single_of_lt (m : ℕ) (j : Fin m) (w : Perm (Fin (m + 1)))
    (h : w j.castSucc < w j.succ) : Rop q qi m j (single w 1) = single (w * adjT j) 1 := by
  rw [Rop_single, if_pos h]

theorem Lop_single_of_lt (m : ℕ) (i : Fin m) (w : Perm (Fin (m + 1)))
    (h : w⁻¹ i.castSucc < w⁻¹ i.succ) : Lop q qi m i (single w 1) = single (adjT i * w) 1 := by
  rw [Lop_single, if_pos h]

/-- An inversion gained on the right is a right ascent. -/
theorem lt_of_ninv_mul_adjT {n : ℕ} (w : Perm (Fin (n + 1))) (j : Fin n)
    (h : ninv (w * adjT j) = ninv w + 1) : w j.castSucc < w j.succ := by
  by_contra hn
  have hne : w j.castSucc ≠ w j.succ := w.injective.ne (Fin.castSucc_lt_succ j).ne
  have hlt : w j.succ < w j.castSucc := lt_of_le_of_ne (not_lt.mp hn) hne.symm
  have h' : (w * adjT j) j.castSucc < (w * adjT j) j.succ := by
    simpa [adjT, Perm.mul_apply, swap_apply_left, swap_apply_right] using hlt
  have e := ninv_mul_adjT_of_lt (w * adjT j) j h'
  rw [mul_assoc, adjT_mul_self, mul_one] at e
  omega

/-- An inversion gained on the left is a left ascent. -/
theorem lt_of_ninv_adjT_mul {n : ℕ} (w : Perm (Fin (n + 1))) (i : Fin n)
    (h : ninv (adjT i * w) = ninv w + 1) : w⁻¹ i.castSucc < w⁻¹ i.succ := by
  apply lt_of_ninv_mul_adjT w⁻¹ i
  rw [← ninv_inv, mul_inv_rev, adjT_inv, inv_inv, ninv_inv, h]

theorem ninv_adjT_mul_le {n : ℕ} (w : Perm (Fin (n + 1))) (i : Fin n) :
    ninv (adjT i * w) ≤ ninv w + 1 := by
  rw [← ninv_inv, mul_inv_rev, adjT_inv, ← ninv_inv w]
  exact ninv_mul_adjT_le w⁻¹ i

theorem Rword_single_one (m : ℕ) (u : List (Fin m))
    (hu : u.length = ninv ((u.map adjT).prod)) :
    Rword q qi m u (single 1 1) = single ((u.map adjT).prod) 1 := by
  induction u using List.reverseRecOn with
  | nil => simp [Rword]
  | append_singleton u j ih =>
      simp only [List.map_append, List.map_singleton, List.prod_append, List.prod_singleton,
        List.length_append, List.length_singleton] at hu ⊢
      have hle := ninv_le_length u
      have hstep := ninv_mul_adjT_le ((u.map adjT).prod) j
      have hred : u.length = ninv ((u.map adjT).prod) := by omega
      simp only [Rword, List.map_append, List.map_singleton, List.reverse_append,
        List.reverse_singleton, List.singleton_append, List.prod_cons, Module.End.mul_apply]
      rw [show ((u.map (Rop q qi m)).reverse).prod = Rword q qi m u from rfl, ih hred,
        Rop_single_of_lt q qi m j _ (lt_of_ninv_mul_adjT _ j (by omega))]

theorem stdWord_reduced' (m : ℕ) (w : Perm (Fin (m + 1))) :
    (stdWord m w).length = ninv (((stdWord m w).map adjT).prod) := by
  rw [stdWord_prod_eq, stdWord_length]

/-- An operator commuting with every `R_j` is determined by its value on `e_1`. -/
theorem eq_of_comm_Rop (m : ℕ) {X Y : Module.End K (RegMod K m)}
    (hX : ∀ j, Commute X (Rop q qi m j)) (hY : ∀ j, Commute Y (Rop q qi m j))
    (h1 : X (single 1 1) = Y (single 1 1)) : X = Y := by
  have hc : ∀ (Z : Module.End K (RegMod K m)), (∀ j, Commute Z (Rop q qi m j)) →
      ∀ u, Commute Z (Rword q qi m u) := by
    intro Z hZ u
    refine Commute.list_prod_right _ _ fun a ha => ?_
    rw [List.mem_reverse, List.mem_map] at ha
    obtain ⟨j, _, rfl⟩ := ha
    exact hZ j
  refine regMod_ext fun w => ?_
  have hw := Rword_single_one q qi m (stdWord m w) (stdWord_reduced' m w)
  rw [stdWord_prod_eq] at hw
  rw [← hw, ← Module.End.mul_apply, (hc X hX _).eq, Module.End.mul_apply, h1,
    ← Module.End.mul_apply, ← (hc Y hY _).eq, Module.End.mul_apply]

/-! ## The Hecke relations for the left operators -/

theorem Lop_quadratic (m : ℕ) (i : Fin m) :
    Lop q qi m i * Lop q qi m i = (q - qi) • Lop q qi m i + (q * qi) • 1 := by
  refine regMod_ext fun w => ?_
  have ht : (adjT i * w)⁻¹ i.castSucc < (adjT i * w)⁻¹ i.succ ↔ w⁻¹ i.succ < w⁻¹ i.castSucc := by
    rw [mul_inv_rev, adjT_inv, Perm.mul_apply, Perm.mul_apply]
    simp only [adjT, swap_apply_left, swap_apply_right]
  have hw : adjT i * (adjT i * w) = w := by rw [← mul_assoc, adjT_mul_self, one_mul]
  have hne : w⁻¹ i.castSucc ≠ w⁻¹ i.succ := w⁻¹.injective.ne (Fin.castSucc_lt_succ i).ne
  simp only [Module.End.mul_apply, LinearMap.add_apply, LinearMap.smul_apply, Module.End.one_apply,
    Lop_single]
  by_cases ha : w⁻¹ i.castSucc < w⁻¹ i.succ
  · have hb : ¬ w⁻¹ i.succ < w⁻¹ i.castSucc := not_lt.mpr ha.le
    simp only [ha, hb, ht, hw, if_true, if_false, Lop_single]
  · have hb : w⁻¹ i.succ < w⁻¹ i.castSucc := lt_of_le_of_ne (not_lt.mp ha) hne.symm
    simp only [ha, hb, ht, hw, if_true, if_false, map_add, map_smul, Lop_single]

theorem Lop_commute_Rop (m : ℕ) (i j : Fin m) : Commute (Lop q qi m i) (Rop q qi m j) :=
  Lop_comm_Rop q qi m i j

/-- A concrete ascent test, decided by computing the swaps. -/
theorem adjT_braid_tests {n : ℕ} (a : Fin n) (hb : (a : ℕ) + 1 < n) :
    let b : Fin n := ⟨(a : ℕ) + 1, hb⟩
    (adjT a)⁻¹ b.castSucc < (adjT a)⁻¹ b.succ ∧
    (adjT b * adjT a)⁻¹ a.castSucc < (adjT b * adjT a)⁻¹ a.succ ∧
    (adjT b)⁻¹ a.castSucc < (adjT b)⁻¹ a.succ ∧
    (adjT a * adjT b)⁻¹ b.castSucc < (adjT a * adjT b)⁻¹ b.succ := by
  intro b
  simp only [b, mul_inv_rev, adjT_inv, Perm.mul_apply]
  simp only [adjT, swap_apply_def]
  refine ⟨?_, ?_, ?_, ?_⟩ <;> split_ifs <;>
    simp only [Fin.lt_iff_val_lt_val, Fin.ext_iff, Fin.coe_castSucc, Fin.val_succ] at * <;> first | omega | simp_all

theorem adjT_commute_test {n : ℕ} (i j : Fin n) (h : (j : ℕ) + 2 ≤ (i : ℕ)) :
    (adjT j)⁻¹ i.castSucc < (adjT j)⁻¹ i.succ ∧ (adjT i)⁻¹ j.castSucc < (adjT i)⁻¹ j.succ := by
  simp only [adjT_inv]
  simp only [adjT, swap_apply_def]
  refine ⟨?_, ?_⟩ <;> split_ifs <;>
    simp only [Fin.lt_iff_val_lt_val, Fin.ext_iff, Fin.coe_castSucc, Fin.val_succ] at * <;> omega

theorem Lop_one (m : ℕ) (i : Fin m) :
    Lop q qi m i (single 1 1) = single (adjT i) 1 := by
  rw [Lop_single_of_lt q qi m i 1 (by simp only [inv_one, Perm.one_apply]; exact Fin.castSucc_lt_succ i),
    mul_one]

theorem Lop_braid (m : ℕ) (i : Fin m) (hi : (i : ℕ) + 1 < m) :
    Lop q qi m i * Lop q qi m ⟨(i : ℕ) + 1, hi⟩ * Lop q qi m i
      = Lop q qi m ⟨(i : ℕ) + 1, hi⟩ * Lop q qi m i * Lop q qi m ⟨(i : ℕ) + 1, hi⟩ := by
  obtain ⟨t1, t2, t3, t4⟩ := adjT_braid_tests i hi
  refine eq_of_comm_Rop q qi m (fun j => ?_) (fun j => ?_) ?_
  · exact ((Lop_commute_Rop q qi m _ j).mul_left (Lop_commute_Rop q qi m _ j)).mul_left
      (Lop_commute_Rop q qi m _ j)
  · exact ((Lop_commute_Rop q qi m _ j).mul_left (Lop_commute_Rop q qi m _ j)).mul_left
      (Lop_commute_Rop q qi m _ j)
  · simp only [Module.End.mul_apply, Lop_one]
    rw [Lop_single_of_lt q qi m _ _ t1, Lop_single_of_lt q qi m _ _ t2,
      Lop_single_of_lt q qi m _ _ t3, Lop_single_of_lt q qi m _ _ t4, ← mul_assoc, ← mul_assoc,
      adjT_braid i hi]

theorem Lop_commute (m : ℕ) (i j : Fin m) (h : (j : ℕ) + 2 ≤ (i : ℕ)) :
    Lop q qi m i * Lop q qi m j = Lop q qi m j * Lop q qi m i := by
  obtain ⟨t1, t2⟩ := adjT_commute_test i j h
  refine eq_of_comm_Rop q qi m (fun k => ?_) (fun k => ?_) ?_
  · exact (Lop_commute_Rop q qi m _ k).mul_left (Lop_commute_Rop q qi m _ k)
  · exact (Lop_commute_Rop q qi m _ k).mul_left (Lop_commute_Rop q qi m _ k)
  · simp only [Module.End.mul_apply, Lop_one]
    rw [Lop_single_of_lt q qi m _ _ t1, Lop_single_of_lt q qi m _ _ t2, adjT_commute i j h]

/-! ## The regular representation and independence -/

/-- **The regular representation** `ρ : H_{m+1}(q) → End_K E`, `σ_i ↦ L_i`. -/
noncomputable def regRep (m : ℕ) : Hecke K q qi m →ₐ[K] Module.End K (RegMod K m) :=
  Hecke.lift K q qi m (Lop q qi m) (Lop_quadratic q qi m) (Lop_braid q qi m) (Lop_commute q qi m)

theorem Lword_single_one (m : ℕ) (u : List (Fin m))
    (hu : u.length = ninv ((u.map adjT).prod)) :
    (u.map (Lop q qi m)).prod (single 1 1) = single ((u.map adjT).prod) 1 := by
  induction u with
  | nil => simp
  | cons i u ih =>
      simp only [List.map_cons, List.prod_cons, List.length_cons, Module.End.mul_apply] at hu ⊢
      have hle := ninv_le_length u
      have hstep := ninv_adjT_mul_le ((u.map adjT).prod) i
      rw [ih (by omega), Lop_single_of_lt q qi m i _ (lt_of_ninv_adjT_mul _ i (by omega))]

/-- **`ρ(T_w) e_1 = e_w`.** -/
theorem regRep_stdElt_one (m : ℕ) (w : Perm (Fin (m + 1))) :
    regRep q qi m (stdElt m w) (single 1 1) = single w 1 := by
  rw [stdElt_eq_prod_word, map_list_prod, List.map_map]
  have h : (regRep q qi m) ∘ (σ K q qi m) = Lop q qi m := by
    funext i; simp [regRep]
  rw [h, Lword_single_one q qi m _ (stdWord_reduced' m w), stdWord_prod_eq]

/-- **The `T_w` are linearly independent**, over any commutative ring and any `q, qi`. -/
theorem stdElt_linearIndependent_any (m : ℕ) :
    LinearIndependent K (stdElt (K := K) (q := q) (qi := qi) m) := by
  let g : Hecke K q qi m →ₗ[K] RegMod K m :=
    LinearMap.applyₗ (single 1 1) ∘ₗ (regRep q qi m).toLinearMap
  refine LinearIndependent.of_comp g ?_
  have hg : g ∘ stdElt m = ⇑(Finsupp.basisSingleOne : Module.Basis _ K (RegMod K m)) := by
    funext w
    simp only [Function.comp_apply, g, LinearMap.coe_comp, LinearMap.applyₗ_apply_apply,
      AlgHom.toLinearMap_apply, regRep_stdElt_one, coe_basisSingleOne]
  rw [hg]
  exact Finsupp.basisSingleOne.linearIndependent

/-- **The standard basis** `{T_w : w ∈ S_{m+1}}` of `H_{m+1}(q)`, over any commutative ring. -/
noncomputable def stdBasisAny (m : ℕ) : Module.Basis (Perm (Fin (m + 1))) K (Hecke K q qi m) :=
  Module.Basis.mk (stdElt_linearIndependent_any q qi m) (span_stdElt_eq_top' q qi m).ge

theorem stdBasisAny_apply (m : ℕ) (w : Perm (Fin (m + 1))) :
    stdBasisAny q qi m w = stdElt m w :=
  Module.Basis.mk_apply _ _ _

/-- **`H_{m+1}(q)` is free of rank `(m+1)!`**, over any nontrivial commutative ring. -/
theorem finrank_hecke_eq_factorial_any [Nontrivial K] (m : ℕ) :
    Module.finrank K (Hecke K q qi m) = (m + 1).factorial := by
  rw [Module.finrank_eq_card_basis (stdBasisAny q qi m), Fintype.card_perm, Fintype.card_fin]

end HeckeCoset
end QOU.SchurWeyl
