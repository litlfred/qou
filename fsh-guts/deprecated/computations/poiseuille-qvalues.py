#!/usr/bin/env python3
"""
Poiseuille flow Q-values: tube width × tube length.

The user's insight: "more complicated the crossing, the narrower
vortex tubes, slower flow." In Poiseuille (viscous) flow:

    Flow rate ∝ r⁴ / (L × η)
    Stored energy ∝ L × η / r⁴

where r = tube radius (∝ |V̂_i|), L = tube length (∝ crossings at σ_i),
η = viscosity (∝ h = q - q⁻¹).

In the Garside staircase at generator σ_i:
  - Tube width: |V̂_i| (vertex volume)
  - Tube length: (n-1-i) crossings at that generator position
  - Each crossing narrows or widens based on quark types

The stored energy functional:
  E = Σ_i (n-1-i) × g(V̂_i)

where g measures the "resistance" of the tube.

Candidates for g:
  g₁(V) = 1/V²           (Poiseuille r⁻⁴, V ∝ r²)
  g₂(V) = -log|V|         (free energy per tube)
  g₃(V) = 1/|V|           (simple inverse)
  g₄(V) = (1-V)²/V²      (deviation from unit flow)

The Q-value = |ΔE| × energy_scale

Usage:
    cd computations && python3 poiseuille-qvalues.py
"""
import math
import json
import sys
from pathlib import Path
from itertools import combinations

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, LN_Q
from experimental_constants import (
    M_E_MEV, Q_TRITIUM_MEV, Q_NEUTRON_MEV,
)

z = 1.0 / (q**0.5 + q**(-0.5))

print("POISEUILLE FLOW Q-VALUES")
print(f"q = {q:.10f}, h = {h:.10f}, z = {z:.10f}")
print("=" * 80)


def typed_d_nucleon(ti, tj):
    if ti == 'p' and tj == 'p': return 0.0
    if ti == 'n' and tj == 'n': return -h
    return -h / 2


def typed_d_quark(fi, fj):
    if fi == 'u' and fj == 'u': return 0.0
    if fi == 'd' and fj == 'd': return -h
    return -h / 2


def chain_V(ordering, gen, type_fn):
    n = len(ordering)
    a, b = 0.0, 1.0
    for j in range(gen + 1, n):
        d = type_fn(ordering[gen], ordering[j])
        new_a = a * h + a * d + b
        new_b = a + b * d
        a, b = new_a, new_b
    return z * a + b


def find_gs(Z, N, type_fn, quark_level=False):
    """Find ground state = minimum energy = maximum Φ = Σ log|V̂_i|."""
    A = Z + N
    best_phi = float('-inf')
    best_ord = None
    for pp in combinations(range(A), Z):
        if quark_level:
            ordering = []
            for i in range(A):
                if i in pp:
                    ordering.extend(['u', 'u', 'd'])
                else:
                    ordering.extend(['u', 'd', 'd'])
        else:
            ordering = ['n'] * A
            for p in pp:
                ordering[p] = 'p'
        n = len(ordering)
        phi = 0.0
        ok = True
        for i in range(n - 1):
            V = chain_V(ordering, i, type_fn)
            if abs(V) < 1e-300:
                ok = False
                break
            phi += math.log(abs(V))
        if ok and phi > best_phi:
            best_phi = phi
            best_ord = ordering[:]
    return best_ord, best_phi


def compute_poiseuille_energy(ordering, type_fn):
    """Compute Poiseuille-style stored energy.

    E = Σ_i w_i × g(V̂_i)

    where w_i = (n-1-i) = tube length at generator i.
    """
    n = len(ordering)
    vols = [chain_V(ordering, i, type_fn) for i in range(n - 1)]

    results = {}

    # g₁: 1/V² (Poiseuille)
    E1 = sum((n - 1 - i) / vols[i]**2 for i in range(n - 1) if abs(vols[i]) > 1e-300)
    results['poiseuille'] = E1

    # g₂: -log|V| (log-resistance)
    E2 = sum((n - 1 - i) * (-math.log(abs(vols[i]))) for i in range(n - 1) if abs(vols[i]) > 1e-300)
    results['log_resistance'] = E2

    # g₃: 1/|V| (simple inverse)
    E3 = sum((n - 1 - i) / abs(vols[i]) for i in range(n - 1) if abs(vols[i]) > 1e-300)
    results['simple_inverse'] = E3

    # g₄: weighted vertex volume sum (original, no length weighting)
    E4 = sum(vols[i] for i in range(n - 1))
    results['vertex_sum'] = E4

    # g₅: length-weighted vertex volume sum
    E5 = sum((n - 1 - i) * vols[i] for i in range(n - 1))
    results['weighted_vertex_sum'] = E5

    # g₆: length-weighted vertex volume DIFFERENCE from 1
    E6 = sum((n - 1 - i) * (1.0 - vols[i]) for i in range(n - 1))
    results['deficit'] = E6

    # g₇: INDIVIDUAL CROSSING contributions (not factored into vertex volumes)
    # The crossing at (gen, j) has coefficient d(gen, j)
    # Count number of each crossing type, weighted by tube length
    n_uu = n_dd = n_ud = 0
    w_uu = w_dd = w_ud = 0
    for gen in range(n - 1):
        L = n - 1 - gen  # tube length at this generator
        for j in range(gen + 1, n):
            d = type_fn(ordering[gen], ordering[j])
            if abs(d) < 1e-15:
                n_uu += 1
                w_uu += L
            elif abs(d + h) < 1e-15:
                n_dd += 1
                w_dd += L
            else:
                n_ud += 1
                w_ud += L
    results['n_uu'] = n_uu
    results['n_dd'] = n_dd
    results['n_ud'] = n_ud
    results['w_uu'] = w_uu
    results['w_dd'] = w_dd
    results['w_ud'] = w_ud

    # g₈: crossing-type weighted energy
    # d-d crossings are "narrow" (high resistance), u-u are "wide" (low resistance)
    # Energy ∝ number of narrow crossings × their length
    E8 = w_dd * h + w_ud * h / 2  # weighted by amplitude AND length
    results['crossing_energy'] = E8

    return results, vols


decays = [
    (0, 1, 1, 0, Q_NEUTRON_MEV,  'n→p'),
    (1, 2, 2, 1, Q_TRITIUM_MEV,  '³H→³He'),
    (2, 4, 3, 3, 3.508,          '⁶He→⁶Li'),
    (6, 8, 7, 7, 0.15648,        '¹⁴C→¹⁴N'),
]

Q0 = 0.78233341  # m_n - m_p - m_e


for level, type_fn, quark_flag, label in [
    ('nucleon', typed_d_nucleon, False, 'NUCLEON'),
    ('quark', typed_d_quark, True, 'QUARK'),
]:
    print(f"\n{'=' * 80}")
    print(f"  {label} LEVEL")
    print(f"{'=' * 80}")

    all_data = []

    for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
        A = Z_par + N_par
        if quark_flag and A > 6:
            continue
        if not quark_flag and A > 14:
            continue

        gs_par, _ = find_gs(Z_par, N_par, type_fn, quark_flag)
        gs_dau, _ = find_gs(Z_dau, N_dau, type_fn, quark_flag)

        E_par, V_par = compute_poiseuille_energy(gs_par, type_fn)
        E_dau, V_dau = compute_poiseuille_energy(gs_dau, type_fn)

        dB = Q_exp - Q0

        print(f"\n  {name} (A={A})")
        print(f"    Q_exp = {Q_exp:.6f} MeV, ΔB = {dB:+.4f} MeV")

        print(f"\n    {'Functional':>25s} | {'E_par':>10s} | {'E_dau':>10s} | {'ΔE':>12s}")
        print(f"    {'':->65s}")

        row = {'name': name, 'A': A, 'Q_exp': Q_exp, 'dB': dB}

        for key in ['poiseuille', 'log_resistance', 'simple_inverse',
                     'vertex_sum', 'weighted_vertex_sum', 'deficit',
                     'crossing_energy']:
            dE = E_par[key] - E_dau[key]
            print(f"    {key:>25s} | {E_par[key]:>+10.4f} | {E_dau[key]:>+10.4f} | {dE:>+12.6f}")
            row[f'dE_{key}'] = dE

        # Crossing type breakdown
        print(f"\n    Crossing types:")
        print(f"      Parent:   uu={E_par['n_uu']:>4d} (w={E_par['w_uu']:>6d}), "
              f"dd={E_par['n_dd']:>4d} (w={E_par['w_dd']:>6d}), "
              f"ud={E_par['n_ud']:>4d} (w={E_par['w_ud']:>6d})")
        print(f"      Daughter: uu={E_dau['n_uu']:>4d} (w={E_dau['w_uu']:>6d}), "
              f"dd={E_dau['n_dd']:>4d} (w={E_dau['w_dd']:>6d}), "
              f"ud={E_dau['n_ud']:>4d} (w={E_dau['w_ud']:>6d})")

        all_data.append(row)

    # Check which functional correlates with ΔB
    if len(all_data) > 1:
        nuclear = [d for d in all_data if d['A'] > 1]
        if len(nuclear) >= 2:
            print(f"\n  CORRELATION WITH ΔB (nuclear decays only):")
            for key in ['poiseuille', 'log_resistance', 'simple_inverse',
                         'vertex_sum', 'weighted_vertex_sum', 'deficit',
                         'crossing_energy']:
                col = f'dE_{key}'
                # Compute correlation
                xs = [d[col] for d in nuclear]
                ys = [d['dB'] for d in nuclear]
                n = len(xs)
                mean_x = sum(xs) / n
                mean_y = sum(ys) / n
                cov_xy = sum((xs[i] - mean_x) * (ys[i] - mean_y) for i in range(n))
                var_x = sum((xs[i] - mean_x)**2 for i in range(n))
                var_y = sum((ys[i] - mean_y)**2 for i in range(n))
                if var_x > 0 and var_y > 0:
                    corr = cov_xy / math.sqrt(var_x * var_y)
                else:
                    corr = 0

                # Regression: ΔB ≈ a × ΔE + b
                if var_x > 1e-15:
                    a = cov_xy / var_x
                    b = mean_y - a * mean_x
                    residuals = [ys[i] - (a * xs[i] + b) for i in range(n)]
                    rss = sum(r**2 for r in residuals)
                else:
                    a = b = rss = float('nan')

                print(f"    {key:>25s}: corr = {corr:+.4f}, "
                      f"ΔB ≈ {a:+.6f}×ΔE + ({b:+.4f}), RSS = {rss:.6f}")

                # If slope is well-determined, show predictions
                if abs(corr) > 0.5 and not math.isnan(a):
                    print(f"      Predictions:")
                    for d in nuclear:
                        dB_pred = a * d[col] + b
                        Q_pred = Q0 + dB_pred
                        err = (Q_pred / d['Q_exp'] - 1) * 100 if d['Q_exp'] > 0 else float('nan')
                        print(f"        {d['name']:>10s}: ΔB_pred = {dB_pred:+.4f}, "
                              f"Q_pred = {Q_pred:.4f} (exp: {d['Q_exp']:.4f}, {err:+.1f}%)")

print("\n" + "=" * 80)
print("  DONE")
print("=" * 80)
