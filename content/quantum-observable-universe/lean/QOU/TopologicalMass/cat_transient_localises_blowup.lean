import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic

/-!
# QOU.TopologicalMass.cat_transient_localises_blowup

**Lemma** ([`lem:topological-mass-cat-transient`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-cat-transient.md)).

*The transient component `α − τ̂ₙ(α) ∈ 𝓐_{n+1}^{trans}` has support
contained in the union of the kernels of `𝔡_{n+1}` at the blow-up
centres `p₁, …, p_N`, and the transient trace decomposes as a sum of
disjoint local contributions:*

    tr(α − τ̂ₙ(α)) = Σ_{i=1}^{N} tr_trans(ϱ, p_i).

## Status

The substantive content is the **localisation**: the transient
component is supported on the kernels of the jet differential `𝔡_{n+1}`
at the blow-up centres, and its trace splits as a sum of disjoint local
contributions.  This rests on the jet-filtration / mass-endomorphism
support analysis (kernel support + disjointness of the blow-up centres),
which is **not available in Mathlib**.

The quantities are modelled as named `opaque` reals — `traceTransient`
(the total transient trace), `traceLocal i` (the local contribution at
`p_i`), with `N` blow-up centres — so the theorem
`traceTransient = Σ_{i<N} traceLocal i` is the genuine unproven
localisation identity between *these specific* objects.  Discharged with
`sorry` per AGENTS.md §1.
-/

namespace QOU.TopologicalMass

open scoped BigOperators

/-- Number of blow-up centres `N`. -/
opaque N : ℕ

/-- The total transient trace `tr(α − τ̂ₙ(α))`. -/
opaque traceTransient : ℝ

/-- The local transient-trace contribution `tr_trans(ϱ, p_i)` at the
    `i`-th blow-up centre. -/
opaque traceLocal : ℕ → ℝ

/-- **Transient trace localises to the blow-up centres.**

The transient trace decomposes as the sum of the disjoint local
contributions at the `N` blow-up centres.  Needs the jet-filtration
support analysis (kernel support + disjointness), not in Mathlib; body
is `sorry`. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-transient.md
theorem cat_transient_localises_blowup :
    traceTransient = (Finset.range N).sum (fun i => traceLocal i) := by
  -- Needs: support(α − τ̂ₙ(α)) ⊆ ⋃ ker 𝔡_{n+1}|_{p_i} and disjointness of
  -- the blow-up centres, giving the disjoint-sum trace decomposition.
  sorry

end QOU.TopologicalMass
