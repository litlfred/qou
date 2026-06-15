#!/usr/bin/env python3
"""
cyclotomic_trilog_imaginary.py — numerical witness for the general
closed forms

  (A) Im Li_3(zeta_n) = (n-1)(n-2) pi^3 / (3 n^3)         for n >= 1
  (B) sum_{k=1..N-1} Cl_3(2 pi k/N) = -(N^2-1)/N^2 zeta(3) for N >= 2

both at 50 decimal digits via mpmath.  Verifies the closed forms at
multiple primes / small composites and records relative residuals.

These two theorems generalise rounds 10 and 11 of PR #634 (which only
established the closed forms at zeta_5).  See:

  - prop:cyclotomic-trilog-imaginary-closed-form (theorem A)
  - prop:cyclotomic-cl3-orbit-sum-general          (theorem B)

Output: cyclotomic-trilog-imaginary.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import time
from datetime import datetime, timezone

from mpmath import mp, mpf, mpc, pi, exp, polylog, im, re, zeta
from mpmath import fabs as mpabs

from witness_base import WitnessBuilder

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

TARGET_NS = [3, 4, 5, 6, 7, 10, 11, 12, 13]


def im_li3_closed_form(n: int) -> mpf:
    """Closed-form value (n - 1)(n - 2) pi^3 / (3 n^3)."""
    n_mp = mpf(n)
    return (n_mp - 1) * (n_mp - 2) * pi ** 3 / (3 * n_mp ** 3)


def im_li3_numerical(n: int) -> mpf:
    """Direct numerical Im Li_3(zeta_n) via mpmath.polylog."""
    zeta_n = exp(mpc(0, 1) * 2 * pi / mpf(n))
    return im(polylog(3, zeta_n))


def orbit_sum_closed_form(N: int) -> mpf:
    """Closed-form -(N^2 - 1)/N^2 * zeta(3)."""
    N_mp = mpf(N)
    return -(N_mp ** 2 - 1) / N_mp ** 2 * zeta(3)


def orbit_sum_numerical(N: int) -> mpf:
    """Direct sum over k = 1..N-1 of Cl_3(2 pi k / N)."""
    s = mpf(0)
    for k in range(1, N):
        zeta_k = exp(mpc(0, 1) * 2 * pi * mpf(k) / mpf(N))
        s += re(polylog(3, zeta_k))
    return s


def main() -> None:
    start = time.monotonic()

    rows_a = []
    rows_b = []
    max_residual_a = mpf(0)
    max_residual_b = mpf(0)

    print("=" * 72)
    print("Theorem A: Im Li_3(zeta_n) = (n - 1)(n - 2) pi^3 / (3 n^3)")
    print("=" * 72)
    print(f"{'n':>4}  {'closed_form':>50s}  {'residual':>15s}")
    for n in TARGET_NS:
        closed = im_li3_closed_form(n)
        direct = im_li3_numerical(n)
        residual = mpabs(closed - direct)
        if residual > max_residual_a:
            max_residual_a = residual
        rows_a.append({
            "n": n,
            "closed_form_str": str(closed),
            "direct_polylog_str": str(direct),
            "residual_str": str(residual),
            "residual_below_1e_45": float(residual) < 1e-45,
        })
        print(f"{n:>4}  {mp.nstr(closed, 12):>50s}  {mp.nstr(residual, 4):>15s}")

    print()
    print("=" * 72)
    print("Theorem B: sum_{k=1..N-1} Cl_3(2 pi k / N) = -(N^2 - 1)/N^2 zeta(3)")
    print("=" * 72)
    print(f"{'N':>4}  {'closed_form':>50s}  {'residual':>15s}")
    for N in TARGET_NS:
        closed = orbit_sum_closed_form(N)
        direct = orbit_sum_numerical(N)
        residual = mpabs(closed - direct)
        if residual > max_residual_b:
            max_residual_b = residual
        rows_b.append({
            "N": N,
            "closed_form_str": str(closed),
            "direct_sum_str": str(direct),
            "residual_str": str(residual),
            "residual_below_1e_45": float(residual) < 1e-45,
        })
        print(f"{N:>4}  {mp.nstr(closed, 12):>50s}  {mp.nstr(residual, 4):>15s}")

    print()
    print(f"max residual (Theorem A): {max_residual_a}")
    print(f"max residual (Theorem B): {max_residual_b}")
    print(f"both below 1e-45: "
          f"{float(max_residual_a) < 1e-45 and float(max_residual_b) < 1e-45}")

    witness = {
        "computation": "cyclotomic-trilog-imaginary",
        "description": (
            "Numerical verification at 50 decimal digits of two "
            "general closed forms for the depth-3 trilog at roots of "
            "unity: (A) Im Li_3(zeta_n) = (n-1)(n-2) pi^3 / (3 n^3) "
            "and (B) sum_{k=1..N-1} Cl_3(2 pi k / N) = -(N^2-1)/N^2 "
            "zeta(3). Both generalise rounds 10 and 11 of PR #634 "
            "from `zeta_5 only` to all roots of unity. Verified at "
            f"n, N in {TARGET_NS}; max residual below 1e-45 in both "
            "theorems."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "precision_decimal_digits": mp.dps,
        "tested_indices": TARGET_NS,
        "theorem_a": {
            "claim": "Im Li_3(zeta_n) = (n - 1)(n - 2) pi^3 / (3 n^3)",
            "rows": rows_a,
            "max_residual_str": str(max_residual_a),
            "all_below_1e_45": float(max_residual_a) < 1e-45,
        },
        "theorem_b": {
            "claim": (
                "sum_{k=1..N-1} Cl_3(2 pi k / N) = -(N^2 - 1)/N^2 zeta(3)"
            ),
            "rows": rows_b,
            "max_residual_str": str(max_residual_b),
            "all_below_1e_45": float(max_residual_b) < 1e-45,
        },
    }
    builder = WitnessBuilder.wrap_legacy(
        "cyclotomic-trilog-imaginary",
        witness,
        script_path=__file__,
        engine="mpmath",
        start_time=start,
    )
    out = builder.save()
    print(f"\nwitness: {out}")


if __name__ == "__main__":
    main()
