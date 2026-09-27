import QOU.SchurWeyl.GenericParameter
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Ring.Abs

/-!
# QOU.SchurWeyl.GenericParameterReal — over `ℝ` the generic hypothesis is free

Beans `qou-j377`, `qou-kwoa`.

`QOU/SchurWeyl/GenericParameter.lean` carries `NotRootOfUnity` over an arbitrary field.
This file carries the one statement that is **specific to `ℝ`** — and specific in the
strong sense: it is *false* over a general field, since a primitive cube root of unity
has `q ≠ 0` and `q ^ 2 ≠ 1` and `q ^ 3 = 1`.

That is exactly why the Wedderburn cone is `ℝ`-only.  `SeminormalRep.zpow_ne_one` gets
"`q` is not a root of unity" for free from `q ≠ 0 ∧ q ^ 2 ≠ 1` because the only real roots
of unity are `±1`; a general field affords no such shortcut and the criterion has to be
carried.  Keeping the two apart, per §7c, makes the boundary visible instead of leaving it
buried in a `Real.log` step three files away.

Because this direction is an *implication into* `NotRootOfUnity`, every `ℝ` statement in
the cone is the specialisation of a generic one — so generalising those files strengthens
no hypothesis and invalidates no downstream use.
-/

namespace QOU.SchurWeyl.GenericParameter

/-- **The bridge: over `ℝ` the hypothesis is free.**  `q ≠ 0` and `q ^ 2 ≠ 1` already give
it, because the only real roots of unity are `±1` — so every `ℝ`-statement in the
Wedderburn cone is the specialisation of a `NotRootOfUnity` statement, and generalising
those files weakens no hypothesis. -/
theorem ofSqNeOne {q : ℝ} (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) : NotRootOfUnity q := by
  intro m hm h
  -- `|q| ^ m = 1` with `|q| > 0` forces `|q| = 1`, hence `q ^ 2 = 1`.
  have habs : |q| ^ m = 1 := by rw [← abs_pow, h, abs_one]
  have habs0 : 0 < |q| := abs_pos.mpr hq0
  have habs1 : |q| = 1 := by
    rcases lt_trichotomy |q| 1 with hlt | heq | hgt
    · exact absurd habs (ne_of_lt (pow_lt_one₀ habs0.le hlt hm.ne'))
    · exact heq
    · exact absurd habs (ne_of_gt (one_lt_pow₀ hgt hm.ne'))
  exact hq2 (by rw [← sq_abs, habs1, one_pow])

end QOU.SchurWeyl.GenericParameter
