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
* `incl` — the parabolic inclusion `W(Aₙ) →* W(A_{n+1})`.
* An **`ℕ`-indexed generator layer** (`gen`) with all three relation families
  restated arithmetically: `gen_mul_self`, `gen_comm`, `gen_braid`.  These are
  the working form for the order-bound induction, whose index side conditions
  are arithmetic rather than `Fin`-shaped.

## The bridge is COMPLETE

`permCoxeterSystem n : CoxeterSystem (Aₙ n) (Equiv.Perm (Fin (n+1)))`, together
with the `IsCoxeterGroup (Equiv.Perm (Fin (n+1)))` instance.  **`S_{n+1}` is the
Coxeter group of type `Aₙ`, formalized.**

The route, in order:

1. `s_rel` — the adjacent transpositions satisfy every type-`Aₙ` relation, so
   `toPerm : (Aₙ n).Group →* S_{n+1}` exists.
2. `toPerm_surjective` — via `Equiv.Perm.mclosure_swap_castSucc_succ`.
3. `inCosets_all` — every element of `W(Aₙ (n+1))` lies in one of `n+2`
   parabolic cosets `H · t_k`, by `simple_induction_right` over the four closure
   cases.
4. `cover_surjective`, `finiteAn`, `card_An_le` — the cover becomes a surjection
   `W(Aₙ n) × Fin (n+2) ↠ W(Aₙ (n+1))`, giving finiteness from the trivial
   `W(Aₙ 0)` and the bound `|W(Aₙ n)| ≤ (n+1)!`.
5. `toPerm_bijective` — `(n+1)! ≥ |W(Aₙ n)| ≥ |S_{n+1}| = (n+1)!` squeezes, so
   the surjection is a bijection.

**Mathlib does not have this.**  Measured before starting: the only
`CoxeterSystem` values in all of Mathlib are the tautological
`CoxeterMatrix.toCoxeterSystem` (the system *on the presented group itself*) and
`CoxeterSystem.map` (transport along an existing `MulEquiv`), and there are
**zero** `IsCoxeterGroup` instances — the whole theory (length, inversions,
exchange) with no concrete group ever plugged in.  This file plugs the first one
in, which means `cs.length` and all of `Coxeter/Length.lean` and
`Coxeter/Inversion.lean` now apply to `Equiv.Perm`.  That is exactly the length
theory AGENTS.md records as missing, and it is what `T_w` well-definedness rests
on (beans `qou-lrz1` / `qou-twwf`).

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


/-! ### An `ℕ`-indexed generator layer

The order-bound induction reasons about indices arithmetically (`i + 1 < j`,
`j + 1 < N`), which is painful through `Fin`.  This layer re-indexes the simple
reflections by `ℕ` with junk value `1` out of range, and restates the three
Coxeter relation families in that form.  `comm_of_sq_one` and
`braid_of_pow_three` are the group-theoretic content, stated for any group. -/

variable (N : ℕ)

/-- `σ_j` as an `ℕ`-indexed generator, with junk value `1` out of range. -/
noncomputable def gen (N : ℕ) (j : ℕ) : (Aₙ N).Group :=
  if h : j < N then CoxeterMatrix.simple (Aₙ N) ⟨j, h⟩ else 1

theorem gen_mul_self (j : ℕ) : gen N j * gen N j = 1 := by
  unfold gen
  split
  · exact (Aₙ N).toCoxeterSystem.simple_mul_simple_self _
  · simp

theorem An_val (i j : Fin N) :
    Aₙ N i j = if (i:ℕ) = j then 1 else (if (j:ℕ) + 1 = i ∨ (i:ℕ) + 1 = j then 3 else 2) := by
  simp only [Aₙ, Matrix.of_apply, Fin.ext_iff]

/-- Two elements of order ≤ 2 whose product squares to 1 commute. -/
theorem comm_of_sq_one {G : Type*} [Group G] {a b : G}
    (ha : a * a = 1) (hb : b * b = 1) (hab : (a * b) * (a * b) = 1) : a * b = b * a := by
  have h := inv_eq_of_mul_eq_one_left hab
  rw [mul_inv_rev, inv_eq_of_mul_eq_one_left ha, inv_eq_of_mul_eq_one_left hb] at h
  exact h.symm

/-- Distant generators commute. -/
theorem gen_comm {i j : ℕ} (hij : i + 1 < j) : gen N i * gen N j = gen N j * gen N i := by
  by_cases hi : i < N
  · by_cases hj : j < N
    · simp only [gen, dif_pos hi, dif_pos hj]
      refine comm_of_sq_one
        ((Aₙ N).toCoxeterSystem.simple_mul_simple_self _)
        ((Aₙ N).toCoxeterSystem.simple_mul_simple_self _) ?_
      have hpow := (Aₙ N).toCoxeterSystem.simple_mul_simple_pow
        (⟨i, hi⟩ : Fin N) (⟨j, hj⟩ : Fin N)
      rw [An_val] at hpow
      simp only [Fin.val_mk] at hpow
      rw [if_neg (by omega), if_neg (by omega), pow_two] at hpow
      exact hpow
    · simp [gen, dif_pos hi, dif_neg hj]
  · simp [gen, dif_neg hi]


/-- From `(ab)³ = 1` with `a, b` involutions, the braid relation. -/
theorem braid_of_pow_three {G : Type*} [Group G] {a b : G}
    (ha : a * a = 1) (hb : b * b = 1) (h3 : (a * b) ^ 3 = 1) : a * b * a = b * a * b := by
  have key : a * b * a * b * a * b = 1 := by
    have e : (a * b) ^ 3 = a * b * a * b * a * b := by
      simp [pow_succ, mul_assoc]
    rw [← e]; exact h3
  have hprod : (a * b * a) * (b * a * b) = 1 := by
    have e : (a * b * a) * (b * a * b) = a * b * a * b * a * b := by simp [mul_assoc]
    rw [e]; exact key
  have hbab : (b * a * b) * (b * a * b) = 1 := by
    calc (b * a * b) * (b * a * b) = b * a * (b * b) * a * b := by simp [mul_assoc]
      _ = b * a * a * b := by rw [hb, mul_one]
      _ = b * (a * a) * b := by simp [mul_assoc]
      _ = b * b := by rw [ha, mul_one]
      _ = 1 := hb
  exact (inv_eq_of_mul_eq_one_left hprod).symm.trans (inv_eq_of_mul_eq_one_left hbab)

/-- Adjacent generators braid. -/
theorem gen_braid {j : ℕ} (hj : j + 1 < N) :
    gen N j * gen N (j + 1) * gen N j = gen N (j + 1) * gen N j * gen N (j + 1) := by
  have hj0 : j < N := by omega
  simp only [gen, dif_pos hj0, dif_pos hj]
  refine braid_of_pow_three
    ((Aₙ N).toCoxeterSystem.simple_mul_simple_self _)
    ((Aₙ N).toCoxeterSystem.simple_mul_simple_self _) ?_
  have hpow := (Aₙ N).toCoxeterSystem.simple_mul_simple_pow
    (⟨j, hj0⟩ : Fin N) (⟨j + 1, hj⟩ : Fin N)
  rw [An_val] at hpow
  simp only [Fin.val_mk] at hpow
  simp only [or_true, if_true] at hpow
  rw [if_neg (show ¬(j = j + 1) by omega)] at hpow
  exact hpow


/-! ### Descending runs and the four coset-closure cases

The order bound is `|W(Aₙ N)| ≤ (N+1)·|W(Aₙ (N-1))|`, obtained by showing that
the union of the `N+1` cosets `H · t_k` — where `H` is the parabolic `incl`
image and `t_k = σ_{N-1} ⋯ σ_k` — is closed under right multiplication by every
generator, hence is all of `W`.

Closure splits into exactly four cases by the position of `i` relative to `k`,
**all four of which are proved below**:

| case | lemma | mechanism |
|---|---|---|
| `i = k` | `t_mul_gen_self` | `σ_k² = 1` |
| `i = k-1` | `t_mul_gen_pred` | the run extends: it *is* `t_{k-1}` |
| `i + 1 < k` | `t_comm` | distant generators commute past every factor |
| `k < i` | `t_push` | `t_k σ_i = σ_{i-1} t_k`, by induction on `i - k` with a braid base |

`t_push` is the only one with real content: the base case `i = k+1` peels the
run twice and combines the braid relation with `t_comm`, and the step case
commutes `σ_k` past `σ_i` and applies the inductive hypothesis one rung up. -/

/-- The descending run `t N k = σ_{N-1} σ_{N-2} ⋯ σ_k`, empty (`= 1`) when `k ≥ N`. -/
noncomputable def t (N k : ℕ) : (Aₙ N).Group :=
  (((List.range' k (N - k)).reverse).map (gen N)).prod

@[simp] theorem t_self (N : ℕ) : t N N = 1 := by
  simp [t]

theorem t_of_ge {N k : ℕ} (h : N ≤ k) : t N k = 1 := by
  simp [t, Nat.sub_eq_zero_of_le h]

/-- The bottom recursion: peel off the last (smallest-index) generator. -/
theorem t_succ {N k : ℕ} (hk : k < N) : t N k = t N (k + 1) * gen N k := by
  unfold t
  have hlen : N - k = (N - (k + 1)) + 1 := by omega
  rw [hlen]
  have hcons : List.range' k (N - (k + 1) + 1) = k :: List.range' (k + 1) (N - (k + 1)) := rfl
  rw [hcons, List.reverse_cons, List.map_append, List.prod_append]
  simp


/-- Case `i = k`: the run absorbs its own bottom generator. -/
theorem t_mul_gen_self {N k : ℕ} (hk : k < N) : t N k * gen N k = t N (k + 1) := by
  rw [t_succ hk, mul_assoc, gen_mul_self, mul_one]

/-- Case `i = k - 1`: the run extends downward. -/
theorem t_mul_gen_pred {N k : ℕ} (hk : 0 < k) (hkN : k ≤ N) :
    t N k * gen N (k - 1) = t N (k - 1) := by
  have h : k - 1 < N := by omega
  have e := t_succ h
  rw [Nat.sub_add_cancel hk] at e
  exact e.symm

/-- A generator distant from every factor of a product commutes past it. -/
theorem gen_comm_prod {N i : ℕ} (L : List ℕ) (h : ∀ j ∈ L, i + 1 < j) :
    (L.map (gen N)).prod * gen N i = gen N i * (L.map (gen N)).prod := by
  induction L with
  | nil => simp
  | cons a L ih =>
      simp only [List.map_cons, List.prod_cons, mul_assoc]
      rw [ih (fun j hj => h j (List.mem_cons_of_mem _ hj))]
      rw [← mul_assoc, ← mul_assoc, ← gen_comm N (h a (List.mem_cons_self ..))]

/-- Case `i + 1 < k`: distant generators commute past the whole run. -/
theorem t_comm {N i k : ℕ} (h : i + 1 < k) : t N k * gen N i = gen N i * t N k := by
  refine gen_comm_prod _ (fun j hj => ?_)
  rw [List.mem_reverse, List.mem_range'_1] at hj
  omega


/-- Case `k < i`: the run pushes a generator down by one.
    `t_k σ_i = σ_{i-1} t_k`. -/
theorem t_push {N : ℕ} (d : ℕ) : ∀ (k i : ℕ), i = k + 1 + d → i < N →
    t N k * gen N i = gen N (i - 1) * t N k := by
  induction d with
  | zero =>
      intro k i hi hiN
      subst hi
      have hk : k < N := by omega
      have hk1 : k + 1 < N := by omega
      simp only [Nat.add_zero, Nat.add_sub_cancel]
      rw [t_succ hk, t_succ hk1]
      have hbr := gen_braid N (show k + 1 < N by omega)
      have hcm := t_comm (N := N) (i := k) (k := k + 1 + 1) (by omega)
      calc t N (k + 1 + 1) * gen N (k + 1) * gen N k * gen N (k + 1)
          = t N (k + 1 + 1) * (gen N (k + 1) * gen N k * gen N (k + 1)) := by
            simp only [mul_assoc]
        _ = t N (k + 1 + 1) * (gen N k * gen N (k + 1) * gen N k) := by rw [hbr]
        _ = (t N (k + 1 + 1) * gen N k) * gen N (k + 1) * gen N k := by
            simp only [mul_assoc]
        _ = (gen N k * t N (k + 1 + 1)) * gen N (k + 1) * gen N k := by rw [hcm]
        _ = gen N k * (t N (k + 1 + 1) * gen N (k + 1) * gen N k) := by
            simp only [mul_assoc]
  | succ d ih =>
      intro k i hi hiN
      subst hi
      have hk : k < N := by omega
      rw [t_succ hk]
      have hcomm := gen_comm N (show k + 1 < k + 1 + (d + 1) by omega)
      have hIH := ih (k + 1) (k + 1 + 1 + d) rfl (by omega)
      calc t N (k + 1) * gen N k * gen N (k + 1 + (d + 1))
          = t N (k + 1) * (gen N k * gen N (k + 1 + (d + 1))) := by simp only [mul_assoc]
        _ = t N (k + 1) * (gen N (k + 1 + (d + 1)) * gen N k) := by rw [hcomm]
        _ = (t N (k + 1) * gen N (k + 1 + 1 + d)) * gen N k := by
            simp only [mul_assoc]; ring_nf
        _ = (gen N (k + 1 + 1 + d - 1) * t N (k + 1)) * gen N k := by rw [hIH]
        _ = gen N (k + 1 + (d + 1) - 1) * (t N (k + 1) * gen N k) := by
            simp only [mul_assoc]; ring_nf


/-! ### The parabolic coset cover

`inCosets_all` is the structural heart of the order bound: **every** element of
`W(Aₙ (n+1))` lies in one of the `n+2` cosets `H · t_k`, where `H` is the
`incl`-image parabolic.  It is proved by `CoxeterSystem.simple_induction_right`,
whose inductive step is exactly `inCosets_mul_gen` — which in turn is where the
four closure cases above are consumed, one per branch of a trichotomy on `i` vs
`k`.

What this does **not** yet do is turn the cover into a cardinality statement.
That needs the surjection `(Aₙ n).Group × Fin (n+2) → (Aₙ (n+1)).Group`, a
finiteness induction anchored at the trivial `W(Aₙ 0)`, and then the comparison
against `|S_{n+1}| = (n+1)!`. -/

theorem incl_simple (n : ℕ) (i : Fin n) :
    incl n (CoxeterMatrix.simple (Aₙ n) i) =
      CoxeterMatrix.simple (Aₙ (n + 1)) i.castSucc :=
  PresentedGroup.toGroup.of _

/-- The parabolic contains every generator of index `< n`. -/
theorem gen_mem_incl_range {n i : ℕ} (hi : i < n) :
    gen (n + 1) i ∈ (incl n).range := by
  refine ⟨CoxeterMatrix.simple (Aₙ n) ⟨i, hi⟩, ?_⟩
  rw [incl_simple]
  simp only [gen, dif_pos (show i < n + 1 by omega)]
  rfl

/-- Membership in the union of the `n+2` parabolic cosets `H · t_k`. -/
def InCosets (n : ℕ) (x : (Aₙ (n + 1)).Group) : Prop :=
  ∃ k, k ≤ n + 1 ∧ ∃ h ∈ (incl n).range, x = h * t (n + 1) k

theorem inCosets_one (n : ℕ) : InCosets n 1 :=
  ⟨n + 1, le_rfl, 1, one_mem _, by simp⟩


/-- **The coset union is closed under right multiplication by a generator.**
    This is where the four cases of the closure argument are consumed. -/
theorem inCosets_mul_gen {n : ℕ} {x : (Aₙ (n + 1)).Group} (hx : InCosets n x)
    {i : ℕ} (hi : i < n + 1) : InCosets n (x * gen (n + 1) i) := by
  obtain ⟨k, hkN, h, hh, rfl⟩ := hx
  rcases lt_trichotomy i k with hik | hik | hik
  · rcases Nat.lt_or_ge (i + 1) k with hlt | hge
    · exact ⟨k, hkN, h * gen (n + 1) i, mul_mem hh (gen_mem_incl_range (by omega)), by
        rw [mul_assoc, t_comm hlt, ← mul_assoc]⟩
    · have hk : k = i + 1 := by omega
      subst hk
      refine ⟨i, by omega, h, hh, ?_⟩
      rw [mul_assoc]
      congr 1
      simpa using t_mul_gen_pred (N := n + 1) (k := i + 1) (by omega) (by omega)
  · subst hik
    exact ⟨i + 1, by omega, h, hh, by rw [mul_assoc, t_mul_gen_self (by omega)]⟩
  · exact ⟨k, hkN, h * gen (n + 1) (i - 1),
      mul_mem hh (gen_mem_incl_range (by omega)), by
        rw [mul_assoc, t_push (i - k - 1) k i (by omega) hi, ← mul_assoc]⟩

/-- **Every element lies in one of the `n+2` parabolic cosets.** -/
theorem inCosets_all (n : ℕ) (x : (Aₙ (n + 1)).Group) : InCosets n x := by
  refine (Aₙ (n + 1)).toCoxeterSystem.simple_induction_right x (inCosets_one n) ?_
  intro w j hw
  have : (Aₙ (n + 1)).toCoxeterSystem.simple j = gen (n + 1) j := by
    simp only [gen, dif_pos j.isLt]
    rfl
  rw [this]
  exact inCosets_mul_gen hw j.isLt


/-! ### The order bound, and the Coxeter system

`cover_surjective` turns the coset cover into a surjection
`W(Aₙ n) × Fin (n+2) ↠ W(Aₙ (n+1))`.  That gives finiteness by induction from
the trivial `W(Aₙ 0)`, and the bound `|W(Aₙ n)| ≤ (n+1)!`.  Since `toPerm` is
surjective onto `S_{n+1}`, whose order is exactly `(n+1)!`, the two cardinalities
squeeze together and `toPerm` is **bijective**. -/

/-- The coset cover, as a surjection from `W(Aₙ n) × Fin (n+2)`. -/
theorem cover_surjective (n : ℕ) :
    Function.Surjective (fun p : (Aₙ n).Group × Fin (n + 2) =>
      incl n p.1 * t (n + 1) (p.2 : ℕ)) := by
  intro x
  obtain ⟨k, hk, h, ⟨a, rfl⟩, rfl⟩ := inCosets_all n x
  exact ⟨(a, ⟨k, by omega⟩), rfl⟩

/-- `W(A₀)` is trivial: there are no generators. -/
theorem eq_one_of_A0 (x : (Aₙ 0).Group) : x = 1 := by
  refine (Aₙ 0).toCoxeterSystem.simple_induction (p := fun w => w = 1) x
    (fun i => i.elim0) rfl ?_
  intro w w' hw hw'
  rw [hw, hw', one_mul]

instance : Subsingleton ((Aₙ 0).Group) :=
  ⟨fun a b => (eq_one_of_A0 a).trans (eq_one_of_A0 b).symm⟩

instance finiteAn : ∀ n : ℕ, Finite ((Aₙ n).Group)
  | 0 => Finite.of_subsingleton
  | (n + 1) => by
      have := finiteAn n
      exact Finite.of_surjective _ (cover_surjective n)

open Nat

/-- **The order bound: `|W(Aₙ n)| ≤ (n+1)!`.** -/
theorem card_An_le : ∀ n : ℕ, Nat.card ((Aₙ n).Group) ≤ (n + 1)!
  | 0 => by
      have h1 : Nat.card ((Aₙ 0).Group) = 1 :=
        Nat.card_eq_one_iff_unique.mpr ⟨inferInstance, inferInstance⟩
      rw [h1]
      norm_num [Nat.factorial]
  | (n + 1) => by
      have ih := card_An_le n
      have hs := Nat.card_le_card_of_surjective _ (cover_surjective n)
      simp only [Nat.card_prod, Nat.card_fin] at hs
      calc Nat.card ((Aₙ (n + 1)).Group)
          ≤ Nat.card ((Aₙ n).Group) * (n + 2) := hs
        _ ≤ (n + 1)! * (n + 2) := Nat.mul_le_mul_right _ ih
        _ = (n + 1 + 1)! := by rw [Nat.factorial_succ (n + 1)]; ring

theorem card_perm_fin (n : ℕ) : Nat.card (Equiv.Perm (Fin (n + 1))) = (n + 1)! := by
  rw [Nat.card_eq_fintype_card, Fintype.card_perm, Fintype.card_fin]

/-- **`toPerm` is bijective.** -/
theorem toPerm_bijective (n : ℕ) : Function.Bijective (toPerm n) := by
  refine (Nat.bijective_iff_surjective_and_card _).mpr ⟨toPerm_surjective n, ?_⟩
  have hle : Nat.card ((Aₙ n).Group) ≤ Nat.card (Equiv.Perm (Fin (n + 1))) := by
    rw [card_perm_fin]; exact card_An_le n
  have hge : Nat.card (Equiv.Perm (Fin (n + 1))) ≤ Nat.card ((Aₙ n).Group) :=
    Nat.card_le_card_of_surjective _ (toPerm_surjective n)
  omega

/-- **`S_{n+1}` is the Coxeter group of type `Aₙ`.** -/
noncomputable def permCoxeterSystem (n : ℕ) :
    CoxeterSystem (Aₙ n) (Equiv.Perm (Fin (n + 1))) :=
  ⟨(MulEquiv.ofBijective (toPerm n) (toPerm_bijective n)).symm⟩

instance (n : ℕ) : IsCoxeterGroup (Equiv.Perm (Fin (n + 1))) :=
  ⟨_, Aₙ n, ⟨permCoxeterSystem n⟩⟩


end QOU.Hecke.SymmetricCoxeter
