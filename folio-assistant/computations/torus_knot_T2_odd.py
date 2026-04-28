#!/usr/bin/env python3
"""C10 — Odd-N ring closure barrier from T(2, N) torus knots.

Backs `prop:odd-N-ring-barrier` and the supporting definition
`def:torus-knot-T2-odd-alexander` in the Organic Chemistry chapter.

Statement
---------
For odd $N = 2m + 1 \\ge 3$, the closed ring is a torus knot
$T(2, N)$ (a single component, as opposed to the 2-component link
of even $N$).  The closure barrier follows the same Alexander-weight
formula

    ΔE_{closure}(N)  =  [(N - 1) - Δ_{T(2,N)}(q₀)] · |q + q⁻¹|_mol,

where Δ_{T(2,N)}(q) for odd N has the symmetric closed form

    Δ_{T(2, 2m+1)}(q)  =  (q^{2m+1} + q^{-(2m+1)}) / (q + q^{-1}).

In particular, Δ_{T(2,3)}(1) = 1 (trefoil), Δ_{T(2,5)}(1) = 1
(cinquefoil), and in general Δ_{T(2, 2m+1)}(1) = 1 for all m.

Usage
-----
    python3 torus_knot_T2_odd.py
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
    e_mol_eV = alpha**2 * m_ratio * e_nuc_MeV * 1e6
    e_mol_kJpermol = ev_to_kj_per_mol(e_mol_eV)

    rows = []
    for N in [3, 5, 7, 9, 11, 13]:
        delta_sym = alexander_T2N_closed(N)
        delta_q0 = float(sp.N(delta_sym.subs(q, Q)))
        delta_one = float(sp.limit(delta_sym, q, 1))
        chain_weight = N - 1
        weight_diff = chain_weight - delta_q0
        barrier_kJpermol = weight_diff * e_mol_kJpermol
        rows.append({
            "N": N,
            "torus_knot": f"T(2,{N})",
            "alexander_symbolic": str(sp.simplify(delta_sym)),
            "alexander_at_q_eq_1": delta_one,
            "alexander_at_q0": delta_q0,
            "chain_weight": chain_weight,
            "weight_difference": weight_diff,
            "barrier_predicted_kJ_per_mol": barrier_kJpermol,
        })

    w = WitnessBuilder("torus-knot-T2-odd", engine="sympy")
    w.set_description(
        "Odd-N ring closure barrier from torus-knot T(2, N) Alexander "
        "polynomials, N = 3, 5, 7, 9, 11, 13.  Closed-form Δ_{T(2, 2m+1)} "
        "evaluated at q₀; Δ(1) = 1 verified for all odd N."
    )
    w.set_content_block("prop:odd-N-ring-barrier")
    w.add_parameter("q_substrate", float(Q))
    w.add_data("table", rows)

    w.add_assertion(
        "Δ_{T(2,N)}(q=1) == 1 for all odd N in {3,5,7,9,11,13}",
        computed=str(all(int(r["alexander_at_q_eq_1"]) == 1 for r in rows)),
        expected="True",
    )
    w.add_assertion(
        "all odd-N predicted barriers strictly positive",
        computed=str(all(r["barrier_predicted_kJ_per_mol"] > 0 for r in rows)),
        expected="True",
    )
    w.add_assertion(
        "trefoil T(2,3) Alexander symbolic form q² − 1 + q⁻²",
        computed=str(
            sp.expand(alexander_T2N_closed(3) - (q**2 - 1 + q**(-2))) == 0
        ),
        expected="True",
    )

    w.add_caveat(
        "Odd-N ring systems (cyclopropene, cyclopentadienyl, "
        "cycloheptatriene, …) are not equivalently 'aromatic' to "
        "even-N benzene-class systems; the topological prediction "
        "yields a single positive barrier, but Hückel's 4n+2 rule "
        "(implemented in C11) classifies aromaticity differently.  "
        "The witness records the topological barrier; aromatic "
        "stabilisation is left to C11."
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
