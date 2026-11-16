---
# qou-qbe9x
title: 'Geometry gap: C1 has a THIRD singular site at x = q^-2 (orbit [1] on E_q) that no analysis has examined'
status: in-progress
pr: 8195
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T10:10:00Z
updated_at: 2026-10-04T15:10:59Z
parent: qou-frzo
---

**Raised by the owner 2026-08-08:** "are we missing a pair? where are you looking
on one affine chart? do we know its geometry fully?" The answer to the last is
**no**, and here is the concrete thing that was missed.

## What was actually examined

All C1 infinity work -- the 08-01 audits, and everything I did this session --
looked at **one affine chart**: the Newton polygon at `x = infinity` via `deg_x`,
plus the observation that `x = 0` is Fuchsian. Both are LOCAL objects at the two
ends of `C*`.

## The site nobody looked at

`L1 = (q^2 x - 1) sigma^2 - (q-1) sigma - (q-1)`. The LEADING coefficient
degenerates inside `C*`:

    a_2(x) = q^2 x - 1  ->  vanishes at x = q^-2     <-- neither 0 nor infinity
    a_1 = a_0 = -(q-1)  ->  no zeros (q != 1)

So the singular locus is **not** `{0, infinity}`. There is a third site at
`x = q^-2`. On the elliptic curve `E_q = C*/q^Z` -- which is the actual geometry
for a q-difference module, not `P^1` -- that is the class `[q^-2] = [1]`, since
`q^-2` lies in `q^Z`. The **identity orbit**: a distinguished marked point.

## Why this matters for the F(P1,P2) question

The corpus wanted a pair `(P1,P2)`. RSZ (§3.3, integral) and Bugeaud (`bugeaud2011`,
non-integral) both require two slopes **at one point**, and C1 has one slope at
each end -- see `qou-qbp5`. But the geometry is richer than the two ends, and the
richness was never inventoried. Two distinct questions follow:

1. **Is `[1]` an apparent or a genuine singularity?** For q-difference equations a
   zero of the leading coefficient can often be removed by a shearing/gauge
   transformation; the standard normalisation asks that `a_0` and `a_n` not vanish
   in a fundamental annulus. **Do not assume either way** -- this is exactly the
   sort of unchecked assumption that produced the level-`d` error. CHECK IT.
2. **If genuine, what local data does it carry?** and does the global connection
   datum on `E_q` (the surviving rescue-1 Birkhoff route) run between three sites
   rather than two? That would change the expected dimension count, and the
   corpus's `C^2` would need re-deriving from the actual configuration.

## Method note

This was found by asking what the geometry IS rather than re-reading what was
computed. The Newton polygon is a local invariant; computing it correctly at
infinity says nothing about whether infinity is the only interesting place. The
generalisable lesson: **inventory the singular locus before classifying at any
one point of it.**

## Deliverable

A short, exact write-up of C1's singular locus on `E_q`: every site, its type
(Fuchsian / irregular with slope / apparent), and whether `[1]` survives
normalisation. Exact arithmetic; no fitting. Blocks nothing, informs `qou-qbp5`
(the F(P1,P2) objection) and `qou-qbq6` (A1,A2).

## ANSWERED 2026-08-08: the site is GENUINE, not apparent

Companion form `Y(qx) = A(x) Y(x)` with `Y = (y(x), y(qx))^T`:

    A(x) = [[0, 1], [a, a]],   a := (q-1)/(q^2 x - 1)
    det A(x) = -a = -(q-1)/(q^2 x - 1)

On `C*` (q generic): the numerator is a nonzero constant, the denominator has a
simple zero at `x = q^-2`, so `det A` has a **simple pole** there and no zeros:

    div(det A)|_{C*} = -[q^-2],   DEGREE -1

**Degree is a gauge invariant.** Under `Y -> F Y` we get `A -> (sigma F) A F^{-1}`,
so `det A -> (sigma g / g) det A` with `g = det F in C(x)*`. For
`g = x^k prod (x - c_i)^{m_i}`,

    div(sigma g / g)|_{C*} = sum_i m_i ( [c_i/q] - [c_i] )   -- degree 0, always.

So `deg div(det A)|_{C*}` cannot be changed by any gauge transformation. Here it
is `-1 != 0`. **No gauge clears the singularity out of `C*`: the site is not
removable.**

*Precision on the claim.* This shows the MODULE is genuinely singular somewhere in
`C*` (the connection matrix necessarily degenerates on the orbit). It is not by
itself a statement that the local solution space drops rank -- "apparent
singularity" in the classical sense is a finer question. What is settled is that
the site cannot be normalised away, so it must appear in any inventory of C1's
geometry.

## The (0, ?, infinity) structure — owner's question, and a deflation

Owner asked whether `(0, [1], infinity)` aligns with Bring's spacetime `P^1`, and
whether the middle site is `z_q` or `[1]_q`.

- `[1]_q = (q-1)/(q-1) = 1` **identically**, for every `q`. So `[1]_q` and `1` are
  the same object; that refinement adds no structure.
- As a point of `C*` the site is `x = q^-2`. As a class on `E_q = C*/q^Z` it is
  `[q^-2] = [1]`, since `q^-2 in q^Z`. Both descriptions are correct, at different
  levels.

**Deflation (important).** Any three distinct points of `P^1` are Mobius-equivalent
to `(0,1,infinity)`. Three points admit no cross-ratio, hence no modulus. So
"C1 has three marked points, therefore Bring's `P^1`" carries **no information**
on its own -- it is exactly the shape of coincidence the anti-numerology
discipline targets. Do NOT record such an alignment as evidence.

**What does survive, and is better.** In the q-setting the symmetry is not `PGL_2`
but the dilation `x -> qx`. Under THAT group:

- `0` and `infinity` are precisely its **two fixed points**;
- the third site is a full **q-orbit**, and it is the orbit of the **identity**.

So the triple is *(fixed point, identity orbit, fixed point)* -- canonical rather
than chosen. That is why `q^-2` "is" `1` here: the actual symmetry, not a numerical
coincidence.

**To make the Bring link substantive you need a MAP, not a count.** Concretely:
what are the marked points of Bring's `P^1` in the corpus, and is there a morphism
relating `E_q` (or `C*` with its dilation) to that base which carries the identity
orbit to the corpus's marked point? Until such a map is exhibited, treat the
three-point alignment as unsupported.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8195)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/C1SingularLocusAndSlopeLevelBridge.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/c1-singular-locus-and-slope-level-bridge.witness.json` (`scriptHash: fc315c730706`, `scriptCommitSha: 17c1b41227b6c499979110fb6c31637514935ccf`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8195 (`4d59250dbada4070a6545f88b8d6f14fb94d89f6`).
