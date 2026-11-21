"""H9b: folded wall (mirror summed), exact. Sparse vector propagation over 6 strands."""
import sympy as sp
q = sp.symbols('q', positive=True)
f0, f1, f01, g0, g1, g01 = sp.symbols('phi0 phi1 phi01 psi0 psi1 psi01')
N = 6
def Rcol(a, b, qq, inv):  # image of basis e_a e_b under R (or R^-1); 0 = e1, 1 = e2
    hh = qq - 1/qq
    if a == b: return {(a, b): (qq if not inv else 1/qq)}
    if (a, b) == (0, 1): return {(1, 0): 1} if not inv else {(1, 0): 1, (0, 1): -hh}
    return {(0, 1): 1, (1, 0): hh} if not inv else {(0, 1): 1}
def apply_gen(vec, j, inv, qq):  # crossing on strands j, j+1 (1-based)
    out = {}
    for st, c in vec.items():
        for (a, b), w in Rcol(st[j-1], st[j], qq, inv).items():
            ns = st[:j-1] + (a, b) + st[j+1:]
            out[ns] = out.get(ns, 0) + c*w
    return out
def apply_term(vec, term, qq):  # term: list of (j, inv), applied left-to-right as matrix product M = A1 A2 ...
    for (j, inv) in reversed(term): vec = apply_gen(vec, j, inv, qq)
    return vec
def fold(i, sg): return [(3+i, sg < 0), (3-i, sg < 0)]
def apply_word(vec, word, qq):  # word: list of letters; letter = list of (coef, term)
    for letter in reversed(word):
        new = {}
        for coef, term in letter:
            for st, c in apply_term(dict(vec), term, qq).items():
                new[st] = new.get(st, 0) + coef*c
        vec = new
    return vec
from itertools import product
states = list(product((0, 1), repeat=N))
def trace(word, qq, phys):
    tot = 0
    for st in states:
        if sum(1 if x == 0 else -1 for x in st[3:]) != phys: continue
        piv = sp.Integer(1)
        for x in st: piv *= qq if x == 0 else 1/qq
        tot += piv*apply_word({st: 1}, word, qq).get(st, 0)
    return sp.together(sp.expand(tot))
def D_of(word, qq, slot=0):
    wall = [(1, [(3, False)])]
    W = word[:slot] + [wall] + word[slot:]
    Tp, Tn, Bp, Bn = trace(word, qq, 1), trace(word, qq, -1), trace(W, qq, 1), trace(W, qq, -1)
    return sp.factor(sp.cancel(((Tn+Bn)/(Tp+Bp))/(Tn/Tp))), sp.factor(sp.cancel(Tp/Tn))
V3 = [[(1, fold(i, sg))] for (i, sg) in [(1, 1), (2, -1)]*3]
D, r = D_of(V3, q)
print("V3 closed T_p/T_n =", r); print("V3 D(q) =", D)
from qou_substrate.constants import Q_50_DIGIT_STR
q0 = sp.Rational(Q_50_DIGIT_STR)
for v in (sp.Rational(3, 2), sp.Integer(2), q0): print(f"  D({sp.N(v,8)}) = {sp.N(D.subs(q, v), 20)}")
num, den = sp.fraction(D)
print("real roots of denominator in (1, 3):", [sp.N(x, 12) for x in sp.Poly(den, q).real_roots() if 1 < x < 3])
def photon(a0, a1, a01):  # gamma = 1 + a0 s1 + a1 s2 + a01 s1 s2^-1 (ruled photon), folded
    return [(1, []), (a0, fold(1, 1)), (a1, fold(2, 1)), (a01, fold(1, 1) + fold(2, -1))]
pair = [photon(f0, f1, f01), photon(g0, g1, g01)]
hq = q - 1/q
Vchk = [photon(0, 0, q*hq), photon(0, 0, -hq/q)]
print("check: gamma(0,0,qh)gamma(0,0,-h/q) gives same D as V3 at q=3/2:",
      sp.simplify(D_of(Vchk, sp.Rational(3, 2))[0] - D.subs(q, sp.Rational(3, 2))) == 0)
for lab, qq in (("q=1", sp.Integer(1)), ("q0", q0)):
    Dg, rg = D_of(pair, qq)
    print(f"general pair at {lab}: D depends on phi? {any(sp.diff(Dg, s) != 0 for s in (f0,f1,f01,g0,g1,g01))}")
    if lab == "q=1": print("   D at q=1 =", sp.simplify(Dg))
    else:
        for name, sub in (("V3 point", {f0:0,f1:0,f01:qq*(qq-1/qq),g0:0,g1:0,g01:-(qq-1/qq)/qq}),
                          ("phi all 1", {s: 1 for s in (f0,f1,f01,g0,g1,g01)})):
            print(f"   D at {name} = {sp.N(Dg.subs(sub), 20)}")
