/-
  Spectator normalization factor.

  S(Z_spec, N_spec) = a^{Z_spec} × b^{N_spec} where
  a = Σ_c G_P(c) = −h/2 and b = Σ_c G_N(c).

  Ref: [manuscript] Ch 11 §9 / spectator-normalization
-/

import Mathlib.RingTheory.RootsOfUnity.Basic

namespace QOU.ParticleInteractions

/-- Spectator normalization: product of per-nucleon channel sums
    for unchanged nucleons in a beta decay. -/
-- Ref: [manuscript] Ch 11 §9 / spectator-normalization
noncomputable def SpectatorNormalization
    (q : ℝ) (_hq : q > 1) (Z_spec N_spec : ℕ) : ℝ :=
  let h := q - q⁻¹
  let a := -h / 2
  let _b := -3 * (q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (4 * q ^ 3)
  sorry

end QOU.ParticleInteractions
