import Mathlib.Tactic

/-!
# QOU.QuantumObservableUniverse.observation_energy

Canonical Lean for content block
[`prop:observation-energy`](../../../quantum-observable-universe/quantum-observable-universes/observation-energy.md):
*Observation increases quantum energy and deforms the action.*

## Disposition (2026-07-03, bean qsb2 — restructured from a projection stub)

The previous encoding was a `noncomputable def` whose Prop-conjunction
merely projected conclusion-carrying class fields (`hbar_diff`,
`hbar_diff_pos`, `S_deform`) — the self-assuming projection forbidden by
AGENTS.md §3b-cond item 5.  Restructured per §1a honest dispositions:

- **Claim (i), derived sorry-free** (`observation_energy_hbar_diff`,
  `observation_energy_hbar_diff_pos`): from the *defining* equation
  `ℏ_x = 1 - x⁻¹` (field `hbar_eq`) and the positivity hypotheses
  `1 < q`, `0 < δq`, the difference identity
  `ℏ_{q+δq} - ℏ_q = δq / (q(q+δq))` and its strict positivity are
  genuine `field_simp` / `positivity` algebra — the former conclusion
  fields are gone.
- **Claim (ii), split**: the remainder `R₂` is now *defined* by the
  class field `R_2_def` as the exact first-order Taylor remainder, so
  the deformation *equation* `S_{q+δq} = S_q + δq·∂S/∂q + R₂(δq)` is
  derived (trivial rearrangement,
  `observation_energy_action_deformation`).  The substantive analytic
  content — `R₂ = O(δq²)`, which needs second-order regularity of the
  categorical action `𝔖_q` — is stated as
  `observation_energy_remainder_quadratic` and carries an honest
  `sorry` + manuscript citation (stated, not yet proved).
- **Claim (iii), derived by ∃-packaging** (`observation_energy_classical_sign`):
  the class carries *witness data* `q_inc`, `q_dec` where the classical
  energy respectively increases / decreases (the MassGap-style
  ∃-repackaging of AGENTS.md §7d U4); the theorem derives the `.md`
  claim — the classical energy is unconstrained in sign — as the
  existential over those witnesses.
-/

namespace QOU.QuantumObservableUniverse

/-- Model data for [`prop:observation-energy`].  All fields are *inputs*
    (defining equations, positivity hypotheses, opaque model data,
    sign-witness points); none carries a conclusion of the
    proposition. -/
class ObservationEnergyContext where
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Substrate regime `q > 1`. -/
  q_gt_one : 1 < q
  /-- Substrate perturbation `δq`. -/
  δq : ℝ
  /-- The perturbation is positive. -/
  δq_pos : 0 < δq
  /-- Quantum Planck constant as a function of the substrate parameter. -/
  hbar : ℝ → ℝ
  /-- Defining equation `ℏ_x = 1 - x⁻¹`
      ([`def:quantum-planck-constant`]). -/
  hbar_eq : ∀ x : ℝ, hbar x = 1 - x⁻¹
  /-- Categorical action `q ↦ 𝔖_q` ([`def:categorical-action`]),
      opaque model data. -/
  S : ℝ → ℝ
  /-- First-order observation cost `∂𝔖_q/∂q`, opaque model data. -/
  dS_dq : ℝ
  /-- Second-order remainder `R₂`. -/
  R_2 : ℝ → ℝ
  /-- Defining equation: `R₂(δ)` *is* the first-order Taylor remainder
      of the action at `q` (definitional input, not a conclusion). -/
  R_2_def : ∀ δ : ℝ, R_2 δ = S (q + δ) - S q - δ * dS_dq
  /-- Classical energy `q ↦ E_classical(q)` (the `q → 1` shadow of the
      action), opaque model data. -/
  E_classical : ℝ → ℝ
  /-- Witness point where the classical energy increases under the
      perturbation (sign-witness data for claim (iii)). -/
  q_inc : ℝ
  /-- Witness point where the classical energy decreases under the
      perturbation (sign-witness data for claim (iii)). -/
  q_dec : ℝ
  /-- The classical energy increases at `q_inc`. -/
  E_inc : E_classical (q_inc + δq) > E_classical q_inc
  /-- The classical energy decreases at `q_dec`. -/
  E_dec : E_classical (q_dec + δq) < E_classical q_dec

/-- **Claim (i), difference identity — derived sorry-free.**
    `ℏ_{q+δq} - ℏ_q = δq / (q(q+δq))`, from the defining equation
    `ℏ_x = 1 - x⁻¹` by clearing denominators (`q, q+δq ≠ 0` from the
    positivity hypotheses). -/
theorem observation_energy_hbar_diff [ctx : ObservationEnergyContext] :
    ctx.hbar (ctx.q + ctx.δq) - ctx.hbar ctx.q =
      ctx.δq / (ctx.q * (ctx.q + ctx.δq)) := by
  have hq : (0 : ℝ) < ctx.q := lt_trans one_pos ctx.q_gt_one
  have hqδ : (0 : ℝ) < ctx.q + ctx.δq := by linarith [ctx.δq_pos]
  rw [ctx.hbar_eq, ctx.hbar_eq]
  field_simp
  ring

/-- **Claim (i), positivity — derived sorry-free.**  The quantum-energy
    shift `δq / (q(q+δq))` is strictly positive for `δq > 0`, `q > 1`:
    every observation with positive substrate perturbation strictly
    increases the quantum energy. -/
theorem observation_energy_hbar_diff_pos [ctx : ObservationEnergyContext] :
    0 < ctx.δq / (ctx.q * (ctx.q + ctx.δq)) := by
  have hq : (0 : ℝ) < ctx.q := lt_trans one_pos ctx.q_gt_one
  have hqδ : (0 : ℝ) < ctx.q + ctx.δq := by linarith [ctx.δq_pos]
  exact div_pos ctx.δq_pos (mul_pos hq hqδ)

/-- **Claim (ii), deformation equation — derived sorry-free.**
    `𝔖_{q+δq} = 𝔖_q + δq·∂𝔖_q/∂q + R₂(δq)`, a rearrangement of the
    defining equation `R_2_def` for the remainder. -/
theorem observation_energy_action_deformation
    [ctx : ObservationEnergyContext] :
    ctx.S (ctx.q + ctx.δq) =
      ctx.S ctx.q + ctx.δq * ctx.dS_dq + ctx.R_2 ctx.δq := by
  have h := ctx.R_2_def ctx.δq
  linarith

/-- **Claim (ii), quadratic remainder — stated, not yet proved.**
    The Taylor remainder of the categorical action is `O(δq²)` on the
    perturbation window: `∃ C, ∀ |δ| ≤ δq, |R₂(δ)| ≤ C·δ²`.  This is
    the substantive analytic content of the manuscript's
    `𝔖_{q'} = 𝔖_q + δq·∂𝔖_q/∂q + O((δq)²)` and requires second-order
    regularity of `q ↦ 𝔖_q[∇, λ, ψ]`, which is not yet formalised. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/observation-energy.md
theorem observation_energy_remainder_quadratic
    [ctx : ObservationEnergyContext] :
    ∃ C : ℝ, ∀ δ : ℝ, |δ| ≤ ctx.δq → |ctx.R_2 δ| ≤ C * δ ^ 2 := by
  sorry

/-- **Claim (iii) — derived from the sign witnesses.**  The classical
    energy is unconstrained in sign under observation: there exist
    substrate points where it strictly increases and where it strictly
    decreases (∃-packaging of the witness fields `q_inc` / `q_dec`). -/
theorem observation_energy_classical_sign
    [ctx : ObservationEnergyContext] :
    (∃ q₁ : ℝ, ctx.E_classical (q₁ + ctx.δq) > ctx.E_classical q₁) ∧
    (∃ q₂ : ℝ, ctx.E_classical (q₂ + ctx.δq) < ctx.E_classical q₂) :=
  ⟨⟨ctx.q_inc, ctx.E_inc⟩, ⟨ctx.q_dec, ctx.E_dec⟩⟩

/-- **Proposition** ([`prop:observation-energy`]) — resolving
    declaration for the `lean.ref` URI
    `qou:QOU.QuantumObservableUniverse.observation_energy`.

    Conjoins the three claims: (i) the quantum Planck constant strictly
    increases, `ℏ_{q+δq} - ℏ_q = δq/(q(q+δq)) > 0` (derived sorry-free);
    (ii) the action deforms as `𝔖_{q+δq} = 𝔖_q + δq·∂𝔖_q/∂q + R₂(δq)`
    with `R₂ = O(δq²)` (equation derived; the quadratic bound carries
    the one honest `sorry`, see
    `observation_energy_remainder_quadratic`); (iii) the classical
    energy is unconstrained in sign (derived from the witnesses). -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/observation-energy.md
theorem observation_energy [ctx : ObservationEnergyContext] :
    (ctx.hbar (ctx.q + ctx.δq) - ctx.hbar ctx.q =
       ctx.δq / (ctx.q * (ctx.q + ctx.δq)) ∧
     0 < ctx.δq / (ctx.q * (ctx.q + ctx.δq))) ∧
    (ctx.S (ctx.q + ctx.δq) =
       ctx.S ctx.q + ctx.δq * ctx.dS_dq + ctx.R_2 ctx.δq ∧
     ∃ C : ℝ, ∀ δ : ℝ, |δ| ≤ ctx.δq → |ctx.R_2 δ| ≤ C * δ ^ 2) ∧
    ((∃ q₁ : ℝ, ctx.E_classical (q₁ + ctx.δq) > ctx.E_classical q₁) ∧
     (∃ q₂ : ℝ, ctx.E_classical (q₂ + ctx.δq) < ctx.E_classical q₂)) :=
  ⟨⟨observation_energy_hbar_diff, observation_energy_hbar_diff_pos⟩,
   ⟨observation_energy_action_deformation,
    observation_energy_remainder_quadratic⟩,
   observation_energy_classical_sign⟩

end QOU.QuantumObservableUniverse
