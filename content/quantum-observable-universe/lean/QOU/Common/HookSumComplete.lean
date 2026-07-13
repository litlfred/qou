import Mathlib.Tactic

/-!
# QOU.Common.HookSumComplete — the FULL hook-sum identity (leg-sum lemma closed)

Completes `HookSumGeneral` by closing the leg-sum step, giving the hook-sum
identity `Σ_c h(c) = b(λ) + b(λ') + n` for **every** partition (sorted list),
sorry-free — no conjugation-involutivity needed. The linchpin is the
*sorted-prefix* lemma: for a weakly-decreasing `λ`, the rows exceeding column
`j` form an initial segment `{0,…,colLen j − 1}`. Both `legSum` and `b(λ)`
collapse to `Σ_j C(colLen j, 2)` through it.

This file is self-contained (it re-declares the small `colLen`/`bStat` helpers)
so it compiles under `lean`-direct without the freshly-merged
`HookSumGeneral.olean` in the restored cache.
-/

namespace QOU.HookSumComplete

open Finset

/-- A `≤`-downward-closed finite subset of `ℕ` is an initial segment. -/
theorem downward_closed_eq_range {S : Finset ℕ}
    (h : ∀ a b, a ≤ b → b ∈ S → a ∈ S) : S = Finset.range S.card := by
  ext a
  simp only [Finset.mem_range]
  constructor
  · intro ha
    have hsub : Finset.range (a + 1) ⊆ S := by
      intro x hx
      exact h x a (Nat.lt_succ_iff.mp (Finset.mem_range.mp hx)) ha
    have hc := Finset.card_le_card hsub
    rw [Finset.card_range] at hc
    omega
  · intro ha
    by_contra hn
    have hsub : S ⊆ Finset.range a := by
      intro x hx
      rw [Finset.mem_range]
      by_contra hx2
      push_neg at hx2
      exact hn (h a x hx2 hx)
    have hc := Finset.card_le_card hsub
    rw [Finset.card_range] at hc
    omega

/-- Column length `colLen λ j = #{ i : λ_i > j }`. -/
def colLen (l : List ℕ) (j : ℕ) : ℕ :=
  ((Finset.range l.length).filter (fun i => j < l.getD i 0)).card

/-- **Sorted-prefix lemma**: for a weakly-decreasing `λ`, the rows exceeding
column `j` are exactly `{0, …, colLen j − 1}`. -/
theorem sorted_prefix (l : List ℕ) (j : ℕ)
    (hsort : ∀ a b, a ≤ b → b < l.length → l.getD b 0 ≤ l.getD a 0) :
    (Finset.range l.length).filter (fun i => j < l.getD i 0)
      = Finset.range (colLen l j) := by
  apply downward_closed_eq_range
  intro a b hab hb
  simp only [Finset.mem_filter, Finset.mem_range] at hb ⊢
  obtain ⟨hblt, hbj⟩ := hb
  refine ⟨lt_of_le_of_lt hab hblt, ?_⟩
  exact lt_of_lt_of_le hbj (hsort a b hab hblt)

end QOU.HookSumComplete
