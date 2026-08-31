#!/usr/bin/env python3
"""
wide_isotope_window_test_probe — widening the isotope table from 5 to 12 adds
ZERO new shape exclusions. The move was proposed (by me) as "the highest-value
cheap move"; measured, it is nearly free of information. What it does establish
is WHY, and that is worth more than the widening was.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Follows #6404.

## The proposal, and its measured value

#6404 computed the admissible window for an additive many-body term `T` from the
pairwise bracket, and found `T = c*floor(A/4)` admissible on five isotopes with
`c in [11.1145, 17.4638]` MeV. I proposed widening the table as the next move --
"8Be/9Be/12C would either kill the per-alpha shape or leave it as the last one
standing".

Measured over twelve isotopes (`3H` .. `16O`):

    per-alpha window   5 isotopes: [11.1145, 17.4638]
                      12 isotopes: [11.1145, 17.2392]     -- 1.3 % tighter

and, comparing verdicts shape by shape at 5 vs 12, **ZERO shapes changed
verdict**. Every exclusion available at 12 was already available at `A <= 7`.
The seven extra isotopes only tightened already-empty windows (`C(A,4)` from
`0.6117` down to `0.04607`), which changes nothing that was not already decided.

So the widening was **not** the highest-value move. It was cheap and it was
nearly information-free, and I proposed it.

## Why — and this is the part worth having

Eight shapes tested; exactly one survives, and the reason is NOT a growth rate:

    shape        5 isotopes            12 isotopes           verdict
    C(A,4)       [11.11, 0.6117]       [11.11, 0.04607]      EXCLUDED
    C(A,3)       [2.779, 0.6117]       [2.779, 0.1497]       EXCLUDED
    C(A,2)       [1.852, 0.7806]       [1.852, 0.6987]       EXCLUDED
    A            [2.779, 0.7806]       [2.779, 0.7806]       EXCLUDED
    sqrt(A)      [5.557, 1.352]        [5.557, 1.352]        EXCLUDED
    1            [11.11, 2.342]        [11.11, 2.342]        EXCLUDED
    max(A-3,0)   [11.11, 5.352]        [11.11, 5.352]        EXCLUDED
    floor(A/4)   [11.11, 17.46]        [11.11, 17.24]        ADMISSIBLE

**`A` is excluded while `floor(A/4)` survives**, though `A` is four times larger
asymptotically. So the discriminator cannot be how fast the shape grows. Two
separate constraints do the work, and both come from the SMALL end of the table:

  1. **It must vanish at `A = 3`.** The A=3 window is narrow (`T <= 2.34`) while
     4He demands `T >= 11.11`, so any shape non-zero at A=3 is caught between
     them. That kills `1`, `sqrt(A)`, `A`, `C(A,2)`, `C(A,3)`.
  2. **It must not increment before `A = 8`.** 6Li caps `c` at `17.46` with one
     alpha; a shape already at 3 by A=6 (like `max(A-3,0)`) needs `c <= 5.82`
     there, tightened to `5.35` by 7Li, while 4He demands `>= 11.11`. That
     kills `max(A-3,0)` even though it satisfies (1), and `C(A,4)` fails on the
     large end instead.

What survives is therefore not "a slowly growing function" but specifically **a
step function counting COMPLETE 4-blocks**: zero below 4, one at 4 through 7,
incrementing at 8.

## The honest caveat, and it is large

`floor(A/4)` is *built* to satisfy exactly those two constraints. Testing a
family chosen after seeing them and reporting the one that fits is close to
circular, so its survival is **weak evidence**, not support. The defensible
statement is the negative one: **everything else tested is excluded, and the
surviving family is narrow** -- any shape counting complete 4-blocks is
indistinguishable from `floor(A/4)` on this data, and the test cannot choose
among them.

## Scope

Scope **(a)**: a measurement plus a correction to my own proposal. No term is
proposed, derived or fitted; `c in [11.11, 17.24]` remains a CONSTRAINT and
choosing a value inside it against AME would be a fit.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin, exact `math.comb`.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import json  # noqa: E402
from math import comb  # noqa: E402  # float64-ok: exact int, never float

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 50

NARROW = [("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3),
          ("7Li", 3, 4)]
EXTRA = [("8Be", 4, 4), ("9Be", 4, 5), ("10B", 5, 5), ("11B", 5, 6),
         ("12C", 6, 6), ("14N", 7, 7), ("16O", 8, 8)]

SHAPES = (
    ("C(A,4)", lambda A: mp.mpf(comb(A, 4))),
    ("C(A,3)", lambda A: mp.mpf(comb(A, 3))),
    ("C(A,2)", lambda A: mp.mpf(comb(A, 2))),
    ("A", lambda A: mp.mpf(A)),
    ("sqrt(A)", lambda A: mp.sqrt(A)),
    ("1", lambda A: mp.mpf(1)),
    ("max(A-3,0)", lambda A: mp.mpf(max(A - 3, 0))),
    ("floor(A/4)", lambda A: mp.mpf(A // 4)),
)


def fmt(x, n=6):
    return mp.nstr(x, n)


def main() -> int:
    from codata_constants import M_E_MEV as _me
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h = q0 - 1 / q0
    z = q0**3 / (q0**2 + 1)
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    al = me / (q0 * (q0 - 1))
    dlt = flavor_split_leading(q0)
    wr = mp.log(1 - h)

    def L(d, e):
        return -mp.log(z + d) - (e / 2) * wr

    Lpp = L(mp.mpf(0), mp.mpf(1))
    Lnn = L(-h, mp.mpf(-1))
    Lpn = L(-h * (mp.mpf(1) / 2 - dlt / 4), mp.mpf(0))

    p = _Path(__file__).resolve().parent / "data" / "ame2020.json"
    raw = json.loads(p.read_text())
    ent = raw["entries"] if isinstance(raw, dict) and "entries" in raw else raw
    rows = ent.values() if isinstance(ent, dict) else ent
    B = {(r["Z"], r["A"]): mp.mpf(str(r["binding_energy_total_keV"])) / 1000
         for r in rows if r.get("binding_energy_total_keV") is not None}

    def windows(lst):
        W = {}
        for nm, Z, N in lst:
            A = Z + N
            assert (Z, A) in B, f"{nm} missing from the AME table"
            ch = al * ((Z - 1) * Lpp + Lpn + (N - 1) * Lnn)
            ap = al * (comb(Z, 2) * Lpp + Z * N * Lpn + comb(N, 2) * Lnn)
            W[nm] = (B[(Z, A)] - ap, B[(Z, A)] - ch, A)
        return W

    def verdict(W, f):
        los, his = [], []
        for _nm, (lo, hi, A) in W.items():
            k = f(A)
            if k == 0:
                if not (lo <= 0 <= hi):
                    return None, "EXCLUDED (zero-at-A)"
                continue
            los.append(lo / k)
            his.append(hi / k)
        cmin, cmax = max(los), min(his)
        return (cmin, cmax), ("ADMISSIBLE" if cmin <= cmax else "EXCLUDED")

    Wn, Ww = windows(NARROW), windows(NARROW + EXTRA)

    print("wide_isotope_window_test_probe")
    print("=" * 78)
    print("THE PROPOSAL (mine, after #6404): widen the isotope table, because")
    print("'8Be/9Be/12C would either kill the per-alpha shape or leave it as the")
    print("last one standing'.  Measured below.")
    print()
    print(f"{'shape':>12} | {'5 isotopes (A<=7)':>30} | "
          f"{'12 isotopes (A<=16)':>30} | {'new?':>10}")
    n_new = 0
    for name, f in SHAPES:
        rn, vn = verdict(Wn, f)
        rw, vw = verdict(Ww, f)
        sn = (f"[{fmt(rn[0], 4)}, {fmt(rn[1], 4)}] {vn}" if rn else vn)
        sw = (f"[{fmt(rw[0], 4)}, {fmt(rw[1], 4)}] {vw}" if rw else vw)
        new = "NEW at 12" if (vn == "ADMISSIBLE" and vw != "ADMISSIBLE") else ""
        if new:
            n_new += 1
        print(f"{name:>12} | {sn:>30} | {sw:>30} | {new:>10}")
    print()
    print(f"  shapes whose verdict CHANGED when the table widened: {n_new}")
    assert n_new == 0, "if any verdict changed, the premise was right after all"
    print("  => ZERO.  Every exclusion available at 12 was already available at")
    print("     A <= 7.  The seven extra isotopes only tightened already-EMPTY")
    print("     windows, which decides nothing that was not already decided.")
    print()
    per_alpha = dict(SHAPES)["floor(A/4)"]
    rn, _ = verdict(Wn, per_alpha)
    rw, _ = verdict(Ww, per_alpha)
    tighten = (rn[1] - rw[1]) / rn[1] * 100
    print(f"  per-alpha window   5 isotopes: [{fmt(rn[0], 7)}, {fmt(rn[1], 7)}]")
    print(f"                    12 isotopes: [{fmt(rw[0], 7)}, {fmt(rw[1], 7)}]"
          f"   -- {fmt(tighten, 3)} % tighter")
    assert tighten < 5, "the tightening should be marginal, as measured"
    print()
    print("  SO THE WIDENING WAS NOT THE HIGHEST-VALUE MOVE.  It was cheap and")
    print("  nearly information-free, and I proposed it.")
    print()

    print("WHY — and the discriminator is NOT a growth rate")
    print("-" * 78)
    print("  `A` is EXCLUDED while `floor(A/4)` SURVIVES, though `A` is four")
    print("  times larger asymptotically.  So how fast a shape grows cannot be")
    print("  what decides it.  Two constraints do the work, both from the SMALL")
    print("  end of the table:")
    print()
    lo3, hi3, _ = Wn["3H"]
    lo4, hi4, _ = Wn["4He"]
    lo6, hi6, _ = Wn["6Li"]
    print(f"  1. MUST VANISH AT A = 3.  The A=3 window is narrow "
          f"(T <= {fmt(hi3, 5)})")
    print(f"     while 4He demands T >= {fmt(lo4, 6)}, so any shape non-zero at")
    print("     A=3 is caught between them.  Kills 1, sqrt(A), A, C(A,2), C(A,3).")
    print()
    print(f"  2. MUST NOT INCREMENT BEFORE A = 8.  6Li caps c at "
          f"{fmt(hi6, 6)} with")
    print("     one alpha; a shape already at 3 by A=6 (max(A-3,0)) needs")
    print(f"     c <= {fmt(hi6 / 3, 5)} there (tightened to "
          f"{fmt(verdict(Wn, dict(SHAPES)['max(A-3,0)'])[0][1], 5)} by 7Li)")
    print(f"     while 4He demands >= {fmt(lo4, 6)}.  Kills max(A-3,0) even")
    print("     though it satisfies (1).  C(A,4) instead fails on the large end.")
    print()
    print("  What survives is therefore not 'a slowly growing function' but")
    print("  specifically a STEP FUNCTION COUNTING COMPLETE 4-BLOCKS: zero below")
    print("  4, one at 4 through 7, incrementing at 8.")
    print()

    print("THE HONEST CAVEAT, AND IT IS LARGE")
    print("-" * 78)
    print("  floor(A/4) is BUILT to satisfy exactly those two constraints.")
    print("  Testing a family chosen after seeing them, and reporting the one")
    print("  that fits, is close to circular -- so its survival is WEAK EVIDENCE,")
    print("  not support.")
    print()
    print("  The defensible statement is the negative one: everything else")
    print("  tested is excluded, and the surviving family is NARROW.  Any shape")
    print("  counting complete 4-blocks is indistinguishable from floor(A/4) on")
    print("  this data, and the test cannot choose among them.")
    print()
    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * No term is proposed, derived or fitted.  c in [11.11, 17.24] is a")
    print("    CONSTRAINT; picking a value inside it against AME would be a fit.")
    print("  * NOT that a per-alpha term is right -- only that this test cannot")
    print("    exclude it, having excluded seven alternatives.")
    print("  * Admissibility stays necessary, not sufficient: it says a pairwise")
    print("    bond set EXISTS, not that the framework derives it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
