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
   constant; therefore $\kappa^2 \to 0$: the core flattens.

**Re-scoped 2026-10-13 (owner Q1, `Θ = f·ξ♭`).**  `κ²` is the squared core
aspect ratio of the Townsend covariance.  It used to be read as a squared Levi
condition number, and `κ² → 0` as the "first-order branch (B)" of
`conj:levi-degeneracy`.  Both readings are withdrawn: in dimension 3 the Levi
datum of `ker Θ = ξ^⊥` is the single scalar `ξ·curl ξ`, which vanishes for a
straight pair whatever the core shape.  The mathematics below is unchanged.

(3) uses `Real.log` and the asymptotic fact `τ² log τ → 0`; it is proved,
sorry-free, as `kappa_squared_tends_to_zero` (this paragraph previously said it
was a `sorry`, which had been stale since the 2026-08-10 repair recorded in that
theorem's docstring).  The closed-form identity (2) is fully verified.

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

/-- **First-order flattening limit.**  Under the singular Biot–Savart strain,
    the squared core aspect ratio vanishes at the collision:
    `κ²(τ) → 0` as `τ → 0⁺`.

    The closed form `kappa_squared_closed_form` reduces the claim to the
    standard real-analysis fact `τ² log τ → 0`.  See Townsend §IV and
    Saffman §11.2 for the textbook treatment.

    **Now proved, and the surrounding scaffolding was stale.**  Two docstrings
    stood here.  The first said "the full chain of filter lemmas is mechanical
    but tangential"; the second announced an "**External theorem (§3b-cond
    pattern)** … auto-extracted from the single-sorry theorem body … pending
    Mathlib infrastructure", on a declaration named `..._axiom` that a
    *projecting wrapper* `kappa_squared_tends_to_zero` then consumed.

    None of that was true by the time it was read: the declaration was already
    a `theorem`, not an `axiom`, and its body was a real (broken) filter proof.
    The seven errors were Mathlib API drift, not missing infrastructure —
    `Tendsto.pow` landing in `𝓝 (0^2)`, an rpow/natural-power mismatch, a
    `Pi.div` versus pointwise-division mismatch, and an implicit argument
    passed explicitly.  Repaired, the wrapper collapsed into this theorem, and
    the `_axiom` suffix dropped: nothing outside this file referenced it, and
    `#print axioms` gives `[propext, Classical.choice, Quot.sound]`. -/
-- Ref: [townsend1951]     title: — see folio/schema/references.ts
theorem kappa_squared_tends_to_zero (C₁ C₂ ν : ℝ) (_hC : 0 < C₁) :
    ∀ ε > 0, ∃ δ > 0, ∀ τ :
    ℝ, τ ≠ 0 → 0 < τ → τ < δ →
      |V2 ν C₂ τ / V1 C₁ ν τ| < ε := by
  intro ε hε
  -- The full filter-based limit proof is needed, but we structure the mathematical
  -- reduction to the standard fact τ^2 log τ → 0.
  have h_lim : Filter.Tendsto (fun τ => V2 ν C₂ τ / V1 C₁ ν τ)
      (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) := by
    -- V2/V1 = τ²·(-2ν·log τ + C₂) / (C₁ - ν·τ²); numerator → 0, denominator → C₁ > 0.
    have h_tau2 : Filter.Tendsto (fun τ : ℝ => τ ^ 2)
        (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) := by
      have h : Filter.Tendsto (fun τ : ℝ => τ) (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) :=
        tendsto_nhdsWithin_of_tendsto_nhds Filter.tendsto_id
      simpa using h.pow 2
    -- `tendsto_log_mul_rpow_nhdsGT_zero` is stated with an **rpow**; converting to a
    -- natural power here, once, is what the old proof tried to do inside the
    -- `filter_upwards` — where the exponent had already been normalised away, so
    -- `rw [Real.rpow_natCast]` found no `?x ^ ↑?n` to rewrite.
    have h_tau2_log : Filter.Tendsto (fun τ : ℝ => Real.log τ * τ ^ 2)
        (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) := by
      have h := tendsto_log_mul_rpow_nhdsGT_zero (by norm_num : (0 : ℝ) < 2)
      refine h.congr (fun x => ?_)
      rw [show ((2 : ℝ)) = ((2 : ℕ) : ℝ) by norm_num, Real.rpow_natCast]
    have h_num : Filter.Tendsto (fun τ : ℝ => τ ^ 2 * (-2 * ν * Real.log τ + C₂))
        (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) := by
      have h_sum := (h_tau2_log.const_mul (-2 * ν)).add (h_tau2.const_mul C₂)
      simp only [mul_zero, add_zero] at h_sum
      refine h_sum.congr (fun τ => ?_)
      ring
    have h_den : Filter.Tendsto (fun τ : ℝ => C₁ - ν * τ ^ 2)
        (nhdsWithin 0 (Set.Ioi 0)) (nhds C₁) := by
      have h := h_tau2.const_mul ν
      simpa using tendsto_const_nhds.sub h
    have hC_ne : C₁ ≠ 0 := ne_of_gt _hC
    have h_div : Filter.Tendsto
        (fun τ : ℝ => (τ ^ 2 * (-2 * ν * Real.log τ + C₂)) / (C₁ - ν * τ ^ 2))
        (nhdsWithin 0 (Set.Ioi 0)) (nhds 0) := by
      simpa using h_num.div h_den hC_ne
    refine Filter.Tendsto.congr' ?_ h_div
    filter_upwards [self_mem_nhdsWithin] with τ hτ
    have hτ_pos : 0 < τ := hτ
    have hτ_ne : τ ≠ 0 := ne_of_gt hτ_pos
    unfold V1 V2
    -- `field_simp` closes it; the `ring` that used to follow reported
    -- `No goals to be solved`.
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
  -- `τ` is implicit in `Metric.tendsto_nhdsWithin_nhds`'s conclusion; passing it
  -- explicitly put a real where a membership proof was expected.
  have h_result := hδ h_in h_dist
  rw [Real.dist_eq, sub_zero] at h_result
  exact h_result

end TownsendBiotSavart

end QOU.FluidDynamics
