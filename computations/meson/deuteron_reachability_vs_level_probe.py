#!/usr/bin/env python3
"""What each escape from the deuteron infeasibility would have to buy.

Bean qou-6tcn, follow-on. `deuteron_support_reachability_probe.py` established
that with non-negative occupations of the convention-D (level r = 2) supported
blocks the objective is capped at `max(t)*n_target = 0.146058`, against
`B_D(AME2020) = 2.224566` — short by 15.2x. Three escapes were named: a
different cost, a different Wenzl level, or a program admitting signed
occupations.

Choosing among those is a modelling decision and is NOT made here. What IS
measurable, and is measured here, is **what each one would have to supply** —
so the choice can be made against numbers instead of against intuition.

THE LEVEL SWEEP
===============
The Ocneanu parameter is a family in the Wenzl level `r`,

    z_r = q^r / [r]_q ,

whose `r = 2` member is the canonical `z_2 = q^3/(q^2+1)`
(`su5-hypercharge-n3-gate`). The Schur-Weyl row cap at level `r` is
`ell(lambda) <= r`, so raising `r` widens the support. `y_lambda_su_n(n, q, N)`
takes that rank directly, so the whole family is computable.

For each level the three quantities that decide reachability are recomputed
from scratch:

    support   = {lambda : y_lambda != 0}          (widens with r)
    n_target  = sum_lambda y_lambda chi^lambda    (the Markov trace; MOVES with r)
    t_lambda  = y_lambda * chi^lambda(beta_D)
    ceiling   = max_{support} t_lambda * n_target

`chi^lambda(beta_D)` is a character of the braid image in the irrep `lambda` of
`H_n(q)`. It depends on `q` and `lambda` only, NOT on the Markov parameter, so
the committed values are reused across levels unchanged — that is why only the
weights need recomputing.

WHAT THIS CANNOT DECIDE
=======================
Whether a level other than 2 is available at all. It is not: `Lambda^2 V = 1`
pins the fibre dimension at 2 (`exteriorSquareDim_eq_one_iff`, sorry-free), and
`su5-hypercharge-n3-gate` records that the levels are ALTERNATIVES rather than
stages — one fibre occupies one level, and no construction in the framework
supplies a fibre at any level other than 2. So a level-3 row below is a
statement about a fibre the framework does not have.

That is exactly why it is worth computing: if widening the level does not clear
the AME value either, then the level escape is closed on arithmetic and does
not need the (much harder) existence question answered first.

SCOPE — (a) throughout
======================
MEASURED: the ceiling as a function of level, and the factor by which a cost
would have to grow at the canonical level.

NOT claimed: that any level is realisable; that a cost reaching the ceiling
exists or is derivable; that signed occupations are or are not justified; that
any binding conjecture is true or false. Nothing here computes a binding
contribution, and a ceiling that clears AME would be a necessary condition, not
a sufficient one.
"""

from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 60)

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
COST = HERE.parent / "iterative-lp-dual-h6-deuteron.witness.json"
SDP = HERE.parent / "deuteron-real-sdp.witness.json"
Q0 = mp.mpf(str(Q_50_DIGIT_STR))
ZERO = mp.mpf("1e-40")
LEVELS = [2, 3, 4, 5, 6]


def parse_part(k):
    return tuple(int(p) for p in k.strip("()").rstrip(",").split(",") if p.strip())


def main() -> int:
    wb = WitnessBuilder("deuteron-reachability-vs-level", engine="python-exact")
    wb.set_description(
        "Reachability ceiling max(t)*n_target for the deuteron "
        "operator-selection LP as a function of Wenzl level r, against "
        "B_D(AME2020) = 2.224566. Measures what the 'different level' and "
        "'different cost' escapes from the r=2 infeasibility would each have "
        "to supply. Makes no claim that any level other than 2 is realisable.")

    chi_raw = json.loads(COST.read_text())["data"]["chi_lambda_beta_D_at_q0"]
    chi = {parse_part(k): mp.mpf(str(v)) for k, v in chi_raw.items()}
    ame = mp.mpf(str(json.loads(SDP.read_text())["data"]["B_D_AME_MeV"]))

    print(f"q0 = {mp.nstr(Q0, 25)}   B_D(AME2020) = {mp.nstr(ame, 12)}\n")
    print(f"{'r':>2} {'|supp|':>6} {'max rows':>8} {'n_target':>14} "
          f"{'max t':>14} {'ceiling':>14} {'AME/ceiling':>12}")

    rows = {}
    for r in LEVELS:
        y = y_lambda_su_n(6, Q0, r)
        y = {p: mp.mpf(str(v)) for p, v in y.items()}
        support = [p for p, v in y.items() if abs(v) > ZERO]
        t = {p: y[p] * chi[p] for p in support}
        n_target = mp.fsum(y[p] * chi[p] for p in y)
        t_max = max(t.values())
        ceiling = t_max * n_target
        ratio = ame / ceiling if ceiling != 0 else mp.inf
        rows[f"r={r}"] = {
            "level": r,
            "support_size": len(support),
            "max_rows_in_support": max(len(p) for p in support),
            "n_target": mp.nstr(n_target, 30),
            "max_t": mp.nstr(t_max, 30),
            "ceiling": mp.nstr(ceiling, 30),
            "ame_over_ceiling": mp.nstr(ratio, 30),
            "clears_ame": bool(ceiling >= ame),
        }
        print(f"{r:>2} {len(support):>6} {max(len(p) for p in support):>8} "
              f"{mp.nstr(n_target, 10):>14} {mp.nstr(t_max, 10):>14} "
              f"{mp.nstr(ceiling, 10):>14} {mp.nstr(ratio, 8):>12}")

    # What a DIFFERENT COST would have to be, at the canonical level.
    r2 = rows["r=2"]
    need_t = ame / mp.mpf(r2["n_target"])
    cost_factor = need_t / mp.mpf(r2["max_t"])
    print(f"\nAt the canonical r = 2, a cost reaching AME needs")
    print(f"  max(t) >= AME / n_target = {mp.nstr(need_t, 12)}")
    print(f"  against the actual        {mp.nstr(mp.mpf(r2['max_t']), 12)}")
    print(f"  i.e. a factor of          {mp.nstr(cost_factor, 8)}x")

    any_clears = [k for k, v in rows.items() if v["clears_ame"]]
    print(f"\nlevels whose ceiling clears AME: {any_clears or 'NONE'}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — CONTROL: r=2 reproduces the committed r=2 ceiling. If this drifts,
    #      the sweep is not measuring the same object as the sibling probe.
    wb.add_assertion(
        name="control_r2_reproduces_committed_ceiling",
        computed=r2["ceiling"], expected="0.146057964937", tolerance="1e-9",
        unit="dimensionless",
        source="deuteron_support_reachability_probe.py")

    # A2 — CONTROL: the row cap tracks the level. At r the support may not
    #      exceed r rows; if it did, y_lambda_su_n is not doing what is assumed.
    cap_ok = all(v["max_rows_in_support"] <= v["level"] for v in rows.values())
    wb.add_assertion(
        name="control_row_cap_tracks_level",
        computed="1" if cap_ok else "0", expected="1", tolerance="0",
        unit="boolean", source="Schur-Weyl: ell(lambda) <= r at level r")

    # A3 — CONTROL: the support genuinely widens with r, so the sweep is not
    #      measuring the same program five times.
    widens = len({v["support_size"] for v in rows.values()}) > 1
    wb.add_assertion(
        name="control_support_widens_with_level",
        computed="1" if widens else "0", expected="1", tolerance="0",
        unit="boolean", source="support sizes across r")

    # A4 — THE RESULT: does any level clear AME?
    wb.add_assertion(
        name="levels_clearing_ame", computed=str(len(any_clears)),
        expected="0", tolerance="0", unit="count",
        source="ceiling >= B_D(AME2020) at each r")

    # A5 — THE SHARP FINDING: the ceiling is strictly DECREASING in r, so the
    #      canonical level is the best one and widening the level makes the
    #      gap worse rather than better. Mechanism: y is normalised
    #      (sum y_lambda f^lambda = 1), so a wider support spreads the same
    #      total weight over more blocks and BOTH max(t) and n_target shrink.
    ceils = [mp.mpf(rows[f"r={r}"]["ceiling"]) for r in LEVELS]
    strictly_decreasing = all(a > b for a, b in zip(ceils, ceils[1:]))
    wb.add_assertion(
        name="ceiling_strictly_decreasing_in_level",
        computed="1" if strictly_decreasing else "0", expected="1",
        tolerance="0", unit="boolean",
        source="normalised weights spread over a wider support as r grows")

    # A6 — corollary, stated separately because it is the part that matters
    #      for the choice: r = 2 maximises the ceiling over the levels swept.
    best = max(range(len(LEVELS)), key=lambda i: ceils[i])
    wb.add_assertion(
        name="canonical_level_maximises_ceiling",
        computed=str(LEVELS[best]), expected="2", tolerance="0", unit="level",
        source="argmax over the swept levels")

    wb.add_data("q0", mp.nstr(Q0, 50))
    wb.add_data("B_D_AME_MeV", mp.nstr(ame, 30))
    wb.add_data("per_level", rows)
    wb.add_data("canonical_cost_factor_needed", mp.nstr(cost_factor, 30))
    wb.add_caveat(
        "No level other than 2 is claimed to be realisable. Lambda^2 V = 1 "
        "pins the fibre dimension (exteriorSquareDim_eq_one_iff), and "
        "su5-hypercharge-n3-gate records that levels are ALTERNATIVES, not "
        "stages -- no construction supplies a fibre at any r != 2. A row here "
        "is a statement about a fibre the framework does not have.")
    wb.add_caveat(
        "Scope (a). A ceiling clearing AME would be NECESSARY, not sufficient: "
        "it says room exists, not that any derivable cost reaches it. Nothing "
        "here computes a binding contribution or adjudicates the signed"
        "-occupation option.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
