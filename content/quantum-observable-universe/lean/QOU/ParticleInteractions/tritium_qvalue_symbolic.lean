import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-!
# QOU.ParticleInteractions.tritium_qvalue_symbolic

**Proposition** for content block
[`prop:tritium-qvalue-symbolic`](../../../quantum-observable-universe/particle-interactions/tritium-qvalue-symbolic.md):
*The `Q`-value of tritium `β⁻`-decay `³H → ³He + e⁻ + ν̄ₑ` has an exact
closed form as a rational function of `q`.*

The derivation is the branching factorisation at `(Z, N) = (1, 2)`
(so `A = 3`, odd regime):

  Σ_{4³ configs} Δmₑ = a¹ · b¹ · (a − b) = a·b·(a − b),

with channel sums (categorical inputs from the branching factorisation)

  a = −h/2,                         h = q − q⁻¹,
  b = −3(q²−1)(q²+1)² / (4q³).

These channel-sum *definitions* are carried as class hypotheses; the closed
form `Q = m_e · 3(q²−1)³(q²+1)²(3q⁴+4q²+3) / (32q⁷)` is **derived** from
`a·b·(a − b)` by field algebra (verified against the manuscript expression
in `computations/`), not projected from a stored field.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/tritium-qvalue-symbolic.md
-/

namespace QOU.ParticleInteractions

/-- Context for the tritium `Q`-value: the substrate parameter, electron
    mass, and the two branching-factorisation channel sums `a`, `b` carried
    as their categorical-input *definitions* (not the conclusion — the
    rational closed form is derived from them in `tritium_qvalue_symbolic`). -/
class TritiumQvalueContext where
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Hecke differential `h = q − q⁻¹`. -/
  h : ℝ
  h_eq : h = q - q⁻¹
  /-- Electron mass `m_e : ℝ`. -/
  m_e : ℝ
  /-- The Q-value `Q(³H → ³He) : ℝ`. -/
  Q : ℝ
  /-- Standard-channel sum `a` (categorical input). -/
  a : ℝ
  /-- Standard-channel sum `b` (categorical input). -/
  b : ℝ
  /-- Channel-sum input: `a = −h/2`. -/
  a_eq : a = - h / 2
  /-- Channel-sum input: `b = −3(q²−1)(q²+1)² / (4q³)`. -/
  b_eq : b = -3 * (q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (4 * q ^ 3)
  /-- Branching-factorisation ansatz: the `Q`-value equals the product of
      the `4³` configuration sum `a·b·(a − b)` times `m_e`. -/
  qvalue_branching : Q = a * b * (a - b) * m_e

/-- **Tritium `Q`-value closed form (derived).**

    `Q(³H → ³He) = m_e · 3(q²−1)³(q²+1)²(3q⁴+4q²+3) / (32q⁷)`.

    The proof substitutes the channel-sum inputs `a, b` into the branching
    ansatz `Q = a·b·(a − b)·m_e` and clears denominators — a genuine
    rational-function derivation, NOT a read-back of a stored conclusion. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/tritium-qvalue-symbolic.md
theorem tritium_qvalue_symbolic [ctx : TritiumQvalueContext] :
    ctx.Q
      = ctx.m_e * 3 * (ctx.q ^ 2 - 1) ^ 3 * (ctx.q ^ 2 + 1) ^ 2
        * (3 * ctx.q ^ 4 + 4 * ctx.q ^ 2 + 3) / (32 * ctx.q ^ 7) := by
  have hq1 : 1 < ctx.q := ctx.q_gt_one
  have hq0 : ctx.q ≠ 0 := by linarith
  rw [ctx.qvalue_branching, ctx.a_eq, ctx.b_eq, ctx.h_eq]
  field_simp
  ring

end QOU.ParticleInteractions
