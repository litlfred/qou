import QOU.MassTheory.GroundStateOrderingRefutation
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# Ground-state ordering, convention C with `Real.sqrt` (Transcendental companion)

Split from `QOU.MassTheory.GroundStateOrderingRefutation` (bean `qou-dk7p`). That
file states the excised convention C in the square-root variable `t`, `q = t²`,
as `zCt t = t/(t²+1)`. This file keeps `zC q = √q/(q+1)` and its theorems under
their original names, reducing each to the `t` form via `√(t²) = t`.
-/

namespace QOU.MassTheory.GroundStateOrderingRefutation

/-- Convention C, `z = √q/(q+1)`: excised by the owner ruling of
2026-08-15, retained here only as a cross-check. -/
noncomputable def zC (q : ℝ) : ℝ := Real.sqrt q / (q + 1)

theorem zC_sq_eq {t : ℝ} (ht : 0 < t) : zC (t ^ 2) = zCt t := by
  unfold zC zCt
  rw [Real.sqrt_sq ht.le]

theorem zC_nonneg {q : ℝ} (hq : 0 < q) : 0 ≤ zC q := by
  unfold zC
  exact div_nonneg (Real.sqrt_nonneg q) (by linarith)

/-- `z_C < q` for `q > 1`: convention C also lies below `λ₊ = q`. -/
theorem zC_lt_self {q : ℝ} (hq : 1 < q) : zC q < q := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have hs : Real.sqrt q ≤ q := by
    have h2 : q ≤ q ^ 2 := by nlinarith
    have := Real.sqrt_le_sqrt h2
    rwa [Real.sqrt_sq (le_of_lt hq0)] at this
  unfold zC
  rw [div_lt_iff₀ (by linarith)]
  nlinarith [hs]

theorem cPlus_zC_pos {q : ℝ} (hq : 1 < q) : 0 < cPlus q (zC q) := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  refine cPlus_pos hq0 (lt_of_lt_of_le ?_ (zC_nonneg hq0))
  simpa using inv_pos.mpr hq0

theorem cMinus_zC_pos {q : ℝ} (hq : 1 < q) : 0 < cMinus q (zC q) :=
  cMinus_pos (lt_trans zero_lt_one hq) (zC_lt_self hq)

theorem sortedV1_zC_eq {t : ℝ} (ht : 1 < t) :
    sortedV1 (t ^ 2) (zC (t ^ 2)) = (Anum t - Bnum t * t ^ 12) / (K t * t ^ 6) := by
  rw [zC_sq_eq (lt_trans zero_lt_one ht)]
  exact sortedV1_zCt_eq ht

theorem sortedV1_zC_nonneg {t : ℝ} (ht : 1 < t)
    (hU : 0 ≤ Anum t - Bnum t * t ^ 12) :
    0 ≤ sortedV1 (t ^ 2) (zC (t ^ 2)) := by
  rw [zC_sq_eq (lt_trans zero_lt_one ht)]
  exact sortedV1_zCt_nonneg ht hU

/-- **The refutation under convention C**, in the shape this file
originally carried. -/
theorem prescribed_not_minimiser_A5_conventionC {t : ℝ} (ht : 1 < t)
    (hU : 0 ≤ Anum t - Bnum t * t ^ 12)
    (h23 : sharedV2 (t ^ 2) (zC (t ^ 2)) * sharedV3 (t ^ 2) (zC (t ^ 2)) ≠ 0) :
    ¬ (|prescribedV0 (t ^ 2) (zC (t ^ 2)) * prescribedV1 (t ^ 2) (zC (t ^ 2))
          * (sharedV2 (t ^ 2) (zC (t ^ 2)) * sharedV3 (t ^ 2) (zC (t ^ 2)))|
        ≤ |sortedV0 (t ^ 2) (zC (t ^ 2)) * sortedV1 (t ^ 2) (zC (t ^ 2))
          * (sharedV2 (t ^ 2) (zC (t ^ 2)) * sharedV3 (t ^ 2) (zC (t ^ 2)))|) := by
  rw [zC_sq_eq (lt_trans zero_lt_one ht)] at h23 ⊢
  exact prescribed_not_minimiser_A5_conventionC_t ht hU h23

end QOU.MassTheory.GroundStateOrderingRefutation
