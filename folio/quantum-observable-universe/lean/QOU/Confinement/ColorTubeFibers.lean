import Mathlib.Tactic

/-!
# QOU.ColorTubeFibers

**Canonical declaration** for content block at
[`quantum-observable-universe/brings-surface/color-tube-fibers.ts`](quantum-observable-universe/brings-surface/color-tube-fibers.ts).

Formalises the manuscript **definition** of the color tube `R_z` at
`z ∈ ℙ¹(ℂ)` — the affine curve cut out by the color-tube cubic

`𝐫³ + (4z+1)𝐫² + (6z²+3z+1)𝐫 + (4z³+3z²+2z+1) = 0`

— and the shift `𝐫 = X − z` realising the isomorphism `R_z ≅ 𝓔_z` with the
color elliptic fiber. Pure algebra — generic over any `CommRing` (§7c-clean).
-/

namespace QOU

/-- Data for the color tube `R_z` at a point `z` (the same cubic defines the
    `G_z`, `B_z` tubes with the other resolvent coordinates).

    A `definition` carrier: the base point `z`, and the color-tube cubic
    `cubic` pinned to its manuscript polynomial. Membership `𝐫 ∈ R_z` is
    `cubic 𝐫 = 0`. -/
structure ColorTubeFibers (R : Type*) [CommRing R] where
  /-- The base point `z ∈ ℙ¹`. -/
  z : R
  /-- The color-tube cubic `P_z`. -/
  cubic : R → R
  /-- Defining polynomial of the color tube. -/
  cubic_def : ∀ r,
    cubic r = r ^ 3 + (4 * z + 1) * r ^ 2 + (6 * z ^ 2 + 3 * z + 1) * r
      + (4 * z ^ 3 + 3 * z ^ 2 + 2 * z + 1)

-- Ref: [leitner2026] quantum-observable-universe/brings-surface/color-tube-fibers.ts

/-- The shift `𝐫 = X − z` (the map `X = 𝐜 + z` to the color elliptic fiber
    `𝓔_z`) turns the color-tube cubic into the monic cubic
    `X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`. -/
theorem ColorTubeFibers.shift_to_elliptic {R : Type*} [CommRing R]
    (C : ColorTubeFibers R) (X : R) :
    C.cubic (X - C.z) =
      X ^ 3 + (C.z + 1) * X ^ 2 + (C.z ^ 2 + C.z + 1) * X
        + (C.z ^ 3 + C.z ^ 2 + C.z + 1) := by
  rw [C.cubic_def]; ring

/-- `𝐫 ∈ R_z` (i.e. `cubic 𝐫 = 0`) transports to a root of the shifted monic
    cubic at `X = 𝐫 + z`. -/
theorem shiftedCubic_eq_zero_of_cubic_eq_zero {R : Type*} [CommRing R]
    (C : ColorTubeFibers R) (r : R) (hr : C.cubic r = 0) :
    (r + C.z) ^ 3 + (C.z + 1) * (r + C.z) ^ 2
      + (C.z ^ 2 + C.z + 1) * (r + C.z)
      + (C.z ^ 3 + C.z ^ 2 + C.z + 1) = 0 := by
  have := C.shift_to_elliptic (r + C.z)
  simpa using this.symm.trans (by rw [add_sub_cancel_right]; exact hr)

end QOU
