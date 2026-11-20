#!/usr/bin/env python3
"""The size-only cumulant recursion, written up: what it is, why it is exact,
what it costs, and the first order-six datum it reaches.

WHAT THE RECURSION IS
---------------------
The arc measures `L_S = log(tr_free / tr_S)` with bonds placed among the
nucleons in `S`, and reads the many-body content off the Mobius cumulants over
subsets, `cum L S = L S - sum_{T strictly inside S} cum L T`. That is `2^A - A
- 1` traces at `n = 3A` strands. For an EXCHANGEABLE system -- every nucleon
the same, so `L_S` depends only on `|S|` -- the cumulants depend only on `|S|`
too, and the whole lattice collapses to a scalar recursion in the size:

    c_k  =  L_k  -  sum_{j=2}^{k-1}  C(k, j) . c_j .

That is the `c_k`-only recursion the owner asked for. It is not a model or an
approximation: `QOU.Mass.SubsetCumulantRecursion.cum_eq_sizeCum` proves it for
every set function on every commutative ring, given only that `L` depends on
cardinality alone. Its two inputs are facts about THIS trace, both established
at 200 bits by `the_binding_arc_was_measured_in_float64_probe`:

  * **exchangeability** -- the homonuclear `L_S` depends only on `|S|`
    (spreads `1e-59` at `A = 3, 4, 5`), and
  * **n-independence** -- `L_S` does not see nucleons outside `S` at all, so
    `L_k` can be computed in its own minimal system, `n = 3k`, instead of the
    ambient `n = 3A`.

WHAT IT COSTS, AND WHAT THAT BUYS
---------------------------------
    A    full Mobius, ambient          size-only + minimal-n
    4     11 traces at n = 12           3 pairs at n = 6, 9, 12
    5     26 traces at n = 15           4 pairs at n = 6 .. 15
    6     57 traces at n = 18           5 pairs, ONE of them at n = 18
    7    120 traces at n = 21           6 pairs, one at n = 21

The exact engine reaches `n = 15` in seconds per trace and `n = 18` in hours
per trace (largest block dimension `13260`). Full Mobius at `A = 6` is 57 of
those hours; the recursion is two. That is the difference between an order-six
datum existing and not.

THE FIRST ORDER-SIX DATUM
-------------------------
Homonuclear `A = 6` (`nnnnnn`), 128-bit MPFR, minimal-n route
(`computations/_exact_trace_runs/a6nn.py` on `computations/_exact_trace_engine.py`).
`L_2 .. L_5` come from `n = 6, 9, 12, 15`; `L_6` from two traces at `n = 18`.
The raw values are committed as the sidecar `*.a6_exact.json`; everything
below is re-derived from them at run time, and cross-checked against the
INDEPENDENT `A = 5` ambient run
(`the_binding_arc_was_measured_in_float64_probe.a5_exact.nnnnn.json`, 200-bit,
all 26 subsets at `n = 15`) at the four sizes the two share:

  * `L_2 .. L_5`, minimal-n vs ambient `n = 15` -- the n-independence check
    at `k = 4` across `n = 12` vs `n = 15`, at `k = 3` across `n = 9` vs `15`,
    at `k = 2` across `n = 6` vs `15`;
  * `c_2 .. c_5`, recursion vs the full 26-subset Mobius.

The result section is printed by the probe; the numbers are not restated here
so that the docstring cannot drift from the sidecar.

WHAT THIS IS NOT
----------------
It is the exchangeable case only. `6He` (`pnpnnn`) is not exchangeable, its
cumulants need the full lattice, and 57 traces at `n = 18` are out of reach
exactly. One order-six datum, in the one system where the recursion applies,
is what exists. Whether the hierarchy converges is not settled by one more
term; the A=5 ordering sweep already showed the ratio straddling 1.

Bean `qou-wx83` (precision) / `t7qv` (mass/binding gap).
"""
from __future__ import annotations

import json
import sys
from itertools import combinations
from math import comb
from pathlib import Path

COMP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
STEM = Path(__file__).stem
A6_SIDE = HERE / f"{STEM}.a6_exact.json"
A5_SIDE = HERE / "the_binding_arc_was_measured_in_float64_probe.a5_exact.nnnnn.json"


def size_only(Lk: dict, kmax: int) -> dict:
    cs: dict = {}
    for k in range(2, kmax + 1):
        cs[k] = Lk[k] - sum(comb(k, j) * cs[j] for j in range(2, k))
    return cs


def full_mobius(Ls: dict, A: int):
    cum: dict = {}
    for r in range(2, A + 1):
        for S in combinations(range(A), r):
            c = Ls[S]
            for m in range(2, r):
                c -= sum(cum[T] for T in combinations(S, m))
            cum[S] = c
    return cum


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    if not A6_SIDE.exists():
        print(f"\n  A=6 sidecar absent: {A6_SIDE.name}")
        return 1
    d6 = json.load(open(A6_SIDE))
    bits6 = int(d6["bits"])
    floor6 = mp.mpf(2) ** (-(bits6 - 12))
    L6 = {int(k): mp.mpf(v) for k, v in d6["L"].items()}
    print(f"\nA=6 sidecar: {bits6} bits, L_k for k = {sorted(L6)}   "
          f"(cross-check floor {mp.nstr(floor6, 3)})")
    kmax = max(L6)
    if kmax < 6:
        print("  NOTE: sidecar is PARTIAL -- L_6 not yet landed; order-six section skipped")

    print("\n" + "=" * 68)
    print("§1  L_k IN ITS OWN MINIMAL SYSTEM vs THE AMBIENT n=15 RUN")
    print("=" * 68)
    have5 = A5_SIDE.exists()
    if have5:
        d5 = json.load(open(A5_SIDE))
        L5 = {tuple(int(x) for x in k.strip("()").split(",") if x.strip()): mp.mpf(v)
              for k, v in d5["L"].items()}
        worst_n = mp.mpf(0)
        for k in range(2, min(kmax, 5) + 1):
            amb = L5[tuple(range(k))]
            gap = abs(L6[k] - amb)
            worst_n = max(worst_n, gap)
            print(f"  L_{k}:  n={3*k:2d} minimal  {mp.nstr(L6[k], 30)}"
                  f"\n         n=15 ambient  {mp.nstr(amb, 30)}   |diff| {mp.nstr(gap, 3)}")
        check("n-independence: L_2..L_5 agree between minimal-n and ambient n=15 "
              "below the 128-bit floor", worst_n < floor6)
    else:
        print("  (A=5 sidecar absent; cross-check skipped)")
    if kmax >= 6:
        print(f"  L_6:  n=18 minimal  {mp.nstr(L6[6], 30)}   (no ambient run exists)")

    print("\n" + "=" * 68)
    print("§2  THE SIZE-ONLY RECURSION  c_k = L_k - sum_{j<k} C(k,j) c_j")
    print("=" * 68)
    cs = size_only(L6, kmax)
    if have5:
        cum5 = full_mobius(L5, 5)
        worst_c = max(abs(cum5[tuple(range(k))] - cs[k]) for k in range(2, min(kmax, 5) + 1))
        for k in range(2, min(kmax, 5) + 1):
            print(f"  c_{k}:  recursion  {mp.nstr(cs[k], 30)}"
                  f"\n        full Mobius {mp.nstr(cum5[tuple(range(k))], 30)}")
        print(f"  worst |diff| over k = 2..5: {mp.nstr(worst_c, 3)}")
        check("recursion reproduces the 26-subset full Mobius at k = 2..5 "
              "below the 128-bit floor", worst_c < floor6)
    if kmax < 6:
        bad = [n for n, ok in checks if not ok]
        print(f"\n  (order-six section pending L_6)\n{len(checks) - len(bad)}/{len(checks)} checks passed")
        return 1 if bad else 0
    print(f"  c_6:  recursion  {mp.nstr(cs[6], 30)}   <- the order-six datum")

    print("\n" + "=" * 68)
    print("§3  THE HOMONUCLEAR A=6 HIERARCHY, TOTALS C(6,k) c_k")
    print("=" * 68)
    try:
        from codata_constants import M_E_MEV as _ME  # noqa: E402
        ME = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
        from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402
        q = Q_MP
        alpha = ME / (q * (q - 1))
    except Exception:  # pragma: no cover
        alpha = None
    prev = None
    tots = {}
    print("  k   terms   c_k (single)        C(6,k) c_k        MeV         |ratio|")
    for k in range(2, 7):
        tot = comb(6, k) * cs[k]
        tots[k] = tot
        rt = abs(tot / prev) if prev is not None else None
        mev = mp.nstr(alpha * tot, 8) if alpha is not None else "-"
        print(f"  {k}   {comb(6, k):>3d}    {mp.nstr(cs[k], 12):>16s}  {mp.nstr(tot, 12):>16s}"
              f"  {mev:>10s}   {mp.nstr(rt, 6) if rt is not None else '-'}")
        prev = tot
    signs = ["+" if tots[k] > 0 else "-" for k in range(2, 7)]
    print(f"  signs {signs}")
    resid = abs(sum(tots.values()) - L6[6])
    print(f"  L_6 reconstructed from the totals: {mp.nstr(sum(tots.values()), 30)}"
          f"   vs L_6 {mp.nstr(L6[6], 30)}   |diff| {mp.nstr(resid, 3)}")
    check("reconstruction: sum_k C(6,k) c_k = L_6 (the recursion read backwards)",
          resid < floor6)
    check("signs at k = 2..5 are + - - +, as at A = 5",
          signs[:4] == ["+", "-", "-", "+"])
    print(f"\n  order-six: c_6 = {mp.nstr(cs[6], 20)}, sign {signs[4]}, "
          f"|C(6,6) c_6 / C(6,5) c_5| = {mp.nstr(abs(tots[6] / tots[5]), 6)}")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(STEM, engine="python")
        wb.set_description(
            "The size-only cumulant recursion c_k = L_k - sum_{j<k} C(k,j) c_j "
            "(Lean: QOU.Mass.SubsetCumulantRecursion.cum_eq_sizeCum), valid for "
            "exchangeable systems, combined with n-independence of L_S, reaches "
            "order six with five minimal-system trace pairs instead of 57 ambient "
            "n=18 traces. Re-derives everything from the committed 128-bit A=6 "
            "sidecar and cross-checks L_2..L_5 and c_2..c_5 against the "
            "independent 200-bit A=5 ambient run. Reports the first order-six "
            "cumulant of the homonuclear bond model.")
        for k in range(2, 7):
            wb.add_data(f"L_{k}_minimal_n_{bits6}bit", mp.nstr(L6[k], 36))
            wb.add_data(f"c_{k}_single", mp.nstr(cs[k], 36))
            wb.add_data(f"c_{k}_total_C6k", mp.nstr(tots[k], 36))
        wb.add_data("signs_k2_to_k6", "".join(signs))
        wb.add_data("ratio_k6_over_k5", mp.nstr(abs(tots[6] / tots[5]), 12))
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Exchangeable (homonuclear) case only. The recursion does not apply "
            "to 6He (pnpnnn), whose cumulants need the full lattice: 57 traces at "
            "n=18, out of exact reach. One order-six datum, in the one system "
            "where the recursion is a theorem.")
        wb.add_caveat(
            "L_6 is a 128-bit (about 38-digit) MPFR value from a detached run; "
            "L_2..L_5 in the same sidecar are 128-bit too. Cross-checks against "
            "the 200-bit A=5 run are therefore floored at ~1e-35, and that is the "
            "floor the checks use. The physical ceiling is Q_ERR ~ 1e-12 "
            "regardless.")
        wb.add_caveat(
            "One more term does not settle convergence. The A=5 twelve-ordering "
            "sweep showed |c_5/c_4| straddling 1 across orderings; the value "
            "reported here is one ordering-free (exchangeable) number at k=6.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
