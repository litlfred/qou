/-
Copyright (c) 2026 Quantum Observable Universe Collaboration. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Collaboration
-/
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Tactic

/-!
# Toroidal Harmonics Principal Mode, Order-Gap Projection, and Parabolic Cylinder Jet Recurrence

Unconditional formalization of the differential-algebraic structure underlying
`prop:qbeta-toroidal-harmonics-basis` (`mass-endomorphism/qbeta-toroidal-harmonics-basis.md`):

1. **Principal Half-Integer Azimuthal Mode (`m = ±1/2`) Eliminates the Singular Toroidal Barrier:**
   In the longitudinal coordinate $\eta$, the Toroidal Harmonic ODE
   $$F''(\eta) - \left(n^2 - \frac{1}{4} + \frac{m^2 - \frac{1}{4}}{\sinh^2 \eta}\right) F(\eta) = 0$$
   has centrifugal numerator $m^2 - \tfrac{1}{4} = 0$ if and only if $m = \pm\tfrac{1}{2}$.
   At $m = \pm\tfrac{1}{2}$ the singular $1/\sinh^2\eta$ barrier vanishes identically for every
   $\eta \in \mathbb{R}$, and the global smooth hyperbolic basis
   $F(\eta) = c_+ \cosh(\omega\eta) + c_- \sinh(\omega\eta)$ ($\omega^2 = n^2 - \tfrac{1}{4}$)
   solves the exact ODE with Wronskian $\omega$.

2. **Mode-Selective Order-Gap (`c_1 = 0`, Eliminating $O(\sqrt{u})$):**
   Symmetric projection $\Pi_{\mathrm{even}}(g)(w) = \tfrac{1}{2}(g(w) + g(-w))$ in the square-root
   coordinate $w = \sqrt{u}$ annihilates all odd powers of $w$ (in particular the $w^1 = \sqrt{u}$
   channel), and on the quadratic coordinate $u = w^2$ a normalized quartic jet
   $F(u) = 1 + c_1 u + c_2 u^2 + c_3 u^3 + c_4 u^4$ has vanishing linear slope $F'(0) = 0$ if and
   only if $c_1 = 0$, leaving $1 + c_2 u^2 + c_3 u^3 + c_4 u^4$.

3. **Simple Turning-Point Existence & Parabolic Cylinder (Weber) Jet Recurrence (`c_4 = 2 ↔ C = -22`):**
   - For $|n| < \tfrac{1}{2}$ and $|m| > \tfrac{1}{2}$, the toroidal potential vanishes at the unique
     positive $\sinh^2 \eta_* = \frac{m^2 - 1/4}{1/4 - n^2} > 0$, where $\frac{d}{d\eta} V_{\mathrm{tor}}(\eta_*) \neq 0$
     (regular Liouville–Green simple turning point).
   - Applying the Parabolic Cylinder (Weber) operator
     $\mathcal{L}_{A,B,C}(P) = P'' + (A + B u + C u^2) P$ to
     $P(u) = 1 + c_1 u + c_2 u^2 + c_3 u^3 + c_4 u^4$ yields the exact recurrence
     $$\mathrm{coeff}_0 = 2 c_2 + A, \qquad
       \mathrm{coeff}_1 = 6 c_3 + A c_1 + B, \qquad
       \mathrm{coeff}_2 = 12 c_4 + A c_2 + B c_1 + C.$$
     Under the order-gap $c_1 = 0$ and quadratic rung $c_2 = -1$ ($A = 2$), vanishing of the
     jet residuals through $u^2$ forces $C = 2 - 12 c_4$; in particular,
     $$c_4 = 2 \iff C = -22$$
     (with $(A, B, C) = (2, 12, -22)$ at $(c_1, c_2, c_3, c_4) = (0, -1, -2, 2)$).
-/

namespace QOU.MassEndomorphism.QBetaToroidalHarmonicsBasis

open Polynomial

/-- Centrifugal barrier numerator $\kappa_{\mathrm{tor}}(m) = m^2 - \frac{1}{4}$ of the Toroidal
Harmonic ODE in longitudinal coordinate $\eta$. -/
noncomputable def toroidalCentrifugalCoeff (m : ℝ) : ℝ :=
  m ^ 2 - 1 / 4

/-- Full longitudinal Toroidal Harmonic potential
$V_{\mathrm{tor}}(n, m, \eta) = \bigl(n^2 - \frac{1}{4}\bigr) + \frac{m^2 - 1/4}{\sinh^2 \eta}$. -/
noncomputable def toroidalPotential (n m η : ℝ) : ℝ :=
  (n ^ 2 - 1 / 4) + toroidalCentrifugalCoeff m / (Real.sinh η) ^ 2

/-- Smooth principal-mode hyperbolic combination
$F(\eta) = c_+ \cosh(\omega \eta) + c_- \sinh(\omega \eta)$. -/
noncomputable def principalToroidalMode (ω cPlus cMinus η : ℝ) : ℝ :=
  cPlus * Real.cosh (ω * η) + cMinus * Real.sinh (ω * η)

/-- First derivative of `principalToroidalMode` with respect to $\eta$. -/
noncomputable def principalToroidalModeDeriv1 (ω cPlus cMinus η : ℝ) : ℝ :=
  cPlus * (ω * Real.sinh (ω * η)) + cMinus * (ω * Real.cosh (ω * η))

/-- Second derivative of `principalToroidalMode` with respect to $\eta$. -/
noncomputable def principalToroidalModeDeriv2 (ω cPlus cMinus η : ℝ) : ℝ :=
  ω ^ 2 * principalToroidalMode ω cPlus cMinus η

/-- Exact characterization of the vanishing centrifugal barrier:
$m^2 - \frac{1}{4} = 0 \iff m = \frac{1}{2} \lor m = -\frac{1}{2}$, at which $V_{\mathrm{tor}}(n, m, \eta)$
reduces identically to $n^2 - \frac{1}{4}$ for every $\eta \in \mathbb{R}$. -/
theorem toroidalCentrifugalCoeff_zero_iff_and_principal_potential (n m η : ℝ) :
    (toroidalCentrifugalCoeff m = 0 ↔ m = 1 / 2 ∨ m = -1 / 2) ∧
      toroidalPotential n (1 / 2) η = n ^ 2 - 1 / 4 ∧
      toroidalPotential n (-1 / 2) η = n ^ 2 - 1 / 4 := by
  refine ⟨?_, ?_, ?_⟩
  · unfold toroidalCentrifugalCoeff
    have hfac : m ^ 2 - 1 / 4 = (m - 1 / 2) * (m + 1 / 2) := by ring
    rw [hfac, mul_eq_zero]
    constructor
    · rintro (h1 | h2)
      · exact Or.inl (by linarith)
      · exact Or.inr (by linarith)
    · rintro (rfl | rfl) <;> norm_num
  · unfold toroidalPotential toroidalCentrifugalCoeff
    norm_num
  · unfold toroidalPotential toroidalCentrifugalCoeff
    norm_num

/-- **Exact Solution & Non-Degenerate Wronskian of the Principal-Mode (`m = ±1/2`) Toroidal ODE:**
Whenever $\omega^2 = n^2 - \frac{1}{4}$, the smooth function
$F(\eta) = c_+ \cosh(\omega\eta) + c_- \sinh(\omega\eta)$ satisfies:
1. `HasDerivAt F (F'(\eta)) \eta` and `HasDerivAt F' (F''(\eta)) \eta` for every $\eta \in \mathbb{R}$,
2. $F''(\eta) - V_{\mathrm{tor}}(n, 1/2, \eta) F(\eta) = 0$ for every $\eta \in \mathbb{R}$,
3. Basis Wronskian $\cosh(\omega\eta)\cdot\frac{d}{d\eta}\sinh(\omega\eta) - \sinh(\omega\eta)\cdot\frac{d}{d\eta}\cosh(\omega\eta) = \omega$. -/
theorem principalToroidalMode_solves_exact_ode
    {n ω : ℝ} (hω : ω ^ 2 = n ^ 2 - 1 / 4) (cPlus cMinus η : ℝ) :
    HasDerivAt (principalToroidalMode ω cPlus cMinus)
        (principalToroidalModeDeriv1 ω cPlus cMinus η) η ∧
      HasDerivAt (principalToroidalModeDeriv1 ω cPlus cMinus)
        (principalToroidalModeDeriv2 ω cPlus cMinus η) η ∧
      principalToroidalModeDeriv2 ω cPlus cMinus η -
          toroidalPotential n (1 / 2) η * principalToroidalMode ω cPlus cMinus η = 0 ∧
      Real.cosh (ω * η) * (ω * Real.cosh (ω * η)) -
          Real.sinh (ω * η) * (ω * Real.sinh (ω * η)) = ω := by
  have hlin : HasDerivAt (fun x : ℝ => ω * x) ω η := by
    simpa using (hasDerivAt_id η).const_mul ω
  have hcosh : HasDerivAt (fun x : ℝ => Real.cosh (ω * x)) (Real.sinh (ω * η) * ω) η := by
    simpa [Function.comp_def] using (Real.hasDerivAt_cosh (ω * η)).comp η hlin
  have hsinh : HasDerivAt (fun x : ℝ => Real.sinh (ω * x)) (Real.cosh (ω * η) * ω) η := by
    simpa [Function.comp_def] using (Real.hasDerivAt_sinh (ω * η)).comp η hlin
  have hd1 : HasDerivAt (principalToroidalMode ω cPlus cMinus)
      (principalToroidalModeDeriv1 ω cPlus cMinus η) η := by
    unfold principalToroidalMode principalToroidalModeDeriv1
    convert (hcosh.const_mul cPlus).add (hsinh.const_mul cMinus) using 1
    ring
  have hd2 : HasDerivAt (principalToroidalModeDeriv1 ω cPlus cMinus)
      (principalToroidalModeDeriv2 ω cPlus cMinus η) η := by
    unfold principalToroidalModeDeriv1 principalToroidalModeDeriv2 principalToroidalMode
    convert (hsinh.const_mul (cPlus * ω)).add (hcosh.const_mul (cMinus * ω)) using 1
    · ext x; simp only [Pi.add_apply]; ring
    · ring
  have hode : principalToroidalModeDeriv2 ω cPlus cMinus η -
      toroidalPotential n (1 / 2) η * principalToroidalMode ω cPlus cMinus η = 0 := by
    rw [(toroidalCentrifugalCoeff_zero_iff_and_principal_potential n (1 / 2) η).2.1]
    unfold principalToroidalModeDeriv2
    rw [hω, sub_self]
  have hwronsk : Real.cosh (ω * η) * (ω * Real.cosh (ω * η)) -
      Real.sinh (ω * η) * (ω * Real.sinh (ω * η)) = ω := by
    calc
      Real.cosh (ω * η) * (ω * Real.cosh (ω * η)) -
          Real.sinh (ω * η) * (ω * Real.sinh (ω * η)) =
        ω * (Real.cosh (ω * η) ^ 2 - Real.sinh (ω * η) ^ 2) := by ring
      _ = ω * 1 := by rw [Real.cosh_sq_sub_sinh_sq]
      _ = ω := mul_one ω
  exact ⟨hd1, hd2, hode, hwronsk⟩

/-- **Liouville–Green Regular Simple Turning-Point Theorem:**
For $|n| < \frac{1}{2}$ and $|m| > \frac{1}{2}$, the toroidal potential $V_{\mathrm{tor}}(n, m, \eta)$
at any $\eta_*$ with $\sinh \eta_* > 0$ vanishes if and only if
$\sinh^2 \eta_* = \frac{m^2 - 1/4}{1/4 - n^2} > 0$, and at that turning point its derivative
$V_{\mathrm{tor}}'(\eta_*) = -\frac{2(m^2 - 1/4)\cosh\eta_*}{\sinh^3\eta_*}$ is strictly negative
(hence non-zero, guaranteeing a non-degenerate linear Airy / local Weber reduction). -/
theorem toroidal_regular_turning_point
    {n m ηStar : ℝ} (hn : n ^ 2 < 1 / 4) (hm : 1 / 4 < m ^ 2)
    (hsinh_pos : 0 < Real.sinh ηStar) :
    (toroidalPotential n m ηStar = 0 ↔
        (Real.sinh ηStar) ^ 2 = (m ^ 2 - 1 / 4) / (1 / 4 - n ^ 2)) ∧
      HasDerivAt (toroidalPotential n m)
        (-2 * toroidalCentrifugalCoeff m * Real.cosh ηStar / (Real.sinh ηStar) ^ 3) ηStar ∧
      -2 * toroidalCentrifugalCoeff m * Real.cosh ηStar / (Real.sinh ηStar) ^ 3 < 0 := by
  have hα_pos : 0 < 1 / 4 - n ^ 2 := by linarith
  have hβ_pos : 0 < toroidalCentrifugalCoeff m := by
    unfold toroidalCentrifugalCoeff; linarith
  have hsq_pos : 0 < (Real.sinh ηStar) ^ 2 := sq_pos_of_pos hsinh_pos
  have hsinh_ne : Real.sinh ηStar ≠ 0 := ne_of_gt hsinh_pos
  have hiff : toroidalPotential n m ηStar = 0 ↔
      (Real.sinh ηStar) ^ 2 = (m ^ 2 - 1 / 4) / (1 / 4 - n ^ 2) := by
    unfold toroidalPotential toroidalCentrifugalCoeff
    have hα_ne : 1 / 4 - n ^ 2 ≠ 0 := ne_of_gt hα_pos
    have hsq_ne : (Real.sinh ηStar) ^ 2 ≠ 0 := ne_of_gt hsq_pos
    rw [eq_div_iff hα_ne]
    constructor
    · intro hzero
      have hmul : ((n ^ 2 - 1 / 4) + (m ^ 2 - 1 / 4) / (Real.sinh ηStar) ^ 2) *
          (Real.sinh ηStar) ^ 2 = 0 := by rw [hzero, zero_mul]
      rw [add_mul, div_mul_cancel₀ _ hsq_ne] at hmul
      linear_combination -hmul
    · intro hroot
      have hmul : (n ^ 2 - 1 / 4) * (Real.sinh ηStar) ^ 2 + (m ^ 2 - 1 / 4) = 0 := by
        linear_combination -hroot
      calc
        (n ^ 2 - 1 / 4) + (m ^ 2 - 1 / 4) / (Real.sinh ηStar) ^ 2 =
            ((n ^ 2 - 1 / 4) * (Real.sinh ηStar) ^ 2 + (m ^ 2 - 1 / 4)) /
              (Real.sinh ηStar) ^ 2 := by
          rw [add_div, mul_div_cancel_right₀ _ hsq_ne]
        _ = 0 := by rw [hmul, zero_div]
  have hderiv : HasDerivAt (toroidalPotential n m)
      (-2 * toroidalCentrifugalCoeff m * Real.cosh ηStar / (Real.sinh ηStar) ^ 3) ηStar := by
    unfold toroidalPotential
    have hsinh_sq : HasDerivAt (fun x : ℝ => (Real.sinh x) ^ 2)
        (2 * Real.sinh ηStar * Real.cosh ηStar) ηStar := by
      convert (Real.hasDerivAt_sinh ηStar).pow 2 using 1
      ring
    have hquot : HasDerivAt (fun x : ℝ => toroidalCentrifugalCoeff m / (Real.sinh x) ^ 2)
        (-(toroidalCentrifugalCoeff m * (2 * Real.sinh ηStar * Real.cosh ηStar)) /
          ((Real.sinh ηStar) ^ 2) ^ 2) ηStar := by
      simpa using (hasDerivAt_const ηStar (toroidalCentrifugalCoeff m)).div hsinh_sq (ne_of_gt hsq_pos)
    have hconst : HasDerivAt (fun _ : ℝ => n ^ 2 - 1 / 4) 0 ηStar :=
      hasDerivAt_const ηStar (n ^ 2 - 1 / 4)
    convert hconst.add hquot using 1
    field_simp [hsinh_ne]
    ring
  have hslope_neg :
      -2 * toroidalCentrifugalCoeff m * Real.cosh ηStar / (Real.sinh ηStar) ^ 3 < 0 := by
    have hcosh_pos : 0 < Real.cosh ηStar := Real.cosh_pos ηStar
    have hcube_pos : 0 < (Real.sinh ηStar) ^ 3 := pow_pos hsinh_pos 3
    have hnum_neg : -2 * toroidalCentrifugalCoeff m * Real.cosh ηStar < 0 := by
      nlinarith
    exact div_neg_of_neg_of_pos hnum_neg hcube_pos
  exact ⟨hiff, hderiv, hslope_neg⟩

/-- Normalized quartic ladder polynomial $P(u) = 1 + c_1 u + c_2 u^2 + c_3 u^3 + c_4 u^4$ over any
commutative ring $R$. -/
noncomputable def weberJetPoly {R : Type*} [CommRing R] (c₁ c₂ c₃ c₄ : R) : R[X] :=
  1 + C c₁ * X + C c₂ * X ^ 2 + C c₃ * X ^ 3 + C c₄ * X ^ 4

/-- Parabolic Cylinder (Weber) differential operator
$\mathcal{L}_{A,B,C}(P)(u) = P''(u) + (A + B u + C u^2) P(u)$ on $R[X]$. -/
noncomputable def parabolicCylinderOp {R : Type*} [CommRing R] (A B C_param : R) (P : R[X]) : R[X] :=
  P.derivative.derivative + (C A + C B * X + C C_param * X ^ 2) * P

/-- Over any commutative ring $R$, the first three Taylor coefficients ($u^0, u^1, u^2$) of
$\mathcal{L}_{A,B,C}(1 + c_1 u + c_2 u^2 + c_3 u^3 + c_4 u^4)$ equal
$2 c_2 + A$, $6 c_3 + A c_1 + B$, and $12 c_4 + A c_2 + B c_1 + C$. -/
theorem parabolicCylinderOp_weberJetPoly_coeffs {R : Type*} [CommRing R]
    (A B C_param c₁ c₂ c₃ c₄ : R) :
    (parabolicCylinderOp A B C_param (weberJetPoly c₁ c₂ c₃ c₄)).coeff 0 = 2 * c₂ + A ∧
      (parabolicCylinderOp A B C_param (weberJetPoly c₁ c₂ c₃ c₄)).coeff 1 =
        6 * c₃ + A * c₁ + B ∧
      (parabolicCylinderOp A B C_param (weberJetPoly c₁ c₂ c₃ c₄)).coeff 2 =
        12 * c₄ + A * c₂ + B * c₁ + C_param := by
  have hderiv2 :
      (weberJetPoly c₁ c₂ c₃ c₄).derivative.derivative =
        C (2 * c₂) + C (6 * c₃) * X + C (12 * c₄) * X ^ 2 := by
    unfold weberJetPoly
    simp only [derivative_add, derivative_mul, derivative_one, derivative_C, derivative_X,
      derivative_X_pow, zero_mul, zero_add, mul_one]
    ext k
    simp only [coeff_add, coeff_C_mul, coeff_X_pow, coeff_C, coeff_X]
    rcases k with _ | _ | _ | k <;> simp <;> ring
  have hprod :
      parabolicCylinderOp A B C_param (weberJetPoly c₁ c₂ c₃ c₄) =
        C (2 * c₂) + C (6 * c₃) * X + C (12 * c₄) * X ^ 2 +
          (C A + C B * X + C C_param * X ^ 2) * weberJetPoly c₁ c₂ c₃ c₄ := by
    unfold parabolicCylinderOp
    rw [hderiv2]
  rw [hprod]
  unfold weberJetPoly
  refine ⟨?_, ?_, ?_⟩
  · simp [coeff_add, coeff_mul, coeff_one, coeff_X]
  · simp [coeff_add, coeff_mul, coeff_one, coeff_X, Finset.Nat.antidiagonal_succ]; ring
  · simp [coeff_add, coeff_mul, coeff_one, coeff_X, Finset.Nat.antidiagonal_succ]; ring

/-- **Mode-Selective Order-Gap & Exact Parabolic Cylinder Recurrence (`c_4 = 2 ↔ C = -22`):**
1. Symmetrizing any square-root-coordinate series $g(w) = 1 + a_1 w + a_2 w^2 + a_3 w^3 + a_4 w^4$
   via $\tfrac{1}{2}(g(w) + g(-w))$ kills the odd $w = \sqrt{u}$ and $w^3 = u\sqrt{u}$ terms identically,
   yielding $1 + a_2 w^2 + a_4 w^4$; and on $P(u) = 1 + c_1 u + c_2 u^2 + c_3 u^3 + c_4 u^4$,
   $(P'(0) = 0) \iff (c_1 = 0)$.
2. The first three Taylor coefficients ($u^0, u^1, u^2$) of
   $\mathcal{L}_{A,B,C}(1 + c_1 u + c_2 u^2 + c_3 u^3 + c_4 u^4)$ equal
   $2 c_2 + A$, $6 c_3 + A c_1 + B$, and $12 c_4 + A c_2 + B c_1 + C$.
3. Under the order-gap $c_1 = 0$ and canonical quadratic rung $c_2 = -1$, vanishing of
   $\mathrm{coeff}_0, \mathrm{coeff}_1, \mathrm{coeff}_2$ at $c_3 = -2$ holds if and only if
   $A = 2$, $B = 12$, and $C = 2 - 12 c_4$; in particular,
   **$c_4 = 2$ holds if and only if $C = -22$** (with $(A, B, C) = (2, 12, -22)$). -/
theorem parabolic_cylinder_order_gap_and_c4_iff :
    (∀ (w a₁ a₂ a₃ a₄ : ℝ),
        ((1 + a₁ * w + a₂ * w ^ 2 + a₃ * w ^ 3 + a₄ * w ^ 4) +
          (1 + a₁ * (-w) + a₂ * (-w) ^ 2 + a₃ * (-w) ^ 3 + a₄ * (-w) ^ 4)) / 2 =
          1 + a₂ * w ^ 2 + a₄ * w ^ 4) ∧
      (∀ (c₁ c₂ c₃ c₄ : ℚ),
        (weberJetPoly c₁ c₂ c₃ c₄).derivative.coeff 0 = 0 ↔ c₁ = 0) ∧
      (∀ (A B C_param c₁ c₂ c₃ c₄ : ℝ),
        (parabolicCylinderOp A B C_param (weberJetPoly c₁ c₂ c₃ c₄)).coeff 0 = 2 * c₂ + A ∧
          (parabolicCylinderOp A B C_param (weberJetPoly c₁ c₂ c₃ c₄)).coeff 1 =
            6 * c₃ + A * c₁ + B ∧
          (parabolicCylinderOp A B C_param (weberJetPoly c₁ c₂ c₃ c₄)).coeff 2 =
            12 * c₄ + A * c₂ + B * c₁ + C_param) ∧
      (∀ (A B C_param c₄ : ℚ),
        ((parabolicCylinderOp A B C_param (weberJetPoly 0 (-1) (-2) c₄)).coeff 0 = 0 ∧
          (parabolicCylinderOp A B C_param (weberJetPoly 0 (-1) (-2) c₄)).coeff 1 = 0 ∧
          (parabolicCylinderOp A B C_param (weberJetPoly 0 (-1) (-2) c₄)).coeff 2 = 0) ↔
          (A = 2 ∧ B = 12 ∧ C_param = 2 - 12 * c₄)) ∧
      (∀ (C_param c₄ : ℚ),
        (parabolicCylinderOp 2 12 C_param (weberJetPoly 0 (-1) (-2) c₄)).coeff 2 = 0 →
          (c₄ = 2 ↔ C_param = -22)) := by
  refine ⟨?_, ?_, fun A B C_param c₁ c₂ c₃ c₄ =>
    parabolicCylinderOp_weberJetPoly_coeffs A B C_param c₁ c₂ c₃ c₄, ?_, ?_⟩
  · intro w a₁ a₂ a₃ a₄
    ring
  · intro c₁ c₂ c₃ c₄
    unfold weberJetPoly
    simp only [derivative_add, derivative_mul, derivative_one, derivative_C, derivative_X,
      derivative_X_pow, zero_mul, zero_add, mul_one, coeff_add, coeff_C_mul, coeff_X_pow,
      coeff_C]
    simp
  · intro A B C_param c₄
    have hc := parabolicCylinderOp_weberJetPoly_coeffs A B C_param 0 (-1) (-2) c₄
    rw [hc.1, hc.2.1, hc.2.2]
    constructor
    · rintro ⟨h0, h1, h2⟩
      exact ⟨by linarith, by linarith, by linarith⟩
    · rintro ⟨rfl, rfl, rfl⟩
      exact ⟨by ring, by ring, by ring⟩
  · intro C_param c₄ h2
    have hc := (parabolicCylinderOp_weberJetPoly_coeffs 2 12 C_param 0 (-1) (-2) c₄).2.2
    rw [hc] at h2
    constructor
    · intro hc4; linarith
    · intro hC; linarith

end QOU.MassEndomorphism.QBetaToroidalHarmonicsBasis
