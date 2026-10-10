import QOU.Mathlib.SchenstedPartitionShape
import QOU.Mathlib.PartitionListBridge

/-!
# QOU.MathlibExt.CarrierReindexBridge — the `Nat.Partition ↔ YoungDiagram` reindex facts

The two facts that let the `Nat.Partition n`-carrier fake-degree sum be reindexed to the
`{ν : YoungDiagram // card = n}`-carrier telescope sum, via `partitionShapeEquiv`:

* `numStandardYoungTableaux` of the equiv-image is the partition's `dimSYT` (definitional);
* the equiv-image's `rowLens` is the partition's `toList`.

Both import only already-built corpus modules. Used by `NormalizedSumClosure` to discharge the
reindex step of the telescope closure of `normalizedSum n q = 1`.
-/

namespace QOU.MathlibExt.CarrierReindexBridge

open QOU.Mathlib
open QOU.Mathlib.PartitionListBridge (toList)

variable {n : ℕ}

/-- The SYT count of the `partitionShapeEquiv`-image is the partition's `dimSYT` (definitional:
`dimSYT p := numStandardYoungTableaux (partitionShape p)`). -/
theorem numSTY_partitionShapeEquiv (p : Nat.Partition n) :
    numStandardYoungTableaux
        ((partitionShapeEquiv n p : {ν : YoungDiagram // ν.cells.card = n}) : YoungDiagram)
      = dimSYT p := by
  rw [partitionShapeEquiv_apply]; rfl

/-- The `rowLens` of the `partitionShapeEquiv`-image is the partition's `toList`. -/
theorem rowLens_partitionShapeEquiv (p : Nat.Partition n) :
    ((partitionShapeEquiv n p : {ν : YoungDiagram // ν.cells.card = n}) : YoungDiagram).rowLens
      = toList p := by
  rw [partitionShapeEquiv_apply]
  exact YoungDiagram.rowLens_ofRowLens_eq_self
    (fun x hx => p.parts_pos ((Multiset.mem_sort _).mp hx))

end QOU.MathlibExt.CarrierReindexBridge
