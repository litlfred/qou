/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Reeb Eigenphase Scale-Gauge Invariance, Andersen–Kashaev Potential Bridge Ratio, JSJ Per-Piece Volume Additivity, Faddeev Upper-Half-Plane Convergence, and Guéritaud Two-Bridge Layered Tetrahedra Bricks
(Beans: qou-0g4z, qou-mo1n, qou-qsns, qou-sib1, qou-yvyd)

This module establishes the self-contained algebraic bricks for:
1. `reeb_eigenphase_scale_gauge_invariance_and_difference_lock` (`qou-0g4z`):
   For the normalized character ratio `χ_λ / d_λ` feeding the per-vertex seminormal
   eigenphase `θ_λ = arccos(χ_λ / d_λ)`, scaling both `(χ_λ, d_λ) ↦ (s * χ_λ, s * d_λ)`
   by any non-zero radial scale `s ≠ 0` leaves `(s * χ_λ) / (s * d_λ) = χ_λ / d_λ`
   strictly invariant, and any additive radial gauge shift `γ` cancels in the mirror
   difference `(γ + e1) - (γ + e2) = e1 - e2`.
2. `andersen_kashaev_potential_vs_complex_volume_bridge_ratio` (`qou-mo1n`):
   In the Andersen–Kashaev / GGM state-integral normalization bridge where the full
   Neumann–Zagier potential satisfies `kappa_shape = 2 * kappa_pot`, matching the
   quadratic meridian expansion `kappa_shape * c_shape_sq = kappa_pot * c_pot_sq` with
   `kappa_pot ≠ 0` forces `c_pot_sq = 2 * c_shape_sq`, and `2 * V_cs - V_cs = V_cs ≠ 0`
   whenever `V_cs ≠ 0`.
3. `jsj_torus_decomposition_per_piece_volume_additivity` (`qou-qsns`):
   Under a JSJ torus decomposition of a link complement into three hyperbolic pieces
   with volumes `(V1, V2, V3)` and a flat Seifert piece `V_seifert = 0`, the total
   volume satisfies `V_total = V1 + V2 + V3 + V_seifert = V1 + V2 + V3`, and when
   `0 < V1`, `0 < V2`, `0 < V3`, the total volume strictly exceeds any single piece
   (`V1 < V_total`) and satisfies `0 < V_total`.
4. `faddeev_modular_b_squared_upper_half_plane_convergence_witness` (`qou-sib1`):
   For the Faddeev quantum dilogarithm modular parameter `τ = b^2` with `b = u_r + i * u_i`,
   the imaginary part of `-τ = -b^2` is `-2 * u_r * u_i`; whenever `0 < u_r` and `u_i < 0`,
   one has `0 < -2 * u_r * u_i`, placing `-τ` strictly in the upper half-plane where the
   Andersen–Kashaev / Faddeev state integral converges, while `|b^2|^2 = (u_r^2 - u_i^2)^2 +
   (2 * u_r * u_i)^2 = (u_r^2 + u_i^2)^2`.
5. `gueritaud_two_bridge_layered_tetrahedron_count_and_farey_sum` (`qou-yvyd`):
   In Guéritaud's pillowcase layered triangulation of a two-bridge knot `S(p, q)` with
   crossing number `c`, the tetrahedron count `N_tet(c) = 2 * (c - 3)` yields `N_tet(4) = 2`
   for `4_1 = S(5, 2)` and `N_tet(5) = 4` for `5_2 = S(7, 3)`, with step increment
   `N_tet(c + 1) - N_tet(c) = 2` and rational continued-fraction identities
   `5 / 2 = 2 + 1 / 2` and `7 / 3 = 2 + 1 / 3`.
-/

import Mathlib.Tactic

namespace QOU.QBeta.StateIntegralBridgeAndTwoBridgeLayeredNZBrick

/-- Guéritaud pillowcase layered tetrahedron count `2 * (c - 3)` for a two-bridge knot
of crossing number `c` (`qou-yvyd`). -/
def gueritaudLayeredTetCount (c : ℚ) : ℚ :=
  2 * (c - 3)

/-- Imaginary part `-2 * u_r * u_i` of the negative modular parameter `-τ = -b^2`
for `b = u_r + i * u_i` (`qou-sib1`). -/
def negTauImagPart (u_r u_i : ℝ) : ℝ :=
  -2 * u_r * u_i

/-- **Theorem 1 (`qou-0g4z`)**: Radial scale invariance `(s * chi) / (s * d) = chi / d`
for `s ≠ 0` and additive gauge cancellation `(gamma + e1) - (gamma + e2) = e1 - e2` in
the Reeb eigenphase channel. -/
theorem reeb_eigenphase_scale_gauge_invariance_and_difference_lock
    (s chi d gamma e1 e2 : ℝ)
    (hs : s ≠ 0) :
    (s * chi) / (s * d) = chi / d ∧
      (gamma + e1) - (gamma + e2) = e1 - e2 := by
  refine ⟨mul_div_mul_left chi d hs, by ring⟩

/-- **Theorem 2 (`qou-mo1n`)**: Andersen–Kashaev potential vs complex-volume bridge-scale
ratio: when `kappa_shape = 2 * kappa_pot` and `kappa_shape * c_shape_sq = kappa_pot * c_pot_sq`
with `kappa_pot ≠ 0`, one has `c_pot_sq = 2 * c_shape_sq`, and `2 * V_cs - V_cs = V_cs ≠ 0`
whenever `V_cs ≠ 0`. -/
theorem andersen_kashaev_potential_vs_complex_volume_bridge_ratio
    (kappa_shape kappa_pot c_shape_sq c_pot_sq V_cs : ℝ)
    (h_norm : kappa_shape = 2 * kappa_pot)
    (h_match : kappa_shape * c_shape_sq = kappa_pot * c_pot_sq)
    (hk : kappa_pot ≠ 0)
    (hV : V_cs ≠ 0) :
    c_pot_sq = 2 * c_shape_sq ∧
      2 * V_cs - V_cs = V_cs ∧
      2 * V_cs - V_cs ≠ 0 := by
  have h_prod : kappa_pot * c_pot_sq = kappa_pot * (2 * c_shape_sq) := by
    linear_combination -h_match + c_shape_sq * h_norm
  have h_ratio : c_pot_sq = 2 * c_shape_sq := mul_left_cancel₀ hk h_prod
  have h_diff : 2 * V_cs - V_cs = V_cs := by ring
  have h_nz : 2 * V_cs - V_cs ≠ 0 := by
    rw [h_diff]
    exact hV
  exact ⟨h_ratio, h_diff, h_nz⟩

/-- **Theorem 3 (`qou-qsns`)**: JSJ torus decomposition per-piece volume additivity
with flat Seifert piece `V_seifert = 0`, strict piece dominance `V1 < V_total`, and
positivity `0 < V_total`. -/
theorem jsj_torus_decomposition_per_piece_volume_additivity
    (V_total V1 V2 V3 V_seifert : ℝ)
    (h_sum : V_total = V1 + V2 + V3 + V_seifert)
    (h_seifert : V_seifert = 0)
    (h1 : 0 < V1)
    (h2 : 0 < V2)
    (h3 : 0 < V3) :
    V_total = V1 + V2 + V3 ∧
      V1 < V_total ∧
      0 < V_total := by
  have h_add : V_total = V1 + V2 + V3 := by linarith [h_sum, h_seifert]
  have h_dom : V1 < V_total := by linarith [h_add, h2, h3]
  have h_pos : 0 < V_total := by linarith [h1, h_dom]
  exact ⟨h_add, h_dom, h_pos⟩

/-- **Theorem 4 (`qou-sib1`)**: Upper-half-plane convergence condition `0 < negTauImagPart u_r u_i`
when `0 < u_r` and `u_i < 0`, together with the norm-square identity
`(u_r^2 - u_i^2)^2 + (2 * u_r * u_i)^2 = (u_r^2 + u_i^2)^2`. -/
theorem faddeev_modular_b_squared_upper_half_plane_convergence_witness
    (u_r u_i : ℝ)
    (hr : 0 < u_r)
    (hi : u_i < 0) :
    0 < negTauImagPart u_r u_i ∧
      (u_r ^ 2 - u_i ^ 2) ^ 2 + (2 * u_r * u_i) ^ 2 = (u_r ^ 2 + u_i ^ 2) ^ 2 := by
  unfold negTauImagPart
  have h_neg_ui : 0 < -u_i := neg_pos.mpr hi
  have h_pos : 0 < -2 * u_r * u_i := by
    have h1 : 0 < (2 : ℝ) * u_r := mul_pos two_pos hr
    have h2 : 0 < (2 * u_r) * (-u_i) := mul_pos h1 h_neg_ui
    linarith
  have h_norm : (u_r ^ 2 - u_i ^ 2) ^ 2 + (2 * u_r * u_i) ^ 2 = (u_r ^ 2 + u_i ^ 2) ^ 2 := by
    ring
  exact ⟨h_pos, h_norm⟩

/-- **Theorem 5 (`qou-yvyd`)**: Guéritaud pillowcase layered tetrahedron counts
`N_tet(4) = 2` for `4_1 = S(5, 2)` and `N_tet(5) = 4` for `5_2 = S(7, 3)`, step increment
`N_tet(c + 1) - N_tet(c) = 2`, and rational continued-fraction identities
`5 / 2 = 2 + 1 / 2` and `7 / 3 = 2 + 1 / 3`. -/
theorem gueritaud_two_bridge_layered_tetrahedron_count_and_farey_sum
    (c : ℚ) :
    gueritaudLayeredTetCount 4 = 2 ∧
      gueritaudLayeredTetCount 5 = 4 ∧
      gueritaudLayeredTetCount (c + 1) - gueritaudLayeredTetCount c = 2 ∧
      (5 : ℚ) / 2 = 2 + 1 / 2 ∧
      (7 : ℚ) / 3 = 2 + 1 / 3 := by
  unfold gueritaudLayeredTetCount
  refine ⟨by norm_num, by norm_num, by ring, by norm_num, by norm_num⟩

end QOU.QBeta.StateIntegralBridgeAndTwoBridgeLayeredNZBrick
