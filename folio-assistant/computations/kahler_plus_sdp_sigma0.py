#!/usr/bin/env python3
"""
Kähler lift × SDP-optimal σ₀_p=3, σ₀_n=2 across all atoms.

Combines two session findings:
  (1) Atom-level SDP: (σ₀_p=3, σ₀_n=2) beats paper's (2,4) by 2.6×
  (2) Kähler lift (k=0..4): 4He→0.0016%, 16O→0.0085% at best levels

Tests: does Kähler + SDP-σ₀ stack multiplicatively?

Key: the existing kahler_single_level_all.py hardcodes proton=2σ₀,
neutron=4σ₀. This script replaces with (3, 2) and reruns all atoms
at Kähler levels 0..4.
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
    for k in range(1, max_k + 1):
        f = 1.0 - qi0**k * v
        if abs(f) < 1e-300: return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15: break
    return s


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1: return (sp.Integer(1), sp.Integer(0))
    elif ti == 0 and tj == 0: return (sp.Integer(1), -HA_sym)
    else: return (sp.Integer(1), -HA_sym / 2)


def per_gen_volumes_sym(gen_idx, ordering, sigma0_p=3, sigma0_n=2):
    """Symbolic per-generator V̂ with configurable σ₀ counts."""
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    A = len(ordering)
    g_count = sigma0_p if ordering[gen_idx] == 1 else sigma0_n
    gluon = [(sp.Integer(1), sp.Integer(0))] * g_count
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
    V_std = z_sym * a + b
    V_full = W_SYM * sp_v + W_STD * V_std + W_ALT * ap_v
    return sp.expand(V_full)


def ground(Z, N):
    o=[]; pi=ni=0
    for _ in range(Z+N):
        if pi<Z and (ni>=N or pi/max(Z,1)<=ni/max(N,1)): o.append(1); pi+=1
        else: o.append(0); ni+=1
    return o


def kahler_at_level(V_sym, k):
    """V̂^(k) = k-fold Kähler jet = add (q-1)^k · ∂^k V̂ / k!."""
    if k == 0:
        return V_sym
    result = V_sym
    for order in range(1, k+1):
        deriv = sp.diff(V_sym, q_sym, order)
        result = result + (q_sym - 1)**order * deriv / sp.factorial(order)
    return result


def B_kahler_sdp(Z, N, k_level, sigma0_p=3, sigma0_n=2):
    """Nuclear binding at Kähler level k, with SDP-optimal σ₀."""
    A = Z + N
    if A < 2: return 0.0
    ordering = ground(Z, N)
    B = 0.0
    for gi in range(A - 1):
        V_sym = per_gen_volumes_sym(gi, ordering, sigma0_p, sigma0_n)
        V_k = kahler_at_level(V_sym, k_level)
        V_val = float(V_k.subs(q_sym, q0))
        B += M_E_MEV * ln_phi_q(abs(V_val))
    return B


AME = {'D':2.224566, 'T':8.481798, '3He':7.718058, '4He':28.295674,
       '6Li':31.994571, '7Li':39.244529, '9Be':58.164980,
       '10B':64.750861, '12C':92.161728}
ATOMS = [('D',1,1), ('T',1,2), ('3He',2,1), ('4He',2,2),
         ('6Li',3,3), ('7Li',3,4), ('9Be',4,5),
         ('10B',5,5), ('12C',6,6)]

print("="*100)
print(f"KÄHLER × SDP-σ₀ (σ₀_p=3, σ₀_n=2) across atoms D..12C, levels 0..4")
print("="*100)
print(f"{'atom':>5} {'A':>2}  {'AME':>10}  " +
      "  ".join(f"k={k}':>10" for k in range(5)) + "  best_k  best_err")
print("-"*110)

rows = []
for name, Z, N in ATOMS:
    A = Z + N
    Mtot = A * 938.272
    B_by_k = []
    err_by_k = []
    for k in range(5):
        try:
            B = B_kahler_sdp(Z, N, k)
            err = abs(B - AME[name])/Mtot*100
        except Exception as e:
            B, err = float('nan'), float('nan')
        B_by_k.append(B)
        err_by_k.append(err)
    finite = [(k, e) for k, e in enumerate(err_by_k) if math.isfinite(e)]
    if not finite:
        best_k, best_err = -1, float('nan')
    else:
        best_k, best_err = min(finite, key=lambda x: x[1])
    Bs = "  ".join(f"{b:>9.3f}" if math.isfinite(b) else "      nan" for b in B_by_k)
    print(f"{name:>5} {A:>2}  {AME[name]:>+10.4f}  {Bs}  k={best_k}  {best_err:.4f}%")
    rows.append({'atom': name, 'A': A, 'AME': AME[name],
                 'B_by_level': B_by_k, 'err_pct_by_level': err_by_k,
                 'best_level': best_k, 'best_err_pct': best_err})

mean_best = np.mean([r['best_err_pct'] for r in rows if math.isfinite(r['best_err_pct'])])
print(f"\nMean best-level error across atoms: {mean_best:.4f}%")

# Compare to (2,4)
print(f"\nComparison to paper's (σ₀_p=2, σ₀_n=4):")
for name, Z, N in ATOMS:
    A = Z + N
    Mtot = A * 938.272
    errs_24 = []
    for k in range(5):
        try:
            B = B_kahler_sdp(Z, N, k, sigma0_p=2, sigma0_n=4)
            errs_24.append(abs(B - AME[name])/Mtot*100)
        except Exception:
            errs_24.append(float('nan'))
    best_24 = min([e for e in errs_24 if math.isfinite(e)], default=float('nan'))
    row_32 = next(r for r in rows if r['atom'] == name)
    improvement = best_24 / row_32['best_err_pct'] if row_32['best_err_pct']>0 else float('nan')
    print(f"  {name:>5}  (3,2):{row_32['best_err_pct']:.4f}%  "
          f"(2,4):{best_24:.4f}%  ratio (2,4)/(3,2) = {improvement:.2f}×")

out = Path(__file__).parent / "kahler-plus-sdp-sigma0.witness.json"
out.write_text(json.dumps({
    "computation": "kahler-plus-sdp-sigma0",
    "description": "Kähler lift + SDP-optimal σ₀ (3,2) across all atoms.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "sigma0_p": 3, "sigma0_n": 2,
    "results": rows,
    "mean_best_err_pct": mean_best,
}, indent=2, default=str))
print(f"\nWitness: {out}")
