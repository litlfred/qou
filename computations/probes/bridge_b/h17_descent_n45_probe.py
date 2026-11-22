"""H17: Lusztig descent at n = 4 (weight-1 wall) and n = 5 (weight-3 wall). See h17_preregistration.md."""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
ns = {}; exec(open(os.path.join(here, "h14_kl_folding_probe.py")).read().split("n = 6\namb_gens")[0], ns)
kl_basis, compose, coxeter, padd, pmul = ns["kl_basis"], ns["compose"], ns["coxeter"], ns["padd"], ns["pmul"]
import sympy as sp
from collections import deque

def run(n, b_amb, w_amb):
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
        def left_Tinv(ti, X):
            R = left_T(ti, X); vt = {L[ti]: 1, -L[ti]: -1}
            for y, a in X.items(): R[y] = padd(R.get(y, {}), pmul(vt, a), -1)
            return {k: v for k, v in R.items() if v}
        return length, left_T, left_Tinv
    def word_elem(ops, lT, lTi):
        X = {one: {0: 1}}
        for ti, sg in reversed(ops):
            X = lT(ti, X) if sg > 0 else lTi(ti, X)
        return X
    def to_c(X, C, length):
        X = {k: dict(v) for k, v in X.items()}; out = {}
        while X:
            x = max(X, key=lambda y: length[y]); a = X[x]; out[x] = a
            for y, p in C[x].items():
                X[y] = padd(X.get(y, {}), pmul(a, p), -1)
                if not X[y]: del X[y]
        return out
    amb = [s(j) for j in range(1, n)]
    Ca, la = kl_basis(amb, [1]*(n-1), n)
    _, aT, aTi = make_alg(amb, [1]*(n-1))
    def amb_letter(word, sg):   # T_word or its inverse, as ambient ops (left to right)
        ops = [(j-1, 1) for j in word]
        return ops if sg > 0 else [(j-1, -1) for j in reversed(word)]
    X_ops = (amb_letter(b_amb, 1) + amb_letter(w_amb, -1)) * 3
    X = word_elem(X_ops, aT, aTi)
    def prod(word):
        g = one
        for j in word: g = compose(g, s(j))
        return g
    bg, wg = prod(b_amb), prod(w_amb)
    Lb, Lw = len(b_amb), len(w_amb)
    fg, fL = [bg, wg], [Lb, Lw]
    Cf, lf = kl_basis(fg, fL, n)
    _, fT, fTi = make_alg(fg, fL)
    Z = word_elem([(0, 1), (1, -1)] * 3, fT, fTi)
    ac = to_c(X, Ca, la); zc = to_c(Z, Cf, lf)
    phi = {x: a for x, a in ac.items() if x in Cf}
    keys = set(phi) | set(zc)
    mod2 = all(all((phi.get(x, {}).get(e, 0) - zc.get(x, {}).get(e, 0)) % 2 == 0
                   for e in set(phi.get(x, {})) | set(zc.get(x, {}))) for x in keys)
    equal = all(phi.get(x, {}) == zc.get(x, {}) for x in keys)
    dropped = sum(1 for x in ac if x not in Cf)
    print(f"n = {n}: weights (b, w) = ({Lb}, {Lw}); |W| = {len(lf)}; ambient KL terms {len(ac)}, swapped (dropped) {dropped}")
    print(f"  1. Phi(X) = Z mod 2: {mod2}")
    print(f"  2. Phi(X) == Z: {equal}")
    def from_c(cc):
        T = {}
        for x, a in cc.items():
            for y, p in Cf[x].items(): T[y] = padd(T.get(y, {}), pmul(a, p))
        return {k: v for k, v in T.items() if v}
    phiT = from_c(phi)
    # 3. two-strand model
    v = sp.symbols('v', positive=True)
    Qb = v**2; h = Qb - 1/Qb
    R = sp.Matrix([[Qb,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,Qb]])
    sw = v**Lw - v**(-Lw)
    Kw = sp.kronecker_product(sp.Matrix([[sw, 1], [1, 0]]), sp.eye(2))
    quad = sp.simplify((Kw - v**Lw*sp.eye(4))*(Kw + sp.eye(4)/v**Lw)) == sp.zeros(4)
    rel = sp.simplify(Kw*R*Kw*R - R*Kw*R*Kw) == sp.zeros(4)
    bquad = sp.simplify((R - Qb*sp.eye(4))*(R + sp.eye(4)/Qb)) == sp.zeros(4)
    print(f"  3. two-strand model, wall weight {Lw}: bulk quadratic {bquad}, wall quadratic {quad}, B2 relation KRKR = RKRK {rel}")
    if not rel:
        print("     no weight-%d wall in this model; no trace reported" % Lw)
        return
    rep = {0: R, 1: Kw}
    red = {one: []}; Qd = deque([one])
    while Qd:
        w = Qd.popleft()
        for ti, g in enumerate(fg):
            x = compose(g, w)
            if x not in red: red[x] = [ti] + red[w]; Qd.append(x)   # BFS: first visit is a reduced word in W
    def mat(Tel):
        M = sp.zeros(4)
        for x, p in Tel.items():
            coeff = sum(c*v**e for e, c in p.items()); P = sp.eye(4)
            for ti in red[x]: P = P*rep[ti]
            M += coeff*P
        return M
    K = sp.diag(Qb, 1/Qb); K2 = sp.kronecker_product(K, K)
    Hd = [2, 0, 0, -2]
    from qou_substrate.constants import Q_50_DIGIT_STR
    q0 = sp.Rational(Q_50_DIGIT_STR)
    for label, T in (("folded Z", Z), ("naive Phi(X)", phiT)):
        M = K2*mat(T)
        for vv, lab in ((q0, "q0"), (sp.Rational(1000001, 1000000), "q~1")):
            Mv = M.subs(v, vv)
            parts = {wt: sp.N(sum(Mv[k, k] for k in range(4) if Hd[k] == wt), 20) for wt in (2, 0, -2)}
            print(f"     {label} at {lab}: weight-space traces {parts}")

run(4, [1, 3], [2])
run(5, [1, 4], [2, 3, 2])
