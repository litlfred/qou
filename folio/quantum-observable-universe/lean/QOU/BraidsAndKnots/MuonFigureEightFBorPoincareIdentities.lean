/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
-/
import QOU.BraidsAndKnots.NucleonWeightSpaceTraces
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-!
# Muon `4₁` Wenzl Markov Trace, Chiral `F_Bor` Poincaré Weight, and Asymmetric Seifert Factorization

Unconditional algebraic identities over an arbitrary field `{K : Type*} [Field K]`
(`0 sorry`, zero archimedean imports per §7c) supporting beans `qou-1ozb`,
`qou-6gf9`, `qou-24w9`, and `qou-gbsa` (companion audit:
`docs/audits/2026-11-24-muon-41-fbor-poincare-worldline-adjudication.md`;
80-dps probe: `computations/probes/muon_fbor_poincare_and_worldline_loop_probe.py`).

## Main declarations

1. **Three-strand `(2,1)` weight-space characters and Wenzl `N = 2` Markov trace (`qou-1ozb`, `qou-6gf9`):**
   - `wenzl_weights_partition_of_unity`: `y_{(3)}(q) + 2 y_{(2,1)}(q) = 1` for
     `y_{(3)}(q) = (q⁴ + 1) / (q² + 1)²` and `y_{(2,1)}(q) = q² / (q² + 1)²`.
   - `chi21_half_twist_eq_zero`: on the half-twist `Δ₃ = A₁ A₂ A₁`,
     `χ_{(2,1)}(Δ₃) = tr(A₁ A₂ A₁) - q³ = 0`.
   - `chi21_figure_eight_closed_form`: on the figure-eight braid `4₁ = (A₁ A₂⁻¹)²`,
     `χ_{(2,1)}(4₁) = tr((A₁ A₂⁻¹)²) - 1 = (q⁸ - 2q⁶ + q⁴ - 2q² + 1) / q⁴`.
   - `markov_trace_figure_eight_polynomial_form` and
     `markov_trace_figure_eight_balanced_form`:
     `y_{(3)}(q) · 1 + y_{(2,1)}(q) · χ_{(2,1)}(4₁) = (q⁸ - q⁶ + q⁴ - q² + 1) / (q² (q² + 1)²) = (q⁵ + q⁻⁵) / (q + q⁻¹)³`.
   - `markov_trace_figure_eight_eq_ratio_mul_t25` and
     `markov_trace_figure_eight_div_t25`: exact ratio `2 q³ / ((q² + 1)(q⁴ + 1))`
     between `tr_M(4₁)` and the bar-symmetrized two-strand `T(2,5)` Markov trace.

2. **Chiral horizontal-Dirac Poincaré identity for `F_Bor`'s `/ q³` (`qou-24w9`):**
   - `chiral_hecke_quadratic_iff`: for `T = q⁻¹ σ` (`q ≠ 0`),
     `(T - 1)(T + q⁻²) = 0 ↔ (σ - q)(σ + q⁻¹) = 0`.
   - `fbor_qfactorial_over_q3_factored` and `fbor_qfactorial_over_q3_poincare_expanded`:
     `(q² + 1 + q⁻²)(q + q⁻¹) / q³ = (1 + q⁻²)(1 + q⁻² + q⁻⁴) = 1 + 2 q⁻² + 2 q⁻⁴ + q⁻⁶`.

3. **Asymmetric Seifert determinant / balanced Alexander factorization (`qou-gbsa`):**
   - `seifert_factor_t29_cleared`, `seifert_factor_t35_cleared`, and
     `seifert_product_cleared`: polynomial factorizations of the `T(2,9)` and
     `T(3,5)` cyclotomic factors.
   - `seifert_product_at_q_inv_eq_balanced_alexander`: over `[Field K]`, at `t = q⁻¹`,
     `(t² - t + 1)(t⁶ - t³ + 1)(t⁸ - t⁷ + t⁵ - t⁴ + t³ - t + 1) = q⁻⁸ Δ_{T(2,9)}(q) Δ_{T(3,5)}(q)`.

No numerical value enters.
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {K : Type*} [Field K]

/-! ## 1. Wenzl `N = 2` Markov Trace of `Δ₃` and `4₁` and the `T(2,5)` Ratio -/

/-- Wenzl `N = 2` three-strand symmetric-sector weight `y_{(3)}(q) = (q⁴ + 1) / (q² + 1)²`. -/
def wenzlWeight3 (q : K) : K := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- Wenzl `N = 2` three-strand standard-sector weight `y_{(2,1)}(q) = q² / (q² + 1)²`. -/
def wenzlWeight21 (q : K) : K := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- Three-strand half-twist braid `Δ₃ = σ₁ σ₂ σ₁` on the `(2,1)` weight space. -/
def halfTwistBraid3 (q : K) : Matrix (Fin 3) (Fin 3) K := A₁ q * A₂ q * A₁ q

/-- Three-strand figure-eight braid `4₁ = (σ₁ σ₂⁻¹)²` on the `(2,1)` weight space. -/
def figureEightBraid3 (q : K) : Matrix (Fin 3) (Fin 3) K :=
  (A₁ q * A₂Inv q) * (A₁ q * A₂Inv q)

/-- Irreducible `V_{(2,1)}` character on `Δ₃ = σ₁ σ₂ σ₁`, obtained by subtracting
the trivial one-dimensional `V_{(3)}` eigenvalue `q³` from the 3D `(2,1)` weight-space trace. -/
def chi21HalfTwist (q : K) : K := trace (halfTwistBraid3 q) - q ^ 3

/-- Irreducible `V_{(2,1)}` character on `4₁ = (σ₁ σ₂⁻¹)²` (writhe `0`, trivial eigenvalue `1`),
obtained by subtracting `1` from the 3D `(2,1)` weight-space trace. -/
def chi21FigureEight (q : K) : K := trace (figureEightBraid3 q) - 1

/-- Normalised Wenzl `N = 2` Markov trace of the figure-eight knot `4₁` on three strands:
`y_{(3)}(q) · 1 + y_{(2,1)}(q) · χ_{(2,1)}(4₁)`. -/
def markovTraceFigureEight (q : K) : K :=
  wenzlWeight3 q * 1 + wenzlWeight21 q * chi21FigureEight q

/-- Bar-symmetrized two-strand `N = 2` Markov trace of `T(2,5) = σ₁⁵`:
`((q² + q⁻²)(q⁵ + q⁻⁵)) / (2 (q + q⁻¹)²)`. -/
def barSymTraceT25TwoStrand (q : K) : K :=
  (q ^ 2 + q⁻¹ ^ 2) * (q ^ 5 + q⁻¹ ^ 5) / (2 * (q + q⁻¹) ^ 2)

/-- Non-vanishing of `[2]_q = q + q⁻¹` whenever `q ≠ 0` and `q² + 1 ≠ 0`. -/
theorem q_add_inv_ne_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    q + q⁻¹ ≠ 0 := by
  intro h
  apply hq2
  have hmul : q * (q + q⁻¹) = q ^ 2 + 1 := by
    field_simp
  rw [← hmul, h, mul_zero]

/-- Non-vanishing of `q² + q⁻²` whenever `q ≠ 0` and `q⁴ + 1 ≠ 0`. -/
theorem q_sq_add_inv_sq_ne_zero (q : K) (hq : q ≠ 0) (hq4 : q ^ 4 + 1 ≠ 0) :
    q ^ 2 + q⁻¹ ^ 2 ≠ 0 := by
  intro h
  apply hq4
  have hmul : q ^ 2 * (q ^ 2 + q⁻¹ ^ 2) = q ^ 4 + 1 := by
    field_simp
  rw [← hmul, h, mul_zero]

/-- Non-vanishing of `q⁵ + q⁻⁵` whenever `q ≠ 0` and `q¹⁰ + 1 ≠ 0`. -/
theorem q_pow5_add_inv_pow5_ne_zero (q : K) (hq : q ≠ 0) (hq10 : q ^ 10 + 1 ≠ 0) :
    q ^ 5 + q⁻¹ ^ 5 ≠ 0 := by
  intro h
  apply hq10
  have hmul : q ^ 5 * (q ^ 5 + q⁻¹ ^ 5) = q ^ 10 + 1 := by
    field_simp
  rw [← hmul, h, mul_zero]

/-- Partition of unity for the three-strand `N = 2` Wenzl weights:
`y_{(3)}(q) + 2 y_{(2,1)}(q) = 1`. -/
theorem wenzl_weights_partition_of_unity (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    wenzlWeight3 q + 2 * wenzlWeight21 q = 1 := by
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  unfold wenzlWeight3 wenzlWeight21
  field_simp
  ring

/-- On the three-strand half-twist `Δ₃ = A₁ A₂ A₁`, the two-dimensional standard Hecke
character vanishes identically: `χ_{(2,1)}(Δ₃) = tr(A₁ A₂ A₁) - q³ = 0`. -/
theorem chi21_half_twist_eq_zero (q : K) (hq : q ≠ 0) :
    chi21HalfTwist q = 0 := by
  simp [chi21HalfTwist, halfTwistBraid3, A₁, A₂, Matrix.trace_fin_three]
  field_simp
  ring

/-- Closed rational polynomial form of `χ_{(2,1)}(4₁) = tr((A₁ A₂⁻¹)²) - 1` on `4₁`. -/
theorem chi21_figure_eight_closed_form (q : K) (hq : q ≠ 0) :
    chi21FigureEight q =
      (q ^ 8 - 2 * q ^ 6 + q ^ 4 - 2 * q ^ 2 + 1) / q ^ 4 := by
  simp [chi21FigureEight, figureEightBraid3, A₁, A₂Inv, Matrix.trace_fin_three]
  field_simp
  ring

/-- Expanded rational form of the full Wenzl `N = 2` Markov trace on `4₁`:
`y_{(3)}(q) · 1 + y_{(2,1)}(q) · χ_{(2,1)}(4₁) = (q⁸ - q⁶ + q⁴ - q² + 1) / (q² (q² + 1)²)`. -/
theorem markov_trace_figure_eight_polynomial_form (q : K) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    markovTraceFigureEight q =
      (q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 1) / (q ^ 2 * (q ^ 2 + 1) ^ 2) := by
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  rw [markovTraceFigureEight, chi21_figure_eight_closed_form q hq]
  unfold wenzlWeight3 wenzlWeight21
  field_simp
  ring

/-- Compact bar-symmetric form of the full Wenzl `N = 2` Markov trace on `4₁`:
`tr_M(4₁) = (q⁵ + q⁻⁵) / (q + q⁻¹)³`. -/
theorem markov_trace_figure_eight_balanced_form (q : K) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    markovTraceFigureEight q = (q ^ 5 + q⁻¹ ^ 5) / (q + q⁻¹) ^ 3 := by
  have hsq : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  have hqi : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq2
  have hqi3 : (q + q⁻¹) ^ 3 ≠ 0 := pow_ne_zero 3 hqi
  rw [markov_trace_figure_eight_polynomial_form q hq hq2]
  field_simp
  ring

/-- Exact multiplicative relation between the three-strand Markov trace `tr_M(4₁)` and
the bar-symmetrized two-strand `T(2,5)` trace, with ratio `2 q³ / ((q² + 1)(q⁴ + 1))`. -/
theorem markov_trace_figure_eight_eq_ratio_mul_t25 (q : K) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    markovTraceFigureEight q =
      (2 * q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + 1))) * barSymTraceT25TwoStrand q := by
  have hqi : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq2
  have hqi2 : (q + q⁻¹) ^ 2 ≠ 0 := pow_ne_zero 2 hqi
  have hqi3 : (q + q⁻¹) ^ 3 ≠ 0 := pow_ne_zero 3 hqi
  rw [markov_trace_figure_eight_balanced_form q hq hq2]
  unfold barSymTraceT25TwoStrand
  field_simp

/-- Exact quotient form of the `tr_M(4₁) / tr_M^{\mathrm{bar}}(T(2,5))` identity. -/
theorem markov_trace_figure_eight_div_t25 (q : K) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + 1 ≠ 0) (hq10 : q ^ 10 + 1 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    markovTraceFigureEight q / barSymTraceT25TwoStrand q =
      2 * q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + 1)) := by
  have hqi : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq2
  have hq2i : q ^ 2 + q⁻¹ ^ 2 ≠ 0 := q_sq_add_inv_sq_ne_zero q hq hq4
  have hq5i : q ^ 5 + q⁻¹ ^ 5 ≠ 0 := q_pow5_add_inv_pow5_ne_zero q hq hq10
  have ht25 : barSymTraceT25TwoStrand q ≠ 0 := by
    unfold barSymTraceT25TwoStrand
    exact div_ne_zero (mul_ne_zero hq2i hq5i) (mul_ne_zero h2 (pow_ne_zero 2 hqi))
  rw [markov_trace_figure_eight_eq_ratio_mul_t25 q hq hq2 hq4 h2,
      mul_div_cancel_right₀ _ ht25]

/-! ## 2. Chiral Horizontal-Dirac Poincaré Identity for `F_Bor`'s `/ q³` (`qou-24w9`) -/

/-- Chiral Hecke generator `T = q⁻¹ σ` satisfies the chiral quadratic relation
`(T - 1)(T + q⁻²) = 0` if and only if `σ` satisfies the balanced skein relation
`(σ - q)(σ + q⁻¹) = 0`. -/
theorem chiral_hecke_quadratic_iff (q σ : K) (hq : q ≠ 0) :
    (q⁻¹ * σ - 1) * (q⁻¹ * σ + q⁻¹ ^ 2) = 0 ↔ (σ - q) * (σ + q⁻¹) = 0 := by
  have hscale :
      (σ - q) * (σ + q⁻¹) = q ^ 2 * ((q⁻¹ * σ - 1) * (q⁻¹ * σ + q⁻¹ ^ 2)) := by
    field_simp
  constructor
  · intro h
    rw [hscale, h, mul_zero]
  · intro h
    rw [hscale] at h
    exact (mul_eq_zero.mp h).resolve_left (pow_ne_zero 2 hq)

/-- Factored `S₃` Poincaré-polynomial form of `[3]_q! / q³` in the chiral parameter `q⁻²`:
`((q² + 1 + q⁻²)(q + q⁻¹)) / q³ = (1 + q⁻²)(1 + q⁻² + q⁻⁴)`. -/
theorem fbor_qfactorial_over_q3_factored (q : K) (hq : q ≠ 0) :
    (q ^ 2 + 1 + q⁻¹ ^ 2) * (q + q⁻¹) / q ^ 3 =
      (1 + q⁻¹ ^ 2) * (1 + q⁻¹ ^ 2 + q⁻¹ ^ 4) := by
  field_simp

/-- Length-graded `S₃` Bruhat Poincaré expansion `(1 + u)(1 + u + u²) = 1 + 2u + 2u² + u³`
at `u = q⁻²` (multiplicities `1, 2, 2, 1` for Coxeter lengths `0, 1, 2, 3`). -/
theorem poincare_s3_factored_eq_expanded (q : K) :
    (1 + q⁻¹ ^ 2) * (1 + q⁻¹ ^ 2 + q⁻¹ ^ 4) =
      1 + 2 * q⁻¹ ^ 2 + 2 * q⁻¹ ^ 4 + q⁻¹ ^ 6 := by
  ring

/-- Full identity `[3]_q! / q³ = P_{S₃}(q⁻²) = 1 + 2 q⁻² + 2 q⁻⁴ + q⁻⁶`. -/
theorem fbor_qfactorial_over_q3_poincare_expanded (q : K) (hq : q ≠ 0) :
    (q ^ 2 + 1 + q⁻¹ ^ 2) * (q + q⁻¹) / q ^ 3 =
      1 + 2 * q⁻¹ ^ 2 + 2 * q⁻¹ ^ 4 + q⁻¹ ^ 6 := by
  rw [fbor_qfactorial_over_q3_factored q hq, poincare_s3_factored_eq_expanded q]

/-! ## 3. Asymmetric Seifert Determinant / Balanced Alexander Factorization (`qou-gbsa`) -/

/-- Cyclotomic Seifert factor `Φ₆(t) Φ₁₈(t) = (t² - t + 1)(t⁶ - t³ + 1)` of `T(2,9)`. -/
def seifertFactorT29 (t : K) : K := (t ^ 2 - t + 1) * (t ^ 6 - t ^ 3 + 1)

/-- Cyclotomic Seifert factor `Φ₁₅(t) = t⁸ - t⁷ + t⁵ - t⁴ + t³ - t + 1` of `T(3,5)`. -/
def seifertFactorT35 (t : K) : K :=
  t ^ 8 - t ^ 7 + t ^ 5 - t ^ 4 + t ^ 3 - t + 1

/-- Balanced Alexander rational function `Δ_{T(2,9)}(q) = q⁻⁴ (q¹⁸ - 1)(q - 1) / ((q² - 1)(q⁹ - 1))`. -/
def balancedAlexanderT29 (q : K) : K :=
  q⁻¹ ^ 4 * (q ^ 18 - 1) * (q - 1) / ((q ^ 2 - 1) * (q ^ 9 - 1))

/-- Balanced Alexander rational function `Δ_{T(3,5)}(q) = q⁻⁴ (q¹⁵ - 1)(q - 1) / ((q³ - 1)(q⁵ - 1))`. -/
def balancedAlexanderT35 (q : K) : K :=
  q⁻¹ ^ 4 * (q ^ 15 - 1) * (q - 1) / ((q ^ 3 - 1) * (q ^ 5 - 1))

/-- Homological Bring–Seifert pairing factor `κ_{\mathrm{Seifert}}(q) = q⁸ / (Δ_{T(2,9)}(q) Δ_{T(3,5)}(q))`
(`b₁(Σ₄) = 8`). -/
def kappaSeifert (q : K) : K :=
  q ^ 8 / (balancedAlexanderT29 q * balancedAlexanderT35 q)

/-- Cleared polynomial factorization for `T(2,9)`:
`(1 - t²)(1 - t⁹)(t² - t + 1)(t⁶ - t³ + 1) = (1 - t¹⁸)(1 - t)`. -/
theorem seifert_factor_t29_cleared (t : K) :
    (1 - t ^ 2) * (1 - t ^ 9) * seifertFactorT29 t = (1 - t ^ 18) * (1 - t) := by
  unfold seifertFactorT29
  ring

/-- Cleared polynomial factorization for `T(3,5)`:
`(1 - t³)(1 - t⁵)(t⁸ - t⁷ + t⁵ - t⁴ + t³ - t + 1) = (1 - t¹⁵)(1 - t)`. -/
theorem seifert_factor_t35_cleared (t : K) :
    (1 - t ^ 3) * (1 - t ^ 5) * seifertFactorT35 t = (1 - t ^ 15) * (1 - t) := by
  unfold seifertFactorT35
  ring

/-- Combined cleared polynomial factorization for `T(2,9) × T(3,5)`. -/
theorem seifert_product_cleared (t : K) :
    (1 - t ^ 2) * (1 - t ^ 9) * (1 - t ^ 3) * (1 - t ^ 5) *
        (seifertFactorT29 t * seifertFactorT35 t) =
      (1 - t ^ 18) * (1 - t ^ 15) * (1 - t) ^ 2 := by
  have h29 := seifert_factor_t29_cleared t
  have h35 := seifert_factor_t35_cleared t
  calc
    (1 - t ^ 2) * (1 - t ^ 9) * (1 - t ^ 3) * (1 - t ^ 5) *
        (seifertFactorT29 t * seifertFactorT35 t)
      = ((1 - t ^ 2) * (1 - t ^ 9) * seifertFactorT29 t) *
          ((1 - t ^ 3) * (1 - t ^ 5) * seifertFactorT35 t) := by ring
    _ = ((1 - t ^ 18) * (1 - t)) * ((1 - t ^ 15) * (1 - t)) := by rw [h29, h35]
    _ = (1 - t ^ 18) * (1 - t ^ 15) * (1 - t) ^ 2 := by ring

/-- Individual `T(2,9)` asymmetric Seifert evaluation at `t = q⁻¹`:
`seifertFactorT29(q⁻¹) = q⁻⁴ Δ_{T(2,9)}(q)`. -/
theorem seifert_t29_at_q_inv_eq_q_inv4_alexander (q : K) (hq : q ≠ 0)
    (hq2 : q ^ 2 - 1 ≠ 0) (hq9 : q ^ 9 - 1 ≠ 0) :
    seifertFactorT29 q⁻¹ = q⁻¹ ^ 4 * balancedAlexanderT29 q := by
  unfold seifertFactorT29 balancedAlexanderT29
  field_simp
  ring

/-- Individual `T(3,5)` asymmetric Seifert evaluation at `t = q⁻¹`:
`seifertFactorT35(q⁻¹) = q⁻⁴ Δ_{T(3,5)}(q)`. -/
theorem seifert_t35_at_q_inv_eq_q_inv4_alexander (q : K) (hq : q ≠ 0)
    (hq3 : q ^ 3 - 1 ≠ 0) (hq5 : q ^ 5 - 1 ≠ 0) :
    seifertFactorT35 q⁻¹ = q⁻¹ ^ 4 * balancedAlexanderT35 q := by
  unfold seifertFactorT35 balancedAlexanderT35
  field_simp
  ring

/-- Full asymmetric Seifert determinant / balanced Alexander identity over `[Field K]`:
at `t = q⁻¹` (with `q ≠ 0`, `q - 1 ≠ 0`, `q² - 1 ≠ 0`, `q⁹ - 1 ≠ 0`, `q³ - 1 ≠ 0`, `q⁵ - 1 ≠ 0`),
`(t² - t + 1)(t⁶ - t³ + 1)(t⁸ - t⁷ + t⁵ - t⁴ + t³ - t + 1) = q⁻⁸ Δ_{T(2,9)}(q) Δ_{T(3,5)}(q)`. -/
theorem seifert_product_at_q_inv_eq_balanced_alexander (q : K)
    (hq : q ≠ 0) (_hq1 : q - 1 ≠ 0)
    (hq2 : q ^ 2 - 1 ≠ 0) (hq9 : q ^ 9 - 1 ≠ 0)
    (hq3 : q ^ 3 - 1 ≠ 0) (hq5 : q ^ 5 - 1 ≠ 0) :
    ((q⁻¹) ^ 2 - q⁻¹ + 1) * ((q⁻¹) ^ 6 - (q⁻¹) ^ 3 + 1) *
        ((q⁻¹) ^ 8 - (q⁻¹) ^ 7 + (q⁻¹) ^ 5 - (q⁻¹) ^ 4 + (q⁻¹) ^ 3 - q⁻¹ + 1) =
      q⁻¹ ^ 8 * (balancedAlexanderT29 q * balancedAlexanderT35 q) := by
  change seifertFactorT29 q⁻¹ * seifertFactorT35 q⁻¹ =
    q⁻¹ ^ 8 * (balancedAlexanderT29 q * balancedAlexanderT35 q)
  rw [seifert_t29_at_q_inv_eq_q_inv4_alexander q hq hq2 hq9,
      seifert_t35_at_q_inv_eq_q_inv4_alexander q hq hq3 hq5]
  ring

/-- Reciprocal identity connecting `κ_{\mathrm{Seifert}}(q) = q⁸ / (Δ_{T(2,9)}(q) Δ_{T(3,5)}(q))`
directly to the asymmetric Seifert polynomial product evaluated at `t = q⁻¹`. -/
theorem seifert_product_at_q_inv_mul_kappa_seifert_eq_one (q : K)
    (hq : q ≠ 0) (hq1 : q - 1 ≠ 0)
    (hq2 : q ^ 2 - 1 ≠ 0) (hq9 : q ^ 9 - 1 ≠ 0)
    (hq3 : q ^ 3 - 1 ≠ 0) (hq5 : q ^ 5 - 1 ≠ 0)
    (hq18 : q ^ 18 - 1 ≠ 0) (hq15 : q ^ 15 - 1 ≠ 0) :
    (((q⁻¹) ^ 2 - q⁻¹ + 1) * ((q⁻¹) ^ 6 - (q⁻¹) ^ 3 + 1) *
        ((q⁻¹) ^ 8 - (q⁻¹) ^ 7 + (q⁻¹) ^ 5 - (q⁻¹) ^ 4 + (q⁻¹) ^ 3 - q⁻¹ + 1)) *
      kappaSeifert q = 1 := by
  have hd29 : balancedAlexanderT29 q ≠ 0 := by
    unfold balancedAlexanderT29
    exact div_ne_zero
      (mul_ne_zero (mul_ne_zero (pow_ne_zero 4 (inv_ne_zero hq)) hq18) hq1)
      (mul_ne_zero hq2 hq9)
  have hd35 : balancedAlexanderT35 q ≠ 0 := by
    unfold balancedAlexanderT35
    exact div_ne_zero
      (mul_ne_zero (mul_ne_zero (pow_ne_zero 4 (inv_ne_zero hq)) hq15) hq1)
      (mul_ne_zero hq3 hq5)
  rw [seifert_product_at_q_inv_eq_balanced_alexander q hq hq1 hq2 hq9 hq3 hq5]
  unfold kappaSeifert
  have hprod : balancedAlexanderT29 q * balancedAlexanderT35 q ≠ 0 := mul_ne_zero hd29 hd35
  field_simp

end QOU.BraidsAndKnots
