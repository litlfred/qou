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

open QOU.BraidKnot.IdentityI (dimHLF sz)

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
