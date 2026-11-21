import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Units.Basic

/-!
# The Schwinger proper-time measure and its unit

Content block: `def:schwinger-measure-unit` (predicted-spectra).

The density SHAPE of the Schwinger proper-time measure `ς·ds/s`, stated
over a generic commutative ring per §7c: `density ς s = ς · s⁻¹` with the
proper time `s` carried as a **unit** `s : Rˣ`, and the canonical unit
`canonicalUnit = 1`. The archimedean reading — the multiplicative Haar
measure on `(0, ∞)`, one nat per proper-time e-fold under `k_B = 1` — and
its shape rigidity live on the `ℝ`-side of the wall in
`QOU.Archimedean.SchwingerMeasureShape` (`scale_invariant_density_unique`,
`one_nat_per_efold`); this file carries the fibre-level algebraic object
that downstream consumers reference.

The CANONICITY of `ς = 1` is conjectural, not proved: it is conditionally
forced by `conj:schwinger-measure-computational-time`
(`SchwingerMeasureComputationalTime.unit_eq_one_of_keystone_normalizer`)
or by owner premises P1/P2; unconditionally it is a unit convention per
the 2026-07-19 owner ruling (R2 is not derived-proved). Defining the
object does not assert the conjecture.

Base ring (§7c): generic `{R : Type*} [CommRing R]` — no field, no
division, no `Real.*`, no ordering. Nothing here needs an inverse of an
element that can vanish: the proper time is invertible (archimedeanly
`s > 0`), so it is carried as `s : Rˣ`, which is exactly what the former
`Field` + `s ≠ 0` / `lam ≠ 0` side conditions encoded. The archimedean
specialisation stays in the separate `SchwingerMeasureShape` file.

-- Ref: [leitner2026] docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md
-/

namespace QOU.Archimedean.SchwingerMeasureUnit

variable {R : Type*} [CommRing R]

/-- The Schwinger proper-time density with unit `ς`: `s ↦ ς · s⁻¹` — the
fibre-level shape of the measure `ς·ds/s` (narrative symbol: `ς` is
written `varsigma`; the audit lineage's `c` is register-reserved for
color). The proper time `s` ranges over the units of `R`. -/
def density (ς : R) (s : Rˣ) : R := ς * ((s⁻¹ : Rˣ) : R)

/-- The canonical Schwinger unit `ς = 1` — "one nat per proper-time
e-fold" under `k_B = 1`. Canonicity is conjecturally backed (see the
module docstring); this is a definition naming a construction, not a
claim. -/
def canonicalUnit : R := 1

/-- The density satisfies the multiplicative scale-invariance functional
equation `density ς (λ·s) · λ = density ς s` — the generic-ring face of
the `ℝ`-side uniqueness `SchwingerMeasureShape.scale_invariant_density_unique`.
The former `lam ≠ 0`, `s ≠ 0` hypotheses are now carried by the types. -/
theorem density_scale_invariant (ς : R) (lam s : Rˣ) :
    density ς (lam * s) * ((lam : Rˣ) : R) = density ς s := by
  unfold density
  rw [mul_inv_rev, Units.val_mul, mul_assoc, mul_assoc, Units.inv_mul, mul_one]

/-- With the canonical unit the density is the reciprocal `s⁻¹`. -/
theorem canonicalUnit_density (s : Rˣ) :
    density (canonicalUnit : R) s = ((s⁻¹ : Rˣ) : R) := by
  unfold density canonicalUnit
  rw [one_mul]

end QOU.Archimedean.SchwingerMeasureUnit
