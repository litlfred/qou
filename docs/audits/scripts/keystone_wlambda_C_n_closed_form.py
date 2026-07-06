#!/usr/bin/env python3
"""Closed form for the W_lambda defect's small-h coefficient C(n), and the
EXACT explanation of the sign change at n = 7.

Follows the merged probe `keystone_wlambda_Z_defect_n_scaling.py` (PR #2525),
which found 1 - Z(n) = C(n) h^2 + O(h^4) with empirical 24*C(n) for n = 2..8:
3, 7, 10, 10, 5, -7, -28 -- and left C(n) as an UNIDENTIFIED empirical sequence
(a hook-moment guess had been refuted).

This script DERIVES and verifies the closed form.

Derivation (pure perturbation theory; no fit, no correspondence chain)
----------------------------------------------------------------------
Put q = e^{x/2}, so [m]_q = sinh(m x/2)/sinh(x/2) = m[1 + (m^2-1)x^2/24 + O(x^4)]
and h = q - q^{-1} = 2 sinh(x/2), h^2 = x^2 + O(x^4).

  d_q(lambda) = [n]_q! / prod_cells [h_c]_q
              = dim(lambda) * [1 + (x^2/24)(S_n - T_lambda) + O(x^4)],
  where dim(lambda) = n!/prod h_c   (q=1 hook-length formula),
        S_n     = sum_{k=1}^n (k^2 - 1),
        T_lambda = sum_{cells c in lambda} (h_c^2 - 1).

Since Z(n) = (1/[n]_q!) sum_lambda d_q(lambda)^2 and sum_lambda dim^2 = n!,

  1 - Z(n) = (h^2/24) [ (2/n!) sum_lambda dim(lambda)^2 sum_c h_c^2  -  S_n ] + O(h^4).

The bracket needs the Plancherel-expected squared-hook sum
  M(n) := (1/n!) sum_{lambda |- n} dim(lambda)^2 sum_{c in lambda} h_c^2.
This script verifies (exact integer arithmetic) the closed form

  M(n) = n(3n - 1)/2.                                   (identity I)

Substituting M(n) and S_n = n(n+1)(2n+1)/6 - n collapses the bracket to

  24 C(n) = -n(n-1)(2n-13)/6,    i.e.   C(n) = -n(n-1)(2n-13)/144.   (closed form)

The SIGN CHANGE is now exact: 24 C(n) = -(n)(n-1)(2n-13)/6 has integer roots'
neighbour at 2n - 13 = 0  =>  n = 6.5, so C(n) > 0 for 2 <= n <= 6 and C(n) < 0
for n >= 7.  The n=7 sign flip found numerically in #2525 is the factor (2n-13)
crossing zero between n=6 and n=7 -- not an artifact.

Verification (this script)
--------------------------
  (A) identity I:  M(n) = n(3n-1)/2  exactly, n = 2..14  (rational/integer).
  (B) closed form: 24 C(n) = -n(n-1)(2n-13)/6 matches the high-precision
      finite-difference C_emp(n) = (1 - Z(n,q))/h^2 as h -> 0, n = 2..12.
  (C) sign: C(n) > 0 for 2<=n<=6, = 0 has no integer root (n=6.5), < 0 for n>=7.

No fit; q_0 and 210 ppb are never used (C(n) is q-independent leading data).
"""
import sys
from fractions import Fraction
from math import factorial

import mpmath as mp

mp.mp.dps = 60


# ----- exact (q = 1) combinatorics -----
def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, mx), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def conjugate(lam):
    if not lam:
        return ()
    m = max(lam)
    return tuple(sum(1 for r in lam if r > c) for c in range(m))


def hooks(lam):
    lamp = conjugate(lam)
    hs = []
    for i, row in enumerate(lam):
        for j in range(row):
            hs.append((row - j - 1) + (lamp[j] - i - 1) + 1)
    return hs


def dim(lam):
    n = sum(lam)
    prod = 1
    for h in hooks(lam):
        prod *= h
    return factorial(n) // prod


def M_exact(n):
    """M(n) = (1/n!) sum_lambda dim(lambda)^2 sum_cells h^2  (exact Fraction)."""
    tot = 0
    for lam in partitions(n):
        d = dim(lam)
        tot += d * d * sum(h * h for h in hooks(lam))
    return Fraction(tot, factorial(n))


def C_closed(n):
    """24*C(n) closed form = -n(n-1)(2n-13)/6  (exact Fraction)."""
    return Fraction(-n * (n - 1) * (2 * n - 13), 6)


# ----- high-precision numeric Z(n) for the finite-difference cross-check -----
def qint(m, q):
    if q == 1:
        return mp.mpf(m)
    return (q**m - q**(-m)) / (q - q**(-1))


def qfact(n, q):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint(k, q)
    return r


def qdim(lam, q):
    denom = mp.mpf(1)
    for h in hooks(lam):
        denom *= qint(h, q)
    return qfact(sum(lam), q) / denom


def Z(n, q):
    fact = qfact(n, q)
    return sum(qdim(lam, q)**2 / fact for lam in partitions(n))


def C_emp(n):
    """(1 - Z(n,q))/h^2 at tiny h (-> C(n))."""
    h = mp.mpf("1e-6")
    q = (h + mp.sqrt(h**2 + 4)) / 2          # solve q - 1/q = h
    return (1 - Z(n, q)) / h**2


def main():
    print("Closed form for the W_lambda defect coefficient C(n)")
    print("=" * 64)

    # (A) identity I: M(n) = n(3n-1)/2
    print("\n(A) Plancherel squared-hook mean  M(n) = (1/n!) sum dim^2 sum h^2")
    print(f"{'n':>3}{'M(n) exact':>14}{'n(3n-1)/2':>14}{'match':>8}")
    idA = True
    for n in range(2, 15):
        m = M_exact(n)
        cf = Fraction(n * (3 * n - 1), 2)
        ok = (m == cf)
        idA = idA and ok
        print(f"{n:>3}{str(m):>14}{str(cf):>14}{('OK' if ok else 'FAIL'):>8}")

    # (B) closed form vs finite-difference C_emp
    print("\n(B) 24*C(n):  closed form  -n(n-1)(2n-13)/6   vs   numeric (1-Z)/h^2")
    print(f"{'n':>3}{'24*C closed':>14}{'24*C_emp':>18}{'|err|':>12}")
    idB = True
    for n in range(2, 13):
        closed = C_closed(n)                       # = 24*C(n)
        emp24 = 24 * C_emp(n)
        err = abs(mp.mpf(closed.numerator) / closed.denominator - emp24)
        ok = err < mp.mpf("1e-6")
        idB = idB and ok
        print(f"{n:>3}{str(closed):>14}{mp.nstr(emp24, 11):>18}{mp.nstr(err, 3):>12}")

    # (C) sign pattern
    print("\n(C) sign of C(n) = -(n)(n-1)(2n-13)/144  (root of 2n-13 at n=6.5)")
    signs = {n: (1 if C_closed(n) > 0 else (-1 if C_closed(n) < 0 else 0))
             for n in range(2, 11)}
    pos = [n for n in signs if signs[n] > 0]
    neg = [n for n in signs if signs[n] < 0]
    print(f"    C(n) > 0 for n in {pos}")
    print(f"    C(n) < 0 for n in {neg}")
    idC = (pos == [2, 3, 4, 5, 6]) and (min(neg) == 7)

    print("\n--- SELF-CHECKS ---")
    print(f"  (A) M(n) = n(3n-1)/2 exact (n=2..14)        : {'PASS' if idA else 'FAIL'}")
    print(f"  (B) 24C(n) = -n(n-1)(2n-13)/6 (n=2..12)      : {'PASS' if idB else 'FAIL'}")
    print(f"  (C) sign flip exactly at n=7 (2n-13 root 6.5): {'PASS' if idC else 'FAIL'}")

    print("\n--- RESULT ---")
    print("  1 - Z(n) = -[ n(n-1)(2n-13)/144 ] h^2 + O(h^4).")
    print("  The empirical sequence 24C(n) = 3,7,10,10,5,-7,-28 (#2525) is exactly")
    print("  -n(n-1)(2n-13)/6.  The n=7 sign change is the linear factor (2n-13)")
    print("  vanishing at n=6.5 -- a PROVED structural feature, not an artifact.")
    print("  Key lemma: the Plancherel mean of sum_cells h^2 is n(3n-1)/2.")
    print("  => the q-Bessel/heat-kernel target (#2503) is now a closed formula,")
    print("     not an empirical table: any S^1-equivariant index realizing W_lambda")
    print("     must reproduce the sub-leading coefficient -n(n-1)(2n-13)/144.")
    print("  Bar-even (h^2) => still cannot be the bar-odd 210 ppb shift. No fit.")

    all_ok = idA and idB and idC
    print("\nALL CHECKS PASS." if all_ok else "\nSELF-CHECK FAILED.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
