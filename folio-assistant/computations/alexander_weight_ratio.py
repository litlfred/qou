#!/usr/bin/env python3
"""C5 — Threading half-weight ratio  Δ_{T(2,2m)}(q)/N → ½  as |q| → 1.

Backs `prop:threading-half-weight` in the Organic Chemistry chapter.

The central topological claim of the chapter is that, for every even
N = 2m, the threading link's per-atom Alexander weight tends to ½ in
the classical limit::

        lim_{q → 1}  Δ_{T(2,2m)}(q) / N  =  1/2.

This script verifies the limit symbolically for N = 2, 4, …, 14, and
records the deviation at the substrate value q₀ for each N.

Algorithm
---------
1. Symbolic limit via :func:`lib.alexander.alexander_half_weight_ratio`.
2. Numerical evaluation at q = q₀ (substrate parameter) for the
   actual deviation that propagates into the molecular crossing
   energy.
3. Series expansion around q = 1 to leading order in (q − 1)² for
   each even N, exposing the curvature of the per-atom weight.

Usage
-----
    python3 alexander_weight_ratio.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp

from lib.alexander import (
    alexander_T2N_closed,
    alexander_half_weight_ratio,
    q,
)
from q_parameter import Q
from witness_base import WitnessBuilder


def main() -> int:
    w = WitnessBuilder("alexander-weight-ratio", engine="sympy")
    w.set_description(
        "Verifies Δ_{T(2,2m)}(q)/N → 1/2 as |q| → 1 for even N = 2,…,14, "
        "the central topological claim of the threading-link chapter."
    )
    w.set_content_block("prop:threading-half-weight")
    w.add_parameter("q_substrate", float(Q))

    rows = []
    for N in [2, 4, 6, 8, 10, 12, 14]:
        ratio_sym = alexander_half_weight_ratio(N)
        # Numerical ratio at q = q₀.
        ratio_q0 = float(sp.N(alexander_T2N_closed(N).subs(q, Q) / N))
        # Curvature (q-1)² coefficient.
        series = sp.series(alexander_T2N_closed(N) / N, q, 1, 4).removeO()
        rows.append({
            "N": N,
            "ratio_at_unit_symbolic": str(ratio_sym),
            "ratio_at_unit_numeric": float(ratio_sym),
            "ratio_at_q0": ratio_q0,
            "deviation_from_half_at_q0": ratio_q0 - 0.5,
            "series_about_q_eq_1": str(series),
        })
        w.add_assertion(
            f"limit Δ/N at q=1 for N={N} == 1/2",
            computed=str(ratio_sym),
            expected="1/2",
        )
    w.add_data("table", rows)

    # Headline assertion: chapter's defining claim.
    w.add_assertion(
        "all even N yield limit 1/2",
        computed=str(all(
            sp.simplify(alexander_half_weight_ratio(N) - sp.Rational(1, 2)) == 0
            for N in [2, 4, 6, 8, 10, 12, 14]
        )),
        expected="True",
    )

    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
