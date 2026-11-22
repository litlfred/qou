#!/usr/bin/env python3
"""How much of the scored D1 = A Q_beta comes from the selected word? (qou-99qc, audit section 17)

D1 = A: Q_beta = |eps_flavour(V^3)| * E0_tower, eps_flavour(X) = -h tr_W(X)/[2]^3, because the plain
traces on the two T^3 weight spaces are equal for every word. FlavourSplitWordShare.lean proves
tr_W(V^3) = 3 - h^4 [3]. This probe re-checks that identity exactly, and prints the value split
into its word-free part 3h/[2]^3 E0 and the word's correction -h^5[3]/[2]^3 E0 at the proton pin.
Prints only; writes no witness. mpmath end to end.
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

Q_BETA_CODATA_STR = "0.78233341"  # comparison only


def main() -> int:
    x = sp.symbols("q", positive=True)
    P = x**12 - 3 * x**10 + 3 * x**8 - 5 * x**6 + 3 * x**4 - 3 * x**2 + 1
    hs, b3 = x - 1 / x, x**2 + 1 + x**-2
    ok = sp.simplify(-P / x**6 - (3 - hs**4 * b3)) == 0
    print(f"[{'PASS' if ok else 'FAIL'}] tr_W(V^3) = -P(q)/q^6 = 3 - h^4 [3]")
    mp.mp.dps = 50
    q = mp.mpf(str(q_at()))
    me = mp.mpf(str(M_E_MEV))
    h, b2, br3 = q - 1 / q, q + 1 / q, q**2 + 1 + q**-2
    E0 = me / (q * (q - 1)) / (1 - ((q - 1) / q) ** 2)
    lead = 3 * h / b2**3 * E0
    word = -(h**5) * br3 / b2**3 * E0
    tot = lead + word
    codata = mp.mpf(Q_BETA_CODATA_STR)
    print(f"\nq0 = {mp.nstr(q, 20)}; E0 (tower) = {mp.nstr(E0, 15)} MeV")
    print(f"  word-free part 3h/[2]^3 E0 = {mp.nstr(lead, 12)} MeV")
    print(f"  word correction -h^5[3]/[2]^3 E0 = {mp.nstr(word, 12)} MeV ({mp.nstr(word / tot * 100, 6)} % of the value)")
    print(f"  scored D1 = A value = {mp.nstr(tot, 12)} MeV ({mp.nstr((tot / codata - 1) * 100, 6)} % vs CODATA, comparison only)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
