#!/usr/bin/env python3
"""
LP dual: find knot operator weights that match all Q-values simultaneously.

min |Σ w_K × Q_K(decay) - Q_exp(decay)|  for all decays
subject to: w_K ≥ 0, Σ w_K = 1
"""

import numpy as np
from scipy.optimize import linprog, minimize

# Channel data from hecke-irrep --knots (min-eigenvalue confinement)
# Rows: decays, Columns: knot operators
# Operators available for each decay depend on strand count

# n→p (3 quarks, only 2-strand knots): trefoil, cinquefoil, borromean, figure8
# ³H→³He (9 quarks): all 6
# ⁶He→⁶Li (18 quarks): all 6

# Using all 6 operators. For n→p where T34/weak unavailable, use 0.
Q_channels = np.array([
    # trefoil  cinque  T34    weak   borr   fig8
    [0.1325,  0.1325, 0.0,   0.0,   0.1327, 0.1340],  # n→p
    [0.8010,  0.7050, 0.7319, 0.7488, 0.7922, 0.7154],  # ³H→³He
    [5.5824,  0.0594, 2.4341, 0.7798, 5.6328, 2.5641],  # ⁶He→⁶Li
])

Q_exp = np.array([0.782, 0.019, 3.508])
knot_names = ["trefoil", "cinquefoil", "T34", "weak", "borromean", "figure8"]

print("=" * 70)
print("  KNOT OPERATOR LP DUAL")
print("=" * 70)

print("\n─── Channel data (MeV) ───")
print(f"  {'Knot':<14} {'n→p':>8} {'³H→³He':>8} {'⁶He→⁶Li':>8}")
print("  " + "-" * 38)
for j, name in enumerate(knot_names):
    print(f"  {name:<14} {Q_channels[0,j]:>8.4f} {Q_channels[1,j]:>8.4f} {Q_channels[2,j]:>8.4f}")
print(f"  {'Q_exp':<14} {Q_exp[0]:>8.4f} {Q_exp[1]:>8.4f} {Q_exp[2]:>8.4f}")

# ── Method 1: Least squares with non-negative weights ───────────
print("\n─── Method 1: Non-negative least squares ───")
from scipy.optimize import nnls
# Solve: Q_channels^T @ w ≈ Q_exp, w ≥ 0
# This is nnls(A, b) where A = Q_channels^T, b = Q_exp
residual_norm, w_nnls = None, None
try:
    w_nnls, residual_norm = nnls(Q_channels.T, Q_exp)
    Q_pred = Q_channels.T @ w_nnls  # Wait, dimensions: Q_channels is 3×6, we want 6 weights
    # Actually: we want w (6,) such that Q_channels @ w ≈ Q_exp (3,)
    # nnls solves Ax = b with x ≥ 0, so A = Q_channels (3×6), b = Q_exp (3,)
    # But nnls expects A to be m×n with m ≥ n. We have 3×6 (underdetermined).
    # Use minimize instead.
except:
    pass

# ── Method 2: Minimize weighted residual ─────────────────────────
print("\n─── Method 2: Constrained optimization ───")

def objective(w):
    """Sum of squared relative errors."""
    Q_pred = Q_channels @ w  # (3,) = (3×6) @ (6,)
    rel_err = (Q_pred - Q_exp) / Q_exp
    return np.sum(rel_err**2)

from scipy.optimize import minimize

# Constraints: w >= 0, sum(w) = 1
bounds = [(0, None)] * 6
constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0}]

# Try multiple starting points
best_result = None
best_obj = float('inf')

for trial in range(100):
    rng = np.random.RandomState(trial)
    w0 = rng.dirichlet(np.ones(6))
    result = minimize(objective, w0, method='SLSQP', bounds=bounds, constraints=constraints)
    if result.success and result.fun < best_obj:
        best_obj = result.fun
        best_result = result

if best_result is not None:
    w = best_result.x
    Q_pred = np.dot(Q_channels, w)

    print(f"\n  Optimal weights (Σw = {np.sum(w):.4f}):")
    for j, name in enumerate(knot_names):
        if w[j] > 1e-6:
            print(f"    {name:<14} w = {w[j]:.6f}")
        else:
            print(f"    {name:<14} w = 0 (inactive)")

    print(f"\n  {'Decay':<14} {'Q_pred':>8} {'Q_exp':>8} {'Error':>8}")
    print("  " + "-" * 38)
    for i, decay in enumerate(["n→p", "³H→³He", "⁶He→⁶Li"]):
        err = (Q_pred[i] - Q_exp[i]) / Q_exp[i] * 100
        print(f"  {decay:<14} {Q_pred[i]:>8.4f} {Q_exp[i]:>8.4f} {err:>+7.2f}%")

    print(f"\n  RMS relative error: {np.sqrt(best_obj/3)*100:.2f}%")

# ── Method 3: Signed weights (allow negative) ───────────────────
print("\n─── Method 3: Unconstrained (signed weights) ───")
# Solve Q_channels @ w = Q_exp (underdetermined, min-norm)
w_lstsq, residuals, rank, sv = np.linalg.lstsq(Q_channels, Q_exp, rcond=None)
Q_pred_lstsq = np.dot(Q_channels, w_lstsq)

print(f"  Min-norm solution (Σw = {np.sum(w_lstsq):.4f}):")
for j, name in enumerate(knot_names):
    print(f"    {name:<14} w = {w_lstsq[j]:>+.6f}")

print(f"\n  {'Decay':<14} {'Q_pred':>8} {'Q_exp':>8} {'Error':>8}")
print("  " + "-" * 38)
for i, decay in enumerate(["n→p", "³H→³He", "⁶He→⁶Li"]):
    err = (Q_pred_lstsq[i] - Q_exp[i]) / Q_exp[i] * 100
    print(f"  {decay:<14} {Q_pred_lstsq[i]:>8.4f} {Q_exp[i]:>8.4f} {err:>+7.2f}%")

print("\n" + "=" * 70)
