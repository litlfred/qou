/-
# The complex dilogarithm `Li₂ : ℂ → ℂ` — the Mathlib gap, filled on the disc

**Mathlib has no polylogarithm at all** (checked 2026-08-06: no `Polylog`, no
`dilog`, no `Real.dilog`). QOU already carries a *real* one —
`QOU.QPochhammer.LiTwo : ℝ → ℝ` with `LiTwo_reflection'` proved sorry-free on
`(0,1)` — but the 5₂ saddle sum rule needs `Li₂` at **complex** arguments, and
that is what this file starts.

## Why the complex case is needed

The three roots of the 5₂ saddle cubic `y³ − 2y² + 3y − 1` are

    y₃ = 0.4301597…          real, in (0,1)   — covered by the real `LiTwo`
    y₁ = 0.78492 + 1.30714i  complex, |y₁| = 1.52 > 1
    y₂ = conj y₁

so exactly one of the three is in reach of the existing real theory. See bean
`qou-ph1k`.

## Scope of THIS file — honest

Defines `cLiTwo` by its defining power series and proves exactly three things,
all sorry-free:

* `cLiTwo_zero` — the value at the origin;
* `cLiTwo_term_norm_le` — the term bound `‖zᵏ⁺¹/(k+1)²‖ ≤ ‖z‖ᵏ⁺¹`;
* `cLiTwo_summable` — convergence on the **open unit disc**.

That is the whole of it. This is a foundation, not a usable dilogarithm yet.

It does **not** provide:

* agreement with the real `QOU.QPochhammer.LiTwo` on ℝ (deliberately: that
  import would tie this file to QOU and defeat the upstreaming goal below);
* analytic continuation past `|z| = 1` — needed for `y₁` (`|y₁| = 1.52`);
* the complex Euler reflection `Li₂ z + Li₂ (1−z) = π²/6 − log z · log(1−z)`;
* the inversion formula `Li₂ z + Li₂ (1/z) = −π²/6 − ½·log(−z)²`, the standard
  route to `|z| > 1`.

**None of those is stubbed** — no `sorry`, no `True`-valued placeholder, no
axiom. The file asserts only what it proves. Remaining work: `qou-ph1k`.

In particular this does **not** yet discharge `hrefl` in
`QOU.QBeta.FiveTwo.sum_reflection_of_branch`; the reflection identity is the
next brick, and it needs the continuation first.

## Upstreaming

This is deliberately written in Mathlib style (series definition, `Summable`
lemmas, no QOU-specific dependencies beyond Mathlib itself) so it can be
offered upstream once the continuation and reflection land. Upstreaming is
premature until then and has no bean of its own; it is recorded as a follow-on
inside `qou-gkco`. (An earlier revision of this line cited a bean `qou-mlib`
that was never created — corrected 2026-08-06.)

-- Ref: [manuscript] bean qou-ph1k; docs/coordination/1ppq-qbeta.md 2026-08-02
-- Ref: [lewin1981] Polylogarithms and Associated Functions, L. Lewin
-/
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Analysis.Analytic.OfScalars
import Mathlib.Analysis.Analytic.Basic
import Mathlib.Analysis.Analytic.ChangeOrigin

namespace QOU.MathlibExt

open Complex

/-- The complex dilogarithm as its defining power series,
`Li₂ z = ∑_{k ≥ 0} z^(k+1)/(k+1)²`.

Indexed from `k = 0` with numerator `z^(k+1)` so the `k`-th term is
`z^(k+1)/(k+1)²`, matching `QOU.QPochhammer.LiTwo` term by term. Outside the
closed unit disc the `tsum` is `0` by Mathlib's junk-value convention; the
lemmas below are all guarded by a disc hypothesis. -/
noncomputable def cLiTwo (z : ℂ) : ℂ :=
  ∑' k : ℕ, z ^ (k + 1) / ((k : ℂ) + 1) ^ 2

@[simp] theorem cLiTwo_zero : cLiTwo 0 = 0 := by
  unfold cLiTwo
  simp

/-- Each term is dominated by `‖z‖^(k+1)`, since `1/(k+1)² ≤ 1`. -/
theorem cLiTwo_term_norm_le (z : ℂ) (k : ℕ) :
    ‖z ^ (k + 1) / ((k : ℂ) + 1) ^ 2‖ ≤ ‖z‖ ^ (k + 1) := by
  have hk : (1 : ℝ) ≤ ‖((k : ℂ) + 1) ^ 2‖ := by
    have : ((k : ℂ) + 1) = ((k + 1 : ℕ) : ℂ) := by push_cast; ring
    rw [this, ← Nat.cast_pow, Complex.norm_natCast]
    exact_mod_cast Nat.one_le_iff_ne_zero.mpr (by positivity)
  rw [norm_div, norm_pow]
  calc ‖z‖ ^ (k + 1) / ‖((k : ℂ) + 1) ^ 2‖
      ≤ ‖z‖ ^ (k + 1) / 1 := by gcongr
      _ = ‖z‖ ^ (k + 1) := by ring

/-- The defining series converges on the open unit disc. -/
theorem cLiTwo_summable {z : ℂ} (hz : ‖z‖ < 1) :
    Summable fun k : ℕ => z ^ (k + 1) / ((k : ℂ) + 1) ^ 2 := by
  refine Summable.of_norm_bounded (g := fun k : ℕ => ‖z‖ ^ (k + 1)) ?_ ?_
  · exact (summable_geometric_of_lt_one (norm_nonneg z) hz).mul_left ‖z‖ |>.congr
      fun k => by rw [pow_succ']
  · intro k
    exact cLiTwo_term_norm_le z k

/-! ### Standard power-series indexing

`cLiTwo` is written `∑' k, z^(k+1)/(k+1)²` so that it matches
`QOU.QPochhammer.LiTwo` term by term (which is what makes `cLiTwo_ofReal`
unconditional). Mathlib's power-series machinery — `FormalMultilinearSeries.
ofScalars`, whose sum is `∑' n, cₙ • xⁿ` — wants the other indexing.

Rather than redefine `cLiTwo` and break the bridge, the two indexings are
reconciled here. This is step 1 of the analyticity route recorded in bean
`qou-gkco`; steps 2–3 (radius `= 1`, hence `AnalyticOnNhd` on the disc) are
not done. -/

/-- The coefficients of `Li₂` in standard indexing: `c₀ = 0`, `cₙ = 1/n²`. -/
noncomputable def cLiTwoCoeff (n : ℕ) : ℂ := if n = 0 then 0 else ((n : ℂ) ^ 2)⁻¹

@[simp] theorem cLiTwoCoeff_zero : cLiTwoCoeff 0 = 0 := by simp [cLiTwoCoeff]

theorem cLiTwoCoeff_succ (k : ℕ) :
    cLiTwoCoeff (k + 1) = (((k : ℂ) + 1) ^ 2)⁻¹ := by
  simp only [cLiTwoCoeff, Nat.succ_ne_zero, if_false]
  push_cast
  ring_nf

/-- The standard-indexed series is summable on the open unit disc. -/
theorem cLiTwoCoeff_summable {z : ℂ} (hz : ‖z‖ < 1) :
    Summable fun n : ℕ => cLiTwoCoeff n * z ^ n := by
  refine Summable.of_norm_bounded (g := fun n : ℕ => ‖z‖ ^ n) ?_ ?_
  · exact summable_geometric_of_lt_one (norm_nonneg z) hz
  · intro n
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · simp
    · have hk : (1 : ℝ) ≤ ‖(n : ℂ)‖ ^ 2 := by
        rw [Complex.norm_natCast]
        have h1 : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
        nlinarith
      simp only [cLiTwoCoeff, hn.ne', if_false, norm_mul, norm_inv, norm_pow]
      calc (‖(n : ℂ)‖ ^ 2)⁻¹ * ‖z‖ ^ n
          ≤ 1 * ‖z‖ ^ n := by
            gcongr
            exact inv_le_one_of_one_le₀ hk
        _ = ‖z‖ ^ n := one_mul _

/-- **The two indexings agree.** `cLiTwo z = ∑' n, cₙ zⁿ` with `c` as above. -/
theorem cLiTwo_eq_tsum_coeff {z : ℂ} (hz : ‖z‖ < 1) :
    cLiTwo z = ∑' n : ℕ, cLiTwoCoeff n * z ^ n := by
  rw [(cLiTwoCoeff_summable hz).tsum_eq_zero_add]
  simp only [cLiTwoCoeff_zero, zero_mul, zero_add, cLiTwoCoeff_succ]
  unfold cLiTwo
  refine tsum_congr fun k => ?_
  rw [div_eq_inv_mul]

/-- Every coefficient has norm `≤ 1`: `c₀ = 0` and `‖1/n²‖ = 1/n² ≤ 1`. -/
theorem cLiTwoCoeff_norm_le_one (n : ℕ) : ‖cLiTwoCoeff n‖ ≤ 1 := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  · have h1 : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
    have hk : (1 : ℝ) ≤ ‖(n : ℂ)‖ ^ 2 := by
      rw [Complex.norm_natCast]; nlinarith
    simp only [cLiTwoCoeff, hn.ne', if_false, norm_inv, norm_pow]
    exact inv_le_one_of_one_le₀ hk

/-- **Step 2 of the analyticity route (bean `qou-gkco`): radius `≥ 1`.**

Immediate from `cLiTwoCoeff_norm_le_one` via `le_radius_of_bound` at `r = 1`,
with no ratio test needed. Combined with `cLiTwo_eq_tsum_coeff`, this says the
defining series of `cLiTwo` is a genuine power series on the open unit disc.

Step 3 — upgrading this to `AnalyticOnNhd ℂ cLiTwo (Metric.ball 0 1)`, which
is what the identity theorem needs — is **not** done here. -/
theorem cLiTwo_radius_ge_one :
    1 ≤ (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).radius := by
  have h : ∀ n : ℕ,
      ‖FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff n‖ * ((1 : NNReal) : ℝ) ^ n ≤ 1 := by
    intro n
    rw [FormalMultilinearSeries.ofScalars_norm]
    simpa using cLiTwoCoeff_norm_le_one n
  simpa using FormalMultilinearSeries.le_radius_of_bound _ 1 h

/-- **Step 3: `cLiTwo` is represented by its power series on the unit ball.** -/
theorem cLiTwo_hasFPowerSeriesOnBall :
    HasFPowerSeriesOnBall cLiTwo
      (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff) 0 1 := by
  have hrad : 0 < (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).radius :=
    lt_of_lt_of_le (by norm_num) cLiTwo_radius_ge_one
  refine (((FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).hasFPowerSeriesOnBall
    hrad).mono (by norm_num) cLiTwo_radius_ge_one).congr ?_
  intro z hz
  rw [mem_emetric_ball_zero_iff] at hz
  have hz' : ‖z‖ < 1 := by
    rw [show (1 : ENNReal) = ((1 : NNReal) : ENNReal) by simp, enorm_lt_coe] at hz
    exact_mod_cast hz
  have hsum : (FormalMultilinearSeries.ofScalars ℂ cLiTwoCoeff).sum z
      = ∑' n : ℕ, cLiTwoCoeff n * z ^ n := by
    simpa [smul_eq_mul] using
      congrFun (FormalMultilinearSeries.ofScalarsSum_eq_tsum cLiTwoCoeff) z
  rw [hsum, ← cLiTwo_eq_tsum_coeff hz']

/-- **`cLiTwo` is analytic on the open unit disc.**

The hypothesis the identity theorem needs. With
`QOU.Archimedean.cLiTwo_reflection_ofReal` (the reflection identity already
proved on the real segment `(0,1)` — a set with an accumulation point), this is
what would give the complex reflection identity on the disc. That continuation
step is **not** taken here; extending past `|z| = 1` needs the inversion
formula on top. Bean `qou-gkco`. -/
theorem cLiTwo_analyticOnNhd :
    AnalyticOnNhd ℂ cLiTwo (EMetric.ball (0 : ℂ) 1) :=
  cLiTwo_hasFPowerSeriesOnBall.analyticOnNhd

end QOU.MathlibExt
