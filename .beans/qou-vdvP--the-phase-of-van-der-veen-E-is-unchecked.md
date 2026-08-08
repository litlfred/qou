---
# qou-vdvP
title: 'The phase of van der Veen E is unchecked — everything in qou-vdvS is moduli'
status: completed
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

## Resolution — done, same day it was opened

`psi = exp(+i pi (4a+3c-3d)/4)` — the sign in van der Veen's **Lemma 5**, not
the one the retracted probe used. So

    Q_inf = exp(+i pi (4a+3c-3d)/4) * 2^{-n/2} * sqrt(2/A)
    Im E  = pi * arctan(m/n) + pi^2 (4a+3c-3d)/2

**Method.** Measure the COMPLEX `Q_N` at `N = 0 mod 16`. There van der Veen's
CS factor `e^{(4a+7c-7d) N pi i/8}` is exactly 1, so the measurement imports no
convention at all — which matters, because the CS convention turned out to be
one of the things that is wrong. Across 12 chains the error against `psi = +`
is 4e-7 to 1.1e-6 and falls as O(1/N); against `psi = -` it is 0.34 to 1.19 on
the 9 chains where the two differ (`psi` and its conjugate coincide exactly when
`4a+3c-3d = 0 mod 4` — the guess in the original ask, that the `A`-real
Borromean chains would isolate `psi`, was backwards: those are precisely the
degenerate ones).

**Independent corroboration, from van der Veen himself.** His `b >= 2` constant
in the main theorem is `E = 2 pi (c+d) log 2 + (4a+3c-3d)/4 * 2 pi^2 i`, whose
imaginary part agrees exactly. That is the same line whose REAL part is
sign-wrong (slip 3) — right about the phase, wrong about the logarithm, which is
a coherent single-typo story rather than two independent errors.

**And the ask's second suspicion was right.** It flagged that `CS` is quoted two
ways (`4a+c-d` at `c+d=1`, `4a-7c+7d` otherwise) "as if they were the same
object", and predicted the phase bookkeeping had a demonstrated failure mode.
Measuring the N-linear phase gives `4a-c+d` and `4a+7c-7d` — **the same `(c-d)`
sign flip as slip 2, in both branches.** Indeed `4a+c-d` IS the expression Step 3
reuses for `A`, so slips 2 and this one have one root cause, not two. The branch
difference is only `phi_N`, defined differently in the two cases, contributing a
linear phase `-8(c-d)` in the second. His Lemma-4 proof uses the correct
`(4a+7c-7d)`, which is why `Q_inf` is well defined despite the main theorem.

**Nothing in the corpus moves.** `c_sigma` depends on `|Q_inf|` only. This
completes `E` rather than correcting anything.

Probe section (vi); audit "The phase, resolved".
