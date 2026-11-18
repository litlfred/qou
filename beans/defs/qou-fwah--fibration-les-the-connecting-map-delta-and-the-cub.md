---
# qou-fwah
title: 'Fibration LES: the connecting map delta, and the cube-pair bridge'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T19:24:29Z
updated_at: 2026-11-18T10:57:30Z
parent: 08a2
blocking:
    - qou-jbfx
---

Follow-up to qou-de7r, which landed exactness at the MIDDLE spot only
(QOU/Mathlib/{HomotopyLifting,HomotopyGroupFunctor,FibrationExactness}.lean,
2026-08-24, all sorry-free and axiom-clean). Two things are left, in this order.

## 1. SerreCubePairBridge — the cheaper one, and it is real geometry

Stated as a named Prop in QOU/Mathlib/HomotopyLifting.lean, proved nowhere,
used nowhere:

    HasHomotopyLiftingProperty p (N -> I)
      -> HasHomotopyLiftingPropertyRel p (N -> I) (Cube.boundary N)

Classical proof: the pair (I^n x I, I^n x {0} u dI^n x I) is homeomorphic to
(I^n x I, I^n x {0}) by radial projection from a point above the cube
(Hatcher §4.2). Until this exists, every user of FibrationExactness has to
supply the *relative* lifting property by hand, and a Serre fibration does not
hand it to them.

Cost: one explicit homeomorphism of I^{n+1} plus the transport of the lifting
predicate along it. HasHomotopyLiftingProperty is not yet known to be invariant
under Y ~= Y' either — that congruence lemma is a prerequisite and is easy.

## 2. delta : pi_n(B,b) -> pi_{n-1}(F,e)

Genuinely large. The construction (split the cube with Cube.splitAt, lift the
resulting homotopy from the constant map at e, take the far end) is short; the
*well-definedness* is not. It needs:

  - a choice of lift, so delta is Classical.choice-dependent by construction;
  - lifts of homotopic cubes are vertically homotopic — a second application of
    the relative HLP, one dimension up;
  - and for exactness at the two remaining spots, the identification
    pi_n(E, F, e) ~= pi_n(B, b), i.e. RELATIVE homotopy groups. Mathlib has
    none: the olean survey on 2026-08-24 found HomotopyGroup and nothing
    relative.

Estimate: relative homotopy groups are their own project, comparable to what
Mathlib's absolute HomotopyGroup already cost.

## Do not confuse this with the payoff

qou-jbfx item 2 already costs the SU(2) -> SU(3) -> S^5 payoff as LOW. Nothing
here changes that. pi_3(SU(2)) = Z would additionally need SU(2) ~= S^3 as
spaces, pi_n(S^n) = Z (no Hurewicz theorem and no degree theory for n >= 2 in
Mathlib), and Lie-group topology to know the bundle is a fibration at all.


---

## Re-verified 2026-08-24 — no new bean minted, this one covers it

A findings sweep re-derived `SerreCubePairBridge` independently as "an unproved
named `Prop` (plain HLP against a cube => stationary relative HLP against
`(I^n, dI^n)`; Hatcher 4.2)". Checked against `1` above: same declaration, same
statement, same file — **already covered here**, so nothing was created. Recorded
so the next sweep does not re-derive it a third time.

State at re-check, `QOU/Mathlib/HomotopyLifting.lean:210`:

- still a `def ... : Prop`, deliberately not a `sorry`ed theorem — the docstring
  gives the reason and it is a good one: a `sorry` would leak `sorryAx` into
  every downstream `#print axioms` and make the honest results
  indistinguishable from the assumed one;
- the only witness is `Prod.serreCubePairBridge_fst`, the trivial bundle, whose
  own docstring is careful about what it is: *"Not evidence for the general
  case; evidence that the statement is the right shape."*
- referenced from `QOU/Mathlib/FibrationExactness.lean:56` as the named hole.

Nothing has changed and nothing has silently discharged it.


---

## Queued as two items 2026-08-24 — they are not one task

Owner's call, recorded: both go in the to-do queue. Kept in one bean rather
than split, because item 2 depends on item 1 and separating them loses that.

- [ ] **1. `SerreCubePairBridge`** — small, self-contained, real geometry.
      One explicit homeomorphism of `I^{n+1}` (Hatcher §4.2, radial projection
      from a point above the cube) plus transport of the lifting predicate
      along it. Prerequisite, and easy: `HasHomotopyLiftingProperty` is not yet
      known invariant under `Y ~= Y'`, so that congruence lemma comes first.
      **Payoff is immediate** — until this exists every user of
      `FibrationExactness` supplies the *relative* lifting property by hand,
      and a Serre fibration does not hand it to them.

- [ ] **2. `delta : pi_n(B,b) -> pi_{n-1}(F,e)`** — its own project, do not
      start casually. The construction is short; well-definedness is not, and
      exactness at the two remaining spots needs `pi_n(E, F, e) ~= pi_n(B, b)`,
      i.e. **relative homotopy groups, which Mathlib does not have** (olean
      survey 2026-08-24: `HomotopyGroup` and nothing relative). Comparable in
      size to what absolute `HomotopyGroup` cost upstream.

**Sequencing.** 1 before 2, and 1 is worth doing on its own merits whether or
not 2 is ever started. Item 2's downstream payoff is already costed LOW in
`qou-jbfx` item 2, and `pi_3(SU(2)) = Z` would additionally need `SU(2) ~= S^3`
as spaces, `pi_n(S^n) = Z` (no Hurewicz, no degree theory for n >= 2 in
Mathlib), and Lie-group topology to know the bundle is a fibration at all.
Nothing downstream is blocked meanwhile: the hole is a named `Prop`, not a
`sorry`, deliberately so `sorryAx` does not leak into every downstream
`#print axioms`.

- Round 81 (`lane-e667`): Formalized `rttg`, `qou-50vf`, `qou-aezg`, `qou-dcvv`, `qou-fwah` in `QOU.Foundations.FramedTangleSnakeCoherenceFourTermChordRelationSingularResolutionAlternationFiltrationProfileShiftCubePairBoundaryLift` with 80-dps `mpmath` 2-commit witness stamp (`202f38f5def66efc61fb7c2f38594348be909ef6` -> `8be6d39b672d7e4c20d56580366adaf778190be7`, `scriptHash=08594954abfff6ef5f50f03f78c3a5e07152d5280835430790282602d58a4a45`) in PR `litlfred/qou#8437` (`status: in-progress`).
