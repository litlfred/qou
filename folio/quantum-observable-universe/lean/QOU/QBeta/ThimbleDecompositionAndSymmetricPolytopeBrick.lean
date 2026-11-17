/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Thimble State-Integral Balance, Symmetric Angle Polytope, and Prolongation Bricks
(Beans: qou-h7yk, qou-krvm, qou-kyst, qou-lbth, qou-o41q)

This module establishes the self-contained algebraic bricks for:
1. `fantini_wheeler_thimble_state_integral_decomposition_balance` (`qou-h7yk`):
   When a state integral `I_state` decomposes into two conjugate Lefschetz-thimble
   Laplace contributions `n_plus * L_plus + n_minus * L_minus + R_tail` with
   terminating tail algorithm (`R_tail = 0`), equal intersection multiplicities
   `n_plus = c`, `n_minus = c`, and conjugate Stokes shifts `L_plus = I_0 + delta`,
   `L_minus = I_0 - delta`, the Stokes ambiguity `delta` cancels identically and
   `I_state = 2 * c * I_0`.
2. `symmetric_angle_polytope_barycenter_fixed_and_strict_concave_gap` (`qou-krvm`):
   On the symmetric angle-structure hyperplane `x + y = S` under the involution
   `(x, y) ↦ (y, x)`, the unique fixed point is `x_star = S / 2`, `y_star = S / 2`,
   and the quadratic concave objective `F(x, y) = F_max - kappa * ((x - S / 2) ^ 2 + (y - S / 2) ^ 2)`
   satisfies `F_max - F(x, y) = (kappa / 2) * (x - y) ^ 2 ≥ 0` (`kappa > 0`),
   attaining `F(x, y) ≤ F_max` with equality at `x = y = S / 2`.
3. `qdifference_prolongation_symbol_commutator_obstruction_identity` (`qou-kyst`):
   The q-difference prolongation symbol `E_M - q * M_E` decomposes into the
   classical commutator `E_M - M_E` minus the q-deformation defect `(q - 1) * M_E`;
   at `q = 1` it equals `E_M - M_E`, while on any commutative shadow `E_M = M_E`
   with `M_E ≠ 0` and `q ≠ 1`, the symbol is strictly nonzero (`E_M - q * M_E ≠ 0`).
4. `elliptic_divisor_degree_zero_and_weierstrass_factor_cancellation` (`qou-lbth`):
   When two doubly-periodic meromorphic candidates share the same zero and pole
   multiplicities (`ord_z1 = ord_z2`, `ord_p1 = ord_p2`) and weighted divisor
   centres (`Z1 = Z2`, `P1 = P2`) on the fundamental parallelogram, the divisor
   order of their ratio `(ord_z1 - ord_p1) - (ord_z2 - ord_p2) = 0` and Abel
   lattice defect `(Z1 - P1) - (Z2 - P2) = 0` vanish identically.
5. `bloch_suslin_antisymmetric_duplication_and_inversion_annihilation` (`qou-o41q`):
   For a five-term functional satisfying `D_x_sq = 2 * D_x - 2 * D_neg_x`,
   odd parity `D_neg_x = -D_x` yields the duplication scaling `D_x_sq = 4 * D_x`,
   whereas even parity `D_neg_x = D_x` collapses `D_x_sq = 0` (the real-orientation
   degeneracy identified in `qou-o41q`).
-/

import Mathlib.Tactic

namespace QOU.QBeta.ThimbleDecompositionAndSymmetricPolytopeBrick

/-- Quadratic concave angle-structure objective around the symmetric barycenter
`(S / 2, S / 2)` (`qou-krvm`). -/
noncomputable def symmetricPolytopeConcaveObjective
    (F_max kappa S x y : ℝ) : ℝ :=
  F_max - kappa * ((x - S / 2) ^ 2 + (y - S / 2) ^ 2)

/-- **Theorem 1 (`qou-h7yk`)**: Conjugate Lefschetz-thimble state-integral
decomposition with terminating tail algorithm (`R_tail = 0`) cancels the Stokes
ambiguity `delta` identically and yields `I_state = 2 * c * I_0`. -/
theorem fantini_wheeler_thimble_state_integral_decomposition_balance
    (I_state n_plus n_minus L_plus L_minus R_tail c I_0 delta : ℝ)
    (h_decomp : I_state = n_plus * L_plus + n_minus * L_minus + R_tail)
    (h_tail : R_tail = 0)
    (hn_p : n_plus = c)
    (hn_m : n_minus = c)
    (hL_p : L_plus = I_0 + delta)
    (hL_m : L_minus = I_0 - delta) :
    I_state = 2 * c * I_0 ∧ I_state - 2 * c * I_0 = 0 := by
  have h_bal : I_state = 2 * c * I_0 := by
    rw [h_decomp, h_tail, hn_p, hn_m, hL_p, hL_m]
    ring
  exact ⟨h_bal, sub_eq_zero.mpr h_bal⟩

/-- **Theorem 2 (`qou-krvm`)**: On the symmetric angle-structure slice `x + y = S`,
the quadratic concave objective `symmetricPolytopeConcaveObjective F_max kappa S x y`
is swap-invariant, satisfies `F_max - F(x, y) = (kappa / 2) * (x - y) ^ 2`, and is
bounded above by `F_max` for `kappa > 0`. -/
theorem symmetric_angle_polytope_barycenter_fixed_and_strict_concave_gap
    (F_max kappa S x y : ℝ)
    (hkappa : 0 < kappa)
    (h_sum : x + y = S) :
    symmetricPolytopeConcaveObjective F_max kappa S y x =
        symmetricPolytopeConcaveObjective F_max kappa S x y ∧
      F_max - symmetricPolytopeConcaveObjective F_max kappa S x y =
        (kappa / 2) * (x - y) ^ 2 ∧
      symmetricPolytopeConcaveObjective F_max kappa S x y ≤ F_max := by
  unfold symmetricPolytopeConcaveObjective
  have h_swap :
      F_max - kappa * ((y - S / 2) ^ 2 + (x - S / 2) ^ 2) =
        F_max - kappa * ((x - S / 2) ^ 2 + (y - S / 2) ^ 2) := by
    ring
  have h_gap :
      F_max - (F_max - kappa * ((x - S / 2) ^ 2 + (y - S / 2) ^ 2)) =
        (kappa / 2) * (x - y) ^ 2 := by
    have hS : S = x + y := h_sum.symm
    rw [hS]
    ring
  have h_nonneg : 0 ≤ (kappa / 2) * (x - y) ^ 2 := by
    exact mul_nonneg (by positivity) (sq_nonneg _)
  have h_le :
      F_max - kappa * ((x - S / 2) ^ 2 + (y - S / 2) ^ 2) ≤ F_max := by
    linarith [h_gap, h_nonneg]
  exact ⟨h_swap, h_gap, h_le⟩

/-- **Theorem 3 (`qou-kyst`)**: Decomposition of the q-difference prolongation
symbol `E_M - q * M_E = (E_M - M_E) - (q - 1) * M_E`, classical limit at `q = 1`,
and nonvanishing obstruction on a commutative shadow `E_M = M_E ≠ 0` when `q ≠ 1`. -/
theorem qdifference_prolongation_symbol_commutator_obstruction_identity
    (E_M M_E q : ℝ) :
    E_M - q * M_E = (E_M - M_E) - (q - 1) * M_E ∧
      (q = 1 → E_M - q * M_E = E_M - M_E) ∧
      (E_M = M_E ∧ M_E ≠ 0 ∧ q ≠ 1 → E_M - q * M_E ≠ 0) := by
  have h_id : E_M - q * M_E = (E_M - M_E) - (q - 1) * M_E := by ring
  have h_q1 : q = 1 → E_M - q * M_E = E_M - M_E := by
    intro h1
    rw [h1]
    ring
  have h_ne : E_M = M_E ∧ M_E ≠ 0 ∧ q ≠ 1 → E_M - q * M_E ≠ 0 := by
    rintro ⟨h_comm, hME, hq⟩
    have h_rewrite : E_M - q * M_E = -(q - 1) * M_E := by
      rw [h_comm]
      ring
    rw [h_rewrite]
    have hq1_ne : -(q - 1) ≠ 0 := neg_ne_zero.mpr (sub_ne_zero.mpr hq)
    exact mul_ne_zero hq1_ne hME
  exact ⟨h_id, h_q1, h_ne⟩

/-- **Theorem 4 (`qou-lbth`)**: Divisor-degree and Abel-sum cancellation for the
ratio of two doubly-periodic meromorphic candidates sharing identical zero/pole
multiplicities and weighted divisor centres on the fundamental parallelogram. -/
theorem elliptic_divisor_degree_zero_and_weierstrass_factor_cancellation
    (ord_z1 ord_p1 ord_z2 ord_p2 Z1 P1 Z2 P2 : ℝ)
    (h_liouville1 : ord_z1 - ord_p1 = 0)
    (h_same_z : ord_z2 = ord_z1)
    (h_same_p : ord_p2 = ord_p1)
    (h_same_Z : Z2 = Z1)
    (h_same_P : P2 = P1) :
    ord_z2 - ord_p2 = 0 ∧
      (ord_z1 - ord_p1) - (ord_z2 - ord_p2) = 0 ∧
      (Z1 - P1) - (Z2 - P2) = 0 := by
  have h_l2 : ord_z2 - ord_p2 = 0 := by
    linarith [h_liouville1, h_same_z, h_same_p]
  have h_ord_diff : (ord_z1 - ord_p1) - (ord_z2 - ord_p2) = 0 := by
    linarith [h_liouville1, h_l2]
  have h_abel_diff : (Z1 - P1) - (Z2 - P2) = 0 := by
    linarith [h_same_Z, h_same_P]
  exact ⟨h_l2, h_ord_diff, h_abel_diff⟩

/-- **Theorem 5 (`qou-o41q`)**: Dichotomy for the Bloch-Suslin duplication
relation `D_x_sq = 2 * D_x - 2 * D_neg_x`: odd inversion parity `D_neg_x = -D_x`
gives `D_x_sq = 4 * D_x`, whereas even parity `D_neg_x = D_x` forces `D_x_sq = 0`. -/
theorem bloch_suslin_antisymmetric_duplication_and_inversion_annihilation
    (D_x D_neg_x D_x_sq : ℝ)
    (h_dup : D_x_sq = 2 * D_x - 2 * D_neg_x) :
    (D_neg_x = -D_x → D_x_sq = 4 * D_x) ∧
      (D_neg_x = D_x → D_x_sq = 0) := by
  refine ⟨?_, ?_⟩
  · intro h_odd
    linarith [h_dup, h_odd]
  · intro h_even
    linarith [h_dup, h_even]

end QOU.QBeta.ThimbleDecompositionAndSymmetricPolytopeBrick
