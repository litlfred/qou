import QOU.BraidKnot.DeltaLambdaSignRule
import Mathlib.Combinatorics.Enumerative.Partition

/-!
# QOU.BraidKnot.PartitionNatBridge — custom `Partition n` ≃ `Nat.Partition n`

`DeltaLambdaSignRule.Partition n` (a **sorted list** of positive parts summing to `n`) and
Mathlib's `Nat.Partition n` (a **multiset** of positive parts summing to `n`) carry the same
data: a `(· ≥ ·)`-sorted list is determined by its underlying multiset, and any multiset sorts
to a unique weakly-decreasing list. `partitionEquivNatPartition` makes this an `Equiv`.

This is the missing **encoding bridge** for the Burnside reindexing
(`DeltaLambdaSignRule.burnside`, `Σ_λ (f^λ)² = n!`). Composed with
`SpechtClassification.partitionEquivYoungIndex` (`Nat.Partition n ≃ PartitionIndex n`) it yields
`Partition n ≃ PartitionIndex n`, the reindexing over which the SYT sum-of-squares
`OVTopAssembly.sum_numSYT_sq_eq_factorial` (`Σ_i (#SYT i.diagram)² = n!`) is stated. The remaining
steps to discharge `burnside` are the `List`-complete/`Nodup` ↔ `Finset.univ` sum transport along
this equiv, and the hook-length bridge `dimIrrep = numSYT` (see the `burnside` roadmap comment).

Construction mirrors `SpechtClassification.partitionEquivYoungIndex` (same `Multiset.sort`
round-trip: `Multiset.sort_eq`, `List.mergeSort_eq_self` on an already-sorted list).

-- Ref: [sagan2001] Sagan, The Symmetric Group (partitions as sorted lists / multisets)
-/

open scoped BigOperators

namespace QOU.BraidKnot.PartitionNatBridge

open DeltaLambdaSignRule

/-- Two custom partitions with equal `parts` lists are equal (the other three fields are
`Prop`s, so proof-irrelevant).

The `Partition.` prefix here is **not** a namespace component — it is the *type* name, which
is what lets `QOU.BraidKnot.PartitionReindex` call this as
`PartitionNatBridge.Partition.ext'`. The LWC-2 namespace sweep (`22728b8801`) stripped it,
which broke both call sites in `PartitionReindex` and the `apply` below; restored here.

The proof now delegates to `DeltaLambdaSignRule.Partition.ext`, the `@[ext]` lemma that lives
with the structure itself. This declaration is kept as the name `PartitionReindex` already
uses. -/
theorem Partition.ext' {n : ℕ} {Λ Λ' : Partition n} (h : Λ.parts = Λ'.parts) : Λ = Λ' :=
  DeltaLambdaSignRule.Partition.ext h

/-- **Custom `Partition n` ≃ `Nat.Partition n`.** The forward map coerces the sorted parts list
to a multiset; the inverse sorts the multiset into a weakly-decreasing list. -/
noncomputable def partitionEquivNatPartition (n : ℕ) :
    Partition n ≃ Nat.Partition n where
  toFun Λ :=
    { parts := (Λ.parts : Multiset ℕ)
      parts_pos := fun {i} hi => Λ.pos i (by rwa [Multiset.mem_coe] at hi)
      parts_sum := by rw [Multiset.sum_coe]; exact Λ.sum_eq }
  invFun p :=
    { parts := p.parts.sort (· ≥ ·)
      pos := fun q hq => p.parts_pos (by rwa [Multiset.mem_sort] at hq)
      sum_eq := by
        rw [← Multiset.sum_coe, Multiset.sort_eq]; exact p.parts_sum
      sorted := Multiset.sort_sorted (· ≥ ·) p.parts }
  left_inv Λ := by
    apply Partition.ext
    show ((Λ.parts : Multiset ℕ)).sort (· ≥ ·) = Λ.parts
    rw [Multiset.coe_sort, List.mergeSort_eq_self]
    exact Λ.sorted
  right_inv p := by
    apply Nat.Partition.ext
    show ((p.parts.sort (· ≥ ·) : Multiset ℕ)) = p.parts
    rw [Multiset.sort_eq]

end QOU.BraidKnot.PartitionNatBridge
