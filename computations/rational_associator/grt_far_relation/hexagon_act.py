# Exact over Q (fractions.Fraction), in U(t3) truncated by degree. Bean qou-3fdg, stage 3e.
# 1. Solve the hexagon (repo form, LowDegree.lean)
#      e^{(t13+t23)/2} = phi(t13,t12) e^{t13/2} phi(t23,t13) e^{t23/2} phi(t12,t23)
#    degree by degree for a group-like phi = exp(psi), psi Lie, psi_2 = [X,Y]/24.
# 2. With g = exp(sigma3), sigma3 = [X,[X,Y]] + [Y,[X,Y]], check that
#      phi~(A,B) = phi(g A g^-1, B) g
#    satisfies the same hexagon, and that the transported-family identities used in
#    HexagonAction.lean hold: (5.14) G2 G3 G1 = 1 and G1 t13 G1^-1 + G3^-1 t23 G3 = t13 + t23.
# 3. Control: g = exp([X,Y]) (fails (5.14)) breaks the hexagon of phi~.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from t3 import add, sc, mul, br, U, V, W, ONE, X, Y, iszero, ev, inv1, expL, conj, conjR, RED, ideal_red
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5
T12, T13, T23 = U, V, W

def lb(a, b): return br(a, b, 12)
def lyndon(k):
    # a spanning set of degree-k Lie monomials in X, Y (right-normed brackets)
    out = []
    import itertools
    for w in itertools.product([0, 1], repeat=k):
        if w[-1] == w[-2]: continue
        e = X if w[-1] == 0 else Y
        e2 = X if w[-2] == 0 else Y
        cur = lb(e2, e)
        for l in reversed(w[:-2]): cur = lb(X if l == 0 else Y, cur)
        if cur: out.append(cur)
    # reduce to a basis
    basis, rows = [], []
    for v in out:
        if indep(rows, v): basis.append(v); rows.append(v)
    return basis
def indep(rows, v):
    keys = sorted({k for r in rows + [v] for k in r})
    M = [[r.get(k, 0) for k in keys] for r in rows + [v]]
    return rank(M) == len(M)
def rank(M):
    M = [row[:] for row in M]; r = 0
    for c in range(len(M[0]) if M else 0):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = Fr(M[i][c]) / M[r][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r
def expHalf(x, D): return expL(sc(Fr(1, 2), x), D)
def hexres(phi_at, D):
    lhs = expHalf(add(T13, T23), D)
    rhs = ONE
    for f in [phi_at(T13, T12), expHalf(T13, D), phi_at(T23, T13), expHalf(T23, D), phi_at(T12, T23)]:
        rhs = mul(rhs, f, D)
    return add(lhs, sc(-1, rhs))
def part(x, d): return {k: v for k, v in x.items() if len(k) == d}
def reduce_deg(x, d):
    if d not in RED: RED[d] = ideal_red(d)
    return RED[d][0](part(x, d))

# 1. solve psi degree by degree
psi = sc(Fr(1, 24), lb(X, Y))
for d in range(3, DMAX + 1):
    base = reduce_deg(hexres(lambda a, b: ev(expL(psi, d), a, b, d), d), d)
    B = lyndon(d)
    cols = []
    for bvec in B:
        trial = add(psi, bvec)
        r = reduce_deg(hexres(lambda a, b: ev(expL(trial, d), a, b, d), d), d)
        cols.append(add(r, sc(-1, base)))  # linear in the degree-d coefficient
    keys = sorted({k for c in cols + [base] for k in c})
    A = [[c.get(k, 0) for c in cols] + [-base.get(k, 0)] for k in keys]
    # Gauss-Jordan over Q
    n = len(B); r = 0; piv = []
    for c in range(n):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]; f = Fr(1) / A[r][c]; A[r] = [f * a for a in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                g_ = A[i][c]; A[i] = [a - g_ * b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
    if any(row[-1] != 0 for row in A[r:]):
        print('degree', d, ': hexagon has no solution extending the lower degrees'); sys.exit(1)
    coef = [Fr(0)] * n
    for i, c in enumerate(piv): coef[c] = A[i][-1]
    for cf, bvec in zip(coef, B): psi = add(psi, sc(cf, bvec))
    print('degree', d, ': solved, free parameters', n - len(piv))
D = DMAX
phi = expL(psi, D)
print('phi hexagon to degree', D, ':', iszero(hexres(lambda a, b: ev(phi, a, b, D), D), D))

def act(phi, gp, D):
    def at(a, b):
        G = ev(gp, a, b, D)
        return mul(G, ev(phi, a, conj(G, b, D), D), D)   # G phi(a, G^-1 b G)
    return at
sig3 = add(lb(X, lb(X, Y)), lb(Y, lb(X, Y)))
for name, l in [('exp(sigma3)', sig3), ('exp([X,Y])', lb(X, Y))]:
    gp = expL(l, D)
    G1, G2, G3 = ev(gp, T13, T12, D), ev(gp, T23, T13, D), ev(gp, T12, T23, D)
    h514 = add(mul(mul(G2, G3, D), G1, D), sc(-1, ONE))
    tr = add(conjR(G1, T13, D), conj(G3, T23, D), sc(-1, add(T13, T23)))
    print(name, ': (5.14) G2G3G1=1', iszero(h514, D), '| G1 t13 G1^-1 + G3^-1 t23 G3 = t13+t23',
          iszero(tr, D), '| hexagon of phi~', iszero(hexres(act(phi, gp, D), D), D))
