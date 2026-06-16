#!/usr/bin/env python3
"""Probe: cyclotomic-trilog-imaginary-closed-form
(`prop:cyclotomic-trilog-imaginary-closed-form`).

Verifies the universal closed form

    Im Li_3(ζ_n)  =  (n − 1)(n − 2) · π³ / (3 n³)

for the imaginary part of the trilogarithm at every primitive n-th
root of unity ζ_n = e^{2πi/n}.  The closed form is exact in
ℚ · π³ (Tate-rational) for every n.

Tested for n = 2, 3, …, 12 against mpmath's `polylog(3, ζ_n)` at
50 dps.  All residues at the mpmath numerical-precision floor.

Probe also documents the **n = 1 boundary case**: ζ_1 = 1, and
Li_3(1) = ζ(3) ≈ 1.2020569 (real), so Im Li_3(1) = 0 — agrees
with the closed form (0 · (−1) · π³ / 3 = 0).

Emits `cyclotomic-trilog-imaginary-closed-form-probe.witness.json`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Path bridge — keeps flat-namespace imports (`from witness_base
# import ...`) working from the new cluster subdirectory. See
# computations/_path_bridge.py for details.
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401, E402

from mpmath import mp, mpc, mpf, polylog, exp, pi  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def _zeta_n(n: int) -> "mpc":
    """Primitive n-th root of unity ζ_n = e^{2πi/n}."""
    return exp(mpc(0, 2 * pi / n))


def _closed_form(n: int) -> "mpf":
    """Closed form (n−1)(n−2) π³ / (3 n³)."""
    return mpf(n - 1) * mpf(n - 2) * pi ** 3 / (3 * mpf(n) ** 3)


def main() -> int:
    builder = WitnessBuilder(
        "cyclotomic-trilog-imaginary-closed-form-probe",
        engine="mpmath",
    )
    mp.dps = 50

    results = []
    max_residue = mpf(0)
    for n in range(1, 13):  # n = 1 … 12
        if n == 1:
            z = mpc(1, 0)
        else:
            z = _zeta_n(n)
        li3 = polylog(3, z)
        im_li3 = mpc(li3).imag
        closed = _closed_form(n)
        residue = abs(im_li3 - closed)
        max_residue = max(max_residue, residue)
        results.append({
            "n": n,
            "Im_Li3_zeta_n_direct": float(im_li3),
            "closed_form_value": float(closed),
            "residue": float(residue),
            "Tate_rational_form":
                f"({n - 1})({n - 2}) π³ / (3 · {n}³)",
        })

    (
        builder
        .set_description(
            "I1 probe for prop:cyclotomic-trilog-imaginary-closed-"
            "form.  Verifies Im Li_3(ζ_n) = (n−1)(n−2)π³/(3n³) for "
            "n = 1, 2, …, 12 against mpmath's `polylog(3, ζ_n)` at "
            "50 dps.  All residues at numerical precision (~1e-49); "
            "the closed form is exact in ℚ · π³ (Tate-rational) for "
            "every n, which projects to zero in the Beilinson "
            "regulator quotient 𝒫_3 → 𝒫_3 / Tate."
        )
        .set_content_block(
            "prop:cyclotomic-trilog-imaginary-closed-form")
        .add_parameter("n_range_tested", "1..12")
        .add_parameter("max_residue", float(max_residue))
        .add_data("per_n_results", results)
        .add_assertion(
            name="im_li3_zeta_n_closed_form_all_n_1_to_12",
            computed=float(max_residue),
            expected=0.0,
            tolerance=1e-40,
            unit=(
                "max over n ∈ {1, …, 12} of "
                "|Im Li_3(ζ_n)_mpmath − (n−1)(n−2)π³/(3n³)|"
            ),
            source=(
                "Kummer reflection formula (Lewin 1991, Eq. 6.10) "
                "applied to ζ_n = e^{2πi/n}; principal-log identity "
                "for −ζ_n gives the closed form."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'n':<4} {'Im Li_3(ζ_n)':<25} {'(n-1)(n-2)π³/(3n³)':<25} {'residue':<12}")
    for r in results:
        print(f"  {r['n']:<2}   "
              f"{r['Im_Li3_zeta_n_direct']:<25.20f} "
              f"{r['closed_form_value']:<25.20f} "
              f"{r['residue']:<12.2e}")
    print()
    print(f"max residue across n = 1…12: {float(max_residue):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
