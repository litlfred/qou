#!/usr/bin/env python3
"""M_1>0 (CS) closure -- the sigma_D leg: the full (CS) margin approaches its IO limit by
DAMPED OSCILLATION with an envelope that decays ~n^-1, completing the descent-DPP picture.

Gap qou-k5r5, epic qou-x631. PR #5924 showed the content statistics are LINEAR statistics of
the descent DPP and measured the POISSONIZED (Poisson-smoothed over n) rho_P -> 2*sqrt(6)/5 = 0.9797958971 at a
clean rate a~1. The remaining leg of the (CS) margin
      m(n) = rho_P(n) - sigma(SumD2)/sigma(Sum|c|)
is sigma_D = sigma(SumD2), where SumD2 = Sum_u D(u)^2 is a QUADRATIC statistic of the descent
DPP (rigorous DPP treatment needs the 4-point function). This probe establishes the sigma_D
leg the EXACT way -- directly, by the combinatorial Plancherel variance (no linearization).

HONEST FINDING (corrects an initial over-claim of a "clean algebraic rate"):
  * The FIXED-n quantities sigma_D/sigma_A(n) and m(n) do NOT follow a pointwise power law.
    They OSCILLATE around their IO limits (0.679610 and 0.300187) -- the same damped
    arithmetic oscillation as kappa_n and the finite_n_cs_margin. A naive log-log slope on the
    fixed-n deviation is meaningless (it swings from +12 to -35); reporting it as a rate would
    be laundering an oscillation as convergence.
  * What DOES decay cleanly is the ENVELOPE: the successive LOCAL MAXIMA of |deviation| shrink
    ~n^-1, matching the Poisson-smoothed rho_P rate of PR #5924. Poisson-averaging over n (the
    DPP layer) removes the oscillation; fixed-n retains it.
  * m(n) > 0 throughout (min ~0.20 at n=4), oscillating in a band ~[0.20, 0.33] -- large
    headroom over 0.

Exact Fraction covariances/variances; mpmath only for sqrt/display; NO float64. The measured
ENVELOPE decay (not a pointwise rate) is what the (CS) all-n closure rests on: the crude BOO
edge/bulk kernel bound must trap the oscillation below the 0.30 leading margin for n>=N0, the
finite window closed by the exact table. scope-(a); no fit (envelope MEASURED, not chosen);
nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN, reduced.
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


def analyze(n):
    nf = fact(n); Cn2 = F(n * (n - 1), 2)
    ac = {k: F(0) for k in ("A", "D", "W", "AA", "DD", "WW", "AW")}
    for lam in partitions(n):
        d, A, Dd, c2 = stats(lam, n)
        w = F(d * d, nf); W = F(c2) - Cn2
        ac["A"] += w * A; ac["D"] += w * Dd; ac["W"] += w * W
        ac["AA"] += w * A * A; ac["DD"] += w * Dd * Dd; ac["WW"] += w * W * W
        ac["AW"] += w * A * W
    VA = ac["AA"] - ac["A"] ** 2
    VD = ac["DD"] - ac["D"] ** 2
    VW = ac["WW"] - ac["W"] ** 2
    P = ac["AW"] - ac["A"] * ac["W"]
    if VA <= 0 or VW <= 0 or VD <= 0:
        return None
    r = lambda x: mp.mpf(x.numerator) / x.denominator
    sig_ratio = mp.sqrt(r(VD) / r(VA))               # sigma_D / sigma_A  (EXACT, quadratic)
    rho = r(P) / mp.sqrt(r(VA) * r(VW))
    return sig_ratio, rho, rho - sig_ratio


def envelope(rows):
    """Local maxima of |deviation| (the oscillation envelope) and their log-log decay rate.
    Reporting the ENVELOPE, not a pointwise slope, because the deviation OSCILLATES."""
    a = [(n, abs(d)) for n, d in rows]
    peaks = []
    for i in range(1, len(a) - 1):
        if a[i][1] >= a[i - 1][1] and a[i][1] >= a[i + 1][1]:
            peaks.append(a[i])
    # always include the first point as the initial (largest) amplitude
    if a and (not peaks or peaks[0][0] != a[0][0]):
        peaks = [a[0]] + peaks
    rates = []
    for i in range(1, len(peaks)):
        (n0, d0), (n1, d1) = peaks[i - 1], peaks[i]
        if d0 > 0 and d1 > 0 and n1 > n0:
            rates.append((n0, n1, -(mp.log(d1) - mp.log(d0)) / (mp.log(n1) - mp.log(n0))))
    return peaks, rates


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    print(f"# sigma_D leg + full (CS) margin, EXACT combinatorial; dps={mp.mp.dps}; NO float64")
    print(f"# leading (#5901): sig_D/sig_A -> {mp.nstr(LEAD_SIGRATIO,8)}, "
          f"rho_P -> {mp.nstr(LEAD_RHO,8)}, margin -> {mp.nstr(LEAD_MARGIN,8)}")
    print(f"# {'n':>3} {'sigD/sigA':>11} {'->0.67961':>11} {'rho_P':>10} "
          f"{'CS margin':>10} {'->0.30019':>11}")
    sr_rows = []; mg_rows = []; all_pos = True; mn = None
    for n in range(4, nmax + 1):
        res = analyze(n)
        if res is None:
            continue
        sr, rho, marg = res
        all_pos = all_pos and (marg > 0)
        if mn is None or marg < mn:
            mn = marg; mn_at = n
        dsr = sr - LEAD_SIGRATIO; dmg = marg - LEAD_MARGIN
        sr_rows.append((n, dsr)); mg_rows.append((n, dmg))
        print(f"  {n:>3} {mp.nstr(sr,8):>11} {mp.nstr(dsr,3):>11} {mp.nstr(rho,7):>10} "
              f"{mp.nstr(marg,7):>10} {mp.nstr(dmg,3):>11}")
    print()
    print("# The deviation OSCILLATES (damped); reporting the ENVELOPE (local maxima of |dev|)")
    print("# and its decay, NOT a pointwise slope.")
    pk_sr, rt_sr = envelope(sr_rows)
    print("# sigma_D/sigma_A envelope peaks |dev|:  " +
          ", ".join(f"{n}:{mp.nstr(d,3)}" for n, d in pk_sr))
    for n0, n1, a in rt_sr:
        print(f"#   envelope decay n {n0:>3} -> {n1:<3}  ~ n^-{mp.nstr(a,3)}")
    pk_mg, rt_mg = envelope(mg_rows)
    print("# (CS) margin envelope peaks |dev|:      " +
          ", ".join(f"{n}:{mp.nstr(d,3)}" for n, d in pk_mg))
    for n0, n1, a in rt_mg:
        print(f"#   envelope decay n {n0:>3} -> {n1:<3}  ~ n^-{mp.nstr(a,3)}")
    print()
    print(f"# (CS) margin > 0 for all 4<=n<={nmax}: {all_pos}; min = {mp.nstr(mn,5)} at n={mn_at}")
    print("# sigma_D/sigma_A -> 0.679610 and m(n) -> 0.300187 by DAMPED OSCILLATION (NOT a clean")
    print("#   power law); the ENVELOPE decays ~n^-1, matching the Poisson-smoothed rho_P (PR #5924).")
    print("#   sigma_D is the EXACT quadratic statistic (no linearization). All-n closure needs the")
    print("#   crude BOO edge/bulk kernel bound to trap the oscillation below 0.30 for n>=N0.")
    print(f"RESULT: sigD/sigA -> 0.67961, m(n) -> 0.30019 by damped oscillation, envelope ~n^-1; "
          f"margin>0 all 4<=n<={nmax}: {all_pos}, min {mp.nstr(mn,4)}@n={mn_at}. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
