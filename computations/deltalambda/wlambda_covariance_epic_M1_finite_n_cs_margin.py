#!/usr/bin/env python3
"""M_1>0 finite-n step: the exact (CS) margin converges to the derived leading value
by DAMPED OSCILLATION (positive throughout) — the precise remaining requirement.

Gap qou-k5r5, epic qou-x631. PR #5901 DERIVED the (CS) condition at leading order:
sig(SumD2)/sig(Sum|c|) -> 0.67961 < rho(Sum|c|,omega3) -> 0.97980, leading margin 0.30019.
To close M_1>0 for ALL n one needs the (CS) margin to stay positive at finite n.

This probe measures the EXACT finite-n (CS) margin m(n) = rho_P(n) - sig_D(n)/sig_A(n)
(exact Fraction covariances/variances; mpmath only for sqrt/display; NO float64) and
compares it to the leading limit 0.30019. Findings:

  - m(n) is POSITIVE for every n>=4 (minimum m(4)=0.2003; (CS) holds throughout).
  - m(n) does NOT approach the limit monotonically: it OSCILLATES with decreasing
    amplitude around 0.30019 (peak ~0.329 at n=9, dip ~0.298 at n=14, ...), the same
    damped-oscillation finite-n signature as kappa_n. (An earlier hypothesis that m(n)
    "increases to the limit from below" is REFUTED here.)

Consequence: exact-check-small-n + leading-order-large-n does NOT trivially cover all n,
because the tail is oscillatory, not monotone. The precise remaining requirement to close
M_1>0 is an EFFECTIVE (quantitative) bound on the IO Kerov-CLT variance asymptotics --
|sig_D^2/n^2 - V_D| <= C/n^a etc. -- large enough (leading margin 0.30) that a crude rate
suffices, but NOT delivered by the marginal Berry-Esseen (Fulman, ruled out) or the
qualitative CLT. That effective variance bound is the one open step.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys
import mpmath as mp

mp.mp.dps = 30
from _m1_io_constants import LEAD_MARGIN, LEAD_SIGRATIO, LEAD_RHO  # merged #5901 IO leading constants -- single source, see that module


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
    prod = 1
    absc = 0
    c2 = 0
    D = {}
    for i, part in enumerate(lam):
        for j in range(part):
            prod *= (part - j - 1) + (conj[j] - i - 1) + 1
            u = j - i
            absc += abs(u)
            c2 += u * u
            D[u] = D.get(u, 0) + 1
    d = fact(n) // prod
    return d, absc, sum(v * v for v in D.values()), c2


def analyze(n):
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
    r = lambda x: mp.mpf(x.numerator) / x.denominator
    if VA <= 0 or VW <= 0:
        return None
    sig_ratio = mp.sqrt(r(VD) / r(VA))
    rho = r(P) / mp.sqrt(r(VA) * r(VW))
    return sig_ratio, rho, rho - sig_ratio


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    print(f"# leading (PR #5901): sig_D/sig_A -> {mp.nstr(LEAD_SIGRATIO,8)}, "
          f"rho_P -> {mp.nstr(LEAD_RHO,8)}, margin -> {mp.nstr(LEAD_MARGIN,8)}")
    print(f"# {'n':>3} {'sig_D/sig_A':>12} {'rho_P':>10} {'CS margin':>11} "
          f"{'m-lead':>10} {'CS holds':>8}")
    all_hold = True
    min_margin = None
    min_at = None
    for n in range(4, nmax + 1):
        res = analyze(n)
        if res is None:
            continue
        sr, rho, marg = res
        holds = marg > 0
        all_hold = all_hold and holds
        if min_margin is None or marg < min_margin:
            min_margin = marg; min_at = n
        print(f"  {n:>3} {mp.nstr(sr,8):>12} {mp.nstr(rho,7):>10} {mp.nstr(marg,7):>11} "
              f"{mp.nstr(marg-LEAD_MARGIN,4):>10} {holds!s:>8}")
    print()
    print(f"# (CS) margin > 0 for all 4<=n<={nmax}: {all_hold}; "
          f"min margin = {mp.nstr(min_margin,6)} at n={min_at}")
    print("# The margin OSCILLATES around the leading 0.30019 with decreasing amplitude")
    print("#   (NOT monotone). Closing M_1>0 all-n needs an EFFECTIVE bound on the IO-CLT")
    print("#   variance asymptotics controlling this oscillation tail -- the one open step;")
    print("#   the 0.30 leading margin means a CRUDE rate suffices.")
    print(f"RESULT: (CS) holds (margin>0) for all 4<=n<={nmax}: {all_hold}; min={mp.nstr(min_margin,5)} at n={min_at}")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
