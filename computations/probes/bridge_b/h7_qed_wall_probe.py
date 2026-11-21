"""H7 part B: the M_QED (charge-pair) functional of EM1 with one strand-1 type-B wall inserted.
Exact over Q(q, s, p, Y): wall K = [[s, 1], [-p, 0]] (d = 0 branch, s = x+y, p = xy), Q_a = H_a/2 + Y/2.
Word V^3 = (s1 s2^-1)^3 = gamma(0,0,qh) gamma(0,0,-q^-1 h) (ruled photon)."""
import sympy as sp
from sympy import kronecker_product as kp
from itertools import product
q, s, p, Y = sp.symbols('q s p Y')
hh = q - 1/q
R = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,hh,0],[0,0,0,q]]); Ri = sp.simplify(R.inv())
I2 = sp.eye(2); H = sp.diag(1,-1); K = sp.diag(q,1/q)
Kw = sp.Matrix([[s,1],[-p,0]])
def on(M, k):
    m = [I2,I2,I2]; m[k] = M; return kp(kp(m[0],m[1]),m[2])
def gen(M, i): return kp(M, I2) if i == 1 else kp(I2, M)
K3 = kp(kp(K,K),K); Htot = on(H,0)+on(H,1)+on(H,2)
W = on(Kw, 0)
def Qat(k): return on(H,k)/2 + Y/2*sp.eye(8)
def trw(M, w):
    idx = [k for k in range(8) if Htot[k,k] == w]
    return sp.expand((K3*M).extract(idx,idx).trace())
word = [(1,+1),(2,-1)]*3
L = [gen(R if sg > 0 else Ri, i) for (i,sg) in word]; n = len(L)
pos = [[0,1,2]]
for (i,sg) in word:
    cur = pos[-1][:]
    for a in range(3):
        if cur[a] == i-1: cur[a] = i
        elif cur[a] == i: cur[a] = i-1
    pos.append(cur)
def run(tw):
    """Wall inserted at letter boundary tw (before letter tw); at a tie the wall acts first."""
    def build(ins):  # ins: dict slot -> list of operators applied in order
        M = sp.eye(8)
        for t in range(n+1):
            for O in ins.get(t, []): M = M*O
            if t < n: M = M*L[t]
        return M
    out = {}
    for w in (1, -1):
        base = trw(build({tw: [W]}), w)
        tot = 0; npairs = 0
        for t1 in range(n):
            for t2 in range(t1, n):
                npairs += 1
                for a, b in product(range(3), repeat=2):
                    if a == b: continue
                    ins = {}
                    ins.setdefault(tw, []).append(W)
                    ins.setdefault(t1, []).append(Qat(pos[t1][a]))
                    ins.setdefault(t2, []).append(Qat(pos[t2][b]))
                    tot += trw(build(ins), w)
        out[w] = (sp.factor(base), sp.factor(sp.cancel(tot/npairs/base)))
    return out
from qou_substrate.constants import Q_50_DIGIT_STR
q0 = sp.Rational(Q_50_DIGIT_STR)
res = {}
for tw in range(n+1):
    res[tw] = run(tw)
    Ep, En = res[tw][1][1], res[tw][-1][1]
    print(f"wall at slot {tw}: depends on p (=xy)? {sp.diff(Ep,p)!=0 or sp.diff(En,p)!=0}; on s? {sp.diff(Ep,s)!=0 or sp.diff(En,s)!=0}")
Ep, En = res[0][1][1], res[0][-1][1]
same = all(sp.simplify(res[t][1][1]-Ep)==0 and sp.simplify(res[t][-1][1]-En)==0 for t in res)
print("same for all 7 wall slots:", same)
print("E_wall(p) =", sp.factor(Ep)); print("E_wall(n) =", sp.factor(En))
d = sp.factor(sp.simplify(En-Ep)); print("E_wall(n)-E_wall(p) =", d)
print("q=1: E(p) =", sp.factor(sp.limit(Ep,q,1)), " E(n) =", sp.factor(sp.limit(En,q,1)), " diff =", sp.factor(sp.limit(En-Ep,q,1)))
for Yv in (sp.Rational(1,3), sp.Rational(-1,3)):
    print(f"[conditional on Y={Yv}] at q0: E(p)={sp.N(Ep.subs({q:q0,Y:Yv}),15)}, E(n)={sp.N(En.subs({q:q0,Y:Yv}),15)}, diff={sp.N(d.subs({q:q0,Y:Yv}),15)}")
