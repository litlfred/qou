/-
# The ideal-tetrahedron volume `D(z)` IS the genuine measure of the normalized chimney

**Unconditional, sorry-free, no new axiom.**  This is the sharpest *volume-level*
statement the corpus can make about the ideal-tetrahedron volume without the
missing hyperbolic-geometry primitives — and it is strictly weaker than T2.

## What this proves

For a shape parameter `z` in the upper half plane whose three dihedral angles
`(tetAngle₁ z, tetAngle₂ z, tetAngle₃ z)` are acute, the **Bloch–Wigner volume**
`BlochWigner_lob z = D(z)` — which is exactly `IdealTetrahedron.volume`
(`QOU/MathlibExt/IdealTriangulation.lean`, `volume := BlochWigner_lob shape`) —
equals the **genuine hyperbolic measure** `dx dy dz / z³`
(`HyperbolicVolume.hypVolume`) of the concrete vertical chimney over the
inscribed triangle of those angles in Milnor's normalized position:

    hypVolume (chimney (inscribedTriangle 1 t (α z) (β z) (γ z)) 1) = ENNReal.ofReal (D(z))

Both sides are `Λ(α) + Λ(β) + Λ(γ)`: the left by the already-proved, sorry-free
`hypVolume_chimney_inscribedTriangle` (Milnor's circumcentre subdivision against
the genuine `dV = dx dy dz / z³` measure); the right by the *definition* of
`BlochWigner_lob` as that same Λ-sum.

## Why it is worth stating (and what it upgrades)

`IdealTetrahedron.volume` carries a standing apology in its own docstring:
*"the identification with a hyperbolic volume in the metric sense is not
available."*  For **acute** shapes this bridge supplies exactly that missing
measure-theoretic identification: `D(z)` is not merely a dilogarithm number, it
is the honest `hypVolume` of a concrete region of `H³`.  Nothing previously
stated the link `hypVolume(chimney …) = D(z)`; the two facts
(`hypVolume(chimney) = Λ-sum` and `D(z) = Λ-sum`) sat in different subsystems
(Archimedean measure vs. Knot / Bloch–Wigner) with no theorem joining them.

## 🛑 WHAT THIS DOES **NOT** DO — read before citing (the T2 guard)

This is an equality of **volumes** (a single non-negative real), **NOT** an
equality of **regions**.  It does **NOT** prove that the ideal tetrahedron of
dihedral angles `(α, β, γ)` *is* this chimney — equal volume is not equal set,
and infinitely many regions share a measure.  Concretely:

* It does **NOT** prove, and does not depend on, `MostowIdealTetVolume`'s
  `region_eq_chimney` (the genuine `tetRegion = chimney` identification).  **T2
  (`qou-idvt`) remains OPEN**: Mathlib has no ideal simplices, so the
  ideal-tetrahedron *region* is not even definable, let alone equal to the
  chimney.  This bridge sidesteps the region entirely by working with the
  *defined* scalar `D(z)`.
* It does **NOT** discharge `qou-krvm` (iv).  That hypothesis is about the
  concavity / invariance of the volume functional on the angle-structure
  polytope; the analytic half was already done (`tetVol_strictConcaveOn`), and
  the geometric half (T2) is still conditional-on-class in
  `MostowIdealTetVolume.idealTetVolume_eq_lambda_sum`.  This file adds no
  instance and no axiom.

So this is a genuine cross-subsystem *volume* identity — the honest ceiling of
what is provable while the region identification is missing — and it is
deliberately labelled as such.

Archimedean (ℝ, ℂ): `arg`, `Λ`, the hyperbolic measure, ordering, `π` — §7c.

-- Ref: [milnor1982] Appendix (the Λ-sum volume of an ideal tetrahedron)
-- Ref: [thurston1978] Ch. 7 (shape parameters and ideal simplices)
-- Ref: [leitner2026] beans qou-idvt (T2, still open), qou-krvm (iv), qou-7y3g
-/

import QOU.Archimedean.OrthoschemeTiling
import QOU.Archimedean.BlochWignerLobachevsky

namespace QOU.Archimedean.IdealTetVolumeChimneyBridge

open MeasureTheory
open QOU.Archimedean
open QOU.Archimedean.HyperbolicVolume

/-- **The Bloch–Wigner ideal-tetrahedron volume `D(z)` equals the genuine
hyperbolic measure of the normalized chimney over its inscribed triangle.**

For `z` in the upper half plane with acute dihedral angles, `BlochWigner_lob z`
(= `IdealTetrahedron.volume` for the ideal tetrahedron of shape `z`) is the
`dx dy dz / z³` measure of the concrete vertical chimney over the inscribed
triangle at radius `1`, in Milnor's normalized position.

**Unconditional and sorry-free**; it uses no `MostowIdealTetVolume` instance.
It is an equality of *volumes*, not of *regions* — see the module header: it does
NOT prove the ideal tetrahedron IS the chimney (T2 / `region_eq_chimney` stays
open), and it does NOT discharge `qou-krvm` (iv). -/
theorem blochWigner_lob_eq_hypVolume_chimney
    (z : ℂ) (t : ℝ) (hz : 0 < z.im)
    (hα : tetAngle₁ z < Real.pi / 2)
    (hβ : tetAngle₂ z < Real.pi / 2)
    (hγ : tetAngle₃ z < Real.pi / 2) :
    hypVolume (chimney (inscribedTriangle 1 t (tetAngle₁ z) (tetAngle₂ z) (tetAngle₃ z)) 1)
      = ENNReal.ofReal (BlochWigner_lob z) := by
  have h1 : 0 < tetAngle₁ z := (arg_mem_Ioo_of_im_pos z hz).1
  have h2 : 0 < tetAngle₂ z := (arg_mem_Ioo_of_im_pos _ (tet_im_pos z hz).1).1
  have h3 : 0 < tetAngle₃ z := (arg_mem_Ioo_of_im_pos _ (tet_im_pos z hz).2).1
  have hsum : tetAngle₁ z + tetAngle₂ z + tetAngle₃ z = Real.pi :=
    tetAngles_sum_eq_pi z hz
  rw [hypVolume_chimney_inscribedTriangle (by norm_num) h1 h2 h3 hα hβ hγ hsum]
  rfl

end QOU.Archimedean.IdealTetVolumeChimneyBridge
