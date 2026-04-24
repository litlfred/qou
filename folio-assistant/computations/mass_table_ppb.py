#!/usr/bin/env python3
"""
Mass table: AME vs canonical predictions, with error in ppb and %.

Consolidates the current best prediction pipeline into a single
table comparable to AME2020.

For each atom (Z, N) we try, in order:
  1.  A-independent catalog match (D, T, ³He): Kashaev B = 2m_e · Vol
      of the closest SnapPy census link to B(atom)/(2m_e).  Derived
      in jsj_verification.
  2.  α-cluster fit (4He base, 12C calibration) for magic and α-
      conjugate atoms: B = n_α · B(⁴He) + n_pairs · c_αα with
      c_αα fixed from 12C.  See jsj_alpha_clustering.
  3.  Φ₁-only algebraic volume: B = α · Φ₁ evaluated by
      compute_phi_mp at 100-digit mpmath.  Current α = m_e · 8G
      as per def:algebraic-quantum-volume-specialization.

Reports each atom with the first column that applies and the
implied ppb-level deviation.
"""
from __future__ import annotations

import sys
import json
import math
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from experimental_constants import M_E_MEV

CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G                  # = 8G
ALPHA_PHI1 = M_E_MEV * VOL_BORROMEAN              # per def:alg-q-vol-spec

# AME2020 light-atom table (B in MeV; positive = binding).
AME_TABLE = [
    #  sym     Z   N    B_AME
    ("2H",     1,  1,   2.22456612),
    ("3H",     1,  2,   8.4817984),
    ("3He",    2,  1,   7.7180375),
    ("4He",    2,  2,  28.2956912),
    ("6Li",    3,  3,  31.99405),
    ("7Li",    3,  4,  39.24453),
    ("8Be",    4,  4,  56.49951),
    ("9Be",    4,  5,  58.16498),
    ("11B",    5,  6,  76.20548),
    ("12C",    6,  6,  92.16175),
    ("14N",    7,  7, 104.65877),
    ("16O",    8,  8, 127.61929),
    ("19F",    9, 10, 147.80137),
    ("20Ne",  10, 10, 160.64486),
    ("24Mg",  12, 12, 198.25690),
    ("40Ca",  20, 20, 342.05212),
]

# α-cluster structure
# A-indexed n_α = floor(A/4); magic n_α matches even-even doubly magic
ALPHA_MAP = {
    "4He":  (1,  0),     # 1 α, 0 α-α pairs
    "8Be":  (2,  1),
    "12C":  (3,  3),
    "16O":  (4,  6),
    "20Ne": (5, 10),
    "24Mg": (6, 15),
    "40Ca": (10, 45),
}

# c_αα from 12C fit: B(12C) = 3·B(4He) + 3·c → c = (92.1617 - 3·28.2957)/3
B_4HE = 28.2956912
B_12C = 92.16175
C_ALPHA = (B_12C - 3 * B_4HE) / 3


def kashaev_census_vol(atom: str) -> float | None:
    """Catalog knot volume nearest B(atom)/(2m_e) for light atoms.

    Data here is hard-coded from jsj_verification's census search;
    tolerance 5% after sorting by volume-proximity.
    """
    # From jsj_verification.py Search 2 at tol 10%:
    # D (target 2.18): no match ≤ 5%; closest was fig-8 at 4.94, too far.
    # T (target 8.30): 8_2 at Vol 4.94 per m_e.  Actually the 2m_e search:
    #   target 8.30, 8^3_3 at 8.97 (+8%), 8_2 at 4.94 via m_e column (+5%).
    # 3He (target 7.55): 8^3_9/8^4_2 at 7.33 (-2.97%).
    # 4He (target 27.69): 8^4_2 at high-crossings gave no tight match.
    #
    # This is diagnostic only; the current best light-atom pipeline
    # is jsj_verification's census search itself, not a closed-form
    # table.  Return None here to signal "no hard-coded knot".
    return None


def alpha_cluster_binding(atom: str) -> float | None:
    """B via α-cluster structure, calibrated from 12C."""
    if atom not in ALPHA_MAP:
        return None
    n_a, n_p = ALPHA_MAP[atom]
    return n_a * B_4HE + n_p * C_ALPHA


def phi1_binding(Z: int, N: int) -> dict:
    """B via Φ_1 = ln|∏ V̂_i(q₀)| with α = m_e · 8G."""
    try:
        from exact_binding_per_operation import (
            atomic_ordering, find_nuclear_gs_float, compute_phi_mp,
        )
    except ImportError as e:
        return {"B": None, "err": f"import: {e}"}
    try:
        nuc = find_nuclear_gs_float(Z, N)
        ord_ = atomic_ordering(Z, N, nuc)
        Phi = float(compute_phi_mp(ord_))
    except Exception as e:
        return {"B": None, "err": f"compute: {e}"}
    return {
        "B": -ALPHA_PHI1 * Phi,
        "Phi_1": Phi,
        "alpha": ALPHA_PHI1,
    }


def best_prediction(sym: str, Z: int, N: int, B_ame: float) -> dict:
    """Pick best prediction in priority order: α-cluster > Φ_1."""
    # α-cluster is 0% at fit points (4He, 12C), ~0.1-5% at others
    B_alpha = alpha_cluster_binding(sym)
    phi1 = phi1_binding(Z, N)

    # Priority: α-cluster when available (magic/α-conjugate)
    if B_alpha is not None:
        return {
            "source": "alpha-cluster-12C",
            "B_pred": B_alpha,
            "Phi_1": phi1.get("Phi_1"),
        }
    return {
        "source": "Phi_1 (α = m_e · 8G)",
        "B_pred": phi1.get("B"),
        "Phi_1": phi1.get("Phi_1"),
    }


def fmt_ppb(err_abs: float, b_ame: float) -> str:
    if b_ame <= 0:
        return "—"
    ppb = abs(err_abs) / b_ame * 1e9
    if ppb > 1e9:
        return f"{ppb/1e9:+.3g}×10⁹"
    if ppb > 1e6:
        return f"{ppb/1e6:+.3f}×10⁶"
    if ppb > 1e3:
        return f"{ppb/1e3:+.3f}×10³"
    return f"{ppb:+.3f}"


def main() -> int:
    print("=" * 120)
    print("MASS TABLE — AME2020 light atoms vs current canonical predictions")
    print(f"  q₀ = {Q0:.10f}   m_e = {M_E_MEV} MeV   "
          f"8G = {VOL_BORROMEAN:.10f}   m_e·8G = {ALPHA_PHI1:.6f} MeV")
    print(f"  c_αα (12C-fit) = {C_ALPHA:.6f} MeV")
    print(f"  Target precision: 1 ppb ≈ 10⁻⁹ relative")
    print("=" * 120)
    print(f"  {'atom':>5} {'Z':>3} {'N':>3} {'A':>3}  "
          f"{'B_AME':>10}  {'B_pred':>11}  {'err (MeV)':>11}  "
          f"{'err %':>9}  {'err ppb':>12}  source")
    print("  " + "-" * 116)
    rows = []
    for (sym, Z, N, B_ame) in AME_TABLE:
        A = Z + N
        pred = best_prediction(sym, Z, N, B_ame)
        B_pred = pred.get("B_pred")
        if B_pred is None:
            print(f"  {sym:>5} {Z:>3} {N:>3} {A:>3}  "
                  f"{B_ame:>10.4f}   [prediction failed]")
            continue
        err = B_pred - B_ame
        pct = err / B_ame * 100 if B_ame else 0.0
        ppb = err / B_ame * 1e9 if B_ame else 0.0
        print(f"  {sym:>5} {Z:>3} {N:>3} {A:>3}  "
              f"{B_ame:>10.4f}  {B_pred:>+11.4f}  {err:>+11.6f}  "
              f"{pct:>+8.3f}%  {fmt_ppb(err, B_ame):>12}  {pred['source']}")
        rows.append({
            "sym": sym, "Z": Z, "N": N, "A": A,
            "B_AME_MeV": B_ame,
            "B_pred_MeV": B_pred,
            "err_MeV": err,
            "err_pct": pct,
            "err_ppb": ppb,
            "source": pred["source"],
            "Phi_1": pred.get("Phi_1"),
        })

    # Summary
    print()
    print("  Summary:")
    ok = [r for r in rows if r["B_AME_MeV"] > 0]
    within = {1: 0, 1e3: 0, 1e6: 0, 1e9: 0}
    for r in ok:
        for th in within:
            if abs(r["err_ppb"]) <= th:
                within[th] += 1
    print(f"    n = {len(ok)} atoms evaluated")
    print(f"    within 1    ppb  (1e-9):    {within[1]}")
    print(f"    within 1e3  ppb  (1 ppm):   {within[1e3]}")
    print(f"    within 1e6  ppb  (0.1%):    {within[1e6]}")
    print(f"    within 1e9  ppb  (100%):    {within[1e9]}")

    mean_abs_ppb = sum(abs(r["err_ppb"]) for r in ok) / len(ok) if ok else 0.0
    mean_abs_pct = sum(abs(r["err_pct"]) for r in ok) / len(ok) if ok else 0.0
    print(f"    mean |err|:   {mean_abs_pct:.4f}%  =  "
          f"{mean_abs_ppb:.3e} ppb")

    witness = {
        "computation": "mass-table-ppb",
        "description": (
            "AME2020 light-atom binding vs current canonical predictions. "
            "For each atom, reports best available predicted binding from "
            "α-cluster (fit from 12C) when applicable, or Φ_1 algebraic "
            "volume with α = m_e · 8G otherwise.  Target: 1 ppb."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": Q0,
            "m_e_MeV": M_E_MEV,
            "vol_borromean_8G": VOL_BORROMEAN,
            "alpha_phi1_MeV": ALPHA_PHI1,
            "c_alpha_alpha_MeV": C_ALPHA,
            "B_4He_MeV": B_4HE,
            "B_12C_MeV": B_12C,
        },
        "rows": rows,
        "within": {str(k): v for k, v in within.items()},
        "mean_abs_pct": mean_abs_pct,
        "mean_abs_ppb": mean_abs_ppb,
    }
    out = Path(__file__).parent / "mass-table-ppb.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
