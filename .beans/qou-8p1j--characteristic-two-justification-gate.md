---
# qou-8p1j
title: 'qou-8p1x/j: is there a STRUCTURAL reason the colour sector is characteristic 2?'
status: todo
type: task
created_at: 2026-08-07T12:40:00Z
updated_at: 2026-08-07T12:40:00Z
---

Parent: `qou-8p1x`. **The load-bearing unknown for `qou-8p1h`.**

The Bruhat route reaches `PSL(2,7) = GL(3,F_2)` and the Fano plane by
specialising the framework's own `H_n(q)` at `n = 3, q = 2`. Everything about
that route lives or dies on one question:

> **Is there a structural reason the colour sector is the characteristic-2
> specialisation — or is `q = 2` chosen because it yields `168`?**

If the latter, this is numerology and the anti-fit discipline catches it.

## The candidate worth testing, and why it is only a candidate

The framework already carries a **mod-2 / parity structure**: the
bar-involution `q -> q^{-1}`, the bar-even / bar-odd decomposition used
throughout the `Q_beta` and `c_k` work, the Type B folding of `AGENTS.md` §7b
(whose fixed points are the bar-invariant normal forms), and `EkParitySplit`.
`F_2` is the residue field of that parity.

**That is a suggestive coincidence, not a derivation.** The bar-involution is
an involution on a deformation parameter; `F_2` is a field of characteristic 2.
Asserting they are the same structure because both are "mod 2" is exactly the
move the corpus-grep and anti-laundering rules exist to catch. Do not write it
down as a link until there is a map.

## What would count as an answer

Something with the shape: a functor / specialisation from the framework's
`q`-generic categorical layer to `F_2`-linear data, under which the bar
involution becomes the Frobenius (or the residue map), **derived from the
substrate rather than posited**. Absent that, record the route as
attractive-but-unjustified.

## What would count as a refutation

Equally valuable: show the parity structure is *not* a characteristic-2
specialisation — e.g. that the bar-involution's fixed locus does not reduce
mod 2 compatibly, or that the framework's `q` cannot specialise to a prime
power without breaking a proved property. That would close `qou-8p1h`
cleanly and leave `qou-8p1i` as the only live route.
