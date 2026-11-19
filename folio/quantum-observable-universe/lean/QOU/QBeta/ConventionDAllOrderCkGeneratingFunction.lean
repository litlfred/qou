import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Positivity
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.QBeta.CoshHolonomyAndGPMTBaseBridge

/-!
# All-Order Convention-D Higher-`c_k` Generating Function, Lagrange–Bürmann Critical Radius, and Distinct-Partition Extraction (`qou-q2oa`, `qou-cds1`)

This module formalizes the all-order algebraic and real-analytic theory of the Convention-D
neutron-beta decay ladder product
$$\Pi_{\mathrm{op}}(u) = \prod_{k=2}^{\infty} \bigl(1 + c_k u^k\bigr)
  = 1 + \sum_{n=2}^{\infty} p_n u^n$$
derived purely from the parameter-free Convention-D + GPMT + Two-Term Categorical Lagrangian
operator building blocks:

1. **Section 1 (Bar-Even `H = (q - q⁻¹)^2` Rational & Polynomial Structure of All Operator Building Blocks)**:
   * Every bar-even component of the Convention-D + GPMT + Two-Term Borromean `V^3` operator is an
     exact rational function or polynomial in the single bar-invariant variable
     `H := hSq q = (q - q⁻¹)^2`:
     - `w21_zD_eq_inv_hSq_add_four`: `w_{(2,1)}(z_D) = 1 / (H + 4)`
     - `w3_zD_eq_hSq_add_two_div_hSq_add_four`: `w_{(3)}(z_D) = (H + 2) / (H + 4)`
     - `dMod111Abs_sq_eq_inv_hSq`: `|d_D(S^{(1^3)})|^2 = 1 / ((H + 4)(H + 3)^2)`
     - `kdFullTwistChar_eq_hSq_poly`: `C_{KD}^{(6)}(q) = 1 + (9/2) H + 3 H^2 + (1/2) H^3`
     - `trace_QAdjp_borromeanV3_eq_hSq_poly`: `tr((Q_{12}^{(p)} + Q_{23}^{(p)}) V_p^3) = -2 H^2 (H + 3) / 9`
     - `trace_QAdjn_borromeanV3_connected_eq_hSq_poly`:
       `tr((Q_{12}^{(n)} + Q_{23}^{(n)}) V_n^3)_{conn} = H^2 (2 H + 3) / 9`
     - `trace_QAdj_connected_diff_borromeanV3_eq_hSq_poly`:
       `Δtr_{QED,conn}(V^3) = H^2 (4 H + 9) / 9`
     - `loopMeanW3_sq_eq_hSq_rat`: `((q + q⁻¹) w_{(3)}(z_D))^2 = (H + 2)^2 / (H + 4)`
   * Theorem `trace_QAdj_connected_diff_borromeanV3_eq_mul_uBarSq` proves that the connected
     4th-order Borromean `V^3` `(n - p)` QED trace difference shares the exact `H^2 = (q - q⁻¹)^4`
     leading order of the squared ladder expansion coordinate
     `uBarSq H = H^2 (H + 3) / (16 (H + 4))`:
     `Δtr_{QED,conn}(V^3) = (16 (H + 4)(4 H + 9) / (9 (H + 3))) · uBarSq H`.

2. **Section 2 (Jacobian Factorization, Real-Axis Strict Monotonicity, and Critical Branch Point `H_*`)**:
   * The squared bar-even ladder coordinate `uBarSq H = H^2 (H + 3) / (16 (H + 4))` has
     quotient-rule derivative numerator `H · (2 H^2 + 15 H + 24)` (`uBarSq_deriv_numerator_factorization`)
     and exact two-point difference numerator factorization (`uBarSq_numerator_diff_factorization`),
     yielding strict monotonicity `uBarSq_strictMonoOn_nonneg` across the entire physical real
     half-line `H ≥ 0` (`q ∈ ℝ \ {0}`).
   * In the complex `H`-plane, the critical quadratic `criticalQuad H = 2 H^2 + 15 H + 24` satisfies
     `8 · criticalQuad H = (4 H + 15)^2 - 33` (`criticalQuad_discriminant_eq_33`) and vanishes at
     `criticalBranchPointH = (-15 + √33) / 4 ∈ (-3, -2)` (`criticalQuad_at_criticalBranchPointH`,
     `criticalBranchPointH_bounds`), strictly closer to `H = 0` than the `[3]_q = 0` zero at
     `H = -3` and the `[2]_q = 0` pole at `H = -4`. This branch point determines the exact
     Lagrange–Bürmann radius of convergence `R_u = √(uBarSq H_*) ≈ 0.3690087298281905`
     (`lagrangeBurmannRadiusSq_pos`).

3. **Section 3 (Distinct-Partition Triangular Bijection Between `(c_2, ..., c_{10})` and `(p_2, ..., p_{10})`)**:
   * Because each factor `(1 + c_k u^k)` in `∏_{k=2}^∞ (1 + c_k u^k)` is linear in `u^k`, the power-series
     coefficient `p_n = [u^n] ∏_{k≥2} (1 + c_k u^k)` is the sum over partitions of `n` into
     **distinct parts `≥ 2`**.
   * Theorems `ckFromSeries_seriesFromCk` and `seriesFromCk_ckFromSeries` establish a division-free
     polynomial bijection over any commutative ring `R` between the ladder coefficients
     `(c_2, ..., c_{10})` and the Taylor coefficients `(p_2, ..., p_{10})`, and
     `truncatedProduct4_sub_series4` and `truncatedProduct6_sub_series6` certify the explicit
     polynomial product expansions.

4. **Section 4 (Geometric Cauchy Tail Bound Below `1 ppQ = 10^{-15}`)**:
   * Theorems `geometric_tail_ratio_bound_N8` and `geometric_tail_ratio_bound_N9` prove that for any
     convergence ratio `0 ≤ r ≤ 1/40` (bounding the physical ratio `u(q_0) / R_u ≈ 0.0230774 < 1/40`),
     the geometric Cauchy remainder `r^{N+1} / (1 - r)` is strictly below `4 × 10^{-15}` at `N = 8`
     and strictly below `10^{-16} < 10^{-15}` (`1 ppQ`) at `N = 9`.

Compute companion: `computations/qbeta/qbeta_convention_d_all_order_ck_generating_probe.py`
Witness: `computations/qbeta/qbeta-convention-d-all-order-ck-generating.witness.json`
-/

namespace QOU.QBeta.ConventionDAllOrderCkGeneratingFunction

open Matrix
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.QBeta.CoshHolonomyAndGPMTBaseBridge

/-! ## Section 1: Bar-Even `H = (q - q⁻¹)^2` Rational & Polynomial Structure of Operator Building Blocks -/

section BarEvenHStructure

variable {K : Type*} [Field K]

/-- The bar-invariant squared holonomy step `H(q) = (q - q⁻¹)^2`. -/
def hSq (q : K) : K := (q - q⁻¹) ^ 2

/-- Bar-invariance of `hSq`: `hSq (q⁻¹) = hSq q`. -/
theorem hSq_inv (q : K) : hSq q⁻¹ = hSq q := by
  unfold hSq
  rw [inv_inv]
  ring

/-- Vanishing at the classical limit `q = 1`: `hSq 1 = 0`. -/
theorem hSq_one : hSq (1 : K) = 0 := by
  unfold hSq
  simp

/-- Fundamental Laurent bridge `q^2 + 1 = q · (q + q⁻¹)` squared:
`(q^2 + 1)^2 = q^2 · (hSq q + 4)`. -/
theorem q_sq_add_one_sq_eq_q_sq_mul_hSq_add_four (q : K) (hq : q ≠ 0) :
    (q ^ 2 + 1) ^ 2 = q ^ 2 * (hSq q + 4) := by
  unfold hSq
  field_simp
  ring

/-- Fundamental Laurent bridge for the quantum integer `[3]_q` numerator:
`q^4 + q^2 + 1 = q^2 · (hSq q + 3)`. -/
theorem q_pow_four_add_q_sq_add_one_eq_q_sq_mul_hSq_add_three (q : K) (hq : q ≠ 0) :
    q ^ 4 + q ^ 2 + 1 = q ^ 2 * (hSq q + 3) := by
  unfold hSq
  field_simp
  ring

/-- Fundamental Laurent bridge for the symmetric Wedderburn numerator:
`q^4 + 1 = q^2 · (hSq q + 2)`. -/
theorem q_pow_four_add_one_eq_q_sq_mul_hSq_add_two (q : K) (hq : q ≠ 0) :
    q ^ 4 + 1 = q ^ 2 * (hSq q + 2) := by
  unfold hSq
  field_simp
  ring

/-- Fundamental Laurent bridge for the 4th-order Borromean `V^3` factor:
`(q - 1)^4 (q + 1)^4 = q^4 · (hSq q)^2`. -/
theorem q_sub_one_pow_four_mul_q_add_one_pow_four_eq_hSq_sq (q : K) (hq : q ≠ 0) :
    (q - 1) ^ 4 * (q + 1) ^ 4 = q ^ 4 * (hSq q) ^ 2 := by
  unfold hSq
  field_simp
  ring

/-- **Exact Bar-Even `H`-Form of the Nucleon Wedderburn Weight `w_{(2,1)}(z_D)`**:
`w_{(2,1)}(z_D) = 1 / (hSq q + 4)`. -/
theorem w21_zD_eq_inv_hSq_add_four (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (hH4 : hSq q + 4 ≠ 0) :
    w21 q (zD q) = 1 / (hSq q + 4) := by
  rw [w21_conventionD q hq2 hq4]
  rw [q_sq_add_one_sq_eq_q_sq_mul_hSq_add_four q hq]
  field_simp

/-- **Exact Bar-Even `H`-Form of the Symmetric Wedderburn Weight `w_{(3)}(z_D)`**:
`w_{(3)}(z_D) = (hSq q + 2) / (hSq q + 4)`. -/
theorem w3_zD_eq_hSq_add_two_div_hSq_add_four (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (hH4 : hSq q + 4 ≠ 0) :
    w3 q (zD q) = (hSq q + 2) / (hSq q + 4) := by
  rw [w3_conventionD q hq2 hq4]
  rw [q_pow_four_add_one_eq_q_sq_mul_hSq_add_two q hq,
      q_sq_add_one_sq_eq_q_sq_mul_hSq_add_four q hq]
  field_simp

/-- **Exact Bar-Even `H`-Form of the Squared GPMT `(1^3)` Modified Quantum Dimension**:
`|d_D(S^{(1^3)})|^2 = 1 / ((hSq q + 4)(hSq q + 3)^2)`. -/
theorem dMod111Abs_sq_eq_inv_hSq (q : K) (hq : q ≠ 0)
    (hH4 : hSq q + 4 ≠ 0) (hH3 : hSq q + 3 ≠ 0) :
    (dMod111Abs q) ^ 2 = 1 / ((hSq q + 4) * (hSq q + 3) ^ 2) := by
  rw [dMod111Abs_eq_div q, div_pow, mul_pow]
  rw [q_sq_add_one_sq_eq_q_sq_mul_hSq_add_four q hq,
      q_pow_four_add_q_sq_add_one_eq_q_sq_mul_hSq_add_three q hq]
  field_simp

/-- **Exact Bar-Even Cubic `H`-Polynomial Form of the 6-Crossing Full-Twist Character `C_{KD}^{(6)}(q)`**:
`kdFullTwistChar q = 1 + (9/2) H + 3 H^2 + (1/2) H^3`. -/
theorem kdFullTwistChar_eq_hSq_poly (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    kdFullTwistChar q =
      1 + (9 / 2 : K) * hSq q + 3 * (hSq q) ^ 2 + (1 / 2 : K) * (hSq q) ^ 3 := by
  unfold kdFullTwistChar hSq
  field_simp
  ring

/-- **Exact Bar-Even Cubic `H`-Polynomial Form of the 3×3 Proton Borromean `V^3` Charge Trace**:
`tr((Q_{12}^{(p)} + Q_{23}^{(p)}) V_p^3) = -2 H^2 (H + 3) / 9`. -/
theorem trace_QAdjp_borromeanV3_eq_hSq_poly (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trace ((Q12p + Q23p) * borromeanV3A q) =
      -2 * (hSq q) ^ 2 * (hSq q + 3) / 9 := by
  have h9 : (9 : K) = 3 * 3 := by ring
  rw [trace_QAdjp_borromeanV3 q hq h3]
  have hfac :
      -2 * (q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) =
        -2 * ((q - 1) ^ 4 * (q + 1) ^ 4) * (q ^ 4 + q ^ 2 + 1) := by ring
  rw [hfac, q_sub_one_pow_four_mul_q_add_one_pow_four_eq_hSq_sq q hq,
      q_pow_four_add_q_sq_add_one_eq_q_sq_mul_hSq_add_three q hq, h9]
  field_simp

/-- **Exact Bar-Even Cubic `H`-Polynomial Form of the Connected 3×3 Neutron Borromean `V^3` Charge Trace**:
`tr((Q_{12}^{(n)} + Q_{23}^{(n)}) V_n^3) + (2/9) tr(V_n^3) = H^2 (2 H + 3) / 9`. -/
theorem trace_QAdjn_borromeanV3_connected_eq_hSq_poly (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q) =
      (hSq q) ^ 2 * (2 * hSq q + 3) / 9 := by
  have h9 : (9 : K) = 3 * 3 := by ring
  have hnum : 2 * q ^ 4 - q ^ 2 + 2 = q ^ 2 * (2 * hSq q + 3) := by
    unfold hSq
    field_simp
    ring
  rw [trace_QAdjn_borromeanV3_connected q hq h3,
      q_sub_one_pow_four_mul_q_add_one_pow_four_eq_hSq_sq q hq, hnum, h9]
  field_simp

/-- **Exact Bar-Even Cubic `H`-Polynomial Form of the Connected `(n - p)` Borromean `V^3` QED Trace Difference**:
`Δtr_{QED,conn}(V^3) = H^2 (4 H + 9) / 9`. -/
theorem trace_QAdj_connected_diff_borromeanV3_eq_hSq_poly (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    (trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q)) -
        trace ((Q12p + Q23p) * borromeanV3A q) =
      (hSq q) ^ 2 * (4 * hSq q + 9) / 9 := by
  have h9 : (9 : K) = 3 * 3 := by ring
  rw [trace_QAdjn_borromeanV3_connected_eq_hSq_poly q hq h3,
      trace_QAdjp_borromeanV3_eq_hSq_poly q hq h3, h9]
  field_simp
  ring

/-- **Exact Bar-Even `H`-Rational Form of the Squared Loop-Mean Factor `((q + q⁻¹) w_{(3)}(z_D))^2`**:
`((q + q⁻¹) · w_{(3)}(z_D))^2 = (hSq q + 2)^2 / (hSq q + 4)`. -/
theorem loopMeanW3_sq_eq_hSq_rat (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (hH4 : hSq q + 4 ≠ 0) :
    ((q + q⁻¹) * w3 q (zD q)) ^ 2 = (hSq q + 2) ^ 2 / (hSq q + 4) := by
  rw [w3_zD_eq_hSq_add_two_div_hSq_add_four q hq hq2 hq4 hH4]
  have hqp : (q + q⁻¹) ^ 2 = hSq q + 4 := by
    unfold hSq
    field_simp
    ring
  rw [mul_pow, div_pow, hqp]
  field_simp

end BarEvenHStructure

/-! ## Section 2: Jacobian Factorization, Real-Axis Strict Monotonicity, and Critical Branch Point `H_*` -/

section LagrangeBurmannCriticalRadius

variable {K : Type*} [Field K]

/-- The squared bar-even Convention-D ladder coordinate as a rational function of `H = (q - q⁻¹)^2`:
`uBarSq(H) = H^2 (H + 3) / (16 (H + 4))`. -/
def uBarSq (H : K) : K :=
  H ^ 2 * (H + 3) / (16 * (H + 4))

/-- The critical quadratic factor of `d(uBarSq)/dH`:
`criticalQuad(H) = 2 H^2 + 15 H + 24`. -/
def criticalQuad (H : K) : K :=
  2 * H ^ 2 + 15 * H + 24

/-- Equivalence between `uBarSq (hSq q)` and the Convention-D Laurent formula
`((q - q⁻¹)^2 / 4)^2 · (q^4 + q^2 + 1) / (q^2 + 1)^2`. -/
theorem uBarSq_hSq_eq_laurent (q : K) (hq : q ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    uBarSq (hSq q) =
      (q - q⁻¹) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (16 * (q ^ 2 + 1) ^ 2) := by
  have h16 : (16 : K) = 2 * 2 * 2 * 2 := by ring
  unfold uBarSq
  rw [q_pow_four_add_q_sq_add_one_eq_q_sq_mul_hSq_add_three q hq,
      q_sq_add_one_sq_eq_q_sq_mul_hSq_add_four q hq]
  unfold hSq at *
  rw [h16]
  field_simp

/-- **Exact Ratio Between the 2-Term Borromean `(n - p)` QED Matrix Trace Difference and `uBarSq (hSq q)`**:
Because both `Δtr_{QED,conn}(V^3)` and `uBarSq (hSq q)` share the exact `H^2 = (q - q⁻¹)^4`
factor (`O(s^4)` at `q = 1`), their ratio is a nonsingular rational function of `H`:
`Δtr_{QED,conn}(V^3) = (16 (H + 4)(4 H + 9) / (9 (H + 3))) · uBarSq H`. -/
theorem trace_QAdj_connected_diff_borromeanV3_eq_mul_uBarSq (q : K) (hq : q ≠ 0)
    (hH3 : hSq q + 3 ≠ 0) (hH4 : hSq q + 4 ≠ 0)
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    (trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q)) -
        trace ((Q12p + Q23p) * borromeanV3A q) =
      (16 * (hSq q + 4) * (4 * hSq q + 9) / (9 * (hSq q + 3))) * uBarSq (hSq q) := by
  have h16 : (16 : K) = 2 * 2 * 2 * 2 := by ring
  have h9 : (9 : K) = 3 * 3 := by ring
  rw [trace_QAdj_connected_diff_borromeanV3_eq_hSq_poly q hq h3]
  unfold uBarSq
  rw [h16, h9]
  field_simp

/-- **Quotient-Rule Derivative Numerator Factorization for `uBarSq`**:
With numerator `N(H) = H^3 + 3 H^2` (`N'(H) = 3 H^2 + 6 H`) and denominator factor `D(H) = H + 4`
(`D'(H) = 1`), the quotient-rule numerator `N'(H) D(H) - N(H) D'(H)` factors as
`H · criticalQuad H = H (2 H^2 + 15 H + 24)`. -/
theorem uBarSq_deriv_numerator_factorization {R : Type*} [CommRing R] (H : R) :
    (3 * H ^ 2 + 6 * H) * (H + 4) - (H ^ 3 + 3 * H ^ 2) * 1 =
      H * (2 * H ^ 2 + 15 * H + 24) := by
  ring

/-- **Two-Point Cross-Multiplied Difference Factorization for `uBarSq`**:
`(H₁^2 (H₁ + 3))(H₂ + 4) - (H₂^2 (H₂ + 3))(H₁ + 4)` factors as `(H₁ - H₂)` times a polynomial
with strictly positive coefficients on `H₁, H₂ ≥ 0`. -/
theorem uBarSq_numerator_diff_factorization {R : Type*} [CommRing R] (H₁ H₂ : R) :
    (H₁ ^ 2 * (H₁ + 3)) * (H₂ + 4) - (H₂ ^ 2 * (H₂ + 3)) * (H₁ + 4) =
      (H₁ - H₂) *
        (H₁ * H₂ * (H₁ + H₂) + 4 * (H₁ ^ 2 + H₁ * H₂ + H₂ ^ 2) +
          3 * H₁ * H₂ + 12 * (H₁ + H₂)) := by
  ring

/-- **Discriminant Completion of `criticalQuad`**:
`8 · (2 H^2 + 15 H + 24) = (4 H + 15)^2 - 33`. -/
theorem criticalQuad_discriminant_eq_33 (H : K) :
    8 * criticalQuad H = (4 * H + 15) ^ 2 - 33 := by
  unfold criticalQuad
  ring

/-- Over `ℝ`, for all `H ≥ 0`, `uBarSq H ≥ 0` and `criticalQuad H ≥ 24 > 0` (complete absence of
singularities or critical points on the physical half-line `H ≥ 0`). -/
theorem uBarSq_nonneg_and_criticalQuad_pos {H : ℝ} (hH : 0 ≤ H) :
    0 ≤ uBarSq H ∧ 24 ≤ criticalQuad H := by
  constructor
  · unfold uBarSq
    positivity
  · unfold criticalQuad
    have hsq : 0 ≤ H ^ 2 := sq_nonneg H
    linarith

/-- **Strict Monotonicity of `uBarSq` on the Physical Real Half-Line `H ≥ 0`**:
For `0 ≤ H₂ < H₁`, `uBarSq H₂ < uBarSq H₁`. -/
theorem uBarSq_strictMonoOn_nonneg {H₁ H₂ : ℝ} (hH₂ : 0 ≤ H₂) (hlt : H₂ < H₁) :
    uBarSq H₂ < uBarSq H₁ := by
  have hH₁ : 0 < H₁ := lt_of_le_of_lt hH₂ hlt
  have hD₁ : 0 < H₁ + 4 := by linarith
  have hD₂ : 0 < H₂ + 4 := by linarith
  rw [← sub_pos]
  unfold uBarSq
  have hdiff :
      H₁ ^ 2 * (H₁ + 3) / (16 * (H₁ + 4)) - H₂ ^ 2 * (H₂ + 3) / (16 * (H₂ + 4)) =
        ((H₁ ^ 2 * (H₁ + 3)) * (H₂ + 4) - (H₂ ^ 2 * (H₂ + 3)) * (H₁ + 4)) /
          (16 * (H₁ + 4) * (H₂ + 4)) := by
    field_simp
  rw [hdiff, uBarSq_numerator_diff_factorization]
  have hsub : 0 < H₁ - H₂ := sub_pos.mpr hlt
  have hbrack :
      0 < H₁ * H₂ * (H₁ + H₂) + 4 * (H₁ ^ 2 + H₁ * H₂ + H₂ ^ 2) +
            3 * H₁ * H₂ + 12 * (H₁ + H₂) := by
    positivity
  have hden : 0 < 16 * (H₁ + 4) * (H₂ + 4) := by positivity
  exact div_pos (mul_pos hsub hbrack) hden

/-- The nearest complex/negative-axis critical branch point `H_* = (-15 + √33) / 4` of
`uBarSq(H)`, which determines the Lagrange–Bürmann radius of convergence `R_u`. -/
noncomputable def criticalBranchPointH : ℝ :=
  (-15 + Real.sqrt 33) / 4

/-- `criticalBranchPointH` is an exact root of `criticalQuad H = 2 H^2 + 15 H + 24`. -/
theorem criticalQuad_at_criticalBranchPointH :
    criticalQuad criticalBranchPointH = 0 := by
  have hdisc := criticalQuad_discriminant_eq_33 criticalBranchPointH
  have hlin : 4 * criticalBranchPointH + 15 = Real.sqrt 33 := by
    unfold criticalBranchPointH
    ring
  rw [hlin, Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 33), sub_self] at hdisc
  linarith

/-- **Singularity-Ordering Bounds on `criticalBranchPointH`**:
`-3 < criticalBranchPointH` and `criticalBranchPointH < -2` (in fact `-2.32 < H_* < -2.31`),
proving that as `|H|` grows from `0`, the Lagrange–Bürmann branch point `|H_*| ≈ 2.313859`
is encountered strictly before the `[3]_q = 0` zero at `H = -3` and the `[2]_q = 0` pole at `H = -4`. -/
theorem criticalBranchPointH_bounds :
    -3 < criticalBranchPointH ∧ criticalBranchPointH < -2 := by
  unfold criticalBranchPointH
  have hlow : (5 : ℝ) < Real.sqrt 33 := by
    rw [← Real.sqrt_sq (by norm_num : (0 : ℝ) ≤ 5)]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  have hhigh : Real.sqrt 33 < 6 := by
    rw [← Real.sqrt_sq (by norm_num : (0 : ℝ) ≤ 6)]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  constructor <;> linarith

/-- Exact closed form for the squared Lagrange–Bürmann radius of convergence
`R_u^2 = uBarSq(H_*) = H_*^2 (H_* + 3) / (16 (H_* + 4)) > 0`. -/
noncomputable def lagrangeBurmannRadiusSq : ℝ :=
  uBarSq criticalBranchPointH

/-- Strict positivity of `lagrangeBurmannRadiusSq` (`R_u^2 > 0`). -/
theorem lagrangeBurmannRadiusSq_pos : 0 < lagrangeBurmannRadiusSq := by
  unfold lagrangeBurmannRadiusSq uBarSq
  have hb := criticalBranchPointH_bounds
  have hH_neg : criticalBranchPointH < 0 := by linarith [hb.2]
  have hH_sq_pos : 0 < criticalBranchPointH ^ 2 := sq_pos_of_neg hH_neg
  have hH3_pos : 0 < criticalBranchPointH + 3 := by linarith [hb.1]
  have hH4_pos : 0 < 16 * (criticalBranchPointH + 4) := by linarith [hb.1]
  exact div_pos (mul_pos hH_sq_pos hH3_pos) hH4_pos

end LagrangeBurmannCriticalRadius

/-! ## Section 3: Distinct-Partition Triangular Bijection Between `(c_2, ..., c_{10})` and `(p_2, ..., p_{10})` -/

section DistinctPartitionBijection

variable {R : Type*} [CommRing R]

/-- Tuple of ladder product coefficients `(c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_{10})`
in `∏_{k=2}^{10} (1 + c_k u^k)`. -/
structure CkTuple10 (R : Type*) where
  c2 : R
  c3 : R
  c4 : R
  c5 : R
  c6 : R
  c7 : R
  c8 : R
  c9 : R
  c10 : R
  deriving DecidableEq, Repr

/-- Tuple of power-series Taylor coefficients `(p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_{10})`
in `1 + ∑_{n=2}^{10} p_n u^n`. -/
structure SeriesTuple10 (R : Type*) where
  p2 : R
  p3 : R
  p4 : R
  p5 : R
  p6 : R
  p7 : R
  p8 : R
  p9 : R
  p10 : R
  deriving DecidableEq, Repr

/-- Forward distinct-partition map `seriesFromCk`: given `(c_2, ..., c_{10})`, returns the
coefficients `(p_2, ..., p_{10})` of `∏_{k=2}^{10} (1 + c_k u^k) mod u^{11}`, where `p_n` sums
over all partitions of `n` into distinct integers `≥ 2`. -/
def seriesFromCk (c : CkTuple10 R) : SeriesTuple10 R where
  p2 := c.c2
  p3 := c.c3
  p4 := c.c4
  p5 := c.c5 + c.c2 * c.c3
  p6 := c.c6 + c.c2 * c.c4
  p7 := c.c7 + c.c2 * c.c5 + c.c3 * c.c4
  p8 := c.c8 + c.c2 * c.c6 + c.c3 * c.c5
  p9 := c.c9 + c.c2 * c.c7 + c.c3 * c.c6 + c.c4 * c.c5 + c.c2 * c.c3 * c.c4
  p10 := c.c10 + c.c2 * c.c8 + c.c3 * c.c7 + c.c4 * c.c6 + c.c2 * c.c3 * c.c5

/-- Triangular division-free inverse map `ckFromSeries`: extracts `(c_2, ..., c_{10})` uniquely
from the power-series coefficients `(p_2, ..., p_{10})` via `c_n = p_n - [u^n] ∏_{k=2}^{n-1} (1 + c_k u^k)`. -/
def ckFromSeries (p : SeriesTuple10 R) : CkTuple10 R :=
  let c2 := p.p2
  let c3 := p.p3
  let c4 := p.p4
  let c5 := p.p5 - c2 * c3
  let c6 := p.p6 - c2 * c4
  let c7 := p.p7 - c2 * c5 - c3 * c4
  let c8 := p.p8 - c2 * c6 - c3 * c5
  let c9 := p.p9 - c2 * c7 - c3 * c6 - c4 * c5 - c2 * c3 * c4
  let c10 := p.p10 - c2 * c8 - c3 * c7 - c4 * c6 - c2 * c3 * c5
  ⟨c2, c3, c4, c5, c6, c7, c8, c9, c10⟩

/-- **Exact Left Inverse (Unique Triangular Extraction of `c_2 ... c_{10}` from `p_2 ... p_{10}`)**:
`ckFromSeries (seriesFromCk c) = c` over any commutative ring `R`. -/
theorem ckFromSeries_seriesFromCk (c : CkTuple10 R) :
    ckFromSeries (seriesFromCk c) = c := by
  cases c
  dsimp only [seriesFromCk, ckFromSeries]
  congr 1 <;> ring

/-- **Exact Right Inverse (Power-Series Reconstruction from `c_2 ... c_{10}`)**:
`seriesFromCk (ckFromSeries p) = p` over any commutative ring `R`. -/
theorem seriesFromCk_ckFromSeries (p : SeriesTuple10 R) :
    seriesFromCk (ckFromSeries p) = p := by
  cases p
  dsimp only [ckFromSeries, seriesFromCk]
  congr 1 <;> ring

/-- **Degree-4 Truncated Product Expansion Identity (`k = 2, 3, 4`)**:
`(1 + c_2 u^2)(1 + c_3 u^3)(1 + c_4 u^4) - (1 + p_2 u^2 + p_3 u^3 + p_4 u^4) = u^5 · R_5(c, u)`. -/
theorem truncatedProduct4_sub_series4 (c : CkTuple10 R) (u : R) :
    (1 + c.c2 * u ^ 2) * (1 + c.c3 * u ^ 3) * (1 + c.c4 * u ^ 4) -
        (1 + (seriesFromCk c).p2 * u ^ 2 + (seriesFromCk c).p3 * u ^ 3 +
          (seriesFromCk c).p4 * u ^ 4) =
      u ^ 5 * (c.c2 * c.c3 + c.c2 * c.c4 * u + c.c3 * c.c4 * u ^ 2 +
        c.c2 * c.c3 * c.c4 * u ^ 4) := by
  unfold seriesFromCk
  ring

/-- **Degree-6 Truncated Product Expansion Identity (`k = 2, ..., 6`)**:
`∏_{k=2}^6 (1 + c_k u^k) - (1 + ∑_{n=2}^6 p_n u^n)` is divisible by `u^7`. -/
theorem truncatedProduct6_sub_series6 (c : CkTuple10 R) (u : R) :
    (1 + c.c2 * u ^ 2) * (1 + c.c3 * u ^ 3) * (1 + c.c4 * u ^ 4) *
        (1 + c.c5 * u ^ 5) * (1 + c.c6 * u ^ 6) -
      (1 + (seriesFromCk c).p2 * u ^ 2 + (seriesFromCk c).p3 * u ^ 3 +
        (seriesFromCk c).p4 * u ^ 4 + (seriesFromCk c).p5 * u ^ 5 +
        (seriesFromCk c).p6 * u ^ 6) =
      u ^ 7 *
        ((c.c2 * c.c5 + c.c3 * c.c4) +
          (c.c2 * c.c6 + c.c3 * c.c5) * u +
          (c.c3 * c.c6 + c.c4 * c.c5 + c.c2 * c.c3 * c.c4) * u ^ 2 +
          (c.c4 * c.c6 + c.c2 * c.c3 * c.c5) * u ^ 3 +
          (c.c5 * c.c6 + c.c2 * c.c3 * c.c6 + c.c2 * c.c4 * c.c5) * u ^ 4 +
          (c.c2 * c.c4 * c.c6 + c.c3 * c.c4 * c.c5) * u ^ 5 +
          (c.c2 * c.c5 * c.c6 + c.c3 * c.c4 * c.c6) * u ^ 6 +
          (c.c3 * c.c5 * c.c6 + c.c2 * c.c3 * c.c4 * c.c5) * u ^ 7 +
          (c.c4 * c.c5 * c.c6 + c.c2 * c.c3 * c.c4 * c.c6) * u ^ 8 +
          c.c2 * c.c3 * c.c5 * c.c6 * u ^ 9 +
          c.c2 * c.c4 * c.c5 * c.c6 * u ^ 10 +
          c.c3 * c.c4 * c.c5 * c.c6 * u ^ 11 +
          c.c2 * c.c3 * c.c4 * c.c5 * c.c6 * u ^ 13) := by
  unfold seriesFromCk
  ring

end DistinctPartitionBijection

/-! ## Section 4: Geometric Cauchy Tail Bound Below `1 ppQ = 10^{-15}` -/

section GeometricCauchyTailBounds

/-- **Finite-Truncation Geometric Cauchy Remainder Bound at `N = 8`**:
For any dimensionless convergence ratio `0 ≤ r ≤ 1/40` (bounding the physical substrate ratio
`u(q_0) / R_u ≈ 0.0230774 < 1/40 = 0.025`), the geometric tail `r^9 / (1 - r)` at truncation
order `N = 8` satisfies `r^9 / (1 - r) < 4 × 10^{-15}`. -/
theorem geometric_tail_ratio_bound_N8 {r : ℝ} (hr0 : 0 ≤ r) (hr : r ≤ 1 / 40) :
    r ^ 9 / (1 - r) < 4 / 10 ^ 15 := by
  have h1mr : 39 / 40 ≤ 1 - r := by linarith
  have h1mr_pos : 0 < 1 - r := by linarith
  have hr9 : r ^ 9 ≤ (1 / 40 : ℝ) ^ 9 := pow_le_pow_left₀ hr0 hr 9
  have hdiv : r ^ 9 / (1 - r) ≤ (1 / 40 : ℝ) ^ 9 / (39 / 40) := by
    exact div_le_div₀ (by positivity) hr9 (by norm_num) h1mr
  have hnum : (1 / 40 : ℝ) ^ 9 / (39 / 40) < 4 / 10 ^ 15 := by norm_num
  exact lt_of_le_of_lt hdiv hnum

/-- **Finite-Truncation Geometric Cauchy Remainder Bound at `N = 9` (Sub-`1 ppQ = 10^{-15}`)**:
For any dimensionless convergence ratio `0 ≤ r ≤ 1/40`, the geometric tail `r^{10} / (1 - r)`
at truncation order `N = 9` satisfies `r^{10} / (1 - r) < 10^{-16} < 10^{-15}` (`1 ppQ`). -/
theorem geometric_tail_ratio_bound_N9 {r : ℝ} (hr0 : 0 ≤ r) (hr : r ≤ 1 / 40) :
    r ^ 10 / (1 - r) < 1 / 10 ^ 16 ∧ (1 / 10 ^ 16 : ℝ) < 1 / 10 ^ 15 := by
  constructor
  · have h1mr : 39 / 40 ≤ 1 - r := by linarith
    have hr10 : r ^ 10 ≤ (1 / 40 : ℝ) ^ 10 := pow_le_pow_left₀ hr0 hr 10
    have hdiv : r ^ 10 / (1 - r) ≤ (1 / 40 : ℝ) ^ 10 / (39 / 40) := by
      exact div_le_div₀ (by positivity) hr10 (by norm_num) h1mr
    have hnum : (1 / 40 : ℝ) ^ 10 / (39 / 40) < 1 / 10 ^ 16 := by norm_num
    exact lt_of_le_of_lt hdiv hnum
  · norm_num

end GeometricCauchyTailBounds

end QOU.QBeta.ConventionDAllOrderCkGeneratingFunction
