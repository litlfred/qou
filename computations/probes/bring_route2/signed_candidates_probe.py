#!/usr/bin/env python3
"""Route 2 correction (beans qou-99qc, qou-pzsi): the seen candidates WITH their signs.

Route 2 and options 1-1d took the seen candidates from
`qbeta_candidate_closures_are_links_probe.CANDIDATES`. That list is a generator
sequence with the signs erased; it is legitimate there, because that probe needs only
the strand permutation. Under route 2 the sign matters: sigma_1^-1 maps to L^-1, not L.

The canonical nucleon (`pyhecke.atom.build_nucleon_nf`) is, for the proton,
    (s0 s1^-1)^3 . s0 [uu] . (s0 + s0^-1)/2 [ud] . (s1 + s1^-1)/2 [ud] . s0 s0 [gluon]
For the neutron (udd) the pairs (0,1) and (0,2) are ud and (1,2) is dd, so the element is
    (s0 s1^-1)^3 . (s0 + s0^-1)/2 [ud] . (s0 + s0^-1)/2 [ud] . s1^-1 [dd] . s0 s0 [gluon].
CORRECTED 2026-10-11: this probe first used "uu -> dd" for the neutron, i.e.
s0^-1 . avg(s0) . avg(s1), which is not what the builder computes (max NF deviation 0.111).
The check `expansion_reproduces_builder_*` now verifies each expansion against
`pyhecke.atom.build_nucleon_nf_mp` in H_3(q0). The ud letters are averages, so each element is a sum of FOUR braids. This probe reports
route 2 for each of the four (eight, both nucleons), for the sign-erased word route 2 actually used, and for
the gamma-gamma words (s0 s1^-1)^k. No energy, no selection, and no Q_beta / CODATA /
mass input. SL(2,Z) is exact (int); the Bring length uses mpmath (80 dps, set by R2).
"""
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bring_route2_probe as R2  # noqa: E402

ROOT = HERE.parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python", "computations", "computations/substrate"):
    sys.path.insert(0, str(ROOT / _p))

CORE = [(0, 1), (1, -1)] * 3
GLUON = [(0, 1), (0, 1)]


def proton_terms():
    return {f"proton term s0^{a:+d} s1^{b:+d}": CORE + [(0, 1), (0, a), (1, b)] + GLUON
            for a in (1, -1) for b in (1, -1)}


def neutron_terms():
    return {f"neutron term s0^{a:+d} s0^{b:+d}": CORE + [(0, a), (0, b), (1, -1)] + GLUON
            for a in (1, -1) for b in (1, -1)}


def expansion_matches_builder(terms, quarks, dps=50):
    """Sum of the four braids, each weight 1/4, in H_3(q0) == build_nucleon_nf_mp(quarks)."""
    from pyhecke import atom as A
    from pyhecke import gram
    with mp.workdps(dps):
        h = gram.h_mp(dps)
        one, zero = mp.mpf(1), mp.mpf(0)
        tot = [zero] * 6
        for w in terms.values():
            nf = [one, zero, zero, zero, zero, zero]
            for g, e in w:
                nf = A.hm_mp(nf, one, zero if e == 1 else -h, g, dps)
            tot = [x + y / 4 for x, y in zip(tot, nf)]
        ref = A.build_nucleon_nf_mp(list(quarks), dps)
        dev = max(abs(x - y) for x, y in zip(tot, ref))
        return dev < mp.mpf(10) ** (-(dps - 10)), mp.nstr(dev, 5)

GEN = {(0, 1): [[1, 1], [0, 1]], (0, -1): [[1, -1], [0, 1]],
       (1, 1): [[1, 0], [-1, 1]], (1, -1): [[1, 0], [1, 1]]}


def image(w):
    M = [[1, 0], [0, 1]]
    for x in w:
        M = R2.imul(M, GEN[x])
    return M


def row(w):
    g = image(w)
    fx = [p for p in ("inf", 0, 1) if R2.act_p1f2(g, p) == p]
    out = {"word": [f"s{a}^{e:+d}" for a, e in w], "sl2z": g, "trace": g[0][0] + g[1][1],
           "p1f2_fixed": [str(p) for p in fx]}
    if len(fx) != 1:
        out["status"] = "no loop: permutation does not fix exactly one point (route 2 rule)"
        return out
    h = R2.H_TO_INF[fx[0]]
    gp = R2.imul(R2.imul(h, g), R2.inv(h))
    M = R2.to_h4(gp)
    hw = R2.rosen_word(M)
    r = R2.h4_5_order(M)
    s, u = R2.delta245()
    trd = R2.word_trace_delta(hw, s, u)
    if abs(trd) > 2 + mp.mpf(10) ** -25 and r:
        out["status"] = "loop"
        out["L"] = mp.nstr(r * 2 * mp.acosh(abs(trd) / 2), 25)
    else:
        out["status"] = "no loop: elliptic or parabolic in Delta(2,4,5)"
    return out


def main():
    pt, nt = proton_terms(), neutron_terms()
    terms = {k: row(w) for k, w in {**pt, **nt}.items()}
    okp, devp = expansion_matches_builder(pt, "uud")
    okn, devn = expansion_matches_builder(nt, "udd")
    shadow = row([(x, 1) for x in [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]])
    gg = {f"(s0 s1^-1)^{k}": row([(0, 1), (1, -1)] * k) for k in range(1, 7)}
    checks = {
        "vertex_image_is_[[2,1],[1,1]]": image([(0, 1), (1, -1)]) == [[2, 1], [1, 1]],
        "shadow_reproduces_route2_nuc11_image": shadow["sl2z"] == R2.sl2z(R2.CANDIDATES["nuc11_interleaved"]),
        "all_four_proton_terms_have_a_loop": all(t["status"] == "loop" for k, t in terms.items() if k.startswith("proton")),
        "expansion_reproduces_builder_proton": okp,
        "expansion_reproduces_builder_neutron": okn,
        "no_gamma_gamma_word_gets_a_loop_under_route2_rule": all(t["status"] != "loop" for t in gg.values()),
    }
    out = {"proton_terms": terms, "sign_erased_nuc11_used_by_route2": shadow,
           "gamma_gamma_words": gg, "checks": checks,
           "builder_max_deviation": {"proton": devp, "neutron": devn},
           "neutron_terms_with_a_loop": sum(t["status"] == "loop" for k, t in terms.items() if k.startswith("neutron"))}
    print(json.dumps(out, indent=1, default=str))
    (HERE / "results_signed.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
