#!/usr/bin/env python3
"""Route 7 of the 5₂ saddle sum rule: was Route 6's refutation actually complete?

Context
-------
Bean ``qou-r7ml`` (child of ``qou-0yqu``).  Route 6 tested Zagier's **enhanced
dilogarithm** (``library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf``, §II.1 B)

    D̃(ẑ) = Li₂(z) + ½·u·v      on   X̃ = {(u,v) : eᵘ + eᵛ = 1},  values in ℂ/(π²/2)ℤ

against the sum rule ``Σⱼ Re Vⱼ = −3π²/2`` and refuted it scope-(a), reporting
"no integer branch offset matches".  Its witness is
``computations/qbeta-5two-enhanced-dilog.witness.json``.

This probe re-opens exactly one gate of that witness.

**Gate G3 of the Route-6 witness — "Σⱼ Re D̃ is an exact rational multiple of
π²/2" — was evaluated at the PRINCIPAL BRANCH ONLY.**  It records the single
number ``sum_re_Dtilde = 2.777534425978115064062537`` and
``ratio_to_half_pi_sq = 0.5628…``, not an integer, and concludes refuted.  The
branch integers were never varied *for the sum*.  (Gate G1 does scan
``(n,m) ∈ [−2,2]²``, but for the different, per-root claim ``Vⱼ = 3·D̃``.)

Writing ``u = log y + 2πia`` and ``v = log(1−y) + 2πib``, the branch shift adds

    −π·bⱼ·arg(yⱼ) − π·aⱼ·arg(1−yⱼ) − 2π²·aⱼbⱼ

to ``Re D̃(yⱼ)``.  So the sum has TWO free integers per root, not one.

Gates
-----
G1  Control: reproduce the sum rule Σⱼ Re Vⱼ = −3π²/2 at 60 dps.
G2  Reproduce Route 6's principal-branch value and its π²/2 ratio exactly.
G3  The two structural identities the θ-cancellation rests on:
        Σⱼ Re L(yⱼ) = π²/2 − (2/3)·π·θ        (L = Rogers = principal-branch D̃)
        arg(1 − y₁)  = (2/3)·(θ − π)
G4  The θ-coefficient of Σⱼ Re D̃ vanishes iff  3(b₁−b₂) + 2(a₁−a₂) = −2.
    Route 6's a = 0 reduces this to 3(b₁−b₂) = −2, INSOLUBLE over ℤ — which is
    precisely why it saw no match.  With `a` free it IS soluble.
G5  The exact reachable set:  Σⱼ Re D̃(yⱼ)/π² ∈ 11/6 + 2ℤ.
    Derived (1/2 + (2/3)k − 2m with k ≡ 2 mod 3) and brute-forced.
G6  Neither target is in it: −1/2 (the Route-6 witness's own target, from
    V = 3·D̃) nor −3/2 (the raw sum-rule constant).
G7  THE KILL: the same construction lands in π²ℚ for every control cubic
    y^p = (1−y)^q as well — including the bean's named control y³−y²+2y−1,
    which is y³ = (1−y)². Rationality separates nothing. Route-2 trap.

Verdict
-------
Route 7 REFUTED, scope-(a) — and the modulus hypothesis that motivated it is
WRONG on its own terms: ℂ/2π²ℤ vs ℂ/(π²/2)ℤ is irrelevant here, because the
branch shift contributes −2π²aⱼbⱼ, always a multiple of 2π² and hence of π²/2
too.  The real defect in Route 6 was the single fixed branch integer, not the
modulus.  Route 6's conclusion stands; its stated reason does not.
"""
from __future__ import annotations

import json
import pathlib

from mpmath import (arg, binomial, fabs, im, log, mp, mpc, mpf, nstr, pi,
                    polylog, polyroots, re)

mp.dps = 60
DPS_REPORT = 25


def roots_of(coeffs):
    rs = list(polyroots(coeffs, maxsteps=300, extraprec=600))
    cplx = sorted([r for r in rs if abs(im(r)) > mpf(10) ** -40], key=lambda z: -im(z))
    real = [r for r in rs if abs(im(r)) <= mpf(10) ** -40]
    if len(cplx) != 2 or len(real) != 1:
        return None
    return [cplx[0], cplx[1], mpc(re(real[0]))]


def cubic_pq(p, q):
    """y^p - (1-y)^q as descending coefficients of a cubic."""
    c = [mpf(0)] * 4
    c[3 - p] += 1
    for k in range(q + 1):
        c[3 - k] -= binomial(q, k) * (-1) ** k
    return c


def rogers(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def re_Dtilde(z, a, b):
    u = log(z) + 2j * pi * a
    v = log(1 - z) + 2j * pi * b
    return re(polylog(2, z) + u * v / 2)


def reachable(Y, window=4, w3=2, tol=mpf(10) ** -25, constrained=True):
    """All Σⱼ Re D̃/π² that are rational (den | 6).

    ``constrained=True`` restricts to the 5₂ θ-cancelling family
    ``3(b₁−b₂) + 2(a₁−a₂) = −2``.  That condition is specific to ``y² = (1−y)³``;
    for a control ``y^p = (1−y)^q`` the analogous condition has different
    coefficients, so controls must be swept with ``constrained=False`` and the
    rationality tested directly.
    """
    # Exact decomposition -- verified in G0 -- so the sweep is pure arithmetic
    # after three polylog evaluations:
    #     Re D̃(z,a,b) = Re L(z) − π·b·arg(z) − π·a·arg(1−z) − 2π²·a·b
    pre = [(re(rogers(z)), arg(z), arg(1 - z)) for z in Y]
    pi2 = pi ** 2
    vals = set()
    R = range(-window, window + 1)
    R3 = range(-w3, w3 + 1)
    for a1 in R:
        for a2 in R:
            for b1 in R:
                for b2 in R:
                    if constrained and 3 * (b1 - b2) + 2 * (a1 - a2) != -2:
                        continue
                    head = mpf(0)
                    for (rl, ag, ag1), a, b in zip(pre[:2], (a1, a2), (b1, b2)):
                        head += rl - pi * b * ag - pi * a * ag1 - 2 * pi2 * a * b
                    rl3, ag3, ag13 = pre[2]
                    for a3 in R3:
                        for b3 in R3:
                            s = (head + rl3 - pi * b3 * ag3 - pi * a3 * ag13
                                 - 2 * pi2 * a3 * b3) / pi2
                            n6 = mp.nint(s * 6)
                            if fabs(s - n6 / 6) < tol:
                                vals.add(int(n6))
    return sorted(mpf(v) / 6 for v in vals)


def main():
    gates = []
    Y = roots_of([mpf(1), mpf(-2), mpf(3), mpf(-1)])
    y1, _y2, y3 = Y
    theta = arg(y1)

    # G0 -- the decomposition the sweep relies on
    worst = mpf(0)
    for z in Y:
        for a in (-2, 0, 3):
            for b in (-1, 2, 4):
                lhs = re_Dtilde(z, a, b)
                rhs = re(rogers(z)) - pi * b * arg(z) - pi * a * arg(1 - z) - 2 * pi ** 2 * a * b
                worst = max(worst, fabs(lhs - rhs))
    gates.append({"gate": "G0",
                  "claim": "Re Dtilde(z,a,b) = Re L(z) - pi*b*arg(z) - pi*a*arg(1-z) - 2 pi^2 a b",
                  "worst_abs_error": nstr(worst, 8),
                  "note": "makes the branch sweep pure arithmetic after 3 polylog calls",
                  "pass": bool(worst < mpf(10) ** -50)})

    # G1 -- control: the sum rule itself
    bs = (-1, +1, +1)
    tot = sum(re(3 * polylog(2, z) + (log(z) + b * pi * 1j) ** 2) for z, b in zip(Y, bs))
    g1 = tot - (-3 * pi ** 2 / 2)
    gates.append({"gate": "G1", "claim": "sum_j Re V_j == -3 pi^2/2 (control)",
                  "sum_re_V": nstr(tot, DPS_REPORT),
                  "residual": nstr(g1, 8), "pass": bool(fabs(g1) < mpf(10) ** -50)})

    # G2 -- reproduce Route 6's principal-branch number
    base = sum(re(rogers(z)) for z in Y)
    r6 = mpf("2.777534425978115064062537")
    gates.append({"gate": "G2", "claim": "reproduce Route-6 witness G3 principal-branch value",
                  "sum_re_Dtilde_principal": nstr(base, DPS_REPORT),
                  "route6_witness_value": str(r6),
                  "delta": nstr(base - r6, 8),
                  "ratio_to_half_pi_sq": nstr(base / (pi ** 2 / 2), 20),
                  "pass": bool(fabs(base - r6) < mpf(10) ** -24)})

    # G3 -- the two structural identities
    d1 = base - (pi ** 2 / 2 - (mpf(2) / 3) * pi * theta)
    d2 = arg(1 - y1) - (mpf(2) / 3) * (theta - pi)
    gates.append({"gate": "G3", "claim": "sum Re L = pi^2/2 - (2/3) pi theta  and  arg(1-y1) = (2/3)(theta-pi)",
                  "theta": nstr(theta, DPS_REPORT),
                  "residual_sum_re_L": nstr(d1, 8), "residual_arg": nstr(d2, 8),
                  "pass": bool(fabs(d1) < mpf(10) ** -50 and fabs(d2) < mpf(10) ** -50)})

    # G4 -- the solubility split that Route 6 missed
    sol_free = [(a, b) for a in range(-6, 7) for b in range(-6, 7) if 3 * b + 2 * a == -2]
    sol_a0 = [b for b in range(-20, 21) if 3 * b == -2]
    gates.append({"gate": "G4",
                  "claim": "theta cancels iff 3(b1-b2)+2(a1-a2) = -2; Route 6's a=0 makes it insoluble",
                  "solutions_with_a_free_sample": [list(s) for s in sol_free[:6]],
                  "n_solutions_a_free": len(sol_free),
                  "solutions_with_a_fixed_zero": sol_a0,
                  "route6_scan_was_principal_branch_only_for_the_sum": True,
                  "pass": bool(len(sol_free) > 0 and len(sol_a0) == 0)})

    # G5 -- the exact reachable coset
    vals = reachable(Y)
    coset_ok = all(fabs((v - mpf(11) / 6) / 2 - mp.nint((v - mpf(11) / 6) / 2)) < mpf(10) ** -25
                   for v in vals)
    gates.append({"gate": "G5", "claim": "sum_j Re Dtilde / pi^2 in 11/6 + 2Z (exactly)",
                  "n_values": len(vals),
                  "min": nstr(vals[0], 12), "max": nstr(vals[-1], 12),
                  "all_congruent_11_over_6_mod_2": bool(coset_ok),
                  "derivation": "1/2 + (2/3)k - 2m with k = a1-a2 = 2 mod 3, m = a1b1+a2b2+a3b3",
                  "pass": bool(coset_ok)})

    # G6 -- both targets excluded
    tg = {}
    for nm, t in (("-1/2 (V = 3*Dtilde; the Route-6 witness's own G3 target)", mpf(-1) / 2),
                  ("-3/2 (the raw sum-rule constant)", mpf(-3) / 2)):
        k = (t - mpf(11) / 6) / 2
        tg[nm] = {"in_reachable_set": bool(any(fabs(v - t) < mpf(10) ** -25 for v in vals)),
                  "(t - 11/6)/2": nstr(k, 12),
                  "is_integer": bool(fabs(k - mp.nint(k)) < mpf(10) ** -25)}
    gates.append({"gate": "G6", "claim": "neither sum-rule target lies in the reachable coset",
                  "targets": tg,
                  "pass": bool(not any(v["in_reachable_set"] for v in tg.values()))})

    # G7 -- THE KILL: controls do the same thing
    controls = []
    for (p, q, tag) in ((2, 3, "5_2 TARGET"), (3, 2, "control A (bean's named control)"),
                        (1, 3, "control B"), (3, 1, "control C")):
        Yc = roots_of(cubic_pq(p, q))
        if Yc is None:
            continue
        vc = reachable(Yc, window=3, w3=2, constrained=False)
        controls.append({"p": p, "q": q, "tag": tag,
                         "cubic": [int(x) for x in cubic_pq(p, q)],
                         "n_rational_landings": len(vc),
                         "sample": [nstr(v, 10) for v in vc[:4]],
                         # distinct consecutive gaps; 2 is the true coset spacing, and
                         # larger gaps are search-window truncation at the extremes,
                         # not structure.
                         "distinct_spacings": sorted({nstr(vc[i + 1] - vc[i], 6)
                                                      for i in range(len(vc) - 1)}),
                         "modal_spacing_is_2": bool(len(vc) > 1 and sum(
                             1 for i in range(len(vc) - 1)
                             if fabs((vc[i + 1] - vc[i]) - 2) < mpf(10) ** -25) > (len(vc) - 1) / 2)})
    gates.append({"gate": "G7",
                  "claim": "KILL: control cubics y^p=(1-y)^q also land in pi^2 Q -- rationality separates nothing",
                  "controls": controls,
                  "interpretation": "same failure mode as Route 2: the property is generic to the shape, "
                                    "not arithmetic of the 5_2 trace field",
                  "pass": bool(all(c["n_rational_landings"] > 0 for c in controls))})

    out = {
        "probe": "qbeta_5two_route7_enhanced_dilog_branch_freedom",
        "bean": "qou-r7ml",
        "parent_bean": "qou-0yqu",
        "dps": mp.dps,
        "reopens": "computations/qbeta-5two-enhanced-dilog.witness.json gate G3",
        "gates": gates,
        "verdict": {
            "route7": "REFUTED, scope-(a)",
            "route6_conclusion": "STANDS",
            "route6_stated_reason": "INCOMPLETE -- G3 varied no branch integers for the sum; "
                                    "with a free, 3(b1-b2)+2(a1-a2)=-2 IS soluble and exact "
                                    "rationality IS reachable",
            "modulus_hypothesis": "WRONG -- C/2pi^2 Z vs C/(pi^2/2) Z is irrelevant: the branch "
                                  "shift contributes -2 pi^2 a_j b_j, a multiple of 2pi^2 and of "
                                  "pi^2/2 alike. The quarter-lattice coincidence -3pi^2/2 = "
                                  "-(3/4)(2pi^2) was not the mechanism.",
            "sum_rule_status": "verified to 80 dps, unproved -- UNCHANGED",
        },
    }
    dest = pathlib.Path(__file__).resolve().parents[1] / "qbeta-5two-route7-enhanced-dilog-branch-freedom.witness.json"
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim']}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: Route 7 refuted scope-(a); Route 6's conclusion stands, its stated reason does not.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
