import QOU.LiftingDescent.CrossedModuleSurfaceHolonomy
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Tactic

/-!
# QOU.LiftingDescent.SpatialDimensionBinder — `d` as an actual binder

**The gap this closes.** The spatial dimension `d` is named throughout the
corpus and is a binder nowhere. `q-navier-stokes.lean` carries `dim : Nat := 3`
as a structure field with a default that no theorem varies; the descent rungs
`rem:descent-reduction-{three,two,…}` are prose. Nothing in the Lean tree takes
`d` and proves something whose *content* changes with it.

**What `d` is allowed to bind to here.** Only one thing in the descent ladder is
both `d`-dependent and already pinned by proved corpus results: **whether the
mass identity's surface `Σ` can carry a boundary.** The mass identity integrates
a two-dimensional multiplicative integral, so `Σ` is 2-dimensional; it can be a
*proper* submanifold — and so can have non-empty boundary — exactly when the
ambient dimension strictly exceeds 2. Below that it is forced to be the base
itself (closed), or to degenerate.

That threshold is what separates the rungs, and it is where the physics sits:
with no boundary the feedback image of the surface holonomy is trivial, so by
`CrossedModuleSurfaceHolonomy.ker_le_center` (sorry-free) the holonomy is
**central** — the mass is abelian. With a boundary it need not be.

## The honest shape, and what is assumed

`DescentStratum` carries the 2-dimensional Stokes theorem as an explicit
**hypothesis field**, because the corpus cites it (Yekutieli Thm 0.4.2) and does
not prove it. This is the §3b-cond conditional-class pattern, and it is used in
the non-degenerate direction required there: the class supplies the *input*
(`Φ h = 1` at a boundaryless stratum) and `mass_central_of_closed` **derives**
the conclusion through `ker_le_center`, rather than carrying the conclusion as a
field and projecting it.

## Why this is not decoration — `d` is load-bearing, and that is PROVED

A `d`-indexed statement is worthless if the same conclusion holds at every `d`.
`stratumThree` exhibits a stratum at `d = 3` whose realised holonomies include a
**non-central** element, so `mass_central_of_closed` genuinely fails there:
`exists_realised_not_central_at_three`. Its hypothesis is therefore not
removable, and the family really does vary across the threshold. The witness is
the adjoint crossed module of `Equiv.Perm (Fin 3)`, whose centre is trivial.

## What this does NOT do

It does not formalise differential geometry, manifolds, or forms. `d : ℕ` is a
label and the geometric content — that a 2-dimensional `Σ` admits a boundary iff
`2 < d` — enters as the *definition* `BoundaryAvailable`, not as a theorem. So
this makes `d` a real binder over the *consequence* (centrality), not over the
geometry itself. Formalising the geometry is a separate and much larger task.

Base ring §7c: none — group theory and `ℕ`, no `ℝ`, nothing archimedean.

-- Ref: [yekutieli2015] https://arxiv.org/abs/1007.1250 — Thm 0.4.2 (2-dim Stokes).
-- Ref: [leitner2026] folio/quantum-observable-universe/lifting-and-descent/descent-reduction-two.md
-/

namespace QOU.LiftingDescent.SpatialDimension

open QOU.LiftingDescent.CrossedModuleSurfaceHolonomy

/-- The mass identity's surface `Σ` is two-dimensional: the multiplicative
integral of `def:mass-identity` is the 2-dimensional one. -/
def massSurfaceDim : ℕ := 2

/-- `Σ` can be a **proper** submanifold of the base, hence can carry a non-empty
boundary, exactly when the ambient dimension strictly exceeds its own. At or
below that, `Σ` is forced to be the whole base (closed) or to degenerate. -/
def BoundaryAvailable (d : ℕ) : Prop := massSurfaceDim < d

/-- The threshold, in the form the descent ladder uses it: a boundary is
available exactly from dimension three up. -/
theorem boundaryAvailable_iff (d : ℕ) : BoundaryAvailable d ↔ 3 ≤ d := by
  unfold BoundaryAvailable massSurfaceDim
  omega

theorem boundaryAvailable_three : BoundaryAvailable 3 := by
  rw [boundaryAvailable_iff]

theorem not_boundaryAvailable_two : ¬ BoundaryAvailable 2 := by
  rw [boundaryAvailable_iff]; omega

theorem not_boundaryAvailable_one : ¬ BoundaryAvailable 1 := by
  rw [boundaryAvailable_iff]; omega

theorem not_boundaryAvailable_zero : ¬ BoundaryAvailable 0 := by
  rw [boundaryAvailable_iff]; omega

/-- A rung of the descent ladder at spatial dimension `d`.

`realised` is the set of surface holonomies the stratum actually produces, and
`feedback_trivial_of_closed` is the 2-dimensional Stokes theorem as it bears on
this rung: at a dimension with no boundary available, a realised surface
holonomy has trivial feedback image. That field is an **assumption** — the
corpus cites Yekutieli for it and does not prove it. -/
structure DescentStratum (G H : Type*) [Group G] [Group H] where
  /-- The crossed module of the stratum. -/
  C : CrossedModule G H
  /-- The spatial dimension of the base. -/
  d : ℕ
  /-- The surface holonomies this stratum realises. -/
  realised : H → Prop
  /-- 2-dimensional Stokes at a boundaryless stratum (ASSUMED, not proved). -/
  feedback_trivial_of_closed :
    ¬ BoundaryAvailable d → ∀ h, realised h → C.Φ h = 1

variable {G H : Type*} [Group G] [Group H]

/-- **Below the threshold the mass is central.** At a stratum whose dimension
leaves no room for a boundary, every realised surface holonomy is central, so
the mass is an abelian invariant.

The conclusion is *derived*: the Stokes field supplies `Φ h = 1`, and
`ker_le_center` — which is proved from the Peiffer identity, not assumed —
carries it to centrality. -/
theorem mass_central_of_closed (S : DescentStratum G H)
    (hd : ¬ BoundaryAvailable S.d) {h : H} (hr : S.realised h) :
    h ∈ Subgroup.center H :=
  ker_le_center S.C (MonoidHom.mem_ker.mpr (S.feedback_trivial_of_closed hd h hr))

/-- The dimension-2 rung, as a value of the family. -/
theorem mass_central_at_two (S : DescentStratum G H) (hd : S.d = 2)
    {h : H} (hr : S.realised h) : h ∈ Subgroup.center H :=
  mass_central_of_closed S (hd ▸ not_boundaryAvailable_two) hr

/-- The dimension-1 rung. -/
theorem mass_central_at_one (S : DescentStratum G H) (hd : S.d = 1)
    {h : H} (hr : S.realised h) : h ∈ Subgroup.center H :=
  mass_central_of_closed S (hd ▸ not_boundaryAvailable_one) hr

/-! ### `d` is load-bearing

Everything above would be decoration if the conclusion held at every `d`. It
does not, and the rest of this file proves that rather than asserting it. -/

/-- Any group is a crossed module over itself, with the identity feedback and
conjugation as the twisting. -/
def adjoint (H : Type*) [Group H] : CrossedModule H H where
  Φ := MonoidHom.id H
  Ψ := MulAut.conj
  equivariant := by intro g h; simp [MulAut.conj]
  peiffer := by intro h h'; simp [MulAut.conj]

/-- A stratum at `d = 3`, realising everything. The Stokes field is discharged
because its hypothesis is false at this dimension: a boundary *is* available. -/
def stratumThree (H : Type*) [Group H] : DescentStratum H H where
  C := adjoint H
  d := 3
  realised := fun _ => True
  feedback_trivial_of_closed := fun hn => absurd boundaryAvailable_three hn

/-- An element failing to commute with something is not central. -/
theorem not_mem_center_of_noncomm {a b : H} (hab : a * b ≠ b * a) :
    a ∉ Subgroup.center H := by
  intro ha
  exact hab ((Subgroup.mem_center_iff.mp ha b).symm)

/-- **The threshold is real.** At `d = 3` there is a realised surface holonomy
that is *not* central, so `mass_central_of_closed` cannot be extended past the
threshold and its dimension hypothesis is not removable. -/
theorem exists_realised_not_central_at_three :
    ∃ h : Equiv.Perm (Fin 3),
      (stratumThree (Equiv.Perm (Fin 3))).realised h ∧
      h ∉ Subgroup.center (Equiv.Perm (Fin 3)) := by
  refine ⟨Equiv.swap 0 1, trivial, not_mem_center_of_noncomm (b := Equiv.swap 1 2) ?_⟩
  decide

end QOU.LiftingDescent.SpatialDimension
