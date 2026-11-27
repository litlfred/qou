import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Powerset
import Mathlib.Tactic

/-!
# Classical reading 3 bounds the merge count by `n − log₂(n+1)`

Brief C2 of the compute-accuracy epic (`qou-myts`), towards the open kernel `qou-brng`.
Companion of `QOU.MassTheory.ClassicalLogBindingCycleCount`, whose ceiling `n − 1` merges is
reached only by an `n`-cycle. Audit: `docs/audits/2026-11-27-binding-ceiling-at-q0.md`.

## Setting

Let `σ ∈ Sₙ` have `c` cycles with lengths `ℓ : Fin c → ℕ`, `∑ ℓ = n`. A `σ`-invariant subset
of `{1,…,n}` is a union of cycles, so the number of invariant `k`-subsets is

    a_k = #{ s ⊆ Fin c : ∑_{i ∈ s} ℓ i = k }        (`subsetSums ℓ k`).

By Young's rule the permutation module on `k`-subsets is `M^{(n−k,k)} = ⊕_{j ≤ k} S^{(n−j,j)}`,
so the two-row irreducible characters are `χ_{(n−k,k)}(σ) = a_k − a_{k−1}` for `k ≤ n/2`
(-- Ref: [sagan2001] Thm 2.11.2 and §2.3; [james1984representation]). Reading 3 of the γγ rule asks for
`χ_λ ≥ 0` on every block with `y_λ > 0`; under convention D those are exactly the two-row
blocks. At `q = 1` and the top level it therefore says `a_0 ≤ a_1 ≤ … ≤ a_{⌊n/2⌋}`. That is the
hypothesis `hmono` below. The bridge from characters to `a_k` is the cited step and is not
formalised here; the theorems are stated on `a_k`.

## What is proved

1. `subsetSums_symm` — `a_k = a_{n−k}` (complement).
2. `subsetSums_pos_of_mono` — with `hmono`, every `a_k ≥ 1` for `k ≤ n`.
3. `succ_le_two_pow_of_pos` — if every `a_k ≥ 1` for `k ≤ n`, then `n + 1 ≤ 2^c`.
4. `succ_le_two_pow_of_mono` — classical top-level reading 3 forces `n + 1 ≤ 2^c`, so the merge
   count `n − c` is at most `n − ⌈log₂(n+1)⌉`, against `n − 1` without reading 3.
5. `six_strands_three_cycles` — at `n = 6`, `c ≥ 3`.

The bound is sharp for `n ≤ 30` (cycle lengths `1, 2, 4, …`; computed in the audit, not proved
here). No empirical number appears in any statement.
-/

namespace QOU.MassTheory.ClassicalReading3MergeBound

open Finset

variable {c : ℕ}

/-- `a_k`: the number of index sets of cycles whose lengths sum to `k`, i.e. the number of
invariant `k`-subsets of a permutation with cycle lengths `ℓ`. -/
def subsetSums (ℓ : Fin c → ℕ) (k : ℕ) : ℕ :=
  #(univ.filter fun s : Finset (Fin c) => ∑ i ∈ s, ℓ i = k)

theorem subsetSums_zero_pos (ℓ : Fin c → ℕ) : 1 ≤ subsetSums ℓ 0 := by
  unfold subsetSums
  apply Finset.card_pos.mpr
  exact ⟨∅, by simp⟩

/-- Complementation: `a_k = a_{n−k}` when the lengths sum to `n`. -/
theorem subsetSums_symm (ℓ : Fin c → ℕ) {n k : ℕ} (hn : ∑ i, ℓ i = n) (hk : k ≤ n) :
    subsetSums ℓ k = subsetSums ℓ (n - k) := by
  unfold subsetSums
  refine Finset.card_bij (fun s _ => univ \ s) ?_ ?_ ?_
  · intro s hs
    simp only [mem_filter, mem_univ, true_and] at hs ⊢
    have h := Finset.sum_sdiff (s₁ := s) (s₂ := univ) (f := ℓ) (subset_univ s)
    omega
  · intro s _ t _ h
    simpa using congrArg (univ \ ·) h
  · intro t ht
    refine ⟨univ \ t, ?_, by simp⟩
    simp only [mem_filter, mem_univ, true_and] at ht ⊢
    have h := Finset.sum_sdiff (s₁ := t) (s₂ := univ) (f := ℓ) (subset_univ t)
    omega

/-- Monotone up to the middle plus `a_0 ≥ 1` and symmetry gives `a_k ≥ 1` for every `k ≤ n`. -/
theorem subsetSums_pos_of_mono (ℓ : Fin c → ℕ) {n : ℕ} (hn : ∑ i, ℓ i = n)
    (hmono : ∀ k, k + 1 ≤ n / 2 → subsetSums ℓ k ≤ subsetSums ℓ (k + 1)) :
    ∀ k ≤ n, 1 ≤ subsetSums ℓ k := by
  have low : ∀ k ≤ n / 2, 1 ≤ subsetSums ℓ k := by
    intro k hk
    induction k with
    | zero => exact subsetSums_zero_pos ℓ
    | succ j ih => exact le_trans (ih (by omega)) (hmono j hk)
  intro k hk
  by_cases h : k ≤ n / 2
  · exact low k h
  · rw [subsetSums_symm ℓ hn hk]
    exact low (n - k) (by omega)

/-- Distinct sums come from distinct index sets, so covering `0, …, n` needs `n + 1 ≤ 2^c`. -/
theorem succ_le_two_pow_of_pos (ℓ : Fin c → ℕ) {n : ℕ}
    (hpos : ∀ k ≤ n, 1 ≤ subsetSums ℓ k) : n + 1 ≤ 2 ^ c := by
  classical
  have hdisj : (↑(range (n + 1)) : Set ℕ).PairwiseDisjoint
      (fun k => univ.filter fun s : Finset (Fin c) => ∑ i ∈ s, ℓ i = k) := by
    intro a _ b _ hab
    simp only [Function.onFun]
    rw [Finset.disjoint_filter]
    intro s _ h1 h2
    exact hab (h1.symm.trans h2)
  have hsum : ∑ k ∈ range (n + 1), subsetSums ℓ k ≤ 2 ^ c := by
    unfold subsetSums
    rw [← Finset.card_biUnion hdisj]
    calc _ ≤ #(univ : Finset (Finset (Fin c))) := card_le_univ _
      _ = 2 ^ c := by simp
  have hge : n + 1 ≤ ∑ k ∈ range (n + 1), subsetSums ℓ k := by
    calc n + 1 = ∑ _k ∈ range (n + 1), 1 := by simp
      _ ≤ _ := Finset.sum_le_sum fun k hk => hpos k (by simpa [Nat.lt_succ_iff] using hk)
  omega

/-- **Classical reading 3 bounds the merges.** If the two-row characters of a permutation with
cycle lengths `ℓ` (`c` cycles, `n` points) are non-negative, then `n + 1 ≤ 2^c`. -/
theorem succ_le_two_pow_of_mono (ℓ : Fin c → ℕ) {n : ℕ} (hn : ∑ i, ℓ i = n)
    (hmono : ∀ k, k + 1 ≤ n / 2 → subsetSums ℓ k ≤ subsetSums ℓ (k + 1)) : n + 1 ≤ 2 ^ c :=
  succ_le_two_pow_of_pos ℓ (subsetSums_pos_of_mono ℓ hn hmono)

/-- On six strands classical reading 3 leaves at least three cycles, so at most three merges
(two for an even permutation, `merges_even_of_sign_one`). -/
theorem six_strands_three_cycles (ℓ : Fin c → ℕ) (hn : ∑ i, ℓ i = 6)
    (hmono : ∀ k, k + 1 ≤ 6 / 2 → subsetSums ℓ k ≤ subsetSums ℓ (k + 1)) : 3 ≤ c := by
  have h := succ_le_two_pow_of_mono ℓ hn hmono
  by_contra hc
  interval_cases c <;> simp at h

end QOU.MassTheory.ClassicalReading3MergeBound
