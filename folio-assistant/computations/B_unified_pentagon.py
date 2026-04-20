#!/usr/bin/env python3
"""
Unified single-vortex mass formula via pentagon operation.

The per-irrep mass is the Euler generating function over subsets:

    m^λ(ρ) = (1/z) · [∏_i (1 + z · Φ_q(V̂_i^λ)) - 1]

This equals Σ_{S≠∅} z^{|S|-1} · ∏_{i∈S} Φ_q(V̂_i^λ) when pentagon
operates (Φ_q multiplicative: Φ_q(uv) = Φ_q(u)Φ_q(v)).

The unified binding is:

    B(Z,N) = Σ_λ w_λ · m_e · ln|m^λ(ρ)|

**Regime crossover (structural, not case-by-case):**
- A ≤ 3: too few generators; m^λ ≈ Σ Φ_q(V̂) (linear sum regime)
- A ≥ 4: ∏ dominates; ln|m^λ| ≈ Σ ln|Φ_q(V̂)| + const (log sum regime)

Triples (|S|=3) and higher are retained — negligible at 3 decimal
places but required for 1 ppm precision.

We test TWO conventions:
  (A) Pentagon-operational: Φ_q(∏V) = ∏ Φ_q(V̂)
      → m^λ = (1/z)[∏(1+zΦ_q(V̂_i)) - 1]
  (B) Pentagon-exact: compute Φ_q on each subset product explicitly
      → m^λ = Σ_{S≠∅} z^{|S|-1} Φ_q(∏_{i∈S} V̂_i)

At A≥4 these should agree up to O(ℏ_q²); at A≤3 they diverge.
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


def phi_q(v, max_k=500):
    """Φ_q(v) = ∏_{k≥1}(1 - q^{-k} v)."""
    if v == 0: return 1.0
    p = 1.0
    for k in range(1, max_k+1):
        f = 1 - qi0**k * v
        p *= f
        if abs(qi0**k * v) < 1e-15: break
    return p


def ln_phi_q(v):
    val = phi_q(v)
    if abs(val) < 1e-300: return -float('inf')
    return math.log(abs(val))


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


def m_lambda_operational(V_list):
    """(A) Pentagon-operational: m^λ = (1/z)[∏(1+z·Φ_q(V̂)) - 1]."""
    prod = 1.0
    for V in V_list:
        prod *= (1.0 + z * phi_q(abs(V)))
    return (prod - 1.0) / z


def m_lambda_exact(V_list):
    """(B) Pentagon-exact: m^λ = Σ_{S≠∅} z^{|S|-1} Φ_q(∏V̂)."""
    n = len(V_list)
    m = 0.0
    for k in range(1, n+1):
        for S in itertools.combinations(range(n), k):
            V_prod = 1.0
            for i in S:
                V_prod *= V_list[i]
            m += (z ** (k-1)) * phi_q(abs(V_prod))
    return m


def B_unified(Z, N, mode='operational'):
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
        V_list = []
        for gi in range(n_gens):
            V_i = V_char_div_dim(gi, ordering, shape)
            V_list.append(0.0 if V_i is None else V_i)
        if mode == 'operational':
            m = m_lambda_operational(V_list)
        else:
            m = m_lambda_exact(V_list)
        if m == 0 or not math.isfinite(m):
            ln_m = 0.0
        else:
            ln_m = math.log(abs(m))
        contrib = w * M_E_MEV * ln_m
        B += contrib
        breakdown.append({'partition': str(p), 'weight': w, 'm': m,
                          'ln_m': ln_m, 'contrib': contrib})
    return B, breakdown


AME = {'D':2.224566, 'T':8.481798, '3He':7.718058, '4He':28.295674,
       '6Li':31.994571, '7Li':39.244529, '9Be':58.164980,
       '12C':92.161728}
ATOMS = [('D',1,1), ('T',1,2), ('3He',2,1), ('4He',2,2),
         ('6Li',3,3), ('7Li',3,4), ('9Be',4,5)]

for mode in ['operational', 'exact']:
    print(f"\n{'='*90}")
    print(f"UNIFIED pentagon formula, mode={mode}  (V̂=χ/dim, triples+ retained)")
    print(f"{'='*90}")
    print(f"{'atom':>5} {'A':>2} {'B':>10} {'AME':>10} {'err_pct':>10}")
    print('-'*55)
    results = []
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        B, bd = B_unified(Z, N, mode=mode)
        err = abs(B - AME[name])/Mtot*100
        print(f"{name:>5} {A:>2} {B:>+10.4f} {AME[name]:>+10.4f} {err:>9.4f}%")
        results.append({'atom': name, 'A': A, 'B': B, 'AME': AME[name],
                        'err_pct': err, 'mode': mode})
    if mode == 'operational':
        results_op = results
    else:
        results_ex = results

out = Path(__file__).parent / "B-unified-pentagon.witness.json"
out.write_text(json.dumps({
    "computation": "B-unified-pentagon",
    "description": "Unified m^λ via pentagon (Euler generating function); two modes.",
    "formula_A_operational": "m^λ = (1/z)[∏(1+z·Φ_q(V̂)) - 1]",
    "formula_B_exact": "m^λ = Σ_{S≠∅} z^{|S|-1} Φ_q(∏V̂)",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "results_operational": results_op,
    "results_exact": results_ex,
}, indent=2, default=str))
print(f"\nWitness: {out}")
