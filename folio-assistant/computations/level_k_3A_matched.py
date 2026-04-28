#!/usr/bin/env python3
"""
LEVEL-k = 3A MATCHED scheme:

For each atom (Z, N), only include self-conjugate partitions λ ⊢ 3A
(matching the atomic strand count) with Scheme C suppression:

    Δ_total(Z, N) = -m_e · Σ_{λ ⊢ 3A, λ = λ'} (H_q(λ) / dim_q V_λ) · f(Z, N)

This is the most physical generalization: each atom "sees" only the
representations at its own Hecke level.  The Wigner (2,2) ⊢ 4
correction is added separately as the universal k=4 pn-pairing
contribution.

Combine with the per-generator inter-only Φ baseline.
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
q3 = Q0**2 + 1 + QI**2
q2 = Q0 + QI
HA2 = H_A**2


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for i in range(2, n+1):
        out *= q_int(i)
    return out


def transpose_partition(lam):
    if not lam:
        return tuple()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def hook_product_q(lam):
    out = mp.mpf(1)
    for h in young_hooks(lam):
        out *= q_int(int(h))
    return out


def dim_q_lam(lam):
    n = sum(lam)
    return q_fact(n) / hook_product_q(lam)


def self_conjugate(n):
    return [tuple(lam) for lam in partitions_of(n)
             if transpose_partition(tuple(lam)) == tuple(lam)]


# Reuse inter-only Phi from prior work (per-generator basis)
def chain_lambda_sym(chain):
    out = mp.mpf(1)
    for c, d in chain:
        out *= mp.mpf(c)*Q0 + mp.mpf(d)
    return out


def chain_lambda_alt(chain):
    out = mp.mpf(1)
    for c, d in chain:
        out *= -mp.mpf(c)/Q0 + mp.mpf(d)
    return out


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


def per_gen_chains(Z, N, include_inter=True, include_intra=True):
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    gens = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=include_inter)
        intra_g_lo = 3*k; intra_g_hi = 3*k + 1
        for c, d, g in chain_k:
            is_intra = (intra_g_lo <= g <= intra_g_hi)
            if (is_intra and include_intra) or (not is_intra and include_inter):
                gens[g].append((c, d))
    return gens


def phi_inter(Z, N):
    chains_full = per_gen_chains(Z, N)
    chains_p = per_gen_chains(1, 0, include_inter=False)
    chains_n = per_gen_chains(0, 1, include_inter=False)

    def collect(chains):
        s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for ch in chains:
            if not ch: continue
            v = chain_std_zb(ch); d = chain_det(ch)
            ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
            if v != 0: s1 += mp.log(mp.fabs(v))
            if d != 0: s2 += mp.log(mp.fabs(d))
            if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
        return s1, s2, s3

    P1f, P2f, P3f = collect(chains_full)
    P1p, P2p, P3p = collect(chains_p)
    P1n, P2n, P3n = collect(chains_n)
    return (P1f - Z*P1p - N*P1n,
             P2f - Z*P2p - N*P2n,
             P3f - Z*P3p - N*P3n)


def main() -> int:
    print("=" * 100)
    print("LEVEL-k = 3A MATCHED scheme  (Scheme C: H_q/dim_q · f)")
    print("=" * 100)
    print()

    delta_W_unit = me * q3 * q2**2  # k=4 Wigner unit, MeV
    AME_BIND = {'D': 2.22456612, 'T': 8.481798,
                 '³He': 7.718058, '⁴He': 28.29566}
    M_H_ATOMIC = M_P_MEV + M_E_MEV
    ISOTOPES = [
        ('D',   1, 1, 1876.12393, AME_BIND['D']),
        ('T',   1, 2, 2809.43215, AME_BIND['T']),
        ('³He', 2, 1, 2809.41347, AME_BIND['³He']),
        ('⁴He', 2, 2, 3728.40133, AME_BIND['⁴He']),
    ]

    # Several occupancy variants
    occ_models = {
        'min(Z,N)/A': lambda Z, N, A: min(Z, N) / A if A > 0 else 0,
        'min(Z,N)':   lambda Z, N, A: min(Z, N),
        '1/A':         lambda Z, N, A: 1/A if A > 0 else 0,
        'sqrt(min(Z,N)/A)': lambda Z, N, A: (min(Z, N) / A)**0.5 if A > 0 else 0,
        'Z=N gate * min/A': lambda Z, N, A: (min(Z, N) / A) if (Z == N and A > 0) else 0,
        'Z=N gate * 1/A':   lambda Z, N, A: (1 / A) if (Z == N and A > 0) else 0,
    }

    for occ_name, occ_fn in occ_models.items():
        print(f"  Occupancy = {occ_name}")
        print(f"  {'iso':<6} {'3A':>3} {'#λ':>3} {'Σ_λ H_q/dim_q':>15} "
              f"{'Δ_3A (MeV)':>12} {'B_pred':>10} {'B_AME':>10} {'err %':>10}")
        rows = []
        for name, Z, N, M_ref, B_ame in ISOTOPES:
            A = Z + N
            n_strands = 3 * A
            sc_lams = self_conjugate(n_strands)
            sum_ratio = mp.mpf(0)
            for lam in sc_lams:
                Hq = hook_product_q(lam)
                dq = dim_q_lam(lam)
                sum_ratio += Hq / dq
            f = occ_fn(Z, N, A)
            delta_3A = -float(me) * float(sum_ratio) * f  # negative = bound

            # Baseline: per-gen inter-only Phi + k=4 Wigner
            P1, P2, P3 = phi_inter(Z, N)
            binding = float(alpha_bind) * (float(P1) - 2*float(q3)*float(P2) + float(HA2)*float(P3))
            delta_W = -float(delta_W_unit) * min(Z, N) / A
            M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
            M_pred = M_free + binding + delta_W + delta_3A
            B_pred = -(binding + delta_W + delta_3A)
            err = (B_pred - B_ame) / B_ame * 100
            print(f"  {name:<6} {n_strands:>3} {len(sc_lams):>3} {float(sum_ratio):>15.4f} "
                  f"{delta_3A:>+12.4f} {B_pred:>+10.4f} {B_ame:>+10.4f} {err:>+9.2f}%")
            rows.append({
                'iso': name, 'Z': Z, 'N': N, 'A': A, 'n_strands': n_strands,
                'n_self_conj_partitions': len(sc_lams),
                'sum_Hq_over_dq': float(sum_ratio),
                'delta_3A_MeV': delta_3A,
                'binding_MeV': binding,
                'Wigner_MeV': delta_W,
                'M_pred_MeV': M_pred,
                'B_pred_MeV': B_pred,
                'B_AME_MeV': B_ame,
                'err_pct': err,
            })
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
