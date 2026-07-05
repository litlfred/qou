import Mathlib.Tactic

/-!
# QOU.SkeinResolutionObstruction

**Canonical declaration** for content block at
[`quantum-observable-universe/braids-and-knots/skein-resolution-obstruction.ts`](quantum-observable-universe/braids-and-knots/skein-resolution-obstruction.ts).

Formalises the manuscript **definition** of the Skein resolution obstruction
`κ_c^comp(L,q)` — the image of the universal obstruction class
`χ(A) ∈ HH² ≅ k` under the resolution-tree restriction map (the fourth
evaluation of `χ(A)`; cf. `thm:qou-obstruction-reduction`). Generic over the
coefficient ring (§7c-clean).
-/

namespace QOU

/-- Data for the Skein resolution obstruction on a link `L`.

    A `definition` carrier: the universal obstruction class `χ ∈ R` (the
    Hochschild `HH² ≅ k` value), the additive resolution-tree restriction map
    `res`, and the obstruction `κ = res χ`. -/
structure SkeinResolutionObstruction (R : Type*) [CommRing R] where
  /-- The universal obstruction class `χ(A) ∈ HH² ≅ k`. -/
  χ : R
  /-- The resolution-tree restriction map (additive). -/
  res : R →+ R
  /-- The Skein resolution obstruction `κ = res(χ)`. -/
  κ : R
  /-- `κ` is the restriction of the universal class. -/
  κ_def : κ = res χ

namespace SkeinResolutionObstruction

variable {R : Type*} [CommRing R] (S : SkeinResolutionObstruction R)

/-- A vanishing universal class forces the resolution obstruction to vanish:
    if `χ(A) = 0` then `κ_c^comp(L,q) = 0` (the degree-0 answer is
    extractable). -/
theorem kappa_eq_zero_of_chi_zero (h : S.χ = 0) : S.κ = 0 := by
  rw [S.κ_def, h, map_zero]

end SkeinResolutionObstruction

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/skein-resolution-obstruction.ts

end QOU
