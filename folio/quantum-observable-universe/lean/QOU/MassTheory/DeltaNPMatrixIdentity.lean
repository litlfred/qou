import QOU.MassTheory.HolonomyConnectionSplit

/-!
# The n − p difference of `tr(𝒟²)` on the nucleon weight blocks

`𝒟 = q⁻¹(hol − 1) + (1 − q⁻¹) T³` on the proton and neutron weight spaces (3 × 3 blocks),
with `hol = (σ₀σ₁⁻¹)³` (`Vp`, `Vn` of `HolonomyConnectionSplit`) and `T³ = +½`, `−½` on them.
`∇ = hol − 1` is an identification that has not been ruled.

Result: `tr(𝒟_n²) − tr(𝒟_p²) = 2 q⁻¹ (1 − q⁻¹) (q² − 1)⁴ (q⁴ + q² + 1) / q⁶`,
i.e. `2 q⁻¹ (1 − q⁻¹) h⁴ [3]_q`. The two squared pieces cancel, because the holonomies
are conjugate (`Vn3_conj`), and only the Reeb–holonomy cross term remains.
Generic field of characteristic ≠ 2 (§7c; `T³ = ±½` needs `2 ≠ 0`). No empirical input.
-/

namespace QOU.MassTheory.DeltaNPMatrixIdentity

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.MassTheory.HolonomyConnectionSplit

variable {R : Type*} [Field R]

/-- `𝒟` on a weight block with holonomy `V³` and Reeb eigenvalue `t`. -/
def Dblock (q t : R) (V : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 3) (Fin 3) R :=
  q⁻¹ • (V ^ 3 - 1) + ((1 - q⁻¹) * t) • (1 : Matrix (Fin 3) (Fin 3) R)

theorem trace_sq_affine (a c : R) (X : Matrix (Fin 3) (Fin 3) R) :
    trace ((a • X + c • (1 : Matrix (Fin 3) (Fin 3) R)) ^ 2) =
      a ^ 2 * trace (X ^ 2) + 2 * a * c * trace X + 3 * c ^ 2 := by
  simp only [sq, Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.mul_one, Matrix.one_mul, trace_add, trace_smul, trace_one,
    Fintype.card_fin, smul_eq_mul]
  push_cast
  ring

theorem trace_conj (P M : Matrix (Fin 3) (Fin 3) R) (hP : IsUnit P.det) :
    trace (P * M * P⁻¹) = trace M := by
  rw [Matrix.trace_mul_comm, ← Matrix.mul_assoc, Matrix.nonsing_inv_mul _ hP, Matrix.one_mul]

theorem delta_np_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : R) ≠ 0) :
    trace (Dblock q (-(1 / 2)) (Vn q) ^ 2) - trace (Dblock q (1 / 2) (Vp q) ^ 2) =
      2 * q⁻¹ * (1 - q⁻¹) * ((q ^ 2 - 1) ^ 4 * (q ^ 4 + q ^ 2 + 1)) / q ^ 6 := by
  have hdet : IsUnit (P q).det := by
    rw [det_P q hq]
    exact isUnit_iff_ne_zero.mpr (div_ne_zero (neg_ne_zero.mpr hq2) (pow_ne_zero 4 hq))
  set X := Vp q ^ 3 - 1 with hX
  have hXn : Vn q ^ 3 - 1 = P q * X * (P q)⁻¹ := by
    rw [Vn3_conj q hq hq2, hX, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_one,
      Matrix.mul_nonsing_inv _ hdet]
  have hXn2 : (Vn q ^ 3 - 1) ^ 2 = P q * X ^ 2 * (P q)⁻¹ := by
    rw [hXn, sq, sq]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (P q)⁻¹ (P q), Matrix.nonsing_inv_mul _ hdet, Matrix.one_mul]
  have htr : trace X = -((q ^ 2 - 1) ^ 4 * (q ^ 4 + q ^ 2 + 1)) / q ^ 6 := by
    rw [hX, trace_sub, trace_one, Fintype.card_fin]
    have := trace_Vp3_sub_three q hq
    push_cast at this ⊢
    linear_combination this
  unfold Dblock
  rw [trace_sq_affine, trace_sq_affine, hXn2, trace_conj _ _ hdet, hXn, trace_conj _ _ hdet,
    ← hX, htr]
  field_simp
  ring

/-- For any connection `∇` on the proton block and its conjugate on the neutron block, the
n − p difference of `tr(𝒟²)` is only the cross term: `−2 q⁻¹ (1 − q⁻¹) tr ∇_p`. So only the
trace of the chosen connection matters, e.g. `log hol` or `(hol − hol⁻¹)/2` (trace 0) give 0. -/
theorem delta_np_general (q : R) (hq : q ≠ 0) (h2 : (2 : R) ≠ 0) (Pm Fp : Matrix (Fin 3) (Fin 3) R)
    (hP : IsUnit Pm.det) :
    trace ((q⁻¹ • (Pm * Fp * Pm⁻¹) + ((1 - q⁻¹) * (-(1 / 2))) • (1 : Matrix (Fin 3) (Fin 3) R)) ^ 2)
      - trace ((q⁻¹ • Fp + ((1 - q⁻¹) * (1 / 2)) • (1 : Matrix (Fin 3) (Fin 3) R)) ^ 2) =
      -2 * q⁻¹ * (1 - q⁻¹) * trace Fp := by
  have hsq : (Pm * Fp * Pm⁻¹) ^ 2 = Pm * Fp ^ 2 * Pm⁻¹ := by
    rw [sq, sq]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc Pm⁻¹ Pm, Matrix.nonsing_inv_mul _ hP, Matrix.one_mul]
  rw [trace_sq_affine, trace_sq_affine, hsq, trace_conj _ _ hP, trace_conj _ _ hP]
  field_simp
  ring

end QOU.MassTheory.DeltaNPMatrixIdentity
