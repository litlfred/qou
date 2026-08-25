import QOU.BraidKnot.SpechtWedderburnCriterion
import QOU.BraidKnot.SYTEncodingBridgeTwo
import QOU.Mathlib.PartitionsOfBridge

/-!
# QOU.BraidKnot.SpechtWedderburnLe12 — the Wedderburn split, unconditionally, for `n ≤ 12`

Brick 6 of **W1+W3** of the Wedderburn epic (`qou-bxw4`), and the first **unconditional** result
of the arc.

`SpechtWedderburnCriterion` reduced the split to one number: `spechtProduct` is an algebra
isomorphism as soon as `Σ_{μ ⊢ n} (#SYT μ)² = n!`. That number is not open at every `n` — the
corpus already proves it for `n ≤ 12`, by a route with no RSK correspondence in it at all
(`PartitionsOfBridge.rskBurnsideHolds_le12`: `decide`-verified list-model data fed through the
hook-length bridge). Measured, not assumed: `#print axioms` on that theorem reports only
`propext, Classical.choice, Quot.sound`.

So for `n ≤ 12`,

  **`k[S_n] ≃ₐ[k] ∏_{μ ⊢ n} End_k(S^μ)`**

over any characteristic-zero field, sorry-free and axiom-free.

## What the bridge costs

Two index changes, both already available:

* `SpechtClassification.partitionEquivYoungIndex : Nat.Partition n ≃ PartitionIndex n` — and the
  diagram it produces is *definitionally* `RSKBurnsideTarget.partitionShape`, since both are
  `YoungDiagram.ofRowLens` of the weakly-decreasingly sorted parts;
* `SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux` — the two SYT encodings in this corpus
  (0-indexed `BraidKnot`, 1-indexed `Mathlib`) have the same count.

## Honest scope

`n ≤ 12` only **in this file**. The general case is exactly `RSKBurnsideHolds n` for general `n`,
which is the RSK correspondence — and the Schensted programme this paragraph pointed at has since
landed it (`QOU.Mathlib.rskBurnsideHolds`). The unconditional split is
`SpechtWedderburnGeneral.spechtEquiv`; this file is retained as the small-`n` route, which needs no
RSK at all.

**Corrected 2026-08-23.** This paragraph used to continue: *"Nothing here proves it, and
`sn_isotypic_specht_split` — stated for all `n` — remains open, as do the two keystones that
inherit `sorryAx` from it."* That is no longer the state of the world:
`sn_isotypic_specht_split`'s `sorry` became the class `SnIsotypicSpechtSplit`, which is now
**inhabited** (`SnIsotypicSpechtSplitInstance`). Likewise `RSKBridge.RSK_substrate_axiom` is no
longer an `axiom` — it is a theorem, proved from the same result. Check with `#print axioms` rather
than by reading imports, as before.

## Base ring (§7c)

`variable {k : Type} [Field k] [CharZero k]`. No `ℝ`.
-/

namespace QOU.BraidKnot.SpechtWedderburnLe12

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open QOU.BraidKnot.SpechtWedderburnCriterion
open Equiv (Perm)
open Module

variable {k : Type} [Field k] [CharZero k]

/-- The diagram attached to a partition by `partitionEquivYoungIndex` is the one
`RSKBurnsideTarget.partitionShape` names: both are `ofRowLens` of the weakly-decreasingly sorted
parts. -/
theorem diagram_partitionEquiv (n : ℕ) (p : Nat.Partition n) :
    (partitionEquivYoungIndex n p).diagram = QOU.Mathlib.partitionShape p := rfl

/-- `#SYT` in the `BraidKnot` (0-indexed) encoding agrees with `dimSYT`, which is stated in the
`Mathlib` (1-indexed) encoding. -/
theorem numSYT_partitionEquiv (n : ℕ) (p : Nat.Partition n) :
    numSYT (partitionEquivYoungIndex n p).diagram = QOU.Mathlib.dimSYT p := by
  rw [diagram_partitionEquiv]
  exact SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux _

/-- **Reindexing the RSK/Burnside identity** from `Nat.Partition n` onto `PartitionIndex n`, which
is the index the Specht machinery uses. -/
theorem sum_numSYT_sq_of_rskBurnside (n : ℕ) (h : QOU.Mathlib.RSKBurnsideHolds n) :
    ∑ i : PartitionIndex n, (numSYT i.diagram) ^ 2 = Nat.factorial n := by
  classical
  rw [← Equiv.sum_comp (partitionEquivYoungIndex n) (fun i => (numSYT i.diagram) ^ 2), ← h]
  exact Finset.sum_congr rfl (fun p _ => by rw [numSYT_partitionEquiv])

/-- **The Wedderburn split of `k[S_n]`, unconditionally, for `n ≤ 12`.**

`k[S_n] ≃ₐ[k] ∏_{μ ⊢ n} End_k(S^μ)` over any characteristic-zero field: partition-indexed, block
`μ` acting on the Specht module `S^μ`.

Everything the split needs is proved — the commutant is the base field (W2), the map is
partition-indexed and block-sized by construction, and it is injective — leaving only the count
`Σ_μ (#SYT μ)² = n!`, which the corpus proves for `n ≤ 12` with no RSK correspondence
(`PartitionsOfBridge.rskBurnsideHolds_le12`).

`-- Ref: [sagan2001] §1.10, §2.4; [james1984representation]`. -/
noncomputable def spechtEquiv_le12 (n : ℕ) (hn : n ≤ 12) :
    MonoidAlgebra k (Perm (Fin n)) ≃ₐ[k]
      (∀ i : PartitionIndex n, Module.End k (SpechtSubmodule (k := k) i.diagram)) :=
  spechtEquiv_of_sum_sq (k := k) n
    (sum_sq_of_numSYT (k := k) n
      (sum_numSYT_sq_of_rskBurnside n
        (QOU.Mathlib.PartitionsOfBridge.rskBurnsideHolds_le12 n (by simp [Nat.lt_succ_of_le hn]))))

/-- The bijectivity statement behind `spechtEquiv_le12`, for callers that want the map rather than
the equivalence. -/
theorem spechtProduct_bijective_le12 (n : ℕ) (hn : n ≤ 12) :
    Function.Bijective (SpechtActionInjective.spechtProduct (k := k) n) :=
  spechtProduct_bijective_of_sum_sq (k := k) n
    (sum_sq_of_numSYT (k := k) n
      (sum_numSYT_sq_of_rskBurnside n
        (QOU.Mathlib.PartitionsOfBridge.rskBurnsideHolds_le12 n (by simp [Nat.lt_succ_of_le hn]))))

end QOU.BraidKnot.SpechtWedderburnLe12
