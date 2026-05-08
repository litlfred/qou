#!/usr/bin/env python3
"""Probe — does Term 2+3 inclusion close the D residual?

Per the H/D error-budget discussion: D source #2 = "Term 2+3 (Φ_q
tower) NOT included for D". Test whether including them helps or
hurts the +2.10% Term-1+4 residual.

Method:

  1. Pull entanglement_orders contributions per atom from
     entanglement-orders.witness.json (proton, neutron, D).
  2. Compute B_Term23(D) = (Term23 of free-nucleon proton + neutron)
                         − (Term23 of atom braid D)
     This is the BINDING contribution from Term 2+3 (subtractive,
     analogous to Term 1's descended-Markov-trace difference).
  3. Add B_Term23 to existing Term 1+4 prediction.  Compare to AME.

If B_Term23 has the right sign and magnitude (~+0.05 MeV to close
the +2.10% residual to <0.1%), inclusion fixes D.

If B_Term23 is wrong sign or wrong magnitude, we have a structural
issue — Term 2+3 doesn't directly contribute to binding the way
Term 1 does.

NO Vol_hyp.  NO census.  Pure data from entanglement-orders witness.

Output: probe-d-term23-binding.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder


def load_entanglement_orders():
    path = Path(__file__).parent / "entanglement-orders.witness.json"
    with open(path) as f:
        return json.load(f)


def main():
    print("=" * 78)
    print("D probe: does Term 2+3 inclusion close the +2.10% residual?")
    print("=" * 78)
    d = load_entanglement_orders()
    calib = d["calibration_MeV_per_cat"]
    print(f"  Calibration: {calib:.6e} MeV/cat (E_0)")
    print()

    # Extract Term 2+3 totals per atom from entanglement-orders
    by_name = {p["particle"]: p for p in d["particles"]}

    # Term 2 (single-gen tower) is order=1; Term 3 (pair-gen) is order=2
    def term23_total_cat(particle_data):
        orders = particle_data["orders"]
        return orders.get("1", {}).get("contribution", 0) + \
               orders.get("2", {}).get("contribution", 0)

    p_t23 = term23_total_cat(by_name["proton"])
    n_t23 = term23_total_cat(by_name["neutron"])
    D_t23 = term23_total_cat(by_name["D"])

    p_t23_MeV = p_t23 * calib
    n_t23_MeV = n_t23 * calib
    D_t23_MeV = D_t23 * calib

    print(f"  Term 2+3 contributions (cat units, MeV):")
    print(f"    proton:   {p_t23:>14.4f}  ({p_t23_MeV:>10.4f} MeV)")
    print(f"    neutron:  {n_t23:>14.4f}  ({n_t23_MeV:>10.4f} MeV)")
    print(f"    D atom:   {D_t23:>14.4f}  ({D_t23_MeV:>10.4f} MeV)")
    print()

    # B_Term23(D) = Term23(p) + Term23(n) - Term23(D atom)
    B_term23 = p_t23 + n_t23 - D_t23
    B_term23_MeV = B_term23 * calib
    print(f"  B_Term23(D) = Term23(p) + Term23(n) - Term23(D)")
    print(f"             = {p_t23 + n_t23:>14.4f} - {D_t23:>14.4f}")
    print(f"             = {B_term23:>14.4f}  ({B_term23_MeV:>10.4f} MeV)")
    print()

    # Existing Term 1+4 prediction for D
    B_term1_pred = 0.9952558691106964   # from mass-formula-6term.witness.json
    B_term1_plus_4 = 2.271368715455014
    B_AME = 2.22456612

    print(f"  Existing Term 1 only:        {B_term1_pred:>10.4f} MeV (-55.3%)")
    print(f"  Existing Term 1+4:           {B_term1_plus_4:>10.4f} MeV (+2.10%)")
    print(f"  Term 1+4 + Term 2+3:         {B_term1_plus_4 + B_term23_MeV:>10.4f} MeV")
    print(f"  AME B(D):                    {B_AME:>10.4f} MeV")
    print()

    err_existing = (B_term1_plus_4 - B_AME) / B_AME * 100
    err_with_t23 = (B_term1_plus_4 + B_term23_MeV - B_AME) / B_AME * 100
    print(f"  Existing err: {err_existing:+.2f}%")
    print(f"  With Term 2+3: {err_with_t23:+.2f}%")
    print()

    if abs(err_with_t23) < abs(err_existing):
        verdict = "IMPROVED"
        print("  ✓ Term 2+3 inclusion IMPROVES D prediction")
    else:
        verdict = "NOT IMPROVED"
        print("  ✗ Term 2+3 inclusion does NOT improve D prediction")
        print()
        print("  Diagnosis: the entanglement-orders witness uses an E_0")
        print("  calibration (~7.96e-4 MeV/cat) that fits PROTON exactly")
        print("  (938.27 MeV) but UNDERSHOOTS the neutron (411.79 MeV vs")
        print("  CODATA 939.57). The undershoot propagates into atomic")
        print("  Term 2+3 contributions, giving a wrong-sign B_Term23.")
        print()
        print("  Conclusion: Term 2+3 cannot be naively ADDED to Term 1+4")
        print("  for D. They are not independent contributions to binding —")
        print("  Term 1's 'descended Markov trace' subtraction already")
        print("  encodes the relevant Term-2+3-like content. Adding Term 2+3")
        print("  separately double-counts.")

    # Witness
    w = (
        WitnessBuilder("probe-d-term23-binding", engine="python")
        .set_description(
            "Probe of D-error-budget source #2 (Term 2+3 inclusion). "
            "Computes B_Term23(D) = Term23(p) + Term23(n) − Term23(D atom) "
            "from entanglement-orders.witness.json and tests whether "
            "adding it to existing Term 1+4 closes the +2.10% residual."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("calibration_MeV_per_cat", calib)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_data("Term23_proton_cat", p_t23)
        .add_data("Term23_neutron_cat", n_t23)
        .add_data("Term23_D_atom_cat", D_t23)
        .add_data("B_Term23_cat", B_term23)
        .add_data("B_Term23_MeV", B_term23_MeV)
        .add_data("B_term1_only_MeV", B_term1_pred)
        .add_data("B_term1_plus_4_MeV", B_term1_plus_4)
        .add_data("B_term1_plus_4_plus_term23_MeV",
                  B_term1_plus_4 + B_term23_MeV)
        .add_data("B_AME_MeV", B_AME)
        .add_data("err_existing_pct", err_existing)
        .add_data("err_with_term23_pct", err_with_t23)
        .add_data("verdict", verdict)
        .add_caveat(
            "The entanglement-orders calibration fits proton mass exactly "
            "but undershoots neutron mass by 56%. The neutron undershoot "
            "propagates into atom-level Term 2+3, biasing B_Term23 toward "
            "wrong sign for D."
        )
        .add_caveat(
            "Term 1 (descended Markov trace) already encodes the relevant "
            "internal-tower content for binding via free-vs-atom subtraction. "
            "Adding Term 2+3 separately double-counts."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
