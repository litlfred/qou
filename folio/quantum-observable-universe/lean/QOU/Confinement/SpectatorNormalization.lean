import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.SpectatorNormalization

**Canonical declaration** for content block referenced by
`qou:QOU.ParticleInteractions.SpectatorNormalization`.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.ParticleInteractions



/-- Abstract context for the `SpectatorNormalization` claim —
    manuscript-themed typed fields below; the spectator-count
    identity for `β⁻`-decay is captured. -/
class SpectatorNormalizationContext where
  /-- Proton number `Z` of parent. -/
  Z : ℕ
  /-- Neutron number `N` of parent. -/
  N : ℕ
  /-- Number of converting nucleons (always `1` for `β⁻` decay). -/
  converting : ℕ
  /-- Number of spectator protons (always `Z` for `β⁻` decay). -/
  spectator_p : ℕ
  /-- Number of spectator neutrons (always `N − 1` for `β⁻` decay). -/
  spectator_n : ℕ

/-- **Content statement** (from manuscript):

The **spectator normalization** captures the contribution of
unchanged nucleons to the Q-value character sum.  In a beta
decay ${}^A_Z X \to {}^A_{Z+1} Y + e^- + \bar\nu$, only one
neutron converts to a proton; the remaining $Z$ protons and
$N - 1$ neutrons are spectators.

    The Lean encoding **names** the conditional conjecture as a `Prop`
    (pattern C of the vacuity-fix playbook): the context class is the
    carrier of the spectator-count data, and `SpectatorNormalization`
    is the proposition that the spectator decomposition holds for that
    data.  It is *not* asserted (no `theorem … := ⟨ctx.claim_*⟩`
    self-assuming projection); an instance discharging it is the open
    conditional claim. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/spectator-normalization.ts
def SpectatorNormalization (ctx : SpectatorNormalizationContext) : Prop :=
    ctx.converting = 1 ∧ ctx.spectator_p = ctx.Z ∧ ctx.spectator_n = ctx.N - 1

end QOU.ParticleInteractions
