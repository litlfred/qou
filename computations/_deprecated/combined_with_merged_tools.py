#!/usr/bin/env python3
"""
Combine merged tools with our best formula:

Base:  M(Z,N) = Z*m_p + N*m_n + Z*m_e
             + α * (Φ_1 − 2[3]_q Φ_2 + H_A² Φ_3)      [inter-gen direct]
             + Δ_W + Δ_3A + Δ_SF

Test whether adding an atom-level Wedderburn Φ_q tower contribution
(from the merged branch's `atom_level_wedderburn_tower.py`) further
reduces residual errors in T, ³He, ⁴He bindings.

The Wedderburn tower term is:
    Δ_wed = β · Σ_{λ ⊢ 3A} w_λ · Φ_q(|χ^λ(β_atom)|/dim_q V_λ)

with some scale β.  Try β = α/10, α, 10·α, -α, and inter/full modes.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from hecke_core import (h as H_A_F, z as Z_MARKOV, _step_chain_generic)
from hecke_characters import dim_q, young_hooks, partitions_of
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
H_A = Q0 - QI
me = mp.mpf(str(M_E_MEV))
z_m = mp.mpf(str(float(Z_MARKOV)))
G = mp.catalan
alpha_bind = me * 8 * G
q3_q = Q0**2 + 1 + QI**2
q2_q = Q0 + QI
HA2 = H_A**2


def q_int(n): return (Q0**n - QI**n) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for i in range(2, n+1): out *= q_int(i)
    return out


def transpose_partition(lam):
    if not lam: return tuple()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def hook_product_q(lam):
    out = mp.mpf(1)
    for h in young_hooks(lam): out *= q_int(int(h))
    return out


def dim_q_lam(lam):
    return q_fact(sum(lam)) / hook_product_q(lam)


def self_conjugate(n):
    return [tuple(lam) for lam in partitions_of(n)
             if transpose_partition(tuple(lam)) == tuple(lam)]


def chain_std_zb(chain):
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        a, b = a*(cm*H_A + dm) + b*cm, a*cm + b*dm
    return z_m * a + b


def chain_det(chain):
    D = mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        D *= (dm*(cm*H_A + dm) - cm*cm)
    return D


def chain_lambda_sym(chain):
    out = mp.mpf(1)
    for c, d in chain: out *= mp.mpf(c)*Q0 + mp.mpf(d)
    return out


def chain_lambda_alt(chain):
    out = mp.mpf(1)
    for c, d in chain: out *= -mp.mpf(c)/Q0 + mp.mpf(d)
    return out


def per_gen_chains_full(Z, N):
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    gens = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=True)
        for c, d, g in chain_k:
            gens[g].append((c, d))
    return gens


def phi_inter_gen(Z, N):
    A = Z + N
    chains = per_gen_chains_full(Z, N)
    inter_gens = [3*k + 2 for k in range(A - 1)]
    s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    for g_idx in inter_gens:
        if g_idx >= len(chains): continue
        ch = chains[g_idx]
        if not ch: continue
        v = chain_std_zb(ch); d = chain_det(ch)
        ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
        if v != 0: s1 += mp.log(mp.fabs(v))
        if d != 0: s2 += mp.log(mp.fabs(d))
        if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
    return s1, s2, s3


def main() -> int:
    print("=" * 100)
    print("COMBINED FORMULA: our best + atom-level Wedderburn tower probe")
    print("=" * 100)
    print()

    # Load pre-computed tower values from witness JSON (atom-level Wedderburn
    # is slow; use cached values from merged branch).
    have_tower = False
    tower_data = {}
    wit_path = Path(__file__).parent / "atom-level-wedderburn-tower.witness.json"
    if wit_path.exists():
        w = json.loads(wit_path.read_text())
        # Map results by label
        label_map = {'p': 'p (1H)', 'n': 'n', 'D atom': 'D',
                      'T atom': 'T', '3He atom': '³He'}
        for src, dst in label_map.items():
            if src in w.get('results', {}):
                r = w['results'][src]
                tower_data[dst] = {
                    'trM': r.get('descended_tr_M', 0.0),
                    'phi_q_sum': r.get('phi_q_atom_sum', 0.0),
                }
        have_tower = bool(tower_data)
        print(f"  Loaded tower data for: {list(tower_data.keys())}")

    AME_BIND = {'D': 2.22456612, 'T': 8.481798,
                 '³He': 7.718058, '⁴He': 28.29566}
    M_H_ATOMIC = M_P_MEV + M_E_MEV
    ISOTOPES = [
        ('p (1H)', 1, 0, M_H_ATOMIC, 0.0),
        ('n',      0, 1, M_N_MEV,    0.0),
        ('D',      1, 1, 1876.12393, AME_BIND['D']),
        ('T',      1, 2, 2809.43215, AME_BIND['T']),
        ('³He',    2, 1, 2809.41347, AME_BIND['³He']),
        ('⁴He',    2, 2, 3728.40133, AME_BIND['⁴He']),
    ]

    delta_W_unit = me * q3_q * q2_q**2

    # Pre-compute k=3A self-conjugate sums
    k3A_sums = {n: sum(hook_product_q(lam)/dim_q_lam(lam)
                          for lam in self_conjugate(n))
                 for n in [3, 6, 9, 12]}

    # Try several combinations
    # Scales for the additional Wedderburn-tower term
    scales = {
        'no_tower': 0.0,
        'beta=+alpha/10': float(alpha_bind) / 10,
        'beta=-alpha/10': -float(alpha_bind) / 10,
        'beta=+alpha/100': float(alpha_bind) / 100,
        'beta=-alpha/100': -float(alpha_bind) / 100,
    }

    for scale_name, beta in scales.items():
        print(f"  Variant: {scale_name} (β = {beta:+.4f} MeV)")
        print(f"  {'iso':<8} {'B_pred':>10} {'B_AME':>10} {'B err':>10}")
        for name, Z, N, M_ref, B_ame in ISOTOPES:
            A = Z + N
            P1, P2, P3 = phi_inter_gen(Z, N)
            binding = float(alpha_bind) * (float(P1) - 2*float(q3_q)*float(P2) + float(HA2)*float(P3))
            delta_W = -float(delta_W_unit) * (min(Z,N)/A) if (A>=2 and Z>=1 and N>=1) else 0.0
            n_str = 3*A
            delta_3A = (-float(me) * float(k3A_sums.get(n_str, 0)) * (min(Z,N)/A)
                          if (Z == N and A >= 2) else 0.0)
            delta_SF = (-float(delta_W_unit) * (Z*(Z-1)//2 + N*(N-1)//2)
                          if (Z != N and A >= 2) else 0.0)
            # NEW: tower term
            if have_tower and tower_data.get(name) is not None:
                phi_q = tower_data[name]['phi_q_sum']
                delta_tower = beta * phi_q  # negative tower tightens binding if beta < 0
            else:
                delta_tower = 0.0
            M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
            M_pred = M_free + binding + delta_W + delta_3A + delta_SF + delta_tower
            B_pred = -(binding + delta_W + delta_3A + delta_SF + delta_tower)
            err_B = ((B_pred - B_ame) / B_ame * 100) if B_ame != 0 else 0.0
            print(f"  {name:<8} {B_pred:>+10.4f} {B_ame:>+10.4f} {err_B:>+9.2f}%")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
