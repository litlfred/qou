#!/usr/bin/env python3
"""
Self-conjugate partition corrections for D, T, ³He, ⁴He.

The Wigner (2,2)⊢4 partition is one of MANY self-conjugate partitions
λ = λ' that contribute T=0 isoscalar pairing.  At 3A strands, the full
T=0 binding is

    Δ_pairing(Z, N) = -m_e · Σ_{λ ⊢ 3A, λ = λ'} H_q(λ) · f_λ(Z, N) / |stab|

where:
  H_q(λ) = ∏_{x ∈ λ} [h_x(λ)]_q  is the q-hook product
  f_λ(Z, N) is the occupancy factor (how many ways the (Z,N) atom
            populates the λ representation; for fully-paired (Z=N)
            atoms this is maximal)
  |stab|   normalisation against over-counting symmetries

For simplicity, we use f_λ = min(Z,N)/A · w_λ  where w_λ = (dim_q V_λ)²
is the algebraic Wedderburn weight (paper: confined-knot-binding).

This script:
1. Enumerates ALL self-conjugate λ ⊢ 3A for each isotope.
2. Computes H_q(λ) and w_λ for each.
3. Sums contributions to total pairing energy.
4. Adds to the inter-only Wedderburn binding to predict atomic mass.
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
    for k in range(2, n+1):
        out *= q_int(k)
    return out


def transpose_partition(lam):
    if not lam:
        return tuple()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def hook_product_q(lam):
    """H_q(λ) = ∏_{x ∈ λ} [h_x(λ)]_q."""
    hooks = young_hooks(lam)
    out = mp.mpf(1)
    for h in hooks:
        out *= q_int(int(h))
    return out


def dim_q_lam(lam):
    """dim_q V_λ via q-deformed hook formula."""
    n = sum(lam)
    return q_fact(n) / hook_product_q(lam)


def self_conjugate_partitions(n):
    """Enumerate self-conjugate partitions of n."""
    return [tuple(lam) for lam in partitions_of(n)
             if transpose_partition(tuple(lam)) == tuple(lam)]


# Reuse 3-term inter-only Φ from prior work
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


def per_generator_chains(Z, N, include_inter=True, include_intra=True):
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
    """Inter-only Φ_1, Φ_2, Φ_3 (subtract free constituents)."""
    Phi1, Phi2, Phi3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    chains_full = per_generator_chains(Z, N, include_inter=True, include_intra=True)
    chains_intra_p = per_generator_chains(1, 0, include_inter=False, include_intra=True)
    chains_intra_n = per_generator_chains(0, 1, include_inter=False, include_intra=True)

    def collect(chains):
        s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for ch in chains:
            if not ch:
                continue
            v = chain_std_zb(ch); d = chain_det(ch)
            ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
            if v != 0: s1 += mp.log(mp.fabs(v))
            if d != 0: s2 += mp.log(mp.fabs(d))
            if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
        return s1, s2, s3

    P1f, P2f, P3f = collect(chains_full)
    P1p, P2p, P3p = collect(chains_intra_p)
    P1n, P2n, P3n = collect(chains_intra_n)
    return (P1f - Z*P1p - N*P1n,
             P2f - Z*P2p - N*P2n,
             P3f - Z*P3p - N*P3n)


def main() -> int:
    print("=" * 100)
    print("SELF-CONJUGATE PARTITION CORRECTIONS")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
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

    # Print self-conjugate partition catalogue per 3A
    for n in [3, 6, 9, 12]:
        sc_lams = self_conjugate_partitions(n)
        print(f"  Self-conjugate partitions of {n}: {len(sc_lams)}")
        for lam in sc_lams:
            Hq = float(hook_product_q(lam))
            dq = float(dim_q_lam(lam))
            print(f"    λ = {lam}: H_q(λ) = {Hq:>12.6f}, dim_q = {dq:>12.4e}")
    print()

    # Compute pairing correction = -m_e · Σ H_q(λ) · w_λ · min(Z,N)/A / total_w
    rows = []
    print(f"  {'iso':<8} {'Phi_1':>10} {'Phi_2':>10} {'Phi_3':>10} "
          f"{'binding':>10} {'pair_total':>12} {'M_pred':>10} {'CODATA':>10} {'err %':>8}")

    for name, Z, N, M_ref, B_ame in ISOTOPES:
        A = Z + N
        n_strands = 3 * A
        if A >= 2 and Z >= 1 and N >= 1:
            sc_lams = self_conjugate_partitions(n_strands)
            # Total pairing: sum H_q(λ) weighted by dim_q(λ)² then normalized
            pair_corr = mp.mpf(0)
            total_w = mp.mpf(0)
            for lam in sc_lams:
                w = dim_q_lam(lam)**2
                pair_corr += hook_product_q(lam) * w
                total_w += w
            if total_w > 0:
                pair_corr = pair_corr / total_w
            # Scale by min(Z,N)/A as occupancy
            pair_corr_MeV = -float(me) * float(pair_corr) * min(Z, N) / A
        else:
            pair_corr_MeV = 0.0

        Phi1, Phi2, Phi3 = phi_inter(Z, N)
        binding = float(alpha_bind) * (float(Phi1) - 2*float(q3)*float(Phi2) + float(HA2)*float(Phi3))
        M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
        M_pred = M_free + binding + pair_corr_MeV
        err = (M_pred - M_ref) / M_ref * 100
        print(f"  {name:<8} {float(Phi1):>+10.4f} {float(Phi2):>+10.4f} {float(Phi3):>+10.4f} "
              f"{binding:>+10.4f} {pair_corr_MeV:>+12.4f} "
              f"{M_pred:>10.4f} {M_ref:>10.4f} {err:>+7.3f}%")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'Phi_1_inter': float(Phi1),
            'Phi_2_inter': float(Phi2),
            'Phi_3_inter': float(Phi3),
            'binding_MeV': binding,
            'pair_corr_MeV': pair_corr_MeV,
            'M_pred_MeV': M_pred,
            'M_codata_MeV': M_ref,
            'err_pct': err,
            'B_ame_MeV': B_ame,
        })

    # Bindings
    print()
    print(f"  Implied bindings vs AME (B > 0 = bound):")
    print(f"  {'iso':<8} {'B_pred':>10} {'B_AME':>10} {'err %':>10}")
    for r in rows:
        if r['B_ame_MeV'] is None or r['B_ame_MeV'] == 0:
            continue
        B_pred = -(r['binding_MeV'] + r['pair_corr_MeV'])
        err = (B_pred - r['B_ame_MeV']) / r['B_ame_MeV'] * 100
        print(f"  {r['iso']:<8} {B_pred:>+10.4f} {r['B_ame_MeV']:>+10.4f} {err:>+9.2f}%")

    witness = {
        'computation': 'self-conjugate-partition-corrections',
        'description': (
            'Sum over ALL self-conjugate partitions λ ⊢ 3A weighted '
            'by H_q(λ)·(dim_q V_λ)² normalised by Σ(dim_q)².  Tests '
            'whether richer partition spectrum bridges D and 4He '
            'binding gaps where the simple (2,2)|-4 Wigner correction '
            'was insufficient.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'isotopes': rows,
    }
    out = Path(__file__).parent / "self-conjugate-partition-corrections.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
