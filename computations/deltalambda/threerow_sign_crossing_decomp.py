#!/usr/bin/env python3
"""threerow_sign_crossing_decomp.py — which ≥3-row partitions drive the deuteron
sign crossing of F_D(q)=Σ_{λ⊢6,ℓ≥3} y_λ(q)·χ^λ(β_D;q)·Δ_λ?

Companion decomposition to threerow_sign_crossing_probe.py. Prints the per-λ
term y_λ·χ^λ·Δ_λ at q→1⁺ and at q₀ (proton anchor) so the structural cause of
the crossing (which block flips / which competition tips) is visible. Audit-only.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

sys.path[:0] = [
    str(Path(__file__).resolve().parent.parent),
    str(Path(__file__).resolve().parent.parent / "substrate"),
    str(Path(__file__).resolve().parent.parent / "hecke"),
]
import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402

from threerow_sign_crossing_probe import (  # noqa: E402
    chi_atom, delta_lambda, Q0, Q_LO,
)
from schur_principal_mpmath import y_lambda_at_q0_mpmath, partitions_of  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

warnings.filterwarnings("ignore")
set_compute_dps()


def decomp(Z, N, name):
    n = 3 * (Z + N)
    print(f"\n=== {name}  n={n}  per-λ term y_λ·χ^λ·Δ_λ  (ℓ(λ)≥3) ===")
    print(f"{'λ':22s} {'Δ_λ':>6} {'term(q_lo)':>14} {'term(q₀)':>14}")
    y_lo = y_lambda_at_q0_mpmath(n, Q_LO)
    y_0 = y_lambda_at_q0_mpmath(n, Q0)
    tlo = t0 = mp.mpf(0)
    rows = []
    for lam in partitions_of(n):
        if len(lam) < 3:
            continue
        dl = delta_lambda(lam)
        a = y_lo[lam] * chi_atom(lam, Z, N, Q_LO) * dl
        b = y_0[lam] * chi_atom(lam, Z, N, Q0) * dl
        tlo += a
        t0 += b
        rows.append((lam, dl, float(a), float(b)))
    rows.sort(key=lambda r: -abs(r[3]))
    for lam, dl, a, b in rows:
        print(f"{str(lam):22s} {dl:>6d} {a:>14.5e} {b:>14.5e}")
    print(f"{'TOTAL':22s} {'':>6} {float(tlo):>14.5e} {float(t0):>14.5e}")


if __name__ == "__main__":
    decomp(1, 1, "D")
