#!/usr/bin/env python3
"""
D-SPECIFIC DIAGNOSTIC: investigate why deuterium binding is
wrong-sign even after Z=N gate + k=3A correction.

Approaches tried in this script:

1. Direct g2-only Φ for D (instead of subtraction approach).
2. k=3 self-conjugate (2,1) ⊢ 3 contribution at various occupancies.
3. Full chains vs inter-only comparison.
4. Per-generator decomposition: which generator dominates D's Φ_1?
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


def main() -> int:
    print("=" * 100)
    print("D-SPECIFIC DIAGNOSTIC")
    print("=" * 100)
    print()

    # Probe 1: per-generator decomposition of D's Φ values
    print("  Probe 1: D per-generator Φ contributions (full chains)")
    chains = per_gen_chains(1, 1, include_inter=True, include_intra=True)
    print(f"  {'gen':>3} {'len':>3} {'V_std':>12} {'det':>12} "
          f"{'sym':>12} {'alt':>12} {'log|V_std|':>12} {'log|det|':>12}")
    for g_idx, ch in enumerate(chains):
        if not ch:
            print(f"  {g_idx:>3} (empty)")
            continue
        v = chain_std_zb(ch); d = chain_det(ch)
        ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
        log_v = float(mp.log(mp.fabs(v))) if v != 0 else float('nan')
        log_d = float(mp.log(mp.fabs(d))) if d != 0 else float('nan')
        print(f"  {g_idx:>3} {len(ch):>3} {float(v):>+12.4f} {float(d):>+12.4f} "
              f"{float(ls):>+12.4f} {float(la):>+12.4f} {log_v:>+12.4f} {log_d:>+12.4f}")
    print()

    # Probe 2: g2 (inter only) vs g0+g1 (intra p) vs g3+g4 (intra n)
    print("  Probe 2: D split by intra-p (g0,g1) vs inter (g2) vs intra-n (g3,g4)")
    intra_p = chains[0] + chains[1]
    inter   = chains[2]
    intra_n = chains[3] + chains[4]
    for label, ch in [('intra-p (g0,g1)', intra_p),
                       ('inter   (g2)',  inter),
                       ('intra-n (g3,g4)', intra_n)]:
        v = chain_std_zb(ch) if ch else mp.mpf(1)
        d = chain_det(ch) if ch else mp.mpf(1)
        ls = chain_lambda_sym(ch) if ch else mp.mpf(1)
        la = chain_lambda_alt(ch) if ch else mp.mpf(1)
        log_v = float(mp.log(mp.fabs(v))) if v != 0 else float('nan')
        print(f"  {label:<22} log|V_std| = {log_v:+.4f}, V_std = {float(v):+.4f}")
    print()

    # Probe 3: free p has 2 gens (g0, g1), but their CHAINS are not the
    # same as in D (where prev_types differs).  Compare:
    print("  Probe 3: free p chains vs intra-p in D")
    chains_p = per_gen_chains(1, 0, include_inter=False, include_intra=True)
    for g_idx in range(min(len(chains_p), 2)):
        ch_p = chains_p[g_idx]
        ch_d = chains[g_idx]
        v_p = chain_std_zb(ch_p) if ch_p else mp.mpf(1)
        v_d = chain_std_zb(ch_d) if ch_d else mp.mpf(1)
        print(f"  g{g_idx}: free-p len={len(ch_p)} V={float(v_p):+.4f}, "
              f"in-D len={len(ch_d)} V={float(v_d):+.4f}, "
              f"same? {ch_p == ch_d}")
    print()

    # Probe 4: try lower-k self-conjugate corrections for D
    print("  Probe 4: lower-k self-conjugate (2,1) ⊢ 3 contribution to D")
    Hq_21_3 = q_int(3) * q_int(1) * q_int(1)  # hooks of (2,1) are 3, 1, 1
    dq_21_3 = (q_int(3) * q_int(2) * q_int(1)) / Hq_21_3  # [3]_q!/H_q
    Hq_22_4 = q_int(3) * q_int(2) * q_int(2) * q_int(1)  # (2,2): hooks 3,2,2,1
    dq_22_4 = (q_int(4) * q_int(3) * q_int(2) * q_int(1)) / Hq_22_4
    print(f"    (2,1)|-3: H_q = {float(Hq_21_3):.4f}, dim_q = {float(dq_21_3):.4f}, "
          f"H_q/dim_q = {float(Hq_21_3/dq_21_3):.4f}")
    print(f"    (2,2)|-4: H_q = {float(Hq_22_4):.4f}, dim_q = {float(dq_22_4):.4f}, "
          f"H_q/dim_q = {float(Hq_22_4/dq_22_4):.4f}")
    # Apply Scheme C with various occupancies for D:
    occupancies = {
        '1': 1.0,
        'A=2': 2.0,
        'min(Z,N)=1': 1.0,
        '1/A=0.5': 0.5,
    }
    print(f"\n  Per-occupancy Δ_(2,1)⊢3 for D:")
    for nm, f in occupancies.items():
        delta = -float(me) * float(Hq_21_3 / dq_21_3) * f
        print(f"    occupancy={nm:<12}: Δ = {delta:+.4f} MeV")
    print()

    # Probe 5: try summing k=3 + k=4 + k=6 with Z=N gate
    print("  Probe 5: combined k=3 + k=4 (Wigner) + k=6 with Z=N gate (D, ⁴He)")

    # k=3 (2,1)
    delta_W_unit_k3 = me * Hq_21_3
    delta_W_unit_k4 = me * q3 * q2**2  # k=4 Wigner
    Hq_321 = q_int(5) * q_int(3) * q_int(1) * q_int(3) * q_int(1) * q_int(1)
    # Compute correctly via young_hooks of (3,2,1) = [5,3,1,3,1,1]
    # actually let me use existing function
    from hecke_characters import young_hooks
    hk_321 = young_hooks((3,2,1))
    Hq_321_exact = mp.mpf(1)
    for h in hk_321:
        Hq_321_exact *= q_int(int(h))
    print(f"  Probe 5 hook check: hooks of (3,2,1) = {hk_321}")
    print(f"  Probe 5 H_q((3,2,1)) = {float(Hq_321_exact):.4f}")

    iso_data = [('D', 1, 1, 2.22456612), ('⁴He', 2, 2, 28.29566)]
    print(f"  {'iso':<6} {'Δ_W(k=4)':>10} {'Δ_(2,1)(k=3)':>14} {'Δ_(3,2,1)(k=6)':>16} "
          f"{'sum':>8}")
    for name, Z, N, B_ame in iso_data:
        A = Z + N
        f_min = min(Z, N) / A
        # k=3: Z=N gate * min/A
        delta_k3 = -float(me) * float(Hq_21_3 / dq_21_3) * (f_min if Z==N else 0)
        # k=4 Wigner (already)
        delta_k4 = -float(delta_W_unit_k4) * f_min
        # k=6 (3,2,1) with Z=N gate * min/A
        dq_321 = q_int(6) * q_int(5) * q_int(4) * q_int(3) * q_int(2) * q_int(1) / Hq_321_exact
        # actually dim_q V_λ = [n]_q! / H_q(λ)
        dq_321 = mp.mpf(1)
        for j in range(2, 7):
            dq_321 *= q_int(j)
        dq_321 = dq_321 / Hq_321_exact
        delta_k6 = -float(me) * float(Hq_321_exact / dq_321) * (f_min if Z==N else 0)
        total = delta_k3 + delta_k4 + delta_k6
        print(f"  {name:<6} {delta_k4:>+10.4f} {delta_k3:>+14.4f} {delta_k6:>+16.4f} "
              f"{total:>+8.4f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
