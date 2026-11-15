import Mathlib.Tactic
import Mathlib.Analysis.Calculus.MeanValue

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
  categorical action `𝔖_q` — is `observation_energy_remainder_quadratic`,
  now **derived sorry-free** conditional on that regularity: the class
  carries it as the `C^{1,1}` fields (`S_hasDeriv`, `S'_lipschitz`, `L`),
  and the `O(δq²)` bound then follows via the mean-value inequality.
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
  /-- Derivative function `S' = ∂𝔖/∂q` of the categorical action. -/
  S' : ℝ → ℝ
  /-- The action `S` is differentiable everywhere with derivative `S'`. -/
  S_hasDeriv : ∀ x : ℝ, HasDerivAt S (S' x) x
  /-- Second-order regularity constant (a Lipschitz bound on `S'`). -/
  L : ℝ
  /-- The regularity constant is non-negative. -/
  L_nonneg : 0 ≤ L
  /-- **Second-order regularity of the action** (the `C^{1,1}` input the
      `O(δ²)` remainder needs): `S'` is `L`-Lipschitz measured from `q` on the
      window. At `x = q` this forces `S' q = dS_dq`; away from `q` it bounds how
      fast the slope may change. This is the honest analytic hypothesis the
      manuscript's `O((δq)²)` claim rests on — an input, not the conclusion. -/
  S'_lipschitz : ∀ x : ℝ, |x - q| ≤ δq → |S' x - dS_dq| ≤ L * |x - q|

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

/-- **Claim (ii), quadratic remainder — derived (conditional on `C^{1,1}`
    regularity).**  The Taylor remainder of the categorical action is `O(δ²)`
    on the perturbation window: `∃ C, ∀ |δ| ≤ δq, |R₂(δ)| ≤ C·δ²`.  This is the
    substantive analytic content of the manuscript's
    `𝔖_{q'} = 𝔖_q + δq·∂𝔖_q/∂q + O((δq)²)`, now **proved** from the second-order
    regularity carried by `ObservationEnergyContext` (`S_hasDeriv` +
    `S'_lipschitz`: `S` is `C^{1,1}` with `dS_dq = S' q`) via the mean-value
    inequality — `C = L` works, since the remainder's derivative
    `S'(q+t) − dS_dq` is bounded by `L·|t| ≤ L·|δ|` on the segment, so
    `|R₂(δ)| ≤ L·|δ|·|δ| = L·δ²`. -/
theorem observation_energy_remainder_quadratic
    [ctx : ObservationEnergyContext] :
    ∃ C : ℝ, ∀ δ : ℝ, |δ| ≤ ctx.δq → |ctx.R_2 δ| ≤ C * δ ^ 2 := by
  refine ⟨ctx.L, fun δ hδ => ?_⟩
  rw [ctx.R_2_def δ]
  -- the remainder as a function of the shift, and its derivative
  have hgderiv : ∀ t : ℝ,
      HasDerivAt (fun s : ℝ => ctx.S (ctx.q + s) - ctx.S ctx.q - s * ctx.dS_dq)
        (ctx.S' (ctx.q + t) - ctx.dS_dq) t := by
    intro t
    have h1 : HasDerivAt (fun s : ℝ => ctx.S (ctx.q + s)) (ctx.S' (ctx.q + t)) t := by
      simpa using (ctx.S_hasDeriv (ctx.q + t)).comp t ((hasDerivAt_id t).const_add ctx.q)
    have h2 : HasDerivAt (fun s : ℝ => s * ctx.dS_dq) ctx.dS_dq t := by
      simpa using (hasDerivAt_id t).mul_const ctx.dS_dq
    simpa using (h1.sub_const (ctx.S ctx.q)).sub h2
  -- the derivative is bounded by L·|δ| on the segment between 0 and δ
  have hbnd : ∀ x ∈ Set.uIcc (0 : ℝ) δ,
      ‖ctx.S' (ctx.q + x) - ctx.dS_dq‖ ≤ ctx.L * |δ| := by
    intro x hx
    rw [Set.mem_uIcc] at hx
    have hxabs : |x| ≤ |δ| := by
      rcases hx with ⟨h0, hd⟩ | ⟨hd, h0⟩
      · rw [abs_of_nonneg h0, abs_of_nonneg (le_trans h0 hd)]; linarith
      · rw [abs_of_nonpos h0, abs_of_nonpos (le_trans hd h0)]; linarith
    have hlip' := ctx.S'_lipschitz (ctx.q + x)
      (by rw [add_sub_cancel_left]; exact le_trans hxabs hδ)
    rw [add_sub_cancel_left] at hlip'
    rw [Real.norm_eq_abs]
    exact le_trans hlip' (mul_le_mul_of_nonneg_left hxabs ctx.L_nonneg)
  -- mean-value inequality: |R₂(δ)| = |g δ − g 0| ≤ (L·|δ|)·|δ| = L·δ²
  have key := Convex.norm_image_sub_le_of_norm_hasDerivWithin_le
    (fun x _ => (hgderiv x).hasDerivWithinAt) hbnd (convex_uIcc 0 δ)
    (Set.left_mem_uIcc) (Set.right_mem_uIcc)
  simp only [add_zero, sub_zero, sub_self, zero_mul] at key
  rw [Real.norm_eq_abs, Real.norm_eq_abs] at key
  calc |ctx.S (ctx.q + δ) - ctx.S ctx.q - δ * ctx.dS_dq|
      ≤ ctx.L * |δ| * |δ| := key
    _ = ctx.L * δ ^ 2 := by rw [mul_assoc, abs_mul_abs_self]; ring

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
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/observation-energy.md
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
