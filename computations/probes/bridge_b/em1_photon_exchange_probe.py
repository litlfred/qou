"""EM1 photon-exchange probe (pre-registered in em1_preregistration.md). Exact over Q(q)."""
import sympy as sp
from sympy import kronecker_product as kp
from itertools import product
q = sp.symbols('q', positive=True)
hh = q - 1/q
R = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,hh,0],[0,0,0,q]]); Ri = R.inv()
I2 = sp.eye(2); H = sp.diag(1,-1); K = sp.diag(q,1/q)
def on(M, p):  # single-strand op at position p in 0..2
    m = [I2,I2,I2]; m[p] = M; return kp(kp(m[0],m[1]),m[2])
def gen(M, i): return kp(M, I2) if i == 1 else kp(I2, M)
K3 = kp(kp(K,K),K); Htot = on(H,0)+on(H,1)+on(H,2)
def Qat(p): return on(H,p)/2 + sp.eye(8)/6
def wsp(w): return [k for k in range(8) if Htot[k,k] == w]
def trw(M, w):
    idx = wsp(w); return sp.simplify((K3*M).extract(idx,idx).trace())
def E(word, w):
    L = [gen(R if s > 0 else Ri, i) for (i,s) in word]
    nL = len(L)
    # positions of quark a after t letters
    pos = [[0,1,2]]
    for (i,s) in word:
        cur = pos[-1][:]
        for a in range(3):
            if cur[a] == i-1: cur[a] = i
            elif cur[a] == i: cur[a] = i-1
        pos.append(cur)
    def prefix(t0, t1):
        M = sp.eye(8)
        for k in range(t0, t1): M = M*L[k]
        return M
    base = trw(prefix(0,nL), w)
    tot = 0; npairs = 0
    for t1 in range(nL):
        for t2 in range(t1, nL):
            npairs += 1
            for a, b in product(range(3), repeat=2):
                if a == b: continue
                M = prefix(0,t1)*Qat(pos[t1][a])*prefix(t1,t2)*Qat(pos[t2][b])*prefix(t2,nL)
                tot += trw(M, w)
    return sp.simplify(tot/npairs/base)
q0 = sp.Rational('1.1099785827513808')
V3 = [(1,+1),(2,-1)]*3
for name, word in [("V^3", V3), ("V^6", V3*2), ("identity (V^0)", [])]:
    if not word:
        # identity: no slots; use equal-time single slot
        Ep = sp.Rational(0); En = None
        print(name, ": equal-time only, constant by the pre-registration"); continue
    Ep = E(word, 1); En = E(word, -1)
    print(f"{name}: E(p) = {sp.factor(Ep)}")
    print(f"        E(n) = {sp.factor(En)}")
    print(f"   q=1: E(p) = {sp.limit(Ep, q, 1)}, E(n) = {sp.limit(En, q, 1)}")
    d = sp.simplify(En - Ep)
    print(f"   E(n)-E(p) = {sp.factor(d)}")
    print(f"   at q0: E(p) = {sp.N(Ep.subs(q,q0),12)}, E(n) = {sp.N(En.subs(q,q0),12)}, diff = {sp.N(d.subs(q,q0),12)}, q=1 diff = {sp.limit(d,q,1)}")
