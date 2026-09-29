import QOU.BraidKnot.ContentSqSumBridge
import QOU.BraidKnot.SnIsotypicSpechtSplitInstance
import QOU.BraidKnot.OVTopAssembly
import QOU.BraidKnot.IdentityIPlancherelConditional
import QOU.BraidKnot.SpechtWedderburnLe12
import QOU.Mathlib.PartitionsOfBridge
import QOU.Mathlib.IdentityIHLFBridge

/-!
# QOU.BraidKnot.PlancherelSnDataGeneral — Identity I's Plancherel data, at every `n`

`IdentityI.PlancherelSnData n` carries the two standard `S_n` facts Identity I is conditional on:

* **(i)** `Σ_λ dim(λ)² = n!`, and
* **(ii)** `2·Σ_λ dim(λ)²·(Σ_{c∈λ} c(c)²) = n(n−1)·n!`, the cleared content-square Plancherel mean.

Both were supplied only by hand-registered `decide` instances at `n = 2 … 12`, so the conditional
Identity I results (`IdentityI.two_sum_dim_sq_hooks`, `IdentityI.twoM_eq_plancherel_hook_sum`) were
usable only in that range. This file builds the datum for **every** `n`.

## What each half now rests on

* **(i)** is `PartitionsOfBridge.sum_map_dimHLF_sq`, i.e. the Robinson–Schensted correspondence
  (`QOU.Mathlib.rskBurnsideHolds`) transported to the list model.
* **(ii)** is `RegularRepBlockTrace.identityB_conditional` applied to the assembled spectral datum
  `OVTopAssembly.snSpectralData`, whose class hypothesis is inhabited by
  `SnIsotypicSpechtSplitInstance` — reindexed off `PartitionIndex n` onto the list enumerator
  through `SpechtWedderburnLe12.numSYT_partitionEquiv` (dimensions) and
  `ContentSqSumBridge.contentSqSum_ofRowLens` (contents).

The second bridge is the one that did not exist: the OV/JM layer states the eigenvalue as
`JucysMurphy.contentSqSum` over a diagram's cells, and `PlancherelSnData` states it as
`IdentityI.sumSqContents` over a row-length list. Identity (ii) held for all `n` in the first form
since `identityB_general`; it could not be written in the second.

## Not an instance, on purpose

`plancherelSnDataGeneral` is a `def`, not an `instance`: `IdentityIPlancherelInstances` registers
eleven per-`n` instances, and `PlancherelSnData` is a **data**-carrying class, so a competing
general instance would make `h.parts` / `h.dim` depend on which one resolution picked. The per-`n`
instances stay the resolvable ones (and stay cheaper) inside their range; the general-`n` payoff is
stated directly by `two_sum_dim_sq_hooks_general` / `twoM_eq_plancherel_hook_sum_general` below,
which carry no hypothesis at all.

Pure combinatorics on `ℕ`/`ℤ` plus the assembled Wedderburn datum over `ℚ`; nothing archimedean;
no fit.
-/

namespace QOU.BraidKnot.PlancherelSnDataGeneral

open QOU.BraidKnot
open QOU.BraidKnot.IdentityI (dimHLF sumSqContents sumSqHooks sz partitionsOf PlancherelSnData)
open QOU.Mathlib.PartitionsOfBridge (mem_partitionsOf partitionsOf_nodup sum_map_partitionsOf
  sum_map_dimHLF_sq)
open QOU.Mathlib.PartitionListBridge (toList)

/-! ## The content bridge on the partition index -/

/-- The Jucys–Murphy content-square eigenvalue of `partitionShape p` is the list-model
`sumSqContents` of `p`'s sorted parts — `ContentSqSumBridge.contentSqSum_ofRowLens` read at the
diagram `partitionShape` names. -/
theorem contentSqSum_partitionShape {n : ℕ} (p : Nat.Partition n) :
    JucysMurphy.contentSqSum (QOU.Mathlib.partitionShape p) = sumSqContents (toList p) :=
  ContentSqSumBridge.contentSqSum_ofRowLens _ _

/-! ## Identity (ii), transported to the list model -/

/-- **Identity (ii) on the Specht partition index** — `identityB_conditional` applied to the
assembled datum `snSpectralData (R := ℚ)`, whose `ω` / `d` fields are `contentSqSum` / `numSYT`
by definition. -/
theorem sum_index_content (n : ℕ) :
    ∑ i : SpechtClassification.PartitionIndex n,
        ((JucysMurphy.contentSqSum i.diagram : ℤ) : ℚ) * ((numSYT i.diagram : ℕ) : ℚ) ^ 2
      = (n.factorial : ℚ) * (n.choose 2 : ℚ) :=
  RegularRepBlockTrace.identityB_conditional (OVTopAssembly.snSpectralData (R := ℚ) n)

/-- **Identity (ii) on the abstract partition index**, in `ℚ`. -/
theorem sum_partition_content_rat (n : ℕ) :
    ∑ p : Nat.Partition n,
        ((sumSqContents (toList p) : ℤ) : ℚ) * ((dimHLF (toList p) : ℕ) : ℚ) ^ 2
      = (n.factorial : ℚ) * (n.choose 2 : ℚ) := by
  classical
  rw [← sum_index_content n, ← Equiv.sum_comp (SpechtClassification.partitionEquivYoungIndex n)
    (fun i => ((JucysMurphy.contentSqSum i.diagram : ℤ) : ℚ) * ((numSYT i.diagram : ℕ) : ℚ) ^ 2)]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [SpechtWedderburnLe12.numSYT_partitionEquiv,
    SpechtWedderburnLe12.diagram_partitionEquiv,
    contentSqSum_partitionShape, QOU.Mathlib.dimSYT_eq_dimHLF]
  rfl

/-- **Identity (ii) on the abstract partition index**, in `ℤ`. -/
theorem sum_partition_content_int (n : ℕ) :
    ∑ p : Nat.Partition n, sumSqContents (toList p) * (dimHLF (toList p) : ℤ) ^ 2
      = (n.factorial : ℤ) * (n.choose 2 : ℤ) := by
  exact_mod_cast sum_partition_content_rat n

/-- **Identity (ii) on the list enumerator** `partitionsOf n`. -/
theorem sum_map_content (n : ℕ) :
    ((partitionsOf n).map (fun l => sumSqContents l * (dimHLF l : ℤ) ^ 2)).sum
      = (n.factorial : ℤ) * (n.choose 2 : ℤ) := by
  rw [sum_map_partitionsOf n (fun l => sumSqContents l * (dimHLF l : ℤ) ^ 2)]
  exact sum_partition_content_int n

/-! ## Arithmetic: clearing the binomial -/

/-- `2·binom(n,2) = n(n−1)`, over `ℤ` (so the `n = 0` truncated subtraction does not intrude). -/
theorem two_mul_choose_two (n : ℕ) : 2 * (n.choose 2 : ℤ) = (n : ℤ) * ((n : ℤ) - 1) := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [Nat.choose_succ_succ m 1, Nat.choose_one_right]
    push_cast
    push_cast at ih
    linear_combination ih

/-! ## The datum, at every `n` -/

/-- **`PlancherelSnData n`, for every `n`.** The partitions are the list enumerator
`partitionsOf n`, the dimension is the Frame–Robinson–Thrall hook-length value `dimHLF`, and the
two axioms are the transported identities above. -/
def plancherelSnDataGeneral (n : ℕ) : PlancherelSnData n where
  parts := (partitionsOf n).toFinset
  parts_sorted := fun l hl => (mem_partitionsOf.mp (List.mem_toFinset.mp hl)).1
  parts_sz := fun l hl => (mem_partitionsOf.mp (List.mem_toFinset.mp hl)).2.2
  dim := dimHLF
  sum_dim_sq := by
    classical
    have hN : ∑ l ∈ (partitionsOf n).toFinset, (dimHLF l) ^ 2 = n.factorial := by
      rw [List.sum_toFinset _ (partitionsOf_nodup n)]
      exact sum_map_dimHLF_sq n
    calc ∑ l ∈ (partitionsOf n).toFinset, ((dimHLF l : ℤ)) ^ 2
        = ((∑ l ∈ (partitionsOf n).toFinset, (dimHLF l) ^ 2 : ℕ) : ℤ) := by push_cast; rfl
      _ = (n.factorial : ℤ) := by rw [hN]
  two_sum_dim_sq_content := by
    classical
    have hsum : ∑ l ∈ (partitionsOf n).toFinset, (dimHLF l : ℤ) ^ 2 * sumSqContents l
        = (n.factorial : ℤ) * (n.choose 2 : ℤ) := by
      rw [List.sum_toFinset _ (partitionsOf_nodup n), ← sum_map_content n]
      exact congrArg List.sum (List.map_congr_left fun l _ => mul_comm _ _)
    rw [hsum]
    linear_combination (n.factorial : ℤ) * two_mul_choose_two n

/-- **Cross-check against the hand-registered `n = 4` instance.** `IdentityIPlancherelInstances`
lists the partitions of `4` by hand; the enumerator produces the same finset, so the general datum
is the same datum there and not a differently-indexed near-miss. -/
example : (plancherelSnDataGeneral 4).parts = IdentityI.plancherelSnData_four.parts := by decide

/-- The dimensions agree too — both are `dimHLF`. -/
example : (plancherelSnDataGeneral 4).dim = IdentityI.plancherelSnData_four.dim := rfl

/-- The class is inhabited at every `n`. -/
theorem plancherelSnData_nonempty (n : ℕ) : Nonempty (PlancherelSnData n) :=
  ⟨plancherelSnDataGeneral n⟩

/-! ## The payoff — Identity I at every `n`, with no hypothesis -/

/-- **Identity I, unconditional, at every `n`.** The Plancherel-expected squared-**hook** sum,
cleared of `1/n!`, is `n(3n−1)·n!`. This is `IdentityI.two_sum_dim_sq_hooks` with its class
hypothesis discharged by `plancherelSnDataGeneral` — previously available only at `n ≤ 12`. -/
theorem two_sum_dim_sq_hooks_general (n : ℕ) :
    2 * ∑ l ∈ (partitionsOf n).toFinset, (dimHLF l : ℤ) ^ 2 * sumSqHooks l
      = (n : ℤ) * (3 * (n : ℤ) - 1) * (n.factorial : ℤ) :=
  IdentityI.two_sum_dim_sq_hooks (h := plancherelSnDataGeneral n) n

/-- **The keystone's `twoM` is its representation-theoretic definition, at every `n`.**
`WLambdaDefect.twoM n = n(3n−1)` carries Identity I as a bare `def`; this says that closed form
**is** the Plancherel squared-hook sum (cleared by `2` / `n!`) — with no hypothesis, where before
the bridge held only for `n = 2 … 12`. -/
theorem twoM_eq_plancherel_hook_sum_general (n : ℕ) :
    2 * ∑ l ∈ (partitionsOf n).toFinset, (dimHLF l : ℤ) ^ 2 * sumSqHooks l
      = QOU.BraidKnot.WLambdaDefect.twoM (n : ℤ) * (n.factorial : ℤ) :=
  IdentityI.twoM_eq_plancherel_hook_sum (h := plancherelSnDataGeneral n) n

end QOU.BraidKnot.PlancherelSnDataGeneral
