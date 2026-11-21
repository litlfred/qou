#!/usr/bin/env python3
"""morita_ramanujan_qairy_connection_probe.py — bean qou-cp1x.

Cross-check of Morita, "A connection formula between the Ramanujan function
and the q-Airy function" (2011) [morita-t2011], library/arxiv-1104.0755v2/,
against the corpus A_w zero-asymptotics probe
(computations/probes/awzero_asymptotics_probe.py, bean qou-k16h).

PRE-REGISTERED (written before running):

  Source facts used (PDF text layer, pp. 2-4):
    S1  A_q(x) = sum_{n>=0} q^{n^2} (-x)^n / (q;q)_n  (the corpus A_w with q = w).
    S2  Ai_q(x) = sum_{n>=0} (-1)^n q^{n(n-1)/2} (-x)^n / (-q, q; q)_n.
    S3  theta(x) = sum_{n in Z} q^{n(n-1)/2} x^n.
    S4  Theorem: for x in C*,
          A_{q^2}(-q^3/x^2) = { theta(x/q) Ai_q(-x) + theta(-x/q) Ai_q(x) }
                              / (q, -1; q)_infinity.

  Checks (mpmath 50 dps):
    A  S4 at q in {0.3, sqrt(0.7), sqrt(w_p)}, w_p = 1/q0_proton (the
       substrate w = q~^-1 of the corpus probe), x in {0.37+0.2i, -1.1+0.9i,
       2.5i, 0.05-0.4i}: rel < 1e-35.
    B  The corpus zeros: with w = q^2, find the zeros zeta_n (n = 1..6) of the
       corpus A_w by findroot from w^{1-2n}; at x_n = i sqrt(q^3/zeta_n) the
       bracketed right side of S4 vanishes, |RHS| / (|theta(x/q) Ai_q(-x)| +
       |theta(-x/q) Ai_q(x)|) < 1e-35, for w in {0.49, 0.7, w_p}.
    C  The theta-lattice reading: with Ai_q -> 1 the bracket's zeros are
       exactly x^2 = -q^{4n+1}, i.e. zeta_n = w^{1-2n}, the corpus's tropical
       corners. Checked: theta(x/q) + theta(-x/q) = 0 at those x, rel < 1e-40.
    Reported, not gated: the first-order shift from linearising
    Ai_q(+-x) = 1 +- x/(1-q^2) + ..., as (zeta_n/w^{1-2n} - 1)/(-kappa(w) w^n)
    with the corpus kappa(w) = (w;w^2)^2 / [(1-w)(w^2;w^2)^2].
    PASS iff A, B, C.

Run: python3 -u computations/probes/morita_ramanujan_qairy_connection_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from awzero_asymptotics_probe import kappa, qpoch_inf  # noqa: E402


def A(q, x):
    tot, t, n, poch = mp.mpc(0), mp.mpc(1), 0, mp.mpf(1)
    tiny = mp.mpf(10) ** (-mp.mp.dps - 10)
    while True:
        term = q ** (n * n) * (-x) ** n / poch
        tot += term
        if abs(term) < tiny * max(1, abs(tot)) and n > 3:
            return tot
        n += 1
        poch *= 1 - q ** n


def Ai(q, x):
    tot, n, den = mp.mpc(0), 0, mp.mpf(1)
    tiny = mp.mpf(10) ** (-mp.mp.dps - 10)
    while True:
        term = (-1) ** n * q ** (n * (n - 1) // 2) * (-x) ** n / den
        if n * (n - 1) % 2:
            term = (-1) ** n * q ** (mp.mpf(n * (n - 1)) / 2) * (-x) ** n / den
        tot += term
        if abs(term) < tiny * max(1, abs(tot)) and n > 3:
            return tot
        n += 1
        den *= (1 + q ** n) * (1 - q ** n)


def theta(q, x):
    tot = mp.mpc(0)
    tiny = mp.mpf(10) ** (-mp.mp.dps - 10)
    n = 0
    while True:
        t1 = q ** (mp.mpf(n * (n - 1)) / 2) * x ** n
        t2 = q ** (mp.mpf((-n - 1) * (-n - 2)) / 2) * x ** (-n - 1)
        tot += t1 + t2
        if abs(t1) + abs(t2) < tiny * max(1, abs(tot)) and n > 3:
            return tot
        n += 1


def bracket(q, x):
    a = theta(q, x / q) * Ai(q, -x)
    b = theta(q, -x / q) * Ai(q, x)
    return a + b, abs(a) + abs(b)


def main() -> int:
    mp.mp.dps = 50
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools/qou-substrate/python"))
    from qou_substrate.constants import Q_50_DIGIT_STR
    wp = 1 / mp.mpf(Q_50_DIGIT_STR)
    t35, t40 = mp.mpf(10) ** -35, mp.mpf(10) ** -40
    xs = [mp.mpc("0.37", "0.2"), mp.mpc("-1.1", "0.9"), mp.mpc(0, "2.5"), mp.mpc("0.05", "-0.4")]
    worst = mp.mpf(0)
    for q in (mp.mpf("0.3"), mp.sqrt(mp.mpf("0.7")), mp.sqrt(wp)):
        pref = qpoch_inf(q, q) * qpoch_inf(-1, q)
        for x in xs:
            lhs = A(q ** 2, -q ** 3 / x ** 2)
            rhs = bracket(q, x)[0] / pref
            worst = max(worst, abs(lhs - rhs) / abs(lhs))
    a_ok = worst < t35
    print(f"A  Morita connection formula, worst rel {mp.nstr(worst, 3)}: {a_ok}")
    b_ok = True
    c_ok = True
    for w in (mp.mpf("0.49"), mp.mpf("0.7"), wp):
        q = mp.sqrt(w)
        k = kappa(w)
        for n in range(1, 7):
            z0 = w ** (1 - 2 * n)
            zn = mp.findroot(lambda z: mp.re(A(w, z)), z0)
            x = 1j * mp.sqrt(q ** 3 / zn)
            val, scale = bracket(q, x)
            r = abs(val) / scale
            b_ok &= r < t35
            x0 = 1j * q ** (2 * n + mp.mpf(1) / 2)
            th = theta(q, x0 / q) + theta(q, -x0 / q)
            rc = abs(th) / (abs(theta(q, x0 / q)) + abs(theta(q, -x0 / q)))
            c_ok &= rc < t40
            if n in (1, 3, 6):
                shift = (zn / z0 - 1) / (-k * w ** n)
                print(f"   w={mp.nstr(w, 8)} n={n}: zeta_n = {mp.nstr(zn, 15)}, "
                      f"|bracket| rel {mp.nstr(r, 3)}, (zeta_n/w^(1-2n)-1)/(-kappa w^n) = {mp.nstr(shift, 10)}")
    print(f"B  corpus zeros are zeros of the Morita bracket: {b_ok}")
    print(f"C  theta(x/q)+theta(-x/q) = 0 at x^2 = -q^(4n+1): {c_ok}")
    ok = a_ok and b_ok and c_ok
    print("ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
