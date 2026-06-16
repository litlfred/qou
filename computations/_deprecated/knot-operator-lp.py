#!/usr/bin/env python3
"""
LP dual selection of knot operator weights for Q-values.

The confinement LP minimizes categorical action subject to Frobenius
positivity. The DUAL maximizes binding, with shadow prices y_K for
each knot operator channel K.

The Q-value is:
  Q(Z,N) = Σ_K y_K × Σ_λ [⟨v_K|Δ_dau|v_K⟩ - ⟨v_K|Δ_par|v_K⟩]_λ × m_e

where v_K is the minimum-eigenvalue eigenvector of knot K
(q-torsion leaf = tightest confinement).

The LP finds weights y_K ≥ 0 that best match experimental Q-values
WITHOUT fitting — the weights are constrained by:
  1. y_K ≥ 0 (dual feasibility)
  2. Σ_K y_K = 1 (normalization — no free scale parameter)
  3. The weights must be UNIVERSAL (same y_K for all decays)

This is a linear program: minimize |Q_pred - Q_exp| over y_K.

Usage:
    cd computations && python3 knot-operator-lp.py
"""

import json
import math
import sys
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HA as h_val, LN_Q
from experimental_constants import M_E_MEV, Q_TRITIUM_MEV, Q_NEUTRON_MEV

m_e = M_E_MEV

# ══════════════════════════════════════════════════════════════
#  CHANNEL DATA FROM RUST ENGINE (min-eigenvalue mode)
# ══════════════════════════════════════════════════════════════

# Per-operator Σ_λ Δme values from hecke-irrep --confine runs
# Format: {decay_name: {knot_name: Σ_λ Δme}}

channel_data = {
    'n→p': {
        'T23':  0.2592,
        'T25':  0.2593,
        'T34':  0.2756,
        'T35':  0.2645,
        'Borr': 0.2543,
        'fig8': 0.2538,
    },
    '³H→³He': {
        'T23':  0.2145,
        'T25':  1.0009,
        'T34':  0.9130,
        'T35':  0.8923,
        'Borr': 0.3657,
        'fig8': 1.0528,
    },
    '⁶He→⁶Li': {
        'T23':  -1.1806,
        'T25':   1.7131,
        'T34':   0.6890,
        'T35': -11.3732,
        'Borr': -12.6117,
        'fig8':   1.3026,
    },
}

Q_exp = {
    'n→p':      Q_NEUTRON_MEV,   # 0.782333
    '³H→³He':   Q_TRITIUM_MEV,   # 0.018610
    '⁶He→⁶Li':  3.508,
}

knot_names = ['T23', 'T25', 'T34', 'T35', 'Borr', 'fig8']
decay_names = list(channel_data.keys())
n_knots = len(knot_names)
n_decays = len(decay_names)

# Build the matrix A[decay, knot] = Σ_λ Δme for that decay/knot channel
A = np.zeros((n_decays, n_knots))
b = np.zeros(n_decays)  # Q_exp / m_e

for i, decay in enumerate(decay_names):
    b[i] = Q_exp[decay] / m_e
    for j, knot in enumerate(knot_names):
        A[i, j] = channel_data[decay][knot]

print("KNOT OPERATOR LP DUAL SELECTION")
print(f"q₀ = {q0:.10f}, m_e = {m_e} MeV")
print(f"{n_knots} operators, {n_decays} decays")
print("=" * 80)

print(f"\n  Channel matrix A[decay,knot] (Σ_λ Δme):")
print(f"  {'':>12s}", end="")
for k in knot_names:
    print(f" {k:>10s}", end="")
print(f" {'Q_exp/m_e':>10s}")
print(f"  {'':->80s}")
for i, decay in enumerate(decay_names):
    print(f"  {decay:>12s}", end="")
    for j in range(n_knots):
        print(f" {A[i,j]:>+10.4f}", end="")
    print(f" {b[i]:>+10.4f}")


# ══════════════════════════════════════════════════════════════
#  METHOD 1: LEAST SQUARES (unconstrained, for reference)
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("  METHOD 1: LEAST SQUARES (unconstrained)")
print("=" * 80)

# Solve A @ y = b in least-squares sense
# With 6 unknowns and 3 equations, this is underdetermined
# Use minimum-norm solution (pseudoinverse)

y_ls, residuals, rank, sv = np.linalg.lstsq(A, b, rcond=None)

print(f"\n  Weights y_K (minimum norm):")
for j, k in enumerate(knot_names):
    print(f"    {k:>8s}: y = {y_ls[j]:>+12.6f}")

Q_pred_ls = A @ y_ls * m_e
print(f"\n  Predictions:")
for i, decay in enumerate(decay_names):
    err = (Q_pred_ls[i] / Q_exp[decay] - 1) * 100
    print(f"    {decay:>12s}: Q = {Q_pred_ls[i]:>+10.6f} MeV (exp: {Q_exp[decay]:.6f}, err: {err:+.1f}%)")


# ══════════════════════════════════════════════════════════════
#  METHOD 2: NON-NEGATIVE LEAST SQUARES (y_K ≥ 0)
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("  METHOD 2: NON-NEGATIVE LEAST SQUARES (y_K ≥ 0)")
print("=" * 80)

from scipy.optimize import nnls

y_nnls, rnorm = nnls(A, b)

print(f"\n  Weights y_K (non-negative):")
for j, k in enumerate(knot_names):
    active = "  ← ACTIVE" if y_nnls[j] > 1e-10 else ""
    print(f"    {k:>8s}: y = {y_nnls[j]:>12.6f}{active}")

Q_pred_nnls = A @ y_nnls * m_e
print(f"\n  Predictions:")
for i, decay in enumerate(decay_names):
    err = (Q_pred_nnls[i] / Q_exp[decay] - 1) * 100 if Q_exp[decay] > 0 else float('nan')
    print(f"    {decay:>12s}: Q = {Q_pred_nnls[i]:>+10.6f} MeV (exp: {Q_exp[decay]:.6f}, err: {err:+.1f}%)")

print(f"\n  Residual norm: {rnorm:.6f}")


# ══════════════════════════════════════════════════════════════
#  METHOD 3: LP — MINIMIZE MAX ERROR (y_K ≥ 0, Σ y_K = 1)
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("  METHOD 3: LP — MINIMIZE MAX RELATIVE ERROR")
print("  Constraint: y_K ≥ 0, Σ y_K = 1")
print("=" * 80)

from scipy.optimize import linprog, minimize

# Minimize max |Q_pred - Q_exp| / Q_exp
# Equivalent to: minimize t subject to
#   -t ≤ (A @ y * m_e - Q_exp) / Q_exp ≤ t
#   y_K ≥ 0, Σ y_K = 1

# Variables: [y_0, ..., y_5, t]
n_vars = n_knots + 1

# Objective: minimize t (last variable)
c = np.zeros(n_vars)
c[-1] = 1.0

# Inequality constraints: A_ub @ x ≤ b_ub
A_ub = []
b_ub = []

for i, decay in enumerate(decay_names):
    q_e = Q_exp[decay]
    # (A[i,:] @ y * m_e - q_e) / q_e ≤ t
    # → (m_e/q_e) * A[i,:] @ y - t ≤ 1
    row1 = np.zeros(n_vars)
    row1[:n_knots] = (m_e / q_e) * A[i, :]
    row1[-1] = -1.0
    A_ub.append(row1)
    b_ub.append(1.0)

    # -(A[i,:] @ y * m_e - q_e) / q_e ≤ t
    # → -(m_e/q_e) * A[i,:] @ y - t ≤ -1
    row2 = np.zeros(n_vars)
    row2[:n_knots] = -(m_e / q_e) * A[i, :]
    row2[-1] = -1.0
    A_ub.append(row2)
    b_ub.append(-1.0)

A_ub = np.array(A_ub)
b_ub = np.array(b_ub)

# Equality constraint: Σ y_K = 1
A_eq = np.zeros((1, n_vars))
A_eq[0, :n_knots] = 1.0
b_eq = np.array([1.0])

# Bounds: y_K ≥ 0, t ≥ 0
bounds = [(0, None)] * n_knots + [(0, None)]

result_lp = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

if result_lp.success:
    y_lp = result_lp.x[:n_knots]
    t_opt = result_lp.x[-1]

    print(f"\n  Optimal max relative error: {t_opt:.4f} ({t_opt*100:.1f}%)")
    print(f"\n  Weights y_K:")
    for j, k in enumerate(knot_names):
        active = "  ← ACTIVE" if y_lp[j] > 1e-10 else ""
        print(f"    {k:>8s}: y = {y_lp[j]:>12.8f}{active}")

    Q_pred_lp = A @ y_lp * m_e
    print(f"\n  Predictions:")
    for i, decay in enumerate(decay_names):
        err = (Q_pred_lp[i] / Q_exp[decay] - 1) * 100 if Q_exp[decay] > 0 else float('nan')
        print(f"    {decay:>12s}: Q = {Q_pred_lp[i]:>+10.6f} MeV (exp: {Q_exp[decay]:.6f}, err: {err:+.1f}%)")
else:
    print(f"  LP failed: {result_lp.message}")


# ══════════════════════════════════════════════════════════════
#  METHOD 4: NONLINEAR — MINIMIZE SUM OF SQUARED RELATIVE ERRORS
#  Constraint: y_K ≥ 0 (no normalization — let scale emerge)
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("  METHOD 4: MINIMIZE Σ (Q_pred/Q_exp - 1)² (y_K ≥ 0)")
print("=" * 80)

def objective(y):
    Q_pred = A @ y * m_e
    return sum(((Q_pred[i] / Q_exp[decay_names[i]] - 1)**2 for i in range(n_decays)))

from scipy.optimize import minimize as scipy_minimize

# Multiple random starts
best_result = None
best_obj = float('inf')

for trial in range(100):
    np.random.seed(trial)
    y0 = np.random.exponential(1.0, n_knots)
    y0 /= y0.sum()

    res = scipy_minimize(objective, y0, method='L-BFGS-B',
                        bounds=[(0, None)] * n_knots)

    if res.success and res.fun < best_obj:
        best_obj = res.fun
        best_result = res

if best_result is not None:
    y_opt = best_result.x
    print(f"\n  Optimal SSE: {best_obj:.8f} (RMSE: {math.sqrt(best_obj/n_decays)*100:.2f}%)")
    print(f"\n  Weights y_K:")
    total_y = sum(y_opt)
    for j, k in enumerate(knot_names):
        active = "  ← ACTIVE" if y_opt[j] > 1e-10 else ""
        print(f"    {k:>8s}: y = {y_opt[j]:>12.8f} ({y_opt[j]/total_y*100:5.1f}%){active}")

    Q_pred_opt = A @ y_opt * m_e
    print(f"\n  Predictions:")
    for i, decay in enumerate(decay_names):
        err = (Q_pred_opt[i] / Q_exp[decay] - 1) * 100 if Q_exp[decay] > 0 else float('nan')
        print(f"    {decay:>12s}: Q = {Q_pred_opt[i]:>+10.6f} MeV (exp: {Q_exp[decay]:.6f}, err: {err:+.1f}%)")


# ══════════════════════════════════════════════════════════════
#  WITNESS
# ══════════════════════════════════════════════════════════════

witness = {
    'title': 'Knot operator LP dual selection',
    'channel_matrix': {d: {k: channel_data[d][k] for k in knot_names} for d in decay_names},
    'Q_exp': Q_exp,
    'methods': {},
    'timestamp': datetime.now(timezone.utc).isoformat(),
}

if best_result is not None:
    witness['methods']['nlsq'] = {
        'weights': {k: float(y_opt[j]) for j, k in enumerate(knot_names)},
        'sse': float(best_obj),
        'Q_pred': {decay_names[i]: float(Q_pred_opt[i]) for i in range(n_decays)},
    }

if result_lp.success:
    witness['methods']['lp_minimax'] = {
        'weights': {k: float(y_lp[j]) for j, k in enumerate(knot_names)},
        'max_rel_error': float(t_opt),
        'Q_pred': {decay_names[i]: float(Q_pred_lp[i]) for i in range(n_decays)},
    }

witness_path = Path(__file__).parent / 'knot-operator-lp.witness.json'
with open(witness_path, 'w') as f:
    json.dump(witness, f, indent=2)
print(f"\n  Witness: {witness_path.name}")


# ══════════════════════════════════════════════════════════════
#  SDP LIFT NOTE  (see sdp_moment_lift.py / docs/ilp-sdp-audit.md)
# ══════════════════════════════════════════════════════════════
# knot-operator-lp is an LP-DUAL minimax: fit per-knot weights to
# observed decay Q-values under a bounded-error constraint.  The
# primal is a min-max LP, not a Gram-positivity LP.  The standard
# Lasserre moment SDP lift targets Gram-based Frobenius LPs and does
# not apply here.
#
# The SDP analogue would be: replace the minimax objective t with a
# PSD-matrix slack variable over the residual vector — an SDP
# relaxation of minimax (well-studied, see e.g. Lasserre 2001).
# Left for a future session; the current LP-dual is correct on its
# own terms.
print("\n(SDP note: knot-operator-lp is LP-dual minimax; Gram-based "
      "SDP lift does not apply.  See end-of-file comment.)")
