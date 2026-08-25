#!/usr/bin/env python3
"""M_1>0 sign: pin the 2nd-order coefficient a_1 of kappa_n = kappa + a_1 n^{-1/2}+...

Gap qou-k5r5. kappa_n = M_1/n^{5/2} -> kappa = 128/(225 pi^2). The one-sided sign
'kappa_n >= kappa for n>=13' would follow from the SIGN of the leading correction:
if kappa_n - kappa = a_1 n^{-1/2} + a_2 n^{-1} + ... with a_1 > 0, then kappa_n -> kappa
FROM ABOVE. This probe extracts a_1 (and a_2,...) by an EXACT-data multi-term fit:
solve kappa_n - kappa = sum_{j=1}^{J} a_j n^{-j/2} on high-n windows, for increasing
J, and check whether a_1 stabilizes to a clean positive value.

M_1 computed EXACTLY (Fraction, direct Plancherel); kappa and the fit in mpmath 60 dps.
Honest: this extrapolates; it does NOT prove a_1>0. If a_1 is unstable / sign-ambiguous,
that is reported. NO float64. scope-(a); no fit-to-production; nothing wired; L2 unchanged.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys
import mpmath as mp

mp.mp.dps = 60


def partitions(n):
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for p in range(min(n, mx), 0, -1):
            for r in gen(n - p, p):
                yield (p,) + r
    yield from gen(n, n)


@lru_cache(maxsize=None)
def factorial(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def exact_M1(n):
    nf = factorial(n)
    Cn2 = F(n * (n - 1), 2)
    sH = sW = sHW = 0
    for lam in partitions(n):
        m = lam[0] if lam else 0
        conj = [0] * m
        for part in lam:
            for j in range(part):
                conj[j] += 1
        prod = 1
        H = 0
        c2 = 0
        for i, part in enumerate(lam):
            for j in range(part):
                prod *= (part - j - 1) + (conj[j] - i - 1) + 1
                H += (part - j - 1) + (conj[j] - i - 1) + 1
                c2 += (j - i) ** 2
        w = (factorial(n) // prod) ** 2
        om = F(c2) - Cn2
        sH += w * H
        sW += w * om
        sHW += w * H * om
    EH = F(sH, nf); EW = F(sW, nf)
    return F(sHW, nf) - EH * EW   # = Cov(Sum_h, omega3) = M_1


def main():
    nlo = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    nhi = int(sys.argv[2]) if len(sys.argv) > 2 else 44
    kappa = mp.mpf(128) / (225 * mp.pi ** 2)
    print(f"# kappa = {mp.nstr(kappa,15)}; fitting kappa_n - kappa = sum a_j n^(-j/2)")
    kn = {}
    for n in range(nlo, nhi + 1):
        M1 = exact_M1(n)
        kn[n] = mp.mpf(M1.numerator) / M1.denominator / mp.power(n, mp.mpf(5) / 2) - kappa
    # multi-term fits: for J terms use the top J points (windowed), report a_1
    def fit(ns_window, J):
        # solve sum_{j=1}^{J} a_j n^{-j/2} = kn[n] for the J points in ns_window
        A = mp.matrix(J, J)
        b = mp.matrix(J, 1)
        for r, n in enumerate(ns_window):
            for c in range(J):
                A[r, c] = mp.power(n, -mp.mpf(c + 1) / 2)
            b[r] = kn[n]
        sol = mp.lu_solve(A, b)
        return [sol[j] for j in range(J)]

    alln = list(range(nlo, nhi + 1))
    print(f"# {'J':>2} {'window (top J)':>22} {'a_1':>16} {'a_2':>14} {'a_3':>14}")
    for J in range(1, 6):
        win = alln[-J:]
        try:
            a = fit(win, J)
            a1 = a[0]
            a2 = a[1] if J >= 2 else mp.mpf('nan')
            a3 = a[2] if J >= 3 else mp.mpf('nan')
            print(f"  {J:>2} {str((win[0],win[-1])):>22} {mp.nstr(a1,10):>16} {mp.nstr(a2,8):>14} {mp.nstr(a3,8):>14}")
        except Exception as e:
            print(f"  {J:>2} fit failed: {e}")
    # also: rolling 3-term fit of a_1 across windows to see stability/sign
    print("# rolling 3-term (a_1,a_2,a_3) fits across sliding windows -> a_1 stability/sign:")
    a1s = []
    for start in range(0, len(alln) - 3 + 1, max(1, (len(alln)-3)//8)):
        win = alln[start:start + 3]
        try:
            a = fit(win, 3)
            a1s.append((win, a[0]))
            print(f"#   window {(win[0],win[-1])}: a_1 = {mp.nstr(a[0],8)}")
        except Exception:
            pass
    signs = [1 if a > 0 else (-1 if a < 0 else 0) for _, a in a1s]
    print(f"# a_1 sign across windows: {'all +' if all(s>0 for s in signs) else ('all -' if all(s<0 for s in signs) else 'MIXED')}")
    print("RESULT: a_1 (n^-1/2 coeff of kappa_n) extrapolation tabulated; sign is the target for kappa_n->kappa from above.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
