import QOU.BraidKnot.RSKBurnsideDischarge
import QOU.BraidKnot.PartitionReindex
import QOU.BraidsAndKnots.YoungDiagramTailFirstInstance

/-!
# The Plancherel normalisation `Σ_λ (f^λ)² = k!` in the `sytDim` / `partsOf` encoding

The last open premise of `YoungDiagramTailFirstInstance.nuV_top_closed_form`:
`tiltNorm k 0 = k!`, i.e. `Σ_{λ ∈ partsOf k} (sytDim λ)² = k!`.

Every ingredient is now proved; this file is the glue:

* `SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux` — the two SYT encodings agree;
* `SYTEnum.numSYTenum_eq_numStandardYoungTableaux` + `sytDim_eq_numSYTenum` — the hook-length side,
  so `sytDim l = numSYT (ofRowLens l _)`;
* `PartitionReindex.sum_map_eq_sum_partitionIndex` — a complete, `parts`-nodup list of custom
  partitions sums like `Finset.univ (PartitionIndex k)`;
* `OVTopAssembly.sum_numSYT_sq_eq_factorial` — the RSK sum-of-squares on that index.

The enumerator `partsOf k` supplies the completeness and nodup hypotheses via `partsOf_facts`,
`mem_partsFuel` and `partsFuel_nodup`.
-/

namespace QOU.BraidsAndKnots.PlancherelNormalisation

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge
open QOU.BraidsAndKnots.YoungDiagramKernelPincer
open QOU.BraidKnot

/-- `partsOf k` as a list of *typed* partitions (proofs attached from `partsOf_facts`). -/
def partsOfP (k : ℕ) : List (DeltaLambdaSignRule.Partition k) :=
  (partsOf k).attach.map (fun x =>
    { parts := x.1
      pos := fun i hi => (partsOf_facts k x.1 x.2).2.1 i hi
      sum_eq := (partsOf_facts k x.1 x.2).1
      sorted := (partsOf_facts k x.1 x.2).2.2 })

/-- Forgetting the attached proofs recovers the enumerator. -/
theorem map_parts_partsOfP (k : ℕ) :
    (partsOfP k).map DeltaLambdaSignRule.Partition.parts = partsOf k := by
  rw [partsOfP, List.map_map]
  simpa using List.attach_map_val (partsOf k)

/-- The index equiv sends a typed partition to the diagram of its (already sorted) parts. -/
theorem diagram_partitionEquivIndex (k : ℕ) (Λ : DeltaLambdaSignRule.Partition k) :
    (PartitionReindex.partitionEquivIndex k Λ).diagram
      = YoungDiagram.ofRowLens Λ.parts Λ.sorted := by
  have hsort : ((Λ.parts : Multiset ℕ)).sort (· ≥ ·) = Λ.parts := by
    rw [Multiset.coe_sort, List.mergeSort_eq_self]
    exact Λ.sorted
  show QOU.Mathlib.partitionShape (PartitionNatBridge.partitionEquivNatPartition k Λ) = _
  unfold QOU.Mathlib.partitionShape
  congr 1

/-- **The summand identity**: on the partition index, the RSK weight `numSYT` *is* the kernel's
hook-length dimension `sytDim`. Chains the SYT-encoding bridge with the hook-length side. -/
theorem numSYT_diagram_eq_sytDim (k : ℕ) (Λ : DeltaLambdaSignRule.Partition k) :
    numSYT ((PartitionReindex.partitionEquivIndex k Λ).diagram) = sytDim Λ.parts := by
  rw [diagram_partitionEquivIndex k Λ,
    SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux,
    ← QOU.Mathlib.SYTEnum.numSYTenum_eq_numStandardYoungTableaux Λ.parts Λ.sorted,
    ← YoungDiagramKernelDimPos.sytDim_eq_numSYTenum Λ.parts Λ.sorted Λ.pos]

/-- **The Plancherel normalisation** in the kernel's own encoding:
`Σ_{λ ⊢ k} (f^λ)² = k!`. -/
theorem sum_sytDim_sq_eq_factorial (k : ℕ) :
    ((partsOf k).map (fun l => (sytDim l) ^ 2)).sum = Nat.factorial k := by
  have hcomplete : ∀ Λ : DeltaLambdaSignRule.Partition k,
      Λ.parts ∈ (partsOfP k).map DeltaLambdaSignRule.Partition.parts := by
    intro Λ
    rw [map_parts_partsOfP]
    exact mem_partsFuel Λ.parts k k k Λ.sum_eq (fun x hx => Λ.pos x hx)
      (fun x hx => by
        have := mem_le_headD Λ.parts Λ.sorted x hx
        have hhd : Λ.parts.headD 0 ≤ k := by
          rw [← Λ.sum_eq]
          exact getD_le_sum Λ.parts 0 |>.trans_eq (by rw [getD_zero_eq_headD]) |>.symm ▸
            (getD_zero_eq_headD Λ.parts ▸ getD_le_sum Λ.parts 0)
        omega)
      Λ.sorted
      (by
        rw [← Λ.sum_eq]
        exact length_le_sum Λ.parts (fun x hx => Λ.pos x hx))
  have hnodup : ((partsOfP k).map DeltaLambdaSignRule.Partition.parts).Nodup := by
    rw [map_parts_partsOfP]
    exact partsFuel_nodup k k k
  have hre := PartitionReindex.sum_map_eq_sum_partitionIndex k (partsOfP k) hcomplete hnodup
    (fun i => (numSYT i.diagram) ^ 2)
  have hlhs : ((partsOfP k).map
        (fun Λ => (numSYT ((PartitionReindex.partitionEquivIndex k Λ).diagram)) ^ 2)).sum
      = ((partsOf k).map (fun l => (sytDim l) ^ 2)).sum := by
    rw [← map_parts_partsOfP k, List.map_map]
    refine congrArg List.sum (List.map_congr_left fun Λ _ => ?_)
    simp only [Function.comp_apply]
    rw [numSYT_diagram_eq_sytDim k Λ]
  rw [← hlhs, hre]
  exact OVTopAssembly.sum_numSYT_sq_eq_factorial k

/-- The normalisation in the ℝ form the pincer's `tiltNorm` takes. -/
theorem tiltNorm_zero_eq_factorial (k : ℕ) :
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
  rw [← hcast, sum_sytDim_sq_eq_factorial k]

/-- **The (TAIL) first instance, unconditionally**: the exact closed form
`ν_n = n(n−2)(n−3)·C(2n−4, n−2) / (3·n!)`, with the normalisation premise now discharged. -/
theorem nuV_top_closed_form_unconditional (r : ℕ) (hr : 1 ≤ r) (hk' : r + 2 ≤ 20) :
    nuV (r + 2) (r + 2)
      = ((r : ℝ) + 2) * (r : ℝ) * ((r : ℝ) - 1) * (((2 * r).choose r : ℕ) : ℝ)
          / (3 * (Nat.factorial (r + 2) : ℝ)) :=
  YoungDiagramTailFirstInstance.nuV_top_closed_form r hr hk'
    (tiltNorm_zero_eq_factorial (r + 2))

end QOU.BraidsAndKnots.PlancherelNormalisation
