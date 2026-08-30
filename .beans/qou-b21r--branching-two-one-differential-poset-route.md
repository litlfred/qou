---
# qou-b21r
title: 'branching_two_one: the differential-poset route (needs ONE lemma, not RSK)'
status: todo
type: task
priority: normal
tags:
    - lean
    - needs:combinatorics
created_at: 2026-08-30T14:46:08Z
updated_at: 2026-08-30T14:46:08Z
---

`RSKIdentitiesContext.branching_two_one` is the class's one remaining open field
(QOU/BraidKnot/YoungTableauStandard.lean). Its docstrings said it is "discharged by the RSK
correspondence", the open P1-P5 program. **That is probably wrong, and it is the same
mis-diagnosis that kept `sum_dimSYT_eq_involution` parked for weeks** (qou-jlam, qou-m3xr).

## The route

    G(mu, k) := sum_{|lam|=k} f^lam * f^{lam/mu},    claim  G(mu,k) = (k!/|mu|!) * f^mu

At mu = (2,1) -- f^mu = 2, |mu|! = 6 -- that is `3 * sum = k!`, i.e. branching_two_one verbatim.

Induction on k, base G(mu, |mu|) = f^mu (the only lam of size |mu| containing mu is mu):

    G(mu, k+1) = sum_lam f^lam * sum_{nu <. lam, nu >= mu} f^{nu/mu}   [skew branching]
               = sum_nu  f^{nu/mu} * sum_{lam .> nu} f^lam             [transpose]
               = sum_nu  f^{nu/mu} * (k+1) * f^nu                      [upSum_eq]
               = (k+1) * G(mu, k)

## Status of the three inputs

* **upSum_eq** -- PROVED sorry-free (PR #6164), QOU/Mathlib/YoungLatticeUpOperator.lean.
* **the transposition** -- the same Finset.sum_comm manoeuvre `pairTerm` performs in that
  file; the device carries over directly.
* **skew branching** -- THE ONE OPEN INPUT. `f^{lam/mu} = sum over corners c of lam with
  c not in mu of f^{(lam-c)/mu}`, i.e. remove the largest entry of a skew SYT. Direct
  analogue of the proved QOU.Mathlib.numStandardYoungTableaux_branching, over
  `SkewStandardYoungTableau` (QOU/BraidKnot/YoungTableauStandard.lean:134, `fDimSkew`, which
  guards on containment and is 0 otherwise -- the guard matters, see
  `skewSYT_nonempty_of_not_le`: unguarded, branching_two_one is FALSE at k=3).

## Evidence, and its limit

`computations/combinatorics/branching_two_one_route_probe.py` confirms the identity EXACTLY
for k = 3..11 (exact integers, no float constructed).

**It does NOT verify skew branching.** The probe computes f^{lam/mu} BY that recursion, so it
assumes the open input. Read it as "the route's arithmetic is sound", not as a partial proof.
Stated explicitly because the whole point of this bean is that a plausible-sounding
justification was previously mistaken for an established one.

## Do not

* Do not record branching_two_one as proved, or the route as more than a route.
* Do not conclude from qou-jlam that "no RSK identity needs RSK". THIS one has a checked
  non-RSK route; that says nothing about the other RSK-family targets.
* Do not remove the containment guard on fDimSkew to simplify the sum -- it is what makes the
  statement true.
