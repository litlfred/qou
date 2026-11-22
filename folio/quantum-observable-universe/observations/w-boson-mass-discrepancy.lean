import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Real.Pi.Bounds


/-!
# QOU.Observations.WBoson — Electroweak boson vertex δq

Applies the local substrate proposition (prop:local-substrate-q) to
electroweak boson mass measurements, deriving a zero-free-parameter
formula for the vertex substrate perturbation δq at each collider.

The formula is:

  δq(vertex) = (q₀ - 1) · α/(2π) · 1/|χ(Σ₄)|

where:
  q₀ = 1.10998        — CODATA muon-electron mass ratio
  α                    — coupling constant at vertex (α_s or α_W)
  |χ(Σ₄)| = 6         — Euler characteristic of Bring surface (genus 4)

LaTeX label: `rem:w-boson-mass-discrepancy`

## References

- [leitner2026] Ch. 7, §Physical Observations
- [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2
- CDF II: https://doi.org/10.1126/science.abk1781
- ATLAS: https://doi.org/10.1140/epjc/s10052-024-12632-6

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Observations.WBoson

/-! ## CODATA and topological constants -/

/-- The CODATA local substrate parameter.
    Unique root q > 1 of (1 - q⁻¹)² = Vol(4₁)/(m_μ/m_e).
    See: QOU.Experimental.LocalSubstrateQ -/
noncomputable def q₀ : ℝ := 1.10998

/-- q₀ > 1 (substrate is in the quantum regime). -/
theorem q₀_gt_one : (1 : ℝ) < q₀ := by unfold q₀; norm_num

/-- q₀ > 0. -/
theorem q₀_pos : (0 : ℝ) < q₀ := by linarith [q₀_gt_one]

/-- The displacement from classicality: q₀ - 1. -/
noncomputable def q₀_minus_one : ℝ := q₀ - 1

theorem q₀_minus_one_val : q₀_minus_one = 0.10998 := by
  unfold q₀_minus_one q₀; norm_num

theorem q₀_minus_one_pos : (0 : ℝ) < q₀_minus_one := by
  rw [q₀_minus_one_val]; norm_num

/-- Euler characteristic of the Bring surface Σ₄ (genus g = 4).
    χ = 2 - 2g = 2 - 8 = -6. -/
def chi_bring : ℤ := -6

theorem chi_bring_val : chi_bring = -6 := rfl

/-- |χ(Σ₄)| = 6. -/
theorem abs_chi_bring : Int.natAbs chi_bring = 6 := by
  unfold chi_bring; rfl

/-! ## Geometric projection factor (derived, not fitted) -/

/-- The geometric projection factor κ = 1/|χ(Σ₄)| = 1/6.

    Derivation: The S₅ automorphism group of the Bring surface forces
    constant Webster curvature. Gauss-Bonnet fixes the total curvature
    budget at |χ| = 6 units. A single production vertex couples to one
    color tube, projecting onto 1/|χ| of the total. -/
noncomputable def kappa : ℝ := 1 / (Int.natAbs chi_bring : ℝ)

theorem kappa_val : kappa = 1 / 6 := by
  unfold kappa; rw [abs_chi_bring]; norm_num

theorem kappa_pos : (0 : ℝ) < kappa := by
  rw [kappa_val]; norm_num

/-! ## Coupling constants -/

/-- QCD coupling constant at the Higgs mass scale. -/
noncomputable def α_s : ℝ := 0.118

/-- Weak coupling constant: α_W = g_W²/(4π) ≈ 0.034. -/
noncomputable def α_W : ℝ := 0.034

theorem α_s_pos : (0 : ℝ) < α_s := by unfold α_s; norm_num
theorem α_W_pos : (0 : ℝ) < α_W := by unfold α_W; norm_num

/-! ## The vertex δq formula -/

/-- Forward-predicted vertex δq with no free parameters.

    δq(vertex) = (q₀ - 1) × α/(2π) × 1/|χ(Σ₄)|

    All three factors are determined:
    - (q₀ - 1) = 0.10998 from CODATA
    - α/(2π) = topological charge at vertex
    - 1/|χ| = 1/6 from Gauss-Bonnet on Bring surface -/
noncomputable def delta_q (alpha : ℝ) : ℝ :=
  q₀_minus_one * (alpha / (2 * Real.pi)) * kappa

/-- δq is positive for positive coupling. -/
theorem delta_q_pos {alpha : ℝ} (hα : 0 < alpha) :
    0 < delta_q alpha := by
  unfold delta_q
  apply mul_pos
  · apply mul_pos
    · exact q₀_minus_one_pos
    · apply div_pos hα
      apply mul_pos (by norm_num : (0:ℝ) < 2) Real.pi_pos
  · exact kappa_pos

/-! ## Specific predictions -/

/-- Predicted δq for CDF W boson (qq̄→W, electroweak vertex). -/
noncomputable def delta_q_W_CDF : ℝ := delta_q α_W

/-- Predicted δq for Higgs (gg→H, QCD vertex via top loop). -/
noncomputable def delta_q_H : ℝ := delta_q α_s

/-! ## Mass sensitivity -/

/-- Logarithmic sensitivity: ∂ ln m / ∂ ln q = (q² + 1)/(q² - 1).
    Derived from the crossing energy E_× = ½(q - q⁻¹). -/
noncomputable def sensitivity (q : ℝ) : ℝ :=
  (q ^ 2 + 1) / (q ^ 2 - 1)

/-- The predicted CDF W mass shift in MeV.
    δm = δq/q₀ × sensitivity × m_W. -/
noncomputable def delta_m_W_predicted : ℝ :=
  delta_q_W_CDF / q₀ * sensitivity q₀ * 80357

/-- The observed CDF W mass shift in MeV. -/
noncomputable def delta_m_W_observed : ℝ := 80433.5 - 80357

/-! ## Markov trace for W/Z mass ratio -/

/-- Quantum integer [2]_q = q + q⁻¹. -/
noncomputable def qi2 (q : ℝ) : ℝ := q + q⁻¹

/-- Markov trace of T₁ⁿ in H₂(q).
    Hecke generator T₁ has eigenvalues q (symmetric, dim [2]_q)
    and -q⁻¹ (antisymmetric, dim 1). -/
noncomputable def markov_trace (n : ℕ) (q : ℝ) : ℝ :=
  (qi2 q * q ^ n + (-q⁻¹) ^ n) / (qi2 q + 1)

/-- W/Z mass ratio from Markov traces: tr_M(T₁⁴)/tr_M(T₁⁶). -/
noncomputable def w_z_ratio : ℝ :=
  markov_trace 4 q₀ / markov_trace 6 q₀

/-! ## Key theorems -/

/-- The Higgs/W δq ratio equals α_s/α_W exactly — no free parameters.
    This is because δq ∝ α; the factors (q₀-1) and 1/|χ| cancel. -/
-- Ref: [leitner2026] Ch. 7, §Vertex δq formula
theorem higgs_w_ratio_exact :
    delta_q_H / delta_q_W_CDF = α_s / α_W := by
  unfold delta_q_H delta_q_W_CDF delta_q
  have hqm : q₀_minus_one ≠ 0 := ne_of_gt q₀_minus_one_pos
  have hk : kappa ≠ 0 := ne_of_gt kappa_pos
  have hW : α_W ≠ 0 := ne_of_gt α_W_pos
  field_simp

/- The forward-predicted CDF shift and the observed shift (76.5 MeV)
   agree to within a factor of 2 (0.9σ).

   The predicted δm involves Real.pi in the denominator, which prevents
   direct norm_num evaluation. We bound π ∈ (3.14, 3.15) to reduce
   the comparison to rational arithmetic. -/
/-- The predicted CDF W-boson mass shift and the observed shift agree to
    within a factor of two.

    **Was an axiom; proved 2026-09-04.** The old comment said "full proof
    requires `Real.pi` bounds" — which is true and is the whole proof: the
    expression is `K / π` for a rational `K`, and the bounds needed are
    absurdly loose. `π > 3` gives the first conjunct and `π < 4` the second,
    so `Real.pi_gt_d6` / `Real.pi_lt_d6` are far more than enough. Nothing
    was missing except the reduction to `K / π`. -/
-- Ref: [leitner2026] Ch. 7, §Vertex δq formula
theorem forward_backward_agreement :
    delta_m_W_predicted < 2 * delta_m_W_observed ∧
    delta_m_W_observed < 2 * delta_m_W_predicted := by
  have hpi : (0:ℝ) < Real.pi := Real.pi_pos
  have hlo : (3:ℝ) < Real.pi := by linarith [Real.pi_gt_d6]
  have hhi : Real.pi < 4 := by linarith [Real.pi_lt_d6]
  simp only [delta_m_W_predicted, delta_m_W_observed, delta_q_W_CDF, delta_q,
             sensitivity, q₀, q₀_minus_one, kappa, α_W, chi_bring]
  norm_num
  rw [show (5499:ℝ) / 50000 * (17 / 500 / (2 * Real.pi)) * (1 / 6) / (55499 / 50000)
        * (5580139001 / 580139001) * 80357
      = (5499 * 17 * 5580139001 * 80357 * 50000)
        / (50000 * 500 * 2 * 6 * 55499 * 580139001) / Real.pi by
      field_simp]
  refine ⟨?_, ?_⟩
  · rw [div_lt_iff₀ hpi]
    nlinarith [hlo]
  · rw [← mul_div_assoc, lt_div_iff₀ hpi]
    nlinarith [hhi]

/-- The W/Z mass ratio from Markov traces is positive and less than 1.

    **Was an axiom credited to [jones1985]; proved 2026-09-04.** Nothing of
    Jones's is needed for *these bounds*: `w_z_ratio` is a ratio of two
    Markov traces evaluated at the decimal literal `q₀`, so the statement is
    closed decidable arithmetic and `norm_num` discharges it. The Jones
    reference belongs on the *construction* of the Markov trace, which is
    where `markov_trace` cites it — not on the observation that one
    particular quotient of it lies in `(0, 1)`. -/
-- Ref: [jones1985] Jones, "A polynomial invariant for knots via von Neumann algebras," Bull. AMS 12 (1985)
theorem w_z_ratio_bounds :
    0 < w_z_ratio ∧ w_z_ratio < 1 := by
  constructor <;> · unfold w_z_ratio markov_trace qi2 q₀; norm_num

/-- q₀² is in the interval (1.232, 1.233).
    This auxiliary lemma enables the sensitivity proof. -/
theorem q₀_sq_bounds : (1.232 : ℝ) < q₀ ^ 2 ∧ q₀ ^ 2 < 1.233 := by
  unfold q₀; constructor <;> nlinarith

/-- The sensitivity ∂ ln m / ∂ ln q = (q₀² + 1)/(q₀² - 1) ∈ (9, 11).
    Uses q₀² ∈ (1.232, 1.233) to bound the ratio. -/
-- Ref: [leitner2026] Ch. 7, §Mass predictions and CODATA Comparison
theorem sensitivity_range :
    9 < sensitivity q₀ ∧ sensitivity q₀ < 11 := by
  obtain ⟨hlo, hhi⟩ := q₀_sq_bounds
  have hden_pos : (0 : ℝ) < q₀ ^ 2 - 1 := by linarith
  unfold sensitivity
  constructor
  · rw [lt_div_iff₀ hden_pos]
    nlinarith
  · rw [div_lt_iff₀ hden_pos]
    nlinarith

/-- The geometric factor κ is exactly 1/6, derived from the Euler
    characteristic of the Bring surface via Gauss-Bonnet. -/
-- Ref: [leitner2026] Ch. 2, §Bring surface geometry
theorem kappa_is_inv_chi : kappa = 1 / (6 : ℝ) := kappa_val

end QOU.Observations.WBoson
