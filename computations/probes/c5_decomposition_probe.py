#!/usr/bin/env python3
"""
Numerical cross-check of c_5 closed-form identities proved in
`folio/quantum-observable-universe/braids-and-knots/c5-involution-leibniz-decomposition.lean`.

Per the "proven-but-unwired" audit (PR following #1252 Option E Phase 1a),
the c5 file has 3 algebraic identities with no compute witness:

  1. quantum_two_squared_eq_skein_squared_plus_four:
       [2]_q² = (q - q⁻¹)² + 4 = h² + 4

  2. hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared:
       b²(q) = (q⁴+q²+1)/(q²+1)² = 1 - 1/[2]_q²

  3. c5_decomposition_via_quantum_two (composite):
       c_5(q) = -b²(q) - 1/2 = -3/2 + 1/[2]_q² = -3/2 + 1/(h² + 4)

These are pure field algebra over [Field R] (proved in Lean via
`field_simp; ring`); numerical cross-check at canonical q_0 to ≤ 1e-40
acts as regression guard if either Lean or the canonical pin drifts.

c_5 feeds the silver-ratio Q_β arithmetic per
`prop:silver-ratio-beta-decay-null` and `prop:neutron-qvalue-symbolic`.

Audit-only; cites the c5-involution-leibniz-decomposition content block.
"""



from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

from experimental_constants import MU_OVER_E
from q_parameter import Q_50_DIGIT_STR, Q_MP
from witness_base import WitnessBuilder
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    set_compute_dps()

    q = Q_MP
    qi = 1 / q
    h = q - qi

    # Symbolic q-bracket [2]_q
    two_q = q + qi

    # Hoefsmit off-diagonal squared (the standard closed form)
    b_sq_direct = (q**4 + q**2 + 1) / (q**2 + 1) ** 2
    b_sq_via_quantum_two = 1 - 1 / two_q**2

    # c_5 closed forms
    c5_via_decomposition = -b_sq_direct - mp.mpf(1) / 2  # c5Decomposition
    c5_via_quantum_two = -mp.mpf(3) / 2 + 1 / two_q**2  # c5_decomposition_via_quantum_two
    c5_via_skein = -mp.mpf(3) / 2 + 1 / (h**2 + 4)  # c5RationalMap

    w = WitnessBuilder("c5-decomposition-probe", engine="mpmath")
    w.set_description(
        "Numerical cross-check of three c_5 closed-form identities from "
        "`c5-involution-leibniz-decomposition.lean`: (1) [2]_q² = h²+4, "
        "(2) b² = 1 - 1/[2]_q², (3) c_5 = -3/2 + 1/[2]_q² = -3/2 + 1/(h²+4). "
        "Closes the 'proven-but-unwired' gap identified post-PR #1252 audit "
        "for the highest-centrality (silver-ratio Q_β chain) Lean theorem "
        "lacking a production-compute witness."
    )
    w.set_audit_only("docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md")
    w.set_content_block("prop:c5-involution-leibniz-decomposition")
    w.add_parameter("precision_dps", 50)
    w.add_parameter("q_0", str(q))
    w.add_parameter("hecke_h", str(h))
    w.add_parameter("quantum_two", str(two_q))
    w.add_parameter("b_sq_direct", str(b_sq_direct))
    w.add_parameter("c5_value_at_q_0", str(c5_via_quantum_two))

    # Identity 1: [2]_q² = h² + 4
    w.add_assertion(
        name="lean_quantum_two_squared_eq_skein_squared_plus_four",
        computed=str(two_q**2),
        expected=str(h**2 + 4),
        tolerance=1e-40,
        source="theorem quantum_two_squared_eq_skein_squared_plus_four",
    )

    # Identity 2: b²(q) = 1 - 1/[2]_q²
    w.add_assertion(
        name="lean_hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared",
        computed=str(b_sq_direct),
        expected=str(b_sq_via_quantum_two),
        tolerance=1e-40,
        source="theorem hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared",
    )

    # Identity 3 (composite): c_5(q) = -b² - 1/2 = -3/2 + 1/[2]_q²
    w.add_assertion(
        name="lean_c5_decomposition_via_quantum_two",
        computed=str(c5_via_decomposition),
        expected=str(c5_via_quantum_two),
        tolerance=1e-40,
        source="theorem c5_decomposition_via_quantum_two",
    )

    # Identity 4: c_5(q) via skein rational map (h-form) matches the [2]_q form
    w.add_assertion(
        name="lean_c5RationalMap_at_skein_eq_c5Decomposition",
        computed=str(c5_via_skein),
        expected=str(c5_via_decomposition),
        tolerance=1e-40,
        source="theorem c5RationalMap_at_skein_eq_c5Decomposition",
    )

    w.add_caveat(
        "The Lean identities are PROVED (sorry-free, field_simp; ring over "
        "generic [Field R]); this witness only verifies the canonical "
        "substrate-q_0 specialisation. The outer empirical claim "
        "'c_5 matches Q_β data to 2.4%' is a separate downstream check, "
        "not asserted here."
    )

    out = w.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
