import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.ParticleInteractions.positron_correction

**Proposition** for content block
[`prop:positron-correction`](../../../quantum-observable-universe/particle-interactions/positron-correction.md):
*The character sum `Σ_λ χ_λ(Δ)` subtracts the categorical action of both
fermions produced in pair creation (2 units of `m_e`), but the `Q`-value
subtracts only the emitted electron (1 unit). The difference is the positron
action:*

  Q = Σ_char · m_e + 1 · m_e,        the `+1` being `m_{e⁺}/m_e = 1`.

The structural `Q`-value form `Q = (Σ_char + r)·m_e` and the positron
mass-ratio fact `r = 1` are carried as categorical/physical *inputs*; the
boxed identity `Q = Σ_char·m_e + m_e` is **derived** from them by ring
algebra.  The regime-applicability case split is encoded by an `if`-defined
`applied_correction` and both branches are derived, not projected.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/positron-correction.md
-/

namespace QOU.ParticleInteractions

/-- Context for the positron correction.  Carries the categorical character
    sum `Σ_char`, the structural `Q`-value form `Q = (Σ_char + r)·m_e`, and
    the positron mass-ratio `r = m_{e⁺}/m_e = 1` as *inputs*; the corrected
    identity and the regime case split are derived. -/
class PositronCorrectionContext where
  /-- Electron mass `m_e : ℝ`. -/
  m_e : ℝ
  /-- The Q-value `Q : ℝ`. -/
  Q : ℝ
  /-- The character-sum-derived contribution `Σ_char : ℝ`. -/
  «Σ_char» : ℝ
  /-- Positron-to-electron mass ratio `r = m_{e⁺}/m_e` (physical input). -/
  r : ℝ
  /-- Physical input: `m_{e⁺}/m_e = 1`. -/
  positron_ratio_one : r = 1
  /-- Structural `Q`-value form: `Q = (Σ_char + r)·m_e` — the character sum
      plus the positron-action units, scaled by `m_e`. -/
  qvalue_form : Q = («Σ_char» + r) * m_e
  /-- Predicate: the current regime is a pair-creation regime. -/
  is_pair_creation : Prop
  /-- Decidability of the regime predicate (so the `if` is well-formed). -/
  decPairCreation : Decidable is_pair_creation

attribute [instance] PositronCorrectionContext.decPairCreation

/-- The applied positron correction: `m_e` in a pair-creation regime, else
    `0`.  Definition (not a stored conclusion). -/
noncomputable def appliedPositronCorrection [ctx : PositronCorrectionContext] : ℝ :=
  if ctx.is_pair_creation then ctx.m_e else 0

/-- **Corrected `Q`-value identity (derived).**

    `Q = Σ_char · m_e + m_e`, where the `+m_e` is the positron action
    `(m_{e⁺}/m_e)·m_e = 1·m_e`.  Derived from the structural form
    `Q = (Σ_char + r)·m_e` and `r = 1` by ring algebra — not a projection. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/positron-correction.md
theorem positron_correction [ctx : PositronCorrectionContext] :
    ctx.Q = ctx.«Σ_char» * ctx.m_e + ctx.m_e ∧
    (ctx.is_pair_creation → appliedPositronCorrection = ctx.m_e) ∧
    (¬ctx.is_pair_creation → appliedPositronCorrection = 0) := by
  refine ⟨?_, ?_, ?_⟩
  · -- corrected identity: substitute r = 1 into the structural form.
    rw [ctx.qvalue_form, ctx.positron_ratio_one]; ring
  · -- pair-creation regime: the `if` reduces to `m_e`.
    intro hpc; simp [appliedPositronCorrection, hpc]
  · -- non-pair-creation regime: the `if` reduces to `0`.
    intro hnpc; simp [appliedPositronCorrection, hnpc]

end QOU.ParticleInteractions
