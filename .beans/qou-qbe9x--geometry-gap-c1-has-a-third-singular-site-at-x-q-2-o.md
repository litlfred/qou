---
# qou-qbe9x
title: 'Geometry gap: C1 has a THIRD singular site at x = q^-2 (orbit [1] on E_q) that no analysis has examined'
status: todo
type: task
priority: high
created_at: 2026-08-08T10:10:00Z
updated_at: 2026-08-08T10:10:00Z
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
