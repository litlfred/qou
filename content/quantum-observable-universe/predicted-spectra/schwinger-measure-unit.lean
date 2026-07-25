import Mathlib.Tactic.FieldSimp

/-!
# The Schwinger proper-time measure and its unit

Content block: `def:schwinger-measure-unit` (predicted-spectra).

The density SHAPE of the Schwinger proper-time measure `ς·ds/s`, stated
over a generic field per §7c: `density ς s = ς / s`, with the canonical
unit `canonicalUnit = 1`. The archimedean reading — the multiplicative
Haar measure on `(0, ∞)`, one nat per proper-time e-fold under `k_B = 1`
— and its shape rigidity live on the `ℝ`-side of the wall in
`QOU.Archimedean.SchwingerMeasureShape` (`scale_invariant_density_unique`,
`one_nat_per_efold`); this file carries the fibre-level algebraic object
that downstream consumers reference.

The CANONICITY of `ς = 1` is conjectural, not proved: it is conditionally
forced by `conj:schwinger-measure-computational-time`
(`SchwingerMeasureComputationalTime.unit_eq_one_of_keystone_normalizer`)
or by owner premises P1/P2; unconditionally it is a unit convention per
the 2026-07-19 owner ruling (R2 is not derived-proved). Defining the
object does not assert the conjecture.

Base ring (§7c): generic `{K : Type*} [Field K]` — only field operations;
no `Real.*`, no ordering. The archimedean specialisation stays in the
separate `SchwingerMeasureShape` file.

-- Ref: [manuscript] docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md
-/

namespace QOU.Archimedean.SchwingerMeasureUnit

variable {K : Type*} [Field K]

/-- The Schwinger proper-time density with unit `ς`: `s ↦ ς / s` — the
fibre-level shape of the measure `ς·ds/s` (narrative symbol: `ς` is
written `varsigma`; the audit lineage's `c` is register-reserved for
color). -/
def density (ς s : K) : K := ς / s

/-- The canonical Schwinger unit `ς = 1` — "one nat per proper-time
e-fold" under `k_B = 1`. Canonicity is conjecturally backed (see the
module docstring); this is a definition naming a construction, not a
claim. -/
def canonicalUnit : K := 1

/-- The density satisfies the multiplicative scale-invariance functional
equation `density ς (λ·s) · λ = density ς s` for `λ, s ≠ 0` — the
generic-field face of the `ℝ`-side uniqueness
`SchwingerMeasureShape.scale_invariant_density_unique`. -/
theorem density_scale_invariant (ς lam s : K) (hlam : lam ≠ 0) (hs : s ≠ 0) :
    density ς (lam * s) * lam = density ς s := by
  unfold density
  field_simp

/-- With the canonical unit the density is the reciprocal `1 / s`. -/
theorem canonicalUnit_density (s : K) :
    density (canonicalUnit : K) s = 1 / s := rfl

end QOU.Archimedean.SchwingerMeasureUnit
