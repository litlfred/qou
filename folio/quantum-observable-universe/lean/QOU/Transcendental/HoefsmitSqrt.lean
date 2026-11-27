import QOU.MassTheory.GammaGammaSelectorH3
import Mathlib.Data.Real.Sqrt

/-!
# QOU.Transcendental.HoefsmitSqrt

The positive Hoefsmit off-diagonal entry `b = √(a·a' + 1) = √[3]_q / [2]_q` of the
orthogonal `(2,1)` representation of `H₃(q)`.

It sits behind the transcendental boundary (owner ruling 2026-11-27, bean `qou-dk7p`)
because `Real.sqrt` is a completion of `ℚ`, and `b` is not in `ℚ(q)`: it lies in the
quadratic extension `ℚ(q)(√[3]_q)`. Every γγ-selection result
(`GammaGammaSelectorH3`, `GammaGammaVertexOrder`, `GammaGammaFrobeniusSelection` and
the files built on them) is stated for an arbitrary `b` with `HoefsmitRoot q b`, i.e.
`b² = a·a' + 1`. This file supplies the one real root that witnesses the hypothesis.

No empirical value enters this file.
-/

namespace QOU.Transcendental.HoefsmitSqrt

open QOU.Mass.GammaGammaSelectorH3

/-- `b = √(a·a' + 1)`, the positive Hoefsmit off-diagonal entry. -/
noncomputable def hoefsmitB (q : ℝ) : ℝ := Real.sqrt (hoefsmitA q * hoefsmitA' q + 1)

/-- The positive square root is a Hoefsmit root for every `0 < q ≠ 1`. -/
theorem hoefsmitRoot_hoefsmitB {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    HoefsmitRoot q (hoefsmitB q) := by
  show Real.sqrt _ ^ 2 = _
  rw [Real.sq_sqrt]
  rw [hoefsmitA_mul_A'_add_one hq hq1]
  exact (qThree_div_qTwo_sq_pos hq).le

/-- `b > 0` for every `0 < q ≠ 1`. -/
theorem hoefsmitB_pos {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) : 0 < hoefsmitB q := by
  unfold hoefsmitB
  rw [hoefsmitA_mul_A'_add_one hq hq1]
  exact Real.sqrt_pos.mpr (qThree_div_qTwo_sq_pos hq)

end QOU.Transcendental.HoefsmitSqrt
