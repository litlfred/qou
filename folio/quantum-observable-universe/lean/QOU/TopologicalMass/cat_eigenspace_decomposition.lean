import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.TopologicalMass.cat_eigenspace_decomposition — orthogonal mass decomposition

**Lemma** ([`lem:topological-mass-cat-eigenspace`](../../../mass-endomorphism/topological-mass-cat-eigenspace.md)).

Let `α = (∫_A ⊗ id) ∘ Δ ∘ ρ` be the categorical mass integrand of a
closed cycle `ρ`. When the Frobenius pairing is compatible with the
`*`-involution, the descent involution `τ̂_n` gives an orthogonal
decomposition of `α` into descended and transient components:

`m(ρ) = ‖tr(τ̂_n(α))‖ + ‖tr(α − τ̂_n(α))‖`.

## 2026-09-03 — the docstring described a repair that was never made

This module's own notes said:

> *"the body is an **honest `sorry`** with a manuscript citation (§1a item
> 2), not a self-assuming projection."*

The body was `ctx.decomposition` — the projection — and the file contained no
`sorry` at all.  Fifth file in this drain whose prose asserts the repair while
the code does the opposite.

Its neighbouring sentence is accurate and worth keeping, because it records
that this file has been through one repair already: the version before that
laundered `α = α_descended + α_transient` through a fictitious
`intermediate_sum`.  So the history is tautology → projection-described-as-
`sorry`, and both descriptions were written at the time of the code they
describe.

## `nrm` was a free function, so the statement was not about norms

Beyond the projection: `α`, `tau_hat`, `tr`, `nrm` and `m_rho` were all class
**fields**, so the instance chose them.  In particular `nrm : ℝ → ℝ` is an
arbitrary function — nothing makes it a norm, sub-additive, or even
non-negative — and `tr` likewise.  A `[CatEigenspaceDecompositionContext]`
binder therefore assumed nothing, and the equation it carried was not a claim
about traces and norms but about three unconstrained functions.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

`cat_eigenspace_decomposition` is now a **`Prop`-valued definition over
caller-supplied data**, and two genuinely different things are separated:

* `split_eq` — the **algebraic** identity `α = τ̂α + (α − τ̂α)`, proved by
  `ring`. This is a tautology and is stated here **as** one, because it is
  precisely what the pre-2026 version laundered as the lemma's content. It
  holds for every `τ̂` whatever, so it says nothing about descent.
* `transient_antiInvariant` — real content: if `τ̂` is additive on differences
  and involutive, the transient component is **anti-invariant**,
  `τ̂(α − τ̂α) = −(α − τ̂α)`. That is the eigenspace statement the lemma's name
  promises, and it is proved sorry-free.
* `not_cat_eigenspace_decomposition_of_free_data` — the norm-additivity
  equation is refutable at free data, so a `sorry` over it would read as
  "true, not yet proved" about something false.

## What is still open, stated rather than implied

**Norm-additivity itself.** This is the lemma's whole content, and it is
**not** Pythagoras. Pythagoras for the `*`-compatible Frobenius pairing gives
additivity of *squared* norms, `‖a + b‖² = ‖a‖² + ‖b‖²`. For two non-zero
orthogonal vectors it forces the triangle inequality to be **strict**
(`QOU.Torsion.norm_add_lt_of_inner_eq_zero`, PR #8581). An earlier version of
this docstring called norm-additivity "Pythagoras"; that was wrong. Norm
additivity holds iff the two trace values lie on a common ray
(`QOU.Torsion.mass_decomposition_eq_iff`), i.e. share a sign or phase, and
that is open (beans `qou-27ys`, `qou-tmeq`). It also cannot be stated honestly
while `nrm` is an arbitrary `ℝ → ℝ`. Nothing in this file builds `α` from
`(∫_A ⊗ id) ∘ Δ ∘ ρ`, the descent involution `τ̂_n`, the Frobenius trace, or the
`*`-involution.

**Base ring (§7c).** `ℝ`: the mass norm is an archimedean (real) norm.

Bean `qou-z9ws`.

-- Ref: [leitner2026] quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.md
-/

namespace QOU.TopologicalMass

/-- **The algebraic split is a tautology**, and is recorded as one.

`α = τ̂(α) + (α − τ̂(α))` holds for every function `τ̂` whatever — no descent,
no involution, no pairing. It is stated here because an earlier version of
this file presented exactly this identity, routed through a fictitious
`intermediate_sum`, as the lemma's content. Naming it as trivial is what
keeps it from being mistaken for the claim again. -/
theorem split_eq (tau_hat : ℝ → ℝ) (α : ℝ) :
    α = tau_hat α + (α - tau_hat α) := by
  ring

/-- **The transient component is anti-invariant** — the eigenspace content of
the lemma's name, derived.

If the descent map is additive on differences and involutive, then
`τ̂(α − τ̂α) = −(α − τ̂α)`: the transient part lies in the `−1` eigenspace of
`τ̂`. Sorry-free, and independent of any norm or pairing. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.md
theorem transient_antiInvariant {tau_hat : ℝ → ℝ}
    (hsub : ∀ x y, tau_hat (x - y) = tau_hat x - tau_hat y)
    (hinv : ∀ x, tau_hat (tau_hat x) = x) (α : ℝ) :
    tau_hat (α - tau_hat α) = -(α - tau_hat α) := by
  rw [hsub, hinv]; ring

/-- **Orthogonal decomposition of the categorical mass**
([`lem:topological-mass-cat-eigenspace`]), as a proposition over
caller-supplied data:

`m(ρ) = ‖tr(τ̂_n(α))‖ + ‖tr(α − τ̂_n(α))‖`.

**Named, not asserted.** Read the module docstring first: with `nrm` and `tr`
arbitrary functions this is not yet a statement about norms or traces, and
the norm-additivity that is the lemma's actual content is open. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-endomorphism/topological-mass-cat-eigenspace.md
def cat_eigenspace_decomposition (m_rho α : ℝ) (tau_hat tr nrm : ℝ → ℝ) : Prop :=
  m_rho = nrm (tr (tau_hat α)) + nrm (tr (α - tau_hat α))

/-- **The decomposition is refutable at freely-chosen data**, which is why it
is named rather than carried as a `sorry`.

With every function constantly zero and `m(ρ) = 1` it reads `1 = 0`. -/
theorem not_cat_eigenspace_decomposition_of_free_data :
    ¬ cat_eigenspace_decomposition 1 0 (fun _ => 0) (fun _ => 0) (fun _ => 0) := by
  simp [cat_eigenspace_decomposition]

end QOU.TopologicalMass
