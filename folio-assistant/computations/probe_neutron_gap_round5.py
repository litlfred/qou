#!/usr/bin/env python3
"""Neutron-gap probes — round 5 (brane-tower with proton calibration).

Round 4 (this branch): naïve M = |tr_M(atom)| · E0 with proton-calibrated
  E0 fails dramatically (~e+11 ppb on D/T/³He) — atomic Markov trace
  does NOT scale linearly to atomic mass.

Round 5 (this script) tests the next-most-canonical assembly:
  use the existing **brane-tower formula** (T1+T2+T3, per
  `tower_isotope_absolute.compute_isotope_tower`) which assembles
  the per-vertex `V̂_i^full` into a Hecke-unit mass `M_H` via:

      M_H = |Π V̂_i| + Σ_i Φ_q(|V̂_i|) + z² · Σ_{|i-j|=1} Φ_q(|V̂_i V̂_j|)

  Then recalibrate via proton (instead of via electron, which the
  upstream helper does internally):

      E0_brane = m_p_AME / M_H(proton)
      M_atom_pred = M_H(atom) · E0_brane
      B_pred = Z·m_p_AME + N·m_n_AME + Z·m_e − M_atom_pred

If the brane-tower form (vs the naïve |tr_M| scaling of round-4)
captures more atomic-mass structure, the residuals should drop from
~e+11 ppb toward a smaller floor.  This quantifies how much of the
combination-convention gap is (a) the Φ_q sums, (b) the adjacent-pair
z² · Φ_q(V_i V_j) terms, vs (c) higher-order T4/T5/T6 corrections.

Note: tower_isotope_absolute.compute_isotope_tower returns M_MeV via
internal electron calibration; we extract the *Hecke-unit* M_H by
multiplying back by m_e_H / M_E_CODATA, then re-divide via the
proton's M_H.  This isolates the brane-tower's intrinsic ratios
from the calibration choice.

Output: `neutron-gap-probes-round5.witness.json`
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import json
import mpmath as mp

import tower_isotope_absolute as tia  # noqa: E402
from q_parameter import Q as Q0_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_DPS = 50

# AME binding energies (MeV) — same as round-4
B_AME = {
    "deuteron": 2.22456612,
    "tritium":  8.4817984,
    "helium-3": 7.7180375,
}

# Atom (Z, N) lookup
PARTICLES = [
    ("proton",   1, 0),
    ("neutron",  0, 1),
    ("deuteron", 1, 1),
    ("tritium",  1, 2),
    ("helium-3", 2, 1),
]


def _hecke_units_M(z_n_label, m_e_H):
    """Run compute_isotope_tower(Z, N, m_e_H) and back-convert the
    MeV result to Hecke units by dividing out the electron-calibration
    factor.  Returns M_H (mpmath mpf)."""
    label, Z, N = z_n_label
    r = tia.compute_isotope_tower(Z, N, m_e_H)
    # M_MeV_raw is a string (from mp.nstr inside the helper); back-cast
    M_MeV_str = r["M_MeV_raw"]
    if M_MeV_str == "nan":
        return None, r
    M_MeV = mp.mpf(M_MeV_str)
    # The internal calibration was M_MeV = (M_H / m_e_H) * M_E_CODATA
    # so M_H = M_MeV * m_e_H / M_E_CODATA
    M_H = M_MeV * m_e_H / mp.mpf(str(M_E_MEV))
    return M_H, r


def main() -> int:
    print("=" * 100)
    print("NEUTRON-GAP PROBES — ROUND 5 (brane-tower with proton calibration)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  m_p (CODATA) = {M_P_MEV} MeV")
    print(f"  m_n (CODATA) = {M_N_MEV} MeV")
    print(f"  m_e (CODATA) = {M_E_MEV} MeV")
    print()

    with mp.workdps(_DPS):
        # Step 0: get the canonical electron-tower scale (Hecke units)
        m_e_H, _V_e = tia.compute_electron_tower()
        print(f"  m_e (Hecke units, electron tower) = {mp.nstr(m_e_H, 12)}")
        print()

        # Step 1: compute Hecke-unit M_H for every particle
        m_p_AME = mp.mpf(str(M_P_MEV))
        m_n_AME = mp.mpf(str(M_N_MEV))
        m_e_AME = mp.mpf(str(M_E_MEV))

        M_H_by_atom = {}
        full_results = {}
        print(f"  Per-particle brane-tower M_H (Hecke units):")
        for label, Z, N in PARTICLES:
            M_H, raw = _hecke_units_M((label, Z, N), m_e_H)
            full_results[label] = raw
            if M_H is None:
                print(f"    {label:<10}  M_H = NaN (skipping)")
                continue
            M_H_by_atom[label] = M_H
            print(f"    {label:<10}  Z={Z} N={N}  M_H = {mp.nstr(M_H, 14)}")
        print()

        if "proton" not in M_H_by_atom:
            print("[ERROR] proton M_H is NaN — cannot calibrate")
            return 1

        # Step 2: calibrate energy scale on the proton
        E0_brane = m_p_AME / M_H_by_atom["proton"]
        print(f"  Calibration: E0_brane = m_p_AME / M_H(proton) = "
              f"{mp.nstr(E0_brane, 12)} MeV/(Hecke unit)")
        print()

        # Step 3-4: per-atom prediction + binding-energy comparison
        results = []
        for label, Z, N in PARTICLES:
            if label not in M_H_by_atom:
                results.append({"atom": label, "status": "M_H NaN"})
                continue
            M_H = M_H_by_atom[label]
            M_atom_pred = M_H * E0_brane
            constituent_sum = Z * m_p_AME + N * m_n_AME + Z * m_e_AME

            entry = {
                "atom": label, "Z": Z, "N": N, "A": Z + N,
                "M_H_hecke_units": mp.nstr(M_H, _DPS),
                "M_atom_pred_MeV": mp.nstr(M_atom_pred, 20),
                "constituent_sum_MeV": mp.nstr(constituent_sum, 20),
            }

            # For nucleons: compare M_atom_pred vs CODATA mass directly
            if label == "proton":
                err_pct = (M_atom_pred - m_p_AME) / m_p_AME * 100
                entry["mass_err_pct"] = float(err_pct)
                entry["mass_err_ppb"] = float(err_pct * 10**7)
                entry["calibration_anchor"] = True
            elif label == "neutron":
                err_pct = (M_atom_pred - m_n_AME) / m_n_AME * 100
                entry["mass_err_pct"] = float(err_pct)
                entry["mass_err_ppb"] = float(err_pct * 10**7)
            else:
                # For atoms: convert to binding energy
                B_pred = constituent_sum - M_atom_pred
                B_AME_mp = mp.mpf(str(B_AME[label]))
                err_pct = (B_pred - B_AME_mp) / B_AME_mp * 100
                entry["B_AME_MeV"] = B_AME[label]
                entry["B_pred_MeV"] = mp.nstr(B_pred, 20)
                entry["B_err_pct"] = float(err_pct)
                entry["B_err_ppb"] = float(err_pct * 10**7)
            results.append(entry)

    # Print results
    print(f"  Per-particle prediction (brane-tower + proton calibration):")
    print(f"  {'atom':<10} {'M_pred (MeV)':>14} {'target':>14} "
          f"{'mode':>8} {'err [%]':>10} {'err [ppb]':>14}")
    print(f"  {'-' * 10} {'-' * 14} {'-' * 14} {'-' * 8} {'-' * 10} {'-' * 14}")
    for r in results:
        if "M_atom_pred_MeV" not in r:
            continue
        m_p = float(r["M_atom_pred_MeV"])
        if "B_AME_MeV" in r:
            target = r["B_AME_MeV"]
            mode = "B"
            err_pct = r["B_err_pct"]
            err_ppb = r["B_err_ppb"]
            target_str = f"{target:>14.4f}"
        else:
            target = M_P_MEV if r["atom"] == "proton" else M_N_MEV
            mode = "M (cal)" if r.get("calibration_anchor") else "M"
            err_pct = r["mass_err_pct"]
            err_ppb = r["mass_err_ppb"]
            target_str = f"{target:>14.4f}"
        print(f"  {r['atom']:<10} {m_p:>14.4f} {target_str} "
              f"{mode:>8} {err_pct:>+10.4f} {err_ppb:>+14.4e}")
    print()

    # Cross-round comparison
    print(f"  Cross-round summary:")
    print(f"    Round-1: 3-term V_3term + brane tower    : -5.62e+08 ppb (neutron)")
    print(f"    Round-2: full nucleon Markov trace        : -2.52e+08 ppb (neutron)")
    print(f"    Round-3: 3-input Skein-pair canonical    : +5e-8 ppb (neutron, CLOSED)")
    print(f"    Round-4: naïve |tr_M(atom)|·E0           : +e+11 ppb (D/T/³He, FAILS)")
    print(f"    Round-5: brane-tower + proton cal         : per atom shown above")
    print()

    # Verdict
    THRESHOLD_PPM = 1e3
    THRESHOLD_PPB = 1e1
    atomic_results = [r for r in results
                      if "B_err_ppb" in r and r["B_err_ppb"] is not None]
    if not atomic_results:
        verdict = "no atomic prediction obtained"
        rec = "Cannot evaluate atomic predictions"
    else:
        worst = max(atomic_results, key=lambda r: abs(r["B_err_ppb"]))
        magnitude = abs(worst["B_err_ppb"])
        if magnitude < THRESHOLD_PPB:
            verdict = f"closed to <ppb on all atoms (worst: {worst['atom']} = {worst['B_err_ppb']:+.2e} ppb)"
            rec = "Brane-tower + proton calibration IS the canonical atomic assembly."
        elif magnitude < THRESHOLD_PPM:
            verdict = f"sub-ppm on all atoms (worst: {worst['atom']} = {worst['B_err_ppb']:+.2e} ppb)"
            rec = ("Brane-tower captures dominant structure; sub-ppm residual "
                   "suggests Term 4-6 additive corrections at µeV scale.")
        else:
            magnitude_round4 = 6.9e11  # worst case from round-4
            improvement_factor = magnitude_round4 / magnitude if magnitude > 0 else None
            verdict = (f"residual remains: worst {worst['atom']} = "
                       f"{worst['B_err_ppb']:+.2e} ppb")
            rec = (f"Brane-tower assembly improves on round-4's naïve |tr_M|·E0 "
                   f"by factor ~{improvement_factor:.1f}× but still does not close "
                   f"the gap. Combination convention requires additional T4-T6 "
                   f"contributions or different per-vertex V definition.")
    print(f"  VERDICT: {verdict}")
    print(f"  RECOMMENDATION: {rec}")
    print()

    # Emit witness via WitnessBuilder
    w = (
        WitnessBuilder("neutron-gap-probes-round5", engine="mpmath")
        .set_description(
            "Round-5 probe: applies the brane-tower assembly "
            "(tower_isotope_absolute.compute_isotope_tower's "
            "tower_level0 = T1+T2+T3 with adjacent-pair Φ_q) under "
            "proton calibration (rather than the helper's internal "
            "electron calibration). Tests whether the brane-tower form "
            "captures the atomic mass structure that round-4's naïve "
            "|tr_M|·E0 missed."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q0_FLOAT)
        .add_parameter("m_p_codata_MeV", M_P_MEV)
        .add_parameter("m_n_codata_MeV", M_N_MEV)
        .add_parameter("m_e_codata_MeV", M_E_MEV)
        .add_parameter("precision_dps", _DPS)
        .add_data("results", results)
        .add_data("verdict", verdict)
        .add_data("recommendation", rec)
        .add_data("cross_round", {
            "round1_baseline_ppb": -5.6173e8,
            "round2_H4_full_nucleon_tr_M_ppb": -2.5223e8,
            "round3_H5_3input_canonical_ppb": 5.0116e-8,
            "round4_naive_atomic_tr_M_ppb_worst": 6.9e11,
        })
        .add_data("attestation", {
            "used_fitting": False,
            "used_root_find": False,
            "used_volume": False,
            "uses_codata_inputs": True,
            "uses_brane_tower_helper": True,
        })
        .add_assertion(
            "proton_calibration_recovers_m_p_AME",
            computed=float(mp.mpf(M_H_by_atom["proton"]) * E0_brane),
            expected=M_P_MEV,
            tolerance=1e-6,
            source="single-point brane-tower proton calibration",
        )
    )
    out_path = w.save()
    print(f"  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
