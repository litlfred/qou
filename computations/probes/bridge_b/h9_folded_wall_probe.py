"""H9: folded (doubled-strand) wall. Exact rational arithmetic at fixed q (q0, 2, 3/2, and q=1)."""
import sympy as sp
from sympy import Rational as Qr
from functools import reduce
def run(q):
    h = q - 1/q
    R = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]); Ri = R.inv()
    I2 = sp.eye(2); K = sp.diag(q, 1/q)
    N = 6
    def gen(M, j):  # crossing on strands j, j+1 (1-based)
        return sp.kronecker_product(sp.kronecker_product(sp.eye(2**(j-1)), M), sp.eye(2**(N-j-1)))
    G = {j: gen(R, j) for j in range(1, N)}; Gi = {j: gen(Ri, j) for j in range(1, N)}
    def fold(i, sg):  # sigma_i of B_3 -> sigma_{3+i} sigma_{3-i}
        A = G if sg > 0 else Gi; return A[3+i]*A[3-i]
    word = [fold(i, sg) for (i, sg) in [(1,1),(2,-1)]*3]
    tau = G[3]
    K6 = reduce(sp.kronecker_product, [K]*N)
    wt = [sum(1 if (k >> (N-1-b)) & 1 == 0 else -1 for b in range(N)) for k in range(2**N)]
    def wts(k):
        bits = [1 if (k >> (N-1-b)) & 1 == 0 else -1 for b in range(N)]
        return sum(bits[3:]), sum(bits[:3])  # physical, mirror
    def tr(M, sel):
        KM = K6*M; return sum(KM[k,k] for k in range(2**N) if sel(*wts(k)))
    def prod(L):
        M = sp.eye(2**N)
        for X in L: M = M*X
        return M
    closed = prod(word)
    out = {}
    for name, selp, seln in [("R-sum", lambda a,b: a==1, lambda a,b: a==-1),
                             ("R-iota", lambda a,b: a==1 and b==-1, lambda a,b: a==-1 and b==1)]:
        Tp, Tn = tr(closed, selp), tr(closed, seln)
        Ds = set(); Bs = []
        for t in range(len(word)+1):
            W = prod(word[:t] + [tau] + word[t:])
            Bp, Bn = tr(W, selp), tr(W, seln)
            Bs.append((Bp, Bn))
            Ds.add(sp.nsimplify(((Tn+Bn)/(Tp+Bp))/(Tn/Tp)) if Tp != 0 and Tn != 0 and Tp+Bp != 0 else None)
        out[name] = (Tp, Tn, Bs, Ds)
    return out
from qou_substrate.constants import Q_50_DIGIT_STR
q0 = sp.Rational(Q_50_DIGIT_STR)
for label, qv in [("q=1", sp.Integer(1)), ("q=3/2", Qr(3,2)), ("q=2", sp.Integer(2)), ("q0", q0)]:
    res = run(qv)
    for name, (Tp, Tn, Bs, Ds) in res.items():
        ratio = (Tp/Tn) if Tn != 0 else None
        print(f"{label} {name}: T_p/T_n = {sp.N(ratio,20) if ratio is not None else 'n/a (T_n=0)'}; q^2 = {sp.N(qv**2,20)}; "
              f"slot-independent B: {len(set(Bs))==1}; D values = {[sp.N(d,20) if d is not None else None for d in Ds]}")
