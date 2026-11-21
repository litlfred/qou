/-
# T2 — the ideal-tetrahedron volume identity.  The ideal tetrahedron is now an
# INDEPENDENT object and `region = chimney` is a PROVED theorem, closed MODULO
# ONE relocated cited fact (the totally-geodesic-plane model).

## Status (read this before citing — honest proven-vs-cited split)

**UPGRADE (region independence, PR #5176 / beans qou-idvt, qou-473l).**  The
former version adopted the chimney AS the ideal-tetrahedron region and proved
`region_eq_chimney` by `rfl`.  That has been replaced: the ideal tetrahedron is
now DEFINED from its four ideal vertices (`idealTetrahedron` in
`IdealTetFromVertices`, the intersection of four geodesic half-spaces built via
`IdealBoundaryGeodesicPlane`), and `region_eq_chimney` is a **proved set-equality**
(`idealTet_eq_chimney`, File A3), sorry-free, axioms
`[propext, Classical.choice, Quot.sound]` only.

**Proved in Lean, sorry-free, no new axiom:**

1. **Conformality** (`hypAngle_eq_angle`): the upper half-space metric is
   conformal, so a dihedral angle read off Euclidean face tangents at any height
   IS the hyperbolic dihedral angle.
2. **The chimney's three ∞-edge dihedral angles are `(α, β, γ)`**
   (`chimney_infedge_dihedral_eq_vertexAngle`) — a genuine computation, with the
   interior orientation of the edge-perpendicular in-face vectors certified
   (`infedge_orientation_*`).  `α + β + γ = π` is what forces the values.
3. **The chimney's genuine hyperbolic volume is `Λ(α)+Λ(β)+Λ(γ)`**
   (`hypVolume_chimney_inscribedTriangle`, pre-existing) against `dx dy dz / z³`.
4. **NEW: `idealTetrahedron … = chimney …`** (`idealTet_eq_chimney`, File A3) — the
   vertex-defined region equals the Milnor chimney, proved by DERIVING the three
   chord half-planes from the three vertical faces (via `sarea_circlePoint_unit`
   and the vertex-incidence orientation) and matching the hemisphere face to the
   chimney floor.  This is what makes `region_eq_chimney` a real proof.

**Cited, NOT proved in Lean — a single fact, now RELOCATED to File A1:**

* **The totally-geodesic-plane classification** ([ratcliffe] §4.6–4.7;
  [thurston1978] Ch. 7): in the upper half-space model the totally-geodesic planes
  ARE the vertical Euclidean planes and the hemispheres centred on `∂H³`.  This is
  ADOPTED as the concrete geodesic-plane model in
  `IdealBoundaryGeodesicPlane.geodesicPlaneThrough` — a **definition with a
  citation**, on the same footing as `hypVolume := dx dy dz / z³` and `hypAngle`
  are adopted in this corpus.  It is **not** an `axiom` and **not** a `sorry`; a
  reader who declines it reads every downstream theorem as a statement about the
  concrete Euclidean sets, one who grants it reads them as statements about genuine
  geodesic faces.  This is the ONLY residual — NOT a from-metric proof (Mathlib
  4.24.0 has no hyperbolic metric), and honestly so.

## What is NOT claimed (do not oversell)

This is **not** "T2 proved unconditionally with zero citations" — that is
impossible in Mathlib 4.24.0.  The deliverable is precisely: *the ideal
tetrahedron is independently defined, `region = chimney` is PROVED, and the sole
residual is the relocated geodesic-plane model-faithfulness citation.*  The
`MostowIdealTetVolume` class is now **optional**: `idealTetVolume_of_vertices`
gives the volume identity for the concrete vertex-defined region WITHOUT the class.

Archimedean (ℝ): `Λ`, the hyperbolic volume measure, ordering, `π` — §7c.

-- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
--      (Appendix: the ideal-simplex volume formula and the normalized position)
-- Ref: [thurston1978] Ch. 7 (ideal simplices, geodesic faces, the Lobachevsky function)
-- Ref: [ratcliffe] §4.6–4.7 (the totally-geodesic-plane classification, cited in File A1)
-- Ref: [leitner2026] beans qou-idvt (T2), qou-5gai (H1–H5), qou-krvm (iv), qou-473l
-/

import QOU.Archimedean.OrthoschemeTiling
import QOU.Archimedean.IdealTetFacesFromInscribedTriangle
import QOU.Archimedean.IdealTetEqChimney

-- The class name intentionally repeats the namespace tail (per the block's `lean.ref`
-- convention, as in `RealisationVolumeCompatibility`); the resulting duplicated-namespace
-- lint is cosmetic and disabled here.
set_option linter.dupNamespace false

namespace QOU.Archimedean.MostowIdealTetVolume

open MeasureTheory
open QOU.Archimedean
open QOU.Archimedean.HyperbolicVolume

-- @conjecture: primary  (T2 geometric input — depends on no other conjecture class)

/-- **The ideal-tetrahedron region + its dihedral angles, as a §3b conditional
class.**

A datum supplies, for every acute admissible dihedral-angle triple `(α, β, γ)`,
the region `tetRegion α β γ` that a genuine ideal tetrahedron of those dihedral
angles occupies in Milnor's normalized position, together with:

* `region_eq_chimney`: the region IS a vertical chimney over the inscribed
  triangle (Milnor's normalization — the cited geometric input); and
* `tetDihedralAngles`: the region's **three ∞-edge dihedral angles are
  `(α, β, γ)`** — the real geometric content, PROVED in File 4 for the chimney
  (`chimney_infedge_dihedral_eq_vertexAngle`).  This field carries the dihedral
  angles, not the volume conclusion, and cannot be met by an arbitrary chimney
  over the wrong triangle. -/
class MostowIdealTetVolume where
  /-- The region an ideal tetrahedron of dihedral angles `(α, β, γ)` occupies in
  the upper half-space `H³`, in Milnor's normalized position. -/
  tetRegion : ℝ → ℝ → ℝ → Set (Fin 3 → ℝ)
  /-- **Milnor's normalization (cited geometric input).**  For an acute admissible
  triple, the region equals the vertical chimney over the inscribed triangle. -/
  region_eq_chimney : ∀ {α β γ : ℝ}, 0 < α → 0 < β → 0 < γ →
    α < Real.pi / 2 → β < Real.pi / 2 → γ < Real.pi / 2 → α + β + γ = Real.pi →
    ∃ t : ℝ, tetRegion α β γ = chimney (inscribedTriangle 1 t α β γ) 1
  /-- **The dihedral-angle content (PROVED in File 4 for the realizing chimney).**
  There is a normalized position `t` in which the region is the chimney over the
  inscribed triangle AND the three ∞-edge dihedral angles — the hyperbolic angles
  between the interior edge-perpendicular in-face vectors of the pairs of vertical
  faces — are exactly `(α, β, γ)`.  This is the real geometric content the class
  requires of an instance; it is discharged by
  `chimney_infedge_dihedral_eq_vertexAngle`. -/
  tetDihedralAngles : ∀ {α β γ : ℝ}, 0 < α → 0 < β → 0 < γ →
    α < Real.pi / 2 → β < Real.pi / 2 → γ < Real.pi / 2 → α + β + γ = Real.pi →
    ∃ t : ℝ, tetRegion α β γ = chimney (inscribedTriangle 1 t α β γ) 1
      ∧ dihedralAngle 1 (edgePerp (chordNormal (t + γ)) 1)
          (edgePerp (chordNormal (t + 2 * γ + 2 * α + β)) (-1)) = α
      ∧ dihedralAngle 1 (edgePerp (chordNormal (t + γ)) (-1))
          (edgePerp (chordNormal (t + 2 * γ + α)) 1) = β
      ∧ dihedralAngle 1 (edgePerp (chordNormal (t + 2 * γ + α)) (-1))
          (edgePerp (chordNormal (t + 2 * γ + 2 * α + β)) 1) = γ

/-- **T2, on the class (§3b-cond).**  The genuine hyperbolic volume
`dx dy dz / z³` of the ideal-tetrahedron region of acute dihedral angles
`(α, β, γ)` equals `Λ(α) + Λ(β) + Λ(γ)`.

**Derived, not assumed**: the class supplies only that the region is a chimney
(`region_eq_chimney`); the volume value comes from the already-PROVED, sorry-free
`hypVolume_chimney_inscribedTriangle`.  The proof does real work — `rw` the region
identity, then discharge with the proved analytic theorem. -/
theorem idealTetVolume_eq_lambda_sum [MostowIdealTetVolume]
    {α β γ : ℝ} (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ)
    (hα : α < Real.pi / 2) (hβ : β < Real.pi / 2) (hγ : γ < Real.pi / 2)
    (hsum : α + β + γ = Real.pi) :
    hypVolume (MostowIdealTetVolume.tetRegion α β γ)
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  obtain ⟨t, ht⟩ :=
    MostowIdealTetVolume.region_eq_chimney hα0 hβ0 hγ0 hα hβ hγ hsum
  rw [ht]
  exact hypVolume_chimney_inscribedTriangle (by norm_num) hα0 hβ0 hγ0 hα hβ hγ hsum

/-- **The REAL instance — now with the region-equality PROVED, not adopted.**  The
ideal-tetrahedron region is the *independently defined* `idealTetrahedron` of File A2
(the intersection of four geodesic half-spaces built from the four ideal vertices),
NOT a chimney by fiat.  `region_eq_chimney` is now discharged by the **proved**
set-equality `idealTet_eq_chimney` (File A3) — a genuine theorem replacing the former
`rfl` — and `tetDihedralAngles` by the File-4 proof that the chimney's three ∞-edge
dihedral angles are `(α, β, γ)`.

This is the anti-laundering content twice over: the region is an independent object,
and BOTH class fields are proved (the region-equality is no longer definitional).  It
closes T2 **modulo the single cited totally-geodesic / normalized-position
identification** (relocated to File A1's `geodesicPlaneThrough` — a definition with a
citation, not an axiom or `sorry`). -/
instance instMostowIdealTetVolume : MostowIdealTetVolume where
  tetRegion := fun α _β γ =>
    idealTetrahedron (circlePoint 1 0) (circlePoint 1 (0 + 2 * γ))
      (circlePoint 1 (0 + 2 * γ + 2 * α))
  -- The three acuteness binders `_hα _hβ _hγ` are demanded by the class field's
  -- type, not by the proof: `idealTet_eq_chimney` dropped them (they were carried
  -- but never used — see its docstring), so this instance discharges the field
  -- from positivity and `hsum` alone.
  region_eq_chimney := fun hα0 hβ0 hγ0 _hα _hβ _hγ hsum =>
    ⟨0, idealTet_eq_chimney hα0 hβ0 hγ0 hsum⟩
  tetDihedralAngles := fun hα0 hβ0 hγ0 hα hβ hγ hsum =>
    ⟨0, idealTet_eq_chimney hα0 hβ0 hγ0 hsum,
      (chimney_infedge_dihedral_eq_vertexAngle hα0 hβ0 hγ0 hα hβ hγ hsum).1,
      (chimney_infedge_dihedral_eq_vertexAngle hα0 hβ0 hγ0 hα hβ hγ hsum).2.1,
      (chimney_infedge_dihedral_eq_vertexAngle hα0 hβ0 hγ0 hα hβ hγ hsum).2.2⟩

/-- **T2, UNCONDITIONAL (no class) — the volume of the independently-defined ideal
tetrahedron.**  For an acute admissible triple `α + β + γ = π`, the genuine hyperbolic
volume `dx dy dz / z³` of the vertex-defined region
`idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t+2γ)) (circlePoint 1 (t+2γ+2α))`
is `Λ(α) + Λ(β) + Λ(γ)`.

This does **not** go through the `MostowIdealTetVolume` class: the region is defined
from its four ideal vertices (File A2), proved equal to the chimney (File A3), and the
chimney's volume is the already-proved `hypVolume_chimney_inscribedTriangle`.  The
class above is now *optional* — a labelled §3b-cond packaging — since the volume
identity holds unconditionally for the concrete region.  Closed modulo the single
cited totally-geodesic model-faithfulness fact (File A1); everything else is
Lean-proved, sorry-free.

The acuteness here is REAL, unlike the acuteness `idealTet_eq_chimney` used to
carry: it is consumed by `hypVolume_chimney_inscribedTriangle`, whose wedges need
`ψ < π/2`.  The obtuse companion is
`ObtuseTiling.idealTetVolume_of_vertices_obtuse`, which swaps that one step for
the obtuse tiling and is otherwise the same two lines. -/
theorem idealTetVolume_of_vertices {t α β γ : ℝ}
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ)
    (hα : α < Real.pi / 2) (hβ : β < Real.pi / 2) (hγ : γ < Real.pi / 2)
    (hsum : α + β + γ = Real.pi) :
    hypVolume (idealTetrahedron (circlePoint 1 t) (circlePoint 1 (t + 2 * γ))
        (circlePoint 1 (t + 2 * γ + 2 * α)))
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  rw [idealTet_eq_chimney hα0 hβ0 hγ0 hsum]
  exact hypVolume_chimney_inscribedTriangle (by norm_num) hα0 hβ0 hγ0 hα hβ hγ hsum

/-- **`idealTetVolume_eq_lambda_sum` fires unconditionally** — confirming the
class is inhabited by the real instance above.  For the Milnor-normalized
ideal-tetrahedron region of acute dihedral angles `(α, β, γ)`, the genuine
hyperbolic volume is `Λ(α) + Λ(β) + Λ(γ)`.

Closed modulo the cited totally-geodesic / normalized-position identification (the
one fact Mathlib cannot express); everything else is Lean-proved, sorry-free. -/
theorem idealTetVolume_fires {α β γ : ℝ} (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ)
    (hα : α < Real.pi / 2) (hβ : β < Real.pi / 2) (hγ : γ < Real.pi / 2)
    (hsum : α + β + γ = Real.pi) :
    hypVolume (MostowIdealTetVolume.tetRegion α β γ)
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) :=
  idealTetVolume_eq_lambda_sum hα0 hβ0 hγ0 hα hβ hγ hsum

/-- **The dihedral-angle field is genuinely restrictive (§3b-tax non-degeneracy).**
The whole space `ℝ³` cannot be a `region_eq_chimney` region: a chimney lies inside
the upper half-space (`chimney_subset_upperHalfSpace`), so the point at height `-1`
is in `univ` but in no chimney.  Together with `tetDihedralAngles` requiring the
*correct* vertex angles, the class asserts real content — it is not
auto-satisfiable. -/
theorem region_eq_chimney_is_restrictive :
    ¬ ∀ {α β γ : ℝ}, 0 < α → 0 < β → 0 < γ →
        α < Real.pi / 2 → β < Real.pi / 2 → γ < Real.pi / 2 → α + β + γ = Real.pi →
        ∃ t : ℝ, (Set.univ : Set (Fin 3 → ℝ)) = chimney (inscribedTriangle 1 t α β γ) 1 := by
  intro h
  have hpos : (0 : ℝ) < Real.pi / 3 := by positivity
  have hlt : Real.pi / 3 < Real.pi / 2 := by
    have hπ : 0 < Real.pi := Real.pi_pos
    linarith
  have hsum : Real.pi / 3 + Real.pi / 3 + Real.pi / 3 = Real.pi := by ring
  obtain ⟨t, hU⟩ := h hpos hpos hpos hlt hlt hlt hsum
  have hmem : (fun _ : Fin 3 => (-1 : ℝ))
      ∈ chimney (inscribedTriangle 1 t (Real.pi / 3) (Real.pi / 3) (Real.pi / 3)) 1 := by
    rw [← hU]; trivial
  have hup := chimney_subset_upperHalfSpace _ _ hmem
  simp only [upperHalfSpace, Set.mem_setOf_eq] at hup
  norm_num at hup

end QOU.Archimedean.MostowIdealTetVolume
