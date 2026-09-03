#!/usr/bin/env python3
"""t7qv Gap #3 (A=3 mirror): the quoted "best structural 2.52 %" is a menu min.

Bean t7qv lists "Gap #3: A=3 mirror magnitude (3H/3He; best structural 2.52 %)".
This probe audits that number, because the corpus already contains its own
verdict on it and the bean's phrasing does not carry it.

FINDING 1: the 2.52 % is a SELECTION, and the corpus says so
--------------------------------------------------------------
docs/audits/2026-05-31-option-e-kashiwara-refresh-assessment.md:

    v9 | "all symmetries" on top of v8 | T-3He diff only |
       m_pi.hbar_q.(1+hbar_q).M_asym = +2.52 % |
       9 scales x 9 inputs (81 candidates) + explicit back-solve

    ... FITTED + BACK-SOLVED. This is the PR #1578 (1+q)/2 antipattern verbatim
    ... The 81-candidate menu min (+2.52 %) is also a fit.

So the headline is the minimum over an 81-candidate menu, and the published
0.11 % beside it is an explicit back-solve. Neither is parameter-free.

FINDING 2: the parameter-free number is 2.899 %, so the menu bought 13 %
-------------------------------------------------------------------------
From the corpus's own four-point table
(docs/audits/2026-08-08-volume-binding-four-point-is-unrunnable.md), both A = 3
targets ARE usable, so the ratio test runs with zero free parameters:

    B(3H)/B(3He)          = 8.4817962 / 7.71804132   = 1.09895709
    Vol(8_11)/Vol(L6a4)   = 8.286316818 / 7.327724753 = 1.13081715
    discrepancy                                        = 2.899 %

Against that, the 81-candidate menu min of 2.52 % is a 13 % reduction in the
error. That is what 81 degrees of selection freedom bought.

FINDING 3: and 2.52 % from 81 candidates is expected, not surprising
----------------------------------------------------------------------
With N independent candidates each landing inside the tolerance with
probability p, P(the best one does) >= 1 - exp(-N p)
(QOU.MathlibExt.SelectionBound.menu_min_prob_ge, sorry-free). For N = 81 and
candidate errors uniform on [0, R]:

    R = 0.25 -> P = 0.9998     R = 1.0 -> P = 0.873
    R = 0.50 -> P = 0.985      R = 2.0 -> P = 0.642

Even granting candidate errors spread over a full 100 %, a menu min at or below
2.52 % arrives by chance seven times in eight. It is not evidence for the
structure that produced it.

FINDING 4: what the mirror splitting actually is
--------------------------------------------------
dB = B(3H) - B(3He) = 0.76375 MeV, and the naive Coulomb estimate
(3/5) Z(Z-1) e^2 / R for 3He gives 0.82-1.02 MeV over R = 1.7-2.1 fm, i.e.
dB/E_C = 0.75-0.93. The splitting is three-quarters to fully accounted for by
Coulomb alone. A charge-BLIND topological ratio therefore has almost nothing
left to explain, and conversely any structural account must reproduce a
Coulomb-sized effect; in this model the only charge dependence enters through
the link assignment (8_11 vs L6a4), which comes from the braid word.

CONSEQUENCE FOR THE BEAN. Gap #3 is WIDER than recorded, not narrower: the
honest parameter-free figure is 2.899 %, and the 2.52 % beside it should not be
quoted as a structural result.
"""
import json
import time
from pathlib import Path

from mpmath import mp, mpf, nstr

mp.dps = 30


def main():
    t0 = time.monotonic_ns()
    checks = []
    B_T = mpf("8.4817962"); V_T = mpf("8.286316818")
    B_He = mpf("7.71804132"); V_He = mpf("7.327724753")
    ratio_B = B_T / B_He
    ratio_V = V_T / V_He
    disc = ratio_V / ratio_B - 1
    menu = mpf("0.0252")
    checks.append({
        "name": "FINDING 2: parameter-free discrepancy is 2.899 %, menu min bought 13 %",
        "pass": abs(disc) > menu,
        "detail": (
            f"Both A = 3 targets are usable in the corpus four-point table, so "
            f"the ratio test runs with ZERO free parameters: "
            f"B(3H)/B(3He) = {nstr(ratio_B, 9)}, Vol(8_11)/Vol(L6a4) = "
            f"{nstr(ratio_V, 9)}, discrepancy = {nstr(100 * disc, 5)} %. The "
            f"bean's quoted 'best structural 2.52 %' is smaller by a factor "
            f"{nstr(abs(disc) / menu, 4)}, i.e. the 81-candidate menu reduced "
            f"the error by {nstr(100 * (1 - menu / abs(disc)), 3)} % -- that is "
            f"what 81 degrees of selection freedom bought."),
    })
    rows = []
    for R in ("0.25", "0.5", "1.0", "2.0"):
        Rr = mpf(R)
        p = menu / Rr
        exact = 1 - (1 - p) ** 81
        bound = 1 - mp.exp(-(81 * p))
        rows.append({"R": R, "p": nstr(p, 5), "P_exact": nstr(exact, 5),
                     "P_lower_bound": nstr(bound, 5)})
    checks.append({
        "name": "FINDING 3: a 2.52 % menu min from 81 candidates is EXPECTED",
        "pass": all(mpf(r["P_exact"]) >= mpf(r["P_lower_bound"]) for r in rows)
                and mpf(rows[2]["P_exact"]) > mpf(8) / 10,
        "detail": (
            f"With N candidates each inside tolerance with probability p, "
            f"P(best one is) >= 1 - exp(-N p) -- QOU.MathlibExt.SelectionBound."
            f"menu_min_prob_ge, sorry-free on [propext, Classical.choice, "
            f"Quot.sound]. For N = 81 and candidate errors uniform on [0, R]: "
            + "; ".join(f"R = {r['R']} -> P = {r['P_exact']}" for r in rows)
            + f". CONTROL: the closed-form P and the exponential lower bound "
            f"agree in order at every R, with the bound below the exact value "
            f"as it must be. Even granting errors spread over a full 100 %, a "
            f"menu min at or below 2.52 % arrives by chance seven times in "
            f"eight, so it is not evidence for the structure that produced it."),
    })
    dB = B_T - B_He
    coul = []
    for R in ("1.7", "1.9", "2.1"):
        Ec = (mpf(3) / 5) * 2 * 1 * mpf("1.43996") / mpf(R)
        coul.append({"R_fm": R, "E_C_MeV": nstr(Ec, 5),
                     "dB_over_EC": nstr(dB / Ec, 4)})
    checks.append({
        "name": "FINDING 4: the mirror splitting is 75-93 % naive Coulomb",
        "pass": all(mpf(1) / 2 < mpf(c["dB_over_EC"]) < 1 for c in coul),
        "detail": (
            f"dB = B(3H) - B(3He) = {nstr(dB, 8)} MeV. Naive Coulomb "
            f"(3/5) Z(Z-1) e^2 / R for 3He, with e^2 = 1.43996 MeV.fm: "
            + "; ".join(f"R = {c['R_fm']} fm -> {c['E_C_MeV']} MeV, "
                        f"dB/E_C = {c['dB_over_EC']}" for c in coul)
            + ". So Coulomb alone accounts for three-quarters to all of the "
            "splitting. A charge-BLIND topological ratio has almost nothing "
            "left to explain; conversely any structural account must reproduce "
            "a Coulomb-sized effect, and here the only charge dependence enters "
            "through the link assignment (8_11 vs L6a4) from the braid word."),
    })
    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("a3-mirror-selection.witness.json").write_text(
        json.dumps({
        "q0Anchor": "independent",
        "q0AnchorReason": "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: t7qv Gap #3 (A=3 mirror): the quoted \"best structural 2.52 %\" is a menu min.",
            "probe": "a3_mirror_selection", "bean": ["t7qv"],
            "lean": "QOU.MathlibExt.SelectionBound",
            "ratio_B": nstr(ratio_B, 12), "ratio_V": nstr(ratio_V, 12),
            "discrepancy_pct": nstr(100 * disc, 8),
            "menu_min_pct": "2.52", "selection": rows, "coulomb": coul,
            "checks": checks, "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: Gap #3 is WIDER than the bean records. The parameter-free figure")
    print("RESULT:   is 2.899 %; the 2.52 % beside it is an 81-candidate menu min,")
    print("RESULT:   reproducible by chance ~7 times in 8, and the corpus already")
    print("RESULT:   calls it a fit. It should not be quoted as structural.")
    print("RESULT: gap t7qv #3 stays OPEN.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
