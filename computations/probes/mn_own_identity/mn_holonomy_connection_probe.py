"""Pre-registered in PREREGISTRATION-holonomy-connection.md. Exact sympy, no floats.

nabla_hol = hol - 1 with hol = B3 = (s0 s1^-1)^3 (nucleon) and X_e = s0 s1 s0 (electron),
on the weight spaces of (C^2)^{x3}; states = normalised eigenvectors of hol itself.
"""
import json, itertools, sympy as sp

q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2 = sp.eye(2)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
B3 = sp.simplify((s0*s1.inv())**3)
Xe = s0*s1*s0
basis = list(itertools.product([0,1], repeat=3))
def wspace(nup): return [i for i,b in enumerate(basis) if b.count(0)==nup]
def restrict(M, idx):
    out = M.extract(idx, idx)
    # check invariance
    other = [i for i in range(8) if i not in idx]
    assert sp.simplify(M.extract(other, idx)) == sp.zeros(len(other), len(idx))
    return sp.simplify(out)
res = {"checks": {"hecke": bool(sp.simplify((Rc-q*sp.eye(4))*(Rc+sp.eye(4)/q))==sp.zeros(4))}}
def spectrum(M):
    p = sp.factor(M.charpoly(sp.Symbol('t')).as_expr())
    ev = sp.roots(sp.Poly(M.charpoly(sp.Symbol('t')).as_expr(), sp.Symbol('t')))
    return p, {sp.factor(k): v for k, v in ev.items()}
weights = {"proton_W(2,1)": (2, q), "neutron_W(1,2)": (1, 1/q)}
nuc = {}
for name, (nup, w) in weights.items():
    M = restrict(B3, wspace(nup))
    p, ev = spectrum(M)
    branches = []
    for lam, m in ev.items():
        mu = sp.factor(lam - 1)
        branches.append({"eigenvalue": str(lam), "mult": int(m), "mu": str(mu),
                         "weighted_horizontal_qinv_w_mu": str(sp.factor(w*mu/q)),
                         "mu_at_q1": str(sp.simplify(mu.subs(q,1)))})
    nuc[name] = {"charpoly": str(p), "branches": branches}
    res[name] = nuc[name]
ele = {}
for name, (nup, w) in weights.items():
    M = restrict(Xe, wspace(nup)); p, ev = spectrum(M)
    ele[name] = {"charpoly": str(p), "eigen_minus_1": {str(k): str(sp.factor(k-1)) for k in ev}}
res["electron_Xe"] = ele
# 12 check: any mu == 12, or any ratio of nucleon mu to electron (eig-1) == 12
mus = [sp.sympify(b["mu"]) for v in nuc.values() for b in v["branches"]]
emus = [sp.sympify(x) for v in ele.values() for x in v["eigen_minus_1"].values()]
hits = []
for a in mus:
    if sp.simplify(a-12)==0: hits.append(("mu", str(a)))
    for b in emus:
        if b != 0 and sp.simplify(a/b-12)==0: hits.append(("ratio", str(a), str(b)))
for a in mus:
    for b in mus:
        if b != 0 and sp.simplify(a/b-12)==0: hits.append(("n/p", str(a), str(b)))
res["twelve_hits"] = hits
res["verdict"] = "PASS" if hits else "scope-(a) negative: no 12 in the holonomy-connection class"
out = json.dumps(res, indent=2); print(out)
open(__file__.replace('.py','.out.json'),'w').write(out+"\n")
