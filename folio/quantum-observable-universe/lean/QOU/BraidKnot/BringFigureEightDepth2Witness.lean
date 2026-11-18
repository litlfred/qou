import Mathlib.Tactic

/-!
# QOU.BraidKnot.BringFigureEightDepth2Witness — conjecture carrier

**§3b-cond class axiomatisation** for content block
[`conj:bring-figure-eight-depth-2-witness`](../../../mass-theory/bring-figure-eight-depth-2-witness.md):
*Bring figure-8 volume as depth-2 grouplike value (50-digit numerical witness)*.

Primary conjecture carrier with **no instance** — the honest open state per
AGENTS.md §3b-tax.

## What changed (bean `qou-ffwk`)

The previous field schema was a scalar `residual : ℝ` plus a field asserting it
vanishes, which is inhabited by `⟨0, rfl⟩`. The class chose its own witness, so
it asserted nothing and a downstream `[BringFigureEightDepth2Witness]`
hypothesis was not a meaningful conditional. The compared quantities are now
class **parameters**, so an instance must discharge the claim for the caller's
data.

Two stale statements in the old header are also corrected: the axiom-and-instance
pair had been removed without the header being updated.

## Which half is the conjecture

The block asserts a chain:

```
Vol(S³ \ 4₁)  =  std(2 Im Li₂^q(e^{iπ/3}))  =  2 Cl₂(π/3)
```

and its own status note splits it: *"**Numerically discharged at 50 digits via
mpmath** … **Conjectural** as a structural identification of the depth-2
grouplike value with `Vol(4₁)`."* So the two equalities have different standing,
and only the **first** is conjectural. The second is the evaluation, verified to
50 digits by `computations/gb_depth_period_bring_fig8.py` with a committed
witness, and the block records that a partial-sum cross-check agrees to about 13
digits.

The class therefore carries **one** field, the structural identification.
Folding the evaluation in as a second field would mark verified work as
conjectural, which is the mirror image of the defect this bean exists to fix.
The evaluation enters instead as a hypothesis of `evaluates_to` below, so a
caller composes the two and the provenance of each stays visible.

Equality is stated exactly, not within a tolerance. The block writes `=` and the
50-digit figure is *evidence for* the identity rather than a claim that it holds
only approximately — unlike `conj:gs-archimedean-agreement-*`, which writes `≈`
and whose carriers are parameterised by a tolerance for that reason.

## Conditionality that cannot be expressed here, and why

The block states the conjecture is *"conditional on
`conj:gb-depth-period-correspondence`"*. That would naturally be an instance
parameter — the §3b-cond shape — but it cannot be one: the corresponding class
`QOU.AlgebraicSubstrate.GBDepthPeriodCorrespondence` exists only as a
**co-located stub** (`mass-theory/gb-depth-period-correspondence.lean`), and per
`QOU.GroundRingAnnotations` co-located stubs are documentation that `lake` does
not compile. A library module cannot import one.

So the dependency is documented here and not enforced by the elaborator. Making
it enforceable requires promoting that carrier into `lean/QOU/`, which is its
own piece of work and is not attempted here. Recorded rather than quietly
dropped: an instance of this class does **not** discharge the correspondence it
rests on.

## Base ring (§7c)

`ℝ` is required and not a gratuitous specialisation. The left side is a
hyperbolic volume, the right is a standard part — the map out of the graded
structure into the observable value. Both live on the observable side of the
substrate wall by construction; that is what "archimedean" means in this block's
own depth table.
-/

namespace QOU.BraidKnot

/-- **Bring figure-8 volume as a depth-2 grouplike value.**

The conjecture of
[`conj:bring-figure-eight-depth-2-witness`](../../../mass-theory/bring-figure-eight-depth-2-witness.md):
the hyperbolic volume of the figure-8 knot equals the standard part of the
depth-2 grouplike value at the regular-ideal-tetrahedron shape parameter.

Parameters are the caller's data:

* `figureEightVolume` — `Vol(S³ \ 4₁)`, the archimedean side;
* `grouplikeStd` — `std(2 Im Li₂^q(e^{iπ/3}))`, the algebraic side.

Both sides carry Goncharov period-depth 2 and iterated-integral depth 2
respectively. That match is **not** a field: the block derives it "by
construction of the Bloch–Wigner regulator", so it is a fact the conjecture is
stated against, not part of what the conjecture asserts.

An instance **is** the conjecture, for that data. None is provided, and an
instance would still not discharge `conj:gb-depth-period-correspondence` — see
the header. -/
class BringFigureEightDepth2Witness (figureEightVolume grouplikeStd : ℝ) : Prop where
  /-- **The conjecture**: the structural identification of the volume with the
      depth-2 grouplike value. -/
  identifies : figureEightVolume = grouplikeStd

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  History: this file previously carried
--     axiom bringFigureEightDepth2Witness_conjecture : BringFigureEightDepth2Witness
--     noncomputable instance : BringFigureEightDepth2Witness := …
-- i.e. the conjecture was asserted by `axiom` and installed as a global
-- instance, so every downstream `[BringFigureEightDepth2Witness]` resolved for
-- free and the assumption was invisible outside `#print axioms`.  Removed, not
-- completed.  The field schema is now content-bearing as well; see the header.
--
-- Note for `qou-ffwk`'s inventory: that bean greps for the old vanishing
-- field's name, which is deliberately written nowhere in this file — not even
-- in this history — so the file drops out of the grep instead of matching it
-- forever from its own changelog.

namespace BringFigureEightDepth2Witness

/-- **The conjecture composed with the verified evaluation.**

`hClosedForm` is the numerically discharged half — `std(2 Im Li₂^q(e^{iπ/3})) =
2 Cl₂(π/3)`, established to 50 digits by the block's committed witness, not by
this file. Supplying it as a hypothesis rather than a field is what keeps the
two halves' provenance distinct: the instance carries the conjecture, the
argument carries the computation. -/
theorem evaluates_to {figureEightVolume grouplikeStd clausenClosedForm : ℝ}
    [h : BringFigureEightDepth2Witness figureEightVolume grouplikeStd]
    (hClosedForm : grouplikeStd = clausenClosedForm) :
    figureEightVolume = clausenClosedForm :=
  h.identifies.trans hClosedForm

/-! ### The class is satisfiable, and only at data that satisfies it

Two checks in opposite directions. Tightening a vacuous carrier can overshoot
into one nobody can ever instantiate, which is a false claim rather than an open
one. And the tightening is pointless unless inhabitation genuinely depends on
the data. Neither is an `instance`, so typeclass resolution cannot pick either
up and silently close a downstream hypothesis. -/

/-- **Not over-corrected**: inhabited whenever the two sides agree, so the class
being open is not an artefact of its being empty. -/
theorem nonempty_of_eq (x : ℝ) : Nonempty (BringFigureEightDepth2Witness x x) :=
  ⟨⟨rfl⟩⟩

/-- **Inhabitation depends on the data** — the property the old schema lacked
entirely. Here is data at which the class is **refutable**: two sides that
differ. Under the previous shape no choice of anything could fail, so a wrong
identification had nothing to fail against. -/
theorem not_of_ne {x y : ℝ} (hxy : x ≠ y) : ¬ BringFigureEightDepth2Witness x y :=
  fun h => hxy h.identifies

/-- **Zero-residual form of the depth-2 identification.** -/
theorem volume_sub_grouplikeStd_eq_zero {figureEightVolume grouplikeStd : ℝ}
    [h : BringFigureEightDepth2Witness figureEightVolume grouplikeStd] :
    figureEightVolume - grouplikeStd = 0 :=
  sub_eq_zero.mpr h.identifies

/-- **Single-tetrahedron volume identification:**
    when the depth-2 standard part evaluates to $2\,\mathrm{Cl}_2(\pi/3)$,
    half the figure-8 volume equals $\mathrm{Cl}_2(\pi/3)$. -/
theorem half_volume_eq_clausen {figureEightVolume grouplikeStd clausenPi3 : ℝ}
    [h : BringFigureEightDepth2Witness figureEightVolume grouplikeStd]
    (hClausen : grouplikeStd = 2 * clausenPi3) :
    figureEightVolume / 2 = clausenPi3 := by
  have h1 := evaluates_to (h := h) hClausen
  linarith

/-- **Positivity transfer from the Clausen evaluation:**
    when $\mathrm{Cl}_2(\pi/3) > 0$ and the depth-2 standard part evaluates
    to $2\,\mathrm{Cl}_2(\pi/3)$, the figure-8 volume is strictly positive. -/
theorem pos_of_clausen_pos {figureEightVolume grouplikeStd clausenPi3 : ℝ}
    [h : BringFigureEightDepth2Witness figureEightVolume grouplikeStd]
    (hClausen : grouplikeStd = 2 * clausenPi3) (hPos : 0 < clausenPi3) :
    0 < figureEightVolume := by
  have h1 := evaluates_to (h := h) hClausen
  linarith

end BringFigureEightDepth2Witness

end QOU.BraidKnot
