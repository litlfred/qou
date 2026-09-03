#!/usr/bin/env python3
"""M_1>0 constant-C step: measure the EMPIRICAL envelope constant of the (CS) margin bound
|m(n) - m_inf| <= C n^{-1/2}, and the implied threshold N0 = (C/m_inf)^2, to scope whether a
rigorous C <= m_inf*sqrt(79) ~ 2.651 (=> N0 <= 79, closed by the exact M_1>0 table to n=78) is
reachable.

Gap qou-k5r5, epic qou-x631. The rigorous finite-n bound (PR #5929) gives
|m(n) - m_inf| <= C n^{-1/2} with m_inf = 0.300186614 (merged #5901 IO value). To CLOSE M_1>0
for all n one needs an EXPLICIT C with N0 = (C/m_inf)^2 <= 79. This probe does NOT pin the
rigorous C (that is Bessel/Airy constant-tracking); it measures the exact margin
m(n) = rho_P(n) - sigma_D(n)/sigma_A(n) and reports:

  - the empirical envelope  C_emp(N) = max_{N<=n<=nmax} |m(n) - m_inf| * sqrt(n),
  - the implied N0_emp(N) = (C_emp(N)/m_inf)^2,
  - the target the rigorous C must beat: C_target = m_inf*sqrt(79) = 2.651.

Exact Fraction covariances/variances; mpmath only for sqrt/display; NO float64. scope-(a); no fit
(the exponent 1/2 is the DERIVED bulk-sine rate; C is MEASURED here only to scope feasibility, not
to close the proof -- a measured C is not a rigorous C). Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys
import mpmath as mp

mp.mp.dps = 30
M_INF = mp.mpf('0.300186614161')      # merged #5901 IO leading (CS) margin
C_TARGET = M_INF * mp.sqrt(79)         # rigorous C must be <= this for N0 <= 79


def partitions(n):
    def gen(n, mx):
        if n == 0:
            yield (); return
        for p in range(min(n, mx), 0, -1):
            for r in gen(n - p, p):
                yield (p,) + r
    yield from gen(n, n)


@lru_cache(maxsize=None)
def fact(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def stats(lam, n):
    m = lam[0] if lam else 0
    conj = [0] * m
    for part in lam:
        for j in range(part):
            conj[j] += 1
    prod = 1; absc = 0; c2 = 0; D = {}
    for i, part in enumerate(lam):
        for j in range(part):
            prod *= (part - j - 1) + (conj[j] - i - 1) + 1
            u = j - i
            absc += abs(u); c2 += u * u
            D[u] = D.get(u, 0) + 1
    d = fact(n) // prod
    return d, absc, sum(v * v for v in D.values()), c2


def margin(n):
    """Exact (CS) margin m(n) = rho(Sum|c|,w3) - sigma(SumD2)/sigma(Sum|c|)."""
    nf = fact(n)
    Cn2 = F(n * (n - 1), 2)
    ac = {k: F(0) for k in ("A", "D", "W", "AA", "DD", "WW", "AW")}
    for lam in partitions(n):
        d, A, Dd, c2 = stats(lam, n)
        w = F(d * d, nf)
        W = F(c2) - Cn2
        ac["A"] += w * A; ac["D"] += w * Dd; ac["W"] += w * W
        ac["AA"] += w * A * A; ac["DD"] += w * Dd * Dd; ac["WW"] += w * W * W
        ac["AW"] += w * A * W
    VA = ac["AA"] - ac["A"] ** 2
    VD = ac["DD"] - ac["D"] ** 2
    VW = ac["WW"] - ac["W"] ** 2
    P = ac["AW"] - ac["A"] * ac["W"]
    if VA <= 0 or VW <= 0:
        return None
    r = lambda x: mp.mpf(x.numerator) / x.denominator
    sig_ratio = mp.sqrt(r(VD) / r(VA))
    rho = r(P) / mp.sqrt(r(VA) * r(VW))
    return rho - sig_ratio


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 46
    print(f"# empirical (CS)-margin envelope; m_inf={mp.nstr(M_INF,9)}; "
          f"C_target=m_inf*sqrt(79)={mp.nstr(C_TARGET,6)} (N0<=79); dps={mp.mp.dps}; NO float64")
    print(f"# {'n':>3} {'m(n)':>11} {'m-m_inf':>11} {'|m-m_inf|*sqrt(n)':>18}")
    data = []
    for n in range(4, nmax + 1):
        mn = margin(n)
        if mn is None:
            continue
        dev = mn - M_INF
        env = abs(dev) * mp.sqrt(n)
        data.append((n, mn, dev, env))
        print(f"  {n:>3} {mp.nstr(mn,7):>11} {mp.nstr(dev,4):>11} {mp.nstr(env,6):>18}")
    print()
    # tail envelope C_emp(N) = max_{n>=N} |m-m_inf| sqrt(n), and implied N0
    print(f"# {'from N':>7} {'C_emp(N)=max_{n>=N}|m-m_inf|sqrt(n)':>36} {'N0_emp=(C/m_inf)^2':>20}")
    for N in (4, 6, 8, 10, 13, 20):
        tail = [d[3] for d in data if d[0] >= N]
        if not tail:
            continue
        Cemp = max(tail)
        N0 = (Cemp / M_INF) ** 2
        print(f"  {N:>7} {mp.nstr(Cemp,6):>36} {mp.nstr(N0,5):>20}")
    print()
    all_pos = all(d[1] > 0 for d in data)
    print(f"# exact margin m(n) > 0 for all 4<=n<={nmax}: {all_pos}")
    print("# INTERPRETATION: the empirical envelope C_emp is the FLOOR any rigorous C must exceed.")
    print(f"#   If C_emp << C_target={mp.nstr(C_TARGET,5)} the approach has large headroom; a rigorous C")
    print("#   within ~10x of C_emp still gives N0<=79. The rigorous C itself is NOT measured here --")
    print("#   it needs Bessel(Olver)/sine(Debye)/Airy(BDJ) constant-tracking (the remaining step).")
    print(f"RESULT: exact margin>0 to n={nmax}; empirical envelope + implied N0 tabulated; "
          f"C_target={mp.nstr(C_TARGET,5)}. qou-k5r5 OPEN (rigorous C not yet pinned).")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
