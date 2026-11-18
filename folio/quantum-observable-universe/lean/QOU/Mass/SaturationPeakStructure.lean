/-
QOU.Mass.SaturationPeakStructure — the per-nucleon binding curve PEAKS strictly below its bulk
coefficient, so the peak value carries no information about the bulk constant.

Arc context (bk-crossing mass-binding; bean `qou-brng`, residual R3). The R3 probe
(`computations/brng_hbarq2_saturation_genericity_probe.py`) MEASURED that the empirical `B/A/m_N`
rises to `0.954·ℏ_q²` at ⁶²Ni and then FALLS (²³⁸U: `0.821·ℏ_q²`), while the fundamental volume
coefficient is `a_V/m_N ≈ 1.71·ℏ_q²`. That measurement is what makes the `B/A ≈ ℏ_q²` match
numerology rather than a saturation prediction: `ℏ_q²` was being compared to an interior maximum, not
to a saturation limit.

This file supplies the STRUCTURAL reason, so the R3 verdict rests on a theorem rather than on a table
of nuclides. Nothing here is fitted and no substrate constant appears — it is a statement about the
SHAPE of any volume−surface−Coulomb binding curve.

## Setup

Write the per-nucleon binding in the standard volume−surface−Coulomb shape, in the variable
`u = A^(1/3) > 0` (which removes every fractional power and makes the whole file elementary):

    f(u) = a_V − a_S/u − a_C·u²

with `a_V` the bulk (volume) coefficient, `a_S > 0` the surface cost, `a_C ≥ 0` the Coulomb cost.

## Results

* `perNucleon_lt_volume` — for `a_S > 0`, `a_C ≥ 0` and any `u > 0`, `f(u) < a_V`. **The curve never
  attains the bulk coefficient**: the surface term alone keeps it strictly below, at every mass
  number. So the maximum of the observed curve is strictly less than `a_V`.
* `volume_gap` — the deficit is exactly the surface-plus-Coulomb cost, `a_V − f(u) = a_S/u + a_C·u²`,
  which is bounded away from zero on any bounded range of `u`.
* `perNucleon_increasing` / `perNucleon_decreasing` — the curve RISES while
  `a_C(u₁+u₂)u₁u₂ < a_S` and FALLS once `a_C(u₁+u₂)u₁u₂ > a_S`. With `a_C > 0` both regimes occur,
  so the curve has an interior maximum: **it peaks and then declines.** (Stated as an explicit
  algebraic threshold rather than via a derivative, so the file needs no calculus.)

## What this establishes for the arc

The empirical `B/A` peak is an **interior maximum of a surface/Coulomb competition**, not a
saturation limit — its location and height are set by `a_S` and `a_C`, and it lies strictly below
`a_V` by `perNucleon_lt_volume`. Identifying that peak with any fundamental constant is therefore a
category error: the peak is not a bulk quantity. This is the structural form of R3's numerical
finding, and it holds for every parameter choice — no fit, no anchor, no substrate input.

## Scope — what is NOT claimed

That the volume−surface−Coulomb shape is the *correct* model of nuclear binding is an empirical
input (the semi-empirical mass formula), not proved here; this file proves what follows FROM that
shape. Nothing here derives `a_V`, `a_S` or `a_C`, and nothing here mentions `ℏ_q` — the point is
precisely that the peak's height is independent of any substrate constant.

Ground ring `ℝ` (§7c: archimedean — division and ordering are essential to the statement). No fit.
-/
import Mathlib.Tactic

namespace QOU.Mass.SaturationPeakStructure

/-- Per-nucleon binding in the volume−surface−Coulomb shape, in the variable `u = A^(1/3) > 0`:
`f(u) = a_V − a_S/u − a_C·u²`. -/
noncomputable def perNucleon (aV aS aC u : ℝ) : ℝ := aV - aS / u - aC * u ^ 2

/-- **The deficit from the bulk coefficient is exactly the surface-plus-Coulomb cost.** -/
theorem volume_gap (aV aS aC u : ℝ) :
    aV - perNucleon aV aS aC u = aS / u + aC * u ^ 2 := by
  unfold perNucleon; ring

/-- **The curve never attains the bulk coefficient.** For a positive surface cost and a non-negative
Coulomb cost, `f(u) < a_V` at every `u > 0` — so the observed maximum of the per-nucleon binding lies
STRICTLY BELOW `a_V`. This is the structural reason the empirical `B/A` peak is not the bulk
coefficient, and hence why matching a constant to that peak says nothing about the bulk. -/
theorem perNucleon_lt_volume (aV aS aC u : ℝ) (haS : 0 < aS) (haC : 0 ≤ aC) (hu : 0 < u) :
    perNucleon aV aS aC u < aV := by
  unfold perNucleon
  have h1 : 0 < aS / u := div_pos haS hu
  have h2 : 0 ≤ aC * u ^ 2 := mul_nonneg haC (sq_nonneg u)
  linarith

/-- The exact difference of the curve at two points — the algebraic engine for the rising and
falling branches below. -/
theorem perNucleon_sub (aV aS aC u₁ u₂ : ℝ) (h₁ : u₁ ≠ 0) (h₂ : u₂ ≠ 0) :
    perNucleon aV aS aC u₁ - perNucleon aV aS aC u₂
      = (u₂ - u₁) * (aC * (u₁ + u₂) - aS / (u₁ * u₂)) := by
  unfold perNucleon
  field_simp
  ring

/-- **Rising branch.** While the Coulomb cost is small against the surface cost
(`a_C(u₁+u₂)u₁u₂ < a_S`), the per-nucleon binding INCREASES with mass number. -/
theorem perNucleon_increasing (aV aS aC u₁ u₂ : ℝ) (h₁ : 0 < u₁) (h₂ : u₁ < u₂)
    (h : aC * (u₁ + u₂) * (u₁ * u₂) < aS) :
    perNucleon aV aS aC u₁ < perNucleon aV aS aC u₂ := by
  have hu₂ : 0 < u₂ := lt_trans h₁ h₂
  have hprod : 0 < u₁ * u₂ := mul_pos h₁ hu₂
  have hkey : aC * (u₁ + u₂) - aS / (u₁ * u₂) < 0 := by
    rw [sub_neg, lt_div_iff₀ hprod]
    linarith
  have hd : 0 < u₂ - u₁ := sub_pos.mpr h₂
  have hsub := perNucleon_sub aV aS aC u₁ u₂ (ne_of_gt h₁) (ne_of_gt hu₂)
  nlinarith [mul_pos hd (neg_pos.mpr hkey)]

/-- **Falling branch.** Once the Coulomb cost dominates the surface cost
(`a_C(u₁+u₂)u₁u₂ > a_S`), the per-nucleon binding DECREASES with mass number. Together with
`perNucleon_increasing` this gives an interior maximum: the curve peaks and then declines, exactly as
the AME data do beyond A≈60. -/
theorem perNucleon_decreasing (aV aS aC u₁ u₂ : ℝ) (h₁ : 0 < u₁) (h₂ : u₁ < u₂)
    (h : aS < aC * (u₁ + u₂) * (u₁ * u₂)) :
    perNucleon aV aS aC u₂ < perNucleon aV aS aC u₁ := by
  have hu₂ : 0 < u₂ := lt_trans h₁ h₂
  have hprod : 0 < u₁ * u₂ := mul_pos h₁ hu₂
  have hkey : 0 < aC * (u₁ + u₂) - aS / (u₁ * u₂) := by
    rw [sub_pos, div_lt_iff₀ hprod]
    linarith
  have hd : 0 < u₂ - u₁ := sub_pos.mpr h₂
  have hsub := perNucleon_sub aV aS aC u₁ u₂ (ne_of_gt h₁) (ne_of_gt hu₂)
  nlinarith [mul_pos hd hkey]

/-- **The peak is not a bulk quantity — the interpretive punchline.** Whatever mass number maximises
the per-nucleon binding, its value is strictly below `a_V`, and the shortfall is precisely the
surface-plus-Coulomb cost at that point. Therefore a constant matching the observed peak matches an
interior maximum of a surface/Coulomb competition, not the bulk coefficient — the two differ by a
parameter-dependent amount with no fundamental significance. -/
theorem peak_is_not_bulk (aV aS aC uPeak : ℝ) (haS : 0 < aS) (haC : 0 ≤ aC) (hu : 0 < uPeak) :
    perNucleon aV aS aC uPeak < aV
      ∧ aV - perNucleon aV aS aC uPeak = aS / uPeak + aC * uPeak ^ 2 :=
  ⟨perNucleon_lt_volume aV aS aC uPeak haS haC hu, volume_gap aV aS aC uPeak⟩


/-- **Positivity of the bulk shortfall (`qou-8lxd`).**
For `0 < aS`, `0 ≤ aC`, and `0 < u`, `0 < aV - perNucleon aV aS aC u`. -/
theorem volume_gap_pos (aV aS aC u : ℝ) (haS : 0 < aS) (haC : 0 ≤ aC) (hu : 0 < u) :
    0 < aV - perNucleon aV aS aC u :=
  sub_pos.mpr (perNucleon_lt_volume aV aS aC u haS haC hu)

end QOU.Mass.SaturationPeakStructure
