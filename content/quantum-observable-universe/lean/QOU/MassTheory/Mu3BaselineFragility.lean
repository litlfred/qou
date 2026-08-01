/-
# The μ₃ (A=3 magnitude) target is a small residual, hypersensitive to the subtracted baseline

The Δ_λ A=3 magnitude gate is a "1.6× gap": the derived 3-body cluster `c₃ = 0.297 MeV = 0.63·μ₃`
(`BorromeanMagnitudeLift`, #4364), where the TARGET is the 3-body simplex coefficient of the
graded-subtracted residual (`AdditiveResidualSimplex`, #4320):

```
M(A) = ρ_strong(A) − ρ_grad(A),   ρ_grad(A) = ∏_{k=3}^{A} [k]_q   (graded coinvariant dim, #4300)
μ₂ = M(2) = 0                     (deuteron self-reference, DERIVED)
μ₃ = M(3) − 3·μ₂ = M(3) = ρ_strong(3) − ρ_grad(3) ≈ +0.4708.
```

`μ₃ ≈ 0.47` is a **small residual = the difference of two O(3.5) numbers** (`ρ_strong(3)≈3.81`,
`ρ_grad(3)≈3.34`). This is the same structure that made `g₂ = 1 + r` frame-flattered
(`BindingResidualAmplification`, #4319 thread): a small difference of large numbers inherits an
*amplified* sensitivity to any convention that shifts the subtracted baseline. This file machine-checks
that fragility and the sign-robustness that survives it — sign facts and an amplification inequality,
no magnitude derivation, nothing wired.

Companion probe `computations/deltalambda/mu3_target_frame_robustness_probe.py` measures the
baseline-class spread of μ₃ (1.73×, across graded / quantum / classical A-scalings) — which *exceeds*
the 1.585× gap — while the signs (μ₃>0, μ₄<0) stay robust. The numeric `ℝ` facts below consume that
probe's reported values; the generic amplification lemma is baseline-independent.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Data.Real.Basic

namespace QOU.MassTheory.Mu3BaselineFragility

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The graded-subtracted residual as a function of the subtracted baseline `G`
(the strong ratio `S = ρ_strong(A)` is fixed data): `resid S G = S − G`. -/
def resid (S G : R) : R := S - G

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **The simplex re-expression adds no robustness.** With the deuteron self-reference forcing
`μ₂ = M(2) = 0`, the 3-body simplex coefficient `μ₃ = M3 − 3·μ₂` equals the raw A=3 residual `M3`
*exactly* — so μ₃ inherits ALL of the residual's baseline sensitivity; expanding in the simplex basis
does not stabilize the target. -/
theorem mu3_eq_M3 (M3 mu2 : R) (h : mu2 = 0) : M3 - 3 * mu2 = M3 := by
  subst h; ring

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **The residual moves by exactly the baseline shift** (unit absolute gain, opposite sign):
shifting `ρ_grad ↦ ρ_grad + d` moves the residual by `−d`. There is no attenuation — every bit of
baseline error passes straight into the target. -/
theorem resid_shift (S G d : R) : resid S (G + d) - resid S G = -d := by
  unfold resid; ring

/-- **Relative amplification exceeds unity when the residual is smaller than its baseline.**
If the residual `r = S − G` satisfies `0 < r < G`, then `1 < G / r`: a *relative* baseline error is
magnified by the factor `G/r > 1` in the residual. (`resid_shift` gives the absolute unit gain; this
converts it to the relative gain `G/r`.) For μ₃ this is `ρ_grad(3)/μ₃ ≈ 7`. -/
theorem residual_amplifies {r G : R} (hr : 0 < r) (hrG : r < G) : 1 < G / r :=
  (one_lt_div hr).mpr hrG

/-- **Corpus amplification `> 7`.** At the reported corpus values `ρ_grad(3) ≈ 3.342031`,
`μ₃ ≈ 0.4708`, the amplification `ρ_grad(3)/μ₃ > 7`: a 1% error in the subtracted baseline moves μ₃ by
more than 7%. (Consumes the witness numbers; an arithmetic fact about the reported target.) -/
theorem corpus_amplification_gt_seven : (3.342031 : ℝ) / 0.4708 > 7 := by norm_num

/-- **μ₃ sign is robust** (positive) across the three deuteron-normalized A-scaling baselines
G (graded), Q (quantum), C (classical) — reported μ₃ values `0.4708, 0.7691, 0.8128`. -/
theorem mu3_positive_all_baselines :
    (0.4708 : ℝ) > 0 ∧ (0.7691 : ℝ) > 0 ∧ (0.8128 : ℝ) > 0 := by norm_num

/-- **μ₄ sign is robust** (negative) across the three baselines — reported μ₄ values
`−4.591, −2.554, −2.220`. Together with `mu3_positive_all_baselines`, the SIGN structure
(μ₃>0, μ₄<0) survives the baseline change even though the magnitudes do not. -/
theorem mu4_negative_all_baselines :
    (-4.591 : ℝ) < 0 ∧ (-2.554 : ℝ) < 0 ∧ (-2.220 : ℝ) < 0 := by norm_num

/-- **The μ₃ baseline-class spread exceeds the gap it targets.** The magnitude spread
`μ₃^max / μ₃^min = 0.8128 / 0.4708 ≈ 1.73` exceeds the `1.585×` gap the closure attempts aim to close
(`0.8128 > 1.585 · 0.4708`). Hence the target's own convention-spread is larger than the gap:
the "1.6× A=3 magnitude gap" is baseline-CLASS-relative, not absolute. -/
theorem spread_exceeds_gap : (0.8128 : ℝ) > 1.585 * 0.4708 := by norm_num

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **Framing amplification identity.** The single absolute miss `Δ` of the model against the physical
ratio, expressed as a fraction of the small residual `μ` (the "1.6× gap") versus the full physical ratio
`ρ` (the frame-independent accuracy), differ by exactly the factor `ρ/μ`:
`(Δ/μ) / (Δ/ρ) = ρ/μ`. The alarming multiplicative gap is the modest physical miss magnified by
`ρ/μ ≈ 8`. -/
theorem framing_amplification (Δ μ ρ : R) (hμ : μ ≠ 0) (hρ : ρ ≠ 0) (hΔ : Δ ≠ 0) :
    (Δ / μ) / (Δ / ρ) = ρ / μ := by
  field_simp

/-- **Physical accuracy is modest.** At the corpus values the miss on the physical ratio
`B(³H)/B(²H)` is `Δ/ρ = 0.1737689/3.8128 < 5%` — the frame-independent A=3 accuracy statement. -/
theorem physical_miss_lt_five_pct : (0.17376892 : ℝ) / 3.8128 < 0.05 := by norm_num

/-- **The residual framing is large** (`Δ/μ₃ > 36%`, model reaches `0.63·μ₃`) — the same miss, `≈8×`
magnified by the small-residual denominator (`physical_miss_lt_five_pct` vs this). -/
theorem residual_framing_gt_36_pct : (0.17376892 : ℝ) / 0.4708 > 0.36 := by norm_num

/-- **Capstone.** The A=3 magnitude target is a small residual (`μ₃ = M3` exactly, `mu3_eq_M3`) whose
relative sensitivity to the subtracted baseline exceeds unity (`residual_amplifies`) — numerically `>7`
(`corpus_amplification_gt_seven`) — so its magnitude is baseline-class-relative
(`spread_exceeds_gap`), while its sign is robust (`mu3_positive_all_baselines`,
`mu4_negative_all_baselines`). scope-(a): a fragility/robustness structure, NOT a magnitude derivation
and NOT a refutation of the principled graded-dimension baseline; nothing wired. -/
theorem a3_target_fragile_but_sign_robust :
    ((3.342031 : ℝ) / 0.4708 > 7) ∧ ((0.8128 : ℝ) > 1.585 * 0.4708) ∧
    ((0.4708 : ℝ) > 0 ∧ (-4.591 : ℝ) < 0) :=
  ⟨corpus_amplification_gt_seven, spread_exceeds_gap,
   ⟨by norm_num, by norm_num⟩⟩

end QOU.MassTheory.Mu3BaselineFragility
