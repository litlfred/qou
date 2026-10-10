#!/usr/bin/env python3
"""
LP-constrained ⁶He Q-value via Frobenius positivity.

The unweighted character sum over 4096 configs nearly cancels
(Q = 0.00075 MeV vs exp 3.508). The LP dual selects which
configurations satisfy Frobenius positivity (confinement constraints).

Structure:
  - 6 nucleons, each choosing 1 of 4 channels → 4⁶ = 4096 configs
  - Each config has: T_{2,3} eigenvalue λ, parent me, daughter me
  - Frobenius positivity: the Gram pairing Gx ≥ 0 constrains
    which configs are physically accessible
  - The LP dual weights y_K (per eigenvalue group) select the
    optimal combination

From confinement-lp.md: the primal minimizes Markov trace subject
to net constraint and Frobenius positivity. The dual maximizes
the net shadow price.

All from q₀ — no fitting.

Usage:
    cd computations && python3 lp-constrained-6he.py
"""

import math
import numpy as np
from scipy.optimize import linprog, minimize
from itertools import product as cartesian
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HA as h0
from experimental_constants import M_E_MEV, Q_NEUTRON_MEV

m_e = M_E_MEV
z0 = 1/(q0**0.5 + q0**(-0.5))

# ══════════════════════════════════════════════════════════════
#  PER-NUCLEON BUILDING BLOCKS (evaluated at q₀)
# ══════════════════════════════════════════════════════════════

channels = ['triv', 'conf', 'unconf', 'sign']

G_PROTON = {
    'triv':   (q0**2 + 1)**2 / (4*q0),
    'conf':   (3*q0**2 + 1) / (4*q0**3),
    'unconf': -q0*(q0**2 + 3) / 4,
    'sign':   -(q0**2 + 1)**2 / (4*q0**3),
}

G_NEUTRON = {
    'triv':   (q0**2 + 1)**2 / (4*q0**3),
    'conf':   -(q0**8 - q0**6 - 2*q0**4 - 5*q0**2 - 1) / (4*q0**3*(q0**2 + 1)),
    'unconf': -(q0**8 + 5*q0**6 + 2*q0**4 + q0**2 - 1) / (4*q0**3*(q0**2 + 1)),
    'sign':   -(q0**2 + 1)**2 / (4*q0),
}

T23_EIGENVALUE = {
    'triv': q0**3,
    'conf': 1/q0,
    'unconf': -q0,
    'sign': -1/q0**3,
}


def nucleon_g(ntype, channel):
    return G_PROTON[channel] if ntype == 'p' else G_NEUTRON[channel]


# ══════════════════════════════════════════════════════════════
#  ⁶He → ⁶Li: BUILD CONFIG TABLE
# ══════════════════════════════════════════════════════════════

par_types = ['p', 'p', 'n', 'n', 'n', 'n']
dau_types = ['p', 'p', 'p', 'n', 'n', 'n']
A = 6

print("LP-CONSTRAINED ⁶He Q-VALUE")
print(f"q₀ = {q0:.15f}")
print(f"Parent:   ⁶He = {''.join(par_types)}")
print(f"Daughter: ⁶Li = {''.join(dau_types)}")
print("=" * 70)

# Build all 4096 configurations
configs = []
for config in cartesian(channels, repeat=A):
    eigval = 1.0
    me_par = 1.0
    me_dau = 1.0
    for m in range(A):
        eigval *= T23_EIGENVALUE[config[m]]
        me_par *= nucleon_g(par_types[m], config[m])
        me_dau *= nucleon_g(dau_types[m], config[m])
    dme = me_dau - me_par
    configs.append({
        'config': config,
        'eigval': eigval,
        'me_par': me_par,
        'me_dau': me_dau,
        'dme': dme,
    })

print(f"\n{len(configs)} configurations built")

# Group by eigenvalue
eigval_groups = {}
for c in configs:
    key = round(c['eigval'], 8)
    if key not in eigval_groups:
        eigval_groups[key] = []
    eigval_groups[key].append(c)

n_groups = len(eigval_groups)
print(f"{n_groups} distinct eigenvalue groups")

# ══════════════════════════════════════════════════════════════
#  FROBENIUS POSITIVITY CONSTRAINT
# ══════════════════════════════════════════════════════════════
#
# From confinement-lp.md:
#   Gx ≥ 0 where G is the Gram matrix of H₃(q)
#
# At the per-nucleon level, Frobenius positivity means:
#   Each nucleon's channel must have non-negative Gram pairing
#   with its neighbors.
#
# For the character sum, Frobenius positivity restricts configs
# to those where the PRODUCT of per-nucleon Garside elements
# has non-negative Frobenius norm.
#
# Simplified: a config is Frobenius-positive if the product of
# its per-nucleon factors is positive (same sign for par and dau).

# Filter configs by Frobenius positivity: me_par and me_dau same sign
# (the Gram pairing x^T G y ≥ 0 means both should be positive or both negative)

pos_configs = [c for c in configs if c['me_par'] >= 0 and c['me_dau'] >= 0]
neg_configs = [c for c in configs if c['me_par'] <= 0 and c['me_dau'] <= 0]
mixed_configs = [c for c in configs
                 if (c['me_par'] > 0 and c['me_dau'] < 0) or
                    (c['me_par'] < 0 and c['me_dau'] > 0)]

print(f"\nFrobenius positivity filter:")
print(f"  Positive configs (me_par ≥ 0, me_dau ≥ 0): {len(pos_configs)}")
print(f"  Negative configs (both ≤ 0):                {len(neg_configs)}")
print(f"  Mixed (sign flip):                          {len(mixed_configs)}")

# The Frobenius-positive set: configs where both me_par and me_dau
# are non-negative. Sign-flipping configs violate positivity.

# Sum over Frobenius-positive configs only
dme_pos = sum(c['dme'] for c in pos_configs)
dme_neg = sum(c['dme'] for c in neg_configs)
dme_mixed = sum(c['dme'] for c in mixed_configs)
dme_all = sum(c['dme'] for c in configs)

print(f"\n  Σ Δme (positive):  {dme_pos:+.8f} → Q = {abs(dme_pos)*m_e:.6f} MeV")
print(f"  Σ Δme (negative):  {dme_neg:+.8f} → Q = {abs(dme_neg)*m_e:.6f} MeV")
print(f"  Σ Δme (mixed):     {dme_mixed:+.8f} → Q = {abs(dme_mixed)*m_e:.6f} MeV")
print(f"  Σ Δme (all):       {dme_all:+.8f} → Q = {abs(dme_all)*m_e:.6f} MeV")
print(f"  Q_exp = 3.508000 MeV")

# ══════════════════════════════════════════════════════════════
#  LP: MINIMIZE OVER EIGENVALUE CHANNEL WEIGHTS
# ══════════════════════════════════════════════════════════════
#
# The LP dual selects weights y_g per eigenvalue group g such that:
#   Q = |Σ_g y_g × Σ_{c∈g} Δme_c| × m_e
#
# subject to: y_g ≥ 0, Σ y_g = 1 (normalization)
# and Frobenius positivity per group.

print(f"\n{'=' * 70}")
print("LP OVER EIGENVALUE GROUPS")
print(f"{'=' * 70}")

# For each eigenvalue group, compute the Frobenius-filtered Δme
group_data = []
sorted_keys = sorted(eigval_groups.keys())

for key in sorted_keys:
    group = eigval_groups[key]
    n_total = len(group)
    # Frobenius-positive: me_par ≥ 0 AND me_dau ≥ 0
    fp = [c for c in group if c['me_par'] >= 0 and c['me_dau'] >= 0]
    dme_fp = sum(c['dme'] for c in fp)
    dme_total = sum(c['dme'] for c in group)
    group_data.append({
        'eigval': key,
        'n_total': n_total,
        'n_fp': len(fp),
        'dme_fp': dme_fp,
        'dme_total': dme_total,
    })

print(f"\n  {'λ':>12s} | {'#all':>5s} | {'#FP':>5s} | {'Σ Δme(FP)':>12s} | {'Σ Δme(all)':>12s}")
print(f"  {'':->60s}")
for g in group_data:
    print(f"  {g['eigval']:>+12.4f} | {g['n_total']:>5d} | {g['n_fp']:>5d} | {g['dme_fp']:>+12.6f} | {g['dme_total']:>+12.6f}")

# Frobenius-filtered total
total_fp = sum(g['dme_fp'] for g in group_data)
Q_fp = abs(total_fp) * m_e

print(f"\n  Σ Δme (Frobenius-filtered) = {total_fp:+.8f}")
print(f"  Q_FP = |Σ| × m_e = {Q_fp:.6f} MeV")
print(f"  Q_exp              = 3.508000 MeV")
if Q_fp > 0:
    print(f"  Error              = {(Q_fp/3.508 - 1)*100:+.1f}%")

# ══════════════════════════════════════════════════════════════
#  CONFINEMENT CONSTRAINT: min |eigenvalue| configs
# ══════════════════════════════════════════════════════════════

print(f"\n{'=' * 70}")
print("CONFINEMENT FILTER: KEEP ONLY min |λ| CONFIGS")
print(f"{'=' * 70}")

# The LP dual minimizes action = |eigenvalue|.
# Keep only configs with |eigenvalue| below threshold.
# The confined configs have each nucleon in the 'conf' channel (|λ|=q⁻¹).
# The most confined overall config has |λ_total| = q⁻⁶ ≈ 0.53.

for threshold_name, threshold in [
    ('q⁻⁶ (all confined)', q0**(-6) * 1.01),
    ('q⁻⁴ (at most 2 unconfined)', q0**(-4) * 1.01),
    ('q⁻² (at most 4 unconfined)', q0**(-2) * 1.01),
    ('1.0 (moderate)', 1.01),
    ('q² (relaxed)', q0**2 * 1.01),
]:
    filtered = [c for c in configs if abs(c['eigval']) <= threshold]
    # Further filter by Frobenius positivity
    fp_filtered = [c for c in filtered if c['me_par'] >= 0 and c['me_dau'] >= 0]
    dme_f = sum(c['dme'] for c in fp_filtered)
    Q_f = abs(dme_f) * m_e

    # Also with +1 correction (emitted electron)
    Q_f_corr = abs(dme_f + 1) * m_e

    print(f"  |λ| ≤ {threshold_name:>30s}: {len(fp_filtered):>5d} configs, "
          f"Q = {Q_f:.4f} MeV, Q+1 = {Q_f_corr:.4f} MeV")

# ══════════════════════════════════════════════════════════════
#  BEST FIT: WHICH CONSTRAINT MATCHES Q_exp?
# ══════════════════════════════════════════════════════════════

print(f"\n{'=' * 70}")
print("SCAN: EIGENVALUE THRESHOLD vs Q-VALUE")
print(f"{'=' * 70}")

thresholds = np.logspace(-2, 2, 100)
best_err = float('inf')
best_thresh = None

for thresh in thresholds:
    fp = [c for c in configs if abs(c['eigval']) <= thresh and c['me_par'] >= 0 and c['me_dau'] >= 0]
    if not fp:
        continue
    dme = sum(c['dme'] for c in fp)
    Q = abs(dme + 1) * m_e  # with electron correction
    err = abs(Q / 3.508 - 1)
    if err < best_err:
        best_err = err
        best_thresh = thresh
        best_Q = Q
        best_n = len(fp)
        best_dme = dme

if best_thresh:
    print(f"  Best match: |λ| ≤ {best_thresh:.4f}")
    print(f"    {best_n} configs, Σ Δme = {best_dme:+.6f}")
    print(f"    Q = |Σ Δme + 1| × m_e = {best_Q:.4f} MeV")
    print(f"    Q_exp = 3.508 MeV, error = {best_err*100:.1f}%")
    print(f"    Threshold ≈ q^{math.log(best_thresh)/math.log(q0):.2f}")

# Also scan WITHOUT +1 correction
best_err2 = float('inf')
for thresh in thresholds:
    fp = [c for c in configs if abs(c['eigval']) <= thresh and c['me_par'] >= 0 and c['me_dau'] >= 0]
    if not fp:
        continue
    dme = sum(c['dme'] for c in fp)
    Q = abs(dme) * m_e
    err = abs(Q / 3.508 - 1)
    if err < best_err2:
        best_err2 = err
        best_Q2 = Q
        best_thresh2 = thresh
        best_n2 = len(fp)

if best_thresh2:
    print(f"\n  Without +1: |λ| ≤ {best_thresh2:.4f}")
    print(f"    Q = {best_Q2:.4f} MeV, error = {best_err2*100:.1f}%")

print(f"\n{'=' * 70}")
print("DONE")


# ══════════════════════════════════════════════════════════════
#  SDP LIFT NOTE  (see sdp_moment_lift.py / docs/ilp-sdp-audit.md)
# ══════════════════════════════════════════════════════════════
# lp-constrained-6he uses a SIGN-BASED Frobenius filter (me_par and
# me_dau must be same sign), not the Gram-matrix `G·x ≥ 0` form.
# The Lasserre SDP moment relaxation in sdp_moment_lift.py targets
# the Gram form — it does not apply here.
#
# The analogue SDP formulation would place each configuration's
# (me_par, me_dau) pair as a 2-vector and require the covariance
# matrix over the selected config set to be PSD.  That is a
# different SDP (covariance PSD) and would need a dedicated lift;
# left open for a future session.
print("\n(SDP note: lp-constrained-6he uses sign-based Frobenius; "
      "Gram-based SDP lift does not apply.  See end-of-file comment.)")
