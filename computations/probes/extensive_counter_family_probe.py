#!/usr/bin/env python3
"""What else is extensive? — the full counter × normaliser family, measured.

THE QUESTION
------------
Two probes narrowed the extensive-term problem to a single number:

* `braid_nucleus_map_exponent_probe` (bean `qou-imcd`) — the braid→nucleus map
  reproduces the extensive **exponent** exactly (1.0, the SEMF volume term),
  leaving a pure multiplicative residual of ≈ 6.9×.
* `markov_normalisation_convention_span_probe` (bean `qou-78pt`) — that residual
  is **not** available from the normalisation convention: the family spans 1.33×
  against a 6–15× deficit.

Which leaves: *what else in the framework is extensive?* This probe answers it by
enumeration rather than by proposal — every counter the canonical atomic word
offers, crossed with every normaliser convention.

WHAT IS MEASURED
----------------
The counters are read off `atom_braid_word_3A`, not assumed. All four are
**exactly linear in A**, with zero residual across A = 2…56:

    bonds             A − 1        slope  1
    averaged letters  2A + 1       slope  2      (matches the module's own docstring)
    strands           3A           slope  3      (n_strands = 12 at ⁴He)
    letters           12A − 1      slope 12      (the Hecke word's length)

The letter count is the find: it is exactly **4× the strand count**, and nothing
before this had used it as the extensive counter.

THE RESULT
----------
Across the whole 4 × 4 family the extensive coefficient spans

    0.355 … 5.663 MeV/nucleon

against `B/A ≈ 8.5` and `a_V ≈ 15.8`. **The maximum is still 1.50× short of the
plateau and 2.79× short of `a_V`.**

So the missing factor is neither a normalisation nor a counter. Both of the
obvious places to look have now been enumerated and both come up short — which is
a stronger statement than "we have not found it yet".

WHAT THIS PROBE REFUSES TO DO
-----------------------------
Moving from the strand counter to the letter counter shrinks the deficit from
6.9× to 1.50×. That is *suggestive* and it is exactly the move the ROAST
(`2026-08-07-l2-attack-options-ROAST.md` §R0.1) caught the original memo making:
picking the family member that lands nearest the target and presenting the choice
as structure. Nothing here fixes which counter is the physical one, so this probe
reports the whole family and selects no member.

Usage:
    python3 computations/probes/extensive_counter_family_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40

M_E_MEV = mp.mpf("0.51099895069")
B_OVER_A_PLATEAU = mp.mpf("8.5")
SEMF_A_V = mp.mpf("15.8")

ISOTOPES = [(1, 1), (1, 2), (2, 2), (3, 3), (6, 6), (8, 8), (20, 20), (26, 30)]


def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    w = WitnessBuilder("extensive-counter-family-probe")
    w.set_description(
        "Enumerates every extensive counter the canonical atomic word offers, crossed "
        "with every normaliser convention, and measures whether any combination reaches "
        "the empirical extensive coefficient. None does."
    )

    # ---- measure the counters (read off the word, not assumed) --------------
    table = []
    for Z, N in ISOTOPES:
        A = Z + N
        word = atom_braid_word_3A(Z, N, include_inter=True)
        averaged = sum(
            1 for c, d, g in word
            if abs(float(d)) > 1e-12 and abs(abs(float(d)) - float(h)) > 1e-9
        )
        table.append({"A": A, "strands": 3 * A, "letters": len(word),
                      "averaged_letters": averaged, "bonds": A - 1})

    def slope_and_residual(key: str):
        a1, a2 = table[0]["A"], table[-1]["A"]
        v1, v2 = table[0][key], table[-1][key]
        s = mp.mpf(v2 - v1) / (a2 - a1)
        icept = v1 - s * a1
        worst = max(abs(r[key] - (s * r["A"] + icept)) for r in table)
        return s, worst

    counters, exact_linear = {}, True
    for key in ("bonds", "averaged_letters", "strands", "letters"):
        s, worst = slope_and_residual(key)
        counters[key] = s
        if worst > mp.mpf("1e-20"):
            exact_linear = False

    w.add_assertion(
        "all_counters_exactly_linear_in_A",
        computed="1" if exact_linear else "0",
        expected="1",
        source="max residual from a straight line, over A=2..56, for each of the four "
               "counters read off atom_braid_word_3A",
    )
    # The module's own docstring states there are 2A+1 averaged letters; the counter
    # is measured here independently, so this is a genuine cross-check.
    w.add_assertion(
        "averaged_letter_slope_matches_module_docstring",
        computed=mp.nstr(counters["averaged_letters"], 20),
        expected="2",
        tolerance="1e-20",
        source="measured slope vs mass_at_3A_proper's documented '2A + 1 such non-braid letters'",
    )

    # ---- cross with the normaliser family -----------------------------------
    normalisers = {
        "[2]_q = q + 1/q": q + 1 / q,
        "[2]_Q = 1 + q^2": 1 + q ** 2,
        "kauffman q^(1/2)+q^(-1/2)": mp.sqrt(q) + 1 / mp.sqrt(q),
        "1 + q^4": 1 + q ** 4,
    }
    grid, best = {}, mp.mpf(0)
    for cname, cslope in counters.items():
        grid[cname] = {}
        for nname, nval in normalisers.items():
            v = cslope * mp.log(nval) * M_E_MEV
            grid[cname][nname] = mp.nstr(v, 10)
            best = max(best, v)

    w.add_assertion(
        "no_family_member_reaches_plateau",
        computed="1" if best < B_OVER_A_PLATEAU else "0",
        expected="1",
        source=f"family maximum {mp.nstr(best, 8)} MeV/nucleon vs the empirical B/A "
               f"plateau {B_OVER_A_PLATEAU} MeV/nucleon (independent: nuclear data)",
    )

    w.add_parameter("q0", mp.nstr(q, 30))
    w.add_data("counter_measurements", table)
    w.add_data("counter_slopes_per_nucleon",
               {k: mp.nstr(v, 10) for k, v in counters.items()})
    w.add_data("counter_forms", {
        "bonds": "A - 1", "averaged_letters": "2A + 1",
        "strands": "3A", "letters": "12A - 1",
        "note": "all exactly linear, zero residual over A=2..56; letters is exactly 4x strands",
    })
    w.add_data("coefficient_grid_MeV_per_nucleon", grid)
    w.add_data("family_extremes", {
        "max_MeV_per_nucleon": mp.nstr(best, 10),
        "shortfall_vs_plateau": mp.nstr(B_OVER_A_PLATEAU / best, 8),
        "shortfall_vs_a_V": mp.nstr(SEMF_A_V / best, 8),
    })
    w.add_data("verdict", (
        "The missing factor is neither a normalisation nor a counter. Every extensive "
        "counter the atomic word offers is exactly linear in A with slope in {1,2,3,12}; "
        "crossed with every normaliser convention the coefficient spans 0.355..5.663 "
        "MeV/nucleon, and the maximum is still 1.50x short of the B/A plateau and 2.79x "
        "short of a_V. Both obvious places to look are now enumerated and both come up "
        "short. NOTE: switching from the strand counter to the letter counter shrinks the "
        "deficit from 6.9x to 1.50x -- suggestive, and exactly the member-picking the "
        "ROAST caught the original memo doing. Nothing here fixes which counter is "
        "physical, so no member is selected."
    ))

    out = w.save()
    print(f"wrote {out}")
    print(f"  counter slopes (per nucleon)      : "
          f"{ {k: float(v) for k, v in counters.items()} }")
    print(f"  all exactly linear in A           : {exact_linear}")
    print(f"  family max                        : {mp.nstr(best, 8)} MeV/nucleon")
    print(f"  shortfall vs B/A plateau (8.5)    : {mp.nstr(B_OVER_A_PLATEAU / best, 6)}x")
    print(f"  shortfall vs a_V (15.8)           : {mp.nstr(SEMF_A_V / best, 6)}x")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
