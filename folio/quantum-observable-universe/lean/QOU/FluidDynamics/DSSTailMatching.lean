import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.SpecialFunctions.Gamma.Beta
import QOU.FluidDynamics.BeltramiSteadyEuler

/-!
# QOU.FluidDynamics.DSSTailMatching — algebraic core of the non-Galerkin
# route assessment for Part B of `conj:regularity-breakdown`

Bean `qou-innq` (wall: Part B by a non-Galerkin method). Audit:
`docs/audits/2026-11-27-qns-part-b-route-assessment.md`.

Part B asks for a nonzero smooth backward discretely self-similar (DSS) Leray
profile `V(y, s)`, `P`-periodic in `s`, with `|V| ~ |y|⁻¹`. This file proves the
three algebraic facts that the route assessment rests on. All are sorry-free,
use no `axiom`, contain no empirical value, and take no literature theorem as a
hypothesis. Analytic inputs (spherical-harmonic and Fourier decomposition, the
Kummer connection formulas DLMF 13.2.41–13.2.42 and 13.7.1) are cited in the
audit, not assumed here.

## Contents

* **§1 Energy obstruction (abstract).** For `g(c) = A c + Q c` on a real inner
  product space, with `⟪A c, c⟫ < 0` for `c ≠ 0`: if the quadratic part conserves
  the pairing (`⟪Q c, c⟫ = 0`), the only zero is `c = 0`
  (`eq_zero_of_conservative`). Any nonzero zero has strictly positive flux
  `⟪Q c, c⟫ = −⟪A c, c⟫ > 0` (`flux_pos_of_ne_zero`). In the audit `A` is the
  Gaussian-weighted Ornstein–Uhlenbeck part of the Leray operator (at `ν = 1`,
  weight `e^{−|y|²/4}`) and the flux is the weighted radial Bernoulli flux
  `½∮∫ (|V|²/2 + Π)(y·V) e^{−|y|²/4}`. A witness shows the hypotheses admit a
  nonzero solution, so the second theorem is not vacuous
  (`nonzero_solution_witness`).
* **§2 Lamb-gradient profiles see no nonlinearity.** If the Lamb vector
  `u × curl u` is a gradient `∇φ`, then `(u·∇)u = ∇(|u|²/2) − ∇φ`, so the
  nonlinear term is absorbed by the pressure and the Leray system for such a
  profile is the linear Stokes–Leray system (`adv_grad_of_lambGrad`). Beltrami
  fields are the case `φ = 0` (`lambGrad_of_beltrami`).
* **§3 Kummer sector coefficients never vanish.** For the vorticity of a
  linear Stokes–Leray profile, the angular-degree-`l`, Fourier-mode-`μ` sector
  is Kummer's equation with `a = (l + 2)/2 + iμ`, `b = l + 3/2`. The regular
  solution grows like `Γ(b)/Γ(a) · e^z z^{a−b}` and the decaying solution is
  singular at `0` with coefficient `Γ(b − 1)/Γ(a)`. Both coefficients are
  nonzero for every `l` and `μ` (`growth_coeff_ne_zero`,
  `singular_coeff_ne_zero`), which is the algebraic heart of the linear
  Liouville statement in the audit: a linear Stokes–Leray DSS profile in the
  decay class is zero.
-/

namespace QOU.FluidDynamics.DSSTailMatching

open scoped InnerProductSpace

/-! ## §1 Energy obstruction for `A c + Q c = 0` -/

section Energy

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- A strictly dissipative linear part and a pairing-conserving quadratic part
admit only the zero solution of `A c + Q c = 0`. -/
theorem eq_zero_of_conservative (A Q : E → E)
    (hA : ∀ c, c ≠ 0 → ⟪A c, c⟫_ℝ < 0) (hQ : ∀ c, ⟪Q c, c⟫_ℝ = 0)
    {c : E} (h : A c + Q c = 0) : c = 0 := by
  by_contra hc
  have h1 : ⟪A c + Q c, c⟫_ℝ = 0 := by rw [h, inner_zero_left]
  rw [inner_add_left, hQ c, add_zero] at h1
  exact (hA c hc).ne h1

/-- Flux balance: a nonzero solution of `A c + Q c = 0` with strictly
dissipative `A` has `⟪Q c, c⟫ = −⟪A c, c⟫ > 0`. -/
theorem flux_pos_of_ne_zero (A Q : E → E)
    (hA : ∀ c, c ≠ 0 → ⟪A c, c⟫_ℝ < 0)
    {c : E} (h : A c + Q c = 0) (hc : c ≠ 0) :
    ⟪Q c, c⟫_ℝ = -⟪A c, c⟫_ℝ ∧ 0 < ⟪Q c, c⟫_ℝ := by
  have h1 : ⟪A c + Q c, c⟫_ℝ = 0 := by rw [h, inner_zero_left]
  rw [inner_add_left] at h1
  have := hA c hc
  constructor <;> linarith

/-- Non-vacuity: on `ℝ` with `A c = −c` (strictly dissipative) and the
non-conservative quadratic `Q c = c²`, the point `c = 1` is a nonzero solution,
and its flux is `1 > 0`. -/
theorem nonzero_solution_witness :
    (∀ c : ℝ, c ≠ 0 → ⟪-c, c⟫_ℝ < 0) ∧ (-(1 : ℝ)) + 1 ^ 2 = 0 ∧
      0 < ⟪(1 : ℝ) ^ 2, (1 : ℝ)⟫_ℝ := by
  refine ⟨fun c hc => ?_, by norm_num, ?_⟩
  · rw [inner_neg_left]; exact neg_neg_of_pos (real_inner_self_pos.mpr hc)
  · rw [one_pow]; exact real_inner_self_pos.mpr one_ne_zero

end Energy

/-! ## §2 Lamb-gradient profiles -/

section Lamb

open QOU.FluidDynamics.BeltramiSteadyEuler

/-- The Lamb vector `u × curl u` equals `∇φ`. -/
def LambGrad (u : VField) (φ : SField) : Prop :=
  ∀ x y z,
    u.u₂ x y z * u.curl₃ x y z - u.u₃ x y z * u.curl₂ x y z = px φ x y z ∧
    u.u₃ x y z * u.curl₁ x y z - u.u₁ x y z * u.curl₃ x y z = py φ x y z ∧
    u.u₁ x y z * u.curl₂ x y z - u.u₂ x y z * u.curl₁ x y z = pz φ x y z

/-- If the Lamb vector is the gradient `∇φ`, the advection `(u·∇)u` is
`∇(|u|²/2) − ∇φ`, componentwise. The nonlinear term of the Leray system is then
a pure gradient and is absorbed by the pressure. -/
theorem adv_grad_of_lambGrad (u : VField) (hu : u.SlicesDiff) {φ : SField}
    (hφ : LambGrad u φ) (x y z : ℝ) :
    u.adv u.u₁ x y z = px u.ke x y z - px φ x y z ∧
    u.adv u.u₂ x y z = py u.ke x y z - py φ x y z ∧
    u.adv u.u₃ x y z = pz u.ke x y z - pz φ x y z := by
  obtain ⟨h1, h2, h3⟩ := hφ x y z
  refine ⟨?_, ?_, ?_⟩
  · rw [lamb₁ u hu, h1]
  · rw [lamb₂ u hu, h2]
  · rw [lamb₃ u hu, h3]

/-- Beltrami fields (`curl u = λ u`) have Lamb vector `0 = ∇0`. -/
theorem lambGrad_of_beltrami (u : VField) {lam : ℝ} (hb : u.IsBeltrami lam) :
    LambGrad u (fun _ _ _ => 0) := by
  intro x y z
  obtain ⟨c1, c2, c3⟩ := hb x y z
  simp only [px, py, pz, deriv_const']
  refine ⟨?_, ?_, ?_⟩ <;> simp only [c1, c2, c3] <;> ring

end Lamb

/-! ## §3 Kummer sector coefficients -/

section Kummer

open Complex

/-- Kummer parameter `a = (l + 2)/2 + iμ` of the vorticity sector of angular
degree `l` and Fourier frequency `μ` in `s`. -/
noncomputable def sectorA (l : ℕ) (μ : ℝ) : ℂ := ((l : ℂ) + 2) / 2 + (μ : ℂ) * I

/-- Kummer parameter `b = l + 3/2`. -/
noncomputable def sectorB (l : ℕ) : ℂ := (l : ℂ) + 3 / 2

theorem sectorA_re (l : ℕ) (μ : ℝ) : (sectorA l μ).re = ((l : ℝ) + 2) / 2 := by
  simp [sectorA]

theorem sectorA_re_pos (l : ℕ) (μ : ℝ) : 0 < (sectorA l μ).re := by
  rw [sectorA_re]; positivity

theorem sectorB_re (l : ℕ) : (sectorB l).re = (l : ℝ) + 3 / 2 := by
  rw [show sectorB l = (((l : ℝ) + 3 / 2 : ℝ) : ℂ) by simp [sectorB], Complex.ofReal_re]

theorem sectorB_re_pos (l : ℕ) : 0 < (sectorB l).re := by
  rw [sectorB_re]; positivity

theorem sectorB_sub_one_re_pos (l : ℕ) : 0 < (sectorB l - 1).re := by
  rw [Complex.sub_re, sectorB_re, Complex.one_re]
  linarith [(Nat.cast_nonneg l : (0 : ℝ) ≤ l)]

/-- `a` is never a pole of `Γ`: `Γ(a) ≠ 0`, so `1/Γ(a) ≠ 0`. -/
theorem gamma_sectorA_ne_zero (l : ℕ) (μ : ℝ) : Gamma (sectorA l μ) ≠ 0 :=
  Complex.Gamma_ne_zero_of_re_pos (sectorA_re_pos l μ)

/-- The exponential-growth coefficient `Γ(b)/Γ(a)` of the regular Kummer
solution is nonzero in every sector. -/
theorem growth_coeff_ne_zero (l : ℕ) (μ : ℝ) :
    Gamma (sectorB l) / Gamma (sectorA l μ) ≠ 0 :=
  div_ne_zero (Complex.Gamma_ne_zero_of_re_pos (sectorB_re_pos l))
    (gamma_sectorA_ne_zero l μ)

/-- The coefficient `Γ(b − 1)/Γ(a)` of the singular part `z^{1−b}` of the
decaying Kummer solution is nonzero in every sector. -/
theorem singular_coeff_ne_zero (l : ℕ) (μ : ℝ) :
    Gamma (sectorB l - 1) / Gamma (sectorA l μ) ≠ 0 :=
  div_ne_zero (Complex.Gamma_ne_zero_of_re_pos (sectorB_sub_one_re_pos l))
    (gamma_sectorA_ne_zero l μ)

end Kummer

end QOU.FluidDynamics.DSSTailMatching
