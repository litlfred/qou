#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; per-block magnitude probe.
"""Per-block-magnitude binding — does the operator-valued (don't-collapse-
blocks-before-|·|) form that closes the DEUTERON extend to A=3?

Two parameter-free readings of the canonical binding
`B = E_0·(tr_M(W_free) − tr_M(W_atom))` differ only in where the modulus
sits relative to the Wedderburn sum:

  scalar (collapse first):   B = E_0·( |Σ_λ y_λ χ^λ(free)| − |Σ_λ y_λ χ^λ(atom)| )
  per-block (operator-valued): B = E_0·( Σ_λ y_λ|χ^λ(free)| − Σ_λ y_λ|χ^λ(atom)| )

The scalar form gives the deuteron at −79 % (binding_canonical.py); the
per-block form gives +3.6 % (derive_binding_bar_pairing.py, #1742). The
per-block form is the operator-valued reading: each Wedderburn block
keeps its own archimedean magnitude before summing, so per-block phase
cancellation is not allowed to wipe out the binding. NO per-partition
Δ_λ is introduced — every factor (y_λ, χ^λ, E_0) is already derived.

This probe runs the per-block form for D, T, ³He at q₀ and reports the
residual vs AME. If A=3 lands near the deuteron's few-percent, the
operator-valued per-block magnitude is the parameter-free A≥3 closure.
EXPLORATORY: no fit; E_0 is the CAL-3 calibration used by binding_canonical.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_Path(__file__).resolve().parent / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401 — Phase-6 bridge

import mpmath as mp  # noqa: E402

from habiro_coefficients_interpolate import (  # noqa: E402
    chi_lambda_numerical, atomic_braid_to_crossings,
)
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from schur_weyl_symbolic import partitions_of  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = set_compute_dps()
q0 = mp.mpf(str(Q0))
M_E = mp.mpf(str(M_E_MEV))
E0 = M_E / (q0 * (q0 - 1))                      # 𝔈₀ ≈ 4.186 MeV (CAL-3)

ISO = {"D": (1, 1), "T": (1, 2), "3He": (2, 1)}
AME_B = {"D": mp.mpf("2.2245662"), "T": mp.mpf("8.4818"),
         "3He": mp.mpf("7.7180")}


def _per_block_mag(Z, N, inter):
    """Σ_λ y_λ(q₀)·|Re χ^λ(β; q₀)| — per-block (operator-valued) magnitude.

    Each Wedderburn block contributes its own |χ^λ|; blocks are NOT summed
    (with sign) before the modulus, so per-block phase cancellation cannot
    erase the binding. This is the form that closes the deuteron."""
    cr = atomic_braid_to_crossings(Z, N, include_inter=inter)
    total = mp.mpf(0)
    for lam in partitions_of(3 * (Z + N)):
        chi, d = chi_lambda_numerical(lam, q0, cr)
        if d == 0:
            continue
        y = y_lambda_wenzl_bridge_numeric(lam, q0, dps=DPS)
        total += mp.re(y) * abs(mp.re(chi))
    return total


def _scalar_mag(Z, N, inter):
    """|Σ_λ y_λ χ^λ| — scalar (collapse-first) magnitude, for contrast."""
    cr = atomic_braid_to_crossings(Z, N, include_inter=inter)
    s = mp.mpf(0)
    for lam in partitions_of(3 * (Z + N)):
        chi, d = chi_lambda_numerical(lam, q0, cr)
        if d == 0:
            continue
        y = y_lambda_wenzl_bridge_numeric(lam, q0, dps=DPS)
        s += mp.re(y) * mp.re(chi)
    return abs(s)


def main() -> int:
    print(f"E_0 = {float(E0):.4f} MeV   q₀ = {float(q0):.6f}   dps = {DPS}\n")
    print(f"{'iso':<5}{'B_perblock':<12}{'B_scalar':<12}{'AME':<9}"
          f"{'perblk err%':<13}{'scalar err%':<12}")
    results = {}
    for name, (Z, N) in ISO.items():
        Bp = E0 * (_per_block_mag(Z, N, False) - _per_block_mag(Z, N, True))
        Bs = E0 * (_scalar_mag(Z, N, False) - _scalar_mag(Z, N, True))
        ep = (Bp - AME_B[name]) / AME_B[name]
        es = (Bs - AME_B[name]) / AME_B[name]
        results[name] = {
            "B_perblock_MeV": float(Bp), "B_scalar_MeV": float(Bs),
            "AME_MeV": float(AME_B[name]),
            "err_perblock": float(ep), "err_scalar": float(es),
        }
        print(f"{name:<5}{float(Bp):<12.4f}{float(Bs):<12.4f}"
              f"{float(AME_B[name]):<9.4f}{float(ep)*100:<+13.1f}"
              f"{float(es)*100:<+12.1f}")

    wb = WitnessBuilder("binding-per-block-magnitude-a3", engine="mpmath")
    wb.data["E0_MeV"] = fmt = float(E0)
    wb.data["q_0"] = str(Q0)
    wb.data["results"] = results
    wb.data["formula_perblock"] = "B = E_0·(Σ_λ y_λ|χ^λ(free)| − Σ_λ y_λ|χ^λ(atom)|)"
    wb.data["note"] = (
        "Operator-valued per-block magnitude vs scalar collapse-first. "
        "No per-partition Δ_λ; E_0 is CAL-3. EXPLORATORY probe.")
    wb.add_assertion("deuteron_perblock_within_5pct",
                     computed=abs(results["D"]["err_perblock"]),
                     expected=0.0, tolerance=0.05)
    wb.save()
    print("\n✓ Witness: binding-per-block-magnitude-a3.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
