import Mathlib.Tactic

/-!
# The discriminant of the colour cubic — generic identities

Chip on `conj:hecke-monodromy-step-two` (`QOU.Mass.HeckeMonodromy`). The probe
`computations/probes/colour_cubic_branch_monodromy_probe.py` computes, exactly in `sympy`, the
`X`-discriminant of the colour cubic `P(X, z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`:

  `disc_X P = −(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16)`,

and records two facts about the sextic `D(z)` in that bracket that this file makes theorems over
a generic field:

* `colourDiscriminant_reciprocal` — `D` is **reciprocal**: `z⁶ · D(z⁻¹) = D(z)` for `z ≠ 0`. This
  is the structural reason the six branch points come in pairs `z ↔ 1/z` on a common ray, which
  is what forced the probe's lasso paths to detour (its `lasso(...)` docstring).
* `colourDiscriminant_sos` — the sum-of-squares identity
  `D(z) = (4z³ + 3z² + 3z + 4)² + 2z²(z² + 1)`, a pure ring identity. Over an ordered field it
  gives `D > 0` everywhere, i.e. **no real branch point** — that archimedean consequence lives in
  `QOU/Mass/ColourCubicDiscriminantReal.lean` per §7c.

The *discriminant* is `−D`, so its sign is opposite; only the vanishing locus matters for the
branch points, and `D` and `−D` share it.

Base ring §7c: `CommRing R` for the sum of squares, `Field K` for the reciprocity (needs `z⁻¹`).

-- Ref: [leitner2026] computations/probes/colour_cubic_branch_monodromy_probe.py
-- Ref: [leitner2026] folio/quantum-observable-universe/mass-theory/hecke-monodromy-step-two.md
-/

namespace QOU.Mass.ColourCubicDiscriminant

section Generic

variable {R : Type*} [CommRing R]

/-- The sextic `D(z) = 16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16`; the `X`-discriminant of the
colour cubic is `−D(z)`. -/
def colourDiscriminant (z : R) : R :=
  16 * z ^ 6 + 24 * z ^ 5 + 35 * z ^ 4 + 50 * z ^ 3 + 35 * z ^ 2 + 24 * z + 16

/-- **Sum of squares.** `D(z) = (4z³ + 3z² + 3z + 4)² + 2z²(z² + 1)`. -/
theorem colourDiscriminant_sos (z : R) :
    colourDiscriminant z = (4 * z ^ 3 + 3 * z ^ 2 + 3 * z + 4) ^ 2 + 2 * z ^ 2 * (z ^ 2 + 1) := by
  unfold colourDiscriminant; ring

/-- The discriminant at `z = 0` (the probe's base point) is `−16`; not a branch point. -/
theorem colourDiscriminant_zero : colourDiscriminant (0 : R) = 16 := by
  simp [colourDiscriminant]

end Generic

section Field

variable {K : Type*} [Field K]

/-- **Reciprocity.** `z⁶ · D(z⁻¹) = D(z)` for `z ≠ 0`: branch points come in pairs `z ↔ 1/z`. -/
theorem colourDiscriminant_reciprocal {z : K} (hz : z ≠ 0) :
    z ^ 6 * colourDiscriminant z⁻¹ = colourDiscriminant z := by
  unfold colourDiscriminant
  field_simp
  ring

/-- Hence `z` is a root of `D` iff `z⁻¹` is, for `z ≠ 0`. -/
theorem colourDiscriminant_root_iff_inv {z : K} (hz : z ≠ 0) :
    colourDiscriminant z = 0 ↔ colourDiscriminant z⁻¹ = 0 := by
  rw [← colourDiscriminant_reciprocal hz]
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h6 | h
    · exact absurd (pow_eq_zero_iff (by norm_num : (6 : ℕ) ≠ 0) |>.mp h6) hz
    · exact h
  · intro h; rw [h, mul_zero]

end Field

end QOU.Mass.ColourCubicDiscriminant
