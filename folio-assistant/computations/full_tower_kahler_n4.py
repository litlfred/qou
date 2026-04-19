#!/usr/bin/env python3
"""
Full tower at Kähler level 4 (new default) + D direction-sensitivity scan.

Per user (2026-04-19):
  "n=4 is new default"
  "Investigate D's direction sensitivity — is there a config where
   Kähler both converges AND aims toward AME?"

Part A: Rerun the light-atom binding table at Kähler level 4 (the
new default cutoff, chosen to capture 99.99% of the tower within
keV precision on all light atoms).

Part B: For deuterium, scan (pg, m_pn, k ∈ 0..4) and identify the
config with smallest |B - B_AME| where Kähler at each level n=1..4
moves B toward AME (monotone improving direction).
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

HBAR_Q = (q0 - 1.0) / q0
q_sym = sp.Symbol('q', positive=True)
HA_sym = q_sym - 1 / q_sym
z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))

qint2 = (q0**2 - qi0**2) / (q0 - qi0)
W_SYM = 1.0 / (qint2**2 + 2)
W_STD = qint2**2 / (qint2**2 + 2)
W_ALT = W_SYM

DEFAULT_KAHLER_LEVEL = 4


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


def per_gen_volumes_sym(gen_idx, ordering, pg=None, m_pp=1, m_pn=1, m_nn=1):
    """Per-gen V^λ as symbolic expressions in q_sym."""
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    A = len(ordering)
    if pg is None:
        gluon_count = 2 if ordering[gen_idx] == 1 else 4
    else:
        gluon_count = pg
    for _ in range(gluon_count):
        c, d = sp.Integer(1), sp.Integer(0)
        a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                 sp.expand(a * c + b * d))
        sp_v = sp.expand(sp_v * (c * q_sym + d))
        ap_v = sp.expand(ap_v * (-c / q_sym + d))
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        ti, tj = ordering[gen_idx], ordering[j]
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


def kahler_lift_n(V_sym, n):
    """Apply Kähler lift n times symbolically.
    V^{(k+1)} = V^{(k)} + ℏ_q · q · dV^{(k)}/dq = V^{(k)} + (q-1) dV^{(k)}/dq.
    """
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


def B_at_level_k(Z, N, k, pg=None, m_pp=1, m_pn=1, m_nn=1):
    """Level-k binding contribution before hbar_q^{2k} weighting.
    Evaluates ln|Phi_q(V^(k))| on the k-times Kähler-lifted V^λ."""
    A = Z + N
    if A < 2:
        return 0.0
    ordering = ground_state(Z, N)
    Bs = Bd = Ba = 0.0
    for i in range(A - 1):
        vs, vd, va = per_gen_volumes_sym(
            i, ordering, pg=pg, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
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


def B_tower_sum(Z, N, n_max=DEFAULT_KAHLER_LEVEL, pg=None,
                   m_pp=1, m_pn=1, m_nn=1):
    """Kähler tower SUM up to level n_max (INCLUSIVE).

    B_tower = Σ_{k=0}^{n_max} ℏ_q^{2k} · B^{(k)}
    """
    total = 0.0
    for k in range(n_max + 1):
        Bk = B_at_level_k(Z, N, k, pg=pg, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        total += HBAR_Q**(2 * k) * Bk
    return total


def B_full(Z, N, kahler_level=DEFAULT_KAHLER_LEVEL, pg=None,
              m_pp=1, m_pn=1, m_nn=1):
    """Full-tower binding summed up to given Kähler level."""
    return B_tower_sum(Z, N, n_max=kahler_level, pg=pg,
                          m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)


AME = {
    "D":   2.224566, "T":   8.481798, "3He": 7.718058,
    "4He": 28.295674, "6Li": 31.994571, "7Li": 39.244529,
}


if __name__ == "__main__":
    # Part A: light atoms at Kähler level 4 (new default)
    print("=" * 120)
    print(f"PART A: LIGHT-ATOM BINDING AT KÄHLER LEVEL {DEFAULT_KAHLER_LEVEL} (NEW DEFAULT)")
    print("=" * 120)
    print(f"\n  {'atom':>6} {'Z':>2} {'N':>2}  "
          f"{'B (n=0)':>10} {'B (n=4)':>10}  {'B_AME':>10}  "
          f"{'err n=0':>10} {'err n=4':>10}  {'Δ':>9}")
    print("  " + "-" * 100)

    part_a = []
    for name, Z, N in [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1),
                          ("4He", 2, 2), ("6Li", 3, 3), ("7Li", 3, 4)]:
        A = Z + N
        Mtot = A * 938.272
        B_AME = AME[name]
        B_n0 = B_full(Z, N, kahler_level=0)
        B_n4 = B_full(Z, N, kahler_level=4)
        err_n0 = abs(B_n0 - B_AME) / Mtot * 100
        err_n4 = abs(B_n4 - B_AME) / Mtot * 100
        marker = " ✓" if err_n4 < err_n0 else (" ✗" if err_n4 > err_n0 else "  ")
        print(f"  {name:>6} {Z:>2} {N:>2}  "
              f"{B_n0:>+10.4f} {B_n4:>+10.4f}  {B_AME:>+10.4f}  "
              f"{err_n0:>9.4f}% {err_n4:>9.4f}%{marker} "
              f"{B_n4 - B_n0:>+9.4f}")
        part_a.append({
            "atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME,
            "B_n0_MeV": B_n0, "B_n4_MeV": B_n4,
            "err_n0_pct": err_n0, "err_n4_pct": err_n4,
            "kahler_improves": err_n4 < err_n0,
        })

    # Part B: D direction sensitivity scan
    print("\n" + "=" * 120)
    print("PART B: D DIRECTION-SENSITIVITY SCAN")
    print("(for each (pg, m_pn), show B at k=0,1,2,3,4 and detect monotone-improving direction)")
    print("=" * 120)
    B_AME = AME["D"]
    Mtot = 2 * 938.272

    print(f"\n  {'pg':>3} {'m_pn':>5} | {'k=0':>9} {'k=1':>9} {'k=2':>9} {'k=3':>9} {'k=4':>9} | "
          f"{'err_k=0':>8} {'err_k=4':>8} {'monotone?':>10}")
    print("  " + "-" * 110)

    part_b = []
    for pg in [0, 1, 2]:
        for m_pn in [1, 2, 3]:
            B_levels = []
            err_levels = []
            for k in range(5):
                B = B_full(1, 1, kahler_level=k, pg=pg, m_pn=m_pn)
                B_levels.append(B)
                err_levels.append(abs(B - B_AME) / Mtot * 100)
            # Monotone-improving: err decreases or stays with k
            monotone = all(err_levels[i+1] <= err_levels[i] + 1e-6
                                for i in range(4))
            if monotone:
                monot_str = " ✓ MONOTONE"
            elif err_levels[4] < err_levels[0]:
                monot_str = " ⇒ improves"
            elif err_levels[4] > err_levels[0]:
                monot_str = " ✗ worsens"
            else:
                monot_str = "  = flat"
            print(f"  {pg:>3} {m_pn:>5} | "
                  + " ".join(f"{b:>+9.4f}" for b in B_levels) + " | "
                  + f"{err_levels[0]:>7.4f}% {err_levels[4]:>7.4f}%"
                  + monot_str)
            part_b.append({
                "pg": pg, "m_pn": m_pn,
                "B_at_levels": B_levels,
                "err_at_levels": err_levels,
                "monotone_improving": monotone,
                "err_k0": err_levels[0],
                "err_k4": err_levels[4],
            })

    monotone_configs = [r for r in part_b if r["monotone_improving"]]
    print(f"\n  Monotone-improving D configs ({len(monotone_configs)}): "
          f"{[(r['pg'], r['m_pn']) for r in monotone_configs]}")
    if monotone_configs:
        best_mono = min(monotone_configs, key=lambda r: r["err_k4"])
        print(f"  Best monotone: pg={best_mono['pg']}, m_pn={best_mono['m_pn']}  "
              f"err at k=0 → k=4: {best_mono['err_k0']:.4f}% → {best_mono['err_k4']:.4f}%")

    out = Path(__file__).parent / "full-tower-kahler-n4.witness.json"
    out.write_text(json.dumps({
        "computation": "full-tower-kahler-n4",
        "description": (
            f"Full tower with Kähler level {DEFAULT_KAHLER_LEVEL} "
            "(new default per user directive). Part A: light-atom "
            "binding table at n=4 vs n=0 baseline. Part B: D "
            "direction-sensitivity scan across (pg, m_pn) to find "
            "configs where Kähler monotonically improves prediction."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "M_E_MEV": M_E_MEV,
                          "kahler_level_default": DEFAULT_KAHLER_LEVEL},
        "part_a_light_atoms": part_a,
        "part_b_D_direction": part_b,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
