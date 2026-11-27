#!/usr/bin/env python3
"""Habiro cyclotomic coefficients c_k(K; q) of the weaving knots W(3,m) = closure of
V0^m (V0 = s0 s1^-1), EXACT, and their signs at the Kashaev roots of unity.

Pre-registration: PREREGISTRATION.md, Addendum 1 (question Q4).

  J_N(K; q) = sum_{k<N} c_k(K; q) * prod_{j=1}^{k} {N+j}{N-j},   {a} = v^a - v^-a,
  c_k in Z[q^{+-1}] independent of N (Habiro). At q = zeta_N the product is
  prod 4 sin^2(pi j/N) >= 0, so <K>_N is a term-wise non-negative sum iff
  c_k(zeta_N) >= 0 for all k < N.

Exact arithmetic: integer Laurent polynomials in w = q^{1/4} (numpy int64
convolution with a rigorous pre-multiplication overflow bound; an overflow risk
raises instead of wrapping). The colored Jones state model is the one pinned in
weaving_kashaev_probe.py. Evaluation of the exact c_k at zeta_M uses mpmath
(dps 50); the polynomials themselves are exact.

Run: python3 -u .../weaving_habiro_coefficients.py [Kmax]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 50
HERE = Path(__file__).resolve().parent
LIM = 2 ** 62
CONV = (True, True, False, 1, 1, 1)
PERIOD = [-1, 2]
NAME = {2: "4_1", 4: "8_18", 5: "10_123"}


class L:
    """Laurent polynomial sum c[i] w^(lo+i), integer coefficients."""
    __slots__ = ("lo", "c")

    def __init__(self, lo: int, c):
        c = np.asarray(c, dtype=np.int64)
        nz = np.nonzero(c)[0]
        if len(nz) == 0:
            self.lo, self.c = 0, np.zeros(0, dtype=np.int64)
        else:
            self.lo, self.c = lo + int(nz[0]), c[nz[0]:nz[-1] + 1].copy()

    @staticmethod
    def mono(k: int, a: int = 1) -> "L":
        return L(k, [a])

    def iszero(self):
        return len(self.c) == 0

    def __add__(self, o: "L") -> "L":
        if self.iszero():
            return o
        if o.iszero():
            return self
        lo = min(self.lo, o.lo)
        hi = max(self.lo + len(self.c), o.lo + len(o.c))
        r = np.zeros(hi - lo, dtype=np.int64)
        if np.abs(self.c).max() + np.abs(o.c).max() >= LIM:
            raise OverflowError("add")
        r[self.lo - lo:self.lo - lo + len(self.c)] += self.c
        r[o.lo - lo:o.lo - lo + len(o.c)] += o.c
        return L(lo, r)

    def __neg__(self):
        return L(self.lo, -self.c)

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o: "L") -> "L":
        if self.iszero() or o.iszero():
            return L(0, [])
        bound = int(np.abs(self.c).sum(dtype=object)) * int(np.abs(o.c).max())
        if bound >= LIM:
            raise OverflowError("mul")
        return L(self.lo + o.lo, np.convolve(self.c, o.c))

    def divexact(self, d: "L") -> "L":
        """Exact division by d whose top coefficient is +-1; raises if inexact."""
        if d.iszero():
            raise ZeroDivisionError
        lead = int(d.c[-1])
        assert lead in (1, -1)
        rem = [int(x) for x in self.c]
        rlo = self.lo
        n, m = len(rem), len(d.c)
        dc = [int(x) for x in d.c]
        if n < m:
            if any(rem):
                raise ArithmeticError("inexact")
            return L(0, [])
        q = [0] * (n - m + 1)
        for i in range(n - m, -1, -1):
            coef = rem[i + m - 1] * lead
            q[i] = coef
            if coef:
                for j in range(m):
                    rem[i + j] -= coef * dc[j]
        if any(rem):
            raise ArithmeticError("inexact division")
        return L(rlo - d.lo, q)

    def eval(self, w):
        return sum(int(a) * w ** (self.lo + i) for i, a in enumerate(self.c) if a)


def br(a: int) -> L:  # {a} = v^a - v^-a, v = w^2
    if a == 0:
        return L(0, [])
    return L.mono(2 * a) - L.mono(-2 * a)


def poch(a: int, b: int) -> L:
    out = L.mono(0)
    for k in range(b):
        out = out * br(a - k)
    return out


def binom_table(amax: int):
    C = [[L(0, [])] * (amax + 1) for _ in range(amax + 1)]
    for a in range(amax + 1):
        C[a][0] = L.mono(0)
        for b in range(1, a + 1):
            C[a][b] = L.mono(2 * b) * C[a - 1][b] + L.mono(-2 * (a - b)) * C[a - 1][b - 1]
    return C


def f_table(n: int):
    C = binom_table(2 * n + 2)
    F = {}
    for eps in (1, -1):
        for i in range(n + 1):
            for j in range(n + 1):
                for r in range(n + 1):
                    if eps > 0:
                        val = L.mono(-((n - 2 * i) * (n - 2 * j) + r * (r - 1)), (-1) ** r) \
                            * C[j + r][r] * poch(n + r - i, r)
                    else:
                        val = L.mono((n - 2 * i - 2 * r) * (n - 2 * j + 2 * r) + r * (r - 1)) \
                            * C[i + r][r] * poch(n + r - j, r)
                    F[(eps, i, j, r)] = val
    return F


def apply_crossing(states, g, n, F):
    lop, ijp, ijm, sgp, sgm, _cs = CONV
    p = abs(g) - 1
    eps = 1 if g > 0 else -1
    left_over = lop if eps > 0 else (not lop)
    ij_over_under = ijp if eps > 0 else ijm
    sgn = sgp if eps > 0 else sgm
    new = {}
    for c, wt in states.items():
        a, b = c[p], c[p + 1]
        over, under = (a, b) if left_over else (b, a)
        i, j = (over, under) if ij_over_under else (under, over)
        for r in range(n + 1):
            o2, u2 = over - sgn * r, under + sgn * r
            if not (0 <= o2 <= n and 0 <= u2 <= n):
                continue
            fv = F[(eps, i, j, r)]
            if fv.iszero():
                continue
            nc = list(c)
            if left_over:
                nc[p], nc[p + 1] = u2, o2
            else:
                nc[p], nc[p + 1] = o2, u2
            nc = tuple(nc)
            t = wt * fv
            new[nc] = new[nc] + t if nc in new else t
    return new


def colored_jones(m: int, n: int) -> L:
    """J'_n(W(3,m)) as an exact Laurent polynomial in w (colour n = dimension n+1)."""
    F = f_table(n)
    total = L(0, [])
    for r1 in range(n + 1):
        for r2 in range(n + 1):
            start = (0, r1, r2)
            st = {start: L.mono(0)}
            for g in PERIOD * m:
                st = apply_crossing(st, g, n, F)
            wt = st.get(start)
            if wt is None:
                continue
            clos = L.mono(sum(2 * CONV[5] * (-n + 2 * b) for b in (r1, r2)))
            total = total + wt * clos
    return total


def habiro_prod(N: int, k: int) -> L:
    out = L.mono(0)
    for j in range(1, k + 1):
        out = out * br(N + j) * br(N - j)
    return out


def main() -> int:
    Kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    t0 = time.time()
    out = {"preregistration": "PREREGISTRATION.md Addendum 1 (Q4)", "Kmax": Kmax, "knots": {}}
    for m in (2, 4, 5):
        J = {}
        cs = []
        for N in range(1, Kmax + 2):
            J[N] = colored_jones(m, N - 1)
            # triangular solve for c_{N-1}
            rest = J[N]
            for k, ck in enumerate(cs):
                rest = rest - ck * habiro_prod(N, k)
            ck = rest.divexact(habiro_prod(N, N - 1))
            cs.append(ck)
            print(f"{NAME[m]} c_{N-1}: w-degree [{ck.lo},{ck.lo+len(ck.c)-1}], "
                  f"terms={int(np.count_nonzero(ck.c))}, max|coef|={int(np.abs(ck.c).max()) if len(ck.c) else 0}"
                  f"  [{time.time()-t0:.0f}s]", flush=True)
        # consistency: re-derive J_N from the c_k for every N computed
        for N in range(1, Kmax + 2):
            recon = L(0, [])
            for k in range(N):
                recon = recon + cs[k] * habiro_prod(N, k)
            assert (recon - J[N]).iszero(), (m, N)
        rec = {"c": [], "signs": []}
        for k, ck in enumerate(cs):
            rec["c"].append({"lo": ck.lo, "coeffs": [int(x) for x in ck.c]})
            vals = []
            neg = []
            for M in range(k + 1, 61):
                wM = mp.expjpi(mp.mpf(1) / (2 * M))  # w = e^{2 pi i/(4M)}
                z = ck.eval(wM)
                vals.append((M, z))
                if z.real < -mp.mpf(10) ** -30 or abs(z.imag) > mp.mpf(10) ** -30 * (1 + abs(z)):
                    neg.append(M)
            rec["signs"].append({
                "k": k,
                "M_with_negative_or_nonreal": neg,
                "min_real": mp.nstr(min(z.real for _, z in vals), 12),
                "max_abs_imag": mp.nstr(max(abs(z.imag) for _, z in vals), 3),
                "sample": {str(M): mp.nstr(z.real, 12) for M, z in vals[:6]},
            })
            print(f"{NAME[m]} k={k}: c_k(zeta_M), M={k+1}..60: min Re = {rec['signs'][-1]['min_real']},"
                  f" max|Im| = {rec['signs'][-1]['max_abs_imag']},"
                  f" negative/non-real at M = {neg[:12]}{'...' if len(neg) > 12 else ''}", flush=True)
        out["knots"][NAME[m]] = rec
    out["elapsed_s"] = round(time.time() - t0)
    (HERE / "weaving-habiro.result.json").write_text(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
