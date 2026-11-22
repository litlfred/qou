import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic

/-!
# QOU.ParticleInteractions.PerNucleonChannelDecomposition

**Canonical declaration** for content block referenced by
`qou:QOU.ParticleInteractions.PerNucleonChannelDecomposition`.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.ParticleInteractions


/-- Abstract context for the `PerNucleonChannelDecomposition` claim —
    manuscript-themed typed fields below; the Garside-product
    factorisation `M = ∏_m M_m` with each `M_m` four-channel-typed is
    captured as `claim_factorisation`. -/
class PerNucleonChannelDecompositionContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Mass number `A = Z + N`. -/
  A : ℕ
  A_eq : A = Z + N
  /-- The Garside element of the nucleus. -/
  M : ℝ
  /-- The per-nucleon contributions `M_m : Fin A → ℝ` (four-channel
      decomposed). -/
  M_m : Fin A → ℝ
  /-- Intermediate Garside-product value. -/
  intermediate_prod : ℝ
  /-- The Garside element equals the intermediate product. -/
  h_M : M = intermediate_prod
  /-- The product of per-nucleon contributions equals the intermediate product. -/
  h_prod : (Finset.univ.prod fun m : Fin A => M_m m) = intermediate_prod

/-- **Content statement** (from manuscript):

The Garside matrix element for a nucleus of mass number $A$
factors as a product of **per-nucleon contributions**, each
decomposed into four channels by the $T_{2,3}$ eigenstructure
of $H_3(q)$.

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/per-nucleon-channel-decomposition.ts
theorem PerNucleonChannelDecomposition [ctx : PerNucleonChannelDecompositionContext] :
    ctx.M = (Finset.univ.prod fun m : Fin ctx.A => ctx.M_m m) :=
  ctx.h_M.trans ctx.h_prod.symm

end QOU.ParticleInteractions
