import QOU.BraidKnot.ConfinedParticle
import QOU.BraidKnot.ConfinementCategory
import QOU.Descartes.HeckeRep
import QOU.Descartes.HeckeH3
import QOU.Interactions.ConfinementLP

/-!
# Level Sufficiency

For a confined particle `P` admitting normal forms at strand counts
`n₀ ≤ n₁` related by confinement reduction, the Markov trace
coincides on both representations whenever `k_max(P, q) ≤ n₀`.

Justifies computing mass, binding, and Jones polynomial at the
coarsest level (e.g. nucleon-level for atoms) and unfolding to a
deeper level (quark-level) only when `k_max > n` forces it
(magic shell / SDP).

## References

- [prop:level-sufficiency]
- [def:confined-particle]
- [def:confinement-category]
- [jones1987]
-/

namespace QOU.BraidKnot

open QOU.Descartes

/-- Witnessed partition truncation `k_max(P, q)` of the confinement
    SDP at `(P, q)` — the largest Wedderburn block `λ ⊢ k` with
    non-zero projection in the optimal `Φ*`. -/
-- Ref: [manuscript] braids-and-knots/confinement-level
opaque kMax : ConfinedParticle → R_q → ℕ

/-- Markov trace of a confined particle at `(P, q)`. Placeholder —
    the full definition routes through `HeckeRep.character` applied
    to the Markov-class canonical representative, closed under the
    Markov property of the trace tower. For `n = 3`, specialises to
    `markovTraceNF` of `QOU.Interactions.ConfinementLP`. -/
-- Ref: [manuscript] braids-and-knots/wedderburn-mass-formula
-- Ref: [jones1987] https://doi.org/10.2307/1971403
opaque markovTrace : ConfinedParticle → R_q → R_q

/-- **Level sufficiency — typeclass (Pattern 4).**

    Witnesses Markov-trace invariance under an unfolding morphism
    `P → P'` for a *specific* confined-particle pair satisfying the
    coverage hypothesis. The headline result is the Markov tower
    property (Jones), but its formalisation in Lean depends on the
    full `HeckeRep.character` machinery; until then, callers supply
    the witness for the pairs they actually use. -/
-- Ref: [manuscript] braids-and-knots/level-sufficiency
-- Ref: [jones1987] https://doi.org/10.2307/1971403
class LevelSufficient
    (P P' : ConfinedParticle) (q : R_q)
    (_h_unfold : ConfMorphism P P')
    (_h_cover : kMax P q ≤ P.coarseStrands) : Prop where
  /-- Markov trace agrees on the coarse and unfolded reps. -/
  trace_eq : markovTrace P q = markovTrace P' q

/-- **Level sufficiency (headline)** (per-instance form).
    Backed by `LevelSufficient`. -/
-- Ref: [manuscript] braids-and-knots/level-sufficiency
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem LevelSufficiency
    (P P' : ConfinedParticle) (q : R_q)
    (h_unfold : ConfMorphism P P')
    (h_cover : kMax P q ≤ P.coarseStrands)
    [hi : LevelSufficient P P' q h_unfold h_cover] :
    markovTrace P q = markovTrace P' q :=
  hi.trace_eq

/-- **Default-coarse corollary.** The Markov trace at the coarsest
    level satisfying `k_max ≤ n` is exact; deeper unfolding
    produces the same value. -/
-- Ref: [manuscript] braids-and-knots/level-sufficiency
theorem default_coarse_exact
    (P : ConfinedParticle) (q : R_q)
    (h_cover : kMax P q ≤ P.coarseStrands)
    (P' : ConfinedParticle) (h : ConfMorphism P P')
    [LevelSufficient P P' q h h_cover] :
    markovTrace P' q = markovTrace P q :=
  (LevelSufficiency P P' q h h_cover).symm

end QOU.BraidKnot
