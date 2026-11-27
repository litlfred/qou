#!/usr/bin/env python3
"""qbeta_thetak_mode_set_depth_probe.py — bean qou-8vt2: depth |Λ| of the q-heat-kernel recursion.

Companion to HeckeTemperleyLieb/QHeatKernelModeSet.lean.

The per-mode bracket g_λ(q) = Σ_{c∈λ} (q^c − q^{−c})² = Σ_c (q^{2c} + q^{−2c} − 2) is a Laurent
polynomial whose q^{2k} coefficient (k > 0) counts the cells with |content| = k. So g_λ, and
with it μ_λ = q^{−1/2} g_λ, depends exactly on the multiset {|c| : c ∈ λ}. Two λ ⊢ n give the
same exponential in Z_q(t) = Σ_λ d_λ exp_q(−μ_λ t) iff those multisets agree.

The Lean file proves conjugate partitions have equal rates. This probe counts, for
Λ = all λ ⊢ n, the number of DISTINCT rates (the depth of the q-difference equation), and
compares it with the number of conjugation classes.

Exact integer combinatorics; no anchor, no measured value.

Gates:
  G1  rates are conjugation-invariant (every n ≤ 20)
  G2  for n ≤ 7 the rates separate conjugation classes: |Λ| = 1,1,2,3,4,6,8
  G3  n = 8 is the first collision: |Λ| = 10 < 12 conjugation classes
  G4  n = 3: depth 2, with rates g_(3) = (q−q⁻¹)² + (q²−q⁻²)² and g_(2,1) = 2(q−q⁻¹)²
"""
from __future__ import annotations

import sys
from collections import Counter


def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for p in partitions(n - k, k):
            yield (k,) + p


def conjugate(p):
    return tuple(sum(1 for x in p if x > j) for j in range(p[0])) if p else ()


def rate_key(p):
    """g_λ as a Laurent polynomial in q^2: {k: coeff of q^{2k}} — exact, not sampled."""
    g = Counter()
    for i, r in enumerate(p):
        for j in range(r):
            c = j - i
            g[c] += 1
            g[-c] += 1
            g[0] -= 2
    return tuple(sorted((k, v) for k, v in g.items() if v))


def depth_table(nmax):
    rows = []
    for n in range(1, nmax + 1):
        P = list(partitions(n))
        classes = {frozenset([p, conjugate(p)]) for p in P}
        conj_ok = all(rate_key(p) == rate_key(conjugate(p)) for p in P)
        rates = {rate_key(p) for p in P}
        rows.append((n, len(P), len(classes), len(rates), conj_ok))
    return rows


def main() -> int:
    rows = depth_table(20)
    print(" n  |Irr H_n|  conj-classes  |Λ| distinct rates")
    for n, a, b, c, _ in rows:
        print(f"{n:2}  {a:8}  {b:12}  {c:6}")
    g3 = rate_key((3,))
    g21 = rate_key((2, 1))
    gates = [
        ("G1 conjugation-invariant, n ≤ 20", all(r[4] for r in rows)),
        ("G2 |Λ| = conj-classes = 1,1,2,3,4,6,8 for n ≤ 7",
         [r[3] for r in rows[:7]] == [1, 1, 2, 3, 4, 6, 8]
         and all(r[2] == r[3] for r in rows[:7])),
        ("G3 first collision at n = 8: 10 < 12", rows[7][2:4] == (12, 10)),
        # (q−q⁻¹)² + (q²−q⁻²)²  ->  q^{±2}: 1, q^{±4}: 1, q^0: −4
        ("G4 n = 3: two rates, (3) and (2,1)",
         rows[2][3] == 2 and g3 == ((-2, 1), (-1, 1), (0, -4), (1, 1), (2, 1))
         and g21 == ((-1, 2), (0, -4), (1, 2))),
    ]
    ok = True
    for name, g in gates:
        print(f"  [{'PASS' if g else 'FAIL'}] {name}")
        ok = ok and g
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
