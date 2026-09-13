---
# qou-a2w5
title: 'GAP: does the assembly move the pair separations, and by how much — route (2)''s entire many-body content, unmeasurable until a nucleus has a derived geometry'
status: todo
type: task
priority: normal
created_at: 2026-09-13T19:14:01Z
updated_at: 2026-09-13T19:14:44Z
---

Extracted from `qou-o6ml` §"CONSTRAINT 3b" (2026-09-13, MobiusMutualChannel.lean
section 9g), which names this in one sentence and gives it no tracker. It is the
arc's one precisely-stated open problem and it was sitting in a 1,856-line bean.

## The statement, and it is a theorem not a hope

`mobius_b3_ne_zero_forces_moved_sep` (sorry-free, `[propext, Classical.choice,
Quot.sound]`; file 52/52, `lean -DautoImplicit=false -s 65536` exit 0):

> Any nonzero `b_3` from the Mobius mutual channel is **entirely** the
> assembly's effect on the pair separations.

Contrapositive of `mobius_b3_eq_zero_of_sep_eq`, which routes through
`b3_eq_zero_of_pairLocal`: if the assemblies do not move the pair's
separations, `b_3` vanishes identically.

AME2020 gives `b_3 = +1.4262225` MeV (`AmeBindingNotPairwise.ame_b3_eq`); the
model gives exactly **0**. So the hypothesis is not idle — something must move,
or route (2) contributes nothing to the extensive term.

**THE OPEN QUESTION, verbatim from section 9g:** *"NOT CLAIMED: that the
assemblies DO move the separations in this framework, nor by how much. That is
a geometric measurement section 9g does not make, and it is the open thing."*

## WHY IT CANNOT BE MEASURED TODAY — checked, not assumed

`sep` is a **bare field** of `LinkEmbedding` (`MobiusEnergy.lean:228`):

    sep : Fin n -> Real -> Fin n -> Real -> Real

carrying only axioms — `sep_symm`, `sep_nonneg`, `disjoint`, `sep_self`. No
derivation. To ask whether an assembly moves the separations you need a
**concrete configuration per assembly**, and the corpus has none.

Measured: every concrete `LinkEmbedding` in the tree is a synthetic test family.

  shrinkingLink      MobiusMutualChannel.lean:165   a COUNTEREXAMPLE (no uniform
                                                    separation exists for it)
  separatedLink m R  MobiusMutualChannel.lean:1025  a PARAMETERISED family, used
                                                    to prove no positive uniform
                                                    lower bound exists
  Nonempty (LinkEmbedding M n)  MobiusEnergy.lean:323   an existence witness

**None of them is a nucleus.** Nothing in the corpus says "this is 3He's
geometry".

## SO THIS IS THE SIXTH RELOCATION TO THE SAME BLOCKER — but its SHAPE changed

Routes (1), (2), (4), the flux leg and the upper-bound leg all terminate at
"the framework has no derived geometric realisation of a nucleus". This makes
six. Recording that plainly so nobody reads this bean as an independent front.

**But what is needed is NOT what the volume route needed, and that difference is
the actionable part.** The carrier blocker was *which census link is the nucleus*
— a **topological type**, for a hyperbolic-volume lookup. This needs a canonical
**metric configuration**: separations, not volume. Two consequences:

1. **The `A+1` closure being non-geometric does NOT disqualify it here**
   (`qou-mbbf`: every atom non-hyperbolic, volume exactly 0, all six
   word/averaging settings). A non-hyperbolic link still embeds in `R^3` with
   perfectly good separations; it just carries no canonical hyperbolic metric.
   So the measurement that closed the *volume* route does not close this one.
2. **The requirement is strictly weaker than the volume route's** — and that is
   the one direction this arc has not been pushed.

## WHOSE IT IS

Section 9g's own conclusion: *"the route's deliverable is the same object
`qou-ales` is deriving (gamma-gamma + the confinement SDP at q_0), not a separate
one."* That matches `qou-mbbf`'s independent arrival from the carrier side — two
routes, one conclusion, reached the same day without contact.

`qou-ales` selects **words** (`beta_Bor`, the H_6 bond `G^3`) and has never been
asked for a **geometry**. Whether it can be is a framing question for that bean,
not this one.

## NOT CLAIMED

That the assemblies do or do not move the separations (unmeasured — that IS the
gap); that a geometry is derivable from a gamma-gamma-selected word; that route
(2) is dead (it is not — section 9g is a specification of what it owes, not a
refutation); or that this bean is independently workable today (it is not, and
the "why" above is the point).

## CROSS-LINKS

  qou-o6ml   the arc; CONSTRAINT 3 and 3b are its two newest entries
  qou-dux3   completed — the FHW route end to end, "empty where we need it"
  qou-mbbf   the A+1 component law + the non-geometricity measurement
  qou-ales   gamma-gamma + confinement SDP; owns the derived-object question
  qou-brng / qou-rwhv / qou-eptr   the b_3 extensive-term front (all in-progress)
