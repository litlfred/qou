import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# Two averaged crossings on one generator collapse to a scalar

`qou-cxon` Q2 measured that the convention-D cyclotomic exponent is `3A - 1`
minus two per neutron, and that the per-neutron cancellation fires **iff some
generator carries two or more averaged crossings** (12/12 configurations,
`d_frame_neutron_cyclotomic_rule_probe.py`).  That producer offered a
Hecke-collapse reading and flagged it explicitly as an *interpretation*, not a
proof.

It is a proof, and this file is it.

An averaged crossing is `σ + d` with `2d = -h`, `h = q - q⁻¹`.  Squaring it
inside the Hecke relation `σ² = h·σ + 1` gives

  `(σ + d)² = (h + 2d)·σ + (1 + d²)`

so at `2d = -h` the `σ` coefficient is **exactly zero** and the product is a
scalar.  Scaled by 4 to stay division-free, that scalar is exactly the
cyclotomic square the measurement saw cancel:

  `q²·(4 + h²) = (q² + 1)²`

## Why this explains the rule rather than restating it

* **Only the averaged coefficient collapses.**  `sq_sigma_coeff_vanishes` is
  matched by `sigmaCoeff_full_ne_zero` and `sigmaCoeff_identity_ne_zero`: at
  `d = -h` the residual `σ` coefficient is `-h`, at `d = 0` it is `h`.  Both
  are nonzero whenever `h ≠ 0`.  The collapse is a property of the
  colour-averaging value, not of squaring.
* **Co-location is forced.**  The collapse is a statement about a product of
  two factors on the **same** generator.  Two averaged crossings on different
  generators are never multiplied by this identity — which is why the measured
  rule is `max(gen0_avg, gen1_avg) ≥ 2` and not a total count.
* **Saturation follows.**  A third averaged crossing multiplies the scalar by
  `(σ + d)` again, reintroducing `σ` (`cube_eq_scalar_mul`), so no further
  `(q²+1)` appears.  That is the measured saturation: three on one generator
  still cancels 2, not 3.

## Base ring

A generic `CommRing` (§7c), and **division-free throughout**.  An earlier
draft of this file stated the same facts over a `Field` using `h/2` and
`h²/4`; that is unsound at characteristic 2, where `2 = 0` and `h/2` is not
the averaged coefficient at all.  Carrying the hypothesis as `2 * d = -h`
instead of dividing removes the characteristic assumption rather than
patching it, and the scaled cyclotomic identity `q²(4 + h²) = (q²+1)²` needs
no inverse of `q` either.  Nothing archimedean, no ordering, no `ℝ`.
-/

namespace QOU.BraidsAndKnots

variable {R : Type*} [CommRing R]

/-- The `σ` coefficient of `(σ + d)²` under the Hecke relation
`σ² = h·σ + 1`, before any choice of `d`. -/
theorem sq_sigma_coeff (σ h d : R) (hHecke : σ ^ 2 = h * σ + 1) :
    (σ + d) ^ 2 = (h + 2 * d) * σ + (1 + d ^ 2) := by
  linear_combination hHecke

/-- **The collapse.**  For the colour-averaged coefficient, characterised
division-free by `2 * d = -h`, the `σ` coefficient vanishes and the square of
an averaged crossing is the scalar `1 + d²`. -/
theorem sq_sigma_coeff_vanishes (σ h d : R) (hHecke : σ ^ 2 = h * σ + 1)
    (hd : 2 * d = -h) : (σ + d) ^ 2 = 1 + d ^ 2 := by
  have step : (σ + d) ^ 2 = (h + 2 * d) * σ + (1 + d ^ 2) :=
    sq_sigma_coeff σ h d hHecke
  rw [step, hd]
  ring

/-- **Control.**  A full crossing `d = -h` leaves `σ` coefficient `-h`, nonzero
whenever `h` is — no collapse. -/
theorem sigmaCoeff_full_ne_zero (h : R) (hh : h ≠ 0) : h + 2 * (-h) ≠ 0 := by
  have : h + 2 * (-h) = -h := by ring
  rw [this]
  simpa using hh

/-- **Control.**  An identity crossing `d = 0` leaves `σ` coefficient `h`,
again nonzero whenever `h` is — no collapse. -/
theorem sigmaCoeff_identity_ne_zero (h : R) (hh : h ≠ 0) :
    h + 2 * (0 : R) ≠ 0 := by
  simpa using hh

/-- The bare cyclotomic identity behind the collapse scalar. -/
theorem four_sq_add_sub_one_sq (q : R) :
    4 * q ^ 2 + (q ^ 2 - 1) ^ 2 = (q ^ 2 + 1) ^ 2 := by
  ring

/-- **The scalar is the cyclotomic square.**  With `h = q - q⁻¹` — carried
division-free as `q * h = q² - 1` — the collapse scalar scaled by `4q²` is
exactly `(q² + 1)²`, the factor whose cancellation the Q2 measurement
observed, once per pair of co-located averaged crossings. -/
theorem scaledCollapseScalar_eq_cyclotomicSq (q h : R)
    (hqh : q * h = q ^ 2 - 1) : q ^ 2 * (4 + h ^ 2) = (q ^ 2 + 1) ^ 2 := by
  linear_combination (q * h + q ^ 2 - 1) * hqh

/-- **Saturation.**  A third averaged crossing on the same generator
reintroduces `σ`: the cube is the collapse scalar times `(σ + d)`, so no
second `(q²+1)²` is produced.  This is why the measured cancellation is 2 even
when a generator carries three averaged crossings. -/
theorem cube_eq_scalar_mul (σ h d : R) (hHecke : σ ^ 2 = h * σ + 1)
    (hd : 2 * d = -h) : (σ + d) ^ 3 = (1 + d ^ 2) * (σ + d) := by
  have cube : (σ + d) ^ 3 = (σ + d) ^ 2 * (σ + d) := by ring
  rw [cube, sq_sigma_coeff_vanishes σ h d hHecke hd]

end QOU.BraidsAndKnots
