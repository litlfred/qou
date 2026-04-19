#!/usr/bin/env python3
"""
Recompute ALL atoms under the revised `def:kahler-jet-lift`
interpretation: evaluate at V^(k) directly, no tower sum.

Per user (2026-04-19):
  "shift def:kahler-jet-lift to mean 'evaluate at V^(k)'"
  "recompute ALL"

For each atom: compute B(Z, N) at Kähler level n_cut = 4, i.e.
  𝔪 = Σ_λ w_λ · m_e · Σ_i ln|Φ_q(V̂_i^{λ,(4)}(q))|
with V̂^{(4)} = 4-fold application of V → V + (q-1)·dV/dq.
Compare to n=0 (no Kähler) and n_cut ∈ {1, 2, 3, 4}.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV

q_sym = sp.Symbol('q', positive=True)
HA_sym = q_sym - 1 / q_sym
z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))

qint2 = (q0**2 - qi0**2) / (q0 - qi0)
W_SYM = 1.0 / (qint2**2 + 2)
W_STD = qint2**2 / (qint2**2 + 2)
W_ALT = W_SYM

DEFAULT_KAHLER = 4


def ln_phi_q(v, max_k=500):
    if v == 0:
        return 0.0
    s = 0.0
    for k in range(1, max_k + 1):
        f = 1.0 - qi0**k * v
        if abs(f) < 1e-300:
            return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15:
            break
    return s


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1:
        return (sp.Integer(1), sp.Integer(0))
    elif ti == 0 and tj == 0:
        return (sp.Integer(1), -HA_sym)
    else:
        return (sp.Integer(1), -HA_sym / 2)


def per_gen_volumes_sym(gen_idx, ordering):
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    A = len(ordering)
    gluon = [(sp.Integer(1), sp.Integer(0))] * (
        2 if ordering[gen_idx] == 1 else 4)
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


def kahler_lift_n(V_sym, n):
    """Apply V → V + (q-1) dV/dq iteratively n times."""
    V = V_sym
    for _ in range(n):
        V = sp.expand(V + (q_sym - 1) * sp.diff(V, q_sym))
    return V


def ground_state(Z, N):
    o = []
    pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


def B_at_level_k(Z, N, k):
    """Evaluate m^{(k)} = Σ_λ w_λ m_e Σ_i ln|Φ_q(V^(k))|."""
    A = Z + N
    if A < 2:
        return 0.0
    ordering = ground_state(Z, N)
    Bs = Bd = Ba = 0.0
    for i in range(A - 1):
        vs, vd, va = per_gen_volumes_sym(i, ordering)
        if k > 0:
            vs = kahler_lift_n(vs, k)
            vd = kahler_lift_n(vd, k)
            va = kahler_lift_n(va, k)
        Bs += ln_phi_q(abs(float(vs.subs(q_sym, q0))))
        Bd += ln_phi_q(abs(float(vd.subs(q_sym, q0))))
        Ba += ln_phi_q(abs(float(va.subs(q_sym, q0))))
    return (W_SYM * M_E_MEV * Bs
              + W_STD * M_E_MEV * Bd
              + W_ALT * M_E_MEV * Ba)


AME = {
    "D":   2.224566, "T":   8.481798, "3He": 7.718058,
    "4He": 28.295674, "6Li": 31.994571, "7Li": 39.244529,
    "9Be": 58.164980, "10B": 64.750861, "12C": 92.161728,
    "14N": 104.658605, "16O": 127.619334, "20Ne": 160.644859,
}


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1),   ("T",   1, 2),   ("3He", 2, 1),
        ("4He", 2, 2),   ("6Li", 3, 3),   ("7Li", 3, 4),
        ("9Be", 4, 5),   ("10B", 5, 5),   ("12C", 6, 6),
        ("14N", 7, 7),   ("16O", 8, 8),   ("20Ne", 10, 10),
    ]

    print("=" * 140)
    print(f"RECOMPUTE ALL — def:kahler-jet-lift = 'evaluate at V^(k)'")
    print(f"q0 = {q0}  m_e = {M_E_MEV}  default cutoff n = {DEFAULT_KAHLER}")
    print("=" * 140)
    print(f"\n  {'atom':>6} {'Z':>3} {'N':>3}  "
          + "  ".join(f"{'B(n=' + str(n) + ')':>10}" for n in range(5))
          + f"  {'B_AME':>10}  "
          + "  ".join(f"{'err n=' + str(n):>9}" for n in range(5)))
    print("  " + "-" * 138)

    results = []
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        B_AME = AME[name]
        B_levels = []
        err_levels = []
        for k in range(5):
            B = B_at_level_k(Z, N, k)
            B_levels.append(B)
            err_levels.append(abs(B - B_AME) / Mtot * 100)
        row = f"  {name:>6} {Z:>3} {N:>3}  " + "  ".join(f"{b:>+10.3f}" for b in B_levels)
        row += f"  {B_AME:>+10.4f}  " + "  ".join(f"{e:>8.4f}%" for e in err_levels)
        # Marker for best level
        best_n = int(np.argmin(err_levels))
        row += f"  best n={best_n}"
        print(row)
        results.append({
            "atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME,
            "B_at_levels": B_levels,
            "err_at_levels_pct": err_levels,
            "best_level": best_n,
            "best_err_pct": err_levels[best_n],
            "Mtot_MeV": Mtot,
        })

    # Summary
    err_at_n0 = [r["err_at_levels_pct"][0] for r in results]
    err_at_n4 = [r["err_at_levels_pct"][4] for r in results]
    print(f"\n  MEAN err n=0: {np.mean(err_at_n0):.4f}%")
    print(f"  MEAN err n=4: {np.mean(err_at_n4):.4f}%")
    print(f"  MEAN best-per-atom: {np.mean([r['best_err_pct'] for r in results]):.4f}%")

    # Level distribution of best
    best_levels = [r["best_level"] for r in results]
    print(f"  Best-level distribution: "
          f"n=0:{best_levels.count(0)} n=1:{best_levels.count(1)} "
          f"n=2:{best_levels.count(2)} n=3:{best_levels.count(3)} "
          f"n=4:{best_levels.count(4)}")

    out = Path(__file__).parent / "kahler-single-level-all-atoms.witness.json"
    out.write_text(json.dumps({
        "computation": "kahler-single-level-all-atoms",
        "description": (
            "Recompute ALL atoms under revised def:kahler-jet-lift = "
            "evaluate at V^(k) (single-level, not tower sum). Shows "
            "B at k=0..4 for D through 20Ne, identifies per-atom "
            "best level."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "M_E_MEV": M_E_MEV,
                          "W_sym": W_SYM, "W_std": W_STD, "W_alt": W_ALT},
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
