#!/usr/bin/env python3
"""Route 71 -- Ohtsuki's 5_2 critical point IS the corpus saddle cubic, and its
critical value IS Vol(5_2).

Beans `qou-thmb` (the Picard-Lefschetz / volume route) and `qou-xblo` (the sum
rule lane whose cubic this turns out to be).

SOURCE (ingested this session, library/104171-qt-83/10.4171-qt-83.pdf, blob 632e54ac)
-----------------------------------------------------------------------
T. Ohtsuki, "On the asymptotic expansion of the Kashaev invariant of the 5_2
knot", Quantum Topol. 7 (2016) 669-735, DOI 10.4171/QT/83.  67 pages.

The volume conjecture for 5_2 is a THEOREM there -- this settles the question
bean `qou-thmb` recorded as unverified memory.  Ohtsuki's Appendix C gives the
critical-point system of the potential; §3 is the saddle point method.

WHAT THIS PROBE ESTABLISHES
---------------------------
Ohtsuki's potential (Introduction, p.671) is

    Vhat(x,y) = Li_2(xy) + Li_2(1/(xy)) + Li_2(y) - Li_2(1/y) - Li_2(1/x) - Li_2(1)

and his critical-point system (Appendix C, eq. before (77), at hbar -> 0) is

    (1 - x)*y = 1,      x*(y - 1)^2 = 1

Eliminating y = 1/(1-x) gives  x^3 = (1-x)^2.  The corpus's own 5_2 saddle
cubic, carried since Route 1 and proved about all session, is  y^2 = (1-y)^3.
**These are the same equation under x = 1 - y** -- the reflection z -> 1-z that
`FiveTwoComplexPentagon.cRogersL_add_one_sub` already proves in Lean.

And at the COMPLEX critical point, Im Vhat = Vol(5_2) exactly.

So the corpus's saddle data and Ohtsuki's volume-conjecture saddle are the same
object in different coordinates.  That is the bridge from this lane to the
volume -- it is NOT the volume conjecture itself, see G5.

**The 5_2 sum rule is PROVED** (`FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`).
The 5_2 VOLUME conjecture is Ohtsuki's theorem, not the corpus's, and is not
formalized here.
"""

import json
import pathlib

from mpmath import (fabs, im, mp, mpc, mpf, nstr, pi, polylog, polyroots, re)

# The corpus's own recorded value: qou-mass/_internal/knot_volumes.py,
# `_SNAPPY_HP_50` -- SnapPy high-precision, 50 dps.  NOT a typed-from-memory
# constant; see the "lesson" field below for why that distinction earned itself.
VOL_5_2_SNAPPY_50 = "2.8281220883307831627638988092766349427709813173006"

OHTSUKI_CUBIC = [1, -1, 2, -1]     # x^3 - x^2 + 2x - 1  <=>  x^3 = (1-x)^2
CORPUS_CUBIC = [1, -2, 3, -1]      # y^3 - 2y^2 + 3y - 1 <=>  y^2 = (1-y)^3


def vhat(x, y):
    """Ohtsuki's potential, Quantum Topol. 7 (2016) p.671."""
    return (polylog(2, x * y) + polylog(2, 1 / (x * y)) + polylog(2, y)
            - polylog(2, 1 / y) - polylog(2, 1 / x) - polylog(2, mpf(1)))


def main() -> int:
    mp.dps = 80
    tol = mpf(10) ** -60
    gates = []
    vol = mpf(VOL_5_2_SNAPPY_50)

    oh = polyroots(OHTSUKI_CUBIC, maxsteps=2000, extraprec=9000)
    co = polyroots(CORPUS_CUBIC, maxsteps=2000, extraprec=9000)

    # ---- G1: the critical system eliminates to x^3 = (1-x)^2 ---------------
    resid = []
    for x in oh:
        y = 1 / (1 - x)
        resid.append(max(fabs((1 - x) * y - 1), fabs(x * (y - 1) ** 2 - 1)))
    gates.append({
        "gate": "G1",
        "claim": "Ohtsuki's critical-point system (1-x)y = 1, x(y-1)^2 = 1 (Appendix C) is "
                 "solved exactly by y = 1/(1-x) with x a root of x^3 = (1-x)^2. Checked by "
                 "residual of BOTH equations at all three roots",
        "max_system_residual": nstr(max(resid), 10),
        "pass": bool(max(resid) < tol),
    })

    # ---- G2: it IS the corpus cubic, under x = 1 - y -----------------------
    mismatch = max(min(fabs((1 - y) - x) for x in oh) for y in co)
    gates.append({
        "gate": "G2",
        "claim": "THE IDENTIFICATION. {1 - y : y a root of the corpus saddle cubic y^2=(1-y)^3} "
                 "equals the root set of Ohtsuki's x^3=(1-x)^2, exactly. So the corpus's 5_2 "
                 "saddle cubic and Ohtsuki's volume-conjecture critical point are the same "
                 "equation in coordinates differing by z -> 1-z -- the reflection already proved "
                 "in Lean as cRogersL_add_one_sub",
        "corpus_roots": [nstr(z, 25) for z in co],
        "ohtsuki_roots": [nstr(z, 25) for z in oh],
        "max_setwise_mismatch": nstr(mismatch, 10),
        "pass": bool(mismatch < tol),
    })

    # ---- G3: the critical value at the COMPLEX point is Vol(5_2) -----------
    xc = [z for z in oh if im(z) > mpf(10) ** -60][0]
    yc = 1 / (1 - xc)
    Vc = vhat(mpc(xc), mpc(yc))
    dv = fabs(im(Vc) - vol)
    gates.append({
        "gate": "G3",
        "claim": "THE PAYOFF. At the complex critical point, Im Vhat = Vol(5_2) -- agreeing with "
                 "the corpus's own SnapPy HP 50-dps constant to its full recorded precision. This "
                 "is the bridge from the corpus's saddle data to the hyperbolic volume",
        "x_critical": nstr(xc, 30),
        "y_critical": nstr(yc, 30),
        "Vhat_at_critical": nstr(Vc, 30),
        "Im_Vhat": nstr(im(Vc), 60),
        "Vol_5_2_corpus_snappy_50dps": VOL_5_2_SNAPPY_50,
        "residual": nstr(dv, 10),
        "extends_corpus_constant_to_79_dps": nstr(im(Vc), 79),
        "pass": bool(dv < mpf(10) ** -48),
    })

    # ---- G4: the REAL critical point does not give the volume (control) ----
    xr = re([z for z in oh if fabs(im(z)) < mpf(10) ** -60][0])
    Vr = vhat(mpc(xr), mpc(1 / (1 - xr)))
    gates.append({
        "gate": "G4",
        "claim": "CONTROL: the branch matters. At the REAL critical point Im Vhat = 1.7668..., "
                 "which is NOT Vol(5_2) = 2.8281... So the geometric solution is the complex "
                 "critical point, and a probe that forgot to select it would report a wrong "
                 "volume rather than an obvious failure",
        "x_real": nstr(xr, 25),
        "Im_Vhat_at_real_point": nstr(im(Vr), 25),
        "distance_from_volume": nstr(fabs(fabs(im(Vr)) - vol), 10),
        "pass": bool(fabs(fabs(im(Vr)) - vol) > mpf(1) / 2),
    })

    # ---- G5: scope ---------------------------------------------------------
    gates.append({
        "gate": "G5",
        "claim": "SCOPE, so this cannot be overread. What is checked here is that the critical "
                 "VALUE of Ohtsuki's potential is the volume. The volume CONJECTURE is the "
                 "asymptotic  2pi/N log <5_2>_N -> Vol(5_2), which needs the saddle point method "
                 "of Ohtsuki §3-5 plus the Poisson summation of §4 -- 67 pages, none of it here "
                 "and none of it in Lean. Nor does the corpus's proved SUM RULE give the volume: "
                 "D cancels identically on the Galois orbit",
        "critical_value_identified": True,
        "volume_conjecture_formalized": False,
        "sum_rule_gives_volume": False,
        "pass": True,
    })

    out = {
        "probe": "qbeta_5two_route71_ohtsuki_critical_point",
        "beans": ["qou-thmb", "qou-xblo"], "dps": mp.dps,
        "source": {
            "ref": "Ohtsuki, Quantum Topol. 7 (2016) 669-735, DOI 10.4171/QT/83",
            "file": "library/104171-qt-83/10.4171-qt-83.pdf", "blob": "632e54acc09336ae9dbfc1207bef99a13a5f72a4",
            "settles": "the 5_2 volume conjecture IS a published theorem -- bean qou-thmb "
                       "recorded this as unverified memory; it is now verified from the paper.",
        },
        "gates": gates,
        "verdict": {
            "identification": "Ohtsuki's 5_2 critical point x^3=(1-x)^2 and the corpus's saddle "
                              "cubic y^2=(1-y)^3 are the same equation under x = 1-y.",
            "volume": "Im Vhat at the complex critical point = Vol(5_2), residual 4.9e-50 "
                      "(the precision floor of the corpus's own 50-dps constant).",
            "not_established": "the volume conjecture itself (the asymptotic). Ohtsuki proves it; "
                               "nothing here formalizes it.",
            "sum_rule_status": "PROVED (FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule)",
        },
        "lesson": "The first run of this probe reported a 3.8e-13 mismatch, stable across "
                  "dps = 40/60/80/120 -- so not a precision artifact. The cause was a Vol(5_2) "
                  "constant typed from memory, wrong from the 12th digit. The corpus's recorded "
                  "SnapPy HP 50-dps value is authoritative and its docstring already warns that a "
                  "15-dps literature anchor (2.82812208833410) was wrong. Take the constant from "
                  "the corpus, never from memory; and a residual that does NOT shrink with dps is "
                  "evidence about the inputs, not about the identity.",
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route71-ohtsuki-critical-point.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "Ohtsuki's 5_2 critical point IS the corpus saddle cubic under z -> 1-z, and its "
        "critical value IS Vol(5_2). The volume conjecture is Ohtsuki's published theorem, "
        "not formalized here."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
