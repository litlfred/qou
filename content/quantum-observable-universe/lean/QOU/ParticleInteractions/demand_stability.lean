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
    manuscript-themed typed fields below; sub-claims encode (i)
    stable, (ii) unstable, (iii) phase-boundary regimes of the
    atom `𝓐(Z, N)`. -/
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
  /-- Manuscript sub-claim (i) — Beta stability: for every single-
      nucleon exchange at fixed `A = Z + N`, `|dem(Z, N)|` is the
      minimum among neighbouring `(Z ± 1, N ∓ 1)`. -/
  claim_i_beta_stable :
    dem_mag Z N ≤ dem_mag (Z + 1) (N - 1) ∧
    dem_mag Z N ≤ dem_mag (Z - 1) (N + 1)
  /-- Manuscript sub-claim (ii) — Shell-closed: noble-gas-like atom
      has empty demand (all NF coefficients non-negative). -/
  claim_ii_shell_closed : dem_mag Z N = 0
  /-- Markov-trace `tr_M(𝓐(Z, N))`. -/
  trM : ℕ → ℕ → ℝ
  /-- Manuscript sub-claim (iii) — Doubly magic: the atom is a local
      minimum of `tr_M` among neighbours `(Z ± 1, N ± 1)`. -/
  claim_iii_doubly_magic :
    trM Z N ≤ trM (Z + 1) N ∧ trM Z N ≤ trM (Z - 1) N ∧
    trM Z N ≤ trM Z (N + 1) ∧ trM Z N ≤ trM Z (N - 1)

/-- **Proposition statement** (from manuscript):

The derived atom $\mathcal{A}(Z, N)$ is:*

1.

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/demand-stability.ts
theorem demand_stability [ctx : DemandStabilityContext] :
    (ctx.dem_mag ctx.Z ctx.N ≤ ctx.dem_mag (ctx.Z + 1) (ctx.N - 1) ∧
     ctx.dem_mag ctx.Z ctx.N ≤ ctx.dem_mag (ctx.Z - 1) (ctx.N + 1)) ∧
    ctx.dem_mag ctx.Z ctx.N = 0 ∧
    (ctx.trM ctx.Z ctx.N ≤ ctx.trM (ctx.Z + 1) ctx.N ∧
     ctx.trM ctx.Z ctx.N ≤ ctx.trM (ctx.Z - 1) ctx.N ∧
     ctx.trM ctx.Z ctx.N ≤ ctx.trM ctx.Z (ctx.N + 1) ∧
     ctx.trM ctx.Z ctx.N ≤ ctx.trM ctx.Z (ctx.N - 1)) :=
  by refine ⟨ctx.claim_i_beta_stable, ctx.claim_ii_shell_closed, ctx.claim_iii_doubly_magic⟩

end QOU.ParticleInteractions
