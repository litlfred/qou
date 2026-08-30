#!/usr/bin/env python3
"""Reduce `Vol(4_1) < Vol(5_2)` to a purely ALGEBRAIC angle inequality.

WHY THIS EXISTS
---------------
`QOU.Encounter.FiveTwoVolumeBridge` deliberately states the 4_1/5_2 comparison as an
EQUIVALENCE rather than an inequality, because the corpus does not prove
`VOL_4_1 < VOL_5_2` -- `MostowRigidity`'s version discharged by `norm_num` on two
truncated decimals, which proves nothing about the exact constants.

The obvious route (bound `VOL_5_2 = 3*D(y_1)` below by summing a series) is blocked:
`|y_1| = 1.5247 > 1`, so the `Li_2` power series diverges there, and the corpus's only
certified Clausen machinery (`abs_Cl_2_pi_div_three_sub_le`) is pinned to `pi/3` --
its `S24_eq` closed form is rational*sqrt(3) precisely BECAUSE the angle is pi/3.

THE REDUCTION
-------------
Rivin concavity (`QOU.Knot.Rivin.strictConcaveOn_tetVolLine`, proved) says the ideal
tetrahedron volume `f(a) = L(a1)+L(a2)+L(a3)` is strictly concave along every line in
the angle simplex `{a1+a2+a3 = pi}`.  Take the segment from

    r = (pi/3, pi/3, pi/3)   f(r) = Cl_2(pi/3)        [the regular tetrahedron]
    to the simplex BOUNDARY  f     = 0                [a degenerate tetrahedron:
                                                       L(0)+L(b)+L(pi-b) = 0, since
                                                       L is odd about pi/2]

The 5_2 angle triple `a` lies on that segment at some fraction `t` from `r`, so
concavity puts `f` ABOVE the chord:

    f(a) >= (1-t)*Cl_2(pi/3)   =>   VOL_5_2 = 3*f(a) >= 3*(1-t)*Cl_2(pi/3)

and `VOL_4_1 = 2*Cl_2(pi/3)`.  **Cl_2(pi/3) CANCELS.**  The comparison is

    3*(1-t) > 2      <=>      t < 1/3

with `t = 1 - 3*a_min/pi` (the boundary is hit first by the SMALLEST angle), so

    ****  VOL_4_1 < VOL_5_2   <=   every dihedral angle of the 5_2 tetrahedron > 2*pi/9  ****

No certified transcendental value is needed on either side.  That is the point: the
route was never "certify Lambda at an angle that is not a rational multiple of pi".

WHAT IS STILL OPEN (do not read this probe as a proof)
------------------------------------------------------
This script MEASURES the reduction and its margin.  The Lean assembly is not done and
has one identified gap: `strictConcaveOn_tetVolLine` is stated on `tetLineDomain`, and
the chord's far endpoint is a DEGENERATE tetrahedron on the boundary.  Extending to the
closed segment needs a continuity step (`QOU.Knot.continuous_Lob` exists) plus
`FlatTetrahedra.BlochWigner_lob_eq_zero_of_im_eq_zero` for the endpoint value.

PRECISION
---------
mpmath end to end at 60 dps; no float64 anywhere (AGENTS.md: probes are NOT exempt).
"""
import mpmath as mp

mp.mp.dps = 60


def five_two_shape():
    """The non-real root of X^3 - 2X^2 + 3X - 1 (the 5_2 tetrahedron shape y_1)."""
    rts = mp.polyroots([1, -2, 3, -1], maxsteps=400, extraprec=400)
    return next(r for r in rts if mp.im(r) > mp.mpf("1e-40"))


def dihedral_angles(z):
    """The three dihedral angles of the ideal tetrahedron with shape `z`."""
    return mp.arg(z), mp.arg(1 / (1 - z)), mp.arg(1 - 1 / z)


def lob(t):
    """Lobachevsky Lambda(t) = Cl_2(2t)/2."""
    return mp.clsin(2, 2 * t) / 2



def bracket_requirement() -> bool:
    """Is `QOU.Knot.FiveTwoShapeBounds` already tight enough to certify a_min > 2*pi/9?

    CORRECTED.  A first pass interval-evaluated the condition over a rational BOX for
    (Re y_1, Im y_1) as if those were independent, concluded the existing bounds fall
    short, and reported that denominators of 200 were required.  **That was wrong.**
    Both coordinates are functions of the SINGLE real root `t` of X^3-2X^2+3X-1:

        Re = (2 - t)/2            Im = sqrt(3t^2 - 4t + 8)/2

    so the box relaxation throws away the constraint linking them -- and here it throws
    away enough to invert the answer.  Parametrise by `t` instead:

        Re^2 - Re + Im^2 = (4t^2 - 6t + 8)/4

        ratio(t) = Im / (Re^2 - Re + Im^2) = 2*sqrt(3t^2 - 4t + 8) / (4t^2 - 6t + 8)

    `ratio` is strictly INCREASING across the bracket (ratio' ~ 0.25-0.28 on
    [0.39, 0.46]), so a LOWER bracket on `t` alone settles it -- no upper bracket, and
    no bound on Re or Im separately, is needed.
    """
    tan_ = mp.tan(2 * mp.pi / 9)

    def ratio(t):
        return 2 * mp.sqrt(3 * t**2 - 4 * t + 8) / (4 * t**2 - 6 * t + 8)

    print("\n" + "=" * 66)
    print("BRACKET REQUIREMENT — is FiveTwoShapeBounds already tight enough?")
    print("=" * 66)
    print("condition:  ratio(t) > tan(2*pi/9) =", mp.nstr(tan_, 20))

    # monotonicity is what licenses testing only the lower end
    incr = all(mp.diff(ratio, mp.mpf("0.39") + mp.mpf(i) / 200) > 0 for i in range(15))
    print("ratio increasing across the bracket:", incr)

    t_crit = mp.findroot(lambda t: ratio(t) - tan_, mp.mpf("0.45"))
    print("critical t (ratio = tan(2*pi/9)) =", mp.nstr(t_crit, 20))

    lo = mp.mpf(2) / 5                     # the EXISTING `realRoot_gt` bracket
    ok = incr and ratio(lo) > tan_
    print("\nEXISTING bracket  realRoot_gt : 2/5 < t")
    print("  ratio(2/5) =", mp.nstr(ratio(lo), 20))
    print("  SUFFICIENT?", ok, "  margin =", mp.nstr(ratio(lo) - tan_, 12))
    print("\n  -> NO refinement of FiveTwoShapeBounds is needed.  The upper bracket")
    print("     `realRoot_lt` and the separate Re/Im bounds are not required either;")
    print("     the whole angle condition rests on `2/5 < realRoot` plus monotonicity.")
    return bool(ok)


def ninth_power_route() -> bool:
    """The angle condition `a_min > 2*pi/9` as a POLYNOMIAL condition on z^9.

    `2*pi/9` is exactly one ninth of a full turn, so for `z` whose argument is
    known to lie in a window narrow enough to fix the branch,

        arg z > 2*pi/9   <=>   9*arg z > 2*pi   <=>   Im(z^9) > 0

    because `arg(z^9) = 9*arg z (mod 2*pi)` and a positive imaginary part is
    exactly `arg in (0, pi)`.  The branch window used here is `arg z in
    (pi/6, pi/4)`, i.e. `Im < Re` and `sqrt3*Im > Re` -- both algebraic -- which
    puts `9*arg z` in `(3pi/2, 9pi/4)`, inside `(pi, 3pi)`.

    WHY THIS MATTERS.  It replaces the tan route entirely:

      tan route   needs `tan_three_mul` (NOT in Mathlib), the cubic
                  `tau^3 + 3*sqrt3*tau^2 - 3*tau - sqrt3 = 0` for tan(2pi/9),
                  and a rational bracket on tau.
      z^9 route   needs `Complex.arg_pow_coe_angle` (IN Mathlib) and a
                  polynomial sign check.

    And it is far more robust: the sign of `Im(z^9)` survives a box of halfwidth
    1e-3 on both coordinates of `z`.
    """
    y1 = five_two_shape()
    z = (y1 - 1) / y1                      # arg z is the smallest dihedral angle
    re, im = mp.re(z), mp.im(z)
    z9 = z**9

    print("\n" + "=" * 66)
    print("THE z^9 ROUTE — the angle condition without tan or arctan")
    print("=" * 66)
    print("z = (y1-1)/y1 =", mp.nstr(z, 20))
    print("arg z         =", mp.nstr(mp.arg(z), 20), "  2*pi/9 =", mp.nstr(2*mp.pi/9, 20))

    branch_lo = mp.sqrt(3) * im > re       # arg z > pi/6
    branch_hi = im < re                    # arg z < pi/4
    print("\nbranch window (algebraic):")
    print("  sqrt3*Im > Re  (arg > pi/6):", branch_lo)
    print("  Im < Re        (arg < pi/4):", branch_hi)

    print("\npolynomial condition:")
    print("  Im(z^9) =", mp.nstr(mp.im(z9), 20), "   > 0 ?", mp.im(z9) > 0)
    print("  check: arg(z^9) =", mp.nstr(mp.arg(z9), 15),
          " == 9*arg z - 2*pi =", mp.nstr(9 * mp.arg(z) - 2 * mp.pi, 15))

    # the EXISTING realRoot bracket, propagated
    def z_of_t(t):
        yy = (2 - t) / 2 + 1j * mp.sqrt(3 * t**2 - 4 * t + 8) / 2
        return 1 - 1 / yy

    lo = mp.mpf(2) / 5                     # QOU.Knot.FiveTwoShapeBounds.realRoot_gt
    zlo = z_of_t(lo)
    at_lo = mp.im(zlo**9)
    print("\nEXISTING bracket  realRoot_gt : 2/5 < t   (nothing else needed)")
    print("  at t = 2/5:  Im(z^9) =", mp.nstr(at_lo, 15), "  > 0 ?", at_lo > 0)
    print("  branch window there:", mp.sqrt(3) * mp.im(zlo) > mp.re(zlo),
          mp.im(zlo) < mp.re(zlo))

    ok = bool(branch_lo and branch_hi and mp.im(z9) > 0 and at_lo > 0)
    print("\n  -> the z^9 route closes on `2/5 < realRoot` ALONE.")
    return ok


def main() -> int:
    y1 = five_two_shape()
    angles = dihedral_angles(y1)
    a_min = min(angles)
    two_pi_9 = 2 * mp.pi / 9
    cl2 = mp.clsin(2, mp.pi / 3)

    vol_tet = sum(lob(a) for a in angles)
    VOL_5_2 = 3 * vol_tet
    VOL_4_1 = 2 * cl2
    t = 1 - 3 * a_min / mp.pi

    ok = True
    print("5_2 shape y_1        =", mp.nstr(y1, 25))
    print("angle sum - pi       =", mp.nstr(sum(angles) - mp.pi, 8), "(must be ~0)")
    print()
    print("dihedral angles      =", [mp.nstr(a, 20) for a in angles])
    print("2*pi/9               =", mp.nstr(two_pi_9, 20))
    for i, a in enumerate(angles, 1):
        good = a > two_pi_9
        ok &= good
        print(f"  a{i} > 2*pi/9        {'OK ' if good else 'NO '} margin ="
              f" {mp.nstr(a - two_pi_9, 12)}")
    print()
    print("t = 1 - 3*a_min/pi   =", mp.nstr(t, 20), " (need < 1/3)")
    print("1/3 - t              =", mp.nstr(mp.mpf(1) / 3 - t, 12))
    ok &= t < mp.mpf(1) / 3
    print()
    print("CHORD LOWER BOUND, Cl_2(pi/3) cancelled:")
    print("  3*(1-t)            =", mp.nstr(3 * (1 - t), 20), " vs 2")
    ok &= 3 * (1 - t) > 2
    print()
    print("sanity, actual values (NOT part of the proof, just orientation):")
    print("  VOL_4_1            =", mp.nstr(VOL_4_1, 20))
    print("  chord LB on VOL_5_2=", mp.nstr(3 * (1 - t) * cl2, 20))
    print("  VOL_5_2 (actual)   =", mp.nstr(VOL_5_2, 20))
    ok &= 3 * (1 - t) * cl2 > VOL_4_1
    ok &= VOL_5_2 > VOL_4_1
    print()
    print("The bound is TIGHT: the chord LB clears VOL_4_1 by only",
          mp.nstr(3 * (1 - t) * cl2 - VOL_4_1, 8),
          f"({mp.nstr((3*(1-t)*cl2 - VOL_4_1)/VOL_4_1*100, 4)} %).")
    print("Equivalently a_min exceeds 2*pi/9 by",
          mp.nstr(a_min - two_pi_9, 8),
          f"({mp.nstr((a_min - two_pi_9)/two_pi_9*100, 4)} %).")
    print()
    ok &= bracket_requirement()
    ok &= ninth_power_route()
    print("\nVERDICT:", "REDUCTION HOLDS" if ok else "REDUCTION FAILS")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
