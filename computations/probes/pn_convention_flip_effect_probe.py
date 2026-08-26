#!/usr/bin/env python3
"""What the strict_averaged -> bring_color_weighted flip actually moves.

# Why this probe exists

A green test suite is not evidence about this flip. The Rust crate's 212
tests pass identically before and after it, because its only atom tests
(`vacuum`, `hydrogen`) have NO p-n bond at all. The check that means
something is a quantity computed for an atom with Z >= 1 AND N >= 1,
measured against a prediction derived independently of the code under test.

# What it establishes

1. THE SHIFT IS A SINGLE FACTOR, AND IT DOES NOT GROW WITH A.

   `closed_form_ratio` walks the canonical ordering `["p"]*Z + ["n"]*N` and
   multiplies one factor per adjacent pair. That ordering is all protons
   followed by all neutrons, so it contains EXACTLY ONE p-n boundary --
   for the deuteron and for carbon-12 alike. The flip therefore multiplies
   the closed-form trace ratio by one A-independent factor

       f_canon / f_blind = 1 + 1.4149466e-04

   Verified here to > 55 decimal places for 2H, 3H, 3He, 4He, 7Li and 12C.

   This matters for the migration: the effect is not an accumulating
   per-bond error but a single known multiplier, so a consumer that takes a
   RATIO of two mixed atoms sees it cancel exactly, and a consumer of a
   pure-flavour system does not see it at all.

2. Z = 0 OR N = 0 IS UNTOUCHED. The proton and the neutron have no mixed
   bond, so their ratios are bit-identical across the flip. Any witness
   whose atoms are all pure-flavour needs no regeneration.

3. THE A-INDEPENDENCE IS A PROPERTY OF THE CANONICAL ORDERING, NOT A
   THEOREM. An interleaved ordering (p n p n ...) has A-1 mixed bonds and
   would shift by the factor raised to that power. Anything that varies the
   ordering -- `canonical_ordering_dof_probe.py` does exactly this -- must
   not inherit the single-factor result from here.

Bean qou-cblw. Owner authorisation 2026-08-26.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (_HERE.parent, _HERE.parent / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from mpmath import mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from closed_form_tau_M import closed_form_ratio, markov_z, hecke_h  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

DPS = 60

ATOMS = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1),
         ("4He", 2, 2), ("7Li", 3, 4), ("12C", 6, 6)]
PURE = [("proton", 1, 0), ("neutron", 0, 1), ("2p", 2, 0), ("2n", 0, 2)]


def main() -> int:
    _started = time.monotonic()
    mp.dps = DPS
    # `q_parameter.Q` is a float64. Carrying it here would cap every
    # printed value at 17 significant digits while the corpus computes
    # these factors at 50 dps -- the committed witnesses record
    # 0.508157887748645593880406757381..., which is the 50-dps value and
    # diverges from the f64-q one at digit 18.
    q = mp.mpf(Q_50_DIGIT_STR)
    z, h = markov_z(q), hecke_h(q)
    delta = flavor_split_leading(q)

    f_blind = z - h / 2
    f_canon = z - h * (mp.mpf(1) / 2 - delta / 4)
    predicted = f_canon / f_blind - 1

    w = WitnessBuilder("pn-convention-flip-effect", engine="mpmath",
                       output_dir=_HERE, start_time=_started)
    w.set_description(
        "What the strict_averaged -> bring_color_weighted p-n flip moves. "
        "The canonical ordering p..p n..n carries exactly ONE p-n boundary "
        "for every atom, so the flip is a single A-independent factor "
        "1 + 1.4149466e-04 on the closed-form trace ratio, not an "
        "accumulating per-bond error; pure-flavour systems are untouched."
    )
    w.set_content_block("prop:pn-averaging-uniqueness")
    # Emitted BY THE PRODUCER. A hand-built witness that gets these keys
    # backfilled downstream loses them on every re-run -- the bare-producer
    # hazard AGENTS.md records under the witness staleness triage.
    w.add_parameter("q0Anchor", "proton")
    w.add_parameter("q0", mp.nstr(q, 50))
    w.add_assertion("f_pn_blind", mp.nstr(f_blind, 30),
                    "0.508157887748645593880406757381")
    w.add_assertion("f_pn_canonical", mp.nstr(f_canon, 30),
                    "0.508229789376738962577995797656")
    # Exact identity, so the residual is pure arithmetic noise at 60 dps.
    # A tolerance is required: asserting == 0.0 against 8.6e-63 fails, which
    # is a defect in the assertion and not in the mathematics.
    w.add_assertion("per_bond_gap_is_h_delta_over_4",
                    mp.nstr(abs((f_canon - f_blind) - h * delta / 4), 5), "0.0",
                    tolerance="1e-55",
                    source="the whole difference is exactly h*delta/4")

    print(f"f_pn  blind      {mp.nstr(f_blind, 30)}")
    print(f"f_pn  canonical  {mp.nstr(f_canon, 30)}")
    print(f"predicted shift  {mp.nstr(predicted, 30)}\n")

    print(f"{'atom':>8} {'p-n bonds':>10} {'measured rel shift':>34} {'agrees to':>10}")
    for name, Z, N in ATOMS:
        order = ["p"] * Z + ["n"] * N
        bonds = sum(1 for k in range(len(order) - 1) if order[k] != order[k + 1])
        rb = closed_form_ratio(Z, N, q, pn_convention="strict_averaged")
        rc = closed_form_ratio(Z, N, q, pn_convention="bring_color_weighted")
        rel = (rc - rb) / rb
        discrepancy = abs(rel / predicted - 1)
        agree = int(-mp.log10(discrepancy)) if discrepancy > 0 else DPS
        print(f"{name:>8} {bonds:>10} {mp.nstr(rel, 25):>34} {agree:>7} dp")
        w.add_assertion(f"{name}_mixed_bond_count", str(bonds), "1",
                        source="canonical ordering p..p n..n has ONE p-n boundary")
        # Numeric, not a rendered string: a string assertion cannot express
        # "at least this good", so `agrees_to_57_dp` vs `agrees_to_>=50_dp`
        # compares unequal and reports a failure on a correct result.
        w.add_assertion(f"{name}_shift_matches_single_factor_prediction",
                        mp.nstr(discrepancy, 5), "0.0", tolerance="1e-50",
                        source="relative discrepancy vs f_canon/f_blind - 1")

    print()
    for name, Z, N in PURE:
        rb = closed_form_ratio(Z, N, q, pn_convention="strict_averaged")
        rc = closed_form_ratio(Z, N, q, pn_convention="bring_color_weighted")
        same = rb == rc
        print(f"{name:>8}  Z={Z} N={N}  unchanged by the flip: {same}")
        w.add_assertion(f"{name}_unchanged_by_flip", str(same), "True",
                        source="no mixed bond, so no factor to move")

    path = w.save(extra={"data": {
        "q0": mp.nstr(q, 25),
        "delta": mp.nstr(delta, 25),
        "f_pn_strict_averaged": mp.nstr(f_blind, 30),
        "f_pn_bring_color_weighted": mp.nstr(f_canon, 30),
        "relative_shift": mp.nstr(predicted, 30),
        "mixed_bonds_in_canonical_ordering": 1,
        "a_independence_is_an_ordering_property_not_a_theorem": True,
    }})
    print(f"\nwitness -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
