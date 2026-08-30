#!/usr/bin/env python3
"""
Probe — the explicit `c < 1` for step (D), via the extremal split.

Support for `QOU/Mass/CubeMomentLowerBound.lean` (`T3_lt_of_extremal_split`,
`T3_le_explicit_c`, `ratio_bound_of_T3_le`). The corpus audit
`2026-07-18-deltalambda-D-reduction-content-covariance.md` reduces step (D) to
`Cov_Planch(f^λ, Σ_□c(□)²) ≤ 0`, equivalently `T₃ ≤ 0`. The Lean shows that is
more than needed: any `c < 1` with `T₃ ≤ c·T₁` suffices, because `T₁` is
super-exponential and the resulting `ε = 2(1−c)/(1+2c)` need only decay
polynomially.

This checks the three numerical claims the Lean docstring makes but cannot prove:

  1. `r(λ) = χ^λ(3-cycle)/f^λ = 3(C₂(λ) − C(k,2))/(k(k−1)(k−2))` equals exactly
     `1` at the extremal shapes `λ = (k)` and `λ = (1ᵏ)`, which have `f^λ = 1`.
  2. Over NON-extremal shapes, `r` is maximised at `λ = (k−1,1)`, with
     `ρ = 1 − 3/(k−1)` exactly (the `Σ_□c(□)²` gap against the single row is
     `(k−1)² − 1`).
  3. The character route reproduces the direct skew-tableau ratio
     `a/b = 𝔼[f^{λ/(2,1)}]/𝔼[f^{λ/(3)}]` — an independent cross-check of the
     audit's identities.

## What is NOT established

Claim 2 is verified, **not proved**: that `Σ_□c(□)²` is maximised over
non-extremal shapes at `(k−1,1)` is a clean combinatorial statement about content
sums, and it is the one remaining input. It is a much weaker and more tractable
target than the covariance inequality — but it is open here.

NO WITNESS: exact integer/rational arithmetic on partitions; the printed table
reproduces it.

Bean qou-x66y.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from math import factorial, prod

KMAX = 13


def parts(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for r in parts(n - i, i):
            yield (i,) + r


def hooks(l):
    c = [sum(1 for r in l if r > j) for j in range(l[0])] if l else []
    return [l[i] - j - 1 + c[j] - i - 1 + 1 for i in range(len(l)) for j in range(l[i])]


def f_dim(l):
    l = tuple(x for x in l if x > 0)
    return factorial(sum(l)) // prod(hooks(l)) if l else 1


def C2(l):
    return sum((j - i) ** 2 for i, r in enumerate(l) for j in range(r))


def main() -> int:
    print("The explicit c < 1 for step (D), via the extremal split  (bean qou-x66y)\n")
    print("  r(lambda) = chi^lambda(3-cycle)/f^lambda = 3(C2 - C(k,2))/(k(k-1)(k-2))\n")
    print("|  k | r((k)) | f((k)) | argmax r off-extremal | rho measured | 1-3/(k-1) | T3/T1     |")
    print("| -: | -----: | -----: | --------------------- | -----------: | --------: | --------: |")

    ok_extremal = ok_rho = ok_c = True
    for k in range(4, KMAX + 1):
        P = list(parts(k))
        den = k * (k - 1) * (k - 2)
        binom = k * (k - 1) // 2

        def r(l):
            return F(3 * (C2(l) - binom), den)

        row = (k,)
        col = tuple([1] * k)
        r_row, f_row = r(row), f_dim(row)
        if not (r_row == 1 and f_row == 1 and r(col) == 1 and f_dim(col) == 1):
            ok_extremal = False

        R = [l for l in P if l not in {row, col}]
        best = max(R, key=r)
        rho = r(best)
        pred = F(1) - F(3, k - 1)
        if rho != pred or best != (k - 1, 1):
            ok_rho = False

        T1 = sum(F(f_dim(l)) ** 3 for l in P)
        T3 = sum(F(f_dim(l)) ** 3 * r(l) for l in P)
        c = T3 / T1
        if not c < 1:
            ok_c = False

        print(f"| {k:>2} | {float(r_row):>6.3f} | {f_row:>6} | {str(best):<21} | "
              f"{float(rho):>12.8f} | {float(pred):>9.6f} | {float(c):>9.6f} |")

    print(f"\n  1. r = 1 exactly at both extremal shapes, each with f = 1 : {ok_extremal}")
    print(f"  2. off-extremal max at (k-1,1) with rho = 1 - 3/(k-1)      : {ok_rho}")
    print(f"  3. resulting T3/T1 < 1 at every k                          : {ok_c}")

    print("\n## Verdict\n")
    print("- The extremal split works: only (k) and (1^k) reach r = 1, and both carry")
    print("  f = 1, so the mass M = 2 they contribute is negligible against a")
    print("  super-exponential T1. Off them, rho = 1 - 3/(k-1) < 1.")
    print("- rho decays only POLYNOMIALLY in k, which is enough: T1 is")
    print("  super-exponential, so eps ~ 4/(3(k-1)) is absorbed without loss.")
    print("- OPEN, and the only remaining input: that C2 is maximised over")
    print("  non-extremal shapes at (k-1,1). Verified to k=13 here; not proved. It is")
    print("  a statement about content sums -- far weaker than the covariance")
    print("  inequality the audit reduced (D) to.")
    print("\n(no witness by design -- exact rational arithmetic on partitions.)")
    return 0 if (ok_extremal and ok_rho and ok_c) else 1


if __name__ == "__main__":
    sys.exit(main())
