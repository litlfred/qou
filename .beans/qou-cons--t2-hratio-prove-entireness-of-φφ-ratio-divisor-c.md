---
# qou-cons
title: 'T2: hratio — prove entireness of Φ₁/Φ₂ ratio (divisor cancellation: two FaddeevPhi solutions share zero/pole lattice)'
status: todo
type: task
created_at: 2026-07-27T14:57:31Z
updated_at: 2026-07-27T14:57:31Z
---


## 2026-08-08 — NOT PROVABLE AS STATED. The class has no regularity field.

After qou-rp5f was reduced to this bean, `hratio` is the single remaining input
to uniqueUpToScalar. It cannot be derived from `FaddeevPhi b Phi` and
`FaddeevPhi b Psi`.

`FaddeevPhi` has exactly three fields — `hb`, `shift_b`, `shift_binv` — and NONE
asks for holomorphy, continuity, or even measurability. So the solution set is
closed under multiplication by ANY doubly-periodic function, however bad.
Sorry-free in `QOU/Mathlib/FaddeevSolutionSet.lean`:

    faddeevPhi_mul_periodic          FaddeevPhi Phi + E periodic under ib and i/b
                                     => FaddeevPhi (Phi * E)
    latticeIndicator                 the indicator of Z.ib + Z.(i/b)
    latticeIndicator_periodic_b/binv doubly periodic, values in {0,1}
    faddeevPhi_mul_latticeIndicator  the witness: Phi * latticeIndicator is
                                     another FaddeevPhi solution

Both shift axioms carry a prefactor that does not see E, and the half-shifts
+-ib/2 differ by exactly the period ib — so E cancels. Pure algebra, no analysis.

WHY THIS IS THE RIGHT DIAGNOSIS, not a technicality: the classical solution set
is Phi_b * {ELLIPTIC}, and "elliptic" carries the regularity that makes the ratio
meromorphic. Strip regularity from the class and "elliptic" degrades to "doubly
periodic", which is far too big. DoublyPeriodicLiouville.const_of_doublyPeriodic
is precisely the statement that DIFFERENTIABILITY closes that gap — the missing
hypothesis is exactly the one the class lacks.

TWO HONEST ROUTES, pick one:
  (a) add a regularity field to FaddeevPhi (meromorphy) and re-derive the divisor
      statement from the shift equations; or
  (b) keep the class and carry hratio as a hypothesis about the specific pair —
      which is what ratio_const_of_entire_ratio already does.

What is NOT available is proving this bean from what is currently there. Anyone
who tries using only the three class fields is wasting the attempt.

Status left todo: the bean is real work, but its statement needs fixing first.

## 2026-08-08 (later) — AND THE REDUCTION IS CIRCULAR. hratio IS the theorem.

Beyond being unprovable from the class, `hratio` is not a sub-problem at all.
Proved sorry-free in `QOU/Mathlib/RigidityReductionScope.lean`:

    hratio_iff_conclusion (hper) :
      Differentiable C (fun z => Psi z / Phi z)  <->  exists c, forall z, Psi z / Phi z = c

Forward is `ratio_const_of_entire_ratio`; backward is that a constant is
differentiable. Given `hper` — which IS smaller, and is now discharged
(qou-rp5f / FaddeevRatioPeriodic) — the hypothesis `hratio` and the conclusion
`uniqueUpToScalar` are the SAME STATEMENT. Classically: the ratio is elliptic,
and an elliptic function is entire exactly when it is constant.

So the advertised reduction

    uniqueUpToScalar  <==  hratio (qou-cons) + hper (qou-rp5f)

has one real edge (hper, done) and one identity edge. Anyone who "proves this
bean" has proved uniqueUpToScalar outright, using an input that is nowhere in the
current chain.

WHAT THE MISSING INPUT IS. FaddeevSolutionSet shows the solution set absorbs any
doubly-periodic factor, so the functional equations ALONE cannot pin a solution
up to scalar; with regularity that becomes "elliptic", and non-constant elliptic
functions exist. An extra condition is MANDATORY: a growth bound, a minimality
principle, or a pinned divisor.

THIS PARTIALLY REHABILITATES THE HADAMARD DIRECTION (qou-v4if). Its retracted
motivation — "phiBProd is selected among its elliptic multiples by a
growth/minimality principle" — was reaching for exactly this mandatory input, and
was RIGHT that one is needed. What was wrong was aiming Hadamard at phiBProd,
which is not entire. A growth argument aimed at the two entire HALVES, or at a
pinned divisor, is still a live candidate — a much smaller claim than the one
retracted, and proved nowhere yet.

RESTATE THIS BEAN before working it. As written it is the theorem, not a step.
