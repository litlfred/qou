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
6. `subsetSums_cons` — adding a cycle of length `r` gives `a'_k = a_k + a_{k−r}` (`k ≥ r`).
7. `mono_of_binary`, `exists_mono_clog`, `max_merges_eq` — **sharpness**: for every `n` the
   positive cycle lengths `n + 1 − 2^d, 2^(d−1), …, 2, 1` (`2^d ≤ n < 2^(d+1)`, so
   `⌈log₂(n+1)⌉` cycles) satisfy the monotonicity hypothesis. The maximum merge count under
   classical top-level reading 3 is therefore exactly `n − ⌈log₂(n+1)⌉`.
8. `AllLevelsMono`, `clog_le_of_allLevels`, `exists_allLevels_clog` — the same statement with
   reading 3 imposed at every level `m ≤ n` (restricted cycle lengths `restrictLen`). The binary
   layout (points `0 | 1 2 | 3 4 5 6 | …`) satisfies it at every level, so the extra levels do
   not lower the maximum `n − ⌈log₂(n+1)⌉`. The restriction-to-level-`m` step (splicing out
   points `≥ m`) is modelled on cycle labels, not derived from `E_{n→m}`.

No empirical number appears in any statement.
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

theorem subsetSums_cons (r : ℕ) (ℓ : Fin c → ℕ) (k : ℕ) :
    subsetSums (Fin.cons r ℓ : Fin (c + 1) → ℕ) k =
      subsetSums ℓ k + if r ≤ k then subsetSums ℓ (k - r) else 0 := by
  classical
  set L : Fin (c + 1) → ℕ := Fin.cons r ℓ with hL
  let pre : Finset (Fin (c + 1)) → Finset (Fin c) := fun t => univ.filter fun i => i.succ ∈ t
  have hmap : ∀ s : Finset (Fin c), ∑ i ∈ s.map (Fin.succEmb c), L i = ∑ i ∈ s, ℓ i := by
    intro s; simp [L, Finset.sum_map]
  have hnot : ∀ s : Finset (Fin c), (0 : Fin (c + 1)) ∉ s.map (Fin.succEmb c) := by
    intro s; simp [Fin.succ_ne_zero]
  have hpre_map : ∀ s : Finset (Fin c), pre (s.map (Fin.succEmb c)) = s := by
    intro s; ext i; simp [pre]
  have hpre_ins : ∀ s : Finset (Fin c), pre (insert 0 (s.map (Fin.succEmb c))) = s := by
    intro s; ext i; simp [pre, Fin.succ_ne_zero]
  have herase : ∀ t : Finset (Fin (c + 1)), (pre t).map (Fin.succEmb c) = t.erase 0 := by
    intro t; ext j
    cases j using Fin.cases with
    | zero => simp [Fin.succ_ne_zero]
    | succ j => simp [pre, Fin.succ_ne_zero]
  have hsum_t : ∀ t : Finset (Fin (c + 1)), 0 ∈ t → ∑ i ∈ t, L i = r + ∑ i ∈ pre t, ℓ i := by
    intro t h0
    rw [← Finset.add_sum_erase t L h0, ← herase, hmap]; simp [L]
  have hsum_t' : ∀ t : Finset (Fin (c + 1)), 0 ∉ t → ∑ i ∈ t, L i = ∑ i ∈ pre t, ℓ i := by
    intro t h0
    rw [← hmap, herase, Finset.erase_eq_of_notMem h0]
  unfold subsetSums
  rw [← Finset.filter_card_add_filter_neg_card_eq_card (p := fun t : Finset (Fin (c + 1)) => 0 ∉ t),
    Finset.filter_filter, Finset.filter_filter]
  congr 1
  · refine Finset.card_nbij' (fun t => pre t) (fun s => s.map (Fin.succEmb c)) ?_ ?_ ?_ ?_
    · intro t ht
      simp only [coe_filter, mem_univ, true_and, Set.mem_setOf_eq] at ht ⊢
      rw [← hsum_t' t ht.2]; exact ht.1
    · intro s hs
      simp only [coe_filter, mem_univ, true_and, Set.mem_setOf_eq] at hs ⊢
      exact ⟨by rw [hmap]; exact hs, hnot s⟩
    · intro t ht
      simp only [coe_filter, mem_univ, true_and, Set.mem_setOf_eq] at ht
      dsimp only
      rw [herase, Finset.erase_eq_of_notMem ht.2]
    · intro s _; exact hpre_map s
  · split_ifs with hr
    · refine Finset.card_nbij' (fun t => pre t) (fun s => insert 0 (s.map (Fin.succEmb c)))
        ?_ ?_ ?_ ?_
      · intro t ht
        simp only [coe_filter, mem_univ, true_and, Set.mem_setOf_eq, not_not] at ht ⊢
        have := hsum_t t ht.2; omega
      · intro s hs
        simp only [coe_filter, mem_univ, true_and, Set.mem_setOf_eq, not_not] at hs ⊢
        refine ⟨?_, Finset.mem_insert_self _ _⟩
        rw [Finset.sum_insert (hnot s), hmap]; simp [L]; omega
      · intro t ht
        simp only [coe_filter, mem_univ, true_and, Set.mem_setOf_eq, not_not] at ht
        dsimp only
        rw [herase, Finset.insert_erase ht.2]
      · intro s _; exact hpre_ins s
    · rw [Finset.card_eq_zero, Finset.filter_eq_empty_iff]
      intro t _ ⟨hk, h0⟩
      rw [not_not] at h0
      have := hsum_t t h0; omega

/-- Binary cycle lengths `2^(d-1), …, 2, 1` (index `0` carries the largest). -/
def binLen : (d : ℕ) → Fin d → ℕ
  | 0 => Fin.elim0
  | d + 1 => Fin.cons (2 ^ d) (binLen d)

theorem binLen_pos : ∀ (d : ℕ) (i : Fin d), 1 ≤ binLen d i
  | 0, i => i.elim0
  | d + 1, i => by
    cases i using Fin.cases with
    | zero => simp [binLen, Nat.one_le_two_pow]
    | succ j => simpa [binLen] using binLen_pos d j

theorem sum_binLen : ∀ d : ℕ, ∑ i, binLen d i = 2 ^ d - 1
  | 0 => by simp
  | d + 1 => by
    simp only [binLen, Fin.sum_cons, sum_binLen d, pow_succ]
    have := Nat.one_le_two_pow (n := d)
    omega

theorem subsetSums_binLen : ∀ (d k : ℕ), subsetSums (binLen d) k = if k < 2 ^ d then 1 else 0
  | 0, k => by
    unfold subsetSums
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · simp
    · simp [Nat.lt_one_iff, hk.ne', Finset.sum_of_isEmpty]; omega
  | d + 1, k => by
    simp only [binLen]
    rw [subsetSums_cons, subsetSums_binLen d, subsetSums_binLen d, pow_succ]
    split_ifs <;> omega

/-- **Attainment.** For `2^d ≤ n < 2^(d+1)` the cycle lengths `n + 1 − 2^d, 2^(d−1), …, 2, 1`
(`d + 1` positive lengths summing to `n`) satisfy the monotonicity hypothesis of
`succ_le_two_pow_of_mono`. -/
theorem mono_of_binary (d n : ℕ) (hlo : 2 ^ d ≤ n) (hhi : n < 2 ^ (d + 1)) :
    (∀ i, 1 ≤ (Fin.cons (n + 1 - 2 ^ d) (binLen d) : Fin (d + 1) → ℕ) i) ∧
      ∑ i, (Fin.cons (n + 1 - 2 ^ d) (binLen d) : Fin (d + 1) → ℕ) i = n ∧
      ∀ k, k + 1 ≤ n / 2 →
        subsetSums (Fin.cons (n + 1 - 2 ^ d) (binLen d) : Fin (d + 1) → ℕ) k ≤
          subsetSums (Fin.cons (n + 1 - 2 ^ d) (binLen d) : Fin (d + 1) → ℕ) (k + 1) := by
  have h1 := Nat.one_le_two_pow (n := d)
  rw [pow_succ] at hhi
  refine ⟨?_, ?_, ?_⟩
  · intro i
    cases i using Fin.cases with
    | zero => simp only [Fin.cons_zero]; omega
    | succ j => simpa using binLen_pos d j
  · rw [Fin.sum_cons, sum_binLen]; omega
  · intro k hk
    rw [subsetSums_cons, subsetSums_cons, subsetSums_binLen, subsetSums_binLen,
      subsetSums_binLen, subsetSums_binLen]
    have : n / 2 < 2 ^ d := by omega
    split_ifs <;> omega

/-- The bound of `succ_le_two_pow_of_mono` in `clog` form: `⌈log₂(n+1)⌉ ≤ c`. -/
theorem clog_le_of_mono (ℓ : Fin c → ℕ) {n : ℕ} (hn : ∑ i, ℓ i = n)
    (hmono : ∀ k, k + 1 ≤ n / 2 → subsetSums ℓ k ≤ subsetSums ℓ (k + 1)) :
    Nat.clog 2 (n + 1) ≤ c :=
  (Nat.clog_le_iff_le_pow (by norm_num)).2 (succ_le_two_pow_of_mono ℓ hn hmono)

/-- **Sharpness.** For every `n` there are `⌈log₂(n+1)⌉` positive cycle lengths summing to `n`
that satisfy classical top-level reading 3, so `n − ⌈log₂(n+1)⌉` merges is attained. -/
theorem exists_mono_clog (n : ℕ) :
    ∃ ℓ : Fin (Nat.clog 2 (n + 1)) → ℕ, (∀ i, 1 ≤ ℓ i) ∧ ∑ i, ℓ i = n ∧
      ∀ k, k + 1 ≤ n / 2 → subsetSums ℓ k ≤ subsetSums ℓ (k + 1) := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · rw [show Nat.clog 2 (0 + 1) = 0 by simp]
    exact ⟨Fin.elim0, fun i => i.elim0, by simp, fun k hk => by omega⟩
  · obtain ⟨d, hd⟩ : ∃ d, Nat.clog 2 (n + 1) = d + 1 :=
      ⟨_, (Nat.succ_pred_eq_of_pos (Nat.clog_pos (by norm_num) (by omega))).symm⟩
    have h1 := Nat.le_pow_clog (b := 2) (by norm_num) (n + 1)
    have h2 := Nat.pow_pred_clog_lt_self (b := 2) (by norm_num) (x := n + 1) (by omega)
    rw [hd] at h1 h2 ⊢
    simp only [Nat.pred_succ] at h2
    exact ⟨_, mono_of_binary d n (by omega) (by omega)⟩

/-- **The maximum merge count under classical top-level reading 3 is `n − ⌈log₂(n+1)⌉`.**
Every admissible cycle type merges at most that many, and some admissible cycle type with
positive lengths merges exactly that many. -/
theorem max_merges_eq (n : ℕ) :
    (∀ (c : ℕ) (ℓ : Fin c → ℕ), ∑ i, ℓ i = n →
        (∀ k, k + 1 ≤ n / 2 → subsetSums ℓ k ≤ subsetSums ℓ (k + 1)) →
        n - c ≤ n - Nat.clog 2 (n + 1)) ∧
      ∃ ℓ : Fin (Nat.clog 2 (n + 1)) → ℕ, (∀ i, 1 ≤ ℓ i) ∧ ∑ i, ℓ i = n ∧
        ∀ k, k + 1 ≤ n / 2 → subsetSums ℓ k ≤ subsetSums ℓ (k + 1) :=
  ⟨fun _ ℓ hn hmono => Nat.sub_le_sub_left (clog_le_of_mono ℓ hn hmono) n, exists_mono_clog n⟩

/-! ## All levels

`E_{n→m}` at `q = 1` sends a permutation to a positive multiple of the permutation of the
first `m` points obtained by splicing out the others; its cycles are the cycles of `σ`
intersected with `{0,…,m−1}` (the non-empty ones). With `f p` the cycle containing point `p`,
the restricted cycle lengths are `restrictLen f m`. A label with no point below `m` gives a
zero entry, which doubles every `a_k` (`subsetSums_cons_zero`) and so leaves the monotonicity
unchanged. All-levels classical reading 3 is `AllLevelsMono f n`. The character bridge is the
same cited step as above (-- Ref: [sagan2001] Thm 2.11.2) and is not formalised. -/

theorem subsetSums_cons_zero (ℓ : Fin c → ℕ) (k : ℕ) :
    subsetSums (Fin.cons 0 ℓ : Fin (c + 1) → ℕ) k = 2 * subsetSums ℓ k := by
  rw [subsetSums_cons]; simp; omega

/-- Restricted cycle lengths: the number of points below `m` in each cycle. -/
def restrictLen (f : ℕ → Fin c) (m : ℕ) (i : Fin c) : ℕ :=
  #((range m).filter fun p => f p = i)

/-- Classical reading 3 at every level `m ≤ n`. -/
def AllLevelsMono (f : ℕ → Fin c) (n : ℕ) : Prop :=
  ∀ m ≤ n, ∀ k, k + 1 ≤ m / 2 →
    subsetSums (restrictLen f m) k ≤ subsetSums (restrictLen f m) (k + 1)

theorem sum_restrictLen (f : ℕ → Fin c) (m : ℕ) : ∑ i, restrictLen f m i = m := by
  unfold restrictLen
  rw [← Finset.card_eq_sum_card_fiberwise (fun _ _ => mem_univ _), card_range]

/-- All levels contain the top level, so the bound `⌈log₂(n+1)⌉ ≤ c` still holds. -/
theorem clog_le_of_allLevels (f : ℕ → Fin c) {n : ℕ} (h : AllLevelsMono f n) :
    Nat.clog 2 (n + 1) ≤ c :=
  clog_le_of_mono (restrictLen f n) (sum_restrictLen f n) (h n le_rfl)

/-- Binary layout: points `0, 1–2, 3–6, …` fill cycles of lengths `1, 2, 4, …`, and the
points from `2^D − 1` on go to label `0`. -/
def binLayout : (D : ℕ) → ℕ → Fin (D + 1)
  | 0 => fun _ => 0
  | D + 1 => fun p => if p < 2 ^ (D + 1) - 1 then (binLayout D p).succ else 0

theorem restrictLen_binLayout_zero (m : ℕ) : restrictLen (binLayout 0) m = fun _ => m := by
  funext i
  have hi : i = 0 := Fin.fin_one_eq_zero i
  subst hi
  simp [restrictLen, binLayout]

theorem restrictLen_binLayout_succ (D m : ℕ) :
    restrictLen (binLayout (D + 1)) m =
      Fin.cons (m - min m (2 ^ (D + 1) - 1))
        (restrictLen (binLayout D) (min m (2 ^ (D + 1) - 1))) := by
  funext i
  cases i using Fin.cases with
  | zero =>
    simp only [restrictLen, Fin.cons_zero]
    rw [show ((range m).filter fun p => binLayout (D + 1) p = 0) =
        Finset.Ico (min m (2 ^ (D + 1) - 1)) m by
      ext p
      simp only [mem_filter, mem_range, mem_Ico, binLayout]
      split_ifs with h
      · simp only [Fin.succ_ne_zero, and_false, false_iff]; omega
      · simp only [and_true]; omega]
    simp
  | succ j =>
    simp only [restrictLen, Fin.cons_succ]
    congr 1
    ext p
    simp only [mem_filter, mem_range, binLayout]
    split_ifs with h
    · simp only [Fin.succ_inj]
      constructor
      · rintro ⟨h1, h2⟩; exact ⟨by omega, h2⟩
      · rintro ⟨h1, h2⟩; exact ⟨by omega, h2⟩
    · simp only [(Fin.succ_ne_zero j).symm, and_false, false_iff]
      omega

theorem restrictLen_binLayout_full : ∀ D : ℕ,
    restrictLen (binLayout D) (2 ^ (D + 1) - 1) = binLen (D + 1)
  | 0 => by
    rw [restrictLen_binLayout_zero]
    funext i
    have hi : i = 0 := Fin.fin_one_eq_zero i
    subst hi
    simp [binLen]
  | D + 1 => by
    rw [restrictLen_binLayout_succ, show min (2 ^ (D + 1 + 1) - 1) (2 ^ (D + 1) - 1) =
      2 ^ (D + 1) - 1 by rw [pow_succ 2 (D + 1)]; omega, restrictLen_binLayout_full D]
    conv_rhs => rw [binLen]
    congr 1
    rw [pow_succ 2 (D + 1)]
    have := Nat.one_le_two_pow (n := D + 1)
    omega

/-- The binary layout satisfies classical reading 3 at every level `m ≤ 2^(D+1) − 1`. -/
theorem allLevelsMono_binLayout : ∀ D : ℕ, AllLevelsMono (binLayout D) (2 ^ (D + 1) - 1)
  | 0 => by
    intro m hm k hk
    simp at hm
    omega
  | D + 1 => by
    intro m hm k hk
    have hp := pow_succ 2 (D + 1)
    have h1 := Nat.one_le_two_pow (n := D + 1)
    rw [restrictLen_binLayout_succ]
    by_cases hlow : m ≤ 2 ^ (D + 1) - 1
    · rw [show min m (2 ^ (D + 1) - 1) = m from min_eq_left hlow,
        show m - m = 0 from Nat.sub_self m, subsetSums_cons_zero, subsetSums_cons_zero]
      exact Nat.mul_le_mul_left 2 (allLevelsMono_binLayout D m hlow k hk)
    · rw [show min m (2 ^ (D + 1) - 1) = 2 ^ (D + 1) - 1 by omega,
        restrictLen_binLayout_full D,
        show m - (2 ^ (D + 1) - 1) = m + 1 - 2 ^ (D + 1) by omega]
      exact (mono_of_binary (D + 1) m (by omega) (by omega)).2.2 k hk

/-- At its top level every label of the binary layout is a non-empty cycle. -/
theorem restrictLen_binLayout_pos (D n : ℕ) (hlo : 2 ^ D ≤ n) (hhi : n < 2 ^ (D + 1)) (i) :
    1 ≤ restrictLen (binLayout D) n i := by
  cases D with
  | zero =>
    rw [restrictLen_binLayout_zero]; simp at hlo; exact hlo
  | succ E =>
    have hp := pow_succ 2 (E + 1)
    have hp' := pow_succ 2 E
    have h1 := Nat.one_le_two_pow (n := E)
    rw [restrictLen_binLayout_succ, show min n (2 ^ (E + 1) - 1) = 2 ^ (E + 1) - 1 by omega,
      restrictLen_binLayout_full E, show n - (2 ^ (E + 1) - 1) = n + 1 - 2 ^ (E + 1) by omega]
    exact (mono_of_binary (E + 1) n hlo hhi).1 i

/-- **All-levels sharpness.** For every `n ≥ 1` there is a labelling of `n` points by
`⌈log₂(n+1)⌉` non-empty cycles that satisfies classical reading 3 at every level `m ≤ n`.
With `clog_le_of_allLevels`, the all-levels condition has the same maximum merge count
`n − ⌈log₂(n+1)⌉` as the top-level condition. -/
theorem exists_allLevels_clog (n : ℕ) (hn : 1 ≤ n) :
    ∃ f : ℕ → Fin (Nat.clog 2 (n + 1)), AllLevelsMono f n ∧
      ∀ i, 1 ≤ restrictLen f n i := by
  obtain ⟨d, hd⟩ : ∃ d, Nat.clog 2 (n + 1) = d + 1 :=
    ⟨_, (Nat.succ_pred_eq_of_pos (Nat.clog_pos (by norm_num) (by omega))).symm⟩
  have h1 := Nat.le_pow_clog (b := 2) (by norm_num) (n + 1)
  have h2 := Nat.pow_pred_clog_lt_self (b := 2) (by norm_num) (x := n + 1) (by omega)
  rw [hd] at h1 h2 ⊢
  simp only [Nat.pred_succ] at h2
  refine ⟨binLayout d, fun m hm => allLevelsMono_binLayout d m (by omega), ?_⟩
  exact restrictLen_binLayout_pos d n (by omega) (by omega)

end QOU.MassTheory.ClassicalReading3MergeBound
