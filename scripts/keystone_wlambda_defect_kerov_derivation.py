#!/usr/bin/env python3
"""W_λ defect cubic C(n) — ANALYTIC derivation from Plancherel moments (Kerov route).

Closes the keystone ledger's deferred item: "C(n)'s derivation from the defect
stays deferred ... the h²-order moment collapse is not yet symbolic" (#2744).
Here C(n) is derived in closed form from Identity I — no Richardson/Taylor
extraction, no interpolation, no fit. Exact rational arithmetic.

Setup.  W_λ = [n]_q! / (∏_c [h_c]_q)²  (q-hook-length form of the q-Plancherel
weight; Σ_λ W_λ = Z(n), the defect is 1 − Z(n)). With q = e^η,
[m]_q = sinh(mη)/sinh(η), the log expands as

    log [m]_q = log m + (m²−1) η²/6 − (m⁴−1) η⁴/180 + …

so   log W_λ = log(dim(λ)²/n!) + A_λ η² + O(η⁴),
     A_λ = (1/6)[ Σ_{k=1}^n (k²−1) − 2 Σ_c (h_c²−1) ].

Since the q→1 weights w_λ = dim(λ)²/n! are the Plancherel measure (Σ_λ w_λ = 1),

    1 − Z(n) = −η² · Σ_λ w_λ A_λ + O(η⁴),
    Σ_λ w_λ A_λ = (1/6)[ Σ_k (k²−1) − 2(M(n) − n) ],   M(n) = Σ_λ w_λ Σ_c h_c².

M(n) is exactly **Identity I**, the Plancherel hook-square mean = n(3n−1)/2
(keystone, proved). With h = q − 1/q = 2 sinh η (so η² = h²/4 at leading order),
the coefficient of h² in 1 − Z(n) is

    C(n) = −(1/4) · Σ_λ w_λ A_λ = −n(n−1)(2n−13)/144,

reproducing the keystone defect cubic 144·C(n) = −n(n−1)(2n−13) — now DERIVED
from Identity I, not cross-checked numerically.

Higher rungs c_{2k}(n) follow the same recursion: the η^{2k} coefficient of
1 − Z(n) is a polynomial in the Plancherel content/hook power-sum moments
(Σ_λ w_λ Σ_c h_c^{2j}), assembled from the log-sinh coefficients and the exp
cross-terms — the Kerov-polynomial / free-cumulant expansion of the q-Plancherel
measure. This replaces the per-order Richardson/Taylor extraction in
keystone_wlambda_defect_coeff_ladder.py with a moment recursion.
"""
from fractions import Fraction as F
from math import factorial, prod


def partitions(n):
    def gen(m, mx):
        if m == 0:
            yield ()
            return
        for k in range(min(m, mx), 0, -1):
            for rest in gen(m - k, k):
                yield (k,) + rest
    return list(gen(n, n))


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    hs = []
    for i, row in enumerate(lam):
        for j in range(row):
            hs.append((row - j - 1) + (conj[j] - i - 1) + 1)
    return hs


def dim(lam, n):
    return F(factorial(n), prod(hooks(lam)))


def hooksq_plancherel_mean(n):  # M(n) = Σ_λ w_λ Σ_c h_c²
    tot = F(0)
    for lam in partitions(n):
        d = dim(lam, n)
        tot += d * d * F(sum(h * h for h in hooks(lam)))
    return tot / F(factorial(n))


def C_from_moments(n):
    Sk = sum(k * k - 1 for k in range(1, n + 1))
    M = hooksq_plancherel_mean(n)
    SwA = F(1, 6) * (F(Sk) - 2 * (M - n))
    return -F(1, 4) * SwA  # coefficient of h² in 1 − Z(n)


def main():
    hdr = f"{'n':>2} {'M(n)':>8} {'n(3n-1)/2':>10} {'C(n)':>10} {'-n(n-1)(2n-13)/144':>20} {'ok':>5}"
    print(hdr)
    ok_all = True
    for n in range(2, 13):
        M = hooksq_plancherel_mean(n)
        Mref = F(n * (3 * n - 1), 2)
        C = C_from_moments(n)
        Cref = F(-n * (n - 1) * (2 * n - 13), 144)
        ok = (M == Mref and C == Cref)
        ok_all = ok_all and ok
        print(f"{n:>2} {str(M):>8} {str(Mref):>10} {str(C):>10} {str(Cref):>20} {str(ok):>5}")
    assert ok_all, "moment-derived C(n) disagrees with the keystone cubic"
    print("\nVERDICT: C(n) = -n(n-1)(2n-13)/144 DERIVED from Identity I "
          "M(n)=n(3n-1)/2 via the Plancherel-moment route (no fit, no Taylor extraction).")


if __name__ == "__main__":
    main()
