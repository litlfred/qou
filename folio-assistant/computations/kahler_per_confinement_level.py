#!/usr/bin/env python3
"""
Single-level Kähler applied INDEPENDENTLY at each confinement level.

Not multi-level propagation. Each confinement level has its OWN
Kähler-jet-lifted formula, evaluated separately:

  quark level:    m_q(q) → m_q(q) + Σ (q-1)^k · ∂^k m_q / k!   [k=1..K]
  hadron level:   m_H(q) → m_H(q) + Σ (q-1)^k · ∂^k m_H / k!
  nuclear level:  B(q)   → B(q)   + Σ (q-1)^k · ∂^k B / k!     [current]
  atomic level:   A(q)   → A(q)   + Σ (q-1)^k · ∂^k A / k!

Each Kähler is applied to THAT level's closed-form q-expression.
Currently we only have Kähler at nuclear level (4He = 0.0016%).

This script adds Kähler at the HADRON level: applied to the proton
and neutron mass formulas directly. Expected effect: proton 1.8% → ?
"""
import sys, math, json
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

q_sym = sp.Symbol('q', positive=True)
HA_sym = q_sym - 1 / q_sym
z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))


def qi_sym(n): return (q_sym**n - q_sym**(-n)) / (q_sym - 1/q_sym)

def kahler_step(expr, n_orders):
    if n_orders == 0: return expr
    result = expr
    for k in range(1, n_orders + 1):
        result = result + (q_sym - 1)**k * sp.diff(expr, q_sym, k) / sp.factorial(k)
    return result


def ln_phi_q(v, max_k=500):
    if v == 0: return 0.0
    s = 0.0
    for k in range(1, max_k+1):
        f = 1.0 - (1/q0)**k * v
        if abs(f) < 1e-300: return float('inf')
        s -= math.log(abs(f))
        if abs((1/q0)**k * v) < 1e-15: break
    return s


def phi_q_sym(v_sym):
    """Φ_q(v) at a symbolic q, evaluated numerically at q=q₀.

    We can't symbolically compute Φ_q(v(q)) closed-form, so we
    evaluate numerically after Kähler step at q=q₀.
    """
    v_val = float(v_sym.subs(q_sym, q0))
    return math.exp(ln_phi_q(abs(v_val)))


# ── Proton mass formula at HADRON level ───────────────────────────────────
# Replicates mass_endomorphism.py's proton_cross, but symbolic in q.

def per_gen_V_sym(gen_idx, crossings_per_gen):
    """Symbolic V̂_full(q) for one generator — Wedderburn 3-channel."""
    # Wedderburn 3-channel weights at H_3
    qint2 = (q_sym**2 - q_sym**(-2)) / (q_sym - 1/q_sym)
    W_SYM_s = 1 / (qint2**2 + 2)
    W_STD_s = qint2**2 / (qint2**2 + 2)
    W_ALT_s = W_SYM_s

    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    for c_coef, d_coef in crossings_per_gen.get(gen_idx, []):
        c, d = sp.Rational(c_coef).limit_denominator(1000000), \
               (sp.Rational(d_coef).limit_denominator(1000000)
                if not isinstance(d_coef, sp.Expr) else d_coef)
        # If d is -h, replace with -HA_sym; our crossings store numerical h
        if d_coef < 0 and abs(d_coef + (q0 - 1/q0)) < 1e-10:
            d = -HA_sym
        elif d_coef < 0 and abs(d_coef + (q0 - 1/q0)/2) < 1e-10:
            d = -HA_sym / 2
        a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                sp.expand(a * c + b * d))
        sp_v = sp.expand(sp_v * (c * q_sym + d))
        ap_v = sp.expand(ap_v * (-c / q_sym + d))
    V_std = z_sym * a + b
    return sp.expand(W_SYM_s * sp_v + W_STD_s * V_std + W_ALT_s * ap_v)


HA_num = q0 - 1/q0

proton_cross = {
    0: [(1.0, 0.0)] * 3          # B_3 Borromean σ_0
       + [(1.0, 0.0)]            # uu
       + [(1.0, -HA_num/2)]      # ud
       + [(1.0, 0.0)] * 2,       # 2 gluon modes
    1: [(1.0, -HA_num)] * 3      # B_3 Borromean σ_1⁻¹
       + [(1.0, -HA_num/2)]      # ud
}

neutron_cross = {
    0: [(1.0, 0.0)] * 3 + [(1.0, -HA_num)] + [(1.0, -HA_num/2)]
       + [(1.0, 0.0)] * 2,
    1: [(1.0, -HA_num)] * 3 + [(1.0, -HA_num/2)]
}

electron_cross = {0: [(1.0, 0.0)] * 3}


def mass_tower_sym(n_strands, crossings, kahler_order=0):
    """Symbolic tower mass = descent + Σ Φ_q(V̂_i) + z² Σ Φ_q(V̂_i V̂_j)."""
    V_list_sym = [per_gen_V_sym(gi, crossings) for gi in range(n_strands - 1)]
    # Apply Kähler at HADRON level to each V̂_i
    V_list_kahler = [kahler_step(V, kahler_order) for V in V_list_sym]
    # Descent |∏V̂|
    prod_sym = sp.Integer(1)
    for V in V_list_kahler: prod_sym = sp.expand(prod_sym * V)
    desc_val = abs(float(prod_sym.subs(q_sym, q0)))
    # Singletons
    single_val = sum(phi_q_sym(V) for V in V_list_kahler)
    # Pairs
    cross_val = 0.0
    for i in range(len(V_list_kahler)):
        for j in range(i+1, len(V_list_kahler)):
            pair_sym = sp.expand(V_list_kahler[i] * V_list_kahler[j])
            cross_val += (1/(math.sqrt(q0) + 1/math.sqrt(q0)))**2 * \
                         phi_q_sym(pair_sym)
    return desc_val + single_val + cross_val


print("="*90)
print("KÄHLER AT HADRON LEVEL — applied to proton/neutron mass formulas")
print("="*90)
print(f"CODATA m_p = {M_P_MEV} MeV   m_n = {M_N_MEV} MeV")

# Electron reference (k=0, no Kähler at electron level for now)
e_total = mass_tower_sym(2, electron_cross, kahler_order=0)
print(f"Electron tower reference = {e_total:.4f}  (k=0)")

print(f"\n{'Kähler':>8}  {'m_p_pred':>12}  {'err_p_pct':>9}  {'m_n_pred':>12}  {'err_n_pct':>9}")
print("-"*70)

rows = []
for k in [0, 1, 2, 3]:
    try:
        p_total = mass_tower_sym(3, proton_cross, kahler_order=k)
        n_total = mass_tower_sym(3, neutron_cross, kahler_order=k)
    except Exception as e:
        print(f"  k={k}: error: {e}")
        continue
    m_p_pred = (p_total / e_total) * M_E_MEV
    m_n_pred = (n_total / e_total) * M_E_MEV
    err_p = abs(m_p_pred - M_P_MEV)/M_P_MEV*100
    err_n = abs(m_n_pred - M_N_MEV)/M_N_MEV*100
    print(f"k={k:>6}  {m_p_pred:>+12.4f}  {err_p:>8.4f}%  "
          f"{m_n_pred:>+12.4f}  {err_n:>8.4f}%")
    rows.append({
        'kahler_order': k,
        'm_p_pred': m_p_pred, 'err_p_pct': err_p,
        'm_n_pred': m_n_pred, 'err_n_pct': err_n,
    })

out = Path(__file__).parent / "kahler-per-confinement-level.witness.json"
out.write_text(json.dumps({
    "computation": "kahler-per-confinement-level",
    "description": "Kähler at HADRON confinement level (proton/neutron mass).",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "results": rows,
}, indent=2, default=str))
print(f"\nWitness: {out}")
