import QOU.BraidKnot.SpechtCentralC2Scalar
import QOU.BraidKnot.SpechtWedderburnGeneral
import QOU.BraidKnot.SnWedderburnPartitionBridge
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv

/-!
# QOU.BraidKnot.SnIsotypicSpechtSplitInstance — the keystone class, inhabited

`SnWedderburnPartitionBridge.SnIsotypicSpechtSplit R` axiomatises the isotypic Wedderburn split of
`R[S_n]` in matrix form, together with the statement that it sends the Jucys–Murphy central element
`C₂` to the family of block scalars `contentSqSum`. A large part of the corpus is stated
conditionally on it — `OVTopAssembly`, `RSKBurnsideDischarge`, `BurnsideDischarge`,
`PieceASpechtCharacter`, `PlancherelNormalisation` — and until now **nothing inhabited it**.

**`instance : SnIsotypicSpechtSplit k`** for any characteristic-zero field `k`. Everything it needs
is proved:

* the split itself, for every `n`, is `SpechtWedderburnGeneral.spechtEquiv` — which exists because
  `QOU.Mathlib.rskBurnsideHolds` (epic `qou-nrex`, brick 42) discharged the count;
* the matrix form is `algEquivMatrix (Module.finBasis …)`, a basis choice, applied blockwise;
* the `C₂` statement is `SpechtCentralC2Scalar.spechtProduct_centralC2`, and an algebra equivalence
  carries `c • 1` to `c • 1`.

## What this discharges

Every `[SnIsotypicSpechtSplit ℚ]` hypothesis in the corpus is now satisfiable by instance
resolution, so the results carrying it are unconditional.

Note the direction of the dependency, because it is the reverse of the one the corpus previously
had: `RSKBurnsideDischarge.rskBurnsideHolds` derives the RSK/Burnside identity *from* this class.
This instance is built from `QOU.Mathlib.rskBurnsideHolds`, which is proved from the Robinson–
Schensted correspondence with no hypothesis at all — so the identity is not being assumed anywhere
in this chain.

## Base ring

Any characteristic-zero field. The class's use sites are all at `ℚ`, but the construction is
generic — the split, the matrix form and the `C₂` alignment never mention `ℚ` — so the instance is
stated where it actually holds.
-/

namespace QOU.BraidKnot.SnIsotypicSpechtSplitInstance

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open Equiv (Perm)

variable {k : Type} [Field k] [CharZero k]

/-- Each Specht block, as a matrix algebra of its own rank. -/
noncomputable def blockMatrix (μ : YoungDiagram) :
    Module.End k (SpechtSubmodule (k := k) μ) ≃ₐ[k]
      Matrix (Fin (Module.finrank k (SpechtSubmodule (k := k) μ)))
             (Fin (Module.finrank k (SpechtSubmodule (k := k) μ))) k :=
  algEquivMatrix (Module.finBasis k (SpechtSubmodule (k := k) μ))

/-- **The split, in the matrix form the keystone states.** -/
noncomputable def matrixSplit (n : ℕ) :
    MonoidAlgebra k (Perm (Fin n)) ≃ₐ[k]
      (∀ i : PartitionIndex n,
        Matrix (Fin (Module.finrank k (SpechtSubmodule (k := k) i.diagram)))
               (Fin (Module.finrank k (SpechtSubmodule (k := k) i.diagram))) k) :=
  (SpechtWedderburnGeneral.spechtEquiv (k := k) n).trans
    (AlgEquiv.piCongrRight (fun i => blockMatrix (k := k) i.diagram))

/-- **The split sends `C₂` to the block scalars.** -/
theorem matrixSplit_centralC2 (n : ℕ) :
    matrixSplit (k := k) n (RegularRepTrace.centralC2 n)
      = fun i : PartitionIndex n =>
          ((JucysMurphy.contentSqSum i.diagram : ℤ) : k) •
          (1 : Matrix (Fin (Module.finrank k (SpechtSubmodule (k := k) i.diagram)))
                      (Fin (Module.finrank k (SpechtSubmodule (k := k) i.diagram))) k) := by
  funext i
  show blockMatrix (k := k) i.diagram
      (SpechtWedderburnGeneral.spechtEquiv (k := k) n (RegularRepTrace.centralC2 n) i) = _
  rw [show (SpechtWedderburnGeneral.spechtEquiv (k := k) n (RegularRepTrace.centralC2 n) i)
        = SpechtActionInjective.spechtProduct (k := k) n (RegularRepTrace.centralC2 n) i from rfl,
    SpechtCentralC2Scalar.spechtProduct_centralC2, map_zsmul, map_one,
    Int.cast_smul_eq_zsmul]

/-- **The keystone class is inhabited**, over any characteristic-zero field.

The class's use sites are all at `ℚ`, but nothing in the construction is: the split, the matrix
form and the `C₂` alignment are all generic, so the instance is stated where it actually holds. -/
instance instSnIsotypicSpechtSplit :
    QOU.BraidKnot.SnWedderburnPartitionBridge.SnIsotypicSpechtSplit k where
  exists_split n := ⟨matrixSplit (k := k) n, matrixSplit_centralC2 (k := k) n⟩

end QOU.BraidKnot.SnIsotypicSpechtSplitInstance
