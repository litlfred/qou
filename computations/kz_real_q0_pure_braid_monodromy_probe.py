#!/usr/bin/env python3
"""KZ monodromy at the real substrate pin agrees with the Jimbo R-matrix,
sector by sector in the total weight (n = 3, pure braids).

Question (goal #1, bean qou-ywyq; proof page categorical-mass-markov-proof,
scope point 3). The discrete mass identity
    tr_M(beta) = wi^{m+1} Tr(K^{(x)n} Hol(beta))
is proved in Lean (QOU.Torsion.MassTraceMarkov) with Hol the ordered product
of Jimbo R-matrices. Promoting Hol to the holonomy of the sl2
Knizhnik-Zamolodchikov connection needs (a) Kohno's theorem at the coupling
that gives the REAL value q0 > 1, which is purely imaginary, and (b) an
intertwiner that preserves total weight, so that the weighted trace
Tr(K^{(x)n} .) transports. This probe tests both at n = 3 numerically.

Setup. V = C^2, Omega_ab = e_a f_b + f_a e_b + (1/2) h_a h_b (eigenvalue 1/2
on the triplet, -3/2 on the singlet). KZ: dF = lam sum Omega_ab dlog(z_a-z_b) F.
Slice z1 = 0, z3 = 1, z2 = x: dF/dx = lam (Omega_12/x + Omega_23/(x-1)) F.
Loop of x around 0 is the pure braid sigma_1^2; around 1 it is sigma_2^2.
Base point x = 1/2, loops of radius 1/2.

Convention, fixed by eigenvalues of sigma_1^2 alone (not by the products
tested): q = e^{i pi lam}, and theta(sigma_i^2) ~ q^{-1} (Rhat_i)^2 with
Rhat the Jimbo R-matrix (eigenvalues q on the triplet, -1/q on the singlet).
At q = q0 this gives lam = ln q0 / (i pi), purely imaginary.

Test. For each pure-braid word w and each total-weight sector s,
    Tr_s theta(w) = q^{-len(w)/2... } Tr_s phi(w)
with the scalar fixed above. A weight-sector match for a PRODUCT of
non-commuting loops is evidence for a weight-preserving intertwiner, not
implied by the eigenvalue matching. The integrator is classical RK4 in mpmath;
the residual must fall like h^4 (factor ~16 when steps double), which is what
separates discretisation error from a genuine mismatch.

What this does NOT show: n > 3, the full (non-pure) braid group, or anything
about whether the framework's substrate connection IS this KZ connection
(bean qou-d0qq). No float arithmetic; q0 is the proton pin (input).
"""
import itertools
import sys

import mpmath as mp

sys.path.insert(0, "tools/qou-substrate/python")
from qou_substrate.constants import q_at  # noqa: E402

mp.mp.dps = 40
N = 8
B = list(itertools.product([0, 1], repeat=3))  # 0 = up, 1 = down
IDX = {b: i for i, b in enumerate(B)}


def omega(a, b):
    M = mp.zeros(N, N)
    for s in B:
        i = IDX[s]
        M[i, i] += mp.mpf(1) / 2 * (1 if s[a] == s[b] else -1)
        if s[a] != s[b]:
            t = list(s)
            t[a], t[b] = s[b], s[a]
            M[IDX[tuple(t)], i] += 1
    return M


O12, O23 = omega(0, 1), omega(1, 2)


def transport(path, lam, steps):
    F = mp.eye(N)
    h = mp.mpf(1) / steps

    def f(t, Y):
        x, dx = path(t)
        return lam * (O12 / x + O23 / (x - 1)) * Y * dx

    for k in range(steps):
        t0 = k * h
        k1 = f(t0, F)
        k2 = f(t0 + h / 2, F + k1 * (h / 2))
        k3 = f(t0 + h / 2, F + k2 * (h / 2))
        k4 = f(t0 + h, F + k3 * h)
        F = F + (k1 + 2 * k2 + 2 * k3 + k4) * (h / 6)
    return F


def loop0(t):
    z = mp.expj(2 * mp.pi * t)
    return z / 2, 1j * mp.pi * z


def loop1(t):
    z = mp.expj(2 * mp.pi * t)
    return 1 - z / 2, -1j * mp.pi * z


def rhat(q):
    R = mp.zeros(4, 4)
    R[0, 0] = q
    R[3, 3] = q
    R[1, 2] = 1
    R[2, 1] = 1
    R[2, 2] = q - 1 / q
    return R


def embed(R, pos):
    M = mp.zeros(N, N)
    for s in B:
        for t in B:
            if all(s[k] == t[k] for k in range(3) if k not in (pos, pos + 1)):
                M[IDX[t], IDX[s]] = R[2 * t[pos] + t[pos + 1], 2 * s[pos] + s[pos + 1]]
    return M


def sector_traces(M):
    out = {}
    for s in B:
        w = sum(1 if c == 0 else -1 for c in s)  # 2 * total weight
        out[w] = out.get(w, 0) + M[IDX[s], IDX[s]]
    return out


def residuals(lam, steps):
    q = mp.expj(mp.pi * lam)
    M0, M1 = transport(loop0, lam, steps), transport(loop1, lam, steps)
    R1, R2 = embed(rhat(q), 0), embed(rhat(q), 1)
    P1, P2 = R1 * R1, R2 * R2
    words = {
        "s1^2": (M0, P1, q ** -1),
        "s2^2": (M1, P2, q ** -1),
        "s1^2 s2^2": (M0 * M1, P1 * P2, q ** -2),
        "s2^2 s1^2": (M1 * M0, P2 * P1, q ** -2),
        "s1^2 s2^-2": (M0 * mp.inverse(M1), P1 * mp.inverse(P2), mp.mpf(1)),
    }
    out = {}
    for name, (th, ph, sc) in words.items():
        a, b = sector_traces(th), sector_traces(ph)
        out[name] = (max(abs(a[k] - sc * b[k]) for k in a), max(abs(a[k]) for k in a))
    return out


def main():
    q0 = q_at(40)
    lam0 = mp.log(q0) / (1j * mp.pi)
    print("q0 =", mp.nstr(q0, 20), " lam0 =", mp.nstr(lam0, 12))
    ok = True
    coarse, fine = residuals(lam0, 200), residuals(lam0, 400)
    for name in coarse:
        e1, size = coarse[name]
        e2, _ = fine[name]
        ratio = e1 / e2
        good = e2 < mp.mpf("1e-12") * size and ratio > 10
        ok &= good
        print(f"{name:12s} |Tr| {mp.nstr(size, 6):>10s}  err200 {mp.nstr(e1, 3):>9s}  "
              f"err400 {mp.nstr(e2, 3):>9s}  ratio {mp.nstr(ratio, 4):>7s}  {'PASS' if good else 'FAIL'}")
    # negative control: R-matrix at the wrong orientation q -> 1/q must NOT match
    q = mp.expj(mp.pi * lam0)
    M0, M1 = transport(loop0, lam0, 200), transport(loop1, lam0, 200)
    Rw1, Rw2 = embed(rhat(1 / q), 0), embed(rhat(1 / q), 1)
    a = sector_traces(M0 * M1)
    b = sector_traces(Rw1 * Rw1 * Rw2 * Rw2)
    bad = max(abs(a[k] - q ** -2 * b[k]) for k in a)
    neg = bad > mp.mpf("1e-3")
    ok &= neg
    print("negative control (q -> 1/q):", mp.nstr(bad, 4), "PASS" if neg else "FAIL")
    print("ALL PASS" if ok else "FAILURES")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
