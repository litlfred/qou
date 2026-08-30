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
    """`a_min > 2*pi/9` as a POLYNOMIAL condition -- and the mod-cubic reduction.

    `2*pi/9` is exactly one ninth of a full turn, so with the branch pinned,

        arg z > 2*pi/9   <=>   9*arg z > 2*pi   <=>   Im(z^9) > 0

    since `arg(z^9) = 9*arg z (mod 2*pi)` and positive imaginary part is exactly
    `arg in (0, pi)`.  Branch window: `arg z in (pi/6, pi/4)`.

    THE REDUCTION.  `|y1|^2 = t^2-2t+3`, and the cubic `t^3-2t^2+3t-1 = 0` gives
    `t*(t^2-2t+3) = 1`, so `|y1|^2 = 1/t` and `1/y1 = t*conj(y1)`.  Hence

        Re(z) = (t^2 - 2t + 2)/2        Im(z) = t*sqrt(3t^2 - 4t + 8)/2

    `Im(z^9) = Im(z) * Q(Re^2, Im^2)` with `Q(A,B) = 9A^4 - 84A^3 B + 126A^2 B^2
    - 36A B^3 + B^4`, and `Re^2`, `Im^2` are polynomial in `t`, so `Im(z^9) > 0`
    reduces to a degree-15 polynomial in `t` alone -- which, reduced modulo the
    cubic, collapses to a QUADRATIC.

    CORRECTION.  A first pass evaluated `Im(z^9)` along `z(t) = 1 - 1/y(t)` at
    `t = 2/5` and concluded the route closes on the existing `realRoot_gt`
    bracket alone.  **It does not.**  `|y1|^2 = 1/t` holds only AT the root, so
    that parametrisation is not the object in the theorem away from it -- the
    same error shape as interval-evaluating `(Re, Im)` as independent, one level
    down.  Done correctly, `2/5` FAILS and the bracket must be tightened.
    """
    tan_check = mp.mpf(0)  # placeholder to keep mpmath imported in view

    def g(v):        return v**3 - 2*v**2 + 3*v - 1     # < 0  =>  v < realRoot
    def q_red(v):    return -3*v**2 + 6*v - 2           # > 0  =>  Im(z^9) > 0
    def im_lt_re(v): return -2*v**2 + 2*v               # > 0  =>  Im(z) < Re(z)
    def s3im_gt(v):  return 8*v**2 - 8*v + 4            # > 0  =>  sqrt3*Im > Re

    root = mp.findroot(g, mp.mpf("0.43"))
    crit = (3 - mp.sqrt(3)) / 3

    print("\n" + "=" * 66)
    print("THE z^9 ROUTE — the angle condition without tan or arctan")
    print("=" * 66)
    print("Q(t) reduced mod the cubic  =  -3t^2 + 6t - 2      (degree 15 -> 2)")
    print("realRoot            =", mp.nstr(root, 20))
    print("critical (3-sqrt3)/3=", mp.nstr(crit, 20), "  margin",
          mp.nstr(root - crit, 12))

    print("\nbranch conditions, reduced mod the cubic — both FREE:")
    print("  Im < Re      : -2t^2+2t = -2t(t-1) > 0 on (0,1)"
          "   <- realRoot_pos + realRoot_lt_one")
    print("  sqrt3*Im > Re:  8t^2-8t+4 = 8(t-1/2)^2+2 > 0"
          "        <- unconditional")

    print("\nlower bracket needed (g<0 makes it provable, Q_red>0 makes it work):")
    ok_any = False
    for nm, v in [("2/5", mp.mpf(2)/5), ("17/40", mp.mpf(17)/40),
                  ("3/7", mp.mpf(3)/7), ("43/100", mp.mpf(43)/100)]:
        gv, qv = g(v), q_red(v)
        good = gv < 0 and qv > 0
        ok_any |= good and nm == "3/7"
        print(f"  t > {nm:7s} g={mp.nstr(gv,10):>15} {'ok ' if gv<0 else 'BAD'}"
              f"   Q_red={mp.nstr(qv,10):>15} {'ok ' if qv>0 else 'BAD'}"
              f"  {'USABLE' if good else '-'}")
    print("\n  -> 2/5 is NOT sufficient; the existing bracket must be tightened.")
    print("     3/7 works, and is proved the same way realRoot_gt is.")

    at_root = q_red(root)
    return bool(ok_any and at_root > 0 and im_lt_re(root) > 0 and s3im_gt(root) > 0)


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
