"""`c4` at A = 3 and A = 4 — the last gap in the Borromean convergence picture.

WHY
---
`qou-yaig` measured `c1..c4` at `A = 2` and `c1..c3` at `A = 3, 4`, and read the
ratio columns as: one anomalous order (the second), then rapid convergence. The
`c4` evidence for that — the step that turned a single settling into a trend —
exists at **`A = 2` only**, because the committed `P_OF` gives `P = 6` to the
three two-nucleon cases and nothing else.

That is the last stated gap in the bean, in its own words:

    "c4 is A = 2 only. T and 3He sit at committed P = 5 and 4He at P = 3, so
     none reaches c4 without a further long-compute run. Four orders at one A
     is still a shape, not a convergence proof."

This is that run. `c4` needs `a4`, hence `d.p > 4`, hence `P >= 6` everywhere.

WHAT IT DECIDES
---------------
Whether the order-4 collapse seen at `A = 2` (|c4/c3| of 0.011 and 0.012, about
forty times smaller than the `c3/c2` step) is a property of the two-nucleon case
or of the expansion. The `c3` column already showed **no `A` trend** at all
(0.4023, 0.6817, 0.8087, 0.5295, 0.5999), so the honest prior is that `c4/c3`
will likewise be flat in `A` — but that is a prior, not a result, and a flat
`c3` column is not evidence about `c4`.

    all three A collapse   -> the one-bad-order shape is the expansion's, not
                              an artefact of A = 2.
    A = 3 or 4 does NOT    -> the A = 2 collapse was special, and the trend
                              claim must be narrowed to A = 2 in the bean, the
                              audit doc and PR #6966.

COST — this is the expensive one and is ordered accordingly
-----------------------------------------------------------
Measured on this same pipeline: `n = 12` took 295 s at `P = 4` and 352 s at
`P = 5`; `n = 9` at `P = 5` was ~20 s per case. So `P = 6` at `n = 9` should be
minutes and `P = 6` at `n = 12` is the long pole.

**The three cases are run cheapest-first and each prints its full row the moment
it completes**, so a timeout or a kill on `4He` cannot cost the `A = 3` results
— the failure mode that a single all-cases sweep has and this deliberately does
not.

CONTROLS: every case must reproduce its recorded `c0`, `c1`, `c2` AND `c3`
before its `c4` is read.

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
REC = {                       # c1, c2, c3 as measured earlier in this bean
    "T":   (F(1, 64), F(99, 128), F(101, 16)),
    "3He": (F(1, 8), F(157, 128), F(839, 128)),
    "4He": (F(7, 128), F(439, 512), F(1329, 256)),
}
# cheapest first: n = 9 before n = 12
CASES = [("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
A2 = (("pp", "-585/128", -0.1081), ("pn", "109/192", 0.0105), ("nn", "27/32", 0.0124))


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
        A = Z + N
        log(f"=== {name} (Z={Z},N={N}, n={3*A}, P={P}) — "
            f"{'the long pole' if A == 4 else 'expect minutes'} …")
        d = tr_M_series(Z, N, False, P, log=log) - tr_M_series(Z, N, True, P, log=log)
        if d.p <= 4:
            failures.append(f"{name}: d.p = {d.p}, cannot reach c4 at P = {P}")
            log(f"    {name}: d.p = {d.p} — c4 UNREACHABLE at P = {P}")
            continue
        a = [d.coeff(k) for k in range(5)]
        c2, c3, c4 = a[1] + a[2], a[2] + a[3], a[3] + a[4]
        rc1, rc2, rc3 = REC[name]
        for label, got, want in (("a0", a[0], c0_derived(A)), ("a1", a[1], rc1),
                                 ("c2", c2, rc2), ("c3", c3, rc3)):
            if got != want:
                failures.append(f"{name}: {label} = {got} != recorded {want}")
        r43 = (q(c4) * h ** 4) / (q(c3) * h ** 3)
        rows.append((name, A, c4, r43))
        # print the row NOW, so a later timeout cannot cost it
        log(f"    ROW  {name}  A={A}  c4 = {c4}   c4ℏ⁴/c3ℏ³ = {float(r43):.4f}")

    print()
    print("=" * 66)
    print(f"  the c4 column, {'complete' if len(rows) == 3 else 'PARTIAL'}:")
    for n, c4s, r in A2:
        print(f"    {n:>4s}  A=2   {c4s:>10s}   {r:8.4f}")
    for name, A, c4, r in rows:
        print(f"    {name:>4s}  A={A}   {str(c4):>10s}   {float(r):8.4f}")
    print("=" * 66)
    ok = [r for name, A, c4, r in rows]
    if len(rows) == 3 and all(abs(r) < 1 for r in ok):
        print("  Every A collapses at order 4. The one-bad-order shape is a")
        print("  property of the expansion, not an artefact of A = 2.")
    elif rows and any(abs(r) >= 1 for r in ok):
        print("  NOT every A collapses. The A = 2 collapse was special, and the")
        print("  trend claim must be NARROWED to A = 2 in the bean, the audit doc")
        print("  and PR #6966.")
    print()
    print("  Still unbounded by anything here: c5 and beyond.")
    print()

    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        return 1
    print(f"PASS  {len(rows)}/3 cases, 4 controls each (c0, c1, c2, c3 reproduced)")
    return 0 if len(rows) == 3 else 1


if __name__ == "__main__":
    raise SystemExit(main())
