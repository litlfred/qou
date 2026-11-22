import Mathlib.Logic.Function.Basic
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.DimMasterPentagon — the D17 conjecture carrier

**Sibling-resolution carrier** for content block
[`conj:dim-master-pentagon`](dim-master-pentagon.md): *D17 DIM master Pentagon*.

**No instance is provided** — the honest open state for a conjecture (AGENTS.md §3b).

## 2026-09-05 — this carrier used to assert nothing

It read, in full:

```lean
class DimMasterPentagon where
  holds : Prop
```

A field typed `: Prop` has the *universe* of propositions as its type, so an instance
supplies a proposition rather than a proof of one: `instance : DimMasterPentagon := ⟨True⟩`
type-checks and discharges the class, and every `[DimMasterPentagon]`-conditional theorem
was therefore conditional on nothing.

**The defect class is known, and this file does not report a new finding.** Bean
`qou-tsnp` — *"GAP: 12 conjecture carriers axiomatised as `holds : Prop` assert
nothing"* — lists this carrier among its twelve, and
[`docs/audits/2026-08-23-free-prop-field-census.md`](../../../docs/audits/2026-08-23-free-prop-field-census.md)
(PR #5562, beans `qou-tsnp` / `qou-lo1t`) is the corpus-wide census, measuring **156 free
`: Prop` fields across 105 carriers** with a re-runnable detector at
[`scripts/free-prop-field-audit.py`](../../../scripts/free-prop-field-audit.py). That census
names this carrier explicitly — *"`DimMasterPentagon`'s entire body is `holds : Prop`"* —
and compiles the `⟨True⟩` instance in its reproduction probe
([`2026-08-23-free-prop-field-triviality-probe.lean`](../../../docs/audits/2026-08-23-free-prop-field-triviality-probe.lean)).
It was named earlier still in `2026-06-07-klr-gs-order-formalization-plan.md`. **What is new
here is the repair, not the diagnosis.** D9 (`IsospinFromCanonicalBowtie`) and D10
(`SpinFromSo3Fiber`) were closed the same way; this is the third of the twelve.

Two stale pointers in the old header are also dropped: it referred the reader to
`../lean/QOU/BraidsAndKnots/DIMMasterPentagon.lean` "(file pending)", which does not exist
in the library tree, and spelled the class `DIMMasterPentagon`, which is not the declared
name (the `.ts` manifest's `lean.ref` is `qou:QOU.BraidsAndKnots.DimMasterPentagon`).

## What the block claims

The `.md` is two sentences:

> The Ding–Iohara–Miki algebra $U_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})$ carries a
> universal Pentagon identity that specializes to each operational Pentagon flavor.

[`docs/duality-tracker.md`](../../../docs/duality-tracker.md) row **D17** says which
flavours: *"DIM `U_{q,t}` master Pentagon specialises to Faddeev / Rogers / Macdonald /
Pachner (D15) / Bloch (D16)"*. The literature anchor is Bourgine,
*On pentagon identity in Ding–Iohara–Miki algebra* (arXiv:2112.14687), placed in the
corpus by [`2026-05-24-pentagon-identity-broad-context.md`](../../../docs/audits/2026-05-24-pentagon-identity-broad-context.md)
§2.7, which records the same claim: the Macdonald pentagon and the q-dilogarithm pentagon
are both special cases of a master pentagon for **group-like elements** in DIM.

The block therefore asserts two things, and they need separating: a **master identity
exists**, and it **specialises**. Both are encoded below; the mechanism connecting them is a
theorem, not an axiom.

## What is encoded

**The word shape is the operator/group-like one**, quoted verbatim from the corpus's own
statement of it in
[`q-dilogarithm-pentagon-associator.md`](../quantum-observable-universes/q-dilogarithm-pentagon-associator.md):

    Φ(P) Φ(Q) = Φ(Q) Φ(P + Q) Φ(P)

read here abstractly as `Φ u ⬝ Φ v = (Φ v ⬝ Φ (u ⊛ v)) ⬝ Φ u`, with the argument composition
`⊛` and the operator product `⬝` both carried by the datum. That is Bourgine's shape (a
relation among group-likes), and it is the shape the master identity has.

**`specialises` is a hypothesis about caller-supplied data.** The class takes the master
datum and the family of flavour data as **parameters**, following the design rule recorded
in [`QOU/AlgebraicSubstrate/ConditionalClasses.lean`](../lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean)
after that file's own retraction — *"shape is not content, and the difference is
refutability"*: an `∃` over a self-chosen quantity cannot be false, while a `∀` about a
quantity the *caller* supplies can. So the class **is refutable** —
`dimMasterPentagon_refutable` below exhibits a master/flavour pair at which no instance can
exist — which the previous `holds : Prop` was not.

**The transport is a theorem, not a class field.** `PentagonSpecialisation.transport` derives
the flavour pentagon from the master pentagon along an intertwining, product-preserving,
argument-surjective map. It is an unconditional algebraic fact about word identities and is
discharged here rather than assumed, so the class carries only what is genuinely open: that
such specialisations exist. `transport_apply` is the same statement before surjectivity is
used, which isolates exactly what surjectivity buys — the flavour pentagon on the *image*
needs no surjectivity; reaching *every* flavour argument does.

`PentagonDatum.Holds` is a predicate on data, not a conjecture carrier, so `def … : Prop` is
the right shape for it (matching `PentagonCoherent` in `archimedean-functor-uniqueness.lean`
and `PentagonRegular` in `QBeta/FiveTwoComplexPentagon.lean`); the detector-blindness row for
`def … : Prop` concerns carriers, which is what `DimMasterPentagon` below is and remains.

## What is NOT encoded, and why

**The DIM algebra itself.** The corpus carries no `U_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})`
type — no quantum toroidal algebra, no group-like subset of one. The master datum is therefore
a class **parameter**, not a construction, and this file does **not** claim that the DIM
algebra's group-likes form a `PentagonDatum` satisfying `Holds`. That identification is the
conjecture's substantive content and it stays unformalised. This is the case `qou-tsnp`'s
guard describes — *"if a conjecture's claim cannot yet be stated against existing types … the
honest outcome is to say so and leave the carrier, noting what type must grow first"* — so:
**what must grow first is a Ding–Iohara–Miki (quantum toroidal `gl₁`) algebra type with its
group-like elements.** The claim is *partly* statable, so the statable part is stated.

**Which named flavours are reached.** The flavour index is an arbitrary caller-supplied type
rather than a hard-coded enumeration of the tracker's five, because those five are not all
presented in this word shape. Faddeev's is (it is the display above); Macdonald's and the
Pachner/6j fusion move are operator/state-sum relations of the same kind. **Rogers (D-cluster
q-dilogarithm) and Bloch (D16) appear in the corpus in the *additive five-term* form**
`Li₂(y) + Li₂(x) = Li₂(xy) + Li₂(α) + Li₂(β)` — five terms over five arguments, not four
operators over three. That is the classical limit of the operator pentagon, and a classical
limit is **not** a product-preserving map, so `transport` does not reach it. Hard-coding the
five would assert a uniformity across word shapes that has not been established here.

**NOT claimed:** that any specialisation exists. Axiomatising `specialises` is the §3b
conjecture pattern, not a derivation (AGENTS.md §"Axiomatization is NOT a Proof"). The
Bourgine result is cited by the block; it is not machine-checked here.

**Base ring (§7c).** Nothing archimedean: no `ℝ`, no ordering, no `Real.*`. The operator
product is a bare binary operation rather than a `Monoid`, because the pentagon word is
written with explicit parenthesisation and so needs no associativity — the additive and
multiplicative realisations are then both instances, and requiring less makes the transport
theorem stronger.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/dim-master-pentagon.ts
-/

namespace QOU.BraidsAndKnots

universe uA uO uF

/-- **A pentagon datum.** An argument type with a composition `compose`, an operator type
with a product `mul`, and an assignment `Φ` of an operator to each argument — the data a
pentagon relation is stated about.

`mul` is a bare binary operation, not a monoid multiplication: the pentagon word below is
fully parenthesised, so associativity is never needed, and both the multiplicative operator
form and the additive five-term form are instances. -/
structure PentagonDatum where
  /-- Arguments of the group-like assignment (Faddeev's Weyl-pair operators `P`, `Q`). -/
  Args : Type uA
  /-- Operators the assignment lands in. -/
  Ops : Type uO
  /-- The operator product. -/
  mul : Ops → Ops → Ops
  /-- Composition of arguments (`P + Q` in Faddeev's form). -/
  compose : Args → Args → Args
  /-- The group-like assignment. -/
  Φ : Args → Ops

/-- **The pentagon relation** for a datum: `Φ u ⬝ Φ v = (Φ v ⬝ Φ (u ⊛ v)) ⬝ Φ u`.

This is the Faddeev–Kashaev operator form `Φ(P) Φ(Q) = Φ(Q) Φ(P + Q) Φ(P)` with the
parenthesisation written out. It is a predicate on data, not a conjecture carrier. -/
def PentagonDatum.Holds (D : PentagonDatum.{uA, uO}) : Prop :=
  ∀ x y : D.Args,
    D.mul (D.Φ x) (D.Φ y)
      = D.mul (D.mul (D.Φ y) (D.Φ (D.compose x y))) (D.Φ x)

/-- **A specialisation** of one pentagon datum to another: a map on arguments and a map on
operators that together respect composition, the product, and the group-like assignment.

This is what "the master pentagon *specialises to* a flavour" has to mean if the flavour's
pentagon is to follow from the master's — and `transport` below shows that it does. -/
structure PentagonSpecialisation (master flavour : PentagonDatum.{uA, uO}) where
  /-- The map on arguments. -/
  onArgs : master.Args → flavour.Args
  /-- The map on operators. -/
  onOps : master.Ops → flavour.Ops
  /-- Every flavour argument is hit. Only this field is archimedean-free bookkeeping: it is
  what upgrades the pentagon on the image to the pentagon everywhere (see `transport`). -/
  onArgs_surjective : Function.Surjective onArgs
  /-- The operator map preserves the product. -/
  onOps_mul : ∀ a b, onOps (master.mul a b) = flavour.mul (onOps a) (onOps b)
  /-- The argument map preserves composition. -/
  onArgs_compose :
    ∀ x y, onArgs (master.compose x y) = flavour.compose (onArgs x) (onArgs y)
  /-- The two maps intertwine the group-like assignments. -/
  intertwines : ∀ x, onOps (master.Φ x) = flavour.Φ (onArgs x)

/-- **The pentagon transports along a specialisation, on the image.** Surjectivity is not
used here, which is the point: the flavour pentagon holds at every pair of arguments coming
from the master, whether or not those exhaust the flavour's arguments. -/
theorem PentagonSpecialisation.transport_apply {master flavour : PentagonDatum.{uA, uO}}
    (S : PentagonSpecialisation master flavour) (h : master.Holds) (x y : master.Args) :
    flavour.mul (flavour.Φ (S.onArgs x)) (flavour.Φ (S.onArgs y))
      = flavour.mul
          (flavour.mul (flavour.Φ (S.onArgs y))
            (flavour.Φ (flavour.compose (S.onArgs x) (S.onArgs y))))
          (flavour.Φ (S.onArgs x)) := by
  have key := congrArg S.onOps (h x y)
  simpa [S.onOps_mul, S.intertwines, S.onArgs_compose] using key

/-- **The specialised datum satisfies the pentagon.** This is the derivable half of D17: if a
master identity holds and a specialisation exists, the flavour identity is a consequence, not
a further assumption. Surjectivity of `onArgs` is exactly what extends `transport_apply` from
the image to all of the flavour's arguments. -/
theorem PentagonSpecialisation.transport {master flavour : PentagonDatum.{uA, uO}}
    (S : PentagonSpecialisation master flavour) (h : master.Holds) : flavour.Holds := by
  intro x y
  obtain ⟨a, rfl⟩ := S.onArgs_surjective x
  obtain ⟨b, rfl⟩ := S.onArgs_surjective y
  exact S.transport_apply h a b

/-- **CONJECTURE (D17).** A master pentagon identity — Bourgine's, among group-like elements
of the Ding–Iohara–Miki algebra `U_{q,t}(gl₁ double-hat)` — that specialises to each
operational pentagon flavour.

`master` and `flavour` are supplied **by the caller**, so the class is false at data that do
not satisfy these fields (see `dimMasterPentagon_refutable`). The flavour index `F` is
likewise the caller's: the tracker's five named flavours are not all presented in this word
shape, and hard-coding them would assert more than the header supports.

**This does not say the DIM algebra carries such a datum** — the corpus has no type for that
algebra, so the master datum is a parameter rather than a construction. That identification
is the part of D17 that stays unformalised; see the header.

**No instance is provided.** Downstream results consume this as
`[DimMasterPentagon master flavour]` and are genuinely conditional on it.

-- Ref: [leitner2026] conj:dim-master-pentagon -/
class DimMasterPentagon {F : Type uF} (master : PentagonDatum.{uA, uO})
    (flavour : F → PentagonDatum.{uA, uO}) : Prop where
  /-- **The master identity.** The group-like assignment satisfies the pentagon word. -/
  master_holds : master.Holds
  /-- **The specialisation claim.** Each flavour is reached from the master by a
  composition-, product- and `Φ`-respecting surjection. By `PentagonSpecialisation.transport`
  this forces every flavour's own pentagon, which is what "unified algebraic ancestor" has to
  deliver. -/
  specialises : ∀ f : F, Nonempty (PentagonSpecialisation master (flavour f))

/-- The one-point datum: everything collapses, so the pentagon word is trivially satisfied.
Used only as the master half of the refutation below. -/
def trivialPentagon : PentagonDatum.{0, 0} where
  Args := Unit
  Ops := Unit
  mul := fun _ _ => ()
  compose := fun _ _ => ()
  Φ := fun _ => ()

theorem trivialPentagon_holds : trivialPentagon.Holds := fun _ _ => rfl

/-- A datum whose pentagon **fails**: one argument, operators `ℕ` under addition, and the
constant group-like `1`. The pentagon word reads `1 + 1 = (1 + 1) + 1`. -/
def badPentagon : PentagonDatum.{0, 0} where
  Args := Unit
  Ops := ℕ
  mul := fun a b => a + b
  compose := fun _ _ => ()
  Φ := fun _ => 1

theorem badPentagon_not_holds : ¬ badPentagon.Holds := by
  intro h
  have hx : (1 : ℕ) + 1 = 1 + 1 + 1 := h () ()
  norm_num at hx

/-- The class is **refutable**, which the previous `holds : Prop` carrier was not: the
one-point master datum satisfies the pentagon, so `master_holds` is discharged, but no
specialisation to `badPentagon` can exist — one would transport the pentagon onto a datum
where it fails.

Stated as a theorem rather than left to the docstring because "the carrier asserts something"
is precisely the property that was missing, and a reader should see it discharged rather than
take the prose's word. Note the refutation runs *through* `transport`, so it also exercises
the derivable half above. -/
theorem dimMasterPentagon_refutable :
    ¬ DimMasterPentagon trivialPentagon (fun _ : Unit => badPentagon) := by
  intro hc
  obtain ⟨S⟩ := hc.specialises ()
  exact badPentagon_not_holds (S.transport hc.master_holds)

end QOU.BraidsAndKnots
