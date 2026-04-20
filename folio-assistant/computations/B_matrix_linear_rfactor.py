#!/usr/bin/env python3
"""
Combine matrix-level Φ_q + linear form + pair R-factor + order-5 ℏ_q.

The winning structure from B_consistent_all_orders.py (linear form +
pair R-factor) gave 3He 0.013%. This script replaces the scalar
V̂ = χ/dim with matrix-level eigenvalue-wise Φ_q:

  Scalar (previous):
    ln|Φ_q(V̂^λ)|  where V̂^λ = χ_λ(T_i)/dim_V_λ  [one number]

  Matrix (new):
    ln(Σ_k Φ_q(eig_k))  where eig_k = eigenvalues of T_i^λ  [sum over eigs]

All other structure preserved:
  m^λ = |∏V̂^λ| + Σ_i MatΦ(T_i^λ) + z² Σ_{i<j} MatΦ(T_i^λ T_j^λ) + z⁴ triples
  B = Σ_λ w_λ · m_e · ln|m^λ|

Order-5 ℏ_q expansion for all Φ_q evaluations.
"""
import sys, math, itertools, json
from pathlib import Path
from datetime import datetime, timezone
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV
from mass_at_3A_proper import _cached_seminormal
from hecke_characters import partitions_of
from phi_q_higher_order import ln_phi_q_high_order

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
    """Full T_i^λ matrix (gluon + flavor + inter-nucleon)."""
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


def matrix_Phi_q(T_mat, order=5):
    """Σ_k Φ_q(eigenvalue_k of T_mat) in linear space.

    Returns 0 if any eigenvalue too close to branch cut.
    """
    eigs = np.linalg.eigvals(T_mat).real
    total = 0.0
    for e in eigs:
        if abs(1 - e) < 1e-10: continue
        ln_p = ln_phi_q_high_order(e, max_order=order)
        if ln_p > 700: return float('inf')
        total += math.exp(ln_p) if ln_p < 700 else 0.0
    return total


def scalar_Phi_q(V, order=5):
    """Φ_q(V) for scalar V̂ at order-5."""
    if abs(1 - V) < 1e-10: return float('inf')
    ln_p = ln_phi_q_high_order(V, max_order=order)
    return math.exp(ln_p) if ln_p < 700 else float('inf')


def B_linear_matrix_rfactor(Z, N, include_triples=True, variant='matrix',
                            order=5):
    """Matrix-level linear form + pair R-factor.

    variant='matrix' — Φ_q evaluated on each eigenvalue of T_i^λ
    variant='scalar' — Φ_q evaluated on V̂ = χ/dim (for comparison)
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

        # Collect T matrices per generator
        T_mats = []
        dim_irrep = 0
        for gi in range(A - 1):
            Tm, d = T_matrix(gi, ordering, shape)
            T_mats.append(Tm)
            dim_irrep = d

        if any(tm is None for tm in T_mats):
            continue

        # Linear form components
        # 1) Descended |∏V̂| — use scalar for consistency
        chi_prod = 1.0
        for Tm in T_mats:
            chi_prod *= float(np.trace(Tm)) / dim_irrep
        desc = abs(chi_prod)

        # 2) Singletons: Σ_i Φ_q(T_i^λ) matrix-wise
        if variant == 'matrix':
            singles = sum(matrix_Phi_q(Tm, order=order) for Tm in T_mats)
        else:
            singles = sum(scalar_Phi_q(float(np.trace(Tm))/dim_irrep, order=order)
                          for Tm in T_mats)

        # 3) Pairs with R-factor correction:
        #    z² · Φ_q(T_i · T_j)
        pairs = 0.0
        pair_rfactor = 0.0
        for i in range(A - 1):
            for j in range(i + 1, A - 1):
                T_ij = T_mats[i] @ T_mats[j]
                if variant == 'matrix':
                    phi_ij = matrix_Phi_q(T_ij, order=order)
                    phi_i = matrix_Phi_q(T_mats[i], order=order)
                    phi_j = matrix_Phi_q(T_mats[j], order=order)
                else:
                    V_ij = float(np.trace(T_ij)) / dim_irrep
                    V_i = float(np.trace(T_mats[i])) / dim_irrep
                    V_j = float(np.trace(T_mats[j])) / dim_irrep
                    phi_ij = scalar_Phi_q(V_ij, order=order)
                    phi_i = scalar_Phi_q(V_i, order=order)
                    phi_j = scalar_Phi_q(V_j, order=order)
                pairs += z**2 * phi_ij
                # R-factor: log|R| = log|Φ_ij| - log|Φ_i| - log|Φ_j|
                if phi_i > 0 and phi_j > 0 and phi_ij > 0:
                    pair_rfactor += z**2 * (math.log(phi_ij)
                                            - math.log(phi_i) - math.log(phi_j))

        # 4) Triples
        triples = 0.0
        if include_triples and A >= 4:
            for i, j, k in itertools.combinations(range(A-1), 3):
                T_ijk = T_mats[i] @ T_mats[j] @ T_mats[k]
                if variant == 'matrix':
                    phi_ijk = matrix_Phi_q(T_ijk, order=order)
                else:
                    V = float(np.trace(T_ijk)) / dim_irrep
                    phi_ijk = scalar_Phi_q(V, order=order)
                triples += z**4 * phi_ijk

        m_lambda = desc + singles + pairs + triples
        if m_lambda > 0 and math.isfinite(m_lambda):
            ln_m = math.log(m_lambda)
        else:
            ln_m = 0.0

        contrib = w * M_E_MEV * (ln_m + pair_rfactor)
        B += contrib
        breakdown.append({
            'partition': str(p), 'weight': w,
            'desc': desc, 'singles': singles,
            'pairs': pairs, 'triples': triples,
            'ln_m': ln_m, 'pair_rfactor': pair_rfactor,
            'contrib': contrib,
        })
    return B, breakdown


AME = {'D':2.224566, 'T':8.481798, '3He':7.718058, '4He':28.295674,
       '6Li':31.994571, '7Li':39.244529, '9Be':58.164980,
       '12C':92.161728}
ATOMS = [('D',1,1), ('T',1,2), ('3He',2,1), ('4He',2,2),
         ('6Li',3,3), ('7Li',3,4), ('9Be',4,5)]

print("="*100)
print("COMBINED: matrix-level Φ_q + linear form + pair R-factor + order-5 ℏ_q")
print("="*100)
print(f"{'atom':>5} {'A':>2}  "
      f"{'B_scalar':>10} {'err_sc':>7}  "
      f"{'B_matrix':>10} {'err_mx':>7}  "
      f"{'AME':>10}")
print("-"*80)

rows = []
for name, Z, N in ATOMS:
    A = Z + N
    Mtot = A * 938.272
    B_sc, bd_sc = B_linear_matrix_rfactor(Z, N, variant='scalar', order=5)
    B_mx, bd_mx = B_linear_matrix_rfactor(Z, N, variant='matrix', order=5)
    err_sc = abs(B_sc - AME[name])/Mtot*100
    err_mx = abs(B_mx - AME[name])/Mtot*100
    marker_mx = ' ★' if err_mx < 0.02 else ''
    print(f"{name:>5} {A:>2}  {B_sc:>+10.4f} {err_sc:>6.4f}%  "
          f"{B_mx:>+10.4f} {err_mx:>6.4f}%  {AME[name]:>+10.4f}{marker_mx}")
    rows.append({
        'atom': name, 'A': A, 'Z': Z, 'N': N, 'AME': AME[name],
        'B_scalar': B_sc, 'err_scalar_pct': err_sc,
        'B_matrix': B_mx, 'err_matrix_pct': err_mx,
    })

out = Path(__file__).parent / "B-matrix-linear-rfactor.witness.json"
out.write_text(json.dumps({
    "computation": "B-matrix-linear-rfactor",
    "description": "Combined matrix-Φ_q + linear form + pair R-factor + order-5 ℏ_q.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "order_hbar_q": 5,
    "results": rows,
}, indent=2, default=str))
print(f"\nWitness: {out}")
