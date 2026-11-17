/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Two-Row Frobenius Stratum Drift, Connected-Sum Trace Multiplicativity, Scale-Free α-Cluster Ratio, Whitehead One-Loop Prefactor Lock, and McPhail-Snyder Edge-Lattice Rank Bricks
(Beans: qou-2row, qou-301d, qou-3wvl, qou-k00d, qou-t7az)

This module establishes the self-contained algebraic bricks for:
1. `two_row_frobenius_stratum_drift_and_non_constant_obstruction` (`qou-2row`):
   When the effective two-row Frobenius prefactor `ρ_F(A)` drifts between `A = 4` (`⁴He`)
   and `A = 16` (`¹⁶O`) with `rho_4 ≠ rho_16`, no `A`-independent constant `c0` can
   simultaneously equal both (`¬ (c0 = rho_4 ∧ c0 = rho_16)`), the drift difference
   `rho_16 - rho_4` is strictly nonzero, and the `N = 12` two-row partition count
   `12 / 2 + 1 = 7` matches the seven active `[12 - k, k]` blocks (`k = 0..6`).
2. `connected_sum_amplitude_multiplicativity_free_energy_split` (`qou-301d`):
   Under connected-sum factorisation `A_total = T1 * T2 * I_conn` with additive
   log-amplitude `L_total = L1 + L2 + L_I`, the connected binding deficit satisfies
   `(L1 + L2) - L_total = -L_I`, and whenever `0 < T1`, `0 < T2`, `0 < I_conn`, the
   composite amplitude is strictly positive (`0 < T1 * T2 * I_conn`).
3. `scale_free_alpha_cluster_ratio_q0_scale_cancellation` (`qou-3wvl`):
   For the `α`-cluster binding expansion `B(n_α) = s0 * (n_α * b_alpha + delta_surf)`
   anchored at `B(1) = s0 * b_alpha` with overall dimensionful scale `s0 ≠ 0` and
   `b_alpha ≠ 0`, the scale-free normalized surface residual
   `(s0 * (n_alpha * b_alpha + delta_surf) - n_alpha * (s0 * b_alpha)) / (s0 * b_alpha)`
   equals `delta_surf / b_alpha`, cancelling `s0` identically.
4. `whitehead_one_loop_prefactor_torsion_inverse_square_root_lock` (`qou-k00d`):
   Under the Gukov–Murakami / Andersen–Kashaev one-loop law `c_sigma_sq * (2 * tau_DG) = 1`,
   at the canonical Whitehead torsion `tau_DG = 4` one has `c_sigma_sq = 1 / 8` and
   `c_sigma_sq ^ 2 = 1 / 64`.
5. `mcphail_snyder_diagrammatic_edge_lattice_rank_and_input_shift` (`qou-t7az`):
   For a 4-valent planar knot diagram with `c` crossings, the edge-lattice rank `E = 2 * c`
   and face count `F = c + 2` satisfy Euler's relation `c - 2 * c + (c + 2) = 2`, while
   shifting the input log-meridian datum `mu ↦ mu + delta_mu` shifts the linear phase
   `alpha * (mu + delta_mu) - alpha * mu = alpha * delta_mu ≠ 0` whenever `alpha ≠ 0`
   and `delta_mu ≠ 0`.
-/

import Mathlib.Tactic

namespace QOU.QBeta.TwoRowFrobeniusStratumAndConnectedSumTraceBrick

/-- Two-row partition count `N / 2 + 1` for even strand count `N` (`qou-2row`). -/
def twoRowPartitionCount (N : ℚ) : ℚ :=
  N / 2 + 1

/-- Scale-coupled `α`-cluster binding energy `s0 * (n_alpha * b_alpha + delta_surf)`
(`qou-3wvl`). -/
def alphaClusterBinding (s0 n_alpha b_alpha delta_surf : ℝ) : ℝ :=
  s0 * (n_alpha * b_alpha + delta_surf)

/-- Diagrammatic edge-lattice rank `2 * c` for a 4-valent knot diagram with `c` crossings
(`qou-t7az`). -/
def diagrammaticEdgeLatticeRank (c : ℚ) : ℚ :=
  2 * c

/-- **Theorem 1 (`qou-2row`)**: Non-constant obstruction across `⁴He` (`rho_4`) and
`¹⁶O` (`rho_16`) when `rho_4 ≠ rho_16`, non-vanishing drift `rho_16 - rho_4 ≠ 0`, and
`twoRowPartitionCount 12 = 7`. -/
theorem two_row_frobenius_stratum_drift_and_non_constant_obstruction
    (rho_4 rho_16 c0 : ℝ)
    (h_drift : rho_4 ≠ rho_16) :
    ¬ (c0 = rho_4 ∧ c0 = rho_16) ∧
      rho_16 - rho_4 ≠ 0 ∧
      twoRowPartitionCount 12 = 7 := by
  unfold twoRowPartitionCount
  have h_no_const : ¬ (c0 = rho_4 ∧ c0 = rho_16) := by
    rintro ⟨h4, h16⟩
    exact h_drift (h4.symm.trans h16)
  have h_sub : rho_16 - rho_4 ≠ 0 := sub_ne_zero.mpr (Ne.symm h_drift)
  exact ⟨h_no_const, h_sub, by norm_num⟩

/-- **Theorem 2 (`qou-301d`)**: Connected-sum free-energy subtraction
`(L1 + L2) - L_total = -L_I` when `L_total = L1 + L2 + L_I`, and strict positivity
`0 < T1 * T2 * I_conn` of the factorised amplitude when `0 < T1`, `0 < T2`, `0 < I_conn`. -/
theorem connected_sum_amplitude_multiplicativity_free_energy_split
    (L_total L1 L2 L_I T1 T2 I_conn : ℝ)
    (h_log : L_total = L1 + L2 + L_I)
    (hT1 : 0 < T1)
    (hT2 : 0 < T2)
    (hI : 0 < I_conn) :
    (L1 + L2) - L_total = -L_I ∧
      0 < T1 * T2 * I_conn := by
  have h_sub : (L1 + L2) - L_total = -L_I := by linarith [h_log]
  have h_pos : 0 < T1 * T2 * I_conn := mul_pos (mul_pos hT1 hT2) hI
  exact ⟨h_sub, h_pos⟩

/-- **Theorem 3 (`qou-3wvl`)**: Exact cancellation of the overall scale `s0 ≠ 0` in the
normalized `α`-cluster surface residual `(B(n_α) - n_α * B(1)) / B(1) = delta_surf / b_alpha`. -/
theorem scale_free_alpha_cluster_ratio_q0_scale_cancellation
    (s0 n_alpha b_alpha delta_surf : ℝ)
    (hs0 : s0 ≠ 0)
    (hb : b_alpha ≠ 0) :
    (alphaClusterBinding s0 n_alpha b_alpha delta_surf -
        n_alpha * alphaClusterBinding s0 1 b_alpha 0) /
      alphaClusterBinding s0 1 b_alpha 0 =
      delta_surf / b_alpha := by
  unfold alphaClusterBinding
  have h_num :
      s0 * (n_alpha * b_alpha + delta_surf) - n_alpha * (s0 * (1 * b_alpha + 0)) =
        s0 * delta_surf := by
    ring
  have h_den : s0 * (1 * b_alpha + 0) = s0 * b_alpha := by
    ring
  rw [h_num, h_den]
  exact mul_div_mul_left delta_surf b_alpha hs0

/-- **Theorem 4 (`qou-k00d`)**: Whitehead one-loop prefactor lock: when
`c_sigma_sq * (2 * tau_DG) = 1` and `tau_DG = 4`, one has `c_sigma_sq = 1 / 8` and
`c_sigma_sq ^ 2 = 1 / 64`. -/
theorem whitehead_one_loop_prefactor_torsion_inverse_square_root_lock
    (c_sigma_sq tau_DG : ℚ)
    (h_gm : c_sigma_sq * (2 * tau_DG) = 1)
    (h_tau : tau_DG = 4) :
    c_sigma_sq = 1 / 8 ∧
      c_sigma_sq ^ 2 = 1 / 64 := by
  have hc : c_sigma_sq = 1 / 8 := by linarith [h_gm, h_tau]
  have hc2 : c_sigma_sq ^ 2 = 1 / 64 := by
    rw [hc]
    norm_num
  exact ⟨hc, hc2⟩

/-- **Theorem 5 (`qou-t7az`)**: Planar 4-valent knot diagram Euler identity
`c - diagrammaticEdgeLatticeRank c + (c + 2) = 2` and non-vanishing phase shift
`alpha * (mu + delta_mu) - alpha * mu = alpha * delta_mu ≠ 0` under an input meridian
perturbation `delta_mu ≠ 0` (`alpha ≠ 0`). -/
theorem mcphail_snyder_diagrammatic_edge_lattice_rank_and_input_shift
    (c alpha mu delta_mu : ℚ)
    (ha : alpha ≠ 0)
    (hd : delta_mu ≠ 0) :
    c - diagrammaticEdgeLatticeRank c + (c + 2) = 2 ∧
      alpha * (mu + delta_mu) - alpha * mu = alpha * delta_mu ∧
      alpha * (mu + delta_mu) - alpha * mu ≠ 0 := by
  unfold diagrammaticEdgeLatticeRank
  have h_euler : c - 2 * c + (c + 2) = 2 := by ring
  have h_shift : alpha * (mu + delta_mu) - alpha * mu = alpha * delta_mu := by ring
  have h_nz : alpha * (mu + delta_mu) - alpha * mu ≠ 0 := by
    rw [h_shift]
    exact mul_ne_zero ha hd
  exact ⟨h_euler, h_shift, h_nz⟩

end QOU.QBeta.TwoRowFrobeniusStratumAndConnectedSumTraceBrick
