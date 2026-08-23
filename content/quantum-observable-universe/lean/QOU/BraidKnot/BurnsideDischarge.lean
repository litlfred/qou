import QOU.BraidKnot.PartitionHookProductBridge
import QOU.BraidKnot.PartitionReindex
import QOU.BraidKnot.RSKBurnsideDischarge

/-!
# QOU.BraidKnot.BurnsideDischarge — `Σ_λ (f^λ)² = n!` over the custom `Partition` encoding

Discharges `DeltaLambdaSignRule.burnside` from its two roadmap bridges, both of which
are now proved, plus the Wedderburn/dimension side.

`burnside` was a **self-assuming projection**: `BurnsideContext` carried the burnside
conclusion itself as a class field, and the "proof" was `ctx.burnside_claim …` — a
`P → P` with no mathematical content (AGENTS.md §3b-cond rule 5). Nobody could supply
the instance honestly, so every downstream use was gated on an assumption.

This file supplies the instance from an actual derivation:

    (partitions.map fun Λ => Λ.dimIrrep ^ 2).sum
  = (partitions.map fun Λ => numSYT (partitionEquivIndex n Λ).diagram ^ 2).sum
        -- bridge (1): `dimIrrep_eq_numSYT` (PartitionHookProductBridge) + `toYoungDiagram_eq` below
  = ∑ i : PartitionIndex n, numSYT i.diagram ^ 2
        -- bridge (2): `PartitionReindex.sum_map_eq_sum_partitionIndex`
  = n!
        -- `OVTopAssembly.sum_numSYT_sq_eq_factorial`

## Why a leaf module

`burnside` is stated in `QOU.BraidKnot.DeltaLambdaSignRule`, which is *upstream* of
every ingredient — `PartitionReindex → PartitionNatBridge → DeltaLambdaSignRule`, and
likewise for the hook-product bridge. The discharge therefore cannot live at the
statement site without a cycle; it moves downstream to this leaf, exactly as the FRT
hook-length formula did in `QOU.BraidKnot.HookProductHLF`.

## Honest axiom status

**Correction (2026-08-23).** The paragraph that stood here said `burnside_proved` is *not*
sorry-free, because `OVTopAssembly.sum_numSYT_sq_eq_factorial` carried `sorryAx` from two named
sorries. That is no longer the state of the world, and neither half of it is:
`centralC2_acts_by_contentSqSum` is proved, and `sn_rational_specht_split`'s `sorry` was replaced
by the class `SnIsotypicSpechtSplit`, which is now **inhabited**
(`SnIsotypicSpechtSplitInstance`, from the RSK correspondence rather than from any assumption).
Measured: `#print axioms` on `burnside_proved` reports `[propext, Classical.choice, Quot.sound]`.
A hypothesis-free restatement is checked in `WedderburnUnconditional`.

Before, the burnside claim was *assumed wholesale* through an instance nobody
could provide. Then it became *derived* with two located obligations in the
Oka–Vershik assembly. Both of those are now discharged, so it is derived outright.
Bridges (1) and (2) were always axiom-clean.

-- Ref: [sagan2001] Sagan, The Symmetric Group §1.10–§3.10 (RSK; Σ (f^λ)² = n!)
-- Ref: [manuscript] docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md (axiom (i))
-/

namespace QOU.BraidKnot.BurnsideDischarge

open QOU.BraidKnot DeltaLambdaSignRule

/-- Coercing a weakly-decreasing list to a `Multiset` and sorting it back is the identity.
This is the same round-trip `PartitionNatBridge.partitionEquivNatPartition`'s `left_inv`
performs; isolated here because the shape identity below needs it on its own. -/
theorem sort_coe_parts {n : ℕ} (Λ : Partition n) :
    ((Λ.parts : Multiset ℕ)).sort (· ≥ ·) = Λ.parts := by
  rw [Multiset.coe_sort, List.mergeSort_eq_self]
  exact Λ.sorted

/-- **The shape glue.** The `YoungDiagram` a custom `Partition n` denotes is the diagram
carried by its image under the reindexing equiv — i.e. bridge (1)'s `toYoungDiagram` and
bridge (2)'s `partitionEquivIndex` agree on shapes.

Both sides are `YoungDiagram.ofRowLens` of the same parts list; the right-hand side takes
the scenic route through `Nat.Partition`'s multiset, which `sort_coe_parts` undoes. -/
theorem toYoungDiagram_eq {n : ℕ} (Λ : Partition n) :
    toYoungDiagram Λ = (PartitionReindex.partitionEquivIndex n Λ).diagram := by
  rw [PartitionReindex.partitionEquivIndex, Equiv.trans_apply,
    RSKBurnsideDischarge.diagram_partitionEquiv, QOU.Mathlib.partitionShape, toYoungDiagram]
  congr 1
  exact (sort_coe_parts Λ).symm

/-- **Burnside / RSK over the custom `Partition` encoding**, derived rather than assumed:
`Σ_λ (f^λ)² = n!` for a `parts`-complete, `parts`-`Nodup` list of partitions of `n`.

Composes bridge (1) (`dimIrrep_eq_numSYT`, axiom-clean), the shape glue above, bridge (2)
(`sum_map_eq_sum_partitionIndex`, axiom-clean), and the Wedderburn dimension sum
(`OVTopAssembly.sum_numSYT_sq_eq_factorial`).

**Corrected 2026-08-23.** That last citation read *"which carries the residual `sorryAx` — see the
module docstring"*. It does not: it carries a class hypothesis, `SnIsotypicSpechtSplit`, which is
now inhabited by `SnIsotypicSpechtSplitInstance`, and `#print axioms` on it reports
`[propext, Classical.choice, Quot.sound]`. -/
theorem burnside_proved (n : ℕ) (partitions : List (Partition n)) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ]
    (hcomplete : ∀ μ : Partition n, μ.parts ∈ partitions.map Partition.parts)
    (hnodup : (partitions.map Partition.parts).Nodup) :
    (partitions.map fun Λ => Λ.dimIrrep ^ 2).sum = Nat.factorial n := by
  have hmap : (partitions.map fun Λ => Λ.dimIrrep ^ 2)
      = partitions.map fun Λ =>
          (numSYT ((PartitionReindex.partitionEquivIndex n Λ).diagram)) ^ 2 := by
    refine List.map_congr_left fun Λ _ => ?_
    rw [dimIrrep_eq_numSYT, toYoungDiagram_eq]
  rw [hmap, PartitionReindex.sum_map_eq_sum_partitionIndex n partitions hcomplete hnodup
    (fun i => (numSYT i.diagram) ^ 2)]
  exact OVTopAssembly.sum_numSYT_sq_eq_factorial n

/-- The `BurnsideContext` instance, now backed by `burnside_proved` instead of assumed.

With this in scope, `DeltaLambdaSignRule.burnside` is no longer conditional in practice:
its class argument resolves to a derivation. The class itself is left in place upstream
(removing it is an upstream edit and would churn every `[BurnsideContext]` signature);
what changes is that it is now *inhabited by a proof*. -/
instance instBurnsideContext [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ] : DeltaLambdaSignRule.BurnsideContext where
  burnside_claim n partitions hcomp hnodup := burnside_proved n partitions hcomp hnodup

end QOU.BraidKnot.BurnsideDischarge
