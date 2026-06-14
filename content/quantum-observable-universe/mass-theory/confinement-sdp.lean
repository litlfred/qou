import QOU.Basic

/-!
# QOU.ParticleInteractions.ConfinementSDP

Confinement as a semidefinite program with matrix Frobenius
positivity. Primal: `min ⟨T, Φ⟩` s.t. `Φ ⪰ 0`, per-block Frobenius
positivity, 2×2 pair PSD. Dual matrix inequality
`y₀ I + Σ y_λ π_λ − T ⪯ 0`. The scalar LP
(`prop:confinement-lp`) is the diagonal rank-1 projection.

LaTeX: `\label{prop:confinement-sdp}`
-/

namespace QOU.ParticleInteractions

class ConfinementSDPData where
  primalOpt : ℝ
  nTarget : ℝ
  y0Star : ℝ
  slaterStrictFeasible : Prop

/-- **Confinement SDP primal–dual**.
    At any `(P, q)` with Slater-strict feasibility, strong duality holds
    between the primal matrix-Frobenius SDP and the dual matrix shadow prices. -/
-- Ref: [manuscript] prop:confinement-sdp
theorem confinement_sdp [ctx : ConfinementSDPData] (h : ctx.slaterStrictFeasible) :
    ctx.primalOpt = ctx.nTarget * ctx.y0Star := by
  sorry

end QOU.ParticleInteractions
