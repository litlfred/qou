import QOU.Mathlib.SYTEnumeration

/-!
# QOU.Mathlib.SYTBranchingRecursion — step 1 of closing `dimAitkenIdentity`

The general-`n` hook-length formula `numSYTenum = dimHLF` is isolated to the single cited sorry
`SYTHookFormulaGeneral.dimAitkenIdentity`.  The route to closing it (scoped in
`docs/workplans/2026-06-28-syt-hlf-branching-bijection-scope.md`) is the **corner-removal branching
recursion**: both the brute-force count and the closed form satisfy

    F(λ)  =  Σ_{i a removable corner of λ}  F(λ⁻ⁱ),        F ∈ {numSYTenum, dimHLF}.

This file lands **step 1**: the corner-removal combinators and the *exact, sorry-free, `decide`-verified*
branching identities for small `n`.  They serve two purposes:

* they **pin the precise statements** the eventual general lemmas
  (`numSYTenum_branching` (B) — the hard bijection — and `dimHLF_branching` (A) — pure β-algebra) must
  prove, removing any ambiguity in the off-by-one corner bookkeeping; and
* they are a **regression backstop**: any future general proof must agree with these on `n ≤ 5`.

No new `sorry` is introduced — per the net-sorry discipline in the scope doc, the general statements
(A)/(B) are added only when (A) is provable sorry-free.  Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (dimHLF sz prodHooks)

/-- Remove one cell from row `i`: decrement `l[i]` by `1` (a trailing `0` row is harmless — `chunk`
gives it `0` cells, `prodHooks` an empty product, `sz` an unchanged sum). -/
def decrementRow (l : List ℕ) (i : ℕ) : List ℕ := l.set i (l.getD i 0 - 1)

/-- The removable-corner row indices of `l`: rows strictly longer than the row below
(`l.getD (i+1) 0 = 0` when there is no row below, so the last nonzero row always qualifies). -/
def removableCornerIdxs (l : List ℕ) : List ℕ :=
  (List.range l.length).filter (fun i => l.getD (i + 1) 0 < l.getD i 0)

/-- The branching sum `Σ_{i corner} F(λ⁻ⁱ)` for a count-valued `F`. -/
def branchSum (F : List ℕ → ℕ) (l : List ℕ) : ℕ :=
  ((removableCornerIdxs l).map (fun i => F (decrementRow l i))).sum

/-! ### Foundation lemmas (sorry-free)

Structural facts the eventual general (A)/(B) proofs and their strong induction need: the size
decreases by exactly one under a corner removal, and that decrease is strict — the well-founded
termination measure for the branching recursion. -/

/-- Each row length is bounded by the total size. -/
theorem getD_le_sz (l : List ℕ) (i : ℕ) (h : i < l.length) : l.getD i 0 ≤ sz l := by
  unfold sz
  have hgd : l.getD i 0 = l[i] := by
    simp [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h]
  have hself : l.set i (l.getD i 0) = l := by rw [hgd]; simp
  have hs := List.sum_set l i (l.getD i 0)
  rw [hself] at hs; simp only [h, if_true] at hs; omega

/-- **Removing a cell drops the size by exactly one.** `sz (decrementRow l i) = sz l - 1` for any
in-range positive row `i`. -/
theorem sz_decrementRow (l : List ℕ) (i : ℕ) (h : i < l.length) (hpos : 0 < l.getD i 0) :
    sz (decrementRow l i) = sz l - 1 := by
  unfold sz decrementRow
  have hgd : l.getD i 0 = l[i] := by
    simp [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h]
  have hself : l.set i (l.getD i 0) = l := by rw [hgd]; simp
  have hsum : (l.take i).sum + l.getD i 0 + (l.drop (i + 1)).sum = l.sum := by
    have hs := List.sum_set l i (l.getD i 0)
    rw [hself] at hs; simp only [h, if_true] at hs; omega
  rw [List.sum_set]; simp only [h, if_true]; omega

/-- Membership in `removableCornerIdxs`: in range, and strictly longer than the row below. -/
theorem mem_removableCornerIdxs {l : List ℕ} {i : ℕ} :
    i ∈ removableCornerIdxs l ↔ i < l.length ∧ l.getD (i + 1) 0 < l.getD i 0 := by
  unfold removableCornerIdxs
  simp [List.mem_filter, List.mem_range]

/-- **The branching recursion is well-founded.** Every corner-removed shape is strictly smaller —
the termination measure (`sz`) for the strong induction that will compose (A)+(B) into the HLF. -/
theorem sz_decrementRow_lt {l : List ℕ} {i : ℕ} (hi : i ∈ removableCornerIdxs l) :
    sz (decrementRow l i) < sz l := by
  rw [mem_removableCornerIdxs] at hi
  obtain ⟨hlen, hgt⟩ := hi
  have hpos : 0 < l.getD i 0 := lt_of_le_of_lt (Nat.zero_le _) hgt
  have hle := getD_le_sz l i hlen
  rw [sz_decrementRow l i hlen hpos]; omega

/-- **Corner removal preserves the partition shape.** Decrementing a removable corner keeps the row
lengths weakly decreasing — the invariant the strong-induction hypotheses are stated over. -/
theorem decrementRow_sorted {l : List ℕ} {i : ℕ} (hl : List.Sorted (· ≥ ·) l)
    (hi : i ∈ removableCornerIdxs l) : List.Sorted (· ≥ ·) (decrementRow l i) := by
  rw [mem_removableCornerIdxs] at hi
  obtain ⟨hlen, hgt⟩ := hi
  have hgdi : l.getD i 0 = l[i] := by
    simp [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hlen]
  rw [List.Sorted, List.pairwise_iff_getElem] at hl
  have hcorner : ∀ c (hc : c < l.length), i < c → l[i] > l[c] := by
    intro c hc hic
    have hi1 : i + 1 < l.length := by omega
    have hgd1 : l.getD (i + 1) 0 = l[i + 1] := by
      simp [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi1]
    have hstep := hgt
    rw [hgdi, hgd1] at hstep
    rcases Nat.lt_or_ge (i + 1) c with h1 | h1
    · exact lt_of_le_of_lt (hl (i + 1) c hi1 hc h1) hstep
    · have hc' : c = i + 1 := by omega
      subst hc'; exact hstep
  rw [decrementRow, List.Sorted, List.pairwise_iff_getElem]
  intro a b ha hb hab
  rw [List.length_set] at ha hb
  simp only [List.getElem_set]
  by_cases hai : i = a
  · rw [if_pos hai]
    by_cases hbi : i = b
    · rw [if_pos hbi]
    · rw [if_neg hbi]
      have hcb := hcorner b hb (by omega)
      omega
  · rw [if_neg hai]
    by_cases hbi : i = b
    · rw [if_pos hbi]
      have hac := hl a i ha hlen (by omega)
      omega
    · rw [if_neg hbi]
      exact hl a b ha hb hab

/-! ### Base case + composition (sorry-free)

The strong-induction base (`sz = 0`) and the reduction of the whole hook-length formula to the two
branching obligations.  No new `sorry`: `numSYTenum_eq_dimHLF_of_branchings` is *conditional* on (A)
`dimHLF` branching and (B) `numSYTenum` branching as explicit hypotheses (per the net-sorry discipline
in bean `sy7b` — the general (A)/(B) are added only when (A) is proved sorry-free). -/

/-- `chunk l []` is all-empty rows: the empty filling laid out on shape `l`. -/
theorem chunk_nil : ∀ l : List ℕ, chunk l [] = List.replicate l.length [] := by
  intro l; induction l with
  | nil => rfl
  | cons a t ih => simp [chunk, ih, List.replicate_succ]

/-- Columns of an all-empty layout are trivially strictly increasing. -/
theorem colsOK_replicate_nil : ∀ k, colsOK (List.replicate k ([] : List ℕ)) = true
  | 0 => rfl
  | 1 => rfl
  | (k + 2) => by
      show colsOK ([] :: [] :: List.replicate k []) = true
      simp only [colsOK, List.zip_nil_right, List.all_nil, Bool.true_and]
      exact colsOK_replicate_nil (k + 1)

/-- **Base count.** The empty shape (`sz l = 0`) has exactly one standard tableau. -/
theorem numSYTenum_sz_zero (l : List ℕ) (h : sz l = 0) : numSYTenum l = 1 := by
  unfold numSYTenum
  have hs : l.sum = 0 := h
  rw [hs]
  simp only [List.range_zero, List.map_nil, allPerms, List.countP_cons, List.countP_nil]
  unfold isStdFilling
  rw [chunk_nil]
  simp [strictInc, colsOK_replicate_nil]

/-- The hook product of the empty shape is `1`. -/
theorem prodHooks_sz_zero (l : List ℕ) (h : sz l = 0) : prodHooks l = 1 := by
  have hz : ∀ x ∈ l, x = 0 := by
    have := (List.sum_eq_zero_iff (l := l)).1 h; intro x hx; exact this x hx
  unfold prodHooks
  apply List.prod_eq_one
  intro x hx
  simp only [List.mem_map, List.mem_range] at hx
  obtain ⟨i, hi, rfl⟩ := hx
  have hgi : l.getD i 0 = 0 := by
    rcases Nat.lt_or_ge i l.length with h1 | h1
    · rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h1]
      exact hz l[i] (List.getElem_mem h1)
    · rw [List.getD_eq_getElem?_getD, List.getElem?_eq_none h1]; rfl
  rw [hgi]; simp

/-- **Base dimension.** `dimHLF` of the empty shape is `1`. -/
theorem dimHLF_sz_zero (l : List ℕ) (h : sz l = 0) : dimHLF l = 1 := by
  unfold dimHLF; rw [h, prodHooks_sz_zero l h]; simp

/-- **Composition: the hook-length formula from the two branching recursions (sorry-free).**
Given that both the brute-force count (B) and the closed form (A) satisfy the corner-removal
recursion on every positive-size sorted shape, `numSYTenum = dimHLF` for **all** sorted shapes — by
strong induction on `sz`, with `sz_decrementRow_lt` the termination measure and `sz = 0` the base.
This reduces the general-`n` hook-length formula (hence `dimAitkenIdentity`) to exactly (A) + (B). -/
theorem numSYTenum_eq_dimHLF_of_branchings
    (hB : ∀ m, List.Sorted (· ≥ ·) m → 0 < sz m → numSYTenum m = branchSum numSYTenum m)
    (hA : ∀ m, List.Sorted (· ≥ ·) m → 0 < sz m → dimHLF m = branchSum dimHLF m)
    (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) : numSYTenum l = dimHLF l := by
  suffices H : ∀ n l, sz l = n → List.Sorted (· ≥ ·) l → numSYTenum l = dimHLF l from
    H (sz l) l rfl hl
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro l hn hl
    rcases Nat.eq_zero_or_pos n with h0 | hpos
    · subst h0
      rw [numSYTenum_sz_zero l hn, dimHLF_sz_zero l hn]
    · rw [hB l hl (by omega), hA l hl (by omega)]
      unfold branchSum
      apply congrArg List.sum
      apply List.map_congr_left
      intro i hi
      have h2 := sz_decrementRow_lt hi
      exact ih _ (by omega) (decrementRow l i) rfl (decrementRow_sorted hl hi)

/-- **(B) branching, `decide`-verified for `n ≤ 4` (sorry-free).** The brute-force `#SYT` satisfies the
corner-removal recursion `numSYTenum λ = Σ_{i corner} numSYTenum(λ⁻ⁱ)`.  The decide-pinned target for
the eventual general `numSYTenum_branching`. -/
theorem numSYTenum_branching_le4 :
    ∀ l ∈ shapesLE4, numSYTenum l = branchSum numSYTenum l := by decide

/-- **(B) branching, `decide`-verified for `n = 5` (sorry-free).** -/
theorem numSYTenum_branching_5 :
    ∀ l ∈ shapes5, numSYTenum l = branchSum numSYTenum l := by decide

/-- **(A) branching, `decide`-verified for `n ≤ 4` (sorry-free).** The Frame–Robinson–Thrall closed
form satisfies the same recursion `dimHLF λ = Σ_{i corner} dimHLF(λ⁻ⁱ)`.  The decide-pinned target for
the eventual general `dimHLF_branching` (the pure β-number Lagrange identity). -/
theorem dimHLF_branching_le4 :
    ∀ l ∈ shapesLE4, dimHLF l = branchSum dimHLF l := by decide

/-- **(A) branching, `decide`-verified for `n = 5` (sorry-free).** -/
theorem dimHLF_branching_5 :
    ∀ l ∈ shapes5, dimHLF l = branchSum dimHLF l := by decide

end QOU.Mathlib.SYTEnum
