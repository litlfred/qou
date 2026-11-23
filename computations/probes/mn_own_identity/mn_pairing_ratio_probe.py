"""Pre-registered in PREREGISTRATION-pairing-ratio-and-mirror.md (part A).

Mixed-state matter expectation <X> = tr(K X)/tr(K) on a sector, exact Q(q).
Electron X_e = rho(s0 s1 s0); nucleon X_N = rho((s0 s1^-1)^3). Ratio vs 12.
Exact sympy throughout; no floats.
"""
import json, itertools, sympy as sp

q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2 = sp.eye(2)
s0 = sp.kronecker_product(Rc, I2)
s1 = sp.kronecker_product(I2, Rc)
s1i = s1.inv()
K1 = sp.diag(q, 1/q)
K = sp.kronecker_product(sp.kronecker_product(K1, K1), K1)

Xe = s0*s1*s0
Vw = s0*s1i
XN = sp.simplify(Vw*Vw*Vw)

basis = list(itertools.product([0,1],[0,1],[0,1]))  # 0 = up (weight q), 1 = down
def sector(nup):
    return [i for i,b in enumerate(basis) if b.count(0)==nup]
def ev(X, idx):
    num = sum(((K*X)[i,i]) for i in idx)
    den = sum(K[i,i] for i in idx)
    return sp.simplify(num/den)

checks = {}
allidx = list(range(8))
Ee = ev(Xe, allidx)
res = {}
for name, idxN in [("E1_whole", allidx), ("E2_proton_sector", sector(2)), ("E2_neutron_sector", sector(1))]:
    EN = ev(XN, idxN)
    r = sp.factor(sp.simplify(EN/Ee))
    res[name] = {"nucleon_expectation": str(sp.factor(EN)), "ratio": str(r),
                 "ratio_at_q1": str(sp.simplify(r.subs(q,1))),
                 "ratio_eq_12_identically": bool(sp.simplify(r-12)==0)}
res["electron_expectation_whole"] = str(sp.factor(Ee))
# sanity checks
checks["hecke_relation"] = bool(sp.simplify((Rc-q*sp.eye(4))*(Rc+sp.eye(4)/q))==sp.zeros(4))
checks["braid_relation"] = bool(sp.simplify(s0*s1*s0 - s1*s0*s1)==sp.zeros(8))
checks["K_commutes_with_braids"] = bool(sp.simplify(K*s0-s0*K)==sp.zeros(8))
res["checks"] = checks
res["verdict"] = ("PASS" if any(v.get("ratio_eq_12_identically") for k,v in res.items() if isinstance(v,dict) and "ratio" in v)
                  else "scope-(a) negative: no sector in the pre-registered class gives ratio 12")
out = json.dumps(res, indent=2)
print(out)
open(__file__.replace('.py','.out.json'),'w').write(out+"\n")
