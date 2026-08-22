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
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
    M_DEUTERON_MEV_VALIDATION, M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)

set_compute_dps()

# Empirical binding energies / masses (MeV), exploratory comparison targets
# only (not substrate inputs). Both columns are now READ from the registry.
#
# The masses were hand-typed and each was wrong: d -17.0 eV (-9.1 ppb),
# He3 -4.1 eV (-1.5 ppb), He4 -33.8 eV (-9.1 ppb) against the validation
# witness. Same defect class as bean qou-r8zo, where a sibling dashboard
# carried four hand-typed nuclear masses and two were ~250 sigma out --
# and the B column here was already read from the registry while the m
# column beside it was not.
#
# They are also no longer round-tripped through float64. The old shape was
#     "B": float(AME_B_..._VALIDATION)      then    mp.mpf(repr(v["B"]))
# which takes an exact mpf, truncates it to a float, and rebuilds an mpf
# from the float's digits -- so the registry's precision was discarded at
# the door and the `mp.mpf` on the way back in bought nothing. A probe is
# a computations/ script and is covered by the NO-FLOAT64 family.
EMPIRICAL = {
    "d":   {"B": AME_B_DEUTERON_MEV_VALIDATION, "m": M_DEUTERON_MEV_VALIDATION},
    "He3": {"B": AME_B_HE3_MEV_VALIDATION,      "m": M_HE3_MEV_VALIDATION},
    "He4": {"B": AME_B_HE4_MEV_VALIDATION,      "m": M_HE4_MEV_VALIDATION},
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
        bm = v["B"] / v["m"]
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
                # Serialised as strings: a bare mpf is not JSON, and a bare
                # float64 would trip the raw-float64 ratchet.
                "empirical_inputs_MeV": {
                    k: {kk: str(vv) for kk, vv in v.items()}
                    for k, v in EMPIRICAL.items()
                },
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
