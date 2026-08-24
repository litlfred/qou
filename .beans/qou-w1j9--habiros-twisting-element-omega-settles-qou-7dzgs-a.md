---
# qou-w1j9
title: Habiro's twisting element omega settles qou-7dzg's (A)-vs-(B) — the ribbon twist is colour-determined, not a free label
status: todo
type: task
priority: normal
created_at: 2026-08-24T17:33:32Z
updated_at: 2026-08-24T18:46:59Z
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


## 2026-08-24 — the alpha rung is ANSWERED, and I had the twist wrong

Recording this in the bean because the next agent on this arc will hit the same
fork, and the commit message alone is not where they will look.

### Two twists, not one

    ribbon twist (modular T-matrix)   theta_lambda = q^{c(lambda)}
    full twist                        Delta^2 = theta^2 = q^{2c(lambda)}

The probe originally called `q^{c}` the FULL-twist eigenvalue. Wrong. That
mislabel is what made T3 look conditional.

### Why this nearly became a false "corpus inconsistency" report

`computations/chi-content-eigenbasis.witness.json` states the full twist acts as
`q^{2c(lambda)}` and calls it "the proved ribbon eigenvalue". Read against
`KeystoneModularTwist.lean`'s `theta = q^{contentSum}`, that looks like two live
values of alpha with one of them asserted "proved" — i.e. exactly the
two-live-spellings failure class this corpus keeps paying for.

**It is not a contradiction.** The witness describes `Delta^2`; the Lean
describes `theta`; `Delta^2 = theta^2`. Both correct. The only defect is the
witness's wording, which uses "ribbon eigenvalue" for the FULL twist — worth a
one-line fix if someone is in that file, not worth a PR on its own.

I was one step from filing this as an inconsistency. The discriminator was
reading the Lean file's header, which says plainly it is building the modular
T-matrix on a SIMPLE object.

### alpha = 1 rests on Lean, not on a citation

    QOU.BraidKnot.Keystone.theta (q : R) (l : List Nat) : R := q ^ (contentSum l)

sorry-free, generic `[GroupWithZero R]`, no ordering and no R (§7c-clean). So T3
is not "conditional on a convention cited from AGENTS.md" as this bean and the
PR body previously said. Correct that wherever it is repeated.

**Residual softness, not discharged:** that file's own docstring hedges the
exponent is the content sum *"(up to convention)"*. Nothing in the corpus
discharges the hedge. Discharging it means deriving the exponent from the
corpus's own Hecke convention `(sigma_i - q)(sigma_i + q^-1) = 0` — that is the
next rung, and it is real work, not bookkeeping.

### gzs0 was arithmetically right the whole time

`q^-3 = q^{T/2}` at `T = -6`: `T = 2c` IS the full-twist exponent and `q^{T/2}`
IS the ribbon twist. gzs0 had both numbers and their relation correct. Only its
"-2 per Borromean component" gloss is wrong (no per-component referent). Do not
"correct" gzs0's numbers — correct only that phrase.

### T5 — the bar-parity finding now has a mechanism

`Keystone.theta_conjugate` (sorry-free): `theta_{lambda'} = theta_lambda^-1`,
from the signed content flip `c(lambda') = -c(lambda)`. The S-matrix half of the
modular data is bar-EVEN (`qDim_conj`: `d_q(lambda') = d_q(lambda)`).

So the ribbon twist is the bar-ODD half of the modular data and the only half
that CAN break bar symmetry. T1's "the /q^3 is F_Bor's unique bar-breaker" is
therefore forced rather than incidental — and `(1^3)` being the transpose of
`(3)` gives `theta_{(1^3)} = theta_{(3)}^-1 = q^-3` directly, without needing the
content-sum arithmetic at all.
