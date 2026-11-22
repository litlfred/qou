#!/usr/bin/env python3
"""gw_modular_monodromy_vs_routeB_probe.py — bean qou-godb.

Cross-check of Garoufalidis & Wheeler, "Modular q-holonomic modules" (2022)
[garoufalidis-wheeler-modular], library/arxiv-2203.17029v1/, Thms 1.6-1.7,
against the corpus Route-B probe
computations/probes/qlift_routeB_connection_matrix_probe.py, which records a
"theta growth |A_m| ~ q^{gamma m^2}, gamma ~ 1/4" for a 2x2 gauge between the
C1 kernel and GGM eq 49.

PRE-REGISTERED (written before running):

  Source facts used (PDF text layer):
    S1  eq (46): theta(t;q) = sum_k (-1)^k q^{k(k+1)/2} t^k, |q| < 1.
    S2  eq (28), the 4_1 module: t q f(qt) + (1-2t) f(t) + t q^{-1} f(t/q) = 0.
    S3  eq (25) (Thm 1.6, Appell-Lerch module) and eq (31) (Thm 1.7, 4_1
        module): the single non-trivial monodromy entries M_21 as theta
        quotients.

  Checks:
    A  (sympy, exact) GGM eq 49 as the corpus writes it,
       z_{m+1} = (2 - q^m) z_m - z_{m-1}, is S2 with q -> p = 1/q on the
       lattice t = p^m under the diagonal gauge f(p^m) = q^m z_m.
    B  (mpmath 50 dps, q = 2/5) M_21 of (25) and of (31) are q-elliptic in t:
       M_21(qt) = M_21(t), rel < 1e-40, at three (t, lambda, mu) samples. So on
       any lattice t = q^m t_0 they are constant: growth exponent 0.
    C  The Route-B witness's asymptotic-window gamma_est at q = 1.05 and
       q = 1.10998 is >= 0.15 (its own theta class), i.e. it differs from the
       exponent 0 of the Thm 1.6/1.7 monodromy entries.
    AMENDMENT after the first run (statement and thresholds unchanged): A
    reported False because my check compared gw with corpus * q^m * t * p
    (= corpus / q), a coding slip. Substituting t = q^{-m} by hand, gw equals
    the corpus operator with factor exactly 1, and A now compares them directly.
    PASS iff A, B, C. Reading if PASS: the Route-B gamma is a growth mismatch
    between two different recurrences (C1 vs eq 49), not a monodromy of the
    kind Thm 1.6/1.7 computes, so those theta entries cannot "explain" it.

Run: python3 -u computations/probes/gw_modular_monodromy_vs_routeB_probe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent


def theta(t, q):
    tot = mp.mpc(0)
    tiny = mp.mpf(10) ** (-mp.mp.dps - 10)
    k = 0
    while True:
        a = (-1) ** k * q ** (mp.mpf(k * (k + 1)) / 2) * t ** k
        b = (-1) ** (-k - 1) * q ** (mp.mpf((-k - 1) * (-k)) / 2) * t ** (-k - 1)
        tot += a + b
        if abs(a) + abs(b) < tiny * max(1, abs(tot)) and k > 3:
            return tot
        k += 1


def qinf(a, q):
    r, x = mp.mpc(1), mp.mpc(a)
    while abs(x) > mp.mpf(10) ** (-mp.mp.dps - 10):
        r *= 1 - x
        x *= q
    return r


def M25(t, lam, mu, q):
    return -(qinf(q, q) ** 3 * theta(t / q, q) * theta(mu / lam, q) * theta(1 / (lam * mu * t), q)
             / (theta(1 / lam, q) * theta(mu, q) * theta(1 / (lam * t), q) * theta(1 / (mu * t), q)))


def M31(t, lam, q):
    q4, q2 = q ** (mp.mpf(1) / 4), mp.sqrt(q)
    num = theta(q * t, q) * theta(t * lam, q) * theta(t * lam / q2, q) * theta(t * lam ** 2 / q2, q)
    den = (theta(t * lam * q4, q) * theta(-t * lam * q4, q) * theta(t * lam / q4, q)
           * theta(-t * lam / q4, q) * theta(lam / q, q) * theta(lam / q ** (mp.mpf(3) / 2), q))
    return num / den


def main() -> int:
    q, z = sp.symbols("q z", positive=True)
    m = sp.symbols("m", integer=True)
    p = 1 / q
    t = p ** m
    F = lambda k: q ** k * sp.Function("z")(k)
    gw = t * p * F(m + 1) + (1 - 2 * t) * F(m) + t / p * F(m - 1)
    corpus = sp.Function("z")(m + 1) - (2 - q ** m) * sp.Function("z")(m) + sp.Function("z")(m - 1)
    a_ok = sp.simplify(sp.expand(gw - corpus)) == 0
    print(f"A  GGM eq 49 = GW eq (28) at p = 1/q, t = p^m, f = q^m z: {a_ok}")
    mp.mp.dps = 50
    qq = mp.mpf(2) / 5
    samples = [(mp.mpc("0.7", "0.3"), mp.mpc("1.3", "-0.4"), mp.mpc("0.55", "0.8")),
               (mp.mpc("-1.9", "0.6"), mp.mpc("0.45", "0.35"), mp.mpc("2.2", "0.1")),
               (mp.mpc("0.15", "-1.1"), mp.mpc("-0.8", "0.9"), mp.mpc("-0.6", "-0.5"))]
    worst = mp.mpf(0)
    for (tt, lam, mu) in samples:
        worst = max(worst, abs(M25(qq * tt, lam, mu, qq) / M25(tt, lam, mu, qq) - 1),
                    abs(M31(qq * tt, lam, qq) / M31(tt, lam, qq) - 1))
    b_ok = worst < mp.mpf(10) ** -40
    print(f"B  M_21 of (25), (31) q-elliptic in t, worst rel {mp.nstr(worst, 3)}: {b_ok}")
    w = json.loads((HERE / "qlift_routeB_connection_matrix_probe.witness.json").read_text())
    per = w["results"]["per_q"]
    gam = {r["q"]: [mp.mpf(run["asym_window"]["gamma_est"]) for run in r["runs"]] for r in per}
    c_ok = all(g >= mp.mpf("0.15") for qv in ("1.05", "1.10998") for g in gam[qv])
    print(f"C  Route-B gamma_est (asym window) = "
          f"{ {k: [mp.nstr(x, 6) for x in v] for k, v in gam.items()} }; q>1 all >= 0.15: {c_ok}")
    ok = a_ok and b_ok and c_ok
    print("ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
