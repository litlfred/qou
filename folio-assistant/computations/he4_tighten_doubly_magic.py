#!/usr/bin/env python3
"""
Tighten ⁴He binding (+19% over) — needs ~+5.45 MeV un-binding correction
specific to doubly-magic Z=N=2 nuclei.

Currently:
  binding (3-term) = -0.53
  Δ_W              = -3.14
  Δ_3A (Z=N k=12)  = -33.18  ← dominant
  Δ_T1+ (pp+nn)    = +3.11
  Total            = -33.74 MeV
  AME              = -28.30 MeV
  Over-bound by    = -5.44 MeV (need +5.44)

Try several Hecke-derived candidates for a doubly-magic A=4 patch:
  M1: +m_e · H_q((2,2))     ≈ +6.29 MeV   (k=4 Wigner partition value)
  M2: +m_e · H_q((3,1))     ≈ +5.00 MeV   (k=4 hook partition)
  M3: +m_e · H_q((2,1)) * 2 ≈ +3.11 MeV   (k=3 self-conj * 2 pn pairs)
  M4: +m_e · [3]_q^2        ≈ +4.73 MeV
  M5: +m_e · H_q((2,2))/dim ≈ +3.08 MeV
  M6: +m_e · [4]_q · [2]_q  ≈ +5.00 MeV   ((3,1) hook product)
  M7: +m_e · q3*q2          ≈ +3.45 MeV
  M8: +m_e · H_q((3,1))/dim_q  k=4 hook ⊢ 4
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
    print("⁴He TIGHTENING via doubly-magic A=4 correction")
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

    delta_W_unit = me * q3_q * q2_q**2  # k=4 Wigner unit
    Hq_21 = float(hook_product_q((2, 1)))
    Hq_22 = float(hook_product_q((2, 2)))
    Hq_31 = float(hook_product_q((3, 1)))
    dq_22 = float(dim_q_lam((2, 2)))
    dq_31 = float(dim_q_lam((3, 1)))
    print(f"  k=3 (2,1)  : H_q = {Hq_21:.4f}")
    print(f"  k=4 (2,2)  : H_q = {Hq_22:.4f}, dim_q = {dq_22:.4f}, H/d = {Hq_22/dq_22:.4f}")
    print(f"  k=4 (3,1)  : H_q = {Hq_31:.4f}, dim_q = {dq_31:.4f}, H/d = {Hq_31/dq_31:.4f}")
    print(f"  [3]_q² = {float(q3_q**2):.4f}, [4]_q·[2]_q = {float(q_int(4)*q_int(2)):.4f}, "
          f"[3]_q·[2]_q = {float(q3_q*q2_q):.4f}")
    print()

    k3A_sums = {n: sum(hook_product_q(lam)/dim_q_lam(lam)
                          for lam in self_conjugate(n))
                 for n in [3, 6, 9, 12]}

    # Existing stack (without ⁴He patch)
    def base_binding(Z, N, A, P1, P2, P3):
        binding = float(alpha_bind) * (float(P1) - 2*float(q3_q)*float(P2) + float(HA2)*float(P3))
        delta_W = -float(delta_W_unit) * (min(Z,N)/A) if (A>=2 and Z>=1 and N>=1) else 0.0
        n_str = 3*A
        delta_3A = (-float(me) * float(k3A_sums.get(n_str, 0)) * (min(Z,N)/A)
                      if (Z == N and A >= 2) else 0.0)
        delta_SF = (-float(delta_W_unit) * (Z*(Z-1)//2 + N*(N-1)//2)
                      if (Z != N and A >= 2) else 0.0)
        delta_D = (+float(me) * Hq_21) if A == 2 else 0.0
        delta_T1pp = +float(me) * Hq_21 * (Z*(Z-1)//2 + N*(N-1)//2)
        return binding + delta_W + delta_3A + delta_SF + delta_D + delta_T1pp

    variants = {
        'M1: +m_e·H_q((2,2)) [4He only]':       lambda Z, N, A: +float(me) * Hq_22 if (Z==N==2) else 0,
        'M2: +m_e·H_q((3,1)) [4He only]':       lambda Z, N, A: +float(me) * Hq_31 if (Z==N==2) else 0,
        'M3: +m_e·H_q((2,1))·2 [4He only]':     lambda Z, N, A: +float(me) * Hq_21 * 2 if (Z==N==2) else 0,
        'M4: +m_e·[3]_q² [4He only]':           lambda Z, N, A: +float(me) * float(q3_q**2) if (Z==N==2) else 0,
        'M5: +m_e·H_q((2,2))/dim [4He]':        lambda Z, N, A: +float(me) * (Hq_22/dq_22) if (Z==N==2) else 0,
        'M6: +m_e·[4]_q·[2]_q [4He]':           lambda Z, N, A: +float(me) * float(q_int(4)*q_int(2)) if (Z==N==2) else 0,
        'M7: +m_e·[3]_q·[2]_q [4He]':           lambda Z, N, A: +float(me) * float(q3_q*q2_q) if (Z==N==2) else 0,
        'M8: +m_e·H_q((3,1))/dim [4He]':        lambda Z, N, A: +float(me) * (Hq_31/dq_31) if (Z==N==2) else 0,
    }

    for vname, vfn in variants.items():
        print(f"  Variant: {vname}")
        print(f"  {'iso':<8} {'D_4He':>10} {'B_pred':>10} {'B_AME':>10} {'B err':>10}")
        for name, Z, N, M_ref, B_ame in ISOTOPES:
            A = Z + N
            P1, P2, P3 = phi_inter_gen(Z, N)
            base = base_binding(Z, N, A, P1, P2, P3)
            d4he = vfn(Z, N, A)
            B_pred = -(base + d4he)
            err_B = ((B_pred - B_ame) / B_ame * 100) if B_ame != 0 else 0.0
            print(f"  {name:<8} {d4he:>+10.4f} {B_pred:>+10.4f} {B_ame:>+10.4f} {err_B:>+9.2f}%")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
