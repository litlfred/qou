/-
Copyright (c) 2026 litlfred. All rights reserved.

# Hecke photon-projector insertions on the muon carrier 4₁ do not force a w² dressing

Bean `qou-6gf9` (compute-accuracy C3, epic `qou-myts`).
Probe: `computations/probes/mu_p_projector_insertion_w_order_probe.py`
(witness `mu-p-projector-insertion-w-order.witness.json`).

## The question

PR #9362 left `−(3α/4π)·w²`, `w = q + q⁻¹ − 2`, as an UNWIRED working
assumption for the correction to the muon carrier `Vol(4₁)/ℏ_q²`. It would be
derived only if a natural observable of `4₁ = (σ₁σ₂⁻¹)²` had vanishing
`O(w⁰)` and `O(w¹)` terms and a *forced* `w²` coefficient. This file tests the
photon-projector insertion class, `e_i = (q − σ_i)/[2]_q`, in the 3-dimensional
representation used by the corpus's muon probes, with SU(2) Markov weights.

Everything here is a statement over a generic field `K`. No measured quantity
enters any statement.

## What is proved (sorry-free)

1. `trace_E1_word41`, `trace_E2_word41`: the single-insertion traces in closed
   form.
2. `pairCorr_eq`: the bar-symmetric single insertion, normalised by
   `tr_M(4₁)`, is `(s⁴ − 6s² + 7)/(s⁴ − 5s² + 5)` with `s = q + q⁻¹ = [2]_q`.
   Its denominator is `(q¹⁰ + 1)/(q⁵ s)`, so the nearest pole sits at
   `s = 2cos(π/10)`, which bounds the radius of every `w`-expansion.
3. `pairCorr_at_one`: at `q = 1` the correlator is `−1`, so the `O(w⁰)` term
   does not vanish.
4. `pair_taylor`, `doubles_taylor`, `connected_taylor`: exact third-order
   remainder identities giving the `O(1), O(w), O(w²)` coefficients
   `(−1, 20, −203)`, `(−11, 217, −8811/4)`, `(−21, 617, −41051/4)`. The `w`-forms
   of the double and connected correlators are taken from the probe (exact
   sympy); only the single insertion is derived here from the matrices.
5. `w2_coeff_not_forced`: for every `c : ℚ` there is a combination of
   `1, S₁ = 4·pair, D` whose `O(1)` and `O(w)` coefficients vanish and whose
   `O(w²)` coefficient is `c`. Cancelling `O(1)` and `O(w)` is therefore a
   two-parameter choice, and the class does not fix the `w²` coefficient.

Scope (a) for the route: this is about the projector-insertion class only. It
does not exclude a dressing from a different construction.
-/
import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Trace

namespace QOU.BraidsAndKnots.MuPProjectorInsertionWOrder

open Matrix

variable {K : Type*} [Field K]

/-- `σ₁` in the 3-dimensional representation (eigenvalues `q`, `q`, `−q⁻¹`). -/
def A1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, 0, 1; 0, 1, q - q⁻¹]

/-- `σ₂` in the 3-dimensional representation. -/
def A2 (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, 0; 1, q - q⁻¹, 0; 0, 0, q]

/-- `σ₂⁻¹`. -/
def A2inv (q : K) : Matrix (Fin 3) (Fin 3) K := !![q⁻¹ - q, 1, 0; 1, 0, 0; 0, 0, q⁻¹]

theorem A2_mul_A2inv (q : K) (hq : q ≠ 0) : A2 q * A2inv q = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [A2, A2inv, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp

/-- The photon projector `e₁ = (q − σ₁)/[2]_q`. -/
def E1 (q : K) : Matrix (Fin 3) (Fin 3) K := (q + q⁻¹)⁻¹ • (q • (1 : Matrix (Fin 3) (Fin 3) K) - A1 q)

/-- The photon projector `e₂ = (q − σ₂)/[2]_q`. -/
def E2 (q : K) : Matrix (Fin 3) (Fin 3) K := (q + q⁻¹)⁻¹ • (q • (1 : Matrix (Fin 3) (Fin 3) K) - A2 q)

/-- The muon carrier word `4₁ = (σ₁σ₂⁻¹)²`. -/
def word41 (q : K) : Matrix (Fin 3) (Fin 3) K := A1 q * A2inv q * A1 q * A2inv q

theorem trace_E1_word41 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    trace (E1 q * word41 q) = -(q ^ 6 + q ^ 2 - 1) / (q ^ 4 * (q ^ 2 + 1)) := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply h2; field_simp at h; linear_combination h
  simp [trace, E1, A1, A2inv, word41, Matrix.mul_apply, Fin.sum_univ_three,
    Matrix.smul_apply, Matrix.sub_apply, Matrix.one_apply]
  field_simp
  ring

theorem trace_E2_word41 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    trace (E2 q * word41 q) = (q ^ 6 - q ^ 4 - 1) / (q ^ 2 + 1) := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply h2; field_simp at h; linear_combination h
  simp [trace, E2, A1, A2, A2inv, word41, Matrix.mul_apply, Fin.sum_univ_three,
    Matrix.smul_apply, Matrix.sub_apply, Matrix.one_apply]
  field_simp
  ring

theorem trace_word41 (q : K) (hq : q ≠ 0) :
    trace (word41 q) = (q ^ 2 - 1) ^ 2 * (q ^ 4 + 1) / q ^ 4 := by
  simp [trace, A1, A2inv, word41, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

/-- SU(2) Markov weights (the `(1,1,1)` weight is zero). -/
def y3 (q : K) : K := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2
def y21 (q : K) : K := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- `tr_M(4₁) = y₃·χ_(3) + y₂₁·χ_(21)`; `4₁` has exponent sum 0, so `χ_(3) = 1`
and `χ_(21) = tr − 1` in the 3-dimensional representation. -/
def trM41 (q : K) : K := y3 q + y21 q * (trace (word41 q) - 1)

theorem trM41_eq (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    trM41 q = (q ^ 10 + 1) / (q ^ 2 * (q ^ 2 + 1) ^ 3) := by
  rw [trM41, trace_word41 q hq, y3, y21]
  field_simp
  ring

/-- The bar-symmetric single insertion `⟨e₁⟩ + ⟨e₂⟩`, normalised by `tr_M(4₁)`.
The projectors kill the trivial representation, so only `y₂₁` contributes. -/
def pairCorr (q : K) : K := y21 q * (trace (E1 q * word41 q) + trace (E2 q * word41 q)) / trM41 q

/-- The pair correlator as a rational function of `q`. -/
theorem pairCorr_eq_q (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h8 : q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 1 ≠ 0) :
    pairCorr q = (q ^ 8 - 2 * q ^ 6 + q ^ 4 - 2 * q ^ 2 + 1) / (q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 1) := by
  have hq2 : q ^ 2 * (q ^ 2 + 1) ^ 2 ≠ 0 := mul_ne_zero (pow_ne_zero 2 hq) (pow_ne_zero 2 h2)
  have hZ : trM41 q = (q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 1) / (q ^ 2 * (q ^ 2 + 1) ^ 2) := by
    rw [trM41_eq q hq h2, div_eq_div_iff (mul_ne_zero (pow_ne_zero 2 hq) (pow_ne_zero 3 h2)) hq2]
    ring
  have hZne : trM41 q ≠ 0 := by rw [hZ]; exact div_ne_zero h8 hq2
  unfold pairCorr
  rw [div_eq_div_iff hZne h8, hZ, trace_E1_word41 q hq h2, trace_E2_word41 q hq h2, y21]
  field_simp
  ring

/-- The pair correlator in `s = q + q⁻¹ = [2]_q`. -/
theorem pairCorr_eq (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (hZ : (q + q⁻¹) ^ 4 - 5 * (q + q⁻¹) ^ 2 + 5 ≠ 0) :
    pairCorr q = ((q + q⁻¹) ^ 4 - 6 * (q + q⁻¹) ^ 2 + 7) /
      ((q + q⁻¹) ^ 4 - 5 * (q + q⁻¹) ^ 2 + 5) := by
  have hfac : (q + q⁻¹) ^ 4 - 5 * (q + q⁻¹) ^ 2 + 5 =
      (q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 1) / q ^ 4 := by
    field_simp; ring
  have h8 : q ^ 8 - q ^ 6 + q ^ 4 - q ^ 2 + 1 ≠ 0 := by
    intro h; apply hZ; rw [hfac, h, zero_div]
  have hnum : (q + q⁻¹) ^ 4 - 6 * (q + q⁻¹) ^ 2 + 7 =
      (q ^ 8 - 2 * q ^ 6 + q ^ 4 - 2 * q ^ 2 + 1) / q ^ 4 := by
    field_simp; ring
  rw [pairCorr_eq_q q hq h2 h8, hfac, hnum, div_div_div_cancel_right₀ (pow_ne_zero 4 hq)]

/-- At `q = 1` the bar-symmetric single insertion is `−1`: the `O(w⁰)` term
is nonzero. -/
theorem pairCorr_at_one : pairCorr (1 : ℚ) = -1 := by
  rw [pairCorr_eq (1 : ℚ) one_ne_zero (by norm_num) (by norm_num)]
  norm_num

/-! ## The same correlators in `w = s − 2`, and their Taylor data -/

/-- Common denominator `s⁴ − 5s² + 5` written in `w = s − 2`. -/
def P (w : K) : K := w ^ 4 + 8 * w ^ 3 + 19 * w ^ 2 + 12 * w + 1

theorem P_eq (s : K) : P (s - 2) = s ^ 4 - 5 * s ^ 2 + 5 := by unfold P; ring

theorem pair_num_eq (s : K) :
    (s - 2) ^ 4 + 8 * (s - 2) ^ 3 + 18 * (s - 2) ^ 2 + 8 * (s - 2) - 1 = s ^ 4 - 6 * s ^ 2 + 7 := by
  ring

/-- Pair correlator: `N − P·(−1 + 20w − 203w²) = w³·g`. -/
theorem pair_taylor (w : K) :
    (w ^ 4 + 8 * w ^ 3 + 18 * w ^ 2 + 8 * w - 1) - P w * (-1 + 20 * w - 203 * w ^ 2) =
      w ^ 3 * (203 * w ^ 3 + 1604 * w ^ 2 + 3699 * w + 2072) := by
  unfold P; ring

/-- All doubles, `D = 2(5w⁶+…−22)/((w+2)²P)` (w-form from the probe):
coefficients `(−11, 217, −8811/4)`. -/
theorem doubles_taylor (w : ℚ) :
    2 * (5 * w ^ 6 + 60 * w ^ 5 + 272 * w ^ 4 + 576 * w ^ 3 + 549 * w ^ 2 + 148 * w - 22) -
      (w + 2) ^ 2 * P w * (-11 + 217 * w - 8811 / 4 * w ^ 2) =
      w ^ 3 * (8811 / 4 * w ^ 5 + 26216 * w ^ 4 + 474273 / 4 * w ^ 3 + 252647 * w ^ 2 +
        1001811 / 4 * w + 89890) := by
  unfold P; ring

/-- Connected doubles (w-form from the probe): coefficients `(−21, 617, −41051/4)`. -/
theorem connected_taylor (w : ℚ) :
    2 * (w + 1) * (w + 3) * (7 * w ^ 6 + 84 * w ^ 5 + 363 * w ^ 4 + 664 * w ^ 3 + 452 * w ^ 2 +
        80 * w - 14) - (w + 2) ^ 2 * P w ^ 2 * (-21 + 617 * w - 41051 / 4 * w ^ 2) =
      w ^ 3 * (41051 / 4 * w ^ 9 + 204638 * w ^ 8 + 3464697 / 2 * w ^ 7 + 8105730 * w ^ 6 +
        91430961 / 4 * w ^ 5 + 39705400 * w ^ 4 + 83211889 / 2 * w ^ 3 + 24535550 * w ^ 2 +
        27745491 / 4 * w + 580450) := by
  unfold P; ring

/-- **Non-forcing.** Taylor vectors `(O(1), O(w), O(w²))`: constant `(1,0,0)`,
`S₁ = (−4, 80, −812)`, `D = (−11, 217, −8811/4)`. For every target `c`, the
combination `x₀·1 + x₁·S₁ + x₂·D` with `x₂ = −5c`, `x₁ = 217c/16`, `x₀ = −3c/4`
has vanishing `O(1)` and `O(w)` and `O(w²) = c`. -/
theorem w2_coeff_not_forced (c : ℚ) :
    ∃ x0 x1 x2 : ℚ,
      x0 * 1 + x1 * (-4) + x2 * (-11) = 0 ∧
      x1 * 80 + x2 * 217 = 0 ∧
      x1 * (-812) + x2 * (-8811 / 4) = c := by
  refine ⟨-3 * c / 4, 217 * c / 16, -5 * c, ?_, ?_, ?_⟩ <;> ring

/-- No single member of the class has vanishing leading term: the constant
coefficients of pair, `S₁`, `D`, `C` are `−1, −4, −11, −21`. -/
theorem leading_terms_nonzero :
    (-1 : ℚ) ≠ 0 ∧ (-4 : ℚ) ≠ 0 ∧ (-11 : ℚ) ≠ 0 ∧ (-21 : ℚ) ≠ 0 := by norm_num

end QOU.BraidsAndKnots.MuPProjectorInsertionWOrder
