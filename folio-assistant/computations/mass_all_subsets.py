#!/usr/bin/env python3
"""
Full single-vortex mass formula with ALL subset terms (not truncated
at singletons or pairs).

Per prop:mass-endomorphism-tower §Proof: "Each subset S ⊆
{0,...,n-2} contributes a blow-up centre with spectral coordinate
∏_{i∈S} V̂_i and Markov weight z^{|S|}".

Full formula:

  m^λ(ρ) = Σ_{S ≠ ∅, S ⊆ gens} z^{|S|-1} · Φ_q(∏_{i∈S} V̂_i^λ)
          + (descended term — may be absorbed into S=full)

Applied per-irrep with Wedderburn weights; in log form:

  B = Σ_λ w_λ · m_e · Σ_{S ≠ ∅} z^{2(|S|-1)} · ln|Φ_q(∏ V̂_i^λ)|

where the log exponent 2(|S|-1) reflects the Markov weight z^|S|
translated through |Φ_q|.
"""
import sys, json, math, itertools
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV
from mass_at_3A_proper import _cached_seminormal
from hecke_characters import partitions_of

z = 1/(math.sqrt(q0) + 1/math.sqrt(q0))
h = q0 - qi0


def ln_phi_q(v, max_k=500):
    if v == 0: return 0
    s = 0
    for k in range(1, max_k+1):
        f = 1 - qi0**k * v
        if abs(f) < 1e-300: return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15: break
    return s


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


def V_char_div_dim(gen_idx, ordering, shape):
    """V̂_i^λ = χ_λ(T_i)/dim(V_λ) via seminormal."""
    try:
        sigmas, dim_irrep, _ = _cached_seminormal(shape)
    except Exception:
        return None
    if dim_irrep == 0: return None
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
        chi = float(prod.diagonal().sum())
    else:
        chi = float(np.trace(prod))
    return chi / dim_irrep


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


def B_all_subsets(Z, N, z_exponent_formula='2(|S|-1)'):
    """Full subset-sum binding formula."""
    A = Z + N
    if A < 2: return 0.0
    ordering = ground(Z, N)
    parts = list(partitions_of(A))
    dq = [dim_q_hook(list(p)) for p in parts]
    sum_dq2 = sum(d**2 for d in dq)
    weights = [d**2 / sum_dq2 for d in dq]

    n_gens = A - 1
    B = 0.0
    breakdown = []
    for pi, p in enumerate(parts):
        shape = tuple(p)
        w = weights[pi]
        # Compute V̂_i for each gen using normalized character
        V_list = []
        for gi in range(n_gens):
            V_i = V_char_div_dim(gi, ordering, shape)
            if V_i is None:
                V_i = 0.0
            V_list.append(V_i)
        # Sum over all nonempty subsets
        per_irrep_sum = 0.0
        for k in range(1, n_gens + 1):
            for subset in itertools.combinations(range(n_gens), k):
                V_prod = 1.0
                for i in subset:
                    V_prod *= V_list[i]
                if z_exponent_formula == '2(|S|-1)':
                    z_exp = 2 * (k - 1)
                elif z_exponent_formula == '|S|':
                    z_exp = k
                elif z_exponent_formula == '|S|-1':
                    z_exp = k - 1
                else:
                    z_exp = 0
                coeff = z ** z_exp
                per_irrep_sum += coeff * ln_phi_q(abs(V_prod))
        B += w * M_E_MEV * per_irrep_sum
        breakdown.append({'partition': str(p), 'weight': w,
                          'per_irrep_sum': per_irrep_sum,
                          'contrib_MeV': w * M_E_MEV * per_irrep_sum})
    return B, breakdown


AME = {'D':2.224566, 'T':8.481798, '3He':7.718058, '4He':28.295674,
       '6Li':31.994571, '7Li':39.244529, '9Be':58.164980,
       '12C':92.161728}
ATOMS = [('D',1,1), ('T',1,2), ('3He',2,1), ('4He',2,2),
         ('6Li',3,3), ('7Li',3,4), ('9Be',4,5)]

for formula in ['2(|S|-1)', '|S|-1']:
    print(f"\n{'='*100}")
    print(f"ALL-SUBSET formula with z^{formula} weight (V̂ = χ/dim)")
    print(f"{'='*100}")
    print(f"{'atom':>5} {'A':>2} {'B':>10} {'AME':>10} {'err_pct':>10}")
    print('-'*55)
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        B, _ = B_all_subsets(Z, N, z_exponent_formula=formula)
        err = abs(B - AME[name])/Mtot*100
        print(f"{name:>5} {A:>2} {B:>+10.3f} {AME[name]:>+10.4f} {err:>9.4f}%")
