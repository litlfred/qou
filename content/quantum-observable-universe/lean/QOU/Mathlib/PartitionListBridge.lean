import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Data.Multiset.Sort
import Mathlib.Data.List.Sort

/-!
# QOU.Mathlib.PartitionListBridge — `Nat.Partition n` ↔ the weakly-decreasing `List ℕ` model

The Identity I combinatorics (`QOU.BraidKnot.IdentityI`, the keystone `W_λ` defect input) is
developed over a **computable model** of a partition: a weakly-decreasing `List ℕ` of positive
parts summing to `n` (so `decide` can run over `allPartsLE9` etc.).  Mathlib's abstract index for
the same object is `Nat.Partition n` (a `Multiset ℕ` of positive parts with `parts_sum = n`).

The general-`n` discharge of Identity I's two `PlancherelSnData` axioms (the
`docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md` program, phase **P5**) must
bridge these two indices — e.g. to push the `RSKBridge`/regular-representation
`∑_{Λ : Nat.Partition n} dim(Λ)² = n!` (axiom (i)) onto the `List ℕ`-model `dimHLF` the per-`n`
instances use, and to range an abstract `∑_{Λ}` over the concrete sorted lists.

This file builds that bridge **sorry-free**, over core Mathlib only (no representation theory, no
hook-length formula — those are the genuinely Mathlib-absent pieces of the program):

* `toList`  — `Nat.Partition n → List ℕ`, the parts sorted weakly-decreasing;
* `toList_sorted` / `toList_pos` / `toList_sum` / `toList_coe` — it lands in the model;
* `ofList`  — the inverse on a valid (sorted-or-not, positive, size-`n`) list;
* `equivSortedList` — the resulting `Equiv` `Nat.Partition n ≃ {l // weakly-decreasing ∧ pos ∧ sum = n}`.

Base ring is irrelevant (pure combinatorics on `ℕ`); nothing archimedean.
-/

namespace QOU.Mathlib.PartitionListBridge

open Nat

variable {n : ℕ}

/-- The weakly-decreasing list of parts of a `Nat.Partition n`. -/
def toList (p : Nat.Partition n) : List ℕ := p.parts.sort (· ≥ ·)

/-- `toList p` is weakly decreasing — the hypothesis the Identity I `(A)` proof consumes
(`l.Sorted (· ≥ ·)`). -/
theorem toList_sorted (p : Nat.Partition n) : (toList p).Sorted (· ≥ ·) :=
  Multiset.sort_sorted _ _

/-- `toList p` carries exactly the parts multiset (sorting forgets nothing). -/
theorem toList_coe (p : Nat.Partition n) : (toList p : Multiset ℕ) = p.parts :=
  Multiset.sort_eq _ _

/-- Membership in `toList p` is membership in the parts. -/
theorem mem_toList {p : Nat.Partition n} {a : ℕ} : a ∈ toList p ↔ a ∈ p.parts := by
  rw [← Multiset.mem_coe, toList_coe]

/-- Every entry of `toList p` is positive (a genuine partition has positive parts). -/
theorem toList_pos (p : Nat.Partition n) : ∀ a ∈ toList p, 0 < a :=
  fun _a ha => p.parts_pos (mem_toList.mp ha)

/-- `toList p` sums to `n`. -/
theorem toList_sum (p : Nat.Partition n) : (toList p).sum = n := by
  have h : ((toList p : Multiset ℕ)).sum = p.parts.sum := by rw [toList_coe]
  rwa [Multiset.sum_coe, p.parts_sum] at h

/-- Build a `Nat.Partition n` from any list of positive parts summing to `n` (order ignored). -/
def ofList (l : List ℕ) (hpos : ∀ a ∈ l, 0 < a) (hsum : l.sum = n) : Nat.Partition n where
  parts := (l : Multiset ℕ)
  parts_pos := by intro a ha; exact hpos a (Multiset.mem_coe.mp ha)
  parts_sum := by simpa using hsum

@[simp] theorem ofList_parts (l : List ℕ) (hpos : ∀ a ∈ l, 0 < a) (hsum : l.sum = n) :
    (ofList l hpos hsum).parts = (l : Multiset ℕ) := rfl

/-- **Round trip I** — `ofList (toList p) … = p`.  Partitions are determined by their parts
multiset, and `toList` preserves it (`toList_coe`). -/
theorem ofList_toList (p : Nat.Partition n)
    (hpos : ∀ a ∈ toList p, 0 < a) (hsum : (toList p).sum = n) :
    ofList (toList p) hpos hsum = p := by
  apply Nat.Partition.ext
  simp [ofList, toList_coe]

/-- **Round trip II** — `toList (ofList l …) = l` when `l` is already weakly decreasing.  Both
sides are weakly-decreasing lists with the same underlying multiset, hence equal
(`List.eq_of_perm_of_sorted`, using antisymmetry of `· ≥ ·` on `ℕ`). -/
theorem toList_ofList (l : List ℕ) (hpos : ∀ a ∈ l, 0 < a) (hsum : l.sum = n)
    (hsorted : l.Sorted (· ≥ ·)) :
    toList (ofList l hpos hsum) = l := by
  have hperm : (toList (ofList l hpos hsum)).Perm l := by
    rw [← Multiset.coe_eq_coe, toList_coe]; rfl
  exact List.eq_of_perm_of_sorted hperm (toList_sorted _) hsorted

/-- **The bridge `Equiv`** — `Nat.Partition n ≃ {weakly-decreasing positive lists summing to n}`.
The right-hand subtype is precisely the computable model the Identity I combinatorics range over,
so an abstract `∑_{Λ : Nat.Partition n}` transports to a sum over the sorted-list model and back. -/
def equivSortedList (n : ℕ) :
    Nat.Partition n ≃ {l : List ℕ // l.Sorted (· ≥ ·) ∧ (∀ a ∈ l, 0 < a) ∧ l.sum = n} where
  toFun p := ⟨toList p, toList_sorted p, toList_pos p, toList_sum p⟩
  invFun l := ofList l.1 l.2.2.1 l.2.2.2
  left_inv p := ofList_toList p (toList_pos p) (toList_sum p)
  right_inv l := by
    apply Subtype.ext
    exact toList_ofList l.1 l.2.2.1 l.2.2.2 l.2.1

end QOU.Mathlib.PartitionListBridge
