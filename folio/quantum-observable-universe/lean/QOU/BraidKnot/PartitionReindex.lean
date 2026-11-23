import QOU.BraidKnot.PartitionNatBridge
import QOU.BraidKnot.SpechtClassification

/-!
# QOU.BraidKnot.PartitionReindex — Burnside reindexing (bridge 2, complete)

Completes **bridge (2)** of the `DeltaLambdaSignRule.burnside` roadmap. The encoding equiv
`PartitionNatBridge.partitionEquivNatPartition` (`Partition n ≃ Nat.Partition n`) composes with
`SpechtClassification.partitionEquivYoungIndex` (`Nat.Partition n ≃ PartitionIndex n`) to give
`partitionEquivIndex : Partition n ≃ PartitionIndex n`. Over it, a **complete, parts-deduplicated
list** of custom partitions transports its sum to the `Finset.univ` sum over `PartitionIndex n`
(`sum_map_eq_sum_partitionIndex`) — exactly the reindexing `burnside` needs to consume
`OVTopAssembly.sum_numSYT_sq_eq_factorial` (`Σ_i (#SYT i.diagram)² = n!`).

Bridge (1), the hook-length identity `dimIrrep = numSYT`, is **now proved** as
`QOU.BraidKnot.dimIrrep_eq_numSYT` (`PartitionHookProductBridge`, from
`HookProductHLF.numSYT_mul_hookProduct` + the custom↔YoungDiagram `hookProduct` bridge).
Both ingredients `burnside` needs are therefore available; what remains is assembling them
into the `burnside` statement itself.

-- Ref: [sagan2001] Sagan, The Symmetric Group
-/

open scoped BigOperators

namespace QOU.BraidKnot.PartitionReindex

open DeltaLambdaSignRule SpechtClassification PartitionNatBridge

/-- `Partition n` is a `Fintype`, transported from `Nat.Partition n` along the encoding equiv. -/
noncomputable instance instFintypePartition (n : ℕ) : Fintype (Partition n) :=
  Fintype.ofEquiv (Nat.Partition n) (partitionEquivNatPartition n).symm

/-- `Partition n` has decidable equality (the `parts` list decides it, `Partition.ext'`). -/
instance instDecidableEqPartition (n : ℕ) : DecidableEq (Partition n) := fun Λ Λ' =>
  decidable_of_iff (Λ.parts = Λ'.parts) ⟨PartitionNatBridge.Partition.ext', fun h => h ▸ rfl⟩

/-- The composed **reindexing equiv** `Partition n ≃ PartitionIndex n`. -/
noncomputable def partitionEquivIndex (n : ℕ) : Partition n ≃ PartitionIndex n :=
  (partitionEquivNatPartition n).trans (partitionEquivYoungIndex n)

/-- **Burnside reindexing — bridge (2), complete.** A list of custom partitions of `n` that is
`parts`-complete and `parts`-`Nodup`, summed through the reindexing equiv into `PartitionIndex n`,
equals the `Finset.univ` sum. -/
theorem sum_map_eq_sum_partitionIndex {M : Type*} [AddCommMonoid M] (n : ℕ)
    (partitions : List (Partition n))
    (hcomplete : ∀ μ : Partition n, μ.parts ∈ partitions.map Partition.parts)
    (hnodup : (partitions.map Partition.parts).Nodup)
    (g : PartitionIndex n → M) :
    (partitions.map fun Λ => g (partitionEquivIndex n Λ)).sum = ∑ i : PartitionIndex n, g i := by
  -- `partitions` is `Nodup` as partitions, and contains every partition.
  have hnd : partitions.Nodup := hnodup.of_map _
  have hmem : ∀ Λ : Partition n, Λ ∈ partitions := by
    intro Λ
    obtain ⟨Λ', hΛ', hpe⟩ := List.mem_map.mp (hcomplete Λ)
    have : Λ = Λ' := PartitionNatBridge.Partition.ext' hpe.symm
    exact this ▸ hΛ'
  -- Hence `partitions` is a permutation of `univ.toList`.
  have hperm : List.Perm partitions (Finset.univ : Finset (Partition n)).toList := by
    apply List.perm_of_nodup_nodup_toFinset_eq hnd (Finset.nodup_toList _)
    ext Λ
    simp only [List.mem_toFinset, Finset.mem_toList, Finset.mem_univ, hmem Λ]
  -- Reindex the Fintype sum through the equiv, then match the permuted list sum.
  rw [← Equiv.sum_comp (partitionEquivIndex n) g]
  rw [(hperm.map fun Λ => g (partitionEquivIndex n Λ)).sum_eq]
  rw [Finset.sum_map_toList (Finset.univ : Finset (Partition n)) fun Λ => g (partitionEquivIndex n Λ)]

/-- Subtracting the full Fintype sum over PartitionIndex from the mapped partition list sum yields zero. -/
theorem sum_map_sub_sum_partitionIndex_eq_zero {M : Type*} [AddCommGroup M] (n : ℕ)
    (partitions : List (Partition n))
    (hcomplete : ∀ μ : Partition n, μ.parts ∈ partitions.map Partition.parts)
    (hnodup : (partitions.map Partition.parts).Nodup)
    (g : PartitionIndex n → M) :
    (partitions.map fun Λ => g (partitionEquivIndex n Λ)).sum
      - ∑ i : PartitionIndex n, g i = 0 := by
  rw [sum_map_eq_sum_partitionIndex n partitions hcomplete hnodup g, sub_self]

end QOU.BraidKnot.PartitionReindex
