#!/usr/bin/env python3
"""
Per-nucleon gluon multiplicity SDP on the H_A 3-channel framework
(correct per prop:tower-binding-energy).

Replaces sdp_gluon_multiplicity.py which used the H_{3A} Plancherel
tr_M framework. Per the domain audit 2026-04-19, the correct formula
is

  B(Z,N) = Σ_{λ∈{sym,std,alt}} w_λ · m_e · Σ_{i=0}^{A-2} ln|Φ_q(V̂_i^λ)|

with V̂_i^λ built from:
  (a) per-nucleon gluon self-coupling (currently 2·σ₀ on proton,
      4·σ₀ on neutron — hardcoded in full-tower-mass.per_gen_volumes)
  (b) inter-nucleon crossings (see sdp_inter_nucleon_hA.py)

Decision: per-nucleon gluon decoration ∈ {none, s0, s1, L+, L-}
(the LP-dual-active set from confinement-lp.py). Each nucleon can
have a different decoration; K = 5 candidates per nucleon.

For A nucleons, cartesian product is 5^A candidates. SDP returns
the joint argmin plus dual gaps.

Dual-certificate form: min |B_pred − B_AME| per atom / across atoms.
"""
from __future__ import annotations

import sys
import json
import math
import time
import itertools
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0, HA as h
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

q_sym = sp.Symbol('q', positive=True)
HA_sym = q_sym - 1 / q_sym
z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))

qint2 = (q0**2 - qi0**2) / (q0 - qi0)
w_sym = 1.0 / (qint2**2 + 2)
w_std = qint2**2 / (qint2**2 + 2)
w_alt = w_sym


GLUON_CANDIDATES = {
    "none": [],
    "s0":   [(sp.Integer(1), sp.Integer(0))],             # σ_0
    "s0s0": [(sp.Integer(1), sp.Integer(0))] * 2,         # default proton
    "s0x4": [(sp.Integer(1), sp.Integer(0))] * 4,         # default neutron
    "s1":   [(sp.Integer(1), -HA_sym)],                    # σ_1⁻¹-like
    "Lp":   [(sp.Integer(1), sp.Integer(0)),
              (sp.Integer(1), -HA_sym)],                    # L+ (σ_0 σ_1⁻¹)
    "Lm":   [(sp.Integer(1), -HA_sym),
              (sp.Integer(1), sp.Integer(0))],              # L- (σ_1⁻¹ σ_0)
}
# LP-dual-active set matching atom_sdp_gluon_search.py CANDIDATES_DUAL
GLUON_OPS = ["none", "s0", "s1", "Lp", "Lm"]


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1:
        return (sp.Integer(1), sp.Integer(0))
    elif ti == 0 and tj == 0:
        return (sp.Integer(1), -HA_sym)
    else:
        return (sp.Integer(1), -HA_sym / 2)


def per_gen_volumes_gluon(gen_idx, ordering, gluons):
    """Per-gen per-channel V̂ with custom gluon decoration per nucleon.

    gluons: tuple of length A giving one GLUON_OPS key per nucleon.
    """
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    A = len(ordering)
    # Per-nucleon gluon: apply the gluon of THIS nucleon (gen_idx's
    # nucleon) since gluon crossings live at nucleon slot.
    gluon = GLUON_CANDIDATES[gluons[gen_idx]]
    for c, d in gluon:
        a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                 sp.expand(a * c + b * d))
        sp_v = sp.expand(sp_v * (c * q_sym + d))
        ap_v = sp.expand(ap_v * (-c / q_sym + d))
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                 sp.expand(a * c + b * d))
        sp_v = sp.expand(sp_v * (c * q_sym + d))
        ap_v = sp.expand(ap_v * (-c / q_sym + d))
    return sp_v, z_sym * a + b, ap_v


def ln_Phi_q(V, max_k=500):
    if V == 0:
        return 0.0
    s = 0.0
    for k in range(1, max_k + 1):
        f = 1.0 - qi0**k * V
        if abs(f) < 1e-300:
            return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * V) < 1e-15:
            break
    return s


def ground_state(Z, N):
    o = []
    pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


def B_pred(Z, N, gluons):
    A = Z + N
    if A < 2:
        return 0.0
    ordering = ground_state(Z, N)
    B_s = B_d = B_a = 0.0
    for i in range(A - 1):
        vs, vd, va = per_gen_volumes_gluon(i, ordering, gluons)
        B_s += ln_Phi_q(abs(float(vs.subs(q_sym, q0))))
        B_d += ln_Phi_q(abs(float(vd.subs(q_sym, q0))))
        B_a += ln_Phi_q(abs(float(va.subs(q_sym, q0))))
    return (w_sym * M_E_MEV * B_s + w_std * M_E_MEV * B_d
              + w_alt * M_E_MEV * B_a)


if __name__ == "__main__":
    # Keep small A for quick feedback (5^A candidates).
    ATOMS = [
        ("D",    1,  1,  2.22452),     #  25 candidates
        ("T",    1,  2,  8.481821),    # 125
        ("3He",  2,  1,  7.71804),     # 125
        ("4He",  2,  2, 28.295674),    # 625
    ]

    out_path = (Path(__file__).parent
                 / "gluon-multiplicity-sdp-hA.witness.json")
    print("=" * 115)
    print("GLUON PER-NUCLEON MULTIPLICITY SDP — H_A 3-channel framework")
    print(f"q0 = {q0}, m_e = {M_E_MEV} MeV  "
          f"(candidates per nucleon: {GLUON_OPS})")
    print("=" * 115)

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        combos = list(itertools.product(GLUON_OPS, repeat=A))
        print(f"\n{name} (Z={Z}, N={N}, A={A}, {len(combos)} candidates)")
        t0 = time.time()
        rows = []
        for combo in combos:
            try:
                B = B_pred(Z, N, combo)
                err = abs(B - B_AME) / Mtot * 100
                rows.append({"combo": "_".join(combo),
                                 "B_pred_MeV": B,
                                 "err_pct": err,
                                 "gap_vs_AME_MeV": B - B_AME})
            except Exception as e:
                rows.append({"combo": "_".join(combo),
                                 "error": str(e)})
        dt = time.time() - t0
        valid = [r for r in rows if "err_pct" in r]
        if not valid:
            continue
        best = min(valid, key=lambda r: r["err_pct"])
        for r in valid:
            r["dual_gap"] = r["err_pct"] - best["err_pct"]
        print(f"  {'★':<1} {best['combo']:<40} "
              f"B={best['B_pred_MeV']:>+8.3f}  "
              f"err={best['err_pct']:.4f}%  [{dt:.1f}s]")
        top5 = sorted(valid, key=lambda r: r["dual_gap"])[1:6]
        for r in top5:
            print(f"    {r['combo']:<40} "
                  f"B={r['B_pred_MeV']:>+8.3f}  "
                  f"err={r['err_pct']:.4f}%  gap={r['dual_gap']:+.4f}%")
        all_results.append({
            "atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME,
            "n_candidates": len(valid),
            "best": best,
            "time_sec": dt,
            "top10": sorted(valid, key=lambda r: r["dual_gap"])[:10],
        })
        out_path.write_text(json.dumps({
            "computation": "gluon-multiplicity-sdp-hA",
            "description": (
                "SDP over per-nucleon gluon decoration ∈ "
                f"{GLUON_OPS} on the H_A 3-channel framework. "
                "Replaces H_{3A} Plancherel variant "
                "sdp_gluon_multiplicity.py."),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "parameters": {"q0": q0, "M_E_MEV": M_E_MEV,
                              "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
                              "gluon_ops": GLUON_OPS},
            "results": all_results,
        }, indent=2, default=str))

    print("\n" + "=" * 115)
    print("CROSS-ATOM AGREEMENT")
    picks = {r["atom"]: r["best"]["combo"] for r in all_results}
    print(f"  Per-atom best: {picks}")
    print(f"\nWitness: {out_path}")
