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
  /-- The ambient space of the primal variable `Φ`.  A field because this
      class held three real optima and no primal variable at all, so there
      was nothing for Slater's condition to quantify over. -/
  Primal : Type
  /-- Strict positive-definiteness `Φ ≻ 0`. -/
  PosDef : Primal → Prop
  /-- The primal feasible set. -/
  Feasible : Primal → Prop
  primalOpt : ℝ
  nTarget : ℝ
  y0Star : ℝ
  /-- Strong duality, hypothesised on **Slater's condition itself** rather
      than on a proposition the instance picks.

      `slaterStrictFeasible : Prop` was a field typed with the universe
      `Prop`, so `strong_duality` read as Slater-conditional while its
      antecedent was whatever the instance chose — `True` included, which
      makes the implication unconditional.

      (Needs abstract LP/SDP duality infrastructure that does not exist in
      Mathlib; kept as an honest assumption for models without
      certificates.) -/
  strong_duality : (∃ Φ : Primal, PosDef Φ ∧ Feasible Φ) →
    primalOpt = nTarget * y0Star

/-- **Slater's condition** for a given SDP context: a strictly feasible
    point exists.  Restores the name `slaterStrictFeasible` as a definition
    over the carried cone, so call sites read as before while the
    proposition is now fixed rather than chosen. -/
def ConfinementSDPData.slaterStrictFeasible (ctx : ConfinementSDPData) : Prop :=
  ∃ Φ : ctx.Primal, ctx.PosDef Φ ∧ ctx.Feasible Φ

/-- **Confinement SDP primal–dual**.
    At any `(P, q)` with Slater-strict feasibility, strong duality holds
    between the primal matrix-Frobenius SDP and the dual matrix shadow prices. -/
-- Ref: [leitner2026] prop:confinement-sdp
theorem confinement_sdp [ctx : ConfinementSDPData] (h : ctx.slaterStrictFeasible) :
    ctx.primalOpt = ctx.nTarget * ctx.y0Star := by
  exact ctx.strong_duality h

end QOU.ParticleInteractions
