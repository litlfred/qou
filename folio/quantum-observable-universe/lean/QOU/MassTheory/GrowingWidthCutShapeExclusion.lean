/-
GrowingWidthCutShapeExclusion.lean — a monotone model cannot reproduce a
non-monotone target, and no rescaling repairs it.  The quantitative form gives
the floor on how badly any single constant must miss.

WHAT THIS IS FOR.  Addendum 23 Front 1 proposed a cut of width `w·A` across the
`3A`-strand atom word and measured its entropy `S(k)`, leaving the front open
with the verdict *"`w` is a free parameter, and that is the whole problem"*.
The probe
`computations/meson/growing_width_cut_shape_exclusion_probe.py` measures the two
facts that close it without choosing any `w`:

  * `S(k)/k` is strictly increasing over `k = 1..64`, so for every fixed `w` the
    model's per-nucleon prediction `g_w(A) = E₀·S(⌊wA⌋)/A` is non-decreasing in
    `A` (verified for 581 values of `w` across `[0.10, 3.00]`);
  * the AME per-nucleon binding is NOT non-decreasing — it peaks at ⁴He
    and dips at ⁶Li (the AME values are in the probe and in
    `QOU.Observations.GrowingWidthCutMeasuredSpread`).

`no_constant_scale_matches_of_mono` below is the exclusion those two facts feed:
a model non-decreasing across two points, times ANY non-negative constant, stays
non-decreasing across them, so it cannot equal data that decreases there.  The
failure is in the SHAPE, not the normalisation — which is why it survives an
arbitrary overall rescaling on top of `w`, and excludes the whole two-parameter
family at once.

`best_constant_error_lower_bound_of_sq` is the quantitative form: given the spread
of the per-isotope required rescalings, every constant misses by at least the
square root of that spread, and `constant_error_at_least_two_of_four_le` gives the
factor-two floor whenever the spread is at least four. The measured spread and its
instantiation live in the comparison layer,
`QOU.Observations.GrowingWidthCutMeasuredSpread`.

WHAT IS NOT PROVED.  That `S(k)/k` is monotone for ALL `k`: it is measured
monotone on `1..64`, which is all the light isotopes reach, and it enters here
as a hypothesis (`hg`), not as a theorem.  Nor is anything here a claim about
what the missing binding term IS — only that this one-parameter family is not
it.  No measured value enters this file.

This file is over `ℝ` (AGENTS.md §7c): it compares model to measurement and
needs an ordering. The square root is a ring symbol `s` with `0 ≤ s` and
`s² = x` (bean `qou-dk7p`); the `Real.sqrt` forms, under their original names,
are in `QOU/Transcendental/MassTheory/GrowingWidthCutShapeExclusionReal.lean`.

@module QOU.MassTheory.GrowingWidthCutShapeExclusion
-/

import Mathlib.Data.Real.Basic
import Mathlib.Order.MinMax
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

set_option autoImplicit false

namespace QOU.MassTheory

/-- **The exclusion.**  A model that does not decrease across two points cannot,
after any non-negative rescaling, reproduce data that does decrease across them.

`g₁, g₂` are the model's per-nucleon values at ⁴He and ⁶Li; `b₁, b₂` the AME
ones; `c` an arbitrary overall scale.  The hypothesis `hg : g₁ ≤ g₂` is what the
probe verifies for every `w`, and `hb : b₂ < b₁` is the ⁴He peak. -/
theorem no_constant_scale_matches_of_mono
    (g₁ g₂ b₁ b₂ c : ℝ) (hg : g₁ ≤ g₂) (hc : 0 ≤ c)
    (hb : b₂ < b₁) (h₁ : c * g₁ = b₁) (h₂ : c * g₂ = b₂) : False := by
  have hmul : c * g₁ ≤ c * g₂ := mul_le_mul_of_nonneg_left hg hc
  rw [h₁, h₂] at hmul
  linarith

/-- **Non-vacuity I.**  The conclusion is not forced by the shape of the
hypotheses: drop only `hb` (let the data be non-decreasing too) and matching
becomes possible.  So the theorem really is about the ⁴He peak. -/
theorem matching_possible_when_data_nondecreasing :
    ∃ g₁ g₂ b₁ b₂ c : ℝ, g₁ ≤ g₂ ∧ 0 ≤ c ∧ b₁ ≤ b₂ ∧ c * g₁ = b₁ ∧ c * g₂ = b₂ :=
  ⟨1, 2, 1, 2, 1, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- **Non-vacuity II.**  The monotonicity hypothesis is load-bearing, not
decorative: a model that DOES decrease across the two points matches the same
decreasing data exactly.  This is why the probe must verify `hg` for every `w`
rather than assume it. -/
theorem mono_hypothesis_is_load_bearing :
    ∃ g₁ g₂ b₁ b₂ c : ℝ,
      ¬ (g₁ ≤ g₂) ∧ 0 ≤ c ∧ b₂ < b₁ ∧ c * g₁ = b₁ ∧ c * g₂ = b₂ :=
  ⟨2, 1, 2, 1, 1, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- The geometric mean never exceeds the max: any `s ≥ 0` with `s² = x·y` is at
most `max x y`. -/
theorem le_max_of_sq_eq_mul {x y s : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) (hs : 0 ≤ s)
    (hs2 : s ^ 2 = x * y) : s ≤ max x y := by
  have hm : 0 ≤ max x y := le_trans hx (le_max_left x y)
  have h : x * y ≤ max x y * max x y :=
    mul_le_mul (le_max_left x y) (le_max_right x y) hy hm
  nlinarith

/-- **The quantitative form.**  If the per-isotope rescalings that would be
required span `[rmin, rmax]`, then for EVERY positive constant `c` the worst
multiplicative error is at least `√(rmax / rmin)`, the symbol `s ≥ 0` with
`s² = rmax / rmin`.

`rmax / c` is how far the constant undershoots the isotope needing the most;
`c / rmin` how far it overshoots the one needing the least.  No `c` escapes
both. -/
theorem best_constant_error_lower_bound_of_sq
    {rmin rmax c s : ℝ} (hmin : 0 < rmin) (hle : rmin ≤ rmax) (hc : 0 < c)
    (hs : 0 ≤ s) (hs2 : s ^ 2 = rmax / rmin) :
    s ≤ max (rmax / c) (c / rmin) := by
  have hrmax : 0 < rmax := lt_of_lt_of_le hmin hle
  have e : (rmax / c) * (c / rmin) = rmax / rmin := by
    field_simp
  exact le_max_of_sq_eq_mul (le_of_lt (div_pos hrmax hc)) (le_of_lt (div_pos hc hmin)) hs
    (hs2.trans e.symm)

/-- **The factor-two floor from a spread of at least four.**  If the required
rescalings span `[rmin, rmax]` with `4·rmin ≤ rmax`, every positive constant `c` is off
by at least a factor of two somewhere. No square root is needed: if both ratios were
below `2`, their product `rmax/rmin` would be below `4`.

This file carries no measured values. The instantiation at the measured spread is in
`QOU.Observations.GrowingWidthCutMeasuredSpread`, the comparison layer. -/
theorem constant_error_at_least_two_of_four_le
    {rmin rmax c : ℝ} (hmin : 0 < rmin) (h4 : 4 * rmin ≤ rmax) (hc : 0 < c) :
    (2 : ℝ) ≤ max (rmax / c) (c / rmin) := by
  by_contra hlt
  push_neg at hlt
  have h1 : rmax / c < 2 := lt_of_le_of_lt (le_max_left _ _) hlt
  have h2 : c / rmin < 2 := lt_of_le_of_lt (le_max_right _ _) hlt
  rw [div_lt_iff₀ hc] at h1
  rw [div_lt_iff₀ hmin] at h2
  nlinarith

end QOU.MassTheory
