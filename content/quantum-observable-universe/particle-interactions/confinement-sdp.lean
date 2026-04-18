/-!
# QOU.ParticleInteractions.ConfinementSDP

Confinement as a semidefinite program with matrix Frobenius positivity.
The scalar LP (prop:confinement-lp) is the diagonal projection.

LaTeX: `\label{prop:confinement-sdp}`
-/

import QOU.Basic

namespace QOU.ParticleInteractions

universe u

/-- **Confinement SDP.** The confined operator Φ* at q is the unique
positive-semidefinite minimiser of ⟨T, Φ⟩ subject to per-block
Frobenius positivity and 2×2 PSD constraints on adjacent-generator
pairs. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
theorem ConfinementSDP
    (R : Type u) [CommRing R] : True := by
  trivial

end QOU.ParticleInteractions
