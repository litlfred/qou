import QOU.AlgebraicSubstrate.qou_obstruction_reduction

/-!
# QOU.SkeinResolutionObstruction

**Canonical declaration** for content block at
[`quantum-observable-universe/braids-and-knots/skein-resolution-obstruction.ts`](quantum-observable-universe/braids-and-knots/skein-resolution-obstruction.ts).

Formalises the manuscript **definition** of the Skein resolution obstruction
`κ_c^comp(L,q)` — the image of the universal obstruction class
`χ(A) ∈ HH² ≅ k` under the resolution-tree restriction map (the *fourth*
evaluation of `χ(A)`; cf. `thm:qou-obstruction-reduction`).

**De-axiomatised (2026-07-06, bean `7kzn`).** The universal class is no longer
a free field: it is cross-wired to the **same** `QouObstructionReductionContext`
that `qou_obstruction_reduction` uses — `octx.chi_A` **is** the universal class.
So this is literally the fourth evaluation of the one obstruction class, and the
vanishing statements are derived through the shared context's
`kappa_vanishes_iff_chi`.

**Repaired 2026-08-09.** This file did not compile on `main`: it referenced three
members that no version of `QouObstructionReductionContext` has —
`obstruction_class`, `obstruction_class_eq` and `kappa_vanishes_iff`. A rename to
`chi_A` / `kappa_vanishes_def` was never propagated here, and with the class field
and the class-consumer in different files nothing caught it. Kept generic over the coefficient ring `R`
(§7c: no archimedean construct is used).
-/

namespace QOU

open QOU.AlgebraicSubstrate (QouObstructionReductionContext)

/-- Data for the Skein resolution obstruction on a link `L`, over the shared
    QOU obstruction context.

    A `definition` carrier: the additive resolution-tree restriction map `res`
    (from `HH² ≅ k = ℤ` to the coefficient ring `R`) and the obstruction
    `κ = res(χ(A))`, where `χ(A) = octx.chi_A` is the **canonical**
    universal class carried by `QouObstructionReductionContext`. -/
structure SkeinResolutionObstruction (R : Type*) [CommRing R]
    [octx : QouObstructionReductionContext] where
  /-- The resolution-tree restriction map (additive), `HH² ≅ ℤ → R`. -/
  res : ℤ →+ R
  /-- The Skein resolution obstruction `κ = res(χ(A))`. -/
  κ : R
  /-- `κ` is the restriction of the *canonical* universal obstruction class. -/
  κ_def : κ = res octx.chi_A

namespace SkeinResolutionObstruction

variable {R : Type*} [CommRing R] [octx : QouObstructionReductionContext]
    (S : SkeinResolutionObstruction R)

/-- A vanishing Euler characteristic forces the resolution obstruction to
    vanish: if `χ(A) = 0` then `κ_c^comp(L,q) = 0` (the degree-0 answer is
    extractable). Now derived through the shared context's `chi_A`, not a
    free-field hypothesis. -/
theorem kappa_eq_zero_of_chi_zero (h : octx.chi_A = 0) : S.κ = 0 := by
  rw [S.κ_def, h, map_zero]

/-- Consistency with the Kummer obstruction of `qou_obstruction_reduction`:
    when `χ(A) = 0` every Kummer level vanishes (`n ∣ 0`), so the Skein
    obstruction agrees with the categorical obstruction reduction — they are
    evaluations of the same class. -/
theorem kummer_vanishes_of_chi_zero (h : octx.chi_A = 0) (n : ℕ) :
    octx.kappa_vanishes n := by
  rw [QOU.AlgebraicSubstrate.kappa_vanishes_iff_chi n, h]
  exact dvd_zero _

end SkeinResolutionObstruction

-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/skein-resolution-obstruction.ts

end QOU
