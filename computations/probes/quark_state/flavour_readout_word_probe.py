#!/usr/bin/env python3
"""Per-letter flavour readout from a WORD of single-letter quarks (bean qou-qs1x).

Exact sympy over Q(q) / Q[h]; no float, no fitting, no target value. For the nucleon word
core . l(g1,e1) l(g2,e2) l(g3,e3), with core = (s0 s1^-1)^3 and a letter l(g,e) = s_g + c(e) h 1
(c(u) = 0, c(d) = -1, i.e. s or s^-1 = s - h), count how many of the 8 flavour assignments give
DISTINCT objects at four resolutions:
  (A) the full NF element of H_3 (6 coords, polynomials in h),
  (B) its h^1 part only,
  (C) the (2,1) image (2x2 matrix over Q(q)),
  (D) the (2,1) character (trace).
for every generator placement (g1,g2,g3) in {0,1}^3. Output: results.json beside this file.
"""
import itertools
import json
from pathlib import Path

import sympy as sp

h, q = sp.symbols("h q")


def m0(v):
    return [v[1], v[0] + h * v[1], v[3], v[2] + h * v[3], v[5], v[4] + h * v[5]]


def m1(v):
    return [v[2], v[4], v[0] + h * v[2], v[5], v[1] + h * v[4], v[3] + h * v[5]]


def mul(u, v):  # mulNF, same structure constants as QOU.Machinery.H3.mulNF
    t = [u, m0(u), m1(u), m0(m1(u)), m1(m0(u)), m0(m1(m0(u)))]
    return [sp.expand(sum(v[j] * t[j][i] for j in range(6))) for i in range(6)]


E0 = [1, 0, 0, 0, 0, 0]
S = {0: [0, 1, 0, 0, 0, 0], 1: [0, 0, 1, 0, 0, 0]}
C = {"u": 0, "d": -1}


def letter(g, c):
    return [S[g][i] + c * h * E0[i] for i in range(6)]


def word(letters):
    w = E0
    for g, c in letters:
        w = mul(w, letter(g, c))
    return w


CORE = [(0, 0), (1, -1)] * 3
A = sp.Matrix([[q, -1 / q], [0, -1 / q]])
B = sp.Matrix([[-1 / q, 0], [-q, q]])


def rho(v):
    M = [sp.eye(2), A, B, B * A, A * B, A * B * A]
    return sp.simplify(sum((v[i] * M[i] for i in range(6)), sp.zeros(2, 2)).subs(h, q - 1 / q))


def main():
    out = {}
    for pl in itertools.product((0, 1), repeat=3):
        objs = {"A_full_NF": {}, "B_h1_part": {}, "C_21_matrix": {}, "D_21_trace": {}}
        for fl in itertools.product("ud", repeat=3):
            v = word(CORE + [(g, C[f]) for g, f in zip(pl, fl)])
            M = rho(v)
            key = "".join(fl)
            objs["A_full_NF"][key] = tuple(sp.expand(x) for x in v)
            objs["B_h1_part"][key] = tuple(sp.expand(x).coeff(h, 1) for x in v)
            objs["C_21_matrix"][key] = tuple(sp.factor(x) for x in M)
            objs["D_21_trace"][key] = sp.factor(M.trace())
        res = {}
        for lvl, d in objs.items():
            classes = {}
            for k, val in d.items():
                classes.setdefault(val, []).append(k)
            res[lvl] = {"distinct": len(classes), "classes": sorted(sorted(c) for c in classes.values())}
        out["".join(map(str, pl))] = res
        print(pl, {k: v["distinct"] for k, v in res.items()}, res["A_full_NF"]["classes"])
    Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
