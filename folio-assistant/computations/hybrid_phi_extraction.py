#!/usr/bin/env python3
"""
HYBRID Φ extraction: each functional uses the chain it MOST naturally lives on
under the Frobenius S-classification.

Per prop:frobenius-s-classification:
  Φ_1 (trace)      : S-mixed -- needs symmetrization or inter-gen direct
  Φ_2 (det)        : S-invariant per Lemma 3.2 -- can use full chain safely
  Φ_3 (chirality)  : S-anti-invariant -- but H_A² · Φ_3 needs careful handling

Hybrid hypothesis:
  Φ_1 = inter-gen direct (preserves np splitting, gives correct sign)
  Φ_2 = FULL chain (already S-invariant, full info)
  Φ_3 = FULL chain or inter-gen direct (test both)

Goal: bridge binding under-prediction (D +41%, T -38%, ³He -32%, ⁴He -76%)
without breaking np splitting (currently exact).

Comparison with derived-only baseline:
  Variant H1: Φ_1 inter-gen, Φ_2 full,     Φ_3 inter-gen (current)
  Variant H2: Φ_1 inter-gen, Φ_2 full,     Φ_3 full       (test)
  Variant H3: Φ_1 inter-gen, Φ_2 inter,    Φ_3 full       (test)
  Variant H4: Φ_1 full,      Φ_2 full,     Φ_3 full       (full -- baseline)
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
Wigner_unit = me * q3_q * q2_q**2


def chain_lambda_sym(chain):
    out = mp.mpf(1)
    for c, d in chain: out *= mp.mpf(c)*Q0 + mp.mpf(d)
    return out
def chain_lambda_alt(chain):
    out = mp.mpf(1)
    for c, d in chain: out *= -mp.mpf(c)/Q0 + mp.mpf(d)
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


def phi_select(Z, N, mode_phi1, mode_phi2, mode_phi3):
    """Compute (Φ_1, Φ_2, Φ_3) with each Φ using its own chain mode.
    mode in {'inter', 'full', 'subtracted'}.
    """
    A = Z + N
    chains = per_gen_chains_full(Z, N)
    inter_gens = [3*k + 2 for k in range(A - 1)] if A >= 2 else []

    def collect(gen_indices):
        s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for g_idx in gen_indices:
            if g_idx >= len(chains): continue
            ch = chains[g_idx]
            if not ch: continue
            v = chain_std_zb(ch); d = chain_det(ch)
            ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
            if v != 0: s1 += mp.log(mp.fabs(v))
            if d != 0: s2 += mp.log(mp.fabs(d))
            if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
        return s1, s2, s3

    full_gens = list(range(len(chains)))
    P1f, P2f, P3f = collect(full_gens)
    P1i, P2i, P3i = collect(inter_gens)

    def pick(mode, full_val, inter_val):
        return full_val if mode == 'full' else inter_val

    return (pick(mode_phi1, P1f, P1i),
             pick(mode_phi2, P2f, P2i),
             pick(mode_phi3, P3f, P3i))


def main():
    print("=" * 100)
    print("HYBRID Φ EXTRACTION: per-functional chain mode")
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

    variants = {
        'H1: Φ_1 inter, Φ_2 inter, Φ_3 inter (current)': ('inter', 'inter', 'inter'),
        'H2: Φ_1 inter, Φ_2 full,  Φ_3 inter':           ('inter', 'full',  'inter'),
        'H3: Φ_1 inter, Φ_2 full,  Φ_3 full':            ('inter', 'full',  'full'),
        'H4: Φ_1 inter, Φ_2 inter, Φ_3 full':            ('inter', 'inter', 'full'),
        'H5: Φ_1 full,  Φ_2 full,  Φ_3 full (no split)': ('full',  'full',  'full'),
    }

    for vname, (m1, m2, m3) in variants.items():
        print(f"  {vname}")
        print(f"  {'iso':<8} {'Φ_1':>10} {'Φ_2':>10} {'Φ_3':>10} "
              f"{'binding':>10} {'M_pred':>10} {'B_pred':>10} {'B_AME':>10} "
              f"{'M err':>8} {'B err':>8}")
        for name, Z, N, M_ref, B_ame in ISOTOPES:
            A = Z + N
            P1, P2, P3 = phi_select(Z, N, m1, m2, m3)
            binding = float(alpha_bind) * (float(P1) - 2*float(q3_q)*float(P2) + float(HA2)*float(P3))
            delta_W = -float(Wigner_unit) * (min(Z,N)/A) if (A>=2 and Z>=1 and N>=1) else 0.0
            n_pp = Z*(Z-1)//2; n_nn = N*(N-1)//2
            delta_T1 = (-float(Wigner_unit) * ((n_pp + n_nn)/A)
                          if (A >= 2 and (n_pp + n_nn) > 0) else 0.0)
            M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
            M_pred = M_free + binding + delta_W + delta_T1
            err_M = (M_pred - M_ref) / M_ref * 100
            B_pred = -(binding + delta_W + delta_T1)
            err_B = ((B_pred - B_ame) / B_ame * 100) if B_ame != 0 else 0.0
            print(f"  {name:<8} {float(P1):>+10.3f} {float(P2):>+10.3f} {float(P3):>+10.3f} "
                  f"{binding:>+10.3f} {M_pred:>10.3f} {B_pred:>+10.3f} {B_ame:>+10.3f} "
                  f"{err_M:>+7.3f}% {err_B:>+7.2f}%")

        # Check np splitting
        rows = {n: 0 for n in ['p (1H)', 'n']}
        for name, Z, N, M_ref, B_ame in ISOTOPES:
            if name not in rows:
                continue
            P1, P2, P3 = phi_select(Z, N, m1, m2, m3)
            A = Z + N
            binding = float(alpha_bind) * (float(P1) - 2*float(q3_q)*float(P2) + float(HA2)*float(P3))
            delta_W = -float(Wigner_unit) * (min(Z,N)/A) if (A>=2 and Z>=1 and N>=1) else 0.0
            n_pp = Z*(Z-1)//2; n_nn = N*(N-1)//2
            delta_T1 = (-float(Wigner_unit) * ((n_pp + n_nn)/A)
                          if (A >= 2 and (n_pp + n_nn) > 0) else 0.0)
            M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
            rows[name] = M_free + binding + delta_W + delta_T1
        if rows['p (1H)'] != 0 and rows['n'] != 0:
            np_pred = rows['n'] - rows['p (1H)'] + M_E_MEV
            np_err = (np_pred - (M_N_MEV - M_P_MEV)) / (M_N_MEV - M_P_MEV) * 100
            print(f"    np splitting: {np_pred:+.4f} MeV (CODATA +1.293), err {np_err:+.3f}%")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
