#!/usr/bin/env python3
"""Probe: cyclotomic-cl3-orbit-sum-general
(`prop:cyclotomic-cl3-orbit-sum-general`).

The n = 3 specialization of the universal Clausen-orbit identity:

    Σ_{k=1}^{N-1}  Cl_3(2πk/N)  =  −(N² − 1)/N²  ·  ζ(3).

Plus the **half-sum identity** for odd N:

    Σ_{k=1}^{(N-1)/2}  Cl_3(2πk/N)  =  −(N² − 1) / (2 N²)  ·  ζ(3).

The half-sum identity uses the reflection symmetry Cl_3(θ) =
Cl_3(2π − θ) (since Cl_3 = Re Li_3 and conjugation fixes the real
part) — for odd N the (N−1)/2 unique values appear twice in the
full sum, halving cleanly; for even N the term at k = N/2
(angle π) has no partner and the simple halving breaks down.

This probe complements the `cyclotomic-orbit-sum-all-depths` probe
(commit 364b58e44, which covers the full sum at every depth) by
explicitly verifying the parity-halved odd-N reduction.

Tested for N = 3, 5, 7, 9, 11 (5 odd values).  All residues at
~1e-49.

Emits `cyclotomic-cl3-orbit-sum-general-probe.witness.json`.
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


def _cl3(theta: "mpf") -> "mpf":
    """Cl_3(θ) = Re Li_3(e^{iθ})."""
    return mpc(polylog(3, exp(mpc(0, theta)))).real


def _full_closed_form(N: int) -> "mpf":
    return -(mpf(N) ** 2 - 1) / (mpf(N) ** 2) * zeta(3)


def _half_closed_form(N: int) -> "mpf":
    return -(mpf(N) ** 2 - 1) / (2 * mpf(N) ** 2) * zeta(3)


def main() -> int:
    builder = WitnessBuilder(
        "cyclotomic-cl3-orbit-sum-general-probe",
        engine="mpmath",
    )
    mp.dps = 50

    results = []
    max_full_residue = mpf(0)
    max_half_residue = mpf(0)
    ODD_N = [3, 5, 7, 9, 11]

    for N in ODD_N:
        full_sum = sum(
            (_cl3(2 * pi * mpf(k) / N) for k in range(1, N)),
            mpf(0),
        )
        half_sum = sum(
            (_cl3(2 * pi * mpf(k) / N) for k in range(1, (N + 1) // 2)),
            mpf(0),
        )
        full_closed = _full_closed_form(N)
        half_closed = _half_closed_form(N)
        full_residue = abs(full_sum - full_closed)
        half_residue = abs(half_sum - half_closed)
        max_full_residue = max(max_full_residue, full_residue)
        max_half_residue = max(max_half_residue, half_residue)
        results.append({
            "N": N,
            "full_sum_direct": float(full_sum),
            "full_closed_form": float(full_closed),
            "full_residue": float(full_residue),
            "half_sum_direct": float(half_sum),
            "half_closed_form": float(half_closed),
            "half_residue": float(half_residue),
        })

    (
        builder
        .set_description(
            "I1 probe for prop:cyclotomic-cl3-orbit-sum-general.  "
            "Verifies (a) the full Clausen-3 orbit sum closed form "
            "Σ_{k=1..N-1} Cl_3(2πk/N) = −(N²−1)/N² · ζ(3), and "
            "(b) the half-sum identity for odd N: "
            "Σ_{k=1..(N-1)/2} Cl_3(2πk/N) = −(N²−1)/(2N²) · ζ(3).  "
            "Tested at N ∈ {3, 5, 7, 9, 11} via mpmath polylog at "
            "50 dps; both residues at the numerical-precision "
            "floor (~1e-49).  Complements the all-depths orbit-sum "
            "probe by witnessing the parity-halved odd-N "
            "reduction explicitly."
        )
        .set_content_block(
            "prop:cyclotomic-cl3-orbit-sum-general")
        .add_parameter("N_range_odd_only", "3, 5, 7, 9, 11")
        .add_parameter("max_full_sum_residue",
                       float(max_full_residue))
        .add_parameter("max_half_sum_residue",
                       float(max_half_residue))
        .add_data("per_N_results", results)
        .add_assertion(
            name="cl3_full_orbit_sum_closed_form",
            computed=float(max_full_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over N ∈ {3,5,7,9,11} of |Σ Cl_3 − "
                "(−(N²−1)/N² · ζ(3))|"
            ),
            source=(
                "Multiplication formula Σ_{k=0..N-1} Li_n(ζ_N^k) "
                "= N^{1-n} Li_n(1) at n = 3, taking real parts."
            ),
        )
        .add_assertion(
            name="cl3_half_orbit_sum_closed_form_odd_N",
            computed=float(max_half_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over N ∈ {3,5,7,9,11} of |Σ_{k=1..(N-1)/2} "
                "Cl_3 − (−(N²−1)/(2N²) · ζ(3))|"
            ),
            source=(
                "Reflection symmetry Cl_3(2πk/N) = Cl_3(2π(N-k)/N); "
                "for odd N the (N-1)/2 distinct values each appear "
                "twice in the full sum, so the half-sum is exactly "
                "half the full sum."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'N':<3} {'full sum':<18} {'-(N²-1)/N² ζ(3)':<18} "
          f"{'half sum':<18} {'-(N²-1)/(2N²) ζ(3)':<18}")
    for r in results:
        print(f"  {r['N']:<2} "
              f"{r['full_sum_direct']:<18.12f} "
              f"{r['full_closed_form']:<18.12f} "
              f"{r['half_sum_direct']:<18.12f} "
              f"{r['half_closed_form']:<18.12f}")
    print()
    print(f"max full-sum residue: {float(max_full_residue):.2e}")
    print(f"max half-sum residue: {float(max_half_residue):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
