#!/usr/bin/env python3
"""
chain_bond_arrangement_dependence_probe — instantiating ChainBondOrderDependence on
the live producer, and measuring what its hypothesis actually costs.

Bean `qou-brng`, arc `bk-crossing-mass-binding`; related `qou-48is`.

## The question

`QOU.MassTheory.ChainBondOrderDependence` (sorry-free, on `main`) proves

    orderIndependent_iff        : the chain bond sum is invariant under every
                                  rearrangement  IFF  L_pp = L_pn = L_nn
    not_orderIndependent_of_ne  : L_pp ≠ L_nn  ⟹  arrangement-dependent, every A ≥ 3

That is a theorem about a generic scalar `L`. It says nothing on its own about any
producer — the arity discipline (AGENTS.md §"Grep the claim SHAPE"): a conditional
lemma proves the implication, never the premise. This probe supplies the premise
for the live producer and then measures the consequence.

`computations/closed_form_tau_M.py::closed_form_ratio` is a CHAIN: it loops
`for k_idx in range(A - 1)` over adjacent pairs of a hardcoded ordering
`["p"]*Z + ["n"]*N`, multiplying one factor per adjacent pair:

    L_pp = z
    L_nn = z − h
    L_pn = z − h·(1/2 − δ/4)      δ = flavor_split_leading(q)

So the hypothesis `L_pp ≠ L_nn` reduces to `h ≠ 0`, i.e. `q ≠ 1` — which holds at
every substrate pin. Checked here rather than asserted.

## What is measured

1. The three factors, and the exact gaps `L_pp − L_nn` and `L_pp − L_pn`.
2. `closed_form_ratio`'s chain product over EVERY arrangement of the multiset (for
   small A) or over a spanning set of arrangements (larger A), and the spread.
3. Which arrangement the producer actually uses, and where it sits in that spread.

## Scope

Scope **(a)** throughout. This does not say the chain is the wrong bond set for the
physics; it measures that the chain observable is not a function of `(Z, N)` alone,
so a number read off it carries an undetermined factor set by a convention nothing
in the corpus derives. The complete-graph path has the same defect measured
independently in `qou-48is` (O(10 %) for `tr_M` at A ≥ 3).

Multiplicativity note: the chain product depends on the arrangement ONLY through the
multiset of adjacent-pair kinds `(n_pp, n_pn, n_nn)` with `n_pp + n_pn + n_nn = A−1`.
So enumerating arrangements is enumerating attainable bond multisets, and the extreme
arrangements are the ones minimising and maximising `n_pn`.

NO FLOAT64: mpmath `mpf` throughout at 50 dps; `float` appears nowhere. The q₀ pin is
the experimental (proton) default per AGENTS.md §q₀ anchor convention.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from itertools import combinations  # noqa: E402

import mpmath as mp  # noqa: E402

from closed_form_tau_M import markov_z, hecke_h  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import q_at  # noqa: E402

mp.mp.dps = 50


def chain_factors(q: mp.mpf) -> dict[str, mp.mpf]:
    """The three adjacent-pair factors, exactly as `closed_form_ratio` builds them
    in its `bring_color_weighted` branch (the canonical p/n convention)."""
    z = markov_z(q)
    h = hecke_h(q)
    delta = flavor_split_leading(q)
    return {
        "pp": z,
        "nn": z - h,
        "pn": z - h * (mp.mpf(1) / 2 - delta / 4),
    }


def chain_product(ordering: tuple[str, ...], L: dict[str, mp.mpf]) -> mp.mpf:
    """`closed_form_ratio`'s product, for an arbitrary ordering."""
    prod = mp.mpf(1)
    for a, b in zip(ordering, ordering[1:]):
        prod *= L["pp"] if a == b == "p" else (L["nn"] if a == b == "n" else L["pn"])
    return prod


def bond_multiset(ordering: tuple[str, ...]) -> tuple[int, int, int]:
    npp = npn = nnn = 0
    for a, b in zip(ordering, ordering[1:]):
        if a == b == "p":
            npp += 1
        elif a == b == "n":
            nnn += 1
        else:
            npn += 1
    return (npp, npn, nnn)


def all_orderings(Z: int, N: int):
    """Every DISTINCT arrangement of Z protons and N neutrons, as C(A,Z) tuples.

    Enumerated by choosing the proton positions. `set(permutations(...))` is the
    obvious spelling and is wrong: it generates `A!` tuples before deduplicating,
    which is 87 billion at A=14 rather than the 3432 distinct arrangements.
    """
    A = Z + N
    out = []
    for pos in combinations(range(A), Z):
        s = set(pos)
        out.append(tuple("p" if i in s else "n" for i in range(A)))
    return out


def fmt(x, n=12):
    return mp.nstr(x, n)


def main() -> int:
    q = q_at()  # experimental (proton) pin — AGENTS.md standing directive
    L = chain_factors(q)

    print("chain_bond_arrangement_dependence_probe")
    print("=" * 78)
    print(f"q0 (proton pin)  = {fmt(q, 20)}")
    print(f"z  = markov_z(q) = {fmt(L['pp'], 20)}")
    print(f"h  = hecke_h(q)  = {fmt(hecke_h(q), 20)}")
    print(f"delta            = {fmt(flavor_split_leading(q), 20)}")
    print()

    print("STEP 1 — the hypothesis of ChainBondOrderDependence.not_orderIndependent_of_ne")
    print(f"  L_pp = z                  = {fmt(L['pp'], 20)}")
    print(f"  L_pn = z - h(1/2 - d/4)   = {fmt(L['pn'], 20)}")
    print(f"  L_nn = z - h              = {fmt(L['nn'], 20)}")
    print(f"  L_pp - L_nn = h           = {fmt(L['pp'] - L['nn'], 20)}")
    print(f"  L_pp - L_pn               = {fmt(L['pp'] - L['pn'], 20)}")
    print(f"  L_pn - L_nn               = {fmt(L['pn'] - L['nn'], 20)}")
    ne = L["pp"] != L["nn"]
    all_ne = ne and L["pp"] != L["pn"] and L["pn"] != L["nn"]
    print(f"  hypothesis  L_pp != L_nn                : {ne}")
    print(f"  all three pairwise distinct             : {all_ne}")
    print("  => the theorem's antecedent HOLDS at the live pin, so its conclusion")
    print("     applies to this producer: the chain product is arrangement-dependent")
    print("     at every A >= 3.  What follows measures by how much.")
    print()

    print("STEP 2 — the spread over arrangements, and where the producer sits")
    print("  'canonical' = the ordering closed_form_ratio hardcodes, ['p']*Z+['n']*N")
    print(f"{'nucleus':>8} {'Z':>3} {'N':>3} {'#ord':>6} {'#bondsets':>10} "
          f"{'min':>16} {'max':>16} {'max/min':>12} {'canon rank':>11}")
    NUCLEI = [("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3),
              ("7Li", 3, 4), ("9Be", 4, 5), ("12C", 6, 6), ("14N", 7, 7)]
    rows = []
    for name, Z, N in NUCLEI:
        orders = all_orderings(Z, N)
        vals = {}
        for o in orders:
            vals[o] = chain_product(o, L)
        bondsets = {bond_multiset(o) for o in orders}
        vmin, vmax = min(vals.values()), max(vals.values())
        canon = tuple(["p"] * Z + ["n"] * N)
        vcanon = vals[canon]
        # rank of the canonical value among the DISTINCT attainable values
        distinct = sorted({mp.nstr(v, 30) for v in vals.values()})
        rank = distinct.index(mp.nstr(vcanon, 30)) + 1
        ratio = vmax / vmin
        print(f"{name:>8} {Z:>3} {N:>3} {len(orders):>6} {len(bondsets):>10} "
              f"{fmt(vmin, 10):>16} {fmt(vmax, 10):>16} {fmt(ratio, 8):>12} "
              f"{f'{rank}/{len(distinct)}':>11}")
        rows.append((name, Z, N, vmin, vmax, vcanon, ratio, len(distinct)))
    print()

    print("STEP 3 — the canonical arrangement against the extremes")
    print("  rel = (v_canon - v) / v_canon,  i.e. how far the reported number would")
    print("  move if a different arrangement of the SAME (Z, N) were chosen.")
    print(f"{'nucleus':>8} {'canonical':>18} {'vs min':>11} {'vs max':>11} "
          f"{'canon bonds':>13} {'argmin bonds':>14} {'argmax bonds':>14}")
    for name, Z, N, vmin, vmax, vcanon, ratio, ndist in rows:
        canon = tuple(["p"] * Z + ["n"] * N)
        bm = bond_multiset(canon)
        # which bond multiset attains each extreme
        bmin = bmax = None
        for o in all_orderings(Z, N):
            v = chain_product(o, L)
            if v == vmin and bmin is None:
                bmin = bond_multiset(o)
            if v == vmax and bmax is None:
                bmax = bond_multiset(o)
        rmin = (vcanon - vmin) / vcanon
        rmax = (vcanon - vmax) / vcanon
        print(f"{name:>8} {fmt(vcanon, 12):>18} {fmt(rmin, 6):>11} "
              f"{fmt(rmax, 6):>11} {str(bm):>13} {str(bmin):>14} {str(bmax):>14}")
    print()
    # The 'vs min' column is the SAME number for every nucleus with Z,N >= 1, and
    # the argmin column says why: canonical is (n_pp, 1, n_nn) and the argmin is
    # (n_pp - 1, 2, n_nn) -- exactly ONE pp -> pn swap.  So the ratio is L_pn/L_pp
    # with everything else cancelling, independent of A, Z and N.
    predicted = hecke_h(q) * (mp.mpf(1) / 2 - flavor_split_leading(q) / 4) / L["pp"]
    observed = [(vcanon - vmin) / vcanon
                for (_n, Z, N, vmin, _vx, vcanon, _r, _d) in rows if Z >= 1 and N >= 1
                and bond_multiset(tuple(["p"] * Z + ["n"] * N))[0] >= 1]
    print("  The 'vs min' column is constant, and the argmin column says why:")
    print("  canonical is (n_pp, 1, n_nn) and argmin is (n_pp - 1, 2, n_nn) -- exactly")
    print("  one pp -> pn swap, so everything else cancels and the ratio is")
    print("      1 - L_pn/L_pp  =  h(1/2 - d/4) / z,")
    print("  independent of A, Z and N.  Checked, not asserted:")
    print(f"      predicted  h(1/2-d/4)/z = {fmt(predicted, 20)}")
    for v in observed[:1]:
        print(f"      observed   1 - vmin/vcanon = {fmt(v, 20)}")
    agree = all(abs(v - predicted) < mp.mpf(10) ** (-40) for v in observed)
    print(f"      agree to 1e-40 on all {len(observed)} nuclei with n_pp >= 1: {agree}")
    print()

    print("STEP 4 — why the canonical ordering is always an EXTREME, not a middle")
    print("  The chain product depends on the arrangement only through (n_pp, n_pn,")
    print("  n_nn).  ['p']*Z+['n']*N attains the MINIMUM possible n_pn (exactly 1 for")
    print("  Z,N >= 1), which is the interface-minimality the module docstring cites.")
    print(f"{'nucleus':>8} {'canon n_pn':>11} {'min n_pn':>9} {'max n_pn':>9} "
          f"{'canon is argmin?':>17}")
    for name, Z, N in NUCLEI:
        orders = all_orderings(Z, N)
        pns = [bond_multiset(o)[1] for o in orders]
        canon_pn = bond_multiset(tuple(["p"] * Z + ["n"] * N))[1]
        print(f"{name:>8} {canon_pn:>11} {min(pns):>9} {max(pns):>9} "
              f"{str(canon_pn == min(pns)):>17}")
    print()

    print("Reading")
    print("-" * 78)
    print("  * The antecedent of not_orderIndependent_of_ne HOLDS for this producer:")
    print("    L_pp - L_nn = h != 0 at the live pin, exactly.  So the theorem applies")
    print("    and the chain observable is arrangement-dependent at every A >= 3.")
    print("  * The producer resolves that dependence by HARDCODING one arrangement,")
    print("    the interface-minimal ['p']*Z+['n']*N.  That is a cost property, not")
    print("    a selection rule -- the same gap qou-48is records for the")
    print("    complete-graph path, where the orbit identity ranges over S_Z x S_N")
    print("    and so never compares two different arrangements.")
    print("  * Scope (a).  The spread measured above is the size of an undetermined")
    print("    convention factor, not evidence that the chain is the wrong bond set.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
