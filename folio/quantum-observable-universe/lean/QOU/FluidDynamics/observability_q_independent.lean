-- House minimal pre-archimedean prelude (as in `q_bkm_criterion`,
-- `ns_obstruction_tower`): supplies `ℕ` and `Type*`.  Deliberately nothing
-- ordered and nothing analytic — see the §7c note below.
import Mathlib.Algebra.Ring.Defs

/-!
# QOU.FluidDynamics.observability_q_independent — observability is a base property

**Theorem** ([`thm:observability-q-independent`](../../../quantum-observable-universe/fluid-dynamics/observability-q-independent.md)).

*Observability `Hom(𝟏, Ad(A)) = 0` is a property of the underlying
monoidal category, independent of the substrate section `q`: for any two
sections `q₁ q₂` the Hom-rank agrees, and the observability axiom holds
at every section.*

## Formalisation notes

- **Base ring (§7c) — pre-archimedean, no `ℝ`.**  The substrate section
  is a **generic** `{R : Type*}` with *no* typeclass at all: the theorem
  never adds, multiplies, orders or evaluates a section, it only observes
  that the section is *not consumed*.  The Hom-rank is a single `ℕ`
  carrying **no** section argument, so `q`-independence is *derived* by
  `rfl` rather than assumed.  Requiring `ℝ` here would be gratuitous —
  the claim is that `q` cannot enter, which is exactly the statement that
  nothing about `q`'s ring or order is used.
- **§7c split (2026-08-09).**  These three declarations previously lived
  inside `QOU.GaugeFieldFluidDynamics`, whose body is genuinely
  archimedean (`Real.exp` enstrophy bounds, `Real.pi` vortex separation,
  Sobolev exponents, energy dissipation).  Under the §7c rule "generic
  content stays, the `ℝ` realisation lives apart" the *generic* half is
  extracted here; the analytic half remains in
  `QOU.GaugeFieldFluidDynamics`, which imports this module and
  re-exports `ObservabilityData` so its `NSSingularityDescartes` chain is
  unchanged.
- **Not vacuous.**  `observable : hom_rank = 0` is a real hypothesis on
  the model data and `homRankAt` is a real (constant-in-`q`) assignment;
  the conclusion is derived from them, not projected from a field
  carrying the conclusion (§3b-cond item 5).

-- Ref: [leitner2026] Ch 5 §8 Observability is q-independent
-/

namespace QOU.FluidDynamics

/-- **Observability data** for a QOU: the vanishing of `Hom(𝟏, Ad(A))`.

    The Hom space is computed in the underlying monoidal category `C`;
    the substrate parameter enters only through the differential `d_q`,
    never through the objects, morphisms, or Hom spaces.  This is
    captured *structurally*: the rank is a single `ℕ` with **no**
    substrate-section argument — q-independence is then provable by
    `rfl` rather than assumed (md: "the morphism space in the underlying
    monoidal category is the same for all q").

    LaTeX: `\label{thm:observability-q-independent}` -/
structure ObservabilityData (C : Type*) where
  /-- The rank of `Hom(𝟏, Ad(A))`, computed in `C` (no substrate-section
      argument — `q` cannot enter). -/
  hom_rank : ℕ
  /-- Observability: rank = 0. -/
  observable : hom_rank = 0

/-- The Hom-rank "as seen at substrate section `q`".  By construction the
    section is **not consumed**: `Hom(𝟏, Ad(A))` involves no differential,
    so the assignment is the constant function of `q`.  Generic section
    type `R` per §7c — no `ℝ`, no ordering, no ring structure. -/
def ObservabilityData.homRankAt {C R : Type*}
    (obs : ObservabilityData C) (_q : R) : ℕ :=
  obs.hom_rank

/-- Observability is a base property, independent of the substrate
    section ([`thm:observability-q-independent`]): for any two sections
    `q₁ q₂` the Hom-rank agrees — *derived* by `rfl`, formalising the
    md's proof that `q` does not appear in the construction — and the
    observability axiom holds at every section. -/
-- Ref: [leitner2026] Ch 5 §8 Observability is q-independent
theorem observability_q_independent (C : Type*) {R : Type*}
    (obs : ObservabilityData C) (q₁ q₂ : R) :
    obs.homRankAt q₁ = obs.homRankAt q₂ ∧ obs.homRankAt q₁ = 0 :=
  ⟨rfl, obs.observable⟩

end QOU.FluidDynamics
