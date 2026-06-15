#!/usr/bin/env python3
"""
DIRECT inter-generator Φ extraction — bypasses the over-counting of
the subtraction approach.

D-specific diagnostic showed that the inter-only Φ_1 via subtraction
(Φ_full − Z·Φ_p − N·Φ_n) was contaminated by intra-chain values that
differ between free constituents and in-atom (because in-atom chains
include strand-context from other nucleons).

Direct extraction: identify inter-nucleon generators (those between
strands of different nucleons) and sum Φ over JUST those generators.

For atom (Z, N) with A nucleons:
  - Strands of nucleon k: 3k, 3k+1, 3k+2
  - Inter generator at position 3k+2 (connects nucleon k strand 2
    to nucleon k+1 strand 0)

Implementation: per_gen_chains as before, but only include the
inter-gen positions in the Φ sum.

Combine with k=3A self-conjugate Z=N-gate correction (Scheme C).
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


def phi_inter_gen_direct(Z, N):
    """Φ from JUST the inter-nucleon generators (positions 3k+2)."""
    A = Z + N
    chains = per_gen_chains_full(Z, N)
    inter_gens = [3*k + 2 for k in range(A - 1)]   # generators connecting nucleons
    s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    for g_idx in inter_gens:
        if g_idx >= len(chains):
            continue
        ch = chains[g_idx]
        if not ch:
            continue
        v = chain_std_zb(ch); d = chain_det(ch)
        ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
        if v != 0: s1 += mp.log(mp.fabs(v))
        if d != 0: s2 += mp.log(mp.fabs(d))
        if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
    return s1, s2, s3


def main() -> int:
    print("=" * 100)
    print("DIRECT inter-gen-only Φ + k=3A Z=N-gate correction")
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

    delta_W_unit = me * q3 * q2**2

    # Pre-compute k=3A self-conjugate sums
    k3A_sums = {}
    for n in [3, 6, 9, 12]:
        sc = self_conjugate(n)
        s = sum(hook_product_q(lam) / dim_q_lam(lam) for lam in sc)
        k3A_sums[n] = s

    print(f"  {'iso':<8} {'Φ_1':>10} {'Φ_2':>10} {'Φ_3':>10} "
          f"{'binding':>10} {'D_W(k=4)':>10} {'Δ_3A':>10} {'M_pred':>10} "
          f"{'CODATA':>10} {'err %':>8}")
    rows = []
    for name, Z, N, M_ref, B_ame in ISOTOPES:
        A = Z + N
        n_str = 3*A
        P1, P2, P3 = phi_inter_gen_direct(Z, N)
        binding = float(alpha_bind) * (float(P1) - 2*float(q3)*float(P2) + float(HA2)*float(P3))
        if A >= 2 and Z >= 1 and N >= 1:
            delta_W = -float(delta_W_unit) * min(Z, N) / A
        else:
            delta_W = 0.0
        # Z=N gate k=3A
        if Z == N and A >= 2 and n_str in k3A_sums:
            delta_3A = -float(me) * float(k3A_sums[n_str]) * (min(Z, N) / A)
        else:
            delta_3A = 0.0
        M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
        M_pred = M_free + binding + delta_W + delta_3A
        err = (M_pred - M_ref) / M_ref * 100
        print(f"  {name:<8} {float(P1):>+10.4f} {float(P2):>+10.4f} {float(P3):>+10.4f} "
              f"{binding:>+10.4f} {delta_W:>+10.4f} {delta_3A:>+10.4f} "
              f"{M_pred:>10.4f} {M_ref:>10.4f} {err:>+7.3f}%")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'Phi_1_inter_gen': float(P1),
            'Phi_2_inter_gen': float(P2),
            'Phi_3_inter_gen': float(P3),
            'binding_MeV': binding,
            'Wigner_MeV': delta_W,
            'Delta_3A_MeV': delta_3A,
            'M_pred_MeV': M_pred,
            'M_codata_MeV': M_ref,
            'err_pct': err,
            'B_ame_MeV': B_ame,
        })

    print()
    print(f"  Implied bindings (B > 0 = bound):")
    print(f"  {'iso':<8} {'B_pred':>10} {'B_AME':>10} {'err %':>10}")
    for r in rows:
        if r['B_ame_MeV'] is None or r['B_ame_MeV'] == 0:
            continue
        B_pred = -(r['binding_MeV'] + r['Wigner_MeV'] + r['Delta_3A_MeV'])
        err = (B_pred - r['B_ame_MeV']) / r['B_ame_MeV'] * 100
        print(f"  {r['iso']:<8} {B_pred:>+10.4f} {r['B_ame_MeV']:>+10.4f} {err:>+9.2f}%")

    # np splitting
    print()
    p_row = next(r for r in rows if r['iso'].startswith('p'))
    n_row = next(r for r in rows if r['iso'] == 'n')
    delta_pred = (n_row['M_pred_MeV'] - p_row['M_pred_MeV']) + M_E_MEV
    delta_codata = M_N_MEV - M_P_MEV
    print(f"  Bare np splitting:")
    print(f"    M_pred(n) - M_pred(1H) + m_e = {delta_pred:+.6f} MeV")
    print(f"    CODATA Δm_{{n-p}}              = {delta_codata:+.6f} MeV")
    print(f"    err = {(delta_pred-delta_codata)/delta_codata*100:+.3f}%")

    witness = {
        'computation': 'wedderburn-inter-gen-direct',
        'description': (
            'Direct inter-generator-only Φ extraction (no subtraction): '
            'sum Phi only over generators that connect different '
            'nucleons (positions 3k+2 for k=0..A-2).  Combined with '
            'Z=N-gate k=3A self-conjugate partition correction (Scheme C: '
            'm_e * H_q(λ) / dim_q V_λ).'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'isotopes': rows,
    }
    out = Path(__file__).parent / "wedderburn-inter-gen-direct.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
