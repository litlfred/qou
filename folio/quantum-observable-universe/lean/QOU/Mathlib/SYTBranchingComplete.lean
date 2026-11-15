import QOU.Mathlib.SYTBranchingRecursion
import QOU.Mathlib.SYTCornerListConnection

/-!
# QOU.Mathlib.SYTBranchingComplete — closing branching obligation (B) of `SYTBranchingRecursion`

`SYTBranchingRecursion.numSYTenum_eq_dimHLF_of_branchings` reduces the general hook-length formula
(hence `dimAitkenIdentity`) to two obligations:

* **(B)** `numSYTenum m = branchSum numSYTenum m` — the hard standard-tableau bijection;
* **(A)** `dimHLF m = branchSum dimHLF m` — the pure β-number Lagrange identity.

This file **discharges (B)** sorry-free, by transporting `SYTCornerListConnection.cornerRecursion_proof`
(`numSYTenum = ∑_{corners} numSYTenum ∘ removeCorner`, proved via the structural branching rule) onto the
scaffold's `decrementRow` / `removableCornerIdxs` / `branchSum` vocabulary.  The two presentations differ
only cosmetically: `decrementRow` keeps a vanished `0`-length row that `removeCorner` filters away, and
`numSYTenum` is invariant under that trailing zero (`numSYTenum_filter_eq`).

Only (A) — the β-Lagrange identity — remains for the general HLF.  Pure combinatorics on `ℕ`; nothing
archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (sz dimHLF)

/-- The scaffold's `removableCornerIdxs` is exactly the connection's `corners` (same predicate over the
same range — `IsCorner` adds only the `i < length` already guaranteed by `List.range`). -/
theorem removableCornerIdxs_eq_corners (l : List ℕ) : removableCornerIdxs l = corners l := by
  unfold removableCornerIdxs corners
  apply List.filter_congr
  intro i hi
  rw [List.mem_range] at hi
  rw [decide_eq_decide]
  unfold IsCorner
  exact ⟨fun h => ⟨hi, h⟩, fun h => h.2⟩

/-- `decrementRow` and `removeCorner` give the same standard-tableau count: they differ only by the
trailing `0`-length row that `removeCorner` filters, which leaves `numSYTenum` unchanged. -/
theorem numSYTenum_decrementRow (l : List ℕ) (i : ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hi : i ∈ removableCornerIdxs l) :
    numSYTenum (decrementRow l i) = numSYTenum (removeCorner l i) := by
  have heq : removeCorner l i = (decrementRow l i).filter (· != 0) := rfl
  rw [numSYTenum_filter_eq (decrementRow l i) (decrementRow_sorted hl hi), ← heq]

/-- **Branching obligation (B), discharged (sorry-free).** The brute-force standard-tableau count
satisfies the corner-removal recursion `numSYTenum m = ∑_{i corner} numSYTenum (m⁻ⁱ)` — the hard
bijection half of `numSYTenum_eq_dimHLF_of_branchings`.  Proved by transporting `cornerRecursion_proof`
onto the scaffold's `branchSum` vocabulary. -/
theorem numSYTenum_branching (m : List ℕ) (hm : List.Sorted (· ≥ ·) m) (hsz : 0 < sz m) :
    numSYTenum m = branchSum numSYTenum m := by
  rw [cornerRecursion_proof m hm hsz]
  unfold branchSum
  rw [removableCornerIdxs_eq_corners]
  apply congrArg List.sum
  apply List.map_congr_left
  intro i hi
  exact (numSYTenum_decrementRow m i hm (by rw [removableCornerIdxs_eq_corners]; exact hi)).symm

/-- **The general HLF, now reduced to the single β-Lagrange identity (A).** Plugging the proved (B)
`numSYTenum_branching` into the scaffold's composition leaves only (A) `dimHLF_branching` as a
hypothesis — `numSYTenum = dimHLF` for every sorted shape, conditional on (A) alone. -/
theorem numSYTenum_eq_dimHLF_of_dimHLF_branching
    (hA : ∀ m, List.Sorted (· ≥ ·) m → 0 < sz m → dimHLF m = branchSum dimHLF m)
    (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) : numSYTenum l = dimHLF l :=
  numSYTenum_eq_dimHLF_of_branchings numSYTenum_branching hA l hl

end QOU.Mathlib.SYTEnum
