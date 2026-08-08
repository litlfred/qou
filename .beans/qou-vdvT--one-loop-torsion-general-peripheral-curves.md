---
# qou-vdvT
title: 'Extend one_loop_torsion.py to general peripheral curves, and test the a-twisted Whitehead chains'
status: todo
type: task
priority: high
tags:
    - one-loop
    - adjoint-torsion
    - van-der-veen
    - c-sigma
    - snappy
created_at: 2026-08-08T18:40:00Z
updated_at: 2026-08-08T19:55:00Z
---

## The ask

`one_loop(M, curves=...)` in `computations/one_loop_torsion.py` currently picks,
per cusp, either the meridian (`0`) or the longitude (`1`). Extend it to a
general integral combination `p*mu + q*lambda`.

## Why this is the sharpest available test of the closed form

`qou-vdvS` derived, for the b=1 Whitehead chains,

    |tau_DG|(W_{a,1,c,d}) = 2^{2n-2} sqrt(n^2 + m^2),   n = c+d,  m = 4a-c+d

Note that `Vol(W_{a,b,c,d}) = 8(c+d)Lambda(pi/4)` is **independent of `a`**. By
Thurston-Jorgensen only finitely many manifolds share a volume, so the chains
`W_{a,1,c,d}` for `a` in Z cannot be infinitely many distinct manifolds: they
are the SAME manifold with a different peripheral framing. In van der Veen's
Lemma 1 this is visible directly — `a` enters only through the phase
`chi^{4a-c+d}`, never through `S_{n,k}`.

So the `a`-dependence of the formula above is a prediction about the
**change-of-curve law** for the DG invariant, testable at zero cost against
manifolds the corpus already has, with no new colored-Jones computation. The
`a = 0` cases are already confirmed to 18 digits (L5a1, L6a4, L8n5, L10n100,
L10n103). The `a != 0` cases are untested and would be the first check of the
formula's phase-driven half.

Worked example to aim at: `W_{1,1,1,0}` has `n = 1, m = 3`, so `|tau| = sqrt10
= 3.16227766...`, against `sqrt2` for `W_{0,1,1,0} = L5a1` — the same manifold,
a different framing.

## The trap

The corpus has already confirmed the module's change-of-curve law against
SnapPy's cusp shapes for the meridian/longitude swap (`cusp_shape_residuals`).
Extending to `p*mu + q*lambda` must keep that self-test passing, and must not
quietly re-normalise: `one_loop`'s docstring says the overall normalization at
`c >= 2` is inherited from `c = 1`, so read ratios.

## Definition of done

General `(p,q)` curves supported, the existing `self_test()` still green, and
`|tau_DG|` computed for at least two `a != 0` chains and compared against
`2^{2n-2} sqrt(n^2+m^2)`. A negative result is worth as much as a positive one
and must be reported as loudly.

## The cheap route is closed — checked 2026-08-08

Hoped: since `Vol(W_{a,1,c,d})` is independent of `a`, the twisted chains must be
2-cusped manifolds of octahedral volume, so maybe they can be FOUND rather than
built, and `|tau_DG|` read off with the existing meridian-only code.

They cannot. Scanning `OrientableCuspedCensus(cusps=2)` for volume
3.663862376708876 returns exactly two manifolds:

    m129 (= L5a1, the Whitehead link)   |tau| = sqrt2   = W_{0,1,1,0}
    m125 (the Whitehead sister)          |tau| = sqrt8

The prediction for `W_{a,1,1,0}` is `|tau| = sqrt(1 + (4a-1)^2)`: sqrt2, sqrt10,
sqrt26, sqrt50, ... Neither census manifold carries sqrt10, and `sqrt8` needs
`m^2 = 7`, not a square, so `m125` is not `W_{a,1,c,d}` for any integer `a`
either (it is a census manifold, not necessarily a link in S^3).

**This does not refute the prediction — it confirms the framing reading.** The
`a`-twisted chains are the SAME complement with a different peripheral framing,
exactly as the volume-independence argument said, so `one_loop(M)` on the
default meridians can only ever return the `a = 0` value. There is no
alternative manifold carrying the `a != 0` values, so if the law holds at
`a != 0` it MUST hold through the change-of-curve law.

So general `(p,q)` peripheral curves are not a convenience here, they are the
only access. This bean stands, better motivated.
