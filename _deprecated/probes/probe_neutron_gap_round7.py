#!/usr/bin/env python3
"""Neutron-gap probes — round 7 (per-bond Skein-pair binding hypothesis).

Round 1-3: nucleon-only (closed at 5e-8 ppb via 3-input Skein-pair).
Round 4-6: atomic |tr_M|·E0 + variants → fail at ~10¹¹ ppb.

Round 7 hypothesis: extend round-3's 3-input Skein-pair scheme to
the atomic level. An atom (Z, N) has internal nucleon-nucleon bonds
of three types: p-p, p-n, n-n. Binding energy assembles as

  B = z_inv · (n_pp · μ_pp + n_pn · μ_pn + n_nn · μ_nn)

where z_inv = (q + q⁻¹) / (q^{1/2} + q^{-1/2}) is the Skein-pair
factor (round 3), n_·· are bond counts in the K_A complete-graph
topological model on Z+N nucleons, and μ_·· are three structural
inputs (analogous to Q_β at the nucleon level).

Calibration: D, T, ³He determine the 3 unknowns exactly (3
measurements, 3 inputs, no fitting). Predictions on ⁴He, ⁶Li, ⁷Li,
⁹Be, ¹²C, ¹⁶O test the per-bond hypothesis.

Output: neutron-gap-probes-round7.witness.json
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from q_parameter import Q as Q0_FLOAT  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_DPS = 50

# AME 2020 binding energies (MeV)
B_AME_MEV = {
    "deuteron":   2.22456612,    # ²H
    "tritium":    8.4817984,     # ³H
    "helium-3":   7.7180375,     # ³He
    "helium-4":  28.295673,      # ⁴He (α)
    "lithium-6": 31.99405,       # ⁶Li
    "lithium-7": 39.244626,      # ⁷Li
    "beryllium-9": 58.16498,     # ⁹Be
    "carbon-12": 92.16175,       # ¹²C
    "oxygen-16":127.61932,       # ¹⁶O
}

# (Z, N) lookup
Z_N = {
    "deuteron":   (1, 1), "tritium":  (1, 2), "helium-3": (2, 1),
    "helium-4":   (2, 2), "lithium-6":(3, 3), "lithium-7":(3, 4),
    "beryllium-9":(4, 5), "carbon-12":(6, 6), "oxygen-16":(8, 8),
}


def bond_counts_K_complete(Z: int, N: int) -> tuple[int, int, int]:
    """K_A complete graph: every pair of nucleons forms a bond.
    Returns (n_pp, n_pn, n_nn)."""
    n_pp = Z * (Z - 1) // 2
    n_pn = Z * N
    n_nn = N * (N - 1) // 2
    return n_pp, n_pn, n_nn


def main() -> int:
    print("=" * 100)
    print("NEUTRON-GAP PROBES — ROUND 7 (per-bond Skein-pair binding)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  Hypothesis: B = z_inv · (n_pp μ_pp + n_pn μ_pn + n_nn μ_nn)")
    print(f"  Bond model: K_A complete graph (every nucleon pair = 1 bond)")
    print()

    with mp.workdps(_DPS):
        q = mp.mpf(str(Q0_FLOAT))
        z_inv = (q + 1/q) / (mp.sqrt(q) + 1/mp.sqrt(q))
        print(f"  z_inv = (q+q⁻¹) / (q^½+q^-½) = {mp.nstr(z_inv, 12)}")
        print()

        # Calibration: solve μ_pp, μ_pn, μ_nn from D, T, ³He.
        # D (Z=1,N=1):    n_pn=1                  → B(D)/z_inv = μ_pn
        # T (Z=1,N=2):    n_pn=2, n_nn=1          → B(T)/z_inv = 2μ_pn + μ_nn
        # ³He (Z=2,N=1):  n_pp=1, n_pn=2          → B(³He)/z_inv = μ_pp + 2μ_pn
        b_d  = mp.mpf(str(B_AME_MEV["deuteron"]))
        b_t  = mp.mpf(str(B_AME_MEV["tritium"]))
        b_h3 = mp.mpf(str(B_AME_MEV["helium-3"]))
        mu_pn = b_d / z_inv
        mu_nn = b_t / z_inv - 2 * mu_pn
        mu_pp = b_h3 / z_inv - 2 * mu_pn

        print(f"  Calibrated structural inputs:")
        print(f"    μ_pn = {mp.nstr(mu_pn, 12)}  (from D)")
        print(f"    μ_nn = {mp.nstr(mu_nn, 12)}  (from T)")
        print(f"    μ_pp = {mp.nstr(mu_pp, 12)}  (from ³He)")
        print()

        # Predictions on every atom in the AME table
        print(f"  {'atom':<13} {'Z':>2} {'N':>2} "
              f"{'n_pp':>4} {'n_pn':>4} {'n_nn':>4} "
              f"{'B_AME':>9} {'B_pred':>9} {'err [%]':>8} {'err [ppb]':>14}")
        print(f"  {'-'*13} {'-'*2} {'-'*2} {'-'*4} {'-'*4} {'-'*4} "
              f"{'-'*9} {'-'*9} {'-'*8} {'-'*14}")

        results = []
        for atom, b_ame_val in B_AME_MEV.items():
            Z, N = Z_N[atom]
            n_pp, n_pn, n_nn = bond_counts_K_complete(Z, N)
            B_pred = z_inv * (n_pp * mu_pp + n_pn * mu_pn + n_nn * mu_nn)
            B_AME_mp = mp.mpf(str(b_ame_val))
            err_pct = (B_pred - B_AME_mp) / B_AME_mp * 100
            err_ppb = err_pct * mp.mpf(10**7)
            calibration = atom in {"deuteron", "tritium", "helium-3"}
            tag = " [calib]" if calibration else ""
            print(f"  {atom:<13} {Z:>2} {N:>2} "
                  f"{n_pp:>4} {n_pn:>4} {n_nn:>4} "
                  f"{b_ame_val:>9.4f} {float(B_pred):>9.4f} "
                  f"{float(err_pct):>+8.3f} {float(err_ppb):>+14.4e}{tag}")
            results.append({
                "atom": atom,
                "Z": Z, "N": N, "A": Z + N,
                "bonds": {"pp": n_pp, "pn": n_pn, "nn": n_nn},
                "B_AME_MeV": b_ame_val,
                "B_pred_MeV": mp.nstr(B_pred, 20),
                "err_pct": float(err_pct),
                "err_ppb": float(err_ppb),
                "is_calibration": calibration,
            })
        print()

        # Verdict
        non_calib = [r for r in results if not r["is_calibration"]]
        worst = max(non_calib, key=lambda r: abs(r["err_ppb"]))
        worst_pct = max(non_calib, key=lambda r: abs(r["err_pct"]))
        if abs(worst["err_ppb"]) < 1e3:
            verdict = (f"K_A bond model closes to <ppm precision on prediction set — "
                       f"worst {worst['atom']}: {worst['err_ppb']:+.2e} ppb")
        elif abs(worst_pct["err_pct"]) < 5:
            verdict = (f"K_A bond model gives <5% accuracy on prediction set — "
                       f"worst {worst_pct['atom']}: {worst_pct['err_pct']:+.2f}%. "
                       f"Indicates bond-graph topology is close but needs refinement.")
        else:
            verdict = (f"K_A complete-graph hypothesis FALSIFIED — "
                       f"worst {worst_pct['atom']}: {worst_pct['err_pct']:+.2f}% ({worst_pct['err_ppb']:+.2e} ppb). "
                       f"The right bond topology is not fully-connected.")
        print(f"  VERDICT: {verdict}")

    w = (
        WitnessBuilder("neutron-gap-probes-round7", engine="mpmath")
        .set_description(
            "Round-7 probe: per-bond Skein-pair binding "
            "B = z_inv · (n_pp μ_pp + n_pn μ_pn + n_nn μ_nn) under "
            "K_A complete-graph bond counting. Three structural inputs "
            "(μ_pp, μ_pn, μ_nn) calibrated from D/T/³He. Tests on "
            "⁴He, ⁶Li, ⁷Li, ⁹Be, ¹²C, ¹⁶O. Generalizes round-3's "
            "nucleon n/p Skein-pair scheme to the atomic level."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q0_FLOAT)
        .add_parameter("precision_dps", _DPS)
        .add_parameter("z_inv", mp.nstr(z_inv, 30))
        .add_parameter("mu_pn_MeV", mp.nstr(mu_pn, 20))
        .add_parameter("mu_nn_MeV", mp.nstr(mu_nn, 20))
        .add_parameter("mu_pp_MeV", mp.nstr(mu_pp, 20))
        .add_parameter("bond_model", "K_A complete graph")
        .add_parameter("hypothesis", "B = z_inv · Σ_t n_t μ_t for t ∈ {pp, pn, nn}")
        .add_data("results", results)
        .add_data("verdict", verdict)
        .add_data("attestation", {
            "used_fitting": False,
            "used_root_find": False,
            "uses_codata_inputs": False,
            "calibration_atoms": ["deuteron", "tritium", "helium-3"],
            "calibration_count": 3,
            "structural_inputs": 3,
        })
    )
    out_path = w.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
