#!/usr/bin/env python3
"""
Probe — the alpha direction is squeezed from BOTH sides. Honest negative on qou-bid3.

`two_channel_total_binding_floor_probe.py` closed the last two-nucleon repair
route (T-odd ribbon twist) on a framing invariant, and concluded that the only
surviving free object in `B = -alpha * log(mu)` is `alpha` itself: the
two-nucleon floor `alpha * log 4 >= 2.1510 MeV` requires

    alpha <= 1.5516 MeV      against the framework's E_0 = 4.1860 MeV.

Bean `qou-bid3` recorded that direction WITH A DO-NOT-FIT GATE, requiring the
many-body sum be measured first: "if the A>=24 band is ALSO over-bound by ~2.7x
this is one scale error, not a two-nucleon defect." This probe runs that
measurement. **It is not one scale error.**

## The measurement

From `collective_term_budget_probe.py` (production `_bond_type_L`, convention D,
proton pin), the chain closed form against AME2020:

    iso     B_AME/A    chain/A    chain/AME
    2H       1.1123     1.4164      1.27x  OVER
    3H       2.8273     2.0466      0.72x  under
    4He      7.0739     2.1703      0.31x  under
    12C      7.6801     2.6729      0.35x  under
    56Fe     8.7904     2.8977      0.33x  under
    208Pb    7.8675     2.9907      0.38x  under

**The chain over-binds exactly one nucleus — the deuteron — and under-binds
every other, by ~3x.** The sign flips between `A = 2` and `A = 3`.

## The squeeze

`B_chain` is linear in `alpha` (it is `alpha` times a sum of derived per-bond
`L`s), so rescaling `alpha` rescales every row uniformly. The two constraints
therefore pull in opposite directions:

    two-nucleon floor   needs   alpha <= 1.5516 MeV
    many-body A >= 12   needs   alpha LARGER (or a large positive collective term)

At `alpha = 1.5516` the 56Fe under-binding goes from 3.03x to **8.18x**. There is
no value of a uniform `alpha` that satisfies both; the admissible interval is
empty.

## Consequence for qou-bid3

The `alpha` direction as stated — a single scale error — is **closed**. The 2.70x
two-nucleon over-binding is not a global miscalibration of `E_0`; it is specific
to the two-nucleon sector, where the framework's sign structure is also wrong.
The two defects are the same defect.

This is what the do-not-fit gate was for: proposing `alpha ~ 1.55` to fit the
deuteron would have silently multiplied the many-body error by 2.7x, in a place
the two-nucleon probe does not look.

## What survives

**Scope-(a).** This excludes a *uniform* rescaling of `alpha`. It does not
exclude:

* a **channel-dependent** or **A-dependent** `alpha` — but note that is no longer
  one constant, it is a function, and deriving it is a strictly harder problem
  than the one it replaces;
* a binding law other than `-alpha * log mu`;
* the large positive collective term the budget probe already measures
  (`R/alpha = 1.3240` per nucleon, mixed-sign in `A`) — which is the many-body
  side's own open item and is not an `alpha` question at all.

The honest summary: the two-nucleon sector is not repairable by any of the
interface-side moves (six routes, all closed), and it is not repairable by the
one scale it has left. What remains is a change to the binding law or to what
the two-nucleon states are — both larger than a parameter.

NO WITNESS: a linear rescaling applied to the production chain closed form; the
table reproduces it.

Bean qou-bid3; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp
from _precision import set_compute_dps  # noqa: E402

# (label, A, B_AME/A, chain/A) from collective_term_budget_probe.py at alpha = E_0
ROWS = [
    ("2H", 2, "1.1123", "1.4164"),
    ("3H", 3, "2.8273", "2.0466"),
    ("3He", 3, "2.5727", "1.7915"),
    ("4He", 4, "7.0739", "2.1703"),
    ("6Li", 6, "5.3323", "2.4216"),
    ("12C", 12, "7.6801", "2.6729"),
    ("16O", 16, "7.9762", "2.7358"),
    ("24Mg", 24, "8.2607", "2.7986"),
    ("40Ca", 40, "8.5513", "2.8489"),
    ("56Fe", 56, "8.7904", "2.8977"),
    ("208Pb", 208, "7.8675", "2.9907"),
]
E0_STR = "4.1859813632944758969"
ALPHA_MAX = "1.5516"   # from the two-nucleon floor: nature_total / log 4


def main() -> int:
    set_compute_dps()
    E0 = mp.mpf(E0_STR)
    amax = mp.mpf(ALPHA_MAX)
    scale = amax / E0

    print("The alpha direction is squeezed from BOTH sides — qou-bid3 negative.\n")
    print(f"  two-nucleon floor requires   alpha <= {mp.nstr(amax, 6)} MeV")
    print(f"  framework has                E_0    = {mp.nstr(E0, 6)} MeV")
    print(f"  ratio                                 {mp.nstr(scale, 6)}\n")

    print("Chain closed form vs AME2020 at the CURRENT alpha, and at the required one:\n")
    print("| iso   |   A | B_AME/A | chain/A | chain/AME | chain/A @1.5516 | ratio @1.5516 |")
    print("| ----- | --: | ------: | ------: | --------: | --------------: | ------------: |")
    over = []
    under = []
    for lab, A, ame_s, ch_s in ROWS:
        ame = mp.mpf(ame_s)
        ch = mp.mpf(ch_s)
        r = ch / ame
        ch2 = ch * scale
        r2 = ch2 / ame
        (over if r > 1 else under).append((lab, r, r2))
        print(f"| {lab:<5} | {A:3d} | {mp.nstr(ame, 6)} | {mp.nstr(ch, 6)} "
              f"| {mp.nstr(r, 4)}x | {mp.nstr(ch2, 6)} | {mp.nstr(r2, 4)}x |")

    print(f"\n  OVER-bound at current alpha : {[l for l, _, _ in over]}")
    print(f"  UNDER-bound at current alpha: {[l for l, _, _ in under]}\n")
    print("  The chain over-binds EXACTLY ONE nucleus — the deuteron — and under-binds")
    print("  every other by ~3x. The sign flips between A = 2 and A = 3.\n")

    fe_now = mp.mpf("2.8977") / mp.mpf("8.7904")
    fe_req = fe_now * scale
    print("## The squeeze\n")
    print("  B_chain is LINEAR in alpha (alpha times a sum of derived per-bond L's),")
    print("  so rescaling alpha rescales every row uniformly:\n")
    print(f"    two-nucleon floor    needs  alpha <= {mp.nstr(amax, 6)}")
    print("    many-body A >= 12    needs  alpha LARGER (or a big positive collective term)\n")
    print(f"  At alpha = {mp.nstr(amax, 6)} the 56Fe under-binding goes from "
          f"{mp.nstr(1/fe_now, 4)}x to {mp.nstr(1/fe_req, 4)}x.")
    print("  The admissible interval for a uniform alpha is EMPTY.\n")

    print("## Consequence for qou-bid3\n")
    print("  The alpha direction AS STATED — a single scale error — is CLOSED. The")
    print("  2.70x two-nucleon over-binding is not a global miscalibration of E_0; it")
    print("  is specific to the two-nucleon sector, where the sign structure is also")
    print("  wrong. The two defects are the same defect.")
    print("\n  This is what the do-not-fit gate was for: proposing alpha ~ 1.55 to fit")
    print("  the deuteron would have multiplied the many-body error by 2.7x, in a")
    print("  place the two-nucleon probe does not look.\n")

    print("## What survives (scope-(a))\n")
    print("  Excluded: a UNIFORM rescaling of alpha. NOT excluded: a channel- or")
    print("  A-dependent alpha (but that is a function, not a constant — a strictly")
    print("  harder problem than the one it replaces); a binding law other than")
    print("  -alpha log mu; the large positive collective term the budget probe")
    print("  already measures (R/alpha = 1.3240 per nucleon, mixed-sign in A), which")
    print("  is the many-body side's own open item and not an alpha question.")
    print("\n  Honest summary: the two-nucleon sector is not repairable by any")
    print("  interface-side move (six routes closed) nor by the one scale it has")
    print("  left. What remains is a change to the binding law or to what the")
    print("  two-nucleon states are — both larger than a parameter.")
    print("\n(no witness by design — a linear rescaling of the production chain.)")

    assert over and [l for l, _, _ in over] == ["2H"], "expected only 2H over-bound"
    assert fe_req < fe_now, "rescaling should worsen the many-body deficit"
    return 0


if __name__ == "__main__":
    sys.exit(main())
