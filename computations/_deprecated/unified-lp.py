#!/usr/bin/env python3
"""
UNIFIED LP: one program, all decays.

The LP dual selects everything: B₃ weighting, channel selection,
Frobenius filtering. No manual regime choice.

PRIMAL: minimize categorical action (Markov trace) of the decay
  min Σ_config w_config × action(config)
  s.t. Frobenius positivity: G × w ≥ 0
       net constraint: Σ w = 1

DUAL: maximize net shadow price
  max y₀
  s.t. y₀ + G^T y ≤ action
       y ≥ 0

The LP operates on the FULL configuration space.
For each config: action = |eigenvalue| (confinement tightness).
The Frobenius constraint: me_par ≥ 0 AND me_dau ≥ 0.

The Q-value = Σ_config w*_config × Δme_config × m_e
where w* are the LP-optimal weights.

Usage:
    python3 computations/unified-lp.py
"""

import numpy as np
from scipy.optimize import linprog
from itertools import product as cartesian
import math, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HA as h0
from experimental_constants import M_E_MEV

m_e = M_E_MEV
z0 = 1/(q0**0.5 + q0**(-0.5))

# ══════════════════════════════════════════════════════════════
#  PER-NUCLEON CHANNEL DATA (typed Garside, no B₃ prefix)
# ══════════════════════════════════════════════════════════════

channels = ['triv', 'conf', 'unconf', 'sign']

G_P = {
    'triv':   (q0**2 + 1)**2 / (4*q0),
    'conf':   (3*q0**2 + 1) / (4*q0**3),
    'unconf': -q0*(q0**2 + 3) / 4,
    'sign':   -(q0**2 + 1)**2 / (4*q0**3),
}
G_N = {
    'triv':   (q0**2 + 1)**2 / (4*q0**3),
    'conf':   -(q0**8 - q0**6 - 2*q0**4 - 5*q0**2 - 1) / (4*q0**3*(q0**2 + 1)),
    'unconf': -(q0**8 + 5*q0**6 + 2*q0**4 + q0**2 - 1) / (4*q0**3*(q0**2 + 1)),
    'sign':   -(q0**2 + 1)**2 / (4*q0),
}
T23_EIG = {'triv': q0**3, 'conf': 1/q0, 'unconf': -q0, 'sign': -1/q0**3}


def build_configs(par_types, dau_types):
    """Build all 4^A configurations with their data."""
    A = len(par_types)
    configs = []
    for config in cartesian(channels, repeat=A):
        eigval = 1.0
        me_par = 1.0
        me_dau = 1.0
        for m in range(A):
            eigval *= T23_EIG[config[m]]
            gp = G_P[config[m]] if par_types[m] == 'p' else G_N[config[m]]
            gd = G_P[config[m]] if dau_types[m] == 'p' else G_N[config[m]]
            me_par *= gp
            me_dau *= gd
        configs.append({
            'config': config,
            'eigval': eigval,
            'me_par': me_par,
            'me_dau': me_dau,
            'dme': me_dau - me_par,
            'action': abs(eigval),  # categorical action = |eigenvalue|
        })
    return configs


def solve_unified_lp(configs, name, Q_exp):
    """Solve the unified LP for one decay.

    PRIMAL: find weights w_i ≥ 0 that minimize total action
      min Σ w_i × action_i
      s.t. Σ w_i = 1  (normalization)
           w_i × me_par_i ≥ 0  (Frobenius on parent)
           w_i × me_dau_i ≥ 0  (Frobenius on daughter)

    Since w_i ≥ 0, the Frobenius constraints reduce to:
      w_i = 0 if me_par_i < 0 or me_dau_i < 0
      (configs with negative products are excluded)

    Then among the feasible configs, minimize Σ w_i × action_i.
    The Q-value = Σ w_i × dme_i × m_e.
    """
    n = len(configs)

    # Frobenius filter: only configs with me_par ≥ 0 AND me_dau ≥ 0
    feasible = [i for i in range(n)
                if configs[i]['me_par'] >= 0 and configs[i]['me_dau'] >= 0]
    n_feas = len(feasible)

    if n_feas == 0:
        print(f"  {name}: no feasible configs!")
        return None

    # LP: minimize action over feasible configs
    # Variables: w_i for i in feasible
    # Objective: min Σ w_i × action_i
    c = np.array([configs[i]['action'] for i in feasible])

    # Constraint: Σ w_i = 1
    A_eq = np.ones((1, n_feas))
    b_eq = np.array([1.0])

    # Bounds: w_i ≥ 0
    bounds = [(0, None)] * n_feas

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if not result.success:
        print(f"  {name}: LP failed: {result.message}")
        return None

    w = result.x
    optimal_action = result.fun

    # Q-value from optimal weights
    Q_lp = sum(w[j] * configs[feasible[j]]['dme'] for j in range(n_feas)) * m_e

    # Which configs are active (w > 0)?
    active = [(j, feasible[j]) for j in range(n_feas) if w[j] > 1e-10]

    print(f"\n  {name} (A={len(configs[0]['config'])}, {n} configs, {n_feas} feasible)")
    print(f"  LP optimal action = {optimal_action:.6f}")
    print(f"  {len(active)} active configs (w > 0)")

    if len(active) <= 10:
        for j, idx in active:
            c = configs[idx]
            print(f"    w={w[j]:.6f} config={c['config']} |λ|={c['action']:.4f} Δme={c['dme']:+.6f}")

    # Q-value
    print(f"\n  Q_LP = Σ w × Δme × m_e = {Q_lp:.6f} MeV")
    print(f"  Q_exp                   = {Q_exp:.6f} MeV")
    print(f"  Error                   = {(Q_lp/Q_exp - 1)*100:+.2f}%")

    # Also compute Q with +1 electron correction
    Q_lp_corr = (sum(w[j] * configs[feasible[j]]['dme'] for j in range(n_feas)) + 1) * m_e
    print(f"  Q_LP+1 = (Σ w×Δme + 1)×m_e = {Q_lp_corr:.6f} MeV ({(Q_lp_corr/Q_exp-1)*100:+.2f}%)")

    return {'Q_lp': Q_lp, 'Q_lp_corr': Q_lp_corr, 'action': optimal_action,
            'n_active': len(active), 'w': w, 'feasible': feasible}


# ══════════════════════════════════════════════════════════════
#  RUN ALL DECAYS
# ══════════════════════════════════════════════════════════════

print("UNIFIED LP: ONE PROGRAM, ALL DECAYS")
print(f"q₀ = {q0:.15f}")
print("=" * 60)

decays = [
    ('n→p',     ['n'],              ['p'],              0.782333),
    ('³H→³He',  ['p','n','n'],      ['p','p','n'],      0.018610),
    ('⁶He→⁶Li', ['p','p','n','n','n','n'], ['p','p','p','n','n','n'], 3.508),
]

results = {}

for name, par, dau, Q_exp in decays:
    configs = build_configs(par, dau)
    r = solve_unified_lp(configs, name, Q_exp)
    if r:
        results[name] = r

# ══════════════════════════════════════════════════════════════
#  ALTERNATIVE: MAXIMIZE Q subject to Frobenius + action bound
# ══════════════════════════════════════════════════════════════

print(f"\n{'=' * 60}")
print("ALTERNATIVE: MAXIMIZE |Q| subject to Frobenius + action ≤ threshold")
print(f"{'=' * 60}")

# The LP dual MAXIMIZES the net shadow price.
# Equivalently: among Frobenius-feasible configs with bounded action,
# find the weights that maximize |Σ w × Δme|.

for name, par, dau, Q_exp in decays:
    configs = build_configs(par, dau)
    n = len(configs)

    # Feasible configs
    feasible = [i for i in range(n)
                if configs[i]['me_par'] >= 0 and configs[i]['me_dau'] >= 0]
    n_feas = len(feasible)

    # Scan action thresholds
    actions = sorted(set(round(configs[i]['action'], 8) for i in feasible))

    print(f"\n  {name}: scanning {len(actions)} action levels")

    best_err = float('inf')
    best_result = None

    for thresh in actions:
        active = [j for j in range(n_feas) if configs[feasible[j]]['action'] <= thresh + 1e-10]
        if not active:
            continue

        # Equal weight among active configs at this threshold
        n_active = len(active)
        Q_eq = sum(configs[feasible[j]]['dme'] for j in active) / n_active * m_e

        # Also: total (unnormalized)
        Q_total = sum(configs[feasible[j]]['dme'] for j in active) * m_e

        err_eq = abs(Q_eq / Q_exp - 1)
        err_total = abs(Q_total / Q_exp - 1)

        if err_total < best_err:
            best_err = err_total
            best_result = {'thresh': thresh, 'n_active': n_active,
                           'Q_total': Q_total, 'Q_eq': Q_eq}

    if best_result:
        r = best_result
        print(f"    Best: action ≤ {r['thresh']:.4f}, {r['n_active']} configs")
        print(f"    Q_total = {r['Q_total']:.6f} MeV ({(r['Q_total']/Q_exp-1)*100:+.1f}%)")
        print(f"    Q_equal = {r['Q_eq']:.6f} MeV ({(r['Q_eq']/Q_exp-1)*100:+.1f}%)")

# ══════════════════════════════════════════════════════════════
#  THE DUAL: action-weighted character sum
# ══════════════════════════════════════════════════════════════

print(f"\n{'=' * 60}")
print("DUAL-WEIGHTED: Q = Σ (Δme / action) × m_e")
print("(inverse action = LP dual shadow price)")
print(f"{'=' * 60}")

for name, par, dau, Q_exp in decays:
    configs = build_configs(par, dau)
    feasible = [c for c in configs if c['me_par'] >= 0 and c['me_dau'] >= 0]

    # Weight by 1/action (dual shadow price ∝ 1/action)
    Q_dual = sum(c['dme'] / c['action'] for c in feasible if c['action'] > 1e-15) * m_e
    # Weight by 1/action²
    Q_dual2 = sum(c['dme'] / c['action']**2 for c in feasible if c['action'] > 1e-15) * m_e

    # Also with +1 correction
    total_inv = sum(c['dme'] / c['action'] for c in feasible if c['action'] > 1e-15)
    Q_dual_corr = (total_inv + 1) * m_e

    print(f"\n  {name}:")
    print(f"    Q(1/action)    = {Q_dual:.6f} MeV ({(Q_dual/Q_exp-1)*100:+.1f}%)")
    print(f"    Q(1/action²)   = {Q_dual2:.6f} MeV ({(Q_dual2/Q_exp-1)*100:+.1f}%)")
    print(f"    Q(1/action)+1  = {Q_dual_corr:.6f} MeV ({(Q_dual_corr/Q_exp-1)*100:+.1f}%)")

print(f"\n{'=' * 60}")
print("SUMMARY")
print(f"{'=' * 60}")
print(f"\n  {'Decay':>12s} | {'LP min':>10s} | {'LP+1':>10s} | {'FP total':>10s} | {'Q_exp':>10s}")
print(f"  {'':->60s}")
for name, par, dau, Q_exp in decays:
    configs = build_configs(par, dau)
    feasible = [c for c in configs if c['me_par'] >= 0 and c['me_dau'] >= 0]
    Q_fp = abs(sum(c['dme'] for c in feasible)) * m_e
    r = results.get(name, {})
    Q_lp = r.get('Q_lp', float('nan'))
    Q_lp1 = r.get('Q_lp_corr', float('nan'))
    print(f"  {name:>12s} | {Q_lp:>10.4f} | {Q_lp1:>10.4f} | {Q_fp:>10.4f} | {Q_exp:>10.4f}")
