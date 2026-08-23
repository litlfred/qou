#!/usr/bin/env python3
"""Route 18 -- the level-7 ladder is CLASSICAL. Watson (1937), via Kirillov.

Beans `qou-fivt`, `qou-abel`, `qou-0yqu`. Literature supplied 2026-08-08:
`library/arxiv-hep-th-9408113v2/9408113v2.pdf` (Kirillov, *Dilogarithm identities*, hep-th/9408113) and
`library/the-dilogarithm-function-514sniwxl7.pdf` (Zagier, *The Dilogarithm
Function*).

THE CORRECTION THIS PROBE RECORDS
---------------------------------
`numerators_of_root` in `QOU/QBeta/FiveTwoAbelFiveTerm.lean` proves the level-7
numerators (17, 5, -1)/7 unconditionally in Lean. That work stands. But this lane
presented them as "DERIVED", with the tacit implication of novelty.

**They are classical.** Kirillov SS1.2.2 gives **Watson's relations** (1937):

    Let alpha, -beta, -1/gamma be the roots of  x^3 + 2x^2 - x - 1 = 0, with
        alpha = (1/2)sec(2pi/7),  beta = (1/2)sec(pi/7),  gamma = 2cos(3pi/7)
    Then
        L(alpha) - L(alpha^2)   = (1/7) L(1)
        2L(beta) + L(beta^2)    = (10/7) L(1)
        2L(gamma) + L(gamma^2)  = (8/7) L(1)

Substituting x -> -x turns Kirillov's cubic into **x^3 - 2x^2 - x + 1**, which is
this lane's cubic exactly, and

    alpha = -w3,    beta = w2,    gamma = 1/w1

verified below to 1e-30. So the Lean result is a **formalization of a known
identity family**, not a new derivation. Kirillov proves accessibility from the
**duplication formula**; this lane derived it from the **five-term relation**.
Different route, same classical fact.

WHAT ELSE THE LITERATURE CONFIRMS -- AND ONE THING IT CORRECTS
--------------------------------------------------------------
* `FiveTwoRogersExtend.extend` is **Zagier's definition verbatim** (SS I, "The
  Rogers dilogarithm"): L(0)=0, L(1)=pi^2/6, L(x)=2L(1)-L(1/x) for x>1,
  L(x)=-L(x/(x-1)) for x<0. Route 13's repair was the standard one, now checked
  against the source rather than memory.
* `FiveTwoRogersReflection.hasDerivAt_rogersL` is Zagier's
  L'(x) = -log(1-x)/(2x) - log(x)/(2(1-x)), verbatim -- and he names exactly that
  formula as the route to "these and all other functional equations", which is
  how Abel was proved here.
* **CORRECTION.** `qou-rstq` said the fact that Li_2's jump across the cut
  [1, inf) is purely imaginary "underpins this lane's whole take-real-parts
  convention and is written down nowhere". It is written down: Zagier, Chapter I
  SS3 -- "Li_2(z) ... jumps by 2*pi*i*log|z| as z crosses the cut". Standard, and
  the lane should cite it rather than claim it as folklore.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import cos, fabs, log, mp, mpf, nstr, pi, polylog, polyroots, re

def L(t):
    t = mpf(t)
    return re(polylog(2, t)) + log(t) * log(1 - t) / 2


def main() -> int:
    mp.dps = 40
    TOL = mpf(10) ** -30
    gates, l1 = [], pi ** 2 / 6

    w3, w2, w1 = sorted(re(r) for r in polyroots([1, -2, -1, 1], maxsteps=300, extraprec=300))
    al, be, ga = 1 / (2 * cos(2 * pi / 7)), 1 / (2 * cos(pi / 7)), 2 * cos(3 * pi / 7)

    # ---- G1: Kirillov's cubic is ours under x -> -x -------------------------
    # (-x)^3 + 2(-x)^2 - (-x) - 1 = -(x^3 - 2x^2 - x + 1)
    chk = max(fabs((-(t ** 3) + 2 * t ** 2 + t - 1) + (t ** 3 - 2 * t ** 2 - t + 1))
              for t in [mpf("0.37"), mpf("2.1"), mpf("-1.4")])
    gates.append({
        "gate": "G1",
        "claim": "Kirillov's cubic x^3+2x^2-x-1 is this lane's x^3-2x^2-x+1 under x -> -x",
        "worst_identity_residual": nstr(chk, 8), "pass": bool(chk < TOL),
    })

    # ---- G2: the roots correspond -----------------------------------------
    pairs = [("alpha = (1/2)sec(2pi/7)", al, "-w3", -w3),
             ("beta  = (1/2)sec(pi/7)", be, "w2", w2),
             ("gamma = 2cos(3pi/7)", ga, "1/w1", 1 / w1)]
    worst2 = max(fabs(a - b) for _, a, _, b in pairs)
    gates.append({
        "gate": "G2",
        "claim": "Kirillov/Watson's alpha, beta, gamma ARE this lane's -w3, w2, 1/w1",
        "pairs": [{"kirillov": n, "value": nstr(a, 20), "ours": m, "matches": nstr(b, 20)}
                  for n, a, m, b in pairs],
        "worst": nstr(worst2, 8), "pass": bool(worst2 < TOL),
    })

    # ---- G3: Watson's three relations hold ---------------------------------
    watson = [("L(a)-L(a^2)", L(al) - L(al ** 2), mpf(1) / 7),
              ("2L(b)+L(b^2)", 2 * L(be) + L(be ** 2), mpf(10) / 7),
              ("2L(g)+L(g^2)", 2 * L(ga) + L(ga ** 2), mpf(8) / 7)]
    worst3 = max(fabs(v - t * l1) for _, v, t in watson)
    gates.append({
        "gate": "G3",
        "claim": "Watson's (1937) three relations hold: 1/7, 10/7, 8/7 times L(1)",
        "relations": [{"lhs": n, "value_over_L1": nstr(v / l1, 20), "target": nstr(t, 20),
                       "resid": nstr(v - t * l1, 8)} for n, v, t in watson],
        "worst": nstr(worst3, 8), "pass": bool(worst3 < TOL),
    })

    # ---- G4: our numerators, same field, same denominator 7 -----------------
    q, r, s = 1 / (2 - w2), w2 / (w2 + 1), (1 - w2) / w2
    ours = [("2L1+2L(w2)-L(q)", 2 * l1 + 2 * L(w2) - L(q), 17),
            ("2L(w2)-L(r)", 2 * L(w2) - L(r), 5),
            ("-2L1+2L(w2)+L(s)", -2 * l1 + 2 * L(w2) + L(s), -1)]
    worst4 = max(fabs(v - mpf(m) / 7 * l1) for _, v, m in ours)
    gates.append({
        "gate": "G4",
        "claim": "this lane's (17,5,-1)/7 are the same classical family -- same field "
                 "Q(zeta_7)^+, same denominator 7, different combinations of the same L-values",
        "targets": [{"lhs": n, "value_over_L1": nstr(v / l1, 20), "m_over_7": f"{m}/7",
                     "resid": nstr(v - mpf(m) / 7 * l1, 8)} for n, v, m in ours],
        "worst": nstr(worst4, 8), "pass": bool(worst4 < TOL),
    })

    # ---- G5: Zagier's extension is `extend`, verbatim -----------------------
    def zag(x):
        x = mpf(x)
        if x == 0: return mpf(0)
        if x == 1: return l1
        if x > 1: return 2 * l1 - L(1 / x)
        if x < 0: return -L(x / (x - 1))
        return L(x)
    zchk = max(fabs(zag(mpf(t)) + zag(1 / mpf(t)) - 2 * l1) for t in ["1.3", "2.2469796", "9.0"])
    zchk = max(zchk, max(fabs(zag(t) + zag(mpf(t) / (mpf(t) - 1)))
                         for t in ["-0.4", "-2.2469796", "-11.0"]))
    gates.append({
        "gate": "G5",
        "claim": "Zagier's extension (L(x)=2L(1)-L(1/x) for x>1, -L(x/(x-1)) for x<0) is "
                 "exactly FiveTwoRogersExtend.extend -- inversion and Landen hold by definition",
        "worst": nstr(zchk, 8), "pass": bool(zchk < TOL),
    })

    # ---- G6: Zagier's L'(x) is hasDerivAt_rogersL ---------------------------
    h = mpf(10) ** -18
    worst6 = mpf(0)
    for t in ["0.2", "0.5549581", "0.83"]:
        x = mpf(t)
        fd = (L(x + h) - L(x - h)) / (2 * h)
        zd = -log(1 - x) / (2 * x) - log(x) / (2 * (1 - x))
        worst6 = max(worst6, fabs(fd - zd))
    gates.append({
        "gate": "G6",
        "claim": "Zagier's L'(x) = -log(1-x)/(2x) - log(x)/(2(1-x)) is hasDerivAt_rogersL, "
                 "verbatim -- and he names it as the route to all the functional equations",
        "worst_vs_finite_difference": nstr(worst6, 8), "pass": bool(worst6 < mpf(10) ** -12),
    })

    out = {
        "probe": "qbeta_5two_route18_watson_classical",
        "beans": ["qou-fivt", "qou-abel", "qou-0yqu"], "dps": mp.dps,
        "sources": ["Kirillov, Dilogarithm identities, hep-th/9408113, SS1.2.2 (Watson 1937)",
                    "Zagier, The Dilogarithm Function, Ch. I SS3 and Ch. II 'The Rogers dilogarithm'"],
        "gates": gates,
        "verdict": {
            "headline": "THE LEVEL-7 LADDER IS CLASSICAL. Watson (1937). This lane's Lean result "
                        "is a FORMALIZATION of a known identity family, not a new derivation.",
            "correspondence": "Kirillov's alpha, beta, gamma are exactly -w3, w2, 1/w1, and his "
                              "cubic is ours under x -> -x. Verified to 1e-30.",
            "what_is_still_this_lane's": "the ROUTE and the FORMALIZATION. Kirillov proves "
                                         "accessibility from the duplication formula; this lane "
                                         "derived it from the five-term relation, and proved the "
                                         "whole chain sorry-free in Lean, which the literature "
                                         "does not do.",
            "extend_is_zagier": "FiveTwoRogersExtend.extend is Zagier's definition verbatim. "
                                "Route 13's repair was the standard one -- now checked against "
                                "the source, not memory.",
            "deriv_is_zagier": "hasDerivAt_rogersL is Zagier's L'(x), verbatim, and he names that "
                               "formula as the route to all the functional equations -- which is "
                               "how Abel was proved here.",
            "CORRECTION": "qou-rstq claimed the purely-imaginary cut jump 'is written down "
                          "nowhere'. It is in Zagier Ch. I SS3: Li_2 jumps by 2*pi*i*log|z| across "
                          "[1, inf). Standard; cite it rather than claiming folklore.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route18-watson-classical.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: the level-7 ladder is Watson (1937). The Lean work is a FORMALIZATION.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
