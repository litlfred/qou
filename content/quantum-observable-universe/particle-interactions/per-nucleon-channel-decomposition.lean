/-
  Per-nucleon channel decomposition via S₃ᴬ branching.

  The Garside matrix element for a nucleus of mass number A
  factors as a product of per-nucleon contributions, each
  decomposed into four channels by the T_{2,3} eigenstructure
  of H₃(q).

  Ref: [manuscript] Ch 11 §9 / per-nucleon-channel-decomposition
-/

import Mathlib.RingTheory.RootsOfUnity.Basic

namespace QOU.ParticleInteractions

/-- The four channels from T_{2,3} eigendecomposition. -/
inductive KnotChannel where
  | triv   -- trivial (λ = q³)
  | conf   -- confining (λ = q⁻¹)
  | unconf -- unconfining (λ = −q)
  | sign   -- sign (λ = −q⁻³)

/-- Per-nucleon Garside factor G_N(c) as a function of q and channel. -/
-- Ref: [manuscript] Ch 11 §9 / per-nucleon-channel-decomposition
noncomputable def PerNucleonChannelDecomposition
    (q : ℝ) (_hq : q > 1) (nucleonIsProton : Bool) (_c : KnotChannel) : ℝ :=
  sorry

end QOU.ParticleInteractions
