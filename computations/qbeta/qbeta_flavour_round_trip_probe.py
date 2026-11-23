#!/usr/bin/env python3
"""Q_beta under the flavour round-trip rule, labels A and B (bean qou-99qc).

QBetaChiralityReduction.lean: on Delta_S every block-weighted trace gives
Q_beta = (h[2]/2) * y3 * E0, y3 = tau(J). FlavourRoundTrip.lean (sorry-free):
the flavour round trip tr(P s P' s) through the flipping letter is
  label A (sigma3 lines, letter sigma2):  (q^4+1)/(q^2+1)^2   = convention-D y3
  label B (J4 lines, letter sigma3):      (q^2+1)^2(q^4+1)/(q^4+q^2+1)^2
This probe re-checks both identities exactly (sympy, over Q(q)) on the explicit
(3,1) representation and prints Q_beta for each label at the proton pin.

Prints only; writes no witness and touches no production number. Not a
prediction: choosing label B because it lands near CODATA would be selection
against the target (AGENTS.md NO FITTING). mpmath end to end.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402,F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

Q_BETA_CODATA_STR = "0.78233341"  # comparison only, never an input; parsed after dps is set


def exact_checks() -> list[tuple[str, bool]]:
    q = sp.symbols("q", positive=True)
    M = sp.Matrix
    s3 = sp.diag(q, -1 / q, q)
    s2 = M([[(q**2 - 1) / (q * (q**2 + 1)), -(q**4 + 1) / (q * (q**2 + 1)), q * (q**4 + 1) / (q**2 + 1)],
            [-q / (q**2 + 1), q**3 / (q**2 + 1), q**3 / (q**2 + 1)],
            [1 / (q * (q**2 + 1)), 1 / (q * (q**2 + 1)), q**3 / (q**2 + 1)]])
    D = q**4 + q**2 + 1
    Ja = M([[q**2 / D, -(q**4 + 1) / D, 0], [-q**2 / D, (q**4 + 1) / D, 0], [0, 0, 0]])
    Jb = M([[(q**4 + 1) / D, (q**4 + 1) / D, 0], [q**2 / D, q**2 / D, 0], [0, 0, 0]])
    Lu, Ld = sp.diag(1, 0, 0), sp.diag(0, 1, 0)
    yA = (q**4 + 1) / (q**2 + 1) ** 2
    yB = (q**2 + 1) ** 2 * (q**4 + 1) / D**2
    V1 = s2 * s3.inv()
    return [
        ("round trip A = convention-D y3", sp.simplify((Lu * s2 * Ld * s2).trace() - yA) == 0),
        ("round trip B = cJ/2", sp.simplify((Ja * s3 * Jb * s3).trace() - yB) == 0),
        ("round trip B through the gamma-gamma vertex", sp.simplify((Ja * V1 * Jb * V1.inv()).trace() - yB) == 0),
        ("A != B identically", sp.simplify(yA - yB) != 0),
    ]


def main() -> int:
    mp.mp.dps = 50
    Q_BETA_CODATA = mp.mpf(Q_BETA_CODATA_STR)
    ok = True
    for name, passed in exact_checks():
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        ok &= passed
    q = mp.mpf(str(q_at()))
    me = mp.mpf(str(M_E_MEV))
    h, b2, hb = q - 1 / q, q + 1 / q, (q - 1) / q
    E0 = me / (q * (q - 1))
    E0t = E0 / (1 - hb**2)
    unit = h * b2 / 2
    rows = {
        "label A (sigma3) = Markov z_D": (q**4 + 1) / (q**2 + 1) ** 2,
        "label B (J4, strand-4 vertex)": (q**2 + 1) ** 2 * (q**4 + 1) / (q**4 + q**2 + 1) ** 2,
    }
    print(f"\nq0 = {mp.nstr(q, 20)} (proton pin); CODATA Q_beta = {Q_BETA_CODATA} MeV (comparison only)")
    for lab, E in (("order-zero E0", E0), ("tower E0", E0t)):
        print(f"  y3 needed for CODATA, {lab}: {mp.nstr(Q_BETA_CODATA / (unit * E), 12)}")
    for name, y in rows.items():
        for lab, E in (("order-zero E0", E0), ("tower E0", E0t)):
            Qb = unit * y * E
            print(f"  {name:32} {lab:14} y3 = {mp.nstr(y, 10)}  Q_beta = {mp.nstr(Qb, 10)} MeV"
                  f"  ({mp.nstr((Qb / Q_BETA_CODATA - 1) * 100, 6)} %)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
