---
# qou-w1j9
title: Habiro's twisting element omega settles qou-7dzg's (A)-vs-(B) — the ribbon twist is colour-determined, not a free label
status: todo
type: task
priority: normal
created_at: 2026-08-24T17:33:32Z
updated_at: 2026-08-24T17:34:05Z
---

## The source, and why it is decisive

`library/1172-3/sections/sec-005-6-the-twisting-element.md` (Habiro, *On the
colored Jones polynomials of some simple links*, §6) — already in
`references.ts` as docId `1172-3`, so this is a **citation**, not a new result.

Habiro defines `t : B -> B`, the Z[A,A^-1]-linear map given by **one positive
full twist**, and pins it uniquely on the JW basis:

    t(e_n) = (-1)^n A^{n(n+2)}

and an element `omega` in the completion B-hat' with `<omega^{+-1}, x> =
<t^{+-1}(x)>` for x in B^even, i.e. omega **implements** framing change by
encircling.

## What that does to qou-7dzg

7dzg established that `appendix-standard-model/strand-twist-datum.md` asserts two
incompatible sentences: (A) the datum IS the ribbon structure's framing, and (B)
the datum varies at fixed braid word — with (B) load-bearing for the hypercharge
candidacy. 7dzg concluded they cannot both hold but left which one survives open.

Habiro §6 answers it: the ribbon twist is a **scalar determined by the colour**,
exponent `n(n+2)` (the Casimir). There is no free per-strand integer in it. So
**(A) survives and (B) is false of the ribbon framing.** The `t_i : Fin n -> Z`
datum is an extra label the corpus attached to the ribbon structure's name.

This agrees with, and supplies the positive half of, `TwistSeparationContent.lean`
(new on main), which showed the Lean witness `exists_same_writhe_ne_totalTwist`
mentions no braid word at all — its "separation" is just "two integer vectors
have different sums". That file removed the evidence for (B); Habiro removes the
possibility of (B).

**Consequence:** the hypercharge candidacy in `conj:sm-hypercharge-invariant`
rests on a property the ribbon structure provably does not have. Either the block
stops calling the datum a ribbon framing, or the candidacy goes.

## Second, separable use — gzs0's Q2 becomes computable

`qou-gzs0` found `F_Bor = |tr_M(beta_Bor)| . [3]_q! / q^3` has `q^-3 = q^{T/2}`
at T = -6 EXACTLY, of framing shape, on a word of writhe 0 — and concluded the
corpus must **declare** which framing the mass path uses, since
`FramingIsAChoice.lean` proves T=0 is a convention and not derivable.

With omega that stops being a ruling and becomes a probe: is the `/q^3` equal to
`<omega^-1, .>` on the Borromean skein element? `t(e_n) = (-1)^n A^{n(n+2)}` gives
a definite prediction once the A <-> q dictionary is fixed. A match would DERIVE
the mass path's framing; a mismatch would show the `/q^3` is not a framing at all
and gzs0's Q2 identification is a coincidence of shape.

NOT claimed here: that it matches. This is a computation nobody has run.

## Scope

Scope (a) on the gzs0 probe — untested. On the 7dzg half the exclusion rests on a
cited structural fact (twist acts by a colour-determined scalar on simples), not
on a failed search, so it is closer to scope (b); but it is a citation, and the
corpus should carry its own statement before treating it as proved here.
