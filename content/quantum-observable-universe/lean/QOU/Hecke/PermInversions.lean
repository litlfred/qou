import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Order.Fin.Basic
import Mathlib.Tactic

/-!
# QOU.Hecke.Inversions — an ℕ-valued inversion count for `Perm (Fin n)`

Toward the braid half of the `T_w` basis (bean `qou-twwf`).

## Why this exists

`QOU.Hecke.TwBasis` proves the Hecke **quadratic** relation for the right
multiplication operators `Rs i`, using only Mathlib's `length_mul_simple`
dichotomy.  The **braid** relation needs to know *which* branch each length
comparison takes, and the textbook route to that (dihedral reduction through
parabolic cosets) needs machinery Mathlib does not have — measured: the whole
`Mathlib/GroupTheory/Coxeter/` directory is four files (`Basic`, `Inversion`,
`Length`, `Matrix`), with **no** strong exchange property, **no** parabolic
subgroups, and **no** minimal coset representatives.

For type `A` there is a concrete alternative: a descent is just a comparison of
two values, `ℓ(w sᵢ) > ℓ(w) ↔ w(i) < w(i+1)`.  Getting there needs
`ℓ = invCount`, and Mathlib has only `signAux` — the inversion **parity**, as a
`ℤˣ`-valued product — with no ℕ-valued count and no comparison to `ℓ`.  So the
count is built here.

## What is proved (sorry-free)

* `eq_one_of_strictMono` — a strictly monotone permutation of `Fin n` is the
  identity.  Via `StrictMono.orderIsoOfSurjective` and the subsingleton of
  `Fin n ≃o Fin n`.
* `invSet` / `invCount` — the inversion set and its cardinality.
* `invCount_one`.
* **`eq_one_of_invCount_eq_zero`** — no inversions implies the identity.  This is
  the base case of the `ℓ = invCount` induction.

* `swap_pair_lt` — swapping two **adjacent** positions preserves the order of
  every pair except the swapped pair itself.  This is the crux: it is exactly
  what fails for a non-adjacent transposition.
* `card_erase_invSet_swap` — the pair-matching bijection.  Pairs meeting
  `{i, i+1}` in one element swap with each other, so every pair *except*
  `(i, i+1)` contributes identically to both inversion sets.
* **`invCount_mul_swap`** — the step lemma: `invCount (w · sᵢ)` differs from
  `invCount w` by exactly one, upward exactly when `w(i) < w(i+1)`.

## What is NOT proved yet

`ℓ = invCount`, and hence the descent characterisation
`ℓ(w sᵢ) > ℓ(w) ↔ w(i) < w(i+1)`.  Both directions now follow from the step
lemma by induction — `invCount ≤ ℓ` because each generator moves the count by
one, and `ℓ ≤ invCount` by descending induction using
`eq_one_of_invCount_eq_zero` as the base — but neither is written yet.
-/

open Equiv Finset
namespace QOU.Hecke.Inversions

variable {n : ℕ}

/-- A strictly monotone permutation of `Fin n` is the identity. -/
theorem eq_one_of_strictMono {w : Perm (Fin n)} (h : StrictMono w) : w = 1 := by
  have hiso : (StrictMono.orderIsoOfSurjective (w : Fin n → Fin n) h w.surjective)
      = OrderIso.refl (Fin n) := Subsingleton.elim _ _
  ext a
  have h2 : w a = a := by
    simpa using congrArg (fun e : Fin n ≃o Fin n => e a) hiso
  exact congrArg Fin.val h2

/-- The inversion set of a permutation of `Fin n`. -/
def invSet (w : Perm (Fin n)) : Finset (Fin n × Fin n) :=
  Finset.univ.filter (fun p => p.1 < p.2 ∧ w p.2 < w p.1)

/-- The number of inversions. -/
def invCount (w : Perm (Fin n)) : ℕ := (invSet w).card

@[simp] theorem invCount_one : invCount (1 : Perm (Fin n)) = 0 := by
  simp only [invCount, invSet, Perm.coe_one, id_eq, card_eq_zero, filter_eq_empty_iff]
  rintro ⟨a, b⟩ -
  simp only [not_and, not_lt]
  exact fun h => le_of_lt h

/-- **A permutation with no inversions is the identity.** -/
theorem eq_one_of_invCount_eq_zero {w : Perm (Fin n)} (h : invCount w = 0) : w = 1 := by
  refine eq_one_of_strictMono (fun a b hab => ?_)
  by_contra hcon
  have hmem : (a, b) ∈ invSet w := by
    simp only [invSet, mem_filter, mem_univ, true_and]
    refine ⟨hab, lt_of_le_of_ne (not_lt.mp hcon) (fun he => ?_)⟩
    exact absurd (w.injective he) (ne_of_gt hab)
  exact absurd h (Finset.card_ne_zero_of_mem hmem)


/-! ### The step lemma -/

/-- Swapping two *adjacent* positions preserves the order of every pair except
    the swapped pair itself. -/
theorem swap_pair_lt {i : Fin n} {a b : Fin (n + 1)} (hab : a < b)
    (hne : ¬(a = i.castSucc ∧ b = i.succ)) :
    Equiv.swap i.castSucc i.succ a < Equiv.swap i.castSucc i.succ b := by
  have hadj : (i.succ : ℕ) = (i.castSucc : ℕ) + 1 := by simp
  have hab' : (a : ℕ) < (b : ℕ) := hab
  have hne' : ¬((a : ℕ) = (i.castSucc : ℕ) ∧ (b : ℕ) = (i.succ : ℕ)) := by
    rintro ⟨h1, h2⟩
    exact hne ⟨Fin.ext h1, Fin.ext h2⟩
  simp only [Equiv.swap_apply_def]
  split_ifs <;>
    simp only [Fin.lt_def, Fin.ext_iff] at * <;>
    omega


theorem mem_invSet {m : ℕ} {w : Perm (Fin m)} {p : Fin m × Fin m} :
    p ∈ invSet w ↔ p.1 < p.2 ∧ w p.2 < w p.1 := by
  simp [invSet]

/-- Pairs other than the swapped one biject between the two inversion sets. -/
theorem card_erase_invSet_swap (w : Perm (Fin (n + 1))) (i : Fin n) :
    ((invSet (w * Equiv.swap i.castSucc i.succ)).erase (i.castSucc, i.succ)).card
      = ((invSet w).erase (i.castSucc, i.succ)).card := by
  have hAB : i.castSucc < i.succ := by simp [Fin.lt_def]
  have hswap : ∀ x, Equiv.swap i.castSucc i.succ (Equiv.swap i.castSucc i.succ x) = x :=
    fun x => Equiv.swap_apply_self _ _ _
  refine Finset.card_nbij'
    (fun p => (Equiv.swap i.castSucc i.succ p.1, Equiv.swap i.castSucc i.succ p.2))
    (fun p => (Equiv.swap i.castSucc i.succ p.1, Equiv.swap i.castSucc i.succ p.2))
    ?_ ?_ ?_ ?_
  · rintro ⟨a, b⟩ hp
    simp only [Finset.mem_coe, Finset.mem_erase, mem_invSet] at hp ⊢
    obtain ⟨hne, hlt, hinv⟩ := hp
    refine ⟨?_, swap_pair_lt hlt (fun h => hne (by rw [h.1, h.2])), hinv⟩
    intro h1
    have e1 : Equiv.swap i.castSucc i.succ a = i.castSucc := congrArg Prod.fst h1
    have e2 : Equiv.swap i.castSucc i.succ b = i.succ := congrArg Prod.snd h1
    have ha : a = i.succ := by rw [← hswap a, e1]; simp
    have hb : b = i.castSucc := by rw [← hswap b, e2]; simp
    rw [ha, hb] at hlt
    exact absurd hlt (asymm hAB)
  · rintro ⟨a, b⟩ hp
    simp only [Finset.mem_coe, Finset.mem_erase, mem_invSet] at hp ⊢
    obtain ⟨hne, hlt, hinv⟩ := hp
    refine ⟨?_, swap_pair_lt hlt (fun h => hne (by rw [h.1, h.2])), by simpa using hinv⟩
    intro h1
    have e1 : Equiv.swap i.castSucc i.succ a = i.castSucc := congrArg Prod.fst h1
    have e2 : Equiv.swap i.castSucc i.succ b = i.succ := congrArg Prod.snd h1
    have ha : a = i.succ := by rw [← hswap a, e1]; simp
    have hb : b = i.castSucc := by rw [← hswap b, e2]; simp
    rw [ha, hb] at hlt
    exact absurd hlt (asymm hAB)
  · rintro ⟨a, b⟩ _; simp [hswap]
  · rintro ⟨a, b⟩ _; simp [hswap]


theorem mem_invSet_swap_pair (w : Perm (Fin (n + 1))) (i : Fin n) :
    ((i.castSucc, i.succ) ∈ invSet (w * Equiv.swap i.castSucc i.succ))
      ↔ w i.castSucc < w i.succ := by
  rw [mem_invSet]
  simp only [Equiv.Perm.mul_apply, Equiv.swap_apply_left, Equiv.swap_apply_right]
  exact ⟨fun h => h.2, fun h => ⟨by simp [Fin.lt_def], h⟩⟩

theorem mem_invSet_pair (w : Perm (Fin (n + 1))) (i : Fin n) :
    ((i.castSucc, i.succ) ∈ invSet w) ↔ w i.succ < w i.castSucc := by
  rw [mem_invSet]
  exact ⟨fun h => h.2, fun h => ⟨by simp [Fin.lt_def], h⟩⟩

/-- **The inversion count changes by exactly one under an adjacent
    transposition**, upward exactly when the values are in increasing order. -/
theorem invCount_mul_swap (w : Perm (Fin (n + 1))) (i : Fin n) :
    (w i.castSucc < w i.succ ∧
      invCount (w * Equiv.swap i.castSucc i.succ) = invCount w + 1) ∨
    (w i.succ < w i.castSucc ∧
      invCount (w * Equiv.swap i.castSucc i.succ) + 1 = invCount w) := by
  have hcard := card_erase_invSet_swap w i
  have hne : w i.castSucc ≠ w i.succ := by
    intro h
    exact absurd (w.injective h) (by simp [Fin.ext_iff])
  rcases lt_or_gt_of_ne hne with hlt | hgt
  · left
    refine ⟨hlt, ?_⟩
    have h1 : (i.castSucc, i.succ) ∈ invSet (w * Equiv.swap i.castSucc i.succ) :=
      (mem_invSet_swap_pair w i).mpr hlt
    have h2 : (i.castSucc, i.succ) ∉ invSet w := by
      rw [mem_invSet_pair]; exact not_lt.mpr (le_of_lt hlt)
    unfold invCount
    rw [← Finset.card_erase_add_one h1, hcard, Finset.erase_eq_of_notMem h2]
  · right
    refine ⟨hgt, ?_⟩
    have h1 : (i.castSucc, i.succ) ∉ invSet (w * Equiv.swap i.castSucc i.succ) := by
      rw [mem_invSet_swap_pair]; exact not_lt.mpr (le_of_lt hgt)
    have h2 : (i.castSucc, i.succ) ∈ invSet w := (mem_invSet_pair w i).mpr hgt
    unfold invCount
    rw [← Finset.card_erase_add_one h2, ← hcard, Finset.erase_eq_of_notMem h1]


end QOU.Hecke.Inversions
