#!/usr/bin/env python3
"""
EM coupling bar-parity probe (bean qou-pibu) — the taxonomy's last cell,
measured and decomposed exactly.

The EM coupling object is alpha_EM^-1 = q0 * [9]_q * [10]_q (bare), CS-tower
dressed. Under the bar involution q -> 1/q:

  * [n]_q = (q^n - q^-n)/(q - q^-1) is BAR-EVEN (invariant): numerator and
    denominator each flip sign. Verified here numerically to working
    precision at the proton pin; proved generically in
    lean/QOU/Interactions/EmCouplingBarParity.lean.
  * the prefactor q is the full exponential e^lambda (lambda = ln q): neither
    even nor odd. So the BARE EM coupling decomposes exactly as

        C(q) = q*B = cosh(lambda)*B + sinh(lambda)*B,   B = [9]_q [10]_q

    an exact even+odd mix with odd/even ratio tanh(lambda) — the EM sector
    sits at the intertwiner point between the strong (cosh) and weak (sinh)
    channels rather than in either pure channel.
  * the CS tower is NOT bar-covariant in a single parity (hbar_q^2 = (1-1/q)^2
    maps to q^2*hbar_q^2); the corrected coupling's even/odd split is
    reported numerically.

Scope: this derives the bar decomposition of the COUPLING OBJECT. The bar
parity of the EM sector's primary *observable* remains open; the taxonomy's
`parity .electromagnetic = none` is unchanged (see the block's .md).
mpmath end-to-end at 60 dps; no witness (probe); conclusions in the
interaction-sector-taxonomy block + bean qou-pibu.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "substrate"))

from mpmath import mp, mpf  # noqa: E402

mp.dps = 60

from q_parameter import Q_50_DIGIT_STR  # noqa: E402

Q0 = mpf(Q_50_DIGIT_STR)
QI = 1 / Q0


def qint(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def main() -> int:
    ok = True
    print("EM COUPLING BAR-PARITY — exact decomposition at the proton pin")

    # 1. [n]_q bar-invariance (numeric confirmation of the Lean lemma)
    for n in (9, 10):
        a, b = qint(n, Q0), qint(n, QI)
        rel = abs(a - b) / abs(a)
        print(f"  [{n}]_q bar-invariance: rel drift {mp.nstr(rel, 3)}")
        ok &= rel < mpf("1e-55")

    B = qint(9, Q0) * qint(10, Q0)
    C, Cbar = Q0 * B, QI * B
    even, odd = (C + Cbar) / 2, (C - Cbar) / 2
    lam = mp.log(Q0)
    print(f"  bare coupling C = q*[9][10] = {mp.nstr(C, 15)}")
    print(f"  even part (cosh·B) = {mp.nstr(even, 15)}   odd part (sinh·B) = {mp.nstr(odd, 15)}")
    print(f"  odd/even = {mp.nstr(odd / even, 12)}   tanh(ln q0) = {mp.nstr(mp.tanh(lam), 12)}")
    ok &= abs(odd / even - mp.tanh(lam)) < mpf("1e-55")
    ok &= abs(even - mp.cosh(lam) * B) < mpf("1e-50")
    ok &= abs(odd - mp.sinh(lam) * B) < mpf("1e-50")

    # 2. CS tower is not bar-covariant in one parity: hbar^2 -> q^2 hbar^2
    hb2, hb2bar = (1 - QI) ** 2, (1 - Q0) ** 2
    print(f"  hbar_q^2 bar-map factor: {mp.nstr(hb2bar / hb2, 12)}  (= q0^2 = {mp.nstr(Q0**2, 12)})")
    ok &= abs(hb2bar / hb2 - Q0 ** 2) < mpf("1e-55")

    # 3. corrected coupling both ways (full tower recomputed at q and 1/q)
    def alpha_inv(q):
        pi = mp.pi
        bare = q * qint(9, q) * qint(10, q)
        cs29, cs35 = pi ** 2 * mpf(10) / 9, pi ** 2 * mpf(16) / 15
        n2 = qint(2, q)
        c1 = (cs29 + cs35) * (n2 / 2) * (1 - 1 / q) ** 2 / bare
        g11 = cs29 + pi ** 2 * 64 / mpf(18) ** 2
        g22 = cs35 + pi ** 2 * 64 / mpf(15) ** 2
        g12 = pi ** 2 * 289 / (mpf(18) * 15)
        det_cl = g11 * g22 - g12 ** 2
        lk = abs(n2 * qint(5, q) - qint(3, q) * qint(9, q))
        cq29 = pi ** 2 * (n2 ** 2 - 1) * (qint(9, q) ** 2 - 1) / (12 * n2 * qint(9, q))
        cq35 = pi ** 2 * (qint(3, q) ** 2 - 1) * (qint(5, q) ** 2 - 1) / (12 * qint(3, q) * qint(5, q))
        s29, s35 = (n2 - 1) * (qint(9, q) - 1), (qint(3, q) - 1) * (qint(5, q) - 1)
        gq11 = cq29 + pi ** 2 * s29 ** 2 / (n2 * qint(9, q)) ** 2
        gq22 = cq35 + pi ** 2 * s35 ** 2 / (qint(3, q) * qint(5, q)) ** 2
        gq12 = pi ** 2 * lk ** 2 / (n2 * qint(9, q) * qint(3, q) * qint(5, q))
        det_q = gq11 * gq22 - gq12 ** 2
        kappa = det_cl / det_q
        return bare * (1 + c1 / (1 - c1 * kappa))

    ai, aib = alpha_inv(Q0), alpha_inv(QI)
    ev, od = (ai + aib) / 2, (ai - aib) / 2
    print(f"  corrected 1/alpha: at q0 {mp.nstr(ai, 14)}  at 1/q0 {mp.nstr(aib, 14)}")
    print(f"  corrected odd/even = {mp.nstr(od / ev, 10)}  (bare tanh = {mp.nstr(mp.tanh(lam), 10)})")

    print(f"\nRESULT: {'PASS' if ok else 'FAIL'} — EM coupling = e^lambda * (bar-even B): "
          "an exact cosh+sinh mix, not a pure channel")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
