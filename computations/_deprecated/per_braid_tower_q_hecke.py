#!/usr/bin/env python3
"""
Per-braid mass tower with the q-deformed Hecke character (P2.2c v2).

Same per-braid stratification as `per_braid_tower.py`, but with
sub-braid traces computed via `schur_weyl_q_hecke_v2.markov_trace_q_hecke_atomic`
which evaluates χ^λ_q(c·σ + d·I) per crossing, distinguishing
proton from neutron.

Compares to AME atomic masses with m_e (H^0) calibration. Expectation:
- 3He vs 3H now produce different totals (was identical at q=1)
- Calibration spread tightens below 1.06%

Witness: docs/audits/2026-05-01-per-braid-q-hecke-vs-ame.witness.json
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from schur_weyl_q_hecke_v2 import markov_trace_q_hecke_atomic
from q_parameter import Q as Q0_FLOAT

mpmath.mp.dps = 50
q0 = mpmath.mpf(str(Q0_FLOAT))
qi0 = 1 / q0
z_mark = 1 / (q0 ** mpmath.mpf("0.5") + qi0 ** mpmath.mpf("0.5"))

M_E_MEV = 0.51099895000

AME_MASS_MEV = {
    "D":    1875.61294257,
    "3He":  2808.39148127,
    "3H":   2808.92113298,
    "4He":  3727.37909409,
    "12C": 11177.9292,
}


def _safe_phi(z, q=q0, qi=qi0, max_k=200):
    """Φ_q(z) = ∏(1 - q⁻ᵏz)⁻¹ at mpmath precision."""
    z_abs = abs(z)
    if z_abs >= q:
        return mpmath.inf
    product = mpmath.mpf(1)
    for k in range(1, max_k + 1):
        factor = 1 - qi ** k * z_abs
        if abs(factor) < mpmath.mpf("1e-300"):
            return mpmath.inf
        product /= factor
        term = qi ** k * z_abs
        if term < mpmath.mpf("1e-60"):
            break
    return product


def per_braid_mass_q_hecke(Z, N):
    """Per-braid mass tower with q-deformed Hecke character per sub-braid."""
    A = Z + N

    # Level 0: full atomic braid
    desc, _parts = markov_trace_q_hecke_atomic(Z, N, include_inter=True)
    desc = abs(desc)

    # Level 1: per-nucleon sub-braids (single-nucleon = H_3, no inter)
    tr_p = abs(markov_trace_q_hecke_atomic(1, 0, include_inter=False)[0]) if Z > 0 else mpmath.mpf(0)
    tr_n = abs(markov_trace_q_hecke_atomic(0, 1, include_inter=False)[0]) if N > 0 else mpmath.mpf(0)

    # Level 2: per-nucleon-pair sub-braids
    tr_pp = abs(markov_trace_q_hecke_atomic(2, 0, include_inter=True)[0]) if Z >= 2 else mpmath.mpf(0)
    tr_nn = abs(markov_trace_q_hecke_atomic(0, 2, include_inter=True)[0]) if N >= 2 else mpmath.mpf(0)
    tr_pn = abs(markov_trace_q_hecke_atomic(1, 1, include_inter=True)[0]) if Z >= 1 and N >= 1 else mpmath.mpf(0)

    # Single tower
    single = mpmath.mpf(0)
    if Z > 0 and tr_p > 0:
        single += Z * _safe_phi(tr_p)
    if N > 0 and tr_n > 0:
        single += N * _safe_phi(tr_n)

    # Pair tower
    cross = mpmath.mpf(0)
    n_pp = Z * (Z - 1) // 2
    n_nn = N * (N - 1) // 2
    n_pn = Z * N
    if n_pp > 0 and tr_pp > 0:
        cross += n_pp * _safe_phi(tr_pp)
    if n_nn > 0 and tr_nn > 0:
        cross += n_nn * _safe_phi(tr_nn)
    if n_pn > 0 and tr_pn > 0:
        cross += n_pn * _safe_phi(tr_pn)
    cross *= z_mark ** 2

    total = desc + single + cross
    return {
        "Z": Z, "N": N, "A": A,
        "desc": desc, "single": single, "cross": cross, "total": total,
        "tr_p": tr_p, "tr_n": tr_n,
        "tr_pp": tr_pp, "tr_nn": tr_nn, "tr_pn": tr_pn,
    }


print("=" * 88)
print("Per-braid q-Hecke vs AME — does (c, d) distinction tighten the calibration?")
print("=" * 88)
print(f"q_0 = {q0}")
print(f"m_e = {M_E_MEV} MeV")
print()

ATOMS = [("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2)]
# 12C deferred — partition dimensions at 36 strands explode
# (dim_(33,3) ≈ 6545, dim_(31,5) ≈ 257k); seminormal-matrix
# product through ~70 atomic-braid crossings is heavy. Tracked
# as P2.2c-12C.

print(f"  {'Atom':>5} {'A':>3} {'per-braid total':>16} {'AME (MeV)':>12} {'cal/m_e':>14}")
print("  " + "-" * 70)

results = []
ratios = []
for name, Z, N in ATOMS:
    t0 = time.time()
    out = per_braid_mass_q_hecke(Z, N)
    t = time.time() - t0
    total_f = float(out["total"])
    ame = AME_MASS_MEV[name]
    cal_constant = ame / total_f
    cal_over_me = cal_constant / M_E_MEV
    ratios.append(cal_over_me)
    print(f"  {name:>5} {Z+N:>3} {total_f:>16.6e} {ame:>12.4f} {cal_over_me:>14.10f}  ({t:.2f}s)")
    results.append({
        "atom": name, "Z": Z, "N": N, "A": Z + N,
        "per_braid_total": total_f,
        "ame_mass_mev": ame,
        "cal_over_me": cal_over_me,
        "trace_proton": str(out["tr_p"]),
        "trace_neutron": str(out["tr_n"]),
        "descended": str(out["desc"]),
        "single_tower": str(out["single"]) if not mpmath.isinf(out["single"]) else "inf",
        "cross_tower": str(out["cross"]) if not mpmath.isinf(out["cross"]) else "inf",
        "total": str(out["total"]) if not mpmath.isinf(out["total"]) else "inf",
        "time_seconds": t,
    })

mean_ratio = sum(ratios) / len(ratios)
spread = (max(ratios) - min(ratios)) / mean_ratio * 100
print()
print(f"  Mean cal/m_e = {mean_ratio:.6f} (spread {spread:.4f}%)")

# 3He vs 3H direct comparison
he3 = next((r for r in results if r["atom"] == "3He"), None)
h3 = next((r for r in results if r["atom"] == "3H"), None)
if he3 and h3:
    diff = abs(he3["per_braid_total"] - h3["per_braid_total"])
    rel = diff / max(he3["per_braid_total"], h3["per_braid_total"])
    physical_diff = abs(he3["ame_mass_mev"] - h3["ame_mass_mev"])
    print()
    print(f"  3He vs 3H per-braid totals:")
    print(f"    3He: {he3['per_braid_total']:.6f}")
    print(f"    3H : {h3['per_braid_total']:.6f}")
    print(f"    diff: {diff:.6f}  ({rel*100:.6f}% relative)")
    print(f"    physical 3H - 3He = {physical_diff:.4f} MeV (AME)")
    if diff > 1e-6:
        print(f"    ✅ q-Hecke per-braid SPLITS 3He from 3H")

witness = {
    "audit": "Per-braid q-Hecke vs AME",
    "generated": datetime.now(timezone.utc).isoformat(),
    "q_0": str(q0),
    "m_e_mev": M_E_MEV,
    "atoms": results,
    "mean_cal_over_me": mean_ratio,
    "spread_percent": spread,
    "interpretation": (
        "Per-braid mass tower with q-deformed Hecke character "
        "(distinguishes proton from neutron via per-crossing (c, d)). "
        "Compared to AME atomic masses with m_e calibration. "
        "Expected: 3He vs 3H now split; calibration spread tightens "
        "vs the q=1 MN baseline (1.06%)."
    ),
}
out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-per-braid-q-hecke-vs-ame.witness.json"
out_path.write_text(json.dumps(witness, indent=2, default=str))
print()
print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
