#!/usr/bin/env python3
"""
probe_d_dressing_cross_a.py — cross-A discriminator for the (1−h/2)
dressing (owner pick #1 follow-through, 2026-07-04, PR #3266).

EXPLORATORY (probe_ prefix, audit-only). The exact reduction
(probe_d_qbeta_h_invariant) established: Δ_λ(D) = 1/h ⟺
B_D = E₀·(1−h/2)·Δtr, taking the trace-canonical D route from +11.99%
to +0.29%. Before ANY derivation attempt of the dressing, the
formalize-first discipline demands the cheap decisive discriminator:
does the SAME dressing help at A ≥ 3 on the same transfer trace, or is
it D-specific?

Fixed a-priori candidate set (no fitting — each is a closed form named
before the run):

  C0  undressed          B = E₀·Δtr
  C1  flat dressing      B = E₀·(1−h/2)·Δtr
                         (one smoothed bar-averaged crossing, A-blind)
  C2  per-interface      B = E₀·(1−h/2)^(A−1)·Δtr
                         (one dressing per chain interface)

Discriminating logic:
  — if only D improves and A≥3 stays far off under every candidate, the
    dressing is the A=2 SCALE fix and the extensive A≥3 gap is a
    separate mechanism (consistent with the intensive-vs-extensive
    audit + the jet-filtration extensive channel, PR #3270);
  — if C2 tracks A≥3 better than C1, the dressing is per-interface
    structural (supports the σ_avg = σ−h/2 interface reading);
  — known ceiling: the trace difference SATURATES at A≥3 (derived
    growth 1.65× vs AME 12.72×), so no scalar dressing can close A≥3 —
    the probe measures the shape, it cannot wire anything.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
warnings.filterwarnings("ignore")

import mpmath as mp  # noqa: E402

DPS = 50
mp.mp.dps = DPS + 10

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
)
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

ATOMS = (
    ("D", 1, 1, AME_B_DEUTERON_MEV_VALIDATION),
    ("T", 1, 2, AME_B_TRITIUM_MEV_VALIDATION),
    ("3He", 2, 1, AME_B_HE3_MEV_VALIDATION),
    ("4He", 2, 2, AME_B_HE4_MEV_VALIDATION),
)


def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf(str(M_E_MEV))
    h = q - 1 / q
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    dress = 1 - h / 2

    print("=" * 76)
    print("CROSS-A DISCRIMINATOR for the (1−h/2) dressing "
          "(trace-canonical transfer path)")
    print("=" * 76)
    print(f"  E₀ = {mp.nstr(E0, 10)} MeV   (1−h/2) = {mp.nstr(dress, 10)}")
    print(f"  {'atom':5s}{'A':>3s}{'Δtr':>12s}{'B_AME':>9s}"
          f"{'C0 undress':>12s}{'err':>8s}{'C1 flat':>10s}{'err':>8s}"
          f"{'C2 per-ifc':>11s}{'err':>8s}")

    rows = []
    for name, Z, N, B_ame in ATOMS:
        A = Z + N
        ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=DPS)
        dtr = mp.mpf(tf) - mp.mpf(ta)
        B_ame = mp.mpf(str(B_ame))
        c0 = E0 * dtr
        c1 = E0 * dress * dtr
        c2 = E0 * dress ** (A - 1) * dtr
        row = {
            "atom": name, "Z": Z, "N": N, "A": A,
            "Delta_tr": mp.nstr(dtr, 25),
            "B_AME_MeV": mp.nstr(B_ame, 15),
            "C0_undressed_MeV": mp.nstr(c0, 15),
            "C0_err_rel": float(c0 / B_ame - 1),
            "C1_flat_MeV": mp.nstr(c1, 15),
            "C1_err_rel": float(c1 / B_ame - 1),
            "C2_per_interface_MeV": mp.nstr(c2, 15),
            "C2_err_rel": float(c2 / B_ame - 1),
        }
        rows.append(row)
        print(f"  {name:5s}{A:>3d}{mp.nstr(dtr, 6):>12s}"
              f"{float(B_ame):>9.3f}"
              f"{float(c0):>12.4f}{row['C0_err_rel']*100:>+7.1f}%"
              f"{float(c1):>10.4f}{row['C1_err_rel']*100:>+7.1f}%"
              f"{float(c2):>11.4f}{row['C2_err_rel']*100:>+7.1f}%")

    d_row = rows[0]
    a3_best = min(abs(r["C1_err_rel"]) for r in rows[1:])
    verdict = (
        "D-SPECIFIC SCALE FIX: the (1−h/2) dressing closes D to "
        f"{d_row['C1_err_rel']*100:+.2f}% but the best A≥3 candidate "
        f"error remains {a3_best*100:.0f}% — the A≥3 gap is the known "
        "saturating-Δtr (extensive) deficit, NOT the scale. Scope (a): "
        "constrains scalar dressings on this route only."
        if a3_best > 0.15 else
        "dressing helps cross-A — per-interface structural reading "
        "survives; escalate to derivation."
    )
    print(f"\n  VERDICT: {verdict}")

    wb = (WitnessBuilder("probe-d-dressing-cross-a", engine="mpmath")
          .set_description(
              "Cross-A discriminator for the (1−h/2) dressing on the "
              "trace-canonical transfer path: fixed a-priori candidates "
              "C0 undressed / C1 flat / C2 per-interface, evaluated at "
              "D, T, ³He, ⁴He vs AME2020. Derive-or-refute; nothing "
              "wired (Δ_λ gate).")
          .set_audit_only(
              "docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md")
          .add_parameter("q0", Q_50_DIGIT_STR)
          .add_parameter("compute_dps", DPS)
          .add_parameter("dressing", "(1 - h/2), h = q - 1/q")
          .add_data("rows", rows)
          .add_data("verdict", verdict))
    wb.add_assertion(
        "deuteron_dressed_subpercent",
        computed=abs(d_row["C1_err_rel"]) < 0.005, expected=True,
        source="exact reduction check: C1 at D must reproduce the "
               "+0.29% of probe_d_qbeta_h_invariant")
    wb.save()
    print("\nwitness → probe-d-dressing-cross-a.witness.json (audit-only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
