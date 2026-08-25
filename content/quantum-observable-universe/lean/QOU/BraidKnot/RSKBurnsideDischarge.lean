import QOU.BraidKnot.SYTEncodingBridgeTwo
import QOU.BraidKnot.OVTopAssembly
import QOU.Mathlib.RSKBurnsideTarget

/-!
# Discharging `RSKBurnsideHolds`

`QOU.Mathlib.RSKBurnsideHolds n` — `∑_{p ⊢ n} dimSYT p ² = n!` — was introduced as a *target*: a
well-typed `Prop` whose docstring records it as **"not yet a theorem"**, its proof "the RSK
correspondence … which the pinned Mathlib lacks and which is the multi-session next step".

It is now a theorem. Two ingredients that landed independently make it a reindexing:

* `OVTopAssembly.sum_numSYT_sq_eq_factorial` — `∑ i : PartitionIndex n, numSYT i.diagram ² = n!`,
  obtained by specialising the Wedderburn block-trace identity to the assembled `snSpectralData ℚ n`;
* `SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux` — the bridge between the corpus' two
  standard-tableau encodings, which is what let the RSK statement (phrased with `numSYT`) reach
  `dimSYT` (phrased with `numStandardYoungTableaux`).

The remaining glue is `partitionEquivYoungIndex`, whose forward map sends `p` to the diagram
`YoungDiagram.ofRowLens (p.parts.sort (· ≥ ·)) _` — definitionally `RSKBurnsideTarget.partitionShape p`,
the shape `dimSYT` counts. So `Equiv.sum_comp` transports the `PartitionIndex` sum to the
`Nat.Partition` sum.

Note this does **not** by itself discharge `DeltaLambdaSignRule.burnside`
(`∑_λ (dimIrrep λ)² = n!` over the custom `Partition` encoding). The difference is exactly the
encoding: `dimSYT` is defined as an SYT *count*, while `dimIrrep` is defined by hook-length
division. That gap is the roadmap's bridge (1), `dimIrrep = numSYT`, which is **now proved** as
`QOU.BraidKnot.dimIrrep_eq_numSYT` (`PartitionHookProductBridge`). What remains for `burnside`
is bridge (2) — the reindexing `List (Partition n)` (complete + `Nodup`) ↔
`Finset.univ (PartitionIndex n)` — and then wiring the two together.

-- Ref: [sagan2001] Sagan, The Symmetric Group §3.10 (RSK; ∑ (f^λ)² = n!)
-/

namespace QOU.BraidKnot.RSKBurnsideDischarge

open QOU.BraidKnot

/-- The index equiv's forward map produces exactly the shape `dimSYT` counts. -/
theorem diagram_partitionEquiv (n : ℕ) (p : Nat.Partition n) :
    (SpechtClassification.partitionEquivYoungIndex n p).diagram
      = QOU.Mathlib.partitionShape p := rfl

/-- `dimSYT` in the 0-indexed count, via the encoding bridge. -/
theorem dimSYT_eq_numSYT (n : ℕ) (p : Nat.Partition n) :
    QOU.Mathlib.dimSYT p = numSYT (QOU.Mathlib.partitionShape p) := by
  unfold QOU.Mathlib.dimSYT
  exact (SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux _).symm

/-- **`RSKBurnsideHolds`, conditional on `SnIsotypicSpechtSplit`**: `∑_{p ⊢ n} dimSYT p ² = n!`.

Reindex the `PartitionIndex` form of the RSK sum-of-squares along `partitionEquivYoungIndex`,
converting each summand with the SYT-encoding bridge.

**Scope (corrected 2026-08-23).** This carries a class hypothesis and so proves the *implication*;
the docstring above previously read "is now a theorem", which overclaims a conditional proof
(conditional-proved ≠ premise-established). Note also the direction: this derives the identity
*from* the Wedderburn split. The **unconditional** theorem is `QOU.Mathlib.rskBurnsideHolds`, proved
from the Robinson–Schensted correspondence with no hypothesis, and it is what
`SnIsotypicSpechtSplitInstance` is built from — so citing this one as the source of the identity
would be circular. -/
theorem rskBurnsideHolds (n : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ] : QOU.Mathlib.RSKBurnsideHolds n := by
  unfold QOU.Mathlib.RSKBurnsideHolds
  have hstep : ∑ p : Nat.Partition n, (QOU.Mathlib.dimSYT p) ^ 2
      = ∑ p : Nat.Partition n,
          (numSYT ((SpechtClassification.partitionEquivYoungIndex n p).diagram)) ^ 2 := by
    refine Finset.sum_congr rfl fun p _ => ?_
    rw [dimSYT_eq_numSYT n p, diagram_partitionEquiv n p]
  rw [hstep,
    Equiv.sum_comp (SpechtClassification.partitionEquivYoungIndex n)
      (fun i => (numSYT i.diagram) ^ 2)]
  exact OVTopAssembly.sum_numSYT_sq_eq_factorial n

/-- The concrete witness the abstract substrate axiom asked for, now unconditional
(`RSKBurnsideTarget.rskBurnside_imp_substrate` applied to the theorem above). -/
theorem substrate_witness (n : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ] :
    ∃ dimFn : Nat.Partition n → ℕ, ∑ p : Nat.Partition n, (dimFn p) ^ 2 = n.factorial :=
  ⟨QOU.Mathlib.dimSYT, rskBurnsideHolds n⟩

end QOU.BraidKnot.RSKBurnsideDischarge
