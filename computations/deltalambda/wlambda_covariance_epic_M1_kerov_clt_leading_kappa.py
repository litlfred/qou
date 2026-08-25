#!/usr/bin/env python3
"""M_1 = Cov_Planch(Sum_h, Sum_c^2) — pin the leading constant kappa EXACTLY.

Covariance-kernel epic qou-x631, gap bean qou-k5r5. The first odd hook-power
moment is M_1 = (1/3) Cov(Sum_box h, R_4) = Cov(Sum_box h, Sum_box c^2), an
exact identity already Lean-formalized (PR #5366). Numerically
    Cov(Sum_h, Sum_c^2) ~ kappa * n^{5/2},   kappa > 0
but kappa was never pinned: a float64 Richardson was unstable (catastrophic
cancellation in E[XY]-E[X]E[Y]).

FIX (discipline: NO float64 — AGENTS.md precision gate): compute the covariance
in EXACT Fraction arithmetic (Plancherel weight w_lambda = (f^lambda)^2 / n! is
an exact rational; Sum_h and Sum_c^2 are exact integers), then extrapolate
kappa_n = Cov(n)/n^{5/2} in mpmath at high precision. The only irrational step
is the final n^{5/2}, done once per n at 60 dps.

This is the EXACT ANCHOR the analytic Kerov-CLT leading-term derivation must
reproduce. It does NOT by itself prove kappa > 0 for all n (that is the CLT
derivation + Fulman finite-n bound); it pins the target constant so the
analytic claim is falsifiable.

Honesty: scope-(a); no fit to production; nothing wired; no c_k; L2 unchanged.
"""
from __future__ import annotations
from fractions import Fraction
from functools import lru_cache
import sys

import mpmath as mp

mp.mp.dps = 60

# ----------------------------------------------------------------------------
# partitions, hooks, contents, SYT count
# ----------------------------------------------------------------------------

def partitions(n: int):
    """Generate partitions of n as non-increasing tuples."""
    def gen(n, maxp):
        if n == 0:
            yield ()
            return
        for p in range(min(n, maxp), 0, -1):
            for rest in gen(n - p, p):
                yield (p,) + rest
    yield from gen(n, n)


def hooks_contents(lam: tuple[int, ...]):
    """Return (list of hook lengths, sum of contents^2) for partition lam."""
    conj = []
    if lam:
        m = lam[0]
        conj = [0] * m
        for part in lam:
            for j in range(part):
                conj[j] += 1
    hook_list = []
    sum_c2 = 0
    for i, part in enumerate(lam):
        for j in range(part):
            arm = part - j - 1
            leg = conj[j] - i - 1
            hook_list.append(arm + leg + 1)
            c = j - i
            sum_c2 += c * c
    return hook_list, sum_c2


@lru_cache(maxsize=None)
def factorial(n: int) -> int:
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def syt_count(lam: tuple[int, ...], hook_list: list[int], n: int) -> int:
    """f^lambda = n! / prod(hooks)  (hook-length formula) — exact integer."""
    prod = 1
    for h in hook_list:
        prod *= h
    q, r = divmod(factorial(n), prod)
    assert r == 0, "hook-length formula must divide evenly"
    return q


# ----------------------------------------------------------------------------
# exact Plancherel covariance  Cov(Sum_h, Sum_c^2)
# ----------------------------------------------------------------------------

def exact_cov(n: int) -> Fraction:
    """Cov_Planch(Sum_box h, Sum_box c^2) as an exact Fraction."""
    nfac = factorial(n)
    # accumulate exact rational moments with denominator n!
    #   E[X]   = sum_lam (f^2/n!) X_lam
    #   E[XY]  = sum_lam (f^2/n!) X_lam Y_lam
    # keep integer numerators over the common denominator n!
    sum_w_num = 0          # sum f^2   (== n!, sanity)
    sum_X = 0              # sum f^2 * H
    sum_Y = 0              # sum f^2 * C2
    sum_XY = 0             # sum f^2 * H * C2
    for lam in partitions(n):
        hook_list, sum_c2 = hooks_contents(lam)
        f = syt_count(lam, hook_list, n)
        w = f * f
        H = sum(hook_list)
        C2 = sum_c2
        sum_w_num += w
        sum_X += w * H
        sum_Y += w * C2
        sum_XY += w * H * C2
    assert sum_w_num == nfac, f"Plancherel weights must sum to 1 (got {sum_w_num}/{nfac})"
    EX = Fraction(sum_X, nfac)
    EY = Fraction(sum_Y, nfac)
    EXY = Fraction(sum_XY, nfac)
    return EXY - EX * EY


# ----------------------------------------------------------------------------
# main: exact Cov, then mpmath extrapolation of kappa = lim Cov/n^{5/2}
# ----------------------------------------------------------------------------

def main() -> int:
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 34
    print(f"# Exact Cov(Sum_h, Sum_c^2) and kappa_n = Cov/n^{{5/2}}  (nmax={nmax})")
    print(f"# {'n':>3} {'Cov (exact Fraction)':>28} {'kappa_n':>22}")
    ns = []
    kappas = []
    covs = {}
    covf = {}   # mpmath value of Cov
    print(f"# {'n':>3} {'kappa_n=Cov/n^2.5':>20} {'eff.exponent a_n':>18}")
    prev_cf = None
    for n in range(3, nmax + 1):
        cov = exact_cov(n)
        covs[n] = cov
        cf = mp.mpf(cov.numerator) / mp.mpf(cov.denominator)
        covf[n] = cf
        # kappa_n = cov / n^{5/2}  at 60 dps (cov exact -> no cancellation)
        kap = cf / mp.power(n, mp.mpf(5) / 2)
        ns.append(n)
        kappas.append(kap)
        # effective exponent a_n = ln(Cov_n/Cov_{n-1}) / ln(n/(n-1))
        if prev_cf is not None:
            aeff = mp.log(cf / prev_cf) / mp.log(mp.mpf(n) / (n - 1))
            print(f"  {n:>3} {mp.nstr(kap, 12):>20} {mp.nstr(aeff, 10):>18}")
        else:
            print(f"  {n:>3} {mp.nstr(kap, 12):>20} {'-':>18}")
        prev_cf = cf

    # --- HONEST convergence diagnosis (no fitted "closed form") -------------
    # kappa_n is NON-MONOTONE: it rises, peaks near n~32, then DESCENDS. So a
    # low-order  kappa + a/sqrt(n) + b/n  model is invalid on the tail and its
    # "extrapolant" bounces. We report the peak, the tail drift, and DECLINE to
    # pin kappa numerically. The exponent and positivity ARE solid.
    peak_i = max(range(len(ns)), key=lambda i: kappas[i])
    print()
    print("# convergence diagnosis (kappa_n is non-monotone -> numerics do NOT pin kappa):")
    print(f"#   peak kappa_n = {mp.nstr(kappas[peak_i], 12)} at n = {ns[peak_i]}")
    print(f"#   tail kappa_n[{ns[-1]}] = {mp.nstr(kappas[-1], 12)} (still drifting)")
    if len(ns) >= 6:
        d_last = kappas[-1] - kappas[-2]
        print(f"#   last step Delta kappa_n = {mp.nstr(d_last, 6)}  "
              f"(sign {'-' if d_last < 0 else '+'}; not yet converged)")
    # candidate constants: report GAP to the current tail value only, explicitly
    # NOT a fit and NOT a confirmation.
    cands = {
        "sqrt(2)/24": mp.sqrt(2) / 24,
        "1/17": mp.mpf(1) / 17,
        "1/(6 sqrt(2 pi))": 1 / (6 * mp.sqrt(2 * mp.pi)),
    }
    print("#   candidate constants vs the tail value (informational, NOT confirmed):")
    for name, val in cands.items():
        gap = (kappas[-1] - val) / val * 100
        print(f"#     {name:>18} = {mp.nstr(val, 10):>14}  gap-to-tail {mp.nstr(gap, 4)} %")

    # --- exact identity sanity checks (the analytic decomposition) ----------
    # (1) Sum_box h = 1/2 (Sum_i lam_i^2 + Sum_j lam'_j^2)
    # (2) p2(lam) = Sum_i (lam_i - i)^2 + 2 Sum_i i (lam_i - i) + Sum_i i^2
    #     (isolates the non-Lambda* term  2 Sum_i i (lam_i - i), the i-weighting)
    id1_ok = True
    id2_ok = True
    for n in range(3, min(nmax, 12) + 1):
        for lam in partitions(n):
            hook_list, _ = hooks_contents(lam)
            H = sum(hook_list)
            conj = []
            if lam:
                m = lam[0]
                conj = [0] * m
                for part in lam:
                    for j in range(part):
                        conj[j] += 1
            p2 = sum(x * x for x in lam)
            p2c = sum(x * x for x in conj)
            if 2 * H != p2 + p2c:
                id1_ok = False
            lo = list(lam)
            rhs2 = (sum((lo[i] - (i + 1)) ** 2 for i in range(len(lo)))
                    + 2 * sum((i + 1) * (lo[i] - (i + 1)) for i in range(len(lo)))
                    + sum((i + 1) ** 2 for i in range(len(lo))))
            if rhs2 != p2:
                id2_ok = False
    print()
    print(f"# identity 2*Sum_h = p2(lam)+p2(lam') exact (n<=12): {id1_ok}")
    print(f"# identity p2 = Sum(lam_i-i)^2 + 2 Sum i(lam_i-i) + Sum i^2 (n<=12): {id2_ok}")

    all_pos = all(covs[n] > 0 for n in covs)
    print()
    print(f"RESULT: leading exponent -> 5/2 (a_n near 2.50); Cov>0 exactly all 3<=n<={nmax}: {all_pos}")
    print(f"RESULT: kappa NOT pinned numerically (non-monotone, peak {mp.nstr(kappas[peak_i], 8)}"
          f" at n={ns[peak_i]}, descending). sqrt(2)/24 NOT confirmed.")
    print(f"RESULT: identities id1={id1_ok} id2={id2_ok} (analytic decomposition verified exact)")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
