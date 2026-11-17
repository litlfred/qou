/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Habiro Cyclotomic Inhomogeneous Recurrence, Hopf Link CS Pairing, Habiro Tail Geometric Majorant, Distinguished Twist-Knot Trace Lock, and A-Polynomial Branch Phase Bricks
(Beans: qou-2w6j, qou-c9fh, qou-dku0, qou-n5vg, qou-pwgw)

This module establishes the self-contained algebraic bricks for:
1. `habiro_cyclotomic_one_step_inhomogeneous_recurrence` (`qou-2w6j`):
   For the 1-term Habiro cyclotomic evaluation `J^{(1)}(u_N, c1) = 1 + c1 * (2 - u_N)` where
   `u_N = q^N + q^{-N}` satisfies the Chebyshev recurrence `u_{N+1} + u_{N-1} = t * u_N`
   (`t = q + q^{-1}`), the order-2 operator `J^{(1)}(u_{N+1}, c1) - t * J^{(1)}(u_N, c1) +
   J^{(1)}(u_{N-1}, c1)` collapses to the `N`-independent inhomogeneous certificate
   `(2 - t) * (1 + 2 * c1)`.
2. `hopf_link_chern_simons_pairing_nonzero_criterion` (`qou-c9fh`):
   For the two-component Hopf link complement bilinear Chern–Simons torsion pairing
   `CS_Hopf(u1, u2) = 2 * u1 * u2`, one has the polarization identity
   `CS_Hopf(u1, u2) = ((u1 + u2)^2 - (u1 - u2)^2) / 2`, symmetry
   `CS_Hopf(u1, u2) = CS_Hopf(u2, u1)`, and strict non-vanishing `CS_Hopf(u1, u2) ≠ 0`
   whenever `u1 ≠ 0` and `u2 ≠ 0`.
3. `figure_eight_habiro_tail_geometric_majorant_identity` (`qou-dku0`):
   For a geometric Habiro tail majorant with ratio `r` and leading term `t0`, the 3-term
   telescoping identity `(1 - r) * (t0 + r * t0 + r^2 * t0) + r^3 * t0 = t0` holds
   identically, and whenever `0 < r` and `0 < t0` the cubic remainder term satisfies
   `0 < r^3 * t0`.
4. `twist_knot_distinguished_trace_field_quadratic_lock` (`qou-n5vg`):
   At the distinguished `4_1` trace specialization `u = 3` (corresponding to `M + M^{-1} = √5`),
   the quadratic `L^2 - 4 * L + 1` has discriminant `(-4)^2 - 4 * 1 * 1 = 12`, and any root
   pair `(2 + s, 2 - s)` with `s^2 = 3` satisfies `(2 + s) + (2 - s) = 4` and reciprocal unit
   product `(2 + s) * (2 - s) = 1`.
5. `figure_eight_branch_discriminant_and_norm_one_phase_lock` (`qou-pwgw`):
   For conjugate A-polynomial branches `(L1, L2)` with `L1 + L2 = b` and `L1 * L2 = 1`, the
   squared branch separation satisfies `(L1 - L2)^2 = b^2 - 4`, the sum of squares is
   `L1^2 + L2^2 = b^2 - 2`, and in the elliptic scale-match window `b^2 < 4` the discriminant
   is strictly negative (`b^2 - 4 < 0`).
-/

import Mathlib.Tactic

namespace QOU.QBeta.HabiroCyclotomicRecurrenceAndHopfCSBrick

/-- One-term truncated Habiro cyclotomic sum `1 + c1 * (2 - uN)` (`qou-2w6j`). -/
def habiroOneTermTrunc (uN c1 : ℚ) : ℚ :=
  1 + c1 * (2 - uN)

/-- Hopf link bilinear Chern–Simons torsion pairing `2 * u1 * u2` (`qou-c9fh`). -/
def hopfChernSimonsPairing (u1 u2 : ℝ) : ℝ :=
  2 * u1 * u2

/-- Three-term geometric partial sum `t0 + r * t0 + r^2 * t0` for Habiro tail bounding
(`qou-dku0`). -/
def habiroGeometricPartialSum3 (t0 r : ℝ) : ℝ :=
  t0 + r * t0 + r ^ 2 * t0

/-- **Theorem 1 (`qou-2w6j`)**: Order-2 inhomogeneous recurrence certificate for the
1-term Habiro cyclotomic sum under the Chebyshev step `u_next + u_prev = t * u_curr`. -/
theorem habiro_cyclotomic_one_step_inhomogeneous_recurrence
    (u_prev u_curr u_next t c1 : ℚ)
    (h_cheb : u_next + u_prev = t * u_curr) :
    habiroOneTermTrunc u_next c1 - t * habiroOneTermTrunc u_curr c1 +
        habiroOneTermTrunc u_prev c1 =
      (2 - t) * (1 + 2 * c1) := by
  unfold habiroOneTermTrunc
  linear_combination -c1 * h_cheb

/-- **Theorem 2 (`qou-c9fh`)**: Polarization identity, symmetry, and strict non-vanishing
of the Hopf link Chern–Simons pairing `hopfChernSimonsPairing u1 u2 = 2 * u1 * u2`. -/
theorem hopf_link_chern_simons_pairing_nonzero_criterion
    (u1 u2 : ℝ) :
    hopfChernSimonsPairing u1 u2 = ((u1 + u2) ^ 2 - (u1 - u2) ^ 2) / 2 ∧
      hopfChernSimonsPairing u1 u2 = hopfChernSimonsPairing u2 u1 ∧
      (u1 ≠ 0 ∧ u2 ≠ 0 → hopfChernSimonsPairing u1 u2 ≠ 0) := by
  unfold hopfChernSimonsPairing
  refine ⟨by ring, by ring, ?_⟩
  rintro ⟨hu1, hu2⟩
  exact mul_ne_zero (mul_ne_zero two_ne_zero hu1) hu2

/-- **Theorem 3 (`qou-dku0`)**: Exact 3-term geometric telescoping identity
`(1 - r) * habiroGeometricPartialSum3 t0 r + r^3 * t0 = t0` and strict positivity of
the cubic Habiro tail remainder `r^3 * t0` when `0 < r` and `0 < t0`. -/
theorem figure_eight_habiro_tail_geometric_majorant_identity
    (t0 r : ℝ)
    (ht0 : 0 < t0)
    (hr : 0 < r) :
    (1 - r) * habiroGeometricPartialSum3 t0 r + r ^ 3 * t0 = t0 ∧
      0 < r ^ 3 * t0 := by
  unfold habiroGeometricPartialSum3
  have h_tel : (1 - r) * (t0 + r * t0 + r ^ 2 * t0) + r ^ 3 * t0 = t0 := by
    ring
  have h_pos : 0 < r ^ 3 * t0 := mul_pos (pow_pos hr 3) ht0
  exact ⟨h_tel, h_pos⟩

/-- **Theorem 4 (`qou-n5vg`)**: Distinguished `4_1` twist-knot trace specialization at
`s^2 = 3`: the root pair `(2 + s, 2 - s)` has trace `4`, norm `1`, and quadratic
discriminant `(-4)^2 - 4 * 1 * 1 = 12`. -/
theorem twist_knot_distinguished_trace_field_quadratic_lock
    (s : ℝ)
    (hs : s ^ 2 = 3) :
    (2 + s) + (2 - s) = 4 ∧
      (2 + s) * (2 - s) = 1 ∧
      ((-4 : ℝ) ^ 2 - 4 * 1 * 1) = 12 := by
  have h_sum : (2 + s) + (2 - s) = 4 := by ring
  have h_prod : (2 + s) * (2 - s) = 1 := by
    linear_combination -hs
  have h_disc : ((-4 : ℝ) ^ 2 - 4 * 1 * 1) = 12 := by norm_num
  exact ⟨h_sum, h_prod, h_disc⟩

/-- **Theorem 5 (`qou-pwgw`)**: Branch discriminant and second power sum along the
norm-one locus `L1 * L2 = 1` with `L1 + L2 = b`, together with strict negativity of the
discriminant `b^2 - 4 < 0` in the elliptic window `b^2 < 4`. -/
theorem figure_eight_branch_discriminant_and_norm_one_phase_lock
    (L1 L2 b : ℝ)
    (h_tr : L1 + L2 = b)
    (h_norm : L1 * L2 = 1)
    (h_ell : b ^ 2 < 4) :
    (L1 - L2) ^ 2 = b ^ 2 - 4 ∧
      L1 ^ 2 + L2 ^ 2 = b ^ 2 - 2 ∧
      b ^ 2 - 4 < 0 := by
  have h_diff_sq : (L1 - L2) ^ 2 = b ^ 2 - 4 := by
    linear_combination (L1 + L2 + b) * h_tr - 4 * h_norm
  have h_sum_sq : L1 ^ 2 + L2 ^ 2 = b ^ 2 - 2 := by
    linear_combination (L1 + L2 + b) * h_tr - 2 * h_norm
  have h_neg : b ^ 2 - 4 < 0 := by
    linarith [h_ell]
  exact ⟨h_diff_sq, h_sum_sq, h_neg⟩

end QOU.QBeta.HabiroCyclotomicRecurrenceAndHopfCSBrick
