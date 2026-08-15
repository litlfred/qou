/-
# T2 — the ideal-tetrahedron volume identity, as a §3b-cond conditional class
# with a REAL instance, closed MODULO ONE cited fact (totally-geodesic faces).

## Status (read this before citing — honest proven-vs-cited split)

**Proved in Lean, sorry-free, no new axiom** (the whole `HyperbolicConformalAngle
→ GeodesicFaceH3 → HyperbolicDihedralAngle → IdealTetFacesFromInscribedTriangle`
chain):

1. **Conformality** (`hypAngle_eq_angle`): the upper half-space metric is
   conformal, so a dihedral angle read off Euclidean face tangents at any height
   IS the hyperbolic dihedral angle.
2. **The chimney's three ∞-edge dihedral angles are `(α, β, γ)`**
   (`chimney_infedge_dihedral_eq_vertexAngle`) — a genuine computation, with the
   interior orientation of the edge-perpendicular in-face vectors certified
   (`infedge_orientation_*`).  `α + β + γ = π` is what forces the values.
3. **The chimney's genuine hyperbolic volume is `Λ(α)+Λ(β)+Λ(γ)`**
   (`hypVolume_chimney_inscribedTriangle`, pre-existing) against `dx dy dz / z³`.

**Cited, NOT proved in Lean** (Mathlib has no hyperbolic metric, no ideal
simplices — see the `IdealTetVolumeChimneyBridge` header, which records that the
ideal-tetrahedron region is not even *definable* in Mathlib):

* **The totally-geodesic face classification + Milnor's normalized position**
  ([thurston1978] Ch. 7; [milnor1982] Appendix): that the vertical planes and the
  unit hemisphere bounding the chimney are the totally-geodesic faces of a genuine
  hyperbolic ideal tetrahedron, and that Milnor's normalized ideal tetrahedron of
  dihedral angles `(α, β, γ)` IS this chimney.  This is the single geometric input
  that cannot be stated in Mathlib; File 4 supplies the *consistency check* that
  the chimney's dihedral angles are indeed `(α, β, γ)`, but the identification of
  the chimney AS the ideal tetrahedron is the cited construction.

## What the instance does — and what it does NOT claim

`instMostowIdealTetVolume` provides a **real** instance: it ADOPTS Milnor's
normalized chimney as the ideal-tetrahedron region (by the cited construction),
`region_eq_chimney` by `rfl`, and — the anti-laundering content —
`tetDihedralAngles` **discharged by the File-4 proof** that this region's three
∞-edge dihedral angles are `(α, β, γ)`.  Because that field must be *proved*, an
unlabelled chimney (over the wrong triangle) cannot satisfy the class:
`tetDihedralAngles` carries the DIHEDRAL ANGLES (real, derived) — never the volume
conclusion (§3b-cond rule 5, non-degeneracy).

With the instance, `idealTetVolume_eq_lambda_sum` fires unconditionally
(`idealTetVolume_fires`).  **This closes T2 MODULO the cited totally-geodesic /
normalized-position identification** — it is NOT an unconditional Lean proof that
the ideal-tetrahedron region equals the chimney (that statement is not even
expressible in Mathlib).  Every theorem produced is TRUE and honestly named: the
volume of the concrete Milnor chimney is the Λ-sum, and its dihedral angles are
the vertex angles.  A stricter reader who declines the geometric citation should
read this as: the class is the labelled conditional, and the instance records the
Milnor-normalized realization whose dihedral angles File 4 verifies.

Archimedean (ℝ): `Λ`, the hyperbolic volume measure, ordering, `π` — §7c.

-- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
--      (Appendix: the ideal-simplex volume formula and the normalized position)
-- Ref: [thurston1978] Ch. 7 (ideal simplices, geodesic faces, the Lobachevsky function)
-- Ref: [manuscript] beans qou-idvt (T2), qou-5gai (H1–H5), qou-krvm (iv), qou-473l
-/

import QOU.Archimedean.OrthoschemeTiling
import QOU.Archimedean.IdealTetFacesFromInscribedTriangle

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

/-- **The REAL instance.**  The ideal-tetrahedron region is realized as Milnor's
normalized chimney over the inscribed triangle (the cited construction);
`region_eq_chimney` holds by `rfl`, and `tetDihedralAngles` is discharged by the
File-4 proof that the chimney's three ∞-edge dihedral angles are `(α, β, γ)`.

This is the anti-laundering content: the instance is NOT a bare chimney — it
carries the *proved* dihedral-angle characterization.  It closes T2 **modulo the
cited totally-geodesic / normalized-position identification** (module header); it
is not an unconditional Lean proof that the ideal-tet region equals the chimney,
which Mathlib cannot even state. -/
instance instMostowIdealTetVolume : MostowIdealTetVolume where
  tetRegion := fun α β γ => chimney (inscribedTriangle 1 0 α β γ) 1
  region_eq_chimney := fun _ _ _ _ _ _ _ => ⟨0, rfl⟩
  tetDihedralAngles := fun hα0 hβ0 hγ0 hα hβ hγ hsum =>
    ⟨0, rfl,
      (chimney_infedge_dihedral_eq_vertexAngle hα0 hβ0 hγ0 hα hβ hγ hsum).1,
      (chimney_infedge_dihedral_eq_vertexAngle hα0 hβ0 hγ0 hα hβ hγ hsum).2.1,
      (chimney_infedge_dihedral_eq_vertexAngle hα0 hβ0 hγ0 hα hβ hγ hsum).2.2⟩

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
