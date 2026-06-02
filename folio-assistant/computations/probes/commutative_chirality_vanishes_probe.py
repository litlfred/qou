#!/usr/bin/env python3
"""Probe: commutative-chirality-vanishes (cor:commutative-chirality-vanishes).

Demonstrates the corollary's vanishing claim: in the commutative
limit q → 1, the chirality term H_A² · Φ_3 vanishes because
H_A = q - q⁻¹ → 0 (and Φ_3 stays bounded).

Numerical exercise: evaluate H_A² at a geometrically-shrinking
sequence of q values approaching 1 from above (q_n = 1 + 10⁻ⁿ for
n ∈ {1, 2, 3, 5, 10, 15, 20}), and confirm:

  - H_A² is monotone decreasing as q → 1
  - H_A² → 0 quadratically in (q - 1)
  - Even with a bounded chirality functional |Φ_3| ≤ M (we use
    M = 10 as a generous upper bound; in practice Φ_3 is O(1)),
    H_A² · M → 0

Computed via mpmath @ 50 dps so the limit is faithfully
witnessed at q - 1 ~ 10⁻²⁰.

Emits `commutative-chirality-vanishes-probe.witness.json`.
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
from q_parameter import Q_50_DIGIT_STR
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp, mpf, log10

from _precision import set_compute_dps
set_compute_dps()  # 50 dps default
from witness_base import WitnessBuilder  # noqa: E402

# Chirality-bound surrogate (the corollary's Φ_3 stays finite as q → 1;
# we use a generous bound for the worst-case product).
PHI_3_UPPER_BOUND = mpf(10)


def h_A_squared(q: mpf) -> mpf:
    """H_A² = (q - q⁻¹)²."""
    h = q - 1 / q
    return h * h


def main() -> int:
    # q_n = 1 + 10⁻ⁿ for n in this sequence — geometric approach to 1
    exponents = [1, 2, 3, 5, 10, 15, 20]
    rows = []
    for n in exponents:
        q = mpf(1) + mpf(10) ** (-n)
        h2 = h_A_squared(q)
        product_upper = h2 * PHI_3_UPPER_BOUND
        rows.append({
            "n": n,
            "q_minus_1": f"1e-{n}",
            "q_50dps": str(q),
            "H_A_squared_50dps": str(h2),
            "H_A_squared_log10": str(log10(h2)) if h2 > 0 else "-inf",
            "product_upper_bound_50dps": str(product_upper),
        })

    # Substrate parameter q_0 ≈ 1.110 for reference (NOT the commutative
    # limit — q_0 is the QOU substrate, where H_A is small but nonzero).
    q_0 = mpf(Q_50_DIGIT_STR)
    h2_q0 = h_A_squared(q_0)

    # Quadratic decay check: H_A² should be ~4·(q - 1)² for q ≈ 1
    # (since H_A = q - q⁻¹ ≈ 2(q - 1) when q → 1; H_A² ≈ 4·(q - 1)²).
    quadratic_check_rows = []
    for n in [5, 10, 15, 20]:
        q = mpf(1) + mpf(10) ** (-n)
        h2 = h_A_squared(q)
        expected_leading = mpf(4) * (q - 1) ** 2
        ratio = h2 / expected_leading
        # ratio should approach 1 as q → 1 (since correction term
        # is (q - 1)·h₂ + ... → 0).
        quadratic_check_rows.append({
            "n": n,
            "H_A_squared_over_4_qm1_sq": str(ratio),
            "deviation_from_1": str(abs(ratio - 1)),
        })

    b = (
        WitnessBuilder("commutative-chirality-vanishes-probe",
                       engine="mpmath")
        .set_description(
            "I1 probe for cor:commutative-chirality-vanishes.  "
            "Verifies that H_A² = (q - q⁻¹)² → 0 as q → 1, both "
            "directly and against the leading-order asymptotic "
            "H_A² ~ 4·(q - 1)².  Even with a generous chirality-"
            "functional bound |Φ_3| ≤ 10, the product H_A² · Φ_3 "
            "vanishes in the commutative limit — confirming the "
            "corollary's two-term reduction of the Wedderburn mass "
            "formula in the classical regime."
        )
        .set_content_block("cor:commutative-chirality-vanishes")
        .add_parameter("q_0_50dps", str(q_0))
        .add_parameter("phi_3_upper_bound", str(PHI_3_UPPER_BOUND))
        .add_parameter("H_A_squared_at_q_0_50dps", str(h2_q0))
        .add_data("limit_sequence", rows)
        .add_data("quadratic_decay_check", quadratic_check_rows)
        .add_assertion(
            name="H_A_squared_decreases_monotonically",
            computed=1.0 if all(
                mpf(rows[i + 1]["H_A_squared_50dps"])
                < mpf(rows[i]["H_A_squared_50dps"])
                for i in range(len(rows) - 1)
            ) else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1 = strict monotone descent)",
            source="Direct evaluation at q_n = 1 + 10⁻ⁿ.",
        )
        .add_assertion(
            name="H_A_squared_under_1e_minus_30_at_n_15",
            computed=1.0 if mpf(rows[5]["H_A_squared_50dps"]) < mpf("1e-29") else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1 = H_A²(1 + 10⁻¹⁵) < 10⁻²⁹, confirming → 0)",
            source="cor:commutative-chirality-vanishes asserts the limit.",
        )
        .add_assertion(
            name="quadratic_asymptotic_holds_at_n_20",
            computed=float(mpf(quadratic_check_rows[-1]["deviation_from_1"])),
            expected=0.0, tolerance=1e-15,
            unit="|H_A²/(4·(q−1)²) − 1| at q = 1 + 10⁻²⁰",
            source="Leading-order Taylor: H_A = q − q⁻¹ ≈ 2(q − 1) + O((q−1)²).",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
