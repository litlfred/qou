import Mathlib.Tactic

/-!
# QOU.TopologicalMass.cat_transient_localises_blowup

**Lemma** ([`lem:topological-mass-cat-transient`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-cat-transient.md)).

*The transient component `α − τ̂ₙ(α) ∈ 𝓐_{n+1}^{trans}` has support
contained in the union of the kernels of `𝔡_{n+1}` at the blow-up
centres `p₁, …, p_N`, and the transient trace decomposes as a sum of
disjoint local contributions:*

    tr(α − τ̂ₙ(α)) = Σ_{i=1}^{N} tr_trans(ϱ, p_i).

## Structure (hypothesis vs. derivation)

The `.md` lemma has two clauses.  The **first clause** — the transient
component is supported on the kernels of the jet differential
`𝔡_{n+1}` at the disjoint blow-up centres, i.e. it decomposes in the
observation algebra as a sum of local pieces — is the genuine open
geometric input (jet-filtration support analysis, not in Mathlib).  It
is stated as the sub-lemma `CatTransient.transient_decomposition` with
an honest `sorry` + citation (AGENTS.md §1, §1a item 2).

The **second clause** — the displayed trace identity — is *derived*:
the Frobenius trace is additive (carried in the type `ℝ →+ ℝ`), so
applying it to the decomposition and distributing over the finite sum
(`map_sum`) yields `tr(α − τ̂ₙ(α)) = Σᵢ tr_trans(ϱ, pᵢ)`.  The
conclusion is NOT assumed as a field; only the support decomposition
is (the shape of the .md's first clause) — per the
lean-proof-vacuity-audit fix recipe and AGENTS.md §3b-cond item 5.

## Model

The observation algebra `𝓐_{n+1}` and the trace codomain are modelled
additively on `ℝ` via named `opaque` constants (an `opaque` constant
needs a concrete inhabited carrier, so a generic `R` per §7c is not
available here; `ℝ` matches the archimedean trace values used
downstream in this chapter).  `tr_trans(ϱ, pᵢ)` is *defined* as the
trace of the `i`-th local component, not assumed.
-/

namespace QOU.TopologicalMass

namespace CatTransient

/-- Number of blow-up centres `N`. -/
opaque N : ℕ

/-- The categorical mass integrand `α` at level `n + 1` (modelled in
    the observation algebra, here additively on `ℝ`). -/
opaque alpha : ℝ

/-- The descent projector `τ̂ₙ` on the level-`(n+1)` observation
    algebra. -/
opaque tauHat : ℝ → ℝ

/-- The Frobenius categorical trace `tr`, additive on the observation
    algebra (additivity of the trace is standard and carried in the
    bundled-hom type, not assumed as a sub-hypothesis). -/
opaque trFrob : ℝ →+ ℝ

/-- The local transient piece supported in `ker 𝔡_{n+1}` at the `i`-th
    blow-up centre `p_i`. -/
opaque localComponent : ℕ → ℝ

/-- The local transient-trace contribution `tr_trans(ϱ, p_i)` at the
    `i`-th blow-up centre — *defined* as the trace of the `i`-th local
    component. -/
noncomputable def traceLocal (i : ℕ) : ℝ := trFrob (localComponent i)

class CatTransientInputs : Prop where
  /-- Open input -/
  decomp : alpha - tauHat alpha = ∑ i ∈ Finset.range N, localComponent i

/-- **Open geometric input (the .md's first clause).**  The transient
    component `α − τ̂ₙ(α)` is supported on the kernels of `𝔡_{n+1}` at
    the disjoint blow-up centres, hence decomposes in the observation
    algebra as the sum of the local pieces.  Needs the jet-filtration
    support analysis (kernel support + disjointness of the centres),
    not in Mathlib. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-transient.md
theorem transient_decomposition [ctx : CatTransientInputs] :
    alpha - tauHat alpha
      = ∑ i ∈ Finset.range N, localComponent i :=
  ctx.decomp

end CatTransient

open CatTransient in
/-- **Transient trace localises to the blow-up centres**
    ([`lem:topological-mass-cat-transient`]).

`tr(α − τ̂ₙ(α)) = Σ_{i<N} tr_trans(ϱ, p_i)`.  *Derived* (not assumed):
apply the additive trace to the support decomposition
`transient_decomposition` and distribute over the finite sum via
`map_sum`. -/
theorem cat_transient_localises_blowup [CatTransientInputs] :
    trFrob (alpha - tauHat alpha)
      = ∑ i ∈ Finset.range N, traceLocal i := by
  rw [transient_decomposition]
  exact map_sum trFrob localComponent (Finset.range N)

end QOU.TopologicalMass
