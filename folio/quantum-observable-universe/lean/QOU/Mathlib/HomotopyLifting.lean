import Mathlib.Topology.Homotopy.HomotopyGroup
import Mathlib.Tactic

/-!
# QOU.Mathlib.HomotopyLifting — a fibration predicate Mathlib does not have

Bean `qou-de7r`, item 2 of `qou-pan0`. `QOU/Mathlib/LongExactSequence.lean`
supplies the **algebraic** long exact sequence. This file and
`QOU/Mathlib/HomotopyGroupFunctor.lean` /
`QOU/Mathlib/FibrationExactness.lean` supply the beginning of the
**topological** side that would feed it.

## What Mathlib has, checked rather than guessed

The pinned Mathlib (`f897ebcf`, Lean 4.24.0) was surveyed by enumerating the
declarations each olean actually contains, not by recalling names:

* `Mathlib.Topology.Homotopy.HomotopyGroup` — `GenLoop`, `HomotopyGroup`,
  `Cube.boundary`, the `Group`/`CommGroup` instances. So `π_n` exists.
* `Mathlib.Topology.Homotopy.Basic` — `ContinuousMap.Homotopy`, `HomotopyWith`,
  `HomotopyRel`, and `HomotopicRel.comp_continuousMap`.
* `Mathlib.Topology.Homotopy.Lifting` — lifting theorems for **covering maps
  and local homeomorphisms only** (`IsCoveringMap.liftHomotopy`,
  `IsCoveringMap.liftPath`, `IsLocalHomeomorph.monodromy_theorem`). A covering
  map is a fibration with discrete fibres, and its lifts are *unique*; every
  proof there runs on that uniqueness, so none of it generalises.

**There is no fibration.** `Fibration` appears in the olean tree only in
`Order/UpperLower/Fibration` (an order-theoretic notion) and in the abstract
`CategoryTheory` model-category / simplicial-set files, none of which is
connected to `HomotopyGroup` on topological spaces. So the predicate below is
new, and it is written to match how `HomotopyGroup` is built — over the cubes
`N → I` — because a predicate that does not connect to those is worthless here.

## What is defined

`HasHomotopyLiftingProperty p Y` is the ordinary HLP: a homotopy into `B`
indexed by `Y`, together with a lift of its start, extends to a homotopy into
`E`. `IsHurewiczFibration` quantifies over all `Y`; `IsSerreFibration` over the
cubes, which is the version `π_n` needs.

`HasHomotopyLiftingPropertyRel p Y A` is the **stationary relative** HLP: if the
homotopy downstairs never moves on `A`, the lift can be chosen never to move on
`A` either. This is the special case of the homotopy lifting property for the
pair `(Y, A)` in which the prescribed lift over `A × I` is constant — and it is
the only case the exactness argument in `FibrationExactness.lean` uses.

## The gap this file does *not* close

Classically the two are equivalent for cubes: `(Iⁿ × I, Iⁿ × {0} ∪ ∂Iⁿ × I)` is
homeomorphic to `(Iⁿ × I, Iⁿ × {0})`, so a Serre fibration automatically has the
relative property with respect to `(Iⁿ, ∂Iⁿ)`. That homeomorphism — radial
projection from a point above the cube — is a genuine piece of geometry and is
**not proved here**. It is named as `SerreCubePairBridge` so that the hole has
an address rather than being silently absorbed: nothing in this development
proves it, and nothing in this development uses it in a proof.

Consequently the exactness theorem downstream takes
`HasHomotopyLiftingPropertyRel` as a hypothesis directly. That hypothesis is not
vacuous: `Prod.hasHomotopyLiftingPropertyRel_fst` proves it, for every `Y` and
every `A`, for the projection of a trivial bundle `B × F → B`.

-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes
-/

namespace QOU.Mathlib.HomotopyLifting

open unitInterval ContinuousMap

universe u v u' w

variable {E : Type u} {B : Type v} {D : Type u'}
  [TopologicalSpace E] [TopologicalSpace B] [TopologicalSpace D]

/-- **The homotopy lifting property** of `p : E → B` with respect to a space `Y`.

    Given a homotopy `H : I × Y → B` and a map `f : Y → E` lifting its start,
    there is a homotopy `H' : I × Y → E` lifting all of `H` and starting at `f`.

    The argument order `I × Y` (rather than `Y × I`) is deliberate: it is the
    order `ContinuousMap.Homotopy` uses, so a Mathlib homotopy can be fed to
    this predicate with no shuffling. Nothing about the definition depends on
    it, and everything about the usability does. -/
def HasHomotopyLiftingProperty (p : C(E, B)) (Y : Type w) [TopologicalSpace Y] : Prop :=
  ∀ (H : C(I × Y, B)) (f : C(Y, E)), (∀ y, p (f y) = H (0, y)) →
    ∃ H' : C(I × Y, E), (∀ z, p (H' z) = H z) ∧ ∀ y, H' (0, y) = f y

/-- **The stationary relative homotopy lifting property** with respect to a pair
    `(Y, A)`.

    Same data as `HasHomotopyLiftingProperty`, with one hypothesis and one
    conclusion added: if `H` is *constant in `t`* on `A`, the lift may be chosen
    constant in `t` on `A` too.

    This is what the fibration exactness argument needs and the plain HLP does
    not give. Lifting a nullhomotopy of `p ∘ g` produces a map `Iⁿ → E` into the
    fibre, but with no control on `∂Iⁿ` the result is not a based sphere at all
    — the boundary drifts away from the basepoint along the lifted homotopy, and
    the class it would represent does not exist. Pinning the boundary is not a
    convenience; without it there is no theorem. -/
def HasHomotopyLiftingPropertyRel (p : C(E, B)) (Y : Type w) [TopologicalSpace Y]
    (A : Set Y) : Prop :=
  ∀ (H : C(I × Y, B)) (f : C(Y, E)), (∀ y, p (f y) = H (0, y)) →
    (∀ t : I, ∀ a ∈ A, H (t, a) = H (0, a)) →
    ∃ H' : C(I × Y, E), (∀ z, p (H' z) = H z) ∧ (∀ y, H' (0, y) = f y) ∧
      (∀ t : I, ∀ a ∈ A, H' (t, a) = f a)

/-- A **Hurewicz fibration**: the homotopy lifting property against every space
    in the universe `w`. Universe-polymorphic rather than fixed at `Type 0`
    because the spaces this corpus builds do not all live in one universe. -/
def IsHurewiczFibration (p : C(E, B)) : Prop :=
  ∀ (Y : Type w) [TopologicalSpace Y], HasHomotopyLiftingProperty p Y

/-- A **Serre fibration**: the homotopy lifting property against the cubes
    `Iⁿ`. This is the version tied to `π_n`, because `Mathlib`'s `GenLoop` is
    built out of maps from `Fin n → I`. -/
def IsSerreFibration (p : C(E, B)) : Prop :=
  ∀ n : ℕ, HasHomotopyLiftingProperty p (Fin n → I)

theorem IsHurewiczFibration.isSerreFibration {p : C(E, B)}
    (h : IsHurewiczFibration.{u, v, 0} p) : IsSerreFibration p :=
  fun n => h (Fin n → I)

/-- With `A = ∅` the relative property is exactly the absolute one: the extra
    hypothesis and the extra conclusion are both vacuous. Recorded so the
    relative predicate is visibly a *refinement* of the plain one rather than an
    unrelated definition. -/
theorem hasHomotopyLiftingPropertyRel_empty (p : C(E, B)) (Y : Type w) [TopologicalSpace Y] :
    HasHomotopyLiftingPropertyRel p Y ∅ ↔ HasHomotopyLiftingProperty p Y := by
  constructor
  · intro h H f hf
    obtain ⟨H', h1, h2, -⟩ := h H f hf (by simp)
    exact ⟨H', h1, h2⟩
  · intro h H f hf _
    obtain ⟨H', h1, h2⟩ := h H f hf
    exact ⟨H', h1, h2, by simp⟩

/-- The identity has the homotopy lifting property: the homotopy is its own
    lift. Trivial, and it is the first check that the definition is not
    accidentally empty. -/
theorem hasHomotopyLiftingProperty_id (Y : Type w) [TopologicalSpace Y] :
    HasHomotopyLiftingProperty (ContinuousMap.id B) Y := by
  intro H f hf
  refine ⟨H, fun _ => rfl, fun y => ?_⟩
  exact (hf y).symm

/-- Fibrations compose. The proof is the only thing one would guess: lift the
    homotopy through the outer map first, then lift the result through the
    inner one, whose start is already lifted. -/
theorem HasHomotopyLiftingProperty.comp {p : C(E, B)} {q : C(B, D)} {Y : Type w}
    [TopologicalSpace Y] (hp : HasHomotopyLiftingProperty p Y)
    (hq : HasHomotopyLiftingProperty q Y) :
    HasHomotopyLiftingProperty (q.comp p) Y := by
  intro H f hf
  obtain ⟨H₁, hH₁, hH₁0⟩ := hq H (p.comp f) hf
  obtain ⟨H₂, hH₂, hH₂0⟩ := hp H₁ f fun y => (hH₁0 y).symm
  refine ⟨H₂, fun z => ?_, hH₂0⟩
  rw [ContinuousMap.comp_apply, hH₂ z, hH₁ z]

section Trivial

universe uF

variable {F : Type uF} [TopologicalSpace F]

/-- **A trivial bundle is a fibration**, and it satisfies the *relative*
    property as well, for every pair `(Y, A)`.

    This is the theorem that makes everything downstream non-vacuous. The
    relative HLP is taken as a hypothesis by the exactness result, and a
    hypothesis nothing satisfies proves nothing; here it is discharged
    outright. The lift is the only available one — carry the homotopy in the
    base coordinate and hold the fibre coordinate fixed at whatever `f`
    chose — and holding the fibre coordinate fixed is exactly why the boundary
    does not drift. -/
theorem Prod.hasHomotopyLiftingPropertyRel_fst (Y : Type w) [TopologicalSpace Y] (A : Set Y) :
    HasHomotopyLiftingPropertyRel (ContinuousMap.fst : C(B × F, B)) Y A := by
  intro H f hf hstat
  refine ⟨ContinuousMap.prodMk H (ContinuousMap.snd.comp (f.comp ContinuousMap.snd)),
    fun _ => rfl, fun y => ?_, fun t a ha => ?_⟩
  · exact Prod.ext (hf y).symm rfl
  · exact Prod.ext (by simpa using (hstat t a ha).trans (hf a).symm) rfl

/-- The absolute form of the same fact, for reference and for the composition
    lemma. -/
theorem Prod.hasHomotopyLiftingProperty_fst (Y : Type w) [TopologicalSpace Y] :
    HasHomotopyLiftingProperty (ContinuousMap.fst : C(B × F, B)) Y :=
  (hasHomotopyLiftingPropertyRel_empty _ Y).mp (Prod.hasHomotopyLiftingPropertyRel_fst Y ∅)

/-- Hence a trivial bundle is a Hurewicz fibration, and so a Serre one. -/
theorem Prod.isHurewiczFibration_fst :
    IsHurewiczFibration.{max v uF, v, w} (ContinuousMap.fst : C(B × F, B)) :=
  fun Y _ => Prod.hasHomotopyLiftingProperty_fst Y

end Trivial

/-- **The unproved bridge**, stated so that it has a name.

    For a fibration, the plain homotopy lifting property against a cube implies
    the stationary relative property against that cube and its boundary. The
    proof is the pair homeomorphism `(Iⁿ × I, Iⁿ × {0} ∪ ∂Iⁿ × I) ≅ (Iⁿ × I,
    Iⁿ × {0})` obtained by projecting radially from a point above the cube
    (Hatcher, §4.2). It is real geometry, it is **not proved here**, and no
    result in this development invokes it — `FibrationExactness` assumes the
    relative property directly instead.

    Recorded as a `Prop`-valued definition rather than a `sorry`ed theorem on
    purpose: a `sorry` would leak `sorryAx` into every downstream axiom check
    and make the honest results indistinguishable from the assumed one. -/
def SerreCubePairBridge (p : C(E, B)) : Prop :=
  ∀ (N : Type) [Fintype N] [DecidableEq N],
    HasHomotopyLiftingProperty p (N → I) →
      HasHomotopyLiftingPropertyRel p (N → I) (Cube.boundary N)

/-- The bridge holds for a trivial bundle — because there the relative property
    holds unconditionally. Not evidence for the general case; evidence that the
    statement is the right shape. -/
theorem Prod.serreCubePairBridge_fst {F : Type*} [TopologicalSpace F] :
    SerreCubePairBridge (ContinuousMap.fst : C(B × F, B)) :=
  fun _ _ _ _ => Prod.hasHomotopyLiftingPropertyRel_fst _ _

end QOU.Mathlib.HomotopyLifting
