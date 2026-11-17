/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Angle-Structure Feasibility, Clausen Unit-Circle Duplication, and Co-Equational Bridge Bricks
(Beans: qou-0y6l, qou-amvt, qou-fv70, qou-j6mp, qou-mokg)

This module establishes the self-contained algebraic bricks for:
1. `fkr_denominator_clearing_spurious_locus_split` (`qou-0y6l`):
   When denominator-clearing elimination factors `P_cleared = A_denom * Q_true`,
   any root `P_cleared = 0` splits into `A_denom = 0 ∨ Q_true = 0`, and imposing
   the torus saturation equation `A_denom * u_sat = 1` forces `A_denom ≠ 0` and
   uniquely isolates the genuine character-variety root `Q_true = 0`.
2. `angle_structure_interior_simplex_feasibility_and_volume_witness` (`qou-amvt`):
   Around the equilateral ideal tetrahedron centre `(π / 3, π / 3, π / 3)`, any
   perturbation `(π / 3 + d1, π / 3 + d2, π / 3 - d1 - d2)` with `|d1| < π / 6`
   and `|d2| < π / 6` (`π > 0`) satisfies the exact angle-sum constraint
   `α1 + α2 + α3 = π` and strict interior positivity `0 < α1`, `0 < α2`, `0 < α3`.
3. `bloch_wigner_unit_circle_clausen_odd_reflection_and_triplication` (`qou-fv70`):
   For the unit-circle Clausen / Bloch-Wigner function satisfying `D_zero = -D_zero`,
   `D_pi = -D_pi`, and the duplication relation at `π / 3`
   (`D_two_pi_3 = 2 * D_pi_3 - 2 * D_two_pi_3`), one has `D_zero = 0`, `D_pi = 0`,
   `D_two_pi_3 = (2 / 3) * D_pi_3`, and `D_pi_3 + D_two_pi_3 = (5 / 3) * D_pi_3`.
4. `coequational_bridge_vs_entire_egf_stokes_defect_dichotomy` (`qou-j6mp`):
   In the two-channel alien bridge equation
   `delta_omega_f = S_eq * df_dz + A_omega * D_coeq_f`, an entire EGF at `q = 1`
   has vanishing equational Stokes multiplier `S_eq = 0`, reducing the bridge
   purely to the co-equational coefficient-plane channel `delta_omega_f = A_omega * D_coeq_f`,
   which is strictly nonzero whenever `A_omega ≠ 0` and `D_coeq_f ≠ 0`.
5. `bring_hyperbolic_five_fold_tetrahedron_sum_decomposition` (`qou-mokg`):
   When a `C_5`-symmetric 5-tetrahedron hyperbolic volume sum
   `V_Bring = (D_tet + d0) + (D_tet + d1) + (D_tet + d2) + (D_tet + d3) + (D_tet + d4)`
   has zero-sum cyclic perturbations `d0 + d1 + d2 + d3 + d4 = 0`, the total volume
   is `V_Bring = 5 * D_tet` and the per-sector mean is `V_Bring / 5 = D_tet`.
-/

import Mathlib.Tactic

namespace QOU.QBeta.AnglePolytopeFeasibilityAndClausenUnitCircleBrick

/-- Interior angle triple `(pi_val / 3 + d1, pi_val / 3 + d2, pi_val / 3 - d1 - d2)`
for an ideal tetrahedron (`qou-amvt`). -/
noncomputable def perturbedEquilateralAngles (pi_val d1 d2 : ℝ) : ℝ × ℝ × ℝ :=
  (pi_val / 3 + d1, pi_val / 3 + d2, pi_val / 3 - d1 - d2)

/-- **Theorem 1 (`qou-0y6l`)**: Torus saturation `A_denom * u_sat = 1` eliminates
the spurious denominator locus `A_denom = 0` from the cleared FKR polynomial
`P_cleared = A_denom * Q_true`, isolating `Q_true = 0`. -/
theorem fkr_denominator_clearing_spurious_locus_split
    (P_cleared A_denom Q_true u_sat : ℝ)
    (h_fact : P_cleared = A_denom * Q_true)
    (h_zero : P_cleared = 0)
    (h_sat : A_denom * u_sat = 1) :
    (A_denom = 0 ∨ Q_true = 0) ∧ A_denom ≠ 0 ∧ Q_true = 0 := by
  have h_prod_zero : A_denom * Q_true = 0 := h_fact.symm.trans h_zero
  have h_or : A_denom = 0 ∨ Q_true = 0 := mul_eq_zero.mp h_prod_zero
  have hA_ne : A_denom ≠ 0 := by
    intro hA0
    rw [hA0, zero_mul] at h_sat
    exact zero_ne_one h_sat
  have hQ_zero : Q_true = 0 := h_or.resolve_left hA_ne
  exact ⟨h_or, hA_ne, hQ_zero⟩

/-- **Theorem 2 (`qou-amvt`)**: Any perturbation `(d1, d2)` with `|d1| < pi_val / 6`
and `|d2| < pi_val / 6` around the equilateral ideal tetrahedron centre preserves
the angle sum `pi_val` and keeps all three dihedral angles strictly positive. -/
theorem angle_structure_interior_simplex_feasibility_and_volume_witness
    (pi_val d1 d2 : ℝ)
    (hpi : 0 < pi_val)
    (hd1 : |d1| < pi_val / 6)
    (hd2 : |d2| < pi_val / 6) :
    (pi_val / 3 + d1) + (pi_val / 3 + d2) + (pi_val / 3 - d1 - d2) = pi_val ∧
      0 < pi_val / 3 + d1 ∧
      0 < pi_val / 3 + d2 ∧
      0 < pi_val / 3 - d1 - d2 := by
  have h_sum :
      (pi_val / 3 + d1) + (pi_val / 3 + d2) + (pi_val / 3 - d1 - d2) = pi_val := by
    ring
  have hd1_bounds := abs_lt.mp hd1
  have hd2_bounds := abs_lt.mp hd2
  have h1 : 0 < pi_val / 3 + d1 := by linarith [hpi, hd1_bounds.1]
  have h2 : 0 < pi_val / 3 + d2 := by linarith [hpi, hd2_bounds.1]
  have h3 : 0 < pi_val / 3 - d1 - d2 := by linarith [hpi, hd1_bounds.2, hd2_bounds.2]
  exact ⟨h_sum, h1, h2, h3⟩

/-- **Theorem 3 (`qou-fv70`)**: Unit-circle Clausen / Bloch-Wigner oddness at `0`
and `π`, plus the Kubert duplication relation at `π / 3` locking
`D(2π / 3) = (2 / 3) * D(π / 3)` and `D(π / 3) + D(2π / 3) = (5 / 3) * D(π / 3)`. -/
theorem bloch_wigner_unit_circle_clausen_odd_reflection_and_triplication
    (D_zero D_pi D_pi_3 D_two_pi_3 : ℝ)
    (h_zero_odd : D_zero = -D_zero)
    (h_pi_odd : D_pi = -D_pi)
    (h_kubert_dup : D_two_pi_3 = 2 * D_pi_3 - 2 * D_two_pi_3) :
    D_zero = 0 ∧
      D_pi = 0 ∧
      D_two_pi_3 = (2 / 3) * D_pi_3 ∧
      D_pi_3 + D_two_pi_3 = (5 / 3) * D_pi_3 := by
  have hz : D_zero = 0 := by linarith [h_zero_odd]
  have hpi : D_pi = 0 := by linarith [h_pi_odd]
  have h23 : D_two_pi_3 = (2 / 3) * D_pi_3 := by linarith [h_kubert_dup]
  have h53 : D_pi_3 + D_two_pi_3 = (5 / 3) * D_pi_3 := by linarith [h23]
  exact ⟨hz, hpi, h23, h53⟩

/-- **Theorem 4 (`qou-j6mp`)**: Two-channel bridge equation dichotomy: when the
equational Stokes multiplier vanishes (`S_eq = 0`) on the entire binding EGF side,
the alien derivative `delta_omega_f` reduces purely to the co-equational
coefficient-plane term `A_omega * D_coeq_f`. -/
theorem coequational_bridge_vs_entire_egf_stokes_defect_dichotomy
    (delta_omega_f S_eq df_dz A_omega D_coeq_f : ℝ)
    (h_bridge : delta_omega_f = S_eq * df_dz + A_omega * D_coeq_f)
    (h_entire_egf : S_eq = 0) :
    delta_omega_f = A_omega * D_coeq_f ∧
      (A_omega ≠ 0 ∧ D_coeq_f ≠ 0 → delta_omega_f ≠ 0) := by
  have h_coeq : delta_omega_f = A_omega * D_coeq_f := by
    rw [h_bridge, h_entire_egf, zero_mul, zero_add]
  have h_nz : A_omega ≠ 0 ∧ D_coeq_f ≠ 0 → delta_omega_f ≠ 0 := by
    rintro ⟨hA, hD⟩
    rw [h_coeq]
    exact mul_ne_zero hA hD
  exact ⟨h_coeq, h_nz⟩

/-- **Theorem 5 (`qou-mokg`)**: `C_5`-orbit five-tetrahedron Bring volume
decomposition: when cyclic perturbations sum to zero (`d0 + d1 + d2 + d3 + d4 = 0`),
the five-fold sum equals `5 * D_tet` and its orbit average is `D_tet`. -/
theorem bring_hyperbolic_five_fold_tetrahedron_sum_decomposition
    (V_Bring D_tet d0 d1 d2 d3 d4 : ℝ)
    (h_sum5 : V_Bring = (D_tet + d0) + (D_tet + d1) + (D_tet + d2) + (D_tet + d3) + (D_tet + d4))
    (h_cyc_zero : d0 + d1 + d2 + d3 + d4 = 0) :
    V_Bring = 5 * D_tet ∧ V_Bring / 5 = D_tet := by
  have h_five : V_Bring = 5 * D_tet := by
    linarith [h_sum5, h_cyc_zero]
  have h_avg : V_Bring / 5 = D_tet := by
    linarith [h_five]
  exact ⟨h_five, h_avg⟩

end QOU.QBeta.AnglePolytopeFeasibilityAndClausenUnitCircleBrick
