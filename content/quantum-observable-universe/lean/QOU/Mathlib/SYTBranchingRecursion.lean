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

open QOU.BraidKnot.IdentityI (dimHLF)

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
