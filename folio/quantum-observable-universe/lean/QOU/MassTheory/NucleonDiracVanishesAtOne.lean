import QOU.MassTheory.DeltaNPMatrixIdentity

/-!
# At `q = 1` the nucleon `𝒟` vanishes and the electron `𝒟` does not

With `∇ = hol − q^{writhe}·1` (the mass-identity Temperley–Lieb reading, LITERATURE-COMPARISON
§27–§28):
- nucleons: `hol = V³ = (σ₀σ₁⁻¹)³`, a pure braid of writhe 0, so `V³(1) = 1` on both weight
  blocks. With `1 − q⁻¹ = 0` at `q = 1`, the whole `𝒟` is `0` there (`Dblock_one_eq_zero`).
  So any trace with a `𝒟` factor vanishes at `q = 1` (`trace_mul_Dblock_one`); this includes
  `ψ*⊗𝒟ψ` with any `q`-independent charge insertion.
- electron: `σ₀σ₁σ₀` (writhe 3) on the proton block at `q = 1` is the transposition of strands
  0 and 2, so `𝒟_e(1) = halfTwistA 1 − 1 ≠ 0` and `tr(𝒟_e(1)²) = 4`
  (`trace_electron_D_sq_one`).

Consequence (§28): any linear energy map calibrated on the electron gives an n − p difference
that vanishes at `q = 1`. Generic field, characteristic ≠ 2 where `½` appears. No empirical input.
-/

namespace QOU.MassTheory.NucleonDiracVanishesAtOne

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.MassTheory.HolonomyConnectionSplit
open QOU.MassTheory.DeltaNPMatrixIdentity

variable {R : Type*} [Field R]

/-- `V(1) = σ₀σ₁⁻¹` at `q = 1` on the proton block is a 3-cycle. -/
theorem Vp_one : Vp (1 : R) = !![0, 1, 0; 0, 0, 1; 1, 0, 0] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Vp, A₁, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three]

/-- `V(1)` on the neutron block is a 3-cycle. -/
theorem Vn_one : Vn (1 : R) = !![0, 0, 1; 1, 0, 0; 0, 1, 0] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Vn, B₁, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three]

theorem Vp_one_cube : Vp (1 : R) ^ 3 = 1 := by
  rw [Vp_one]; ext i j; fin_cases i <;> fin_cases j <;>
    simp [pow_succ, Matrix.mul_apply, Fin.sum_univ_three]

theorem Vn_one_cube : Vn (1 : R) ^ 3 = 1 := by
  rw [Vn_one]; ext i j; fin_cases i <;> fin_cases j <;>
    simp [pow_succ, Matrix.mul_apply, Fin.sum_univ_three]

theorem Dblock_one_eq_zero_p (t : R) : Dblock (1 : R) t (Vp 1) = 0 := by
  simp [Dblock, Vp_one_cube]

theorem Dblock_one_eq_zero_n (t : R) : Dblock (1 : R) t (Vn 1) = 0 := by
  simp [Dblock, Vn_one_cube]

/-- Any trace containing the nucleon `𝒟` as a factor vanishes at `q = 1`. -/
theorem trace_mul_Dblock_one (t : R) (M N : Matrix (Fin 3) (Fin 3) R) :
    trace (M * Dblock (1 : R) t (Vp 1) * N) = 0 ∧ trace (M * Dblock (1 : R) t (Vn 1) * N) = 0 := by
  simp [Dblock_one_eq_zero_p, Dblock_one_eq_zero_n]

/-- The electron `𝒟` on the proton block, `∇_e = σ₀σ₁σ₀ − q³·1`. -/
def DelectronP (q t : R) : Matrix (Fin 3) (Fin 3) R :=
  q⁻¹ • (halfTwistA q - q ^ 3 • (1 : Matrix (Fin 3) (Fin 3) R)) +
    ((1 - q⁻¹) * t) • (1 : Matrix (Fin 3) (Fin 3) R)

theorem DelectronP_one (t : R) :
    DelectronP (1 : R) t = halfTwistA 1 - 1 := by
  simp [DelectronP]

/-- `σ₀σ₁σ₀` at `q = 1` on the proton block is the transposition of strands 0 and 2. -/
theorem halfTwistA_one : halfTwistA (1 : R) = !![0, 0, 1; 0, 1, 0; 1, 0, 0] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [halfTwistA, A₁, A₂, Matrix.mul_apply, Fin.sum_univ_three]

theorem trace_electron_D_sq_one (t : R) : trace (DelectronP (1 : R) t ^ 2) = 4 := by
  rw [DelectronP_one, halfTwistA_one]
  simp [sq, Matrix.trace, Fin.sum_univ_three, Matrix.mul_apply, Matrix.sub_apply, Matrix.one_apply]
  norm_num

/-- So the electron trace is nonzero at `q = 1` (characteristic ≠ 2). -/
theorem trace_electron_D_sq_one_ne_zero [CharZero R] (t : R) :
    trace (DelectronP (1 : R) t ^ 2) ≠ 0 := by
  rw [trace_electron_D_sq_one]; norm_num

end QOU.MassTheory.NucleonDiracVanishesAtOne
