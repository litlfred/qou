import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# QOU.MathlibExt.CoshCosSeparation — `cosh` and `cos` ratios land on opposite sides of `1`

## What this is for

`docs/canonical-derivation-cheat-sheet.md` §5 records the categorical Weinberg-angle
identity

    `P_W / P_Z = cosh(5 η₀) / cosh(7 η₀) = 0.890836`   against   `cos θ_W = 0.8814`,

a `+1.07 %` deviation, and until 2026-08-30 explained that deviation as *"the
cosh-vs-cos discrepancy"* — the idea being that `q₀` is close enough to `1` that the
hyperbolic ratio is a small perturbation of the trigonometric one.

**That explanation is false, and this file is the reason stated as a theorem rather
than as arithmetic at one point.** For *every* admissible `η` — not just the substrate
value — the two ratios sit on **opposite sides of `1`**:

    `cosh(aη)/cosh(bη) < 1 < cos(aη)/cos(bη)`     for `0 < aη < bη < π/2`.

So swapping `cosh` for `cos` does not perturb the answer by a percent; it moves it
across `1`, in the direction *away* from the SM value `0.8814 < 1`. A residual below
`1` cannot be "the cost of using `cosh`", because `cos` is worse. Measured at the
substrate point, the `cosh ↔ cos` difference is `30.6 %`, against the `1.07 %` being
explained.

The mechanism is the sign of the quadratic term: `cosh x = 1 + x²/2 + …` and
`cos x = 1 − x²/2 + …` disagree at *second* order, so their difference **grows** like
`x²` instead of shrinking. `cos_le_one_le_cosh` below is that fact in the form Mathlib
supports directly.

## What is deliberately not here

The specific decimals — `0.890836`, `1.163849`, `30.6 %`, the `5.11 %` shift in `η₀`
that would make the `cosh` form exact — are numerics at one point, checked at 30
digits with `mpmath`. They are not restated here as Lean theorems: proving a decimal
expansion of `cosh` at a substrate constant needs interval arithmetic and would add no
confidence to the claim that actually does the work, which is the *structural*
separation below. That one holds for the whole admissible range and is what makes the
refutation independent of the value of `q₀`.

Archimedean (ℝ).
-/

namespace QOU.MathlibExt

open Real

/-- A ratio of `cosh` at increasing nonnegative arguments is below `1`.

Stated with `|a| < |b|` because that is the form `Real.cosh_lt_cosh` takes — `cosh` is
even, so it is the magnitudes that order it. -/
theorem cosh_div_cosh_lt_one {a b : ℝ} (hab : |a| < |b|) :
    Real.cosh a / Real.cosh b < 1 := by
  rw [div_lt_one (Real.cosh_pos b)]
  exact Real.cosh_lt_cosh.mpr hab

/-- A ratio of `cos` at increasing arguments in `[0, π/2)` is above `1`.

The hypothesis `b < π/2` is what keeps the denominator positive; past `π/2` the ratio
changes sign and the statement is not the interesting one. -/
theorem one_lt_cos_div_cos {a b : ℝ} (ha : 0 ≤ a) (hab : a < b) (hb : b < π / 2) :
    1 < Real.cos a / Real.cos b := by
  have hpi : 0 < π := Real.pi_pos
  have hcosb : 0 < Real.cos b :=
    Real.cos_pos_of_mem_Ioo ⟨by linarith, hb⟩
  rw [lt_div_iff₀ hcosb, one_mul]
  exact Real.cos_lt_cos_of_nonneg_of_le_pi ha (by linarith) hab

/-- **The separation.** For any two arguments strictly inside `(0, π/2)`, the
hyperbolic ratio is below `1` and the trigonometric ratio is above it.

This is the statement that refutes reading a sub-percent residual as "the cosh-vs-cos
discrepancy": the two forms are not near each other, they are on opposite sides of
`1`, uniformly in the parameter. -/
theorem cosh_div_lt_one_lt_cos_div {a b : ℝ} (ha : 0 < a) (hab : a < b) (hb : b < π / 2) :
    Real.cosh a / Real.cosh b < 1 ∧ 1 < Real.cos a / Real.cos b := by
  refine ⟨cosh_div_cosh_lt_one ?_, one_lt_cos_div_cos ha.le hab hb⟩
  rw [abs_of_pos ha, abs_of_pos (ha.trans hab)]
  exact hab

/-- The scaled form, as the cheat sheet uses it: with integer channel indices `p < r`
and a positive substrate parameter `η` small enough that `r·η` stays inside `(0, π/2)`,
the two candidate readings of the same ratio bracket `1`. -/
theorem cosh_div_lt_one_lt_cos_div_scaled {p r η : ℝ}
    (hη : 0 < η) (hp : 0 < p) (hpr : p < r) (hr : r * η < π / 2) :
    Real.cosh (p * η) / Real.cosh (r * η) < 1
      ∧ 1 < Real.cos (p * η) / Real.cos (r * η) :=
  cosh_div_lt_one_lt_cos_div (mul_pos hp hη)
    (by exact (mul_lt_mul_of_pos_right hpr hη)) hr

/-- `cos x ≤ 1 ≤ cosh x`, the sign asymmetry the separation rests on: the quadratic
term enters `cosh` with `+` and `cos` with `−`, so `1` always sits between them. -/
theorem cos_le_one_le_cosh (x : ℝ) : Real.cos x ≤ 1 ∧ 1 ≤ Real.cosh x :=
  ⟨Real.cos_le_one x, Real.one_le_cosh x⟩

end QOU.MathlibExt
