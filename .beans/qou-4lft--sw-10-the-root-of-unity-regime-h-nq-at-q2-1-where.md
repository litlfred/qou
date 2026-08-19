---
# qou-4lft
title: 'SW-10: the root-of-unity regime — H_n(q) at q^2 = 1, where seminormal form fails'
status: todo
type: task
priority: normal
created_at: 2026-08-19T13:43:42Z
updated_at: 2026-08-19T19:55:53Z
parent: qou-59vq
---

## Why this exists

Every general-lambda result in the SchurWeyl tree carries `q != 0` and `q^2 != 1`
— over R exactly *q is not a root of unity*, the genericity [ram1997] and
[hoefsmit1974] presuppose. Filed 2026-08-19 when #5290 (`qou-t8qh`) closed the
last sorry in the tree, so that the excluded regime is a tracked item rather
than an unremarked hypothesis.

## This is NOT a hypothesis to relax by a better proof

At a root of unity the statements do not merely become harder — they become
FALSE in their current shape:

- `H_n(q)` is no longer semisimple, so there is no Wedderburn iso to
  `(+)_lambda M_{d_lambda}`.
- The partitions lambda |- n no longer index the irreducibles.
- `seminormalParam q d = (q - q^-1)/(1 - q^{-2d})` has a ZERO denominator
  whenever q^{2d} = 1, so the seminormal matrices do not exist at all; at
  q = -1 with even d it is 0/0.
- `Theta = barSymJMSum` acting by a scalar on a d_lambda-dimensional block is
  exactly the shape that fails.

The honest framing is therefore **a different statement for a different
regime**, via cellular / Specht theory (Graham-Lehrer, Dipper-James) rather
than seminormal form — cell modules exist at every q; irreducibility is
replaced by the radical quotient of the cellular bilinear form, and the
irreducibles are indexed by e-regular partitions where e = ord(q^2).

## Prerequisite check before anyone starts

Corpus-grep first: `SpechtStandardBasisCore.lean` and
`SpechtWedderburnCriterion.lean` under BraidKnot are substantial and may
already carry the cellular-side infrastructure this needs. Nothing should be
built here before that is measured.

## Priority

LOW for the QOU program. The physics evaluates at the substrate q0 ~ 1.10998,
which is not a root of unity, so nothing downstream is blocked by this. It is
filed for completeness of the mathematical arc, and because leaving an excluded
regime unnamed is how a hypothesis quietly becomes an assumption.


## Prerequisite MEASURED 2026-08-19 — the answer is NO. Do not start expecting a wiring job.

The §"Prerequisite check before anyone starts" above says `SpechtStandardBasisCore.lean`
and `SpechtWedderburnCriterion.lean` "are substantial and may already carry the
cellular-side infrastructure this needs". They are substantial. They do **not** carry it.

Measured on main `4c8cc533b5` across all **20** `*Specht*` files, **9,050 lines**, all
sorry-free:

| probe | result |
|---|---|
| `(q :` binders — any deformation parameter at all | **0** |
| base object | `MonoidAlgebra k (Equiv.Perm (Fin n))` — the classical group algebra |
| occurrences of the string `Hecke` | **1**, and it is a *docstring* line reading "the corpus's Hecke conventions specialise at q = 1" |

Zero `q` binders in nine thousand lines is the decisive number: this stack has no
deformation parameter, so it cannot be the `q`-cellular theory SW-10 needs. It is the
**q = 1 classical Specht theory**, and its own docstring says so.

Corpus-wide, `cellular` / `Graham-Lehrer` / `Dipper-James` / `e-regular` match six files,
and all six are false positives on inspection:

- `BraidKnot/IwahoriHeckeAPI.lean` — a `-- Ref: [dipper-james1986]` bibliography line.
- `BraidKnot/TwoFiltrationBridge.lean` — "partition-cellular GB-depth", a
  Gröbner-basis-depth notion unrelated to cellular algebras.
- `QBeta/MarkovGramDegenerate.lean` — names a Python probe
  (`gram_radical_cellular_revalidation.py`).
- `AppendixSurreals/Conjectures.lean`, `StandardModel/ColourHeckeRegularHost.lean`,
  `SchurWeyl/QJucysMurphy.lean` — passing mentions.

**There is no cell module, no cellular bilinear form, and no e-regular indexing anywhere
in the tree.** SW-10 is a from-scratch build of Graham-Lehrer/Dipper-James cellular
theory over the Hecke algebra, not a wiring exercise over existing infrastructure. Scope
it as multi-session before claiming it.

The classical stack is not useless — `SpechtClassification`, `SpechtIrreducible`,
`SpechtDominanceCore` give the combinatorial skeleton (dominance order, standard basis,
branching) that the `q`-deformed statements mirror. But it is a *template* to follow, not
a dependency to import: nothing in it is parameterised over `q`, so nothing in it
specialises to the root-of-unity case by instantiation.

### Correcting my own reporting

I first reported this as "zero occurrences of `Hecke`" after checking four files and
generalising to twenty. The true count is **1**. It does not change the conclusion — the
one hit is a comment saying the stack is the q = 1 specialisation, which supports it —
but the number I gave was wrong, and the `(q :` binder count is the measurement that
actually decides the question.
