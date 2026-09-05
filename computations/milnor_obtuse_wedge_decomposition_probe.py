#!/usr/bin/env python3
"""What the obtuse wedge decomposition must be — and why `wedgeAt` alone
cannot supply it.

Bean `qou-w3eg` (H4-5, obtuse case of `Vol = Lambda(a)+Lambda(b)+Lambda(c)`).

WHY THIS PROBE EXISTS.  The sibling probe
`milnor_polar_signed_equivalence_probe.py` established that the polar and
signed-subdivision routes coincide, leaving "one a.e. set identity of the
`milnorWedges_ae_eq_inscribedTriangle` kind" as the remaining geometric step.
Before building that in Lean, this probe fixes WHICH set identity, because the
obvious guess -- reuse `wedgeAt` at the obtuse half-angle -- is wrong.

THE CORPUS DEFINITIONS BEING TESTED (transcribed, not approximated):

  chordHalfplane R t p = { w : <w,u_t> < R cos p }            (OrthoschemeTiling:201)
  wedgeAt      R t p = { w : <w,u_t> < R cos p
                             and |<w,v_t>| < <w,u_t> * tan p }  (OrthoschemeRotation:153)
  inscribedTriangle R t a b c =
      chordHalfplane R (t+c) c
    & chordHalfplane R (t+2c+a) a
    & chordHalfplane R (t+2c+2a+b) b                          (OrthoschemeTiling:223)
  milnorWedges R t a b c =
      wedgeAt R (t+c) c | wedgeAt R (t+2c+a) a
    | wedgeAt R (t+2c+2a+b) b                                 (OrthoschemeLambdaSum:198)

with u_t = (cos t, sin t) and v_t = (-sin t, cos t).

CLAIM 1 (why the acute hypothesis is structural, not technical).  For an
obtuse half-angle `p > pi/2`, `tan p < 0`, so `|<w,v>| < <w,u> tan p` forces
`<w,u> < 0`, while `<w,u> < R cos p < 0` is then unbounded below.  So
`wedgeAt R t p` at obtuse `p` is an UNBOUNDED region opening AWAY from the
circumcentre -- not the isoceles triangle its docstring describes.  Substituting
an obtuse angle into `wedgeAt` therefore does not give "the wedge with a minus
sign"; it gives a different, infinite set.  Checked here by exhibiting points of
arbitrarily large norm inside it.

CLAIM 2 (the decomposition that does hold).  With `c > pi/2` the circumcentre
lies outside the triangle, across the `c`-chord.  The replacement for the
degenerate `c`-wedge is the wedge in the OPPOSITE direction with the ACUTE
half-angle `pi - c = a + b`, and it is SUBTRACTED:

    inscribedTriangle R t a b c
      =(a.e.)  ( wedgeAt R (t+2c+a) a  |  wedgeAt R (t+2c+2a+b) b )
                 \\  wedgeAt R (t+c+pi) (pi-c)

Every half-angle appearing on the right (`a`, `b`, `pi-c = a+b`) is ACUTE when
`c` is obtuse -- which is the same fact `lob_sum_eq_reflected` records on the
Lambda side (`IdealTetObtuseReduction.lean:82`).  So the existing acute wedge
machinery applies to all three pieces unchanged, and the minus sign lives in the
set algebra rather than in a new integral.

Claim 2 is tested by membership over a deterministic grid: every grid point is
classified by both sides and any disagreement is reported with its coordinates.
Boundary points (within `EDGE_TOL` of any defining line) are excluded, since the
identity is only claimed a.e.

NO-FLOAT64: all coordinates and trigonometry are mpmath `mpf`; `float()` appears
nowhere.  Probes are not exempt (AGENTS.md, owner directive 2026-08-18).

Anchor: NONE -- anchor-free hyperbolic/Euclidean geometry, no `q0`, no CODATA.

SCOPE.  This is a statement about SETS in the plane.  It asserts nothing about
the volume identity, and it is not a Lean proof -- it fixes the target for one.
"""

from mpmath import mp, mpf, cos, sin, tan, pi, sqrt

mp.dps = 40

R = mpf(1)
EDGE_TOL = mpf(10) ** (-12)


def _u(t):
    return (cos(t), sin(t))


def _v(t):
    return (-sin(t), cos(t))


def dot_u(w, t):
    return w[0] * cos(t) + w[1] * sin(t)


def dot_v(w, t):
    return -(w[0] * sin(t)) + w[1] * cos(t)


def in_chord_halfplane(w, t, p):
    """chordHalfplane R t p."""
    return dot_u(w, t) < R * cos(p)


def in_wedge_at(w, t, p):
    """wedgeAt R t p -- transcribed verbatim, INCLUDING the sign behaviour at
    obtuse `p`.  No acuteness is assumed."""
    s = dot_u(w, t)
    return s < R * cos(p) and abs(dot_v(w, t)) < s * tan(p)


def in_inscribed_triangle(w, t, a, b, c):
    return (
        in_chord_halfplane(w, t + c, c)
        and in_chord_halfplane(w, t + 2 * c + a, a)
        and in_chord_halfplane(w, t + 2 * c + 2 * a + b, b)
    )


def near_any_edge(w, t, a, b, c):
    """Is `w` within EDGE_TOL of any line used by either side of claim 2?"""
    lines = [
        (t + c, c),
        (t + 2 * c + a, a),
        (t + 2 * c + 2 * a + b, b),
        (t + c + pi, pi - c),
    ]
    for th, ps in lines:
        if abs(dot_u(w, th) - R * cos(ps)) < EDGE_TOL:
            return True
    # wedge side-lines: |<w,v>| = <w,u> tan p
    for th, ps in [(t + 2 * c + a, a), (t + 2 * c + 2 * a + b, b), (t + c + pi, pi - c)]:
        if abs(abs(dot_v(w, th)) - dot_u(w, th) * tan(ps)) < EDGE_TOL:
            return True
    return False


def rhs_decomposition(w, t, a, b, c):
    """(W_a | W_b) \\ W_{pi-c}, all half-angles acute when c is obtuse."""
    in_a = in_wedge_at(w, t + 2 * c + a, a)
    in_b = in_wedge_at(w, t + 2 * c + 2 * a + b, b)
    in_sub = in_wedge_at(w, t + c + pi, pi - c)
    return (in_a or in_b) and not in_sub


def check_claim1():
    """wedgeAt at an OBTUSE half-angle is unbounded (so it is not 'the wedge')."""
    print("=== CLAIM 1: wedgeAt at obtuse half-angle is UNBOUNDED ===")
    ok = True
    for num, den in [(7, 12), (2, 3), (3, 4)]:
        p = pi * num / den
        t = mpf(0)
        # walk out along -u_t, the direction the obtuse wedge opens
        found = []
        for scale in [mpf(2), mpf(10), mpf(100), mpf(1000)]:
            w = (-scale * cos(t), -scale * sin(t))
            if in_wedge_at(w, t, p):
                found.append(scale)
        unbounded = len(found) == 4
        ok &= unbounded
        print(
            f"  p={num}pi/{den:<3} tan(p)={mp.nstr(tan(p), 8):>14}  "
            f"members at |w| in {[str(f) for f in found]}  "
            f"{'UNBOUNDED -> not an isoceles triangle' if unbounded else 'bounded?!'}"
        )
    # and it excludes the near side entirely
    p = pi * 2 / 3
    near = (mpf(1) / 10, mpf(0))
    print(
        f"  point on the +u side at |w|=0.1 is in wedgeAt(p=2pi/3)? "
        f"{in_wedge_at(near, mpf(0), p)}  (expected False)"
    )
    ok &= not in_wedge_at(near, mpf(0), p)
    return ok


def check_claim2():
    """The subtractive decomposition, over a deterministic grid."""
    print("\n=== CLAIM 2: triangle == (W_a | W_b) \\ W_{pi-c}, c obtuse ===")
    ok = True
    # obtuse triples (a + b + c = pi, c > pi/2)
    triples = [
        (pi / 6, pi / 6, pi * 2 / 3),
        (pi / 12, pi / 4, pi * 2 / 3),
        (pi / 8, pi / 8, pi * 3 / 4),
        (pi / 5, pi / 12, pi * 43 / 60),
    ]
    N = 121  # 121x121 grid over [-1.2, 1.2]^2
    for t_num, t_den in [(0, 1), (1, 5)]:
        t = pi * t_num / t_den
        for (a, b, c) in triples:
            assert abs(a + b + c - pi) < mpf(10) ** (-30)
            mismatch = 0
            tested = 0
            skipped = 0
            first_bad = None
            for i in range(N):
                x = mpf(-12) / 10 + (mpf(24) / 10) * i / (N - 1)
                for j in range(N):
                    y = mpf(-12) / 10 + (mpf(24) / 10) * j / (N - 1)
                    w = (x, y)
                    if near_any_edge(w, t, a, b, c):
                        skipped += 1
                        continue
                    tested += 1
                    lhs = in_inscribed_triangle(w, t, a, b, c)
                    rhs = rhs_decomposition(w, t, a, b, c)
                    if lhs != rhs:
                        mismatch += 1
                        if first_bad is None:
                            first_bad = (w, lhs, rhs)
            good = mismatch == 0
            ok &= good
            cdeg = mp.nstr(c * 180 / pi, 6)
            print(
                f"  t={t_num}pi/{t_den} c={cdeg}deg  tested={tested:<6} "
                f"skipped(edge)={skipped:<4} mismatch={mismatch:<5} "
                f"{'OK' if good else 'FAIL'}"
            )
            if first_bad is not None:
                w, lhs, rhs = first_bad
                print(
                    f"      first disagreement at "
                    f"({mp.nstr(w[0], 10)}, {mp.nstr(w[1], 10)}): "
                    f"triangle={lhs} decomposition={rhs}"
                )
    return ok


def main() -> int:
    ok1 = check_claim1()
    ok2 = check_claim2()
    print()
    if ok1 and ok2:
        print(
            "BOTH CLAIMS HOLD.\n"
            "  1. wedgeAt at an obtuse half-angle is unbounded and opens away from\n"
            "     the circumcentre -- so the obtuse case cannot be obtained by\n"
            "     substituting an obtuse angle into the existing wedge.\n"
            "  2. The correct decomposition is (W_a | W_b) \\ W_{pi-c}, whose three\n"
            "     half-angles a, b, pi-c are ALL ACUTE when c is obtuse -- the set\n"
            "     analogue of lob_sum_eq_reflected. The existing acute wedge\n"
            "     machinery applies to every piece; the minus sign lives in the set\n"
            "     algebra.\n"
            "This fixes the target for the Lean a.e. identity. It proves nothing\n"
            "about the volume identity itself."
        )
        return 0
    print("A CLAIM FAILED -- do not cite this decomposition.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
