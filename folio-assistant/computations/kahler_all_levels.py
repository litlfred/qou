#!/usr/bin/env python3
"""
Kähler lift at ALL confinement levels simultaneously.

Architecture:

  quark   →(Kähler n_q orders)→   hadron   →(Kähler n_h orders)→   nuclear   →(Kähler n_a orders)→ atom
  (H_3)                           (per-nucleon V̂)                  (atom V̂)                       (observables)

Each level transition accumulates Kähler jets. The operator V̂ at
the nuclear level is:

  V̂_nuclear(q) = [V̂_quark(q) + (q-1)·∂_q V̂_quark + ... to order n_q]
               embedded in hadron, then Kähler-lifted another n_h orders,
               embedded in atom, then n_a orders.

Total Kähler order N = n_q + n_h + n_a must equal some target.

Existing kahler_single_level_all.py applies only n_a (nuclear-level).
This script propagates Kähler through quark and hadron levels too.

For tractability: track V̂ as a symbolic sympy expression; apply
Kähler step at each level as a symbolic differentiation + q-weighted
addition; evaluate at q=q₀ at the end.
"""
import sys, math, json
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
    if v == 0: return 0.0
    s = 0.0
    for k in range(1, max_k+1):
        f = 1.0 - qi0**k * v
        if abs(f) < 1e-300: return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15: break
    return s


def kahler_step(expr_sym, n_orders: int):
    """Apply n_orders of Kähler jet to a symbolic q-expression."""
    if n_orders == 0: return expr_sym
    result = expr_sym
    for k in range(1, n_orders + 1):
        deriv_k = sp.diff(expr_sym, q_sym, k)
        result = result + (q_sym - 1)**k * deriv_k / sp.factorial(k)
    return result


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1: return (sp.Integer(1), sp.Integer(0))
    elif ti == 0 and tj == 0: return (sp.Integer(1), -HA_sym)
    else: return (sp.Integer(1), -HA_sym / 2)


def V_gen_sym_per_level(gen_idx, ordering,
                         n_quark: int, n_hadron: int, n_nuclear: int,
                         sigma0_p=2, sigma0_n=4):
    """Compute V̂ at nuclear level, applying Kähler at each sub-level.

    Quark level: build σ-products with Kähler at n_quark order.
    Hadron level: apply inter-nucleon crossings, Kähler n_hadron.
    Nuclear level: compose into Wedderburn 3-channel sum, Kähler n_nuclear.
    """
    A = len(ordering)

    # ── Quark level: product of σ's for this nucleon's quark structure ──
    g_count = sigma0_p if ordering[gen_idx] == 1 else sigma0_n
    # Wedderburn channels at quark level
    a_q, b_q = sp.Integer(0), sp.Integer(1)
    sp_q, ap_q = sp.Integer(1), sp.Integer(1)
    for _ in range(g_count):
        a_q, b_q = (sp.expand(a_q * HA_sym + b_q), a_q)
        sp_q = sp.expand(sp_q * q_sym)
        ap_q = sp.expand(ap_q * (-1/q_sym))
    # Apply Kähler at QUARK level to each channel
    a_q = kahler_step(a_q, n_quark)
    b_q = kahler_step(b_q, n_quark)
    sp_q = kahler_step(sp_q, n_quark)
    ap_q = kahler_step(ap_q, n_quark)

    # ── Hadron level: append inter-nucleon flavor crossings ──
    a_h, b_h = a_q, b_q
    sp_h, ap_h = sp_q, ap_q
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        a_h, b_h = (sp.expand(a_h * c * HA_sym + a_h * d + b_h * c),
                    sp.expand(a_h * c + b_h * d))
        sp_h = sp.expand(sp_h * (c * q_sym + d))
        ap_h = sp.expand(ap_h * (-c / q_sym + d))
    # Kähler at HADRON level
    a_h = kahler_step(a_h, n_hadron)
    b_h = kahler_step(b_h, n_hadron)
    sp_h = kahler_step(sp_h, n_hadron)
    ap_h = kahler_step(ap_h, n_hadron)

    # ── Nuclear level: Wedderburn 3-channel combination ──
    V_std = z_sym * a_h + b_h
    V_full = W_SYM * sp_h + W_STD * V_std + W_ALT * ap_h
    V_full = kahler_step(sp.expand(V_full), n_nuclear)
    return V_full


def ground(Z, N):
    o=[]; pi=ni=0
    for _ in range(Z+N):
        if pi<Z and (ni>=N or pi/max(Z,1)<=ni/max(N,1)): o.append(1); pi+=1
        else: o.append(0); ni+=1
    return o


def B_multilevel_kahler(Z, N, n_quark, n_hadron, n_nuclear,
                         sigma0_p=2, sigma0_n=4):
    A = Z + N
    if A < 2: return 0.0
    ordering = ground(Z, N)
    B = 0.0
    for gi in range(A - 1):
        V = V_gen_sym_per_level(gi, ordering, n_quark, n_hadron,
                                 n_nuclear, sigma0_p, sigma0_n)
        V_val = float(V.subs(q_sym, q0))
        B += M_E_MEV * ln_phi_q(abs(V_val))
    return B


AME = {'D':2.224566, 'T':8.481798, '3He':7.718058, '4He':28.295674}
ATOMS = [('D',1,1), ('T',1,2), ('3He',2,1), ('4He',2,2)]

print("="*90)
print("KÄHLER AT ALL CONFINEMENT LEVELS (quark, hadron, nuclear)")
print("="*90)
print(f"{'atom':>5}  {'n_q':>3} {'n_h':>3} {'n_n':>3}  {'B_pred':>10}  "
      f"{'AME':>10}  {'err_pct':>8}")
print("-"*70)

rows = []
# Test key configs: single-level only, all-levels at k=1, all-levels at k=2
configs = [
    (0, 0, 0, "none"),
    (0, 0, 3, "nuclear only k=3"),
    (1, 1, 1, "all levels k=1"),
    (0, 1, 2, "hadron+nuclear"),
    (1, 0, 2, "quark+nuclear"),
    (1, 1, 2, "all k=1 + extra nuclear"),
]
for n_q, n_h, n_n, label in configs:
    print(f"\n-- {label} (n_q={n_q}, n_h={n_h}, n_n={n_n}) --")
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        try:
            B = B_multilevel_kahler(Z, N, n_q, n_h, n_n)
            err = abs(B - AME[name])/Mtot*100
        except Exception as e:
            B, err = float('nan'), float('nan')
        print(f"{name:>5}  {n_q:>3} {n_h:>3} {n_n:>3}  {B:>+10.4f}  "
              f"{AME[name]:>+10.4f}  {err:>7.4f}%")
        rows.append({'atom': name, 'A': A, 'n_quark': n_q, 'n_hadron': n_h,
                     'n_nuclear': n_n, 'B_pred': B, 'AME': AME[name],
                     'err_pct': err, 'config_label': label})

out = Path(__file__).parent / "kahler-all-levels.witness.json"
out.write_text(json.dumps({
    "computation": "kahler-all-levels",
    "description": "Kähler lift at quark, hadron, nuclear confinement levels.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "results": rows,
}, indent=2, default=str))
print(f"\nWitness: {out}")
