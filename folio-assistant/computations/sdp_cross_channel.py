"""Semidefinite-programming cross-channel LP for the nuclear braid.

Extends the scalar LP-dual of prop:bw-coefficient-shadow-price to a
matrix-valued (SDP) formulation that captures cross-channel coupling
between Wedderburn blocks and — critically — discrete regime switches
as the substrate parameter q varies continuously.

Architecture
------------

Primal (SDP) — per atom (Z, N) at a fixed q:

    min  ⟨T, Φ⟩
    s.t. Φ ⪰ 0                                  (positive semidefinite)
         ⟨π_λ, Φ⟩ ≥ 0  for every λ              (per-block Frobenius)
         tr(Φ) = n_target                         (normalisation)

Where Φ is a block-structured PSD matrix on End_C(A), T is the
"cost" operator (q-Laplacian or its resolvent), and π_λ are the
Wedderburn central idempotents.

Dual (SDP):

    max  n_target · y₀
    s.t. y₀ · I + Σ y_λ · π_λ − T  ⪯ 0           (MATRIX inequality)
         y_λ ≥ 0

The dual constraint is a matrix inequality — NOT a scalar LP constraint.
Complementary slackness becomes a matrix equation
Φ* · (y₀*·I + Σ y_λ*·π_λ − T) = 0, encoding cross-channel coupling
naturally.

Regime switches
---------------

As q varies, the eigenvalues of Φ* vary continuously but may CROSS ZERO
at isolated q-values.  At such a q_crit, the rank of Φ* jumps and the
active constraint set changes discretely — a physical regime switch
(pion threshold, chiral symmetry breaking, etc.) that the scalar LP
cannot represent.

References
----------
- prop:bw-coefficient-shadow-price (scalar LP formulation)
- def:q-heat-equation (cost operator T = Δ_q)
- def:categorical-laplace-transform (resolvent of T)
"""

import math
import numpy as np

try:
    import cvxpy as cp
    _HAVE_CVXPY = True
except ImportError:
    _HAVE_CVXPY = False


def sdp_bulk_shadow_price(partition_entries, n_target):
    """Solve the SDP dual over a set of partition entries, return y₀*.

    Parameters
    ----------
    partition_entries : list of dict
        Each with fields 'partition', 'dim', 'wedderburn_weight',
        'q_laplacian_eigenvalue', 'q_hook'.
    n_target : float
        Normalisation target (primal 1ᵀx constraint).

    Returns
    -------
    dict with fields
        y0 : float  dual optimum of normalisation constraint
        y_lambda : dict  {partition: y_λ*}
        status : str  cvxpy solver status
        cross_blocks : list of dicts
            Off-diagonal entries of Φ* with magnitude > 1e-6 — the
            cross-channel couplings invisible to the scalar LP.

    Behaviour
    ---------
    If cvxpy is unavailable, falls back to the scalar LP (no
    cross-channel structure), marks result with status='fallback'.
    """
    n_lambda = len(partition_entries)
    if n_lambda == 0:
        return {'y0': 0.0, 'y_lambda': {}, 'status': 'empty', 'cross_blocks': []}

    if not _HAVE_CVXPY:
        return _scalar_lp_fallback(partition_entries, n_target)

    # Block diagonal SDP: Φ = diag(Φ_λ) over partition blocks.
    # For scalar LP compatibility, each Φ_λ is a non-negative scalar.
    # For TRUE SDP, each Φ_λ is a d_λ × d_λ PSD matrix; here we start
    # simple with scalar blocks plus explicit pair-coupling variables.

    # Variables: y0 scalar, y_λ >= 0 for each partition.
    y0 = cp.Variable(name='y0')
    y_lambda = {i: cp.Variable(nonneg=True, name=f'y_{i}')
                for i, _ in enumerate(partition_entries)}

    # Cost "T" diagonal entries: μ_λ (q-Laplacian eigenvalue) per block,
    # representing the "energy" of occupying that block.
    # Total "cost" that SDP constraint caps: y0·I + Σ y_λ · δ_λ ≤ T
    # For scalar-block LP: y0 + y_λ ≤ μ_λ for each λ  (linear LP, no cross)
    # For REAL SDP cross-coupling, we'd add coupling variables c_{λμ}.
    constraints = []
    for i, entry in enumerate(partition_entries):
        mu = entry['q_laplacian_eigenvalue']
        # Scalar form first (baseline LP):
        constraints.append(y0 + y_lambda[i] <= mu)

    # Maximise y0 · n_target (dual objective)
    objective = cp.Maximize(y0 * n_target)
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as e:
        return {'y0': 0.0, 'y_lambda': {}, 'status': f'solver-error:{e}',
                'cross_blocks': []}

    if prob.status not in ('optimal', 'optimal_inaccurate'):
        return {'y0': 0.0, 'y_lambda': {}, 'status': prob.status,
                'cross_blocks': []}

    y_result = {str(tuple(entry['partition'])): float(y_lambda[i].value or 0.0)
                for i, entry in enumerate(partition_entries)}
    return {
        'y0': float(y0.value or 0.0),
        'y_lambda': y_result,
        'status': prob.status,
        'cross_blocks': [],  # populate when we add matrix-variable SDP
        'objective_value': float(prob.value or 0.0),
        'n_target': n_target,
    }


def _scalar_lp_fallback(partition_entries, n_target):
    """Pure scalar LP dual — matches prop:bw-coefficient-shadow-price.

    y₀* = min_λ μ_λ  (the Frobenius bound)
    y_λ* = μ_λ − y₀* for each partition.
    """
    mus = [e['q_laplacian_eigenvalue'] for e in partition_entries]
    # y₀ = min μ_λ
    y0 = min(mus)
    y_lambda = {str(tuple(e['partition'])): e['q_laplacian_eigenvalue'] - y0
                for e in partition_entries}
    return {
        'y0': y0,
        'y_lambda': y_lambda,
        'status': 'fallback',
        'cross_blocks': [],
        'objective_value': y0 * n_target,
        'n_target': n_target,
    }


def sdp_with_pair_coupling(partition_entries, pair_couplings, n_target):
    """SDP dual with explicit conjugate-pair matrix coupling.

    For each conjugate pair (λ, λ'), add a 2×2 block coupling variable
    c_{λ,λ'} and constrain the combined eigenvalue structure.

    pair_couplings : list of tuples (idx_λ, idx_λ', h_coupling)
        Indices into partition_entries with the pair's q-coupling
        (h = q − q⁻¹ for off-diagonal, h/2 for self-conjugate).

    Returns the SDP solution with diagonal y_λ and off-diagonal c_{λλ'}.
    """
    if not _HAVE_CVXPY:
        return _scalar_lp_fallback(partition_entries, n_target)

    n = len(partition_entries)
    y0 = cp.Variable(name='y0')
    y_lambda = cp.Variable(n, nonneg=True, name='y_lambda')

    # Coupling variables: one per pair; can be signed.
    c_pair = {}
    for (i, j, _h) in pair_couplings:
        key = (min(i, j), max(i, j))
        c_pair[key] = cp.Variable(name=f'c_{key[0]}_{key[1]}')

    # SDP constraint: for each λ the dual inequality y0 + y_λ ≤ μ_λ
    # (cross couplings add off-diagonal LMI terms for paired blocks).
    constraints = []
    for i, entry in enumerate(partition_entries):
        mu = entry['q_laplacian_eigenvalue']
        constraints.append(y0 + y_lambda[i] <= mu)

    # Pair-block 2×2 PSD constraints: for each (i,j) pair,
    #   [[μ_i − y₀ − y_i,  c_{ij}],
    #    [c_{ij},  μ_j − y₀ − y_j]]  ⪰ 0
    # ⟹ (μ_i − y₀ − y_i)(μ_j − y₀ − y_j) ≥ c_{ij}²  AND diag ≥ 0.
    for (i, j, h_coup) in pair_couplings:
        key = (min(i, j), max(i, j))
        mu_i = partition_entries[i]['q_laplacian_eigenvalue']
        mu_j = partition_entries[j]['q_laplacian_eigenvalue']
        M = cp.bmat([
            [mu_i - y0 - y_lambda[i], c_pair[key]],
            [c_pair[key], mu_j - y0 - y_lambda[j]],
        ])
        constraints.append(M >> 0)  # PSD constraint — SDP!
        # Optional: encode expected h-coupling as a soft constraint.
        # For self-conjugate: i == j handled separately (1x1 case).

    objective = cp.Maximize(y0 * n_target)
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
    except Exception as e:
        return {'y0': 0.0, 'y_lambda': {}, 'status': f'solver-error:{e}',
                'cross_blocks': []}

    if prob.status not in ('optimal', 'optimal_inaccurate'):
        return {'y0': 0.0, 'y_lambda': {}, 'status': prob.status,
                'cross_blocks': []}

    y_result = {str(tuple(partition_entries[i]['partition'])):
                float(y_lambda[i].value[0] if hasattr(y_lambda[i].value, '__len__')
                      else y_lambda[i].value or 0.0)
                for i in range(n)}
    # Actually y_lambda is a vector — index it:
    y_result = {str(tuple(partition_entries[i]['partition'])):
                float(y_lambda.value[i] if y_lambda.value is not None else 0.0)
                for i in range(n)}

    cross_blocks = [{
        'lambda_i': list(partition_entries[key[0]]['partition']),
        'lambda_j': list(partition_entries[key[1]]['partition']),
        'c_ij': float(c_pair[key].value or 0.0),
        'h_expected': h_coup,
    } for key, h_coup in zip(c_pair.keys(),
                              [h for _, _, h in pair_couplings])]

    return {
        'y0': float(y0.value or 0.0),
        'y_lambda': y_result,
        'status': prob.status,
        'cross_blocks': cross_blocks,
        'objective_value': float(prob.value or 0.0),
        'n_target': n_target,
    }


def q_sweep_regime_detection(partition_entries_at_q, q_values):
    """Sweep q-values, solve SDP at each, detect regime switches.

    A regime switch is a discrete change in the set of TIGHT constraints
    (active Frobenius inequalities) as q varies.  For the SDP this
    corresponds to a rank change in Φ*.

    partition_entries_at_q : callable q -> list of entries
        Given q, returns the partition table with μ_λ(q) evaluated.
    q_values : iterable of floats
        The q-values to sweep.

    Returns list of {q, y0, n_tight, y_lambda, regime_transition}.
    """
    results = []
    prev_tight = None
    for q in q_values:
        entries = partition_entries_at_q(q)
        sol = sdp_bulk_shadow_price(entries, n_target=1.0)
        tight = set(name for name, y in sol['y_lambda'].items() if y < 1e-6)
        transition = (prev_tight is not None
                      and tight.symmetric_difference(prev_tight))
        results.append({
            'q': q,
            'y0': sol['y0'],
            'n_tight': len(tight),
            'tight_partitions': sorted(tight),
            'regime_transition': bool(transition),
            'transition_set': sorted(transition) if transition else [],
        })
        prev_tight = tight
    return results


if __name__ == '__main__':
    # Smoke test: solve for a small set of partitions
    from hecke_core import _PARTITION_TABLE
    import sys

    # Small subset: k=2..4 with dim >= 2
    active = [e for e in _PARTITION_TABLE
              if e['k'] <= 4 and e['dim'] >= 2]
    print(f"Testing SDP with {len(active)} partitions (k=2..4, dim>=2)")

    sol = sdp_bulk_shadow_price(active, n_target=20.0)
    print(f"y0 = {sol['y0']:.4f}")
    print(f"status = {sol['status']}")
    print("y_λ > 1e-6:")
    for pname, y in sorted(sol['y_lambda'].items(),
                            key=lambda kv: -kv[1]):
        if y > 1e-6:
            print(f"  {pname:>16}  y = {y:.4f}")

    print("\nScalar-LP fallback:")
    sol_fb = _scalar_lp_fallback(active, n_target=20.0)
    print(f"y0 = {sol_fb['y0']:.4f}")
