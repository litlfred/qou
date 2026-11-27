#!/usr/bin/env python3
"""What else is extensive? — the full counter × normaliser family, measured.

⚠ SCALE CORRECTION 2026-08-31 — EVERY MeV FIGURE BELOW IS 8.19x TOO SMALL
-------------------------------------------------------------------------
This probe multiplies its dimensionless logs by `m_e = 0.511 MeV`, unjustified.
The corpus's binding machinery uses the hadronic energy unit
`E_0 = m_e/(q_0(q_0-1)) = 4.18598 MeV` (`b_over_a_evaluator.py`; the `B_sym`
linear chain's `alpha`, CAL-1; the ROAST's `E_0 log N`), larger by
`1/(q_0(q_0-1)) = 8.1917611722`. Corrected:

    whole 4x4 grid   2.909 ... 46.39 MeV/nucleon   (was 0.355 ... 5.663)
    A1's own row     8.722 ... 11.60               (was 1.065 ... 1.416)

so the family maximum no longer falls short of anything — it exceeds `a_V` by
2.9x — and A1's row **overshoots** the 8.5 plateau instead of falling 6-8x below
it. See `computations/probes/extensive_term_energy_scale_reconciliation_probe.py`.

**What survives, and it is the substance of this probe:** the four counters are
read off `atom_braid_word_3A` and are dimensionless. `bonds = A-1`,
`averaged = 2A+1`, `strands = 3A`, `letters = 12A-1`, all exactly linear in `A`
with zero residual, and `letters = 4 x strands` exactly. Both assertions are
scale-free and stand. So does the §"WHICH COUNTER IS A1's" finding that the
normaliser `Z(n) = (1+q^2)^n` is word-independent, hence A1's counter is
**strands** and the other rows are different proposals.

**What is withdrawn:** the sentence "the maximum is still 1.50x short of the
plateau and 2.79x short of `a_V`", the `no_family_member_reaches_plateau`
assertion (true at `m_e`, false at `E_0`), and the conclusion that "the missing
factor is neither a normalisation nor a counter" — at `E_0` there is no missing
factor of that size to explain.

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

WHICH COUNTER IS A1's? — STRANDS, and the normaliser settles it
---------------------------------------------------------------
`y_lambda_symbolic(n)` takes **only `n`**. The Markov trace is
`tr_M(β) = Σ_λ y_λ(q)·χ^λ(β)`, so the word enters through `χ` and *never* through
`y`. The normaliser `Z(n) = (1+q²)^n` is therefore **word-independent**, and the
object A1 proposes to stop discarding counts **strands** — it cannot count
letters or bonds, which are properties of the word.

So for A1 the deficit is **6.0×–8.0×**, not the family minimum. The letter
counter, which would give 1.50×, belongs to a *different* proposal (a per-letter
energy) with no axiom source behind it.

Crossing the two in one grid — as an earlier reading of this probe did — overstates
the available freedom and flatters A1 by a factor of four. That is the same
member-picking the ROAST (`2026-08-07-l2-attack-options-ROAST.md` §R0.1) caught the
original memo doing, arrived at from the other direction. The grid is still
reported in full, because the *other* rows are real proposals someone may want to
motivate; but they are not conventions of one object, and no member is selected.

Usage:
    python3 computations/probes/extensive_counter_family_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40

M_E_MEV = mp.mpf("0.51099895069")
B_OVER_A_PLATEAU = mp.mpf("8.5")
SEMF_A_V = mp.mpf("15.8")

ISOTOPES = [(1, 1), (1, 2), (2, 2), (3, 3), (6, 6), (8, 8), (20, 20), (26, 30)]


def main() -> int:
    q = Q_MP
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
    # RESIDUAL against 0, not value against target: the verdict path
    # (qou_substrate/witness.py) compares float(computed) to float(expected),
    # so a value-vs-value form here could not resolve anything below the
    # float64 floor and the tolerance below it was unreachable by ~10^4.
    # A residual near zero IS representable as a float64 all the way down, so
    # the same tolerance is a real bound on it.
    # Gate: computations/audits/tolerance_below_arithmetic_floor_audit.py.
    w.add_assertion(
        "averaged_letter_slope_matches_module_docstring",
        computed=mp.nstr(abs(counters["averaged_letters"] - 2), 20),
        expected="0",
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

    # ⚠ SCALE-QUALIFIED. True at m_e, FALSE at the corpus's own E_0, where the
    # family maximum is 46.39 MeV/nucleon. Kept, with the qualifier in the name,
    # so the retraction has something to point at rather than vanishing.
    w.add_assertion(
        "no_family_member_reaches_plateau_AT_THE_m_e_SCALE",
        computed="1" if best < B_OVER_A_PLATEAU else "0",
        expected="1",
        source=f"family maximum {mp.nstr(best, 8)} MeV/nucleon AT m_e vs the empirical B/A "
               f"plateau {B_OVER_A_PLATEAU} MeV/nucleon (independent: nuclear data). At "
               f"E_0 = m_e/(q0(q0-1)) the same maximum is "
               f"{mp.nstr(_qbeta_e0.order_zero_scaled(best, q), 8)} MeV/nucleon and the statement is FALSE.",
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
    # ---- which counter is the A1 object? The normaliser answers it. ---------
    # `y_lambda_symbolic(n)` takes ONLY `n`. The Markov trace is
    # `tr_M(beta) = sum_lambda y_lambda(q) * chi^lambda(beta)`: the word enters
    # through `chi`, never through `y`. So the normaliser `Z(n) = (1+q^2)^n` is
    # word-INDEPENDENT, and the quantity A1 proposes to stop discarding counts
    # STRANDS. It cannot count letters, bonds, or anything else read off the word.
    w.add_data("which_counter_is_the_A1_object", {
        "answer": "strands",
        "why": ("y_lambda_symbolic takes only n; tr_M = sum_lambda y_lambda * chi^lambda, "
                "so the word enters through chi and never through the normaliser. Z(n) is "
                "word-independent."),
        "A1_coefficient_MeV_per_nucleon": grid["strands"],
        "A1_deficit_vs_plateau": (
            f"{mp.nstr(B_OVER_A_PLATEAU / (counters['strands'] * mp.log(max(normalisers.values())) * M_E_MEV), 6)}x"
            f" .. {mp.nstr(B_OVER_A_PLATEAU / (counters['strands'] * mp.log(min(normalisers.values())) * M_E_MEV), 6)}x"),
        "correction": ("An earlier reading of this grid treated all sixteen cells as "
                       "conventions of one object. They are not. Only the STRANDS row is "
                       "A1; the other rows are different physical proposals (a per-letter "
                       "or per-bond energy) with no axiom source. Presenting them together "
                       "overstated the available freedom and made A1's deficit look like "
                       "1.50x when for A1 it is 6.0-8.0x."),
    })

    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0_ratio = _qbeta_e0.order_zero_scaled(1, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    w.add_data("SCALE_CORRECTION_2026_08_31", {
        "scale_ratio_E0_over_me": mp.nstr(e0_ratio, 20),
        "corrected_grid_MeV_per_nucleon": {
            cname: {nname: mp.nstr(mp.mpf(v) * e0_ratio, 10) for nname, v in row.items()}
            for cname, row in grid.items()
        },
        "corrected_family_max": mp.nstr(best * e0_ratio, 10),
        "corrected_A1_strands_row_vs_plateau":
            f"{mp.nstr(counters['strands'] * mp.log(min(normalisers.values())) * M_E_MEV * e0_ratio / B_OVER_A_PLATEAU, 6)}x .. "
            f"{mp.nstr(counters['strands'] * mp.log(max(normalisers.values())) * M_E_MEV * e0_ratio / B_OVER_A_PLATEAU, 6)}x OVER",
        "what_survives": "The counter measurements. They are dimensionless and read off "
                         "atom_braid_word_3A: bonds A-1, averaged 2A+1, strands 3A, letters "
                         "12A-1, exactly linear, letters = 4 x strands. Both assertions are "
                         "scale-free. So is the finding that Z(n) is word-independent and "
                         "A1's counter is therefore strands.",
        "what_is_withdrawn": "Every MeV magnitude, the 'still 1.50x short' framing, and the "
                             "conclusion that 'the missing factor is neither a normalisation "
                             "nor a counter' -- at E_0 there is no factor of that size left "
                             "to explain.",
        "see": "computations/probes/extensive_term_energy_scale_reconciliation_probe.py",
    })
    w.add_data("verdict", (
        "The missing factor is neither a normalisation nor a counter. Every extensive "
        "counter the atomic word offers is exactly linear in A with slope in {1,2,3,12}; "
        "crossed with every normaliser convention the coefficient spans 0.355..5.663 "
        "MeV/nucleon, and the maximum is still 1.50x short of the B/A plateau and 2.79x "
        "short of a_V. Both obvious places to look are now enumerated and both come up "
        "short. AND the counter is not free for A1: the normaliser Z(n) is word-independent, "
        "so the object A1 proposes to stop discarding counts STRANDS, giving 6.0-8.0x. The "
        "letter counter (which would give 1.50x) belongs to a DIFFERENT proposal with no "
        "axiom source -- crossing the two in one grid, as an earlier reading of this probe "
        "did, overstates the freedom and flatters A1."
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
