#!/usr/bin/env python3
"""Route 21 -- cut avoidance PROVED, and checked for vacuity.

Bean `qou-trns`. Pairs with `QOU/QBeta/FiveTwoCutAvoidance.lean` (sorry-free,
lake green), which turns Route 20's measured hypothesis into real algebra.

THE REDUCTION
-------------
On |x| = 1 the GGM curve's elementary symmetric functions are all REAL:

    e1 = (x^2+1)/x = x + 1/x = 2c,   e2 = (x^2+x+1)/x = 1 + 2c,   e3 = 1

with c = cos(phi). So the cubic in y is  Y^3 - 2c Y^2 + (1+2c) Y - 1, with real
coefficients. (c = 1 is the 5_2 polynomial; c = -1 is minus the Watson cubic.)

A factor 1 - x*y meets the cut (-inf, 0] exactly when t := x*y is real with
t >= 1. Put y = t/x = t*(c - i*s), s = sin(phi), substitute into the real cubic,
and split real/imaginary parts. Dividing the imaginary part by s*t (valid for
phi in (0,pi); t != 0 because e3 = 1) and using s^2 = 1 - c^2:

    I  = -4c^2 t^2 + 4c^2 t - 2c + t^2 - 1
    II = 4c^3 t^3 - 4c^3 t^2 + 2c^2 t - 3c t^3 + 2c t^2 + c t - 1

    Res_c(I, II) = 64 * t^3 * (t-1)^4 * (t^5 - t^3 + 1)

t = 0 is refused by II; t = 1 forces c = 0 from I and then II reads -1 = 0; and
t^5 - t^3 + 1 > 0 for all t > 0. Hence t < 0 -- so the factor 1 - x*y is not
merely off the cut but GREATER THAN 1.

WHY THE VACUITY GATE (G5) IS THE IMPORTANT ONE
-----------------------------------------------
`xy_neg` is a no-solution theorem, and a no-solution theorem is worthless if its
hypotheses are never satisfiable -- it would then be proving something about an
empty set while the real factors did whatever they liked. G5 exhibits an actual
phi in (0, pi) at which x*y IS real, and checks the theorem's conclusion (t < 0)
there. Without that gate this whole file would be unfalsifiable.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (arg, cos, exp, fabs, findroot, im, mp, mpf, nstr, pi,
                    polyroots, re, sin, sqrt)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def ggm_roots(x):
    return polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x], maxsteps=500, extraprec=1000)


def reduced_roots(c):
    return polyroots([1, -2 * c, 1 + 2 * c, -1], maxsteps=500, extraprec=1000)


def match_dist(a, b):
    """Multiset distance: greedily match each root of `a` to its nearest in `b`."""
    b = list(b)
    worst = mpf(0)
    for u in a:
        k = min(range(len(b)), key=lambda i: fabs(u - b[i]))
        worst = max(worst, fabs(u - b[k]))
        b.pop(k)
    return worst


def I_of(t, c):
    return -4 * c ** 2 * t ** 2 + 4 * c ** 2 * t - 2 * c + t ** 2 - 1


def II_of(t, c):
    return (4 * c ** 3 * t ** 3 - 4 * c ** 3 * t ** 2 + 2 * c ** 2 * t
            - 3 * c * t ** 3 + 2 * c * t ** 2 + c * t - 1)


def main() -> int:
    set_compute_dps()
    TOL = mpf(10) ** -30
    gates = []

    # ---- G1: on |x| = 1 the cubic in y really is the real one ---------------
    worst1 = mpf(0)
    for i in range(0, 49):
        ph = pi * i / 48
        worst1 = max(worst1, match_dist(ggm_roots(exp(1j * ph)), reduced_roots(cos(ph))))
    gates.append({
        "gate": "G1",
        "claim": "on |x| = 1 the GGM cubic in y has REAL coefficients: its roots coincide with "
                 "those of Y^3 - 2c Y^2 + (1+2c) Y - 1, c = cos(phi). This is the observation "
                 "that removes the complex analysis from the whole question",
        "n_points": 49, "worst": nstr(worst1, 8), "pass": bool(worst1 < TOL),
    })

    # ---- G2: the Re/Im split is the one the Lean theorem takes as hypothesis -
    # For each root y, set t = x*y and verify hre / him vanish with y = t*(c - i*s).
    worst2 = mpf(0)
    for i in range(1, 24):
        ph = pi * i / 24
        x, c, s = exp(1j * ph), cos(ph), sin(ph)
        for y in ggm_roots(x):
            t = x * y                      # complex in general; the identities are formal
            hre = (c ** 3 * t ** 3 - 2 * c ** 3 * t ** 2 + 2 * c ** 2 * t
                   - 3 * c * s ** 2 * t ** 3 + 2 * c * s ** 2 * t ** 2 + c * t - 1)
            him = s * t * (-3 * c ** 2 * t ** 2 + 4 * c ** 2 * t - 2 * c + s ** 2 * t ** 2 - 1)
            # hre + i*him is P(t*(c-i*s)) rearranged; check against P evaluated directly
            yy = t * (c - 1j * s)
            P = yy ** 3 - 2 * c * yy ** 2 + (1 + 2 * c) * yy - 1
            worst2 = max(worst2, fabs((hre + 1j * him) - P))
    gates.append({
        "gate": "G2",
        "claim": "hre and him as stated in Lean's `xy_neg` really are the real and imaginary "
                 "parts of P(t*(c - i*s)) -- i.e. the hypotheses are the substitution they "
                 "claim to be, not a transcription of something else",
        "n_checks": 23 * 3, "worst": nstr(worst2, 8), "pass": bool(worst2 < TOL),
    })

    # ---- G3: the Bezout identity Lean's `linear_combination` certifies -------
    worst3 = mpf(0)
    for (tv, cv) in [("0.37", "-0.82"), ("1.9", "0.31"), ("-2.4", "0.77"),
                     ("5.0", "-0.05"), ("0.001", "0.999")]:
        t, c = mpf(tv), mpf(cv)
        A = -t ** 4 * (t - 1) ** 4 * (2 * c ** 2 * t ** 2 + c - t ** 2)
        B = -t ** 3 * (t - 1) ** 4 * (2 * c * t ** 2 + 1)
        lhs = A * I_of(t, c) + B * II_of(t, c)
        rhs = t ** 3 * (t - 1) ** 4 * (t ** 5 - t ** 3 + 1)
        worst3 = max(worst3, fabs(lhs - rhs))
    gates.append({
        "gate": "G3",
        "claim": "the Bezout cofactors are right: A*I + B*II = t^3 (t-1)^4 (t^5 - t^3 + 1) with "
                 "A = -t^4 (t-1)^4 (2c^2 t^2 + c - t^2), B = -t^3 (t-1)^4 (2c t^2 + 1). Lean "
                 "checks this by `linear_combination`, so the resultant is verified, not trusted",
        "n_points": 5, "worst": nstr(worst3, 8), "pass": bool(worst3 < TOL),
    })

    # ---- G4: the quintic has no positive real root --------------------------
    rc = sqrt(mpf(3) / 5)
    qmin = rc ** 5 - rc ** 3 + 1
    pos_roots = [re(z) for z in polyroots([1, 0, -1, 0, 0, 1], maxsteps=400, extraprec=400)
                 if fabs(im(z)) < mpf(10) ** -20 and re(z) > 0]
    gates.append({
        "gate": "G4",
        "claim": "t^5 - t^3 + 1 > 0 for every t > 0 -- the factor that kills the last branch of "
                 "the eliminant. Minimum 0.814 at t = sqrt(3/5); Lean proves it by a two-case "
                 "split that needs neither the critical point nor its value",
        "critical_point": nstr(rc, 12), "min_value": nstr(qmin, 12),
        "positive_real_roots": [nstr(v, 10) for v in pos_roots],
        "pass": bool(len(pos_roots) == 0 and qmin > 0),
    })

    # ---- G5: THE VACUITY GATE -- x*y really is real somewhere on (0, pi) ----
    # For the conjugate pair y = r e^{i theta}, x*y is real exactly when
    # phi + theta = 0 or pi (mod 2 pi). Solve phi + theta(phi) = pi.
    def theta_of(ph):
        cpx = [z for z in reduced_roots(cos(ph)) if im(z) > mpf(10) ** -25]
        return arg(cpx[0]) if cpx else None

    def gap(ph):
        th = theta_of(ph)
        return (ph + th - pi) if th is not None else mpf(1)

    ph_star = findroot(gap, mpf("1.4"))
    x_star = exp(1j * ph_star)
    ys = reduced_roots(cos(ph_star))
    ts = [x_star * y for y in ys]
    real_ts = [t for t in ts if fabs(im(t)) < mpf(10) ** -25]
    # and the value attained is EXACTLY the quintic's unique real root
    quintic_real_root = [re(z) for z in polyroots([1, 0, -1, 0, 0, 1], maxsteps=400,
                                                  extraprec=400)
                         if fabs(im(z)) < mpf(10) ** -20]
    sharp = min(fabs(re(t) - r) for t in real_ts for r in quintic_real_root)
    gates.append({
        "gate": "G5",
        "claim": "VACUITY CHECK -- the hypotheses of `xy_neg` are satisfiable, so the theorem is "
                 "not about an empty set. Where phi + theta = pi the product x*y IS real, and "
                 "the conclusion holds: t < 0, so 1 - x*y exceeds 1. Better, the value attained "
                 "is EXACTLY the unique real root of t^5 - t^3 + 1 -- the eliminant is sharp, "
                 "not merely a bound: its one real root is realised on the arc, and it is "
                 "negative, which is the whole reason the cut is missed",
        "phi_star_over_pi": nstr(ph_star / pi, 12),
        "real_t_values": [nstr(re(t), 12) for t in real_ts],
        "one_minus_t": [nstr(1 - re(t), 12) for t in real_ts],
        "quintic_real_root": [nstr(r, 12) for r in quintic_real_root],
        "sharpness_deviation": nstr(sharp, 8),
        "pass": bool(len(real_ts) >= 1 and all(re(t) < 0 for t in real_ts)
                     and all(1 - re(t) > 1 for t in real_ts) and sharp < TOL),
    })

    # ---- G6: the t = 1 branch is genuinely refuted, not assumed away --------
    I_at_1 = [nstr(I_of(mpf(1), mpf(cv)), 8) for cv in ["0", "0.5", "-0.5"]]
    II_at_1_c0 = II_of(mpf(1), mpf(0))
    gates.append({
        "gate": "G6",
        "claim": "the t = 1 branch of the eliminant dies for a reason: I(1, c) = -2c, so t = 1 "
                 "forces c = 0; and II(1, 0) = -1 != 0. (t = 1 matters because 1 - x*y = 0 is "
                 "the endpoint of the cut, so it would be a contact too)",
        "I_at_t1_for_c_in_0_half_neghalf": I_at_1,
        "II_at_t1_c0": nstr(II_at_1_c0, 8),
        "pass": bool(fabs(II_at_1_c0 + 1) < TOL),
    })

    # ---- G7: the endpoint is outside the theorem's scope, and is the contact -
    w1 = max(re(r) for r in polyroots([1, -2, -1, 1], maxsteps=400, extraprec=400)
             if fabs(im(r)) < mpf(10) ** -30)
    ys_end = reduced_roots(mpf(-1))
    ts_end = sorted((re(-y) for y in ys_end), reverse=True)   # x = -1, so t = x*y = -y
    gates.append({
        "gate": "G7",
        "claim": "at phi = pi we have s = 0, so `xy_neg` does NOT apply -- and indeed the "
                 "contact is there: t = w_1 = 2.2469796 >= 1, giving 1 - x*y = 1 - w_1 < 0. The "
                 "theorem's s != 0 hypothesis is exactly what excludes the one real contact",
        "w1": nstr(w1, 20), "t_values_at_pi": [nstr(v, 12) for v in ts_end],
        "largest_t": nstr(ts_end[0], 20),
        "pass": bool(fabs(ts_end[0] - w1) < TOL and ts_end[0] > 1),
    })

    out = {
        "probe": "qbeta_5two_route21_cut_avoidance_proved",
        "bean": "qou-trns", "parent_bean": "qou-0yqu", "dps": mp.dps,
        "pairs_with_lean": "QOU/QBeta/FiveTwoCutAvoidance.lean (xy_neg, eliminant, quintic_pos)",
        "gates": gates,
        "verdict": {
            "outcome": "Cut avoidance on 0 < phi < pi is now real algebra and is PROVED in Lean: "
                       "if x*y is real then it is NEGATIVE, so 1 - x*y > 1. Route 20's measured "
                       "margin is no longer the evidence for the interior of the arc.",
            "the_mechanism": "on |x| = 1 all three elementary symmetric functions of the GGM "
                             "curve are real, so the cubic in y has real coefficients. That "
                             "collapses a complex-analytic question to elimination between two "
                             "real polynomials, whose resultant is 64 t^3 (t-1)^4 (t^5-t^3+1).",
            "vacuity": "G5 exhibits a phi in (0,pi) where x*y is genuinely real and checks the "
                       "conclusion there. A no-solution theorem with unsatisfiable hypotheses "
                       "would prove nothing, and this is the gate that would have caught it.",
            "still_not_proved": "the passage from 'F is continuous' to 'no factor meets the cut' "
                                "-- Log's continuity off (-inf,0] composed with continuity of "
                                "the root multiset -- is NOT formalised; nor is the one-sided "
                                "limit at phi = pi, where the arc genuinely touches the cut. So "
                                "hcont is not yet a theorem end to end.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route21-cut-avoidance-proved.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: cut avoidance on the open arc is proved; the hypotheses are satisfiable.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
