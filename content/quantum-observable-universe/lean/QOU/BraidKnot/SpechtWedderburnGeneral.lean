import QOU.BraidKnot.SpechtWedderburnLe12
import QOU.Mathlib.SchenstedRSKBurnside

/-!
# QOU.BraidKnot.SpechtWedderburnGeneral — the Wedderburn split, unconditionally, for every `n`

`SpechtWedderburnLe12` proved

  **`k[S_n] ≃ₐ[k] ∏_{μ ⊢ n} End_k(S^μ)`**

for `n ≤ 12`, and named its own limit precisely: *"The general case is exactly `RSKBurnsideHolds n`
for general `n`, which is the RSK correspondence and is the subject of the separate multi-session
Schensted programme."* That programme has landed
(`QOU.Mathlib.rskBurnsideHolds`, epic `qou-nrex` brick 42), so the hypothesis is discharged and the
`n ≤ 12` bound comes off.

Nothing else changes. The reduction, the reindexing, the two encoding bridges and the criterion are
all exactly as `SpechtWedderburnLe12` left them; this file substitutes one argument. That the
substitution is all it takes is the point — the split was never waiting on representation theory,
only on the count.

## Honest scope

The split itself, over a characteristic-zero field, for every `n`. This file does **not** address
`SnWedderburnPartitionBridge.sn_isotypic_specht_split` or the keystones that inherit `sorryAx` from
it; whether the general split discharges those is a separate question about how they are stated, and
is not claimed here.

`-- Ref: [sagan2001] §1.10, §2.4; [james1984representation]`.

## Base ring (§7c)

`variable {k : Type} [Field k] [CharZero k]`. No `ℝ`.
-/

namespace QOU.BraidKnot.SpechtWedderburnGeneral

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtClassification
open QOU.BraidKnot.SpechtWedderburnCriterion
open QOU.BraidKnot.SpechtWedderburnLe12
open Equiv (Perm)
open Module

variable {k : Type} [Field k] [CharZero k]

/-- **The Wedderburn split of `k[S_n]`, unconditionally, for every `n`.**

`k[S_n] ≃ₐ[k] ∏_{μ ⊢ n} End_k(S^μ)` over any characteristic-zero field: partition-indexed, block
`μ` acting on the Specht module `S^μ`. -/
noncomputable def spechtEquiv (n : ℕ) :
    MonoidAlgebra k (Perm (Fin n)) ≃ₐ[k]
      (∀ i : PartitionIndex n, Module.End k (SpechtSubmodule (k := k) i.diagram)) :=
  spechtEquiv_of_sum_sq (k := k) n
    (sum_sq_of_numSYT (k := k) n
      (sum_numSYT_sq_of_rskBurnside n (QOU.Mathlib.rskBurnsideHolds n)))

/-- The bijectivity statement behind `spechtEquiv`, for callers that want the map rather than the
equivalence. -/
theorem spechtProduct_bijective (n : ℕ) :
    Function.Bijective (SpechtActionInjective.spechtProduct (k := k) n) :=
  spechtProduct_bijective_of_sum_sq (k := k) n
    (sum_sq_of_numSYT (k := k) n
      (sum_numSYT_sq_of_rskBurnside n (QOU.Mathlib.rskBurnsideHolds n)))

end QOU.BraidKnot.SpechtWedderburnGeneral
