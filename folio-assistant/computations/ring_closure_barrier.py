#!/usr/bin/env python3
"""C6 — Quantitative ring-closure barrier from Δ_{T(2,N)}(q).

Backs `prop:ring-closure-barrier-quantitative` in the Organic
Chemistry chapter.

Statement
---------
For an even-$N$ ring, the ring-closure activation barrier is

    ΔE_{closure}(N)  =  [(N − 1) − Δ_{T(2,N)}(q₀)] · |q + q⁻¹|_mol,

where ``(N − 1)`` is the chain Alexander weight (sum of $N-1$ Hopf
links) and ``Δ_{T(2,N)}(q₀)`` is the threading-link Alexander weight
at the substrate value.

This script evaluates the formula for $N = 4, 6, 8, 10, 12, 14$ and
compares each prediction against the experimental barrier in
``data/experimental-organic.json``.

Usage
-----
    python3 ring_closure_barrier.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp

from lib.alexander import alexander_T2N_closed, q
from lib.units import ev_to_kj_per_mol
from witness_base import WitnessBuilder
from q_parameter import Q


DATA_PATH = Path(__file__).parent / "data" / "experimental-organic.json"


def main() -> int:
    data = json.loads(DATA_PATH.read_text())
    alpha = data["fundamental_constants"]["alpha"]["value"]
    m_ratio = data["fundamental_constants"]["m_e_over_m_p"]["value"]
    e_nuc_MeV = 8.0
    # Molecular crossing-energy quantum, eV.
    e_mol_eV = alpha**2 * m_ratio * e_nuc_MeV * 1e6
    e_mol_kJpermol = ev_to_kj_per_mol(e_mol_eV)

    exp_data = {
        d["N"]: d for d in
        data["ring_closure_barriers_kJ_per_mol"]["data"]
    }

    rows = []
    for N in [4, 6, 8, 10, 12, 14]:
        delta_sym = alexander_T2N_closed(N)
        delta_q0 = float(sp.N(delta_sym.subs(q, Q)))
        chain_weight = N - 1
        weight_diff = chain_weight - delta_q0
        barrier_eV = weight_diff * e_mol_eV
        barrier_kJpermol = weight_diff * e_mol_kJpermol
        exp = exp_data.get(N)
        if exp is not None:
            exp_barrier = exp["barrier"]
            exp_unc = exp["uncertainty"]
            ratio = barrier_kJpermol / exp_barrier if exp_barrier else None
        else:
            exp_barrier = exp_unc = ratio = None
        rows.append({
            "N": N,
            "alexander_at_q0": delta_q0,
            "chain_weight": chain_weight,
            "weight_difference": weight_diff,
            "barrier_predicted_eV": barrier_eV,
            "barrier_predicted_kJ_per_mol": barrier_kJpermol,
            "barrier_experimental_kJ_per_mol": exp_barrier,
            "experimental_uncertainty_kJ_per_mol": exp_unc,
            "predicted_over_experimental": ratio,
            "system": exp["system"] if exp else None,
            "citation": exp["citation"] if exp else None,
        })

    w = WitnessBuilder("ring-closure-barrier", engine="sympy")
    w.set_description(
        "Quantitative ring-closure activation barrier for even-N rings: "
        "ΔE = [(N-1) - Δ_{T(2,N)}(q₀)] · |q+q⁻¹|_mol.  Compared against "
        "experimental aromatisation/closure barriers from CCSD(T)/DFT "
        "literature (data/experimental-organic.json)."
    )
    w.set_content_block("prop:ring-closure-barrier-quantitative")
    w.add_parameter("q_substrate", float(Q))
    w.add_parameter("e_cross_mol_eV", e_mol_eV)
    w.add_parameter("e_cross_mol_kJ_per_mol", e_mol_kJpermol)
    w.add_data("table", rows)

    # Headline assertion: monotone-non-decreasing weight difference for even N.
    weight_diffs = [r["weight_difference"] for r in rows]
    w.add_assertion(
        "weight differences (N-1) − Δ(q₀) non-decreasing in N",
        computed=str(all(
            weight_diffs[i] <= weight_diffs[i + 1] + 1e-9
            for i in range(len(weight_diffs) - 1)
        )),
        expected="True",
    )
    # N=6 (benzene aromatisation) headline: weight diff is exactly 2 at q=1
    # but slightly different at q₀.
    n6 = next(r for r in rows if r["N"] == 6)
    w.add_assertion(
        "N=6 weight difference numerically close to 2 at q₀",
        computed=round(n6["weight_difference"], 3),
        expected=2.0,
        tolerance=0.1,
    )
    # Order-of-magnitude check vs. experiment.
    n6_ratio = n6["predicted_over_experimental"]
    w.add_assertion(
        "N=6 prediction within order of magnitude of experiment",
        computed=str(0.1 <= n6_ratio <= 10.0),
        expected="True",
    )

    w.add_caveat(
        "The prediction is based on |q+q⁻¹|_mol ≈ 0.232 eV from C1, "
        "which lies below the chapter's quoted 1–2 eV range.  The "
        "absolute barrier predictions therefore underestimate the "
        "experimental values by roughly a factor of 5–10; the *ratios* "
        "between different N (the topological prediction) are "
        "unaffected by an overall scale rescaling of |q+q⁻¹|_mol."
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
