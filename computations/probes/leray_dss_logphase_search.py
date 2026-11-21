#!/usr/bin/env python3
"""Leray DSS search in a log-phase trial basis (arbitrary precision; numerical exploration, NOT a proof).

Backward self-similar Navier--Stokes profile system (y = x/sqrt(T-t), s = -log(T-t)):

    d_s V - Lap V + V/2 + (y.grad)V/2 + (V.grad)V + grad P = 0,   div V = 0,

DSS = V periodic in s with unknown period S (lambda = exp(S/2)), V = sum_m A_m(y) e^{i m w s},
w = 2 pi / S.  Away from the core, d_s + 1/2 + (y.grad)/2 annihilates |y|^{-1} g(yhat, log|y| - s/2),
so a Fourier mode m of an admissible profile has the tail |y|^{-1-2imw}.  The phase-1 probe
(leray_dss_galerkin_search.py) gave every mode the non-oscillating tail |y|^{-1}.

Basis (this probe).  Same angular structure and the same Gaussian TEST fields as phase 1:
  toroidal  T[H,R] = R(rho) (grad H x y)
  poloidal  P[H,R] = curl curl (y H R) = S grad H - 2 l R'(rho) H y,  S = (l+1) R + 2 rho R'
Both are divergence free for ANY differentiable radial R, real or complex.  The TRIAL radial
function of Fourier mode m is

    R_{m} = (c2 + rho)^{-q},   q = p + i theta m w,   p = (l+1)/2 + n (T),  l/2 + n (P),

so at theta = 1 the n = 0 member of mode m decays like |y|^{-1-2imw} exactly (the admissible
log-phase tail) and the field is still exactly divergence free; theta = 0 is the phase-1 basis.
The basis depends on the unknown w, so every Newton step rebuilds the radial tables.

Pressure.  The test fields are the phase-1 Gaussian fields rho^n e^{-rho/4} (T/P, real): exactly
divergence free and Gaussian decaying, so <grad P, psi> = -<P, div psi> = 0 for any P of
polynomial growth, and -Lap integrates by parts.  The trial side carries the oscillation; the
test side is untouched, so the pressure is eliminated exactly as in phase 1.

Quadrature.  Angular integrals are exact (Gauss--Legendre in cos(theta) x uniform phi, of degree
>= the polynomial degree).  Radial: substitution r = sinh(u) (so c2 + rho = cosh(u)^2 at c2 = 1 and
the phase -2 i mu log cosh u has bounded rate 2|mu| tanh u), composite Gauss--Legendre on panels
of width chosen from the largest phase rate, truncated where the Gaussian test weight is below
10^-(dps+15).  The stability of the assembled matrices under a change of the rule is measured
and recorded (quadrature_check).

Arithmetic: python-flint (Arb/Acb ball arithmetic) at LERAY_DPS digits (default 60); the
matrices are used at their midpoints.  No float64 arithmetic anywhere; float() appears only in
display.  Arb is arbitrary precision like mpmath; it is used because pure-Python mpmath (no gmpy2
here) costs ~43 min per Newton step at L2N4 (audit doc §9.4).

Seeds: phase-1 periodic orbits B (L2N2) and C (L2N3) from leray_dss_galerkin_seeds.json
(decimal strings), continued theta: 0 -> 1; random starts with a fixed RNG seed.
"""
import os, sys, json, time, random, itertools
from fractions import Fraction
from math import comb, factorial
from flint import arb, acb, arb_mat, acb_mat, ctx

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from leray_dss_galerkin_search import harmonic_basis_rational, monomials  # exact rational harmonics

DPS = int(os.environ.get("LERAY_DPS", "60"))
ctx.dps = DPS
C2 = arb(1)
ALPHA = arb(1) / 4
QN = int(os.environ.get("LERAY_QN", "24"))       # GL nodes per radial panel
PHASE_PER_PANEL = arb(os.environ.get("LERAY_PPP", "12"))  # max phase change (rad) per panel
LOG = lambda *x: print(*x, flush=True)

def fr(x): return arb(x.numerator) / x.denominator
def mid(z): return z.mid()
def s40(z, d=40): return z.mid().str(d, radius=False)

# ------------------------------------------------------------------ harmonics
def zonal_harmonic(l):
    """r^l P_l(z/r) as rational coefficients on monomials(l) (axisymmetric solid harmonic)."""
    mons = monomials(l); idx = {m: i for i, m in enumerate(mons)}
    coef = [Fraction(0)] * len(mons)
    for k in range(l // 2 + 1):
        ck = Fraction((-1) ** k * comb(l, k) * comb(2 * l - 2 * k, l), 2 ** l)
        for i in range(k + 1):
            for j in range(k + 1 - i):
                kk = k - i - j
                mult = Fraction(factorial(k), factorial(i) * factorial(j) * factorial(kk))
                coef[idx[(2 * i, 2 * j, 2 * kk + l - 2 * k)]] += ck * mult
    # exact harmonicity check
    lap = {}
    for e, c in zip(mons, coef):
        for a in range(3):
            if e[a] >= 2:
                f = list(e); f[a] -= 2; lap[tuple(f)] = lap.get(tuple(f), 0) + c * e[a] * (e[a] - 1)
    assert all(v == 0 for v in lap.values()), "zonal harmonic not harmonic"
    return mons, [coef]

def labels_for(L, N, axi):
    harm = {l: (zonal_harmonic(l) if axi else harmonic_basis_rational(l)) for l in range(1, L + 1)}
    labels = []
    for l in range(1, L + 1):
        for h in range(len(harm[l][1])):
            for kind in 'TP':
                for n in range(N):
                    labels.append((kind, l, h, n))
    return harm, labels

# ------------------------------------------------------------------ angular (exact)
EPS = {}
for i, j, k in itertools.permutations(range(3)):
    EPS[(i, j, k)] = 1 if (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1
def eps(i, j, k): return EPS.get((i, j, k), 0)

def poly_eval(mons, coef, y):
    v = arb(0); g = [arb(0)] * 3; h = [[arb(0)] * 3 for _ in range(3)]
    def mon(e):
        if min(e) < 0: return arb(0)
        return y[0] ** e[0] * y[1] ** e[1] * y[2] ** e[2]
    for e, c in zip(mons, coef):
        if c == 0: continue
        c = fr(c); v += c * mon(e)
        for k in range(3):
            if e[k] > 0:
                ek = list(e); ek[k] -= 1; g[k] += c * e[k] * mon(ek)
                for j in range(3):
                    if ek[j] > 0:
                        ekj = list(ek); f = ekj[j]; ekj[j] -= 1
                        h[k][j] += c * e[k] * f * mon(ekj)
    return v, g, h

def angular_terms(kind, mons, coef, u):
    H, dH, HH = poly_eval(mons, coef, u)
    if kind == 'T':
        g = [sum((eps(i, j, m) * dH[j] * u[m] for j in range(3) for m in range(3)), arb(0)) for i in range(3)]
        V = [g]
        J1 = [[u[k] * g[i] for k in range(3)] for i in range(3)]
        J2 = [[sum((eps(i, j, m) * HH[k][j] * u[m] for j in range(3) for m in range(3)), arb(0))
               + sum((eps(i, j, k) * dH[j] for j in range(3)), arb(0)) for k in range(3)] for i in range(3)]
        J = [J1, J2]
    else:
        V = [list(dH), [H * u[i] for i in range(3)]]
        J = [[[u[k] * dH[i] for k in range(3)] for i in range(3)],
             [[HH[k][i] for k in range(3)] for i in range(3)],
             [[u[k] * u[i] * H for k in range(3)] for i in range(3)],
             [[dH[k] * u[i] + (H if i == k else arb(0)) for k in range(3)] for i in range(3)]]
    return V, J

def gl(m):
    out = [arb.legendre_p_root(m, k, weight=True) for k in range(m)]
    return [x for x, _ in out], [w for _, w in out]

def angular_tables(L, harm, labels):
    deg = 3 * L + 6; nt = deg // 2 + 2; nph = deg + 2
    ct, wt = gl(nt); nodes, wts = [], []
    pi = arb.pi()
    for c, w in zip(ct, wt):
        st = (1 - c * c).sqrt()
        for k in range(nph):
            ph = 2 * pi * k / nph
            nodes.append((st * ph.cos(), st * ph.sin(), c)); wts.append(w * 2 * pi / nph)
    G = len(nodes)
    akeys = sorted({(k, l, h) for (k, l, h, n) in labels})
    AV, AJ = {}, {}
    for ak in akeys:
        k, l, h = ak; mons, bas = harm[l]
        vals = [angular_terms(k, mons, bas[h], u) for u in nodes]
        AV[ak] = [[v[0][t] for v in vals] for t in range(len(vals[0][0]))]
        AJ[ak] = [[v[1][t] for v in vals] for t in range(len(vals[0][1]))]
    vrows = [(ak, s) for ak in akeys for s in range(len(AV[ak]))]
    jrows = [(ak, t) for ak in akeys for t in range(len(AJ[ak]))]
    V = arb_mat(len(vrows), 3 * G, [AV[ak][s][g][i] for (ak, s) in vrows for g in range(G) for i in range(3)])
    VW = arb_mat(len(vrows), 3 * G, [AV[ak][s][g][i] * wts[g] for (ak, s) in vrows for g in range(G) for i in range(3)])
    J = arb_mat(len(jrows), 9 * G, [AJ[ak][t][g][i][k] for (ak, t) in jrows for g in range(G) for i in range(3) for k in range(3)])
    JW = arb_mat(len(jrows), 9 * G, [AJ[ak][t][g][i][k] * wts[g] for (ak, t) in jrows for g in range(G) for i in range(3) for k in range(3)])
    VY = arb_mat(len(vrows), 9 * G, [AV[ak][s][g][i] * nodes[g][k] * wts[g] for (ak, s) in vrows for g in range(G) for i in range(3) for k in range(3)])
    Avv = VW * V.transpose(); Ajj = JW * J.transpose(); Avyj = VY * J.transpose()
    xrows = [(r1, r2) for r1 in vrows for r2 in vrows]
    X = arb_mat(len(xrows), 9 * G, [AV[a1][s][g][i] * AV[a2][t][g][k] * wts[g]
                                     for ((a1, s), (a2, t)) in xrows for g in range(G) for i in range(3) for k in range(3)])
    AB = X * J.transpose()
    vi = {r: i for i, r in enumerate(vrows)}; ji = {r: i for i, r in enumerate(jrows)}; xi = {r: i for i, r in enumerate(xrows)}
    return dict(Avv=Avv, Ajj=Ajj, Avyj=Avyj, AB=AB, vi=vi, ji=ji, xi=xi,
                nV={ak: len(AV[ak]) for ak in akeys}, nJ={ak: len(AJ[ak]) for ak in akeys})

# ------------------------------------------------------------------ radial
def radial_nodes(rate):
    """Panels in u (r = sinh u) on [0, U]; width <= PHASE_PER_PANEL / rate and <= 1/4."""
    rho_max = 4 * arb(10).log() * (DPS + 15)
    U = (rho_max.sqrt()).asinh()
    h = arb(1) / 4
    if rate > 0:
        h2 = PHASE_PER_PANEL / rate
        if h2 < h: h = h2
    P = int((U / h).ceil().unique_fmpz()) + 1
    xs, ws = gl(QN)
    out = []
    for p in range(P):
        a = U * p / P; b = U * (p + 1) / P
        for x, w in zip(xs, ws):
            u = (a + b) / 2 + (b - a) / 2 * x
            r = u.sinh(); ch = u.cosh(); rho = r * r
            out.append((r, rho, (C2 + rho).log(), (b - a) / 2 * w * ch * rho))
    return out

def rterms(kind, l, R, R1, R2, r, rho):
    if kind == 'T':
        return [R * r ** l], [2 * R1 * r ** (l + 1), R * r ** (l - 1)]
    S = (l + 1) * R + 2 * rho * R1; S1 = (l + 3) * R1 + 2 * rho * R2
    C = -2 * l * R1; C1 = -2 * l * R2
    return [S * r ** (l - 1), C * r ** (l + 1)], [2 * S1 * r ** l, (S * r ** (l - 2) if l >= 2 else R * 0),
                                                  2 * C1 * r ** (l + 2), C * r ** l]

def test_radial(kind, l, n, r, rho):
    a = ALPHA; ex = (-a * rho).exp()
    R = rho ** n * ex
    R1 = ((n * rho ** (n - 1) if n > 0 else 0) - a * rho ** n) * ex
    R2 = ((n * (n - 1) * rho ** (n - 2) if n > 1 else 0) - 2 * a * (n * rho ** (n - 1) if n > 0 else 0) + a * a * rho ** n) * ex
    return rterms(kind, l, R, R1, R2, r, rho)

def trial_radial(kind, l, n, r, rho, tau, mu):
    p = arb(l + 1) / 2 + n if kind == 'T' else arb(l) / 2 + n
    q = acb(p, mu); uu = C2 + rho
    R = (-q * tau).exp(); R1 = -q * R / uu; R2 = q * (q + 1) * R / (uu * uu)
    return rterms(kind, l, R, R1, R2, acb(r), acb(rho))

# ------------------------------------------------------------------ system
class System:
    def __init__(self, L, N, K, axi=False):
        self.L, self.N, self.K, self.axi = L, N, K, axi
        self.harm, self.labels = labels_for(L, N, axi)
        self.n = len(self.labels)
        t0 = time.time()
        self.ang = angular_tables(L, self.harm, self.labels)
        self.rkeys = sorted({(k, l, n) for (k, l, h, n) in self.labels})
        self.blocks = sorted({(k, l) for (k, l, h, n) in self.labels})
        LOG(f"  [{L},{N},K={K},axi={axi}] n={self.n} angular tables {time.time()-t0:.1f}s")

    def build(self, om, theta, rate_override=None):
        K, n, A = self.K, self.n, self.ang
        rate = rate_override if rate_override is not None else 4 * K * om * theta
        nodes = radial_nodes(rate)
        M = len(nodes)
        rk = self.rkeys
        # test tables (real), rows (rkey, s)
        tv, tj = {}, {}
        for key in rk:
            k, l, nn = key
            vals = [test_radial(k, l, nn, r, rho) for (r, rho, tau, W) in nodes]
            tv[key] = [[v[0][s] for v in vals] for s in range(len(vals[0][0]))]
            tj[key] = [[v[1][s] for v in vals] for s in range(len(vals[0][1]))]
        vrows = [(key, s) for key in rk for s in range(len(tv[key]))]
        jrows = [(key, s) for key in rk for s in range(len(tj[key]))]
        W = [acb(w) for (_, _, _, w) in nodes]; Wr = [acb(w * r) for (r, _, _, w) in nodes]
        TVW = acb_mat(len(vrows), M, [tv[k][s][j] * W[j] for (k, s) in vrows for j in range(M)])
        TVWr = acb_mat(len(vrows), M, [tv[k][s][j] * Wr[j] for (k, s) in vrows for j in range(M)])
        TJW = acb_mat(len(jrows), M, [tj[k][s][j] * W[j] for (k, s) in jrows for j in range(M)])
        # trial tables per mode m >= 0 (m < 0 by conjugation)
        TV, TJ = {}, {}
        for m in range(0, K + 1):
            mu = theta * m * om
            tvm, tjm = {}, {}
            for key in rk:
                k, l, nn = key
                vals = [trial_radial(k, l, nn, r, rho, tau, mu) for (r, rho, tau, w) in nodes]
                tvm[key] = [[v[0][s] for v in vals] for s in range(len(vals[0][0]))]
                tjm[key] = [[v[1][s] for v in vals] for s in range(len(vals[0][1]))]
            TV[m] = acb_mat(len(vrows), M, [tvm[k][s][j] for (k, s) in vrows for j in range(M)])
            TJ[m] = acb_mat(len(jrows), M, [tjm[k][s][j] for (k, s) in jrows for j in range(M)])
        for m in range(1, K + 1):
            TV[-m] = TV[m].conjugate(); TJ[-m] = TJ[m].conjugate()
        vi = {r: i for i, r in enumerate(vrows)}; ji = {r: i for i, r in enumerate(jrows)}
        lab = self.labels
        # linear operators per mode
        Lm, Mm = {}, {}
        for m in range(0, K + 1):
            Rvv = TVW * TV[m].transpose(); Rjj = TJW * TJ[m].transpose(); Rvy = TVWr * TJ[m].transpose()
            Lmat = acb_mat(n, n); Mmat = acb_mat(n, n)
            for a, (ka, la, ha, na) in enumerate(lab):
                Aa = (ka, la, ha); ra = (ka, la, na)
                for b, (kb, lb, hb, nb) in enumerate(lab):
                    Ab = (kb, lb, hb); rb = (kb, lb, nb)
                    mass = acb(0); grad = acb(0); ydv = acb(0)
                    for s in range(A['nV'][Aa]):
                        for t in range(A['nV'][Ab]):
                            mass += Rvv[vi[(ra, s)], vi[(rb, t)]] * A['Avv'][A['vi'][(Aa, s)], A['vi'][(Ab, t)]]
                    for s in range(A['nJ'][Aa]):
                        for t in range(A['nJ'][Ab]):
                            grad += Rjj[ji[(ra, s)], ji[(rb, t)]] * A['Ajj'][A['ji'][(Aa, s)], A['ji'][(Ab, t)]]
                    for s in range(A['nV'][Aa]):
                        for t in range(A['nJ'][Ab]):
                            ydv += Rvy[vi[(ra, s)], ji[(rb, t)]] * A['Avyj'][A['vi'][(Aa, s)], A['ji'][(Ab, t)]]
                    Mmat[a, b] = mass
                    Lmat[a, b] = grad + mass / 2 + ydv / 2 + acb(0, om * m) * mass
            Lm[m] = Lmat; Mm[m] = Mmat
        # nonlinear: S^{m1,m2}[(a,b),c] = B^{m1m2}[a,b,c] + B^{m2m1}[a,c,b], m1+m2 in [0,K]
        pairs = [(m1, m - m1) for m in range(K + 1) for m1 in range(-K, K + 1) if abs(m - m1) <= K]
        Smat = {p: [[acb(0)] * n for _ in range(n * n)] for p in pairs}
        xrows = [(r1, r2) for r1 in vrows for r2 in vrows]
        xri = {r: i for i, r in enumerate(xrows)}
        TVWl = [[TVW[i, j] for j in range(M)] for i in range(len(vrows))]
        for m1 in range(-K, K + 1):
            m2s = [m2 for (a1, m2) in pairs if a1 == m1]
            if not m2s: continue
            TVl = [[TV[m1][i, j] for j in range(M)] for i in range(len(vrows))]
            X = acb_mat(len(xrows), M, [TVWl[vi[r1]][j] * TVl[vi[r2]][j] for (r1, r2) in xrows for j in range(M)])
            Jcat = acb_mat(len(jrows) * len(m2s), M, [TJ[m2][i, j] for m2 in m2s for i in range(len(jrows)) for j in range(M)])
            Y = X * Jcat.transpose()
            for im2, m2 in enumerate(m2s):
                off = im2 * len(jrows)
                for a, (ka, la, ha, na) in enumerate(lab):
                    Aa = (ka, la, ha); ra = (ka, la, na)
                    for b, (kb, lb, hb, nb) in enumerate(lab):
                        Ab = (kb, lb, hb); rb = (kb, lb, nb)
                        for c, (kc, lc, hc, nc) in enumerate(lab):
                            Ac = (kc, lc, hc); rc = (kc, lc, nc)
                            v = acb(0)
                            for s in range(A['nV'][Aa]):
                                for t in range(A['nV'][Ab]):
                                    xa = A['xi'][((Aa, s), (Ab, t))]; xr = xri[((ra, s), (rb, t))]
                                    for u in range(A['nJ'][Ac]):
                                        ag = A['AB'][xa, A['ji'][(Ac, u)]]
                                        if ag == 0: continue
                                        v += Y[xr, off + ji[(rc, u)]] * ag
                            if v != 0:
                                Smat[(m1, m2)][a * n + b][c] += v
                                Smat[(m2, m1)][a * n + c][b] += v
        S = {p: acb_mat(n * n, n, [x for row in Smat[p] for x in row]) for p in pairs}
        return dict(L=Lm, M=Mm, S=S, pairs=pairs, nodes=M)

# ------------------------------------------------------------------ residual / Newton
def residual(sysd, A, n, K):
    """A: dict m -> acb_mat(n,1), m=0..K.  Returns R[m] (acb_mat n,1) and G[(m1,m2)] (n x n)."""
    def Am(m): return A[m] if m >= 0 else A[-m].conjugate()
    R = {m: sysd['L'][m] * A[m] for m in range(K + 1)}
    G = {}
    for (m1, m2) in sysd['pairs']:
        g = sysd['S'][(m1, m2)] * Am(m2)
        Gm = acb_mat(n, n, [g[i, 0] for i in range(n * n)])
        G[(m1, m2)] = Gm
        R[m1 + m2] += (Gm * Am(m1)) / 2
    return R, G

def pack(A, om, n, K):
    x = [A[0][j, 0].real for j in range(n)]
    for m in range(1, K + 1): x += [A[m][j, 0].real for j in range(n)]
    for m in range(1, K + 1): x += [A[m][j, 0].imag for j in range(n)]
    return x + [om]

def unpack(x, n, K):
    A = {0: acb_mat(n, 1, [acb(x[j]) for j in range(n)])}
    for m in range(1, K + 1):
        A[m] = acb_mat(n, 1, [acb(x[n + (m - 1) * n + j], x[n + n * K + (m - 1) * n + j]) for j in range(n)])
    return A, x[-1]

def flatF(R, A, n, K, pj):
    F = [R[0][j, 0].real for j in range(n)]
    for m in range(1, K + 1): F += [R[m][j, 0].real for j in range(n)]
    for m in range(1, K + 1): F += [R[m][j, 0].imag for j in range(n)]
    F.append(A[1][pj, 0].imag if K >= 1 else arb(0))
    return F

def norm(v): return sum((x * x for x in v), arb(0)).sqrt()

def jacobian(sy, x, theta, pj, sd, F, G, hstep, omega_col=None):
    """Real Jacobian of flatF wrt (Re A, Im A, w); d/dw by one-sided FD with basis rebuild."""
    n, K = sy.n, sy.K
    A, om = unpack(x, n, K)
    D = len(x)
    Jm = arb_mat(D, D)
    # A-derivatives (complex-linear structure)
    def rowoff(m, part):
        if m == 0: return 0 if part == 're' else None
        return n + (m - 1) * n if part == 're' else n + n * K + (m - 1) * n
    def coloff(p, part):
        if p == 0: return 0 if part == 're' else None
        return n + (p - 1) * n if part == 're' else n + n * K + (p - 1) * n
    # collect complex blocks C[m][p] multiplying dA_p (and conj blocks for p<0)
    blocks = {}
    for m in range(K + 1):
        blocks[(m, m)] = blocks.get((m, m), acb_mat(n, n)) + sd['L'][m]
    for (m1, m2), Gm in G.items():
        m = m1 + m2
        blocks[(m, m1)] = blocks.get((m, m1), acb_mat(n, n)) + Gm
    for (m, p), Bk in blocks.items():
        for i in range(n):
            for j in range(n):
                z = Bk[i, j]
                if p >= 0:
                    # dA_p = dx + i dy ; contributes z dx + i z dy
                    cr, ci = coloff(p, 're'), coloff(p, 'im')
                    rr, ri = rowoff(m, 're'), rowoff(m, 'im')
                    Jm[rr + i, cr + j] += z.real
                    if ri is not None: Jm[ri + i, cr + j] += z.imag
                    if ci is not None:
                        Jm[rr + i, ci + j] += -z.imag
                        if ri is not None: Jm[ri + i, ci + j] += z.real
                else:
                    q = -p  # dA_{-q} = dx - i dy
                    cr, ci = coloff(q, 're'), coloff(q, 'im')
                    rr, ri = rowoff(m, 're'), rowoff(m, 'im')
                    Jm[rr + i, cr + j] += z.real
                    if ri is not None: Jm[ri + i, cr + j] += z.imag
                    Jm[rr + i, ci + j] += z.imag
                    if ri is not None: Jm[ri + i, ci + j] += -z.real
    # phase row
    Jm[D - 1, n + n * K + pj] = arb(1)
    if omega_col is not None:
        for i in range(D): Jm[i, D - 1] = omega_col[i]
        return Jm
    # omega column by FD
    sd2 = sy.build(om + hstep, theta, rate_override=4 * K * om * theta)
    R2, _ = residual(sd2, A, n, K)
    F2 = flatF(R2, A, n, K, pj)
    for i in range(D):
        Jm[i, D - 1] = mid((F2[i] - F[i]) / hstep)
    return Jm

def newton(sy, x0, theta, pj, maxit=25, tol_digits=None, log=LOG, fixed_basis_om=None):
    """Full Newton in (A_0, A_m, w); basis depends on w (rebuilt each step), d/dw by one-sided FD."""
    n, K = sy.n, sy.K
    tol = arb(10) ** (-(tol_digits or (DPS - 20)))
    x = [mid(v) for v in x0]; hist = []
    hstep = arb(10) ** (-(DPS // 2))
    for it in range(maxit):
        A, om = unpack(x, n, K)
        sd = sy.build(om, theta)
        R, G = residual(sd, A, n, K)
        F = flatF(R, A, n, K, pj); nf = mid(norm(F)); xn = mid(norm(x[:-1]))
        hist.append(nf)
        log(f"    it={it} |F|={nf.str(4, radius=False)} |A|={xn.str(6, radius=False)} S={(2*arb.pi()/om).str(16, radius=False)} nodes={sd['nodes']}")
        if nf < tol * (1 + xn): return x, nf, hist, True
        if not (nf < arb(10) ** 12) or om <= 0: return x, nf, hist, False
        Jm = jacobian(sy, x, theta, pj, sd, F, G, hstep); D = len(x)
        Jt = Jm.transpose(); N_ = Jt * Jm
        shift = mid(sum((abs(N_[i, i]) for i in range(D)), arb(0)) / D) * arb(10) ** (-(DPS - 15))
        for i in range(D): N_[i, i] += shift
        rhs = Jt * arb_mat(D, 1, F)
        dx = N_.solve(rhs, algorithm="approx")
        # damped step
        lam = arb(1)
        for _ in range(8):
            xt = [mid(x[i] - lam * dx[i, 0]) for i in range(D)]
            if xt[-1] > 0: break
            lam /= 2
        x = xt
    A, om = unpack(x, n, K)
    sd = sy.build(om, theta); R, _ = residual(sd, A, n, K)
    nf = mid(norm(flatF(R, A, n, K, pj)))
    hist.append(nf)
    return x, nf, hist, nf < tol * (1 + mid(norm(x[:-1])))

def mode_norms(x, n, K):
    A, om = unpack(x, n, K)
    out = []
    for m in range(K + 1):
        out.append(mid(sum((abs(A[m][j, 0]) ** 2 for j in range(n)), arb(0)).sqrt()))
    return out

def classify(x, n, K):
    nm = mode_norms(x, n, K); tot = sum((v * v for v in nm), arb(0)).sqrt()
    harm = sum((v * v for v in nm[1:]), arb(0)).sqrt()
    if tot < arb(10) ** -15: return 'trivial', nm
    if harm < arb(10) ** -15 * tot: return 'steady', nm
    return 'periodic', nm

def quadrature_check(sy, om, theta):
    """Assembled-matrix change under a finer radial rule (QN -> QN+12, panel phase 12 -> 8)."""
    global QN, PHASE_PER_PANEL
    a = sy.build(om, theta)
    q0, p0 = QN, PHASE_PER_PANEL
    QN, PHASE_PER_PANEL = QN + 12, arb(8)
    try:
        b = sy.build(om, theta)
    finally:
        QN, PHASE_PER_PANEL = q0, p0
    def md(X, Y):
        best = arb(0)
        for i in range(X.nrows()):
            for j in range(X.ncols()):
                d = abs(mid(X[i, j]) - mid(Y[i, j]))
                if d > best: best = d
        return mid(best)
    dL = max((md(a['L'][m], b['L'][m]) for m in a['L']), key=lambda z: z)
    dS = max((md(a['S'][p], b['S'][p]) for p in a['pairs']), key=lambda z: z)
    sL = max((md(a['L'][m], a['L'][m] * 0) for m in a['L']), key=lambda z: z)
    sS = max((md(a['S'][p], a['S'][p] * 0) for p in a['pairs']), key=lambda z: z)
    return dict(nodes=[a['nodes'], b['nodes']], L_maxabs_change=dL.str(5, radius=False), S_maxabs_change=dS.str(5, radius=False),
                L_maxabs=sL.str(5, radius=False), S_maxabs=sS.str(5, radius=False))

# ------------------------------------------------------------------ drivers
def embed(x, sy_from, sy_to):
    """Map a solution vector between truncations (labels / K); missing entries 0."""
    nf, Kf, nt, Kt = sy_from.n, sy_from.K, sy_to.n, sy_to.K
    idx = {l: i for i, l in enumerate(sy_to.labels)}
    y = [arb(0)] * (nt * (2 * Kt + 1) + 1)
    for jf, l in enumerate(sy_from.labels):
        if l not in idx: continue
        j = idx[l]
        y[j] = x[jf]
        for m in range(1, min(Kf, Kt) + 1):
            y[nt + (m - 1) * nt + j] = x[nf + (m - 1) * nf + jf]
            y[nt + nt * Kt + (m - 1) * nt + j] = x[nf + nf * Kf + (m - 1) * nf + jf]
    y[-1] = x[-1]
    return y

def seed_from_phase1(sy, case_seed):
    idx = {tuple(l): i for i, l in enumerate(sy.labels)}
    n, K, Ks = sy.n, sy.K, case_seed['K']
    x = [arb(v) for v in case_seed['x']]; perm = [idx[tuple(l)] for l in case_seed['labels']]
    y = [arb(0)] * (n * (2 * K + 1) + 1)
    for jj, j in enumerate(perm):
        y[j] = x[jj]
        for m in range(1, min(K, Ks) + 1):
            y[n + (m - 1) * n + j] = x[n + (m - 1) * n + jj]; y[n + n * K + (m - 1) * n + j] = x[n + n * Ks + (m - 1) * n + jj]
    y[-1] = x[-1]
    return y, perm[0]

def summary(x, sy, nf, ok, theta):
    cls, nm = classify(x, sy.n, sy.K)
    om = x[-1]
    return dict(L=sy.L, N=sy.N, K=sy.K, axi=sy.axi, theta=s40(theta, 6), converged=bool(ok), residual=nf.str(5, radius=False),
                cls=cls, period_S=s40(2 * arb.pi() / om) if om > 0 else None,
                mode_norms=[s40(v, 20) for v in nm])

def homotopy(sy, x0, pj, dtheta=arb(1) / 10, dmin=arb(1) / 80, log=LOG):
    """Continue a theta = 0 solution to theta = 1 (log-phase tail). Stops at failure or collapse."""
    x, nf, h, ok = newton(sy, x0, arb(0), pj, maxit=10, log=log)
    path = [summary(x, sy, nf, ok, arb(0))]
    log("  theta=0:", path[-1]['cls'], path[-1]['period_S'], path[-1]['residual'])
    if not ok or path[-1]['cls'] != 'periodic': return x, path, 'no_theta0_orbit'
    th = arb(0); d = dtheta
    while th < 1:
        tt = th + d
        if tt > 1: tt = arb(1)
        xt, nf, h, ok = newton(sy, x, tt, pj, maxit=8, log=log)
        rec = summary(xt, sy, nf, ok, tt)
        log(f"  theta={s40(tt,6)}: ok={ok} cls={rec['cls']} S={rec['period_S']} res={rec['residual']}")
        if ok and rec['cls'] == 'periodic':
            x, th = xt, tt; path.append(rec)
            if d < dtheta: d = d * 2
        elif ok and rec['cls'] != 'periodic':
            path.append(rec); return xt, path, 'collapsed_to_' + rec['cls']
        else:
            d = d / 2
            if d < dmin:
                path.append(rec); return x, path, 'newton_fails_at_theta_' + s40(tt, 6)
    return x, path, 'reached_theta_1'

def corrector_arclength(sy, y_pred, t, W, pj, maxit=8, log=LOG):
    """Newton on [F(x, theta); t.(y - y_pred)] with y = (x, W*theta) (pseudo-arclength corrector)."""
    n, K = sy.n, sy.K
    tol = arb(10) ** (-(DPS - 20)); hstep = arb(10) ** (-(DPS // 2))
    y = [mid(v) for v in y_pred]; D = len(y) - 1
    for it in range(maxit + 1):
        x, th = y[:D], y[D] / W
        if not (th > -1) or not (th < 2): return y, None, False
        A, om = unpack(x, n, K)
        if om <= 0: return y, None, False
        sd = sy.build(om, th); R, G = residual(sd, A, n, K)
        F = flatF(R, A, n, K, pj)
        cons = sum((t[i] * (y[i] - y_pred[i]) for i in range(D + 1)), arb(0))
        nf = mid(norm(F)); xn = mid(norm(x[:-1]))
        if nf < tol * (1 + xn) and abs(cons) < tol * (1 + xn): return y, nf, True
        if it == maxit or not (nf < arb(10) ** 12): return y, nf, False
        Jx = jacobian(sy, x, th, pj, sd, F, G, hstep)
        rate = 4 * K * om * th if th > 0 else None
        sd2 = sy.build(om, th + hstep, rate_override=rate if rate is not None else arb(0))
        R2, _ = residual(sd2, A, n, K); F2 = flatF(R2, A, n, K, pj)
        M = arb_mat(D + 1, D + 1)
        for i in range(D):
            for j in range(D): M[i, j] = Jx[i, j]
            M[i, D] = mid((F2[i] - F[i]) / hstep) / W
        for j in range(D + 1): M[D, j] = t[j]
        rhs = arb_mat(D + 1, 1, F + [cons])
        Mt = M.transpose(); N_ = Mt * M
        shift = mid(sum((abs(N_[i, i]) for i in range(D + 1)), arb(0)) / (D + 1)) * arb(10) ** (-(DPS - 15))
        for i in range(D + 1): N_[i, i] += shift
        dy = N_.solve(Mt * rhs, algorithm="approx")
        y = [mid(y[i] - dy[i, 0]) for i in range(D + 1)]
    return y, nf, False

def arclength_homotopy(sy, x0, pj, th1=arb(1) / 80, maxsteps=200, log=LOG):
    """Secant pseudo-arclength continuation in theta from a theta = 0 orbit. Passes folds in theta.
    y = (x, W theta), W = |x0|; stops at theta = 1, theta < 0 (branch returns), collapse, or ds underflow."""
    x, nf, h, ok = newton(sy, x0, arb(0), pj, maxit=10, log=log)
    path = [summary(x, sy, nf, ok, arb(0))]
    if not ok or path[-1]['cls'] != 'periodic': return x, path, 'no_theta0_orbit'
    W = mid(norm(x[:-1]))
    x1, nf1, _, ok1 = newton(sy, x, th1, pj, maxit=10, log=log)
    if not ok1: return x, path, 'first_natural_step_fails'
    path.append(summary(x1, sy, nf1, ok1, th1))
    y0 = x + [arb(0)]; y1 = x1 + [W * th1]
    ds = mid(norm([y1[i] - y0[i] for i in range(len(y0))])); dsmin = ds / 64; dsmax = ds * 8
    dth_sign = 1; folds = []; t_end = time.time() + float(os.environ.get('LERAY_TMAX', '1e9'))
    for step in range(maxsteps):
        if time.time() > t_end:
            return y1[:-1], path, f'time_budget_at_theta_{s40(y1[-1]/W, 6)}_folds_{len(folds)}'
        sec = [y1[i] - y0[i] for i in range(len(y0))]; L_ = mid(norm(sec)); t = [v / L_ for v in sec]
        yp = [mid(y1[i] + ds * t[i]) for i in range(len(y1))]
        y, nf, ok = corrector_arclength(sy, yp, t, W, pj, log=log)
        if not ok:
            ds = ds / 2
            log(f"   arc step {step}: corrector fails, ds -> {ds.str(4, radius=False)}")
            if ds < dsmin:
                th_last = y1[-1] / W
                return y1[:-1], path, 'arclength_stalls_at_theta_' + s40(th_last, 6)
            continue
        D = len(y) - 1; th = y[D] / W
        rec = summary(y[:D], sy, nf, True, th)
        sgn = 1 if th > y1[D] / W else -1
        if sgn != dth_sign:
            folds.append(s40(y1[D] / W, 10)); rec['fold_before'] = True; dth_sign = sgn
        path.append(rec)
        log(f"   arc step {step}: theta={s40(th,8)} S={rec['period_S'][:18]} |A|={mid(norm(y[:D-1])).str(8, radius=False)} res={rec['residual']} folds={len(folds)}")
        if rec['cls'] != 'periodic': return y[:D], path, 'collapsed_to_' + rec['cls']
        if th < 0: return y[:D], path, f'branch_returns_to_theta_0_after_{len(folds)}_folds'
        if th >= 1:
            xf, nff, _, okf = newton(sy, y[:D], arb(1), pj, maxit=10, log=log)
            path.append(summary(xf, sy, nff, okf, arb(1)))
            return xf, path, ('reached_theta_1' if okf else 'theta1_newton_fails')
        y0, y1 = y1, y
        ds = min(ds * arb(3) / 2, dsmax)
    return y1[:-1], path, f'maxsteps_at_theta_{s40(y1[-1]/W, 6)}_folds_{len(folds)}'

def theta_omega_columns(sy, x, th, pj, sd, F, hstep):
    """dF/dtheta by one FD build (same node set); dF/domega from it analytically.
    The basis depends on (theta, omega) only through u = theta*omega, and L_m carries i*omega*m*M_m
    explicitly, so dF/domega = (theta/omega) dF/dtheta + flat(i m M_m A_m)."""
    n, K = sy.n, sy.K
    A, om = unpack(x, n, K)
    rate = 4 * K * om * th if th > 0 else arb(0)
    sd2 = sy.build(om, th + hstep, rate_override=rate)
    R2, _ = residual(sd2, A, n, K); F2 = flatF(R2, A, n, K, pj)
    Fth = [mid((F2[i] - F[i]) / hstep) for i in range(len(F))]
    ex = {0: acb_mat(n, 1)}
    for m in range(1, K + 1): ex[m] = (sd['M'][m] * A[m]) * acb(0, m)
    E = flatF(ex, A, n, K, pj); E[-1] = arb(0)
    Fom = [mid(th / om * Fth[i] + E[i]) for i in range(len(F))]
    return Fth, Fom

def corrector_chord(sy, y_pred, t, W, pj, maxit=10, log=LOG):
    """Pseudo-arclength corrector: full Newton until |F| < 1e-15(1+|A|), then the bordered Jacobian is
    frozen while each iteration gains >= 6 digits. Returns (y, nf, ok, its)."""
    n, K = sy.n, sy.K
    tol = arb(10) ** (-(DPS - 20)); hstep = arb(10) ** (-(DPS // 2))
    y = [mid(v) for v in y_pred]; D = len(y) - 1
    Mfac = None; prev = None; nf = None
    for it in range(maxit + 1):
        x, th = y[:D], y[D] / W
        if not (th > -1) or not (th < 2): return y, nf, False, it
        A, om = unpack(x, n, K)
        if not (om > 0): return y, nf, False, it
        sd = sy.build(om, th); R, G = residual(sd, A, n, K)
        F = flatF(R, A, n, K, pj)
        cons = sum((t[i] * (y[i] - y_pred[i]) for i in range(D + 1)), arb(0))
        nf = mid(norm(F + [cons])); xn = mid(norm(x[:-1]))
        if nf < tol * (1 + xn): return y, nf, True, it
        if it == maxit or not (nf < arb(10) ** 12): return y, nf, False, it
        # full Newton while far from the solution; chord (reuse) only once the residual is tiny
        # and contracting fast, where a frozen Jacobian still gains >= 6 digits per iteration
        if Mfac is None or nf > arb(10) ** -15 * (1 + xn) or (prev is not None and nf > prev / 10 ** 6):
            Fth, Fom = theta_omega_columns(sy, x, th, pj, sd, F, hstep)
            Jx = jacobian(sy, x, th, pj, sd, F, G, hstep, omega_col=Fom)
            Mb = arb_mat(D + 1, D + 1)
            for i in range(D):
                for j in range(D): Mb[i, j] = Jx[i, j]
                Mb[i, D] = Fth[i] / W
            for j in range(D + 1): Mb[D, j] = t[j]
            Mt = Mb.transpose(); N_ = Mt * Mb
            shift = mid(sum((abs(N_[i, i]) for i in range(D + 1)), arb(0)) / (D + 1)) * arb(10) ** (-(DPS - 15))
            for i in range(D + 1): N_[i, i] += shift
            Mfac = (Mt, N_)
        prev = nf
        Mt, N_ = Mfac
        dy = N_.solve(Mt * arb_mat(D + 1, 1, F + [cons]), algorithm="approx")
        y = [mid(y[i] - dy[i, 0]) for i in range(D + 1)]
    return y, nf, False, maxit

def _vec(v): return [s40(a, DPS) for a in v]
def _unvec(v): return [arb(a) for a in v]

def arclength_run(sy, x0, pj, checkpoint, state=None, th1=arb(1) / 80, log=LOG,
                  tmax=1e9, amp_escape=arb(10) ** 4, S_lo=arb(10) ** -3, S_hi=arb(10) ** 3):
    """Checkpointed secant pseudo-arclength continuation in theta.  checkpoint(state) is called after
    every accepted point (state is JSON-ready).  Stops at the first of: theta >= 1 (then Newton at
    theta = 1 exactly), theta < 0 (returns to theta = 0), closure on the start point, escape
    (|A| > amp_escape*|A_0| or S outside [S_lo, S_hi]), collapse to steady/trivial, step underflow,
    or the time budget."""
    t_end = time.time() + tmax
    if state is None:
        x, nf, h, ok = newton(sy, x0, arb(0), pj, maxit=10, log=log)
        rec = summary(x, sy, nf, ok, arb(0)); rec['amp'] = s40(norm(x[:-1]), 20)
        if not ok or rec['cls'] != 'periodic':
            return x, dict(path=[rec], verdict='no_theta0_orbit')
        W = mid(norm(x[:-1]))
        x1, nf1, _, ok1 = newton(sy, x, th1, pj, maxit=10, log=log)
        r1 = summary(x1, sy, nf1, ok1, th1); r1['amp'] = s40(norm(x1[:-1]), 20)
        if not ok1: return x, dict(path=[rec, r1], verdict='first_natural_step_fails')
        y0 = x + [arb(0)]; y1 = x1 + [W * th1]
        ds = mid(norm([y1[i] - y0[i] for i in range(len(y0))]))
        state = dict(path=[rec, r1], W=s40(W, DPS), y_start=_vec(y0), y0=_vec(y0), y1=_vec(y1),
                     ds=s40(ds, 30), ds_init=s40(ds, 30), dth_sign=1, folds=[], steps=0, verdict='running')
        checkpoint(state)
    W = arb(state['W']); y0 = _unvec(state['y0']); y1 = _unvec(state['y1']); ys = _unvec(state['y_start'])
    ds = arb(state['ds']); ds0 = arb(state['ds_init']); dsmin = ds0 / 64; dsmax = ds0 * 32
    A0 = mid(norm(ys[:-2]))
    def finish(v, xv):
        state['verdict'] = v; state['y1'] = _vec(y1); state['ds'] = s40(ds, 30); checkpoint(state); return xv, state
    while True:
        if time.time() > t_end: return finish(f"time_budget_at_theta_{s40(y1[-1] / W, 8)}", y1[:-1])
        sec = [y1[i] - y0[i] for i in range(len(y0))]; L_ = mid(norm(sec)); t = [v / L_ for v in sec]
        yp = [mid(y1[i] + ds * t[i]) for i in range(len(y1))]
        t0 = time.time()
        y, nf, ok, its = corrector_chord(sy, yp, t, W, pj, log=log)
        state['steps'] += 1
        if not ok:
            ds = ds / 2
            log(f"   step {state['steps']}: corrector fails after {its} its ({time.time()-t0:.0f}s), ds -> {ds.str(4, radius=False)}")
            if ds < dsmin: return finish(f"step_underflow_at_theta_{s40(y1[-1] / W, 8)}", y1[:-1])
            continue
        D = len(y) - 1; th = y[D] / W
        new_sec = [y[i] - y1[i] for i in range(D + 1)]
        reversed_ = sum((new_sec[i] * t[i] for i in range(D + 1)), arb(0)) < 0
        rec = summary(y[:D], sy, nf, True, th); rec['amp'] = s40(norm(y[:D - 1]), 20); rec['corrector_its'] = its
        sgn = 1 if th > y1[D] / W else -1
        if sgn != state['dth_sign']:
            state['folds'].append(s40(y1[D] / W, 12)); rec['fold_before'] = True; state['dth_sign'] = sgn
        state['path'].append(rec)
        amp = mid(norm(y[:D - 1])); om = y[D - 1]
        log(f"   step {state['steps']}: theta={s40(th, 10)} S={rec['period_S'][:20] if rec['period_S'] else None} "
            f"|A|={amp.str(10, radius=False)} res={rec['residual']} its={its} folds={len(state['folds'])} ({time.time()-t0:.0f}s)")
        y0, y1 = y1, y
        state['y0'] = _vec(y0); state['y1'] = _vec(y1)
        # a 60-digit corrector needs ~5 Newton + 1-2 frozen iterations even on easy steps, so the
        # step only shrinks when the corrector is close to its iteration limit
        g = arb(2) if its <= 5 else (arb(3) / 2 if its <= 7 else (arb(1) if its <= 9 else arb(7) / 10))
        ds = min(ds * g, dsmax); state['ds'] = s40(ds, 30)
        checkpoint(state)
        if reversed_:
            # the accepted point lies behind the previous one along the secant: the corrector has
            # landed back on the incoming path (it is not a fold in theta, which keeps the secant's sign)
            return finish(f"continuation_reversed_at_theta_{s40(y0[-1] / W, 8)}", y[:D])
        if rec['cls'] != 'periodic': return finish('collapsed_to_' + rec['cls'], y[:D])
        if not (om > 0) or (2 * arb.pi() / om) > S_hi: return finish('escape_S_to_infinity_or_omega_to_0', y[:D])
        if (2 * arb.pi() / om) < S_lo: return finish('escape_S_to_0', y[:D])
        if amp > amp_escape * A0: return finish('escape_amplitude', y[:D])
        if th < 0: return finish(f"returns_to_theta_0_after_{len(state['folds'])}_folds", y[:D])
        if state['steps'] > 3 and mid(norm([y[i] - ys[i] for i in range(D + 1)])) < ds0 / 4:
            return finish('closes_on_start_point', y[:D])
        if th >= 1:
            xf, nff, _, okf = newton(sy, y[:D], arb(1), pj, maxit=12, log=log)
            rf = summary(xf, sy, nff, okf, arb(1)); rf['amp'] = s40(norm(xf[:-1]), 20)
            state['path'].append(rf); state['x_theta1'] = _vec(xf)
            return finish('reached_theta_1' if okf else 'theta1_newton_fails', xf)

def refine_chain(sy, x, pj, log=LOG):
    """K -> K+1, then N -> N+1, then L -> L+1 (same axi flag), theta = 1."""
    out = []
    steps = [(sy.L, sy.N, sy.K + 1), (sy.L, sy.N + 1, sy.K), (sy.L + 1, sy.N, sy.K)]
    persisted = 0
    for (L, N, K) in steps:
        s2 = System(L, N, K, axi=sy.axi)
        y = embed(x, sy, s2)
        pj2 = {l: i for i, l in enumerate(s2.labels)}[sy.labels[pj]]
        xr, nf, h, ok = newton(s2, y, arb(1), pj2, maxit=12, log=log)
        rec = summary(xr, s2, nf, ok, arb(1)); rec['step'] = f"L{L}N{N}K{K}"
        out.append(rec)
        log(f"  refine {rec['step']}: ok={ok} cls={rec['cls']} S={rec['period_S']} res={rec['residual']}")
        if ok and rec['cls'] == 'periodic': persisted += 1
    return out, persisted

def random_search(sy, nstarts, rng, S0s, log=LOG):
    n, K = sy.n, sy.K
    hits = []
    counts = dict(trivial=0, steady=0, periodic=0, fail=0)
    for t in range(nstarts):
        S0 = arb(S0s[t % len(S0s)])
        amp = arb(10) ** (arb(rng.randint(0, 2500)) / 1000)   # 1 .. 316
        x = [arb(rng.gauss(0, 1)) * amp / (1 + (i // n)) for i in range(n * (2 * K + 1))] + [2 * arb.pi() / S0]
        pj = 0
        x[n + n * K + pj] = arb(0)
        t0 = time.time()
        xr, nf, h, ok = newton(sy, x, arb(1), pj, maxit=20, log=lambda *a: None)
        cls = classify(xr, n, K)[0] if ok else 'fail'
        counts[cls] += 1
        S = (2 * arb.pi() / xr[-1]).str(10, radius=False) if xr[-1] > 0 else '-'
        log(f"  start {t} S0={s40(S0,4)} amp={amp.str(3, radius=False)} -> {cls} S={S} res={nf.str(3, radius=False)} its={len(h)} {time.time()-t0:.0f}s")
        if cls == 'periodic':
            hits.append((xr, pj, summary(xr, sy, nf, ok, arb(1))))
    return counts, hits

def main():
    mode = sys.argv[1]
    tag = os.environ.get("LERAY_TAG", "")
    outf = os.path.join(HERE, f"leray-dss-logphase-{mode}{tag}.witness.json")
    out = dict(description=__doc__.strip().splitlines()[0], dps=DPS, radial_rule=dict(QN=QN, phase_per_panel=s40(PHASE_PER_PANEL, 4)),
               trial_tail='(1+rho)^-(p + i theta m w); theta=1: mode m decays like |y|^(-1-2imw)', mode=mode)
    def save(): json.dump(out, open(outf, 'w'), indent=1)
    if mode == 'validate':
        # theta = 0 reproduces the phase-1 system: phase-1 mpmath steady solutions as residual test
        w = json.load(open(os.path.join(HERE, 'leray-dss-galerkin-search.witness.json')))
        out['phase1_steady_residuals'] = []
        for r in w['results']:
            if (r['L'], r['N']) not in [(2, 2), (2, 3)]: continue
            sy = System(r['L'], r['N'], 0); sd = sy.build(arb(1), arb(0))
            for c in r['candidates']:
                A = {0: acb_mat(sy.n, 1, [acb(arb(v)) for v in c['a']])}
                R, _ = residual(sd, A, sy.n, 0)
                out['phase1_steady_residuals'].append(dict(L=r['L'], N=r['N'], coeff_norm=c['coeff_norm'][:20],
                    max_abs_residual=max(abs(R[0][i, 0]) for i in range(sy.n)).str(5, radius=False)))
                LOG("  ", out['phase1_steady_residuals'][-1])
        out['quadrature_check'] = []
        for (L, N, K, S) in [(2, 2, 4, '0.47'), (2, 3, 3, '0.8'), (3, 2, 3, '1.0')]:
            sy = System(L, N, K)
            qc = quadrature_check(sy, 2 * arb.pi() / arb(S), arb(1)); qc.update(L=L, N=N, K=K, S=S)
            out['quadrature_check'].append(qc); LOG("  quad", qc); save()
    elif mode in ('homotopyB', 'homotopyC'):
        L, N = (2, 2) if mode == 'homotopyB' else (2, 3)
        K = int(os.environ.get('LERAY_K', '4'))
        s = json.load(open(os.path.join(HERE, 'leray_dss_galerkin_seeds.json')))
        cs = [c for c in s['cases'] if c['L'] == L and c['N'] == N][0]['periodic_seeds'][0]
        sy = System(L, N, K)
        x0, pj = seed_from_phase1(sy, cs)
        if os.environ.get('LERAY_ARC'):
            x, path, verdict = arclength_homotopy(sy, x0, pj)
        else:
            x, path, verdict = homotopy(sy, x0, pj)
        out.update(L=L, N=N, K=K, seed=cs['source'], path=path, verdict=verdict)
        LOG("VERDICT", verdict); save()
        if verdict == 'reached_theta_1':
            ref, persisted = refine_chain(sy, x, pj); out['refinement'] = ref; out['persisted_count'] = persisted
            if persisted >= 2: LOG("!!! PERSISTS ACROSS TWO REFINEMENTS — STOP AND REPORT")
            save()
    elif mode in ('arcB', 'arcC'):
        # Phase 4: checkpointed pseudo-arclength continuation; the witness is rewritten after every
        # accepted point, so a manual stop leaves a probe-written file. LERAY_RESUME=1 continues from it.
        L, N = (2, 2) if mode == 'arcB' else (2, 3)
        K = int(os.environ.get('LERAY_K', '4'))
        s = json.load(open(os.path.join(HERE, 'leray_dss_galerkin_seeds.json')))
        cs = [c for c in s['cases'] if c['L'] == L and c['N'] == N][0]['periodic_seeds'][0]
        sy = System(L, N, K)
        x0, pj = seed_from_phase1(sy, cs)
        state = None
        if os.environ.get('LERAY_RESUME') and os.path.exists(outf):
            prev = json.load(open(outf))
            if prev.get('state', {}).get('verdict', '').startswith(('running', 'time_budget')):
                state = prev['state']; state['verdict'] = 'running'
                if os.environ.get('LERAY_REVERSE'):
                    # walk back along the stored secant with a small step to resolve a sharp turn
                    state['y0'], state['y1'] = state['y1'], state['y0']
                    state['ds'] = s40(arb(state['ds_init']) / 4, 30)
                    state.setdefault('reversed_at_steps', []).append(state['steps'])
                state.setdefault('resumed_at_steps', []).append(state['steps'])
                LOG(f"RESUME from step {state['steps']}")
        out.update(L=L, N=N, K=K, seed=cs['source'], phase_condition_index=pj,
                   method='secant pseudo-arclength in (x, W*theta), chord-Newton corrector; '
                          'dF/dtheta by FD (h=1e-%d), dF/domega = (theta/omega) dF/dtheta + i m M_m A_m' % (DPS // 2))
        def ckpt(st):
            out['state'] = st; out['verdict'] = st['verdict']; out['n_points'] = len(st['path']); save()
        x, st = arclength_run(sy, x0, pj, ckpt, state=state, tmax=float(os.environ.get('LERAY_TMAX', '1e9')))
        LOG("VERDICT", st['verdict'])
        if st['verdict'] == 'reached_theta_1':
            ref, persisted = refine_chain(sy, x, pj); out['refinement'] = ref; out['persisted_count'] = persisted
            if persisted >= 1: LOG("!!! THETA=1 CANDIDATE PERSISTS UNDER REFINEMENT — STOP AND REPORT")
            save()
    elif mode == 'random':
        rng = random.Random(int(os.environ.get('LERAY_SEED', '20261121')))
        nst = int(os.environ.get('LERAY_NSTARTS', '20'))
        S0s = ['0.5', '0.75', '1', '1.5', '2', '3', '4', '6', '8', '12']
        out['searches'] = []
        for tok in os.environ.get('LERAY_SYSTEMS', '2,2,3,axi;2,3,3,axi;3,2,3,axi;3,3,3,axi').split(';'):
            p = tok.split(','); L, N, K = int(p[0]), int(p[1]), int(p[2]); axi = len(p) > 3 and p[3] == 'axi'
            sy = System(L, N, K, axi=axi)
            LOG(f"== random L{L}N{N}K{K} axi={axi}")
            counts, hits = random_search(sy, nst, rng, S0s)
            rec = dict(L=L, N=N, K=K, axi=axi, starts=nst, S0=S0s, counts=counts, hits=[h[2] for h in hits], refinement=[])
            for (xr, pj, sm) in hits:
                ref, persisted = refine_chain(sy, xr, pj)
                rec['refinement'].append(dict(hit=sm, chain=ref, persisted_count=persisted))
                if persisted >= 2: LOG("!!! PERSISTS ACROSS TWO REFINEMENTS — STOP AND REPORT")
            out['searches'].append(rec); save()
    save(); LOG("WROTE", outf)

if __name__ == '__main__':
    main()
