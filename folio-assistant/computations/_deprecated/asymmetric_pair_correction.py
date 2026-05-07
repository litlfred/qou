#!/usr/bin/env python3
"""
ASYMMETRIC-PAIR CORRECTION: bridge T, ³He under-binding.

Current scorecard with inter-gen direct + Wigner + Z=N k=3A:
  D    +3.86  vs AME +2.22  (+73%)   sign correct
  T    +3.19  vs AME +8.48  (-62%)   under-bound
  ³He  +3.19  vs AME +7.72  (-59%)   under-bound
  ⁴He +36.86  vs AME +28.30 (+30%)   sign correct

Hypothesis: the Wigner (2,2)⊢4 correction handles only T=0 isoscalar
pn pairs.  Same-flavor pp and nn pairs (T=1 isovector) need their
own correction — possibly via the same partition or a different
self-conjugate structure.

Try: add a SAME-FLAVOR pair contribution
  Δ_SF = -m_e · H_q((2,2)) · (n_pp + n_nn) / A
where n_pp = Z(Z-1)/2, n_nn = N(N-1)/2.

  D      : 0 + 0 = 0,        Δ_SF = 0
  T      : 0 + 1 = 1,        Δ_SF = -6.29·1/3 = -2.10
  ³He    : 1 + 0 = 1,        Δ_SF = -6.29·1/3 = -2.10
  ⁴He    : 1 + 1 = 2,        Δ_SF = -6.29·2/4 = -3.14

Test impact on all four.
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
    if not lam: return tuple()
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
    print("ASYMMETRIC-PAIR CORRECTION (T=1 isovector pp + nn)")
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

    delta_W_unit = me * q3 * q2**2  # Wigner unit at q_0 (~6.29 MeV)

    # Pre-compute k=3A self-conjugate sums (Scheme C)
    k3A_sums = {}
    for n in [3, 6, 9, 12]:
        sc = self_conjugate(n)
        s = sum(hook_product_q(lam) / dim_q_lam(lam) for lam in sc)
        k3A_sums[n] = s

    # Several SF correction variants
    sf_models = {
        'A: -m_e*Hq_22*(n_pp+n_nn)/A': lambda Z, N, A: -float(delta_W_unit) * (
            (Z*(Z-1)//2 + N*(N-1)//2) / A) if A>0 else 0,
        'B: same but full pair count': lambda Z, N, A: -float(delta_W_unit) * (
            (Z*(Z-1)//2 + N*(N-1)//2)) if A>0 else 0,
        'C: A != Z*A asym only':       lambda Z, N, A: -float(delta_W_unit) * (
            (Z*(Z-1)//2 + N*(N-1)//2) / A) if (Z != N and A>0) else 0,
        'D: Z != N, full pair count':  lambda Z, N, A: -float(delta_W_unit) * (
            (Z*(Z-1)//2 + N*(N-1)//2)) if (Z != N and A>0) else 0,
        'E: Z != N, /(A-1)':           lambda Z, N, A: -float(delta_W_unit) * (
            (Z*(Z-1)//2 + N*(N-1)//2) / (A-1)) if (Z != N and A>1) else 0,
    }

    for sf_name, sf_fn in sf_models.items():
        print(f"  Variant: {sf_name}")
        print(f"  {'iso':<8} {'binding':>10} {'D_W':>8} {'D_3A':>8} {'D_SF':>8} "
              f"{'M_pred':>10} {'B_pred':>10} {'B_AME':>10} {'B err':>10}")
        for name, Z, N, M_ref, B_ame in ISOTOPES:
            A = Z + N
            P1, P2, P3 = phi_inter_gen(Z, N)
            binding = float(alpha_bind) * (float(P1) - 2*float(q3)*float(P2) + float(HA2)*float(P3))
            delta_W = -float(delta_W_unit) * (min(Z, N) / A) if (A>=2 and Z>=1 and N>=1) else 0.0
            n_str = 3*A
            delta_3A = (-float(me) * float(k3A_sums.get(n_str, 0)) * (min(Z, N)/A)
                          if (Z == N and A >= 2) else 0.0)
            delta_SF = sf_fn(Z, N, A)
            M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
            M_pred = M_free + binding + delta_W + delta_3A + delta_SF
            err_M = (M_pred - M_ref) / M_ref * 100
            B_pred = -(binding + delta_W + delta_3A + delta_SF)
            err_B = ((B_pred - B_ame) / B_ame * 100) if B_ame != 0 else 0
            print(f"  {name:<8} {binding:>+10.4f} {delta_W:>+8.4f} {delta_3A:>+8.4f} "
                  f"{delta_SF:>+8.4f} {M_pred:>10.4f} {B_pred:>+10.4f} "
                  f"{B_ame:>+10.4f} {err_B:>+9.2f}%")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
