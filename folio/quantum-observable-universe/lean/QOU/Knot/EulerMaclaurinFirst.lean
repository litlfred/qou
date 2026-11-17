/-
# Mathlib-gap infra: the first Euler–Maclaurin correction (bean qou-shrp, step 2)

Mathlib has **no** Euler–Maclaurin formula.  The `qou-shrp` route to van der
Veen's `½` needs only its first correction, and only in the form that pins a
constant rather than one carrying an abstract modulus of continuity — so this
file proves the *monotone-derivative* version, which squeezes:

for `f` differentiable with **antitone** derivative on `[a, a+h]`,

    (h²/2)·f′(a+h)  ≤  ∫_a^{a+h} (f(a+h) − f(u)) du  ≤  (h²/2)·f′(a),

and, summed over the uniform grid `x_i = i·h`,

    (h²/2)·Σ_{i<n} f′(x_{i+1})  ≤  Σ_{i<n} ∫_{cell_i} (f(x_{i+1}) − f(u)) du
                                ≤  (h²/2)·Σ_{i<n} f′(x_i).

Both envelopes are `(h/2)` times a Riemann sum of `f′`, i.e. both converge to
`(h/2)·(f(nh) − f(0))` — the first Euler–Maclaurin term.  That is exactly the
`½` the antitone squeeze of `LogSineSmoothPart` could not pin (measured:
`computations/logsine_smooth_defect_constant.py`).

The proof needs no Fubini and no modulus bookkeeping: the mean value theorem
turns `f(a+h) − f(u)` into `(a+h−u)·f′(ξ)` with `ξ` in the cell, antitonicity
brackets `f′(ξ)` between the endpoint values, and `∫_a^{a+h} (a+h−u) du = h²/2`
does the rest.

Nothing here is QOU-specific; it is stated in Mathlib style for a general `f`
and is a candidate for upstreaming.  Authored under the owner's standing
authorisation to add Mathlib infrastructure rather than route around a gap.
-/

/-
**RETRACTION (2026-08-19) — this file did NOT close an infrastructure gap.**

Its header and the PR that landed it (#5297) said Mathlib has no
Euler-Maclaurin formula and that this is therefore a genuine gap.  Mathlib's
half is true.  The corpus half is false: `QOU/MathlibExt/CompositeEulerMaclaurin.lean`
has carried `abs_integral_sub_composite_le_osc` -- the **composite** rule, with
the `B_2` term and an `O(h^2)` oscillation error -- since 2026-08-10, nine days
before this file was written, alongside `TrapezoidRule.lean` and a worked
application to `logSinc` in `QOU/Knot/LogSincNearZero.lean`.

What survives: the bracket below needs only `f'` **antitone**, where the
composite rule needs a continuous `f''`.  That weaker hypothesis is a real
difference and is why the file is kept rather than deleted.  But for any
application where `f''` exists, prefer the composite rule -- it identifies the
`O(h)` coefficient as `h^2/12 * (f'(b) - f'(a))` where this file only bounds it,
and the bound here is exactly 6x loose.

Full account, including the root cause (the AGENTS.md corpus-grep checklist was
not run before declaring the gap):
`docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md`.
-/

import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

namespace QOU.Knot

open Real MeasureTheory

/-- The mean-value bracket for an antitone derivative: on `u ≤ b`,
    `(b−u)·f′(b) ≤ f b − f u ≤ (b−u)·f′(u)`. -/
theorem sub_bracket_of_antitoneOn_deriv {f f' : ℝ → ℝ} {a b u : ℝ}
    (hderiv : ∀ x ∈ Set.Icc a b, HasDerivAt f (f' x) x)
    (hanti : AntitoneOn f' (Set.Icc a b))
    (hau : a ≤ u) (hub : u ≤ b) :
    (b - u) * f' b ≤ f b - f u ∧ f b - f u ≤ (b - u) * f' u := by
  rcases eq_or_lt_of_le hub with rfl | hlt
  · simp
  · -- MVT on [u, b]
    have hsub : Set.Icc u b ⊆ Set.Icc a b := Set.Icc_subset_Icc hau le_rfl
    have hcont : ContinuousOn f (Set.Icc u b) := fun x hx =>
      ((hderiv x (hsub hx)).continuousAt).continuousWithinAt
    have hio : ∀ x ∈ Set.Ioo u b, HasDerivAt f (f' x) x := fun x hx =>
      hderiv x (hsub (Set.mem_Icc.mpr ⟨hx.1.le, hx.2.le⟩))
    obtain ⟨c, hc, hslope⟩ := exists_hasDerivAt_eq_slope f f' hlt hcont hio
    have hcmem : c ∈ Set.Icc a b :=
      ⟨le_trans hau hc.1.le, hc.2.le⟩
    have humem : u ∈ Set.Icc a b := ⟨hau, hub⟩
    have hbmem : b ∈ Set.Icc a b := ⟨le_trans hau hub, le_rfl⟩
    have hbu : (0:ℝ) < b - u := by linarith
    have hfc : f b - f u = (b - u) * f' c := by
      field_simp at hslope
      linarith [hslope]
    constructor
    · have : f' b ≤ f' c := hanti hcmem hbmem hc.2.le
      nlinarith [this, hbu]
    · have : f' c ≤ f' u := hanti humem hcmem hc.1.le
      nlinarith [this, hbu]

/-- `∫_a^{a+h} (a + h − u) du = h²/2`. -/
theorem integral_sub_linear (a h : ℝ) :
    (∫ u in a..(a + h), (a + h - u)) = h ^ 2 / 2 := by
  have h1 : (∫ u in a..(a + h), (a + h - u))
      = (∫ _u in a..(a + h), (a + h)) - ∫ u in a..(a + h), u := by
    rw [← intervalIntegral.integral_sub intervalIntegrable_const
      intervalIntegral.intervalIntegrable_id]
  rw [h1, intervalIntegral.integral_const, integral_id, smul_eq_mul]
  ring

/-- **First Euler–Maclaurin correction, per cell.**  For `f` with antitone
    derivative on the cell `[a, a+h]`, the right-endpoint defect is bracketed
    by `h²/2` times the endpoint derivatives. -/
theorem cell_defect_bracket {f f' : ℝ → ℝ} {a h : ℝ} (hh : 0 < h)
    (hderiv : ∀ x ∈ Set.Icc a (a + h), HasDerivAt f (f' x) x)
    (hanti : AntitoneOn f' (Set.Icc a (a + h))) :
    h ^ 2 / 2 * f' (a + h) ≤ (∫ u in a..(a + h), (f (a + h) - f u))
      ∧ (∫ u in a..(a + h), (f (a + h) - f u)) ≤ h ^ 2 / 2 * f' a := by
  have hab : a ≤ a + h := by linarith
  have hcont : ContinuousOn f (Set.Icc a (a + h)) := fun x hx =>
    ((hderiv x hx).continuousAt).continuousWithinAt
  have hc1 : IntervalIntegrable (fun _ : ℝ => f (a + h)) volume a (a + h) :=
    intervalIntegrable_const
  have hfint : IntervalIntegrable f volume a (a + h) := by
    rw [intervalIntegrable_iff_integrableOn_Icc_of_le hab]
    exact hcont.integrableOn_Icc
  have hint : IntervalIntegrable (fun u => f (a + h) - f u) volume a (a + h) :=
    hc1.sub hfint
  have hc2 : IntervalIntegrable (fun _ : ℝ => a + h) volume a (a + h) :=
    intervalIntegrable_const
  have hlin : IntervalIntegrable (fun u : ℝ => a + h - u) volume a (a + h) :=
    hc2.sub intervalIntegral.intervalIntegrable_id
  constructor
  · -- lower: replace f′ ξ by the right-endpoint value f′ (a+h)
    have hmono := intervalIntegral.integral_mono_on hab
      (hlin.const_mul (f' (a + h))) hint (fun u hu => by
        have h1 := (sub_bracket_of_antitoneOn_deriv hderiv hanti hu.1 hu.2).1
        rw [mul_comm (f' (a + h)) (a + h - u)]
        exact h1)
    rw [intervalIntegral.integral_const_mul, integral_sub_linear,
      mul_comm (f' (a + h)) (h ^ 2 / 2)] at hmono
    exact hmono
  · -- upper: f′ u ≤ f′ a pointwise, then the same integral
    have hptwise : ∀ u ∈ Set.Icc a (a + h),
        f (a + h) - f u ≤ (a + h - u) * f' a := by
      intro u hu
      have h1 := (sub_bracket_of_antitoneOn_deriv hderiv hanti hu.1 hu.2).2
      have h2 : f' u ≤ f' a := hanti ⟨le_rfl, hab⟩ hu hu.1
      nlinarith [h1, h2, sub_nonneg.mpr hu.2]
    have hmono := intervalIntegral.integral_mono_on hab hint
      (hlin.mul_const (f' a)) hptwise
    rwa [intervalIntegral.integral_mul_const, integral_sub_linear] at hmono

/-- **First Euler–Maclaurin correction on a uniform grid.**  For `f` with
    antitone derivative on `[0, nh]`, the right-endpoint Riemann defect is
    bracketed by `h²/2` times the two endpoint Riemann sums of `f′`:

        (h²/2)·Σ_{i<n} f′(x_{i+1})  ≤  Σ_{i<n} ∫_{cell_i} (f(x_{i+1}) − f(u)) du
                                    ≤  (h²/2)·Σ_{i<n} f′(x_i).

    Both envelopes are `(h/2)` times a Riemann sum of `f′` over `[0, nh]`, so
    both converge to `(h/2)·(f(nh) − f(0))` — the first Euler–Maclaurin term. -/
theorem grid_defect_bracket {f f' : ℝ → ℝ} {h : ℝ} (hh : 0 < h) {n : ℕ}
    (hderiv : ∀ x ∈ Set.Icc (0 : ℝ) ((n : ℝ) * h), HasDerivAt f (f' x) x)
    (hanti : AntitoneOn f' (Set.Icc (0 : ℝ) ((n : ℝ) * h))) :
    h ^ 2 / 2 * (∑ i ∈ Finset.range n, f' (((i : ℝ) + 1) * h))
        ≤ ∑ i ∈ Finset.range n,
            ∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
              (f (((i : ℝ) + 1) * h) - f u)
      ∧ (∑ i ∈ Finset.range n,
            ∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
              (f (((i : ℝ) + 1) * h) - f u))
        ≤ h ^ 2 / 2 * (∑ i ∈ Finset.range n, f' ((i : ℝ) * h)) := by
  have hcell : ∀ i ∈ Finset.range n,
      h ^ 2 / 2 * f' (((i : ℝ) + 1) * h)
          ≤ (∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
              (f (((i : ℝ) + 1) * h) - f u))
        ∧ (∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
              (f (((i : ℝ) + 1) * h) - f u))
          ≤ h ^ 2 / 2 * f' ((i : ℝ) * h) := by
    intro i hi
    have hi' := Finset.mem_range.mp hi
    have hsub : Set.Icc ((i : ℝ) * h) ((i : ℝ) * h + h)
        ⊆ Set.Icc (0 : ℝ) ((n : ℝ) * h) := by
      refine Set.Icc_subset_Icc (by positivity) ?_
      have hin : ((i : ℝ) + 1) ≤ (n : ℝ) := by exact_mod_cast hi'
      nlinarith
    have heq : (i : ℝ) * h + h = ((i : ℝ) + 1) * h := by ring
    have hres := cell_defect_bracket (f := f) (f' := f') (a := (i : ℝ) * h) hh
      (fun x hx => hderiv x (hsub hx)) (hanti.mono hsub)
    rw [heq] at hres
    exact hres
  constructor
  · rw [Finset.mul_sum]
    exact Finset.sum_le_sum fun i hi => (hcell i hi).1
  · rw [Finset.mul_sum]
    exact Finset.sum_le_sum fun i hi => (hcell i hi).2

/-- **Non-negativity of the per-cell Euler–Maclaurin bracket width (`qou-shrp`):**
For `f'` antitone on `[a, a + h]` with `0 < h`, the upper envelope minus the lower
envelope `(h²/2)·(f'(a) - f'(a + h))` is non-negative. -/
theorem cell_defect_width_nonneg {f' : ℝ → ℝ} {a h : ℝ} (hh : 0 < h)
    (hanti : AntitoneOn f' (Set.Icc a (a + h))) :
    0 ≤ h ^ 2 / 2 * (f' a - f' (a + h)) := by
  have hab : a ≤ a + h := by linarith
  have hfa : f' (a + h) ≤ f' a :=
    hanti ⟨le_rfl, hab⟩ ⟨hab, le_rfl⟩ hab
  have hh2 : 0 ≤ h ^ 2 / 2 := by positivity
  exact mul_nonneg hh2 (sub_nonneg.mpr hfa)

/-- **Midpoint refinement of the per-cell Euler–Maclaurin bracket (`qou-shrp`):**
The trapezoidal average `(h²/4)·(f'(a) + f'(a + h))` of the two endpoint envelopes
approximates the cell defect within half the bracket width `(h²/4)·(f'(a) - f'(a + h))`. -/
theorem cell_defect_sub_midpoint_le {f f' : ℝ → ℝ} {a h : ℝ} (hh : 0 < h)
    (hderiv : ∀ x ∈ Set.Icc a (a + h), HasDerivAt f (f' x) x)
    (hanti : AntitoneOn f' (Set.Icc a (a + h))) :
    |(∫ u in a..(a + h), (f (a + h) - f u)) - h ^ 2 / 4 * (f' a + f' (a + h))|
      ≤ h ^ 2 / 4 * (f' a - f' (a + h)) := by
  have hbr := cell_defect_bracket hh hderiv hanti
  rw [abs_sub_le_iff]
  constructor <;> linarith [hbr.1, hbr.2]

end QOU.Knot
