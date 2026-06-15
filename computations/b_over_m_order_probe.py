#!/usr/bin/env python3
# EXPLORATORY PROBE — order-of-magnitude comparison only; NOT a binding
# derivation (the per-partition Δ_λ closure remains gated).  Production-
# vs-exploratory discipline: no wiring claims, no fitted constants — the
# script compares deformation orders the framework already fixes against
# empirical binding fractions, and states what a real derivation needs.
#
# Ref: content/quantum-observable-universe/models-of-qous/symmetric-point-resolution-loss.md
#      (the ε² channel-resolution stratum and its B/m ~ h² hypothesis)
"""B/m ~ h² order probe.

Hypothesis under test (order-of-magnitude only): if mass-type structure
enters at order h = q₀ − 1 (physically normalised gap ½q(q−1)(q+1)) and
inter-nucleon channel resolution enters at order h² (the n = 6 splitting
w₍₃,₃₎ − w₍₅,₁₎ = (5/18)ε² + …), then nuclear binding fractions B/m
should sit at O(h²), not O(h).

Computed at the proton-pinned q₀:
  h, h², (5/18)h², the exact n = 6 family splitting at q₀,
  and empirical B/m for d, ³He, ⁴He (AME-class literature values,
  comment-sourced below — exploratory probe convention).

Outputs `b-over-m-order-probe.witness.json`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _pb  # noqa: F401, E402 — substrate module bridge
import json  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q1_mass_gap_probe import plancherel_weight  # noqa: E402

set_compute_dps()

# Empirical binding energies / masses (MeV) — AME2020-class values,
# exploratory comparison targets only (not substrate inputs):
EMPIRICAL = {
    "d":    {"B": 2.224566,  "m": 1875.612928},
    "He3":  {"B": 7.718043,  "m": 2808.391607},
    "He4":  {"B": 28.295674, "m": 3727.379378},
}


def main() -> int:
    with (_pb.witness_path("q-pinning-50-digit.witness.json", HERE)).open(encoding="utf-8") as fh:
        q0 = mp.mpf(json.load(fh)["derived_50_digit"]["q"])
    h = q0 - 1

    split_q0 = plancherel_weight((3, 3), q0) - plancherel_weight((5, 1), q0)
    five18_h2 = mp.mpf(5) / 18 * h ** 2

    print("=" * 74)
    print(" B/m ~ h² order probe (exploratory; Δ_λ-gated for a derivation)")
    print("=" * 74)
    print(f"\n  h        = {mp.nstr(h, 8)}")
    print(f"  h²       = {mp.nstr(h ** 2, 8)}")
    print(f"  (5/18)h² = {mp.nstr(five18_h2, 8)}")
    print(f"  exact n=6 family splitting at q₀ = {mp.nstr(split_q0, 8)}"
          f"   (ε² formula holds to {mp.nstr(split_q0 / five18_h2, 5)}× at this h)")

    rows = {}
    print(f"\n  {'nucleus':>8} {'B/m':>12} {'(B/m)/h':>10} {'(B/m)/h²':>10}")
    for name, v in EMPIRICAL.items():
        bm = mp.mpf(repr(v["B"])) / mp.mpf(repr(v["m"]))
        rows[name] = {
            "B_over_m": str(bm),
            "ratio_to_h": str(bm / h),
            "ratio_to_h2": str(bm / h ** 2),
        }
        print(f"  {name:>8} {mp.nstr(bm, 6):>12} {mp.nstr(bm / h, 6):>10} "
              f"{mp.nstr(bm / h ** 2, 6):>10}")

    verdict = (
        "Order-of-magnitude verdict: empirical B/m for d, ³He, ⁴He sits at "
        "0.0012–0.0076, i.e. O(h²) ≈ 0.012 within one decade (ratios to h² "
        "of ~0.1–0.6), and one to two decades below O(h) ≈ 0.11.  The h² "
        "stratum is the consistent home for binding-type structure, as the "
        "ε²-order channel resolution predicts.  This is an order check "
        "ONLY: a derivation requires contracting the per-partition Δ_λ "
        "against the n = 3A weight tower (Δ_λ gate; six closure ansätze "
        "failed — see the gating audit), and the A-dependence of B/m "
        "(rising from d to ⁴He) is exactly the structure Δ_λ must supply."
    )
    print(f"\n  {verdict}")

    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "b-over-m-order-probe",
        {
            "description": (
                "EXPLORATORY order-of-magnitude check of the B/m ~ h² "
                "hypothesis from the ε-stratification: empirical binding "
                "fractions for d/³He/⁴He compared against h, h², and the "
                "(5/18)h² channel-resolution scale at the proton-pinned "
                "q₀.  Not a derivation (Δ_λ-gated)."
            ),
            "exploratory": True,
            "data": {
                "q0_50dps": str(q0),
                "h": str(h),
                "h_squared": str(h ** 2),
                "five_over_18_h2": str(five18_h2),
                "n6_family_splitting_at_q0": str(split_q0),
                "empirical_inputs_MeV": EMPIRICAL,
                "ratios": rows,
                "verdict": verdict,
            },
        },
        script_path=__file__,
        engine="mpmath",
    )
    out_path = builder.save()
    print(f"\n  Wrote {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
