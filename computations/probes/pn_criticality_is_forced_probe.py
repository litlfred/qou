#!/usr/bin/env python3
"""
pn_criticality_is_forced_probe — DERIVED: the p-n bond sits at the transfer
matrix's critical point because AVERAGING PUTS IT THERE. The trace is linear in
the bond offset and the two endpoints are `sigma` (d=0) and `sigma^-1` (d=-h),
so the midpoint is trace-zero identically. The criticality carries NO
independent information, and my previous probe's open question is answered
against itself.

What survives, and is not trivial: that midpoint is the **bar-symmetric** point,
`delta` is the **only** bar-breaking in the bond family, and the audit-only
`strict_averaged` convention would sit EXACTLY at criticality with an INFINITE
correlation length.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Answers the question left open
by `pn_critical_point_probe`.

## The question it answers

`pn_critical_point_probe` established `trace(T_pn) = h*delta/2` exactly and said:

    "NOT that the criticality is derived. It is measured: d_pn happens to equal
     -h/2 + h*delta/4, and -h/2 happens to be the trace-zero point. Whether the
     colour weighting was CONSTRUCTED to sit there is a question this probe does
     not answer."

It is answered here, and the answer is **forced, not constructed and not
independent**.

## The derivation — two lines

    trace T(1,d) = h + 2d          LINEAR in d
    d_pp = 0  (sigma)   d_nn = -h  (sigma^-1)      the two braid generators
    midpoint = (0 + (-h))/2 = -h/2   ==>   trace = h + 2(-h/2) = 0

So **the trace-zero point IS the arithmetic mean of the pp and nn letters**, and
it is forced by the trace being affine in `d` with those endpoints. Any
interpolation that places the p-n bond at the midpoint lands on criticality --
the colour weighting did not have to be *constructed* to sit there, and its
sitting there is not evidence for anything.

**So the criticality is NOT an independent structural prediction.** My previous
framing invited reading it as one; it is not.

## What is NOT trivial — the same point is the BAR-SYMMETRIC point

    spec(pp)  = { q, -1/q }         spec(nn) = { -q, 1/q }

The two are **bar images** of each other under `q <-> 1/q`. The midpoint is the
fixed point of that involution, and there `|lambda_1| = |lambda_2| =
1.005448433` exactly. So:

    trace-zero  =  pp/nn midpoint  =  bar-symmetric point

three descriptions of one point. That the *averaging* point and the *bar-fixed*
point coincide is forced by the same affineness, but it is what makes `delta`
interpretable: **`delta` is the only bar-symmetry breaking in the bond family.**

## The consequence that is NOT numerically negligible

`AGENTS.md` records that `bring_color_weighted` (canonical) and
`strict_averaged` (audit-only) differ by "~1e-4 relative -- three to four orders
too small to explain a 27-226 % deficit". **True for the binding MAGNITUDE, and
false for the RANGE:**

    strict_averaged     w = 1/2        d = -h/2            EXACTLY critical
                                                            ratio = 1 exactly
                                                            xi = INFINITE
    bring_color_weighted w = 1/2-d/4   d = -h/2 + h*d/4    ratio = 0.99985699
                                                            xi ~ 6992

So the two conventions are separated by *finite vs infinite correlation length*,
not by 1e-4. The colour weighting is what makes the p-n bond finite-range at
all. That is a structural reason to prefer the canonical convention beyond its
numerical effect, and it is not recorded anywhere I could find.

## And `delta` is not bar-odd

    flavor_split_leading(q)   =  0.00137571080703
    flavor_split_leading(1/q) = -0.00169494787602
    sum                       = -0.00031923707      (bar-odd would be 0)
    ratio                     = -1.2320525          (bar-even would be +1)

So `delta` is of **mixed bar parity** -- neither even nor odd. Worth recording
because the corpus's bar-parity arguments (`z` bar-even, `h` bar-odd) do not
extend to it, and an argument that assumed either would be wrong.

## What is NOT claimed

  * NOT that the colour weighting is wrong or arbitrary. Only that its landing
    at trace-zero-plus-`h*delta/4` is a consequence of averaging, not evidence.
  * NOT that `delta` is the bar-breaking route 1 asked for. Route 1's exact
    antisymmetry is in the eigenvalues of a SINGLE `sigma` (`q` and `-1/q`),
    where `delta` does not enter at all. These are different places in the
    algebra and must not be conflated -- which is exactly the temptation.
  * NOT a binding value. Nothing wired, nothing fitted.

Scope **(a)** for the measurements; the trace-zero derivation is exact algebra.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50
TOL = mp.mpf(10) ** -45


def fmt(x, n=12):
    return mp.nstr(x, n)


def main() -> int:
    q = Q_MP
    h = q - 1 / q
    dx = flavor_split_leading(q)

    def spec(d):
        tr = h + 2 * d
        dt = (h + d) * d - 1
        r = mp.sqrt(tr * tr - 4 * dt)
        e = [(tr + r) / 2, (tr - r) / 2]
        e.sort(key=lambda x: -abs(x))
        return e

    print("pn_criticality_is_forced_probe")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}   h = {fmt(h)}   delta = {fmt(dx)}")
    print()

    print("THE DERIVATION — the criticality is FORCED, in two lines")
    print("-" * 78)
    d_pp, d_nn = mp.mpf(0), -h
    mid = (d_pp + d_nn) / 2
    print("  trace T(1,d) = h + 2d          <- AFFINE in d")
    print(f"  d_pp = {fmt(d_pp)}  (sigma)      d_nn = {fmt(d_nn)}  (sigma^-1)")
    print(f"  midpoint = {fmt(mid)}   =  -h/2 ?  {abs(mid + h / 2) < TOL}")
    print(f"  trace at midpoint = {fmt(h + 2 * mid)}   zero?  "
          f"{abs(h + 2 * mid) < TOL}")
    assert abs(mid + h / 2) < TOL and abs(h + 2 * mid) < TOL
    print()
    print("  => trace-zero IS the arithmetic mean of the two braid-generator")
    print("     letters, forced by affineness with endpoints 0 and -h.")
    print("     ANY interpolation placing p-n at the midpoint lands on")
    print("     criticality.  The colour weighting did not have to be")
    print("     CONSTRUCTED to sit there, and its sitting there is NOT")
    print("     evidence for anything.")
    print()
    print("  ANSWERS pn_critical_point_probe's open question AGAINST ITSELF:")
    print("  the criticality is not an independent structural prediction.")
    print()

    print("WHAT IS NOT TRIVIAL — the same point is the BAR-SYMMETRIC point")
    print("-" * 78)
    epp, enn, em = spec(d_pp), spec(d_nn), spec(mid)
    print(f"  spec(pp)  = {fmt(epp[0], 10):>14}, {fmt(epp[1], 10):>14}"
          f"   = q, -1/q")
    print(f"  spec(nn)  = {fmt(enn[0], 10):>14}, {fmt(enn[1], 10):>14}"
          f"   = -q, 1/q")
    print(f"  spec(mid) = {fmt(em[0], 10):>14}, {fmt(em[1], 10):>14}")
    print(f"  |l1| == |l2| at the midpoint? {abs(abs(em[0]) - abs(em[1])) < TOL}")
    assert abs(abs(em[0]) - abs(em[1])) < TOL, "midpoint must be bar-symmetric"
    assert abs(abs(epp[0]) - q) < TOL and abs(abs(epp[1]) - 1 / q) < TOL
    print()
    print("  pp and nn spectra are BAR IMAGES under q <-> 1/q, and the midpoint")
    print("  is the FIXED POINT of that involution.  So")
    print("      trace-zero = pp/nn midpoint = bar-symmetric point")
    print("  are three descriptions of ONE point -- which is what makes delta")
    print("  interpretable: it is the ONLY bar-breaking in the bond family.")
    print()

    print("THE CONSEQUENCE THAT IS *NOT* NUMERICALLY NEGLIGIBLE")
    print("-" * 78)
    w = mp.mpf(1) / 2 - dx / 4
    d_pn = -h * w
    r_strict = abs(spec(mid)[1]) / abs(spec(mid)[0])
    r_col = abs(spec(d_pn)[1]) / abs(spec(d_pn)[0])
    print(f"  strict_averaged  (audit-only) w = 1/2       ratio = {fmt(r_strict)}")
    print("                                              xi    = INFINITE")
    print(f"  bring_color_weighted (canon)  w = 1/2-d/4   ratio = {fmt(r_col)}")
    print(f"                                              xi    = "
          f"{fmt(1 / (1 - r_col), 6)}")
    assert abs(r_strict - 1) < TOL, "strict average must be exactly critical"
    assert r_col < 1, "colour weighting must lift it off criticality"
    print()
    print("  AGENTS.md records the two conventions as differing by '~1e-4")
    print("  relative -- three to four orders too small to explain a 27-226 %")
    print("  deficit'.  TRUE for the binding MAGNITUDE.  FALSE for the RANGE:")
    print("  they are separated by FINITE vs INFINITE correlation length.")
    print("  The colour weighting is what makes the p-n bond finite-range at")
    print("  all -- a structural reason to prefer it beyond its numerical size.")
    print()

    print("AND delta IS NOT BAR-ODD")
    print("-" * 78)
    fq, fi = flavor_split_leading(q), flavor_split_leading(1 / q)
    print(f"  flavor_split_leading(q)   = {fmt(fq)}")
    print(f"  flavor_split_leading(1/q) = {fmt(fi)}")
    print(f"  sum   = {fmt(fq + fi, 8)}      (bar-ODD would be 0)")
    print(f"  ratio = {fmt(fi / fq, 8)}      (bar-EVEN would be +1)")
    assert abs(fq + fi) > mp.mpf("1e-6"), "delta is not bar-odd"
    assert abs(fi / fq - 1) > mp.mpf("1e-6"), "delta is not bar-even"
    print("  => MIXED bar parity, neither even nor odd.  The corpus's bar-parity")
    print("     arguments (z bar-even, h bar-odd) do NOT extend to delta, and an")
    print("     argument assuming either would be wrong.")
    print()

    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * NOT that the colour weighting is wrong or arbitrary -- only that")
    print("    its landing at trace-zero + h*delta/4 is a CONSEQUENCE of")
    print("    averaging, not evidence for the construction.")
    print("  * NOT that delta is the bar-breaking route 1 asked for.  Route 1's")
    print("    exact antisymmetry is in the eigenvalues of a SINGLE sigma")
    print("    (q and -1/q), where delta does not enter at all.  Different")
    print("    places in the algebra; conflating them is the live temptation.")
    print("  * NOT a binding value.  Nothing wired, nothing fitted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
