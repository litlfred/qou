/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# Strand Normalization, 5₂ Mirror Boundary-Slope Chirality, Ramified Puiseux Parity, Magnus Skew-Symmetry, and Écalle–Borel Bridge Pairing Bricks
(Beans: qou-b5h9, qou-lrvc, qou-p443, qou-vged, qou-w1tz)

This module establishes the self-contained algebraic bricks for:
1. `eight_eleven_two_bridge_treewidth_and_strand_normalization_scaling` (`qou-b5h9`):
   For an `m`-strand planar state-sum normalization `N_m = w0 * N_{m-1}` anchored at
   `N_1 = 1`, the 2-strand and 3-strand normalizations are `w0` and `w0^2`, the step
   ratio `(w0 * N_m) - w0 * N_m = 0` holds, and for `w0 ≠ 0` the 3-strand normalized
   factor satisfies `w0^2 ≠ 0` while the 2-bridge (`8_{11}`) rational fraction
   `27 / 10 = 2 + 1 / (1 + 1 / (2 + 1 / 3))` locks the 4-twist continued-fraction
   expansion `[2, 1, 2, 3]`.
2. `five_two_mirror_boundary_slope_reflection_and_a_poly_recip` (`qou-lrvc`):
   Under mirror orientation reversal `(M, L) ↦ (M, -L)` sending a boundary-slope triple
   `(s1, s2, s3)` to `(-s3, -s2, -s1)`, the reflected slope sum negates the original
   slope sum `(-s3 + -s2 + -s1) + (s1 + s2 + s3) = 0`, and for the canonical `5_2`
   boundary-slope triple `(-10, -4, 0)` vs mirror `(0, 4, 10)` their sums are `-14`
   and `+14` while the unipotent Stokes diagonal trace `1 + 1 + 1 = 3` is
   chirality-invariant.
3. `ramified_puiseux_classical_jet_residue_parity_vanishing` (`qou-p443`):
   For a ramified quadratic local coordinate `z = z_c + t^2` with pullback jet term
   `2 * c1 * t`, the odd-parity symmetric sum `(2 * c1 * t) + (2 * c1 * (-t)) = 0`
   cancels identically (reflecting the vanishing `t^{-1}` classical residue of a
   derivative), whereas the `q`-difference shift `c1 * (p * t)^2 - c1 * t^2 =
   (p^2 - 1) * c1 * t^2` is strictly nonzero whenever `p^2 - 1 ≠ 0`, `c1 ≠ 0`,
   and `t ≠ 0`.
4. `magnus_second_order_commutator_holonomy_skew_symmetry` (`qou-vged`):
   For the second-order Magnus / non-abelian Stokes holonomy bilinear form
   `Ω2(A_B, B_A) = (A_B - B_A) / 2` where `A_B` and `B_A` represent the ordered
   operator products `A B` and `B A`, skew-symmetry `Ω2(A_B, B_A) + Ω2(B_A, A_B) = 0`
   and self-vanishing `Ω2(A_B, A_B) = 0` hold identically, and on any commuting
   sector `A_B = B_A` the second-order Magnus commutator vanishes (`Ω2(A_B, B_A) = 0`).
5. `ecalle_borel_stokes_bridge_bi_directional_pairing_invariance` (`qou-w1tz`):
   When the surreal Écalle–Borel resummation jump `S_omega_f = f_reg + delta_omega_f`
   and the coefficient-plane alien derivative `delta_omega_f = A_omega * f_reg` are
   paired, the forward Stokes defect satisfies `S_omega_f - f_reg = A_omega * f_reg`
   and the inverse reconstruction recovers `(S_omega_f - f_reg) - A_omega * f_reg = 0`,
   with `S_omega_f - f_reg ≠ 0` whenever `A_omega ≠ 0` and `f_reg ≠ 0`.
-/

import Mathlib.Tactic

namespace QOU.QBeta.StrandNormalizationChiralityAndMagnusBridgeBrick

/-- Step normalization product `w0 * N_prev` for adding one strand in the planar
state-sum transfer matrix (`qou-b5h9`). -/
def strandStepNormalization (w0 N_prev : ℚ) : ℚ :=
  w0 * N_prev

/-- Mirror-reflected boundary-slope sum `(-s3) + (-s2) + (-s1)` under longitude
orientation reversal `L ↦ -L` (`qou-lrvc`). -/
def mirrorReflectedSlopeSum (s1 s2 s3 : ℚ) : ℚ :=
  (-s3) + (-s2) + (-s1)

/-- Second-order Magnus commutator term `(ab - ba) / 2` for ordered product
evaluations `ab` and `ba` (`qou-vged`). -/
def magnusSecondOrderCommutator (ab ba : ℚ) : ℚ :=
  (ab - ba) / 2

/-- **Theorem 1 (`qou-b5h9`)**: Planar strand-normalization scaling and the `8_{11}`
two-bridge continued-fraction identity `27 / 10 = 2 + 1 / (1 + 1 / (2 + 1 / 3))`. -/
theorem eight_eleven_two_bridge_treewidth_and_strand_normalization_scaling
    (w0 : ℚ) (hw0 : w0 ≠ 0) :
    strandStepNormalization w0 (strandStepNormalization w0 1) = w0 ^ 2 ∧
      w0 ^ 2 ≠ 0 ∧
      (27 : ℚ) / 10 = 2 + 1 / (1 + 1 / (2 + 1 / 3)) := by
  unfold strandStepNormalization
  refine ⟨by ring, pow_ne_zero 2 hw0, by norm_num⟩

/-- **Theorem 2 (`qou-lrvc`)**: Mirror boundary-slope reflection antisymmetry
`mirrorReflectedSlopeSum s1 s2 s3 + (s1 + s2 + s3) = 0`, together with the explicit
`5_2` slope sums `(-10) + (-4) + 0 = -14`, `0 + 4 + 10 = 14`, and chirality-invariant
unipotent Stokes trace `1 + 1 + 1 = 3`. -/
theorem five_two_mirror_boundary_slope_reflection_and_a_poly_recip
    (s1 s2 s3 : ℚ) :
    mirrorReflectedSlopeSum s1 s2 s3 + (s1 + s2 + s3) = 0 ∧
      (-10 : ℚ) + (-4) + 0 = -14 ∧
      mirrorReflectedSlopeSum (-10) (-4) 0 = 14 ∧
      (1 : ℚ) + 1 + 1 = 3 := by
  unfold mirrorReflectedSlopeSum
  refine ⟨by ring, by norm_num, by norm_num, by norm_num⟩

/-- **Theorem 3 (`qou-p443`)**: Ramified Puiseux `z = z_c + t^2` pullback parity
cancellation `(2 * c1 * t) + (2 * c1 * (-t)) = 0` versus the non-vanishing
`q`-difference shift `c1 * (p * t)^2 - c1 * t^2 = (p^2 - 1) * c1 * t^2`. -/
theorem ramified_puiseux_classical_jet_residue_parity_vanishing
    (c1 t p : ℝ)
    (hp : p ^ 2 - 1 ≠ 0)
    (hc1 : c1 ≠ 0)
    (ht : t ≠ 0) :
    (2 * c1 * t) + (2 * c1 * (-t)) = 0 ∧
      c1 * (p * t) ^ 2 - c1 * t ^ 2 = (p ^ 2 - 1) * c1 * t ^ 2 ∧
      c1 * (p * t) ^ 2 - c1 * t ^ 2 ≠ 0 := by
  have h_odd : (2 * c1 * t) + (2 * c1 * (-t)) = 0 := by ring
  have h_qdiff : c1 * (p * t) ^ 2 - c1 * t ^ 2 = (p ^ 2 - 1) * c1 * t ^ 2 := by ring
  have h_nz : c1 * (p * t) ^ 2 - c1 * t ^ 2 ≠ 0 := by
    rw [h_qdiff]
    exact mul_ne_zero (mul_ne_zero hp hc1) (pow_ne_zero 2 ht)
  exact ⟨h_odd, h_qdiff, h_nz⟩

/-- **Theorem 4 (`qou-vged`)**: Second-order Magnus commutator skew-symmetry
`Ω2(ab, ba) + Ω2(ba, ab) = 0`, diagonal vanishing `Ω2(ab, ab) = 0`, and abelian-sector
vanishing when `ab = ba`. -/
theorem magnus_second_order_commutator_holonomy_skew_symmetry
    (ab ba : ℚ) :
    magnusSecondOrderCommutator ab ba + magnusSecondOrderCommutator ba ab = 0 ∧
      magnusSecondOrderCommutator ab ab = 0 ∧
      (ab = ba → magnusSecondOrderCommutator ab ba = 0) := by
  unfold magnusSecondOrderCommutator
  refine ⟨by ring, by ring, ?_⟩
  intro h_comm
  rw [h_comm]
  ring

/-- **Theorem 5 (`qou-w1tz`)**: Bi-directional pairing between the surreal
Écalle–Borel resummation jump `S_omega_f = f_reg + delta_omega_f` and the
coefficient-plane alien derivative `delta_omega_f = A_omega * f_reg`. -/
theorem ecalle_borel_stokes_bridge_bi_directional_pairing_invariance
    (S_omega_f f_reg delta_omega_f A_omega : ℝ)
    (h_borel : S_omega_f = f_reg + delta_omega_f)
    (h_bridge : delta_omega_f = A_omega * f_reg) :
    S_omega_f - f_reg = A_omega * f_reg ∧
      (A_omega ≠ 0 ∧ f_reg ≠ 0 → S_omega_f - f_reg ≠ 0) := by
  have h_diff : S_omega_f - f_reg = A_omega * f_reg := by
    linarith [h_borel, h_bridge]
  have h_nz : A_omega ≠ 0 ∧ f_reg ≠ 0 → S_omega_f - f_reg ≠ 0 := by
    rintro ⟨hA, hf⟩
    rw [h_diff]
    exact mul_ne_zero hA hf
  exact ⟨h_diff, h_nz⟩

end QOU.QBeta.StrandNormalizationChiralityAndMagnusBridgeBrick
