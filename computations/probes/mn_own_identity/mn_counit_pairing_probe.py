"""Pre-registered in PREREGISTRATION-counit-pairing.md. Exact sympy, no floats.

A: in H_2(q) with generic Frobenius form lambda, the Frobenius counit equals lambda and
   rescales with it, so lambda = epsilon does not fix the scale.
B: in H_3(q) (regular rep, T_w basis), P(X) = tau(S(X) X) with tau the canonical
   symmetrising trace and S(T_w) = T_{w^-1}; ratio P(X_N)/P(X_e) vs 12.
"""
import json, itertools, sympy as sp

q, a, b, s = sp.symbols('q a b s')
h = q - 1/q
res = {}

# ---------- A ----------
# basis e0=1, e1=sig ; structure constants mult[i][j] = coeff vector
def mul2(u, v):
    # u,v coefficient vectors over (1, sig)
    c0 = u[0]*v[0] + u[1]*v[1]
    c1 = u[0]*v[1] + u[1]*v[0] + h*u[1]*v[1]
    return [sp.expand(c0), sp.expand(c1)]
E = [[1, 0], [0, 1]]
lam = lambda u: a*u[0] + b*u[1]
G = sp.Matrix(2, 2, lambda i, j: lam(mul2(E[i], E[j])))
Gi = G.inv()
# coev = sum_ij Gi[i,j] e_i (x) e_j ; Delta(x) = sum Gi[i,j] e_i (x) e_j x  (Frobenius relation)
def Delta(x):
    return {(i, tuple(mul2(E[j], x))): Gi[i, j] for i in range(2) for j in range(2)}
# counit from (id (x) eps) Delta(x) = x : solve eps(1)=e0_, eps(sig)=e1_
e0_, e1_ = sp.symbols('e0_ e1_')
eps = lambda u: e0_*u[0] + e1_*u[1]
eqs = []
for x in E:
    tot = [0, 0]
    for (i, y), c in Delta(x).items():
        tot[i] += c*eps(list(y))
    eqs += [sp.simplify(tot[k] - x[k]) for k in range(2)]
sol = sp.solve(eqs, [e0_, e1_], dict=True)
A1 = len(sol) == 1 and sp.simplify(sol[0][e0_] - a) == 0 and sp.simplify(sol[0][e1_] - b) == 0
res["A"] = {"counit_solution": {str(k): str(sp.simplify(v)) for k, v in sol[0].items()},
            "A1_counit_equals_lambda": bool(A1),
            "A2_counit_rescales_with_lambda": bool(A1),  # eps = (a,b) exactly, so (sa,sb) -> s*eps
            "scale_forced": False,
            "verdict": "lambda = epsilon holds for every (a,b) with det G != 0; no normalisation forced"}
res["A"]["gram_det"] = str(sp.factor(G.det()))

# ---------- B ----------
perms = list(itertools.permutations(range(3)))
def compose(p, r):  # (p*r)(i) = p(r(i))
    return tuple(p[r[i]] for i in range(3))
def length(p):
    return sum(1 for i in range(3) for j in range(i+1, 3) if p[i] > p[j])
gens = [(1, 0, 2), (0, 2, 1)]
idx = {p: k for k, p in enumerate(perms)}
e = (0, 1, 2)
def left_gen(i, vec):
    out = [0]*6
    for w, c in zip(perms, vec):
        if c == 0: continue
        sw = compose(gens[i], w)
        if length(sw) > length(w):
            out[idx[sw]] += c
        else:
            out[idx[w]] += h*c
            out[idx[sw]] += c
    return [sp.expand(x) for x in out]
def Lmat(i):
    cols = []
    for k in range(6):
        v = [0]*6; v[k] = 1
        cols.append(left_gen(i, v))
    return sp.Matrix(cols).T
S0, S1 = Lmat(0), Lmat(1)
S1i = S1.inv()
one = sp.Matrix([1 if p == e else 0 for p in perms])
def elem(M):  # element = M applied to T_e
    return [sp.simplify(x) for x in (M*one)]
Xe = elem(S0*S1*S0)
XN = elem((S0*S1i)**3)
# multiplication of two elements: left-regular matrix of x
def Lof(vec):
    M = sp.zeros(6)
    for w, c in zip(perms, vec):
        if c == 0: continue
        # T_w as product of generators along a reduced word
        word = {(0,1,2): [], (1,0,2): [0], (0,2,1): [1], (1,2,0): [0,1], (2,0,1): [1,0], (2,1,0): [0,1,0]}
        # verify word gives w
        p = e
        for g in reversed(word[w]):
            p = compose(gens[g], p)
        assert p == w, (w, p)
        Tm = sp.eye(6)
        for g in word[w]:
            Tm = Tm*Lmat(g)
        M += c*Tm
    return M
def S(vec):
    out = [0]*6
    for w, c in zip(perms, vec):
        winv = tuple(sorted(range(3), key=lambda i: w[i]))
        out[idx[winv]] += c
    return out
tau = lambda vec: vec[idx[e]]
def P(X):
    prod = Lof(S(X)) * sp.Matrix(X)
    return sp.factor(sp.simplify(tau(list(prod))))
Pe, PN = P(Xe), P(XN)
r = sp.factor(sp.simplify(PN/Pe))
checks = {
  "hecke_relation": bool(sp.simplify((S0 - q*sp.eye(6))*(S0 + sp.eye(6)/q)) == sp.zeros(6)),
  "braid_relation": bool(sp.simplify(S0*S1*S0 - S1*S0*S1) == sp.zeros(6)),
  "tau_symmetric_on_basis": all(sp.simplify(tau(list(Lof([1 if p==u else 0 for p in perms])*sp.Matrix([1 if p==v else 0 for p in perms])))
                                 - tau(list(Lof([1 if p==v else 0 for p in perms])*sp.Matrix([1 if p==u else 0 for p in perms])))) == 0
                                for u in perms for v in perms),
}
res["B"] = {"P_electron": str(Pe), "P_nucleon": str(PN), "ratio": str(r),
            "ratio_at_q1": str(sp.simplify(r.subs(q, 1))),
            "ratio_eq_12_identically": bool(sp.simplify(r - 12) == 0), "checks": checks}
res["verdict"] = {
  "A": "lambda = epsilon does not fix the scale (counit = lambda for every non-degenerate lambda)",
  "B": "PASS" if res["B"]["ratio_eq_12_identically"] else "scope-(a) negative: ratio is not 12 in this class"}
out = json.dumps(res, indent=2)
print(out)
open(__file__.replace('.py', '.out.json'), 'w').write(out + "\n")
