#!/usr/bin/env python3
"""schlesinger_distribution_li2q_probe.py — bean qou-5zbn.

Cross-check of Schlesinger, "Some remarks on q-deformed multiple
polylogarithms" [schlesinger2001], library/arxiv-math-0111022v1/, Lemma 4,
against QOU's symmetric q-dilogarithm Li_2^q(z) = sum_{k>=1} z^k/(k [k]_q),
[k]_q = (q^k - q^-k)/(q - q^-1) (computations/_li_2_q_util.py::li_2_q).

PRE-REGISTERED (written before running):

  Source facts used (PDF text layer):
    S1  Li_n(z;q) = sum_{k>=1} z^k / (1 - q^k)^n  (Schlesinger's normalisation).
    S2  Lemma 4: Li_2(x, q^n) = (1/n) sum_{y^n = x} Li_2(y, q).

  Derivation to be tested (agent's, from S1-S2 and the QOU definition):
    sum_{y^n=x} y^k = n x^{k/n} if n | k, else 0, and [n m]_q = [n]_q [m]_{q^n}
    for the symmetric q-integer. Hence
      (D)  sum_{y^n = x} Li_2^q(y)  =  Li_2^{q^n}(x) / [n]_q,
    which at q = 1 is the classical n^{1-2} Li_2(x). The relation survives in
    the QOU normalisation, with 1/[n]_q in place of Schlesinger's n and the
    same base change q -> q^n.

  Checks (sympy exact for E; mpmath 60 dps elsewhere; q in {q0_proton, 3/2, 2}):
    E  [n m]_q = [n]_q [m]_{q^n} as rational functions, n, m = 1..6.
    A  (D) for x in {0.3, -0.7, 0.5+0.4i}, n = 2..5: rel < 1e-50.
    B  S2 in Schlesinger's normalisation, same x, n, at q in {1/2, 3/2}:
       rel < 1e-50 (control that the root sum is coded right).
    C  Decoy, the same-q form sum_y Li_2^q(y) = n^{-1} Li_2^q(x): must FAIL,
       rel > 1e-3 at q0, n = 5, x = 0.3.
    D  Orbit sum at x = 1, N = 5 (all |zeta^k| = 1 < q, series converges):
       sum_{k=1}^{4} Li_2^q(zeta_5^k) = Li_2^{q^5}(1)/[5]_q - Li_2^q(1),
       rel < 1e-50. Reported, not gated: the ratio of the LHS to Li_2^q(1)
       against the classical constant 5^{-1} - 1 = -4/5.
    PASS iff E, A, B, C, D.

  Premise check (read before running): prop:cl3-zeta5-orbit-sum-identity is
  the classical (q = 1) Li_3 multiplication formula. It contains no q, so
  neither normalisation's deformation enters that proposition; this probe tests
  the bean's question about the q-analogue only.

Run: python3 -u computations/probes/schlesinger_distribution_li2q_probe.py
"""
from __future__ import annotations

import sys

import mpmath as mp
import sympy as sp

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)) + "/..")


def qint(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def li2q(z, q, eps):
    tot, zp, k = mp.mpc(0), mp.mpc(1), 0
    while True:
        k += 1
        zp *= z
        term = zp / (k * qint(k, q))
        tot += term
        if abs(term) < eps and k > 5:
            return tot


def li2s(z, q, eps):
    tot, zp, k = mp.mpc(0), mp.mpc(1), 0
    while True:
        k += 1
        zp *= z
        term = zp / (1 - q ** k) ** 2
        tot += term
        if abs(term) < eps and k > 5:
            return tot


def roots(x, n):
    r = mp.root(x, n)
    return [r * mp.expjpi(2 * mp.mpf(j) / n) for j in range(n)]


def rel(a, b):
    return abs(a - b) / abs(b)


def main() -> int:
    mp.mp.dps = 60
    eps = mp.mpf(10) ** -70
    tol = mp.mpf(10) ** -50
    # E
    Q = sp.symbols("q", positive=True)
    qi = lambda k, b: (b ** k - b ** (-k)) / (b - 1 / b)
    e_ok = all(sp.simplify(qi(n * m, Q) - qi(n, Q) * qi(m, Q ** n)) == 0
               for n in range(1, 7) for m in range(1, 7))
    print(f"E  [nm]_q = [n]_q [m]_(q^n), n,m = 1..6: {e_ok}")
    from qou_substrate.constants import Q_50_DIGIT_STR
    q0 = mp.mpf(Q_50_DIGIT_STR)
    qs = [q0, mp.mpf(3) / 2, mp.mpf(2)]
    xs = [mp.mpf(3) / 10, -mp.mpf(7) / 10, mp.mpc(mp.mpf(1) / 2, mp.mpf(2) / 5)]
    worst = mp.mpf(0)
    for q in qs:
        for x in xs:
            for n in range(2, 6):
                lhs = sum(li2q(y, q, eps) for y in roots(x, n))
                rhs = li2q(x, q ** n, eps) / qint(n, q)
                worst = max(worst, rel(lhs, rhs))
    a_ok = worst < tol
    print(f"A  sum_y Li2^q(y) = Li2^(q^n)(x)/[n]_q, worst rel {mp.nstr(worst, 3)}: {a_ok}")
    worst = mp.mpf(0)
    for q in (mp.mpf(1) / 2, mp.mpf(3) / 2):
        for x in xs:
            for n in range(2, 6):
                lhs = sum(li2s(y, q, eps) for y in roots(x, n)) / n
                rhs = li2s(x, q ** n, eps)
                worst = max(worst, rel(lhs, rhs))
    b_ok = worst < tol
    print(f"B  Schlesinger Lemma 4, worst rel {mp.nstr(worst, 3)}: {b_ok}")
    x = mp.mpf(3) / 10
    lhs = sum(li2q(y, q0, eps) for y in roots(x, 5))
    dec = rel(lhs, li2q(x, q0, eps) / 5)
    c_ok = dec > mp.mpf(10) ** -3
    print(f"C  decoy same-q form at q0, n=5: rel {mp.nstr(dec, 6)} (must exceed 1e-3): {c_ok}")
    z5 = mp.expjpi(mp.mpf(2) / 5)
    orb = sum(li2q(z5 ** k, q0, eps) for k in range(1, 5))
    one = li2q(mp.mpf(1), q0, eps)
    pred = li2q(mp.mpf(1), q0 ** 5, eps) / qint(5, q0) - one
    d_rel = rel(orb, pred)
    d_ok = d_rel < tol
    print(f"D  N=5 orbit sum at q0 = {mp.nstr(orb, 20)}, predicted {mp.nstr(pred, 20)}, rel {mp.nstr(d_rel, 3)}: {d_ok}")
    print(f"   ratio to Li2^q(1): {mp.nstr(orb / one, 15)}  (classical q=1 constant -4/5)")
    ok = e_ok and a_ok and b_ok and c_ok and d_ok
    print("ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
