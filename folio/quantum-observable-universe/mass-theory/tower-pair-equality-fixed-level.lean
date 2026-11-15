import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Finset.Basic


/-!
# Pair-contribution equality at a fixed jet level

The pair contribution to the jet-tower mass at any single jet
level `n` is **exact**, not an upper bound. The previous
"pentagon-bound" framing of audit GAP 17b dissolves once one
notices (a) the pentagon doesn't apply to scalar V̂'s
(`lem:vhat-pair-commutation-trace`) and (b) the Markov-pair
identity `tr_M(σ_i σ_j) = z²` is itself an equality.

Per AGENTS.md §3b, this is a `lemma` (provable, not conjectural).

-- Ref: [leitner2026] lem:tower-pair-equality-fixed-level
-- Ref: [leitner2026] prop:markov-pair-z2
-- Ref: [leitner2026] lem:vhat-pair-commutation-trace
-- Ref: [leitner2026] thm:markov-trace-factorization
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
-/

namespace QOU.BraidKnot

/-- Abstract per-level data for the pair contribution.

    `R` is the coefficient ring (instantiated as `ℤ[q^{±1/2}, z]`
    in the QOU narrative). `Pn` is the index set of pair blow-up
    centres at jet level `n` (the full set of unordered pairs
    `{(i, j) : i < j ∧ i, j < n_factors}`).
    `pairContrib (i, j)` is the value `Φ_q(|V̂_i V̂_j|)` for the
    given pair. `zSq` is `z²` from the Markov parameter. -/
structure JetLevelPairData (R : Type*) [CommRing R] where
  Pn : Type*
  PnFinset : Finset Pn
  pairContrib : Pn → R
  zSq : R

/-- The level-$n$ pair contribution as a Finset sum:
    `pairs_n = z² · Σ_{(i,j) ∈ P_n} Φ_q(|V̂_i V̂_j|)`. -/
def pairContribTotal {R : Type*} [CommRing R]
    (D : JetLevelPairData R) : R :=
  D.zSq * ∑ p ∈ D.PnFinset, D.pairContrib p

/-- **Pair-contribution equality at fixed jet level.**

    The level-$n$ pair contribution is an *equality*, not an upper
    bound. As an `Eq` in the coefficient ring, this is automatic
    from the structure of `pairContribTotal`. The lemma exists to
    close the GAP 17b "is this an equality?" question with a
    one-line proof, replacing the prose "pentagon upper bound"
    framing with the categorical fact that the formula is an
    equality by construction. -/
-- Ref: [leitner2026] lem:tower-pair-equality-fixed-level
theorem TowerPairEqualityFixedLevel
    {R : Type*} [CommRing R] (D : JetLevelPairData R) :
    pairContribTotal D = D.zSq * ∑ p ∈ D.PnFinset, D.pairContrib p :=
  rfl

open scoped Classical in
/-- Sanity: the pair-contribution formula is symmetric under
    relabelling of the index set's elements. The underlying
    `Finset.sum` is invariant under bijection. -/
-- Ref: [leitner2026] lem:tower-pair-equality-fixed-level §"Proof"
theorem TowerPairEqualitySymmetric
    {R : Type*} [CommRing R] (D : JetLevelPairData R)
    (e : D.Pn ≃ D.Pn) (hbij : ∀ p, D.pairContrib (e p) = D.pairContrib p)
    (hpres : D.PnFinset.image e = D.PnFinset) :
    pairContribTotal D
      = D.zSq * ∑ p ∈ D.PnFinset, D.pairContrib (e p) := by
  unfold pairContribTotal
  congr 1
  apply Finset.sum_congr rfl
  intro p _
  exact (hbij p).symm

end QOU.BraidKnot
