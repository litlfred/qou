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
    (7.0739 MeV) and dips at ⁶Li (5.3323 MeV).

`no_constant_scale_matches_of_mono` below is the exclusion those two facts feed:
a model non-decreasing across two points, times ANY non-negative constant, stays
non-decreasing across them, so it cannot equal data that decreases there.  The
failure is in the SHAPE, not the normalisation — which is why it survives an
arbitrary overall rescaling on top of `w`, and excludes the whole two-parameter
family at once.

`best_constant_error_lower_bound` is the quantitative form: given the spread of
the per-isotope required rescalings, every constant misses by at least the
square root of that spread.  Instantiated at the measured spread
(`rmin = 0.5130070` at ²H, `rmax = 2.3770636` at ⁴He),
`measured_constant_error_at_least_two` gives a floor of 2× — the probe's dense
figure is 2.1526×.

WHAT IS NOT PROVED.  That `S(k)/k` is monotone for ALL `k`: it is measured
monotone on `1..64`, which is all the light isotopes reach, and it enters here
as a hypothesis (`hg`), not as a theorem.  Nor is anything here a claim about
what the missing binding term IS — only that this one-parameter family is not
it.  The numbers in `measured_constant_error_at_least_two` are measured inputs
carried in as literals, not derived in Lean.

This file is deliberately over `ℝ` (AGENTS.md §7c): it compares model to
measurement, needs an ordering and `Real.sqrt`, and so belongs on the
archimedean side of the wall.

@module QOU.MassTheory.GrowingWidthCutShapeExclusion
-/

import Mathlib.Analysis.SpecialFunctions.Sqrt
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

/-- The geometric mean never exceeds the max. -/
theorem sqrt_mul_le_max {x y : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) :
    Real.sqrt (x * y) ≤ max x y := by
  have hm : 0 ≤ max x y := le_trans hx (le_max_left x y)
  have h : x * y ≤ max x y * max x y :=
    mul_le_mul (le_max_left x y) (le_max_right x y) hy hm
  calc Real.sqrt (x * y) ≤ Real.sqrt (max x y * max x y) := Real.sqrt_le_sqrt h
    _ = max x y := Real.sqrt_mul_self hm

/-- **The quantitative form.**  If the per-isotope rescalings that would be
required span `[rmin, rmax]`, then for EVERY positive constant `c` the worst
multiplicative error is at least `√(rmax / rmin)`.

`rmax / c` is how far the constant undershoots the isotope needing the most;
`c / rmin` how far it overshoots the one needing the least.  No `c` escapes
both. -/
theorem best_constant_error_lower_bound
    {rmin rmax c : ℝ} (hmin : 0 < rmin) (hle : rmin ≤ rmax) (hc : 0 < c) :
    Real.sqrt (rmax / rmin) ≤ max (rmax / c) (c / rmin) := by
  have hrmax : 0 < rmax := lt_of_lt_of_le hmin hle
  have h := sqrt_mul_le_max (le_of_lt (div_pos hrmax hc)) (le_of_lt (div_pos hc hmin))
  have e : (rmax / c) * (c / rmin) = rmax / rmin := by
    field_simp
  rwa [e] at h

/-- **Instantiated at the measured spread.**  With `rmin = 0.5130070` (²H) and
`rmax = 2.3770636` (⁴He) — the rescalings the balanced cut `w = 3/2` would need
— every constant is off by at least a factor of two somewhere.  The probe's
dense value is 2.1526×; two is the floor this bound certifies.

The two literals are measured inputs, not Lean-derived. -/
theorem measured_constant_error_at_least_two
    {c : ℝ} (hc : 0 < c) :
    (2 : ℝ) ≤ max ((23770636 : ℝ) / 10000000 / c) (c / ((5130070 : ℝ) / 10000000)) := by
  have hmin : (0 : ℝ) < (5130070 : ℝ) / 10000000 := by norm_num
  have hle : (5130070 : ℝ) / 10000000 ≤ (23770636 : ℝ) / 10000000 := by norm_num
  have hb := best_constant_error_lower_bound hmin hle hc
  have h2 : (2 : ℝ) ≤ Real.sqrt ((23770636 : ℝ) / 10000000 / ((5130070 : ℝ) / 10000000)) := by
    rw [show ((23770636 : ℝ) / 10000000 / ((5130070 : ℝ) / 10000000))
          = (23770636 : ℝ) / 5130070 by ring_nf]
    rw [show (2 : ℝ) = Real.sqrt 4 by
      rw [show (4 : ℝ) = 2 * 2 by norm_num, Real.sqrt_mul_self (by norm_num)]]
    exact Real.sqrt_le_sqrt (by norm_num)
  exact le_trans h2 hb

end QOU.MassTheory
