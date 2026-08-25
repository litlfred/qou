---
# qou-dodK
title: 'The sqrt5 slot: do the Aitchison-Rubinstein dodecahedral knots carry a closed-form c_sigma?'
status: scrapped
type: task
priority: normal
tags:
    - one-loop
    - c-sigma
    - adjoint-torsion
    - volume-conjecture
    - brings-surface
    - trace-field
created_at: 2026-08-08T19:20:00Z
updated_at: 2026-08-08T19:20:00Z
---

## The ask

`qou-vdvK` established that closed forms for `c_sigma` exist exactly where the
Laplace saddle sits at a ROOT-OF-UNITY shape, i.e. at a regular ideal polyhedron:

    tetrahedral   z = exp(i pi/3)   Q(zeta_3) = Q(sqrt-3)   |tau| = sqrt3/2      4_1
    octahedral    z = i             Q(zeta_4) = Q(i)        |tau| = 2^{2n-2}|A|  W_{a,1,c,d}

with `A = n - m i` a Gaussian integer. Those are the two imaginary quadratic
fields with extra units — the two Bianchi cases.

The obvious next member is the regular ideal DODECAHEDRON, and there are
manifolds built from it: the two **Aitchison-Rubinstein dodecahedral knots**,
each the union of two regular ideal dodecahedra
(`Vol = 2 x 20.5801932... = 41.1603865...`).

Does `|tau_DG|` for those knots have a closed form, and does it carry `sqrt5`?

## Why this is worth an experiment rather than a derivation

**It probably fails, and the failure is the information.** `Q(zeta_5)` is degree
4 and NOT imaginary quadratic, so there is no Bianchi group and no reason for
`det(Hessian)` to be a radical. The tetrahedral and octahedral cases closed
because their trace fields are the two exceptional imaginary quadratics; a
5-fold case has no such excuse. If `|tau_DG|` comes out as a root of an
irreducible quartic with no radical form, that CONFIRMS the arithmetic
obstruction stated in `qou-vdvK` — which is currently an assertion, not a
demonstration.

If it DOES carry `sqrt5`, that is a third family and a much bigger deal.

## Connection to the Bring material (why the corpus cares)

The `brings-surface` chapter carries a `sqrt5` from the `Z_5` Gauss sum
`sum_k zeta_5^{k^2} = sqrt5` (`bring-trefoil-cinquefoil-channel`), and a
`q`-deformation via `SU_q(1,1)` / Jackson `q`-Bessel
(`brings-q-hyperbolic-geometry`). If a `zeta_5` shape ever produces a `c_sigma`
of the form `5^{-1/4} x (...)`, that is the slot it would occupy, parallel to
`3^{-1/4}` (tetrahedral) and `2^{-3/4}` (octahedral).

**State this carefully and do not assume it.** The Bring knots the corpus names
are the TORUS knots `T_{2,3}` and `T_{2,5}`, which are NOT hyperbolic — their
simplicial volume is zero, the colored Jones grows polynomially, and the whole
`c_sigma` machinery is vacuous there. So the Bring `sqrt5` and a hypothetical
dodecahedral `sqrt5` are related by ANALOGY of the cyclotomic field only, until
something connects them. Do not write them into the paper as one thing.

## How to do it

SnapPy has no `DodecahedralKnots` census. Either construct the two knots from
their standard descriptions, or search `HTLinkExteriors` / the cusped census for
one-cusped manifolds of volume `41.1603865...`, then run
`computations/one_loop_torsion.py`. Compare `|tau_DG|` against `sqrt5`-bearing
candidates AND against being a non-radical algebraic number (compute its minimal
polynomial numerically with PARI/LLL).

## Definition of done

`|tau_DG|` for at least one dodecahedral knot, with its minimal polynomial
identified, and a written verdict on whether the two-closed-form-families claim
in `qou-vdvK` survives.

## Scrapped — the question was right, the target was wrong

This bean asked where a `sqrt5` could enter by the same route as `sqrt3`
(tetrahedral) and `sqrt2` (octahedral), and guessed the regular ideal
DODECAHEDRON / Aitchison-Rubinstein knots, on the reasoning that the pattern is
"regular ideal polyhedra".

That reading was too narrow. The pattern is not polyhedra, it is **norms from
cyclotomic rings**:

    octahedral   norm from Z[i]       sqrt(n^2+m^2)   |A| for A = n - m i
    tetrahedral  norm from Z[zeta_3]  sqrt3

and a norm from `Z[zeta_5]` does not need a 5-fold polyhedron. It arises from a
**cyclic branched cover**, via the classical

    |H_1(Sigma_d(K))| = prod_{j=1}^{d-1} |Delta_K(zeta_d^j)|
                      = |Res(Delta_K, (t^d - 1)/(t - 1))|

which is exactly a norm from `Z[zeta_d]`. Computed for the two torus knots the
`brings-surface` chapter actually names:

    T_{2,3} trefoil    d=5:  |H_1| = 1   -> the POINCARE HOMOLOGY SPHERE Sigma(2,3,5)
    T_{2,5} cinquefoil d=2:  |H_1| = 5   -> the lens space L(5,q)

and the WRT invariant of `L(5,q)` is a Gauss sum, with
`sum_k zeta_5^{k^2} = sqrt5` — the corpus's Bring constant, verified.

The corpus already had half of this: `klein-bring-icosahedral-bridge` states
`P(V)/A_5 = S^2(2,3,5)`, the base of the Seifert fibration `S^3/2I ->
S^2(2,3,5)` of the Poincare sphere. What was missing is that the trefoil the
same chapter calls the electron IS the branch locus: `Sigma_5(3_1) = S^3/2I`.
And `|2I| = 120 = |S_5| = |Aut(Bring)|`.

Superseded by `qou-lz235`. The dodecahedral knots remain a fine curiosity but
are not the `sqrt5` slot and are much harder to get hold of (no SnapPy census).
