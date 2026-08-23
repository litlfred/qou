#!/usr/bin/env python3
"""Probe: hecke-log-decomposition (`prop:hecke-log-decomposition`).

Verifies the algebraic identity

    log(1/h)  =  log(1/ℏ_q)  −  log(1 + q)

equivalent to the factorisation  h = ℏ_q · (q + 1),
where h = q − q⁻¹ (Hecke skein deformation) and
ℏ_q = (q − 1) / q (QOU quantum Planck constant).

Direct chain:  h = (q² − 1)/q = (q − 1)(q + 1)/q = ℏ_q · (q + 1).

Probe both the factorisation form and the log form at q = q_0 (and
at q = 2, q = 1.5 for sanity coverage at different q values).

Emits `hecke-log-decomposition-probe.witness.json`.
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

from mpmath import mp, log  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    builder = WitnessBuilder(
        "hecke-log-decomposition-probe",
        engine="mpmath",
    )
    set_compute_dps()

    test_q_values = [
        ("q_0 (substrate)", Q_MP),
        ("q = 1.5", mp.mpf("1.5")),
        ("q = 2", mp.mpf("2")),
    ]

    results = []
    max_factor_residue = mp.mpf(0)
    max_log_residue = mp.mpf(0)

    for label, q in test_q_values:
        h = q - 1 / q
        hbar_q = (q - 1) / q
        # Factorisation form: h = ℏ_q · (q + 1).
        factor_lhs = h
        factor_rhs = hbar_q * (q + 1)
        factor_residue = mp.fabs(factor_lhs - factor_rhs)
        # Log form: log(1/h) = log(1/ℏ_q) − log(1 + q).
        log_lhs = log(1 / h)
        log_rhs = log(1 / hbar_q) - log(1 + q)
        log_residue = mp.fabs(log_lhs - log_rhs)

        max_factor_residue = max(max_factor_residue,
                                  mp.mpf(factor_residue))
        max_log_residue = max(max_log_residue, mp.mpf(log_residue))

        results.append({
            "label": label,
            "q": float(q),
            "h": float(h),
            "hbar_q": float(hbar_q),
            "factorisation_residue": factor_residue,
            "log_form_residue": log_residue,
        })

    (
        builder
        .set_description(
            "I1 probe for prop:hecke-log-decomposition.  Verifies "
            "h = ℏ_q · (q + 1) and equivalently "
            "log(1/h) = log(1/ℏ_q) − log(1 + q), at three q values "
            "{q_0, 1.5, 2.0}.  h = q − q⁻¹ is the Hecke skein "
            "deformation; ℏ_q = (q − 1)/q is the QOU quantum Planck "
            "constant.  All residues at ~1e-50 (mpmath 50 dps)."
        )
        .set_content_block("prop:hecke-log-decomposition")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("max_factorisation_residue",
                       float(max_factor_residue))
        .add_parameter("max_log_form_residue",
                       float(max_log_residue))
        .add_data("per_q_value_results", results)
        .add_assertion(
            name="factorisation_h_equals_hbar_q_times_q_plus_1",
            computed=float(max_factor_residue),
            expected=0.0, tolerance=1e-40,
            unit="max over {q_0, 1.5, 2} of |h − ℏ_q · (q+1)|",
            source=(
                "Direct algebraic chain: h = (q²−1)/q "
                "= (q−1)(q+1)/q = ℏ_q · (q+1)."
            ),
        )
        .add_assertion(
            name="log_decomposition_identity",
            computed=float(max_log_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over {q_0, 1.5, 2} of "
                "|log(1/h) − log(1/ℏ_q) + log(1+q)|"
            ),
            source=(
                "Taking log of the factorisation: "
                "log(1/h) = log(1/(ℏ_q·(q+1))) = log(1/ℏ_q) − log(1+q)."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'test':<25} {'q':<10} {'h':<15} {'ℏ_q':<15} {'factor_res':<12} {'log_res':<12}")
    for r in results:
        print(f"  {r['label']:<23} {r['q']:<10.6f} "
              f"{r['h']:<15.10f} {r['hbar_q']:<15.10f} "
              f"{r['factorisation_residue']:<12.2e} "
              f"{r['log_form_residue']:<12.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
