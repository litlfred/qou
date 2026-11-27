#!/usr/bin/env python3
"""The multiplicative assembly's 3-body cumulant sign is threshold-forced.

`he4_body_order_shortfall_location_probe.py` (2026-08-29) measured the model's
connected 3-body Ursell cumulant as wrong-signed against AME2020 under all four
convention x bond-typing combinations. This probe establishes WHY, and shows the
reason is not any of the three things one would reach for first.

Under the multiplicative assembly `W(K) = 1 - PROD_{i<j} f_ij` normalised at the
deuteron, in W-units:

    b2 = 1 - fpn,   b3 = (1 - P3) - 3*(1 - fpn) = 3*fpn - 2 - P3

with `P3` the product of bond factors over WHATEVER edge set the 3-body system
carries. Since every bond factor is positive, `P3 >= 0`, hence

    b3 <= 3*fpn - 2      ==>      b3 > 0  requires  fpn > 2/3.

`P3` enters only through its positivity, so the bound is independent of the edge
set, of the like-pair factors `f_pp`/`f_nn`, and of the overall energy scale.

Lean (sorry-free): QOU/MassTheory/MayerThreeBodySign.lean --
`b3_le_of_nonneg`, `lt_of_b3_pos`, `b3_neg_of_le`.

What this probe adds to the Lean: the four measured `fpn` values at 50 dps, the
margin each sits below the threshold, an explicit edge-set sweep at A=3 (chain
vs triangle, both typings, both conventions) confirming edge-set independence
numerically, and a reproduction of the 2026-08-29 `b3` figures as a cross-check
that the W-unit reduction is the same object the earlier probe measured.

Scope-(b) on the conjunction (multiplicative assembly + fpn <= 2/3), invariant
named: positivity of a product of positive bond factors. It does NOT exclude the
bond picture, and it does not close the magnitude.

`-- Ref:` Ursell 1927 / Mayer cluster expansion; `thm:binding-closure-conditional`;
owner ruling R1 2026-08-15 (convention D canonical).
"""
from __future__ import annotations

import datetime
import json
import os
import sys
from itertools import combinations
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import hecke_h, markov_z  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

set_compute_dps()

AME = {"D": AME_B_DEUTERON_MEV_VALIDATION, "3H": AME_B_TRITIUM_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION}

THRESHOLD = mpf(2) / 3


def z_of(q, convention):
    """D = q^3/(q^2+1) canonical; C = sqrt(q)/(q+1) excised, computed here ONLY
    to show the threshold verdict is convention-independent."""
    if convention == "D":
        return markov_z(q)
    if convention == "C":
        return mp.sqrt(q) / (q + 1)
    raise ValueError(convention)


def bond_factor(a, b, z, h, fpn):
    if a == "p" and b == "p":
        return z
    if a == "n" and b == "n":
        return z - h
    return fpn


EDGE_SETS = {
    # A = 3, vertices 0,1,2. The bound must not care which of these is used.
    "triangle": [(0, 1), (0, 2), (1, 2)],
    "chain-01-12": [(0, 1), (1, 2)],
    "chain-01-02": [(0, 1), (0, 2)],
    "chain-02-12": [(0, 2), (1, 2)],
}


def bond_product(order, edges, z, h, fpn):
    p = mpf(1)
    for (i, j) in edges:
        p *= bond_factor(order[i], order[j], z, h, fpn)
    return p


def measure(convention, pn_typing):
    q = Q_MP
    z = z_of(q, convention)
    h = hecke_h(q)
    delta = flavor_split_leading(q)
    if pn_typing == "probe2":
        fpn = z - h * (mpf(1) / 2 - delta / 4)
    elif pn_typing == "chi":
        fpn = z
    else:
        raise ValueError(pn_typing)

    cap = 3 * fpn - 2          # the Lean bound `b3_le_of_nonneg`
    rows = []
    for name, edges in EDGE_SETS.items():
        # isospin average of 3H (p,n,n) and 3He (p,p,n), as the 08-29 inversion
        p3_t = bond_product(["p", "n", "n"], edges, z, h, fpn)
        p3_h = bond_product(["p", "p", "n"], edges, z, h, fpn)
        p3 = (p3_t + p3_h) / 2
        b3 = (1 - p3) - 3 * (1 - fpn)
        rows.append({
            "edge_set": name,
            "n_edges": len(edges),
            "P3_isospin_avg": mp.nstr(p3, 20),
            "b3_W_units": mp.nstr(b3, 20),
            "b3_negative": bool(b3 < 0),
            "respects_cap": bool(b3 <= cap),
        })

    return {
        "convention": convention,
        "pn_typing": pn_typing,
        "z": mp.nstr(z, 20),
        "h": mp.nstr(h, 20),
        "fpn": mp.nstr(fpn, 20),
        "threshold_two_thirds": mp.nstr(THRESHOLD, 20),
        "fpn_below_threshold": bool(fpn < THRESHOLD),
        "margin_below_threshold": mp.nstr(THRESHOLD - fpn, 20),
        "cap_3fpn_minus_2": mp.nstr(cap, 20),
        "cap_negative": bool(cap < 0),
        "edge_sets": rows,
    }


def cross_check_0829(convention, pn_typing):
    """Reproduce the 2026-08-29 b3 in MeV, to show the W-unit reduction above is
    the same object that probe measured. Model: B(K) = B_AME(D)*W(K)/W(D) over
    the COMPLETE graph, then the Ursell inversion b3 = Bbar(3) - 3*b2."""
    q = Q_MP
    z = z_of(q, convention)
    h = hecke_h(q)
    delta = flavor_split_leading(q)
    fpn = z if pn_typing == "chi" else z - h * (mpf(1) / 2 - delta / 4)

    def W(order):
        n = len(order)
        return 1 - bond_product(order, list(combinations(range(n), 2)), z, h, fpn)

    wD = W(["p", "n"])
    scale = AME["D"] / wD
    b2 = scale * wD
    b3 = (scale * W(["p", "n", "n"]) + scale * W(["p", "p", "n"])) / 2 - 3 * b2
    return b2, b3


def main() -> int:
    combos = [(c, t) for c in ("D", "C") for t in ("probe2", "chi")]
    results = [measure(c, t) for c, t in combos]

    print("The 3-body cumulant sign is threshold-forced: b3 > 0 needs fpn > 2/3")
    print(f"  threshold 2/3 = {mp.nstr(THRESHOLD, 20)}\n")
    print(f"  {'conv':>5}{'typing':>9}{'fpn':>24}{'margin':>18}{'cap=3f-2':>18}")
    for r in results:
        print(f"  {r['convention']:>5}{r['pn_typing']:>9}"
              f"{r['fpn']:>24}{r['margin_below_threshold']:>18}"
              f"{r['cap_3fpn_minus_2']:>18}")

    print("\n  edge-set independence at A=3 (b3 in W-units, isospin-averaged):")
    print(f"  {'conv':>5}{'typing':>9}{'edge set':>14}{'b3':>24}{'neg':>6}")
    for r in results:
        for row in r["edge_sets"]:
            print(f"  {r['convention']:>5}{r['pn_typing']:>9}"
                  f"{row['edge_set']:>14}{row['b3_W_units']:>24}"
                  f"{str(row['b3_negative']):>6}")

    print("\n  cross-check vs 2026-08-29 (MeV, complete graph):")
    xchecks = []
    for c, t in combos:
        b2, b3 = cross_check_0829(c, t)
        xchecks.append({"convention": c, "pn_typing": t,
                        "b2_MeV": mp.nstr(b2, 12), "b3_MeV": mp.nstr(b3, 12)})
        print(f"  {c:>5}{t:>9}  b2={mp.nstr(b2, 12):>16}  b3={mp.nstr(b3, 12):>16}")

    assertions = [
        {"name": "every measured fpn is strictly below 2/3",
         "passed": all(r["fpn_below_threshold"] for r in results)},
        {"name": "the cap 3*fpn-2 is negative in every combination",
         "passed": all(r["cap_negative"] for r in results)},
        {"name": "b3 < 0 for EVERY edge set, every typing, every convention",
         "passed": all(row["b3_negative"] for r in results
                       for row in r["edge_sets"])},
        {"name": "b3 respects the Lean cap b3 <= 3*fpn-2 everywhere",
         "passed": all(row["respects_cap"] for r in results
                       for row in r["edge_sets"])},
        {"name": "AME's own b3 is POSITIVE (+1.426222 MeV), so the sign fails",
         "passed": bool(((AME["3H"] + AME["3He"]) / 2 - 3 * AME["D"]) > 0)},
    ]

    witness = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "The multiplicative assembly W = 1 - PROD f cannot yield a positive "
            "3-body Ursell cumulant while fpn <= 2/3. Bound b3 <= 3*fpn - 2 "
            "follows from P3 >= 0 alone, so it is independent of the edge set, "
            "the like-pair factors, and the energy scale."),
        "q0_pin": "proton",
        "q0": Q_50_DIGIT_STR,
        "threshold": mp.nstr(THRESHOLD, 20),
        "results": results,
        "cross_check_2026_08_29_MeV": xchecks,
        "ame_b3_MeV": mp.nstr((AME["3H"] + AME["3He"]) / 2 - 3 * AME["D"], 12),
        "assertions": assertions,
        "free_parameters": 0,
        "scope": ("(b) on the conjunction {multiplicative assembly, fpn <= 2/3}; "
                  "invariant = positivity of a product of positive bond factors. "
                  "Does NOT exclude the bond picture and does NOT close the "
                  "magnitude."),
        "lean": "QOU/MassTheory/MayerThreeBodySign.lean (sorry-free)",
        "related": [
            "probes/he4-body-order-shortfall-location.witness.json",
            "folio/quantum-observable-universe/mass-theory/binding-closure-conditional.md",
        ],
        "owner_ruling": "R1 2026-08-15 — convention D canonical, C excised",
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = _HERE / "mayer-threebody-sign-threshold.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")

    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"\n  Witness: {out.name}   allPassed={witness['allPassed']}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
