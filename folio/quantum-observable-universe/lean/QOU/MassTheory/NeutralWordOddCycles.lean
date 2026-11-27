import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Data.Finset.Sort
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-!
# Neutral braid words close to odd cycles; on six strands reading 3 at `q = 1` forces purity

Bean `qou-cds1`. Audit: `docs/audits/2026-11-27-cds1-neutral-words-odd-cycles.md`.

The six-strand neutral-selection probe found that the γγ words passing reading 3 are exactly the
pure ones (the "multiple of 3" pattern is false in general: `(V₀V₂)⁵`, PR #9624). This file proves
the `q`-free part of that.

## Setting

A braid word on `n + 1` strands is a list of letters `σ_i^{±1}` (`Letter n = Fin n × Bool`),
stored newest letter first. `perm w` is the permutation of its closure (strand `x` ends at
position `perm w x`), and `cross x y w` is the signed number of crossings between strands `x` and
`y`. A word is `SelfNeutral` when every closure component has signed self-crossing count `0`;
the probe's linking neutrality implies it.

## What is proved

1. `even_cross_iff` — two distinct strands cross an even number of times iff they end in their
   starting order (any word, any number of strands).
2. `neg_one_pow_invOn_cycleOf` — inside one cycle `C` of a permutation the inversion count has the
   parity of `#C − 1` (via `sign_eq_signAux` and the order isomorphism `Fin #C ≃o C`).
3. `odd_of_mem_cycleType` — **a self-neutral word closes to a permutation with only odd cycles.**
4. `eq_replicate_of_odd_reading3` — odd cycle lengths summing to 6 satisfy classical reading 3
   (`a₀ ≤ a₁ ≤ a₂ ≤ a₃`, with `χ_{(6−k,k)} = a_k − a_{k−1}`) only for `1⁶`.
5. `perm_eq_one_of_selfNeutral_reading3` — on six strands, self-neutral + classical reading 3
   ⇒ pure braid.

The character-to-`a_k` bridge (Young's rule) is cited, not formalised, exactly as in
`QOU.MassTheory.ClassicalReading3MergeBound`. Statements are at `q = 1`; no `q₀` and no measured
value appears. Passing from `q = 1` to an interval around it is continuity of a Laurent
polynomial, argued in the audit.
-/

open Equiv Equiv.Perm Finset

namespace QOU.MassTheory.NeutralWordOddCycles

theorem sign_eq_signAux {n : ℕ} (σ : Perm (Fin n)) : sign σ = signAux σ := by
  induction σ using swap_induction_on with
  | one => simp [signAux_one]
  | swap_mul f x y hxy ih => rw [map_mul, signAux_mul, ih, sign_swap hxy, signAux_swap hxy]

/-- Inversions of `σ` on `Fin n`, as ordered pairs `x < y` with `σ y < σ x`. -/
def inv {n : ℕ} (σ : Perm (Fin n)) : Finset (Fin n × Fin n) :=
  univ.filter fun p => p.1 < p.2 ∧ σ p.2 < σ p.1

theorem signAux_eq_pow {n : ℕ} (σ : Perm (Fin n)) : signAux σ = (-1) ^ #(inv σ) := by
  unfold signAux
  rw [Finset.prod_ite, prod_const, prod_const_one, mul_one]
  congr 1
  refine Finset.card_bij (fun a _ => (a.2, a.1)) ?_ ?_ ?_
  · intro a ha
    simp only [mem_filter, mem_finPairsLT] at ha
    simp only [inv, mem_filter, mem_univ, true_and]
    refine ⟨ha.1, lt_of_le_of_ne ha.2 ?_⟩
    intro h; exact (ne_of_gt ha.1) (σ.injective h)
  · rintro ⟨a1, a2⟩ ha ⟨b1, b2⟩ hb h
    simp only [Prod.mk.injEq] at h
    obtain ⟨h1, h2⟩ := h
    subst h1; subst h2; rfl
  · rintro ⟨x, y⟩ h
    simp only [inv, mem_filter, mem_univ, true_and] at h
    exact ⟨⟨y, x⟩, by simp [mem_finPairsLT, h.1, h.2.le], rfl⟩


/-- Inversions of `σ` inside a finset `C`. -/
def invOn {n : ℕ} (σ : Perm (Fin n)) (C : Finset (Fin n)) : Finset (Fin n × Fin n) :=
  (C ×ˢ C).filter fun p => p.1 < p.2 ∧ σ p.2 < σ p.1

/-- **Inversion parity of a cycle.** Inside the support `C` of the cycle of `σ` through `x₀`,
`σ` has `(−1)^{#inv} = −(−1)^{#C}`: the inversion count has the parity of `#C − 1`. -/
theorem neg_one_pow_invOn_cycleOf {n : ℕ} (σ : Perm (Fin n)) (x₀ : Fin n) :
    ((-1 : ℤˣ) ^ #(invOn σ (σ.cycleOf x₀).support)) = -(-1) ^ #(σ.cycleOf x₀).support ∨
      (σ.cycleOf x₀).support = ∅ := by
  by_cases hx : σ x₀ = x₀
  · right; simp [cycleOf_eq_one_iff σ |>.2 hx]
  left
  set c := σ.cycleOf x₀ with hcdef
  set C := c.support with hCdef
  have hc : IsCycle c := isCycle_cycleOf σ hx
  have hcσ : ∀ y ∈ C, c y = σ y := by
    intro y hy
    rw [hCdef, hcdef, mem_support_cycleOf_iff' hx] at hy
    rw [hcdef, cycleOf_apply, if_pos hy]
  have h₁ : ∀ x, c x ∈ C ↔ x ∈ C := fun x => apply_mem_support
  set c' := c.subtypePerm h₁
  have hs1 : sign c' = sign c := by
    convert sign_subtypePerm c h₁ (fun x hx => mem_support.2 hx)
  let e : Fin #C ≃o C := C.orderIsoOfFin rfl
  set τ : Perm (Fin #C) := e.toEquiv.symm.permCongr c'
  have hs2 : sign τ = sign c' := sign_permCongr _ _
  have hτ : ∀ j, (e (τ j) : Fin n) = σ (e j) := by
    intro j
    simp only [τ, permCongr_apply, Equiv.symm_symm, RelIso.coe_fn_toEquiv]
    show ((e.toEquiv) ((e.toEquiv).symm (c' (e.toEquiv j))) : Fin n) = σ (e.toEquiv j)
    rw [Equiv.apply_symm_apply]
    simp only [c', subtypePerm_apply]
    exact hcσ _ (e j).2
  have hcard : #(inv τ) = #(invOn σ C) := by
    refine Finset.card_bij (fun a _ => ((e a.1 : Fin n), (e a.2 : Fin n))) ?_ ?_ ?_
    · rintro ⟨a, b⟩ h
      simp only [inv, mem_filter, mem_univ, true_and] at h
      simp only [invOn, mem_filter, mem_product]
      refine ⟨⟨(e a).2, (e b).2⟩, ?_, ?_⟩
      · exact e.strictMono h.1
      · rw [← hτ, ← hτ]; exact e.strictMono h.2
    · rintro ⟨a1, a2⟩ _ ⟨b1, b2⟩ _ h
      simp only [Prod.mk.injEq] at h
      obtain ⟨h1, h2⟩ := h
      rw [Subtype.coe_inj, e.injective.eq_iff] at h1 h2
      rw [h1, h2]
    · rintro ⟨x, y⟩ h
      simp only [invOn, mem_filter, mem_product] at h
      obtain ⟨⟨hxC, hyC⟩, hxy, hσ⟩ := h
      refine ⟨(e.symm ⟨x, hxC⟩, e.symm ⟨y, hyC⟩), ?_, by simp⟩
      simp only [inv, mem_filter, mem_univ, true_and]
      refine ⟨e.symm.strictMono (show (⟨x, hxC⟩ : C) < ⟨y, hyC⟩ from hxy), ?_⟩
      apply e.lt_iff_lt.1
      show (e (τ _) : Fin n) < e (τ _)
      rw [hτ, hτ, OrderIso.apply_symm_apply, OrderIso.apply_symm_apply]
      exact hσ
  rw [← hcard, ← signAux_eq_pow, ← sign_eq_signAux, hs2, hs1, hc.sign]


/-! ## Braid words on `n + 1` strands -/

/-- A letter `σ_i^{±1}`: the crossing of positions `i` and `i+1`, with a sign. -/
abbrev Letter (n : ℕ) := Fin n × Bool

/-- `pos w p` = the strand at position `p` after reading `w`. Words are stored newest letter
first, so `w = ℓ :: w'` means "`w'`, then `ℓ`". -/
def strandAt {n : ℕ} : List (Letter n) → Perm (Fin (n + 1))
  | [] => 1
  | ℓ :: w => strandAt w * swap ℓ.1.castSucc ℓ.1.succ

/-- The permutation of the closure: strand `x` ends at position `perm w x`, which is where the
closure re-enters the top as strand `perm w x`. -/
def perm {n : ℕ} (w : List (Letter n)) : Perm (Fin (n + 1)) := (strandAt w)⁻¹

/-- Letter `ℓ`, read after `w`, is a crossing between strands `x` and `y`. -/
def Crosses {n : ℕ} (w : List (Letter n)) (ℓ : Letter n) (x y : Fin (n + 1)) : Prop :=
  (strandAt w ℓ.1.castSucc = x ∧ strandAt w ℓ.1.succ = y) ∨
    (strandAt w ℓ.1.castSucc = y ∧ strandAt w ℓ.1.succ = x)

instance {n : ℕ} (w : List (Letter n)) (ℓ : Letter n) (x y : Fin (n + 1)) :
    Decidable (Crosses w ℓ x y) := by unfold Crosses; infer_instance

/-- Signed number of crossings between strands `x` and `y`. -/
def cross {n : ℕ} (x y : Fin (n + 1)) : List (Letter n) → ℤ
  | [] => 0
  | ℓ :: w => cross x y w + if Crosses w ℓ x y then (if ℓ.2 then 1 else -1) else 0

/-- An adjacent swap keeps the relative order of two positions unless it swaps exactly them. -/
theorem swap_lt_iff {n : ℕ} (i : Fin n) (a b : Fin (n + 1)) (hab : a ≠ b) :
    (swap i.castSucc i.succ a < swap i.castSucc i.succ b ↔ a < b) ↔
      ¬((a = i.castSucc ∧ b = i.succ) ∨ (a = i.succ ∧ b = i.castSucc)) := by
  have hab' : a.val ≠ b.val := fun h => hab (Fin.ext h)
  have hs : ∀ z : Fin (n + 1), (swap i.castSucc i.succ z).val =
      if z.val = i.val then i.val + 1 else if z.val = i.val + 1 then i.val else z.val := by
    intro z
    rw [swap_apply_def]
    by_cases h1 : z = i.castSucc
    · have : z.val = i.val := by rw [h1]; rfl
      rw [if_pos h1, if_pos this]; rfl
    · have h1' : z.val ≠ i.val := fun h => h1 (Fin.ext h)
      rw [if_neg h1, if_neg h1']
      by_cases h2 : z = i.succ
      · have : z.val = i.val + 1 := by rw [h2]; rfl
        rw [if_pos h2, if_pos this]; rfl
      · have h2' : z.val ≠ i.val + 1 := fun h => h2 (Fin.ext h)
        rw [if_neg h2, if_neg h2']
  rw [Fin.lt_iff_val_lt_val, Fin.lt_iff_val_lt_val, hs, hs]
  simp only [Fin.ext_iff, Fin.coe_castSucc, Fin.val_succ]
  split_ifs <;> omega

/-- **Crossing parity.** Two distinct strands cross an even number of times (signed count) iff
they end in the same relative order as they started. -/
theorem even_cross_iff {n : ℕ} (x y : Fin (n + 1)) (hxy : x ≠ y) (w : List (Letter n)) :
    Even (cross x y w) ↔ (perm w x < perm w y ↔ x < y) := by
  induction w with
  | nil => simp [cross, perm, strandAt]
  | cons ℓ w ih =>
    have hp : ∀ z, perm (ℓ :: w) z = swap ℓ.1.castSucc ℓ.1.succ (perm w z) := by
      intro z; simp [perm, strandAt, mul_inv_rev, swap_inv]
    have hne : perm w x ≠ perm w y := fun h => hxy ((perm w).injective h)
    have key := swap_lt_iff ℓ.1 _ _ hne
    have hC : Crosses w ℓ x y ↔
        ((perm w x = ℓ.1.castSucc ∧ perm w y = ℓ.1.succ) ∨
          (perm w x = ℓ.1.succ ∧ perm w y = ℓ.1.castSucc)) := by
      unfold Crosses perm
      constructor
      · rintro (⟨h1, h2⟩ | ⟨h1, h2⟩)
        · left; rw [← h1, ← h2]; simp
        · right; rw [← h1, ← h2]; simp
      · rintro (⟨h1, h2⟩ | ⟨h1, h2⟩)
        · left; rw [← h1, ← h2]; simp
        · right; rw [← h1, ← h2]; simp
    rw [hp, hp]
    simp only [cross]
    by_cases hc : Crosses w ℓ x y
    · rw [if_pos hc]
      have hk : ¬(swap ℓ.1.castSucc ℓ.1.succ (perm w x) < swap ℓ.1.castSucc ℓ.1.succ (perm w y)
          ↔ perm w x < perm w y) := by rw [key]; exact not_not.2 (hC.1 hc)
      have hodd : Even (cross x y w + if ℓ.2 then 1 else -1) ↔ ¬ Even (cross x y w) := by
        split_ifs
        · exact Int.even_add_one
        · rw [← sub_eq_add_neg, Int.even_sub_one]
      rw [hodd, ih]
      generalize (perm w x < perm w y) = P at *
      generalize (x < y) = X at *
      generalize (swap ℓ.1.castSucc ℓ.1.succ (perm w x) < swap ℓ.1.castSucc ℓ.1.succ (perm w y)) = S at *
      by_cases hP : P <;> by_cases hS : S <;> simp_all
    · rw [if_neg hc, add_zero, ih]
      have hk := key.2 (fun h => hc (hC.2 h))
      rw [hk]


/-- Strands of the closure component through `x₀` (empty if `x₀` is a fixed strand). -/
def comp {n : ℕ} (w : List (Letter n)) (x₀ : Fin (n + 1)) : Finset (Fin (n + 1)) :=
  ((perm w).cycleOf x₀).support

/-- Signed self-crossing count of the component through `x₀`. -/
def selfCross {n : ℕ} (w : List (Letter n)) (x₀ : Fin (n + 1)) : ℤ :=
  ∑ p ∈ (comp w x₀ ×ˢ comp w x₀).filter (fun p => p.1 < p.2), cross p.1 p.2 w

/-- Every closure component has signed self-crossing count `0`. -/
def SelfNeutral {n : ℕ} (w : List (Letter n)) : Prop := ∀ x₀, selfCross w x₀ = 0

/-- The self-crossing count of a component has the parity of its inversion count. -/
theorem selfCross_zmod {n : ℕ} (w : List (Letter n)) (x₀ : Fin (n + 1)) :
    ((selfCross w x₀ : ℤ) : ZMod 2) = (#(invOn (perm w) (comp w x₀)) : ZMod 2) := by
  unfold selfCross invOn
  push_cast
  rw [Finset.card_filter, Nat.cast_sum, Finset.sum_filter]
  refine Finset.sum_congr rfl fun p _ => ?_
  by_cases hlt : p.1 < p.2
  · rw [if_pos hlt]
    have hne : p.1 ≠ p.2 := ne_of_lt hlt
    have hpe := even_cross_iff p.1 p.2 hne w
    have hσne : perm w p.1 ≠ perm w p.2 := fun h => hne ((perm w).injective h)
    by_cases hinv : perm w p.2 < perm w p.1
    · rw [if_pos (⟨hlt, hinv⟩ : p.1 < p.2 ∧ perm w p.2 < perm w p.1)]
      have : ¬ Even (cross p.1 p.2 w) := by
        rw [hpe]; intro h; exact absurd (h.2 hlt) (not_lt.2 hinv.le)
      rw [Int.not_even_iff_odd] at this
      push_cast
      exact (ZMod.intCast_eq_one_iff_odd).2 this
    · rw [if_neg (fun h : p.1 < p.2 ∧ perm w p.2 < perm w p.1 => hinv h.2)]
      have : Even (cross p.1 p.2 w) := by
        rw [hpe]
        exact ⟨fun _ => hlt, fun _ => lt_of_le_of_ne (not_lt.1 hinv) hσne⟩
      push_cast
      exact (ZMod.intCast_eq_zero_iff_even).2 this
  · rw [if_neg hlt, if_neg (fun h : p.1 < p.2 ∧ perm w p.2 < perm w p.1 => hlt h.1)]; simp

/-- **Theorem A.** A self-neutral braid word closes to a permutation all of whose cycles have
odd length. -/
theorem odd_of_mem_cycleType {n : ℕ} (w : List (Letter n)) (hw : SelfNeutral w)
    {k : ℕ} (hk : k ∈ (perm w).cycleType) : Odd k := by
  rw [cycleType_def, Multiset.mem_map] at hk
  obtain ⟨c, hc, rfl⟩ := hk
  have hcyc : c.IsCycle := (mem_cycleFactorsFinset_iff.1 hc).1
  obtain ⟨a, ha⟩ := hcyc.nonempty_support
  have hca : c = (perm w).cycleOf a := cycle_is_cycleOf ha hc
  have haσ : a ∈ (perm w).support := mem_cycleFactorsFinset_support_le hc ha
  have heven : Even #(invOn (perm w) (comp w a)) := by
    rw [← ZMod.natCast_eq_zero_iff_even, ← selfCross_zmod, hw a]; simp
  simp only [comp] at heven
  rcases neg_one_pow_invOn_cycleOf (perm w) a with h | h
  · rw [heven.neg_one_pow] at h
    have h' : ((-1 : ℤˣ) ^ #((perm w).cycleOf a).support : ℤ) = -1 := by
      have := congrArg (fun u : ℤˣ => (u : ℤ)) h
      simp only [Units.val_one, Units.val_neg, Units.val_pow_eq_pow_val] at this
      push_cast; linarith
    push_cast at h'
    rw [Function.comp_apply, hca]
    exact (neg_one_pow_eq_neg_one_iff_odd (by norm_num)).1 h'
  · exact absurd h (Finset.nonempty_iff_ne_empty.1 ⟨a, by
      rw [mem_support_cycleOf_iff]; exact ⟨SameCycle.refl _ _, haσ⟩⟩)


/-! ## Classical reading 3 on six strands -/

/-- `a_k`: the number of sub-multisets of the cycle lengths summing to `k` (index subsets, so
repeated lengths count separately) = the number of invariant `k`-subsets of a permutation with
these cycle lengths. Same quantity as `ClassicalReading3MergeBound.subsetSums`. -/
def ak (m : Multiset ℕ) (k : ℕ) : ℕ := (m.powerset.filter fun s => s.sum = k).card

/-- Classical (`q = 1`) reading 3 on the two-row blocks of `S₆`: `χ_{(6−k,k)} = a_k − a_{k−1} ≥ 0`
for `k = 1, 2, 3` (Young's rule; the character-to-`a_k` bridge is cited, as in
`ClassicalReading3MergeBound`). -/
def Reading3Six (m : Multiset ℕ) : Prop := ak m 0 ≤ ak m 1 ∧ ak m 1 ≤ ak m 2 ∧ ak m 2 ≤ ak m 3

/-- **Theorem B.** Odd cycle lengths summing to `6` pass classical reading 3 only when every
length is `1`. -/
theorem eq_replicate_of_odd_reading3 (m : Multiset ℕ) (hodd : ∀ x ∈ m, Odd x) (hsum : m.sum = 6)
    (hr : Reading3Six m) : m = Multiset.replicate 6 1 := by
  have h135 : ∀ x ∈ m, x = 1 ∨ x = 3 ∨ x = 5 := by
    intro x hx
    have hle : x ≤ 6 := hsum ▸ Multiset.le_sum_of_mem hx
    obtain ⟨j, rfl⟩ := hodd x hx
    omega
  have hm : m = Multiset.replicate (m.count 1) 1 + Multiset.replicate (m.count 3) 3 +
      Multiset.replicate (m.count 5) 5 := by
    ext x
    simp only [Multiset.count_add, Multiset.count_replicate]
    by_cases hx : x ∈ m
    · rcases h135 x hx with rfl | rfl | rfl <;> simp
    · rw [Multiset.count_eq_zero.2 hx]
      split_ifs <;> subst_vars <;> simp_all
  have hs : m.count 1 + 3 * m.count 3 + 5 * m.count 5 = 6 := by
    rw [hm] at hsum; simpa [Multiset.sum_replicate, mul_comm] using hsum
  generalize m.count 1 = a at hm hs
  generalize m.count 3 = b at hm hs
  generalize m.count 5 = c at hm hs
  subst hm
  have h4 : (a = 6 ∧ b = 0 ∧ c = 0) ∨ (a = 3 ∧ b = 1 ∧ c = 0) ∨ (a = 0 ∧ b = 2 ∧ c = 0) ∨
      (a = 1 ∧ b = 0 ∧ c = 1) := by
    have hc : c ≤ 1 := by omega
    have hb : b ≤ 2 := by omega
    interval_cases c <;> interval_cases b <;> omega
  rcases h4 with ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl⟩
  · rfl
  all_goals (revert hr; unfold Reading3Six ak; decide)


/-- **Corollary (six strands).** A self-neutral word on six strands whose closure passes
classical reading 3 is a pure braid. -/
theorem perm_eq_one_of_selfNeutral_reading3 (w : List (Letter 5)) (hw : SelfNeutral w)
    (hr : Reading3Six (perm w).partition.parts) : perm w = 1 := by
  have hodd : ∀ x ∈ (perm w).partition.parts, Odd x := by
    intro x hx
    rw [parts_partition, Multiset.mem_add] at hx
    rcases hx with hx | hx
    · exact odd_of_mem_cycleType w hw hx
    · rw [Multiset.eq_of_mem_replicate hx]; exact odd_one
  have hsum : (perm w).partition.parts.sum = 6 := by
    rw [(perm w).partition.parts_sum]; simp
  have h6 := eq_replicate_of_odd_reading3 _ hodd hsum hr
  rw [← cycleType_eq_zero, Multiset.eq_zero_iff_forall_notMem]
  intro k hk
  have hk' : k ∈ (perm w).partition.parts := by
    rw [parts_partition]; exact Multiset.mem_add.2 (Or.inl hk)
  rw [h6] at hk'
  have := two_le_of_mem_cycleType hk
  rw [Multiset.eq_of_mem_replicate hk'] at this
  omega

end QOU.MassTheory.NeutralWordOddCycles
