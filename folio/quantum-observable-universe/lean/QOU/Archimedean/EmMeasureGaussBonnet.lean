import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-!
# The α_EM per-loop measure as a Gauss–Bonnet invariant

Lean formalisation of the three identities established numerically in
`computations/alpha_em/alpha_em_gauss_bonnet_measure_probe.py`
(audit `docs/audits/2026-07-18-alpha-em-gauss-bonnet-measure.md`):

* the "gauge loop unit" `1/(4π)` is the geometric ratio `|χ|/(2·Area)`;
* the α_EM per-loop measure `1/(8π)` is the Gauss–Bonnet object `|χ|/(4·Area)`,
  which is **genus-independent** (it equals `1/(8π)` for every `g ≠ 1`);
* the Betti reading `1/(π·b₁)` coincides with the measure **only at `g = 4`**.

Here `Area = 4π(g-1)` is the hyperbolic Gauss–Bonnet area `-2π·χ`, `|χ| = 2g-2`,
and `b₁ = 2g` for a genus-`g` surface. Everything is an `ℝ`-identity
(archimedean: `π`, division), so the base ring is `ℝ` per the §7c wall.
-/

namespace QOU.Archimedean.EmMeasureGaussBonnet

open Real

/-- Hyperbolic Gauss–Bonnet area of a genus-`g` surface: `Area = 4π(g-1) = -2π·χ`. -/
noncomputable def area (g : ℝ) : ℝ := 4 * π * (g - 1)

/-- `|χ| = 2g - 2` for a genus-`g` surface (`g ≥ 1`). -/
def absChi (g : ℝ) : ℝ := 2 * g - 2

/-- First Betti number `b₁ = 2g`. -/
def b1 (g : ℝ) : ℝ := 2 * g

/-- The gauge loop unit `1/(4π)` is the geometric ratio `|χ|/(2·Area)` on any
hyperbolic surface (`g ≠ 1`) — no QFT-correspondence input needed. -/
theorem loop_unit_eq_geometric (g : ℝ) (hg : g ≠ 1) :
    absChi g / (2 * area g) = 1 / (4 * π) := by
  have hpi : (π : ℝ) ≠ 0 := ne_of_gt pi_pos
  have hg1 : g - 1 ≠ 0 := sub_ne_zero.mpr hg
  unfold absChi area
  field_simp

/-- The α_EM per-loop measure is the Gauss–Bonnet invariant `|χ|/(4·Area) = 1/(8π)`,
**genus-independent**: it holds for every `g ≠ 1`. -/
theorem measure_eq_gauss_bonnet (g : ℝ) (hg : g ≠ 1) :
    absChi g / (4 * area g) = 1 / (8 * π) := by
  have hpi : (π : ℝ) ≠ 0 := ne_of_gt pi_pos
  have hg1 : g - 1 ≠ 0 := sub_ne_zero.mpr hg
  unfold absChi area
  field_simp
  norm_num

/-- The Betti reading `1/(π·b₁)` equals the per-loop measure `1/(8π)`
**iff `g = 4`** — the coincidence is unique to the Bring genus. -/
theorem b1_reading_coincides_iff_g4 (g : ℝ) :
    1 / (π * b1 g) = 1 / (8 * π) ↔ g = 4 := by
  have hpi : (π : ℝ) ≠ 0 := ne_of_gt pi_pos
  unfold b1
  rw [one_div, one_div, inv_inj]
  constructor
  · intro h
    have h2 : 2 * g = 8 := by
      have hh : π * (2 * g) = π * 8 := by rw [h]; ring
      exact mul_left_cancel₀ hpi hh
    linarith
  · rintro rfl; ring

/-- Corollary: the measure is genus-independent — `|χ|/(4·Area)` takes the same
value `1/(8π)` at two distinct genera. -/
theorem measure_genus_independent (g g' : ℝ) (hg : g ≠ 1) (hg' : g' ≠ 1) :
    absChi g / (4 * area g) = absChi g' / (4 * area g') := by
  rw [measure_eq_gauss_bonnet g hg, measure_eq_gauss_bonnet g' hg']

end QOU.Archimedean.EmMeasureGaussBonnet
