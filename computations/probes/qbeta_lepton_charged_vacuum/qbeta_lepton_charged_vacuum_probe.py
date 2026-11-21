#!/usr/bin/env python3
"""Lepton pair on 5 strands (charged vacuum, option 1) vs the window; see PREREGISTRATION.md.

Exact Laurent arithmetic reused from ../qbeta_lepton_linked_exact (Jimbo R, K = diag(q, 1/q)).
"""
import importlib.util
import itertools
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "_lx", HERE.parent / "qbeta_lepton_linked_exact" / "qbeta_lepton_linked_exact_probe.py")
lx = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lx)

mp.mp.dps = 50
Q0 = mp.mpf("1.1099785827513808")  # proton pin (qou_substrate.constants.Q), display only
N = 8


def parse(w):
    return [int(s) for s in w.split("V")[1:]]


def perm_identity(vs):
    pos = list(range(N))
    for i in vs:
        for j in (i, i + 1):
            pos[j], pos[j + 1] = pos[j + 1], pos[j]
    return pos == list(range(N))


def main():
    q, t = sp.symbols("q", positive=True), sp.symbols("t")
    P = q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1
    D2 = q + 1/q
    eP = q*(-P/q**6)/D2**3
    eN = eP/q**2
    fE = (q**4 + 1)/(q**4*(q**2 + 1))
    beta = lx.gg_word((0, 0, 0))
    obs = lambda b: bin(b >> 5).count("1") == 1  # noqa: E731  nucleon strands 0-2, one d
    juncs = [vs for L in range(7) for vs in itertools.product((1, 2), repeat=L)
             if perm_identity(vs)]
    leps = json.load(open(HERE / "lepton_words_5strand.json"))["words"]
    cache, rows, fac_ok = {}, [], True
    for lw in leps:
        L = [(i + 3, s) for (i, s) in lx.gg_word(parse(lw["word"]))]
        for X in juncs:
            W = lx.gg_word(X) + beta + L
            assert sum(s for _, s in W) == 0
            T = lx.obs_trace(W, N, obs)
            key = tuple(sorted(T.d.items()))
            if key not in cache:
                x = sum(v * q**k for k, v in T.d.items()) / D2**6
                cache[key] = x
            x = cache[key]
            if not X:
                f = fE if lw["kind"] == "e-nubar" else q**6*fE  # fM = q^6 fE (mirror)
                fac_ok &= sp.simplify(x - eP*f) == 0
            rows.append({"lepton": lw["word"], "kind": lw["kind"], "lepton_vertices": lw["vertices"],
                         "junction": "".join(f"V{i}" for i in X), "key": key})
    print(f"words {len(rows)} ({len(leps)} lepton x {len(juncs)} junction); "
          f"distinct values {len(cache)}; unlinked = eps_p*fE (e-nubar), eps_p*fM (mirror) exactly: {fac_ok}")
    verdict = {}
    for key, x in cache.items():
        kinds = {r["kind"] for r in rows if r["key"] == key}
        out = {}
        for kind in kinds:
            g = sp.together(eN - x) if kind == "e-nubar" else sp.together(x - eP)
            num = sp.fraction(sp.factor(g))[0]
            poly = sp.Poly(sp.expand(num.subs(q, 1 + t)), t)
            rts = sorted(r for r in sp.real_roots(poly) if 0 < r <= sp.Rational(3, 20))
            mid = sp.sign(g.subs(q, sp.Rational(21, 20)))
            out[kind] = {"outside_all": bool(len(rts) == 0 and mid > 0),
                         "roots_q": [mp.nstr(1 + mp.mpf(sp.N(r, 40)), 15) for r in rts],
                         "sign_at_21/20": int(mid)}
        edges = {}
        for nm, g in (("x_minus_eps_n", x - eN), ("eps_p_minus_x", eP - x)):
            num = sp.fraction(sp.factor(sp.together(g)))[0]
            poly = sp.Poly(sp.expand(num.subs(q, 1 + t)), t)
            rts = sorted(r for r in sp.real_roots(poly) if 0 < r <= sp.Rational(3, 20))
            edges[nm] = {"roots_q": [mp.nstr(1 + mp.mpf(sp.N(r, 40)), 15) for r in rts],
                         "sign_at_21/20": int(sp.sign(g.subs(q, sp.Rational(21, 20))))}
        xq0 = sp.lambdify(q, [x, eN, eP], "mpmath")(Q0)
        for kind in out:
            out[kind]["window_edges"] = edges
            out[kind]["in_window_at_q0"] = bool(xq0[1] < xq0[0] < xq0[2])
        verdict[key] = {"x_q1": str(sp.limit(x, q, 1)),
                        "x_q0": mp.nstr(sp.lambdify(q, x, "mpmath")(Q0), 15), **{"tests": out}}
    for r in rows:
        v = verdict[r.pop("key")]
        r.update({"x_at_q1": v["x_q1"], "x_q0": v["x_q0"], **v["tests"][r["kind"]]})
    for sub, cut in (("all (<= 6 vertices)", 6), ("<= 5 vertices", 5)):
        rs = [r for r in rows if r["lepton_vertices"] <= cut]
        for kind in ("e-nubar", "mirror"):
            k = [r for r in rs if r["kind"] == kind]
            xs = [mp.mpf(r["x_q0"]) for r in k]
            bad = [r for r in k if not r["outside_all"]]
            print(f"{sub} {kind}: {len(k)} words, x(q0) in [{mp.nstr(min(xs), 6)}, "
                  f"{mp.nstr(max(xs), 6)}], enter window somewhere: {len(bad)}")
            for r in bad:
                print("   ", r)
    print("x(1) values:", sorted({r["x_at_q1"] for r in rows}))
    inq0 = [r for r in rows if r["in_window_at_q0"]]
    print(f"in the window at q0: {len(inq0)} words")
    for r in inq0:
        print("   ", r["kind"], r["lepton"], r["junction"], r["x_q0"], r["window_edges"])
    eb = all(r["outside_all"] for r in rows if r["kind"] == "e-nubar")
    mb = [r for r in rows if r["kind"] == "mirror" and not r["outside_all"]]
    out = {"description": "Lepton pair e- + nu-bar on 5 strands (charged vacuum, option 1): "
                          "x_hat = Tr(K^8 (P_p x 1) rho(X beta_Bor L))/[2]^6 vs (eps_n, eps_p) "
                          "on all q in (1, 23/20]. Exact Laurent arithmetic; exact root isolation.",
           "q0Anchor": "proton", "junctions": ["".join(f"V{i}" for i in X) for X in juncs],
           "rows": rows,
           "summary": {"words": len(rows), "distinct_values": len(cache),
                       "unlinked_equal_eps_p_fE": bool(fac_ok),
                       "e_nubar_all_outside": bool(eb), "mirror_words_entering_window": len(mb),
                       "words_in_window_at_q0": [[r["kind"], r["lepton"], r["junction"]] for r in inq0]}}
    (HERE / "qbeta-lepton-charged-vacuum.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    return 0 if fac_ok else 1


if __name__ == "__main__":
    sys.exit(main())
