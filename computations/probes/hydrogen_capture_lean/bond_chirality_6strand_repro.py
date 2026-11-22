"""Sympy reproduction of the four 6-strand S values of #8804 §43 (exact over Q(q)); no float."""
import itertools, sympy as sp
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
V3 = lambda i: [(i, False), (i+1, True)]*3
V3m = lambda i: [(i, True), (i+1, False)]*3
P = lambda ws: [(i, False) for i in ws]
T3 = lambda s: sp.Rational(sum(1 if x == 0 else -1 for x in s), 2)
e3 = P([3, 4, 3]); e0 = P([0, 1, 0])
cases = {"G_left": (V3(0)+e3+V3(2), [0,1,2]), "G_right": (e0+V3(3)+V3(2), [3,4,5]),
         "Gp_left": (V3(0)+e3+V3m(2), [0,1,2]), "Gp_right": (e0+V3(3)+V3m(2), [3,4,5])}
targets = {"G_left": -4*q*h**4, "G_right": (3*q**2+1)*h**4/q,
           "Gp_left": (q**2+1)*(3*q**4-2*q**2+1)*h**4/q, "Gp_right": -(3*q**2+1)*q**3*h**4}
basis = list(itertools.product([0,1], repeat=6))
for lab,(w,prot) in cases.items():
    diag = {s: sp.expand(word_apply(w, {s:1}).get(s,0)) for s in basis}
    F = {}
    for name, wz in (("O+",2),("O-",1)):
        F[name] = sp.factor(sum(T3(s)*diag[s] for s in basis if sum(1 for k in prot if s[k]==0)==wz))
    S = sp.factor(F["O+"]+F["O-"])
    print(lab, "S =", S, "| target ok:", sp.simplify(S-targets[lab])==0, "| q=1:", S.subs(q,1),
          "| O+(1)=", F["O+"].subs(q,1), "O-(1)=", F["O-"].subs(q,1))
inv = lambda w: [(i, not b) for (i, b) in reversed(w)]
for lab,(n,w,prot) in {"cap_left":(4, V3(0)+inv(P([2,1,0,0,1,2])),[0,1,2]),"cap_right":(4,V3(1)+inv(P([0,1,2,2,1,0])),[1,2,3])}.items():
    bs = list(itertools.product([0,1], repeat=n))
    diag = {s: sp.expand(word_apply(w,{s:1}).get(s,0)) for s in bs}
    for name, wz in (("O+",2),("O-",1)):
        v = sum(T3(s)*diag[s] for s in bs if sum(1 for k in prot if s[k]==0)==wz)
        print(lab,name,"B1(1)=",sp.simplify(v).subs(q,1))
for lab,(w,prot) in cases.items():
    diag = {s: sp.expand(word_apply(w, {s:1}).get(s,0)) for s in basis}
    el=[k for k in range(6) if k not in prot]
    for name, wz in (("O+",2),("O-",1)):
        sel=[s for s in basis if sum(1 for k in prot if s[k]==0)==wz]
        b3 = sum(sp.Rational(sum(1 if s[k]==0 else -1 for k in el),2)*diag[s] for s in sel)
        print(lab,name,"B3e(1)=",sp.simplify(b3).subs(q,1), " #sel states", len(sel))
