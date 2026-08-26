import Mathlib.Tactic
import QOU.Eightfold.Sym2GateFSTrichotomy

/-!
# QOU.Eightfold.SelfDualSectorConfinement — why the search is confined to the groupoid, exactly

Bean `qou-8pl3` Route A, under epic `qou-8lxd`.

## The claim this repairs

`eightfold-open-problems.md` §1 asserts:

> *That the search is confined to the groupoid level is now a theorem, not an
> extrapolation.*  The parity criterion (`Sym2GateParity.lean`) decides the
> `Sym²` gate for a single **irreducible** summand, and a three-dimensional `W`
> need not be irreducible …

The conclusion is right and the stated reason no longer supports it.
`Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three` shows the parity
argument is a theorem about the **self-dual sector**: a complex-type object
passes the gate at *any* dimension, three included
(`Sym2GateComplexType.complex_three_passes_gate`).  So "parity excludes
dimension three" is false as a general statement, and cannot by itself confine
anything.

## What actually confines it

The single-fibre tower is built from `SU(2)`, and **every `SU(2)` irrep is
self-dual** — real for integer spin, quaternionic for half-integer, never
complex.  `Sym2GateMultiplicity` records this and relies on it (*"For `SU(2)`
every irrep is self-dual … hence the mixed pieces contribute nothing"*).

That is the missing premise.  A category with no complex-type objects has no
escape hatch, so the parity conclusion applies there **without exception**:

    no complex type available  ⟹  every passing object has even dimension
                               ⟹  no passing object has dimension 3

`selfDual_category_excludes_dim_three` below is that implication, and
`single_fibre_su2_excludes_dim_three` is it with the `SU(2)` hypothesis named.

So the confinement survives, on a **stronger and more specific** footing than
the chapter states: not *"parity excludes 3"* (false in general) but *"`SU(2)`
is a self-dual category, and in a self-dual category parity excludes 3"*.

## What this tells Route A to build — the point of the file

Route A is recorded as *"construct a three-dimensional object `W` in the
multi-fibre groupoid whose `Sym²(W)` is irreducible.  **Nothing has been
built.**"*  The target can now be stated far more sharply than "more
structure":

**The groupoid must supply a NON-SELF-DUAL object.**  That is not one option
among several — by `gate_forces_complex_of_dim_three` it is the *only* way any
construction reaches dimension three through this gate, and by
`selfDual_category_excludes_dim_three` it is exactly what a single `SU(2)`
fibre cannot provide.

`self_duality_is_the_obstruction` states the two halves together: the property
that fails on one fibre is the *same* property a successful groupoid
construction must exhibit.  A proposed Route A construction can therefore be
checked against a single question — *is its three-dimensional object isomorphic
to its own dual?* — long before its `Sym²` decomposition is computed.  If yes,
it is dead, whatever else it has.

## Scope

This does **not** construct anything, and does not show a non-self-dual object
exists at groupoid level.  Route A stays open.  What is settled is the
specification: a *necessary* condition on any solution, and the precise reason
the single-fibre case fails it.

Nor does it bear on flavour-versus-colour — `TrialitySelectionRule` and
`Sym2GateFSTrichotomy` show the `ℤ/3` grading and the gate are both blind to
that, and nothing here changes it.

## Base ring (§7c)

Inherited from `Sym2GateFSTrichotomy`: pure `ℕ` combinatorics, no ring, no
ordering, no archimedean content.

-- Ref: [fulton-harris1991] §3.5, §11 (the Frobenius–Schur trichotomy; every
-- `SU(2)` irrep is self-dual, real for integer and quaternionic for
-- half-integer spin).
-/

namespace QOU.Eightfold.SelfDualSectorConfinement

open QOU.Eightfold.Sym2GateFSTrichotomy

/-! ## 1. A self-dual category cannot reach dimension three -/

/-- **The confinement, correctly premised.**  In a category where every
occurring irrep is self-dual, no object of dimension `3` passes the `Sym²`
gate.

This is what `eightfold-open-problems.md` §1 needs.  The self-duality
hypothesis is doing the work; without it the statement is false, by
`Sym2GateComplexType.complex_three_passes_gate`. -/
theorem selfDual_category_excludes_dim_three {S fs m dual d}
    (hgate : Passes S fs m dual)
    (hq : QuaternionicEvenDim S fs d)
    (hsd : ∀ i ∈ S, (fs i).SelfDual) :
    dimOf S m d ≠ 3 := by
  intro hdim
  have hev := even_dimOf_of_selfDual hgate hq hsd
  rw [hdim, Nat.even_iff] at hev
  omega

/-- **The single-fibre case.**  `SU(2)` has no complex-type irrep — every one is
self-dual, real for integer and quaternionic for half-integer spin — so the
hypothesis of the previous theorem is satisfied outright and the single-fibre
tower cannot host a three-dimensional object that passes.

The `SU(2)` fact is the cited input (`[fulton-harris1991]` §3.5), carried here
as the hypothesis `hsu2` rather than assumed silently. -/
theorem single_fibre_su2_excludes_dim_three {S fs m dual d}
    (hgate : Passes S fs m dual)
    (hq : QuaternionicEvenDim S fs d)
    (hsu2 : ∀ i ∈ S, fs i = .real ∨ fs i = .quaternionic) :
    dimOf S m d ≠ 3 := by
  refine selfDual_category_excludes_dim_three hgate hq ?_
  intro i hi
  rcases hsu2 i hi with h | h <;> rw [h] <;> trivial

/-! ## 2. Self-duality is the obstruction, stated as one thing -/

/-- **The specification for Route A.**  The two halves together.

*Necessity*: any object of dimension `3` that passes must contain a
complex-type irrep (`gate_forces_complex_of_dim_three`).
*The single-fibre failure*: a category all of whose objects are self-dual
contains none, and so reaches no such object.

So the property a groupoid construction must exhibit is exactly the property a
single `SU(2)` fibre lacks.  A candidate can be tested by asking whether its
three-dimensional object is isomorphic to its own dual, before any `Sym²`
decomposition is attempted. -/
theorem self_duality_is_the_obstruction {S fs m dual d}
    (hgate : Passes S fs m dual)
    (hq : QuaternionicEvenDim S fs d)
    (hdim : dimOf S m d = 3) :
    (∃ i ∈ S, fs i = .complex) ∧ ¬ (∀ i ∈ S, (fs i).SelfDual) := by
  refine ⟨gate_forces_complex_of_dim_three hgate hq hdim, ?_⟩
  intro hsd
  exact selfDual_category_excludes_dim_three hgate hq hsd hdim

/-- The contrapositive as a screening test: a candidate whose irreps are all
self-dual is dead at dimension three, and no further analysis is needed. -/
theorem screen_out_selfDual_candidate {S fs m dual d}
    (hq : QuaternionicEvenDim S fs d)
    (hsd : ∀ i ∈ S, (fs i).SelfDual)
    (hdim : dimOf S m d = 3) :
    ¬ Passes S fs m dual :=
  fun hgate => selfDual_category_excludes_dim_three hgate hq hsd hdim

end QOU.Eightfold.SelfDualSectorConfinement
