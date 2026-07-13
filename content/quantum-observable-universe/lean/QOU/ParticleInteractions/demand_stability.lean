import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# QOU.ParticleInteractions.demand_stability

**Canonical declaration** for content block
[`prop:demand-stability`](../../../quantum-observable-universe/particle-interactions/demand-stability.md): *Demand profile determines nuclear and atomic stability*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.ParticleInteractions

/-- Abstract context for the `demand_stability` claim —
    manuscript-themed typed fields below. -/
class DemandStabilityContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- The derived atom `𝓐(Z, N) : Type`. -/
  Atom : Type
  /-- Demand magnitude `|dem(𝓐(Z, N))| = Σ_{c_w < 0} |c_w|` of the
      atom at `(Z, N)`. -/
  dem_mag : ℕ → ℕ → ℝ
  /-- Markov-trace `tr_M(𝓐(Z, N))`. -/
  trM : ℕ → ℕ → ℝ

/-- The physical hypotheses carried by the Periodic Table Demand Conjecture.
    (Carried as quantified hypotheses, not directly as conclusion fields). -/
class PeriodicTableDemandConjecture (ctx : DemandStabilityContext) : Prop where
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
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/demand-stability.ts
theorem demand_stability (ctx : DemandStabilityContext) [hc : PeriodicTableDemandConjecture ctx] :
    (ctx.dem_mag ctx.Z ctx.N ≤ ctx.dem_mag (ctx.Z + 1) (ctx.N - 1) ∧
     ctx.dem_mag ctx.Z ctx.N ≤ ctx.dem_mag (ctx.Z - 1) (ctx.N + 1)) ∧
    ctx.dem_mag ctx.Z ctx.N = 0 ∧
    (ctx.trM ctx.Z ctx.N ≤ ctx.trM (ctx.Z + 1) ctx.N ∧
     ctx.trM ctx.Z ctx.N ≤ ctx.trM (ctx.Z - 1) ctx.N ∧
     ctx.trM ctx.Z ctx.N ≤ ctx.trM ctx.Z (ctx.N + 1) ∧
     ctx.trM ctx.Z ctx.N ≤ ctx.trM ctx.Z (ctx.N - 1)) :=
  by refine ⟨hc.is_beta_stable, hc.is_shell_closed, hc.is_doubly_magic⟩

end QOU.ParticleInteractions
