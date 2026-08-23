import QOU.BraidKnot.RSKBurnsideDischarge
import QOU.BraidsAndKnots.YoungDiagramTailFirstInstance

/-!
# The Plancherel normalisation `Σ_λ (f^λ)² = k!` in the `sytDim` / `partsOf` encoding

Discharges the last premise of `YoungDiagramTailFirstInstance.nuV_top_closed_form`:
`tiltNorm k 0 = k!`, i.e. `Σ_{λ ∈ partsOf k} (sytDim λ)² = k!`.

## Why the reindexing is rebuilt here

The corpus already has a reindexing of exactly this shape,
`PartitionReindex.sum_map_eq_sum_partitionIndex`, but it is stated over the custom
`DeltaLambdaSignRule.Partition` type — and `DeltaLambdaSignRule.lean` does **not compile** at
present (its `Partition.armLength` / `legLength` / `hookLength` / `hookProduct` / `nStat` /
`conjugate` dot-notation does not resolve; it is one of the known red files targeted by main's
content-sibling compile-repair tranche). Building on it would make this keystone rest on a red
import. So the transport is redone here directly over **Mathlib's `Nat.Partition k`**, whose
dependency cone is green: `partsOf k` ↔ `Nat.Partition k` ↔ `PartitionIndex k`.

## The chain

`Σ_{l ∈ partsOf k} (sytDim l)²`
  → `Σ_{p : Nat.Partition k} (sytDim (p.parts.sort ·≥·))²`   (`Finset.sum_bij`, this file)
  → `Σ_{i : PartitionIndex k} (numSYT i.diagram)²`            (`partitionEquivYoungIndex`)
  → `k!`                                                       (`OVTopAssembly`)

with the summand matched by the SYT-encoding bridge
(`SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux`) composed with the hook-length side
(`numSYTenum_eq_numStandardYoungTableaux`, `sytDim_eq_numSYTenum`).
-/

namespace QOU.BraidsAndKnots.PlancherelNormalisation

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge
open QOU.BraidsAndKnots.YoungDiagramKernelPincer
open QOU.BraidKnot

/-- A member of the enumerator, as a Mathlib partition. -/
def toNatPartition (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) : Nat.Partition k where
  parts := (l : Multiset ℕ)
  parts_pos := fun {i} hi => (partsOf_facts k l hl).2.1 i (by rwa [Multiset.mem_coe] at hi)
  parts_sum := by
    rw [Multiset.sum_coe]
    exact (partsOf_facts k l hl).1

/-- Sorting recovers the list (it was already weakly decreasing). -/
theorem sort_parts_toNatPartition (k : ℕ) (l : List ℕ) (hl : l ∈ partsOf k) :
    ((toNatPartition k l hl).parts).sort (· ≥ ·) = l := by
  show ((l : Multiset ℕ)).sort (· ≥ ·) = l
  rw [Multiset.coe_sort, List.mergeSort_eq_self]
  exact (partsOf_facts k l hl).2.2

/-- **The summand identity**: on the partition index the RSK weight `numSYT` is the kernel's
hook-length dimension `sytDim` of the sorted parts. -/
theorem numSYT_diagram_eq_sytDim (k : ℕ) (p : Nat.Partition k) :
    numSYT ((SpechtClassification.partitionEquivYoungIndex k p).diagram)
      = sytDim (p.parts.sort (· ≥ ·)) := by
  rw [RSKBurnsideDischarge.diagram_partitionEquiv k p]
  show numSYT (YoungDiagram.ofRowLens (p.parts.sort (· ≥ ·)) (Multiset.sort_sorted _ _)) = _
  rw [SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux,
    ← QOU.Mathlib.SYTEnum.numSYTenum_eq_numStandardYoungTableaux
        (p.parts.sort (· ≥ ·)) (Multiset.sort_sorted _ _),
    ← YoungDiagramKernelDimPos.sytDim_eq_numSYTenum (p.parts.sort (· ≥ ·))
        (Multiset.sort_sorted _ _) (SpechtClassification.sorted_parts_pos k p)]

/-- **The reindexing**, over Mathlib's `Nat.Partition` (no dependency on the red custom-`Partition`
file): the enumerator's `Finset` sums like `Finset.univ`.

Generic in the codomain (2026-08-23): the `Finset.sum_bij` argument never looked at `ℕ`, and the
`ℤ`-valued instance is what the content-square total `secondMomentKernel` needs. -/
theorem sum_toFinset_eq_sum_natPartition {M : Type*} [AddCommMonoid M] (k : ℕ) (g : List ℕ → M) :
    ∑ l ∈ (partsOf k).toFinset, g l = ∑ p : Nat.Partition k, g (p.parts.sort (· ≥ ·)) := by
  refine Finset.sum_bij (fun l hl => toNatPartition k l (List.mem_toFinset.mp hl))
    (fun l hl => Finset.mem_univ _) ?_ ?_ ?_
  · -- injective
    intro l hl l' hl' heq
    have h1 := sort_parts_toNatPartition k l (List.mem_toFinset.mp hl)
    have h2 := sort_parts_toNatPartition k l' (List.mem_toFinset.mp hl')
    rw [← h1, ← h2]
    exact congrArg (fun q : Nat.Partition k => q.parts.sort (· ≥ ·)) heq
  · -- surjective
    intro p _
    refine ⟨p.parts.sort (· ≥ ·), List.mem_toFinset.mpr ?_, ?_⟩
    · refine mem_partsFuel _ k k k ?_ ?_ ?_ (Multiset.sort_sorted _ _) ?_
      · rw [← Multiset.sum_coe, Multiset.sort_eq]; exact p.parts_sum
      · exact SpechtClassification.sorted_parts_pos k p
      · intro x hx
        have hle : x ≤ (p.parts.sort (· ≥ ·)).sum := List.single_le_sum
          (fun y hy => Nat.zero_le y) x hx
        rw [← Multiset.sum_coe, Multiset.sort_eq] at hle
        have hps := p.parts_sum
        omega
      · have hlen := length_le_sum (p.parts.sort (· ≥ ·))
          (SpechtClassification.sorted_parts_pos k p)
        have hsum : (p.parts.sort (· ≥ ·)).sum = k := by
          rw [← Multiset.sum_coe, Multiset.sort_eq]; exact p.parts_sum
        omega
    · apply Nat.Partition.ext
      show ((p.parts.sort (· ≥ ·) : Multiset ℕ)) = p.parts
      rw [Multiset.sort_eq]
  · -- values match
    intro l hl
    rw [sort_parts_toNatPartition k l (List.mem_toFinset.mp hl)]

/-- **The Plancherel normalisation**: `Σ_{λ ⊢ k} (f^λ)² = k!`. -/
theorem sum_sytDim_sq_eq_factorial (k : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ] :
    ∑ l ∈ (partsOf k).toFinset, (sytDim l) ^ 2 = Nat.factorial k := by
  rw [sum_toFinset_eq_sum_natPartition k (fun l => (sytDim l) ^ 2)]
  have hsummand : ∀ p : Nat.Partition k,
      (sytDim (p.parts.sort (· ≥ ·))) ^ 2
        = (numSYT ((SpechtClassification.partitionEquivYoungIndex k p).diagram)) ^ 2 := by
    intro p
    rw [numSYT_diagram_eq_sytDim k p]
  rw [Finset.sum_congr rfl (fun p _ => hsummand p),
    Equiv.sum_comp (SpechtClassification.partitionEquivYoungIndex k)
      (fun i => (numSYT i.diagram) ^ 2)]
  exact OVTopAssembly.sum_numSYT_sq_eq_factorial k

/-- The list form (the enumerator is nodup, so its `Finset` sum is its list sum). -/
theorem sum_map_sytDim_sq_eq_factorial (k : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ] :
    ((partsOf k).map (fun l => (sytDim l) ^ 2)).sum = Nat.factorial k := by
  have hnd : (partsOf k).Nodup := partsFuel_nodup k k k
  rw [← List.sum_toFinset (fun l => (sytDim l) ^ 2) hnd]
  exact sum_sytDim_sq_eq_factorial k

/-- The normalisation in the ℝ form `tiltNorm` takes. -/
theorem tiltNorm_zero_eq_factorial (k : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ] :
    tiltNorm k 0 = (Nat.factorial k : ℝ) := by
  unfold tiltNorm
  have hcast : ((((partsOf k).map (fun l => (sytDim l) ^ 2)).sum : ℕ) : ℝ)
      = ((partsOf k).map (fun l => tilt 0 (sytDim l))).sum := by
    rw [Nat.cast_list_sum, List.map_map]
    refine congrArg List.sum (List.map_congr_left fun l _ => ?_)
    simp only [Function.comp_apply]
    rw [tilt_zero]
    push_cast
    ring
  rw [← hcast, sum_map_sytDim_sq_eq_factorial k]

/-- **The (TAIL) first instance, unconditionally**:
`ν_n = n(n−2)(n−3)·C(2n−4, n−2) / (3·n!)`. -/
theorem nuV_top_closed_form_unconditional (r : ℕ) (hr : 1 ≤ r) (hk' : r + 2 ≤ 20) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ] :
    nuV (r + 2) (r + 2)
      = ((r : ℝ) + 2) * (r : ℝ) * ((r : ℝ) - 1) * (((2 * r).choose r : ℕ) : ℝ)
          / (3 * (Nat.factorial (r + 2) : ℝ)) :=
  YoungDiagramTailFirstInstance.nuV_top_closed_form r hr hk'
    (tiltNorm_zero_eq_factorial (r + 2))

end QOU.BraidsAndKnots.PlancherelNormalisation
