#!/usr/bin/env python3
"""Step-3 tail rules R1, R2, R4 (main b611c74d815) re-read with the k = 1 γγ gluon V appended.

Not pre-registered: a re-read of the step-3 table on the element the gluon-segment run admits (CORE·T·V).
Exact sympy over Q(q), convention D, H3, proton pin as an exact rational; mpmath only for display.
Formulas imported unchanged from gg_quark_tail_probe.py / gg_gluon_segment_probe.py. Nothing ranked or selected.
"""
from __future__ import annotations
import importlib.util, os, sys
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("_t", os.path.join(HERE, "gg_quark_tail_probe.py"))
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
G_, A, q = T.G_, T.ALPHA, T.q
RULES = {"R1": {0: "s0", 1: "s1i"}, "R2": {0: "s0i", 1: "s1"}, "R4": {0: "a0", 1: "a1"}}
STEP3 = {("R1", "001"): "-0.42477", ("R2", "001"): "+0.48410", ("R4", "010"): "+0.00031", ("R1", "100"): "-0.36794"}


def fmt_roots(e):
    return [str(sp.N(r, 7)) for r in T.roots_above_1(e)]


def main():
    ok = True
    print("| rule | placement | no gluon: χ_(2,1)(q₀), roots>1 | with V: χ_(2,1)(q₀), roots>1 |")
    print("|---|---|---|---|")
    for rule, m in RULES.items():
        for pl in ["000", "001", "010", "011", "100", "101", "110", "111"]:
            cells = []
            for g in ([], T.V):
                c21 = G_.chi21(T.CORE + [A[m[int(b)]] for b in pl] + g)
                v = sp.N(c21.subs(q, T.Q0), 12)
                cells.append(f"{v:+.5f}, {fmt_roots(c21) or 'none'}")
                if not g and (rule, pl) in STEP3 and f"{v:+.5f}" != STEP3[(rule, pl)]:
                    ok = False
            print(f"| {rule} | {pl} | {cells[0]} | {cells[1]} |")
    r1 = G_.chi21(T.CORE + [A["s0"], A["s0"], A["s1i"]])
    for k, t in G_.TAIL.items():
        print(f"chi21(CORE·TAIL_{k}·V) / chi21(CORE·s0 s0 s1i) =", sp.factor(sp.cancel(G_.chi21(T.CORE + list(t) + T.V) / r1)))
    print("calibration vs step-3 table:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
