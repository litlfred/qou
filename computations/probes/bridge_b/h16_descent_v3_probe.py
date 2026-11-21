"""H16: six-strand doubled V^3 through the KL descent; compare with the folded word; evaluate with the H8 functional."""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
ns = {}; exec(open(os.path.join(here, "h14_kl_folding_probe.py")).read().split("n = 6\namb_gens")[0], ns)
kl_basis, compose, coxeter, padd, pmul = ns["kl_basis"], ns["compose"], ns["coxeter"], ns["padd"], ns["pmul"]
import sympy as sp
n = 6
def s(j):
    p = list(range(n)); p[j-1], p[j] = p[j], p[j-1]; return tuple(p)
one = tuple(range(n))

def make_alg(gens, L):
    length = coxeter(gens, n)
    def left_T(ti, X):
        g = gens[ti]; vt = {L[ti]: 1, -L[ti]: -1}; R = {}
        for y, a in X.items():
            ty = compose(g, y); R[ty] = padd(R.get(ty, {}), a)
            if length[ty] < length[y]: R[y] = padd(R.get(y, {}), pmul(vt, a))
        return {k: v for k, v in R.items() if v}
    def left_Tinv(ti, X):   # T^-1 = T - (v^L - v^-L)
        R = left_T(ti, X); vt = {L[ti]: 1, -L[ti]: -1}
        for y, a in X.items(): R[y] = padd(R.get(y, {}), pmul(vt, a), -1)
        return {k: v for k, v in R.items() if v}
    return length, left_T, left_Tinv

def word_elem(ops, left_T, left_Tinv):
    X = {one: {0: 1}}
    for ti, sg in reversed(ops):     # left-multiply from the right end
        X = left_T(ti, X) if sg > 0 else left_Tinv(ti, X)
    return X

def to_c(X, C, length):
    X = {k: dict(v) for k, v in X.items()}; out = {}
    while X:
        x = max(X, key=lambda y: length[y]); a = X[x]; out[x] = a
        for y, p in C[x].items():
            X[y] = padd(X.get(y, {}), pmul(a, p), -1)
            if not X[y]: del X[y]
    return out

# ambient
amb = [s(j) for j in range(1, 6)]
Ca, la = kl_basis(amb, [1]*5, n)
_, aT, aTi = make_alg(amb, [1]*5)
idx = {j: j-1 for j in range(1, 6)}
V3_amb = [(idx[2], 1), (idx[4], 1), (idx[1], -1), (idx[5], -1)] * 3
XT = word_elem(V3_amb, aT, aTi); XB = word_elem([(idx[3], 1)] + V3_amb, aT, aTi)
# folded
tau, b1, b2 = s(3), compose(s(2), s(4)), compose(s(1), s(5))
fg, fL = [tau, b1, b2], [1, 2, 2]
Cf, lf = kl_basis(fg, fL, n)
_, fT, fTi = make_alg(fg, fL)
V3_f = [(1, 1), (2, -1)] * 3
ZT = word_elem(V3_f, fT, fTi); ZB = word_elem([(0, 1)] + V3_f, fT, fTi)

res = {}
for name, X, Z in (("closed", XT, ZT), ("open", XB, ZB)):
    ac = to_c(X, Ca, la); zc = to_c(Z, Cf, lf)
    phi = {x: a for x, a in ac.items() if x in Cf}
    keys = set(phi) | set(zc)
    mod2 = all(all((phi.get(x, {}).get(e, 0) - zc.get(x, {}).get(e, 0)) % 2 == 0
                   for e in set(phi.get(x, {})) | set(zc.get(x, {}))) for x in keys)
    equal = all(phi.get(x, {}) == zc.get(x, {}) for x in keys)
    dropped = sum(1 for x in ac if x not in Cf)
    print(f"{name}: ambient KL terms {len(ac)}, swapped (dropped) {dropped}; 1. mod-2 agreement Phi(X) vs Z: {mod2}; 2. Phi(X) == Z: {equal}")
    # back to folded T basis
    def from_c(cc):
        T = {}
        for x, a in cc.items():
            for y, p in Cf[x].items(): T[y] = padd(T.get(y, {}), pmul(a, p))
        return {k: v for k, v in T.items() if v}
    res[name] = (from_c(phi), Z)

# H8 representation
v = sp.symbols('v', positive=True)
Qb = v**2; h = Qb - 1/Qb
R = sp.Matrix([[Qb,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,Qb]])
I2 = sp.eye(2); kp = sp.kronecker_product
sw = v - 1/v
Kw = sp.Matrix([[sw, 1], [1, 0]])
rep = {0: kp(kp(Kw, I2), I2), 1: kp(R, I2), 2: kp(I2, R)}
Rp = rep[1]
chk = [sp.simplify(rep[1]*rep[2]*rep[1] - rep[2]*rep[1]*rep[2]) == sp.zeros(8),
       sp.simplify((rep[0]-v*sp.eye(8))*(rep[0]+sp.eye(8)/v)) == sp.zeros(8),
       sp.simplify(rep[0]*Rp*rep[0]*Rp - Rp*rep[0]*Rp*rep[0]) == sp.zeros(8)]
print("3. sanity in H8 rep: bulk braid, wall quadratic, type-B relation:", chk)
# reduced words for folded elements
from collections import deque
red = {one: []}; Qd = deque([one])
while Qd:
    w = Qd.popleft()
    for ti, g in enumerate(fg):
        x = compose(g, w)
        if x not in red and lf[x] == lf[w] + 1: red[x] = [ti] + red[w]; Qd.append(x)
def mat(Tel):
    M = sp.zeros(8)
    for x, p in Tel.items():
        coeff = sum(c*v**e for e, c in p.items())
        P = sp.eye(8)
        for ti in red[x]: P = P*rep[ti]
        M += coeff*P
    return M
K = sp.diag(Qb, 1/Qb); K3 = kp(kp(K, K), K)
H = sp.diag(1, -1); Htot = kp(kp(H, I2), I2) + kp(kp(I2, H), I2) + kp(kp(I2, I2), H)
def tr(M, w, v0):
    ids = [k for k in range(8) if Htot[k, k] == w]
    return ((K3*M).subs(v, v0)).extract(ids, ids).trace()
from qou_substrate.constants import Q_50_DIGIT_STR
q0 = sp.Rational(Q_50_DIGIT_STR)
for label, pick in (("folded word Z (Lusztig descent)", 1), ("naive descent Phi(X)", 0)):
    MT = mat(res["closed"][pick]); MB = mat(res["open"][pick])
    for vv, lab in ((q0, "q0"), (sp.Rational(1000001, 1000000), "q~1")):
        Tp, Tn, Bp, Bn = tr(MT, 1, vv), tr(MT, -1, vv), tr(MB, 1, vv), tr(MB, -1, vv)
        D = ((Tn + Bn)/(Tp + Bp))/(Tn/Tp)
        print(f"  {label} at {lab}: D = {sp.N(D, 20)}")
