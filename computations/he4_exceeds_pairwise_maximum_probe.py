#!/usr/bin/env python3
"""
he4_exceeds_pairwise_maximum_probe — 4He is the ONLY low isotope whose binding
exceeds the complete-graph pairwise maximum. No pairwise bond set on four
nucleons can reach it. The other five are not a single problem with it: two sit
inside the pairwise bracket and one sits below its minimum.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Localises what is left after
#6401 refuted the p-n-letter mechanism and the colour weighting was measured at
~1e-4.

## What is left to explain, and why it needed splitting

The arc has treated "the binding error" as one thing. It is not. Bracketing each
isotope between the two extreme pairwise bond sets separates it cleanly:

    B_chain    = alpha [ (Z-1) L_pp + L_pn + (N-1) L_nn ]     A-1 bonds, the MINIMUM
    B_allpairs = alpha [ C(Z,2) L_pp + Z N L_pn + C(N,2) L_nn ]  C(A,2), the MAXIMUM

Every pairwise bond graph on A nucleons has a bond multiset between these two, so
any pairwise model's prediction lies in `[B_chain, B_allpairs]`. Asking where
`B_AME` falls relative to that interval is a structural question with no free
parameter in it.

## The result — three regimes, not one

    iso   Z N   B_chain  B_allpairs    B_AME   AME/allpairs   verdict
    2H    1 1   2.833163   2.833163   2.224566   0.78519      BELOW both
    3H    1 2   6.140069   8.973232   8.481796   0.94523      INSIDE
    3He   2 1   5.374749   8.207911   7.718041   0.94032      INSIDE
    4He   2 2   8.681655  17.181140  28.295660   1.64690      ABOVE both
    6Li   3 3  14.530150  43.043940  31.993990   0.74329      INSIDE
    7Li   3 4  17.837050  61.464150  39.245080   0.63850      INSIDE

  * **4He is ABOVE the pairwise maximum**, by a factor 1.6469 -- an excess of
    11.11 MeV beyond what ALL SIX pairs can supply. This is not "the pairwise
    model needs a better graph"; it is a proof that no graph suffices, since the
    complete graph is the largest one there is.
  * **2H is BELOW the pairwise minimum.** At A = 2 the chain and the complete
    graph coincide (one bond), so the single p-n bond ALONE over-binds by 27 %.
    That is a different defect: too much energy in one bond, not too little in
    the graph.
  * **3H, 3He, 6Li, 7Li are INSIDE.** For each, some pairwise bond multiset
    reproduces AME exactly. Their problem is WHICH graph -- a coordination
    question -- not a missing many-body term.

## Why this matters for where to look next

The three regimes have different causes and cannot share a fix:

  * a many-body (alpha-cluster) term is REQUIRED at 4He and is not optional --
    the pairwise ceiling is a hard bound, not a tuning range;
  * the same term is NOT required at 3H, 3He, 6Li or 7Li, all of which are
    already reachable pairwise, so a term calibrated at 4He and applied
    uniformly would push them further out;
  * and 2H needs the opposite sign of correction from everything else.

That the alpha-cluster excess does NOT persist into 6Li and 7Li -- both of which
have alpha substructure and both of which sit comfortably inside -- is the part
that should discipline any proposed 4-body term.

## Scope

Scope **(a)**: a bracketing measurement. Nothing is wired, no many-body term is
proposed or fitted, and AME is used only as the comparison target -- never
inverted into a weight. The bond constants come from `q0` through the production
dashboard's closed form.

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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50

ISO = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
       ("6Li", 3, 3), ("7Li", 3, 4)]


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    from codata_constants import M_E_MEV as _me
    q0 = Q_MP
    h = q0 - 1 / q0
    z = q0**3 / (q0**2 + 1)
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    al = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    dlt = flavor_split_leading(q0)
    wr = mp.log(1 - h)

    def L(d, e):
        return -mp.log(z + d) - (e / 2) * wr

    Lpp = L(mp.mpf(0), mp.mpf(1))
    Lnn = L(-h, mp.mpf(-1))
    Lpn = L(-h * (mp.mpf(1) / 2 - dlt / 4), 2 * (mp.mpf(1) / 2 - dlt / 4) - 1)

    p = _Path(__file__).resolve().parent / "data" / "ame2020.json"
    raw = json.loads(p.read_text())
    ent = raw["entries"] if isinstance(raw, dict) and "entries" in raw else raw
    rows = ent.values() if isinstance(ent, dict) else ent
    B = {(r["Z"], r["A"]): mp.mpf(str(r["binding_energy_total_keV"])) / 1000
         for r in rows if r.get("binding_energy_total_keV") is not None}

    print("he4_exceeds_pairwise_maximum_probe")
    print("=" * 78)
    print("THE BRACKET.  Every pairwise bond graph on A nucleons has a bond")
    print("multiset between the CHAIN (A-1 bonds, the minimum connected set) and")
    print("the COMPLETE GRAPH (C(A,2) bonds, the maximum).  So any pairwise")
    print("model's prediction lies in [B_chain, B_allpairs].  Where B_AME falls")
    print("relative to that interval is structural -- no free parameter in it.")
    print()
    print(f"{'iso':>5} {'Z':>2} {'N':>2} {'B_chain':>11} {'B_allpairs':>12} "
          f"{'B_AME':>11} {'AME/chain':>10} {'AME/allpairs':>13} {'verdict':>12}")
    verdicts = {}
    for nm, Z, N in ISO:
        A = Z + N
        ch = al * ((Z - 1) * Lpp + Lpn + (N - 1) * Lnn)
        ap = al * (comb(Z, 2) * Lpp + Z * N * Lpn + comb(N, 2) * Lnn)
        ame = B[(Z, A)]
        if ame > ap:
            v = "ABOVE both"
        elif ame < ch:
            v = "BELOW both"
        else:
            v = "INSIDE"
        verdicts[nm] = (v, ch, ap, ame)
        print(f"{nm:>5} {Z:>2} {N:>2} {fmt(ch, 7):>11} {fmt(ap, 7):>12} "
              f"{fmt(ame, 7):>11} {fmt(ame / ch, 5):>10} "
              f"{fmt(ame / ap, 5):>13} {v:>12}")
    print()

    above = [k for k, (v, *_r) in verdicts.items() if v == "ABOVE both"]
    below = [k for k, (v, *_r) in verdicts.items() if v == "BELOW both"]
    inside = [k for k, (v, *_r) in verdicts.items() if v == "INSIDE"]
    assert above == ["4He"], "4He must be the unique isotope above the maximum"
    assert below == ["2H"], "2H must be the unique isotope below the minimum"
    assert set(inside) == {"3H", "3He", "6Li", "7Li"}, "the rest must be inside"

    print("THREE REGIMES, NOT ONE")
    print("-" * 78)
    _v, ch4, ap4, ame4 = verdicts["4He"]
    print(f"  ABOVE the pairwise maximum: {above}")
    print(f"    4He needs {fmt(ame4 / ap4, 6)}x what ALL SIX pairs can supply --")
    print(f"    an excess of {fmt(ame4 - ap4, 6)} MeV BEYOND the complete graph.")
    print("    This is not 'the pairwise model needs a better graph': the")
    print("    complete graph is the largest graph there is, so it is a proof")
    print("    that NO pairwise bond set suffices.  A many-body term is REQUIRED")
    print("    here, not optional.")
    print()
    _v, ch2, ap2, ame2 = verdicts["2H"]
    print(f"  BELOW the pairwise minimum: {below}")
    print(f"    at A = 2 the chain and complete graph COINCIDE ({fmt(ch2, 6)} =")
    print(f"    {fmt(ap2, 6)}, one bond), so the single p-n bond ALONE over-binds")
    print(f"    by {fmt((ch2 / ame2 - 1) * 100, 4)} %.  A different defect: too")
    print("    much energy in one bond, not too little in the graph -- and it")
    print("    needs the OPPOSITE sign of correction from 4He.")
    print()
    print(f"  INSIDE the bracket: {inside}")
    print("    for each of these, some pairwise bond multiset reproduces AME")
    print("    exactly.  Their problem is WHICH GRAPH -- a coordination question")
    print("    -- not a missing many-body term.")
    print()

    print("WHAT SHOULD DISCIPLINE ANY PROPOSED 4-BODY TERM")
    print("-" * 78)
    print("  6Li and 7Li BOTH have alpha substructure (alpha+d and alpha+t) and")
    print("  BOTH sit comfortably inside the pairwise bracket:")
    for nm in ("6Li", "7Li"):
        _v, ch_, ap_, ame_ = verdicts[nm]
        print(f"    {nm}: AME/allpairs = {fmt(ame_ / ap_, 6)}  "
              f"(head-room to the maximum: {fmt(ap_ - ame_, 6)} MeV)")
    print()
    print("  So the alpha-cluster excess does NOT simply persist up the table.")
    print("  A 4-body term calibrated at 4He and applied uniformly would push")
    print("  6Li and 7Li FURTHER out, not closer.  Whatever the term is, it has")
    print("  to switch off -- or be absorbed -- once the alpha is embedded in a")
    print("  larger nucleus.  That is a strong constraint and it is free: it")
    print("  comes from the bracket, not from a fit.")
    print()

    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * NOT a many-body term.  None is proposed, derived or fitted here.")
    print("  * NOT that the INSIDE isotopes are solved -- only that a pairwise")
    print("    bond set exists that would reach them.  Which graph, and whether")
    print("    the framework derives it, is untouched.")
    print("  * NOT that 4He's excess is 'the alpha cluster'.  The measurement is")
    print("    that it is super-pairwise; naming the mechanism is a separate job.")
    print("  * AME is the comparison target ONLY, never inverted into a weight.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
