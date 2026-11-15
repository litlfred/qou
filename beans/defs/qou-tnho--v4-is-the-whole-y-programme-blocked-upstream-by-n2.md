---
# qou-tnho
title: 'V4: is the whole Y programme blocked upstream by N=2 (row cap)?'
status: completed
type: task
priority: normal
created_at: 2026-08-10T18:23:24Z
updated_at: 2026-08-29T09:02:50Z
---

STRATEGIC / do this first if cheap. #4640 proved sorry-free that N=2 cannot host
the eightfold decomposition (dim V_(1^3) = C(N,3) = 0 iff N<3; decuplet forces
N=3) and the chapter records dim V = 2 as what the framework supplies, with N=3
OPEN. Y is a flavour quantum number on the A_2 weight lattice, which needs N=3.
QUESTION: is the entire hypercharge programme downstream of an unavailable
construction? If yes, V1-V3 are refinements of a blocked branch and the honest
priority is the N=3 construction instead. Cheap to settle by reading the chapter's
own conditionality ledger.


---

# SETTLED 2026-08-29 — YES, blocked upstream. Answer read from the chapter's own ledger.

Taken over as a stalled claim: `in-progress` since 2026-08-10T18:25Z, 19 days
with no movement and no backing branch found. The bean said this was "cheap to
settle by reading the chapter's own conditionality ledger" and it was --
the answer is two lines of `eightfold-open-problems.md`.

## The answer

`content/quantum-observable-universe/eightfold-way/eightfold-open-problems.md`

Line 20, the conditionality ledger row:

  dim V = N = 3 for the flavour fundamental | **open**: framework supplies
  dim V = 2; no q raises the row cap. The *obstruction* is proved; the
  *construction* is missing

Line 39:

  **N = 3** gates every flavour statement below

Line 18, for completeness, marks the octet/decuplet representation theory
"**conditional on N = 3**".

`Y` is a flavour quantum number on the A_2 weight lattice. Every flavour
statement is gated on `N = 3`. `N = 3` has a PROVED obstruction and a MISSING
construction. Therefore the whole `Y` programme sits downstream of an
unavailable construction. **The bean's hypothesis is confirmed.**

## Consequence, which the bean itself stated

"If yes, V1-V3 are refinements of a blocked branch and the honest priority is
the N=3 construction instead."

That now applies. Concretely, the artifacts below are refinements of a blocked
branch -- all of them honest, none of them wrong, but none of them reachable
until `N = 3` exists:

  sm-hypercharge-invariant.lean      HyperchargeInvariant, content-bearing
                                     class, NO INSTANCE (correctly open)
  SecondCrossingInvariant.lean       the Milnor triple-linking candidate
  WritheIndependenceCriterion.lean   a prior agent's correction: the p/n test
                                     falsifies only an INJECTIVE writhe->Y map
                                     (Y = w^2/4 passes), so the published
                                     argument does not establish the
                                     independence requirement it is cited for
  HyperchargeBatteryReduction.lean, TwistBatteryVacuity.lean, etc.

## What I did NOT do, and why

I had a candidate lemma for this area: if `Q` factors through `w` AND `I_3`
factors through `w`, then `Y = 2(Q - I_3)` factors through `w`, contradicting
`HyperchargeInvariant`'s non-factorization clause -- so the INTENDED
instantiation (`Q = w/2`, and the 2026-06-02 audit's finding that the writhe
carries `I_3`) cannot instantiate the class. It is true and I believe it is not
in the corpus (`factors_through_iff` is the only factorisation statement there).

I did not add it. It is a sharper prune on a branch that is already blocked
upstream, so it would refine exactly what this bean says to stop refining. It
is recorded here so it is not lost, and it is worth adding IF the `N = 3`
construction ever lands.

## Corpus-grep note

This area is unusually well-worked and nothing here is a defect. The
hypercharge conjecture is correctly kinded, carries "no instance", bans tuning
explicitly, and a prior agent has already corrected its supporting argument.
The finding is strategic ordering, not error.
