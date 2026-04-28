#!/usr/bin/env python3
"""Neutron-gap probes — round 6 (per-nucleon trace deficit assembly).

Round 1-3: nucleon-only Wedderburn / 3-input Skein-pair → CLOSED.
Round 4: naive |tr_M(atom)| · E0 → fails atoms at ~10¹¹ ppb.
Round 5: brane-tower + proton calibration → 2.9× better, still fails.
Round 6 (this script): test per-nucleon TRACE-DEFICIT assembly.

Hypothesis: atomic binding energy is the categorical trace deficit
  B_pred = E0 · |Z · tr_M(p) + N · tr_M(n) - tr_M(atom)|

with E0 calibrated on the proton:
  E0 = m_p_AME / |tr_M(p)|.

Equivalently: an atom's mass is the linear sum of nucleon-tr_M values
PLUS the trace overshoot of the atomic value, scaled by E0.

  M_atom_pred = E0 · (Z · tr_M(p) + N · tr_M(n) - (Z·tr_M(p) + N·tr_M(n) - tr_M(atom)))
              = E0 · tr_M(atom)   ← falls back to round-4

So the difference vs round-4 is in how we extract BINDING. Round 4
takes B = (Z·m_p + N·m_n + Z·m_e) - M_atom; round 6 takes B = E0 · TRACE
DEFICIT directly without going through atomic mass.

Output: neutron-gap-probes-round6.witness.json
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from q_parameter import Q as Q0_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_DPS = 50

ATOMIC_WITNESS_IN = HERE / "atomic-tr-m-mpfr-50dps.witness.json"

# AME binding energies (MeV)
B_AME = {
    "deuteron": 2.22456612,
    "tritium":  8.4817984,
    "helium-3": 7.7180375,
}

Z_N = {
    "proton":   (1, 0),
    "neutron":  (0, 1),
    "deuteron": (1, 1),
    "tritium":  (1, 2),
    "helium-3": (2, 1),
}


def main() -> int:
    if not ATOMIC_WITNESS_IN.exists():
        print(f"[ERROR] missing input: {ATOMIC_WITNESS_IN}")
        return 1

    atomic = json.loads(ATOMIC_WITNESS_IN.read_text())
    tr_M = {r["atom"]: r["tr_M_at_q0_50dps"] for r in atomic["results"]}

    print("=" * 100)
    print("NEUTRON-GAP PROBES — ROUND 6 (per-nucleon trace-deficit assembly)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  Hypothesis: B_pred = E0 · |Z·tr_M(p) + N·tr_M(n) − tr_M(atom)|")
    print()

    with mp.workdps(_DPS):
        tr_p = mp.mpf(tr_M["proton"])
        tr_n = mp.mpf(tr_M["neutron"])
        m_p = mp.mpf(str(M_P_MEV))
        m_n = mp.mpf(str(M_N_MEV))
        m_e = mp.mpf(str(M_E_MEV))

        # Calibrate E0 on the proton (single-point; no fit)
        E0 = m_p / mp.fabs(tr_p)
        print(f"  E0 = {mp.nstr(E0, 10)} MeV/(tr_M unit)")
        print()

        # Sanity: neutron mass via E0 · |tr_M(n)|
        m_n_pred = mp.fabs(tr_n) * E0
        n_residual_ppb = (m_n_pred - m_n) / m_n * mp.mpf(10**9)
        print(f"  Neutron sanity (round-4 style): "
              f"m_n_pred = {mp.nstr(m_n_pred, 12)} MeV "
              f"(AME {M_N_MEV}), residual = {float(n_residual_ppb):+.2e} ppb")
        print()

        results = []
        for atom_key, b_ame in B_AME.items():
            if atom_key not in tr_M:
                continue
            Z, N = Z_N[atom_key]
            tr_atom = mp.mpf(tr_M[atom_key])
            # Trace deficit
            sum_nucleon_tr = Z * tr_p + N * tr_n
            deficit = sum_nucleon_tr - tr_atom
            B_pred = E0 * mp.fabs(deficit)
            B_AME_mp = mp.mpf(str(b_ame))
            B_err_pct = (B_pred - B_AME_mp) / B_AME_mp * 100
            B_err_ppb = B_err_pct * mp.mpf(10**7)

            # Also compute round-4 style for direct comparison
            constituent_sum = Z * m_p + N * m_n + Z * m_e
            M_atom_r4 = mp.fabs(tr_atom) * E0
            B_r4 = constituent_sum - M_atom_r4
            B_err_r4_ppb = (B_r4 - B_AME_mp) / B_AME_mp * mp.mpf(10**9)

            results.append({
                "atom": atom_key,
                "Z": Z, "N": N, "A": Z + N,
                "tr_M_atom": mp.nstr(tr_atom, 30),
                "Z_tr_p_plus_N_tr_n": mp.nstr(sum_nucleon_tr, 30),
                "trace_deficit": mp.nstr(deficit, 30),
                "B_AME_MeV": b_ame,
                "B_pred_MeV_round6": mp.nstr(B_pred, 20),
                "B_err_ppb_round6": float(B_err_ppb),
                "B_err_ppb_round4_compare": float(B_err_r4_ppb),
            })

        print(f"  {'atom':<10} {'Z':>2} {'N':>2} {'B_AME':>9} "
              f"{'B_pred (R6)':>13} {'err R6 [ppb]':>16} {'err R4 [ppb]':>16}")
        print(f"  {'-'*10} {'-'*2} {'-'*2} {'-'*9} {'-'*13} {'-'*16} {'-'*16}")
        for r in results:
            print(f"  {r['atom']:<10} {r['Z']:>2} {r['N']:>2} "
                  f"{r['B_AME_MeV']:>9.4f} "
                  f"{float(r['B_pred_MeV_round6']):>13.4f} "
                  f"{r['B_err_ppb_round6']:>+16.4e} "
                  f"{r['B_err_ppb_round4_compare']:>+16.4e}")
        print()

        # Verdict
        worst_r6 = max(results, key=lambda r: abs(r["B_err_ppb_round6"]))
        worst_r4 = max(results, key=lambda r: abs(r["B_err_ppb_round4_compare"]))
        if abs(worst_r6["B_err_ppb_round6"]) < abs(worst_r4["B_err_ppb_round4_compare"]):
            improvement = (
                abs(worst_r4["B_err_ppb_round4_compare"]) /
                max(abs(worst_r6["B_err_ppb_round6"]), mp.mpf("1e-30"))
            )
            verdict = (f"R6 improves on R4 by {float(improvement):.2f}× on worst-atom "
                       f"({worst_r6['atom']}: R6 = {worst_r6['B_err_ppb_round6']:+.2e} ppb, "
                       f"R4 = {worst_r4['B_err_ppb_round4_compare']:+.2e} ppb)")
        else:
            verdict = (f"R6 does NOT improve on R4 — trace-deficit hypothesis falsified. "
                       f"Worst R6: {worst_r6['atom']} = {worst_r6['B_err_ppb_round6']:+.2e} ppb")
        print(f"  VERDICT: {verdict}")

    w = (
        WitnessBuilder("neutron-gap-probes-round6", engine="mpmath")
        .set_description(
            "Round-6 probe: tests the per-nucleon trace-deficit "
            "hypothesis B_pred = E0 · |Z·tr_M(p) + N·tr_M(n) − tr_M(atom)| "
            "against AME binding energies for D / T / ³He. Compared to "
            "round-4's |tr_M(atom)| · E0 - constituent_sum. Both calibrate "
            "E0 on the proton; difference is in the binding extraction."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q0_FLOAT)
        .add_parameter("m_p_codata_MeV", M_P_MEV)
        .add_parameter("m_n_codata_MeV", M_N_MEV)
        .add_parameter("m_e_codata_MeV", M_E_MEV)
        .add_parameter("precision_dps", _DPS)
        .add_parameter("hypothesis", "B = E0 · |Z·tr_M(p) + N·tr_M(n) − tr_M(atom)|")
        .add_data("results", results)
        .add_data("verdict", verdict)
        .add_data("attestation", {
            "used_fitting": False,
            "used_root_find": False,
            "uses_codata_inputs": True,
            "uses_upstream_atomic_tr_m": True,
        })
    )
    out_path = w.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
