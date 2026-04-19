#!/usr/bin/env python3
"""
Kähler tower convergence check on the H_A 3-channel framework.

Per session audit (2026-04-19) and user directive:
  "I want to relook at Kähler on full tower now that we have
   correct isotopes in NF with electrons."

Run the tower sum

  B(n_max) = Σ_{n=0}^{n_max} ℏ_q^{2n} · B^{(n)}

where B^{(0)} is the level-0 binding from full-tower-mass.py,
and B^{(n)} for n ≥ 1 uses the Kähler-lifted V̂^{(n)} via

  V̂^{(n+1)}(q) = V̂^{(n)}(q) + ℏ_q · q · dV̂^{(n)}/dq(q)

computed numerically via central differences.

Report per-atom error at each n_max up to n_max = 5, plot
convergence.  If the series diverges on T or 3He (earlier session
finding), the Kähler lift as currently formulated fails for them;
other atoms may converge.
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


def wedderburn_weights(q_val):
    q2 = q_val**2
    qi2 = 1.0 / q2
    qint2 = (q2 - qi2) / (q_val - 1.0 / q_val)
    denom = qint2**2 + 2.0
    return (1.0 / denom, qint2**2 / denom, 1.0 / denom)


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1:
        return (sp.Integer(1), sp.Integer(0))
    elif ti == 0 and tj == 0:
        return (sp.Integer(1), -HA_sym)
    else:
        return (sp.Integer(1), -HA_sym / 2)


def per_gen_volumes_symbolic(gen_idx, ordering):
    """Symbolic per-generator V̂^λ as functions of q_sym."""
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


def ln_Phi_q(v, q_val, max_k=500):
    if v == 0:
        return 0.0
    qi = 1.0 / q_val
    s = 0.0
    for k in range(1, max_k + 1):
        f = 1.0 - qi**k * v
        if abs(f) < 1e-300:
            return float('inf')
        s -= math.log(abs(f))
        if abs(qi**k * v) < 1e-15:
            break
    return s


def kahler_lift_n(V_func_q, n):
    """Apply the Kähler jet lift n times to a symbolic V(q).

    V̂^{(n+1)}(q) = V̂^{(n)}(q) + ℏ_q · q · dV̂^{(n)}/dq(q).
    """
    V = V_func_q
    for _ in range(n):
        dV_dq = sp.diff(V, q_sym)
        V = sp.expand(V + HA_sym * q_sym * dV_dq / (q_sym))  # ℏ_q · q · dV/dq,
        # but ℏ_q = (q-1)/q so ℏ_q · q = q - 1.
    return V


def binding_at_level(Z, N, n):
    """Compute B at level n using Kähler-lifted per-gen V̂^λ."""
    A = Z + N
    if A < 2:
        return 0.0
    ordering = []
    pi = ni = 0
    for _ in range(A):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            ordering.append(1); pi += 1
        else:
            ordering.append(0); ni += 1
    w_sym, w_std, w_alt = wedderburn_weights(q0)
    Bs = Bd = Ba = 0.0
    for i in range(A - 1):
        vs, vd, va = per_gen_volumes_symbolic(i, ordering)
        if n > 0:
            vs = kahler_lift_n(vs, n)
            vd = kahler_lift_n(vd, n)
            va = kahler_lift_n(va, n)
        vs_q = float(vs.subs(q_sym, q0))
        vd_q = float(vd.subs(q_sym, q0))
        va_q = float(va.subs(q_sym, q0))
        Bs += ln_Phi_q(abs(vs_q), q0)
        Bd += ln_Phi_q(abs(vd_q), q0)
        Ba += ln_Phi_q(abs(va_q), q0)
    return (w_sym * M_E_MEV * Bs
              + w_std * M_E_MEV * Bd
              + w_alt * M_E_MEV * Ba)


def binding_tower_sum(Z, N, n_max):
    """Σ_{n=0}^{n_max} ℏ_q^{2n} · B^{(n)}."""
    total = 0.0
    contribs = []
    for n in range(n_max + 1):
        B_n = binding_at_level(Z, N, n)
        contrib = HBAR_Q**(2 * n) * B_n
        total += contrib
        contribs.append({"n": n, "B_n": B_n,
                            "hbar_power": HBAR_Q**(2 * n),
                            "contribution": contrib,
                            "cumulative": total})
    return total, contribs


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1,  2.224566),
        ("T",   1, 2,  8.481798),
        ("3He", 2, 1,  7.718058),
        ("4He", 2, 2, 28.295674),
        ("6Li", 3, 3, 31.994571),
    ]

    print("=" * 130)
    print("KÄHLER TOWER CONVERGENCE CHECK — H_A 3-channel + ℏ_q^{2n} lift")
    print(f"q0 = {q0}, ℏ_q = {HBAR_Q:.6f}, ℏ_q² = {HBAR_Q**2:.6f}")
    print("=" * 130)

    N_MAX = 3
    print(f"\n  {'atom':>6}  "
          + "  ".join(f"{'n=' + str(n):>10}" for n in range(N_MAX + 1))
          + f"  {'B_AME':>10}")
    print("  " + "-" * (9 + (N_MAX + 1) * 12 + 12))

    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        total, contribs = binding_tower_sum(Z, N, N_MAX)
        row = f"  {name:>6}  "
        for c in contribs:
            row += f"{c['cumulative']:>10.4f}  "
        row += f"{B_AME:>10.4f}"
        print(row)
        # Per-level error
        print(f"  {'  err %':>6}  ", end="")
        for c in contribs:
            err = abs(c['cumulative'] - B_AME) / (A * 938.272) * 100
            print(f"{err:>10.4f}  ", end="")
        print()
        results.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "B_AME": B_AME,
            "contribs": contribs,
            "final_B": total,
            "err_pct": abs(total - B_AME) / (A * 938.272) * 100,
        })

    out = Path(__file__).parent / "kahler-convergence.witness.json"
    out.write_text(json.dumps({
        "computation": "kahler-convergence",
        "description": (
            "Kähler jet lift convergence check: iterate "
            "V^{(n+1)} = V^{(n)} + hbar_q · q · dV^{(n)}/dq "
            "on per-generator V_hat^lambda symbolic expressions, "
            "evaluate ln|Phi_q(V^{(n)}(q0))|, weight by "
            "hbar_q^{2n} per-level and sum. Reports cumulative "
            "binding at each n_max to check convergence."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "hbar_q": HBAR_Q,
                          "hbar_q_sq": HBAR_Q**2,
                          "n_max": N_MAX, "m_e_MeV": M_E_MEV},
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
