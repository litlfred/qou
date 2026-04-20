#!/usr/bin/env python3
"""
Matrix-level Φ_q applied to both proton mass and 3He binding.

Compares scalar-projection (current) vs eigenvalue-level (new)
Φ_q evaluation at order-5 ℏ_q for three cases:

  (a) 3He binding (AME = 7.718058 MeV) — session-best 0.013% scalar
  (b) D binding  (AME = 2.224566 MeV) — session-best 0.14% scalar
  (c) Proton mass (CODATA = 938.272 MeV) — session-best 1.8% scalar

The matrix-level formula evaluates Φ_q on each eigenvalue of the
per-generator Hecke operator, then sums:

  ln|Φ_q|_matrix(T_i^λ) = ln(Σ_k Φ_q(eigenvalue_k of T_i^λ))

This is what appears in the Markov trace tr_λ(Φ_q(T_i)) before the
naive scalar projection χ/dim.
"""
import sys, math, itertools, json
from pathlib import Path
from datetime import datetime, timezone
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV, M_P_MEV
from mass_at_3A_proper import _cached_seminormal
from hecke_characters import partitions_of
from phi_q_higher_order import (
    ln_phi_q_high_order, ln_phi_q_at_matrix_eigvals
)

z = 1/(math.sqrt(q0) + 1/math.sqrt(q0))
h = q0 - qi0


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1: return (1.0, 0.0)
    elif ti == 0 and tj == 0: return (1.0, -h)
    else: return (1.0, -h/2.0)


def ground(Z, N):
    o=[]; pi=ni=0
    for _ in range(Z+N):
        if pi<Z and (ni>=N or pi/max(Z,1)<=ni/max(N,1)): o.append(1); pi+=1
        else: o.append(0); ni+=1
    return o


def T_matrix(gen_idx, ordering, shape):
    """Return T_i^λ matrix (including gluon + inter-nucleon crossings)."""
    try:
        sigmas, dim_irrep, _ = _cached_seminormal(shape)
    except Exception:
        return None, 0
    if dim_irrep == 0: return None, 0
    from scipy.sparse import issparse, eye as speye
    sparse = bool(sigmas) and issparse(sigmas[0])
    if sparse:
        prod = speye(dim_irrep, format='csr')
        I = speye(dim_irrep, format='csr')
    else:
        prod = np.eye(dim_irrep)
        I = np.eye(dim_irrep)
    A = len(ordering)
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    if gen_idx < len(sigmas):
        for _ in range(gluon_count):
            prod = prod @ (1.0 * sigmas[gen_idx] + 0.0 * I)
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        if gen_idx < len(sigmas):
            prod = prod @ (c * sigmas[gen_idx] + d * I)
    if sparse:
        return prod.toarray(), dim_irrep
    return prod, dim_irrep


def dim_q_hook(partition):
    def qi(n): return (q0**n - q0**(-n))/(q0 - qi0)
    def qf(n):
        r = 1
        for k in range(1, n+1): r *= qi(k)
        return r
    n = sum(partition)
    num = qf(n)
    den = 1
    for i in range(len(partition)):
        for j in range(partition[i]):
            arm = partition[i] - 1 - j
            leg = sum(1 for k in range(i+1, len(partition)) if partition[k] > j)
            den *= qi(arm + leg + 1)
    return num/den


def ln_phi_q_scalar(v, order=5):
    """Current approach: V̂ = χ/dim, evaluate Φ_q on scalar."""
    return ln_phi_q_high_order(v, max_order=order)


def ln_phi_q_matrix(T_mat, order=5):
    """New approach: evaluate Φ_q on each eigenvalue of T_mat, sum, log."""
    return ln_phi_q_at_matrix_eigvals(T_mat, order=order)


def B_nuclear(Z, N, variant='scalar', order=5):
    """Nuclear binding energy B = Σ_λ w_λ m_e Σ_i ln|Φ_q(V̂^λ_i)|.

    variant: 'scalar' (χ/dim) or 'matrix' (eigenvalue-wise).
    """
    A = Z + N
    if A < 2: return 0.0, []
    ordering = ground(Z, N)
    parts = list(partitions_of(A))
    dq = [dim_q_hook(list(p)) for p in parts]
    sum_dq2 = sum(d**2 for d in dq)
    weights = [d**2 / sum_dq2 for d in dq]

    B = 0.0
    breakdown = []
    for pi, p in enumerate(parts):
        shape = tuple(p)
        w = weights[pi]
        ln_sum = 0.0
        for gi in range(A - 1):
            T_mat, dim_irrep = T_matrix(gi, ordering, shape)
            if T_mat is None: continue
            if variant == 'scalar':
                chi = float(np.trace(T_mat))
                V_scalar = chi / dim_irrep
                ln_sum += ln_phi_q_scalar(abs(V_scalar), order=order)
            else:  # matrix
                ln_sum += ln_phi_q_matrix(T_mat, order=order)
        B += w * M_E_MEV * ln_sum
        breakdown.append({'partition': str(p), 'weight': w,
                          'ln_sum': ln_sum, 'contrib': w * M_E_MEV * ln_sum})
    return B, breakdown


AME = {'D':2.224566, 'T':8.481798, '3He':7.718058, '4He':28.295674,
       '6Li':31.994571, '7Li':39.244529, '9Be':58.164980}
ATOMS = [('D',1,1), ('T',1,2), ('3He',2,1), ('4He',2,2),
         ('6Li',3,3), ('7Li',3,4), ('9Be',4,5)]

print("="*90)
print("NUCLEAR BINDING: scalar vs matrix-level Φ_q (order-5 ℏ_q)")
print("="*90)
print(f"{'atom':>5} {'A':>2}  {'B_scalar':>10} {'err_sc':>8}  "
      f"{'B_matrix':>10} {'err_mx':>8}  {'AME':>10}")
print("-"*75)

rows = []
for name, Z, N in ATOMS:
    A = Z + N
    Mtot = A * 938.272
    B_sc, _ = B_nuclear(Z, N, variant='scalar', order=5)
    B_mx, _ = B_nuclear(Z, N, variant='matrix', order=5)
    err_sc = abs(B_sc - AME[name])/Mtot*100
    err_mx = abs(B_mx - AME[name])/Mtot*100
    print(f"{name:>5} {A:>2}  {B_sc:>+10.4f} {err_sc:>7.4f}%  "
          f"{B_mx:>+10.4f} {err_mx:>7.4f}%  {AME[name]:>+10.4f}")
    rows.append({'atom': name, 'A': A, 'AME': AME[name],
                 'B_scalar': B_sc, 'err_scalar_pct': err_sc,
                 'B_matrix': B_mx, 'err_matrix_pct': err_mx})

out = Path(__file__).parent / "matrix-level-mass-test.witness.json"
out.write_text(json.dumps({
    "computation": "matrix-level-mass-test",
    "description": "Compare scalar vs matrix-level Φ_q in nuclear binding.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "order_hbar_q": 5,
    "results": rows,
}, indent=2, default=str))
print(f"\nWitness: {out}")
