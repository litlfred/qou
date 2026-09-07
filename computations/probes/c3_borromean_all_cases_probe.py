"""`c3` under the Borromean word — item 2 of `qou-yaig`, and #6607's re-measure.

WHY
---
`2026-09-04-c3-confirms-the-crossover-comparable-not-diverging.md` (#6607)
measured `c3` under the GROUPED word. `7db032fb48` (owner ruling, bean
`qou-hu1f`) made Borromean canonical, so every number in it is convention-scoped
and its conclusion — that the orders are comparable rather than diverging — has
never been checked against the word the framework actually uses.

`c1` and `c2` have both now been re-measured (#6931, `qou-yaig`), and BOTH moved
substantially: `c1(4He)` by a factor of 37, `c2(4He)` from `15307/512` to
`439/512`. There is no reason to expect `c3` to be the exception.

COST — and why five cases are cheap and one is not
--------------------------------------------------
`c3` needs `a3`, hence `d.p > 3`. One order is lost to the 0/0 seminormal
quotients, so a case needs `P >= 5`. The committed `P_OF` already provides that
for five of the six:

    pp, pn, nn   P = 6   ->  d.p = 5   c3 reachable, and c4 too
    T, 3He       P = 5   ->  d.p = 4   c3 reachable
    4He          P = 3   ->  d.p = 2   NOT reachable; needs P = 5

So this probe does the five at their committed precision. **4He is deliberately
left out**: `P = 4` at `n = 12` already cost 295 s, with the `[8,4]` and `[7,5]`
Wedderburn blocks alone taking 50 s and 59 s, and the growth per order is steep.
`P = 5` there is a separate long-compute run under the tee-and-progress
discipline, not something to bury inside a five-case sweep.

WHAT THIS CAN AND CANNOT CONCLUDE
---------------------------------
It can say whether the third order is comparable to the second at `A = 2` and
`A = 3` under the canonical word. It **cannot** settle #6607's claim at `A = 4`,
which is where its interest lies — that stays open and is stated as open.

The convention `c_k = a_{k-1} + a_k` follows `c1_leading_coefficient_derived_probe`
so the numbers are comparable with what is already recorded. `c2` is recomputed
here too, as a control: it must reproduce the values measured independently in
#6931 or this run is not measuring what it claims.

NO FLOAT in the extraction: exact `fractions.Fraction` throughout. mpmath only
for the ratio display, at 30 dps.
"""
from __future__ import annotations

import os
import sys
import time
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMP = os.path.dirname(_HERE)
for _p in (_COMP, _HERE, os.path.join(_COMP, "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from c1_leading_coefficient_derived_probe import tr_M_series, c0_derived  # noqa: E402

HBAR_Q = "0.099081716044258508"          # proton pin

# Borromean, measured: c1 in #6931, c2 in #6931 (five) and qou-yaig (4He).
C1 = {"pp": F(1, 8), "pn": F(1, 16), "nn": F(0), "T": F(1, 64), "3He": F(1, 8)}
C2 = {"pp": F(33, 32), "pn": F(25, 32), "nn": F(1, 16),
      "T": F(99, 128), "3He": F(157, 128)}

CASES = [("pp", 2, 0, 6), ("pn", 1, 1, 6), ("nn", 0, 2, 6),
         ("T", 1, 2, 5), ("3He", 2, 1, 5)]


def main() -> int:
    t0 = time.time()

    def log(m):
        print(f"  [{time.time()-t0:7.1f}s] {m}", flush=True)

    mp.mp.dps = 30
    h = mp.mpf(HBAR_Q)
    failures, rows = [], []

    def q(x):
        return mp.mpf(x.numerator) / x.denominator

    for name, Z, N, P in CASES:
        A = Z + N
        log(f"{name} (Z={Z},N={N}, n={3*A}, P={P}) …")
        d = tr_M_series(Z, N, False, P, log=log) - tr_M_series(Z, N, True, P, log=log)
        if d.p <= 3:
            failures.append(f"{name}: d.p = {d.p}, cannot reach c3 at P = {P}")
            continue
        a0, a1, a2, a3 = d.coeff(0), d.coeff(1), d.coeff(2), d.coeff(3)
        c2, c3 = a1 + a2, a2 + a3

        # controls: this run must reproduce what is already independently known
        if a0 != c0_derived(A):
            failures.append(f"{name}: a0 = {a0} != c0_derived({A}) = {c0_derived(A)}")
        if a1 != C1[name]:
            failures.append(f"{name}: a1 = {a1} != recorded c1 {C1[name]}")
        if c2 != C2[name]:
            failures.append(f"{name}: c2 = {c2} != recorded c2 {C2[name]}")

        r32 = (q(c3) * h ** 3) / (q(c2) * h ** 2) if c2 != 0 else None
        rows.append((name, A, c2, c3, r32))
        log(f"    c2 = {c2}  c3 = {c3}   c3·ℏ³/c2·ℏ² = "
            f"{('%.4f' % float(r32)) if r32 is not None else 'n/a (c2=0)'}")

    print()
    print("=" * 74)
    print(f"  {'case':>5s} {'A':>2s} {'c2':>12s} {'c3':>14s}   c3·ℏ³/c2·ℏ²")
    for name, A, c2, c3, r in rows:
        rs = f"{float(r):.4f}" if r is not None else "n/a"
        print(f"  {name:>5s} {A:>2d} {str(c2):>12s} {str(c3):>14s}   {rs:>11s}")
    print("=" * 74)
    print("  4He is NOT here: committed P_OF = 3 gives d.p = 2. It needs P = 5,")
    print("  a separate long-compute run — so #6607's claim at A = 4, which is")
    print("  where its interest lies, REMAINS OPEN.")
    print()

    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        return 1
    print(f"PASS  {len(rows)} cases; every one reproduced its already-recorded "
          f"c0, c1 and c2 before its c3 was read")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
