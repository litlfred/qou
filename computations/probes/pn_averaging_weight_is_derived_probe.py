"""Class B's averaging escape is closed at the corpus's own delta: |delta| < 2 by ~1453x.

Bean `qou-brng`, escape class B (a bond energy that is not sign-definite).

## Why this exists

The 2026-09-12 entry narrowed class B's open "third bond family" to exactly two
hypotheses, and said so in those terms:

    "a third bond family cannot rescue the pattern by moving letters above 1.
     It must break the AVERAGING of the pn letter, or break AFFINENESS of the
     interface law.  Those are the only two hypotheses used, and neither
     mentions a numerical value."

`QOU/MassTheory/PnBetweennessBlocksSignMixed.lean` carries the averaging half as
`pn_betweenness_blocks_signMixed`, whose hypotheses are `-2 < delta` and
`delta < 2` -- the range on which `corpusWeight delta = 1/2 + delta/4` is a
STRICT convex weight.  Stated that way, `|delta| < 2` reads like an assumption a
third family might violate.

**It is not an assumption.  `delta` is derived, in closed form, and at the
substrate it is ~1453x inside the range.**  So the averaging hypothesis is not a
soft spot in the exclusion; it is satisfied by three orders of magnitude, and
class B's remaining escape is AFFINENESS alone.

## The identification, checked rather than assumed

Two objects are called `delta` here and this probe does not take their identity
on trust -- a homonym across two layers is the recurring failure this corpus
names `da-arity-conflation`.  Section 1 derives the match:

    pyhecke.constants (canonical convention `bring_color_weighted`, owner
    ruling R3 of 2026-08-15, reaffirmed 2026-08-26):

        f_pn = z - h*(1/2 - eps),   eps = delta/4,
        delta = flavor_split_leading(q) = (q-1)^2 (1 - q^-4) / 3
              = hbar_q^2 * h_q * [2]_q / 3

    f_pp = z(q) and f_nn = z(1/q) = z - h  (the constants' own
    `fNN_eq_fPP_bar`), so the weighted mean with weight `w` on f_pp is

        w*z + (1-w)*(z - h) = z - (1-w)*h,

    and matching against `z - h*(1/2 - delta/4)` gives 1-w = 1/2 - delta/4,
    i.e.  **w = 1/2 + delta/4 = corpusWeight delta**, the Lean's definition.

Both halves are verified symbolically in section 1, so the Lean's `delta` and
the producer's `DELTA` are the same object.

## Scope

**Scope (b)** for the averaging half: it discharges a hypothesis of an existing
sorry-free theorem from the corpus's own derived quantity, rather than assuming
it.  It does NOT exclude class B -- affineness of `mu = z + d` is untouched and
is now the sole remaining hypothesis -- and it says nothing about magnitude,
which is `qou-brng`'s real open target.

NO ASSERTION HERE IS A FIT: every number is derived or measured.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_ROOT = _Path(__file__).resolve().parents[2]
for _p in (_ROOT / "computations", _ROOT / "tools" / "qou-substrate" / "python",
           _ROOT / "tools" / "pyhecke" / "python"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402

mp.mp.dps = 70


def hdr(s: str) -> None:
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


def main() -> int:
    from pyhecke.constants import (  # noqa: E402
        flavor_split_leading, pn_interface_offset, PN_CONVENTION,
    )

    Q0 = q_at(dps=70)

    # ------------------------------------------------------------ section 1
    hdr("[1] The Lean's `delta` and the producer's `delta` are the SAME object")

    qs = sp.Symbol("q", positive=True)
    z = qs ** 3 / (qs ** 2 + 1)                      # convention D
    h = qs - 1 / qs
    dsym = (qs - 1) ** 2 * (1 - qs ** -4) / 3        # flavor_split_leading

    # f_nn = z(1/q) equals z - h  (the constants' fNN_eq_fPP_bar)
    z_bar = (1 / qs) ** 3 / ((1 / qs) ** 2 + 1)
    chk_bar = sp.simplify(z_bar - (z - h))
    print(f"  z(1/q) - (z - h)                        = {chk_bar}   (exact)")
    assert chk_bar == 0

    # the weighted mean with weight w on f_pp, matched against the producer
    w = sp.Rational(1, 2) + dsym / 4
    mean = sp.simplify(w * z + (1 - w) * (z - h))
    prod = sp.simplify(z - h * (sp.Rational(1, 2) - dsym / 4))
    chk_w = sp.simplify(mean - prod)
    print(f"  w*f_pp + (1-w)*f_nn  -  (z - h(1/2-d/4)) = {chk_w}   (exact)")
    assert chk_w == 0
    print("\n  So corpusWeight(delta) = 1/2 + delta/4 IS the producer's eps = delta/4")
    print("  convention.  The two `delta` are one object; the identification is")
    print("  derived here, not assumed.")

    # also check the closed form against the alternative spelling in the docstring
    hbar, hq, two_q = 1 - 1 / qs, qs - 1 / qs, qs + 1 / qs
    chk_alt = sp.simplify(dsym - hbar ** 2 * hq * two_q / 3)
    print(f"\n  delta - hbar_q^2 * h_q * [2]_q / 3       = {chk_alt}   (exact)")
    assert chk_alt == 0

    # ------------------------------------------------------------ section 2
    hdr("[2] delta is DERIVED, and at the substrate it is far inside (-2, 2)")

    delta0 = flavor_split_leading(Q0)
    print(f"  convention in force      : {PN_CONVENTION}  (owner ruling R3)")
    print(f"  q0                       : {mp.nstr(Q0, 30)}")
    print(f"  delta(q0)                : {mp.nstr(delta0, 30)}")
    print(f"  corpusWeight = 1/2+d/4   : {mp.nstr(mp.mpf(1)/2 + delta0/4, 30)}")
    print(f"\n  the Lean hypothesis is |delta| < 2.  Margin:")
    print(f"    2 / delta(q0)          = {mp.nstr(2 / delta0, 12)}   <- factor inside")
    assert 0 < delta0 < 2
    assert 2 / delta0 > 1000

    # cross-check the producer's own offset against the closed form
    hq0 = Q0 - 1 / Q0
    d_pn_direct = pn_interface_offset(Q0)
    d_pn_closed = -(hq0 * (1 - delta0 / 2) / 2)
    print(f"\n  pn_interface_offset(q0)  = {mp.nstr(d_pn_direct, 25)}")
    print(f"  -h(1 - delta/2)/2        = {mp.nstr(d_pn_closed, 25)}")
    print(f"  |difference|             = {mp.nstr(abs(d_pn_direct - d_pn_closed), 5)}")
    assert abs(d_pn_direct - d_pn_closed) < mp.mpf(10) ** -60

    # ------------------------------------------------------------ section 3
    hdr("[3] What it would take to reach the boundary, and delta's sign")

    # delta(q) = 2  -- solve on the substrate branch q > 1
    f = sp.lambdify(qs, dsym, "mpmath")
    q_edge = mp.findroot(lambda t: f(t) - 2, mp.mpf("3"))
    print(f"  delta(q) = 2  at  q = {mp.nstr(q_edge, 20)}")
    print(f"  substrate q0        = {mp.nstr(Q0, 20)}")
    print(f"  ratio q_edge / q0   = {mp.nstr(q_edge / Q0, 12)}")
    assert q_edge > 2 * Q0

    print("\n  And delta > 0 for every q > 1, so the weight is ALWAYS above 1/2:")
    for qv in ("1.01", "1.10997858275138080759166909561", "1.5", "2.0"):
        qq = mp.mpf(qv)
        dv = f(qq)
        print(f"    q = {qv:<32s} delta = {mp.nstr(dv, 12):>16s}  "
              f"w = {mp.nstr(mp.mpf(1)/2 + dv/4, 12)}")
        assert dv > 0
    print("\n  The tilt is toward f_pp for every substrate value, never past the")
    print("  hull.  Reaching w = 1 (or w = 0) needs delta = +-2, i.e. a modulus")
    print(f"  more than {mp.nstr(q_edge / Q0, 4)}x the substrate's.")

    # ------------------------------------------------------------ section 4
    hdr("[4] Consequence for class B")

    print(f"""  `pn_betweenness_blocks_signMixed` (sorry-free) rules out the sign-mixed
  pattern whenever `-2 < delta < 2`.  Read as a Lean hypothesis that looks
  like an assumption a third bond family might violate.  It is not:

    * `delta` is DERIVED -- a closed rational function of q, fixed by the
      canonical `bring_color_weighted` convention (owner ruling R3);
    * at the substrate it is {mp.nstr(delta0, 12)}, inside the range by a
      factor of {mp.nstr(2 / delta0, 8)};
    * it is positive for every q > 1, so the weight never even approaches
      either end of (0,1).

  So the AVERAGING half of class B's remaining escape is closed at the
  corpus's own value.  **Affineness of the interface law `mu = z + d` is the
  sole surviving class-B hypothesis**, and it is untouched here.

  NOT claimed: that no third bond family exists; that class B is excluded;
  anything about MAGNITUDE, which is qou-brng's real open target -- the
  question "what derived object puts b_pn more than 5x below both
  like-species bonds" is unaffected by this.""")

    print("\nPROBE OK — all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
