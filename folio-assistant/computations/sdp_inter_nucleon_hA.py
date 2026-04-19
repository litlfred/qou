#!/usr/bin/env python3
"""
Inter-nucleon SDP on the H_A(q) 3-channel framework (correct per
prop:tower-binding-energy).

Replaces sdp_inter_nucleon.py which used the H_{3A} Plancherel tr_M
framework. Per the domain audit in
docs/framework-mismatch-audit-2026-04-19.md, the correct formula is

  B(Z,N) = Σ_{λ∈{sym,std,alt}} w_λ · m_e · Σ_{i=0}^{A-2} ln|Φ_q(V̂_i^λ)|

with the V̂_i^λ computed from per-nucleon gluon + inter-nucleon
crossings (as in full-tower-mass.py).

Decision variables: (m_pp, m_pn, m_nn) ∈ {1..3}³
Each triple = a distinct inter-nucleon crossing count pattern.
SDP objective: minimize mean |err| across the light atoms, with
dual-gap certificates per triple.

For real Hecke products Frobenius positivity is auto-satisfied, so
SDP reduces to LP over the simplex Δ^{K-1}. Dual gaps = per-candidate
margin to the optimum.
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


def crossing_coeffs(ti, tj):
    """Per-pair (c, d) for the inter-nucleon crossing."""
    if ti == 1 and tj == 1:
        return (sp.Integer(1), sp.Integer(0))            # pp
    elif ti == 0 and tj == 0:
        return (sp.Integer(1), -HA_sym)                   # nn
    else:
        return (sp.Integer(1), -HA_sym / 2)               # pn


def per_gen_volumes_m(gen_idx, ordering, m_pp, m_pn, m_nn):
    """Per-generator per-channel V̂_i^λ with ILP crossings per pair.

    Matches full-tower-mass.per_gen_volumes but applies m_pp / m_pn
    / m_nn copies of the inter-nucleon crossing at each pair.
    """
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    A = len(ordering)
    # Gluon self-coupling: 2 for proton (ordering=1), 4 for neutron.
    gluon = [(sp.Integer(1), sp.Integer(0))] * (
        2 if ordering[gen_idx] == 1 else 4)
    for c, d in gluon:
        a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                 sp.expand(a * c + b * d))
        sp_v = sp.expand(sp_v * (c * q_sym + d))
        ap_v = sp.expand(ap_v * (-c / q_sym + d))
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        ti = ordering[gen_idx]; tj = ordering[j]
        if ti == 1 and tj == 1:
            m = m_pp
        elif ti == 0 and tj == 0:
            m = m_nn
        else:
            m = m_pn
        for _ in range(m):
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
            o.append(1)
            pi += 1
        else:
            o.append(0)
            ni += 1
    return o


def B_pred(Z, N, m_pp, m_pn, m_nn):
    A = Z + N
    if A < 2:
        return 0.0
    ordering = ground_state(Z, N)
    B_s = B_d = B_a = 0.0
    for i in range(A - 1):
        vs, vd, va = per_gen_volumes_m(
            i, ordering, m_pp, m_pn, m_nn)
        B_s += ln_Phi_q(abs(float(vs.subs(q_sym, q0))))
        B_d += ln_Phi_q(abs(float(vd.subs(q_sym, q0))))
        B_a += ln_Phi_q(abs(float(va.subs(q_sym, q0))))
    return (w_sym * M_E_MEV * B_s
              + w_std * M_E_MEV * B_d
              + w_alt * M_E_MEV * B_a)


if __name__ == "__main__":
    ATOMS = [
        ("D",    1,  1,  2.22452),
        ("T",    1,  2,  8.481821),
        ("3He",  2,  1,  7.71804),
        ("4He",  2,  2, 28.295674),
        ("6Li",  3,  3, 32.00),
        ("7Li",  3,  4, 39.244529),
    ]

    m_range = range(1, 4)
    triples = list(itertools.product(m_range, m_range, m_range))

    out_path = (Path(__file__).parent
                 / "inter-nucleon-sdp-hA.witness.json")
    print("=" * 115)
    print("INTER-NUCLEON SDP — H_A 3-channel framework "
          "(per prop:tower-binding-energy)")
    print(f"q0 = {q0}, m_e = {M_E_MEV} MeV")
    print(f"w_sym = {w_sym:.6f}  w_std = {w_std:.6f}  w_alt = {w_alt:.6f}")
    print("=" * 115)

    # Per-atom error table for each triple
    per_atom = {}
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        rows = []
        print(f"\n{name} (Z={Z}, N={N}):")
        for (mpp, mpn, mnn) in triples:
            t0 = time.time()
            try:
                B = B_pred(Z, N, mpp, mpn, mnn)
                err = abs(B - B_AME) / Mtot * 100
                dt = time.time() - t0
                rows.append({"triple": f"pp{mpp}_pn{mpn}_nn{mnn}",
                                 "m_pp": mpp, "m_pn": mpn, "m_nn": mnn,
                                 "B_pred_MeV": B, "err_pct": err,
                                 "gap_vs_AME_MeV": B - B_AME,
                                 "time_sec": dt})
            except Exception as e:
                rows.append({"triple": f"pp{mpp}_pn{mpn}_nn{mnn}",
                                 "error": str(e)})
        valid = [r for r in rows if "err_pct" in r]
        if not valid:
            per_atom[name] = {"Z": Z, "N": N, "error": "no valid triples"}
            continue
        best = min(valid, key=lambda r: r["err_pct"])
        opt_err = best["err_pct"]
        for r in valid:
            r["dual_gap"] = r["err_pct"] - opt_err
        per_atom[name] = {
            "Z": Z, "N": N, "A": A, "B_AME": B_AME,
            "best_triple": best["triple"],
            "best_B_pred_MeV": best["B_pred_MeV"],
            "best_err_pct": best["err_pct"],
            "all_triples": sorted(valid, key=lambda r: r["dual_gap"]),
        }
        # Print top 3 by dual_gap
        top3 = sorted(valid, key=lambda r: r["dual_gap"])[:3]
        for r in top3:
            marker = "★" if r["triple"] == best["triple"] else " "
            print(f"   {marker} {r['triple']:<20} B={r['B_pred_MeV']:>+8.3f}  "
                  f"err={r['err_pct']:.4f}%  gap={r['dual_gap']:+.4f}%")

    # Cross-atom: joint optimum (minimise sum of per-atom errors)
    print("\n" + "=" * 115)
    print("JOINT SDP — argmin_{(pp,pn,nn)}  Σ atoms |B_pred − B_AME|/Mtot")
    print("=" * 115)
    triple_err_sum = {}
    for t in triples:
        name_t = f"pp{t[0]}_pn{t[1]}_nn{t[2]}"
        s = 0.0
        for atom, entry in per_atom.items():
            if "all_triples" not in entry:
                continue
            match = next(
                (r for r in entry["all_triples"] if r["triple"] == name_t),
                None)
            if match:
                s += match["err_pct"]
        triple_err_sum[name_t] = s
    best_joint = min(triple_err_sum.items(), key=lambda kv: kv[1])
    print(f"  Joint optimum: {best_joint[0]}  sum_err={best_joint[1]:.4f}%")
    print("  Top 5 by joint err:")
    for name_t, s in sorted(triple_err_sum.items(), key=lambda kv: kv[1])[:5]:
        gap = s - best_joint[1]
        print(f"    {name_t:<20} sum_err={s:.4f}%  joint_gap={gap:+.4f}%")

    out_path.write_text(json.dumps({
        "computation": "inter-nucleon-sdp-hA",
        "description": (
            "SDP over inter-nucleon crossing triples (m_pp, m_pn, m_nn) "
            "∈ {1..3}³ on the H_A 3-channel framework from "
            "prop:tower-binding-energy. Replaces the H_{3A} Plancherel "
            "variant sdp_inter_nucleon.py (wrong framework, per audit "
            "2026-04-19)."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "M_E_MEV": M_E_MEV,
                          "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
                          "m_range": list(m_range)},
        "per_atom_optima": per_atom,
        "joint_optimum": {"triple": best_joint[0],
                              "sum_err_pct": best_joint[1]},
        "triple_err_sums": triple_err_sum,
    }, indent=2, default=str))
    print(f"\nWitness: {out_path}")
