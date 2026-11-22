import QOU.Knot.FigureEightComplexVolume

set_option autoImplicit false

/-!
# QOU.Knot.FigureEightQuarticCoefficient — a₄ = i·√3/24 from the NZ longitude

The order-u⁴ extension of `FigureEightComplexVolume` (bean `qou-x88s`): the
E1/E1b probes measured the quartic coefficient of the deformed 4₁ complex
volume as `a₄ = i·0.0721687836487… = i·√3/24` (4-point Richardson on the NZ
longitude integral; a₂ cross-validated to 3×10⁻²⁰, a₄ stable to 4×10⁻¹⁵).
This file DERIVES that value from the Neumann–Zagier integration

    𝔙(u) = 𝔙₀ − ½ ∫₀ᵘ v(t) dt,     v(u) = τ·u + v₃·u³ + O(u⁵),

whose term-wise integration gives `a₂ = −τ/4` and `a₄ = −v₃/8`
(`a_{2k} = −v_{2k−1}/(4k)`). With the CCGLS-recognized coefficients
`τ = −i√3` and `v₃ = −i√3/3` the exact values follow by algebra.

## Provenance tiers (machinery-proved ≠ values-derived)

* The **integration algebra** (`a₂_eq_neg_tau_div_four`,
  `a₄_eq_neg_v₃_div_eight`) is proved here, sorry-free.
* The **coefficient inputs** `τ = −i√3`, `v₃ = −i√3/3` are the CCGLS
  A-polynomial recognition — probe-certified
  (`computations/probes/qbeta_nz_even_series_fourone_probe.py`, the
  `τ = (0,∓1,1)`, `v₃ = (0,∓1,3)` ℚ(√−3) recognition), NOT Lean-derived.
  They enter as definitions whose provenance is this docstring.
* The **log-cos closed form** `−(√3/2)i·log cos u` (which would predict
  `a₆ = i√3/90`) is REFUTED by the E1b measurement
  (`a₆ = i·0.0184431195 ≠ i·0.0192450`, witness
  `qbeta-ohtsuki-nz-bridge-b6.witness.json`) — this file deliberately
  stops at u⁴ and claims no closed form for the series.

## References

- [neumann-zagier1985] Neumann & Zagier, Topology 24 (1985). https://doi.org/10.1016/0040-9383(85)90004-7
- [leitner2026] computations/qbeta/qbeta_ohtsuki_nz_bridge_b4_probe.py (the measurement);
  QOU/Knot/FigureEightComplexVolume.lean (the order-u² file this extends).
-/

namespace QOU.Knot.FigureEightQuarticCoefficient

open QOU.Knot.FigureEightComplexVolume
open QOU.Knot.FigureEightVolume

/-- The quartic modulus `√3/24` — the measured (and here NZ-derived)
`Im`-coefficient at order `u⁴`. -/
noncomputable def quarticModulus : ℝ := Real.sqrt 3 / 24

theorem quarticModulus_pos : 0 < quarticModulus := by
  unfold quarticModulus
  positivity

/-- `a₄ = i·√3/24`. -/
noncomputable def a₄ : ℂ := ⟨0, quarticModulus⟩

@[simp] theorem a₄_re : a₄.re = 0 := rfl
@[simp] theorem a₄_im : a₄.im = quarticModulus := rfl

/-- The NZ longitude's linear coefficient (cusp modulus): `τ = −i·√3`.
CCGLS A-polynomial recognition — probe-certified input, see the module
docstring's provenance tier. -/
noncomputable def tau : ℂ := ⟨0, -Real.sqrt 3⟩

/-- The NZ longitude's cubic coefficient: `v₃ = −i·√3/3`. CCGLS
recognition `(0, ∓1, 3)` — probe-certified input. -/
noncomputable def v₃ : ℂ := ⟨0, -(Real.sqrt 3 / 3)⟩

/-- **NZ integration, order u²:** `𝔙 = 𝔙₀ − ½∫v` integrates `τ·u` to
`−τu²/4`, so `a₂ = −τ/4` — and the file's `a₂ = i√3/4` is exactly that. -/
theorem a₂_eq_neg_tau_div_four : a₂ = -tau / 4 := by
  unfold a₂ tau cuspModulus
  apply Complex.ext <;> simp

/-- **NZ integration, order u⁴:** `−½∫ v₃u³ = −v₃u⁴/8`, so `a₄ = −v₃/8` —
and with the recognized `v₃ = −i√3/3` this IS `i·√3/24`, the E1/E1b
measured value, now derived rather than only measured. -/
theorem a₄_eq_neg_v₃_div_eight : a₄ = -v₃ / 8 := by
  unfold a₄ v₃ quarticModulus
  apply Complex.ext <;> simp
  ring

/-- The quartic-extended deformed complex volume
`𝔙(u) = 𝔙₀ + a₂u² + a₄u⁴`. -/
noncomputable def V₄₁quartic (u : ℂ) : ℂ := (VOL_4_1 : ℂ) + a₂ * u ^ 2 + a₄ * u ^ 4

@[simp] theorem V₄₁quartic_zero : V₄₁quartic 0 = (VOL_4_1 : ℂ) := by
  simp [V₄₁quartic]

/-- The quartic extension agrees with the order-u² model up to the `a₄u⁴`
term. -/
theorem V₄₁quartic_eq_V₄₁_add (u : ℂ) :
    V₄₁quartic u = V₄₁ u + a₄ * u ^ 4 := by
  unfold V₄₁quartic V₄₁
  ring

/-- NZ evenness survives the extension: `𝔙(−u) = 𝔙(u)`. -/
theorem V₄₁quartic_even (u : ℂ) : V₄₁quartic (-u) = V₄₁quartic u := by
  unfold V₄₁quartic
  ring

/-- The imaginary part through order u⁴:
`Im 𝔙 = (√3/4)(Re²u − Im²u) + (√3/24)·Re(u⁴)` — the diagonal structure of
`imV₄₁` plus the quartic correction. -/
theorem imV₄₁quartic (u : ℂ) :
    (V₄₁quartic u).im
      = cuspModulus * (u.re ^ 2 - u.im ^ 2) + quarticModulus * (u ^ 4).re := by
  rw [V₄₁quartic_eq_V₄₁_add, Complex.add_im, imV₄₁]
  congr 1
  simp [Complex.mul_im]

end QOU.Knot.FigureEightQuarticCoefficient
