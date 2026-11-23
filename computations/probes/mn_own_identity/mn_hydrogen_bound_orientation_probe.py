"""Pre-registered PREREGISTRATION-hydrogen-bound-orientation.md. Hydrogen as one bound
6-strand word W = N.e.G; neutrality functionals B1, B2, B3 in both orientations, proton left/right.
Exact sympy over Q(q) (sparse vectors); mpmath 60 dps evaluation. No float64."""
import json, itertools, sympy as sp, mpmath as mp
from qou_substrate import constants as C
mp.mp.dps = 60
q = sp.symbols('q', positive=True); h = q - 1/q; n = 6
basis = list(itertools.product([0, 1], repeat=n)); idx = {b: i for i, b in enumerate(basis)}
# Rc on pair (a,b) in basis 00,01,10,11: columns
R = {(0,0): [((0,0), q)], (0,1): [((1,0), 1)], (1,0): [((0,1), 1), ((1,0), h)], (1,1): [((1,1), q)]}
Ri = {(0,0): [((0,0), 1/q)], (0,1): [((0,1), -h), ((1,0), 1)], (1,0): [((0,1), 1)], (1,1): [((1,1), 1/q)]}
def apply(letter, vec):
    i, inv = letter; M = Ri if inv else R; out = {}
    for s, c in vec.items():
        for (a, b), v in M[(s[i], s[i+1])]:
            t = s[:i] + (a, b) + s[i+2:]; out[t] = out.get(t, 0) + c*v
    return out
def word_apply(word, vec):  # matrix product W = l1 l2 ... lk acts on vec: apply lk first
    for L in reversed(word): vec = apply(L, vec)
    return vec
V3 = lambda i: [(i, False), (i+1, True)]*3
WL = V3(0) + [(3, False), (4, False), (3, False)] + V3(2)
WR = [(0, False), (1, False), (0, False)] + V3(3) + V3(2)
def T3(s, rng): return sp.Rational(sum(1 if s[k] == 0 else -1 for k in rng), 2)
def run(word, prot):
    diag = {}
    for s in basis:
        diag[s] = sp.expand(word_apply(word, {s: 1}).get(s, 0))
    elec = [k for k in range(6) if k not in prot]; res = {}
    for name, w in (("O+", 2), ("O-", 1)):
        sel = [s for s in basis if sum(1 for k in prot if s[k] == 0) == w]
        Kf = lambda s: q**(2*T3(s, range(6)))
        F1 = sum(T3(s, range(6))*diag[s] for s in sel)
        F2 = sum(T3(s, range(6))*Kf(s)*diag[s] for s in sel)
        Fp = sum(T3(s, prot)*diag[s] for s in sel); Fe = sum(T3(s, elec)*diag[s] for s in sel)
        res[name] = {k: sp.factor(sp.simplify(v)) for k, v in
                     (("B1", F1), ("B2", F2), ("B3_proton", Fp), ("B3_electron", Fe))}
    res["S_B1"] = sp.factor(sp.simplify(res["O+"]["B1"] + res["O-"]["B1"]))
    res["S_B2"] = sp.factor(sp.simplify(res["O+"]["B2"] + res["O-"]["B2"]))
    return res
q0 = mp.mpf(C.Q_50_DIGIT_STR)
def ev(e, qv): return mp.nstr(sp.lambdify(q, e, "mpmath")(qv), 25)
out = {"preregistration": "PREREGISTRATION-hydrogen-bound-orientation.md"}
for lab, word, prot in (("W_L_proton_left", WL, [0, 1, 2]), ("W_R_proton_right", WR, [3, 4, 5])):
    r = run(word, prot); blk = {}
    for o in ("O+", "O-"):
        blk[o] = {k: {"exact": str(v), "q=1": str(v.subs(q, 1)), "q0": ev(v, q0),
                      "q=1+1e-20": ev(v, 1 + mp.mpf('1e-20'))} for k, v in r[o].items()}
    for k in ("S_B1", "S_B2"):
        blk[k] = {"exact": str(r[k]), "q=1": str(r[k].subs(q, 1)), "q0": ev(r[k], q0)}
    zero = {o: {k: bool(sp.simplify(r[o][k]) == 0) for k in ("B1", "B2")} for o in ("O+", "O-")}
    blk["exactly_zero"] = zero; out[lab] = blk
s_ = json.dumps(out, indent=1); print(s_)
open(__file__.replace('.py', '.out.json'), 'w').write(s_ + "\n")
