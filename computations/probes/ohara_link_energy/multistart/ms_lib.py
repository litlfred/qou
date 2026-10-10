"""Multi-start helpers. REUSES ohara_lib unchanged (energy, flow, guard,
certificates). Only start generation and the shape invariant are new.
"""
import sys, json, itertools
import numpy as np  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
sys.path.insert(0, "..")
import ohara_lib as L
import ms_words as W

# ------------------------------------------------------------ start generation
def braid_curves_var(word, n, M, R=3.0, a=1.0, zamp=1.0, warp=None):
    """Canonical closed-braid embedding (ohara_lib.braid_strand_positions, unchanged)
    with two extra start parameters:
      zamp : crossing height scale (z -> zamp*z)
      warp : list of (k, c, theta) — slice spacing: the braid-time angle phi_b is
             placed at geometric angle phi_g = phi_b + sum c sin(k phi_b + theta),
             with sum k|c| < 1 so the map is a smooth diffeomorphism of the circle."""
    comps = L.braid_components(word, n)
    phi = np.arange(M) * (2 * np.pi / M)
    P = L.braid_strand_positions(word, n, phi, R, a)
    r = np.hypot(P[..., 0], P[..., 1]); z = P[..., 2] * zamp
    pg = phi.copy()
    if warp:
        assert sum(k * abs(c) for k, c, _ in warp) < 1
        for k, c, th in warp: pg = pg + c * np.sin(k * phi + th)
    Q = np.stack([r * np.cos(pg)[:, None], r * np.sin(pg)[:, None], z], -1)
    return [np.concatenate([Q[:, lab, :] for lab in c], axis=0) for c in comps]

def random_warp(seed, kmax=3, total=0.6):
    rng = np.random.default_rng(seed)
    ks = np.arange(1, kmax + 1); c = rng.uniform(-1, 1, kmax)
    c = c / np.sum(ks * np.abs(c)) * total
    return [(int(k), float(cc), float(rng.uniform(0, 2 * np.pi))) for k, cc in zip(ks, c)]  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities

def mobius_image(curves, seed):
    """Orientation-PRESERVING Möbius image: inversion in a unit sphere about a random
    centre (not near the curve), then a reflection, then a random rotation."""
    rng = np.random.default_rng(seed)
    allp = np.vstack(curves); cen = allp.mean(0); rms = np.sqrt(np.mean(np.sum((allp - cen) ** 2, 1)))
    while True:
        v = rng.normal(size=3); v /= np.linalg.norm(v)
        c0 = cen + v * rms * rng.uniform(0.4, 1.6)  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        if np.min(np.linalg.norm(allp - c0, axis=1)) > 0.25 * rms: break
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(Q) < 0: Q[:, 0] *= -1
    out = []
    for c in curves:
        d = (c - c0) / rms
        y = d / np.sum(d * d, 1)[:, None]
        y[:, 0] *= -1                    # reflection: inversion∘reflection preserves orientation
        out.append(y @ Q.T)
    return out

def perturb(curves, eps, seed, kmax=6):
    """Random smooth perturbation: per component, sum of Fourier modes k=1..kmax with
    random vector coefficients decaying like 1/k, scaled so max displacement = eps*L_c/(2pi)."""
    rng = np.random.default_rng(seed)
    out = []
    for c in curves:
        N = len(c); u = np.arange(N) / N
        Lc = np.sum(np.linalg.norm(np.roll(c, -1, 0) - c, axis=1))
        D = np.zeros_like(c)
        for k in range(1, kmax + 1):
            D += (rng.normal(size=3)[None] * np.cos(2 * np.pi * k * u)[:, None]
                  + rng.normal(size=3)[None] * np.sin(2 * np.pi * k * u)[:, None]) / k
        D *= eps * Lc / (2 * np.pi) / np.max(np.linalg.norm(D, axis=1))
        out.append(c + D)
    return out

# ------------------------------------------------------------ certificates
def make_certify(cls):
    canon_w, canon_n = W.CANON[cls]
    import braid_topology as BT
    ref_link = L.alexander_from_poly(str(BT.burau_alexander(canon_w, canon_n)))
    ref_comp = [L.alexander_from_poly(p) for p in W.COMP_ALEX[cls]]
    def certify(curves):
        if len(curves) != len(ref_comp): return False
        if len(curves) == 2:
            v, _ = L.alexander_values(curves)
            if not L.same_up_to_units(v, ref_link): return False
        vals = [L.alexander_values([c])[0] for c in curves]
        for perm in itertools.permutations(range(len(curves))):
            if all(L.same_up_to_units(vals[i], ref_comp[j]) for i, j in zip(perm, range(len(curves)))):
                return True
        return False
    return certify

def lk_target(cls):
    import braid_topology as BT
    w, n = W.CANON[cls]
    return BT.linking_and_selfwrithe(w, n)[1]

# ------------------------------------------------------------ shape invariant
def shape_spectrum(curves, M=512, q=np.linspace(0.01, 0.99, 99)):  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
    """Möbius-quotiented shape invariant. Inverse-stereographic image in S^3,
    conformally balanced (ohara_lib.mobius_balance's iteration), resampled by S^3
    arclength, then quantiles of the pairwise chordal distances in each block
    (self blocks in order of decreasing self-energy, then the cross block).
    Invariant under the residual O(4); chordal distances lie in [0, 2]."""
    dense = [L.fourier_resample(c, max(4096, 8 * len(c))) for c in curves]
    Ps = [L._inv_stereo(c) for c in dense]
    for _ in range(300):
        Wt = []
        for P in Ps:
            seg = np.linalg.norm(np.roll(P, -1, 0) - P, axis=1); Wt.append(0.5 * (seg + np.roll(seg, 1)))
        allP = np.vstack(Ps); allW = np.concatenate(Wt)
        cc = (allP * allW[:, None]).sum(0) / allW.sum()
        if np.linalg.norm(cc) < 1e-10: break
        Ps = [L._ball_mobius(P, 0.5 * cc) for P in Ps]
        Ps = [P / np.linalg.norm(P, axis=1)[:, None] for P in Ps]
    res = []
    for P in Ps:   # resample by S^3 chordal-arclength
        seg = np.linalg.norm(np.roll(P, -1, 0) - P, axis=1)
        S = np.concatenate([[0], np.cumsum(seg)]); tg = np.arange(M) * S[-1] / M
        Pc = np.vstack([P, P[:1]])
        R = np.stack([np.interp(tg, S, Pc[:, k]) for k in range(4)], 1)
        res.append(R / np.linalg.norm(R, axis=1)[:, None])
    E = [L.self_energy_spectral(c)[0] for c in curves]
    order = np.argsort(E)[::-1]
    res = [res[i] for i in order]
    blocks = []
    for i in range(len(res)):
        D = np.linalg.norm(res[i][:, None] - res[i][None], axis=2)
        iu = np.triu_indices(M, 1); blocks.append(np.quantile(D[iu], q))
    if len(res) == 2:
        D = np.linalg.norm(res[0][:, None] - res[1][None], axis=2); blocks.append(np.quantile(D, q))
    return np.concatenate(blocks), float(np.linalg.norm(cc))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
