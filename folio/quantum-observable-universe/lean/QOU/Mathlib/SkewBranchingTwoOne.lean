import QOU.Mathlib.SkewBranchingSum
import QOU.Mathlib.SYTHookFormula

/-!
# `QOU.Mathlib.SkewBranchingTwoOne` — `RSKIdentitiesContext` is inhabited

`QOU/BraidKnot/YoungTableauStandard.lean` states

    3 · ∑_{λ ⊢ k}  f^λ · f^{λ/(2,1)}  =  k!        (k ≥ 3)

as `branching_two_one`, conditional on the `[RSKIdentitiesContext]` class, and records that **no
instance of that class exists in this corpus** — so neither it nor `c8_superexp`, which inherits
the same hypothesis, could be applied at any concrete `k`.

This file supplies the instance.  It is the general branching sum
`factorial_mul_skewPair_of_le` at `μ = (2,1)`, where `|μ| = 3` and `f^{(2,1)} = 2`:

    3! · G((2,1), k) = k! · 2     ⟹     3 · G((2,1), k) = k!.

## Not RSK

The file header of `YoungTableauStandard` says this identity "requires massive infrastructure
(the RSK correspondence and hook-length formula)".  The route taken here uses **neither**.  It is
the same lesson its sibling `sum_dimSYT_eq_involution` already recorded: Young's lattice is a
`1`-differential poset, and the up-operator identity (`QOU.Mathlib.upSum_eq`) plus the skew
branching rule (`fDimSkew_branching`) give the whole family by finite combinatorics on
`YoungDiagram` — no insertion, no bumping, no permutation ↔ tableau-pair bijection.

The **one** ingredient taken off the shelf is the single number `f^{(2,1)} = 2`, via the
`decide`-verified small-`n` hook-length bridge `numStandardYoungTableaux_eq_dimHLF_le4`.  That is
a computation on one three-cell shape, not the hook-length formula as a general theorem.

Pure combinatorics; nothing archimedean (§7c); no fit.

## References

- [sagan2001] The Symmetric Group, §2 (branching)
- [leitner2026] bean `qou-b21r`
-/

namespace QOU.BraidKnot.YoungTableauStandard

open Finset QOU.Mathlib YoungDiagram
open QOU.BraidKnot.IdentityI (dimHLF)
open QOU.Mathlib.SYTEnum (numStandardYoungTableaux_eq_dimHLF_le4)

/-- **`f^{(2,1)} = 2`** — the hook shape carries exactly two standard tableaux.  Read off the
`decide`-verified small-`n` hook bridge; a computation on one shape, not the general HLF. -/
theorem numStandardYoungTableaux_mu21 : numStandardYoungTableaux mu21 = 2 :=
  (numStandardYoungTableaux_eq_dimHLF_le4 [2, 1] (by decide) (by decide)).trans (by decide)

/-- The `Nat.Partition`-indexed branching sum is `skewPair mu21`, reindexed by
`partitionShapeEquiv`. -/
theorem sum_dimSYT_mul_fDimSkew_eq_skewPair (k : ℕ) :
    (∑ p : Nat.Partition k, dimSYT p * fDimSkew (partitionShape p) mu21)
      = skewPair mu21 k := by
  unfold skewPair
  refine Fintype.sum_equiv (partitionShapeEquiv k) _ _ (fun p => ?_)
  rw [partitionShapeEquiv_apply]
  rfl

/-- **The classical branching identity at `μ = (2,1)`, unconditionally.**

    3 · ∑_{λ ⊢ k}  f^λ · f^{λ/(2,1)}  =  k!        (k ≥ 3)

This is what `RSKIdentitiesContext.branching_two_one` asks for, and it discharges the class. -/
theorem branching_two_one_holds (k : ℕ) (hk : 3 ≤ k) :
    3 * (∑ p : Nat.Partition k, dimSYT p * fDimSkew (partitionShape p) mu21)
      = Nat.factorial k := by
  have hmain := factorial_mul_skewPair_of_le mu21 k (by rw [mu21_card]; exact hk)
  rw [mu21_card, numStandardYoungTableaux_mu21, show Nat.factorial 3 = 6 from by decide] at hmain
  rw [sum_dimSYT_mul_fDimSkew_eq_skewPair k]
  omega

/-- **The class is inhabited.**  `branching_two_one` and `c8_superexp` are now applicable at every
concrete `k ≥ 3`; until this instance existed neither was. -/
instance rskIdentitiesContextInstance : RSKIdentitiesContext where
  branching_two_one := branching_two_one_holds

end QOU.BraidKnot.YoungTableauStandard
