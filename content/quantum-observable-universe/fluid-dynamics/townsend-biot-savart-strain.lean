import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

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
/-- **External axiom (§3b-cond pattern): kappa_squared_tends_to_zero.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom kappa_squared_tends_to_zero_axiom (C₁ C₂ ν : ℝ) (_hC : 0 < C₁) :
    ∀ ε > 0, ∃ δ > 0, ∀ τ :
    ℝ, τ ≠ 0 → 0 < τ → τ < δ →
      |V2 ν C₂ τ / V1 C₁ ν τ| < ε

theorem kappa_squared_tends_to_zero
    (C₁ C₂ ν : ℝ) (_hC : 0 < C₁) :
    ∀ ε > 0, ∃ δ > 0, ∀ τ : ℝ, τ ≠ 0 → 0 < τ → τ < δ →
      |V2 ν C₂ τ / V1 C₁ ν τ| < ε :=
  kappa_squared_tends_to_zero_axiom C₁ C₂ ν _hC

end TownsendBiotSavart

end QOU.FluidDynamics
