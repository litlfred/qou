---
# qou-vdvP
title: 'The phase of van der Veen E is unchecked — everything in qou-vdvS is moduli'
status: todo
type: task
priority: normal
tags:
    - one-loop
    - van-der-veen
    - chern-simons
    - c-sigma
created_at: 2026-08-08T18:40:00Z
updated_at: 2026-08-08T18:40:00Z
---

## The ask

`qou-vdvS` derived `Q_inf = psi * 2^{-n/2} * sqrt(2/A)` and verified it in
**absolute value only**, on 20 chains. The phase was never tested and should not
be cited.

Two concrete reasons to distrust it as it stands:

  * `psi` appears as `exp(+(4a+3c-3d) pi i/4)` in van der Veen's Lemma 5 and as
    `exp(-(4a+3c-3d) pi i/4)` in the retracted version of this corpus's probe.
    Nobody has checked which. Nothing in the modulus-only verification would
    notice.
  * The same paper's `CS` is quoted two ways — `-(4a+c-d)/8 * 2pi^2` when
    `c+d = 1` and `-(4a-7c+7d)/8 * 2pi^2` otherwise — which agree mod 8 but are
    written as if they were the same object. Given that a sign in `A` was
    already found wrong by exactly this `+(c-d)` vs `-(c-d)` confusion, the
    phase bookkeeping in this paper has a demonstrated failure mode.

## How to do it

`Q_N` is already computed from Lemma 1 in the probe and its phase is thrown
away by `abs()`. Keep it, and compare `arg(Q_N)` against
`arg(psi) - (1/2) arg(A)` for both sign conventions of `psi`. The `n = c+d = 2`
chains with `4a-c+d = 0` (Borromean) make `A` real and isolate `psi` cleanly.

## Why it matters, and why it is not urgent

`c_sigma` is a modulus, so nothing the corpus currently asserts depends on the
phase. But `Im E` is the Chern-Simons invariant, and the corpus does carry
CS-valued claims elsewhere; if the phase is ever wired in, this must be settled
first rather than assumed from a formula whose sibling was wrong.

## Definition of done

`arg(Q_inf)` verified against `Q_N` on at least four chains spanning both
`A` real and `A` complex, with the `psi` sign convention stated explicitly.
