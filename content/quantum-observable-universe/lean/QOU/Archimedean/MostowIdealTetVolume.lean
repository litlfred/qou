/-
# T2 — the ideal-tetrahedron volume identity, as a §3b-cond conditional class

**This file does NOT prove T2 and does NOT close `qou-krvm` (iv)** (AGENTS.md
§"Axiomatization is NOT a Proof").  It records the *exact* remaining geometric
gap and packages it honestly: the open geometric input is axiomatised as a
§3b-cond conditional class, and the ideal-tetrahedron volume identity is
**derived** from it by composing with an already-PROVED analytic theorem — never
projected out of the class.

## What T2 is, and how much of it is already proved (READ THIS FIRST)

T2 (`qou-idvt`) is Milnor's volume formula: the hyperbolic volume of the ideal
tetrahedron with dihedral angles `(α, β, γ)` (a positive triple summing to `π`)
equals `Λ(α) + Λ(β) + Λ(γ)`, `Λ` the Lobachevsky function.

The framework has already proved the **analytic** content of this, sorry-free,
against the genuine hyperbolic volume measure `dV = dx dy dz / z³`
(`HyperbolicVolume.hypVolume`, `HyperbolicVolumeMeasure.lean`):

    hypVolume_chimney_inscribedTriangle   (QOU.Archimedean.OrthoschemeTiling)
      : hypVolume (chimney (inscribedTriangle R t α β γ) R)
          = ENNReal.ofReal (Lob α + Lob β + Lob γ)

for acute admissible `(α, β, γ)`.  Here `chimney T R` is the solid over the base
`T` above the hemisphere of radius `R` (`IdealTetrahedronRegion.lean`), and
`inscribedTriangle` is the Euclidean triangle inscribed in the disk with
inscribed angles `(α, β, γ)`.  So **the hard part — that the Λ-sum is the real
hyperbolic volume of a concrete region — is DONE**, via Milnor's circumcentre
subdivision (`OrthoschemeLambdaSum.lean`, `OrthoschemeTiling.lean`).

## The one thing that is NOT proved, stated precisely

What is missing is Milnor's **geometric identification** ([milnor1982] Appendix):
that the chimney over the inscribed triangle IS the ideal tetrahedron of the
corresponding dihedral angles, placed in his normalized position (one face on
the unit hemisphere, opposite vertex at `∞`).  Establishing this in Lean requires
hyperbolic-geometry primitives Mathlib does **not** have — measured over the
restored olean tree (`lake-cache/qou-v4-24-0`, 6990 modules): 0 modules matching
`*hyperbol*`, no ideal points of `H³`, no geodesic faces, no ideal simplex, no
dihedral angle of an ideal simplex, no Mostow rigidity.  See beans `qou-idvt` T2
and `qou-5gai`.

## What this file does — a §3b-cond conditional class (Option B)

`MostowIdealTetVolume` axiomatises **the geometric input, not the conclusion**.
Its content field `region_eq_chimney` says: the region an ideal tetrahedron of
acute dihedral angles `(α, β, γ)` occupies in the upper half-space model, in
Milnor's normalized position, equals a vertical chimney over the inscribed
triangle.  This is the open T2 geometric fact — a **primary conjecture**.

The downstream theorem `idealTetVolume_eq_lambda_sum` then **derives** the volume
identity, discharging its own goal by `rw`-ing the region identity and applying
the PROVED `hypVolume_chimney_inscribedTriangle`.  It is NOT a self-assuming
projection (§3b-cond rule 5): the class carries the region *hypothesis*, and the
theorem does the genuine work of composing it with proved analytic content to
reach a conclusion the class never states.

`mostow_shape_witness` proves the class is *inhabitable* (§3b-tax non-vacuity)
by exhibiting a datum whose region literally IS a chimney — a **shape-witness**,
explicitly NOT the framework's genuine ideal tetrahedron.  It is deliberately an
`example`, not a global `instance`: there is **no** ambient instance, so
`idealTetVolume_eq_lambda_sum` stays genuinely conditional and cannot fire on any
concrete tetrahedron.  The genuine identification — that the framework's ideal
simplex realizes as this chimney — is the open conjecture, and is left with no
instance (the honest open state).

`region_eq_chimney_is_restrictive` records §3b-tax non-degeneracy: the content
field is a real constraint, not auto-satisfied by an arbitrary region map.

Archimedean (ℝ): `Λ`, the hyperbolic volume measure, ordering, `π` — §7c.

-- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
--      (Appendix: the ideal-simplex volume formula and the normalized position)
-- Ref: [thurston1978] Ch. 7 (ideal simplices, the Lobachevsky function)
-- Ref: [manuscript] beans qou-idvt (T2), qou-5gai (H1–H5), qou-krvm (iv)
-/

import QOU.Archimedean.OrthoschemeTiling

namespace QOU.Archimedean.MostowIdealTetVolume

open MeasureTheory
open QOU.Archimedean
open QOU.Archimedean.HyperbolicVolume

-- @conjecture: primary  (T2 geometric input — depends on no other conjecture class)

/-- **T2 geometric input, axiomatised as an open §3b conditional class.**

A datum of this class supplies, for every acute admissible dihedral-angle triple
`(α, β, γ)`, the region `tetRegion α β γ ⊆ upper half-space` that a genuine ideal
tetrahedron of those dihedral angles occupies in Milnor's normalized position —
together with the **open geometric fact** `region_eq_chimney`: that this region
IS a vertical chimney over the inscribed triangle of inscribed angles `(α, β, γ)`
at radius `1`.  Mathlib has no hyperbolic geometry, so this identification cannot
be proved; it is carried here as the conjectural hypothesis.  The class states an
*input*, never the volume conclusion — that is derived downstream. -/
class MostowIdealTetVolume where
  /-- The region an ideal tetrahedron of dihedral angles `(α, β, γ)` occupies in
  the upper half-space `H³`, in Milnor's normalized position. -/
  tetRegion : ℝ → ℝ → ℝ → Set (Fin 3 → ℝ)
  /-- **The open geometric input (T2).**  For an acute admissible triple, the
  ideal tetrahedron's region equals the vertical chimney over the inscribed
  triangle — Milnor's normalization.  This is the fact Mathlib's missing
  hyperbolic geometry would supply; it is the conjectural content of the class. -/
  region_eq_chimney : ∀ {α β γ : ℝ}, 0 < α → 0 < β → 0 < γ →
    α < Real.pi / 2 → β < Real.pi / 2 → γ < Real.pi / 2 → α + β + γ = Real.pi →
    ∃ t : ℝ, tetRegion α β γ = chimney (inscribedTriangle 1 t α β γ) 1

/-- **T2, conditional on `MostowIdealTetVolume` (§3b-cond).**  Given the geometric
input, the genuine hyperbolic volume `dx dy dz / z³` of the ideal tetrahedron of
acute dihedral angles `(α, β, γ)` equals `Λ(α) + Λ(β) + Λ(γ)`.

This is **derived, not assumed**: the class supplies only that the region is a
chimney (`region_eq_chimney`); the volume value comes from the already-PROVED,
sorry-free `hypVolume_chimney_inscribedTriangle`.  The proof does real work —
`rw` the region identity, then discharge with the proved analytic theorem — so it
is not a self-assuming projection.  Fully verified **modulo the class instance**;
the instance for the framework's genuine ideal tetrahedron is the open conjecture
(no such instance is provided). -/
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

/-- **Non-vacuity (§3b-tax) — the class shape is inhabitable.**

Taking `tetRegion α β γ` to be *literally* the chimney over the inscribed
triangle satisfies `region_eq_chimney` (with `t = 0`, by `rfl`).  So the class is
not empty and `idealTetVolume_eq_lambda_sum` is not vacuous.

This is a **shape-witness only** — its `tetRegion` is a Euclidean chimney, NOT the
hyperbolic ideal tetrahedron — so it is an `example`, deliberately not a global
`instance`.  With no ambient instance, `idealTetVolume_eq_lambda_sum` remains
genuinely conditional and cannot be applied to any concrete ideal tetrahedron.
The genuine identification is the open conjecture. -/
example : Nonempty MostowIdealTetVolume :=
  ⟨{ tetRegion := fun α β γ => chimney (inscribedTriangle 1 0 α β γ) 1
     region_eq_chimney := fun _ _ _ _ _ _ _ => ⟨0, rfl⟩ }⟩

/-- **The content field is a genuine restriction (§3b-tax non-degeneracy).**  Not
every region map satisfies `region_eq_chimney`: a datum whose region is all of
`ℝ³` fails it, because a chimney lies inside the upper half-space
(`chimney_subset_upperHalfSpace`) and so cannot be the whole space — the point at
height `-1` is in `univ` but in no chimney.  So the class asserts real content —
it is not auto-satisfiable. -/
theorem region_eq_chimney_is_restrictive :
    ¬ ∀ {α β γ : ℝ}, 0 < α → 0 < β → 0 < γ →
        α < Real.pi / 2 → β < Real.pi / 2 → γ < Real.pi / 2 → α + β + γ = Real.pi →
        ∃ t : ℝ, (Set.univ : Set (Fin 3 → ℝ)) = chimney (inscribedTriangle 1 t α β γ) 1 := by
  intro h
  -- the equilateral triple (π/3, π/3, π/3) is acute and admissible
  have hpos : (0 : ℝ) < Real.pi / 3 := by positivity
  have hlt : Real.pi / 3 < Real.pi / 2 := by
    have hπ : 0 < Real.pi := Real.pi_pos
    linarith
  have hsum : Real.pi / 3 + Real.pi / 3 + Real.pi / 3 = Real.pi := by ring
  obtain ⟨t, hU⟩ := h hpos hpos hpos hlt hlt hlt hsum
  -- the constant point at height -1 is in univ but in no chimney (not in H³)
  have hmem : (fun _ : Fin 3 => (-1 : ℝ))
      ∈ chimney (inscribedTriangle 1 t (Real.pi / 3) (Real.pi / 3) (Real.pi / 3)) 1 := by
    rw [← hU]; trivial
  have hup := chimney_subset_upperHalfSpace _ _ hmem
  simp [upperHalfSpace] at hup

end QOU.Archimedean.MostowIdealTetVolume
