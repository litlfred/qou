import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.Topology.Order.Basic

/-!
# QOU.FluidDynamics.TownsendBiotSavart

Rigorous algebraic content of `rem:townsend-biot-savart-strain`.

The remark studies the Townsend evolution
$$
  dV_1/dt = +2\,\alpha(t)\,V_1 + 2\nu, \qquad
  dV_2/dt = -2\,\alpha(t)\,V_2 + 2\nu,
$$
under the singular Biot–Savart strain
$\alpha(t) = 1/(2(T^\ast - t))$.  In the time-to-collision variable
$\tau = T^\ast - t$ the system becomes the linear pair
$$
  \tau\,V_1' + V_1 = -2\nu\tau, \qquad
  \tau\,V_2' - V_2 = -2\nu\tau,
$$
with the exact solutions
$$
  V_1(\tau) = C_1/\tau - \nu\tau, \qquad
  V_2(\tau) = -2\nu\tau\ln\tau + C_2\,\tau.
$$

What this file rigorously establishes:

1. The two candidate functions and their formal derivatives
   satisfy the linearised ODE pair *algebraically* — `ring`-level
   computations, no calculus library needed.
2. The squared aspect ratio admits the closed form
   $\kappa^2(\tau) = V_2/V_1 = \tau^2(-2\nu\ln\tau + C_2)/
   (C_1 - \nu\tau^2)$.
3. Near collision the numerator scales as $\tau^2\ln\tau$ (which
   tends to $0$) while the denominator tends to a positive
   constant; therefore $\kappa^2 \to 0$ — the
   "first-order branch (B)" claim in `conj:levi-degeneracy`.

(3) uses `Real.log` and an asymptotic fact about $\tau^2 \log \tau$;
the asymptotic limit is left as a Lean `sorry` with a citation to
Townsend, since carrying it out cleanly requires the
`Filter`/`Tendsto` toolkit and a `Real.log`-asymptotic auxiliary
that is currently not on this Lean toolchain.  The closed-form
identity (2) is fully verified.

LaTeX label: `rem:townsend-biot-savart-strain`
-/

namespace QOU.FluidDynamics

namespace TownsendBiotSavart

/-- Candidate solution along the stretching axis,
    $V_1(\tau) = C_1/\tau - \nu\tau$. -/
noncomputable def V1 (C₁ ν τ : ℝ) : ℝ := C₁ / τ - ν * τ

/-- Formal derivative of `V1` w.r.t. $\tau$:
    $V_1'(\tau) = -C_1/\tau^2 - \nu$. -/
noncomputable def V1' (C₁ ν τ : ℝ) : ℝ := -(C₁ / τ ^ 2) - ν

/-- Candidate solution along the compressing axis,
    $V_2(\tau) = -2\nu\tau\ln\tau + C_2\,\tau$. -/
noncomputable def V2 (ν C₂ τ : ℝ) : ℝ :=
  -2 * ν * τ * Real.log τ + C₂ * τ

/-- Formal derivative of `V2` w.r.t. $\tau$:
    $V_2'(\tau) = -2\nu\ln\tau - 2\nu + C_2$. -/
noncomputable def V2' (ν C₂ τ : ℝ) : ℝ :=
  -2 * ν * Real.log τ - 2 * ν + C₂

/-- **ODE-1 holds algebraically.**  The pair `(V1, V1')` satisfies
    $\tau\,V_1' + V_1 = -2\nu\tau$. -/
theorem V1_satisfies_ODE (C₁ ν τ : ℝ) (hτ : τ ≠ 0) :
    τ * V1' C₁ ν τ + V1 C₁ ν τ = -2 * ν * τ := by
  unfold V1 V1'
  field_simp
  ring

/-- **ODE-2 holds algebraically.**  The pair `(V2, V2')` satisfies
    $\tau\,V_2' - V_2 = -2\nu\tau$. -/
theorem V2_satisfies_ODE (ν C₂ τ : ℝ) :
    τ * V2' ν C₂ τ - V2 ν C₂ τ = -2 * ν * τ := by
  unfold V2 V2'
  ring

/-- Closed form for the squared core aspect ratio
    $\kappa^2(\tau) = V_2(\tau)/V_1(\tau)$, factored to expose the
    $\tau^2$ smallness at the collision. -/
theorem kappa_squared_closed_form
    (C₁ C₂ ν τ : ℝ) (hτ : τ ≠ 0) (hden : C₁ - ν * τ ^ 2 ≠ 0) :
    V2 ν C₂ τ / V1 C₁ ν τ
      = τ ^ 2 * (-2 * ν * Real.log τ + C₂) / (C₁ - ν * τ ^ 2) := by
  unfold V1 V2
  field_simp

/-- Helper: the limiting denominator $C_1 - \nu\tau^2$ is positive
    near the collision for $C_1 > 0$. -/
theorem denominator_pos_near_zero
    (C₁ ν : ℝ) (hC : 0 < C₁) :
    ∃ δ > 0, ∀ τ : ℝ, τ ≠ 0 → τ ^ 2 < δ →
      0 < C₁ - ν * τ ^ 2 := by
  by_cases hν : ν ≤ 0
  · refine ⟨1, by norm_num, ?_⟩
    intro τ _ _
    have hτ2 : 0 ≤ τ ^ 2 := sq_nonneg τ
    nlinarith
  · push_neg at hν
    refine ⟨C₁ / ν, by positivity, ?_⟩
    intro τ _ hτ2
    have : ν * τ ^ 2 < C₁ := by
      have hmul : ν * τ ^ 2 < ν * (C₁ / ν) := by
        exact mul_lt_mul_of_pos_left hτ2 hν
      rwa [mul_div_cancel₀ C₁ (ne_of_gt hν)] at hmul
    linarith

/- **First-order branch (B) limit.**  Under the singular
    Biot–Savart strain, the squared core aspect ratio vanishes at
    the collision: $\kappa^2(\tau) \to 0$ as $\tau \to 0^+$.

    The closed form `kappa_squared_closed_form` reduces the claim
    to the standard real-analysis fact $\tau^2 \log \tau \to 0$ as
    $\tau \to 0^+$.  That asymptotic is a Mathlib `Tendsto` fact
    (combining `Real.tendsto_log_div_pow_zero` and continuity); the
    full chain of filter lemmas is mechanical but tangential.  See
    Townsend §IV and Saffman §11.2 for the textbook treatment. -/
-- Ref: [townsend1951]     title: — see content/schema/references.ts
/-- **External theorem (§3b-cond pattern): kappa_squared_tends_to_zero.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
theorem kappa_squared_tends_to_zero_axiom (C₁ C₂ ν : ℝ) (_hC : 0 < C₁) :
    ∀ ε > 0, ∃ δ > 0, ∀ τ :
    ℝ, τ ≠ 0 → 0 < τ → τ < δ →
      |V2 ν C₂ τ / V1 C₁ ν τ| < ε := by
  intro ε hε
  -- The full filter-based limit proof is needed, but we structure the mathematical
  -- reduction to the standard fact τ^2 log τ → 0.
  have h_lim : Filter.Tendsto (fun τ => V2 ν C₂ τ / V1 C₁ ν τ) (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) := by
    -- Strategy: V2/V1 = τ² * (-2ν·log(τ) + C₂) / (C₁ - ν·τ²)
    -- Numerator: τ² * (-2ν·log(τ) + C₂) → 0 since τ²·log(τ) → 0 and τ² → 0
    -- Denominator: C₁ - ν·τ² → C₁ > 0
    -- Key Mathlib fact: tendsto_log_mul_rpow_nhdsGT_zero : log(x) * x^r → 0 for r > 0
    have h_tau2_log : Filter.Tendsto (fun τ => Real.log τ * τ ^ (2 : ℝ)) (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) :=
      tendsto_log_mul_rpow_nhdsGT_zero (by norm_num : (0 : ℝ) < 2)
    -- τ² → 0
    have h_tau2 : Filter.Tendsto (fun τ : ℝ => τ ^ 2) (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) := by
      have : Filter.Tendsto (fun τ : ℝ => τ) (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) :=
        tendsto_nhdsWithin_of_tendsto_nhds Filter.tendsto_id
      exact (this.pow 2).congr (fun _ => rfl)
    -- V2 τ = τ * (-2ν·log(τ) + C₂), so V2/V1 → 0/C₁ = 0
    -- Use the closed form: V2/V1 = τ² * (-2ν·log(τ) + C₂) / (C₁ - ν·τ²)
    -- Numerator → 0, denominator → C₁ > 0
    -- For numerator: τ²·(-2ν·log(τ) + C₂) = -2ν·(log(τ)·τ²) + C₂·τ²
    have h_num : Filter.Tendsto (fun τ => τ ^ 2 * (-2 * ν * Real.log τ + C₂)) (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) := by
      have h1 : Filter.Tendsto (fun τ => -2 * ν * (Real.log τ * τ ^ (2 : ℝ))) (nhdsWithin 0 (Set.Ioi 0)) (nhds (-2 * ν * 0)) :=
        h_tau2_log.const_mul (-2 * ν)
      simp only [mul_zero] at h1
      have h2 : Filter.Tendsto (fun τ : ℝ => C₂ * τ ^ 2) (nhdsWithin 0 (Set.Ioi 0)) (nhds (C₂ * 0)) :=
        h_tau2.const_mul C₂
      simp only [mul_zero] at h2
      have h_sum := h1.add h2
      simp only [add_zero] at h_sum
      apply h_sum.congr'
      filter_upwards [self_mem_nhdsWithin] with τ hτ
      have hτ_pos : 0 < τ := hτ
      rw [Real.rpow_natCast]
      ring
    -- Denominator → C₁
    have h_den : Filter.Tendsto (fun τ : ℝ => C₁ - ν * τ ^ 2) (nhdsWithin 0 (Set.Ioi 0)) (nhds C₁) := by
      have := h_tau2.const_mul ν
      simp only [mul_zero] at this
      exact (tendsto_const_nhds.sub this)
    -- Since C₁ > 0, denominator is eventually nonzero, and ratio → 0/C₁ = 0
    have hC_ne : C₁ ≠ 0 := ne_of_gt _hC
    -- Use the closed form to rewrite V2/V1
    apply Filter.Tendsto.congr'
    · exact Filter.Tendsto.div h_num h_den hC_ne
    · filter_upwards [self_mem_nhdsWithin] with τ hτ
      have hτ_pos : 0 < τ := hτ
      have hτ_ne : τ ≠ 0 := ne_of_gt hτ_pos
      -- Eventually the denominator is nonzero
      unfold V1 V2
      field_simp
  -- Extract eps-delta from Tendsto
  rw [Metric.tendsto_nhdsWithin_nhds] at h_lim
  rcases h_lim ε hε with ⟨δ, hδ_pos, hδ⟩
  use δ, hδ_pos
  intro τ hτ_ne hτ_pos hτ_lt
  have h_in : τ ∈ Set.Ioi (0 : ℝ) := hτ_pos
  have h_dist : dist τ 0 < δ := by
    rw [Real.dist_eq, sub_zero, abs_of_pos hτ_pos]
    exact hτ_lt
  have h_result := hδ τ h_in h_dist
  rw [Real.dist_eq, sub_zero] at h_result
  exact h_result

theorem kappa_squared_tends_to_zero
    (C₁ C₂ ν : ℝ) (_hC : 0 < C₁) :
    ∀ ε > 0, ∃ δ > 0, ∀ τ : ℝ, τ ≠ 0 → 0 < τ → τ < δ →
      |V2 ν C₂ τ / V1 C₁ ν τ| < ε :=
  kappa_squared_tends_to_zero_axiom C₁ C₂ ν _hC

end TownsendBiotSavart

end QOU.FluidDynamics
