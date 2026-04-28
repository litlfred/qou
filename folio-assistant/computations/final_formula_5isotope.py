#!/usr/bin/env python3
"""
Extend final formula to ⁶Li, ⁷Li.

Formula:
  M(Z,N) = Z·m_p + N·m_n + Z·m_e
         + α·(Φ_1 − 2[3]_q·Φ_2 + H_A²·Φ_3)        [paper 3-term]
         + Δ_W       (k=4 Wigner T=0 pn pairing)
         + Δ_3A      (k=3A self-conj, Z=N gate)
         + Δ_SF      (T=1 Z≠N gate)
         + Δ_D       (k=3 (2,1) D-only A=2 patch)
         + Δ_T1+     (T=1 isovector pp+nn)
         + Δ_4He     (doubly-magic [3]_q² patch)

Test on ⁶Li (Z=N=3, A=6, 3A=18) and ⁷Li (Z=3, N=4, A=7, 3A=21).
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
    print("FINAL FORMULA — extension to ⁶Li, ⁷Li")
    print("=" * 100)
    print()

    AME_BIND = {'D': 2.22456612, 'T': 8.481798,
                 '³He': 7.718058, '⁴He': 28.29566,
                 '⁶Li': 31.99405, '⁷Li': 39.24454}
    M_H_ATOMIC = M_P_MEV + M_E_MEV
    ISOTOPES = [
        ('p (1H)', 1, 0, M_H_ATOMIC, 0.0),
        ('n',      0, 1, M_N_MEV,    0.0),
        ('D',      1, 1, 1876.12393, AME_BIND['D']),
        ('T',      1, 2, 2809.43215, AME_BIND['T']),
        ('³He',    2, 1, 2809.41347, AME_BIND['³He']),
        ('⁴He',    2, 2, 3728.40133, AME_BIND['⁴He']),
        ('⁶Li',    3, 3, 5603.05181, AME_BIND['⁶Li']),
        ('⁷Li',    3, 4, 6535.36652, AME_BIND['⁷Li']),
    ]

    delta_W_unit = me * q3_q * q2_q**2
    Hq_21 = float(hook_product_q((2, 1)))
    print(f"  α (Borromean) = m_e·8G   = {float(alpha_bind):.4f} MeV")
    print(f"  Δ_W unit (k=4 Wigner)    = {float(delta_W_unit):.4f} MeV")
    print(f"  H_q((2,1)) (T=1 unit)    = {Hq_21:.4f}")
    print(f"  m_e·[3]_q² (4He patch)   = {float(me)*float(q3_q**2):.4f} MeV")
    print()

    # Pre-compute k=3A self-conjugate sums
    k3A_sums = {}
    for n in [3, 6, 9, 12, 18, 21]:
        sc = self_conjugate(n)
        s = sum(hook_product_q(lam)/dim_q_lam(lam) for lam in sc)
        k3A_sums[n] = (len(sc), float(s))
        print(f"  3A={n}: {len(sc)} self-conjugate λ, Σ H_q/dim_q = {float(s):.4f}")
    print()

    print(f"  {'iso':<8} {'binding':>10} {'D_W':>8} {'D_3A':>10} {'D_SF':>8} "
          f"{'D_D':>6} {'D_T1+':>8} {'D_4He':>7} {'M_pred':>10} {'B_pred':>10} "
          f"{'B_AME':>10} {'err %':>8}")

    rows = []
    for name, Z, N, M_ref, B_ame in ISOTOPES:
        A = Z + N
        n_str = 3 * A
        P1, P2, P3 = phi_inter_gen(Z, N)
        binding = float(alpha_bind) * (float(P1) - 2*float(q3_q)*float(P2) + float(HA2)*float(P3))
        delta_W = -float(delta_W_unit) * (min(Z,N)/A) if (A>=2 and Z>=1 and N>=1) else 0.0
        delta_3A = (-float(me) * k3A_sums.get(n_str, (0, 0.0))[1] * (min(Z,N)/A)
                      if (Z == N and A >= 2) else 0.0)
        delta_SF = (-float(delta_W_unit) * (Z*(Z-1)//2 + N*(N-1)//2)
                      if (Z != N and A >= 2) else 0.0)
        delta_D = (+float(me) * Hq_21) if A == 2 else 0.0
        delta_T1pp = +float(me) * Hq_21 * (Z*(Z-1)//2 + N*(N-1)//2)
        delta_4He = (+float(me) * float(q3_q**2)) if (Z == N == 2) else 0.0

        M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
        M_pred = M_free + binding + delta_W + delta_3A + delta_SF + delta_D + delta_T1pp + delta_4He
        err_M = (M_pred - M_ref) / M_ref * 100
        B_pred = -(binding + delta_W + delta_3A + delta_SF + delta_D + delta_T1pp + delta_4He)
        err_B = ((B_pred - B_ame) / B_ame * 100) if B_ame != 0 else 0.0
        print(f"  {name:<8} {binding:>+10.3f} {delta_W:>+8.3f} {delta_3A:>+10.3f} "
              f"{delta_SF:>+8.3f} {delta_D:>+6.3f} {delta_T1pp:>+8.3f} {delta_4He:>+7.3f} "
              f"{M_pred:>10.4f} {B_pred:>+10.4f} {B_ame:>+10.4f} {err_B:>+7.2f}%")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'binding_MeV': binding, 'delta_W': delta_W, 'delta_3A': delta_3A,
            'delta_SF': delta_SF, 'delta_D': delta_D, 'delta_T1pp': delta_T1pp,
            'delta_4He': delta_4He,
            'M_pred_MeV': M_pred, 'M_codata_MeV': M_ref,
            'B_pred_MeV': B_pred, 'B_AME_MeV': B_ame,
            'err_M_pct': err_M, 'err_B_pct': err_B,
        })

    print()
    print(f"  Bindings vs AME:")
    print(f"  {'iso':<8} {'B_pred':>10} {'B_AME':>10} {'err %':>10}")
    for r in rows:
        if r['B_AME_MeV'] is None or r['B_AME_MeV'] == 0:
            continue
        print(f"  {r['iso']:<8} {r['B_pred_MeV']:>+10.4f} {r['B_AME_MeV']:>+10.4f} "
              f"{r['err_B_pct']:>+9.2f}%")

    witness = {
        'computation': 'final-formula-5-isotope-extension',
        'description': (
            'Extension of final formula stack to 6Li and 7Li.  Tests '
            'whether the stack (3-term Wedderburn + Wigner + k=3A '
            'Z=N gate + T=1 isovector + D-only patch + T=1 pp+nn '
            'isovector + 4He doubly-magic patch) extends correctly '
            'to A=6, 7.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'k3A_sums': {str(k): {'count': v[0], 'sum_Hq_dim': v[1]} for k, v in k3A_sums.items()},
        'isotopes': rows,
    }
    out = Path(__file__).parent / "final-formula-5-isotope.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
