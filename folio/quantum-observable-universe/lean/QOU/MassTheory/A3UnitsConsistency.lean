/-
# The "1.6× A=3 magnitude near-miss" is dimensionally ill-posed AND scale-ambiguous

The corpus (#4364 / three-walls) compares the 3-body cluster `c₃ = 0.297` — a genuine ENERGY in MeV
(`E₀·(1−τ_Borr)`) — directly to the DIMENSIONLESS simplex coefficient `μ₃ = 0.4708`
(`ρ_strong(3) − ρ_grad(3)`). `borromean_h9_magnitude_lift_probe.py:188` admits the pun: *"target
μ₃ = 0.4708 (dimensionless, read as MeV)."* But repairing it does **not** give a single honest gap: the
categorical binding scale is UNPINNED — the master formula `B = m_e·|Σ y_λ χ^λ sgn f^λ|` undershoots
the DEUTERON itself by `C_knot = B_AME/B_cat = 2.2246/0.3801 ≈ 5.85×`, an explicitly FITTED (not
derived) deficit ratio = the open Δ_λ gate. Normalizing `c₃` by the AME deuteron gives a 3.53×
UNDERSHOOT; by the categorical deuteron (scale-consistent, `E₀/m_e` cancels) a 1.66× OVERSHOOT — the
two differ by exactly `C_knot`. So the "1.6× near-miss" is an artifact of the unpinned scale, spanning
overshoot-to-undershoot; the one unambiguous object is `C_knot`, the open gate. **Self-correction:** an
earlier version of this file asserted "the honest gap is 3.53×" — that picked one normalization and
over-claimed; corrected here. scope-(a) calibration; no fit; nothing wired.
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

/-- **`C_knot` — the open Δ_λ gate.** The master formula `B = m_e·|Σ y_λ χ^λ sgn f^λ|` undershoots the
deuteron: `C_knot = B_AME(²H)/B_cat(²H) = 2.224566/0.380132 > 5` (≈5.85×), an explicitly FITTED (not
derived) deficit ratio. This unpinned scale is what makes the A=3 gap ambiguous. -/
theorem c_knot_gt_five : (2.224566 : ℝ) / 0.380132 > 5 := by norm_num

/-- **Normalization A (÷ AME deuteron): a 3.53× UNDERshoot.** `μ₃ / (c₃/B_AME) > 3`. -/
theorem gap_A_undershoot_gt_three : (0.4708 : ℝ) / (0.297 / 2.224566) > 3 := by norm_num

/-- **Normalization B (÷ categorical deuteron, scale-consistent): a 1.66× OVERshoot.** With the
model's own deuteron the scale `E₀/m_e` cancels, giving `(c₃/B_cat)/μ₃` strictly between 1 and 2 — an
overshoot, the opposite sign of normalization A. -/
theorem gap_B_overshoot_between_one_two :
    1 < (0.297 / 0.380132 : ℝ) / 0.4708 ∧ (0.297 / 0.380132 : ℝ) / 0.4708 < 2 := by
  constructor <;> norm_num

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **The two normalizations differ by exactly `C_knot`** (`(c₃/B_cat)/(c₃/B_AME) = B_AME/B_cat`), so
the A=3 gap swings across the whole open-gate factor — a 1.66× overshoot to a 3.53× undershoot. The
"1.6× near-miss" is therefore an artifact of the unpinned categorical binding scale, not a robust
proximity. (Instance of `units_correction_is_scale` with `c = c₃`, `B = B_AME/B_cat`.) -/
theorem normalizations_differ_by_c_knot (c b1 b2 : R) (hc : c ≠ 0) (hb1 : b1 ≠ 0) (hb2 : b2 ≠ 0) :
    (c / b2) / (c / b1) = b1 / b2 := by
  field_simp

/-- **Capstone — the A=3 near-miss is scale-ambiguous, not a units-correctable near-miss.** The gap is
a 3.53× undershoot under one normalization (`gap_A_undershoot_gt_three`) and a 1.66× overshoot under
the scale-consistent one (`gap_B_overshoot_between_one_two`); the two span the unpinned open gate
`C_knot > 5` (`c_knot_gt_five`). So repairing the dimensional pun does not yield a single honest gap —
the real open object is `C_knot` itself (the Δ_λ magnitude). scope-(a) calibration + self-correction;
no fit. -/
theorem a3_near_miss_is_scale_ambiguous :
    ((0.4708 : ℝ) / (0.297 / 2.224566) > 3) ∧
    (1 < (0.297 / 0.380132 : ℝ) / 0.4708 ∧ (0.297 / 0.380132 : ℝ) / 0.4708 < 2) ∧
    ((2.224566 : ℝ) / 0.380132 > 5) :=
  ⟨gap_A_undershoot_gt_three, gap_B_overshoot_between_one_two, c_knot_gt_five⟩

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **Transitive chain rule for three binding scale normalizations (`qou-j0j8`).**
For any nonzero cluster energy `c` and three nonzero normalization scales `b1, b2, b3 : R`,
the product of the pairwise relative normalization ratios equals `b1 / b3`. -/
theorem normalizations_chain_rule (c b1 b2 b3 : R)
    (hc : c ≠ 0) (hb1 : b1 ≠ 0) (hb2 : b2 ≠ 0) (hb3 : b3 ≠ 0) :
    ((c / b2) / (c / b1)) * ((c / b3) / (c / b2)) = b1 / b3 := by
  rw [normalizations_differ_by_c_knot c b1 b2 hc hb1 hb2,
    normalizations_differ_by_c_knot c b2 b3 hc hb2 hb3]
  field_simp

end QOU.MassTheory.A3UnitsConsistency
