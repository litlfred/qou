#!/usr/bin/env python3
"""Which quark tails does γγ + reading 3 admit?  Pre-registration: preregistration.md (5ad34aec2).

Space: CORE·T·G, CORE = V³, V = σ0σ1⁻¹, T = 3 letters from A = {σ_g, σ_g⁻¹, σ_g − h/2 : g = 0,1},
G ∈ {V, σ0²}.  Reading 3 at H3, convention D, proton pin.  Exact sympy over Q(q); the pin is an
exact rational; mpmath only for display.  Formulas imported from gg_gluon_segment_probe.py.
Nothing is ranked by Q_β or data; no survivor is labelled p or n.
"""
from __future__ import annotations
import importlib.util, itertools, json, os, random, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "_gg", os.path.join(HERE, "..", "gg_gluon_segment", "gg_gluon_segment_probe.py"))
G_ = importlib.util.module_from_spec(spec); spec.loader.exec_module(G_)
q, Q0, U, D, UD, h = G_.q, G_.Q0, G_.U, G_.D, G_.UD, G_.h
V, CORE, TAIL = G_.V, G_.CORE, G_.TAIL

ALPHA = {"s0": U(0), "s0i": D(0), "a0": UD(0), "s1": U(1), "s1i": D(1), "a1": UD(1)}
NAMES = list(ALPHA)
GLUONS = {"V": V, "s0^2": G_.SIGMA0_PAIR}
CHECKS = []
def check(n, ok, d=""):
    CHECKS.append((n, bool(ok), d)); print(f"  [{'PASS' if ok else 'FAIL'}] {n} {d}"); return ok

def _split(name):  # "s0" -> ("s", "0", ""), "s0i" -> ("s", "0", "i"), "a1" -> ("a", "1", "")
    return name[0], name[1], name[2:]
def phi(name):  # generator flip σ0 <-> σ1
    k, g, i = _split(name); return k + ("1" if g == "0" else "0") + i
def barn(name):  # letter-wise bar: σ <-> σ⁻¹, average fixed
    k, g, i = _split(name)
    return name if k == "a" else k + g + ("" if i else "i")

def chi_pair(letters):
    return G_.chi3(letters), G_.chi21(letters)

def roots_above_1(expr):
    num = sp.numer(sp.together(expr))
    P = sp.Poly(sp.expand(num), q)
    return [r for r in P.real_roots() if r > 1]

def main():
    print("Calibration")
    tgt = {("s0^2", "p"): "-0.2805933509", ("s0^2", "n"): "-0.3719563247",
           ("V", "p"): "0.2170281485", ("V", "n"): "0.4294149854"}
    for (g, x), want in tgt.items():
        v = G_.at_q0(G_.chi21(CORE + TAIL[x] + GLUONS[g]))
        check(f"C{1 if g == 's0^2' else 2}_{g}_{x}", G_.s(v, 10) == want, f"{G_.s(v, 10)} vs {want}")
    rng = random.Random(0)
    sample = [tuple(rng.choice(NAMES) for _ in range(3)) for _ in range(20)]
    ok = all(G_.zero(G_.chi21(CORE + [ALPHA[n] for n in t] + V) -
                     G_.chi21_matrix(CORE + [ALPHA[n] for n in t] + V)) for t in sample)
    check("C3_seminormal_matches_trace_20_words", ok)
    if not all(c[1] for c in CHECKS):
        print("calibration failed; no results reported"); return 1

    rows = []
    for g, gl in GLUONS.items():
        for t in itertools.product(NAMES, repeat=3):
            w = CORE + [ALPHA[n] for n in t] + gl
            c3, c21 = chi_pair(w)
            v3, v21 = G_.at_q0(c3), G_.at_q0(c21)
            rows.append({"gluon": g, "tail": list(t), "chi3_q0": G_.s(v3, 12), "chi21_q0": G_.s(v21, 12),
                         "pass": bool(v3 >= 0 and v21 >= 0), "_c21": c21})
    out = {"checks": [list(c) for c in CHECKS], "gluons": {}}
    census = {tuple(["s0", "a0", "a1"]): "TAIL_p", tuple(["a0", "a0", "s1i"]): "TAIL_n"}
    for g in GLUONS:
        R = [r for r in rows if r["gluon"] == g]
        S = [r for r in R if r["pass"]]
        Sset = {tuple(r["tail"]) for r in S}
        for r in S:
            r["roots_chi21_above_1"] = [G_.s(sp.N(x, 30), 10) for x in roots_above_1(r["_c21"])]
        info = {"n_tails": len(R), "n_survivors": len(S),
                "census": {v: (k in Sset) for k, v in census.items()},
                "phi_closed": all(tuple(phi(n) for n in t) in Sset for t in Sset),
                "bar_closed": all(tuple(barn(n) for n in t) in Sset for t in Sset),
                "survivors": [{k: v for k, v in r.items() if k != "_c21"} for r in S]}
        out["gluons"][g] = info
        print(f"\nGluon {g}: {len(S)} / {len(R)} tails pass reading 3 at q0; census {info['census']};"
              f" phi-closed {info['phi_closed']}, bar-closed {info['bar_closed']}")
    with open(os.path.join(HERE, "gg-quark-tail.witness.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    return 0

if __name__ == "__main__":
    sys.exit(main())
