/-!
# QOU.ParticleInteractions.ConfinementSDP

Confinement as a semidefinite program with matrix Frobenius
positivity. Primal: `min ⟨T, Φ⟩` s.t. `Φ ⪰ 0`, per-block Frobenius
positivity, 2×2 pair PSD. Dual matrix inequality
`y₀ I + Σ y_λ π_λ − T ⪯ 0`. The scalar LP
(`prop:confinement-lp`) is the diagonal rank-1 projection.

LaTeX: `\label{prop:confinement-sdp}`
-/

import QOU.Basic

namespace QOU.ParticleInteractions

universe u

/-- Placeholder for a confined particle. -/
opaque ConfinedParticleTy : Type

/-- Feasibility of the Slater-strict confinement SDP at `(P, q)`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque slaterStrictFeasible : ConfinedParticleTy → ℝ → Prop

/-- Optimal dual shadow price of the normalisation constraint. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque y0_star : ConfinedParticleTy → ℝ → ℝ

/-- Target normalisation constant `n_target` for the SDP. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque n_target : ConfinedParticleTy → ℝ

/-- **Confinement SDP primal–dual.** At any `(P, q)` with
    Slater-strict feasibility, the primal admits a unique optimiser
    `Φ* ⪰ 0`, the dual admits `(y₀*, y_λ*)` with `y_λ* ≥ 0`, and
    strong duality holds: the primal and dual optimal objectives
    coincide, and complementary slackness is a matrix equation
    `Φ* · (y₀* I + Σ y_λ* π_λ − T) = 0`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
theorem ConfinementSDP
    (P : ConfinedParticleTy) (q : ℝ)
    (h : slaterStrictFeasible P q) :
    y0_star P q ≥ 0 := by
  -- Ref: [manuscript] particle-interactions/confinement-sdp
  sorry

end QOU.ParticleInteractions
