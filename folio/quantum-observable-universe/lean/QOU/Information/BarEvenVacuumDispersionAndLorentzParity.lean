/-
Copyright (c) 2026 Quantum Observable Universe Collaboration. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Collaboration
-/
import Mathlib.Algebra.Algebra.Equiv
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.SpecialFunctions.Complex.LogBounds
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

/-!
# Bar-Even Vacuum Dispersion, Zero Linear Planck Slope, and Observer Modular Covariance

This module formalizes the mathematical results for Referee-Response Lane R1 across three sections:

1. **Section 1 — Bar-Even Symmetric $q$-Phase and Exact Group Velocity:**
   - For $q > 1$ and dimensionless ultraviolet energy ratio $x = \mathfrak{E}_\gamma / \mathfrak{E}_*$,
     defines the symmetric bar-even $q$-phase
     $$\phi_q(x) = \frac{\sinh(x \ln q)}{\sinh(\ln q)} = \frac{q^x - q^{-x}}{q - q^{-1}},$$
     proving exact bar-invariance $\phi_{q^{-1}}(x) = \phi_q(x)$, oddness $\phi_q(-x) = -\phi_q(x)$,
     normalization $\phi_q(0) = 0$, $\phi_q(1) = 1$, and exact Fréchet/real differentiation
     (`HasDerivAt`) yielding
     $$v_g(c_q, q, x) = c_{\mathrm{phys}}(q)\,\cosh(x \ln q), \qquad
       c_{\mathrm{phys}}(q) = c_q \frac{\ln q}{\sinh(\ln q)} > 0.$$

2. **Section 2 — Universal Infrared Light Speed, Zero Linear ($n = 1$) Slope, and Quadratic Bound:**
   - Proves that at $x = 0$, $v_g(c_q, q, 0) = c_{\mathrm{phys}}(q)$: the factor
     $\frac{\ln q}{\sinh(\ln q)}$ renormalizes the universal speed of light uniformly across all
     low-energy modes rather than inducing an infrared $O(\hbar_q)$ frequency dispersion.
   - Proves even energy parity $v_g(c_q, q, -x) = v_g(c_q, q, x)$ and vanishing first derivative
     $\left.\frac{d}{dx} v_g(c_q, q, x)\right|_{x = 0} = 0$, establishing that the linear ($n = 1$)
     Planck-scale dispersion channel vanishes identically by bar-parity.
   - Proves via two-stage mean-value monotonicity on $[0, 1]$ and $\cosh 1 < 2$ that for every
     $|x \ln q| \le 1$,
     $$0 \;\le\; \frac{v_g(c_q, q, x) - c_{\mathrm{phys}}(q)}{c_{\mathrm{phys}}(q)}
       \;=\; \cosh(x \ln q) - 1
       \;\le\; \frac{\cosh 1}{2}\,(x \ln q)^2
       \;\le\; (x \ln q)^2.$$

3. **Section 3 — Observer Covariance of State-Indexed Derivations at Fixed $q \neq 1$ and Vacuum Null:**
   - For any (generally noncommutative) $R$-algebra $A$ at fixed $q \neq 1$, automorphism
     $\Lambda \in \mathrm{Aut}_R(A)$ representing an inertial boost or crystal rotation, state
     functional $\tau \colon A \to_R R$, and state-indexed $R$-linear Leibniz derivation $\xi_\tau$,
     transporting $(\tau, \xi_\tau) \mapsto (\tau \circ \Lambda^{-1},\; \Lambda \circ \xi_\tau \circ \Lambda^{-1})$
     yields a genuine Leibniz derivation that intertwines $\Lambda$ to all iteration orders $n \in \mathbb{N}$
     and preserves every state expectation $\tau(\xi_\tau^{[n]}(a))$ without taking $q \to 1$.
   - When $\tau_{\mathrm{vac}}$ is invariant under a symmetry action $g \mapsto R_g \in \mathrm{Aut}_R(A)$
     and $g$-covariant modular assignment $\xi(\tau \circ R_g^{-1}) = R_g \circ \xi(\tau) \circ R_g^{-1}$
     holds (Tomita–Takesaki / Bisognano–Wichmann covariance), every rotated probe observable
     $O_g = R_g(O)$ has orientation-independent vacuum expectation and modular moments, so any
     orientation modulation in a state $\tau = \tau_{\mathrm{vac}} + \delta\tau$ arises purely from
     the non-vacuum state anisotropy $\delta\tau$.

Compute companion: `computations/probes/bar_even_grb_dispersion_and_lorentz_null_probe.py`
Witness: `computations/probes/bar-even-grb-dispersion-and-lorentz-null.witness.json`
-/

namespace QOU.Information.BarEvenVacuumDispersionAndLorentzParity

open Real

-- ============================================================================
-- § 1. Bar-Even Symmetric q-Phase and Exact Group Velocity
-- ============================================================================

/-- Symmetric bar-even $q$-phase $\phi_q(x) = \sinh(x \ln q) / \sinh(\ln q)$ for dimensionless
energy ratio $x = \mathfrak{E}_\gamma / \mathfrak{E}_*$. -/
noncomputable def barEvenQPhase (q x : ℝ) : ℝ :=
  Real.sinh (x * Real.log q) / Real.sinh (Real.log q)

/-- Uniformly renormalized infrared speed of light
$c_{\mathrm{phys}}(c_q, q) = c_q \cdot (\ln q / \sinh(\ln q))$. -/
noncomputable def physLightSpeed (c_q q : ℝ) : ℝ :=
  c_q * (Real.log q / Real.sinh (Real.log q))

/-- Exact group velocity $v_g(c_q, q, x) = c_{\mathrm{phys}}(c_q, q) \cdot \cosh(x \ln q)$
of the bar-even $q$-phase dispersion relation. -/
noncomputable def barEvenGroupVelocity (c_q q x : ℝ) : ℝ :=
  physLightSpeed c_q q * Real.cosh (x * Real.log q)

/-- For $q > 1$, $\ln q > 0$ and $\sinh(\ln q) > 0$. -/
theorem sinh_log_pos_of_one_lt {q : ℝ} (hq : 1 < q) :
    0 < Real.log q ∧ 0 < Real.sinh (Real.log q) := by
  have hlog : 0 < Real.log q := Real.log_pos hq
  exact ⟨hlog, Real.sinh_pos_iff.mpr hlog⟩

/-- Equivalence of `barEvenQPhase q x` with the symmetric $q$-number quotient
$(q^x - q^{-x}) / (q - q^{-1})$ for every $q > 0$, $q \neq 1$. -/
theorem barEvenQPhase_eq_qPow_diff {q x : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    barEvenQPhase q x = (q ^ x - q ^ (-x)) / (q - q⁻¹) := by
  unfold barEvenQPhase
  have hsinh_num : 2 * Real.sinh (x * Real.log q) = q ^ x - q ^ (-x) := by
    rw [Real.sinh_eq, Real.rpow_def_of_pos hq x, Real.rpow_def_of_pos hq (-x)]
    have hmul1 : Real.log q * x = x * Real.log q := mul_comm _ _
    have hmul2 : Real.log q * -x = -(x * Real.log q) := by ring
    rw [hmul1, hmul2]
    ring
  have hsinh_den : 2 * Real.sinh (Real.log q) = q - q⁻¹ := by
    rw [Real.sinh_eq, Real.exp_log hq, Real.exp_neg, Real.exp_log hq]
    ring
  have hlog_ne : Real.log q ≠ 0 := Real.log_ne_zero_of_pos_of_ne_one hq hq1
  have hden_ne : Real.sinh (Real.log q) ≠ 0 := Real.sinh_ne_zero.mpr hlog_ne
  have hq_sub_ne : q - q⁻¹ ≠ 0 := by
    rw [← hsinh_den]
    exact mul_ne_zero two_ne_zero hden_ne
  calc
    Real.sinh (x * Real.log q) / Real.sinh (Real.log q)
        = (2 * Real.sinh (x * Real.log q)) / (2 * Real.sinh (Real.log q)) := by
          field_simp [hden_ne]
    _ = (q ^ x - q ^ (-x)) / (q - q⁻¹) := by rw [hsinh_num, hsinh_den]

/-- **Bar-invariance** of the symmetric $q$-phase: $\phi_{q^{-1}}(x) = \phi_q(x)$. -/
theorem barEvenQPhase_inv (q x : ℝ) :
    barEvenQPhase q⁻¹ x = barEvenQPhase q x := by
  unfold barEvenQPhase
  rw [Real.log_inv, mul_neg, Real.sinh_neg, Real.sinh_neg, neg_div_neg_eq]

/-- **Oddness** of $\phi_q(x)$ in the dimensionless energy coordinate $x$:
$\phi_q(-x) = -\phi_q(x)$. -/
theorem barEvenQPhase_neg (q x : ℝ) :
    barEvenQPhase q (-x) = -barEvenQPhase q x := by
  unfold barEvenQPhase
  rw [neg_mul, Real.sinh_neg, neg_div]

/-- Normalization of $\phi_q$ at $x = 0$ and $x = 1$ (for $q > 1$). -/
theorem barEvenQPhase_zero_and_one {q : ℝ} (hq : 1 < q) :
    barEvenQPhase q 0 = 0 ∧ barEvenQPhase q 1 = 1 := by
  have hsh : Real.sinh (Real.log q) ≠ 0 := ne_of_gt (sinh_log_pos_of_one_lt hq).2
  unfold barEvenQPhase
  refine ⟨by simp, ?_⟩
  rw [one_mul, div_self hsh]

/-- Positivity and bar-invariance of the physical infrared speed of light $c_{\mathrm{phys}}(c_q, q)$. -/
theorem physLightSpeed_pos_and_inv {c_q q : ℝ} (hc : 0 < c_q) (hq : 1 < q) :
    0 < physLightSpeed c_q q ∧ physLightSpeed c_q q⁻¹ = physLightSpeed c_q q := by
  obtain ⟨hlog, hsh⟩ := sinh_log_pos_of_one_lt hq
  refine ⟨mul_pos hc (div_pos hlog hsh), ?_⟩
  unfold physLightSpeed
  rw [Real.log_inv, Real.sinh_neg, neg_div_neg_eq]

/-- Exact derivative of $\phi_q(x)$ with respect to $x$:
$\frac{d}{dx}\phi_q(x) = \frac{\ln q}{\sinh(\ln q)}\,\cosh(x \ln q)$. -/
theorem hasDerivAt_barEvenQPhase (q x : ℝ) :
    HasDerivAt (barEvenQPhase q)
      ((Real.log q / Real.sinh (Real.log q)) * Real.cosh (x * Real.log q)) x := by
  unfold barEvenQPhase
  have hlin : HasDerivAt (fun y : ℝ => y * Real.log q) (Real.log q) x := by
    simpa using (hasDerivAt_id x).mul_const (Real.log q)
  have hsh : HasDerivAt (fun y : ℝ => Real.sinh (y * Real.log q))
      (Real.cosh (x * Real.log q) * Real.log q) x := by
    simpa [Function.comp_def] using (Real.hasDerivAt_sinh (x * Real.log q)).comp x hlin
  have hdiv := hsh.div_const (Real.sinh (Real.log q))
  convert hdiv using 1
  ring

/-- Exact derivative of the scaled dispersion relation $x \mapsto c_q \phi_q(x)$ equals
`barEvenGroupVelocity c_q q x`. -/
theorem hasDerivAt_scaled_barEvenQPhase (c_q q x : ℝ) :
    HasDerivAt (fun y : ℝ => c_q * barEvenQPhase q y) (barEvenGroupVelocity c_q q x) x := by
  have hd := (hasDerivAt_barEvenQPhase q x).const_mul c_q
  convert hd using 1
  unfold barEvenGroupVelocity physLightSpeed
  ring

-- ============================================================================
-- § 2. Zero Infrared Dispersion, Vanishing Linear Slope, and Quadratic Bound
-- ============================================================================

/-- At $x = 0$, the group velocity equals the universal infrared speed $c_{\mathrm{phys}}(c_q, q)$. -/
theorem barEvenGroupVelocity_at_zero (c_q q : ℝ) :
    barEvenGroupVelocity c_q q 0 = physLightSpeed c_q q := by
  unfold barEvenGroupVelocity
  simp

/-- Even parity in $x$ and bar-invariance in $q$ of `barEvenGroupVelocity`. -/
theorem barEvenGroupVelocity_even_and_inv (c_q q x : ℝ) :
    barEvenGroupVelocity c_q q (-x) = barEvenGroupVelocity c_q q x ∧
      barEvenGroupVelocity c_q q⁻¹ x = barEvenGroupVelocity c_q q x := by
  refine ⟨?_, ?_⟩
  · unfold barEvenGroupVelocity
    rw [neg_mul, Real.cosh_neg]
  · unfold barEvenGroupVelocity physLightSpeed
    rw [Real.log_inv, Real.sinh_neg, neg_div_neg_eq, mul_neg, Real.cosh_neg]

/-- Exact derivative of `barEvenGroupVelocity c_q q` with respect to $x$. -/
theorem hasDerivAt_barEvenGroupVelocity (c_q q x : ℝ) :
    HasDerivAt (barEvenGroupVelocity c_q q)
      (physLightSpeed c_q q * Real.log q * Real.sinh (x * Real.log q)) x := by
  unfold barEvenGroupVelocity
  have hlin : HasDerivAt (fun y : ℝ => y * Real.log q) (Real.log q) x := by
    simpa using (hasDerivAt_id x).mul_const (Real.log q)
  have hch : HasDerivAt (fun y : ℝ => Real.cosh (y * Real.log q))
      (Real.sinh (x * Real.log q) * Real.log q) x := by
    simpa [Function.comp_def] using (Real.hasDerivAt_cosh (x * Real.log q)).comp x hlin
  have hm := hch.const_mul (physLightSpeed c_q q)
  convert hm using 1
  ring

/-- **Identical vanishing of linear ($n = 1$) Planck dispersion:**
$\left.\frac{d}{dx} v_g(c_q, q, x)\right|_{x = 0} = 0$. -/
theorem hasDerivAt_barEvenGroupVelocity_zero (c_q q : ℝ) :
    HasDerivAt (barEvenGroupVelocity c_q q) 0 0 ∧
      deriv (barEvenGroupVelocity c_q q) 0 = 0 := by
  have hd := hasDerivAt_barEvenGroupVelocity c_q q 0
  simp only [zero_mul, Real.sinh_zero, mul_zero] at hd
  exact ⟨hd, hd.deriv⟩

/-- Explicit upper bound $\cosh 1 < 2$ derived from $e < 3$ and $e^{-1} \le 1$. -/
theorem cosh_one_lt_two : Real.cosh 1 < 2 := by
  rw [Real.cosh_eq]
  have he : Real.exp 1 < 3 := lt_trans Real.exp_one_lt_d9 (by norm_num)
  have hne : Real.exp (-1) ≤ 1 := by
    calc
      Real.exp (-1) ≤ Real.exp 0 := Real.exp_le_exp.mpr (by norm_num)
      _ = 1 := Real.exp_zero
  linarith

/-- Sharp quadratic Taylor enclosure of $\cosh u - 1$ on $|u| \le 1$:
$0 \le \cosh u - 1 \le \frac{\cosh 1}{2}\,u^2 \le u^2$. -/
theorem cosh_sub_one_bounds_unit {u : ℝ} (hu : |u| ≤ 1) :
    0 ≤ Real.cosh u - 1 ∧
      Real.cosh u - 1 ≤ (Real.cosh 1 / 2) * u ^ 2 ∧
      (Real.cosh 1 / 2) * u ^ 2 ≤ u ^ 2 := by
  have hnonneg : 0 ≤ Real.cosh u - 1 := sub_nonneg.mpr (Real.one_le_cosh u)
  -- Step 1: prove `sinh t ≤ (cosh 1) * t` on `[0, 1]` via monotonicity of `t ↦ (cosh 1) * t - sinh t`.
  let hfun : ℝ → ℝ := fun t => Real.cosh 1 * t - Real.sinh t
  have hh_deriv : ∀ t : ℝ, HasDerivAt hfun (Real.cosh 1 - Real.cosh t) t := by
    intro t
    have h1 : HasDerivAt (fun s : ℝ => Real.cosh 1 * s) (Real.cosh 1) t := by
      simpa using (hasDerivAt_id t).const_mul (Real.cosh 1)
    exact h1.sub (Real.hasDerivAt_sinh t)
  have hh_mono : MonotoneOn hfun (Set.Icc 0 1) := by
    apply monotoneOn_of_deriv_nonneg (convex_Icc 0 1)
    · exact fun t _ => (hh_deriv t).continuousAt.continuousWithinAt
    · exact fun t _ => (hh_deriv t).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      rw [(hh_deriv t).deriv]
      have habs : |t| ≤ |1| := by
        rw [abs_of_pos ht.1, abs_one]
        exact le_of_lt ht.2
      exact sub_nonneg.mpr (Real.cosh_le_cosh.mpr habs)
  -- Step 2: prove `cosh t - 1 ≤ (cosh 1 / 2) * t^2` on `[0, 1]` via monotonicity of `gfun`.
  let gfun : ℝ → ℝ := fun t => (Real.cosh 1 / 2) * t ^ 2 + 1 - Real.cosh t
  have hg_deriv : ∀ t : ℝ, HasDerivAt gfun (hfun t) t := by
    intro t
    have hsq : HasDerivAt (fun s : ℝ => (Real.cosh 1 / 2) * s ^ 2 + 1)
        (Real.cosh 1 * t) t := by
      have hp : HasDerivAt (fun s : ℝ => s ^ 2) (2 * t) t := by
        simpa using (hasDerivAt_id t).pow 2
      have hm := (hp.const_mul (Real.cosh 1 / 2)).add_const 1
      convert hm using 1
      ring
    exact hsq.sub (Real.hasDerivAt_cosh t)
  have hg_mono : MonotoneOn gfun (Set.Icc 0 1) := by
    apply monotoneOn_of_deriv_nonneg (convex_Icc 0 1)
    · exact fun t _ => (hg_deriv t).continuousAt.continuousWithinAt
    · exact fun t _ => (hg_deriv t).differentiableAt.differentiableWithinAt
    · intro t ht
      rw [interior_Icc] at ht
      rw [(hg_deriv t).deriv]
      have h0_mem : (0 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := ⟨le_refl 0, by norm_num⟩
      have ht_mem : t ∈ Set.Icc (0 : ℝ) 1 := ⟨le_of_lt ht.1, le_of_lt ht.2⟩
      have hh0 : hfun 0 = 0 := by simp [hfun]
      rw [← hh0]
      exact hh_mono h0_mem ht_mem (le_of_lt ht.1)
  have habs_mem : |u| ∈ Set.Icc (0 : ℝ) 1 := ⟨abs_nonneg u, hu⟩
  have h0_mem : (0 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := ⟨le_refl 0, by norm_num⟩
  have hg0 : gfun 0 = 0 := by simp [gfun]
  have hg_abs : 0 ≤ gfun |u| := by
    rw [← hg0]
    exact hg_mono h0_mem habs_mem (abs_nonneg u)
  have hquad_tight : Real.cosh u - 1 ≤ (Real.cosh 1 / 2) * u ^ 2 := by
    have hcos_abs : Real.cosh |u| = Real.cosh u := Real.cosh_abs u
    have hsq_abs : |u| ^ 2 = u ^ 2 := sq_abs u
    dsimp [gfun] at hg_abs
    rw [hcos_abs, hsq_abs] at hg_abs
    linarith
  have hquad_one : (Real.cosh 1 / 2) * u ^ 2 ≤ u ^ 2 := by
    have hc2 : Real.cosh 1 / 2 ≤ 1 := by linarith [cosh_one_lt_two]
    nlinarith [sq_nonneg u]
  exact ⟨hnonneg, hquad_tight, hquad_one⟩

/-- **Quadratic Fractional Vacuum Dispersion Bound:**
For $c_q > 0$, $q > 1$, and $|x \ln q| \le 1$, the fractional group-velocity shift relative to
$c_{\mathrm{phys}}(c_q, q)$ equals $\cosh(x \ln q) - 1$ and satisfies
$0 \le \frac{v_g(c_q, q, x) - c_{\mathrm{phys}}(c_q, q)}{c_{\mathrm{phys}}(c_q, q)}
  \le \frac{\cosh 1}{2}\,(x \ln q)^2 \le (x \ln q)^2$. -/
theorem barEvenGroupVelocity_quadratic_dispersion_bound {c_q q x : ℝ}
    (hc : 0 < c_q) (hq : 1 < q) (hx : |x * Real.log q| ≤ 1) :
    (barEvenGroupVelocity c_q q x - physLightSpeed c_q q) / physLightSpeed c_q q =
        Real.cosh (x * Real.log q) - 1 ∧
      0 ≤ (barEvenGroupVelocity c_q q x - physLightSpeed c_q q) / physLightSpeed c_q q ∧
      (barEvenGroupVelocity c_q q x - physLightSpeed c_q q) / physLightSpeed c_q q ≤
        (Real.cosh 1 / 2) * (x * Real.log q) ^ 2 ∧
      (Real.cosh 1 / 2) * (x * Real.log q) ^ 2 ≤ (x * Real.log q) ^ 2 := by
  have hcphys_pos : 0 < physLightSpeed c_q q := (physLightSpeed_pos_and_inv hc hq).1
  have hcphys_ne : physLightSpeed c_q q ≠ 0 := ne_of_gt hcphys_pos
  have hfrac :
      (barEvenGroupVelocity c_q q x - physLightSpeed c_q q) / physLightSpeed c_q q =
        Real.cosh (x * Real.log q) - 1 := by
    unfold barEvenGroupVelocity
    field_simp [hcphys_ne]
  obtain ⟨h0, h1, h2⟩ := cosh_sub_one_bounds_unit hx
  exact ⟨hfrac, by rwa [hfrac], by rwa [hfrac], h2⟩

/-- Master summary theorem packaging the bar-even $q$-phase derivative, infrared speed universality,
identical vanishing of linear ($n = 1$) dispersion, and quadratic fractional bound. -/
theorem barEven_zero_ir_and_quadratic_dispersion_summary {c_q q x : ℝ}
    (hc : 0 < c_q) (hq : 1 < q) (hx : |x * Real.log q| ≤ 1) :
    barEvenQPhase q⁻¹ x = barEvenQPhase q x ∧
      HasDerivAt (fun y : ℝ => c_q * barEvenQPhase q y) (barEvenGroupVelocity c_q q x) x ∧
      barEvenGroupVelocity c_q q 0 = physLightSpeed c_q q ∧
      deriv (barEvenGroupVelocity c_q q) 0 = 0 ∧
      (barEvenGroupVelocity c_q q x - physLightSpeed c_q q) / physLightSpeed c_q q ≤
        (Real.cosh 1 / 2) * (x * Real.log q) ^ 2 := by
  refine ⟨barEvenQPhase_inv q x,
    hasDerivAt_scaled_barEvenQPhase c_q q x,
    barEvenGroupVelocity_at_zero c_q q,
    (hasDerivAt_barEvenGroupVelocity_zero c_q q).2,
    (barEvenGroupVelocity_quadratic_dispersion_bound hc hq hx).2.2.1⟩

-- ============================================================================
-- § 3. Observer Covariance of State-Indexed Derivations & Vacuum Null Theorem
-- ============================================================================

section ObserverModularCovariance

/-- An $R$-linear Leibniz derivation on a (possibly noncommutative) $R$-algebra $A$, modeling
the state-indexed Tomita–Takesaki / Reeb modular derivation $\xi_\tau$ on the Frobenius–Hopf
aether at fixed $q \neq 1$. -/
structure AlgDerivation (R A : Type*) [CommSemiring R] [Semiring A] [Algebra R A] where
  /-- Underlying $R$-linear endomorphism of $A$. -/
  toLinearMap : A →ₗ[R] A
  /-- Noncommutative Leibniz rule $D(ab) = D(a)\,b + a\,D(b)$. -/
  map_mul' : ∀ a b : A, toLinearMap (a * b) = toLinearMap a * b + a * toLinearMap b

namespace AlgDerivation

section Semiring

variable {R A : Type*} [CommSemiring R] [Semiring A] [Algebra R A]

instance : CoeFun (AlgDerivation R A) (fun _ => A → A) :=
  ⟨fun D => D.toLinearMap⟩

@[ext]
theorem ext {D₁ D₂ : AlgDerivation R A} (h : ∀ a : A, D₁ a = D₂ a) : D₁ = D₂ := by
  cases D₁
  cases D₂
  congr 1
  exact LinearMap.ext h

@[simp]
theorem coe_mk (f : A →ₗ[R] A) (hf : ∀ a b : A, f (a * b) = f a * b + a * f b) (a : A) :
    (⟨f, hf⟩ : AlgDerivation R A) a = f a := rfl

theorem map_add (D : AlgDerivation R A) (a b : A) : D (a + b) = D a + D b :=
  D.toLinearMap.map_add a b

theorem map_smul (D : AlgDerivation R A) (r : R) (a : A) : D (r • a) = r • D a :=
  D.toLinearMap.map_smul r a

theorem map_mul (D : AlgDerivation R A) (a b : A) : D (a * b) = D a * b + a * D b :=
  D.map_mul' a b

/-- Conjugate (pushforward) an $R$-derivation $D$ along an algebra automorphism
$\Lambda \in \mathrm{Aut}_R(A)$: $(\Lambda_* D)(a) = \Lambda(D(\Lambda^{-1}(a)))$. -/
def conj (Λ : A ≃ₐ[R] A) (D : AlgDerivation R A) : AlgDerivation R A where
  toLinearMap := Λ.toLinearMap.comp (D.toLinearMap.comp Λ.symm.toLinearMap)
  map_mul' a b := by
    simp only [LinearMap.comp_apply, AlgEquiv.toLinearMap_apply]
    rw [_root_.map_mul Λ.symm a b, D.map_mul', _root_.map_add Λ,
      _root_.map_mul Λ, _root_.map_mul Λ, Λ.apply_symm_apply, Λ.apply_symm_apply]

@[simp]
theorem conj_apply (Λ : A ≃ₐ[R] A) (D : AlgDerivation R A) (a : A) :
    D.conj Λ a = Λ (D (Λ.symm a)) := rfl

/-- Exact intertwining $(D.\mathrm{conj}\;\Lambda)(\Lambda a) = \Lambda(D a)$ at fixed $q \neq 1$. -/
theorem conj_apply_equiv (Λ : A ≃ₐ[R] A) (D : AlgDerivation R A) (a : A) :
    D.conj Λ (Λ a) = Λ (D a) := by
  simp [conj_apply]

/-- Iterated $n$-th derivation intertwining $((D.\mathrm{conj}\;\Lambda)^{[n]})(\Lambda a) = \Lambda(D^{[n]} a)$. -/
theorem iterate_conj_apply (Λ : A ≃ₐ[R] A) (D : AlgDerivation R A) :
    ∀ (n : ℕ) (a : A), ((D.conj Λ : A → A)^[n]) (Λ a) = Λ (((D : A → A)^[n]) a)
  | 0, a => rfl
  | n + 1, a => by
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply',
      iterate_conj_apply Λ D n a, conj_apply_equiv]

/-- Group-action functoriality of `AlgDerivation.conj`. -/
theorem conj_trans (Λ₁ Λ₂ : A ≃ₐ[R] A) (D : AlgDerivation R A) :
    (D.conj Λ₁).conj Λ₂ = D.conj (Λ₁.trans Λ₂) := by
  ext a
  simp [conj_apply, AlgEquiv.trans_apply, AlgEquiv.symm_trans_apply]

end Semiring

section Ring

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Every $R$-derivation annihilates the multiplicative identity $1 \in A$. -/
theorem map_one (D : AlgDerivation R A) : D 1 = 0 := by
  have h : D (1 * 1) = D 1 * 1 + 1 * D 1 := D.map_mul 1 1
  simp only [mul_one, one_mul] at h
  exact add_eq_right.mp h.symm

/-- Noncommutative inner commutator derivation $X \mapsto H X - X H$ generated by an element
$H \in A$ (instantiating `AlgDerivation` without any derivation hypothesis in its binders). -/
def inner (H : A) : AlgDerivation R A where
  toLinearMap :=
    { toFun := fun X => H * X - X * H
      map_add' := fun X Y => by noncomm_ring
      map_smul' := fun r X => by simp [smul_sub] }
  map_mul' X Y := by
    dsimp only [LinearMap.coe_mk, AddHom.coe_mk]
    noncomm_ring

@[simp]
theorem inner_apply (H X : A) : (inner H : AlgDerivation R A) X = H * X - X * H := rfl

/-- Conjugating an inner derivation `inner H` by an algebra automorphism $\Lambda$ yields
`inner (Λ H)`. -/
theorem conj_inner (Λ : A ≃ₐ[R] A) (H : A) :
    (inner H : AlgDerivation R A).conj Λ = inner (Λ H) := by
  ext X
  simp [conj_apply, inner_apply, map_sub, _root_.map_mul Λ, Λ.apply_symm_apply]

end Ring

end AlgDerivation

/-- Pushforward of an $R$-linear state functional $\tau \colon A \to_R R$ along an observer
automorphism $\Lambda \in \mathrm{Aut}_R(A)$: $\tau_\Lambda(a) = \tau(\Lambda^{-1}(a))$. -/
def boostedState {R A : Type*} [CommSemiring R] [Semiring A] [Algebra R A]
    (Λ : A ≃ₐ[R] A) (τ : A →ₗ[R] R) : A →ₗ[R] R :=
  τ.comp Λ.symm.toLinearMap

@[simp]
theorem boostedState_apply {R A : Type*} [CommSemiring R] [Semiring A] [Algebra R A]
    (Λ : A ≃ₐ[R] A) (τ : A →ₗ[R] R) (a : A) :
    boostedState Λ τ a = τ (Λ.symm a) := rfl

/-- Exact expectation invariance $(\tau_\Lambda)(\Lambda a) = \tau(a)$ and preservation of all
$n$-th modular/Reeb moments under $(\tau, \xi) \mapsto (\tau_\Lambda, \xi.\mathrm{conj}\;\Lambda)$
at fixed $q \neq 1$. -/
theorem boostedState_iterate_derivation_invariant
    {R A : Type*} [CommSemiring R] [Semiring A] [Algebra R A]
    (Λ : A ≃ₐ[R] A) (τ : A →ₗ[R] R) (ξ : AlgDerivation R A) (n : ℕ) (a : A) :
    boostedState Λ τ (Λ a) = τ a ∧
      boostedState Λ τ (((ξ.conj Λ : A → A)^[n]) (Λ a)) = τ (((ξ : A → A)^[n]) a) := by
  refine ⟨by simp [boostedState_apply], ?_⟩
  rw [AlgDerivation.iterate_conj_apply, boostedState_apply, Λ.symm_apply_apply]

/-- Modular stationarity $\tau \circ \xi = 0$ is preserved under every observer automorphism
$\Lambda \in \mathrm{Aut}_R(A)$. -/
theorem trace_stationarity_iff_boosted
    {R A : Type*} [CommSemiring R] [Semiring A] [Algebra R A]
    (Λ : A ≃ₐ[R] A) (τ : A →ₗ[R] R) (ξ : AlgDerivation R A) :
    (∀ a : A, τ (ξ a) = 0) ↔ (∀ b : A, boostedState Λ τ ((ξ.conj Λ) b) = 0) := by
  constructor
  · intro h b
    simp [boostedState_apply, AlgDerivation.conj_apply, h (Λ.symm b)]
  · intro h a
    have hb := h (Λ a)
    simpa [boostedState_apply, AlgDerivation.conj_apply_equiv] using hb

/-- **Observer Covariance & Vacuum Null Orientation Modulation Theorem:**
Let $g \mapsto R_g \in \mathrm{Aut}_R(A)$ be a symmetry representation (rotations/boosts) on a
(generally noncommutative) $R$-algebra $A$ at fixed $q \neq 1$, $\xi$ be a $G$-covariant
state-to-derivation assignment (`∀ g τ, ξ (boostedState (R g) τ) = (ξ τ).conj (R g)`), and
$\tau_{\mathrm{vac}} \colon A \to_R R$ be a $G$-invariant vacuum state (`∀ g, boostedState (R g) τ_vac = τ_vac`).
Then for every probe observable $O \in A$, orientations $g_1, g_2 \in G$, iteration order $n \in \mathbb{N}$,
and non-vacuum state perturbation $\delta\tau \colon A \to_R R$:
1. The vacuum derivation commutes with every symmetry $R_g$: $(\xi\,\tau_{\mathrm{vac}}).\mathrm{conj}\;(R_g) = \xi\,\tau_{\mathrm{vac}}$.
2. Every vacuum modular moment $\tau_{\mathrm{vac}}\bigl((\xi\,\tau_{\mathrm{vac}})^{[n]}(R_g O)\bigr)$
   equals $\tau_{\mathrm{vac}}\bigl((\xi\,\tau_{\mathrm{vac}})^{[n]} O\bigr)$, so the vacuum
   orientation modulation between $g_1$ and $g_2$ vanishes identically.
3. In a perturbed macroscopic state $\tau = \tau_{\mathrm{vac}} + \delta\tau$, the orientation
   difference $\tau(R_{g_1} O) - \tau(R_{g_2} O)$ equals $\delta\tau(R_{g_1} O) - \delta\tau(R_{g_2} O)$,
   isolating non-vacuum state anisotropy $\delta\tau$. -/
theorem observer_covariant_modular_derivation_and_vacuum_null
    {G R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (R_act : G → (A ≃ₐ[R] A))
    (ξ : (A →ₗ[R] R) → AlgDerivation R A)
    (hcov : ∀ (g : G) (τ : A →ₗ[R] R), ξ (boostedState (R_act g) τ) = (ξ τ).conj (R_act g))
    (τ_vac δτ : A →ₗ[R] R)
    (hvac : ∀ g : G, boostedState (R_act g) τ_vac = τ_vac)
    (O : A) (g₁ g₂ : G) (n : ℕ) :
    (ξ τ_vac).conj (R_act g₁) = ξ τ_vac ∧
      τ_vac (((ξ τ_vac : A → A)^[n]) (R_act g₁ O)) -
          τ_vac (((ξ τ_vac : A → A)^[n]) (R_act g₂ O)) = 0 ∧
      (τ_vac + δτ) (R_act g₁ O) - (τ_vac + δτ) (R_act g₂ O) =
        δτ (R_act g₁ O) - δτ (R_act g₂ O) := by
  have hfix : ∀ g : G, (ξ τ_vac).conj (R_act g) = ξ τ_vac := fun g => by
    rw [← hcov g τ_vac, hvac g]
  have hmom : ∀ g : G,
      τ_vac (((ξ τ_vac : A → A)^[n]) (R_act g O)) =
        τ_vac (((ξ τ_vac : A → A)^[n]) O) := fun g => by
    have h1 : ((ξ τ_vac : A → A)^[n]) (R_act g O) =
        R_act g (((ξ τ_vac : A → A)^[n]) O) := by
      have hfg := AlgDerivation.iterate_conj_apply (R_act g) (ξ τ_vac) n O
      rwa [hfix g] at hfg
    rw [h1]
    have h2 : boostedState (R_act g) τ_vac (R_act g (((ξ τ_vac : A → A)^[n]) O)) =
        τ_vac (((ξ τ_vac : A → A)^[n]) O) := by
      simp [boostedState_apply]
    rwa [hvac g] at h2
  have hvac0 : ∀ g : G, τ_vac (R_act g O) = τ_vac O := fun g => by
    have h2 : boostedState (R_act g) τ_vac (R_act g O) = τ_vac O := by
      simp [boostedState_apply]
    rwa [hvac g] at h2
  refine ⟨hfix g₁, ?_, ?_⟩
  · rw [hmom g₁, hmom g₂, sub_self]
  · simp only [LinearMap.add_apply, hvac0 g₁, hvac0 g₂]
    ring

end ObserverModularCovariance

end QOU.Information.BarEvenVacuumDispersionAndLorentzParity
