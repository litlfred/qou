/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Group.Basic
import Mathlib.GroupTheory.GroupAction.Defs

/-!
# Transporting a pointwise identity across a single orbit

A recurring situation: two maps are compared at ONE point of a space carrying a group
action, they agree there, and one wants the agreement at every point.  When the space is a
single orbit and both maps are equivariant, that upgrade is free -- and this file isolates
exactly what it costs.

The content is that **commutativity is the whole hypothesis**, and it is used exactly
once.  `eq_smul_of_transitive_orbit` says: an equivariant `φ` that agrees at one point
with the action of a fixed `b` agrees with it on the entire orbit of that point.  Its
proof is `mul_comm` and nothing else, and `exists_not_forall_eq_of_not_central` shows the
hypothesis cannot be dropped -- for any non-central `b` in any group there is an
equivariant map agreeing with `b` at a point and nowhere else forced to.

`rel_of_transitive_orbit` is the version actually needed when the two maps are only
compared UP TO an equivalence (agreement "modulo a gauge", modulo conjugacy, modulo a
torus action).  It is stated as an `Iff`, which is the useful shape: it propagates a
POSITIVE agreement and a NEGATIVE one equally, so a verdict that varies across an orbit
refutes one of its hypotheses rather than saying anything about the maps.  Here
commutativity is not needed at all -- only that the relation is stable under the action.

## Intended reading

`X` is a zero-dimensional variety whose points form one Galois orbit, `G` the Galois
group, `φ` a map defined by formulas over the base field (hence equivariant), `b` a
distinguished group element, and `r` "differ by an element of a gauge group defined over
the base field" (hence action-stable).  Nothing in this file refers to that situation; it
is stated for an arbitrary group action and proved in full generality.
-/

namespace QOU.Eightfold.GaloisOrbitTransport

variable {G X : Type*}

/-- `φ` commutes with the action: `φ (g • x) = g • φ x`. -/
def IsEquivariant (G : Type*) {X : Type*} [Group G] [MulAction G X] (φ : X → X) : Prop :=
  ∀ (g : G) (x : X), φ (g • x) = g • φ x

/-- `x₀` generates the whole space under the action -- the space is a single orbit. -/
def IsOrbitOf (G : Type*) {X : Type*} [Group G] [MulAction G X] (x₀ : X) : Prop :=
  ∀ x : X, ∃ g : G, x = g • x₀

section CommGroup
variable [CommGroup G] [MulAction G X]

/-- **One point suffices, on a single orbit.**  An equivariant map agreeing at `x₀` with
the action of `b` agrees with it everywhere on the orbit of `x₀`.

Commutativity is used exactly once, to swap `g * b` for `b * g`; see
`exists_not_forall_eq_of_not_central` for why it cannot be dropped. -/
theorem eq_smul_of_transitive_orbit {φ : X → X} (hφ : IsEquivariant G φ) {b : G} {x₀ : X}
    (hx₀ : φ x₀ = b • x₀) (htr : IsOrbitOf G x₀) (x : X) : φ x = b • x := by
  obtain ⟨g, rfl⟩ := htr x
  rw [hφ, hx₀, smul_smul, smul_smul, mul_comm]

end CommGroup

section Rel
variable [Group G] [MulAction G X]

/-- **Agreement up to an action-stable relation propagates across an orbit, both ways.**

Stated as an `Iff`: the relation holds between two equivariant maps at every point of the
orbit precisely when it holds at the generating point.  So a *failure* at one point is a
failure at all of them, which is what makes a constant verdict down an orbit a theorem
rather than a coincidence -- and a verdict that is NOT constant refutes a hypothesis
(equivariance of one map, or stability of `r`) instead of distinguishing the points.

No commutativity is needed here; `r` being carried along by the action is enough. -/
theorem rel_of_transitive_orbit {r : X → X → Prop}
    (hr : ∀ (g : G) (x y : X), r x y ↔ r (g • x) (g • y))
    {φ ψ : X → X} (hφ : IsEquivariant G φ) (hψ : IsEquivariant G ψ)
    {x₀ : X} (htr : IsOrbitOf G x₀) :
    (∀ x : X, r (φ x) (ψ x)) ↔ r (φ x₀) (ψ x₀) := by
  constructor
  · intro h; exact h x₀
  · intro h x
    obtain ⟨g, rfl⟩ := htr x
    rw [hφ, hψ]
    exact (hr g _ _).mp h

/-- The contrapositive, spelled out: a negative verdict at one point of an orbit is a
negative verdict at every point. -/
theorem not_rel_of_transitive_orbit {r : X → X → Prop}
    (hr : ∀ (g : G) (x y : X), r x y ↔ r (g • x) (g • y))
    {φ ψ : X → X} (hφ : IsEquivariant G φ) (hψ : IsEquivariant G ψ)
    {x₀ : X} (htr : IsOrbitOf G x₀) (h : ¬ r (φ x₀) (ψ x₀)) (x : X) :
    ¬ r (φ x) (ψ x) := by
  intro hx
  refine h ?_
  obtain ⟨g, rfl⟩ := htr x
  rw [hφ, hψ] at hx
  exact (hr g _ _).mpr hx

end Rel

/-- **Sharpness: commutativity in `eq_smul_of_transitive_orbit` cannot be dropped.**

For any group `G` acting on itself by left multiplication and any `b` that fails to
commute with something, right multiplication by `b` is equivariant, agrees with `b • ·`
at the identity, and the identity generates -- yet it does not agree with `b • ·`
everywhere.  So the conclusion genuinely needs `G` commutative, not merely the orbit
hypothesis. -/
theorem exists_not_forall_eq_of_not_central [Group G] {b : G}
    (hb : ∃ g : G, g * b ≠ b * g) :
    ∃ φ : G → G, IsEquivariant G φ ∧ φ 1 = b • (1 : G) ∧ IsOrbitOf G (1 : G) ∧
      ¬ (∀ x : G, φ x = b • x) := by
  refine ⟨fun x => x * b, fun g x => by simp [smul_eq_mul, mul_assoc], by simp,
    fun x => ⟨x, by simp⟩, ?_⟩
  obtain ⟨g, hg⟩ := hb
  intro h
  exact hg (h g)

end QOU.Eightfold.GaloisOrbitTransport
