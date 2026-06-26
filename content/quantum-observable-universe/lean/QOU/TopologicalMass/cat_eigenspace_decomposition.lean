import Mathlib.Data.Real.Basic

/-!
# QOU.TopologicalMass.cat_eigenspace_decomposition — orthogonal mass decomposition

**Lemma** ([`lem:topological-mass-cat-eigenspace`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.md)).

Let `α = (∫_A ⊗ id) ∘ Δ ∘ ρ` be the categorical mass integrand of a
closed cycle `ρ`. When the Frobenius pairing is compatible with the
`*`-involution, the descent involution `τ̂_n` gives an orthogonal
decomposition of `α` into descended and transient components:

`m(ρ) = ‖tr(τ̂_n(α))‖ + ‖tr(α − τ̂_n(α))‖`.

## Formalisation notes

- **Honest statement (§1, §1a).** The conclusion is the *actual*
  manuscript equation — the mass `m(ρ)` splits as the sum of the
  descended-component norm `‖tr(τ̂_n(α))‖` and the transient-component
  norm `‖tr(α − τ̂_n(α))‖`. The descended and transient pieces are built
  from the genuine operators `τ̂_n`, `tr`, `‖·‖` applied to `α` and to the
  *algebraic* orthogonal complement `α − τ̂_n(α)`. This replaces the
  earlier laundered tautology `α = α_descended + α_transient` (routed
  through a fictitious `intermediate_sum`), which assumed its own
  conclusion.
- The non-trivial content is **norm-additivity over the orthogonal split**
  (`*`-compatible Frobenius pairing ⇒ Pythagoras), which needs the
  inner-product / orthogonality infrastructure; the body is an **honest
  `sorry`** with a manuscript citation (§1a item 2), not a self-assuming
  projection.
- **Base ring (§7c).** `ℝ`: the mass norm is an archimedean (real) norm.

-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.md
-/

namespace QOU.TopologicalMass

/-- Data of the orthogonal mass-decomposition lemma: the integrand `α`,
    the descent involution `τ̂_n`, the trace `tr`, the mass norm `‖·‖`,
    and the total mass `m(ρ)`. -/
class CatEigenspaceDecompositionContext where
  /-- Categorical mass integrand `α` (modelled in `ℝ`). -/
  α : ℝ
  /-- Descent involution `τ̂_n`. -/
  tau_hat : ℝ → ℝ
  /-- Frobenius categorical trace `tr`. -/
  tr : ℝ → ℝ
  /-- Mass norm `‖·‖`. -/
  nrm : ℝ → ℝ
  /-- Total mass `m(ρ)` of the closed cycle. -/
  m_rho : ℝ

/-- **Orthogonal decomposition of the categorical mass**
    ([`lem:topological-mass-cat-eigenspace`]).

    `m(ρ) = ‖tr(τ̂_n(α))‖ + ‖tr(α − τ̂_n(α))‖`, the descended-plus-transient
    split under the `*`-compatible Frobenius pairing. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.md
theorem cat_eigenspace_decomposition [ctx : CatEigenspaceDecompositionContext] :
    ctx.m_rho
      = ctx.nrm (ctx.tr (ctx.tau_hat ctx.α))
        + ctx.nrm (ctx.tr (ctx.α - ctx.tau_hat ctx.α)) := by
  sorry

end QOU.TopologicalMass
