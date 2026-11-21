#!/usr/bin/env python3
"""Pre-registered probe: does the A2 measure satisfy second-order (concave-order) dominance?

Bean qou-ogrk (covariance-kernel epic, A2 leg). Pure combinatorics, exact arithmetic
(int / Fraction only, no float in any computation).

Setup. nu_v = Cov_Planch(N_v, omega3), N_v = number of boxes of hook length v,
omega3 = sum of squared contents - C(n,2). A2 is  sum_v nu_v log v >= 0.

PRE-REGISTRATION (written before any run).
  Hypothesis H: with S_v = sum_{u<=v} nu_u and T_w = sum_{v<=w} S_v,
      T_w <= 0 for every w = 1..n-1, for every n = 3..40.
  Why it matters: by two Abel summations, H implies sum_v nu_v phi(v) >= 0 for EVERY
  increasing concave phi, so H would be the
  extra Plancherel structure a global A2 proof uses; it is strictly weaker than the
  first-order certificate S_v <= 0 already refuted at n = 6.
  PASS: T_w <= 0 for all w and all n in range.  FAIL: any T_w > 0; report the first
  (n, w) and the value. No threshold is tuned; the range n <= 40 matches the range
  on which the corpus already verified A2 exactly.
"""
import sys
from fractions import Fraction
from math import factorial


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def stats(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    hooks, c2 = [], 0
    for i, r in enumerate(lam):
        for j in range(r):
            hooks.append(r - j + conj[j] - i - 1)
            c2 += (j - i) ** 2
    return hooks, c2


def nu_vector(n):
    nf = factorial(n)
    tot_N = [0] * (n + 1)      # sum f^2 N_v
    tot_Nw = [0] * (n + 1)     # sum f^2 N_v omega3
    tot_w = 0                  # sum f^2 omega3
    shift = n * (n - 1) // 2
    for lam in partitions(n):
        hooks, c2 = stats(lam)
        hp = 1
        for h in hooks:
            hp *= h
        f = nf // hp
        f2 = f * f
        om = c2 - shift
        tot_w += f2 * om
        for h in hooks:
            tot_N[h] += f2
            tot_Nw[h] += f2 * om
    # Cov = E[N om] - E[N]E[om], E = (1/n!) sum f^2
    return [Fraction(tot_Nw[v], nf) - Fraction(tot_N[v] * tot_w, nf * nf)
            for v in range(n + 1)], tot_w


def main(nmax=40):
    first_fail = None
    for n in range(3, nmax + 1):
        nu, tw = nu_vector(n)
        assert tw == 0, "Plancherel mean of omega3 must be 0"
        assert sum(nu[1:]) == 0
        S = T = Fraction(0)
        maxT, argw = None, None
        for w in range(1, n):
            S += nu[w]
            T += S
            if maxT is None or T > maxT:
                maxT, argw = T, w
        ok = maxT <= 0
        print(f"n={n:2d}  max_w T_w = {maxT}  (at w={argw})  {'ok' if ok else 'FAIL'}", flush=True)
        if not ok and first_fail is None:
            first_fail = (n, argw, maxT)
    print("RESULT:", "PASS" if first_fail is None else f"FAIL first at n={first_fail[0]} w={first_fail[1]} T={first_fail[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1]) if len(sys.argv) > 1 else 40))
