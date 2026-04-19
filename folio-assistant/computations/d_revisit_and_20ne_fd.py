#!/usr/bin/env python3
"""
D revisit (sensitivity) + 20Ne completion via finite-difference Kähler.

Per user:
  "2. Revisit D directly — Kähler won't help D, what's the actual
      fix for its 121% over-prediction?"
  "3. Push 20Ne to completion"

PART A — D sensitivity: vary q₀, m_e, W_std, m_pn to see which
parameter dominates D's over-prediction and whether any physically
defensible choice brings D to AME.

PART B — 20Ne via numeric finite-difference Kähler: evaluate
per-gen V^λ(q) at q₀ ± k·δ for k = -N..N, compute dV/dq via central
differences, iterate Kähler lift n_max times.  O(n_max · n_gens)
instead of sympy's O(n_max · n_gens · expand-overhead).
"""
from __future__ import annotations

import sys
import json
import math
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0_default, Q_INV as qi0_default
from experimental_constants import M_E_MEV as M_E_DEFAULT


def wedderburn_weights(q):
    qi = 1.0 / q
    qint2 = (q**2 - qi**2) / (q - qi)
    denom = qint2**2 + 2.0
    return 1.0 / denom, qint2**2 / denom, 1.0 / denom


def ln_phi_q(v, qi, max_k=500):
    if v == 0:
        return 0.0
    s = 0.0
    for k in range(1, max_k + 1):
        f = 1.0 - qi**k * v
        if abs(f) < 1e-300:
            return float('inf')
        s -= math.log(abs(f))
        if abs(qi**k * v) < 1e-15:
            break
    return s


def crossing_coeffs(ti, tj, h):
    if ti == 1 and tj == 1:
        return 1.0, 0.0
    elif ti == 0 and tj == 0:
        return 1.0, -h
    else:
        return 1.0, -h / 2.0


def per_gen_volumes_float(gen_idx, ordering, q, m_pp=1, m_pn=1, m_nn=1):
    """Numeric per-gen V^λ at a given q (no sympy)."""
    h = q - 1.0 / q
    z = 1.0 / (math.sqrt(q) + 1.0 / math.sqrt(q))
    a, b = 0.0, 1.0
    sp_v, ap_v = 1.0, 1.0
    A = len(ordering)
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    for _ in range(gluon_count):
        c, d = 1.0, 0.0
        a, b = a * c * h + a * d + b * c, a * c + b * d
        sp_v *= c * q + d
        ap_v *= -c / q + d
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j], h)
        ti, tj = ordering[gen_idx], ordering[j]
        if ti == 1 and tj == 1:
            m = m_pp
        elif ti == 0 and tj == 0:
            m = m_nn
        else:
            m = m_pn
        for _ in range(m):
            a, b = a * c * h + a * d + b * c, a * c + b * d
            sp_v *= c * q + d
            ap_v *= -c / q + d
    return sp_v, z * a + b, ap_v


def ground_state(Z, N):
    o = []
    pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


def kahler_lift_finite_diff(f_at_q_grid, delta):
    """Apply Kähler lift V → V + (q−1) dV/dq on a grid.

    f_at_q_grid is a numpy array of V(q_k) values at q_k = q0 + k·δ
    for k = -N..N. Returns a new array of V^(1)(q_k) values.
    """
    n = len(f_at_q_grid)
    N = (n - 1) // 2
    out = np.zeros(n)
    for k in range(n):
        if k == 0 or k == n - 1:
            # Edge: forward/backward difference
            if k == 0:
                dV = (f_at_q_grid[1] - f_at_q_grid[0]) / delta
            else:
                dV = (f_at_q_grid[-1] - f_at_q_grid[-2]) / delta
        else:
            # Central difference
            dV = (f_at_q_grid[k + 1] - f_at_q_grid[k - 1]) / (2 * delta)
        q_k = q0_default + (k - N) * delta
        out[k] = f_at_q_grid[k] + (q_k - 1) * dV
    return out


def B_fd(Z, N, kahler_level, q_center=None, m_e=None, w_std_override=None,
         m_pp=1, m_pn=1, m_nn=1, delta=1e-4, n_max=6):
    """Numeric finite-difference binding at given Kähler level."""
    if q_center is None:
        q_center = q0_default
    if m_e is None:
        m_e = M_E_DEFAULT
    A = Z + N
    if A < 2:
        return 0.0
    ordering = ground_state(Z, N)
    w_sym, w_std, w_alt = wedderburn_weights(q_center)
    if w_std_override is not None:
        # Rescale to keep total = 1
        remaining = 1 - w_std_override
        w_sym = w_alt = remaining / 2
        w_std = w_std_override

    # Evaluate per-gen V^λ on grid of q values
    N_grid = max(kahler_level + 2, 3)
    q_grid = [q_center + k * delta for k in range(-N_grid, N_grid + 1)]

    Bs = Bd = Ba = 0.0
    for gen_idx in range(A - 1):
        # Build arrays of V^sym, V^std, V^alt on grid
        vs_grid = np.array([per_gen_volumes_float(
            gen_idx, ordering, q, m_pp, m_pn, m_nn)[0] for q in q_grid])
        vd_grid = np.array([per_gen_volumes_float(
            gen_idx, ordering, q, m_pp, m_pn, m_nn)[1] for q in q_grid])
        va_grid = np.array([per_gen_volumes_float(
            gen_idx, ordering, q, m_pp, m_pn, m_nn)[2] for q in q_grid])

        # Apply Kähler lift kahler_level times on each
        for _ in range(kahler_level):
            vs_grid = kahler_lift_finite_diff(vs_grid, delta)
            vd_grid = kahler_lift_finite_diff(vd_grid, delta)
            va_grid = kahler_lift_finite_diff(va_grid, delta)

        # Evaluate at q_center (middle of grid)
        vs_center = vs_grid[N_grid]
        vd_center = vd_grid[N_grid]
        va_center = va_grid[N_grid]
        qi_center = 1.0 / q_center
        Bs += ln_phi_q(abs(vs_center), qi_center)
        Bd += ln_phi_q(abs(vd_center), qi_center)
        Ba += ln_phi_q(abs(va_center), qi_center)

    return w_sym * m_e * Bs + w_std * m_e * Bd + w_alt * m_e * Ba


AME = {
    "D":   2.224566, "T":   8.481798, "3He": 7.718058,
    "4He": 28.295674, "6Li": 31.994571, "7Li": 39.244529,
    "9Be": 58.164980, "10B": 64.750861, "12C": 92.161728,
    "14N": 104.658605, "16O": 127.619334, "20Ne": 160.644859,
}


if __name__ == "__main__":
    # ── PART A: D sensitivity ─────────────────────────────────
    print("=" * 125)
    print("PART A: D SENSITIVITY — scan q, m_e, W_std, m_pn  (target: B_AME = 2.225)")
    print("=" * 125)

    d_results = []
    Mtot_D = 2 * 938.272

    # A1. vary q
    print("\n  A1. Vary q around 1.11:")
    for q_val in [1.050, 1.080, 1.100, 1.110, 1.120, 1.150, 1.200]:
        B = B_fd(1, 1, kahler_level=0, q_center=q_val)
        err = abs(B - AME["D"]) / Mtot_D * 100
        print(f"    q = {q_val}: B_D = {B:.4f}  err = {err:.4f}%")
        d_results.append({"scan": "q", "value": q_val,
                             "B_D": B, "err_pct": err})

    # A2. vary m_e
    print("\n  A2. Vary m_e (energy unit):")
    for m in [0.2, 0.3, 0.4, 0.511, 0.6, 0.8]:
        B = B_fd(1, 1, kahler_level=0, m_e=m)
        err = abs(B - AME["D"]) / Mtot_D * 100
        print(f"    m_e = {m}: B_D = {B:.4f}  err = {err:.4f}%")
        d_results.append({"scan": "m_e", "value": m,
                             "B_D": B, "err_pct": err})

    # A3. vary w_std
    print("\n  A3. Vary W_std (std Wedderburn weight):")
    for ws in [0.3, 0.5, 0.669, 0.8]:
        B = B_fd(1, 1, kahler_level=0, w_std_override=ws)
        err = abs(B - AME["D"]) / Mtot_D * 100
        print(f"    W_std = {ws}: B_D = {B:.4f}  err = {err:.4f}%")
        d_results.append({"scan": "w_std", "value": ws,
                             "B_D": B, "err_pct": err})

    # A4. vary m_pn
    print("\n  A4. Vary m_pn (inter-nucleon crossings):")
    for m_pn in [0, 1, 2, 3]:
        # m_pn=0: no inter-nucleon crossing; V̂ = just gluon
        try:
            B = B_fd(1, 1, kahler_level=0, m_pn=m_pn)
            err = abs(B - AME["D"]) / Mtot_D * 100
            print(f"    m_pn = {m_pn}: B_D = {B:.4f}  err = {err:.4f}%")
            d_results.append({"scan": "m_pn", "value": m_pn,
                                 "B_D": B, "err_pct": err})
        except Exception as e:
            print(f"    m_pn = {m_pn}: error {e}")

    # ── PART B: 20Ne via FD ────────────────────────────────────
    print("\n" + "=" * 125)
    print("PART B: LIGHT ATOMS INCLUDING 20Ne via finite-difference Kähler")
    print("=" * 125)

    ATOMS = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1),
                ("4He", 2, 2), ("6Li", 3, 3), ("7Li", 3, 4),
                ("9Be", 4, 5), ("10B", 5, 5), ("12C", 6, 6),
                ("14N", 7, 7), ("16O", 8, 8),
                ("20Ne", 10, 10)]

    print(f"\n  {'atom':>6} {'Z':>3} {'N':>3}  "
          + "  ".join(f"{'B(n=' + str(n) + ')':>10}" for n in range(5))
          + f"  {'B_AME':>10}  "
          + "  ".join(f"{'err n=' + str(n):>9}" for n in range(5))
          + "  time")
    print("  " + "-" * 150)

    atom_results = []
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        B_AME = AME[name]
        t0 = time.time()
        B_levels = []
        err_levels = []
        for k in range(5):
            B = B_fd(Z, N, kahler_level=k)
            B_levels.append(B)
            err_levels.append(abs(B - B_AME) / Mtot * 100)
        dt = time.time() - t0
        best_n = int(np.argmin(err_levels))
        row = f"  {name:>6} {Z:>3} {N:>3}  " + "  ".join(f"{b:>+10.3f}" for b in B_levels)
        row += f"  {B_AME:>+10.4f}  " + "  ".join(f"{e:>8.4f}%" for e in err_levels)
        row += f"  n={best_n}({err_levels[best_n]:.3f}%) [{dt:.1f}s]"
        print(row)
        atom_results.append({
            "atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME,
            "B_at_levels": B_levels,
            "err_at_levels_pct": err_levels,
            "best_level": best_n, "best_err_pct": err_levels[best_n],
            "time_sec": dt,
        })

    out = Path(__file__).parent / "d-revisit-and-20ne-fd.witness.json"
    out.write_text(json.dumps({
        "computation": "d-revisit-and-20ne-fd",
        "description": (
            "Part A: D sensitivity across q, m_e, W_std, m_pn. "
            "Part B: light atoms including 20Ne via finite-difference "
            "Kähler lift (numeric, no sympy). Much faster than symbolic "
            "— enables A=20 and beyond."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0_default": q0_default, "m_e_default": M_E_DEFAULT},
        "part_a_D_sensitivity": d_results,
        "part_b_all_atoms": atom_results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
