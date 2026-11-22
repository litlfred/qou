"""H8: open categorical trace = closed pivotal trace + boundary trace (same lambda), word V^3.
Exact sympy. Wall K = [[s,1],[-p,0]] at strand 1 (d = 0 branch); boundary trace is proportional to s."""
import sympy as sp
from sympy import kronecker_product as kp
q, s, p = sp.symbols('q s p')
h = q - 1/q
R = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]); Ri = sp.simplify(R.inv())
I2 = sp.eye(2); H = sp.diag(1,-1); K = sp.diag(q,1/q)
def on(M,k):
    m=[I2,I2,I2]; m[k]=M; return kp(kp(m[0],m[1]),m[2])
K3 = kp(kp(K,K),K); Htot = on(H,0)+on(H,1)+on(H,2)
g = lambda M,i: kp(M,I2) if i==1 else kp(I2,M)
M = sp.eye(8)
for (i,sg) in [(1,1),(2,-1)]*3: M = M*g(R if sg>0 else Ri, i)
W = on(sp.Matrix([[s,1],[-p,0]]),0)
def tr(X,w):
    idx=[k for k in range(8) if Htot[k,k]==w]; return sp.factor(sp.simplify((K3*X).extract(idx,idx).trace()))
Tp, Tn = tr(M,1), tr(M,-1)
Bp, Bn = tr(M*W,1), tr(M*W,-1)
print("closed: T_p =", Tp, "; T_n =", Tn, "; T_p/T_n =", sp.factor(Tp/Tn))
print("boundary: B_p =", Bp, "; B_n =", Bn, "; free of p:", sp.diff(Bp,p)==0 and sp.diff(Bn,p)==0)
D = sp.factor(sp.simplify(((Tn+Bn)/(Tp+Bp))/(Tn/Tp)))
print("D(s) =", D)
from qou_substrate.constants import Q_50_DIGIT_STR
q0 = sp.Rational(Q_50_DIGIT_STR)
cands = {"N1 folding s=h": h, "N2 involutive s=0": sp.Integer(0),
         "N3 unit Markov s=(q^2+1)/q^2": (q**2+1)/q**2, "N4 qdim s=[2]/q": (q+1/q)/q}
for k,v in cands.items():
    Dv = sp.factor(sp.simplify(D.subs(s,v)))
    print(f"{k}: D = {Dv}; q=1 -> {sp.limit(Dv,q,1)}; q0 -> {sp.N(Dv.subs(q,q0),20)}")
