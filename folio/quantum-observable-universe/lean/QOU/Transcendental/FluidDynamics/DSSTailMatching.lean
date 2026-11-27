import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.SpecialFunctions.Gamma.Beta
import QOU.Transcendental.FluidDynamics.BeltramiSteadyEuler

/-!
# QOU.FluidDynamics.DSSTailMatching — algebraic core of the non-Galerkin
# route assessment for Part B of `conj:regularity-breakdown`

Bean `qou-innq` (wall: Part B by a non-Galerkin method). Audit:
`docs/audits/2026-11-27-qns-part-b-route-assessment.md`.

Part B asks for a nonzero smooth backward discretely self-similar (DSS) Leray
profile `V(y, s)`, `P`-periodic in `s`, with `|V| ~ |y|⁻¹`. This file proves the
algebraic facts that the route assessment rests on (§1–§3) and the abstract
radius bounds of the Bernoulli flux route (§4–§5). All are sorry-free,
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
* **§4 Truncation-uniform radius bounds (Bernoulli flux route).** For a
  nonzero zero of `A c + Q c = 0`: if `⟪A c, c⟫ ≤ −κ‖c‖²` and the flux obeys
  `⟪Q c, c⟫ ≤ C‖c‖³`, then `‖c‖ ≥ κ/C` (`norm_ge_of_flux`), with a sharp
  witness. The flux identity alone gives no upper bound: rescaling `Q` by
  `t⁻¹` moves a zero to `t • c` with the same `A` (`zero_rescale`). After
  inverting `A`, a zero of `c + K c = 0` with `K` quadratic satisfies the exact
  radius identity `‖c‖ · ‖K (‖c‖⁻¹ • c)‖ = 1` (`radius_identity`), which gives
  both bounds in terms of `inf` and `sup` of `‖K‖` on the unit sphere
  (`norm_le_of_inf`, `norm_ge_of_sup`), and the blow-up alternative: zeros
  escaping to infinity have directions on which `K` tends to `0`
  (`tendsto_K_dir_zero`).
* **§5 The blow-up set is the Lamb-gradient set.** The advection `(u·∇)u` is a
  gradient `∇(|u|²/2 − ψ)` exactly when the Lamb vector is `∇ψ`
  (`adv_grad_iff_lambGrad`). So the directions along which zeros could escape
  (zeros of the Leray-projected nonlinearity) are the Lamb-gradient fields of
  §2, Beltrami fields included.
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

/-! ## §4 Truncation-uniform radius bounds

Every statement here is about one truncation level, but its constants are the
only thing that depends on the level. So a bound is uniform in the truncation
exactly when its constants (`κ`, `C`, `m`, `M`) are. -/

section RadiusBounds

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- **Non-collapse.** A nonzero zero of `A c + Q c = 0`, with coercive
dissipation `⟪A c, c⟫ ≤ −κ‖c‖²` and a cubic flux bound `⟪Q c, c⟫ ≤ C‖c‖³`,
has `‖c‖ ≥ κ / C`. Only the upper flux bound is needed (the bound has content
when `κ > 0`). -/
theorem norm_ge_of_flux (A Q : E → E) {κ C : ℝ} (hC : 0 < C)
    (hA : ∀ c, ⟪A c, c⟫_ℝ ≤ -κ * ‖c‖ ^ 2)
    (hQ : ∀ c, ⟪Q c, c⟫_ℝ ≤ C * ‖c‖ ^ 3)
    {c : E} (h : A c + Q c = 0) (hc : c ≠ 0) : κ / C ≤ ‖c‖ := by
  have h1 : ⟪A c + Q c, c⟫_ℝ = 0 := by rw [h, inner_zero_left]
  rw [inner_add_left] at h1
  have hA' := hA c
  have hQ' := hQ c
  have hn : 0 < ‖c‖ := norm_pos_iff.mpr hc
  have hn2 : 0 < ‖c‖ ^ 2 := by positivity
  have key : κ * ‖c‖ ^ 2 ≤ (C * ‖c‖) * ‖c‖ ^ 2 := by nlinarith
  have key2 : κ ≤ C * ‖c‖ := le_of_mul_le_mul_right key hn2
  rw [div_le_iff₀ hC]; linarith

/-- Sharpness of `norm_ge_of_flux`: on `ℝ` with `A c = −c` (`κ = 1`) and
`Q c = c²` (flux `c³ ≤ |c|³`, `C = 1`), the zero `c = 1` has `‖c‖ = κ / C`. -/
theorem norm_ge_of_flux_sharp :
    (∀ c : ℝ, ⟪-c, c⟫_ℝ ≤ -1 * ‖c‖ ^ 2) ∧ (∀ c : ℝ, ⟪c ^ 2, c⟫_ℝ ≤ 1 * ‖c‖ ^ 3) ∧
      (-(1 : ℝ)) + 1 ^ 2 = 0 ∧ ‖(1 : ℝ)‖ = 1 / 1 := by
  refine ⟨fun c => ?_, fun c => ?_, by norm_num, by norm_num⟩
  · rw [inner_neg_left, real_inner_self_eq_norm_sq]; linarith
  · simp only [RCLike.inner_apply, conj_trivial, Real.norm_eq_abs, one_mul]
    have h3 : c ^ 2 * c ≤ |c| ^ 3 := by
      have : c ^ 2 * c = c ^ 3 := by ring
      rw [this]; exact le_trans (le_abs_self _) (by rw [abs_pow])
    linarith [mul_comm c (c ^ 2)]

/-- **The flux identity alone bounds no radius from above.** If `A` is linear
and `Q` is homogeneous of degree 2, a zero `c` of `A + Q` moves to the zero
`t • c` of `A + t⁻¹ • Q`, for every `t ≠ 0`. The new quadratic part has flux
constant `C / |t|`, so any upper bound must use a lower bound on `Q`, not only
the flux identity and `C`. -/
theorem zero_rescale (A Q : E → E) (hA : ∀ (s : ℝ) c, A (s • c) = s • A c)
    (hQ : ∀ (s : ℝ) c, Q (s • c) = s ^ 2 • Q c)
    {c : E} (h : A c + Q c = 0) {t : ℝ} (ht : t ≠ 0) :
    A (t • c) + t⁻¹ • Q (t • c) = 0 := by
  rw [hA, hQ, smul_smul, show t⁻¹ * t ^ 2 = t by field_simp, ← smul_add, h, smul_zero]

/-- Inverting the linear part: with `A` a linear equivalence, `A c + Q c = 0`
iff `c + A⁻¹ (Q c) = 0`. -/
theorem zero_iff_inverted (A : E ≃ₗ[ℝ] E) (Q : E → E) (c : E) :
    A c + Q c = 0 ↔ c + A.symm (Q c) = 0 := by
  constructor
  · intro h
    have := congrArg A.symm h
    rwa [map_add, LinearEquiv.symm_apply_apply, map_zero] at this
  · intro h
    have := congrArg A h
    rwa [map_add, LinearEquiv.apply_symm_apply, map_zero] at this

/-- **Exact radius identity.** If `K` is homogeneous of degree 2 and
`c + K c = 0` with `c ≠ 0`, then `‖c‖ · ‖K u‖ = 1` for the direction
`u = ‖c‖⁻¹ • c`. The radius of a nonzero zero is determined by its direction. -/
theorem radius_identity (K : E → E) (hK : ∀ (s : ℝ) c, K (s • c) = s ^ 2 • K c)
    {c : E} (h : c + K c = 0) (hc : c ≠ 0) :
    ‖c‖ * ‖K (‖c‖⁻¹ • c)‖ = 1 := by
  have hn : 0 < ‖c‖ := norm_pos_iff.mpr hc
  have hc' : c = ‖c‖ • (‖c‖⁻¹ • c) := by
    rw [smul_smul, mul_inv_cancel₀ hn.ne', one_smul]
  have hKc : K c = ‖c‖ ^ 2 • K (‖c‖⁻¹ • c) := by
    conv_lhs => rw [hc']
    exact hK _ _
  have hcK : c = -K c := eq_neg_of_add_eq_zero_left h
  have h1 : ‖c‖ = ‖c‖ ^ 2 * ‖K (‖c‖⁻¹ • c)‖ := by
    conv_lhs => rw [hcK]
    rw [norm_neg, hKc, norm_smul, Real.norm_eq_abs, abs_of_nonneg (by positivity)]
  have h2 : ‖c‖ * (‖c‖ * ‖K (‖c‖⁻¹ • c)‖) = ‖c‖ * 1 := by
    rw [← mul_assoc, ← pow_two, ← h1, mul_one]
  exact mul_left_cancel₀ hn.ne' h2

/-- Unit direction of a nonzero vector. -/
theorem norm_dir_eq_one {c : E} (hc : c ≠ 0) : ‖‖c‖⁻¹ • c‖ = 1 := by
  have hn : 0 < ‖c‖ := norm_pos_iff.mpr hc
  rw [norm_smul, norm_inv, norm_norm, inv_mul_cancel₀ hn.ne']

/-- **Upper bound from a sphere infimum.** If `‖K u‖ ≥ m > 0` on the unit
sphere, every nonzero zero of `c + K c = 0` has `‖c‖ ≤ 1 / m`. -/
theorem norm_le_of_inf (K : E → E) (hK : ∀ (s : ℝ) c, K (s • c) = s ^ 2 • K c)
    {m : ℝ} (hm : 0 < m) (hinf : ∀ u : E, ‖u‖ = 1 → m ≤ ‖K u‖)
    {c : E} (h : c + K c = 0) (hc : c ≠ 0) : ‖c‖ ≤ 1 / m := by
  have hid := radius_identity K hK h hc
  have hb := hinf _ (norm_dir_eq_one hc)
  have hn : 0 < ‖c‖ := norm_pos_iff.mpr hc
  rw [le_div_iff₀ hm]
  calc ‖c‖ * m ≤ ‖c‖ * ‖K (‖c‖⁻¹ • c)‖ := mul_le_mul_of_nonneg_left hb hn.le
    _ = 1 := hid

/-- **Lower bound from a sphere supremum.** If `‖K u‖ ≤ M` on the unit sphere,
with `M > 0`, every nonzero zero has `‖c‖ ≥ 1 / M`. -/
theorem norm_ge_of_sup (K : E → E) (hK : ∀ (s : ℝ) c, K (s • c) = s ^ 2 • K c)
    {M : ℝ} (hM : 0 < M) (hsup : ∀ u : E, ‖u‖ = 1 → ‖K u‖ ≤ M)
    {c : E} (h : c + K c = 0) (hc : c ≠ 0) : 1 / M ≤ ‖c‖ := by
  have hid := radius_identity K hK h hc
  have hb := hsup _ (norm_dir_eq_one hc)
  have hn : 0 < ‖c‖ := norm_pos_iff.mpr hc
  rw [div_le_iff₀ hM]
  calc 1 = ‖c‖ * ‖K (‖c‖⁻¹ • c)‖ := hid.symm
    _ ≤ ‖c‖ * M := mul_le_mul_of_nonneg_left hb hn.le

/-- Non-vacuity of `norm_le_of_inf`: on `ℝ`, `K x = x²` has `‖K u‖ = 1` on the
unit sphere and the nonzero zero `c = −1` of `c + c² = 0`, with `‖c‖ = 1/1`. -/
theorem norm_le_of_inf_witness :
    (∀ u : ℝ, ‖u‖ = 1 → (1 : ℝ) ≤ ‖u ^ 2‖) ∧ (-1 : ℝ) + (-1) ^ 2 = 0 ∧
      ‖(-1 : ℝ)‖ = 1 / 1 := by
  refine ⟨fun u hu => ?_, by norm_num, by norm_num⟩
  rw [norm_pow, hu, one_pow]

/-- **Blow-up alternative.** Let `K n` be the inverted quadratic part at
truncation level `n` and `c n` a nonzero zero there. If `‖c n‖ → ∞`, then along
the directions `u n = ‖c n‖⁻¹ • c n` the quadratic part tends to `0`:
`‖K n (u n)‖ → 0`. Escaping zeros concentrate on approximate projective zeros
of the quadratic part. -/
theorem tendsto_K_dir_zero (K : ℕ → E → E)
    (hK : ∀ n (s : ℝ) c, K n (s • c) = s ^ 2 • K n c)
    (c : ℕ → E) (h : ∀ n, c n + K n (c n) = 0) (hc : ∀ n, c n ≠ 0)
    (hinf : Filter.Tendsto (fun n => ‖c n‖) Filter.atTop Filter.atTop) :
    Filter.Tendsto (fun n => ‖K n (‖c n‖⁻¹ • c n)‖) Filter.atTop (nhds 0) := by
  have heq : (fun n => ‖K n (‖c n‖⁻¹ • c n)‖) = fun n => ‖c n‖⁻¹ := by
    funext n
    have hid := radius_identity (K n) (hK n) (h n) (hc n)
    exact eq_inv_of_mul_eq_one_right hid
  rw [heq]; exact hinf.inv_tendsto_atTop

end RadiusBounds

/-! ## §5 The blow-up set is the Lamb-gradient set -/

section BlowUpSet

open QOU.FluidDynamics.BeltramiSteadyEuler

/-- If the advection is `∇(|u|²/2) − ∇ψ` componentwise, the Lamb vector is
`∇ψ`. Converse of `adv_grad_of_lambGrad`. -/
theorem lambGrad_of_adv_grad (u : VField) (hu : u.SlicesDiff) {ψ : SField}
    (h : ∀ x y z,
      u.adv u.u₁ x y z = px u.ke x y z - px ψ x y z ∧
      u.adv u.u₂ x y z = py u.ke x y z - py ψ x y z ∧
      u.adv u.u₃ x y z = pz u.ke x y z - pz ψ x y z) :
    LambGrad u ψ := by
  intro x y z
  obtain ⟨h1, h2, h3⟩ := h x y z
  have l1 := lamb₁ u hu x y z
  have l2 := lamb₂ u hu x y z
  have l3 := lamb₃ u hu x y z
  refine ⟨?_, ?_, ?_⟩ <;> linarith

/-- The advection is a gradient (so its Leray projection vanishes and `u` is a
projective zero of the nonlinearity) exactly when the Lamb vector is a
gradient. -/
theorem adv_grad_iff_lambGrad (u : VField) (hu : u.SlicesDiff) (ψ : SField) :
    (∀ x y z,
      u.adv u.u₁ x y z = px u.ke x y z - px ψ x y z ∧
      u.adv u.u₂ x y z = py u.ke x y z - py ψ x y z ∧
      u.adv u.u₃ x y z = pz u.ke x y z - pz ψ x y z) ↔ LambGrad u ψ :=
  ⟨lambGrad_of_adv_grad u hu, fun h x y z => adv_grad_of_lambGrad u hu h x y z⟩

end BlowUpSet

end QOU.FluidDynamics.DSSTailMatching
