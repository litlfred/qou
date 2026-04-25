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

import QOU.BraidKnot.ConfinedParticle
import QOU.BraidKnot.ConfinementCategory
import QOU.Descartes.HeckeRep
import QOU.Descartes.HeckeH3
import QOU.Interactions.ConfinementLP

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

/-- **Level sufficiency (headline).** If the coarse representation
    of a confined particle captures its full partition content
    (`k_max(P, q) ≤ n₀`), then the Markov trace is preserved under
    any unfolding morphism `P → P'` in the confinement category.

    Trace-class invariants `𝔉` that factor through `markovTrace`
    (mass, binding, Jones polynomial) therefore agree on `P` and
    `P'` whenever the hypothesis holds. -/
-- Ref: [manuscript] braids-and-knots/level-sufficiency
-- Ref: [jones1987] https://doi.org/10.2307/1971403
axiom LevelSufficiency
    (P P' : ConfinedParticle) (q : R_q)
    (h_unfold : ConfMorphism P P')
    (h_cover : kMax P q ≤ P.coarseStrands) :
    markovTrace P q = markovTrace P' q

/-- **Default-coarse corollary.** The Markov trace at the coarsest
    level satisfying `k_max ≤ n` is exact; deeper unfolding
    produces the same value. -/
-- Ref: [manuscript] braids-and-knots/level-sufficiency
theorem default_coarse_exact
    (P : ConfinedParticle) (q : R_q)
    (h_cover : kMax P q ≤ P.coarseStrands)
    (P' : ConfinedParticle) (h : ConfMorphism P P') :
    markovTrace P' q = markovTrace P q :=
  (LevelSufficiency P P' q h h_cover).symm

end QOU.BraidKnot
