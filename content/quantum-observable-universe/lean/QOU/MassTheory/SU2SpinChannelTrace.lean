import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

namespace QOU.MassTheory.SU2SpinChannelTrace

/-- The quantum dimension of the SU(2) singlet (spin-0) is 1. -/
def q_dim_singlet (_q : ℝ) : ℝ := 1

/-- The quantum dimension of the SU(2) triplet (spin-1) is q^2 + 1 + q^{-2}. -/
noncomputable def q_dim_triplet (q : ℝ) : ℝ := q^2 + 1 + q⁻¹^2

/-- The multiplicity-weighted average of the SU(2) two-nucleon spin channels.
    The triplet has statistical weight 3, the singlet has statistical weight 1. -/
noncomputable def su2_spin_channel_average (q : ℝ) : ℝ :=
  (3 * q_dim_triplet q + 1 * q_dim_singlet q) / 4

/-- The empirical legacy H4 scaling factor (Family A linking weight). -/
noncomputable def legacy_h4_scaling (q : ℝ) : ℝ :=
  (3 * q^2 + 4 + 3 * q⁻¹^2) / 4

/-- **Theorem**: The legacy H4 scaling factor is identically the SU(2) spin-channel average. -/
theorem legacy_scaling_is_su2_spin_average (q : ℝ) (_hq : q ≠ 0) :
  su2_spin_channel_average q = legacy_h4_scaling q := by
  dsimp [su2_spin_channel_average, q_dim_triplet, q_dim_singlet, legacy_h4_scaling]
  ring

end QOU.MassTheory.SU2SpinChannelTrace
