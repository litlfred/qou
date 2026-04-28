#!/usr/bin/env python3
"""
3-term Wedderburn formula with AVERAGE-baseline subtraction.

Replaces the per-type subtraction:
    Phi_inter = Phi_full - Z*Phi_p - N*Phi_n
with the symmetric average:
    Phi_inter = Phi_full - A * (Phi_p + Phi_n) / 2

This respects the Z=N exchange symmetry that the commutative-case
diagnostic showed is broken by per-type subtraction (which over-
removes for fully-paired atoms).

Test predicts D and 4He bindings should now have correct sign.
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
q3 = Q0**2 + 1 + QI**2
q2 = Q0 + QI
HA2 = H_A**2
delta_W_unit = me * q3 * q2**2


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


def phi_full(Z, N):
    chains = per_generator_chains(Z, N, include_inter=True, include_intra=True)
    s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    for ch in chains:
        if not ch: continue
        v = chain_std_zb(ch); d = chain_det(ch)
        ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
        if v != 0: s1 += mp.log(mp.fabs(v))
        if d != 0: s2 += mp.log(mp.fabs(d))
        if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
    return s1, s2, s3


def phi_intra_only(Z, N):
    chains = per_generator_chains(Z, N, include_inter=False, include_intra=True)
    s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    for ch in chains:
        if not ch: continue
        v = chain_std_zb(ch); d = chain_det(ch)
        ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
        if v != 0: s1 += mp.log(mp.fabs(v))
        if d != 0: s2 += mp.log(mp.fabs(d))
        if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
    return s1, s2, s3


def main() -> int:
    print("=" * 100)
    print("3-TERM WEDDERBURN with AVERAGE-baseline subtraction")
    print("  Phi_inter = Phi_full - A * (Phi_intra(p) + Phi_intra(n)) / 2")
    print("  (replaces per-type Z*Phi_p + N*Phi_n)")
    print("=" * 100)
    print()

    # Reference baselines
    P1p, P2p, P3p = phi_intra_only(1, 0)
    P1n, P2n, P3n = phi_intra_only(0, 1)
    print(f"  Free intra-only baselines:")
    print(f"    Phi_intra(p) = ({float(P1p):+.4f}, {float(P2p):+.4f}, {float(P3p):+.4f})")
    print(f"    Phi_intra(n) = ({float(P1n):+.4f}, {float(P2n):+.4f}, {float(P3n):+.4f})")
    print(f"    Average      = ({float((P1p+P1n)/2):+.4f}, "
          f"{float((P2p+P2n)/2):+.4f}, {float((P3p+P3n)/2):+.4f})")
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

    print(f"  {'iso':<8} {'Phi_1':>10} {'Phi_2':>10} {'Phi_3':>10} "
          f"{'binding':>10} {'D_W':>8} {'M_pred':>10} {'CODATA':>10} {'err %':>8}")
    rows = []
    for name, Z, N, M_ref, B_ame in ISOTOPES:
        A = Z + N
        P1f, P2f, P3f = phi_full(Z, N)
        # AVERAGE-baseline subtraction
        avg_baseline = mp.mpf(1)/2
        P1_inter = P1f - A * (P1p + P1n) * avg_baseline
        P2_inter = P2f - A * (P2p + P2n) * avg_baseline
        P3_inter = P3f - A * (P3p + P3n) * avg_baseline
        binding = float(alpha_bind) * (float(P1_inter)
                                          - 2*float(q3)*float(P2_inter)
                                          + float(HA2)*float(P3_inter))
        # Wigner correction
        if A >= 2 and Z >= 1 and N >= 1:
            delta_W = -float(delta_W_unit) * min(Z, N) / A
        else:
            delta_W = 0.0
        M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
        M_pred = M_free + binding + delta_W
        err = (M_pred - M_ref) / M_ref * 100
        print(f"  {name:<8} {float(P1_inter):>+10.4f} {float(P2_inter):>+10.4f} "
              f"{float(P3_inter):>+10.4f} {binding:>+10.4f} {delta_W:>+8.4f} "
              f"{M_pred:>10.4f} {M_ref:>10.4f} {err:>+7.3f}%")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'Phi_1_avg': float(P1_inter),
            'Phi_2_avg': float(P2_inter),
            'Phi_3_avg': float(P3_inter),
            'binding_MeV': binding,
            'Wigner_MeV': delta_W,
            'M_pred_MeV': M_pred,
            'M_codata_MeV': M_ref,
            'err_pct': err,
            'B_ame_MeV': B_ame,
        })

    print()
    print(f"  Implied bindings vs AME:")
    print(f"  {'iso':<8} {'B_pred':>10} {'B_AME':>10} {'err %':>10}")
    for r in rows:
        if r['B_ame_MeV'] is None or r['B_ame_MeV'] == 0:
            continue
        B_pred = -(r['binding_MeV'] + r['Wigner_MeV'])
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
        'computation': 'wedderburn-3term-avg-baseline',
        'description': (
            'Average-baseline subtraction Phi_inter = Phi_full - '
            'A*(Phi_p_intra + Phi_n_intra)/2.  Tests whether '
            'symmetric subtraction fixes Z=N (D, 4He) sign flip '
            'identified by commutative-case diagnostic.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'isotopes': rows,
    }
    out = Path(__file__).parent / "wedderburn-3term-avg-baseline.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
