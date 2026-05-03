#!/usr/bin/env python3
"""
Per-braid mass tower — HYBRID: q-Hecke descended + q=1 MN tower.

Per `2026-05-01-q-hecke-norm-analysis.md` Option C: use the q-Hecke
character (with per-crossing (c, d)) for the LEVEL-0 descended
trace where it correctly splits isobars (3He vs 3H differ by
51.6% in the q-Hecke descended), and use the q=1 MN character for
the LEVEL-1/2 Φ_q tower terms where it preserves linear-in-A
scaling.

Hypothesis: this combination gives both:
  (a) Correct isobar splitting from the descended q-Hecke term
  (b) Correct linear-in-A scaling from the q=1 MN tower terms

Witness: docs/audits/2026-05-01-per-braid-hybrid-vs-ame.witness.json
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
# Imports below depend on the sys.path mutation above; suppress E402.
# q-Hecke (proper proton/neutron-distinguishing) for descended
from schur_weyl_q_hecke_v2 import markov_trace_q_hecke_atomic  # noqa: E402
# q=1 MN (linear-in-A scaling) for tower terms
from schur_weyl_mpmath import markov_trace_mpmath  # noqa: E402
from q_parameter import Q as Q0_FLOAT  # noqa: E402

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
    "16O": 14899.16828,
    "40Ca": 37224.9202,
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


# P2.5/B.2 — Cache the 5 sub-braid traces (proton, neutron, pp, nn, pn).
# These are atom-independent: the same five traces recur across every
# atom. Computing once saves time across the per-atom loop.
_SUB_BRAID_CACHE = {}


def _cached_sub_braid_trace(Z_sub, N_sub, include_inter):
    """Return |tr_M(sub-braid)| for a (Z_sub, N_sub) sub-braid via q=1 MN.
    Cached across calls."""
    key = (Z_sub, N_sub, include_inter)
    if key in _SUB_BRAID_CACHE:
        return _SUB_BRAID_CACHE[key]
    if Z_sub + N_sub == 0:
        v = mpmath.mpf(0)
    else:
        tr, _, _ = markov_trace_mpmath(Z_sub, N_sub, include_inter=include_inter)
        v = abs(tr)
    _SUB_BRAID_CACHE[key] = v
    return v


def per_braid_mass_hybrid(Z, N):
    """Hybrid per-braid mass tower.

    Level 0 (descended): q-Hecke with (c, d) — distinguishes isobars.
    Level 1/2 (tower): q=1 MN — preserves linear-in-A scaling.
    """
    A = Z + N

    # Level 0: q-Hecke descended (splits isobars).
    desc_q_hecke, _ = markov_trace_q_hecke_atomic(Z, N, include_inter=True, dim_cap=5000)
    desc = abs(desc_q_hecke)

    # Level 1: per-nucleon traces (CACHED).
    tr_p = _cached_sub_braid_trace(1, 0, False) if Z > 0 else mpmath.mpf(0)
    tr_n = _cached_sub_braid_trace(0, 1, False) if N > 0 else mpmath.mpf(0)

    # Level 2: per-pair traces — q-Hecke (Coulomb-distinguishing per
    # 2026-05-02 principled adoption; q=1 MN gave identical pp=nn=pn,
    # an artifact of the q→1 limit. q-Hecke gives pp:nn:pn = 4.23:1.63:2.69
    # relative ratios — pp/nn = 2.59 reflects Coulomb-like pp repulsion.
    # See docs/audits/2026-05-02-coulomb-q-hecke-principled.md.)
    _PAIR_QH_CACHE = globals().setdefault("_PAIR_QH_CACHE", {})

    def _qhecke_pair_tr(Zsub, Nsub):
        if (Zsub, Nsub) not in _PAIR_QH_CACHE:
            v, _ = markov_trace_q_hecke_atomic(
                Zsub, Nsub, include_inter=True, dim_cap=5000)
            _PAIR_QH_CACHE[(Zsub, Nsub)] = abs(v)
        return _PAIR_QH_CACHE[(Zsub, Nsub)]

    tr_pp = _qhecke_pair_tr(2, 0) if Z >= 2 else mpmath.mpf(0)
    tr_nn = _qhecke_pair_tr(0, 2) if N >= 2 else mpmath.mpf(0)
    tr_pn = _qhecke_pair_tr(1, 1) if Z >= 1 and N >= 1 else mpmath.mpf(0)

    # Single tower (q=1 MN — single-nucleon q-Hecke divergent at Φ_q;
    # P2.2c-norm framework gap pending. Per binding-energy probe,
    # the single-tower correction lives at level 1+.)
    single = mpmath.mpf(0)
    if Z > 0 and tr_p > 0:
        single += Z * _safe_phi(tr_p)
    if N > 0 and tr_n > 0:
        single += N * _safe_phi(tr_n)

    # Pair tower (q-Hecke per-pair, principled)
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
        "desc_q_hecke": desc, "single": single, "cross": cross, "total": total,
    }


if __name__ == "__main__":
    print("=" * 88)
    print("Per-braid HYBRID (q-Hecke descended + q=1 MN tower) vs AME")
    print("=" * 88)
    print(f"q_0 = {q0}")
    print(f"m_e = {M_E_MEV} MeV")
    print()

    ATOMS = [
        ("D", 1, 1),
        ("3He", 2, 1),
        ("3H", 1, 2),
        ("4He", 2, 2),
        ("6Li", 3, 3),
        ("7Li", 3, 4),
        ("9Be", 4, 5),
        ("12C", 6, 6),
        ("16O", 8, 8),
        ("40Ca", 20, 20),
    ]
    # AME values for the new atoms
    AME_MASS_MEV.update({
        "6Li":  5603.05182,
        "7Li":  6535.36573,
        "9Be":  8392.74912,
    })
    # 12C/16O/40Ca deferred — q-Hecke descended at A=12+ requires
    # matrix products through partition dims ~6500+; needs Rust
    # extension chi_q_atomic (P2.2c-12C).

    print(f"  {'Atom':>5} {'A':>3} {'desc(q-Hecke)':>14} {'tower (q=1)':>12} {'total':>14} {'AME (MeV)':>12} {'cal/m_e':>12}")
    print("  " + "-" * 90)

    results = []
    ratios = []
    for name, Z, N in ATOMS:
        t0 = time.time()
        out = per_braid_mass_hybrid(Z, N)
        t = time.time() - t0
        total_f = float(out["total"])
        ame = AME_MASS_MEV[name]
        cal_constant = ame / total_f
        cal_over_me = cal_constant / M_E_MEV
        ratios.append(cal_over_me)
        print(
            f"  {name:>5} {Z+N:>3} {float(out['desc_q_hecke']):>14.6e} "
            f"{float(out['single'] + out['cross']):>12.4e} "
            f"{total_f:>14.4e} {ame:>12.4f} {cal_over_me:>12.8f}  ({t:.1f}s)"
        )
        results.append({
            "atom": name, "Z": Z, "N": N, "A": Z + N,
            "descended_q_hecke": str(out["desc_q_hecke"]),
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

    he3 = next((r for r in results if r["atom"] == "3He"), None)
    h3 = next((r for r in results if r["atom"] == "3H"), None)
    splitting_info = None
    if he3 and h3:
        diff = abs(he3["total"] - h3["total"])
        rel = diff / max(he3["total"], h3["total"])
        physical_diff = abs(he3["ame_mass_mev"] - h3["ame_mass_mev"])
        cal_diff = abs(he3["cal_over_me"] - h3["cal_over_me"])
        print()
        print(f"  3He vs 3H per-braid totals:")
        print(f"    3He: {he3['total']:.4f}")
        print(f"    3H : {h3['total']:.4f}")
        print(f"    diff: {diff:.6e}  ({rel*100:.6e}% relative)")
        print(f"    physical 3H - 3He = {physical_diff:.4f} MeV (AME)")
        print(f"    cal/m_e diff: {cal_diff:.6e}")
        splitting_info = {
            "diff": diff, "rel": rel, "physical_mev": physical_diff,
            "cal_diff": cal_diff,
        }

    witness = {
        "audit": "Per-braid HYBRID (q-Hecke descended + q=1 MN tower) vs AME",
        "generated": datetime.now(timezone.utc).isoformat(),
        "q_0": str(q0),
        "m_e_mev": M_E_MEV,
        "atoms": results,
        "mean_cal_over_me": mean_ratio,
        "spread_percent": spread,
        "splitting": splitting_info,
        "interpretation": (
            "Hybrid per-braid tower: q-Hecke (with per-crossing (c, d)) "
            "for the descended level-0 trace; q=1 MN for the level-1/2 "
            "Φ_q tower terms. Goal: combine isobar splitting (q-Hecke "
            "descended) with linear-in-A scaling (q=1 MN tower)."
        ),
    }
    out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-per-braid-hybrid-vs-ame.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
