import QOU.Archimedean.TotallyGeodesicFaces
import QOU.Archimedean.HyperbolicGeodesicUniqueness

/-!
# T2 — the totally-geodesic classification, made UNCONDITIONAL (zero citation).

This capstone closes the T2 development. The classification "the vertical planes
and hemispheres of the upper half-space model `H³` are totally geodesic" was
originally *cited* (Thurston, GT3M Ch. 2 §2.3). Over the T2 arc it was reduced to
a proof conditional on a single named conjecture, `HypMinimizerUnique` (existence
+ uniqueness of constant-speed length-minimisers in `H³`), and then that
conjecture was itself **derived, sorry-free**:

* **WALL-2** (`HyperbolicNormalization.exists_normalization` /
  `exists_normalization_isom`) — any two points of `H³` are carried to the
  `z`-axis by a `dH`-isometry with a `dH`-isometry left inverse;
* **WALL-4** (`HyperbolicGeodesicZAxisUniqueness.zaxis_minimizer_eq_vseg`) — a
  constant-speed minimiser between two `z`-axis points is the vertical segment;
* **WALL-5** (`HyperbolicGeodesicUniqueness.hypMinimizerUnique_derived`) —
  assembles the two into a genuine witness of `HypMinimizerUnique`.

`hypMinimizerUnique_derived` was deliberately kept a `def` so that promoting it to
a global `instance` — which auto-discharges every `[HypMinimizerUnique]`
hypothesis across the corpus — was a separate, explicit step. This file takes that
step (owner-authorised), and restates the two corpus-face classification theorems
in their now-**unconditional** form.

Everything here is `ℝ`/archimedean (real analysis) — §7c. `#print axioms` on the
unconditional theorems shows only `[propext, Classical.choice, Quot.sound]`: no
`sorryAx`, no new axiom, no remaining conjecture. **T2 is at zero citation.**

-- Ref: [manuscript] beans qou-npxs (wall milestone), qou-0a0z (WALL-2),
--   qou-xidi (WALL-4), qou-r111 (HypMinimizerUnique closure)
-/

namespace QOU.Archimedean

/-- **The T2 geodesic-uniqueness conjecture, promoted to a global instance.**

`HypMinimizerUnique` is no longer open: `hypMinimizerUnique_derived` is a genuine,
machine-verified derivation from WALL-2 + WALL-4. Registering it as an `instance`
makes every `[HypMinimizerUnique]`-conditional theorem in the corpus
unconditional. It is a `Prop` class (proof-irrelevant), so this introduces no
diamond. -/
instance instHypMinimizerUnique : HypMinimizerUnique := hypMinimizerUnique_derived

/-- **The corpus vertical plane is totally geodesic — UNCONDITIONALLY.**

The exact vertical faces the ideal tetrahedron intersects (`verticalPlaneE n d`,
any unit base normal `n`, any offset `d`) are totally geodesic, with no remaining
hypothesis: the `[HypMinimizerUnique]` of `verticalPlane_isTotallyGeodesic` is now
discharged by `instHypMinimizerUnique`. -/
theorem verticalPlane_isTotallyGeodesic_uncond {n : ℝ × ℝ}
    (hn : n.1 ^ 2 + n.2 ^ 2 = 1) (d : ℝ) :
    IsTotallyGeodesic (verticalPlaneE n d) :=
  verticalPlane_isTotallyGeodesic hn d

/-- **The corpus hemisphere is totally geodesic — UNCONDITIONALLY.**

The exact hemispherical face the ideal tetrahedron intersects (`hemisphereE R`,
any radius `R > 0`) is totally geodesic, with no remaining hypothesis. -/
theorem hemisphere_isTotallyGeodesic_uncond {R : ℝ} (hR : 0 < R) :
    IsTotallyGeodesic (hemisphereE R) :=
  hemisphere_isTotallyGeodesic hR

end QOU.Archimedean
