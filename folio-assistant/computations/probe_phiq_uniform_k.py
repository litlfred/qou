#!/usr/bin/env python3
"""Probe — Yekutieli truncation at UNIFORM depth k across atoms.

Question (from user): the existing probe uses per-atom k_max from
joint-tower-sdp-h6-h9.witness.json (D=2, T=9, He3=2). T fails because
its k_max=9 is much deeper. But what if the structural truncation depth
is uniform across atoms — say k=2 for all — and the "GB max_grade"
identification was wrong?

This probe sweeps k ∈ {1, 2, 3, 4, 5, 6, 8, 10} uniformly across
{D, T, He3} and checks whether any single uniform k closes all three
to AME within 10%.

Output: probe-phiq-uniform-k.witness.json
"""
import sys, json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from hecke_core import atom_per_generator_volumes
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder

H_VAL = float(Q0 - 1.0/Q0)
qi0 = 1.0 / Q0
z_mark = 1.0 / (Q0**0.5 + (1.0/Q0)**0.5)

class PhiQPoleHit(Exception):
    """Raised when a Φ_q truncation factor (1 - q^{-k}z) is within
    numerical zero. Subtracting two `inf`s downstream produces NaN and
    silently corrupts witness data, so we surface the pole instead.
    Callers may catch and decide how to handle (skip the atom, fall
    back to a different k, etc.)."""
    def __init__(self, k, qi_pow, z):
        super().__init__(
            f"Φ_q pole encountered at k={k}: |1 - q^(-k)·z| < 1e-14 "
            f"(q^(-k)={qi_pow:.6g}, z={z:.6g})"
        )
        self.k = k
        self.qi_pow = qi_pow
        self.z = z

def Phi_q_truncated(z, k_max):
    """Truncated Φ_q^[≤k_max](z) = ∏_{k=1}^{k_max} (1 - q^{-k}z)^{-1}.
    Raises PhiQPoleHit if a factor is within numerical zero — the
    caller can then skip the atom rather than letting `inf - inf`
    propagate to NaN downstream."""
    product = 1.0
    qi_pow = qi0
    for k in range(1, k_max + 1):
        factor = 1.0 - qi_pow * z
        if abs(factor) < 1e-14:
            raise PhiQPoleHit(k, qi_pow, z)
        product /= factor
        qi_pow *= qi0
    return product

def brane_tower_truncated(Z, N, include_inter, k_max):
    """Returns (T2, T3, magnitudes). May raise PhiQPoleHit, which the
    caller is expected to surface (do not let it become inf-inf=NaN
    downstream)."""
    vols_dict = atom_per_generator_volumes(Z, N, include_inter=include_inter)
    vols = [v["full"] if isinstance(v, dict) else v for v in vols_dict]
    T2 = sum(Phi_q_truncated(abs(v), k_max) for v in vols)
    T3 = sum(Phi_q_truncated(abs(vols[i] * vols[i+1]), k_max)
             for i in range(len(vols) - 1))
    T3 *= z_mark**2
    return T2, T3, [abs(v) for v in vols]

def main():
    HERE = Path(__file__).parent
    AME = {"deuteron": 2.224566, "tritium": 8.481798, "he3": 7.71806}
    Z_N = {"deuteron": (1,1), "tritium": (1,2), "he3": (2,1)}
    rho_map = {"deuteron": 1, "tritium": 2, "he3": 2}
    sigma_3A_witness = json.loads(
        (HERE / "probe-term4-conventions.witness.json").read_text()
    )["sigma_inv_dim_q_at_q0"]
    def sigma(A): return float(sigma_3A_witness[f"n={3*A}"])
    tr_M = {"deuteron": 0.336821, "tritium": 0.078, "he3": 0.179}

    print("=" * 102)
    print("Uniform-k Yekutieli truncation probe")
    print("=" * 102)
    print(f"  q_0 = {Q0}, m_e = {M_E_MEV} MeV, z_mark = {z_mark:.6f}")
    print()

    sweep_k = [1, 2, 3, 4, 5, 6, 8, 10]
    E_0_VAL = 3.131194
    print(f"  Per-atom |V̂_i| ranges:")
    for name, (Z, N) in Z_N.items():
        _, _, mags = brane_tower_truncated(Z, N, True, 1)
        print(f"    {name:>10}: {[f'{v:.4f}' for v in mags]}")
    print()
    print("ABSOLUTE: B = m_e·ρ·(|tr_M|+tower_atom+σ)")
    print("SUBTRACTIVE: B = E_0·(tower_free − tower_atom)")
    print()
    print(f"{'k':>3} {'atom':>10} {'tow_atom':>9} {'tow_free':>9} {'Δtow':>8} "
          f"{'B_abs':>9} {'B_sub':>9} {'AME':>7} {'abs_err%':>8} {'sub_err%':>8}")
    print("-" * 102)

    results = {}
    for k in sweep_k:
        results[k] = {}
        for name, (Z, N) in Z_N.items():
            A = Z + N
            rho = rho_map[name]
            try:
                T2a, T3a, _ = brane_tower_truncated(Z, N, True, k)
                T2f, T3f, _ = brane_tower_truncated(Z, N, False, k)
            except PhiQPoleHit as e:
                # A pole was hit at this (atom, k); skip rather than let
                # inf − inf propagate to NaN in the witness.
                print(f"{k:>3} {name:>10} -- pole hit at k={e.k} (q^-k·z="
                      f"{e.qi_pow * e.z:.6g}), skipping")
                results[k][name] = {"pole_hit": True, "k_at_pole": e.k}
                continue
            tower_a = T2a + T3a
            tower_f = T2f + T3f
            dtow = tower_f - tower_a
            sigma_3A = sigma(A)
            B_abs = M_E_MEV * rho * (abs(tr_M[name]) + tower_a + sigma_3A)
            B_sub = E_0_VAL * dtow
            err_abs = 100.0 * (B_abs - AME[name]) / AME[name]
            err_sub = 100.0 * (B_sub - AME[name]) / AME[name]
            print(f"{k:>3} {name:>10} {tower_a:>9.3f} {tower_f:>9.3f} {dtow:>+8.3f} "
                  f"{B_abs:>9.3f} {B_sub:>+9.3f} {AME[name]:>7.3f} "
                  f"{err_abs:>+8.1f} {err_sub:>+8.1f}")
            results[k][name] = {
                "tower_atom": tower_a, "tower_free": tower_f,
                "delta_tower": dtow,
                "B_abs_MeV": B_abs, "B_sub_MeV": B_sub,
                "AME_MeV": AME[name],
                "err_abs_pct": err_abs, "err_sub_pct": err_sub,
            }
        print()

    print("Verdict (does any uniform k close all three within 10%?):")
    for k in sweep_k:
        max_abs = max(abs(results[k][n]["err_abs_pct"]) for n in AME)
        max_sub = max(abs(results[k][n]["err_sub_pct"]) for n in AME)
        v_a = "YES" if max_abs < 10 else f"NO ({max_abs:.0f}%)"
        v_s = "YES" if max_sub < 10 else f"NO ({max_sub:.0f}%)"
        print(f"  k={k}: ABS={v_a:>12}   SUB={v_s:>12}")

    w = (
        WitnessBuilder("probe-phiq-uniform-k", engine="python")
        .set_description(
            "Test brane-tower formula with Φ_q truncated at UNIFORM depth k "
            "across {D, T, He3}. Tests whether atom-dependent k_max from "
            "GB filtration was misidentified — perhaps a single uniform "
            "structural depth applies."
        )
        .set_content_block("conj:brane-tower-z-habiro")
        .add_parameter("q_0", float(Q0))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("k_sweep", sweep_k)
        .add_data("results", results)
        .add_caveat(
            "Uses absolute paper formula B = m_e·ρ·(|tr_M|+tower+σ); "
            "compares against AME light-isotope binding."
        )
    )
    out = w.save()
    print(f"\nWitness: {out.name}")

if __name__ == "__main__":
    main()
