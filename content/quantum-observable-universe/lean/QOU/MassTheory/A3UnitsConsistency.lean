/-
# The "1.6× A=3 magnitude near-miss" is a units artifact — the honest gap is 3.53×

The corpus (#4364 / three-walls) compares the derived 3-body cluster `c₃ = 0.297` — a genuine ENERGY
in MeV (`E₀·(1−τ_Borr)`, `E₀ = m_e/(q₀(q₀−1)) ≈ 4.19 MeV`) — directly to the simplex coefficient
`μ₃ = 0.4708`, which is DIMENSIONLESS (`ρ_strong(3) − ρ_grad(3)`, a pure ratio; `ρ_strong(2)=1`
confirms). `borromean_h9_magnitude_lift_probe.py:188` admits it: *"target μ₃ = 0.4708 (dimensionless,
read as MeV)."* Converting the cluster into the dimensionless decomposition (`c₃/B(²H)`,
`B(²H) = 2.224566 MeV`) gives the honest gap `3.53×`, not `1.6×`; the correction factor is exactly
`B(²H)`. The derived cluster supplies only 28% (not 63%) of the 3-body binding target — the A=3
magnitude is ~2× further from closure than the headline. scope-(a) calibration; no fit; nothing wired.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp
import Mathlib.Data.Real.Basic

namespace QOU.MassTheory.A3UnitsConsistency

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **The correction factor is exactly `B`.** Comparing a MeV energy `c` to a dimensionless target `μ`
gives the punned gap `μ/c`; the dimensionally-consistent gap divides the energy by the scale `B`
(`c ↦ c/B`), giving `μ/(c/B)`. Their ratio is exactly `B`:
`(μ/(c/B)) / (μ/c) = B`. Here `B = B(²H)`. -/
theorem units_correction_is_scale (μ c B : R) (hμ : μ ≠ 0) (hc : c ≠ 0) (hB : B ≠ 0) :
    (μ / (c / B)) / (μ / c) = B := by
  field_simp

/-- **The honest A=3 3-body gap exceeds 3** (`μ₃ / (c₃/B(²H)) > 3`, ≈3.53×) — versus the punned 1.585×.
The cluster is ~2× further from the target than the headline near-miss. -/
theorem honest_gap_gt_three : (0.4708 : ℝ) / (0.297 / 2.224566) > 3 := by norm_num

/-- **The derived cluster supplies < 30% of the 3-body target** (`(c₃/B(²H))/μ₃ < 0.30`, ≈28.4%) — not
the punned 63%. -/
theorem cluster_supplies_lt_30_pct : (0.297 / 2.224566 : ℝ) / 0.4708 < 0.30 := by norm_num

/-- **Strengthened order-separation.** In honest (dimensionless) units a higher-order closure would
need an h⁶ coefficient `a₁ = (μ₃ − c₃/B(²H))/((c₃/B(²H))·h²) > 50` (≈57.8) — far more anomalous than
the punned 13.4, so the "compute higher orders" route is ruled out even harder. -/
theorem strengthened_required_coeff_gt_fifty :
    ((0.4708 : ℝ) - 0.297 / 2.224566) / ((0.297 / 2.224566) * 0.0437062) > 50 := by norm_num

/-- **Capstone — the near-miss is a units artifact.** The honest gap exceeds 3 (`honest_gap_gt_three`),
the cluster supplies <30% (`cluster_supplies_lt_30_pct`), and the higher-order route is ruled out even
harder (`strengthened_required_coeff_gt_fifty`); the correction is exactly the scale `B`
(`units_correction_is_scale`). scope-(a) calibration; no fit. -/
theorem a3_near_miss_is_units_artifact :
    ((0.4708 : ℝ) / (0.297 / 2.224566) > 3) ∧
    ((0.297 / 2.224566 : ℝ) / 0.4708 < 0.30) ∧
    (((0.4708 : ℝ) - 0.297 / 2.224566) / ((0.297 / 2.224566) * 0.0437062) > 50) :=
  ⟨honest_gap_gt_three, cluster_supplies_lt_30_pct, strengthened_required_coeff_gt_fifty⟩

end QOU.MassTheory.A3UnitsConsistency
