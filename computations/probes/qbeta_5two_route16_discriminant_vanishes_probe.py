#!/usr/bin/env python3
"""Route 16 -- REFUTATION: the discriminant VANISHES on the transport arc.

Bean `qou-trns`; resolves roast item 2 of `qou-rstq`, and refutes a load-bearing
claim in `qou-trns` and `qou-8v3k`.

WHAT WAS CLAIMED
----------------
`qou-trns` closes sub-gap 1 (the branch integer `k = 0`) with a five-step
argument whose step 2 reads:

    "The three branches y_j(x) are continuous and never collide on the arc
     (min |disc| = 0.348), so g is continuous."

and states the envelope theorem's IFT hypothesis as

    "y_j(x) differentiable, which follows from the implicit function theorem
     given non-vanishing discriminant (HAVE IT: min |disc| = 0.348 on the arc)".

`qou-rstq` roast item 2 flagged the measurement: "confirmed by finite
differences, which is evidence, not proof. The IFT hypothesis (min |disc| =
0.348) was measured on a sampled arc -- a finer sweep could in principle find a
near-collision."

WHAT IS TRUE
------------
It is not a near-collision. **min |disc| = 0**, and two of the three branches
collide exactly, at

    theta_0 = 137.9206708879635 deg,  x_0 = e^(i*theta_0),  |x_0| = 1
    y_2 = y_3 = -1.13224188231190019...    (separation 9.4e-26 at 50 dps)

THE PROOF NEEDS NO NUMERICS
---------------------------
The GGM deformed 5_2 curve is  x*y^3 - (x^2+1)*y^2 + (x^2+x+1)*y - x = 0.  Its
discriminant in y is, exactly, in Z[x]:

    disc(x) = x^8 - 6x^7 + 11x^6 - 12x^5 - 11x^4 - 12x^3 + 11x^2 - 6x + 1

which is **palindromic**. So disc(x)/x^4 is a polynomial in u = x + 1/x:

    Q(u) = u^4 - 6u^3 + 7u^2 + 6u - 31

and a point of |x| = 1 is a root of disc **iff** the corresponding
u = 2*cos(theta) is a real root of Q in [-2, 2].  Then, in integers:

    Q(-2) = 16 + 48 + 28 - 12 - 31 = +49
    Q(-1) =  1 +  6 +  7 -  6 - 31 = -23

Q is a real polynomial, so by the intermediate value theorem it has a root in
(-2, -1) subset [-2, 2].  **That is a complete proof, in integer arithmetic,
that the discriminant vanishes somewhere on the unit circle.** Everything below
is confirmation, not the argument.

WHERE 0.348 CAME FROM
---------------------
The dip is narrow. |disc| near the zero grows like |disc'| * delta with
|disc'| ~ 87, so a scan of N points over [0, pi] reports a minimum of about
87 * pi/(2N):

    N =   360  ->  ~0.38     (the 0.348 that was recorded)
    N = 20000  ->  ~0.0068   (measured here)
    N -> inf   ->   0

**A grid minimum was reported as if it were the true minimum.** The zero was
always there; the sampling stepped over it.

WHAT THIS BREAKS
----------------
1. `qou-trns` sub-gap 1 ("k = 0 is PINNED") -- its step 2 assumes the branches
   never collide on the arc. They do. The conclusion S(-1) = S(1) + pi^2 may
   still hold, but this argument does not establish it.
2. The envelope theorem's IFT hypothesis is **false as stated**: the implicit
   function theorem does not apply at x_0.
3. Anything that inherits "min |disc| = 0.348" as a fact.

WHAT IT DOES NOT BREAK
----------------------
The sum rule itself is verified to 80 dps and this probe says nothing against
it. Note also that Sum_j V_j is a **symmetric** function of the roots, and
symmetric functions of the roots of a polynomial stay analytic across a branch
point even though the individual branches do not. So the likely repair is to
work with the symmetric combination throughout, or to deform the path off
|x| = 1 around x_0. Neither is written, and neither is assumed here.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import itertools
import json
import pathlib

from mpmath import acos, exp, fabs, im, mp, mpc, mpf, nstr, pi, polyroots, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

# disc_y of  x*y^3 - (x^2+1)*y^2 + (x^2+x+1)*y - x,  exactly, low -> high
DISC = [1, -6, 11, -12, -11, -12, 11, -6, 1]
# disc(x)/x^4 in u = x + 1/x
QCOEF = [-31, 6, 7, -6, 1]  # low -> high


def disc(x):
    return sum(c * x ** k for k, c in enumerate(DISC))


def disc_direct(x):
    """The discriminant recomputed from the cubic, as an independent check."""
    a, b, c, d = x, -(x ** 2 + 1), x ** 2 + x + 1, -x
    return 18 * a * b * c * d - 4 * b ** 3 * d + b ** 2 * c ** 2 - 4 * a * c ** 3 \
        - 27 * a ** 2 * d ** 2


def qpoly(u):
    return sum(c * u ** k for k, c in enumerate(QCOEF))


def main() -> int:
    set_compute_dps()
    gates = []

    # ---- G1: the coefficient list is right (independent recomputation) -------
    worst = mpf(0)
    for xt in [mpc("0.3", "0.7"), mpc("-1.2", "0.4"), mpc("2", "-3"), mpc(1)]:
        worst = max(worst, fabs(disc(xt) - disc_direct(xt)))
    d1 = disc(mpc(1))
    gates.append({
        "gate": "G1",
        "claim": "disc(x) = x^8-6x^7+11x^6-12x^5-11x^4-12x^3+11x^2-6x+1, checked against "
                 "a direct recomputation from the cubic, and disc(1) = -23 matches the "
                 "5_2 polynomial y^3-2y^2+3y-1",
        "worst_abs_diff": nstr(worst, 8),
        "disc_at_1": nstr(re(d1), 8),
        "pass": bool(worst < mpf(10) ** -40 and fabs(d1 - (-23)) < mpf(10) ** -40),
    })

    # ---- G2: palindromic, hence a polynomial in u = x + 1/x -----------------
    palindromic = DISC == DISC[::-1]
    chk = mpf(0)
    for t in ["0.31", "1.7", "2.9"]:
        x = mpf(t)
        chk = max(chk, fabs(disc(x) / x ** 4 - qpoly(x + 1 / x)))
    gates.append({
        "gate": "G2",
        "claim": "disc is palindromic, so disc(x)/x^4 = Q(u) with u = x + 1/x and "
                 "Q(u) = u^4 - 6u^3 + 7u^2 + 6u - 31",
        "palindromic": palindromic,
        "worst_identity_residual": nstr(chk, 8),
        "pass": bool(palindromic and chk < mpf(10) ** -35),
    })

    # ---- G3: THE PROOF -- integer arithmetic and IVT, no floating point ------
    qm2 = sum(c * (-2) ** k for k, c in enumerate(QCOEF))
    qm1 = sum(c * (-1) ** k for k, c in enumerate(QCOEF))
    gates.append({
        "gate": "G3",
        "claim": "PROOF (integers + IVT): Q(-2) > 0 > Q(-1), so Q has a real root in "
                 "(-2,-1) subset [-2,2], i.e. disc vanishes at a point of |x| = 1",
        "Q_at_minus_2": qm2, "Q_at_minus_1": qm1,
        "arithmetic": "exact integers",
        "pass": bool(isinstance(qm2, int) and isinstance(qm1, int) and qm2 > 0 > qm1),
    })

    # ---- G4: locate it, and confirm the branches actually collide -----------
    u0 = [re(r) for r in polyroots(QCOEF[::-1], maxsteps=300, extraprec=300)
          if fabs(im(r)) < mpf(10) ** -30 and mpf(-2) < re(r) < mpf(2)][0]
    th0 = acos(u0 / 2)
    x0 = exp(1j * th0)
    a, b, c, d = x0, -(x0 ** 2 + 1), x0 ** 2 + x0 + 1, -x0
    ys = polyroots([a, b, c, d], maxsteps=400, extraprec=400)
    seps = [fabs(p - q) for p, q in itertools.combinations(ys, 2)]
    gates.append({
        "gate": "G4",
        "claim": "REFUTATION: two of the three y-branches collide EXACTLY on |x| = 1 -- "
                 "min |disc| is 0, not 0.348",
        "theta_deg": nstr(th0 * 180 / pi, 16),
        "u0": nstr(u0, 20),
        "abs_x0": nstr(fabs(x0), 20),
        "abs_disc_at_x0": nstr(fabs(disc(x0)), 8),
        "min_branch_separation": nstr(min(seps), 8),
        "colliding_value": nstr(re(sorted(ys, key=lambda z: re(z))[0]), 20),
        "pass": bool(fabs(disc(x0)) < mpf(10) ** -40 and min(seps) < mpf(10) ** -20),
    })

    # ---- G5: reproduce how 0.348 was obtained -------------------------------
    rows = []
    for n in (360, 2000, 20000):
        best = min(fabs(disc(exp(1j * pi * i / n))) for i in range(n + 1))
        rows.append({"N": n, "grid_min": nstr(best, 8)})
    n360 = mpf(rows[0]["grid_min"])
    gates.append({
        "gate": "G5",
        "claim": "the recorded 0.348 is a GRID minimum: it shrinks as the scan refines, "
                 "and an N~360 scan of [0,pi] lands near 0.35",
        "grid_minima": rows,
        "note": "a grid minimum was reported as if it were the true minimum; the zero "
                "was always there and the sampling stepped over it",
        "pass": bool(n360 > mpf("0.1")
                     and mpf(rows[2]["grid_min"]) < mpf(rows[1]["grid_min"]) < n360),
    })

    # ---- G6: the base point really is well separated (so the contrast is real)
    ys1 = polyroots([1, -2, 3, -1], maxsteps=300, extraprec=300)
    s1 = min(fabs(p - q) for p, q in itertools.combinations(ys1, 2))
    gates.append({
        "gate": "G6",
        "claim": "at the base point x = 1 the roots ARE well separated (|disc| = 23, "
                 "min separation 1.35) -- the collision is a property of the arc, not of "
                 "the 5_2 point",
        "min_separation_at_x_eq_1": nstr(s1, 8),
        "pass": bool(s1 > mpf("1.3")),
    })

    out = {
        "probe": "qbeta_5two_route16_discriminant_vanishes",
        "bean": "qou-trns",
        "roast_item": "qou-rstq item 2",
        "parent_bean": "qou-0yqu",
        "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "outcome": "REFUTED. The discriminant of the GGM deformed 5_2 curve VANISHES on "
                       "the transport arc |x| = 1, at theta = 137.9206708879635 deg, where "
                       "two of the three y-branches collide exactly. min |disc| = 0, not "
                       "0.348.",
            "proof": "disc is palindromic, so disc(x)/x^4 = Q(x + 1/x) with Q(u) = "
                     "u^4-6u^3+7u^2+6u-31. Points of |x|=1 correspond to real u in [-2,2]. "
                     "Q(-2) = +49 and Q(-1) = -23, both exact integers, so IVT gives a root "
                     "in (-2,-1). No numerics are used in the existence argument.",
            "what_it_breaks": "(1) qou-trns sub-gap 1's step 2, 'the branches never collide "
                              "on the arc', which the k=0 pinning argument rests on; (2) the "
                              "envelope theorem's IFT hypothesis, false as stated; (3) any "
                              "downstream use of 'min |disc| = 0.348'.",
            "where_0.348_came_from": "a grid minimum from an ~N=360 scan of [0,pi]. The dip is "
                                     "narrow (|disc'| ~ 87), so the recorded value is about "
                                     "87*pi/(2N). Refining to N=20000 gives 0.0068.",
            "likely_repair_NOT_done_here": "Sum_j V_j is SYMMETRIC in the roots, and symmetric "
                                           "functions stay analytic across a branch point even "
                                           "though individual branches do not. So working with "
                                           "the symmetric combination, or deforming the path "
                                           "off |x|=1 around x_0, should recover the transport. "
                                           "Neither is written; neither is assumed here.",
            "not_refuted": "the sum rule itself. This probe says nothing against it.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route16-discriminant-vanishes.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: min |disc| = 0, NOT 0.348. The branches collide on the arc at 137.9207 deg.")
    print("         qou-trns's k=0 pinning argument and the envelope IFT hypothesis both break.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
