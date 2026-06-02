#!/usr/bin/env python3
"""
jonquiere_cyclotomic_general.py — numerical witness for the general
Jonquière inversion + Tate-rationality theorems at depth n, all n >= 2.

For every n >= 2 and every K >= 2:

  Li_n(zeta_K) - (-1)^{n-1} Li_n(zeta_K^{-1})
      = -(2 pi i)^n / n! * B_n(1/K)

where B_n is the n-th Bernoulli polynomial.  Equivalently:

  - For n odd:  Im Li_n(zeta_K)  ∈ pi^n · Q   (Tate-rational)
  - For n even: Re Li_n(zeta_K)  ∈ pi^n · Q   (Tate-rational)

with closed form -(2 pi i)^n / (2*[i or 1] * n!) * B_n(1/K).

Verifies the closed form at depths n in {2, 3, 4, 5} and K in
{3, 4, 5, 6, 7} at 50 dps.  Also verifies the general orbit-sum
identity:

  - n odd:  sum_{k=1..N-1} Cl_n(2 pi k / N) = (N^{1-n} - 1) zeta(n)
  - n even: sum_{k=1..N-1} Cl_n(2 pi k / N) = 0  (trivial)

Output: jonquiere-cyclotomic-general.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import time
from datetime import datetime, timezone
from math import factorial

from mpmath import mp, mpf, mpc, pi, exp, polylog, re, im, zeta, bernpoly
from mpmath import fabs as mpabs

from witness_base import WitnessBuilder

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

DEPTHS = [2, 3, 4, 5]
KS = [3, 4, 5, 6, 7]


def jonquiere_closed_form_simple(n: int, K: int) -> mpf:
    """Simpler direct evaluation: closed form is the real-valued
    coefficient.  For n odd:  Im Li_n(zeta_K) = (2 pi)^n / (2 * n!) *
    Im(i^n) * (-1) * B_n(1/K).  But i^n for n odd ∈ {±i}, contributing
    a sign.  Cleanest: just evaluate as a complex expression."""
    Bn = bernpoly(n, mpf(1) / K)
    full = -mpc(0, 2 * pi) ** n / factorial(n) * Bn
    # For n odd: take imaginary part (since LHS is 2i Im Li_n)
    # For n even: take real part (since LHS is 2 Re Li_n)
    if n % 2 == 1:
        return im(full) / 2
    else:
        return re(full) / 2


def li_n_numerical(n: int, K: int):
    """Direct numerical Li_n(zeta_K)."""
    zeta_K = exp(mpc(0, 1) * 2 * pi / mpf(K))
    return polylog(n, zeta_K)


def orbit_sum_predicted(n: int, N: int) -> mpf:
    """Predicted orbit sum sum_{k=1..N-1} Cl_n(2 pi k/N):
    - n odd:  (N^{1-n} - 1) * zeta(n)
    - n even: 0
    """
    if n % 2 == 1:
        return (mpf(N) ** (1 - n) - 1) * zeta(n)
    else:
        return mpf(0)


def orbit_sum_numerical(n: int, N: int) -> mpf:
    """Direct numerical orbit sum.  Cl_n = Re Li_n for n odd, Im Li_n
    for n even (Glaisher convention)."""
    s = mpf(0)
    for k in range(1, N):
        zeta_k = exp(mpc(0, 1) * 2 * pi * mpf(k) / mpf(N))
        li_val = polylog(n, zeta_k)
        if n % 2 == 1:
            s += re(li_val)
        else:
            s += im(li_val)
    return s


def main() -> None:
    start = time.monotonic()

    tate_rows = []
    orbit_rows = []
    max_tate_residual = mpf(0)
    max_orbit_residual = mpf(0)

    print("=" * 76)
    print("Jonquière inversion: Tate-rationality of 'wrong-parity' Li_n(ζ_K)")
    print("=" * 76)
    print(f"{'n':>2} {'K':>3}  {'closed_form':>40s}  {'residual':>13s}")
    for n in DEPTHS:
        for K in KS:
            closed = jonquiere_closed_form_simple(n, K)
            li_val = li_n_numerical(n, K)
            direct = re(li_val) if n % 2 == 0 else im(li_val)
            residual = mpabs(closed - direct)
            if residual > max_tate_residual:
                max_tate_residual = residual
            parity = "even" if n % 2 == 0 else "odd "
            part = "Re" if n % 2 == 0 else "Im"
            tate_rows.append({
                "n": n,
                "K": K,
                "parity": parity,
                "extracted_part": part,
                "closed_form_str": str(closed),
                "direct_str": str(direct),
                "residual_str": str(residual),
                "residual_below_1e_45": float(residual) < 1e-45,
            })
            print(f"{n:>2} {K:>3}  {mp.nstr(closed, 8):>40s}  {mp.nstr(residual, 4):>13s}  ({parity} → {part})")

    print()
    print("=" * 76)
    print("Orbit sum: sum_{k=1..N-1} Cl_n(2 pi k / N)")
    print("=" * 76)
    print(f"{'n':>2} {'N':>3}  {'predicted':>40s}  {'residual':>13s}")
    for n in DEPTHS:
        for N in KS:
            predicted = orbit_sum_predicted(n, N)
            direct = orbit_sum_numerical(n, N)
            residual = mpabs(predicted - direct)
            if residual > max_orbit_residual:
                max_orbit_residual = residual
            parity = "odd " if n % 2 == 1 else "even"
            expected = (
                f"(N^(1-n) - 1) * zeta(n)" if n % 2 == 1 else "0 (trivial)"
            )
            orbit_rows.append({
                "n": n,
                "N": N,
                "parity": parity,
                "predicted_form": expected,
                "predicted_str": str(predicted),
                "direct_sum_str": str(direct),
                "residual_str": str(residual),
                "residual_below_1e_45": float(residual) < 1e-45,
            })
            print(f"{n:>2} {N:>3}  {mp.nstr(predicted, 8):>40s}  {mp.nstr(residual, 4):>13s}  ({parity})")

    print()
    print(f"Max Tate-rationality residual: {max_tate_residual}")
    print(f"Max orbit-sum residual: {max_orbit_residual}")
    print(f"Both below 1e-45: "
          f"{float(max_tate_residual) < 1e-45 and float(max_orbit_residual) < 1e-45}")

    witness = {
        "computation": "jonquiere-cyclotomic-general",
        "description": (
            "Numerical verification at 50 dps of two general theorems "
            "subsuming PR #635 rounds A and B from `n = 3` to all "
            "depths n >= 2: "
            "(E) Tate-rationality of the 'wrong-parity' part of "
            "Li_n(zeta_K) via Jonquière inversion (Im for n odd, "
            "Re for n even); closed form involves Bernoulli polynomial "
            "B_n(1/K). "
            "(F) Orbit-sum sum_{k=1..N-1} Cl_n(2 pi k/N) reduces to "
            "(N^{1-n} - 1) zeta(n) for n odd, vanishes for n even. "
            f"Verified at n in {DEPTHS}, K in {KS}; max residual "
            "below 1e-45 in both theorems."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "precision_decimal_digits": mp.dps,
        "tested_depths": DEPTHS,
        "tested_indices": KS,
        "theorem_e_tate_rationality": {
            "claim": (
                "Li_n(zeta_K) - (-1)^{n-1} Li_n(zeta_K^{-1}) = "
                "-(2 pi i)^n / n! * B_n(1/K)"
            ),
            "rows": tate_rows,
            "max_residual_str": str(max_tate_residual),
            "all_below_1e_45": float(max_tate_residual) < 1e-45,
        },
        "theorem_f_orbit_sum": {
            "claim": (
                "sum_{k=1..N-1} Cl_n(2 pi k / N) = "
                "(N^{1-n} - 1) zeta(n) (n odd) or 0 (n even)"
            ),
            "rows": orbit_rows,
            "max_residual_str": str(max_orbit_residual),
            "all_below_1e_45": float(max_orbit_residual) < 1e-45,
        },
    }
    builder = WitnessBuilder.wrap_legacy(
        "jonquiere-cyclotomic-general",
        witness,
        script_path=__file__,
        engine="mpmath",
    )
    builder._start_time = start
    out = builder.save()
    print(f"\nwitness: {out}")


if __name__ == "__main__":
    main()
