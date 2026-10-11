#!/usr/bin/env python3
"""Route 2: is the gamma-gamma core's Bring loop the same loop as that of the positive 11-letter
braid 00001100011 (equal length to 25 digits, results_pure.md section 2)? Do the three placements
of the core give one loop?

Applies the same-loop rule of preregistration-sameloop.md section 2 unchanged (sameloop_probe.isometric).
No energy, no selection, and no Q_beta / CODATA / mass input.
"""
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bring_route2_probe as R2  # noqa: E402
import bring_loop_energy_probe as E  # noqa: E402
import option1_ropelength_probe as O1  # noqa: E402
import sameloop_probe as SL  # noqa: E402
import signed_candidates_probe as SC  # noqa: E402


def row_for(g, p):
    h = R2.H_TO_INF[p]
    gp = R2.imul(R2.imul(h, g), R2.inv(h))
    M = R2.to_h4(gp)
    return {"h4_word": [list(x) for x in R2.rosen_word(M)], "r_congruence_H4(5)": R2.h4_5_order(M)}


def main():
    s_mp, u_mp = R2.delta245()
    s, u = E.from_mp(s_mp), E.from_mp(u_mp)
    rho, sigmas = R2.s5_epimorphisms()
    core = SC.image([(0, 1), (1, -1)] * 3)
    geo, Ls = {}, {}
    for p in ("inf", 0, 1):
        st = E.loop_setup(f"core@{p}", s_mp, u_mp, sigmas[0], rho, row=row_for(core, p))
        geo[f"core@{p}"] = SL.geometry(st)
        Ls[f"core@{p}"] = st["L"]
    rr = O1.route2_row(tuple(int(c) for c in "00001100011"))
    st = E.loop_setup("w11", s_mp, u_mp, sigmas[0], rho, row=rr)
    geo["00001100011"] = SL.geometry(st)
    Ls["00001100011"] = st["L"]
    ref = "core@inf"
    res = {}
    for k in geo:
        if k == ref:
            continue
        orient, g, n = SL.isometric(geo[ref], geo[k], Ls[ref], s, u)
        res[k] = {"same_loop": orient is not None, "orientation": orient, "nodes_searched": n}
    out = {"lengths": {k: mp.nstr(v, 25) for k, v in Ls.items()}, "vs_core@inf": res}
    print(json.dumps(out, indent=1, default=str))
    (HERE / "results_core_sameloop.json").write_text(json.dumps(out, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
