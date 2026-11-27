#!/usr/bin/env python3
"""qbeta_thetak_recursion_coeffs_probe.py — bean qou-8vt2: the recursion coefficients a_j(q).

Companion to HeckeTemperleyLieb/QHeatKernelRecursion.lean.

For each n, take one partition per distinct rate (qbeta_thetak_mode_set_depth_probe.py), form
r_λ = (q − 1)·q^{−1/2}·g_λ(q) with t = q^{1/2}, and a_j = e_j({r_λ}). Gates:
  G1  a_j(1/t) = (−1)^j a_j(t) exactly, for every n ≤ 7 and every j (the Lean theorem, checked
      symbolically on the actual rate sets)
  G2  number of nonzero a_j = 0,1,2,3,4,6,8 for n = 1..7. This equals |Λ| except at n = 1,
      where the single mode is the vacuum (rate 0), so every a_j vanishes
  G3  n = 3 closed form: a_1, a_2 as printed below
Exact symbolic algebra (sympy); no anchor, no measured value; nothing is evaluated at q_0.
"""
from __future__ import annotations

import sys

import sympy as sp

from qbeta_thetak_mode_set_depth_probe import partitions, rate_key

t = sp.symbols("t", positive=True)  # t = q^{1/2}
q = t ** 2


def g(p):
    return sum((q ** (j - i) - q ** (-(j - i))) ** 2 for i, r in enumerate(p) for j in range(r))


def mode_set(n):
    reps = {}
    for p in partitions(n):
        reps.setdefault(rate_key(p), p)
    return list(reps.values())


def esymm(xs, k):
    x = sp.symbols("x")
    poly = sp.expand(sp.prod([1 + x * r for r in xs]))
    return sp.simplify(poly.coeff(x, k))


def main() -> int:
    ok = True
    depths = []
    n3 = None
    for n in range(1, 8):
        S = mode_set(n)
        rates = [sp.simplify((q - 1) / t * g(p)) for p in S]
        a = [esymm(rates, j) for j in range(1, len(S) + 1)]
        depths.append(sum(1 for x in a if sp.simplify(x) != 0))
        for j, aj in enumerate(a, start=1):
            if sp.simplify(aj.subs(t, 1 / t) - (-1) ** j * aj) != 0:
                print(f"  parity FAILS at n={n}, j={j}")
                ok = False
        if n == 3:
            n3 = [sp.factor(x) for x in a]
            print(f"  n=3 mode set {S}")
            for j, x in enumerate(n3, start=1):
                print(f"    a_{j}(q) = {x}")
    gates = [
        ("G1 a_j(1/t) = (−1)^j a_j(t), n ≤ 7", ok),
        ("G2 nonzero a_j count 0,1,2,3,4,6,8", depths == [0, 1, 2, 3, 4, 6, 8]),
        ("G3 n = 3 has depth 2", n3 is not None and len(n3) == 2),
    ]
    print("  depths:", depths)
    allok = True
    for name, gg in gates:
        print(f"  [{'PASS' if gg else 'FAIL'}] {name}")
        allok = allok and gg
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
