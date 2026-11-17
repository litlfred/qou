import Mathlib.Tactic

/-!
# Crossing-Energy Quadratic Identity and Boxed-Formula Discrepancy (`qou-9ilw`)

This module formalizes the algebraic identities underlying `qou-9ilw`:

1. **Crossing-Energy Quadratic Identity**:
   With per-crossing energy $\mathfrak{E}_\times(q) = \tfrac12 (q - q^{-1})$ and skein
   parameter $h(q) = q - q^{-1} = 2 \mathfrak{E}_\times(q)$, the net decay polynomial
   $\Delta_{\mathrm{net}}(q) = \tfrac12 h(q)(h(q) - 2)$ equals
   $2 \mathfrak{E}_\times(q)(\mathfrak{E}_\times(q) - 1)$, and for $q \neq 0$ factors as
   $\frac{(q^2 - 1)(q^2 - 2q - 1)}{2q^2}$.

2. **Boxed-Formula Factor Discrepancy (Defect 1)**:
   The unfactored expression $\frac{q^2 - 2q - 1}{2q}$ differs from
   $\Delta_{\mathrm{net}}(q)$ by
   $$\Delta_{\mathrm{net}}(q) - \frac{q^2 - 2q - 1}{2q}
     = \frac{(q^2 - q - 1)(q^2 - 2q - 1)}{2q^2},$$
   so the cleared-denominator difference vanishes if and only if $q^2 - q - 1 = 0$
   or $q^2 - 2q - 1 = 0$.

3. **Deformation Factor at the Unit-Crossing-Energy Root**:
   Whenever $q^2 - 2q - 1 = 0$ (so $q \neq 0$), the squared deformation factor
   satisfies $(1 - q^{-1})^2 = 10 - 4q$ (which equals $6 - 4\sqrt{2}$ at $q = 1 + \sqrt{2}$).
-/

namespace QOU.MassTheory.CrossingEnergyQuadraticAndBoxDiscrepancy

/-- Skein parameter $h(q) = q - q^{-1}$. -/
noncomputable def skeinParam (q : ℝ) : ℝ :=
  q - 1 / q

/-- Per-crossing energy $\mathfrak{E}_\times(q) = \tfrac12 (q - q^{-1})$. -/
noncomputable def crossingEnergyVal (q : ℝ) : ℝ :=
  (q - 1 / q) / 2

/-- Net decay expression $\Delta_{\mathrm{net}}(q) = \tfrac12 h(q)(h(q) - 2)$. -/
noncomputable def deltaNetVal (q : ℝ) : ℝ :=
  skeinParam q * (skeinParam q - 2) / 2

/-- The net decay expression equals $2 \mathfrak{E}_\times(q)(\mathfrak{E}_\times(q) - 1)$. -/
theorem deltaNetVal_eq_crossingEnergy_quadratic (q : ℝ) :
    deltaNetVal q = 2 * crossingEnergyVal q * (crossingEnergyVal q - 1) := by
  unfold deltaNetVal skeinParam crossingEnergyVal
  have h_id : (q - 1 / q) * (q - 1 / q - 2) / 2 =
      2 * ((q - 1 / q) / 2) * ((q - 1 / q) / 2 - 1) := by
    ring
  exact h_id

/-- For $q \neq 0$, $\Delta_{\mathrm{net}}(q)$ equals the rational form
$\frac{(q^2 - 1)(q^2 - 2q - 1)}{2q^2}$. -/
theorem deltaNetVal_rational_form (q : ℝ) (hq : q ≠ 0) :
    deltaNetVal q = (q ^ 2 - 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 2) := by
  unfold deltaNetVal skeinParam
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have h_rat : (q - 1 / q) * (q - 1 / q - 2) / 2 =
      (q ^ 2 - 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 2) := by
    field_simp [hq, hq2]
    ring
  exact h_rat

/-- The difference between $\Delta_{\mathrm{net}}(q)$ and $\frac{q^2 - 2q - 1}{2q}$
is $\frac{(q^2 - q - 1)(q^2 - 2q - 1)}{2q^2}$ for all $q \neq 0$. -/
theorem deltaNetVal_minus_linear_denom_form (q : ℝ) (hq : q ≠ 0) :
    deltaNetVal q - (q ^ 2 - 2 * q - 1) / (2 * q) =
      (q ^ 2 - q - 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 2) := by
  rw [deltaNetVal_rational_form q hq]
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have h_diff : (q ^ 2 - 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 2) -
      (q ^ 2 - 2 * q - 1) / (2 * q) =
      (q ^ 2 - q - 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 2) := by
    field_simp [hq, hq2]
    ring
  exact h_diff

/-- For $q \neq 0$, the cleared-denominator discrepancy between $\Delta_{\mathrm{net}}(q)$
and $\frac{q^2 - 2q - 1}{2q}$ factors as $(q^2 - q - 1)(q^2 - 2q - 1)$, vanishing
if and only if $q^2 - q - 1 = 0$ or $q^2 - 2q - 1 = 0$. -/
theorem deltaNetVal_cleared_discrepancy_eq_zero_iff (q : ℝ) (hq : q ≠ 0) :
    (deltaNetVal q - (q ^ 2 - 2 * q - 1) / (2 * q)) * (2 * q ^ 2) = 0 ↔
      q ^ 2 - q - 1 = 0 ∨ q ^ 2 - 2 * q - 1 = 0 := by
  have h_diff := deltaNetVal_minus_linear_denom_form q hq
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have h_fac : (deltaNetVal q - (q ^ 2 - 2 * q - 1) / (2 * q)) * (2 * q ^ 2) =
      (q ^ 2 - q - 1) * (q ^ 2 - 2 * q - 1) := by
    rw [h_diff]
    field_simp [hq, hq2]
    ring
  rw [h_fac]
  exact mul_eq_zero

/-- At any root of $q^2 - 2q - 1 = 0$, the squared deformation factor $(1 - q^{-1})^2$
equals $10 - 4q$. -/
theorem deformFactor_sq_at_unit_crossing_root (q : ℝ) (hq : q ≠ 0)
    (hquad : q ^ 2 - 2 * q - 1 = 0) :
    (1 - 1 / q) ^ 2 = 10 - 4 * q := by
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have h_id : (1 - 1 / q) ^ 2 - (10 - 4 * q) =
      (4 * q - 1) * (q ^ 2 - 2 * q - 1) / q ^ 2 := by
    field_simp [hq, hq2]
    ring
  have h_zero : (1 - 1 / q) ^ 2 - (10 - 4 * q) = 0 := by
    rw [h_id, hquad, mul_zero, zero_div]
  linarith

end QOU.MassTheory.CrossingEnergyQuadraticAndBoxDiscrepancy
