#!/usr/bin/env python3
"""Route 2 energy (beans qou-99qc, qou-pzsi): Mobius-type energy of the Bring loop.

Implements preregistration-energy.md. No Q_beta / CODATA / mass input anywhere.

Geometry.  The loop element is Gam = G^r in Gamma_B = ker(Delta(2,4,5) -> S_5) =
pi_1(Bring), with G the Delta(2,4,5) image of the braid word (bring_route2_probe).
Everything is conjugated so that Gam's axis is the imaginary axis, the loop is
A(s) = i e^s, s in [-L/2, L/2], and the segment midpoint is m = i.  Then
cosh d(i, h i) = |h|_F^2 / 2.

Enumeration bound.  For s, t in [-L/2, L/2] (t is any lift: the axis translations
Gam^n are themselves in Gamma_B), the integrand is non-zero only if some h has
d(A(s), h A(t)) < delta(s, t) <= L/2, so
    d(i, h i) <= d(i, A(s)) + d(A(s), h A(t)) + d(h A(t), h i) <= 1.5 L.
A self-intersection gives an h (not stabilising the axis) whose image axis crosses
the imaginary axis; translating the crossing into the segment gives d(i, h i) <= L.
So every Gamma_B element with displacement <= 1.5 L at i is enumerated.

Arithmetic: mpmath mpf at 30 dps throughout; no float64.
"""
import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
import bring_route2_probe as R2  # noqa: E402

mp.mp.dps = 30
R2.mp.mp.dps = 30

LOOP_WORDS = ["gluon_s1_s0", "gluon_s1_s1", "nuc11_gen_grouped"]
GRIDS = [int(x) for x in __import__("os").environ.get("GRIDS", "120,240,480").split(",")]


# ---------------------------------------------------------------- small SL(2,R) helpers
def mmul(A, B):
    return (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3],
            A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])


def minv(A):
    return (A[3], -A[1], -A[2], A[0])


def from_mp(M):
    return (M[0, 0], M[0, 1], M[1, 0], M[1, 1])


def act(A, z):
    return (A[0] * z + A[1]) / (A[2] * z + A[3])


def key(A, digits=18):
    """Projective key: fix the sign so the first entry that is not ~0 is positive."""
    sgn = 1
    for x in A:
        if abs(x) > mp.mpf(10) ** -10:
            sgn = 1 if x > 0 else -1
            break
    return tuple(mp.nstr(sgn * x, digits) for x in A)


def cosh_disp_i(A):
    return (A[0] ** 2 + A[1] ** 2 + A[2] ** 2 + A[3] ** 2) / 2


def cosh_dist(z, w):
    return 1 + abs(z - w) ** 2 / (2 * z.imag * w.imag)


# ---------------------------------------------------------------- permutations (S_5)
E5 = tuple(range(5))


def pinv(p):
    q = [0] * 5
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)


# ---------------------------------------------------------------- setup per loop
def loop_setup(name, s_mp, u_mp, sig, rho):
    rows = json.loads((Path(__file__).with_name("results.json")).read_text())["rows"]
    row = rows[name]
    word = [tuple(w) for w in row["h4_word"]]
    r = row["r_congruence_H4(5)"]
    s, u = from_mp(s_mp), from_mp(u_mp)
    ui = minv(u)
    G = (1, 0, 0, 1)
    for w in word:
        if w[0] == "S":
            G = mmul(G, s)
        else:
            n = w[1] % 10
            for _ in range(n):
                G = mmul(G, u)
    Gam = (1, 0, 0, 1)
    for _ in range(r):
        Gam = mmul(Gam, G)
    tr = Gam[0] + Gam[3]
    L = 2 * mp.acosh(abs(tr) / 2)
    # fixed points of Gam: c z^2 + (d - a) z - b = 0
    a, b, c, d = Gam
    disc = mp.sqrt((d - a) ** 2 + 4 * b * c)
    x1, x2 = (-(d - a) + disc) / (2 * c), (-(d - a) - disc) / (2 * c)
    # C: z -> (z - x1)/(z - x2), normalised into SL(2,R) with positive determinant
    det = x1 - x2
    sc = 1 / mp.sqrt(abs(det))
    C = (sc, -x1 * sc, sc, -x2 * sc)
    if det < 0:
        C = (-C[0], -C[1], C[2], C[3])
    Gc = mmul(mmul(C, Gam), minv(C))
    assert abs(Gc[1]) < mp.mpf(10) ** -20 and abs(Gc[2]) < mp.mpf(10) ** -20
    # BFS (word length) in Delta for orbit points of fix(s) = i, to centre m near one
    sc_, uc_ = mmul(mmul(C, s), minv(C)), mmul(mmul(C, u), minv(C))
    uci = minv(uc_)
    gens = [(sc_, sig), (uc_, rho), (uci, pinv(rho))]
    p_s = act(C, mp.mpc(0, 1))
    seen = {key((1, 0, 0, 1)): ((1, 0, 0, 1), E5)}
    frontier = [((1, 0, 0, 1), E5)]
    best = None
    for _ in range(9):
        nxt = []
        for (K, pk) in frontier:
            for (g, pg) in gens:
                K2 = mmul(K, g)
                kk = key(K2)
                if kk in seen:
                    continue
                p2 = R2.pcomp(pk, pg)
                seen[kk] = (K2, p2)
                nxt.append((K2, p2))
                z = act(K2, p_s)
                rho_d = mp.asinh(abs(z.real) / z.imag)  # distance to imaginary axis
                foot = abs(z)
                logf = mp.log(foot)
                # keep the foot inside the fundamental segment, any lift is fine
                if best is None or rho_d < best[0]:
                    best = (rho_d, logf, K2, p2)
        frontier = nxt
    rho_d, logf, K, pk = best
    # translate along the axis so the foot is at i
    Dsh = (mp.exp(-logf / 2), 0, 0, mp.exp(logf / 2))
    M = mmul(Dsh, C)
    Kc = mmul(mmul(Dsh, K), minv(Dsh))
    Gm = mmul(mmul(M, Gam), minv(M))
    gs = mmul(mmul(Kc, mmul(mmul(M, s), minv(M))), minv(Kc))
    gu = mmul(mmul(Kc, mmul(mmul(M, u), minv(M))), minv(Kc))
    perm_s = R2.pcomp(R2.pcomp(pk, sig), pinv(pk))
    perm_u = R2.pcomp(R2.pcomp(pk, rho), pinv(pk))
    return dict(name=name, L=L, r=r, Gam=Gm, gens=[(gs, perm_s), (gu, perm_u),
                (minv(gu), pinv(perm_u))], dist_m_cone=rho_d)


def enumerate_kernel(gens, R, slack):
    """All Delta elements with displacement <= R + slack at i, BFS-pruned; return the
    Gamma_B ones (identity permutation) with displacement <= R."""
    cap = mp.cosh(R + slack)
    seen = {key((1, 0, 0, 1)): ((1, 0, 0, 1), E5)}
    frontier = [((1, 0, 0, 1), E5)]
    while frontier:
        nxt = []
        for (h, ph) in frontier:
            for (g, pg) in gens:
                h2 = mmul(h, g)
                if cosh_disp_i(h2) > cap:
                    continue
                kk = key(h2)
                if kk in seen:
                    continue
                p2 = R2.pcomp(ph, pg)
                seen[kk] = (h2, p2)
                nxt.append((h2, p2))
        frontier = nxt
    capR = mp.cosh(R)
    ker = [h for (h, p) in seen.values() if p == E5 and cosh_disp_i(h) <= capR]
    return ker, len(seen)


def is_axis_stabiliser(h):
    return abs(h[1]) < mp.mpf(10) ** -15 and abs(h[2]) < mp.mpf(10) ** -15


def crosses_axis(h):
    # endpoints of h(imaginary axis) are h(0) = b/d and h(inf) = a/c
    if abs(h[3]) < mp.mpf(10) ** -15 or abs(h[2]) < mp.mpf(10) ** -15:
        return False  # an endpoint is at 0 or infinity: shares an endpoint, no transverse crossing
    e0, e1 = h[1] / h[3], h[0] / h[2]
    return (e0 > 0) != (e1 > 0)


def energy(ker_nonstab, L, N, kernel):
    """Periodic trapezoid of 1/D^2 - 1/delta^2 (kernel 'flat') or the sinh version."""
    hstep = L / N
    pts = [-L / 2 + k * hstep for k in range(N)]
    A = [mp.mpc(0, mp.exp(x)) for x in pts]
    # D2[a][b] = best cosh-distance from non-stabiliser h (smaller is closer)
    best = {}
    capc = mp.cosh(L / 2)
    for h in ker_nonstab:
        hA = [act(h, z) for z in A]
        for ia in range(N):
            za = A[ia]
            for ib in range(N):
                cd = cosh_dist(za, hA[ib])
                if cd < capc:
                    k = (ia, ib)
                    if k not in best or cd < best[k]:
                        best[k] = cd
    tot = mp.mpf(0)
    for (ia, ib), cd in best.items():
        dl = abs(pts[ia] - pts[ib])
        dl = min(dl, L - dl)
        dX = mp.acosh(cd)
        if dX >= dl:
            continue
        if kernel == "flat":
            tot += 1 / dX ** 2 - 1 / dl ** 2
        else:
            tot += 1 / (2 * mp.sinh(dX / 2)) ** 2 - 1 / (2 * mp.sinh(dl / 2)) ** 2
    return tot * hstep * hstep


def main():
    s_mp, u_mp = R2.delta245()
    rho, sigmas = R2.s5_epimorphisms()
    checks, out = {}, {}
    for name in LOOP_WORDS:
        st = loop_setup(name, s_mp, u_mp, sigmas[0], rho)
        L = st["L"]
        R = mp.mpf(3) / 2 * L
        ker, nseen = enumerate_kernel(st["gens"], R, mp.mpf(3))
        ker2, _ = enumerate_kernel(st["gens"], R, mp.mpf(4))
        stab = [h for h in ker if is_axis_stabiliser(h)]
        tl = sorted({mp.nstr(2 * mp.acosh(abs(h[0] + h[3]) / 2), 20) for h in stab})
        nonstab = [h for h in ker if not is_axis_stabiliser(h)]
        crossing = [h for h in nonstab if crosses_axis(h)]
        row = {"L": mp.nstr(L, 25), "r": st["r"], "kernel_elements_within_1.5L": len(ker),
               "delta_elements_enumerated": nseen,
               "slack_3_vs_4_same_kernel_set": {key(h) for h in ker} == {key(h) for h in ker2},
               "axis_stabiliser_translation_lengths": tl,
               "self_crossing_elements": len(crossing),
               "dist_midpoint_to_cone_point": mp.nstr(st["dist_m_cone"], 10)}
        Lstr = mp.nstr(L, 20)
        primitive = all(x in ("0.0", Lstr) for x in tl)
        row["primitive"] = primitive
        print(f"{name}: L={mp.nstr(L, 15)} |ker<=1.5L|={len(ker)} (Delta seen {nseen}) "
              f"stab lengths={tl} crossings={len(crossing)} primitive={primitive}", flush=True)
        if crossing or not primitive:
            row["E"] = "+inf (self-intersecting or non-primitive, preregistration-energy §1)"
            row["E_sinh"] = row["E"]
        else:
            for kern in ("flat", "sinh"):
                vals = {}
                for N in GRIDS:
                    vals[N] = energy(nonstab, L, N, kern)
                    print(f"   {kern} N={N}: {mp.nstr(vals[N], 15)}", flush=True)
                row[f"E_{kern}_by_N"] = {str(k): mp.nstr(v, 20) for k, v in vals.items()}
        out[name] = row
        checks[f"{name}_slack_stable"] = row["slack_3_vs_4_same_kernel_set"]
        checks[f"{name}_loop_translation_in_kernel"] = Lstr in tl
    a, b = out["gluon_s1_s0"], out["gluon_s1_s1"]
    checks["conjugate_pair_same_E"] = (a.get("E"), a.get("E_flat_by_N", {}).get("480")) == \
        (b.get("E"), b.get("E_flat_by_N", {}).get("480")) and a["L"] == b["L"]
    for k, v in checks.items():
        print(("PASS " if v else "FAIL ") + k)
    Path(__file__).with_name("results_energy.json").write_text(json.dumps(
        {"description": "Route 2 Bring loop energy; see preregistration-energy.md",
         "mp_dps": mp.mp.dps, "mpmath": mp.__version__, "rows": out, "checks": checks},
        indent=1, default=str))
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
