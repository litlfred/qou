"""Pre-registered in PREREGISTRATION-ratio-class-2.md (committed 9ced266afbb before this ran)."""
import json, itertools, sympy as sp
q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2 = sp.eye(2)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
K1 = sp.diag(q, 1/q)
K = sp.kronecker_product(sp.kronecker_product(K1, K1), K1)
Xe = s0*s1*s0
V = s0*s1.inv(); XN = sp.simplify(V*V*V)
basis = list(itertools.product([0,1],[0,1],[0,1]))
sec = lambda nup: [i for i,b in enumerate(basis) if b.count(0)==nup]
Ee = sp.simplify(sum((K*Xe)[i,i] for i in range(8))/sum(K[i,i] for i in range(8)))
trKXe = sp.simplify(sum((K*Xe)[i,i] for i in range(8)))
def rep(r): r=sp.factor(sp.simplify(r)); return {"ratio":str(r),"at_q1":str(sp.simplify(r.subs(q,1))),"eq_12":bool(sp.simplify(r-12)==0)}
out = {"P1_pure_weight_states":{}, "P2_unnormalised_traces":{}, "P3_hecke_symmetriser":{}}
for name,nup in [("proton",2),("neutron",1)]:
    for i in sec(nup):
        out["P1_pure_weight_states"][f"{name}_{''.join('ud'[x] for x in basis[i])}"] = rep(((K*XN)[i,i]/K[i,i])/Ee)
    out["P2_unnormalised_traces"][name] = rep(sum((K*XN)[i,i] for i in sec(nup))/trKXe)
sym = sp.eye(8) + s0 + s1 + s0*s1 + s1*s0 + s0*s1*s0
XNs = sp.simplify(XN*sym)
for name,nup in [("proton",2),("neutron",1)]:
    idx = sec(nup)
    out["P3_hecke_symmetriser"][name] = rep((sum((K*XNs)[i,i] for i in idx)/sum(K[i,i] for i in idx))/Ee)
passed = [ (g,k) for g,d in out.items() for k,v in d.items() if v["eq_12"]]
out["verdict"] = "PASS: "+str(passed) if passed else "scope-(a) negative: no pre-registered variant gives 12 identically"
s = json.dumps(out, indent=2); print(s)
open(__file__.replace('.py','.out.json'),'w').write(s+"\n")
