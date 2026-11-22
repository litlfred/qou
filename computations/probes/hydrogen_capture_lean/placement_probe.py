"""Pre-registered: PREREGISTRATION-placement.md (commit ab4a8c43cc2).
Reflection Π = X^{⊗4}∘P_rev on the 4-strand hydrogen capture: checks P1–P4. Exact sympy over Q(q);
mpmath 60 dps only for display. No float64."""
import json, itertools, random, sympy as sp, mpmath as mp
from qou_substrate import constants as C
mp.mp.dps = 60
q = sp.symbols('q', positive=True); h = q - 1/q
R = {(0,0): [((0,0), q)], (0,1): [((1,0), 1)], (1,0): [((0,1), 1), ((1,0), h)], (1,1): [((1,1), q)]}
Ri = {(0,0): [((0,0), 1/q)], (0,1): [((0,1), -h), ((1,0), 1)], (1,0): [((0,1), 1)], (1,1): [((1,1), 1/q)]}
N = 4
def apply(L, vec):
    i, inv = L; M = Ri if inv else R; out = {}
    for s, c in vec.items():
        for (a, b), v in M[(s[i], s[i+1])]:
            t = s[:i] + (a, b) + s[i+2:]; out[t] = out.get(t, 0) + c*v
    return out
def diag(word):
    d = {}
    for s in itertools.product([0, 1], repeat=N):
        v = {s: 1}
        for L in reversed(word): v = apply(L, v)
        d[s] = sp.expand(v.get(s, 0))
    return d
T3 = lambda s: sp.Rational(sum(1 if x == 0 else -1 for x in s), 2)
def F(d, prot, w, kexp):
    """tr(T³ · K^kexp · W · Π_O), K = q^{2T³}; Π_O: proton strands carry w zeros."""
    return sp.factor(sp.simplify(sum(T3(s)*q**(2*kexp*T3(s))*d[s] for s in d
                                     if sum(1 for k in prot if s[k] == 0) == w)))
flip = lambda w: [(N - 2 - i, b) for (i, b) in w]
inv = lambda w: [(i, not b) for (i, b) in reversed(w)]
V3 = lambda i: [(i, False), (i+1, True)]*3
P = lambda ws: [(i, False) for i in ws]
capL = V3(0) + inv(P([2, 1, 0, 0, 1, 2]))
capR = V3(1) + inv(P([0, 1, 2, 2, 1, 0]))
L, Rt = [0, 1, 2], [1, 2, 3]
words = {"capL": capL, "capL_gV": V3(0) + [(0, False), (1, True)] + inv(P([2, 1, 0, 0, 1, 2])),
         "capL_gsigma1": V3(0) + [(1, False)] + inv(P([2, 1, 0, 0, 1, 2]))}
rng = random.Random(20261122)
for k in range(6):
    words[f"rand{k}"] = [(rng.randrange(3), rng.random() < 0.5) for _ in range(rng.randrange(4, 11))]
out = {"preregistration": "PREREGISTRATION-placement.md", "commit_prereg": "ab4a8c43cc2", "words": {}}
ok = {"P1": True, "P2": True, "P3": True}
for name, w in words.items():
    dL, dR = diag(w), diag(flip(w))
    r = {}
    for kexp in (0, 1, -1):
        r[kexp] = {"L+": F(dL, L, 2, kexp), "L-": F(dL, L, 1, kexp),
                   "R+": F(dR, Rt, 2, kexp), "R-": F(dR, Rt, 1, kexp)}
    # P1 (unweighted), P2 (weighted, K ↔ K^{-1})
    ok["P1"] &= sp.simplify(r[0]["R+"] + r[0]["L-"]) == 0 and sp.simplify(r[0]["R-"] + r[0]["L+"]) == 0
    ok["P2"] &= sp.simplify(r[1]["R+"] + r[-1]["L-"]) == 0 and sp.simplify(r[1]["R-"] + r[-1]["L+"]) == 0
    SL2 = r[1]["L+"] + r[1]["L-"]; SR2 = r[1]["R+"] + r[1]["R-"]
    ok["P3"] &= sp.simplify(SL2 + SR2 - (q**2 - q**-2)*(r[0]["L+"] - r[0]["L-"])) == 0
    out["words"][name] = {"word": w, "S_B1_L": str(sp.factor(r[0]["L+"] + r[0]["L-"])),
                          "S_B1_R(flip)": str(sp.factor(r[0]["R+"] + r[0]["R-"])),
                          "S_B2_L": str(sp.factor(SL2)), "S_B2_R(flip)": str(sp.factor(SR2))}
# corpus right capture (proton V3 on strands 1-3) against flip(capL)
dcR = diag(capR)
cR = {k: (F(dcR, Rt, 2, k), F(dcR, Rt, 1, k)) for k in (0, 1)}
out["capR_vs_flip_capL"] = {f"kexp{k}": [str(sp.factor(cR[k][0])), str(sp.factor(cR[k][1]))] for k in cR}
dfl = diag(flip(capL))
ok["capR_equals_flip_capL_perorientation"] = all(
    sp.simplify(cR[k][0] - F(dfl, Rt, 2, k)) == 0 and sp.simplify(cR[k][1] - F(dfl, Rt, 1, k)) == 0 for k in (0, 1))
# word-dependent part of S_B2: subtract the identity word
d1L, d1R = diag([]), diag([])
base = {"L": F(d1L, L, 2, 1) + F(d1L, L, 1, 1), "R": F(d1R, Rt, 2, 1) + F(d1R, Rt, 1, 1)}
S2L = sp.factor(sp.simplify(sum(F(diag(capL), L, w_, 1) for w_ in (2, 1)) - base["L"]))
S2R = sp.factor(sp.simplify(cR[1][0] + cR[1][1] - base["R"]))
out["S_B2_minus_identity"] = {"capL": str(S2L), "capR": str(S2R), "identity_L": str(base["L"]), "identity_R": str(base["R"])}
# P4: two-strand partial traces of Ř
Rm = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]])
ptrR = lambda d0, d1: sp.Matrix(2, 2, lambda a, b: sp.simplify(d0*Rm[2*a, 2*b] + d1*Rm[2*a+1, 2*b+1]))
ptrLf = lambda d0, d1: sp.Matrix(2, 2, lambda a, b: sp.simplify(d0*Rm[a, b] + d1*Rm[2+a, 2+b]))
out["P4"] = {"right_K": str(ptrR(q, 1/q)), "right_Kinv": str(ptrR(1/q, q)),
             "left_K": str(ptrLf(q, 1/q)), "left_Kinv": str(ptrLf(1/q, q))}
ok["P4"] = (ptrR(q, 1/q) == q**2*sp.eye(2) and ptrLf(1/q, q) == q**2*sp.eye(2)
            and sp.simplify(ptrLf(q, 1/q)[0, 0] - ptrLf(q, 1/q)[1, 1]) != 0
            and sp.simplify(ptrR(1/q, q)[0, 0] - ptrR(1/q, q)[1, 1]) != 0)
q0 = mp.mpf(C.Q_50_DIGIT_STR)
ev = lambda e: mp.nstr(sp.lambdify(q, sp.sympify(e), "mpmath")(q0), 15)
out["at_q0"] = {k: ev(v) for k, v in out["S_B2_minus_identity"].items()}
out["at_q0"].update({f"{n}:{k}": ev(v) for n, d in out["words"].items() if n.startswith("cap") for k, v in d.items() if k.startswith("S_")})
out["checks"] = ok
open(__file__.replace('.py', '.out.json'), 'w').write(json.dumps(out, indent=1, default=str) + "\n")
print(json.dumps(ok)); print(json.dumps(out["S_B2_minus_identity"], indent=1)); print(json.dumps(out["at_q0"], indent=1))
print(json.dumps(out["capR_vs_flip_capL"])); print(out["P4"])
