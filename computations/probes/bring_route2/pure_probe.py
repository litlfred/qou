#!/usr/bin/env python3
"""Route 2, Part A of preregistration-pure.md (beans qou-99qc, qou-pzsi):
Bring loops for pure braids (all three Gamma_0(2) placements) and for 3-cycle braids via g^3.

No energy, no selection, and no Q_beta / CODATA / mass input. SL(2,Z) is exact; lengths use
mpmath at the 80 dps that bring_route2_probe sets.
"""
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bring_route2_probe as R2  # noqa: E402
import signed_candidates_probe as SC  # noqa: E402

DIG = 25


def place(g, p):
    h = R2.H_TO_INF[p]
    gp = R2.imul(R2.imul(h, g), R2.inv(h))
    out = {"point": str(p), "gamma0_2_rep": gp, "in_gamma0_2": gp[1][0] % 2 == 0}
    M = R2.to_h4(gp)
    hw = R2.rosen_word(M)
    r = R2.h4_5_order(M)
    s, u = R2.delta245()
    trd = R2.word_trace_delta(hw, s, u)
    out["r"] = r
    out["trace_delta245_abs"] = mp.nstr(abs(trd), DIG)
    if abs(trd) > 2 + mp.mpf(10) ** -25 and r:
        out["status"] = "loop"
        out["L"] = r * 2 * mp.acosh(abs(trd) / 2)
    else:
        out["status"] = "no loop: elliptic or parabolic in Delta(2,4,5)"
    return out


def fixed_points(g):
    return [p for p in ("inf", 0, 1) if R2.act_p1f2(g, p) == p]


def assess(g):
    fx = fixed_points(g)
    res = {"sl2z": g, "trace": g[0][0] + g[1][1], "p1f2_fixed": [str(p) for p in fx]}
    if len(fx) == 1:
        pl = place(g, fx[0])
        res.update(rule="one fixed point (route 2 unchanged)", placements=[pl],
                   verdict=pl["status"], L=pl.get("L"))
        return res
    if len(fx) == 3:
        pls = [place(g, p) for p in ("inf", 0, 1)]
        Ls = [mp.nstr(x["L"], DIG) if x["status"] == "loop" else None for x in pls]
        res["placements"] = pls
        res["rule"] = "pure: A1/A2"
        if all(v is not None for v in Ls) and len(set(Ls)) == 1:
            res["verdict"], res["L"] = "loop", pls[0]["L"]
        else:
            res["verdict"], res["L"] = "ambiguous", None
        return res
    g3 = R2.imul(R2.imul(g, g), g)
    sub = assess(g3)
    res.update(rule="3-cycle: A3 via g^3", g_cubed=sub, verdict=sub["verdict"], L_of_g_cubed=sub.get("L"),
               L_of_g_cubed_over_3=(sub["L"] / 3 if sub.get("L") is not None else None))
    return res


def ser(x):
    if isinstance(x, mp.mpf):
        return mp.nstr(x, DIG)
    if isinstance(x, dict):
        return {k: ser(v) for k, v in x.items()}
    if isinstance(x, list):
        return [ser(v) for v in x]
    return x


def main():
    V = [(0, 1), (1, -1)]
    gg = {k: assess(SC.image(V * k)) for k in range(1, 7)}
    checks = {}
    # check 2: all pure placements in Gamma_0(2)
    ok = True
    for r in list(gg.values()) + [r["g_cubed"] for r in gg.values() if "g_cubed" in r]:
        ok &= all(p["in_gamma0_2"] for p in r.get("placements", []))
    checks["pure_placements_in_gamma0_2"] = ok
    # check 3: A3 consistency, g^3 of (V^k) equals direct V^{3k}
    cons = True
    for k in (1, 2, 4, 5):
        direct = assess(SC.image(V * (3 * k)))
        a = gg[k]["L_of_g_cubed"]
        b = direct.get("L")
        cons &= (gg[k]["verdict"] == direct["verdict"]) and (
            (a is None and b is None) or (a is not None and b is not None and mp.nstr(a, DIG) == mp.nstr(b, DIG)))
    checks["A3_cube_equals_direct_3k"] = cons
    # check 1: regression on the 8 nucleon terms
    stored = json.loads((HERE / "results_signed.json").read_text())["proton_terms"]
    reg = True
    nuc = {}
    for key, w in {**SC.proton_terms(), **SC.neutron_terms()}.items():
                r = assess(SC.image(w))
                nuc[key] = r
                st = stored[key]
                reg &= (r["verdict"] == "loop") == (st["status"] == "loop")
                if st["status"] == "loop":
                    reg &= mp.nstr(r["L"], DIG) == st["L"]
    checks["nucleon_terms_reproduce_results_signed"] = reg
    out = {"recipe": "preregistration-pure.md Part A", "gamma_gamma": {f"(s0 s1^-1)^{k}": v for k, v in gg.items()},
           "nucleon_terms": nuc, "checks": checks}
    out = ser(out)
    for k, v in out["gamma_gamma"].items():
        print(k, v["trace"], v["rule"], v["verdict"], v.get("L") or v.get("L_of_g_cubed"),
              [(p["point"], p["status"], p.get("L")) for p in (v.get("placements") or v["g_cubed"]["placements"])])
    print(json.dumps(checks))
    (HERE / "results_pure.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
