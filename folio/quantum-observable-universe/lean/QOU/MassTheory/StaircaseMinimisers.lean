import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
import Mathlib.Algebra.Order.Group.Unbundled.Int
import Mathlib.Data.Finset.NatAntidiagonal
import Mathlib.Order.UpperLower.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Minimisers of `∑ (i + j)` over sets of cells

First step of the partition count behind `conj:cyclotomic-boundary-at-keystone`. The top
exponent of `dim_q λ` is `C(n,2) - N(λ)` with `N(λ) = ∑_{(i,j) ∈ λ} (i + j)`, so the leading
coefficients of `S(n) = ∑_λ dim_q λ` are governed by the diagrams of smallest `N`.

Write `n = T_m + r` with `T_m = m(m+1)/2` and `r ≤ m + 1`. This file proves, for **every** finite
set of `n` cells of `ℕ × ℕ` (not only Young diagrams):

* `N s ≥ N(stair m) + r·m`, where `stair m` is the set of cells on antidiagonals `< m`
  (`le_N_of_card`);
* equality holds exactly when `s = stair m ∪ R` with `R` a set of `r` cells on antidiagonal `m`
  (`N_eq_iff`);
* every such `stair m ∪ R` is a lower set, i.e. a Young diagram (`isLowerSet_stair_union`), and
  there are `C(m+1, r)` of them (`card_choices`).

So the leading coefficient `C(m+1, r)` is the number of minimisers. Not formalised here: the
Laurent expansion of `dim_q λ` and the `δ = 1, 2` counts that give `a₁`, `a₂`.
-/

namespace QOU.Mass.StaircaseMinimisers

open Finset

/-- The antidiagonal index of a cell. -/
def val (c : ℕ × ℕ) : ℕ := c.1 + c.2

/-- `N s = ∑_{c ∈ s} (i + j)`. -/
def N (s : Finset (ℕ × ℕ)) : ℕ := ∑ c ∈ s, val c

/-- The staircase: all cells on antidiagonals `0, …, m-1`. -/
def stair (m : ℕ) : Finset (ℕ × ℕ) := (range m).biUnion antidiagonal

theorem mem_stair {m : ℕ} {c : ℕ × ℕ} : c ∈ stair m ↔ val c < m := by
  simp [stair, val, mem_antidiagonal]

theorem card_stair (m : ℕ) : (stair m).card = ∑ t ∈ range m, (t + 1) := by
  rw [stair, card_biUnion]
  · simp
  · intro a _ b _ hab
    simp only [Function.onFun]
    rw [Finset.disjoint_left]
    intro c ha hb
    rw [mem_antidiagonal] at ha hb
    exact hab (ha.symm.trans hb)

theorem two_mul_card_stair (m : ℕ) : 2 * (stair m).card = m * (m + 1) := by
  rw [card_stair]
  induction m with
  | zero => simp
  | succ k ih => rw [sum_range_succ, mul_add, ih]; ring

theorem N_stair_union {m : ℕ} {R : Finset (ℕ × ℕ)} (hR : R ⊆ antidiagonal m) :
    N (stair m ∪ R) = N (stair m) + R.card * m := by
  have hdisj : Disjoint (stair m) R := by
    rw [Finset.disjoint_left]
    intro c hc hcR
    have := mem_antidiagonal.1 (hR hcR)
    rw [mem_stair, val, this] at hc
    exact lt_irrefl _ hc
  rw [N, sum_union hdisj, ← N]
  congr 1
  rw [sum_congr rfl (g := fun _ => m) (fun c hc => show val c = m from mem_antidiagonal.1 (hR hc)),
    sum_const]
  simp

/-- **Exchange identity.** For sets of equal size, `N s - N t` is the excess of `s \ t` over `k`
plus the deficit of `t \ s` below `k`, for any level `k`. -/
theorem N_sub_N (s t : Finset (ℕ × ℕ)) (h : s.card = t.card) (k : ℕ) :
    (N s : ℤ) - N t = ∑ a ∈ s \ t, ((val a : ℤ) - k) + ∑ b ∈ t \ s, ((k : ℤ) - val b) := by
  have hst : (s \ t).card = (t \ s).card := by
    have h1 := card_sdiff_add_card_inter s t
    have h2 := card_sdiff_add_card_inter t s
    rw [inter_comm] at h2
    omega
  have es : (N s : ℤ) = ∑ c ∈ s ∩ t, (val c : ℤ) + ∑ c ∈ s \ t, (val c : ℤ) := by
    rw [N, Nat.cast_sum]; exact (sum_inter_add_sum_diff s t _).symm
  have et : (N t : ℤ) = ∑ c ∈ s ∩ t, (val c : ℤ) + ∑ c ∈ t \ s, (val c : ℤ) := by
    rw [N, Nat.cast_sum, inter_comm]; exact (sum_inter_add_sum_diff t s _).symm
  rw [es, et, sum_sub_distrib, sum_sub_distrib, sum_const, sum_const, hst]
  ring

/-- **Lower bound.** Any `T_m + r` cells have `N ≥ N(stair m) + r·m`. -/
theorem le_N_of_card {m r : ℕ} {s : Finset (ℕ × ℕ)} (hr : r ≤ m + 1)
    (hs : s.card = (stair m).card + r) : N (stair m) + r * m ≤ N s := by
  obtain ⟨R, hRsub, hRcard⟩ :=
    exists_subset_card_eq (s := antidiagonal m) (n := r) (by simpa using hr)
  have hcard : s.card = (stair m ∪ R).card := by
    rw [card_union_of_disjoint, hRcard, hs]
    rw [Finset.disjoint_left]
    intro c hc hcR
    rw [mem_stair, val, mem_antidiagonal.1 (hRsub hcR)] at hc
    exact lt_irrefl _ hc
  have key := N_sub_N s (stair m ∪ R) hcard m
  have h1 : 0 ≤ ∑ a ∈ s \ (stair m ∪ R), ((val a : ℤ) - m) := by
    apply sum_nonneg
    intro a ha
    have : a ∉ stair m := fun h => (mem_sdiff.1 ha).2 (mem_union_left _ h)
    rw [mem_stair, not_lt] at this
    exact sub_nonneg.2 (by exact_mod_cast this)
  have h2 : 0 ≤ ∑ b ∈ (stair m ∪ R) \ s, ((m : ℤ) - val b) := by
    apply sum_nonneg
    intro b hb
    rcases mem_union.1 (mem_sdiff.1 hb).1 with h | h
    · exact sub_nonneg.2 (by exact_mod_cast (mem_stair.1 h).le)
    · rw [show val b = m from mem_antidiagonal.1 (hRsub h)]; simp
  have := N_stair_union hRsub
  rw [hRcard] at this
  have hc := congrArg (Nat.cast : ℕ → ℤ) this
  push_cast at hc
  have : ((N (stair m) + r * m : ℕ) : ℤ) ≤ N s := by push_cast; linarith
  exact_mod_cast this

/-- **The minimisers.** Among sets of `T_m + r` cells (`r ≤ m + 1`), `N` attains its minimum
exactly at `stair m ∪ R` with `R` a set of `r` cells on antidiagonal `m`. -/
theorem N_eq_iff {m r : ℕ} {s : Finset (ℕ × ℕ)} (hr : r ≤ m + 1) (hs : s.card = (stair m).card + r) :
    N s = N (stair m) + r * m ↔
      ∃ R ⊆ antidiagonal m, R.card = r ∧ s = stair m ∪ R := by
  constructor
  · intro hN
    set R := s.filter (fun c => val c = m) with hRdef
    -- every cell of `s` is on an antidiagonal `≤ m`, and `stair m ⊆ s`
    have hdisj : ∀ t : Finset (ℕ × ℕ), t ⊆ antidiagonal m → Disjoint (stair m) t := by
      intro t ht
      rw [Finset.disjoint_left]
      intro c hc hct
      rw [mem_stair, val, mem_antidiagonal.1 (ht hct)] at hc
      exact lt_irrefl _ hc
    -- compare with `t = stair m ∪ R'` for any `R'` of size `r` on antidiagonal `m`
    have hstair : stair m ⊆ s ∧ ∀ c ∈ s, val c ≤ m := by
      by_contra hcon
      -- exchange identity against `stair m ∪ R'` for some `R' ⊆ antidiagonal m` of size `r`
      obtain ⟨R', hR'sub, hR'card⟩ :=
        exists_subset_card_eq (s := antidiagonal m) (n := r) (by simpa using hr)
      have hcard : s.card = (stair m ∪ R').card := by
        rw [card_union_of_disjoint (hdisj R' hR'sub), hR'card, hs]
      have key := N_sub_N s (stair m ∪ R') hcard m
      have hNt := N_stair_union hR'sub
      rw [hR'card] at hNt
      have hzero : ∑ a ∈ s \ (stair m ∪ R'), ((val a : ℤ) - m) +
          ∑ b ∈ (stair m ∪ R') \ s, ((m : ℤ) - val b) = 0 := by
        rw [← key, hNt, hN]; ring
      have h1 : 0 ≤ ∑ a ∈ s \ (stair m ∪ R'), ((val a : ℤ) - m) := by
        apply sum_nonneg
        intro a ha
        have : a ∉ stair m := fun h => (mem_sdiff.1 ha).2 (mem_union_left _ h)
        rw [mem_stair, not_lt] at this
        exact sub_nonneg.2 (by exact_mod_cast this)
      have h2 : 0 ≤ ∑ b ∈ (stair m ∪ R') \ s, ((m : ℤ) - val b) := by
        apply sum_nonneg
        intro b hb
        rcases mem_union.1 (mem_sdiff.1 hb).1 with h | h
        · exact sub_nonneg.2 (by exact_mod_cast (mem_stair.1 h).le)
        · rw [show val b = m from mem_antidiagonal.1 (hR'sub h)]; simp
      have z1 : ∀ a ∈ s \ (stair m ∪ R'), (val a : ℤ) - m = 0 := (sum_eq_zero_iff_of_nonneg (fun a (ha : a ∈ s \ (stair m ∪ R')) => by
        have : a ∉ stair m := fun h => (mem_sdiff.1 ha).2 (mem_union_left _ h)
        rw [mem_stair, not_lt] at this
        exact sub_nonneg.2 (by exact_mod_cast this))).1 (by linarith)
      have z2 : ∀ b ∈ (stair m ∪ R') \ s, (m : ℤ) - val b = 0 := (sum_eq_zero_iff_of_nonneg (fun b (hb : b ∈ (stair m ∪ R') \ s) => by
        rcases mem_union.1 (mem_sdiff.1 hb).1 with h | h
        · exact sub_nonneg.2 (by exact_mod_cast (mem_stair.1 h).le)
        · rw [show val b = m from mem_antidiagonal.1 (hR'sub h)]; simp)).1 (by linarith)
      apply hcon
      constructor
      · intro c hc
        by_contra hcs
        have := z2 c (mem_sdiff.2 ⟨mem_union_left _ hc, hcs⟩)
        have hc' := mem_stair.1 hc
        omega
      · intro c hc
        by_contra hgt
        push_neg at hgt
        have hcn : c ∉ stair m ∪ R' := by
          intro h
          rcases mem_union.1 h with h | h
          · exact absurd (mem_stair.1 h) (by omega)
          · have := mem_antidiagonal.1 (hR'sub h); simp only [val] at hgt; omega
        have := z1 c (mem_sdiff.2 ⟨hc, hcn⟩)
        omega
    refine ⟨R, fun c hc => mem_antidiagonal.2 (mem_filter.1 hc).2, ?_, ?_⟩
    · have hseq : s = stair m ∪ R := by
        ext c
        constructor
        · intro hc
          rcases (hstair.2 c hc).lt_or_eq with h | h
          · exact mem_union_left _ (mem_stair.2 h)
          · exact mem_union_right _ (mem_filter.2 ⟨hc, h⟩)
        · intro hc
          rcases mem_union.1 hc with h | h
          · exact hstair.1 h
          · exact (mem_filter.1 h).1
      have := hs
      rw [hseq, card_union_of_disjoint (hdisj R (fun c hc => mem_antidiagonal.2
        (mem_filter.1 hc).2))] at this
      omega
    · ext c
      constructor
      · intro hc
        rcases (hstair.2 c hc).lt_or_eq with h | h
        · exact mem_union_left _ (mem_stair.2 h)
        · exact mem_union_right _ (mem_filter.2 ⟨hc, h⟩)
      · intro hc
        rcases mem_union.1 hc with h | h
        · exact hstair.1 h
        · exact (mem_filter.1 h).1
  · rintro ⟨R, hRsub, hRcard, rfl⟩
    rw [N_stair_union hRsub, hRcard]

/-- Every minimiser is a Young diagram: `stair m ∪ R` is a lower set for `R` on antidiagonal `m`. -/
theorem isLowerSet_stair_union {m : ℕ} {R : Finset (ℕ × ℕ)} (hR : R ⊆ antidiagonal m) :
    IsLowerSet ((stair m ∪ R : Finset (ℕ × ℕ)) : Set (ℕ × ℕ)) := by
  intro a b hba ha
  simp only [coe_union, Set.mem_union, mem_coe] at ha ⊢
  rcases eq_or_ne b a with rfl | hne
  · exact ha
  · left
    rw [mem_stair, val]
    have hle : b.1 + b.2 < a.1 + a.2 := by
      obtain ⟨h1, h2⟩ := hba
      rcases Nat.lt_or_ge b.1 a.1 with h | h
      · omega
      · have : b.1 = a.1 := le_antisymm h1 h
        rcases Nat.lt_or_ge b.2 a.2 with h' | h'
        · omega
        · exact absurd (Prod.ext this (le_antisymm h2 h')) hne
    rcases ha with ha | ha
    · rw [mem_stair, val] at ha; omega
    · rw [mem_antidiagonal.1 (hR ha)] at hle; exact hle

/-- There are `C(m+1, r)` minimisers. -/
theorem card_choices (m r : ℕ) : ((antidiagonal m).powersetCard r).card = (m + 1).choose r := by
  simp

end QOU.Mass.StaircaseMinimisers
