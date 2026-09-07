"""`c3` at 4He under Borromean — the one run that closes #6607.

WHY THIS IS SEPARATE FROM `c3_borromean_all_cases_probe`
--------------------------------------------------------
`c3` needs `a3`, hence `d.p > 3`, hence `P >= 5` after the order lost to the 0/0
seminormal quotients. Five of six cases already sit at a committed `P` that
reaches it and are measured in that probe. **4He does not** -- committed
`P_OF["4He"] = 3` -- and it is the expensive one:

    P = 4 at n = 12 cost 295 s, with the [8,4] and [7,5] Wedderburn blocks
    alone at 50 s and 59 s, and the per-order growth is steep.

So this is a long-compute run in its own file, launched under the tee-and-
progress discipline, rather than something buried inside a five-case sweep where
a timeout would silently truncate the sweep's other results.

WHAT IT DECIDES
---------------
`2026-09-04-c3-confirms-the-crossover-comparable-not-diverging.md` (#6607)
concluded from the GROUPED word that the orders are comparable rather than
diverging, and **A = 4 is where its interest lies** -- its headline figures are
the 4He ones (`c2 = +29.8965`, `c3 = +247.98`, ratio `0.8219`).

`qou-yaig` re-measured `A = 2` and `A = 3` under Borromean and found the
conclusion holds there (four of five `c3.h^3/c2.h^2` ratios well below 1). This
run supplies the sixth point, at the `A` that document actually cares about:

    ratio < 1  -> #6607's conclusion holds at its own headline case. The
                  expansion overshoots once, at order 2, and then settles.
    ratio > 1  -> it does NOT hold at A = 4, and the A = 2, 3 agreement was
                  not predictive of the case that matters.

CONTROLS -- three values this run must reproduce before its c3 is read
----------------------------------------------------------------------
    a0 = 7/128     the derived classical floor c0(4)
    a1 = 7/128     the c1(4He) of #6931, confirmed independently at P = 4
    c2 = 439/512   measured at P = 4 in this same bean

If any disagrees, the higher-precision run is not computing the same object and
its c3 means nothing.

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

HBAR_Q = "0.099081716044258508"
C0_HE4 = F(7, 128)
C1_HE4 = F(7, 128)
C2_HE4 = F(439, 512)

# The five ratios measured at committed P in c3_borromean_all_cases_probe.
KNOWN_C3_RATIOS = (("pp", 2, "0.4023"), ("pn", 2, "0.6817"),
                   ("nn", 2, "10.7008 (c1=0, degenerate)"),
                   ("T", 3, "0.8087"), ("3He", 3, "0.5295"))


def main() -> int:
    t0 = time.time()

    def log(m):
        print(f"  [{time.time()-t0:7.1f}s] {m}", flush=True)

    mp.mp.dps = 30
    P = 5
    log(f"4He (Z=2, N=2, n=12) at P = {P} — committed P_OF is 3; P = 4 took 295 s")
    log("expect the [8,4] and [7,5] blocks to dominate")

    log("free word …")
    tf = tr_M_series(2, 2, False, P, log=log)
    log("atom word …")
    ta = tr_M_series(2, 2, True, P, log=log)
    d = tf - ta
    log(f"difference precision after pipeline: d.p = {d.p} (need > 3 for c3)")

    failures = []
    a0, a1 = d.coeff(0), d.coeff(1)
    a2 = d.coeff(2) if d.p > 2 else None
    a3 = d.coeff(3) if d.p > 3 else None
    log(f"a0 = {a0}  a1 = {a1}  a2 = {a2}  a3 = {a3}")

    if a0 != C0_HE4 or a0 != c0_derived(4):
        failures.append(f"a0 = {a0} != derived floor {C0_HE4}")
    if a1 != C1_HE4:
        failures.append(f"a1 = {a1} != the c1(4He) = {C1_HE4} of #6931")
    if a3 is None:
        failures.append(f"c3 still unreachable at P = {P}: d.p = {d.p}")
    c2 = (a1 + a2) if a2 is not None else None
    if c2 is not None and c2 != C2_HE4:
        failures.append(f"c2 = {c2} != the {C2_HE4} measured at P = 4")

    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        return 1

    c3 = a2 + a3
    h = mp.mpf(HBAR_Q)

    def q(x):
        return mp.mpf(x.numerator) / x.denominator

    ratio = (q(c3) * h ** 3) / (q(c2) * h ** 2)

    print()
    print("=" * 74)
    print(f"  c2(4He) = {c2}      c3(4He) = {c3}")
    print(f"  ratio c3·ℏ³/c2·ℏ² = {float(ratio):.4f}")
    print("=" * 74)
    print("  the c3 column, complete:")
    for name, A, r in KNOWN_C3_RATIOS:
        print(f"    {name:>4s}  A={A}   {r}")
    print(f"    {'4He':>4s}  A=4   {float(ratio):.4f}")
    print()
    if ratio < 1:
        print("  VERDICT: the third order does NOT overtake the second at A = 4.")
        print("  #6607's conclusion HOLDS at its own headline case: the expansion")
        print("  overshoots once, at order 2, and then settles.")
        print(f"  (its grouped 4He ratio was 247.98·ℏ/29.8965 = 0.8219, also < 1)")
    else:
        print("  VERDICT: the third order DOES overtake the second at A = 4.")
        print("  #6607's conclusion FAILS at its own headline case, and the")
        print("  A = 2, 3 agreement was not predictive of the case that matters.")
    print()
    print(f"PASS  3/3 controls (a0, a1, c2 all reproduced) and c3(4He) = {c3} measured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
