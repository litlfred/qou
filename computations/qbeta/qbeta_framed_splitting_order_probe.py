#!/usr/bin/env python3
"""At what order in q - 1 can an n/p mass splitting appear? (bean qou-99qc, audit section 15)

Audit section 14: every n/p construction on record (typed crossings Delta_S, the
four-strand state difference of PR #8636) is FIRST order in h relative to the nucleon
trace, while the physical ratio (Q_beta + m_e)/m_p is 1.38e-3. That 248x gap is why
Q_beta needs a scale E0 separate from the nucleon mass.

This probe tests a structural reading, not a number:
  1. The typed-crossing difference changes WRITHE (uu sigma -> dd sigma^-1 lowers w by 2).
     The gamma-gamma vertex sigma_0 sigma_1^-1 has writhe 0, so every gamma-gamma word
     has writhe 0 and its raw Markov trace is a link invariant times a factor fixed by
     the strand count (def:mass-identity, braid classes).
  2. For knots, the Jones polynomial is 1 + 0*x + c2 x^2 + ... in x = t - 1
     (V(1) = 1, V'(1) = 0; [jones1987]); the x^k coefficient is a Vassiliev invariant of
     order <= k ([birmanlin1993]). So two knots read with one shared scale differ at
     order x^k, k >= 2, where k is the first order whose coefficient differs.
  3. At the proton pin, x = q^2 - 1. The probe prints x^k against the physical ratio.

Prints only; writes no witness; selects no knot. Choosing n and p links because their
splitting lands on CODATA would be selection against the target (AGENTS.md NO FITTING).
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

Q_BETA_CODATA_STR = "0.78233341"   # comparison only
M_P_CODATA_STR = "938.27208943"     # comparison only

t, x = sp.symbols("t x")
JONES = {  # standard tables (one chirality each); [jones1987]
    "0_1": sp.Integer(1),
    "3_1": -t**-4 + t**-3 + t**-1,
    "4_1": t**2 - t + 1 - t**-1 + t**-2,
    "5_1": -t**-7 + t**-6 - t**-5 + t**-4 + t**-2,
    "5_2": -t**-6 + t**-5 - t**-4 + 2 * t**-3 - t**-2 + t**-1,
}


def writhe(word: list[int]) -> int:
    return sum(1 if g > 0 else -1 for g in word)


def main() -> int:
    mp.mp.dps = 50
    ok = True
    # 1. writhe bookkeeping
    gg_vertex = [1, -2]                       # sigma_0 sigma_1^-1 in 1-based generator labels
    v3 = gg_vertex * 3
    checks = [
        ("gamma-gamma vertex sigma_0 sigma_1^-1 has writhe 0", writhe(gg_vertex) == 0),
        ("Borromean base V^3 has writhe 0", writhe(v3) == 0),
        ("uu -> dd crossing flip changes writhe by -2", writhe([-1]) - writhe([1]) == -2),
    ]
    # 2. Jones expansion about t = 1
    coeffs = {}
    for k, v in JONES.items():
        s = sp.expand(sp.series(v.subs(t, 1 + x), x, 0, 6).removeO())
        c = [s.coeff(x, i) for i in range(6)]
        coeffs[k] = c
        checks.append((f"{k}: V(1) = 1 and V'(1) = 0", c[0] == 1 and c[1] == 0))
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        ok &= passed
    print("\nJones coefficients of x^0..x^5, x = t - 1:")
    for k, c in coeffs.items():
        print(f"  {k}: {c}")
    # 3. sizes at the proton pin
    q = mp.mpf(str(q_at()))
    me = mp.mpf(str(M_E_MEV))
    xv = q**2 - 1
    h = q - 1 / q
    phys = (mp.mpf(Q_BETA_CODATA_STR) + me) / mp.mpf(M_P_CODATA_STR)
    print(f"\nq0 = {mp.nstr(q, 20)}; x = q0^2 - 1 = {mp.nstr(xv, 12)}; h = {mp.nstr(h, 12)}")
    print(f"physical (Q_beta + m_e)/m_p = {mp.nstr(phys, 10)}  (comparison only)")
    for k in range(1, 7):
        print(f"  x^{k} = {mp.nstr(xv**k, 8):>14}   phys / x^{k} = {mp.nstr(phys / xv**k, 8)}")
    zD = q**3 / (q**2 + 1)
    tp = zD**2 - h / 2 * zD
    dt = h**2 / 2 - h * zD
    print(f"\ntyped-crossing Delta_S (writhe-changing): |Delta t|/t_p = {mp.nstr(abs(dt) / tp, 10)}"
          f" = {mp.nstr(abs(dt) / tp / xv, 6)} x^1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
