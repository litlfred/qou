import QOU.Hecke.SymmetricCoxeter
import QOU.Hecke.PermLength
import QOU.Machinery.CoxeterBruhat

/-!
# The rank matrix of a permutation, and the easy half of Ehresmann's criterion

For `u` a permutation of `Fin n`, its **rank matrix** is

    rk u i m = #{x : x < i and u x < m},

the number of the first `i` positions carrying a value below `m`.  Ehresmann's tableau
criterion (Björner–Brenti, *Combinatorics of Coxeter Groups*, Thm 2.1.5) says that the
Bruhat order on `S_n` is exactly the pointwise comparison of rank matrices:

    u ≤ w   ⟺   rk w i m ≤ rk u i m   for every i and m.

This file proves the **easy** implication, left to right — a subword of a reduced word has
a pointwise-larger rank matrix — directly from `CoxeterBruhat.BruhatLe`'s subword
definition.  The converse (rank criterion ⟹ subword) is not here; it is the one
Mathlib-scale piece of the route below.

## Why this file exists

Mathas' Proposition 3.7 (Dipper–James) says dominance on row-standard `λ`-tableaux is the
Bruhat order on their `d`-images.  `BraidKnot.DominanceIsBruhat.domRel_iff_rankAt` proves
that the **dominance** side of that is itself a rank comparison, read only at the reference
tableau's row cuts.  So 3.7 has no tableau content: both sides compare the rank matrices of
the same two permutations, and the whole difference is *at the row cuts* versus *at every
index*.

The **converse** half of 3.7 — `d(s) ≤ d(t) → s ⊵ t` — is then
`rk_le_of_bruhatLe` here, followed by specialising the inequality to the row cuts and
applying `domRel_iff_rankAt`.  **No reflection order appears in that chain**, so it does not
wait on `BruhatLe → ReflLe` (bean `qou-3k66`), which the corpus previously recorded as its
blocker.

## The two rank steps, and why they are the whole argument

Right multiplication by a simple transposition permutes **positions**, so it can only move
the rank matrix at the single cut between the two positions it swaps
(`rk_mul_swap_of_ne`), where it exchanges the two values (`rk_mul_swap_cut`).  The induction
on a reduced word from the right then needs exactly two facts, and both were measured over
every permutation of `S_3`…`S_5` before being proved:

* **A** (`rk_mul_swap_le`) — if `w` ascends across the cut then `w · s_j` has a
  pointwise-smaller rank matrix.
* **B** (`rk_mul_swap_mono`) — a rank domination survives right multiplication by `s_j`,
  provided the **dominated** permutation ascends across the cut.  Nothing is assumed of the
  other one, which is the part a hand argument gets wrong: the naive case analysis stalls in
  one sub-case and is rescued by the hypothesis at the cut `j + 2`, not at `j` or `j + 1`.

`QOU.Hecke.Inversions.length_mul_swap_eq_succ_iff` supplies the ascent from the Coxeter
length, so the two steps are restated as `rk_mul_simple_le` / `rk_mul_simple_mono` in the
form the induction consumes.

-- Ref: [bjornerbrenti2005] Björner & Brenti, *Combinatorics of Coxeter Groups*, Thm 2.1.5
-- Ref: [mathas1999] Mathas, *Iwahori–Hecke Algebras and Schur Algebras of the Symmetric
--      Group*, Proposition 3.7
-- Ref: [manuscript] beans qou-f3mc, qou-phir;
--      `computations/hecke/dipper_james_rank_criterion_probe.py`
-/

open Equiv Finset

namespace QOU.Machinery.BruhatRank

variable {n : ℕ}

def rk (u : Perm (Fin n)) (i m : ℕ) : ℕ :=
  ∑ x : Fin n, if (x : ℕ) < i ∧ ((u x : Fin n) : ℕ) < m then 1 else 0

theorem rk_succ (u : Perm (Fin n)) (i m : ℕ) (hi : i < n) :
    rk u (i + 1) m = rk u i m + (if ((u ⟨i, hi⟩ : Fin n) : ℕ) < m then 1 else 0) := by
  unfold rk
  have hsplit : ∀ x : Fin n,
      (if (x : ℕ) < i + 1 ∧ ((u x : Fin n) : ℕ) < m then 1 else 0)
        = (if (x : ℕ) < i ∧ ((u x : Fin n) : ℕ) < m then 1 else 0)
          + (if (x : ℕ) = i ∧ ((u x : Fin n) : ℕ) < m then 1 else 0) := by
    intro x
    by_cases hP : ((u x : Fin n) : ℕ) < m
    · simp only [hP, and_true]
      split_ifs <;> omega
    · simp [hP]
  rw [Finset.sum_congr rfl fun x _ => hsplit x, Finset.sum_add_distrib]
  congr 1
  rw [Finset.sum_eq_single (⟨i, hi⟩ : Fin n)]
  · simp
  · intro b _ hb
    have : (b : ℕ) ≠ i := fun h => hb (Fin.ext h)
    simp [this]
  · intro h; exact absurd (Finset.mem_univ _) h

theorem rk_zero (u : Perm (Fin n)) (m : ℕ) : rk u 0 m = 0 := by
  unfold rk; simp

/-- Right multiplication permutes POSITIONS: the swap moves into the position condition
and leaves the value condition alone. -/
theorem rk_mul_swap_eq (u : Perm (Fin (n + 1))) (j : Fin n) (i m : ℕ) :
    rk (u * Equiv.swap j.castSucc j.succ) i m
      = ∑ y : Fin (n + 1),
          if ((Equiv.swap j.castSucc j.succ y : Fin (n + 1)) : ℕ) < i
            ∧ ((u y : Fin (n + 1)) : ℕ) < m then 1 else 0 := by
  unfold rk
  refine (Equiv.sum_comp (Equiv.swap j.castSucc j.succ) _).symm.trans ?_
  refine Finset.sum_congr rfl fun y _ => ?_
  simp [Equiv.Perm.mul_apply, Equiv.swap_apply_self]

theorem rk_mul_swap_of_ne (u : Perm (Fin (n + 1))) (j : Fin n) (i m : ℕ)
    (hi : i ≤ (j : ℕ) ∨ (j : ℕ) + 2 ≤ i) :
    rk (u * Equiv.swap j.castSucc j.succ) i m = rk u i m := by
  rw [rk_mul_swap_eq]
  unfold rk
  refine Finset.sum_congr rfl fun y _ => ?_
  by_cases hya : y = j.castSucc
  · subst hya
    have e : ((j : ℕ) + 1 < i) = ((j : ℕ) < i) := by
      rcases hi with h | h
      · simp [Nat.not_lt.mpr (by omega : i ≤ (j:ℕ)), Nat.not_lt.mpr (by omega : i ≤ (j:ℕ)+1)]
      · simp [(by omega : (j:ℕ) < i), (by omega : (j:ℕ) + 1 < i)]
    simp only [Equiv.swap_apply_left, Fin.coe_castSucc, Fin.val_succ, e]
  · by_cases hyb : y = j.succ
    · subst hyb
      have e : ((j : ℕ) < i) = ((j : ℕ) + 1 < i) := by
        rcases hi with h | h
        · simp [Nat.not_lt.mpr (by omega : i ≤ (j:ℕ)), Nat.not_lt.mpr (by omega : i ≤ (j:ℕ)+1)]
        · simp [(by omega : (j:ℕ) < i), (by omega : (j:ℕ) + 1 < i)]
      simp only [Equiv.swap_apply_right, Fin.coe_castSucc, Fin.val_succ, e]
    · simp [Equiv.swap_apply_of_ne_of_ne hya hyb]

/-- **At the cut `i = j + 1`**, right multiplication by `s_j` replaces the value at
position `j` by the value at position `j + 1`. -/
theorem rk_mul_swap_cut (u : Perm (Fin (n + 1))) (j : Fin n) (m : ℕ) :
    rk (u * Equiv.swap j.castSucc j.succ) ((j : ℕ) + 1) m
      = rk u (j : ℕ) m + (if ((u j.succ : Fin (n + 1)) : ℕ) < m then 1 else 0) := by
  rw [rk_mul_swap_eq]
  have hsplit : ∀ y : Fin (n + 1),
      (if ((Equiv.swap j.castSucc j.succ y : Fin (n + 1)) : ℕ) < (j : ℕ) + 1
          ∧ ((u y : Fin (n + 1)) : ℕ) < m then 1 else 0)
        = (if (y : ℕ) < (j : ℕ) ∧ ((u y : Fin (n + 1)) : ℕ) < m then 1 else 0)
          + (if y = j.succ ∧ ((u y : Fin (n + 1)) : ℕ) < m then 1 else 0) := by
    intro y
    by_cases hP : ((u y : Fin (n + 1)) : ℕ) < m
    · simp only [hP, and_true]
      by_cases hya : y = j.castSucc
      · subst hya
        have hne : (j.castSucc : Fin (n + 1)) ≠ j.succ := Fin.castSucc_lt_succ j |>.ne
        simp [Equiv.swap_apply_left, Fin.val_succ, hne]
      · by_cases hyb : y = j.succ
        · subst hyb
          simp [Equiv.swap_apply_right, Fin.coe_castSucc]
        · have hyv : (y : ℕ) ≠ (j.succ : Fin (n + 1)) := by
            intro h; exact hyb (Fin.ext h)
          simp only [Equiv.swap_apply_of_ne_of_ne hya hyb, hyb, if_false, add_zero]
          have hyc : (y : ℕ) ≠ (j : ℕ) := by
            intro h; exact hya (Fin.ext (by simpa [Fin.coe_castSucc] using h))
          by_cases hlt : (y : ℕ) < (j : ℕ) + 1
          · have : (y : ℕ) < (j : ℕ) := by omega
            simp [hlt, this]
          · have : ¬ ((y : ℕ) < (j : ℕ)) := by omega
            simp [hlt, this]
    · simp [hP]
  rw [Finset.sum_congr rfl fun y _ => hsplit y, Finset.sum_add_distrib]
  congr 1
  rw [Finset.sum_eq_single (j.succ : Fin (n + 1))]
  · simp
  · intro b _ hb; simp [hb]
  · intro h; exact absurd (Finset.mem_univ _) h

/-! ### The two rank steps of the subword induction -/

theorem rk_castSucc_succ (u : Perm (Fin (n + 1))) (j : Fin n) (m : ℕ) :
    rk u ((j : ℕ) + 1) m
      = rk u (j : ℕ) m + (if ((u j.castSucc : Fin (n + 1)) : ℕ) < m then 1 else 0) := by
  have hj : (j : ℕ) < n + 1 := Nat.lt_succ_of_lt j.isLt
  have h := rk_succ u (j : ℕ) m hj
  have e : (⟨(j : ℕ), hj⟩ : Fin (n + 1)) = j.castSucc := rfl
  rwa [e] at h

theorem rk_succ_succ (u : Perm (Fin (n + 1))) (j : Fin n) (m : ℕ) :
    rk u ((j : ℕ) + 2) m
      = rk u ((j : ℕ) + 1) m + (if ((u j.succ : Fin (n + 1)) : ℕ) < m then 1 else 0) := by
  have hj : (j : ℕ) + 1 < n + 1 := Nat.succ_lt_succ j.isLt
  have h := rk_succ u ((j : ℕ) + 1) m hj
  have e : (⟨(j : ℕ) + 1, hj⟩ : Fin (n + 1)) = j.succ := rfl
  rwa [e] at h

/-- **Step A.**  If `w` ascends across the cut then right-multiplying by `s_j` can only
lower the rank matrix. -/
theorem rk_mul_swap_le (w : Perm (Fin (n + 1))) (j : Fin n)
    (hasc : ((w j.castSucc : Fin (n + 1)) : ℕ) < ((w j.succ : Fin (n + 1)) : ℕ))
    (i m : ℕ) :
    rk (w * Equiv.swap j.castSucc j.succ) i m ≤ rk w i m := by
  by_cases hi : i = (j : ℕ) + 1
  · subst hi
    rw [rk_mul_swap_cut, rk_castSucc_succ]
    have : (if ((w j.succ : Fin (n + 1)) : ℕ) < m then 1 else 0)
        ≤ (if ((w j.castSucc : Fin (n + 1)) : ℕ) < m then 1 else 0) := by
      split_ifs <;> omega
    omega
  · rw [rk_mul_swap_of_ne w j i m (by omega)]

/-- **Step B.**  A rank domination survives right multiplication by `s_j`, provided the
DOMINATED permutation ascends across the cut.  Nothing is assumed of the other one. -/
theorem rk_mul_swap_mono (u w : Perm (Fin (n + 1))) (j : Fin n)
    (hasc : ((w j.castSucc : Fin (n + 1)) : ℕ) < ((w j.succ : Fin (n + 1)) : ℕ))
    (h : ∀ i m, rk w i m ≤ rk u i m) (i m : ℕ) :
    rk (w * Equiv.swap j.castSucc j.succ) i m
      ≤ rk (u * Equiv.swap j.castSucc j.succ) i m := by
  by_cases hi : i = (j : ℕ) + 1
  · subst hi
    rw [rk_mul_swap_cut, rk_mul_swap_cut]
    have hj := h (j : ℕ) m
    have hj1 := h ((j : ℕ) + 1) m
    have hj2 := h ((j : ℕ) + 2) m
    rw [rk_castSucc_succ, rk_castSucc_succ] at hj1
    rw [rk_succ_succ, rk_succ_succ, rk_castSucc_succ, rk_castSucc_succ] at hj2
    have hb : (if ((w j.succ : Fin (n + 1)) : ℕ) < m then 1 else 0)
        ≤ (if ((w j.castSucc : Fin (n + 1)) : ℕ) < m then 1 else 0) := by
      split_ifs <;> omega
    split_ifs at hj hj1 hj2 hb ⊢ <;> omega
  · rw [rk_mul_swap_of_ne w j i m (by omega), rk_mul_swap_of_ne u j i m (by omega)]
    exact h i m

/-! ### The Coxeter-length form of the two steps -/

theorem permCoxeterSystem_simple' (n : ℕ) (i : Fin n) :
    (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).simple i = Equiv.swap i.castSucc i.succ := by
  have h := QOU.Hecke.SymmetricCoxeter.toPerm_simple n i
  simp only [CoxeterMatrix.simple] at h
  simpa [QOU.Hecke.SymmetricCoxeter.permCoxeterSystem, CoxeterSystem.simple,
    QOU.Hecke.SymmetricCoxeter.s] using h

theorem rk_mul_simple_le (w : Perm (Fin (n + 1))) (j : Fin n)
    (hlen : (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length
        (w * (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).simple j)
      = (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length w + 1) (i m : ℕ) :
    rk (w * (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).simple j) i m ≤ rk w i m := by
  rw [permCoxeterSystem_simple'] at hlen ⊢
  exact rk_mul_swap_le w j (Fin.lt_def.mp
    ((QOU.Hecke.Inversions.length_mul_swap_eq_succ_iff w j).mp hlen)) i m

theorem rk_mul_simple_mono (u w : Perm (Fin (n + 1))) (j : Fin n)
    (hlen : (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length
        (w * (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).simple j)
      = (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length w + 1)
    (h : ∀ i m, rk w i m ≤ rk u i m) (i m : ℕ) :
    rk (w * (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).simple j) i m
      ≤ rk (u * (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).simple j) i m := by
  rw [permCoxeterSystem_simple'] at hlen ⊢
  exact rk_mul_swap_mono u w j (Fin.lt_def.mp
    ((QOU.Hecke.Inversions.length_mul_swap_eq_succ_iff w j).mp hlen)) h i m

/-! ### Easy Ehresmann: a subword can only raise the rank matrix -/

open QOU.Hecke.SymmetricCoxeter in
theorem isReduced_of_isReduced_concat {ρ : List (Fin n)} {j : Fin n}
    (h : (permCoxeterSystem n).IsReduced (ρ ++ [j])) :
    (permCoxeterSystem n).IsReduced ρ ∧
      (permCoxeterSystem n).length
          ((permCoxeterSystem n).wordProd ρ * (permCoxeterSystem n).simple j)
        = (permCoxeterSystem n).length ((permCoxeterSystem n).wordProd ρ) + 1 := by
  set cs := permCoxeterSystem n with hcs
  have hw : cs.wordProd (ρ ++ [j]) = cs.wordProd ρ * cs.simple j := by
    rw [cs.wordProd_append, cs.wordProd_singleton]
  have hlen : cs.length (cs.wordProd ρ * cs.simple j) = ρ.length + 1 := by
    have := h
    rw [CoxeterSystem.IsReduced, hw] at this
    simpa using this
  have hle : cs.length (cs.wordProd ρ) ≤ ρ.length := cs.length_wordProd_le ρ
  have hcases := cs.length_mul_simple (cs.wordProd ρ) j
  constructor
  · show cs.length (cs.wordProd ρ) = ρ.length
    rcases hcases with h1 | h1 <;> omega
  · rcases hcases with h1 | h1 <;> omega

open QOU.Hecke.SymmetricCoxeter in
/-- **The easy direction of Ehresmann's criterion**, in the form the subword definition
gives it: a subword of a reduced word has a pointwise-larger rank matrix.

The induction is on the reduced word from the RIGHT: `ω = ρ ++ [j]` splits a subword as
`l₁ ++ l₂` with `l₂` empty or `[j]`, which are exactly the two rank steps proved above —
`rk_mul_simple_le` when the last letter is dropped, `rk_mul_simple_mono` when it is kept. -/
theorem rk_le_of_sublist : ∀ ω : List (Fin n), (permCoxeterSystem n).IsReduced ω →
    ∀ ω' : List (Fin n), ω'.Sublist ω → ∀ i m : ℕ,
      rk ((permCoxeterSystem n).wordProd ω) i m
        ≤ rk ((permCoxeterSystem n).wordProd ω') i m := by
  intro ω
  induction ω using List.reverseRecOn with
  | nil =>
      intro _ ω' hsub i m
      rw [List.sublist_nil.mp hsub]
  | append_singleton ρ j ih =>
      intro hred ω' hsub i m
      obtain ⟨hredρ, hlen⟩ := isReduced_of_isReduced_concat hred
      have hw : (permCoxeterSystem n).wordProd (ρ ++ [j])
          = (permCoxeterSystem n).wordProd ρ * (permCoxeterSystem n).simple j := by
        rw [(permCoxeterSystem n).wordProd_append, (permCoxeterSystem n).wordProd_singleton]
      obtain ⟨l₁, l₂, rfl, hl₁, hl₂⟩ := List.sublist_append_iff.mp hsub
      rcases List.sublist_singleton.mp hl₂ with rfl | rfl
      · simp only [List.append_nil]
        rw [hw]
        exact le_trans (rk_mul_simple_le _ j hlen i m) (ih hredρ l₁ hl₁ i m)
      · have hu : (permCoxeterSystem n).wordProd (l₁ ++ [j])
            = (permCoxeterSystem n).wordProd l₁ * (permCoxeterSystem n).simple j := by
          rw [(permCoxeterSystem n).wordProd_append, (permCoxeterSystem n).wordProd_singleton]
        rw [hw, hu]
        exact rk_mul_simple_mono _ _ j hlen (ih hredρ l₁ hl₁) i m

open QOU.Hecke.SymmetricCoxeter QOU.Machinery.CoxeterBruhat in
/-- **`BruhatLe` implies the rank inequality** — the easy half of Ehresmann's criterion,
for the symmetric group.

This is what a consumer of Dipper–James 3.7 needs for the CONVERSE implication
(`d(s) ≤ d(t) → s ⊵ t`): compose it with the specialisation of the rank inequality to the
row cuts and with `DominanceIsBruhat.domRel_iff_rankAt`.  No reflection order appears, so
this route does not wait on `BruhatLe → ReflLe` (bean `qou-3k66`). -/
theorem rk_le_of_bruhatLe {u w : Perm (Fin (n + 1))}
    (h : BruhatLe (permCoxeterSystem n) u w) (i m : ℕ) : rk w i m ≤ rk u i m := by
  obtain ⟨ω, ω', hred, hw, hsub, hu⟩ := h
  rw [← hw, ← hu]
  exact rk_le_of_sublist ω hred ω' hsub i m

end QOU.Machinery.BruhatRank
