#!/usr/bin/env python3
"""Integer sums of braid words: which constants can the own-sector quantum trace reach?

Pre-registration: PREREGISTRATION-sums-and-premise.md (committed before this ran).
T_p(x) = q * tr_{W_p}(x), x = sum_w c_w w, c_w in Z, w a reduced signed word in
sigma_1^{+-1}, sigma_2^{+-1} of length <= 6. Exact sympy over Z[q, 1/q]; no floats, no
measured values.
"""
import itertools, json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

q = sp.symbols("q")
h = q - 1 / q
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])  # NucleonWeightSpaceTraces.A1
A2 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])  # NucleonWeightSpaceTraces.A2
G = {"s1": A1, "s2": A2, "S1": A1 - h * sp.eye(3), "S2": A2 - h * sp.eye(3)}
checks = []
checks.append(("S1 = s1^-1, S2 = s2^-1",
               sp.simplify(A1 * G["S1"]) == sp.eye(3) and sp.simplify(A2 * G["S2"]) == sp.eye(3)))

def Tp(word):
    M = sp.eye(3)
    for g in word:
        M = M * G[g]
    return sp.expand(q * M.trace())

traces, nwords = {}, 0
for L in range(0, 7):
    for w in itertools.product(G, repeat=L):
        if any(a[1] == b[1] and a[0] != b[0] for a, b in zip(w, w[1:])):
            continue
        nwords += 1
        traces.setdefault(Tp(w), " ".join(w) or "1")
polys = list(traces)
SH = 60
exps = sorted({m[0] for p in polys for m in sp.Poly(sp.expand(p * q**SH), q).monoms()})
def vec(p):
    d = dict(sp.Poly(sp.expand(p * q**SH), q).terms())
    return [int(d.get((e,), 0)) for e in exps]
M = sp.Matrix([vec(p) for p in polys]).T
B = hermite_normal_form(M)
assert B.shape[0] == B.shape[1] == len(exps), "lattice not full rank on its monomials"
# every generator lies in the HNF lattice and vice versa (integer solves)
Binv = B.inv()
checks.append(("every word trace is an integer combination of the HNF basis",
               all(all(t.is_integer for t in Binv * sp.Matrix(vec(p))) for p in polys)))
ci = exps.index(SH)
x = Binv[:, ci]
kmin = sp.ilcm(*[sp.fraction(t)[1] for t in x])
# explicit invariant: a coordinate functional, integer on the lattice, fractional on the constant 1
r = next(i for i, t in enumerate(x) if not t.is_integer)
psi = {int(e - SH): Binv[r, j] for j, e in enumerate(exps) if Binv[r, j] != 0}
checks.append(("constants reachable by integer sums are exactly kmin*Z, kmin = 3", kmin == 3))

e1 = sp.expand(Tp(["s1"]) + 2 * Tp(["S1"]))
e2 = sp.expand(Tp(["s2"]) + 2 * Tp(["S2"]))
twelve = sp.expand(4 * Tp(["s1"]) + 8 * Tp(["S1"]))
checks.append(("T_p(s1 + 2 s1^-1) = 3", e1 == 3))
checks.append(("T_p(s2 + 2 s2^-1) = 3 (second element, same value)", e2 == 3))
checks.append(("T_p(4 s1 + 8 s1^-1) = 12, and so is every other multiple of 3", twelve == 12))

# canonical elements of H_3 (reported whatever they give)
red = {"e": [], "1": ["s1"], "2": ["s2"], "12": ["s1", "s2"], "21": ["s2", "s1"], "121": ["s1", "s2", "s1"]}
ln = {k: len(v) for k, v in red.items()}
TT = {k: Tp(v) for k, v in red.items()}
canon = {
    "sum_w T_w": sum(TT.values()),
    "sum_w q^l(w) T_w (symmetriser)": sum(q**ln[k] * TT[k] for k in TT),
    "sum_w q^-l(w) T_w": sum(q**-ln[k] * TT[k] for k in TT),
    "sum_w (-q)^-l(w) T_w (antisymmetriser)": sum((-q)**-ln[k] * TT[k] for k in TT),
    "full twist (s1 s2 s1)^2": Tp(["s1", "s2", "s1", "s1", "s2", "s1"]),
    "Jucys-Murphy L2 + L3": sp.expand(Tp(["s1", "s1"]) + Tp(["s2", "s1", "s1", "s2"])),
}
canon_out = {k: {"T_p": str(sp.factor(sp.simplify(v))), "q_independent": sp.diff(sp.simplify(v), q).simplify() == 0,
                 "at_q_1": str(sp.simplify(v).subs(q, 1))} for k, v in canon.items()}
checks.append(("no canonical element has a q-independent nonzero T_p",
               not any(o["q_independent"] and o["at_q_1"] != "0" for o in canon_out.values())))

ok = all(c for _, c in checks)
for n_, c in checks:
    print(("PASS " if c else "FAIL ") + n_)
print("words:", nwords, "distinct traces:", len(polys), "lattice rank:", len(exps), "kmin:", kmin)
print("invariant psi (q-exponent: coefficient):", psi)
print(json.dumps(canon_out, indent=1))
out = {"probe": "mn_sector_sums_probe", "preregistration": "PREREGISTRATION-sums-and-premise.md",
       "checks": {n_: c for n_, c in checks}, "all_pass": ok, "words_tested": nwords,
       "distinct_traces": len(polys), "lattice_rank": len(exps), "min_positive_constant": int(kmin),
       "invariant_functional": {str(k): str(v) for k, v in psi.items()},
       "elements": {"s1 + 2 s1^-1": "3", "s2 + 2 s2^-1": "3", "4 s1 + 8 s1^-1": "12"},
       "canonical_elements": canon_out,
       "verdict": "integer sums reach exactly 3Z; 12 is allowed, not forced (scope: words of length <= 6)"}
Path(__file__).with_suffix(".out.json").write_text(json.dumps(out, indent=1) + "\n")
raise SystemExit(0 if ok else 1)
