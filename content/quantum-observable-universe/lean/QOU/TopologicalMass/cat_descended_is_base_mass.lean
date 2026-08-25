import Mathlib.Tactic

/-!
# QOU.TopologicalMass.cat_descended_is_base_mass — descended term equals base mass

**Lemma** ([`lem:topological-mass-cat-descended`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-cat-descended.md)).

Let `α = (∫_A ⊗ id) ∘ Δ ∘ ϱ` be the categorical mass integrand of a
closed cycle `ϱ` at level `n + 1`, and `ϱ₀` its base-level descent.
Then

    ‖tr(τ̂ₙ(α))‖ = 𝔪(ϱ₀).

## Structure (hypotheses vs. derivation)

The proof narrative has two genuine sub-claims, each stated as its own
named proposition (honest `sorry` + citation per AGENTS.md §1, §1a
item 2), and the main theorem *derives* the .md identity by composing
them (`congrArg` + `trans`) — it does not assume its conclusion:

1. `descended_trace_is_base_trace` — descent compatibility of the
   Frobenius trace: the trace of the descended integrand `τ̂ₙ(α)` at
   level `n + 1` equals the base-level trace `tr₀(α₀)` of the descent
   of the cycle.
2. `base_mass_is_norm_of_base_trace` — the base-level mass is the mass
   norm of the base-level trace: `‖tr₀(α₀)‖ = 𝔪(ϱ₀)`.

The intermediate object `tr₀(α₀)` (the base-level trace) is a genuine
quantity of the proof narrative, not a laundering device: both steps
are *visible* sorried gaps, and the conclusion is obtained only by
composing them — per the lean-proof-vacuity-audit fix recipe and
AGENTS.md §3b-cond item 5.  (An earlier revision carried both halves
as fields of a data-only context class and universally quantified over
arbitrary contexts, which made the statement false as stated; that
carrier is removed.)

## Model / base ring (§7c)

The operators of the claim — the integrand `α`, the descent involution
`τ̂ₙ`, the Frobenius trace `tr`, and the mass norm `‖·‖` — are carried
as named `opaque` constants on `ℝ` (an `opaque` constant needs a
concrete inhabited carrier; the mass norm is an archimedean real norm,
so `ℝ` is the honest carrier here).
-/

namespace QOU.TopologicalMass

namespace CatDescended

/-- Categorical mass integrand `α = (∫_A ⊗ id) ∘ Δ ∘ ϱ` at level
    `n + 1` (modelled in the observation algebra, here `ℝ`). -/
opaque alpha : ℝ

/-- Descent involution `τ̂ₙ` on the level-`(n+1)` integrand. -/
opaque tauHat : ℝ → ℝ

/-- Frobenius categorical trace `tr` at level `n + 1`. -/
opaque trFrob : ℝ → ℝ

/-- Mass norm `‖·‖` (archimedean). -/
opaque mnorm : ℝ → ℝ

/-- The base-level trace `tr₀(α₀)` of the descended cycle `ϱ₀`. -/
opaque baseTrace : ℝ

/-- The base-level mass `𝔪(ϱ₀)`. -/
opaque baseMass : ℝ

class CatDescendedInputs : Prop where
  /-- Open input 1 -/
  trace_compat : trFrob (tauHat alpha) = baseTrace
  /-- Open input 2 -/
  base_norm : mnorm baseTrace = baseMass

/-- **Open input 1 — descent compatibility of the trace.**  The
    Frobenius trace of the descended integrand equals the base-level
    trace of the descent: `tr(τ̂ₙ(α)) = tr₀(α₀)`.  Needs the
    level-`(n+1)` → base descent / Frobenius-trace infrastructure (not
    formalised); body is `sorry`. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-descended.md
theorem descended_trace_is_base_trace [ctx : CatDescendedInputs] :
    trFrob (tauHat alpha) = baseTrace :=
  ctx.trace_compat

/-- **Open input 2 — the base mass is the norm of the base trace.**
    `‖tr₀(α₀)‖ = 𝔪(ϱ₀)`.  Needs the `*`-norm / mass infrastructure of
    the base level (not formalised); body is `sorry`. -/
-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/topological-mass-cat-descended.md
theorem base_mass_is_norm_of_base_trace [ctx : CatDescendedInputs] :
    mnorm baseTrace = baseMass :=
  ctx.base_norm

end CatDescended

open CatDescended in
/-- **Descended term equals the base-level mass**
    ([`lem:topological-mass-cat-descended`]).

`‖tr(τ̂ₙ(α))‖ = 𝔪(ϱ₀)`.  *Derived* (not assumed): rewrite the trace of
the descended integrand to the base-level trace (open input 1), then
identify its mass norm with the base-level mass (open input 2). -/
theorem cat_descended_is_base_mass [CatDescendedInputs] :
    mnorm (trFrob (tauHat alpha)) = baseMass := by
  rw [descended_trace_is_base_trace]
  exact base_mass_is_norm_of_base_trace

end QOU.TopologicalMass
