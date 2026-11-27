"""Pre-registered in PREREGISTRATION-d2-leading-count.md (e819fb1277c). Exact sympy, no floats.

D = q^-1 (hol - 1) + (1 - q^-1) T3 on W_p (+) W_n of (C^2)^{x3}; h = q - q^-1.
N = lim_{q->1} tr(D^2)/h^2, its W_p / W_n split, and rank of D1 = lim D/h.
"""
import json, itertools, sympy as sp

q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2 = sp.eye(2)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
hol = sp.simplify((s0*s1.inv())**3)
basis = list(itertools.product([0,1], repeat=3))   # 0 = up
T3 = sp.diag(*[sp.Rational(b.count(0) - b.count(1), 2) for b in basis])
D = sp.simplify((hol - sp.eye(8))/q + (1 - 1/q)*T3)
h = q - 1/q
res = {"preregistration": "e819fb1277c", "checks": {}}
res["checks"]["hecke"] = sp.simplify((Rc-q*sp.eye(4))*(Rc+sp.eye(4)/q)) == sp.zeros(4)
out = {}
D1_blocks = []
for name, nup in (("W_p", 2), ("W_n", 1)):
    idx = [i for i,b in enumerate(basis) if b.count(0) == nup]
    other = [i for i in range(8) if i not in idx]
    res["checks"][f"{name} invariant"] = sp.simplify(D.extract(other, idx)) == sp.zeros(5, 3)
    Dw = D.extract(idx, idx)
    D1 = sp.simplify((Dw/h).applyfunc(lambda e: sp.limit(e, q, 1)))
    D1_blocks.append(D1)
    tr2 = sp.factor(sp.simplify((Dw*Dw).trace()))
    lim = sp.limit(tr2/h**2, q, 1)
    res["checks"][f"{name}: lim tr(D^2)/h^2 = tr(D1^2)"] = sp.simplify(lim - (D1*D1).trace()) == 0
    out[name] = {"tr_D2": str(tr2), "lim_tr_D2_over_h2": str(lim), "D1": str(D1.tolist()),
                 "rank_D1": D1.rank()}
D1 = sp.diag(*D1_blocks)
N = sp.nsimplify((D1*D1).trace())
res["W_p"], res["W_n"] = out["W_p"], out["W_n"]
res["N"] = str(N); res["rank_D1"] = D1.rank()
res["N_if_unit_1_minus_qinv"] = str(4*N)
res["all_checks_pass"] = all(res["checks"].values())
res["verdict"] = ("N = 12: mechanism candidate only (depends on unit h and on nabla = hol - 1)"
                  if N == 12 else f"scope-(a) negative: N = {N}, not 12, for this one definition")
s = json.dumps(res, indent=2); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
