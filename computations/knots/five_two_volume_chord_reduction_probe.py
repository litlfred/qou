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
    """How tight must a RATIONAL bracket on y_1 be to certify a_min > 2*pi/9?

    a_min = arg(z) with z = 1 - 1/y, so

        Im(z)/Re(z) = Im(y) / (Re(y)^2 - Re(y) + Im(y)^2)

    and the condition is that this exceeds tan(2*pi/9).  Interval-evaluate the
    right-hand side over a rational box for (Re y, Im y): the denominator
    Re^2 - Re + Im^2 is increasing in Re on Re > 1/2 (which holds here) and in Im,
    so the worst case is smallest numerator over largest denominator.

    This decides whether `QOU.Knot.FiveTwoShapeBounds` (landed #6084) already
    suffices, or whether the Lean brackets must be refined first.
    """
    tan_ = mp.tan(2 * mp.pi / 9)

    def ratio_lo(re_lo, re_hi, im_lo, im_hi):
        d_hi = re_hi**2 - re_hi + im_hi**2      # largest denominator
        return im_lo / d_hi                      # smallest numerator

    print("\n" + "=" * 66)
    print("BRACKET REQUIREMENT — is FiveTwoShapeBounds already tight enough?")
    print("=" * 66)
    print("need Im(z)/Re(z) > tan(2*pi/9) =", mp.nstr(tan_, 20))

    # the bounds QOU.Knot.FiveTwoShapeBounds actually proves
    existing = (mp.mpf(31)/40, mp.mpf(4)/5, mp.mpf(13)/10, mp.mpf(33)/25)
    lo = ratio_lo(*existing)
    print("\nEXISTING (31/40 < Re < 4/5, 13/10 < Im < 33/25):")
    print("  worst-case ratio =", mp.nstr(lo, 15),
          "   SUFFICIENT" if lo > tan_ else
          "   NOT SUFFICIENT, short by " + mp.nstr(tan_ - lo, 10))

    y = five_two_shape()
    re_y, im_y = mp.re(y), mp.im(y)
    print("\nSmallest denominator that suffices:")
    need = None
    for den in (50, 100, 200, 400, 800):
        rl, rh = mp.floor(re_y*den)/den, mp.ceil(re_y*den)/den
        il, ih = mp.floor(im_y*den)/den, mp.ceil(im_y*den)/den
        lo = ratio_lo(rl, rh, il, ih)
        ok = lo > tan_
        print(f"  den={den:4d}  ratio_lo={mp.nstr(lo, 15)}  {'SUFFICIENT' if ok else '-'}")
        if ok and need is None:
            need = (den, int(rl*den), int(rh*den), int(il*den), int(ih*den))
    if need:
        d, a, b, c, e = need
        print(f"\n  -> refine FiveTwoShapeBounds to:  {a}/{d} < Re(y_1) < {b}/{d}")
        print(f"                                     {c}/{d} < Im(y_1) < {e}/{d}")
    return need is not None


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
    print("\nVERDICT:", "REDUCTION HOLDS" if ok else "REDUCTION FAILS")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
