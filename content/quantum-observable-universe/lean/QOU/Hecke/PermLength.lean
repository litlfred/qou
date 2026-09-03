import QOU.Hecke.PermInversions
import QOU.Hecke.SymmetricCoxeter
import Mathlib.GroupTheory.Coxeter.Length

/-!
# QOU.Hecke.PermLength — Coxeter length on `S_{n+1}` IS the inversion count

The gate the braid half of the `T_w` basis was waiting on (bean `qou-twwf`).

## Why this is the right target

`QOU.Hecke.TwBasis` proves the Hecke **quadratic** relation for the operators
`Rs i` using only Mathlib's `length_mul_simple` dichotomy — that lemma says the
length changes by one, without saying *which way*.  The **braid** relation needs
to know which way, and the textbook route (dihedral reduction through parabolic
cosets) needs machinery Mathlib does not have: its whole
`GroupTheory/Coxeter/` directory is four files, with no strong exchange
property, no parabolic subgroups and no minimal coset representatives.

For type `A` the branch is decidable by a **value comparison**, and that is what
this file establishes.

## What is proved (sorry-free)

* `permCox_simple` — the Coxeter system's simple reflections *are* the adjacent
  transpositions.  This is what lets Mathlib's abstract length talk to the
  concrete inversion count.
* `exists_descent` — a permutation other than the identity has an adjacent
  descent (via `Fin.strictMono_iff_lt_succ` and `eq_one_of_strictMono`).
* `length_le_invCount` — by induction on the inversion count, peeling a descent.
* `invCount_le_length` — by reverse induction along a reduced word.
* **`length_eq_invCount`** — `ℓ w = invCount w`.
* **`length_mul_swap_eq_succ_iff`** — the descent characterisation:
  `ℓ(w · sᵢ) = ℓ(w) + 1 ↔ w(i) < w(i+1)`.

Mathlib has neither: it carries `signAux`, the inversion **parity** as a
`ℤˣ`-valued product, and no ℕ-valued count, and it never compares either to `ℓ`.

## What this unlocks, and what it does not

`length_mul_swap_eq_succ_iff` makes every branch condition in `Rs` a comparison
of `w` at two adjacent points, so the braid relation `Rs i ∘ Rs j ∘ Rs i =
Rs j ∘ Rs i ∘ Rs j` becomes a finite case analysis on the relative order of
`w(i)`, `w(i+1)`, `w(i+2)`.  **That case analysis is not done here**, nor is the
algebra map `H_n(q) → End (W →₀ R)` or the independence of the `T_w` that would
follow from it.
-/

open Equiv Finset
namespace QOU.Hecke.Inversions
open QOU.Hecke.SymmetricCoxeter

variable {n : ℕ}

variable {n : ℕ}

/-- The Coxeter system's simple reflections are the adjacent transpositions. -/
@[simp] theorem permCox_simple (i : Fin n) :
    (permCoxeterSystem n).simple i = s n i := by
  show toPerm n (CoxeterMatrix.simple (CoxeterMatrix.Aₙ n) i) = s n i
  exact toPerm_simple n i

/-- A permutation that is not the identity has an adjacent descent. -/
theorem exists_descent {w : Perm (Fin (n + 1))} (h : w ≠ 1) :
    ∃ i : Fin n, w i.succ < w i.castSucc := by
  by_contra hcon
  push_neg at hcon
  refine h (eq_one_of_strictMono (Fin.strictMono_iff_lt_succ.mpr (fun i => ?_)))
  refine lt_of_le_of_ne (hcon i) (fun he => ?_)
  exact absurd (w.injective he) (by simp [Fin.ext_iff])


theorem s_eq_swap (i : Fin n) : s n i = Equiv.swap i.castSucc i.succ := rfl

/-- `ℓ w ≤ invCount w`, by induction on the inversion count. -/
theorem length_le_invCount_aux :
    ∀ (k : ℕ) (w : Perm (Fin (n + 1))), invCount w ≤ k →
      (permCoxeterSystem n).length w ≤ invCount w := by
  intro k
  induction k with
  | zero =>
      intro w hk
      have h0 : invCount w = 0 := Nat.le_zero.mp hk
      rw [eq_one_of_invCount_eq_zero h0]
      simp
  | succ k ih =>
      intro w hk
      by_cases hw : w = 1
      · subst hw; simp
      · obtain ⟨i, hi⟩ := exists_descent hw
        have hdown : invCount (w * Equiv.swap i.castSucc i.succ) + 1 = invCount w := by
          rcases invCount_mul_swap w i with ⟨h1, -⟩ | ⟨-, h2⟩
          · exact absurd hi (asymm h1)
          · exact h2
        have IH := ih (w * Equiv.swap i.castSucc i.succ) (by omega)
        have hlen : (permCoxeterSystem n).length w
            ≤ (permCoxeterSystem n).length (w * Equiv.swap i.castSucc i.succ) + 1 := by
          have hback : w = (w * Equiv.swap i.castSucc i.succ) * (s n i) := by
            rw [s_eq_swap, mul_assoc, Equiv.swap_mul_self, mul_one]
          calc (permCoxeterSystem n).length w
              = (permCoxeterSystem n).length
                  ((w * Equiv.swap i.castSucc i.succ) * (permCoxeterSystem n).simple i) := by
                rw [permCox_simple]; exact congrArg _ hback
            _ ≤ (permCoxeterSystem n).length (w * Equiv.swap i.castSucc i.succ) + 1 := by
                rcases (permCoxeterSystem n).length_mul_simple
                  (w * Equiv.swap i.castSucc i.succ) i with h | h <;> omega
        omega

theorem length_le_invCount (w : Perm (Fin (n + 1))) :
    (permCoxeterSystem n).length w ≤ invCount w :=
  length_le_invCount_aux (invCount w) w le_rfl


theorem invCount_wordProd_le (ω : List (Fin n)) :
    invCount ((permCoxeterSystem n).wordProd ω) ≤ ω.length := by
  induction ω using List.reverseRecOn with
  | nil => simp [CoxeterSystem.wordProd]
  | append_singleton ω i ih =>
      have hw : (permCoxeterSystem n).wordProd (ω ++ [i])
          = (permCoxeterSystem n).wordProd ω * Equiv.swap i.castSucc i.succ := by
        simp [CoxeterSystem.wordProd, permCox_simple, s_eq_swap]
      rw [hw]
      rcases invCount_mul_swap ((permCoxeterSystem n).wordProd ω) i with ⟨-, h⟩ | ⟨-, h⟩ <;>
        simp only [List.length_append, List.length_cons, List.length_nil] <;> omega

theorem invCount_le_length (w : Perm (Fin (n + 1))) :
    invCount w ≤ (permCoxeterSystem n).length w := by
  obtain ⟨ω, hlen, hw⟩ := (permCoxeterSystem n).exists_reduced_word w
  rw [← hlen, hw]
  exact invCount_wordProd_le ω

/-- **Coxeter length is the inversion count.** -/
theorem length_eq_invCount (w : Perm (Fin (n + 1))) :
    (permCoxeterSystem n).length w = invCount w :=
  le_antisymm (length_le_invCount w) (invCount_le_length w)

/-- **The descent characterisation**: the length goes up exactly when the two
    values are in increasing order. -/
theorem length_mul_swap_eq_succ_iff (w : Perm (Fin (n + 1))) (i : Fin n) :
    (permCoxeterSystem n).length (w * Equiv.swap i.castSucc i.succ)
        = (permCoxeterSystem n).length w + 1
      ↔ w i.castSucc < w i.succ := by
  rw [length_eq_invCount, length_eq_invCount]
  constructor
  · intro h
    rcases invCount_mul_swap w i with ⟨h1, -⟩ | ⟨-, h2⟩
    · exact h1
    · omega
  · intro h
    rcases invCount_mul_swap w i with ⟨-, h1⟩ | ⟨h2, -⟩
    · exact h1
    · exact absurd h (asymm h2)

end QOU.Hecke.Inversions
