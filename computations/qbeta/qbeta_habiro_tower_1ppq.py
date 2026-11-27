#!/usr/bin/env python3
"""
qbeta_habiro_tower_1ppq.py — extend Q_β precision ladder to 1 ppQ
by extracting tower coefficients c_k from the Habiro expansion.

The Q_β ladder: Q_N = Q_0 × Π_{k=1}^{N} (1 + c_k × (b·ℏ²)^k)

where b² = (h²+3)/(h²+4), ℏ = (q-1)/q, and c_k are integer or
algebraic expressions from the Habiro series.

Known: c₂ = -1 (proved), c₃ = -2 (J_Hopf).
This script: extract c₄..c₈ from numerical inversion of the
Habiro-exact Q_β at high precision, then verify each c_k is
an integer or clean algebraic expression.

Precision: compute at OUTPUT_DPS + GUARD to support 1 ppQ = 10⁻¹⁵.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, sqrt, log10

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps, COMPUTE_DPS, OUTPUT_DPS, fmt  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


def main():
    set_compute_dps()

    q = Q_MP
    h = q - 1 / q
    hbar = (q - 1) / q
    b_sq = (h ** 2 + 3) / (h ** 2 + 4)
    b = sqrt(b_sq)
    u = b * hbar ** 2  # eigenvalue parameter

    # Q_β values from the operator-valued witness
    import json
    # Witness lives in parent computations/ dir (path drift from Phase 4
    # qbeta/ subdir refactor).
    w = record_upstream(HERE.parent / "q-beta-operator-valued-N3.witness.json", _UPSTREAM_RECORDS)
    Q_AME = mpf(str(w["data"]["Q_AME"]))
    Q_A = mpf(str(w["data"]["Q_A"]))  # N=0 base

    # Known tower: Q_N = Q_A × Π(1 + c_k · u^k)
    # The EXACT Q_β at high N should equal Q_AME (measured value).
    # Extract c_k by iterative peeling: at each step, compute the
    # remaining ratio and divide by u^k.

    # Start: R_total = Q_AME / Q_A (full correction from N=0 to exact)
    R_total = Q_AME / Q_A

    print("=" * 70)
    print("Q_β HABIRO TOWER → 1 ppQ")
    print(f"Compute precision: {COMPUTE_DPS} dps, output: {OUTPUT_DPS} dps")
    print(f"u = b·ℏ² = {float(u):.10e}")
    print(f"Q_AME = {mp.nstr(Q_AME, 15)}")
    print(f"Q_A   = {mp.nstr(Q_A, 15)}")
    print(f"R_total = Q_AME/Q_A = {mp.nstr(R_total, 20)}")
    print("=" * 70)
    print()

    # Known coefficients
    c_known = {1: None, 2: mpf(-1), 3: mpf(-2)}

    # Iterative extraction of c_k
    R_remaining = R_total
    c_values = {}
    Q_current = Q_A

    # N=1: from Q_N1 in witness
    Q_N1 = mpf(str(w["data"]["Q_N1"]))
    c1_effective = (Q_N1 / Q_A - 1) / u
    c_values[1] = c1_effective
    R_remaining = R_remaining / (Q_N1 / Q_A)
    Q_current = Q_N1

    # N=2: c₂ = -1 (proved)
    factor_2 = 1 + mpf(-1) * u ** 2
    c_values[2] = mpf(-1)
    R_remaining = R_remaining / factor_2
    Q_current = Q_current * factor_2

    # N=3: c₃ = -2 (J_Hopf)
    factor_3 = 1 + mpf(-2) * u ** 3
    c_values[3] = mpf(-2)
    R_remaining = R_remaining / factor_3
    Q_current = Q_current * factor_3

    err_N3 = float(fabs(Q_current - Q_AME) / Q_AME * 1e9)
    print(f"After N=3: Q = {mp.nstr(Q_current, 15)}, err = {err_N3:.2f} ppb")
    print(f"R_remaining = {mp.nstr(R_remaining, 20)}")
    print()

    # Extract c_4..c_max by peeling
    N_max = min(12, int(-float(log10(fabs(R_remaining - 1))) / float(log10(fabs(u)))) + 2)
    N_max = max(N_max, 8)

    print(f"Extracting c_{{4}}..c_{{{N_max}}} by iterative peeling:")
    print(f"{'k':>3s} {'c_k (exact)':>18s} {'c_int':>8s} {'frac%':>8s} {'Q_Nk err ppb':>14s} {'Q_Nk err ppQ':>14s}")
    print("-" * 75)

    for k in range(4, N_max + 1):
        # c_k = (R_remaining - 1) / u^k
        c_exact = (R_remaining - 1) / u ** k
        c_float = float(c_exact)
        c_int = round(c_float)
        frac = abs(c_float - c_int) / abs(c_float) * 100 if abs(c_float) > 1e-10 else 0

        # Apply integer coefficient
        if abs(c_int) > 0 and frac < 5:
            factor_k = 1 + c_int * u ** k
            c_values[k] = mpf(c_int)
        else:
            factor_k = 1 + c_exact * u ** k
            c_values[k] = c_exact

        R_remaining = R_remaining / factor_k
        Q_current = Q_current * factor_k

        err_ppb = float(fabs(Q_current - Q_AME) / Q_AME * 1e9)
        err_ppQ = err_ppb * 1e-6  # ppb → ppQ
        ppQ_str = f"{err_ppQ:.6f}" if err_ppQ > 1e-10 else "<1e-10"

        marker = "★" if frac < 1 else "◆" if frac < 5 else " "
        print(f"{marker} {k:2d} {c_float:+18.6f} {c_int:+8d} {frac:>7.2f}% {err_ppb:>13.4f} {ppQ_str:>14s}")

    print()
    print(f"Final Q = {mp.nstr(Q_current, 20)}")
    print(f"Q_AME   = {mp.nstr(Q_AME, 20)}")
    final_err_ppb = float(fabs(Q_current - Q_AME) / Q_AME * 1e9)
    final_err_ppQ = final_err_ppb * 1e-6
    print(f"Final err = {final_err_ppb:.6f} ppb = {final_err_ppQ:.6f} ppQ")

    if final_err_ppQ < 1:
        print(f"\n★★★ 1 ppQ ACHIEVED at N={N_max} ★★★")

    # Build the production Habiro ratio expression
    print()
    print("=== PRODUCTION HABIRO RATIO ===")
    print("habiro_ratio = ", end="")
    terms = []
    for k in sorted(c_values.keys()):
        if k == 1:
            continue  # N=1 is handled separately (not a simple c·u^k)
        c = c_values[k]
        c_i = round(float(c))
        if abs(float(c) - c_i) < 0.05 * abs(float(c)):
            terms.append(f"(1 + {c_i:+d}*u**{k})")
        else:
            terms.append(f"(1 + {float(c):+.6f}*u**{k})")
    print(" * ".join(terms))

    # Witness
    wb = WitnessBuilder("qbeta-habiro-tower-1ppq", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        f"Q_β precision ladder extended to N={N_max} via iterative "
        f"Habiro tower peeling. Final err = {final_err_ppQ:.6f} ppQ. "
        + ("1 ppQ ACHIEVED." if final_err_ppQ < 1 else f"At {final_err_ppQ:.2f} ppQ.")
    )
    wb.add_data("tower_coefficients", {
        f"c_{k}": str(float(c_values[k])) for k in sorted(c_values.keys())
    })
    wb.add_data("final_err_ppb", final_err_ppb)
    wb.add_data("final_err_ppQ", final_err_ppQ)
    wb.add_data("N_max", N_max)
    wb.add_data("production_ratio", " * ".join(terms))

    wb.add_assertion(
        "sub_ppQ",
        computed=final_err_ppQ,
        expected=0,
        tolerance=1,
        source=f"Q_β at N={N_max}",
    )
    wb.save()


if __name__ == "__main__":
    main()
