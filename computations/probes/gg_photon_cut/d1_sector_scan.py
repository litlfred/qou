#!/usr/bin/env python3
"""d1_sector_scan.py — D1 scan, specialised q (generic-Q(q) Groebner timed out; deviation recorded in bean).

For each free-reduced word w (1..MAXC crossings) and each q in QS (exact rationals), decide by Groebner bases
over QQ whether gamma(phi)gamma(psi) = c w (c != 0) has a solution
  IN:  with phi0 = phi1 = psi0 = psi1 = 0 (the phi01-psi01 sector, the V-only grammar), and
  OUT: with (phi0, phi1, psi0, psi1) != 0 (tested by two random linear forms L != 0).
-- Ref: [leitner2026] bean qou-99qc (PRE-REGISTRATION 2026-11-21 12:25Z)
"""
import json
import sys
import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("m", HERE / "two_photon_multiple_words_probe.py")
m = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0]] + sys.argv[1:2]
spec.loader.exec_module(m)

MAXC = int(sys.argv[1]) if len(sys.argv) > 1 else 6
QS = [sp.Integer(2), sp.Rational(3, 2)]
T, T2 = sp.symbols("t t2")
FORMS = [(3, 7, 11, 13), (5, -2, 17, 1)]


def consistent(eqs, extra_vars=()):
    G = sp.groebner(eqs, *m.UNK, T, *extra_vars, order="grevlex")
    return list(G.exprs) != [1]


def base_eqs(w, qv):
    W = m.word_elem(list(w))
    eqs = [sp.numer(sp.together(sp.expand((m.GG.get(u, 0) - m.c * W.get(u, 0)).subs(m.q, qv)))) for u in m.PERMS]
    return [e for e in eqs if e != 0] + [m.c * T - 1]


def main():
    rows = []
    ws = m.words(MAXC)
    extra = [((0, 1), (1, -1)) * 3, ((0, 1), (1, -1)) * 2]
    ws = ws + [w for w in extra if w not in ws]
    for i, w in enumerate(ws):
        r = {"word": m.show(w), "crossings": len(w), "writhe": sum(e for _, e in w), "components": m.components(w)}
        for qv in QS:
            E = base_eqs(w, qv)
            inn = consistent(E + [m.p0, m.p1, m.s0_, m.s1_])
            out = any(consistent(E + [T2 * (a * m.p0 + b * m.p1 + cc * m.s0_ + d * m.s1_) - 1], (T2,))
                      for a, b, cc, d in FORMS[:1])
            r[f"q={qv}"] = {"in_sector": inn, "out_of_sector": out}
        if any(v["in_sector"] or v["out_of_sector"] for k, v in r.items() if k.startswith("q=")):
            rows.append(r)
            print(json.dumps(r), flush=True)
        if i % 100 == 0:
            print(f"  {i}/{len(ws)}", flush=True)
    Path(HERE / f"d1-sector-scan-{MAXC}.json").write_text(json.dumps({"max_crossings": MAXC, "q_values": [str(x) for x in QS],
                                                                     "words_tested": len(ws), "hits": rows}, indent=1))
    print("tested", len(ws), "hits", len(rows))


if __name__ == "__main__":
    main()
