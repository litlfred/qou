#!/usr/bin/env python3
"""Probe: plancherel-weight-boundedness
(`prop:plancherel-weight-boundedness`).

Verifies that the classical Plancherel weights

    w_λ := (dim V_λ)² / n!,   λ ⊢ n

satisfy:

  (1) Non-negativity:  w_λ ∈ [0, 1]
  (2) Normalisation:   Σ_{λ ⊢ n} w_λ = 1   (exact in ℚ)

The proof reduces to the symmetric-group dimension identity
n! = Σ_λ (dim V_λ)², which is verified exactly using integer
arithmetic on standard-Young-tableau counts.

Probed for n = 1, …, 8 (covering H_n up to the n_0 deuteron-scale
ambient algebra used in QOU's nucleon binding work).

Emits `plancherel-weight-boundedness-probe.witness.json`.
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

import math
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from hecke_character_symbolic import standard_young_tableaux  # noqa: E402


def _partitions_of(n: int):
    def go(n_, max_):
        if n_ == 0:
            yield ()
            return
        for i in range(min(n_, max_), 0, -1):
            for tail in go(n_ - i, i):
                yield (i,) + tail
    yield from go(n, n)


def main() -> int:
    builder = WitnessBuilder(
        "plancherel-weight-boundedness-probe",
        engine="python (Fraction)",
    )

    N_RANGE = range(1, 9)  # n = 1 … 8

    per_n_results = []
    max_normalisation_deviation = Fraction(0)
    min_weight_seen = Fraction(1)
    max_weight_seen = Fraction(0)

    for n in N_RANGE:
        n_fact = math.factorial(n)
        per_lambda = []
        total = Fraction(0)
        for shape in _partitions_of(n):
            syts, _, _ = standard_young_tableaux(shape)
            f_lam = len(syts)
            w_lam = Fraction(f_lam * f_lam, n_fact)
            total += w_lam
            min_weight_seen = min(min_weight_seen, w_lam)
            max_weight_seen = max(max_weight_seen, w_lam)
            per_lambda.append({
                "shape": str(shape),
                "dim_V_lambda": f_lam,
                "w_lambda_num": w_lam.numerator,
                "w_lambda_den": w_lam.denominator,
                "w_lambda_float": float(w_lam),
                "in_unit_interval": 0 <= w_lam <= 1,
            })
        deviation = abs(total - Fraction(1))
        max_normalisation_deviation = max(max_normalisation_deviation,
                                            deviation)
        per_n_results.append({
            "n": n,
            "n_factorial": n_fact,
            "num_partitions": len(per_lambda),
            "sum_of_squared_dims": sum(p["dim_V_lambda"] ** 2
                                        for p in per_lambda),
            "weights_sum_num": total.numerator,
            "weights_sum_den": total.denominator,
            "weights_sum_float": float(total),
            "normalisation_residue": float(deviation),
            "per_lambda": per_lambda,
        })

    (
        builder
        .set_description(
            "I1 probe for prop:plancherel-weight-boundedness.  "
            "Verifies (1) w_λ = (dim V_λ)² / n! ∈ [0, 1] and "
            "(2) Σ_{λ ⊢ n} w_λ = 1 exactly in ℚ for n = 1…8.  "
            "Uses integer/Fraction arithmetic on |SYT(λ)| counts; "
            "the identity Σ_λ f_λ² = n! is the classical Frobenius/"
            "Young dimension formula, lifted to H_n(q) via the "
            "Wedderburn-Artin decomposition (q-independent on the "
            "classical dimension)."
        )
        .set_content_block("prop:plancherel-weight-boundedness")
        .add_parameter("n_range_probed", f"{min(N_RANGE)}..{max(N_RANGE)}")
        .add_parameter("max_normalisation_deviation",
                       float(max_normalisation_deviation))
        .add_parameter("min_weight_seen_over_all_n",
                       float(min_weight_seen))
        .add_parameter("max_weight_seen_over_all_n",
                       float(max_weight_seen))
        .add_data("per_n_results", per_n_results)
        .add_assertion(
            name="all_plancherel_weights_in_unit_interval",
            computed=(0.0 if (0 <= min_weight_seen)
                       and (max_weight_seen <= 1) else 1.0),
            expected=0.0, tolerance=0.0,
            unit=(
                "boolean (0 = all w_λ ∈ [0,1] for n=1..8, 1 = some "
                "out of range)"
            ),
            source=(
                "Non-negativity from f_λ² ≥ 0; upper bound 1 since "
                "each summand is bounded by the sum."
            ),
        )
        .add_assertion(
            name="plancherel_weights_sum_exactly_one",
            computed=float(max_normalisation_deviation),
            expected=0.0, tolerance=0.0,
            unit=(
                "max over n ∈ {1,…,8} of |Σ_λ w_λ − 1|  (rational, "
                "exact)"
            ),
            source=(
                "Classical Frobenius dimension formula: "
                "n! = Σ_{λ ⊢ n} (dim V_λ)²."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'n':<3} {'n!':<10} {'# parts':<8} {'Σ dim²':<10} {'Σ w_λ':<25} {'deviation':<12}")
    for r in per_n_results:
        sum_str = f"{r['weights_sum_num']}/{r['weights_sum_den']}"
        print(f"  {r['n']:<3} {r['n_factorial']:<10} "
              f"{r['num_partitions']:<8} "
              f"{r['sum_of_squared_dims']:<10} {sum_str:<25} "
              f"{r['normalisation_residue']:<12.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
