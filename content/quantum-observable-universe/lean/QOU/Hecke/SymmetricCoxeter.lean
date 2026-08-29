import Mathlib.GroupTheory.Coxeter.Matrix
import Mathlib.GroupTheory.Coxeter.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Tactic

set_option linter.unusedSimpArgs false

/-!
# QOU.Hecke.SymmetricCoxeter — `S_{n+1}` and the type-`Aₙ` Coxeter group

The first brick of the `T_w` basis programme (beans `qou-lrz1` / `qou-twwf`).
The `T_w` basis of `H_n(q)` is what `det(Gram)` must be stated against, and it is
the standing Mathlib gap behind the `WenzlCriterion` / `SchurElementCriterion`
discharge.

## What the standing audits say, and what is actually true

The 2026-08-21 `TL_n` scoping audit lists as build item 1 *"`S_n` as a Coxeter
group of type A — **absent**"*, and AGENTS.md records *"`Equiv.Perm` has no
length/inversions"*.  Measured against current Mathlib, that is **stale in one
direction and accurate in the other**:

* **Present.** `CoxeterMatrix.Aₙ`, the whole `CoxeterSystem` API
  (`Mathlib/GroupTheory/Coxeter/{Basic,Length,Inversion,Matrix}.lean`) including
  `length`, and — decisively for surjectivity —
  `Equiv.Perm.mclosure_swap_castSucc_succ`.
* **Absent.** Any connection between `Equiv.Perm` and `CoxeterMatrix.Aₙ`.  A grep
  for `Equiv.Perm` across `GroupTheory/Coxeter/` returns nothing.

So the gap is not the Coxeter theory; it is the **bridge**.  This file builds the
surjective half of that bridge.

## What is proved here (sorry-free, all general `n`)

* `swap_braid_pow_three` / `swap_disjoint_pow_two` — the two transposition
  identities, over any `DecidableEq` type.
* `s n i` — the `i`-th adjacent transposition of `S_{n+1}`.
* `s_rel` — **the adjacent transpositions satisfy every type-`Aₙ` Coxeter
  relation**, all three cases (`i = j`, adjacent, distant) against the actual
  `CoxeterMatrix.Aₙ` entries.
* `toPerm : (Aₙ n).Group →* Equiv.Perm (Fin (n+1))` — the induced map, with
  `toPerm_simple`.
* `toPerm_surjective` — surjective, via Mathlib's
  `Equiv.Perm.mclosure_swap_castSucc_succ`.

## What is NOT proved — the remaining half, stated precisely

`CoxeterSystem M W` is a structure carrying a **`MulEquiv` `W ≃* M.Group`**
(`Coxeter/Basic.lean:154`).  So constructing one needs `toPerm` to be
**injective** as well — i.e. that the presentation imposes *no relations beyond*
the three families, so `|(Aₙ n).Group| ≤ (n+1)!`.

That is the classical hard half of the presentation theorem for `S_n`, and
nothing here bears on it.  It is normally obtained from an order bound
(`|W(Aₙ)| ≤ (n+1)!` by induction over parabolics) or the geometric
representation.

**How hard: Mathlib has never done it for any group.**  Measured — the only
`CoxeterSystem` values in all of Mathlib are the tautological
`CoxeterMatrix.toCoxeterSystem` (the system *on the presented group itself*) and
`CoxeterSystem.map` (transport along an existing `MulEquiv`); there are **zero**
`IsCoxeterGroup` instances.  So Mathlib carries the whole theory —
length, inversions, the exchange property — with **no concrete group** ever
plugged into it.  Completing this bridge is therefore a genuine Mathlib
contribution, not a repo chore, and the surjection above is the first half of
something upstream does not have.  **Do not read this file as
`CoxeterSystem (Aₙ n) (Perm (Fin (n+1)))`** — it is the surjection only.

Scope note (AGENTS.md): the above is a **scope-(a)** statement about what this
file does, not a claim that injectivity is hard *in principle* or blocked.  No
invariant forbids it; it simply is not done here.
-/

open Equiv

namespace QOU.Hecke.SymmetricCoxeter

open CoxeterMatrix

variable {α : Type*} [DecidableEq α]

theorem swap_braid_pow_three (a b c : α) (hab : a ≠ b) (hbc : b ≠ c) (hac : a ≠ c) :
    (Equiv.swap a b * Equiv.swap b c) ^ 3 = 1 := by
  ext x
  simp only [pow_succ, pow_zero, one_mul, Equiv.Perm.mul_apply, Equiv.Perm.one_apply]
  by_cases h1 : x = a
  · subst h1; simp [Equiv.swap_apply_def, hab, hac, hbc, Ne.symm hab, Ne.symm hac, Ne.symm hbc]
  · by_cases h2 : x = b
    · subst h2; simp [Equiv.swap_apply_def, hab, hac, hbc, Ne.symm hab, Ne.symm hac, Ne.symm hbc]
    · by_cases h3 : x = c
      · subst h3; simp [Equiv.swap_apply_def, hab, hac, hbc, Ne.symm hab, Ne.symm hac, Ne.symm hbc]
      · simp [Equiv.swap_apply_of_ne_of_ne, h1, h2, h3]

theorem swap_disjoint_pow_two (a b c d : α)
    (hac : a ≠ c) (had : a ≠ d) (hbc : b ≠ c) (hbd : b ≠ d) :
    (Equiv.swap a b * Equiv.swap c d) ^ 2 = 1 := by
  have hcomm : Equiv.swap a b * Equiv.swap c d = Equiv.swap c d * Equiv.swap a b := by
    ext x
    simp only [Equiv.Perm.mul_apply]
    by_cases h1 : x = a
    · subst h1; simp [Equiv.swap_apply_def, hac, had, hbc, hbd, Ne.symm hac, Ne.symm had, Ne.symm hbc, Ne.symm hbd]
    · by_cases h2 : x = b
      · subst h2; simp [Equiv.swap_apply_def, hac, had, hbc, hbd, Ne.symm hac, Ne.symm had, Ne.symm hbc, Ne.symm hbd]
      · by_cases h3 : x = c
        · subst h3
          simp [Equiv.swap_apply_def, hac, had, hbc, hbd, Ne.symm hac, Ne.symm had, Ne.symm hbc, Ne.symm hbd]
        · by_cases h4 : x = d
          · subst h4
            simp [Equiv.swap_apply_def, hac, had, hbc, hbd, Ne.symm hac, Ne.symm had, Ne.symm hbc, Ne.symm hbd]
          · simp [Equiv.swap_apply_of_ne_of_ne, h1, h2, h3, h4]
  calc (Equiv.swap a b * Equiv.swap c d) ^ 2
      = Equiv.swap a b * (Equiv.swap c d * Equiv.swap a b) * Equiv.swap c d := by
        rw [pow_two]; group
    _ = Equiv.swap a b * (Equiv.swap a b * Equiv.swap c d) * Equiv.swap c d := by
        rw [← hcomm]
    _ = 1 := by
        simp [mul_assoc, ← mul_assoc (Equiv.swap a b), Equiv.swap_mul_self]


/-- The `i`-th adjacent transposition in `S_{n+1}`. -/
def s (n : ℕ) (i : Fin n) : Equiv.Perm (Fin (n + 1)) :=
  Equiv.swap i.castSucc i.succ

theorem castSucc_ne_succ (n : ℕ) (i : Fin n) : i.castSucc ≠ i.succ := by
  simp [Fin.ext_iff]

/-- Helper: `(xy)^3 = x (yx)^3 x⁻¹`, so the braid relation is symmetric in the pair. -/
theorem pow_three_swap {G : Type*} [Group G] (x y : G) (h : (y * x) ^ 3 = 1) :
    (x * y) ^ 3 = 1 := by
  have h' : x * (y * x) ^ 3 * x⁻¹ = 1 := by rw [h, mul_one, mul_inv_cancel]
  simpa [pow_succ, pow_zero, mul_assoc] using h'

theorem s_mul_self (n : ℕ) (i : Fin n) : s n i * s n i = 1 := by
  simp [s, Equiv.swap_mul_self]

/-- **The adjacent transpositions satisfy the type-`Aₙ` Coxeter relations.** -/
theorem s_rel (n : ℕ) (i j : Fin n) : (s n i * s n j) ^ (Aₙ n i j) = 1 := by
  by_cases hij : i = j
  · subst hij
    simp [Aₙ, s_mul_self]
  · have hAd : Aₙ n i j = if (j : ℕ) + 1 = i ∨ (i : ℕ) + 1 = j then 3 else 2 := by
      simp [Aₙ, hij]
    by_cases hadj : (j : ℕ) + 1 = i ∨ (i : ℕ) + 1 = j
    · rw [hAd, if_pos hadj]
      rcases hadj with h | h
      · -- i = j + 1 : shared point is i.castSucc = j.succ
        have hshare : j.succ = i.castSucc := by ext; simp; omega
        apply pow_three_swap
        rw [s, s, hshare]
        exact swap_braid_pow_three _ _ _
          (by simp [Fin.ext_iff]; try omega) (by simp [Fin.ext_iff]; try omega) (by simp [Fin.ext_iff]; try omega)
      · -- j = i + 1 : shared point is i.succ = j.castSucc
        have hshare : i.succ = j.castSucc := by ext; simp; omega
        rw [s, s, ← hshare]
        exact swap_braid_pow_three _ _ _
          (by simp [Fin.ext_iff]; try omega) (by simp [Fin.ext_iff]; try omega) (by simp [Fin.ext_iff]; try omega)
    · rw [hAd, if_neg hadj]
      push_neg at hadj
      have hne : (i : ℕ) ≠ j := fun h => hij (Fin.ext h)
      rw [s, s]
      exact swap_disjoint_pow_two _ _ _ _
        (by simp [Fin.ext_iff]; try omega) (by simp [Fin.ext_iff]; try omega)
        (by simp [Fin.ext_iff]; try omega) (by simp [Fin.ext_iff]; try omega)


/-- **The canonical map from the type-`Aₙ` Coxeter group to `S_{n+1}`.** -/
def toPerm (n : ℕ) : (Aₙ n).Group →* Equiv.Perm (Fin (n + 1)) :=
  PresentedGroup.toGroup (f := s n) (by
    rintro r ⟨⟨i, j⟩, rfl⟩
    simpa [CoxeterMatrix.relation] using s_rel n i j)

@[simp] theorem toPerm_simple (n : ℕ) (i : Fin n) :
    toPerm n (CoxeterMatrix.simple (Aₙ n) i) = s n i := by
  exact PresentedGroup.toGroup.of _


/-- **`toPerm` is surjective**: the adjacent transpositions generate `S_{n+1}`. -/
theorem toPerm_surjective (n : ℕ) : Function.Surjective (toPerm n) := by
  intro g
  have hg : g ∈ Submonoid.closure
      (Set.range fun i : Fin n ↦ Equiv.swap i.castSucc i.succ) := by
    rw [Equiv.Perm.mclosure_swap_castSucc_succ]; exact Submonoid.mem_top g
  induction hg using Submonoid.closure_induction with
  | mem x hx => obtain ⟨i, rfl⟩ := hx
                exact ⟨CoxeterMatrix.simple (Aₙ n) i, toPerm_simple n i⟩
  | one => exact ⟨1, map_one _⟩
  | mul x y _ _ hx hy =>
      obtain ⟨a, rfl⟩ := hx; obtain ⟨b, rfl⟩ := hy
      exact ⟨a * b, map_mul _ _ _⟩

/-! ### The parabolic inclusion

The order-bound route to injectivity (`|W(Aₙ)| ≤ (n+1)!` by induction) needs the
smaller presented group to sit inside the larger one.  That map is built here;
the induction itself is not done — see the header. -/

/-- The `Aₙ` matrix entries depend only on the underlying naturals, so the
    inclusion `Fin n ↪ Fin (n+1)` preserves them. -/
theorem An_castSucc (n : ℕ) (i j : Fin n) :
    Aₙ (n + 1) i.castSucc j.castSucc = Aₙ n i j := by
  simp only [Aₙ, Matrix.of_apply]
  by_cases h : i = j
  · subst h; simp
  · have h' : i.castSucc ≠ j.castSucc := by simpa [Fin.ext_iff] using h
    simp [h, h']

/-- The parabolic inclusion `W(Aₙ) →* W(A_{n+1})`. -/
def incl (n : ℕ) : (Aₙ n).Group →* (Aₙ (n + 1)).Group :=
  PresentedGroup.toGroup (f := fun i : Fin n => CoxeterMatrix.simple (Aₙ (n+1)) i.castSucc) (by
    rintro r ⟨⟨i, j⟩, rfl⟩
    show (FreeGroup.lift fun i : Fin n =>
      CoxeterMatrix.simple (Aₙ (n+1)) i.castSucc) (CoxeterMatrix.relation (Aₙ n) i j) = 1
    have h : ((FreeGroup.lift fun i : Fin n =>
        CoxeterMatrix.simple (Aₙ (n+1)) i.castSucc) (CoxeterMatrix.relation (Aₙ n) i j))
        = (CoxeterMatrix.simple (Aₙ (n+1)) i.castSucc *
           CoxeterMatrix.simple (Aₙ (n+1)) j.castSucc) ^ (Aₙ n i j) := by
      simp [CoxeterMatrix.relation]
    rw [h, ← An_castSucc n i j]
    exact (Aₙ (n+1)).toCoxeterSystem.simple_mul_simple_pow _ _)


end QOU.Hecke.SymmetricCoxeter
