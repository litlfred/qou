#!/usr/bin/env python3
"""The polar route and the signed-subdivision route are the SAME route, and
`psi < pi/2` is exactly the sign condition on the chord offset.

Bean `qou-w3eg` (H4-5, the obtuse case of Milnor's ideal-tetrahedron volume
identity `Vol = Lambda(alpha) + Lambda(beta) + Lambda(gamma)`).

WHY THIS PROBE EXISTS.  The bean lists the candidate routes to the obtuse case
as if they were independent: (2) "a polar form of the full triangle valid for
obtuse" and, separately, the signed-subdivision route it had forecloseed.  This
probe establishes that those two are one route, by deriving the corpus's own
`integral_orthoscheme` integrand from the corpus's own base integrand in polar
coordinates and then locating where it breaks.

WHAT IS CHECKED (three claims, all confirmed at 50 dps):

  1. RADIAL REDUCTION.  The corpus base integrand is
     `1 / (2 (R^2 - x^2 - y^2))` (`hypVolume_chimney_of_ae_lt`,
     `HyperbolicVolumeFubini.lean:275`).  Integrating it radially in polar
     coordinates out to the chord `chordHalfplane R theta psi`
     (`OrthoschemeTiling.lean:201`), whose boundary is at
     `r(phi) = R cos(psi) / cos(phi - theta)`, gives in closed form

         -(1/4) log((cos^2 phi - cos^2 psi) / cos^2 phi)      (theta = 0)

     which is EXACTLY the integrand of `integral_orthoscheme`
     (`OrthoschemeBaseIntegral.lean:260`).  So that theorem is not an
     independent construction: it is the polar radial reduction of the base
     integral, already done.

  2. THE ORTHOSCHEME INTEGRAL.  `int_0^psi` of that closed form equals
     `Lambda(psi)/2`, reproducing `integral_orthoscheme`'s statement.

  3. WHERE IT BREAKS, AND WHY.  The radial bound `r(phi)` is positive iff the
     chord offset `R cos(psi)` is positive, i.e. iff `psi < pi/2`.  At
     `psi = pi/2` the offset is zero (the chord passes through the
     circumcentre); past it the offset is NEGATIVE, meaning the circumcentre
     lies on the FAR side of that chord and the radial ray from the origin
     never reaches it in the positive direction.

CONSEQUENCE (the point of the probe).  `integral_orthoscheme`'s hypothesis
`hpsi : psi < pi/2` is not a technical convenience and not a wedge-disjointness
condition -- it is the statement that the circumcentre is on the inner side of
the chord.  That is the same geometric fact as "the circumcentre leaves the
triangle when an angle is obtuse", which is what forces one piece of Milnor's
subdivision to enter with a minus sign.  So Milnor's sign and the polar route's
`cos psi < 0` are one phenomenon in two vocabularies, and the polar route
cannot be pushed past `pi/2` without reintroducing exactly the sign the signed
route makes explicit.

This is a scope-(a) structural observation, not a refutation of anything: it
says the two routes coincide, so effort on one is effort on the other.  It
asserts NOTHING about the obtuse volume identity, which remains open.

NO-FLOAT64: every quantity is mpmath `mpf` end to end; `float()` appears
nowhere.  Probes are not exempt (AGENTS.md, owner directive 2026-08-18).

Anchor: NONE.  This probe is anchor-free -- it involves no `q0`, no CODATA
input, and no substrate quantity.  It is pure hyperbolic geometry.
"""

from mpmath import mp, mpf, cos, sin, log, quad, pi, clsin

mp.dps = 50

R = mpf(1)

# Tolerances: the closed-form/numeric comparison is limited by `quad`, the
# exact-identity comparison is not.
TOL_QUAD = mpf(10) ** (-40)
TOL_IDENT = mpf(10) ** (-30)


def base_integrand(x, y):
    """The corpus base integrand `1 / (2 (R^2 - x^2 - y^2))`."""
    return 1 / (2 * (R**2 - x**2 - y**2))


def radial_closed_form(psi, phi):
    """Closed form of `int_0^{r(phi)} r * base_integrand dr` with
    `r(phi) = R cos(psi)/cos(phi)`, i.e. the chord at direction `theta = 0`."""
    return -(mpf(1) / 4) * log((cos(phi) ** 2 - cos(psi) ** 2) / cos(phi) ** 2)


def radial_numeric(psi, phi):
    """The same radial integral evaluated numerically from the base integrand,
    in polar coordinates (Jacobian `r`)."""
    r_max = R * cos(psi) / cos(phi)
    return quad(
        lambda r: r * base_integrand(r * cos(phi), r * sin(phi)), [0, r_max]
    )


def lobachevsky(t):
    """`Lambda(t) = Cl_2(2t)/2` -- the corpus's `QOU.Archimedean.Lob`."""
    return clsin(2, 2 * t) / 2


def main() -> int:
    checks = []

    print("=== 1. radial reduction: closed form == numeric base integrand ===")
    for num, den in [(1, 6), (1, 4), (1, 3), (5, 12)]:
        psi = pi * num / den
        for frac in [mpf(1) / 5, mpf(1) / 2, mpf(4) / 5]:
            phi = psi * frac
            closed = radial_closed_form(psi, phi)
            numeric = radial_numeric(psi, phi)
            diff = abs(closed - numeric)
            ok = diff < TOL_QUAD
            checks.append(ok)
            print(
                f"  psi={num}pi/{den:<3} phi/psi={mp.nstr(frac, 3):<6} "
                f"closed={mp.nstr(closed, 20):<24} diff={mp.nstr(diff, 3):<10} "
                f"{'OK' if ok else 'FAIL'}"
            )

    print("\n=== 2. integral_orthoscheme: int_0^psi closed form == Lob(psi)/2 ===")
    for num, den in [(1, 6), (1, 4), (1, 3), (5, 12), (11, 24)]:
        psi = pi * num / den
        lhs = quad(lambda phi: radial_closed_form(psi, phi), [0, psi])
        rhs = lobachevsky(psi) / 2
        diff = abs(lhs - rhs)
        ok = diff < TOL_IDENT
        checks.append(ok)
        print(
            f"  psi={num}pi/{den:<3} int={mp.nstr(lhs, 25):<28} "
            f"Lob/2={mp.nstr(rhs, 25):<28} diff={mp.nstr(diff, 3):<10} "
            f"{'OK' if ok else 'FAIL'}"
        )

    print("\n=== 3. the psi = pi/2 boundary IS the chord-offset sign ===")
    for num, den in [(11, 24), (1, 2), (13, 24), (2, 3)]:
        psi = pi * num / den
        offset = R * cos(psi)
        phi = psi / 2
        r_max = offset / cos(phi)
        acute = psi < pi / 2
        # The claim: offset > 0 exactly when psi < pi/2, and then the radial
        # bound is positive; otherwise the circumcentre is on the far side.
        ok = (offset > 0) == acute and (r_max > 0) == acute
        checks.append(ok)
        side = "inner (offset>0)" if offset > 0 else "FAR side (offset<=0)"
        print(
            f"  psi={num}pi/{den:<3} R*cos(psi)={mp.nstr(offset, 12):>18} "
            f"r(psi/2)={mp.nstr(r_max, 12):>18}  circumcentre on {side}  "
            f"{'OK' if ok else 'FAIL'}"
        )

    passed = sum(1 for c in checks if c)
    total = len(checks)
    print(f"\n{passed}/{total} checks pass")
    if passed != total:
        print(
            "FAILED -- the polar/signed identification above is NOT established; "
            "do not cite it."
        )
        return 1
    print(
        "\nCONCLUSION: integral_orthoscheme is the polar radial reduction of the "
        "base integral, and its `psi < pi/2` hypothesis is exactly "
        "`chord offset R cos(psi) > 0`, i.e. the circumcentre lies inside. "
        "The polar route and the signed-subdivision route are the same route. "
        "Nothing is claimed here about the obtuse volume identity."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
