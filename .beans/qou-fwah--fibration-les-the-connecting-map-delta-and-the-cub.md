---
# qou-fwah
title: 'Fibration LES: the connecting map delta, and the cube-pair bridge'
status: todo
type: task
priority: low
created_at: 2026-08-24T19:24:29Z
updated_at: 2026-08-24T19:24:29Z
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
