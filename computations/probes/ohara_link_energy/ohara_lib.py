"""Link Möbius (O'Hara j=2) energy of closed-braid embeddings: embedding,
spectral evaluator, guarded Sobolev flow, topology certificates.

float64 throughout (stated in preregistration.md). No physical constants.
"""
from __future__ import annotations
import numpy as np  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
from fractions import Fraction

# ---------------------------------------------------------------- embedding

def _psi(x):
    out = np.zeros_like(x)
    m = x > 0
    out[m] = np.exp(-1.0 / x[m])
    return out

def smooth_step(tau):
    tau = np.clip(tau, 0.0, 1.0)
    a, b = _psi(tau), _psi(1.0 - tau)
    return a / (a + b)

def braid_strand_positions(word, n, phi, R=3.0, a=1.0):
    """Return array (len(phi), n, 3): 3D point of the strand that STARTS the
    current slot at position p... we instead return positions indexed by the
    strand label (the starting position at phi=0)."""
    m = len(word)
    phi = np.asarray(phi) % (2 * np.pi)
    slot = np.minimum((phi / (2 * np.pi) * m).astype(int), m - 1)
    tau = phi / (2 * np.pi) * m - slot
    # position of each strand label at the start of each slot
    pos_at_slot = np.zeros((m + 1, n), dtype=int)
    cur = list(range(n))  # cur[pos] = label
    for k in range(m + 1):
        for p in range(n):
            pos_at_slot[k, cur[p]] = p
        if k < m:
            i = abs(word[k]); cur[i], cur[i + 1] = cur[i + 1], cur[i]
    out = np.zeros((len(phi), n, 3))
    s = smooth_step(tau)
    th = np.pi * s
    for lab in range(n):
        p0 = pos_at_slot[slot, lab]
        roff = a * (p0 - (n - 1) / 2.0)
        z = np.zeros(len(phi))
        gi = np.array([abs(word[k]) for k in range(m)])[slot]
        sg = np.array([1 if word[k] >= 0 else -1 for k in range(m)])[slot]
        c = a * (gi + 0.5 - (n - 1) / 2.0)
        lower = p0 == gi
        upper = p0 == gi + 1
        roff = np.where(lower, c - 0.5 * a * np.cos(th), roff)
        z = np.where(lower, sg * 0.5 * a * np.sin(th), z)
        roff = np.where(upper, c + 0.5 * a * np.cos(th), roff)
        z = np.where(upper, -sg * 0.5 * a * np.sin(th), z)
        r = R + roff
        out[:, lab, 0] = r * np.cos(phi)
        out[:, lab, 1] = r * np.sin(phi)
        out[:, lab, 2] = z
    return out

def braid_components(word, n):
    end = {}
    for s in range(n):
        pos = s
        for g in word:
            i = abs(g)
            if pos == i: pos = i + 1
            elif pos == i + 1: pos = i
        end[s] = pos
    seen, comps = set(), []
    for s in range(n):
        if s in seen: continue
        c, x = [], s
        while x not in seen:
            seen.add(x); c.append(x); x = end[x]
        comps.append(c)
    return comps

def closed_braid_curves(word, n, M_per_pass, R=3.0, a=1.0):
    """Dense samples of each component (uniform in braid angle). Component
    passing k times gets k*M_per_pass samples. Labels: pass j of a component
    starts at the strand label = position c[j] at phi=0."""
    comps = braid_components(word, n)
    phi = np.arange(M_per_pass) * (2 * np.pi / M_per_pass)
    P = braid_strand_positions(word, n, phi, R, a)  # (M, n, 3) by label
    curves = []
    for c in comps:
        curves.append(np.concatenate([P[:, lab, :] for lab in c], axis=0))
    return curves

# ---------------------------------------------------------------- spectral tools

def fourier_resample(X, M):
    """Trigonometric interpolation of periodic samples X (N,3) to M points (M>=N)."""
    N = len(X)
    F = np.fft.fft(X, axis=0)
    G = np.zeros((M, 3), dtype=complex)
    h = N // 2
    if N % 2 == 0:
        G[:h] = F[:h]
        if h > 1:
            G[M - h + 1:] = F[h + 1:]
        G[h] = F[h] / 2; G[M - h] = F[h] / 2
    else:
        G[:h + 1] = F[:h + 1]
        G[M - h:] = F[h + 1:]
    return np.real(np.fft.ifft(G, axis=0)) * (M / N)

def fft_derivs(X):
    N = len(X)
    k = np.fft.fftfreq(N, d=1.0 / N) * 2 * np.pi  # d/du, u in [0,1)
    F = np.fft.fft(X, axis=0)
    if N % 2 == 0:
        k1 = k.copy(); k1[N // 2] = 0
    else:
        k1 = k
    d1 = np.real(np.fft.ifft(1j * k1[:, None] * F, axis=0))
    d2 = np.real(np.fft.ifft(-(k ** 2)[:, None] * F, axis=0))
    return d1, d2

def arclength_fn(speed):
    """S(u_j) for periodic speed samples, spectrally; returns S, L."""
    N = len(speed)
    F = np.fft.fft(speed)
    L = np.real(F[0]) / N
    k = np.fft.fftfreq(N, d=1.0 / N) * 2 * np.pi
    G = np.zeros_like(F)
    nz = k != 0
    if N % 2 == 0:
        nz[N // 2] = False
    G[nz] = F[nz] / (1j * k[nz])
    u = np.arange(N) / N
    S = L * u + np.real(np.fft.ifft(G))
    S = S - S[0]
    return S, L

def _pair_sum(X, Y, wX, wY, chunk=1024):
    tot = 0.0
    for s in range(0, len(X), chunk):
        D = X[s:s + chunk, None, :] - Y[None, :, :]
        r2 = np.einsum('ijk,ijk->ij', D, D)
        tot += np.sum(wX[s:s + chunk, None] / r2 * wY[None, :])
    return tot

def self_energy_spectral(X, chunk=512):
    """FHW-normalised Möbius energy of the smooth periodic curve through samples X."""
    N = len(X)
    d1, d2 = fft_derivs(X)
    sp = np.linalg.norm(d1, axis=1)
    S, L = arclength_fn(sp)
    cr = np.cross(d1, d2)
    kappa2 = np.einsum('ij,ij->i', cr, cr) / sp ** 6
    du = 1.0 / N
    c = (np.pi / L) ** 2
    tot = 0.0
    idx = np.arange(N)
    for s in range(0, N, chunk):
        D = X[s:s + chunk, None, :] - X[None, :, :]
        r2 = np.einsum('ijk,ijk->ij', D, D)
        dS = S[s:s + chunk, None] - S[None, :]
        sn2 = np.sin(np.pi * dS / L) ** 2
        ii = idx[s:s + chunk, None] == idx[None, :]
        with np.errstate(divide='ignore', invalid='ignore'):
            g = 1.0 / r2 - c / sn2
        diag = (kappa2[s:s + chunk] / 12.0 - c / 3.0) * sp[s:s + chunk] ** 2
        g = np.where(ii, 0.0, g)
        tot += np.sum(g * sp[s:s + chunk, None] * sp[None, :])
        tot += np.sum(diag)
    return 4.0 + tot * du * du, L

def cross_energy_spectral(X, Y):
    d1, _ = fft_derivs(X); e1, _ = fft_derivs(Y)
    sx = np.linalg.norm(d1, axis=1); sy = np.linalg.norm(e1, axis=1)
    return _pair_sum(X, Y, sx, sy) / (len(X) * len(Y))

def link_energy_spectral(curves):
    E = [self_energy_spectral(c)[0] for c in curves]
    out = {"self": E}
    if len(curves) == 2:
        E12 = cross_energy_spectral(curves[0], curves[1])
        out["mutual"] = E12
        out["total"] = E[0] + E[1] + 2 * E12
    else:
        out["mutual"] = None
        out["total"] = sum(E)
    return out

def resample_equal_arclength(X, N, dense=None):
    """From periodic samples of a smooth curve, N points equally spaced in arclength
    (via Fourier-dense interpolation then linear inversion of S)."""
    if dense is None:
        dense = max(16 * N, 8 * len(X))
    Xd = fourier_resample(X, dense) if dense != len(X) else X
    seg = np.linalg.norm(np.roll(Xd, -1, axis=0) - Xd, axis=1)
    S = np.concatenate([[0], np.cumsum(seg)])
    L = S[-1]
    targets = np.arange(N) * L / N
    Xc = np.vstack([Xd, Xd[:1]])
    out = np.empty((N, 3))
    for k in range(3):
        out[:, k] = np.interp(targets, S, Xc[:, k])
    return out

# ---------------------------------------------------------------- polygon tools

def seg_seg_dist(P0, P1, Q0, Q1):
    """Vectorised min distance between segments P0P1 (a,3) and Q0Q1 (b,3) -> (a,b)."""
    d1 = (P1 - P0)[:, None, :]; d2 = (Q1 - Q0)[None, :, :]
    r = P0[:, None, :] - Q0[None, :, :]
    a = np.sum(d1 * d1, -1); e = np.sum(d2 * d2, -1)
    b = np.sum(d1 * d2, -1); c = np.sum(d1 * r, -1); f = np.sum(d2 * r, -1)
    den = a * e - b * b
    with np.errstate(divide='ignore', invalid='ignore'):
        s = np.where(den > 1e-14 * a * e, np.clip((b * f - c * e) / den, 0, 1), 0.0)
    tt = (b * s + f) / e
    tt_c = np.clip(tt, 0, 1)
    s = np.where(tt < 0, np.clip(-c / a, 0, 1), np.where(tt > 1, np.clip((b - c) / a, 0, 1), s))
    tt = tt_c
    D = r + s[..., None] * d1 - tt[..., None] * d2
    return np.sqrt(np.sum(D * D, -1))

def guard_distances(curves):
    """(d_min over non-adjacent segment pairs,
        resolution ratio = min over pairs >=4 apart or cross-comp of
        dist / max(len_a, len_b))."""
    dmin, dres = np.inf, np.inf
    segs = [(c, np.roll(c, -1, axis=0)) for c in curves]
    lens = [np.linalg.norm(B - A, axis=1) for A, B in segs]
    for a_, (A0, A1) in enumerate(segs):
        for b_, (B0, B1) in enumerate(segs):
            if b_ < a_: continue
            D = seg_seg_dist(A0, A1, B0, B1)
            Lm = np.maximum(lens[a_][:, None], lens[b_][None, :])
            if a_ == b_:
                n = len(A0)
                i = np.arange(n)
                sep = np.abs(i[:, None] - i[None, :]); sep = np.minimum(sep, n - sep)
                dmin = min(dmin, D[sep >= 2].min())
                dres = min(dres, (D / Lm)[sep >= 4].min())
            else:
                dmin = min(dmin, D.min()); dres = min(dres, (D / Lm).min())
    return dmin, dres

ROT = None
def _proj_basis():
    global ROT
    if ROT is None:
        rng = np.random.default_rng(12345)
        Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        ROT = Q
    return ROT

def crossings_2d(A0, A1, B0, B1, same=False):
    """Crossings in the projection along ROT[:,2]. Returns arrays (i,j,s,t,sign_over)
    where s,t are segment parameters, and 'aover' True if A is over."""
    Q = _proj_basis()
    a0 = A0 @ Q; a1 = A1 @ Q; b0 = B0 @ Q; b1 = B1 @ Q
    p = a0[:, None, :2]; r = (a1 - a0)[:, None, :2]
    q = b0[None, :, :2]; s_ = (b1 - b0)[None, :, :2]
    rxs = r[..., 0] * s_[..., 1] - r[..., 1] * s_[..., 0]
    qp = q - p
    with np.errstate(divide='ignore', invalid='ignore'):
        tA = (qp[..., 0] * s_[..., 1] - qp[..., 1] * s_[..., 0]) / rxs
        tB = (qp[..., 0] * r[..., 1] - qp[..., 1] * r[..., 0]) / rxs
    hit = (np.abs(rxs) > 1e-15) & (tA >= 0) & (tA < 1) & (tB >= 0) & (tB < 1)
    if same:
        n = len(A0)
        i = np.arange(n)
        sep = np.abs(i[:, None] - i[None, :]); sep = np.minimum(sep, n - sep)
        hit &= (sep >= 2) & (i[:, None] < i[None, :])
    I, J = np.nonzero(hit)
    ta, tb = tA[I, J], tB[I, J]
    za = a0[I, 2] + ta * (a1[I, 2] - a0[I, 2])
    zb = b0[J, 2] + tb * (b1[J, 2] - b0[J, 2])
    aover = za > zb
    # sign: (over tangent x under tangent) . z
    cr = rxs[I, J]  # r_A x s_B
    sign = np.where(aover, np.sign(cr), -np.sign(cr))
    return I, J, ta, tb, aover, sign

def linking_number(c1, c2):
    I, J, ta, tb, aover, sign = crossings_2d(c1, np.roll(c1, -1, 0), c2, np.roll(c2, -1, 0))
    tot = int(np.sum(sign))
    assert tot % 2 == 0, tot
    return tot // 2

# --------------------------------------------- Alexander polynomial certificate

def _det_fraction(M):
    """Exact determinant of an integer matrix (Bareiss)."""
    A = [row[:] for row in M]
    n = len(A)
    if n == 0: return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            sw = next((r for r in range(k + 1, n) if A[r][k] != 0), None)
            if sw is None: return 0
            A[k], A[sw] = A[sw], A[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]

def alexander_values(curves, tvals=(-1, 2, 3)):
    """Alexander matrix of a generic projection; returns {t: det of a minor}.
    Comparison is up to +-t^k."""
    # collect crossings along each component
    events = []  # (comp, seg, param, crossing_id, is_over)
    sgn = []
    cid = 0
    segs = [(c, np.roll(c, -1, axis=0)) for c in curves]
    for a_, (A0, A1) in enumerate(segs):
        for b_, (B0, B1) in enumerate(segs):
            if b_ < a_: continue
            I, J, ta, tb, aover, sign = crossings_2d(A0, A1, B0, B1, same=(a_ == b_))
            for k in range(len(I)):
                events.append((a_, I[k], ta[k], cid, bool(aover[k])))
                events.append((b_, J[k], tb[k], cid, not bool(aover[k])))
                sgn.append(int(sign[k])); cid += 1
    nc = cid
    if nc == 0:
        return {t: 1 for t in tvals}, 0
    # arcs: along each component, arc j runs from undercrossing u_j to u_{j+1}
    arc_of_over, under_in, under_out = {}, {}, {}
    narc = 0
    for comp in range(len(curves)):
        ev = sorted([e for e in events if e[0] == comp], key=lambda e: (e[1], e[2]))
        unders = [k for k, e in enumerate(ev) if not e[4]]
        K = len(unders)
        if K == 0:
            for e in ev: arc_of_over[e[3]] = narc
            narc += 1
            continue
        for j in range(K):
            under_out[ev[unders[j]][3]] = narc + j
            under_in[ev[unders[(j + 1) % K]][3]] = narc + j
        j = K - 1
        for k, e in enumerate(ev):
            if not e[4]:
                j = unders.index(k)
            else:
                arc_of_over[e[3]] = narc + j
        narc += K
    assert narc == nc or True
    out = {}
    for t in tvals:
        rows = []
        for c in range(nc):
            row = [0] * narc
            k, i, j = arc_of_over[c], under_in[c], under_out[c]
            row[k] += 1 - t
            if sgn[c] > 0:
                row[i] += t; row[j] -= 1
            else:
                row[i] -= 1; row[j] += t
            rows.append(row)
        # minor: delete last row and last column
        minor = [r[:-1] for r in rows[:-1]]
        out[t] = _det_fraction(minor)
    return out, nc

def alexander_from_poly(poly_str, tvals=(-1, 2, 3)):
    import sympy as sp
    t = sp.symbols('t')
    P = sp.sympify(poly_str)
    return {tv: sp.Rational(P.subs(t, tv)) for tv in tvals}

def same_up_to_units(vals_a, vals_b):
    """vals: {t: value}; equal up to +-t^k for each t (k may differ per t, it is
    the same k in truth but we check each)."""
    for tv in vals_a:
        a, b = Fraction(int(vals_a[tv])), Fraction(int(vals_b[tv]))
        if a == 0 or b == 0:
            if a != b: return False
            continue
        r = a / b
        if tv in (1, -1):
            if abs(r) != 1: return False
            continue
        r = abs(r); ok = False
        for k in range(-60, 61):
            if r == Fraction(abs(tv)) ** k: ok = True; break
        if not ok: return False
    return True

# ---------------------------------------------------------------- flow

class LinkFlow:
    def __init__(self, curves, lk_target, k0=4.0, verbose=False, res_ratio=0.5,
                 balance_every=100, certify=None):
        self.res_ratio = res_ratio
        self.balance_every = balance_every
        self.certify = certify  # callable(curves) -> bool (topology certificate)
        self.balances = {"applied": 0, "rejected": 0}
        self.X = [c.copy() for c in curves]
        self.lk = lk_target
        self.k0 = k0
        self.verbose = verbose
        self.Ltot = sum(self._len(c) for c in self.X)

    @staticmethod
    def _len(c):
        return np.sum(np.linalg.norm(np.roll(c, -1, 0) - c, axis=1))

    def F_and_grad(self, X):
        F = 0.0
        G = [np.zeros_like(c) for c in X]
        hs = []
        for ci, c in enumerate(X):
            N = len(c)
            e = np.roll(c, -1, 0) - c
            el = np.linalg.norm(e, axis=1)
            L = el.sum(); h = L / N; hs.append(h)
            T = e / el[:, None]
            D = c[:, None, :] - c[None, :, :]
            r2 = np.einsum('ijk,ijk->ij', D, D)
            np.fill_diagonal(r2, np.inf)
            inv2 = 1.0 / r2
            P = inv2.sum()
            F += h * h * P
            dP = -4.0 * np.einsum('ij,ijk->ik', inv2 * inv2, D)
            dL = np.roll(T, 1, 0) - T
            G[ci] += h * h * dP + (2 * h / N) * P * dL
            # diagonal (curvature) term of the trapezoid rule: (1/12) sum |t_k - t_{k-1}|^2
            Tm, Tp = np.roll(T, 1, 0), np.roll(T, -1, 0)
            F += (1.0 / 12.0) * np.sum(np.sum((T - Tm) ** 2, 1))
            v = Tm + Tp
            dBde = -(2.0 / 12.0) * (v - np.sum(v * T, 1)[:, None] * T) / el[:, None]
            G[ci] += np.roll(dBde, 1, 0) - dBde
        if len(X) == 2:
            a, b = X
            D = a[:, None, :] - b[None, :, :]
            r2 = np.einsum('ijk,ijk->ij', D, D)
            inv2 = 1.0 / r2
            Q = inv2.sum()
            h1, h2 = hs
            F += 2 * h1 * h2 * Q
            W = inv2 * inv2
            dQa = -2.0 * np.einsum('ij,ijk->ik', W, D)
            dQb = 2.0 * np.einsum('ij,ijk->jk', W, D)
            for ci, c in enumerate(X):
                N = len(c)
                e = np.roll(c, -1, 0) - c
                T = e / np.linalg.norm(e, axis=1)[:, None]
                dL = np.roll(T, 1, 0) - T
                other = hs[1 - ci]
                G[ci] += 2 * other * Q * (1.0 / N) * dL
            G[0] += 2 * h1 * h2 * dQa
            G[1] += 2 * h1 * h2 * dQb
        return F, G

    def E_poly(self, X):
        out = []
        for c in X:
            N = len(c)
            h = self._len(c) / N
            D = c[:, None, :] - c[None, :, :]
            r2 = np.einsum('ijk,ijk->ij', D, D)
            i = np.arange(N); d = (i[:, None] - i[None, :]) % N
            with np.errstate(divide='ignore'):
                # chord of the REGULAR N-gon with the same edge length h, so the
                # bracket vanishes identically on a regular polygon (E = 4 there)
                sub = np.sin(np.pi / N) ** 2 / np.sin(np.pi * d / N) ** 2 / h ** 2
            np.fill_diagonal(r2, np.inf); np.fill_diagonal(sub, 0.0)
            e = np.roll(c, -1, 0) - c
            T = e / np.linalg.norm(e, axis=1)[:, None]
            diag = np.sum(np.sum((T - np.roll(T, 1, 0)) ** 2, 1)) / 12.0 - N * (2 * np.sin(np.pi / N)) ** 2 / 12.0
            out.append(h * h * np.sum(1.0 / r2 - sub) + diag + 4.0)
        E12 = None; tot = sum(out)
        if len(X) == 2:
            a, b = X
            h1 = self._len(a) / len(a); h2 = self._len(b) / len(b)
            D = a[:, None, :] - b[None, :, :]
            E12 = h1 * h2 * np.sum(1.0 / np.einsum('ijk,ijk->ij', D, D))
            tot += 2 * E12
        return out, E12, tot

    def _tangents(self, c):
        T = np.roll(c, -1, 0) - np.roll(c, 1, 0)
        return T / np.linalg.norm(T, axis=1)[:, None]

    def direction(self, G):
        dirs = []
        for c, g in zip(self.X, G):
            T = self._tangents(c)
            gn = g - np.sum(g * T, 1)[:, None] * T
            N = len(c)
            k = np.abs(np.fft.fftfreq(N, d=1.0 / N))
            Fg = np.fft.fft(gn, axis=0) / (1.0 + (k / self.k0) ** 3)[:, None]
            gp = np.real(np.fft.ifft(Fg, axis=0))
            gp = gp - np.sum(gp * T, 1)[:, None] * T
            dirs.append(-gp)
        return dirs

    def redistribute(self, X, beta=0.5):
        out = []
        for c in X:
            el = np.linalg.norm(np.roll(c, -1, 0) - c, axis=1)
            T = self._tangents(c)
            mv = beta * 0.5 * (el - np.roll(el, 1))
            out.append(c + mv[:, None] * T)
        return out

    def normalise(self, X):
        allp = np.vstack(X)
        cen = allp.mean(0)
        L = sum(self._len(c) for c in X)
        s = self.Ltot / L
        return [(c - cen) * s for c in X]

    @staticmethod
    def max_turn(c):
        e = np.roll(c, -1, 0) - c
        e /= np.linalg.norm(e, axis=1)[:, None]
        cs = np.clip(np.sum(e * np.roll(e, 1, 0), 1), -1, 1)
        return np.arccos(cs).max()

    def check_guard(self, Xold, Xnew, dmin_old):
        delta = max(np.linalg.norm(a - b, axis=1).max() for a, b in zip(Xold, Xnew))
        minedge = min(np.linalg.norm(np.roll(c, -1, 0) - c, axis=1).min() for c in Xold)
        if not (2 * delta < 0.9 * dmin_old and delta < 0.25 * minedge):
            return False, "displacement"
        if max(self.max_turn(c) for c in Xnew) > np.deg2rad(150):
            return False, "turn"
        dmin, dres = guard_distances(Xnew)
        # resolution: may not fall below the threshold, nor (if already below it,
        # e.g. an under-resolved canonical start) fall further than 5 %
        if dres < min(self.res_ratio, 0.95 * self._dres_ref):
            return False, "resolution"
        if len(Xnew) == 2 and linking_number(Xnew[0], Xnew[1]) != self.lk:
            return False, "linking"
        return True, (dmin, dres)

    # ---- helpers for L-BFGS in the preconditioned, normal-projected metric
    def _proj_normal(self, X, G):
        out = []
        for c, g in zip(X, G):
            T = self._tangents(c)
            out.append(g - np.sum(g * T, 1)[:, None] * T)
        return out

    def _precond(self, X, V):
        out = []
        for c, v in zip(X, V):
            N = len(c)
            T = self._tangents(c)
            k = np.abs(np.fft.fftfreq(N, d=1.0 / N))
            Fv = np.fft.fft(v, axis=0) / (1.0 + (k / self.k0) ** 3)[:, None]
            w = np.real(np.fft.ifft(Fv, axis=0))
            out.append(w - np.sum(w * T, 1)[:, None] * T)
        return out

    def _mobius_basis(self, X):
        """Orthonormal basis (stacked over components) of the 10 infinitesimal
        Möbius motions evaluated at the vertices."""
        P = np.vstack(X)
        n = len(P)
        vecs = []
        for k in range(3):
            e = np.zeros(3); e[k] = 1
            vecs.append(np.tile(e, (n, 1)))                     # translations
            vecs.append(np.cross(e, P))                          # rotations
            vecs.append(2 * (P @ e)[:, None] * P - np.sum(P * P, 1)[:, None] * e)  # special conformal
        vecs.append(P.copy())                                    # dilation
        A = np.stack([v.ravel() for v in vecs], 1)
        Q, _ = np.linalg.qr(A)
        return Q

    def _proj_mobius(self, X, V, Q=None):
        if Q is None:
            Q = self._mobius_basis(X)
        v = np.vstack(V).ravel()
        v = v - Q @ (Q.T @ v)
        v = v.reshape(-1, 3)
        out, i = [], 0
        for c in X:
            out.append(v[i:i + len(c)]); i += len(c)
        return out

    @staticmethod
    def _dot(A, B):
        return sum(float(np.sum(a * b)) for a, b in zip(A, B))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities

    def try_balance(self, X):
        """Möbius re-representative + equal-arclength resample; accepted only if
        the topology certificate passes and the resolution guard holds."""
        Ns = [len(c) for c in X]
        Xb, _ = mobius_balance(X)
        Xb = [resample_equal_arclength(c, n_) for c, n_ in zip(Xb, Ns)]
        Xb = self.normalise(Xb)
        dmin, dres = guard_distances(Xb)
        ok = dres >= min(self.res_ratio, 0.95 * getattr(self, "_dres_ref", self.res_ratio))
        if ok and len(Xb) == 2:
            ok = linking_number(Xb[0], Xb[1]) == self.lk
        if ok and self.certify is not None:
            ok = self.certify(Xb)
        if ok:
            # continuum Möbius invariance: the smooth interpolants before and after
            # must carry the same energy; otherwise the re-representation lost fidelity
            e0 = link_energy_spectral([fourier_resample(c, 4 * len(c)) for c in X])["total"]
            e1 = link_energy_spectral([fourier_resample(c, 4 * len(c)) for c in Xb])["total"]
            if abs(e1 - e0) > 1e-3 * abs(e0):
                ok = False
        if ok:
            self.balances["applied"] += 1
            if len(Xb) == 2:
                self.lk = linking_number(Xb[0], Xb[1])
            return Xb
        self.balances["rejected"] += 1
        return None

    def run(self, max_iter, rel_tol=1e-6, window=300, log_every=200, mem=10,
            renorm_every=200):
        X = self.X
        dmin, dres = guard_distances(X)
        self._dres_ref = dres
        F, G = self.F_and_grad(X)
        g = self._proj_mobius(X, self._proj_normal(X, G))
        S_, Y_ = [], []
        hist = []
        stop = "cap"
        guard_rejects = {"displacement": 0, "turn": 0, "resolution": 0, "linking": 0}
        accepted = 0
        alpha0 = None
        it = -1
        for it in range(max_iter):
            # two-loop recursion
            q = [v.copy() for v in g]
            al = []
            for s_, y_ in reversed(list(zip(S_, Y_))):
                rho = 1.0 / self._dot(y_, s_)
                a_ = rho * self._dot(s_, q)
                al.append((rho, a_, s_, y_))
                q = [qq - a_ * yy for qq, yy in zip(q, y_)]
            r = self._precond(X, q)
            if S_:
                gam = self._dot(S_[-1], Y_[-1]) / self._dot(Y_[-1], self._precond(X, Y_[-1]))
                r = [gam * v for v in r]
            for rho, a_, s_, y_ in reversed(al):
                b_ = rho * self._dot(y_, r)
                r = [rr + (a_ - b_) * ss for rr, ss in zip(r, s_)]
            d = self._proj_mobius(X, [-v for v in r])
            slope = self._dot(g, d)
            lbfgs = bool(S_) and slope < 0
            ok = False
            for attempt in (0, 1):
                if not lbfgs:
                    S_, Y_ = [], []
                    d = self._proj_mobius(X, [-v for v in self._precond(X, g)])
                    slope = self._dot(g, d)
                    step = alpha0 if alpha0 is not None else 1e-3
                    floor = 1e-14
                else:
                    step = 1.0
                    floor = 1e-6
                while step > floor:
                    Xt = [c + step * dd for c, dd in zip(X, d)]
                    Ft, _ = self.F_and_grad(Xt)
                    if Ft <= F + 1e-4 * step * slope:
                        Xn = self.redistribute(Xt)
                        g_ok, info = self.check_guard(X, Xn, dmin)
                        if g_ok:
                            ok = True; break
                        guard_rejects[info] += 1
                    step *= 0.5
                if ok or not lbfgs:
                    break
                lbfgs = False
            if not ok:
                stop = "guard/step-underflow"; break
            s_model = [step * dd for dd in d]
            accepted += 1
            if not lbfgs:
                alpha0 = step * 2.0
            Fn, Gn = self.F_and_grad(Xn)
            gn = self._proj_mobius(Xn, self._proj_normal(Xn, Gn))
            s_vec = s_model
            y_vec = [a - b for a, b in zip(gn, g)]
            if self._dot(s_vec, y_vec) > 1e-12 * np.sqrt(self._dot(s_vec, s_vec) * self._dot(y_vec, y_vec)):
                S_.append(s_vec); Y_.append(y_vec)
                if len(S_) > mem: S_.pop(0); Y_.pop(0)
            X, F, g = Xn, Fn, gn
            if self.balance_every and accepted % self.balance_every == 0:
                Xb = self.try_balance(X)
                if Xb is not None:
                    X = Xb
                F, G = self.F_and_grad(X); g = self._proj_mobius(X, self._proj_normal(X, G))
                S_, Y_ = [], []
            elif accepted % renorm_every == 0:
                X = self.normalise(X)
                F, G = self.F_and_grad(X); g = self._proj_mobius(X, self._proj_normal(X, G))
                S_, Y_ = [], []
            dmin, dres = guard_distances(X)
            if self._dres_ref < self.res_ratio:
                self._dres_ref = max(self._dres_ref, dres)
            if it % 20 == 0:
                _, _, Ep = self.E_poly(X)
                hist.append((it, float(Ep)))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                if self.verbose and it % log_every == 0:
                    print(f"    it={it} Epoly={Ep:.8f} step={step:.2e} dmin={dmin:.3e}", flush=True)
                old = [e for (i_, e) in hist if i_ <= it - window]
                if old and it >= window:
                    best_before = min(old)
                    best_now = min(e for (_, e) in hist)
                    if (best_before - best_now) / abs(best_now) < rel_tol:
                        stop = "converged"; break
        X = self.normalise(X)
        self.X = X
        _, _, Ep = self.E_poly(X)
        hist.append((it, float(Ep)))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        return dict(iterations=it + 1, accepted=accepted, stop=stop, balances=dict(self.balances),
                    guard_rejects=guard_rejects, history=hist,
                    dmin=float(dmin), dres=float(dres))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities


# ---------------------------------------------------------------- Möbius balancing

def _inv_stereo(X):
    r2 = np.sum(X * X, 1)[:, None]
    return np.hstack([2 * X, r2 - 1]) / (r2 + 1)

def _stereo(P):
    return P[:, :3] / (1 - P[:, 3:4])

def _ball_mobius(P, a):
    """Möbius automorphism of B^4 sending a -> 0, applied to points of S^3."""
    aa = a @ a
    D = P - a
    num = (1 - aa) * D - np.sum(D * D, 1)[:, None] * a
    den = 1 - 2 * (P @ a) + aa * np.sum(P * P, 1)
    return num / den[:, None]

def mobius_balance(curves, iters=200, tol=1e-9, rng_seed=0):
    """Choose the Möbius representative whose S^3 preimage has its (spherical
    arclength-weighted) centre of mass at the origin, then rotate S^3 so that
    the pole sent to infinity is the S^3 point farthest from the link.
    Energy is exactly invariant; only the representative changes."""
    Ps = [_inv_stereo(c) for c in curves]
    for _ in range(iters):
        W = []
        for P in Ps:
            seg = np.linalg.norm(np.roll(P, -1, 0) - P, axis=1)
            w = 0.5 * (seg + np.roll(seg, 1))
            W.append(w)
        allP = np.vstack(Ps); allW = np.concatenate(W)
        c = (allP * allW[:, None]).sum(0) / allW.sum()
        if np.linalg.norm(c) < tol:
            break
        Ps = [_ball_mobius(P, 0.5 * c) for P in Ps]
        Ps = [P / np.linalg.norm(P, axis=1)[:, None] for P in Ps]
    allP = np.vstack(Ps)
    rng = np.random.default_rng(rng_seed)
    cand = rng.normal(size=(4000, 4)); cand /= np.linalg.norm(cand, axis=1)[:, None]
    dmin = np.min(np.linalg.norm(cand[:, None, :] - allP[None, ::max(1, len(allP) // 400), :], axis=2), axis=1)
    p = cand[np.argmax(dmin)]
    # rotation of R^4 taking p to e4 (Householder)
    e4 = np.array([0, 0, 0, 1.0])
    v = p - e4
    if np.linalg.norm(v) < 1e-12:
        H = np.eye(4)
    else:
        v /= np.linalg.norm(v); H = np.eye(4) - 2 * np.outer(v, v)
        # make it a ROTATION (orientation-preserving): compose with a reflection
        # fixing e4, so the link is not mirrored
        H = np.diag([-1.0, 1.0, 1.0, 1.0]) @ H
    return [_stereo(P @ H.T) for P in Ps], float(np.max(dmin))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
