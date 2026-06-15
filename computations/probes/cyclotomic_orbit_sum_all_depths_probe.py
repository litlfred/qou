#!/usr/bin/env python3
"""Probe: cyclotomic-orbit-sum-all-depths
(`prop:cyclotomic-orbit-sum-all-depths`).

Verifies the universal orbit-sum identity for the Glaisher Clausen
function at every depth n ≥ 2:

    Σ_{k=1}^{N-1}  Cl_n(2πk/N)
        =  ⎧ (N^{1-n} − 1) · ζ(n)   if n is odd
           ⎩ 0                       if n is even

where

    Cl_n(θ)  =  ⎧ Re Li_n(e^{iθ})  if n is odd
                ⎩ Im Li_n(e^{iθ})  if n is even.

Tested for N = 2, 3, …, 8 and n = 2, 3, 4, 5 (28 (N, n) pairs).
All residues at ~1e-49 (mpmath 50 dps).

Emits `cyclotomic-orbit-sum-all-depths-probe.witness.json`.
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

from mpmath import mp, mpc, mpf, polylog, exp, pi, zeta  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def _clausen(n: int, theta: "mpf") -> "mpf":
    """Cl_n(θ) — Re Li_n(e^{iθ}) for odd n, Im Li_n for even n."""
    z = exp(mpc(0, theta))
    val = polylog(n, z)
    cval = mpc(val)
    return cval.real if n % 2 == 1 else cval.imag


def _closed_form(N: int, n: int) -> "mpf":
    """(N^{1-n} − 1) ζ(n) for odd n; 0 for even n."""
    if n % 2 == 0:
        return mpf(0)
    return (mpf(N) ** (1 - n) - 1) * zeta(n)


def main() -> int:
    builder = WitnessBuilder(
        "cyclotomic-orbit-sum-all-depths-probe",
        engine="mpmath",
    )
    mp.dps = 50

    results = []
    max_residue = mpf(0)
    N_RANGE = list(range(2, 9))     # N = 2, …, 8
    N_RANGE_DEPTHS = [2, 3, 4, 5]   # n = 2, 3, 4, 5

    for N in N_RANGE:
        for n in N_RANGE_DEPTHS:
            orbit_sum = mpf(0)
            for k in range(1, N):
                orbit_sum += _clausen(n, 2 * pi * mpf(k) / N)
            closed = _closed_form(N, n)
            residue = abs(orbit_sum - closed)
            max_residue = max(max_residue, residue)
            results.append({
                "N": N,
                "n": n,
                "parity": "odd" if n % 2 == 1 else "even",
                "orbit_sum_direct": float(orbit_sum),
                "closed_form_value": float(closed),
                "residue": float(residue),
            })

    (
        builder
        .set_description(
            "I1 probe for prop:cyclotomic-orbit-sum-all-depths.  "
            "Verifies the universal Clausen-orbit closed form "
            "Σ_{k=1..N-1} Cl_n(2πk/N) = (N^{1-n}-1)ζ(n) for odd n, "
            "= 0 for even n.  Tested at N = 2, …, 8 and n = 2, 3, "
            "4, 5 (28 cases) via mpmath's polylog at 50 dps.  All "
            "residues at the numerical-precision floor (~1e-49); "
            "the closed form is exact in ζ(n) · ℚ for odd n and "
            "exactly zero for even n."
        )
        .set_content_block("prop:cyclotomic-orbit-sum-all-depths")
        .add_parameter("N_range", "2..8")
        .add_parameter("n_range", "2..5")
        .add_parameter("num_cases_tested",
                       len(N_RANGE) * len(N_RANGE_DEPTHS))
        .add_parameter("max_residue", float(max_residue))
        .add_data("per_N_per_n_results", results)
        .add_assertion(
            name="clausen_orbit_sum_closed_form_all_N_n",
            computed=float(max_residue),
            expected=0.0,
            tolerance=1e-40,
            unit=(
                "max over (N ∈ 2..8, n ∈ 2..5) of |orbit_sum − "
                "((N^{1-n}-1)ζ(n) [odd] or 0 [even])|"
            ),
            source=(
                "Multiplication formula for polylogarithms at roots "
                "of unity (Lewin 1991): "
                "Σ_{k=0..N-1} Li_n(z^{1/N} ζ_N^k) = N^{1-n} Li_n(z). "
                "Set z = 1 and take Re / Im to separate odd / even "
                "depths."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'N':<3} {'n':<3} {'parity':<6} {'orbit sum':<22} {'closed form':<22} {'residue':<10}")
    for r in results:
        print(f"  {r['N']:<2} {r['n']:<2} {r['parity']:<6} "
              f"{r['orbit_sum_direct']:<22.16f} "
              f"{r['closed_form_value']:<22.16f} "
              f"{r['residue']:<10.2e}")
    print()
    print(f"max residue across all (N, n): {float(max_residue):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
