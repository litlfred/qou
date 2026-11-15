import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.Finset.Prod
import Mathlib.Data.Finset.Card
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.IntervalCases

/-!
# QOU.Archimedean.genus_from_hecke_completeness — the embeddable-count half

**Lemma** ([`lem:genus-from-hecke-completeness`](../../../quantum-observable-universe/brings-surface/genus-from-hecke-completeness.md)).

*Let `N g` be the number of torus knots `T_{r,s}` with `r ∈ {2, 3}` whose
Seifert genus is at most `g`.  Then `g = 4` is the least genus at which
`N g ≥ 5`, the number of irreducibles of `H₂(q) ⊕ H₃(q)`.*

## What changed, 2026-09-15

This file previously carried `torusKnotEmbeddingCount` as a hardcoded table
with `| 4 => 5`, and a theorem concluding `torusKnotEmbeddingCount 4 = 5`.
Both were wrong, in the same direction:

* the content block's own table gives **6** at `g = 4`, not 5;
* the table's comment attributed `T_{3,5}` to `g = 3`, while its Seifert
  genus `(3-1)(5-1)/2 = 4` puts it at `g = 4`;
* the understated value was exactly the one that made the `= 5` hold.

The count is now **computed** from the Seifert-genus formula over a `Finset`
rather than tabulated, so it cannot be bent to a theorem's shape again, and
the theorem states the inequality the lemma actually claims (`5 ≤ N 4`).

## What this file does NOT establish

The lemma's companion claim — that the `N 4 = 6` evaluations available at
`g = 4` *span* the 5-dimensional representation — is **false**, and nothing
here should be read as supporting it.  A `T_{r,s}` is the closure of a braid
word on `r` strands, so it evaluates only in the `H_r(q)` columns; the
character matrix is block-diagonal and its rank is bounded by
`min (#r=2 rows) 2 + min (#r=3 rows) 3`.  The two row counts are proved below
(`strandCountTwo_at_four`, `strandCountThree_at_four`), and they give the
bound `2 + 2 = 4 < 5` independently of `q`.  The exact symbolic rank over
`ℚ(q)` is in `computations/audits/genus_completeness_rank_probe.py`; the
scope statement is `rem:torus-evaluation-block-rank`.

-- Ref: [leitner2026] quantum-observable-universe/brings-surface/genus-from-hecke-completeness.md
-/

namespace QOU.Archimedean

/-- Seifert genus of the torus knot `T_{r,s}` for coprime `r < s`:
    `(r-1)(s-1)/2`. -/
def torusKnotGenus (r s : ℕ) : ℕ := (r - 1) * (s - 1) / 2

/-- The torus knots `T_{r,s}` with `r ∈ {2, 3}`, `r < s`, `gcd r s = 1`, of
    Seifert genus at most `g`.  The column bound `2g + 2` is safe: genus at
    most `g` forces `s ≤ 2g + 1` when `r = 2` and `s ≤ g + 1` when `r = 3`. -/
def embeddableTorusKnots (g : ℕ) : Finset (ℕ × ℕ) :=
  (Finset.Icc 2 3 ×ˢ Finset.Icc 2 (2 * g + 2)).filter
    (fun p => p.1 < p.2 ∧ Nat.gcd p.1 p.2 = 1 ∧ torusKnotGenus p.1 p.2 ≤ g)

/-- `N g`, the count of those knots. -/
def torusKnotEmbeddingCount (g : ℕ) : ℕ := (embeddableTorusKnots g).card

/-- The count at `g = 4` is **six**, not five: `T_{2,3}, T_{2,5}, T_{2,7},
    T_{2,9}` from `r = 2` and `T_{3,4}, T_{3,5}` from `r = 3`. -/
theorem torusKnotEmbeddingCount_four : torusKnotEmbeddingCount 4 = 6 := by
  decide

/-- **`g = 4` is the least genus at which the count reaches five.**

    This is the half of `lem:genus-from-hecke-completeness` that is true.
    Stated as an inequality, because the count at `g = 4` is 6; an earlier
    version stated `= 5` and understated the count to match. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/genus-from-hecke-completeness.md
theorem genus_from_hecke_completeness :
    5 ≤ torusKnotEmbeddingCount 4 ∧
    (∀ g < 4, torusKnotEmbeddingCount g < 5) := by
  refine ⟨by decide, ?_⟩
  intro g hg
  interval_cases g <;> decide

/-- Four of the six rows at `g = 4` are two-strand closures. -/
theorem strandCountTwo_at_four :
    ((embeddableTorusKnots 4).filter (fun p => p.1 = 2)).card = 4 := by
  decide

/-- Only **two** of the six are three-strand closures — and that is what
    caps the rank, since the `H₃(q)` block has three columns to fill. -/
theorem strandCountThree_at_four :
    ((embeddableTorusKnots 4).filter (fun p => p.1 = 3)).card = 2 := by
  decide

/-- **The block bound at `g = 4` is four, so the spanning criterion fails.**

    Rank is additive over the blocks of a block-diagonal matrix and each block
    is capped by the smaller of its dimensions, so the rank of the character
    matrix is at most `min r₂ 2 + min r₃ 3` where `rᵢ` is the number of
    `i`-strand rows.  Derived from the two counts above rather than asserted:
    `min 4 2 + min 2 3 = 2 + 2 = 4`. -/
theorem blockRankBound_at_four_lt_five :
    min ((embeddableTorusKnots 4).filter (fun p => p.1 = 2)).card 2
      + min ((embeddableTorusKnots 4).filter (fun p => p.1 = 3)).card 3 < 5 := by
  rw [strandCountTwo_at_four, strandCountThree_at_four]
  decide

end QOU.Archimedean
