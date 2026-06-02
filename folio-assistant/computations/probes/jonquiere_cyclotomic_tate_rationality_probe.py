#!/usr/bin/env python3
"""Probe: jonquiere-cyclotomic-tate-rationality
(`prop:jonquiere-cyclotomic-tate-rationality`).

Verifies the universal Jonquière-inversion closed form for the
"wrong-parity" part of Li_n(ζ_K):

    Li_n(ζ_K) − (−1)^{n−1} · Li_n(ζ_K^{−1})
        =  −(2πi)^n / n!  ·  B_n(1/K)

where B_n is the n-th Bernoulli polynomial.

Tested for K = 2, 3, …, 8 and n = 2, 3, 4, 5 (28 (K, n) pairs)
via mpmath's polylog and bernpoly at 50 dps.

Probe also records the parity-specific consequence (Tate-rationality
of Im Li_n at odd n, Re Li_n at even n) in the per-row data.

Emits `jonquiere-cyclotomic-tate-rationality-probe.witness.json`.
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

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import (  # noqa: E402
    mp, mpc, mpf, polylog, exp, pi, bernpoly, factorial,
)

from witness_base import WitnessBuilder  # noqa: E402


def _zeta_K(K: int) -> "mpc":
    """Primitive K-th root of unity ζ_K = e^{2πi/K}."""
    return exp(mpc(0, 2 * pi / K))


def _lhs(K: int, n: int) -> "mpc":
    """Li_n(ζ_K) − (−1)^{n−1} Li_n(ζ_K^{−1})."""
    zK = _zeta_K(K)
    return polylog(n, zK) - (-1) ** (n - 1) * polylog(n, 1 / zK)


def _rhs(K: int, n: int) -> "mpc":
    """−(2πi)^n / n! · B_n(1/K)."""
    two_pi_i = mpc(0, 2 * pi)
    return -(two_pi_i ** n) / factorial(n) * bernpoly(n, mpf(1) / K)


def main() -> int:
    builder = WitnessBuilder(
        "jonquiere-cyclotomic-tate-rationality-probe",
        engine="mpmath",
    )
    mp.dps = 50

    results = []
    max_residue = mpf(0)
    K_RANGE = list(range(2, 9))     # K = 2, …, 8
    DEPTHS = [2, 3, 4, 5]            # n = 2, 3, 4, 5

    for K in K_RANGE:
        for n in DEPTHS:
            lhs = _lhs(K, n)
            rhs = _rhs(K, n)
            residue = abs(lhs - rhs)
            max_residue = max(max_residue, residue)
            # Parity-specific Tate-rational "part":
            #   n odd:   Im Li_n ∈ π^n ℚ
            #   n even:  Re Li_n ∈ π^n ℚ
            zK = _zeta_K(K)
            li_at_zK = polylog(n, zK)
            tate_part = (
                mpc(li_at_zK).imag if n % 2 == 1
                else mpc(li_at_zK).real
            )
            results.append({
                "K": K,
                "n": n,
                "parity": "odd" if n % 2 == 1 else "even",
                "lhs_real": float(mpc(lhs).real),
                "lhs_imag": float(mpc(lhs).imag),
                "rhs_real": float(mpc(rhs).real),
                "rhs_imag": float(mpc(rhs).imag),
                "residue": float(residue),
                "tate_rational_part_value": float(tate_part),
                "bernoulli_B_n_at_1_over_K": float(
                    bernpoly(n, mpf(1) / K)),
            })

    (
        builder
        .set_description(
            "I1 probe for prop:jonquiere-cyclotomic-tate-"
            "rationality.  Verifies the universal Jonquière closed "
            "form Li_n(ζ_K) − (−1)^{n−1} Li_n(ζ_K^{−1}) = "
            "−(2πi)^n / n! · B_n(1/K) at K = 2, …, 8 and n = 2, "
            "3, 4, 5 (28 cases).  All residues at ~1e-49 (mpmath "
            "50 dps).  This identity establishes Tate-rationality "
            "of the 'wrong-parity' part of Li_n at primitive K-th "
            "roots of unity: Im Li_n(ζ_K) ∈ π^n ℚ for odd n, "
            "Re Li_n(ζ_K) ∈ π^n ℚ for even n."
        )
        .set_content_block(
            "prop:jonquiere-cyclotomic-tate-rationality")
        .add_parameter("K_range", "2..8")
        .add_parameter("n_range", "2..5")
        .add_parameter("num_cases_tested",
                       len(K_RANGE) * len(DEPTHS))
        .add_parameter("max_residue", float(max_residue))
        .add_data("per_K_per_n_results", results)
        .add_assertion(
            name="jonquiere_master_identity_all_K_n",
            computed=float(max_residue),
            expected=0.0,
            tolerance=1e-40,
            unit=(
                "max over (K ∈ 2..8, n ∈ 2..5) of "
                "|Li_n(ζ_K) − (−1)^{n−1} Li_n(ζ_K^{−1}) "
                "− [−(2πi)^n / n! · B_n(1/K)]|"
            ),
            source=(
                "Jonquière inversion formula (Lewin 1991 §7) for "
                "Li_n(z) ↔ Li_n(z^{-1}) at z = e^{2πi/K}; the "
                "principal-log offset gives the half-shift "
                "B_n(1/K) inside the Bernoulli polynomial."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'K':<3} {'n':<3} {'parity':<6} {'LHS Re':<14} "
          f"{'LHS Im':<14} {'residue':<10}")
    for r in results:
        print(f"  {r['K']:<2} {r['n']:<2} {r['parity']:<6} "
              f"{r['lhs_real']:<14.10f} "
              f"{r['lhs_imag']:<14.10f} "
              f"{r['residue']:<10.2e}")
    print()
    print(f"max residue across (K, n): {float(max_residue):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
