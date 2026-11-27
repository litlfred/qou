# Exact over Q (fractions.Fraction). Bean qou-3fdg, stage-4 blocker.
# The exponential for Drinfeld's group law (5.16), (g1 o g2)(A,B) = g1(g2 A g2^-1, B) g2.
# A one-parameter subgroup g_s (g_s o g_e = g_{s+e}) with leading term s*psi solves the linear
# ODE  d/ds g_s = D(g_s) + g_s psi,  D the derivation of Q<A,B> with D(A) = psi A - A psi, D(B) = 0.
# So Exp(psi) = sum_k L^k(1)/k!,  L(x) = D(x) + x psi.  (Graded: L raises degree, the sum is finite
# modulo degree N.)
# Checks, in U(t3) and U(t4) by an exact normal form (t4 = F(t14,t24,t34) semidirect t3,
# U(t3) = U(free(t12,t23)) (x) Q[c3], c3 = t12+t13+t23):
#   (5.12) g(u,v) g(v,u) = 1         [repo name: (5.13)]
#   (5.13) g(w,u) g(v,w) g(u,v) = 1  [repo name: (5.14), the mu = 0 hexagon]
#   (5.14) TCompat                    [Drinfeld's (5.14); repo name: TCompat]
#   (5.15) pentagon in U(t4)
# for Exp(sigma3) and, as a control, for exp(sigma3) (ordinary exponential of series).
import sys, itertools
from fractions import Fraction as Fr
from functools import lru_cache
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6

# ---------- free algebra Q<X,Y>: dict word(tuple of 0/1) -> Fr ----------
def fadd(*xs):
    r = {}
    for x in xs:
        for k, v in x.items(): r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}
def fsc(c, x): return {k: c * v for k, v in x.items() if c * v}
def fmul(a, b, D):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            if len(k1) + len(k2) <= D: r[k1 + k2] = r.get(k1 + k2, 0) + v1 * v2
    return {k: v for k, v in r.items() if v}
FX = {(0,): Fr(1)}; FY = {(1,): Fr(1)}; F1 = {(): Fr(1)}
def fbr(a, b, D): return fadd(fmul(a, b, D), fsc(-1, fmul(b, a, D)))
def fexp(l, D):
    r = dict(F1); t = dict(F1)
    for k in range(1, D + 1):
        t = fsc(Fr(1, k), fmul(t, l, D)); r = fadd(r, t)
    return r
def Exp516(psi, D):
    dA = fbr(psi, FX, D)
    def Dder(x):
        r = {}
        for w, c in x.items():
            for i, l in enumerate(w):
                if l == 0:
                    term = fmul(fmul({w[:i]: c}, dA, D), {w[i + 1:]: Fr(1)}, D)
                    r = fadd(r, term)
        return r
    L = lambda x: fadd(Dder(x), fmul(x, psi, D))
    r = dict(F1); t = dict(F1)
    for k in range(1, D + 1):
        t = fsc(Fr(1, k), L(t)); r = fadd(r, t)
    return r

# ---------- U(t4) normal form ----------
# F letters: 4 = t14, 5 = t24, 6 = t34 ; T letters: 1 = t12, 3 = t23, 9 = c3 (central in t3)
# element: dict (fword, tword, k) -> Fr  meaning fword * tword * c3^k
def br2(a, b): return {(a, b): Fr(1), (b, a): Fr(-1)}
AD = {  # ad_x on F generators, as F-polynomials {fword: coeff}
    1: {4: br2(4, 5), 5: br2(5, 4), 6: {}},
    2: {4: br2(4, 6), 5: {}, 6: br2(6, 4)},     # t13
    3: {4: {}, 5: br2(5, 6), 6: br2(6, 5)},
}
def padd(*xs):
    r = {}
    for x in xs:
        for k, v in x.items(): r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}
AD[9] = {g: padd(AD[1][g], AD[2][g], AD[3][g]) for g in (4, 5, 6)}
def Dx(x, fw):  # derivation ad_x on an F word -> F polynomial
    r = {}
    for i, l in enumerate(fw):
        for w, c in AD[x][l].items():
            nw = fw[:i] + w + fw[i + 1:]; r[nw] = r.get(nw, 0) + c
    return {k: v for k, v in r.items() if v}
@lru_cache(maxsize=None)
def moveT(xs, fw):
    # xs (tuple of T letters, in order) times F word fw  ->  tuple of ((fword, xs'), coeff)
    if not xs or not fw: return (((fw, xs), Fr(1)),)
    x = xs[-1]; r = {}
    for (f2, x2), c in moveT(xs[:-1], fw):
        r[(f2, x2 + (x,))] = r.get((f2, x2 + (x,)), 0) + c
    for w, c in Dx(x, fw).items():
        for (f2, x2), c2 in moveT(xs[:-1], w):
            r[(f2, x2)] = r.get((f2, x2), 0) + c * c2
    return tuple((k, v) for k, v in r.items() if v)
def tnorm(xs):
    k = xs.count(9); return tuple(l for l in xs if l != 9), k
def emul(a, b, D):
    r = {}
    for (f1, t1, k1), c1 in a.items():
        for (f2, t2, k2), c2 in b.items():
            if len(f1) + len(t1) + k1 + len(f2) + len(t2) + k2 > D: continue
            xs = t1 + (9,) * k1
            for (fm, xm), c3 in moveT(xs, f2):
                tw, kk = tnorm(xm + t2)
                key = (f1 + fm, tw, kk + k2)
                r[key] = r.get(key, 0) + c1 * c2 * c3
    return {k: v for k, v in r.items() if v}
E1 = {((), (), 0): Fr(1)}
t12 = {((), (1,), 0): Fr(1)}; t23 = {((), (3,), 0): Fr(1)}; c3 = {((), (), 1): Fr(1)}
t13 = padd(c3, {k: -v for k, v in t12.items()}, {k: -v for k, v in t23.items()})
t14 = {((4,), (), 0): Fr(1)}; t24 = {((5,), (), 0): Fr(1)}; t34 = {((6,), (), 0): Fr(1)}
def esc(c, x): return {k: c * v for k, v in x.items() if c * v}
def ev(p, a, b, D):
    cache = {(): E1}
    r = {}
    for w, c in sorted(p.items(), key=lambda kv: len(kv[0])):
        if w not in cache:
            pre = cache.get(w[:-1])
            if pre is None:
                pre = E1
                for l in w[:-1]: pre = emul(pre, a if l == 0 else b, D)
                cache[w[:-1]] = pre
            cache[w] = emul(pre, a if w[-1] == 0 else b, D)
        r = padd(r, esc(c, cache[w]))
    return r
def einv(x, D):  # inverse of 1 + n
    n = padd(x, esc(-1, E1)); r = dict(E1); t = dict(E1)
    for _ in range(D):
        t = emul(t, esc(-1, n), D); r = padd(r, t)
    return r
def conjR(G, x, D): return emul(emul(G, x, D), einv(G, D), D)

def checks(g, D, label):
    U, V, W = t12, t13, t23
    a512 = padd(emul(ev(g, U, V, D), ev(g, V, U, D), D), esc(-1, E1))
    a513 = padd(emul(emul(ev(g, W, U, D), ev(g, V, W, D), D), ev(g, U, V, D), D), esc(-1, E1))
    gvw, guw = ev(g, V, W, D), ev(g, U, W, D)
    a514 = padd(conjR(gvw, V, D), esc(-1, conjR(guw, padd(V, W), D)), W)
    lhs = emul(ev(g, t12, padd(t23, t24), D), ev(g, padd(t13, t23), t34, D), D)
    rhs = emul(emul(ev(g, t23, t34, D), ev(g, padd(t12, t13), padd(t24, t34), D), D), ev(g, t12, t23, D), D)
    a515 = padd(lhs, esc(-1, rhs))
    def lowest(x): return min((len(f) + len(t) + k for (f, t, k) in x), default=None)
    print(f'{label}, through degree {D}: first failing degree (None = holds) '
          f'(5.12) {lowest(a512)}, (5.13) {lowest(a513)}, (5.14) {lowest(a514)}, (5.15) {lowest(a515)}')

if __name__ == '__main__':
    D = DMAX
    sig3 = fadd(fbr(FX, fbr(FX, FY, D), D), fbr(FY, fbr(FX, FY, D), D))
    checks(Exp516(sig3, D), D, 'Exp(sigma3), (5.16) exponential')
    checks(fexp(sig3, D), D, 'exp(sigma3), ordinary exponential')
    checks(Exp516(fbr(FX, fbr(FX, FY, D), D), D), D, 'Exp([X,[X,Y]]) (not in grt), control')
