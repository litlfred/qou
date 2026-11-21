import QOU.MassTheory.DeltaNPMatrixIdentity

/-!
# n − p of the static quark-charge term `S = QPair · hol`

On the proton block `QPair = 0`, on the neutron block `QPair = −⅓·1`
(`NucleonWeightSpaceTwoTerm`). With `hol = V³` the n − p of `tr S` is
`−⅓·tr(Vn³) = −⅓·tr(Vp³) = −1 + (q²−1)⁴(q⁴+q²+1)/(3q⁶)`, which is `−1` at `q = 1`.
So unlike every `𝒟`-term (`NucleonDiracVanishesAtOne`), this n − p survives at `q = 1`.
Generic field; `3 ≠ 0` (and `2 ≠ 0` at `q = 1`) and `q² + 1 ≠ 0` where needed. Pre-registration:
`computations/probes/mn_own_identity/PREREGISTRATION-static-charge-term.md`.
-/

namespace QOU.MassTheory.StaticChargeTermNP

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.MassTheory.HolonomyConnectionSplit
open QOU.MassTheory.DeltaNPMatrixIdentity

variable {R : Type*} [Field R]

theorem delta_static (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h3' : (3 : R) ≠ 0) :
    trace (QPairN * Vn q ^ 3) - trace (QPairP * Vp q ^ 3) =
      -1 + (q ^ 2 - 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (3 * q ^ 6) := by
  have hdet : IsUnit (P q).det := by
    rw [det_P q hq]
    exact isUnit_iff_ne_zero.mpr (div_ne_zero (neg_ne_zero.mpr hq2) (pow_ne_zero 4 hq))
  have htr : trace (Vn q ^ 3) = trace (Vp q ^ 3) := by
    rw [Vn3_conj q hq hq2, trace_conj _ _ hdet]
  have h3 := trace_Vp3_sub_three q hq
  simp only [QPairN, QPairP, Matrix.zero_mul, Matrix.trace_zero, sub_zero, Matrix.smul_mul,
    Matrix.one_mul, Matrix.trace_smul, smul_eq_mul, htr]
  have : trace (Vp q ^ 3) = 3 - (q ^ 2 - 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / q ^ 6 := by
    rw [← sub_eq_zero]; rw [← sub_eq_zero] at h3; rw [← h3]; ring
  rw [this]; field_simp; ring

/-- At `q = 1` the static n − p is `−1`: it survives. -/
theorem delta_static_one (h2 : (2 : R) ≠ 0) (h3' : (3 : R) ≠ 0) :
    trace (QPairN * Vn (1 : R) ^ 3) - trace (QPairP * Vp (1 : R) ^ 3) = -1 := by
  rw [delta_static 1 one_ne_zero (by norm_num; exact h2) h3']; norm_num

end QOU.MassTheory.StaticChargeTermNP
