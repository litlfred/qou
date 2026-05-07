#!/usr/bin/env python3
"""
Tighten ³He binding (+23% over) via pp-pair-specific correction.

³He has Z=2 (pp pair), T has Z=1 (no pp pair).  CODATA T-³He = +0.76 MeV
(T more bound).  Our formula gives same prediction (both +9.48 MeV).

A pp-specific (un-binding) term distinguishes ³He from T.  Try several
Hecke-derived candidates, all proportional to n_pp = Z(Z-1)/2.

Variants (all +sign = un-binding, like Coulomb repulsion):
  A: +m_e·H_q((2,1))   per pp pair       (uses self-conj k=3)
  B: +m_e·H_q((1,1,1)) per pp pair       (uses antisymmetric k=3)
  C: +m_e·H_q((2,1))/dim_q per pp pair   (Scheme C suppression)
  D: +m_e·H_q((2,2))/dim_q per pp pair   (Wigner partition with positive sign)
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
    print("³He TIGHTENING via pp-pair correction")
    print("=" * 100)
    print()

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
    Hq_21 = float(hook_product_q((2, 1)))
    Hq_111 = float(hook_product_q((1, 1, 1)))
    Hq_22 = float(hook_product_q((2, 2)))
    dq_21 = float(dim_q_lam((2, 1)))
    dq_111 = float(dim_q_lam((1, 1, 1)))
    dq_22 = float(dim_q_lam((2, 2)))

    print(f"  k=3 (2,1) self-conj:      H_q = {Hq_21:.4f}, dim_q = {dq_21:.4f}, "
          f"H_q/dim_q = {Hq_21/dq_21:.4f}")
    print(f"  k=3 (1,1,1) antisym:      H_q = {Hq_111:.4f}, dim_q = {dq_111:.4f}, "
          f"H_q/dim_q = {Hq_111/dq_111:.4f}")
    print(f"  k=4 (2,2) self-conj:      H_q = {Hq_22:.4f}, dim_q = {dq_22:.4f}, "
          f"H_q/dim_q = {Hq_22/dq_22:.4f}")
    print()

    k3A_sums = {n: sum(hook_product_q(lam)/dim_q_lam(lam)
                          for lam in self_conjugate(n))
                 for n in [3, 6, 9, 12]}

    Hq_21D_only = float(hook_product_q((2, 1)))  # for D-patch

    def base_binding(Z, N, A, P1, P2, P3):
        """Existing binding stack (no pp correction yet)."""
        binding = float(alpha_bind) * (float(P1) - 2*float(q3_q)*float(P2) + float(HA2)*float(P3))
        delta_W = -float(delta_W_unit) * (min(Z,N)/A) if (A>=2 and Z>=1 and N>=1) else 0.0
        n_str = 3*A
        delta_3A = (-float(me) * float(k3A_sums.get(n_str, 0)) * (min(Z,N)/A)
                      if (Z == N and A >= 2) else 0.0)
        delta_SF = (-float(delta_W_unit) * (Z*(Z-1)//2 + N*(N-1)//2)
                      if (Z != N and A >= 2) else 0.0)
        delta_D = (+float(me) * Hq_21D_only) if A == 2 else 0.0
        return binding + delta_W + delta_3A + delta_SF + delta_D

    variants = {
        'A: +m_e*H_q((2,1)) per n_pp':                lambda Z, N, A: +float(me) * Hq_21 * (Z*(Z-1)//2),
        'A2: +m_e*H_q((2,1)) per (n_pp + n_nn)':      lambda Z, N, A: +float(me) * Hq_21 * (Z*(Z-1)//2 + N*(N-1)//2),
        'B: +m_e*H_q((1,1,1)) per n_pp':              lambda Z, N, A: +float(me) * Hq_111 * (Z*(Z-1)//2),
        'C: +m_e*H_q((2,1))/dim per n_pp':            lambda Z, N, A: +float(me) * (Hq_21/dq_21) * (Z*(Z-1)//2),
        'D: +m_e*H_q((2,2))/dim per n_pp':            lambda Z, N, A: +float(me) * (Hq_22/dq_22) * (Z*(Z-1)//2),
    }

    for vname, vfn in variants.items():
        print(f"  Variant: {vname}")
        print(f"  {'iso':<8} {'D_pp':>10} {'B_pred':>10} {'B_AME':>10} {'B err':>10}")
        for name, Z, N, M_ref, B_ame in ISOTOPES:
            A = Z + N
            P1, P2, P3 = phi_inter_gen(Z, N)
            base = base_binding(Z, N, A, P1, P2, P3)
            delta_pp = vfn(Z, N, A)
            B_pred = -(base + delta_pp)
            err_B = ((B_pred - B_ame) / B_ame * 100) if B_ame != 0 else 0.0
            print(f"  {name:<8} {delta_pp:>+10.4f} {B_pred:>+10.4f} {B_ame:>+10.4f} {err_B:>+9.2f}%")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
