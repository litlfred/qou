/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLMaps
import Mathlib.Analysis.Convex.SimplicialComplex.Basic
import Mathlib.Analysis.Convex.Combination
import Mathlib.Topology.Algebra.Module.FiniteDimension

set_option autoImplicit false

/-!
# Triangulations, subdivisions and regular neighbourhoods (issue #8902, Moise build part A)

Vocabulary for the relative Moise approximation (part B), built on Mathlib's
`Geometry.SimplicialComplex ℝ E` (faces are finite affinely independent vertex sets, glued along
common faces).

## What is a DEFINITION here

* `Triangulates K P` — `K` has finitely many faces and its underlying space is `P`.
* `IsCompactPolyhedron P` — `P` is triangulated by some `K` (the standard PL definition: a compact
  polyhedron is the underlying space of a finite simplicial complex).
* `IsSubcomplex L K`, `IsFull L K` — `L`'s faces are faces of `K`; full: every face of `K` all of
  whose vertices are vertices of `L` is a face of `L`.
* `Subdivides K' K` — same underlying space, and every face of `K'` lies in a face of `K`.
* `IsLinearOn K f` — `f` is affine on every face of `K`.
* `simplicialNbhd K L` — the union of the faces of `K` meeting `L.space`.
* `IsDerived K' K` — `K'` is a derived (barycentric-type) subdivision of `K`: one vertex `a σ` in
  the open simplex of each face `σ` (a centre of mass with all weights positive), and the faces of
  `K'` are the `a`-images of the chains `σ₀ ⊂ ⋯ ⊂ σₖ` of faces of `K` (finite sets of faces totally
  ordered by inclusion).
* `IsRegularNbhd N P M` — `N` is a second-derived neighbourhood of `P` in `M`: `N` is the simplicial
  neighbourhood of `P` in a second derived `K''` of a triangulation `K` of `M` that contains a
  subcomplex triangulating `P` (Rourke–Sanderson, *Introduction to piecewise-linear topology*,
  Ch. 3).

## What is a THEOREM here

* `Triangulates.isCompact` — a triangulated set is compact.
* `Subdivides.refl`, `Subdivides.trans`.
* `IsSubcomplex.space_subset`.
* `IsLinearOn.mono` — linearity on `K` passes to any subdivision `K'`.

## What is NOT proved here

Existence of triangulations of compact PL sets and the uniqueness of regular neighbourhoods
(existence of derived subdivisions is `exists_derived` in `PLBarycentric.lean`). These are classical (Rourke–Sanderson Ch. 2–3) and are not used by the
Alexander trick (`PLAlexander.lean`).
-/

namespace QOU.MathlibExt.PL

open Set Geometry

variable {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F]

/-- `K` **triangulates** `P`: finitely many faces, underlying space `P`. -/
def Triangulates (K : SimplicialComplex ℝ E) (P : Set E) : Prop :=
  K.faces.Finite ∧ K.space = P

/-- A **compact polyhedron**: the underlying space of a finite simplicial complex. -/
def IsCompactPolyhedron (P : Set E) : Prop := ∃ K : SimplicialComplex ℝ E, Triangulates K P

/-- `L` is a **subcomplex** of `K`. -/
def IsSubcomplex (L K : SimplicialComplex ℝ E) : Prop := L.faces ⊆ K.faces

/-- `L` is a **full** subcomplex of `K`. -/
def IsFull (L K : SimplicialComplex ℝ E) : Prop :=
  IsSubcomplex L K ∧ ∀ s ∈ K.faces, (↑s : Set E) ⊆ L.vertices → s ∈ L.faces

/-- `K'` **subdivides** `K`. -/
def Subdivides (K' K : SimplicialComplex ℝ E) : Prop :=
  K'.space = K.space ∧
    ∀ s ∈ K'.faces, ∃ t ∈ K.faces, convexHull ℝ (s : Set E) ⊆ convexHull ℝ (t : Set E)

/-- `f` is **linear on the simplices of `K`**. -/
def IsLinearOn (K : SimplicialComplex ℝ E) (f : E → F) : Prop :=
  ∀ s ∈ K.faces, ∃ A : E →ᴬ[ℝ] F, EqOn f A (convexHull ℝ (s : Set E))

/-- The **simplicial neighbourhood** of `L` in `K`: the faces of `K` meeting `L.space`. -/
def simplicialNbhd (K L : SimplicialComplex ℝ E) : Set E :=
  ⋃ s ∈ {s | s ∈ K.faces ∧ (convexHull ℝ (s : Set E) ∩ L.space).Nonempty},
    convexHull ℝ (s : Set E)

/-- `K'` is a **derived subdivision** of `K`: a point `a σ` in the relative interior of each face
`σ`, and the faces of `K'` are the images of strict chains of faces. -/
def IsDerived (K' K : SimplicialComplex ℝ E) : Prop :=
  ∃ a : Finset E → E,
    (∀ σ ∈ K.faces, ∃ w : E → ℝ, (∀ v ∈ σ, 0 < w v) ∧ ∑ v ∈ σ, w v = 1 ∧
      a σ = σ.centerMass w id) ∧
    K'.faces = {s : Finset E | ∃ C : Finset (Finset E), C.Nonempty ∧ (∀ σ ∈ C, σ ∈ K.faces) ∧
      (∀ σ ∈ C, ∀ τ ∈ C, σ ⊆ τ ∨ τ ⊆ σ) ∧ (s : Set E) = a '' (C : Set (Finset E))}

/-- `N` is a **regular (second-derived) neighbourhood** of `P` in `M`. -/
def IsRegularNbhd (N P M : Set E) : Prop :=
  ∃ K K' K'' L'' : SimplicialComplex ℝ E,
    Triangulates K M ∧ (∃ L, IsSubcomplex L K ∧ L.space = P) ∧
    IsDerived K' K ∧ IsDerived K'' K' ∧ IsSubcomplex L'' K'' ∧ L''.space = P ∧
    N = simplicialNbhd K'' L''

namespace Triangulates

/-- **A triangulated set is compact.** -/
theorem isCompact {K : SimplicialComplex ℝ E} {P : Set E} (h : Triangulates K P) :
    IsCompact P := by
  obtain ⟨hfin, rfl⟩ := h
  have : K.space = ⋃ s ∈ K.faces, convexHull ℝ (s : Set E) := by
    ext x; simp [SimplicialComplex.mem_space_iff]
  rw [this]
  exact hfin.isCompact_biUnion fun s _ => s.finite_toSet.isCompact_convexHull

end Triangulates

theorem IsCompactPolyhedron.isCompact {P : Set E} (h : IsCompactPolyhedron P) : IsCompact P :=
  let ⟨_, hK⟩ := h; hK.isCompact

namespace Subdivides

theorem refl (K : SimplicialComplex ℝ E) : Subdivides K K :=
  ⟨rfl, fun s hs => ⟨s, hs, subset_rfl⟩⟩

theorem trans {K'' K' K : SimplicialComplex ℝ E} (h₁ : Subdivides K'' K') (h₂ : Subdivides K' K) :
    Subdivides K'' K := by
  refine ⟨h₁.1.trans h₂.1, fun s hs => ?_⟩
  obtain ⟨t, ht, hst⟩ := h₁.2 s hs
  obtain ⟨u, hu, htu⟩ := h₂.2 t ht
  exact ⟨u, hu, hst.trans htu⟩

end Subdivides

theorem IsSubcomplex.space_subset {L K : SimplicialComplex ℝ E} (h : IsSubcomplex L K) :
    L.space ⊆ K.space := by
  intro x hx
  rw [SimplicialComplex.mem_space_iff] at hx ⊢
  obtain ⟨s, hs, hx⟩ := hx
  exact ⟨s, h hs, hx⟩

/-- **Linearity on `K` passes to a subdivision.** -/
theorem IsLinearOn.mono {K K' : SimplicialComplex ℝ E} {f : E → F} (hf : IsLinearOn K f)
    (h : Subdivides K' K) : IsLinearOn K' f := by
  intro s hs
  obtain ⟨t, ht, hst⟩ := h.2 s hs
  obtain ⟨A, hA⟩ := hf t ht
  exact ⟨A, hA.mono hst⟩

end QOU.MathlibExt.PL
