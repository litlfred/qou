import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Complex
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Data.Real.Sqrt

/-!
# The first Habiro coefficient of `8₁₈` is negative at the Kashaev point

`8₁₈` is the closure of `V₀⁴ = (σ₀σ₁⁻¹)⁴ ∈ B₃`. The volume conjecture is proved in
this repository for `V₀²` (`4₁`, `FigureEightVolumeSqueeze.lean`) and `V₀³`
(Borromean rings, `BorromeanVolume.lean`) by a squeeze that needs every term of the
Habiro cyclotomic expansion
`J_N(K; q) = Σ_{k<N} c_k(K; q) · Π_{j=1}^{k} {N+j}{N−j}`
to be non-negative at `q = e^{2πi/N}`, where the product equals `Π 4 sin²(πj/N) ≥ 0`.

**Computed input (not proved here).** The probe
`computations/probes/weaving_kashaev_root_of_unity/weaving_habiro_coefficients.py`
computes the coefficients of `8₁₈` exactly, as integer Laurent polynomials, from the
coloured Jones state model of [arxiv-2209.06973v1] §5. Every division in the
triangular solve is an exact integer division, which checks Habiro's integrality
theorem along the way. It finds
`c₁(8₁₈; q) = q² − 3q + 3 − 3q⁻¹ + q⁻²`.
This file takes that Laurent polynomial as its definition `c1EightEighteen` and does
**not** prove that it is the Habiro coefficient. The identification is computed data,
cited from the probe.

**Proved here, sorry-free.** At `q = e^{iθ}` the polynomial equals
`x² − 3x + 1` with `x = 2 cos θ`, and it is negative at every Kashaev point
`θ = 2π/N`, `N ≥ 5`. So the `k = 1` term of the Habiro sum of `8₁₈` is negative
there, and the positive-sum squeeze used for `4₁` and the Borromean rings does not
apply to `8₁₈` through its Habiro expansion. The roots of `x² − 3x + 1` are
`(3 ± √5)/2`, the squares of the golden ratio and of its inverse.

Audit: `docs/audits/2026-11-27-knot-volume-conjecture.md` §4 (Q4).

-- Ref: [habiro2008] Habiro, "A unified Witten–Reshetikhin–Turaev invariant for integral homology spheres", Invent. Math. 171 (2008), Thm 4.2 (cyclotomic expansion of the coloured Jones polynomial)
-- Ref: [arxiv-2209.06973v1] §5, R-matrix state model of the coloured Jones polynomial
-/

namespace QOU.Knot.EightEighteen

open Real

/-- The Laurent polynomial `q² − 3q + 3 − 3q⁻¹ + q⁻²`, computed (not proved here) to be
the first Habiro coefficient `c₁(8₁₈; q)`. -/
noncomputable def c1EightEighteen (q : ℂ) : ℂ :=
  q ^ 2 - 3 * q + 3 - 3 * q⁻¹ + (q⁻¹) ^ 2

/-- On the unit circle, `c₁(8₁₈; e^{iθ}) = (2 cos θ)² − 3·(2 cos θ) + 1`, a real number. -/
theorem c1EightEighteen_exp (θ : ℝ) :
    c1EightEighteen (Complex.exp (θ * Complex.I)) =
      (((2 * Real.cos θ) ^ 2 - 3 * (2 * Real.cos θ) + 1 : ℝ) : ℂ) := by
  have hinv : (Complex.exp (θ * Complex.I))⁻¹ = Complex.exp (-(θ * Complex.I)) :=
    (Complex.exp_neg _).symm
  have hcos : 2 * Complex.cos (θ : ℂ) =
      Complex.exp (θ * Complex.I) + Complex.exp (-(θ * Complex.I)) := by
    rw [Complex.cos, neg_mul]
    ring
  have hprod : Complex.exp (θ * Complex.I) * Complex.exp (-(θ * Complex.I)) = 1 := by
    rw [← Complex.exp_add, add_neg_cancel, Complex.exp_zero]
  unfold c1EightEighteen
  rw [hinv]
  push_cast
  rw [hcos]
  set a := Complex.exp (θ * Complex.I)
  set b := Complex.exp (-(θ * Complex.I))
  have : (a + b) ^ 2 - 3 * (a + b) + 1 = a ^ 2 - 3 * a + 3 - 3 * b + b ^ 2 + 2 * (a * b - 1) := by
    ring
  rw [this, hprod]
  ring

/-- `x² − 3x + 1 < 0` on the open interval between its roots `(3 ∓ √5)/2`. -/
theorem golden_quadratic_neg {x : ℝ} (h1 : (3 - Real.sqrt 5) / 2 < x)
    (h2 : x < (3 + Real.sqrt 5) / 2) : x ^ 2 - 3 * x + 1 < 0 := by
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  have : x ^ 2 - 3 * x + 1 = (x - (3 - Real.sqrt 5) / 2) * (x - (3 + Real.sqrt 5) / 2) := by
    ring_nf; rw [h5]; ring
  rw [this]
  exact mul_neg_of_pos_of_neg (by linarith) (by linarith)

/-- `cos (2π/5) = (√5 − 1)/4`. -/
theorem cos_two_pi_div_five : Real.cos (2 * π / 5) = (Real.sqrt 5 - 1) / 4 := by
  have h := Real.cos_pi_div_five
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  rw [show 2 * π / 5 = 2 * (π / 5) by ring, Real.cos_two_mul, h]
  ring_nf
  rw [h5]
  ring

/-- **The `k = 1` Habiro coefficient of `8₁₈` is negative at every Kashaev point
`q = e^{2πi/N}` with `N ≥ 5`.** (With the computed identification of
`c1EightEighteen` as `c₁(8₁₈)`; see the module docstring.) -/
theorem c1EightEighteen_neg_at_kashaev (N : ℕ) (hN : 5 ≤ N) :
    ∃ r : ℝ, r < 0 ∧
      c1EightEighteen (Complex.exp ((2 * π / N : ℝ) * Complex.I)) = (r : ℂ) := by
  refine ⟨(2 * Real.cos (2 * π / N)) ^ 2 - 3 * (2 * Real.cos (2 * π / N)) + 1, ?_,
    c1EightEighteen_exp _⟩
  have hNpos : (0 : ℝ) < N := by exact_mod_cast lt_of_lt_of_le (by norm_num) hN
  have hN5 : (5 : ℝ) ≤ N := by exact_mod_cast hN
  have hθ0 : 0 ≤ 2 * π / N := by positivity
  have hθ5 : 2 * π / N ≤ 2 * π / 5 := by
    apply div_le_div_of_nonneg_left (by positivity) (by norm_num) hN5
  have hθπ : 2 * π / 5 ≤ π := by linarith [Real.pi_pos]
  have hcos : Real.cos (2 * π / 5) ≤ Real.cos (2 * π / N) :=
    Real.cos_le_cos_of_nonneg_of_le_pi hθ0 hθπ hθ5
  rw [cos_two_pi_div_five] at hcos
  have hs5 : 2 < Real.sqrt 5 := by
    rw [show (2 : ℝ) = Real.sqrt 4 by
      rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  have hs3 : Real.sqrt 5 < 3 := by
    rw [show (3 : ℝ) = Real.sqrt 9 by
      rw [show (9 : ℝ) = 3 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]]
    exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  have hc1 : Real.cos (2 * π / N) ≤ 1 := Real.cos_le_one _
  apply golden_quadratic_neg
  · linarith
  · linarith

end QOU.Knot.EightEighteen
