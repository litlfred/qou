#!/usr/bin/env python3
"""
Per-braid HYBRID + Coulomb correction (term 3 of SEMF probe).

Replaces the q=1 MN per-pair traces in `per_braid_tower_hybrid`'s
cross tower with q-Hecke per-pair traces. The q-Hecke pair traces
distinguish pp/pn/nn (q=1 MN gives identical 0.0156 for all three;
q-Hecke gives 0.0660 / 0.0419 / 0.0255 respectively — 27% relative
diff between pp and nn).

The single-nucleon (per-nucleon) tower stays at q=1 MN to preserve
linear-in-A scaling (per per_braid_tower_hybrid.py docstring).

Hypothesis: replacing q=1 MN pairs with q-Hecke pairs gives the
proton-proton Coulomb-like enhancement automatically. Test if
this improves cal/m_e at heavy atoms (especially 16O, 40Ca where
Coulomb contribution is largest).

Witness: docs/audits/2026-05-02-per-braid-coulomb.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import (
    per_braid_mass_hybrid, _safe_phi, _cached_sub_braid_trace,
    q0, qi0, z_mark, M_E_MEV, AME_MASS_MEV
)
from schur_weyl_q_hecke_v2 import markov_trace_q_hecke_atomic
from q_parameter import Q as Q0_FLOAT


# Cache q-Hecke per-pair traces (atom-independent, computed once).
_QHECKE_PAIR_CACHE: dict[tuple, mpmath.mpf] = {}


def _qhecke_pair_trace(Z_sub: int, N_sub: int) -> mpmath.mpf:
    """|tr_M^{q-Hecke}(2-strand sub-braid)| — cached."""
    key = (Z_sub, N_sub)
    if key in _QHECKE_PAIR_CACHE:
        return _QHECKE_PAIR_CACHE[key]
    v, _ = markov_trace_q_hecke_atomic(Z_sub, N_sub,
                                         include_inter=True, dim_cap=5000)
    out = abs(v)
    _QHECKE_PAIR_CACHE[key] = out
    return out


def per_braid_mass_coulomb(Z: int, N: int) -> dict:
    """Hybrid + Coulomb: q-Hecke per-pair traces in cross tower.

    - Level-0 descended: q-Hecke (unchanged from per_braid_mass_hybrid)
    - Single-nucleon tower: q=1 MN (preserves linear-in-A)
    - Pair tower: q-Hecke (distinguishes pp/nn/pn — Coulomb-aware)
    """
    A = Z + N

    # Descended (q-Hecke) and single-nucleon (q=1 MN) — same as hybrid
    base = per_braid_mass_hybrid(Z, N)
    desc = base["desc_q_hecke"]
    single = base["single"]

    # NEW: pair tower with q-Hecke per-pair traces
    n_pp = Z * (Z - 1) // 2
    n_nn = N * (N - 1) // 2
    n_pn = Z * N

    cross = mpmath.mpf(0)
    if n_pp > 0:
        tr_pp = _qhecke_pair_trace(2, 0)
        cross += n_pp * _safe_phi(tr_pp)
    if n_nn > 0:
        tr_nn = _qhecke_pair_trace(0, 2)
        cross += n_nn * _safe_phi(tr_nn)
    if n_pn > 0:
        tr_pn = _qhecke_pair_trace(1, 1)
        cross += n_pn * _safe_phi(tr_pn)
    cross *= z_mark ** 2

    total = desc + single + cross

    return {
        "Z": Z, "N": N, "A": A,
        "desc": desc,
        "single": single,
        "cross_qhecke": cross,
        "cross_q1_mn": base["cross"],
        "total": total,
        "total_q1_mn_pair": base["total"],
    }


if __name__ == "__main__":
    print("=" * 100)
    print("Per-braid Coulomb correction — q-Hecke per-pair traces")
    print("=" * 100)
    print(f"q_0 = {q0}")
    print(f"m_e = {M_E_MEV} MeV")
    print()

    # Pre-show the q-Hecke pair traces vs q=1 MN
    print("Per-pair traces (q-Hecke vs q=1 MN):")
    for label, Z_s, N_s in [("pp", 2, 0), ("nn", 0, 2), ("pn", 1, 1)]:
        qh = _qhecke_pair_trace(Z_s, N_s)
        q1 = _cached_sub_braid_trace(Z_s, N_s, True)
        print(f"  {label}: q-Hecke={float(qh):.6f}  q=1 MN={float(q1):.6f}  "
              f"ratio={float(qh/q1):.3f}")
    print(f"  pp/nn ratio (Coulomb-distinguishing): "
          f"{float(_qhecke_pair_trace(2,0)/_qhecke_pair_trace(0,2)):.3f}")
    print()

    ATOMS = [
        ("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2),
        ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5),
        ("12C", 6, 6), ("16O", 8, 8), ("40Ca", 20, 20),
    ]

    print(f"  {'atom':>5} {'A':>3} {'level0 q1':>12} {'level0 +Cb':>12} "
          f"{'AME':>12} {'cal/m_e q1':>12} {'cal/m_e +Cb':>12} {'Δppm':>9}")
    print("  " + "-" * 92)
    rows = []
    ratios_q1 = []
    ratios_cb = []
    for name, Z, N in ATOMS:
        out = per_braid_mass_coulomb(Z, N)
        ame = AME_MASS_MEV[name]
        total_q1 = float(out["total_q1_mn_pair"])
        total_cb = float(out["total"])
        cal_q1 = (ame / total_q1) / M_E_MEV
        cal_cb = (ame / total_cb) / M_E_MEV
        ratios_q1.append(cal_q1)
        ratios_cb.append(cal_cb)
        delta_ppm = (cal_cb - cal_q1) * 1e6
        print(f"  {name:>5} {Z+N:>3} {total_q1:>12.4e} {total_cb:>12.4e} "
              f"{ame:>12.4f} {cal_q1:>12.6f} {cal_cb:>12.6f} {delta_ppm:>+9.1f}")
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": Z + N,
            "level0_q1_total": total_q1,
            "level0_coulomb_total": total_cb,
            "ame_mass_mev": ame,
            "cal_over_me_q1": cal_q1,
            "cal_over_me_coulomb": cal_cb,
            "delta_ppm": delta_ppm,
        })

    mean_q1 = sum(ratios_q1) / len(ratios_q1)
    mean_cb = sum(ratios_cb) / len(ratios_cb)
    spread_q1 = (max(ratios_q1) - min(ratios_q1)) / mean_q1 * 100
    spread_cb = (max(ratios_cb) - min(ratios_cb)) / mean_cb * 100
    print()
    print(f"  q=1 MN pair    : mean cal/m_e = {mean_q1:.6f}  spread = {spread_q1:.4f}%")
    print(f"  q-Hecke pair   : mean cal/m_e = {mean_cb:.6f}  spread = {spread_cb:.4f}%")
    print(f"  Δ spread       : {spread_cb - spread_q1:+.4f}%")
    print()

    out_path = (Path(__file__).parent.parent.parent
                / "docs/audits/2026-05-02-per-braid-coulomb.witness.json")
    out_path.write_text(json.dumps({
        "audit": "Per-braid + Coulomb (q-Hecke per-pair traces)",
        "generated": datetime.now(timezone.utc).isoformat(),
        "q_0": str(q0),
        "m_e_mev": M_E_MEV,
        "qhecke_pair_traces": {
            "pp": float(_qhecke_pair_trace(2, 0)),
            "nn": float(_qhecke_pair_trace(0, 2)),
            "pn": float(_qhecke_pair_trace(1, 1)),
        },
        "atoms": rows,
        "mean_cal_q1": mean_q1, "mean_cal_coulomb": mean_cb,
        "spread_q1_pct": spread_q1, "spread_coulomb_pct": spread_cb,
        "spread_change_pct": spread_cb - spread_q1,
        "interpretation": (
            "Replace q=1 MN per-pair traces with q-Hecke per-pair "
            "traces in the cross tower. q-Hecke distinguishes "
            "pp/pn/nn (q=1 MN does not). Tests SEMF Coulomb term as "
            "a structural feature of q-Hecke."
        ),
    }, indent=2, default=str))
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
