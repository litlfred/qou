"""Pre-registered PREREGISTRATION-hydrogen-capture-and-chirality.md. Arm 1: bond chirality
(6 strands). Arm 2: corpus capture braid (electron strand encircles the proton cable, 4 strands).
Exact sympy over Q(q) on sparse vectors; mpmath 60 dps. No float64."""
import json, itertools, sympy as sp, mpmath as mp
from qou_substrate import constants as C
mp.mp.dps = 60
q = sp.symbols('q', positive=True); h = q - 1/q
R = {(0,0): [((0,0), q)], (0,1): [((1,0), 1)], (1,0): [((0,1), 1), ((1,0), h)], (1,1): [((1,1), q)]}
Ri = {(0,0): [((0,0), 1/q)], (0,1): [((0,1), -h), ((1,0), 1)], (1,0): [((0,1), 1)], (1,1): [((1,1), 1/q)]}
def apply(L, vec):
    i, inv = L; M = Ri if inv else R; out = {}
    for s, c in vec.items():
        for (a, b), v in M[(s[i], s[i+1])]:
            t = s[:i] + (a, b) + s[i+2:]; out[t] = out.get(t, 0) + c*v
    return out
def word_apply(word, vec):
    for L in reversed(word): vec = apply(L, vec)
    return vec
inv = lambda w: [(i, not b) for (i, b) in reversed(w)]
V3 = lambda i: [(i, False), (i+1, True)]*3
V3m = lambda i: [(i, True), (i+1, False)]*3   # (s_i^-1 s_{i+1})^3
P = lambda ws: [(i, False) for i in ws]
T3 = lambda s, rng: sp.Rational(sum(1 if s[k] == 0 else -1 for k in rng), 2)
def run(n, word, prot):
    basis = list(itertools.product([0, 1], repeat=n))
    diag = {s: sp.expand(word_apply(word, {s: 1}).get(s, 0)) for s in basis}
    elec = [k for k in range(n) if k not in prot]; res = {}
    for name, w in (("O+", 2), ("O-", 1)):
        sel = [s for s in basis if sum(1 for k in prot if s[k] == 0) == w]
        F = {"B1": sum(T3(s, range(n))*diag[s] for s in sel),
             "B2": sum(T3(s, range(n))*q**(2*T3(s, range(n)))*diag[s] for s in sel),
             "B3_electron": sum(T3(s, elec)*diag[s] for s in sel)}
        res[name] = {k: sp.factor(sp.simplify(v)) for k, v in F.items()}
    for k in ("B1", "B2"): res["S_" + k] = sp.factor(sp.simplify(res["O+"][k] + res["O-"][k]))
    return res
q0 = mp.mpf(C.Q_50_DIGIT_STR)
def ev(e): return mp.nstr(sp.lambdify(q, e, "mpmath")(q0), 20)
def pack(r):
    d = {}
    for o in ("O+", "O-"):
        d[o] = {k: {"exact": str(v), "q=1": str(v.subs(q, 1)), "q0": ev(v), "zero": bool(v == 0)}
                for k, v in r[o].items()}
    for k in ("S_B1", "S_B2"): d[k] = {"exact": str(r[k]), "q=1": str(r[k].subs(q, 1)), "q0": ev(r[k])}
    return d
e3 = P([3, 4, 3]); e0 = P([0, 1, 0])
cases = {
  "arm1_G_left":   (6, V3(0) + e3 + V3(2), [0, 1, 2]),
  "arm1_G_right":  (6, e0 + V3(3) + V3(2), [3, 4, 5]),
  "arm1_Gp_left":  (6, V3(0) + e3 + V3m(2), [0, 1, 2]),
  "arm1_Gp_right": (6, e0 + V3(3) + V3m(2), [3, 4, 5]),
  "arm2_capture_left":  (4, V3(0) + inv(P([2, 1, 0, 0, 1, 2])), [0, 1, 2]),
  "arm2_capture_right": (4, V3(1) + inv(P([0, 1, 2, 2, 1, 0])), [1, 2, 3]),
}
out = {"preregistration": "PREREGISTRATION-hydrogen-capture-and-chirality.md"}
for lab, (n, w, prot) in cases.items(): out[lab] = pack(run(n, w, prot))
s_ = json.dumps(out, indent=1)
open(__file__.replace('.py', '.out.json'), 'w').write(s_ + "\n")
for lab in cases:
    d = out[lab]; print(lab, {o: (d[o]["B1"]["q0"], d[o]["B2"]["q0"], d[o]["B1"]["q=1"]) for o in ("O+","O-")},
                         "S_B1:", d["S_B1"]["exact"], d["S_B1"]["q0"], "| S_B2 q0:", d["S_B2"]["q0"])
