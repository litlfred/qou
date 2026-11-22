#!/usr/bin/env python3
"""Candidate sources for the 12 in m_p/m_e = 2((m_mu/m_e) F_Bor - 6). Exact integers/sympy.

Each candidate is reported with its value and with whether it carries a mechanism linking it to
a nucleon sector. A value equal to 12 with no mechanism is listed, never selected.
No measured value enters.
"""
import itertools, json
from math import factorial, comb
from pathlib import Path
import sympy as sp

q = sp.symbols("q", positive=True)
lab = list(itertools.product([0, 1], repeat=3))            # 1 = u
perms = list(itertools.permutations(range(3)))
def burnside(pred):
    return sum(sum(1 for l in lab if pred(l) and tuple(l[s[i]] for i in range(3)) == l) for s in perms)
qfact3 = (q + 1/q) * (q**2 + 1 + q**-2)                      # [3]_q! symmetric
casimir = {sp.Rational(3, 2): sp.Rational(15, 4), sp.Rational(1, 2): sp.Rational(3, 4)}
# W_p = weight +1/2 in V^{(x)3}: one vector from spin 3/2, two from spin 1/2
tr_cas_Wp = casimir[sp.Rational(3, 2)] + 2 * casimir[sp.Rational(1, 2)]
genus_bring = 4
rows = {
 "S3 count on proton sector (Burnside)": (burnside(lambda l: sum(l) == 2), "sector"),
 "S3 count on neutron sector": (burnside(lambda l: sum(l) == 1), "sector"),
 "S3 count on both nucleon sectors": (burnside(lambda l: sum(l) in (1, 2)), "sector"),
 "S3 count on whole V^(x)3": (burnside(lambda l: True), "whole space"),
 "2 * F_Bor(1) = 2 [3]_1!": (int(2 * qfact3.subs(q, 1)), "volume-term functional at q=1"),
 "dim H_3 (= |S_3|) * 2": (2 * factorial(3), "none"),
 "dim H_4 / 2": (factorial(4) // 2, "none"),
 "dim TL_3, dim TL_4": ((comb(6, 3) // 4, comb(8, 4) // 5), "none"),
 "|A_4|": (12, "none"),
 "3 colours x 4 weights of V^(x)3": (3 * len({sum(l) for l in lab}), "none"),
 "2 |chi(Bring)|, genus 4": (2 * abs(2 - 2 * genus_bring), "none"),
 "trace of su(2) Casimir on W_p": (str(tr_cas_Wp), "sector"),
}
checks = [("Burnside: proton 6, neutron 6, nucleons 12, whole 24",
           [rows[k][0] for k in list(rows)[:4]] == [6, 6, 12, 24]),
          ("2 F_Bor(1) = 12", rows["2 * F_Bor(1) = 2 [3]_1!"][0] == 12)]
for k, (v, m) in rows.items():
    print(f"{k:42s} {str(v):10s} mechanism: {m}")
ok = all(c for _, c in checks)
for n, c in checks:
    print(("PASS " if c else "FAIL ") + n)
Path(__file__).with_suffix(".out.json").write_text(json.dumps(
    {"probe": "mn_twelve_candidates_probe", "checks": dict(checks), "all_pass": ok,
     "candidates": {k: {"value": v if isinstance(v, (int, str)) else list(v), "mechanism": m} for k, (v, m) in rows.items()},
     "note": "Values equal to 12 without a mechanism are listed, not selected."}, indent=1) + "\n")
raise SystemExit(0 if ok else 1)
