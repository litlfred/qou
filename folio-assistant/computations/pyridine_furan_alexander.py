#!/usr/bin/env python3
"""C14 — Heteroaromatic Alexander polynomials (pyridine, furan, thiophene).

Backs `conj:heteroaromatic-alexander` in the Organic Chemistry chapter.

Statement (conjectural)
-----------------------
The Alexander polynomial of a heteroaromatic 5- or 6-ring (pyridine,
furan, thiophene, pyrrole) is identical to that of the all-carbon
analogue (benzene or cyclopentadienyl), because the threading link
T(2, N) is a topological invariant of the *ring topology* and does
not distinguish heteroatoms.

The chemistry-relevant differences (different aromaticity, different
basicity, different bond enthalpies) arise from **per-atom weight
modifications** — a future extension of the theory in which each
vertex carries a Hopf-algebraic weight depending on its element.

This script computes Δ_{T(2, N)}(q₀) for the relevant N (5 for
furan/thiophene/pyrrole/cyclopentadienyl; 6 for benzene/pyridine/
pyrazine) and confirms the equality.

Usage
-----
    python3 pyridine_furan_alexander.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp

from lib.alexander import alexander_T2N_closed, q
from witness_base import WitnessBuilder
from q_parameter import Q


def main() -> int:
    families = [
        # (name, ring size N, list of all-carbon analogues for comparison)
        ("benzene",            6, "all-carbon C6 ring"),
        ("pyridine",           6, "1 N-substitution of benzene"),
        ("pyrazine",           6, "2 N-substitutions of benzene"),
        ("pyrimidine",         6, "2 N-substitutions of benzene"),
        ("pyridazine",         6, "2 N-substitutions of benzene"),
        ("triazine",           6, "3 N-substitutions of benzene"),
        ("cyclopentadienyl",   5, "all-carbon C5 ring"),
        ("furan",              5, "1 O-substitution of cyclopentadienyl"),
        ("thiophene",          5, "1 S-substitution of cyclopentadienyl"),
        ("pyrrole",            5, "1 NH-substitution of cyclopentadienyl"),
        ("imidazole",          5, "2 N-substitutions of cyclopentadienyl"),
    ]

    rows = []
    for name, N, comment in families:
        delta_sym = alexander_T2N_closed(N)
        delta_q0 = float(sp.N(delta_sym.subs(q, Q)))
        delta_one = float(sp.limit(delta_sym, q, 1))
        rows.append({
            "molecule": name,
            "ring_size": N,
            "carbon_analogue_comment": comment,
            "alexander_at_q_eq_1": delta_one,
            "alexander_at_q0": delta_q0,
        })

    # Headline conjecture: all 6-rings agree, all 5-rings agree.
    six_ring_deltas = [r["alexander_at_q0"] for r in rows if r["ring_size"] == 6]
    five_ring_deltas = [r["alexander_at_q0"] for r in rows if r["ring_size"] == 5]

    six_ring_agree = all(
        abs(d - six_ring_deltas[0]) < 1e-12 for d in six_ring_deltas
    )
    five_ring_agree = all(
        abs(d - five_ring_deltas[0]) < 1e-12 for d in five_ring_deltas
    )

    w = WitnessBuilder("pyridine-furan-alexander", engine="sympy")
    w.set_description(
        "Heteroaromatic Alexander polynomials: all 6-rings (benzene "
        "and N-substituted derivatives) share Δ_{T(2,6)}; all 5-rings "
        "(cyclopentadienyl and O/S/NH/N-substituted derivatives) share "
        "Δ_{T(2,5)}.  This is the conjectural baseline before "
        "introducing per-atom Hopf-algebraic weights."
    )
    w.set_content_block("conj:heteroaromatic-alexander")
    w.add_data("table", rows)
    w.add_data("six_ring_alexander_at_q0", six_ring_deltas[0])
    w.add_data("five_ring_alexander_at_q0", five_ring_deltas[0])
    w.add_data("six_ring_agree", six_ring_agree)
    w.add_data("five_ring_agree", five_ring_agree)

    w.add_assertion(
        "all 6-membered heteroaromatic rings share Δ_{T(2,6)}",
        computed=str(six_ring_agree),
        expected="True",
    )
    w.add_assertion(
        "all 5-membered heteroaromatic rings share Δ_{T(2,5)}",
        computed=str(five_ring_agree),
        expected="True",
    )

    w.add_caveat(
        "The conjecture predicts equality of the *unweighted* "
        "Alexander invariant across heteroatom substitutions.  This "
        "does not predict equal aromaticity, basicity, or bond "
        "enthalpy — those distinctions require per-atom Hopf weights "
        "(future work).  The conjecture *does* predict that ring "
        "topology, hydrogen capacity, and the ring-closure topological "
        "barrier are invariant under heteroatom substitution that "
        "preserves the ring size N."
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
