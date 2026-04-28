#!/usr/bin/env python3
"""C9 — Energy comparison: linear C6 chain vs. benzene ring.

Backs `lem:c6-energy-comparison` in the Organic Chemistry chapter.

Statement
---------
For N = 6, the topological energy difference between the linear-chain
configuration and the closed benzene ring is

    ΔE_{chain→ring}(6)  =  [Δ_{T(2,6)}(q₀) − (N − 1)] · |q + q⁻¹|_mol
                        =  [Δ_{T(2,6)}(q₀) − 5] · |q + q⁻¹|_mol.

In the limit q → 1 this is exactly −2·|q+q⁻¹|_mol, i.e. the ring
is favoured by two crossing-energy units (the half-weight saving on
three of the six pairwise links).

This is the **smoking-gun** prediction for benzene's ring closure
favourability and is the corollary of `prop:threading-half-weight`
applied at $N = 6$.

Usage
-----
    python3 chain_vs_ring_energy_N6.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp

from lib.alexander import alexander_T2N_closed, q
from lib.units import ev_to_kj_per_mol, ev_to_kcal_per_mol
from witness_base import WitnessBuilder
from q_parameter import Q


DATA_PATH = Path(__file__).parent / "data" / "experimental-organic.json"


def main() -> int:
    data = json.loads(DATA_PATH.read_text())
    alpha = data["fundamental_constants"]["alpha"]["value"]
    m_ratio = data["fundamental_constants"]["m_e_over_m_p"]["value"]
    e_nuc_MeV = 8.0
    e_mol_eV = alpha**2 * m_ratio * e_nuc_MeV * 1e6
    e_mol_kJpermol = ev_to_kj_per_mol(e_mol_eV)
    e_mol_kcalpermol = ev_to_kcal_per_mol(e_mol_eV)

    N = 6
    delta_sym = alexander_T2N_closed(N)
    delta_q0 = float(sp.N(delta_sym.subs(q, Q)))
    delta_one = float(sp.limit(delta_sym, q, 1))   # = 3
    chain_weight = N - 1                            # = 5
    weight_diff_q0 = delta_q0 - chain_weight
    weight_diff_one = delta_one - chain_weight      # = -2

    # Energetic comparison.
    delta_E_q0_eV = weight_diff_q0 * e_mol_eV
    delta_E_q0_kJpermol = weight_diff_q0 * e_mol_kJpermol
    delta_E_q0_kcalpermol = weight_diff_q0 * e_mol_kcalpermol

    delta_E_classical_eV = weight_diff_one * e_mol_eV
    delta_E_classical_kJpermol = weight_diff_one * e_mol_kJpermol

    w = WitnessBuilder("chain-vs-ring-energy-N6", engine="sympy")
    w.set_description(
        "Linear C6 chain vs. benzene ring topological energy "
        "difference: ΔE = (Δ_{T(2,6)} − 5) · |q+q⁻¹|_mol.  In the "
        "classical limit q→1, ΔE = −2·|q+q⁻¹|_mol, i.e. the ring is "
        "energetically favoured."
    )
    w.set_content_block("lem:c6-energy-comparison")
    w.add_parameter("N", N)
    w.add_parameter("q_substrate", float(Q))
    w.add_parameter("e_cross_mol_eV", e_mol_eV)
    w.add_data("table", {
        "alexander_at_q0": delta_q0,
        "alexander_at_q_eq_1": delta_one,
        "chain_weight": chain_weight,
        "weight_difference_at_q0": weight_diff_q0,
        "weight_difference_at_q_eq_1": weight_diff_one,
        "delta_E_at_q0_eV": delta_E_q0_eV,
        "delta_E_at_q0_kJ_per_mol": delta_E_q0_kJpermol,
        "delta_E_at_q0_kcal_per_mol": delta_E_q0_kcalpermol,
        "delta_E_classical_eV": delta_E_classical_eV,
        "delta_E_classical_kJ_per_mol": delta_E_classical_kJpermol,
        "ring_favoured_at_q0": weight_diff_q0 < 0,
        "ring_favoured_at_q_eq_1": weight_diff_one < 0,
    })

    w.add_assertion(
        "ΔE in classical limit q→1 equals −2·|q+q⁻¹|_mol",
        computed=round(delta_E_classical_eV, 6),
        expected=round(-2.0 * e_mol_eV, 6),
        tolerance=1e-6,
        unit="eV",
    )
    w.add_assertion(
        "Δ_{T(2,6)}(q=1) = 3",
        computed=int(delta_one),
        expected=3,
    )
    w.add_assertion(
        "ring is energetically favoured (ΔE < 0) in classical limit",
        computed=str(weight_diff_one < 0),
        expected="True",
    )

    w.add_caveat(
        "At q₀ ≈ 1.11, Δ_{T(2,6)}(q₀) ≈ 3.04 > 3, which leaves the "
        "ring still favoured (ΔE ≈ -1.96·|q+q⁻¹|_mol) but with a "
        "small positive correction reflecting the finite-q deviation "
        "from the classical half-weight."
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
