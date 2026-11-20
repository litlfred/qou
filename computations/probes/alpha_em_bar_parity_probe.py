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

Scope (extended, bean qou-z2xz): coupling AND observable level. alpha
carries e^-lambda and alpha^2 (the Hartree q-dependence) e^-2lambda; under
nondegeneracy the coupling is provably NEITHER bar-even NOR bar-odd (Lean:
emCouplingBare_not_bar_even/odd). The taxonomy's `parity .electromagnetic
= none` now means "provably no pure channel", not "unmeasured".
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

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

Q0 = Q_MP
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

    # 4. observable level (bean qou-z2xz): alpha carries the CONJUGATE
    #    exponential e^-lambda; the Hartree scale alpha^2 the doubled e^-2lambda
    A, Abar = 1 / C, 1 / Cbar
    aev, aod = (A + Abar) / 2, (A - Abar) / 2
    print(f"  alpha odd/even = {mp.nstr(aod / aev, 12)}   -tanh(ln q0) = {mp.nstr(-mp.tanh(lam), 12)}")
    ok &= abs(aod / aev + mp.tanh(lam)) < mpf("1e-55")
    A2, A2bar = A ** 2, Abar ** 2
    a2ev, a2od = (A2 + A2bar) / 2, (A2 - A2bar) / 2
    print(f"  alpha^2 odd/even = {mp.nstr(a2od / a2ev, 12)}   -tanh(2 ln q0) = {mp.nstr(-mp.tanh(2 * lam), 12)}")
    ok &= abs(a2od / a2ev + mp.tanh(2 * lam)) < mpf("1e-55")
    # not-pure numerically: C(1/q) differs from both C(q) and -C(q),
    # measured RELATIVE to |C| (no arbitrary magnitude; Copilot, PR #6129)
    ok &= abs(Cbar - C) > mpf("1e-40") * abs(C) and abs(Cbar + C) > mpf("1e-40") * abs(C)

    print(f"\nRESULT: {'PASS' if ok else 'FAIL'} — EM coupling = e^lambda * (bar-even B), "
          "alpha = e^-lambda/B, alpha^2 = e^-2lambda/B^2: provably mixed parity, "
          "no pure channel (Lean: EmCouplingBarParity)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
