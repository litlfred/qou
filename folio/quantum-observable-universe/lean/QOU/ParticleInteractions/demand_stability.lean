import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# QOU.ParticleInteractions.demand_stability

**Canonical declaration** for content block
[`prop:demand-stability`](../../../quantum-observable-universe/particle-interactions/demand-stability.md): *Demand profile determines nuclear and atomic stability*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

## Base ring (§7c)

`Z` and `N` are `ℕ`. The scalars are the demand magnitude `|dem|`, the Markov
trace `tr_M` and the substrate parameter `q`, and the claim only ever compares
them with `≤` or tests `= 0` -- no archimedean construct appears. So the
scalars are a generic ordered commutative ring and the substrate evaluation is
`R := ℝ`.
-/

namespace QOU.ParticleInteractions

variable {R : Type*} [CommRing R] [PartialOrder R]

/-- Abstract context for the `demand_stability` claim —
    manuscript-themed typed fields below. -/
class DemandStabilityContext (R : Type*) [CommRing R] [PartialOrder R] where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Substrate parameter `q`. -/
  q : R
  /-- The derived atom `𝓐(Z, N) : Type`. -/
  Atom : Type
  /-- Demand magnitude `|dem(𝓐(Z, N))| = Σ_{c_w < 0} |c_w|` of the
      atom at `(Z, N)`. -/
  dem_mag : ℕ → ℕ → R
  /-- Markov-trace `tr_M(𝓐(Z, N))`. -/
  trM : ℕ → ℕ → R

/-- The physical hypotheses carried by the Periodic Table Demand Conjecture.
    (Carried as quantified hypotheses, not directly as conclusion fields). -/
class PeriodicTableDemandConjecture (ctx : DemandStabilityContext R) : Prop where
  /-- Beta stability: for every single-nucleon exchange at fixed `A = Z + N`,
      `|dem(Z, N)|` is the minimum among neighbouring `(Z ± 1, N ∓ 1)`. -/
  is_beta_stable :
    ctx.dem_mag ctx.Z ctx.N ≤ ctx.dem_mag (ctx.Z + 1) (ctx.N - 1) ∧
    ctx.dem_mag ctx.Z ctx.N ≤ ctx.dem_mag (ctx.Z - 1) (ctx.N + 1)
  /-- Shell-closed: noble-gas-like atom has empty demand. -/
  is_shell_closed : ctx.dem_mag ctx.Z ctx.N = 0
  /-- Doubly magic: the atom is a local minimum of `tr_M` among neighbours. -/
  is_doubly_magic :
    ctx.trM ctx.Z ctx.N ≤ ctx.trM (ctx.Z + 1) ctx.N ∧
    ctx.trM ctx.Z ctx.N ≤ ctx.trM (ctx.Z - 1) ctx.N ∧
    ctx.trM ctx.Z ctx.N ≤ ctx.trM ctx.Z (ctx.N + 1) ∧
    ctx.trM ctx.Z ctx.N ≤ ctx.trM ctx.Z (ctx.N - 1)


/-- **Proposition statement** (from manuscript):

The derived atom $\mathcal{A}(Z, N)$ is:*

1.

    The Lean encoding below states the manuscript claim conditional on the `PeriodicTableDemandConjecture` hypothesis class. It derives the required inequalities by extracting them from the hypothesis. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/demand-stability.ts
theorem demand_stability (ctx : DemandStabilityContext R) [hc : PeriodicTableDemandConjecture ctx] :
    (ctx.dem_mag ctx.Z ctx.N ≤ ctx.dem_mag (ctx.Z + 1) (ctx.N - 1) ∧
     ctx.dem_mag ctx.Z ctx.N ≤ ctx.dem_mag (ctx.Z - 1) (ctx.N + 1)) ∧
    ctx.dem_mag ctx.Z ctx.N = 0 ∧
    (ctx.trM ctx.Z ctx.N ≤ ctx.trM (ctx.Z + 1) ctx.N ∧
     ctx.trM ctx.Z ctx.N ≤ ctx.trM (ctx.Z - 1) ctx.N ∧
     ctx.trM ctx.Z ctx.N ≤ ctx.trM ctx.Z (ctx.N + 1) ∧
     ctx.trM ctx.Z ctx.N ≤ ctx.trM ctx.Z (ctx.N - 1)) :=
  by refine ⟨hc.is_beta_stable, hc.is_shell_closed, hc.is_doubly_magic⟩

end QOU.ParticleInteractions
