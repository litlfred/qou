---
# qou-w9up
title: 'GAP: no general (n-dim) form of the ansatz-content dichotomy — only 2x2/3-mass cases exist'
status: completed
type: task
priority: normal
created_at: 2026-09-13T05:11:10Z
updated_at: 2026-09-13T10:33:35Z
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


## CLOSED 2026-09-13 — the general form is on `main` (merge `3cb26d4b9f8`)

`content/quantum-observable-universe/lean/QOU/Eightfold/AnsatzContentDichotomy.lean`,
sorry-free, generic `{R : Type*} [CommRing R]`, no numerals, no `q`, no Markov
parameter and no anchor — so nothing in it can be convention-C contaminated.

The gap this bean names was *"the corpus states the dichotomy in prose but never
as a theorem"*. It is now a theorem, and the statement is the one the bean asked
for: predictive content lives in the annihilator of `im(A)` minus the relations
that hold identically.

- `vacuous_of_forces_of_unconstraining` — **the two failure modes are one.** An
  ansatz nothing can refute (`Function.Surjective`) forces only relations that
  were true of every conceivable observable tuple.
- `not_unconstraining_of_discriminating` — the usable contrapositive: a genuine
  prediction **certifies that the model is restrictive**.
- `exists_unreachable_of_discriminating` — makes it operational by naming the
  falsifying observation.
- `nonetAnsatz_unconstraining` re-derives `mixing_unconstrained` as an instance;
  `equalPairAnsatz_discriminating` exhibits the non-degenerate case, so the
  dichotomy's hypothesis is not vacuously satisfiable.

Verification: `lean -DautoImplicit=false -s 65536` exit 0; `#print axioms` on all
8 theorems shows no `sorryAx`. The file imports **only Mathlib** (zero `QOU`
imports), so it is import-cone-disjoint from the rest of the corpus.

One commit shipped RED and said so (`UNVERIFIED` in its own message, a dead
tactic line after `simp` had already closed the goal); fixed in `79ad19219`
before merge. Recorded because a bare `lean` run would not have caught it.
