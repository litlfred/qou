#!/usr/bin/env python3
"""
The std channel has a pentagon-suppression threshold at A=4.

Per user's "what IS special about A < 4 in the Hecke tower?":

H_n(q) Wedderburn decomposition:
  H_2: 2 irreps (sym, alt — both 1-dim). NO std.
  H_3: 3 irreps — sym, std (2-dim), alt. std has 2 generators.
  H_4+: std has 3+ generators.

The std channel's ln|Φ_q(V^std)| contribution requires pentagon-
identity cancellations (prop:pentagon-ascension-bound) for the
O(hbar_q^2) R-factor residual to suppress spurious contributions.
Pentagon needs 3+ elements, achievable only at A >= 4.

Empirical signature: dropping std channel (keeping w_sym = w_alt =
0.1655, setting w_std = 0) improves A <= 3 dramatically but
breaks A >= 4.

This script documents the threshold and proposes an A-dependent
pentagon suppression factor rho(A, std).
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


def per_gen(gen_idx, ordering):
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


def ground(Z, N):
    o = []
    pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


def rho_pentagon(A):
    """A-dependent pentagon suppression factor for the std channel.

    rho(A, std) =
      0                 if A = 2  (H_2 has no std irrep)
      [fit]             if A = 3  (pentagon incomplete, 1-pair residual)
      1                 if A >= 4 (pentagon fully operational)

    For A = 3, the fit value is TBD — empirically ~0.16 for T,
    ~0.56 for 3He from std-contribution-over-AME calibration.
    Absent a categorical derivation, fit per atom.
    """
    if A == 2:
        return 0.0
    elif A == 3:
        return None    # TBD — atom-specific fit required
    else:
        return 1.0


def B_with_rho(Z, N, rho_std):
    A = Z + N
    if A < 2:
        return 0.0
    ordering = ground(Z, N)
    Bs = Bd = Ba = 0.0
    for i in range(A - 1):
        vs, vd, va = per_gen(i, ordering)
        Bs += ln_phi_q(abs(float(vs.subs(q_sym, q0))))
        Bd += ln_phi_q(abs(float(vd.subs(q_sym, q0))))
        Ba += ln_phi_q(abs(float(va.subs(q_sym, q0))))
    return (W_SYM * M_E_MEV * Bs
              + rho_std * W_STD * M_E_MEV * Bd
              + W_ALT * M_E_MEV * Ba)


AME = {'D': (1,1,2.224566), 'T': (1,2,8.481798), '3He': (2,1,7.718058),
         '4He': (2,2,28.295674), '6Li': (3,3,31.994571),
         '7Li': (3,4,39.244529), '9Be': (4,5,58.164980),
         '10B': (5,5,64.750861), '12C': (6,6,92.161728)}


if __name__ == "__main__":
    print("=" * 120)
    print("STD-CHANNEL PENTAGON THRESHOLD at A=4")
    print("rho(A, std) = 0 at A=2, 1 at A >= 4; A=3 fit")
    print("=" * 120)

    # Step 1: verify the threshold — rho = 0 vs rho = 1 on all atoms
    print(f"\n  {'atom':>5} {'A':>2}  "
          f"{'B rho=1 (current)':>17} {'err':>9}  "
          f"{'B rho=0 (no std)':>17} {'err':>9}  "
          f"{'rho_optimal_fit':>15}")
    print("  " + "-" * 115)

    results = []
    for name, (Z, N, B_AME) in AME.items():
        A = Z + N
        Mtot = A * 938.272
        B_full = B_with_rho(Z, N, 1.0)
        B_nostd = B_with_rho(Z, N, 0.0)
        err_full = abs(B_full - B_AME) / Mtot * 100
        err_nostd = abs(B_nostd - B_AME) / Mtot * 100
        # Optimal rho: B_sym + B_alt + rho·B_std = B_AME ⟹
        #             rho = (B_AME − B_sym − B_alt) / B_std
        B_sym_plus_alt = B_nostd
        B_std_contrib = B_full - B_nostd
        if abs(B_std_contrib) < 1e-10:
            rho_opt = None
        else:
            rho_opt = (B_AME - B_sym_plus_alt) / B_std_contrib
        print(f"  {name:>5} {A:>2}  {B_full:>+17.4f} {err_full:>8.4f}%  "
              f"{B_nostd:>+17.4f} {err_nostd:>8.4f}%  "
              f"{rho_opt:>+15.4f}" if rho_opt is not None else
              f"  {name:>5} {A:>2}  {B_full:>+17.4f} {err_full:>8.4f}%  "
              f"{B_nostd:>+17.4f} {err_nostd:>8.4f}%  {'n/a':>15}")
        results.append({
            "atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME,
            "B_rho_1": B_full, "err_rho_1_pct": err_full,
            "B_rho_0": B_nostd, "err_rho_0_pct": err_nostd,
            "rho_optimal_fit": rho_opt,
        })

    # Step 2: interpret rho values
    print(f"\n  Structural reading:")
    for r in results:
        A = r["A"]
        rho = r["rho_optimal_fit"]
        if A == 2:
            note = f"H_2 has NO std irrep; rho should be 0 exactly"
            predicted = 0.0
        elif A == 3:
            note = f"pentagon incomplete (1 std pair, residual ~1); fit value"
            predicted = "?"
        else:
            note = f"pentagon operational (std has {A-1} gens); rho should → 1"
            predicted = 1.0
        flag = ""
        if predicted == 0.0 and abs(rho) < 0.15:
            flag = " ✓ matches prediction"
        elif predicted == 1.0 and abs(rho - 1) < 0.15:
            flag = " ✓ matches prediction"
        print(f"  {r['atom']:>5} (A={A}):  rho_opt = {rho:+.4f}  "
              f"[predicted: {predicted}]{flag}   {note}")

    out = Path(__file__).parent / "std-channel-pentagon-threshold.witness.json"
    out.write_text(json.dumps({
        "computation": "std-channel-pentagon-threshold",
        "description": (
            "The std channel of the 3-channel formula transitions from "
            "spurious contribution (A <= 3) to essential contribution "
            "(A >= 4) via the pentagon-identity cancellation mechanism "
            "of prop:pentagon-ascension-bound. At A=2 std irrep does "
            "not exist in H_2; at A=3 pentagon is incomplete (1 pair); "
            "at A >= 4 pentagon fully operational. Empirical rho values "
            "by atom document the transition."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "M_E_MEV": M_E_MEV,
                          "w_sym": W_SYM, "w_std": W_STD, "w_alt": W_ALT},
        "results": results,
    }, indent=2, default=str))
    print(f"\n  Witness: {out}")
