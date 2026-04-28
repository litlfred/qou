#!/usr/bin/env python3
"""C3 — Alexander polynomials Δ_{T(2,N)}(q) for N = 2, …, 12.

Backs `lem:alexander-T2N-closed-form` in the Organic Chemistry chapter.

Algorithm
---------
For each N in the requested range:

1. Compute the closed-form symmetric Alexander polynomial via
   :func:`lib.alexander.alexander_T2N_closed`.
2. Verify the defining identity
       Δ · (q − q⁻¹) == q^m − q^{-m}    (even N = 2m)
   or
       Δ · (q + q⁻¹) == q^N + q^{-N}    (odd N).
3. Cross-check special values: Δ(1) and Δ(q₀) (numerically, with q₀
   from the substrate parameter ``Q``).

The witness records, for each N, the symbolic expression and the
numerical evaluation at the substrate value, plus a global pass/fail
on the algebraic identity check.

Usage
-----
    python3 alexander_T2N.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp

from lib.alexander import (
    alexander_T2N_closed,
    alexander_weight_at_unit,
    alexander_half_weight_ratio,
    closed_form_consistency,
    q,
)
from q_parameter import Q
from witness_base import WitnessBuilder


def main() -> int:
    w = WitnessBuilder("alexander-T2N", engine="sympy")
    w.set_description(
        "Closed-form Alexander polynomials Δ_{T(2,N)}(q) for N = 2,…,12, "
        "verifying the defining identity (q∓q⁻¹)·Δ == q^m∓q^{-m}."
    )
    w.set_content_block("lem:alexander-T2N-closed-form")
    w.add_parameter("N_range", [2, 12])
    w.add_parameter("q_substrate", float(Q))

    table = []
    for N in range(2, 13):
        expr = alexander_T2N_closed(N)
        ok = closed_form_consistency(N)
        # Numerical evaluation at the substrate parameter.
        delta_q0 = float(sp.N(expr.subs(q, Q)))
        delta_at_1 = sp.Rational(alexander_weight_at_unit(N))
        ratio_at_1 = sp.Rational(alexander_half_weight_ratio(N))
        row = {
            "N": N,
            "alexander_symbolic": str(expr),
            "alexander_at_1": str(delta_at_1),
            "weight_per_atom_at_1": str(ratio_at_1),
            "alexander_at_q0": delta_q0,
            "parity": "even" if N % 2 == 0 else "odd",
            "components": 2 if N % 2 == 0 else 1,
            "identity_passed": bool(ok),
        }
        table.append(row)
        w.add_assertion(
            f"defining_identity_N={N}",
            computed=str(ok),
            expected="True",
        )
    w.add_data("table", table)

    # Spot-check the chapter's headline values.
    # T(2,6):  Δ = q² + 1 + q⁻²,  Δ(1) = 3.
    delta6 = alexander_T2N_closed(6)
    expected_str = sp.expand(q**2 + 1 + q**(-2))
    w.add_assertion(
        "T(2,6) closed form matches q^2 + 1 + q^-2",
        computed=str(sp.simplify(delta6 - expected_str) == 0),
        expected="True",
    )
    w.add_assertion(
        "T(2,6) Δ(1) == 3",
        computed=int(alexander_weight_at_unit(6)),
        expected=3,
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
