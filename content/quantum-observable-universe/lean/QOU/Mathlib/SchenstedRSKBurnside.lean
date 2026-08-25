import QOU.Mathlib.SchenstedRSKEquiv
import QOU.Mathlib.SchenstedPartitionShape
import Mathlib.Data.Fintype.Perm

/-!
# QOU.Mathlib.SchenstedRSKBurnside — `∑_{λ ⊢ n} (#SYT λ)² = n!` for every `n`

Brick 42 of epic `qou-nrex` (RSK inverse), and the end of the epic.

**`rskBurnsideHolds`** — Identity-I axiom (i), for general `n`, from the correspondence rather than
from enumeration. Until now it was proved only for `n ≤ 12`, by `rskBurnsideHolds_le12`, a
`decide`-verified route with no RSK in it.

The three steps are all cardinality algebra; the mathematics is behind them:

* `Nat.card (Equiv.Perm (Fin n)) = n!`;
* the correspondence (brick 40) matches permutations with pairs of standard tableaux on a diagram of
  `n` cells;
* `card_pairs_eq_sum` decomposes that subtype — `Equiv.subtypeSigmaEquiv` turns a subtype of a `Σ`
  into a `Σ` over a subtype, brick 41 re-indexes it by `Nat.Partition n`, and `Nat.card_sigma`
  splits the sum. Each fibre is `SYT(λ) × SYT(λ)`, whose count is `dimSYT²`.

The finiteness `Nat.card_sigma` needs is already in place: `Nat.Partition n` is a `Fintype`, and
`StandardYoungTableau μ` carries the `Finite` instance its own file proves by encoding entries on
the cells.

## What this closes

`RSKBurnsideHolds n` was stated in `RSKBurnsideTarget` as a well-typed `Prop` awaiting exactly this
proof, with the comment "General `n` still awaits RSK". It no longer does.
`rskBurnside_imp_substrate` therefore discharges `RSKBridge.RSK_substrate_axiom n` for every `n`,
and `SpechtWedderburnCriterion.spechtEquiv_of_sum_sq` converts the identity into the general
Wedderburn split.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open YoungDiagram

/-- **The pairs of a common shape, counted by partition.** -/
theorem card_pairs_eq_sum (n : ℕ) :
    Nat.card {X : (Σ μ : YoungDiagram, StandardYoungTableau μ × StandardYoungTableau μ) //
        X.1.cells.card = n}
      = ∑ p : Nat.Partition n, (dimSYT p) ^ 2 := by
  rw [Nat.card_congr (Equiv.subtypeSigmaEquiv
      (fun μ : YoungDiagram => StandardYoungTableau μ × StandardYoungTableau μ)
      (fun μ : YoungDiagram => μ.cells.card = n)),
    Nat.card_congr (Equiv.sigmaCongrLeft' (partitionShapeEquiv n).symm), Nat.card_sigma]
  refine Finset.sum_congr rfl (fun p _ => ?_)
  rw [Nat.card_prod, dimSYT, numStandardYoungTableaux, sq, Equiv.symm_symm, partitionShapeEquiv_apply]

/-- **Identity-I axiom (i), for every `n`** — `∑_{λ ⊢ n} (#SYT λ)² = n!`, proved from the
Robinson–Schensted correspondence. -/
theorem rskBurnsideHolds (n : ℕ) : RSKBurnsideHolds n := by
  rw [RSKBurnsideHolds, ← card_pairs_eq_sum n, ← Nat.card_congr (Schensted.rskEquiv n),
    Nat.card_eq_fintype_card, Fintype.card_perm, Fintype.card_fin]

end QOU.Mathlib
