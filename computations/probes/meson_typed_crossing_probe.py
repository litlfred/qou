#!/usr/bin/env python3
"""
meson_typed_crossing_probe.py — test whether per-typed-crossing
evaluation reproduces the m_K/m_π ratio.

KEY STRUCTURAL FINDING:
  σ₁ is DIAGONAL on V_{(2,1)} (b₁ = 0 exactly, rho=1).
  Only σ₂ has off-diagonal binding (b₂ ≠ 0, rho=2).
  This means σ₁ and σ₂ play structurally different roles
  in the meson braid: σ₁ separates eigenspaces, σ₂ mixes them.

RESULT: Per-typed-crossing model (σ₁^a · σ₂^b) gives
K/π = 1.177, missing CODATA 3.537 by factor 3. The
generator-assignment model fails — strange quark modifies
crossing WEIGHTS, not generator assignments.

The missing factor ~3 suggests the strange-quark enhancement
enters through the VolDensity linking weight (per-typed geometric
factor), not through the Hecke character evaluation alone.
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

from mpmath import mp, mpf, sqrt, fabs, matrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def main():
    set_compute_dps()

    q = mpf(Q_50_DIGIT_STR)
    h = q - 1 / q

    a1 = h / (1 - q ** (-2))
    a1p = h / (1 - q ** 2)
    a2 = h / (1 - q ** (-4))
    a2p = h / (1 - q ** 4)
    b2 = sqrt((h ** 2 + 3) / (h ** 2 + 4))

    qi = lambda n: (q ** n - q ** (-n)) / h
    qf3 = qi(3) * qi(2)
    y3 = q ** 3 / qf3
    y21 = 1 / qf3
    y111 = q ** (-3) / qf3

    sigma2 = matrix([[a2, b2], [b2, a2p]])

    def sigma2_power(n):
        result = matrix([[1, 0], [0, 1]])
        for _ in range(n):
            result = result * sigma2
        return result

    def tr_M_typed(a_pow, b_pow):
        chi3 = q ** (a_pow + b_pow)
        chi111 = (-1 / q) ** (a_pow + b_pow)
        s1a = matrix([[q ** a_pow, 0], [0, (-1 / q) ** a_pow]])
        s2b = sigma2_power(b_pow)
        product = s1a * s2b
        chi21 = product[0, 0] + product[1, 1]
        return y3 * chi3 + y21 * chi21 / 2 + y111 * chi111

    tr_pion = fabs(tr_M_typed(3, 3))
    tr_kaon = fabs(tr_M_typed(3, 5))
    ratio = tr_kaon / tr_pion
    target = mpf("3.53713")

    wb = WitnessBuilder("meson-typed-crossing-probe", engine="mpmath")
    wb.set_description(
        "Per-typed-crossing meson probe. sigma_1 is DIAGONAL on V_{(2,1)} "
        "(b_1=0, rho=1). Typed model (sigma_1^a * sigma_2^b) gives K/pi = 1.18, "
        "missing CODATA 3.54 by 3x. Generator-assignment fails; strange quark "
        "modifies crossing weights, not generator choice."
    )

    wb.add_data("sigma1_diagonal", {
        "a1": str(float(a1)),
        "a1_prime": str(float(a1p)),
        "b1_sq": str(float(a1 * a1p + 1)),
        "conclusion": "sigma_1 is DIAGONAL on (2,1) — b_1 = 0 exactly",
    })
    wb.add_data("sigma2_mixing", {
        "a2": str(float(a2)),
        "a2_prime": str(float(a2p)),
        "b2_sq": str(float((h ** 2 + 3) / (h ** 2 + 4))),
        "conclusion": "sigma_2 has off-diagonal binding — b_2 = sqrt([3]_q/[2]_q^2)",
    })
    wb.add_data("typed_traces", {
        "pion_u3_d3": str(float(tr_pion)),
        "kaon_u3_s5": str(float(tr_kaon)),
        "ratio": str(float(ratio)),
        "CODATA_ratio": str(float(target)),
        "miss_factor": str(float(target / ratio)),
    })

    wb.add_assertion(
        "sigma1_diagonal_b1_zero",
        computed=float(fabs(a1 * a1p + 1)),
        expected=0,
        tolerance=1e-10,
        source="b_1^2 = a_1*a_1' + 1 = 0",
    )

    wb.save()

    print("=== MESON PER-TYPED-CROSSING PROBE ===")
    print()
    print(f"σ₁ on (2,1): DIAGONAL (b₁ = 0, eigenvalues q and −q⁻¹)")
    print(f"σ₂ on (2,1): MIXING   (b₂ = {float(b2):.6f})")
    print()
    print(f"Pion (u=3, d̄=3): |tr_M| = {float(tr_pion):.6f}")
    print(f"Kaon (u=3, s̄=5): |tr_M| = {float(tr_kaon):.6f}")
    print(f"K/π ratio = {float(ratio):.6f} (CODATA: {float(target):.3f}, miss: {float(target/ratio):.1f}×)")


if __name__ == "__main__":
    main()
