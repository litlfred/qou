#!/usr/bin/env python3
"""Leray DSS Galerkin search -- mpmath verification stage (numerical exploration, NOT a proof).

Backward self-similar Navier--Stokes profile system (y = x/sqrt(T-t), s = -log(T-t)):

    d_s V - Lap V + V/2 + (y.grad)V/2 + (V.grad)V + grad P = 0,   div V = 0,

discretely self-similar (DSS) = V periodic in s with unknown period S (scale factor
lambda = exp(S/2)).  Steady (S-independent) is the zero Fourier mode.

Discretisation (Petrov--Galerkin, pressure-free):
  * angular: toroidal / poloidal vector fields built from real solid harmonics H of
    degree l = 1..L (exact rational basis of ker Lap on degree-l homogeneous polys):
        toroidal  T[H,R] = R(rho) (grad H x y)
        poloidal  P[H,R] = curl curl (y H R) = S grad H - 2 l R'(rho) H y,
                  S = (l+1) R + 2 rho R'(rho),   rho = |y|^2
    both exactly divergence free.
  * TRIAL radial functions R = (1+rho)^(-p): p = (l+1)/2 + n (toroidal),
    p = l/2 + n (poloidal), n = 0..N-1.  The n = 0 member has an exact |y|^-1 tail,
    so the trial space is in weak-L3 (and NOT in L3): scale-critical decay.
  * TEST radial functions R = rho^n exp(-rho/4), n = 0..N-1 (Gaussian, so the
    pressure term integrates to zero against every divergence-free test field and
    -Lap integrates by parts).
  * time: Fourier modes exp(2 pi i m s / S), |m| <= K.  For the steady branch only
    m = 0 is needed and this stage verifies only steady candidates (no periodic
    candidate was found in the float64 exploration; see the audit doc).

Integrals are exact in angle (Gauss-Legendre x uniform rule of sufficient degree on
polynomial integrands) and composite Gauss-Legendre in r (integrands analytic,
Gaussian decaying); the quadrature error is measured by doubling the radial nodes.

Everything below is mpmath (no float64 arithmetic); float() appears only in display.
Seeds (starting points for Newton) come from the scratch float64 exploration and are
read as decimal strings from the witness seed file; the converged values reported are
those of the mpmath Newton iteration.
"""
import json, sys, os, time, itertools
from fractions import Fraction
import mpmath as mp

DPS = int(os.environ.get("LERAY_DPS", "60"))
mp.mp.dps = DPS
ALPHA = mp.mpf(1) / 4          # test Gaussian exp(-rho/4)  (OU weight)
EDGES = [0, '0.5', '1.5', 3, 5, 8, 12, 17, 22, 28]

# ---------------------------------------------------------------- harmonics (exact)
def monomials(l):
    return [(i, j, l - i - j) for i in range(l + 1) for j in range(l + 1 - i)]

def harmonic_basis_rational(l):
    """Rational basis of harmonic homogeneous polys of degree l (RREF nullspace)."""
    mons = monomials(l)
    if l < 2:
        return mons, [[Fraction(int(i == k)) for i in range(len(mons))] for k in range(len(mons))]
    lo = monomials(l - 2); idx = {m: k for k, m in enumerate(lo)}
    D = [[Fraction(0)] * len(mons) for _ in lo]
    for c, e in enumerate(mons):
        for k in range(3):
            if e[k] >= 2:
                m = list(e); m[k] -= 2; D[idx[tuple(m)]][c] += e[k] * (e[k] - 1)
    # RREF
    A = [row[:] for row in D]; piv = []; r = 0
    for c in range(len(mons)):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]; pv = A[r][c]; A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
        if r == len(A): break
    free = [c for c in range(len(mons)) if c not in piv]
    basis = []
    for f in free:
        v = [Fraction(0)] * len(mons); v[f] = Fraction(1)
        for i, pc in enumerate(piv): v[pc] = -A[i][f]
        basis.append(v)
    return mons, basis

def poly_eval(mons, coef, y):
    """value, gradient, hessian of sum coef*y^e at point y (mpf triple)."""
    v = mp.mpf(0); g = [mp.mpf(0)] * 3; h = [[mp.mpf(0)] * 3 for _ in range(3)]
    def mon(e):
        if min(e) < 0: return mp.mpf(0)
        return y[0] ** e[0] * y[1] ** e[1] * y[2] ** e[2]
    for e, c in zip(mons, coef):
        if c == 0: continue
        c = mp.mpf(c.numerator) / c.denominator
        v += c * mon(e)
        for k in range(3):
            if e[k] > 0:
                ek = list(e); ek[k] -= 1; g[k] += c * e[k] * mon(ek)
                for j in range(3):
                    if ek[j] > 0:
                        ekj = list(ek); f = ekj[j]; ekj[j] -= 1
                        h[k][j] += c * e[k] * f * mon(ekj)
    return v, g, h

EPS = {}
for i, j, k in itertools.permutations(range(3)):
    EPS[(i, j, k)] = 1 if (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1
def eps(i, j, k): return EPS.get((i, j, k), 0)

# ------------------------------------------------- separable (radial x angular) terms
# A field is sum_t rad_t(r) * ang_t(yhat).  For V: ang is a 3-vector, for J: 3x3 (J[i][k]=d_k V_i).
def angular_terms(kind, l, mons, coef, u):
    H, dH, HH = poly_eval(mons, coef, u)
    if kind == 'T':
        g = [sum(eps(i, j, m) * dH[j] * u[m] for j in range(3) for m in range(3)) for i in range(3)]
        V = [g]
        J1 = [[u[k] * g[i] for k in range(3)] for i in range(3)]
        J2 = [[sum(eps(i, j, m) * HH[k][j] * u[m] for j in range(3) for m in range(3))
               + sum(eps(i, j, k) * dH[j] for j in range(3)) for k in range(3)] for i in range(3)]
        J = [J1, J2]
    else:
        V = [list(dH), [H * u[i] for i in range(3)]]
        J = [[[u[k] * dH[i] for k in range(3)] for i in range(3)],
             [[HH[k][i] for k in range(3)] for i in range(3)],
             [[u[k] * u[i] * H for k in range(3)] for i in range(3)],
             [[dH[k] * u[i] + (H if i == k else 0) for k in range(3)] for i in range(3)]]
    return V, J

def radial_terms(kind, l, n, r, side):
    rho = r * r
    if side == 'trial':
        p = mp.mpf(l + 1) / 2 + n if kind == 'T' else mp.mpf(l) / 2 + n
        u = 1 + rho
        R = u ** (-p); R1 = -p * u ** (-p - 1); R2 = p * (p + 1) * u ** (-p - 2)
    else:
        a = ALPHA; ex = mp.exp(-a * rho)
        R = rho ** n * ex
        R1 = ((n * rho ** (n - 1) if n > 0 else 0) - a * rho ** n) * ex
        R2 = ((n * (n - 1) * rho ** (n - 2) if n > 1 else 0) - 2 * a * (n * rho ** (n - 1) if n > 0 else 0)
              + a * a * rho ** n) * ex
    if kind == 'T':
        V = [R * r ** l]
        J = [2 * R1 * r ** (l + 1), R * r ** (l - 1)]
    else:
        S = (l + 1) * R + 2 * rho * R1; S1 = (l + 3) * R1 + 2 * rho * R2
        C = -2 * l * R1; C1 = -2 * l * R2
        V = [S * r ** (l - 1), C * r ** (l + 1)]
        J = [2 * S1 * r ** l, (S * r ** (l - 2) if l >= 2 else mp.mpf(0)), 2 * C1 * r ** (l + 2), C * r ** l]
    return V, J

def quad_rules(L, m_rad):
    xs, ws = gauss_legendre(m_rad)
    rn, rw = [], []
    E = [mp.mpf(e) for e in EDGES]
    for a, b in zip(E[:-1], E[1:]):
        for x, w in zip(xs, ws):
            r = (a + b) / 2 + (b - a) / 2 * x
            rn.append(r); rw.append((b - a) / 2 * w * r * r)
    deg = 3 * L + 6
    nt = deg // 2 + 2; nph = deg + 2
    ct, wt = gauss_legendre(nt)
    an, aw = [], []
    for c, w in zip(ct, wt):
        st = mp.sqrt(1 - c * c)
        for k in range(nph):
            ph = 2 * mp.pi * k / nph
            an.append((st * mp.cos(ph), st * mp.sin(ph), c)); aw.append(w * 2 * mp.pi / nph)
    return rn, rw, an, aw

_GL = {}
def gauss_legendre(m):
    if m in _GL: return _GL[m]
    xs, ws = [], []
    for k in range(1, m + 1):
        x = mp.cos(mp.pi * (k - mp.mpf(1) / 4) / (m + mp.mpf(1) / 2))
        for _ in range(100):
            p0, p1 = mp.mpf(1), x
            for j in range(2, m + 1):
                p0, p1 = p1, ((2 * j - 1) * x * p1 - (j - 1) * p0) / j
            dp = m * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp; x -= dx
            if abs(dx) < mp.mpf(10) ** (-mp.mp.dps - 5): break
        p0, p1 = mp.mpf(1), x
        for j in range(2, m + 1):
            p0, p1 = p1, ((2 * j - 1) * x * p1 - (j - 1) * p0) / j
        dp = m * (x * p1 - p0) / (x * x - 1)
        xs.append(x); ws.append(2 / ((1 - x * x) * dp * dp))
    _GL[m] = (xs, ws); return xs, ws

# ------------------------------------------------------------------- assemble system
def build_system(L, N, m_rad=40, log=print):
    t0 = time.time()
    rn, rw, an, aw = quad_rules(L, m_rad)
    labels = []; akeys = []; rkeys = []
    harm = {l: harmonic_basis_rational(l) for l in range(1, L + 1)}
    for l in range(1, L + 1):
        for h in range(len(harm[l][1])):
            for kind in 'TP':
                for n in range(N):
                    labels.append((kind, l, h, n))
    akeys = sorted({(k, l, h) for (k, l, h, n) in labels})
    rkeys = sorted({(k, l, n) for (k, l, h, n) in labels})
    # angular tables
    AV, AJ = {}, {}
    for (k, l, h) in akeys:
        mons, bas = harm[l]
        vals = [angular_terms(k, l, mons, bas[h], u) for u in an]
        AV[(k, l, h)] = [[v[0][t] for v in vals] for t in range(len(vals[0][0]))]
        AJ[(k, l, h)] = [[v[1][t] for v in vals] for t in range(len(vals[0][1]))]
    RV, RJ = {}, {}
    for side in ('trial', 'test'):
        for (k, l, n) in rkeys:
            vals = [radial_terms(k, l, n, r, side) for r in rn]
            RV[(side, k, l, n)] = [[v[0][t] for v in vals] for t in range(len(vals[0][0]))]
            RJ[(side, k, l, n)] = [[v[1][t] for v in vals] for t in range(len(vals[0][1]))]
    log(f"  tables L={L} N={N} m_rad={m_rad}: {len(rn)} radial x {len(an)} angular nodes ({time.time()-t0:.0f}s)")
    def rint(*fs):
        return mp.fsum(w * mp.fprod([f[i] for f in fs]) for i, w in enumerate(rw))
    # angular integrals
    def a_vv(A, B):  # sum_i A_i B_i
        return mp.fsum(w * mp.fsum(A[g][i] * B[g][i] for i in range(3)) for g, w in enumerate(aw))
    def a_jj(A, B):
        return mp.fsum(w * mp.fsum(A[g][i][k] * B[g][i][k] for i in range(3) for k in range(3)) for g, w in enumerate(aw))
    def a_vyj(A, B):  # A_i * yhat_k * B_ik
        return mp.fsum(w * mp.fsum(A[g][i] * an[g][k] * B[g][i][k] for i in range(3) for k in range(3)) for g, w in enumerate(aw))
    n = len(labels)
    Ms = mp.matrix(n, n); Lm = mp.matrix(n, n)
    cacheA = {}; cacheR = {}
    for a, (ka, la, ha, na) in enumerate(labels):
        for b, (kb, lb, hb, nb) in enumerate(labels):
            Aa, Ab = (ka, la, ha), (kb, lb, hb)
            key = (Aa, Ab)
            if key not in cacheA:
                cacheA[key] = (
                    [[a_vv(AV[Aa][s], AV[Ab][t]) for t in range(len(AV[Ab]))] for s in range(len(AV[Aa]))],
                    [[a_jj(AJ[Aa][s], AJ[Ab][t]) for t in range(len(AJ[Ab]))] for s in range(len(AJ[Aa]))],
                    [[a_vyj(AV[Aa][s], AJ[Ab][t]) for t in range(len(AJ[Ab]))] for s in range(len(AV[Aa]))])
            Avv, Ajj, Avyj = cacheA[key]
            rk = (('test', ka, la, na), ('trial', kb, lb, nb))
            if rk not in cacheR:
                Va, Ja = RV[rk[0]], RJ[rk[0]]; Vb, Jb = RV[rk[1]], RJ[rk[1]]
                rr = [x * 1 for x in rn]
                cacheR[rk] = (
                    [[rint(Va[s], Vb[t]) for t in range(len(Vb))] for s in range(len(Va))],
                    [[rint(Ja[s], Jb[t]) for t in range(len(Jb))] for s in range(len(Ja))],
                    [[rint(Va[s], Jb[t], rr) for t in range(len(Jb))] for s in range(len(Va))])
            Rvv, Rjj, Rvyj = cacheR[rk]
            mass = mp.fsum(Rvv[s][t] * Avv[s][t] for s in range(len(Avv)) for t in range(len(Avv[0])))
            grad = mp.fsum(Rjj[s][t] * Ajj[s][t] for s in range(len(Ajj)) for t in range(len(Ajj[0])))
            ydv = mp.fsum(Rvyj[s][t] * Avyj[s][t] for s in range(len(Avyj)) for t in range(len(Avyj[0])))
            Ms[a, b] = mass; Lm[a, b] = grad + mass / 2 + ydv / 2
    log(f"  linear part done ({time.time()-t0:.0f}s)")
    # nonlinear  B[a,b,c] = int psi_a,i phi_b,k d_k phi_c,i
    angB = {}
    for A1 in akeys:
        for A2 in akeys:
            for A3 in akeys:
                angB[(A1, A2, A3)] = [[[mp.fsum(w * mp.fsum(AV[A1][s][g][i] * AV[A2][t][g][k] * AJ[A3][u][g][i][k]
                                                              for i in range(3) for k in range(3)) for g, w in enumerate(aw))
                                        for u in range(len(AJ[A3]))] for t in range(len(AV[A2]))] for s in range(len(AV[A1]))]
    log(f"  angular nonlinear tables done ({time.time()-t0:.0f}s)")
    radB = {}
    for R1 in rkeys:
        for R2 in rkeys:
            for R3 in rkeys:
                Va = RV[('test',) + R1]; Vb = RV[('trial',) + R2]; Jc = RJ[('trial',) + R3]
                radB[(R1, R2, R3)] = [[[rint(Va[s], Vb[t], Jc[u]) for u in range(len(Jc))] for t in range(len(Vb))] for s in range(len(Va))]
    log(f"  radial nonlinear tables done ({time.time()-t0:.0f}s)")
    B = {}
    for a, (ka, la, ha, na) in enumerate(labels):
        for b, (kb, lb, hb, nb) in enumerate(labels):
            for c, (kc, lc, hc, nc) in enumerate(labels):
                Ag = angB[((ka, la, ha), (kb, lb, hb), (kc, lc, hc))]
                Rd = radB[((ka, la, na), (kb, lb, nb), (kc, lc, nc))]
                v = mp.fsum(Rd[s][t][u] * Ag[s][t][u] for s in range(len(Ag)) for t in range(len(Ag[0])) for u in range(len(Ag[0][0])))
                if v != 0: B[(a, b, c)] = v
    log(f"  system assembled n={n}, nnz(B)={len(B)} ({time.time()-t0:.0f}s)")
    return dict(labels=labels, Ms=Ms, L=Lm, B=B, n=n)

# ------------------------------------------------------------------ steady Newton
def residual(sysd, a):
    n = sysd['n']; F = sysd['L'] * a
    for (i, j, k), v in sysd['B'].items():
        F[i] += v * a[j] * a[k]
    return F

def jacobian(sysd, a):
    n = sysd['n']; J = sysd['L'].copy()
    for (i, j, k), v in sysd['B'].items():
        J[i, j] += v * a[k]; J[i, k] += v * a[j]
    return J

def lstsq_step(J, F):
    # minimum-norm least squares via normal equations with a tiny Tikhonov shift
    # (rotational zero modes make J rank deficient; the shift is far below the residual floor)
    JT = J.T; A = JT * J; n = A.rows
    shift = mp.mpf(10) ** (-(mp.mp.dps // 2)) * mp.mnorm(A, 1)
    for i in range(n): A[i, i] += shift
    return -mp.lu_solve(A, JT * F)

def newton(sysd, a0, maxit=40, log=print):
    a = a0.copy(); hist = []
    for it in range(maxit):
        F = residual(sysd, a); nf = mp.norm(F); hist.append(nf)
        if nf < mp.mpf(10) ** (-(DPS - 8)) * max(1, mp.norm(a)): break
        a = a + lstsq_step(jacobian(sysd, a), F)
    F = residual(sysd, a)
    return a, mp.norm(F), hist

# ------------------------------------------------------- periodic (DSS) Newton
# Unknowns: A_0 real, A_m complex (m=1..K), omega = 2 pi / S.  A_{-m} = conj(A_m).
# R_m = (L + i omega m Ms) A_m + sum_{m1} B(A_{m1}, A_{m-m1}),  m = 0..K  (exact truncated
# convolution, |m1|,|m-m1| <= K).  Phase condition: Im A_1[0] = 0.
def _mode(A, m):
    return A[m] if m >= 0 else [mp.conj(z) for z in A[-m]]

def periodic_residual(sysd, A, om, K):
    n = sysd['n']; R = []
    for m in range(K + 1):
        r = [mp.fsum(sysd['L'][i, j] * A[m][j] + 1j * om * m * sysd['Ms'][i, j] * A[m][j] for j in range(n)) for i in range(n)]
        for m1 in range(-K, K + 1):
            m2 = m - m1
            if abs(m2) > K: continue
            u = _mode(A, m1); v = _mode(A, m2)
            for (i, j, k), b in sysd['B'].items():
                r[i] += b * u[j] * v[k]
        R.append(r)
    return R

def _flat(R, A, K, n):
    out = [mp.re(x) for x in R[0]]
    for m in range(1, K + 1): out += [mp.re(x) for x in R[m]]
    for m in range(1, K + 1): out += [mp.im(x) for x in R[m]]
    out.append(mp.im(A[1][0]))
    return mp.matrix(out)

def periodic_jacobian(sysd, A, om, K):
    n = sysd['n']; D = n * (2 * K + 1) + 1
    G = {}
    for d in range(-K, K + 1):
        Ad = _mode(A, d); Gd = [[mp.mpc(0)] * n for _ in range(n)]
        for (i, j, k), b in sysd['B'].items():
            Gd[i][j] += b * Ad[k]; Gd[i][k] += b * Ad[j]
        G[d] = Gd
    zero = [[mp.mpc(0)] * n for _ in range(n)]
    def g(d): return G[d] if abs(d) <= K else zero
    J = mp.matrix(D, D)
    def rowblocks(m):  # (row offset real, row offset imag or None)
        if m == 0: return 0, None
        return n + (m - 1) * n, n + n * K + (m - 1) * n
    for m in range(K + 1):
        ro, io = rowblocks(m)
        for p in range(K + 1):
            if p == 0:
                cols = [(0, None)]
            else:
                cols = [(n + (p - 1) * n, 're'), (n + n * K + (p - 1) * n, 'im')]
            for co, typ in cols:
                for i in range(n):
                    for j in range(n):
                        if p == 0:
                            v = g(m)[i][j] + (sysd['L'][i, j] if m == 0 else 0)
                        elif typ == 're':
                            v = g(m - p)[i][j] + g(m + p)[i][j]
                            if m == p: v += sysd['L'][i, j] + 1j * om * m * sysd['Ms'][i, j]
                        else:
                            v = 1j * (g(m - p)[i][j] - g(m + p)[i][j])
                            if m == p: v += 1j * (sysd['L'][i, j] + 1j * om * m * sysd['Ms'][i, j])
                        J[ro + i, co + j] = mp.re(v)
                        if io is not None: J[io + i, co + j] = mp.im(v)
        # omega column
        for i in range(n):
            v = 1j * m * mp.fsum(sysd['Ms'][i, j] * A[m][j] for j in range(n))
            J[ro + i, D - 1] = mp.re(v)
            if io is not None: J[io + i, D - 1] = mp.im(v)
    J[D - 1, n + n * K] = 1
    return J

def periodic_newton(sysd, A, om, K, maxit=12, log=print):
    n = sysd['n']; hist = []
    for it in range(maxit):
        F = _flat(periodic_residual(sysd, A, om, K), A, K, n); nf = mp.norm(F); hist.append(nf)
        log(f"    periodic Newton it={it} |F|={mp.nstr(nf,4)} S={mp.nstr(2*mp.pi/om,15)}")
        xn = mp.norm(mp.matrix([abs(z) for m in range(K + 1) for z in A[m]]))
        if nf < mp.mpf(10) ** (-(DPS - 10)) * max(1, xn): break
        dx = lstsq_step(periodic_jacobian(sysd, A, om, K), F)
        A = [[A[0][j] + dx[j] for j in range(n)]] + \
            [[A[m][j] + dx[n + (m - 1) * n + j] + 1j * dx[n + n * K + (m - 1) * n + j] for j in range(n)] for m in range(1, K + 1)]
        om = om + dx[n * (2 * K + 1)]
    F = _flat(periodic_residual(sysd, A, om, K), A, K, n)
    return A, om, mp.norm(F), hist

def linear_spectrum(sysd):
    E = mp.eig(mp.inverse(sysd['Ms']) * sysd['L'], left=False, right=False)
    return sorted(E, key=lambda z: (mp.re(z), mp.im(z)))

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    seedf = os.path.join(here, 'leray_dss_galerkin_seeds.json')
    outf = os.path.join(here, 'leray-dss-galerkin-search.witness.json')
    seeds = json.load(open(seedf))
    only = os.environ.get('LERAY_CASES')  # e.g. "2,2;2,3"
    if only:
        keep = {tuple(map(int, t.split(','))) for t in only.split(';')}
        seeds['cases'] = [c for c in seeds['cases'] if (c['L'], c['N']) in keep]
        outf = outf.replace('.witness.json', '-' + only.replace(';', '_').replace(',', '') + '.witness.json')
    out = dict(description=__doc__.strip().splitlines()[0], dps=DPS, alpha_test=str(ALPHA),
               trial_tail='(1+rho)^-p, n=0 member ~ |y|^-1 (weak-L3)', results=[])
    log = lambda *x: print(*x, flush=True)
    for case in seeds['cases']:
        L, N = case['L'], case['N']
        log(f"== L={L} N={N}")
        res = dict(L=L, N=N)
        sysd = build_system(L, N, m_rad=case.get('m_rad', 40), log=log)
        spec = linear_spectrum(sysd)
        res['linear_spectrum_lowest'] = [mp.nstr(z, 20) for z in spec[:8]]
        res['linear_spectrum_min_re'] = mp.nstr(min(mp.re(z) for z in spec), 30)
        res['linear_spectrum_max_abs_im'] = mp.nstr(max(abs(mp.im(z)) for z in spec), 5)
        log("  linear spectrum (lowest):", [mp.nstr(z, 8) for z in spec[:6]])
        if case.get('quad_check'):
            sys2 = build_system(L, N, m_rad=case['quad_check'], log=log)
            dM = max(abs(sysd['L'][i, j] - sys2['L'][i, j]) for i in range(sysd['n']) for j in range(sysd['n']))
            dB = max(abs(sysd['B'].get(k, 0) - sys2['B'].get(k, 0)) for k in set(sysd['B']) | set(sys2['B']))
            res['quadrature_change_on_doubling'] = dict(L_maxabs=mp.nstr(dM, 5), B_maxabs=mp.nstr(dB, 5),
                                                        m_rad=[case.get('m_rad', 40), case['quad_check']])
            log("  quadrature check:", res['quadrature_change_on_doubling'])
        res['candidates'] = []
        idx = {tuple(l): i for i, l in enumerate(sysd['labels'])}
        for cand in case.get('steady_seeds', []):
            a0 = mp.matrix(sysd['n'], 1)
            for lab, v in zip(cand['labels'], cand['a']):
                a0[idx[tuple(lab)]] = mp.mpf(v)
            r0 = mp.norm(residual(sysd, a0))
            a, rf, hist = newton(sysd, a0, log=log)
            rec = dict(source=cand.get('source'), seed_residual=mp.nstr(r0, 5), final_residual=mp.nstr(rf, 5),
                       coeff_norm=mp.nstr(mp.norm(a), 20), newton_history=[mp.nstr(h, 3) for h in hist],
                       relative_residual=mp.nstr(rf / mp.norm(a), 5),
                       nontrivial=bool(mp.norm(a) > 1), a=[mp.nstr(x, 50) for x in a])
            log(f"  seed {cand.get('source')}: |F(seed)|={mp.nstr(r0,4)} -> |F|={mp.nstr(rf,4)}  |a|={mp.nstr(mp.norm(a),12)}")
            res['candidates'].append(rec)
        res['periodic_candidates'] = []
        for cand in case.get('periodic_seeds', []):
            K = cand['K']; n = sysd['n']
            x = [mp.mpf(v) for v in cand['x']]
            perm = [idx[tuple(l)] for l in cand['labels']]
            A = [[mp.mpc(0)] * n for _ in range(K + 1)]
            for jj, j in enumerate(perm):
                A[0][j] = mp.mpc(x[jj])
                for m in range(1, K + 1):
                    A[m][j] = mp.mpc(x[n + (m - 1) * n + jj], x[n + n * K + (m - 1) * n + jj])
            om = x[-1]
            A, om, rf, hist = periodic_newton(sysd, A, om, K, log=log)
            nrm = [mp.sqrt(mp.fsum(abs(z) ** 2 for z in A[m])) for m in range(K + 1)]
            rec = dict(source=cand.get('source'), K=K, final_residual=mp.nstr(rf, 5),
                       period_S=mp.nstr(2 * mp.pi / om, 40), scale_lambda=mp.nstr(mp.exp(mp.pi / om), 30),
                       mode_norms=[mp.nstr(v, 12) for v in nrm], newton_history=[mp.nstr(h, 3) for h in hist])
            log(f"  periodic seed {cand.get('source')}: |F|={mp.nstr(rf,4)} S={mp.nstr(2*mp.pi/om,20)}")
            res['periodic_candidates'].append(rec)
        out['results'].append(res)
        json.dump(out, open(outf, 'w'), indent=1)
    log("WROTE", outf)

if __name__ == '__main__':
    main()
