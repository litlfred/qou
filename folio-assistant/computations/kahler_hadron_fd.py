#!/usr/bin/env python3
"""
Kähler at HADRON level via finite differences (numerical, fast).

Evaluates V̂(q) at multiple numerical q values near q₀, fits a
polynomial, takes analytical derivatives, and builds the Kähler jet:

  V̂^{(k)}(q₀) = V̂(q₀) + Σ_{j=1..k} (q-1)^j · V̂^{(j)}(q₀) / j!

For proton/neutron mass at hadron level. Avoids symbolic sympy
overhead that times out on full proton braid.
"""
import sys, math, json
from pathlib import Path
from datetime import datetime, timezone
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV


def ln_phi_q(v, q, max_k=500):
    qi = 1/q
    if v == 0: return 0.0
    s = 0.0
    for k in range(1, max_k+1):
        f = 1.0 - qi**k * v
        if abs(f) < 1e-300: return float('inf')
        s -= math.log(abs(f))
        if abs(qi**k * v) < 1e-15: break
    return s


def per_gen_V_at_q(gen_idx, crossings_per_gen, q):
    """Numerical V̂_full(q) via Wedderburn 3-channel at given q."""
    qi_v = 1/q
    HA_v = q - qi_v
    qint2 = (q**2 - qi_v**2) / (q - qi_v)
    W_SYM = 1 / (qint2**2 + 2)
    W_STD = qint2**2 / (qint2**2 + 2)
    W_ALT = W_SYM
    z = 1 / (math.sqrt(q) + 1/math.sqrt(q))

    a, b = 0.0, 1.0
    sp_v, ap_v = 1.0, 1.0
    for c, d in crossings_per_gen.get(gen_idx, []):
        # d may be stored as numerical at original q0 — use the
        # same FORMULA at new q. Crossing coeffs: (1,0)=uu sym;
        # (1,-h)=dd antisym; (1,-h/2)=ud mixed. Re-derive based on
        # the stored d at q0:
        d_at_q0 = d
        if abs(d_at_q0) < 1e-12: d_new = 0.0
        elif abs(d_at_q0 + (q0 - qi0)) < 1e-10: d_new = -HA_v
        elif abs(d_at_q0 + (q0 - qi0)/2) < 1e-10: d_new = -HA_v/2
        else: d_new = d_at_q0  # literal

        a, b = a * c * HA_v + a * d_new + b * c, a * c + b * d_new
        sp_v *= c * q + d_new
        ap_v *= -c / q + d_new
    V_std = z * a + b
    return W_SYM * sp_v + W_STD * V_std + W_ALT * ap_v


def mass_tower_at_q(n_strands, crossings, q):
    V_list = [per_gen_V_at_q(gi, crossings, q)
              for gi in range(n_strands - 1)]
    prod = 1.0
    for V in V_list: prod *= V
    desc = abs(prod)
    single = sum(math.exp(ln_phi_q(abs(V), q)) for V in V_list)
    cross = 0.0
    z = 1 / (math.sqrt(q) + 1/math.sqrt(q))
    for i in range(len(V_list)):
        for j in range(i+1, len(V_list)):
            cross += z**2 * math.exp(ln_phi_q(abs(V_list[i] * V_list[j]), q))
    return desc + single + cross


def kahler_jet_fd(f, q_center, n_orders, eps=1e-4):
    """Apply Kähler jet f^{(n_orders)}(q) via finite differences.

    f^{(k)}(q_c) ≈ (k-th derivative) computed via central differences.
    Returns f(q_c) + Σ_k (q_c - 1)^k · f^{(k)}(q_c) / k!
    """
    # Central differences: f^(1)(q) = (f(q+ε) - f(q-ε)) / 2ε
    # f^(2)(q) = (f(q+ε) - 2f(q) + f(q-ε)) / ε²
    # f^(3)(q) = (f(q+2ε) - 2f(q+ε) + 2f(q-ε) - f(q-2ε)) / 2ε³
    # f^(4)(q) = (f(q+2ε) - 4f(q+ε) + 6f(q) - 4f(q-ε) + f(q-2ε)) / ε⁴

    f_m2 = f(q_center - 2*eps)
    f_m1 = f(q_center - eps)
    f_0 = f(q_center)
    f_p1 = f(q_center + eps)
    f_p2 = f(q_center + 2*eps)

    derivs = [f_0]  # 0th
    if n_orders >= 1:
        derivs.append((f_p1 - f_m1) / (2*eps))
    if n_orders >= 2:
        derivs.append((f_p1 - 2*f_0 + f_m1) / eps**2)
    if n_orders >= 3:
        derivs.append((f_p2 - 2*f_p1 + 2*f_m1 - f_m2) / (2*eps**3))
    if n_orders >= 4:
        derivs.append((f_p2 - 4*f_p1 + 6*f_0 - 4*f_m1 + f_m2) / eps**4)

    result = f_0
    for k in range(1, min(n_orders, 4) + 1):
        result += (q_center - 1)**k * derivs[k] / math.factorial(k)
    return result


HA_num = q0 - qi0

proton_cross = {
    0: [(1.0, 0.0)] * 3 + [(1.0, 0.0)] + [(1.0, -HA_num/2)] + [(1.0, 0.0)] * 2,
    1: [(1.0, -HA_num)] * 3 + [(1.0, -HA_num/2)]
}

neutron_cross = {
    0: [(1.0, 0.0)] * 3 + [(1.0, -HA_num)] + [(1.0, -HA_num/2)] + [(1.0, 0.0)] * 2,
    1: [(1.0, -HA_num)] * 3 + [(1.0, -HA_num/2)]
}

electron_cross = {0: [(1.0, 0.0)] * 3}


print("="*90)
print("KÄHLER AT HADRON LEVEL (finite differences) applied to m_p, m_n")
print("="*90)
print(f"CODATA m_p = {M_P_MEV} MeV  m_n = {M_N_MEV} MeV")

# Electron reference
e_total = mass_tower_at_q(2, electron_cross, q0)
print(f"Electron tower (no Kähler) = {e_total:.4f}")

print(f"\n{'Kähler k':>8}  {'m_p_pred':>12}  {'err_p_pct':>9}  "
      f"{'m_n_pred':>12}  {'err_n_pct':>9}  {'Δm_np':>9}")
print("-"*85)

rows = []
for k in [0, 1, 2, 3, 4]:
    try:
        p_total = kahler_jet_fd(
            lambda q: mass_tower_at_q(3, proton_cross, q), q0, k)
        n_total = kahler_jet_fd(
            lambda q: mass_tower_at_q(3, neutron_cross, q), q0, k)
    except Exception as e:
        p_total, n_total = float('nan'), float('nan')
    m_p_pred = (p_total / e_total) * M_E_MEV
    m_n_pred = (n_total / e_total) * M_E_MEV
    err_p = abs(m_p_pred - M_P_MEV)/M_P_MEV*100
    err_n = abs(m_n_pred - M_N_MEV)/M_N_MEV*100
    dm = m_n_pred - m_p_pred
    print(f"{k:>8}  {m_p_pred:>+12.4f}  {err_p:>8.4f}%  "
          f"{m_n_pred:>+12.4f}  {err_n:>8.4f}%  {dm:>+9.4f}")
    rows.append({'k': k, 'm_p': m_p_pred, 'err_p_pct': err_p,
                 'm_n': m_n_pred, 'err_n_pct': err_n,
                 'delta_mn_mp': dm})

print(f"\n(CODATA Δm_np = +1.2933 MeV)")

out = Path(__file__).parent / "kahler-hadron-fd.witness.json"
out.write_text(json.dumps({
    "computation": "kahler-hadron-fd",
    "description": "Kähler at hadron confinement level via finite differences.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "results": rows,
}, indent=2, default=str))
print(f"\nWitness: {out}")
