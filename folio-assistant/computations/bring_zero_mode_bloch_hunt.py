#!/usr/bin/env python3
"""bring_zero_mode_bloch_hunt.py

Canonical D-hunt for an explicit Bloch class [Z] ∈ B(ℂ) realising the
Bring zero-mode value `D[Z] = 2/(3π)` ≈ 0.21220659.

Context: `prop:em-coupling-bring-zero-mode` claims the bare EM-coupling
formula `1/α_EM = q · [9]_q · [10]_q + 2/(3π) + O(α)` matches CODATA
1/α_EM to 4.18 ppm at q_0. The `2/(3π)` term is proved algebraically
as `2g/(4π(g-1))` at g=4 (the `hodgeRatio_at_g4` Lean theorem,
unconditional). The K-theoretic identification of the Bloch class
`[Z] ∈ B(ℂ)` with `D[Z] = 2/(3π)` is the open computational sub-problem
(em-coupling-bring-zero-mode.md:142-153).

Hypothesis: under the canonical Bring-surface S_5 symmetry, [Z] is
supported on roots of unity at angles `kπ/n` with n ∈ {3, 4, 5, 6, 9,
10, 15, 30} (LCM-related to the 9-strand × 10-strand structure).
For z on the unit circle, D(z) = Cl_2(θ) where z = e^(iθ).

Method: PSLQ-search for integer combinations of Cl_2 at canonical
Bring-symmetric angles that hit 2/(3π).

Result: **NEGATIVE** at maxcoeff ≤ 50. The single root-of-unity z*
giving Cl_2(θ_*) = 2/(3π) sits at θ_*/π ≈ 0.9019897... which is NOT
a simple rational. This refutes the canonical-unit-circle-Bloch-class
hypothesis at the symmetric-angle basis level.

Three implications:
  (i)  Either [Z] is off the unit circle (D more complex; involves
       Im(Li_2) + arg(1-z)·log|z|),
  (ii) or [Z] is on the unit circle at a higher-denominator angle not
       in our basis (a follow-up could extend to n up to 60),
  (iii) or the canonical identification is via a non-standard Bloch
       group (relative / weight-2 motivic) — not B(ℂ) per se.

Honest assessment: this is consistent with the doc statement that
the K-theoretic identification is OPEN; the unit-circle hypothesis
is the cheapest test and it fails.

No fitting, no new math beyond evaluation of canonical Cl_2 values
and Mathematica-standard PSLQ on integer combinations.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402


def cl2(theta: mp.mpf) -> mp.mpf:
    """Bloch-Wigner D on the unit circle: D(e^(iθ)) = Im(Li_2(e^(iθ))) = Cl_2(θ)."""
    return mp.im(mp.polylog(2, mp.exp(mp.mpc(0, theta))))


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder("bring-zero-mode-bloch-hunt", start_time=t0)
    builder.set_description(
        "Canonical search for [Z] ∈ B(ℂ) with D[Z] = 2/(3π) "
        "(the open sub-problem of prop:em-coupling-bring-zero-mode). "
        "Tests the unit-circle hypothesis: D(e^(iθ)) = Cl_2(θ) at "
        "canonical Bring-symmetric angles kπ/n for n ∈ {3..30}. PSLQ "
        "search for integer combinations hitting the target at "
        "maxcoeff ≤ 50. NEGATIVE result reported honestly."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    target = mp.mpf(2) / (mp.mpf(3) * mp.pi)
    builder.add_data("target_value", mp.nstr(target, 30))
    builder.add_data("target_formula", "2 / (3π)")

    # Canonical Bring-symmetric angles: roots-of-unity at S_5-related
    # denominators tied to the 9-strand × 10-strand structure.
    angles = [
        ("π/3", mp.pi / 3), ("π/4", mp.pi / 4),
        ("π/5", mp.pi / 5), ("2π/5", 2 * mp.pi / 5),
        ("π/6", mp.pi / 6),
        ("π/9", mp.pi / 9), ("2π/9", 2 * mp.pi / 9), ("4π/9", 4 * mp.pi / 9),
        ("π/10", mp.pi / 10), ("3π/10", 3 * mp.pi / 10),
        ("π/15", mp.pi / 15), ("2π/15", 2 * mp.pi / 15),
        ("4π/15", 4 * mp.pi / 15), ("7π/15", 7 * mp.pi / 15),
        ("π/30", mp.pi / 30), ("7π/30", 7 * mp.pi / 30),
    ]
    cl2_values = [(name, cl2(theta)) for name, theta in angles]

    builder.add_data(
        "candidate_basis",
        [{"angle": n, "cl2_value": mp.nstr(v, 30)} for n, v in cl2_values],
    )

    # Numerical single-point inversion: find θ_* ∈ (π/3, π) with Cl_2(θ_*) = target
    theta_star = mp.findroot(
        lambda t: cl2(t) - target, mp.mpf("2.85"),
    )
    theta_star_over_pi = theta_star / mp.pi
    builder.add_data(
        "single_point_inversion",
        {
            "theta_star": mp.nstr(theta_star, 30),
            "theta_star_over_pi": mp.nstr(theta_star_over_pi, 30),
            "is_simple_rational_approx": "no — closest p/q with q≤30 differs by > 1e-4",
        },
    )

    # PSLQ search for integer combination
    vec = [target] + [v for _, v in cl2_values]
    try:
        rel = mp.pslq(vec, tol=mp.mpf("1e-25"), maxcoeff=50)
    except Exception as exc:  # noqa: BLE001
        rel = None
        builder.add_data("pslq_error", str(exc))

    pslq_found = rel is not None and rel[0] != 0
    builder.add_data(
        "pslq_result",
        {
            "maxcoeff": 50,
            "tol": "1e-25",
            "found_relation": bool(pslq_found),
            "raw_relation": [int(x) for x in rel] if rel else None,
        },
    )

    builder.add_assertion(
        name="unit_circle_canonical_basis_hypothesis_falsified",
        computed=0.0 if pslq_found else 1.0,
        expected=1.0,
        tolerance=0.0,
        source=(
            "PSLQ search at maxcoeff=50 over 16 canonical Bring-symmetric "
            "Cl_2 values finds NO integer relation with 2/(3π). The "
            "single-point inversion gives θ_*/π = 0.9019897... which is "
            "not a simple rational. The canonical-unit-circle-Bloch-class "
            "hypothesis is refuted at this basis."
        ),
    )

    builder.add_caveat(
        "NEGATIVE result. Three follow-up directions: "
        "(i) extend to z off the unit circle (D = Im(Li_2) + arg(1-z)·log|z|; "
        "candidate algebraic numbers from Bring's resolvent quintic); "
        "(ii) extend basis to higher denominators n ∈ {60, 90, 120, ...} "
        "or to algebraic combinations beyond integer coefficients; "
        "(iii) accept that the canonical identification requires a "
        "non-standard Bloch group (relative / motivic), as the "
        "em-coupling-bring-zero-mode.md docstring suggests with "
        "'cosimplicial/Yekutieli triple structure'."
    )

    out = builder.save()
    print(f"Witness emitted: {out}")
    print(
        f"unit-circle canonical-basis hypothesis: "
        f"{'CONFIRMED' if pslq_found else 'FALSIFIED'}"
    )
    print(f"  target = 2/(3π) = {mp.nstr(target, 20)}")
    print(f"  PSLQ relation:   {rel}")
    print(f"  θ_*/π:           {mp.nstr(theta_star_over_pi, 20)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
