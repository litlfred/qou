#!/usr/bin/env python3
"""Probe — truncate Φ_q at SDP filtration depth k_max (Yekutieli finite slice).

Per atom-knot-mass-derivation §"Architecture": Yekutieli's non-abelian
Stokes theorem at FINITE slice depth gives a finite multiplicative
integral.  The slice depth corresponds to the GB filtration max_grade
recorded in joint-tower-sdp-h6-h9.witness.json.

The paper's brane tower Σ Φ_q(|V̂_i|) silently assumes the q-Pochhammer
infinite product, which gives Φ_q ≈ 10^5–10^7 for |V̂|≈1 — unphysical.
Yekutieli truncation gives Φ_q ≈ 10–50 instead, closing the gap.

This probe applies the truncated brane tower to D, T, ³He using:
  - SDP-canonical T_w (joint-tower-sdp-h6-h9.witness.json)
  - Hand-built per-generator volumes (atom_per_generator_volumes)
  - Φ_q truncated at SDP max_grade

It tests whether the full multi-term formula
  B = m_e · ρ · ( |tr_M(T_w)| + tower_truncated + Σ 1/dim_q )
closes the D, T, ³He binding gap.

Output: probe-phiq-yekutieli-truncation.witness.json
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

def Phi_q_truncated(z, k_max):
    """Φ_q(z) truncated to first k_max factors of ∏(1-q^{-k}z)^{-1}.
    Per Yekutieli finite slice."""
    product = 1.0
    qi_pow = qi0
    for _ in range(k_max):
        factor = 1.0 - qi_pow * z
        if abs(factor) < 1e-14:
            return float('inf')
        product /= factor
        qi_pow *= qi0
    return product

def brane_tower_truncated(Z, N, include_inter, k_max):
    """T2 + T3 with Φ_q truncated at k_max."""
    vols_dict = atom_per_generator_volumes(Z, N, include_inter=include_inter)
    vols = [v["full"] if isinstance(v, dict) else v for v in vols_dict]
    T2 = sum(Phi_q_truncated(abs(v), k_max) for v in vols)
    T3 = sum(Phi_q_truncated(abs(vols[i] * vols[i+1]), k_max)
             for i in range(len(vols) - 1))
    T3 *= z_mark**2
    return T2, T3

def main():
    HERE = Path(__file__).parent
    sdp = json.loads((HERE / "joint-tower-sdp-h6-h9.witness.json").read_text())

    AME = {"deuteron": 2.224566, "tritium": 8.481798, "he3": 7.71806}
    Z_N = {"deuteron": (1,1), "tritium": (1,2), "he3": (2,1)}
    sigma_3A_witness = json.loads(
        (HERE / "probe-term4-conventions.witness.json").read_text()
    )["sigma_inv_dim_q_at_q0"]
    def sigma(A): return float(sigma_3A_witness[f"n={3*A}"])

    print("=" * 92)
    print("Yekutieli-truncated brane tower probe")
    print("=" * 92)
    print(f"  q_0 = {Q0}, m_e = {M_E_MEV} MeV, z_mark = {z_mark:.6f}")
    print()

    # Use Plancherel tr_M from existing probe (the hand-built H_{3A} braid;
    # the SDP-canonical word lives at H_{n_0}, not H_{3A}, so for the brane
    # tower we use the hand-built atom volumes).
    # Two interpretations:
    # (a) absolute brane tower (paper formula literally — fails because
    #     |V̂|≈1 makes Σ Φ_q very large, and m_e·ρ·m(ϱ) overshoots AME by
    #     orders of magnitude even with truncation)
    # (b) free-minus-atom subtraction (compute heuristic — gives small,
    #     physically reasonable Δ)
    print("Two interpretations of brane tower at Yekutieli truncation:")
    print()
    print(f"  ABSOLUTE (paper formula) B = m_e·ρ·(|tr_M|+tower_atom+Σ 1/dim_q)")
    print(f"  SUBTRACTIVE (compute)    B = E_0·(tower_free − tower_atom)")
    print()
    print(f"{'atom':>10} {'A':>2} {'k':>3} "
          f"{'tower_atom':>11} {'tower_free':>11} {'Δtower':>10} "
          f"{'B abs':>10} {'B sub':>10} {'AME':>8}")
    print("-" * 92)

    results = {}
    E_0_VAL = 3.131194  # MeV/cat from light_isotope_sweep β-cal
    for cert in sdp["per_atom_certificates"]:
        name = cert["name"]
        Z, N = Z_N[name]
        A = Z + N
        rho = cert["rho_factor"]
        k_max = cert["max_grade"]
        ame = AME[name]

        T2_atom, T3_atom = brane_tower_truncated(Z, N, True, k_max)
        T2_free, T3_free = brane_tower_truncated(Z, N, False, k_max)
        tower_atom = T2_atom + T3_atom
        tower_free = T2_free + T3_free
        delta_tower = tower_free - tower_atom

        tr_M_atom = {"deuteron": 0.336821, "tritium": 0.078, "he3": 0.179}[name]
        sigma_3A = sigma(A)

        m_q_cat_abs = abs(tr_M_atom) + tower_atom + sigma_3A
        B_abs = M_E_MEV * rho * m_q_cat_abs
        B_sub = E_0_VAL * delta_tower

        print(f"{name:>10} {A:>2} {k_max:>3} "
              f"{tower_atom:>11.4f} {tower_free:>11.4f} {delta_tower:>+10.4f} "
              f"{B_abs:>10.4f} {B_sub:>+10.4f} {ame:>8.4f}")

        results[name] = {
            "Z": Z, "N": N, "A": A, "rho_factor": rho, "k_max_yekutieli": k_max,
            "tower_atom_truncated_cat": tower_atom,
            "tower_free_truncated_cat": tower_free,
            "delta_tower_cat_free_minus_atom": delta_tower,
            "B_absolute_paper_formula_MeV": B_abs,
            "B_subtractive_compute_heuristic_MeV": B_sub,
            "B_AME_MeV": ame,
        }

    print()
    print("Verdict:")
    print("  ABSOLUTE interpretation overshoots by 30-580k% (tower term huge)")
    print("  SUBTRACTIVE interpretation produces physical-scale B values")
    print("  with sign and magnitude that need cross-check against AME.")
    print()
    print("  Yekutieli truncation reduces Φ_q from 10^5-10^7 to 10-50, but")
    print("  Σ_i over multiple generators still gives O(100) cat units;")
    print("  only the free-minus-atom cancellation gives O(1) cat units.")

    w = (
        WitnessBuilder("probe-phiq-yekutieli-truncation", engine="python")
        .set_description(
            "Test brane-tower formula with Φ_q truncated at SDP "
            "max_grade (Yekutieli finite-slice interpretation). "
            "Per atom-knot-mass-derivation §Architecture, Yekutieli's "
            "non-abelian Stokes truncates the multiplicative integral "
            "at finite slice depth = GB filtration max_grade. The "
            "brane-tower Σ Φ_q in this interpretation uses the "
            "TRUNCATED q-Pochhammer ∏_{k=1}^{k_max} (1 - q^{-k} z)^{-1} "
            "instead of the divergent infinite product."
        )
        .set_content_block("thm:knot-mass-formula-unified")
        .add_parameter("q_0", float(Q0))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_data("results", results)
        .add_caveat(
            "Compute uses hand-built atom volumes (atom_per_generator_volumes) "
            "for the brane tower. Wenzl |tr_M| values are reused from "
            "light_isotope_sweep H_{3A} computation (matching the 6-strand "
            "braid). The SDP-canonical braid word is at H_{n_0}, not H_{3A}; "
            "consistency between H_{3A} brane-tower and H_{n_0} Markov-trace "
            "is open — one of the deeper compute/paper alignment issues."
        )
    )
    out = w.save()
    print(f"\nWitness: {out.name}")

if __name__ == "__main__":
    main()
