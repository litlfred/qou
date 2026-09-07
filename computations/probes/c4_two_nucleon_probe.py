"""`c4` for the three two-nucleon cases — does the settling continue past order 3?

WHY
---
`qou-yaig` measured `c2` and `c3` under the Borromean word and read them together
as: the expansion has ONE BAD ORDER, the second, after which the terms resume
shrinking. That reading rests on **one** step of settling (order 2 -> 3) at two
values of `A`, and the bean says so:

    "Five points across two A is a shape, not a convergence proof."

A single step down is exactly what a fluctuation looks like. Two consecutive
steps down is a trend. This probe supplies the second step where it is cheap.

WHY ONLY pp, pn, nn
-------------------
`c4` needs `a4`, hence `d.p > 4`, hence `P >= 6` after the order lost to the 0/0
seminormal quotients. The committed `P_OF` gives `P = 6` to exactly the three
two-nucleon cases -- `T` and `3He` sit at 5, `4He` at 3 -- so these three are
FREE at `n = 6`, and nothing else is. Extending to `A = 3` would need `P = 6` at
`n = 9`, and to `A = 4` a `P = 6` at `n = 12` well beyond the 295 s that `P = 4`
already cost there.

WHAT IT CAN AND CANNOT SAY
--------------------------
It can say whether the third -> fourth step also shrinks, at `A = 2`. It CANNOT
say anything about `A = 3` or `A = 4`, and it is not a convergence proof at any
`A` -- four orders is still a shape. Stated in the output, not in a footnote.

`nn` is expected to misbehave and is not evidence either way: `c1(nn) = 0`
exactly under the Borromean word, so its ratios have no scale to be measured
against. It was the sole outlier at both previous orders (INFINITE, then
10.7008) for that reason.

Controls: every case must reproduce its recorded `c0`, `c1`, `c2` AND `c3` before
its `c4` is read.

NO FLOAT in the extraction: exact `fractions.Fraction`. mpmath only for display.
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

HBAR_Q = "0.099081716044258508"
C1 = {"pp": F(1, 8), "pn": F(1, 16), "nn": F(0)}
C2 = {"pp": F(33, 32), "pn": F(25, 32), "nn": F(1, 16)}
C3 = {"pp": F(67, 16), "pn": F(43, 8), "nn": F(27, 4)}
CASES = [("pp", 2, 0), ("pn", 1, 1), ("nn", 0, 2)]


def main() -> int:
    t0 = time.time()

    def log(m):
        print(f"  [{time.time()-t0:7.1f}s] {m}", flush=True)

    mp.mp.dps = 30
    h = mp.mpf(HBAR_Q)
    P = 6
    failures, rows = [], []

    def q(x):
        return mp.mpf(x.numerator) / x.denominator

    for name, Z, N in CASES:
        log(f"{name} (Z={Z},N={N}, n=6, P={P}) …")
        d = tr_M_series(Z, N, False, P, log=log) - tr_M_series(Z, N, True, P, log=log)
        if d.p <= 4:
            failures.append(f"{name}: d.p = {d.p}, cannot reach c4 at P = {P}")
            continue
        a = [d.coeff(k) for k in range(5)]
        c2, c3, c4 = a[1] + a[2], a[2] + a[3], a[3] + a[4]
        for label, got, want in (("a0", a[0], c0_derived(2)), ("a1", a[1], C1[name]),
                                 ("c2", c2, C2[name]), ("c3", c3, C3[name])):
            if got != want:
                failures.append(f"{name}: {label} = {got} != recorded {want}")
        r32 = (q(c3) * h ** 3) / (q(c2) * h ** 2)
        r43 = (q(c4) * h ** 4) / (q(c3) * h ** 3)
        rows.append((name, c3, c4, r32, r43))
        log(f"    c4 = {c4}   c3ℏ³/c2ℏ² = {float(r32):.4f}   c4ℏ⁴/c3ℏ³ = {float(r43):.4f}")

    print()
    print("=" * 70)
    print(f"  {'case':>5s} {'c3':>10s} {'c4':>14s}   {'c3/c2':>8s} {'c4/c3':>8s}")
    for name, c3, c4, r32, r43 in rows:
        print(f"  {name:>5s} {str(c3):>10s} {str(c4):>14s}   "
              f"{float(r32):8.4f} {float(r43):8.4f}")
    print("=" * 70)
    ok = [(n, r43) for n, _, _, _, r43 in rows if n != "nn"]
    if ok and all(r < 1 for _, r in ok):
        print("  Both non-degenerate cases shrink AGAIN at order 4. Two consecutive")
        print("  steps down is a trend rather than a fluctuation, which is what the")
        print("  one-bad-order reading needed and did not have.")
    elif ok:
        print("  NOT all non-degenerate cases shrink at order 4 — the one-bad-order")
        print("  reading does NOT extend past order 3 even at A = 2.")
    print()
    print("  LIMITS, and they are real: this is A = 2 ONLY. T and 3He sit at")
    print("  committed P = 5 and 4He at P = 3, so neither can reach c4 without a")
    print("  new long-compute run. Four orders at one A is still a shape, not a")
    print("  convergence proof. nn is degenerate (c1 = 0) and is not evidence.")
    print()

    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        return 1
    print(f"PASS  {len(rows)} cases, 4 controls each (c0, c1, c2, c3 all reproduced)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
