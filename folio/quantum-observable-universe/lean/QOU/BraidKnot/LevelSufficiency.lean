import QOU.BraidKnot.ConfinedParticle
import QOU.BraidKnot.ConfinementCategory
import QOU.Archimedean.HeckeRep
import QOU.Archimedean.HeckeH3
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

open QOU.Archimedean

/-- Witnessed partition truncation `k_max(P, q)` of the confinement
    SDP at `(P, q)` — the largest Wedderburn block `λ ⊢ k` with
    non-zero projection in the optimal `Φ*`.

    **Coarse upper bound.** The full SDP-derived value is bounded
    above by the Markov-class strand count: every Wedderburn block
    that supports non-zero `Φ*` weight indexes a partition of size
    `≤ strandCount`. The bound is tight when every block carries
    weight; the slack is precisely the SDP active-support
    multiplicity. We adopt the upper bound here so `kMax` is a
    closed-form definition; per-instance refinements live in
    `LevelSufficient` witnesses. -/
-- Ref: [leitner2026] braids-and-knots/confinement-level
def kMax (P : ConfinedParticle) (_q : R_q) : ℕ :=
  P.markovClass.strandCount

/-- Markov trace of a confined particle at `(P, q)`. Bound by the
    `HasMarkovTrace` typeclass: callers either build `markovTrace`
    via `markovTraceNF` (the n=3 specialisation in `ConfinementLP`)
    or via the full Hecke-character tower (Jones, n ≥ 4). Replacing
    the previous `opaque` with a class makes the data choice
    visible at every use site. -/
-- Ref: [leitner2026] braids-and-knots/wedderburn-mass-formula
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
class HasMarkovTrace (P : ConfinedParticle) (q : R_q) where
  /-- The Markov trace value at `(P, q)`. -/
  value : R_q

/-- Markov trace accessor, backed by `HasMarkovTrace`. -/
noncomputable def markovTrace (P : ConfinedParticle) (q : R_q)
    [h : HasMarkovTrace P q] : R_q :=
  h.value

/-- **Level sufficiency — typeclass (Pattern 4).**

    Witnesses Markov-trace invariance under an unfolding morphism
    `P → P'` for a *specific* confined-particle pair satisfying the
    coverage hypothesis. The headline result is the Markov tower
    property (Jones), but its formalisation in Lean depends on the
    full `HeckeRep.character` machinery; until then, callers supply
    the witness for the pairs they actually use. -/
-- Ref: [leitner2026] braids-and-knots/level-sufficiency
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
class LevelSufficient
    (P P' : ConfinedParticle) (q : R_q)
    [HasMarkovTrace P q] [HasMarkovTrace P' q]
    (_h_unfold : ConfMorphism P P')
    (_h_cover : kMax P q ≤ P.coarseStrands) : Prop where
  /-- Markov trace agrees on the coarse and unfolded reps. -/
  trace_eq : markovTrace P q = markovTrace P' q

/-- **Reflexivity instance**: when `P = P'` syntactically, the
    Markov trace is trivially equal to itself. -/
instance levelSufficient_refl
    (P : ConfinedParticle) (q : R_q) [HasMarkovTrace P q]
    (h_unfold : ConfMorphism P P)
    (h_cover : kMax P q ≤ P.coarseStrands) :
    LevelSufficient P P q h_unfold h_cover :=
  ⟨rfl⟩

/-- **Level sufficiency (headline)** (per-instance form).
    Backed by `LevelSufficient`.

    **Assumed, not derived here** — the body projects
    `LevelSufficient.trace_eq`, so the trace equality is a hypothesis carried
    by the instance argument, not a result established below. Jones is cited
    for the Markov-trace theory the statement is about; it is not the source
    of a proof performed here. The statement is genuinely conditional (`P`,
    `P'`, `q` are arbitrary), so it may not be strengthened to a global
    `axiom`. -/
-- Ref: [leitner2026] braids-and-knots/level-sufficiency
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
def LevelSufficiency
    (P P' : ConfinedParticle) (q : R_q)
    [HasMarkovTrace P q] [HasMarkovTrace P' q]
    (h_unfold : ConfMorphism P P')
    (h_cover : kMax P q ≤ P.coarseStrands)
    [hi : LevelSufficient P P' q h_unfold h_cover] :
    markovTrace P q = markovTrace P' q :=
  hi.trace_eq

/-- **Default-coarse corollary.** The Markov trace at the coarsest
    level satisfying `k_max ≤ n` is exact; deeper unfolding
    produces the same value. -/
-- Ref: [leitner2026] braids-and-knots/level-sufficiency
theorem default_coarse_exact
    (P : ConfinedParticle) (q : R_q)
    [HasMarkovTrace P q]
    (h_cover : kMax P q ≤ P.coarseStrands)
    (P' : ConfinedParticle) [HasMarkovTrace P' q] (h : ConfMorphism P P')
    [LevelSufficient P P' q h h_cover] :
    markovTrace P' q = markovTrace P q :=
  (LevelSufficiency P P' q h h_cover).symm

end QOU.BraidKnot
