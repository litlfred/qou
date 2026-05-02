#!/usr/bin/env python3
"""
Per-braid hybrid with FULL-Plancherel q-Hecke descended (Phase A.1 wired in).

Same as per_braid_tower_hybrid.py but uses
markov_trace_full_schur_weyl (Plancherel weight, all partitions of
3A) for the descended q-Hecke trace instead of the length-≤-2
2-variable Schur version.

Tower terms (level 1/2) unchanged — still use q=1 MN.

Goal: see if AME calibration spread tightens vs the prior 1.06%.

Witness: docs/audits/2026-05-02-per-braid-hybrid-full-vs-ame.witness.json
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_full_schur_weyl import markov_trace_full_schur_weyl
from schur_weyl_mpmath import markov_trace_mpmath
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
}


def _safe_phi(z, q=q0, qi=qi0, max_k=200):
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


def per_braid_mass_hybrid_full(Z, N):
    A = Z + N

    # Level 0: FULL-Plancherel q-Hecke descended (Phase A.1)
    desc, _, _ = markov_trace_full_schur_weyl(Z, N, include_inter=True, dim_cap=10000)
    desc = abs(desc)

    # Level 1/2: q=1 MN (unchanged from prior hybrid)
    tr_p, _, _ = markov_trace_mpmath(1, 0, include_inter=False) if Z > 0 else (mpmath.mpf(0), [], ())
    tr_n, _, _ = markov_trace_mpmath(0, 1, include_inter=False) if N > 0 else (mpmath.mpf(0), [], ())
    tr_p = abs(tr_p); tr_n = abs(tr_n)

    tr_pp, _, _ = markov_trace_mpmath(2, 0, include_inter=True) if Z >= 2 else (mpmath.mpf(0), [], ())
    tr_nn, _, _ = markov_trace_mpmath(0, 2, include_inter=True) if N >= 2 else (mpmath.mpf(0), [], ())
    tr_pn, _, _ = markov_trace_mpmath(1, 1, include_inter=True) if Z >= 1 and N >= 1 else (mpmath.mpf(0), [], ())
    tr_pp = abs(tr_pp); tr_nn = abs(tr_nn); tr_pn = abs(tr_pn)

    single = mpmath.mpf(0)
    if Z > 0 and tr_p > 0: single += Z * _safe_phi(tr_p)
    if N > 0 and tr_n > 0: single += N * _safe_phi(tr_n)

    cross = mpmath.mpf(0)
    n_pp = Z * (Z - 1) // 2
    n_nn = N * (N - 1) // 2
    n_pn = Z * N
    if n_pp > 0 and tr_pp > 0: cross += n_pp * _safe_phi(tr_pp)
    if n_nn > 0 and tr_nn > 0: cross += n_nn * _safe_phi(tr_nn)
    if n_pn > 0 and tr_pn > 0: cross += n_pn * _safe_phi(tr_pn)
    cross *= z_mark ** 2

    return {"Z": Z, "N": N, "A": A, "desc": desc, "single": single, "cross": cross, "total": desc + single + cross}


print("=" * 88)
print("Per-braid HYBRID with FULL-Plancherel descended (Phase A.1) vs AME")
print("=" * 88)
print(f"q_0 = {q0}")
print()

ATOMS = [("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2)]

print(f"  {'Atom':>5} {'A':>3}  {'desc(full-Plancherel)':>22}  {'tower (q=1)':>12}  {'total':>14}  {'AME (MeV)':>12}  {'cal/m_e':>12}")
print("  " + "-" * 100)

results = []
ratios = []
for name, Z, N in ATOMS:
    t0 = time.time()
    out = per_braid_mass_hybrid_full(Z, N)
    t = time.time() - t0
    total_f = float(out["total"])
    ame = AME_MASS_MEV[name]
    cal_constant = ame / total_f
    cal_over_me = cal_constant / M_E_MEV
    ratios.append(cal_over_me)
    print(
        f"  {name:>5} {Z+N:>3}  {float(out['desc']):>22.6e}  "
        f"{float(out['single'] + out['cross']):>12.4e}  "
        f"{total_f:>14.4e}  {ame:>12.4f}  {cal_over_me:>12.8f}  ({t:.1f}s)"
    )
    results.append({
        "atom": name, "Z": Z, "N": N, "A": Z + N,
        "descended_full_plancherel": str(out["desc"]),
        "single_tower_q1": str(out["single"]) if not mpmath.isinf(out["single"]) else "inf",
        "cross_tower_q1": str(out["cross"]) if not mpmath.isinf(out["cross"]) else "inf",
        "total": total_f,
        "ame_mass_mev": ame,
        "cal_over_me": cal_over_me,
        "time_seconds": t,
    })

mean_ratio = sum(ratios) / len(ratios)
spread = (max(ratios) - min(ratios)) / mean_ratio * 100
print()
print(f"  Mean cal/m_e = {mean_ratio:.6f} (spread {spread:.4f}%)")

# Compare to prior length-≤-2 hybrid
PRIOR = {"D": 0.991802, "3He": 0.989969, "3H": 0.990156, "4He": 0.985360}
print(f"\n  Comparison to length-≤-2 hybrid:")
for r in results:
    delta = r["cal_over_me"] - PRIOR[r["atom"]]
    print(f"    {r['atom']:>5}: {PRIOR[r['atom']]:.6f} → {r['cal_over_me']:.6f} (Δ = {delta:+.6f})")

# 3He vs 3H
he3 = next(r for r in results if r["atom"] == "3He")
h3 = next(r for r in results if r["atom"] == "3H")
diff = abs(he3["total"] - h3["total"])
print(f"\n  3He vs 3H per-braid totals:")
print(f"    3He: {he3['total']:.6f}")
print(f"    3H : {h3['total']:.6f}")
print(f"    diff: {diff:.6e}  ({(diff/max(he3['total'],h3['total']))*100:.6e}% relative)")
print(f"    physical 3H - 3He = {h3['ame_mass_mev'] - he3['ame_mass_mev']:.4f} MeV")
print(f"    cal/m_e diff: {abs(he3['cal_over_me'] - h3['cal_over_me']):.6e}")

witness = {
    "audit": "Per-braid HYBRID with FULL-Plancherel descended (Phase A.1)",
    "generated": datetime.now(timezone.utc).isoformat(),
    "q_0": str(q0),
    "atoms": results,
    "mean_cal_over_me": mean_ratio,
    "spread_percent": spread,
    "interpretation": (
        "Hybrid per-braid mass tower with the descended trace "
        "computed via FULL Plancherel weight × q-Hecke character "
        "(Phase A.1) instead of length-≤-2 2-variable Schur. "
        "Tower terms (level 1/2) still use q=1 MN."
    ),
}

out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-02-per-braid-hybrid-full-vs-ame.witness.json"
out_path.write_text(json.dumps(witness, indent=2, default=str))
print()
print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
