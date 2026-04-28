#!/usr/bin/env python3
"""Neutron-gap probes — round 4 (canonical AME assembly via atomic tr_M).

Round 1 (PR #452): single-channel Wedderburn tweaks → null.
Round 2 (this branch): full nucleon Markov trace → −25 % on neutron.
Round 3 (this branch): 3-input Skein-pair canonical → +5e-8 ppb on
  neutron. CLOSED the n/p split via Q_β as third structural input.
Round 4 (this script): apply the round-3 canonical assembly to the
  ATOMIC tr_M values landed upstream in PR #454
  (`atomic-tr-m-mpfr-50dps.witness.json`):

  1. Calibrate energy scale on the proton:
       E0 = m_p_AME / |tr_M(proton, q_0)|
  2. For each atom (D, T, ³He), predict atomic mass:
       M_atom_pred = |tr_M(atom, q_0)| · E0
  3. Convert to binding energy:
       B_pred = Z·m_p_AME + N·m_n_AME + Z·m_e − M_atom_pred
  4. Compare to AME binding-energy b_ame_mev.

This tests the conjecture: does the upstream atomic tr_M (3A-strand
convention, 50 dps via Hoefsmit + Wenzl bridge) combined with the
canonical proton-calibration assembly close the D/T/³He gap to
sub-ppm or sub-ppb?

If yes → atomic mass-prediction pipeline is largely solved; combination
convention is just `M = |tr_M| · E0` for atoms, no further T2/T3/T4/T5/T6
additive corrections needed at this precision.

If no → quantifies the remaining theory work.

Output: `neutron-gap-probes-round4.witness.json`
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder

_DPS = 50

ATOMIC_WITNESS_IN = HERE / "atomic-tr-m-mpfr-50dps.witness.json"
JOINT_TOWER_WITNESS_IN = HERE / "joint-tower-sdp-rust.witness.json"

# AME binding energies (MeV) — same source as Sprint A v3 inputs.
B_AME = {
    "deuteron": 2.22456612,
    "tritium":  8.4817984,
    "helium-3": 7.7180375,
}

# Atom (Z, N) lookup
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
    tr_M_by_atom = {r["atom"]: r["tr_M_at_q0_50dps"] for r in atomic["results"]}

    print("=" * 100)
    print("NEUTRON-GAP PROBES — ROUND 4 (canonical AME assembly via atomic tr_M)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  m_p (CODATA) = {M_P_MEV} MeV")
    print(f"  m_n (CODATA) = {M_N_MEV} MeV")
    print(f"  m_e (CODATA) = {M_E_MEV} MeV")
    print(f"  source: {ATOMIC_WITNESS_IN.name}")
    print()

    # Atomic tr_M values from upstream PR #454
    print(f"  Atomic tr_M values (3A-strand convention, 50 dps):")
    for atom, tm in tr_M_by_atom.items():
        print(f"    tr_M({atom:<10}) = {tm[:30]}")
    print()

    if "proton" not in tr_M_by_atom:
        print("[ERROR] proton tr_M missing from upstream witness")
        return 1

    with mp.workdps(_DPS):
        tr_p = mp.mpf(tr_M_by_atom["proton"])
        m_p_AME = mp.mpf(str(M_P_MEV))
        m_n_AME = mp.mpf(str(M_N_MEV))
        m_e_AME = mp.mpf(str(M_E_MEV))

        # Step 1: calibrate energy scale on the proton (single point, no fit)
        E0 = m_p_AME / mp.fabs(tr_p)
        print(f"  Calibration: E0 = m_p_AME / |tr_M(proton)| = "
              f"{mp.nstr(E0, 12)} MeV/(tr_M unit)")
        print()

        results = []
        # Step 2-4: per-atom prediction
        for atom_key, b_ame_val in B_AME.items():
            if atom_key not in tr_M_by_atom:
                results.append({
                    "atom": atom_key,
                    "status": "tr_M missing from upstream witness",
                })
                continue
            Z, N = Z_N[atom_key]
            tr_atom = mp.mpf(tr_M_by_atom[atom_key])
            # Step 2: atomic mass prediction
            M_atom_pred = mp.fabs(tr_atom) * E0
            # Step 3: binding energy via constituent sum minus atomic mass
            constituent_sum = Z * m_p_AME + N * m_n_AME + Z * m_e_AME
            B_pred = constituent_sum - M_atom_pred
            B_AME_mp = mp.mpf(str(b_ame_val))
            B_err_pct = (B_pred - B_AME_mp) / B_AME_mp * 100
            B_err_ppb = B_err_pct * mp.mpf(10**7)
            results.append({
                "atom": atom_key,
                "Z": Z,
                "N": N,
                "A": Z + N,
                "tr_M_atom_50dps": mp.nstr(tr_atom, _DPS),
                "M_atom_pred_MeV": mp.nstr(M_atom_pred, 20),
                "constituent_sum_MeV": mp.nstr(constituent_sum, 20),
                "B_AME_MeV": b_ame_val,
                "B_pred_MeV": mp.nstr(B_pred, 20),
                "B_err_pct": float(B_err_pct),
                "B_err_ppb": float(B_err_ppb),
            })

    # Print results
    print(f"  Per-atom binding-energy prediction (canonical assembly):")
    print(f"  {'atom':<12} {'Z':>2} {'N':>2} {'B_AME':>9} {'B_pred':>13} {'err [%]':>10} {'err [ppb]':>14}")
    print(f"  {'-' * 12} {'-' * 2} {'-' * 2} {'-' * 9} {'-' * 13} {'-' * 10} {'-' * 14}")
    for r in results:
        if "B_pred_MeV" not in r:
            print(f"  {r['atom']:<12}  --  --  {'—':>9} {'—':>13} {'—':>10} {'—':>14}  [{r.get('status', '?')}]")
            continue
        b_p = float(r["B_pred_MeV"])
        print(f"  {r['atom']:<12} {r['Z']:>2} {r['N']:>2} "
              f"{r['B_AME_MeV']:>9.4f} {b_p:>13.4f} "
              f"{r['B_err_pct']:>+10.4f} {r['B_err_ppb']:>+14.4e}")
    print()

    # Cross-round comparison
    print(f"  Cross-round comparison (neutron only):")
    print(f"    Round-1 baseline (3-term V_3term): -5.6173e+08 ppb")
    print(f"    Round-2 H4 (full nucleon tr_M):    -2.5223e+08 ppb")
    print(f"    Round-3 H5 (3-input Skein-pair):   +5.0116e-08 ppb (CLOSED)")
    print(f"    Round-4 atomic assembly: ppb errors per atom shown above")
    print()

    # Verdict
    THRESHOLD_PPM = 1e3  # 1 ppm = 1e3 ppb
    THRESHOLD_PPB = 1e1
    finite_rs = [r for r in results if "B_err_ppb" in r]
    if not finite_rs:
        verdict = "no atom evaluated"
        rec = "Cannot evaluate without per-atom tr_M"
    else:
        worst = max(finite_rs, key=lambda r: abs(r["B_err_ppb"]))
        if abs(worst["B_err_ppb"]) < THRESHOLD_PPB:
            verdict = f"closed to <ppb on all atoms (worst: {worst['atom']} = {worst['B_err_ppb']:+.2e} ppb)"
            rec = "Atomic assembly is canonical and complete; no T2/T3/T4/T5/T6 corrections needed at this precision."
        elif abs(worst["B_err_ppb"]) < THRESHOLD_PPM:
            verdict = f"closed to sub-ppm but >ppb (worst: {worst['atom']} = {worst['B_err_ppb']:+.2e} ppb)"
            rec = ("Atomic mass = |tr_M(atom)| · E0 captures the dominant "
                   "structure; remaining sub-ppm residual suggests Term 4-6 "
                   "additive corrections at the µeV scale.")
        else:
            verdict = f"residual remains: worst {worst['atom']} = {worst['B_err_ppb']:+.2e} ppb"
            rec = ("Naïve M = |tr_M| · E0 assembly does NOT close the gap "
                   "for atoms. Combination convention requires more than "
                   "proton-calibration; T2/T3/T4/T5/T6 contributions must "
                   "be added or the brane-tower assembly applied.")
    print(f"  VERDICT: {verdict}")
    print(f"  RECOMMENDATION: {rec}")
    print()

    # Emit witness
    w = (
        WitnessBuilder("neutron-gap-probes-round4", engine="mpmath")
        .set_description(
            "Round-4 canonical-assembly probe: applies round-3's "
            "proton-calibration scheme to upstream's atomic tr_M values "
            "(atomic-tr-m-mpfr-50dps.witness.json from PR #454, 3A-strand "
            "convention, 50 dps via Hoefsmit + Wenzl). Tests whether "
            "M = |tr_M(atom)| · E0 closes D/T/³He binding-energy ppb "
            "residual when E0 is calibrated on the proton."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q0_FLOAT)
        .add_parameter("m_p_codata_MeV", M_P_MEV)
        .add_parameter("m_n_codata_MeV", M_N_MEV)
        .add_parameter("m_e_codata_MeV", M_E_MEV)
        .add_parameter("precision_dps", _DPS)
        .add_parameter("source_witness", str(ATOMIC_WITNESS_IN.name))
        .add_data("results", results)
        .add_data("verdict", verdict)
        .add_data("recommendation", rec)
        .add_data("cross_round", {
            "round1_baseline_ppb": -5.6173e8,
            "round2_H4_full_nucleon_tr_M_ppb": -2.5223e8,
            "round3_H5_3input_canonical_ppb": 5.0116e-8,
            "note": "rounds 1-3 are nucleon-only; round-4 is atomic D/T/³He",
        })
        .add_data("attestation", {
            "used_fitting": False,
            "used_root_find": False,
            "used_volume": False,
            "uses_codata_inputs": True,
            "uses_upstream_atomic_tr_m": True,
        })
        # Sanity-only assertions (proton calibration is exact by construction)
        .add_assertion(
            "proton_calibration_recovers_m_p_AME",
            computed=float(mp.fabs(tr_p) * E0),
            expected=M_P_MEV,
            tolerance=1e-6,
            source="single-point E0 = m_p_AME / |tr_M(proton)|",
        )
    )
    out_path = w.save()
    print(f"  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
