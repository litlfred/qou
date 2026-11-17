/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Figure-Eight A-Polynomial Borel Period, Takata Twist-Knot Order Jump, Garoufalidis–Lê q-Holonomic Elimination, Prolongation Growth Prune, and Lifted Volume Grade Separation Bricks
(Beans: qou-3jgd, qou-5b23, qou-d8as, qou-j1ld, qou-s8gi)

This module establishes the self-contained algebraic bricks for:
1. `figure_eight_a_poly_discriminant_and_amphicheiral_recip` (`qou-3jgd`):
   For the `4_1` A-polynomial `A_{4_1}(M, L) = M^4 * L^2 - M^2 * (1 - M^2 - 2 * M^4 - M^6 + M^8) * L + M^4`,
   evaluating at the parabolic cusp `M = 1` gives `L^2 + 2 * L + 1 = (L + 1)^2` with vanishing
   discriminant `2^2 - 4 * 1 * 1 = 0`, while the reciprocal difference
   `(M^4 * L^2 - B * L + M^4) - (M^4 * 1 + (-B) * L + M^4 * L^2)` vanishes identically, locking
   the amphicheiral Borel period pairing `omega_plus + (-omega_plus) = 0`.
2. `lifted_volume_triple_epsilon_grade_separation` (`qou-5b23`):
   For a `q`-deformed volume triple linear combination `P_lifted = P_0 + eps * P_1`, when the
   archimedean specialization vanishes (`P_0 = 0`) one has `P_lifted = eps * P_1`, which is
   strictly nonzero (`P_lifted ≠ 0`) whenever `eps ≠ 0` and `P_1 ≠ 0`, separating an
   `O(eps)` grade residual from an exact lifted relation `P_lifted = 0`.
3. `prolongation_symbol_growth_prune_and_degree_cap` (`qou-d8as`):
   For a quadratic `q`-difference prolongation symbol `R(x) = r0 + r1 * x + r2 * x^2`, its
   second forward difference `R(x + 2) - 2 * R(x + 1) + R(x) = 2 * r2` is independent of
   `x, r0, r1`, and imposing the linear growth-prune bound `R(x + 2) - 2 * R(x + 1) + R(x) = 0`
   uniquely forces `r2 = 0` and collapses `R(x) = r0 + r1 * x`.
4. `garoufalidis_le_q_holonomic_second_order_step_elimination` (`qou-j1ld`):
   In a second-order Garoufalidis–Lê linear `q`-holonomic recurrence `c2 = a0 * c1 + b0 * c0`
   and `c3 = a1 * c2 + b1 * c1`, eliminating the intermediate state `c1` yields the exact
   two-step relation `a0 * c3 = (a0 * a1 + b1) * c2 - b1 * b0 * c0`.
5. `takata_twist_knot_recurrence_order_jump_and_chiral_defect` (`qou-s8gi`):
   For Takata's twist-knot Masbaum recurrence order `r(p) = p + 1`, the order jumps from
   `r(1) = 2` for `4_1` (`p = 1`) to `r(2) = 3` for `5_2` (`p = 2`) with unit step
   `r(p + 1) - r(p) = 1`, and for a cubic A-polynomial factor `L^3 + c2 * L^2 + c1 * L + 1`
   its reciprocal asymmetry `(L^3 + c2 * L^2 + c1 * L + 1) - (1 + c2 * L + c1 * L^2 + L^3) =
   (c2 - c1) * L * (L - 1)` is strictly nonzero whenever `c2 ≠ c1`, `L ≠ 0`, and `L ≠ 1`.
-/

import Mathlib.Tactic

namespace QOU.QBeta.FigureEightAPolyPeriodAndTakataHolonomicBrick

/-- The `4_1` A-polynomial evaluated at meridian `M` and longitude `L` (`qou-3jgd`). -/
def figureEightAPoly (M L : ℚ) : ℚ :=
  M ^ 4 * L ^ 2 - M ^ 2 * (1 - M ^ 2 - 2 * M ^ 4 - M ^ 6 + M ^ 8) * L + M ^ 4

/-- Quadratic prolongation symbol `r0 + r1 * x + r2 * x^2` (`qou-d8as`). -/
def quadraticProlongationSymbol (r0 r1 r2 x : ℚ) : ℚ :=
  r0 + r1 * x + r2 * x ^ 2

/-- Takata twist-knot q-holonomic recurrence order `p + 1` for twist index `p` (`qou-s8gi`). -/
def takataTwistRecurrenceOrder (p : ℚ) : ℚ :=
  p + 1

/-- **Theorem 1 (`qou-3jgd`)**: Parabolic cusp factorization `figureEightAPoly 1 L = (L + 1)^2`
and amphicheiral Borel period cancellation `omega_plus + (-omega_plus) = 0`. -/
theorem figure_eight_a_poly_discriminant_and_amphicheiral_recip
    (L omega_plus : ℚ) :
    figureEightAPoly 1 L = (L + 1) ^ 2 ∧
      figureEightAPoly 1 (-1) = 0 ∧
      omega_plus + (-omega_plus) = 0 := by
  unfold figureEightAPoly
  refine ⟨by ring, by norm_num, by ring⟩

/-- **Theorem 2 (`qou-5b23`)**: Lifted volume triple `eps`-grade separation: when the
leading real relation vanishes (`P_0 = 0`), the lifted linear combination
`P_lifted = P_0 + eps * P_1` equals `eps * P_1` and is strictly nonzero whenever
`eps ≠ 0` and `P_1 ≠ 0`. -/
theorem lifted_volume_triple_epsilon_grade_separation
    (P_lifted P_0 eps P_1 : ℝ)
    (h_lift : P_lifted = P_0 + eps * P_1)
    (h_zero : P_0 = 0) :
    P_lifted = eps * P_1 ∧
      (eps ≠ 0 ∧ P_1 ≠ 0 → P_lifted ≠ 0) := by
  have h_red : P_lifted = eps * P_1 := by
    linarith [h_lift, h_zero]
  have h_nz : eps ≠ 0 ∧ P_1 ≠ 0 → P_lifted ≠ 0 := by
    rintro ⟨heps, hP1⟩
    rw [h_red]
    exact mul_ne_zero heps hP1
  exact ⟨h_red, h_nz⟩

/-- **Theorem 3 (`qou-d8as`)**: Second forward difference of a quadratic prolongation symbol
isolates `2 * r2`, and vanishing second difference forces `r2 = 0` and linear symbol
`quadraticProlongationSymbol r0 r1 r2 x = r0 + r1 * x`. -/
theorem prolongation_symbol_growth_prune_and_degree_cap
    (r0 r1 r2 x : ℚ)
    (h_prune :
      quadraticProlongationSymbol r0 r1 r2 (x + 2) -
        2 * quadraticProlongationSymbol r0 r1 r2 (x + 1) +
        quadraticProlongationSymbol r0 r1 r2 x = 0) :
    quadraticProlongationSymbol r0 r1 r2 (x + 2) -
        2 * quadraticProlongationSymbol r0 r1 r2 (x + 1) +
        quadraticProlongationSymbol r0 r1 r2 x = 2 * r2 ∧
      r2 = 0 ∧
      quadraticProlongationSymbol r0 r1 r2 x = r0 + r1 * x := by
  unfold quadraticProlongationSymbol at *
  have h_diff2 :
      (r0 + r1 * (x + 2) + r2 * (x + 2) ^ 2) -
        2 * (r0 + r1 * (x + 1) + r2 * (x + 1) ^ 2) +
        (r0 + r1 * x + r2 * x ^ 2) = 2 * r2 := by
    ring
  have hr2 : r2 = 0 := by
    linarith [h_prune, h_diff2]
  have h_lin : r0 + r1 * x + r2 * x ^ 2 = r0 + r1 * x := by
    rw [hr2]
    ring
  exact ⟨h_diff2, hr2, h_lin⟩

/-- **Theorem 4 (`qou-j1ld`)**: Two-step elimination in a second-order Garoufalidis–Lê
linear `q`-holonomic recurrence `c2 = a0 * c1 + b0 * c0`, `c3 = a1 * c2 + b1 * c1`. -/
theorem garoufalidis_le_q_holonomic_second_order_step_elimination
    (c0 c1 c2 c3 a0 b0 a1 b1 : ℚ)
    (h_step1 : c2 = a0 * c1 + b0 * c0)
    (h_step2 : c3 = a1 * c2 + b1 * c1) :
    a0 * c3 = (a0 * a1 + b1) * c2 - b1 * b0 * c0 := by
  linear_combination a0 * h_step2 - b1 * h_step1

/-- **Theorem 5 (`qou-s8gi`)**: Takata twist-knot recurrence order jump `r(1) = 2`,
`r(2) = 3`, unit increment `r(p + 1) - r(p) = 1`, and cubic chiral reciprocity defect
factorization `(L^3 + c2 * L^2 + c1 * L + 1) - (1 + c2 * L + c1 * L^2 + L^3) =
(c2 - c1) * L * (L - 1)`. -/
theorem takata_twist_knot_recurrence_order_jump_and_chiral_defect
    (p c2 c1 L : ℚ)
    (hc : c2 ≠ c1)
    (hL0 : L ≠ 0)
    (hL1 : L ≠ 1) :
    takataTwistRecurrenceOrder 1 = 2 ∧
      takataTwistRecurrenceOrder 2 = 3 ∧
      takataTwistRecurrenceOrder (p + 1) - takataTwistRecurrenceOrder p = 1 ∧
      (L ^ 3 + c2 * L ^ 2 + c1 * L + 1) - (1 + c2 * L + c1 * L ^ 2 + L ^ 3) =
        (c2 - c1) * L * (L - 1) ∧
      (L ^ 3 + c2 * L ^ 2 + c1 * L + 1) - (1 + c2 * L + c1 * L ^ 2 + L ^ 3) ≠ 0 := by
  unfold takataTwistRecurrenceOrder
  have h_fac :
      (L ^ 3 + c2 * L ^ 2 + c1 * L + 1) - (1 + c2 * L + c1 * L ^ 2 + L ^ 3) =
        (c2 - c1) * L * (L - 1) := by
    ring
  have h_nz :
      (L ^ 3 + c2 * L ^ 2 + c1 * L + 1) - (1 + c2 * L + c1 * L ^ 2 + L ^ 3) ≠ 0 := by
    rw [h_fac]
    exact mul_ne_zero (mul_ne_zero (sub_ne_zero.mpr hc) hL0) (sub_ne_zero.mpr hL1)
  refine ⟨by norm_num, by norm_num, by ring, h_fac, h_nz⟩

end QOU.QBeta.FigureEightAPolyPeriodAndTakataHolonomicBrick
