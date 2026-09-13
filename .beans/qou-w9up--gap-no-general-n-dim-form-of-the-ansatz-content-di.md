---
# qou-w9up
title: 'GAP: no general (n-dim) form of the ansatz-content dichotomy — only 2x2/3-mass cases exist'
status: todo
type: task
priority: normal
created_at: 2026-09-13T05:11:10Z
updated_at: 2026-09-13T05:12:50Z
---

## The gap (corpus-grepped 2026-09-13, six paths; no general version found)

Three sorry-free theorems in `QOU/Eightfold/` say when a linear mass ansatz has
predictive content. **All three are fixed-size** (3 masses / 2x2). There is no
general n-dimensional statement, and the general statement is where the content is.

- `GellMannOkuboIdentity.gmo_cannot_discriminate (a b c a' b' c' : R)` - the GMO
  relation holds IDENTICALLY under the ansatz, for any parameters. The prediction
  is **vacuous**: observing GMO confirms nothing.
- `DecupletEqualSpacing.equal_spacing_cannot_discriminate (a b c a' b' c' : R)` - same shape.
- `NonetMixingUnconstrained.mixing_unconstrained (d1 l1 l2 : R)` - the ansatz
  constrains **nothing**: with the octet entry `d1` held fixed, EVERY pair of
  physical masses `(l1,l2)` is realised. The prediction is **empty**.
  Its own docstring draws the contrast and says: "Here it forces nothing, so the
  measured mixing IS information - and deriving it would be a real prediction."

## Why a general version is worth proving
The three are two OPPOSITE failure modes of one phenomenon, and the corpus states
the dichotomy in prose but never as a theorem:
- **vacuous** - the relation holds on all of the observable space, so it does not
  test the ansatz;
- **empty** - the ansatz's image IS the whole observable space, so no observation
  can refute it.

Predictive content lives exactly in the annihilator of `im(A)` for the
parameter -> observable map `A`, MINUS the relations that hold identically.
Stated that way it applies to every multiplet in the framework, not just the nonet,
and it is checkable with no numbers in it - so there is no fitting surface.

## Convention safety (checked, because the owner flagged the eightfold conclusions)
`NonetMixingUnconstrained.lean` imports ONLY `Mathlib.Algebra.Ring.Defs` and
`Mathlib.Tactic`; it contains **zero** occurrences of `markovZ`, `q_0`, `q0`,
`Markov` or `convention`; it is generic over `{R} [CommRing R]` and
`charPoly_factors_of_trace_det_match` is proved by `subst; subst; ring`.
It therefore **cannot** be convention-C contaminated - there is no convention in it.
The same check should be run on the other two before leaning on them.

## Default if nothing is done
The dichotomy stays a docstring remark on one 2x2 file, and each future multiplet
re-derives (or fails to notice) whether its ansatz has content.
