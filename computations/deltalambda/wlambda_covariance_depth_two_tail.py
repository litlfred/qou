#!/usr/bin/env python3
"""Depth-2 tail of the covariance-kernel hook spectrum, nu_{n-2}(n) = Cov_Planch(N_{n-2}, omega_3).

Three independent evaluations, exact Fraction arithmetic, no float:
  1. brute force over all partitions of n (hook-length formula, contents);
  2. the one-family k-sum  (2/n!) * sum_{k=0}^{n} f_k^2 * omega_3(k),
     f_k = (n-k-2)(k-1)(k-2) C(n,k) / (2(n-2)), shape (n-k, 3, 1^{k-3}) and its boundary terms;
  3. the closed form (n-2)(n-5) Q(n) C(2n-8,n-4) / (6 (n-3) n!).
Sign onset n_2 = 10 is proved in Lean (YoungDiagramTailThirdInstance.nuDepthTwo_pos_iff).
Audit: docs/audits/2026-11-27-covariance-kernel-depth-two-tail.md.  No fit; nothing wired.
"""
from fractions import Fraction as F
from math import comb, factorial
import sys


def parts(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for p in parts(n - k, k):
            yield (k,) + p


def brute(n):
    tot = F(0)
    for l in parts(n):
        lc = [sum(1 for r in l if r > j) for j in range(l[0])]
        hs = [(r - j - 1) + (lc[j] - i - 1) + 1 for i, r in enumerate(l) for j in range(r)]
        hp = 1
        for h in hs:
            hp *= h
        f = factorial(n) // hp
        w = sum((j - i) ** 2 for i, r in enumerate(l) for j in range(r)) - comb(n, 2)
        tot += F(f * f, factorial(n)) * hs.count(n - 2) * w
    return tot  # E[omega_3] = 0, so no centring


def ksum(n):
    s = F(0)
    for k in range(n + 1):
        a, b = n - k, k - 3
        f = F((n - k - 2) * (k - 1) * (k - 2) * comb(n, k), 2 * (n - 2))
        om = F((a - 1) * a * (2 * a - 1), 6) + 2 + F((b + 1) * (b + 2) * (2 * b + 3), 6) - 1 - F(n * (n - 1), 2)
        s += f * f * om
    return 2 * s / factorial(n)


def Q(n):
    return n**6 - 25 * n**5 + 235 * n**4 - 1067 * n**3 + 2528 * n**2 - 3112 * n + 1680


def closed(n):
    return F((n - 2) * (n - 5) * Q(n) * comb(2 * n - 8, n - 4), 6 * (n - 3) * factorial(n))


def main(nmax=26):
    rows, ok = [], True
    for n in range(4, nmax + 1):
        b, k, c = brute(n), ksum(n), closed(n)
        good = b == k == c
        ok = ok and good
        rows.append({"n": n, "nu": str(b), "sign": (b > 0) - (b < 0), "agree": good})
        print(f"{n} | nu = {b} | agree: {good}", flush=True)
    onset_ok = all((r["sign"] > 0) == (r["n"] == 6 or r["n"] >= 10) for r in rows)
    print(f"RESULT: brute == k-sum == closed form n=4..{nmax}: {ok}; sign pattern: {onset_ok}")
    ok = ok and onset_ok
    try:
        sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[1] / "substrate"))
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-depth-two-tail", engine="python-exact")
        w.set_description(
            "Depth-2 tail nu_{n-2}(n) = Cov_Planch(N_{n-2}, omega_3) = (n-2)(n-5)Q(n)C(2n-8,n-4)/(6(n-3)n!), "
            "Q = n^6-25n^5+235n^4-1067n^3+2528n^2-3112n+1680. Brute force, one-family k-sum and "
            "closed form agree exactly. Sign onset n_2 = 10 (Lean, sorry-free). The closed-form "
            "identity itself is not formalized. No fit; nothing wired.")
        w.add_data("rows", rows)
        w.add_assertion("depth_two_tail_closed_form", computed=str(int(ok)), expected="1", tolerance=0,
                        source=f"brute vs k-sum vs closed form, n=4..{nmax}")
        print(f"Witness: {w.save()}")
    except ImportError as e:
        print(f"(witness skipped — witness_base unavailable: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
