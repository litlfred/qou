#!/usr/bin/env python3
"""
DERIVED-ONLY formula -- no menu-of-variants fits.

Per user direction: drop all variant-selected corrections; keep only
components with explicit derivation in the paper.

Formula:
  M(Z,N) = Z·m_p + N·m_n + Z·m_e
         + α·(Φ_1 − 2[3]_q·Φ_2 + H_A²·Φ_3)        [paper 3-term]
         + Δ_W         (paper: T=0 Wigner)
         + Δ_T1        (natural extension of Wigner to T=1)

with:
  α = m_e · 8G                                       (Borromean, derived)
  Δ_W = -m_e · H_q((2,2)) · min(Z,N)/A               (paper)
  Δ_T1 = -m_e · H_q((2,2)) · (n_pp + n_nn)/A         (natural T=1 analog)
       where n_pp = Z(Z-1)/2, n_nn = N(N-1)/2

Φ from inter-gen direct (structural choice, NOT a fit).

DROPPED (all were variant-selections from a menu of options):
  - Δ_3A  (Z=N gate, k=3A self-conjugate Scheme C)
  - Δ_SF  (Z≠N gate, full pair count, no /A)
  - Δ_D   (D-only A=2 patch, +m_e·H_q((2,1)))
  - Δ_T1+ (pp+nn isovector +m_e·H_q((2,1))·n_same)
  - Δ_4He (doubly-magic +m_e·[3]_q²)

These produced good fits but each was chosen from 5-8 variants by best
match to AME -- hence technically fitted (discrete model selection).
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

# Wigner unit = m_e · H_q((2,2)) = m_e · [3]_q · [2]_q²
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


def main():
    print("=" * 100)
    print("DERIVED-ONLY formula (no variant-selected fits)")
    print("=" * 100)
    print()
    print(f"  α (Borromean)  = m_e · 8G = {float(alpha_bind):.4f} MeV")
    print(f"  Wigner unit    = m_e · H_q((2,2)) = {float(Wigner_unit):.4f} MeV")
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

    print(f"  {'iso':<8} {'binding':>10} {'D_W':>8} {'D_T1':>8} {'M_pred':>10} "
          f"{'B_pred':>10} {'B_AME':>10} {'err M %':>9} {'err B %':>9}")
    rows = []
    for name, Z, N, M_ref, B_ame in ISOTOPES:
        A = Z + N
        P1, P2, P3 = phi_inter_gen(Z, N)
        binding = float(alpha_bind) * (float(P1) - 2*float(q3_q)*float(P2) + float(HA2)*float(P3))
        # Wigner: -m_e · H_q((2,2)) · min(Z,N)/A
        delta_W = (-float(Wigner_unit) * (min(Z,N)/A)
                     if (A >= 2 and Z >= 1 and N >= 1) else 0.0)
        # Natural T=1 extension: -m_e · H_q((2,2)) · (n_pp + n_nn)/A
        n_pp = Z*(Z-1)//2; n_nn = N*(N-1)//2
        delta_T1 = (-float(Wigner_unit) * ((n_pp + n_nn)/A)
                      if (A >= 2 and (n_pp + n_nn) > 0) else 0.0)
        M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
        M_pred = M_free + binding + delta_W + delta_T1
        err_M = (M_pred - M_ref) / M_ref * 100
        B_pred = -(binding + delta_W + delta_T1)
        err_B = ((B_pred - B_ame) / B_ame * 100) if B_ame != 0 else 0.0
        print(f"  {name:<8} {binding:>+10.3f} {delta_W:>+8.3f} {delta_T1:>+8.3f} "
              f"{M_pred:>10.4f} {B_pred:>+10.4f} {B_ame:>+10.4f} {err_M:>+8.3f}% {err_B:>+8.2f}%")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'binding_MeV': binding, 'delta_W': delta_W, 'delta_T1': delta_T1,
            'M_pred_MeV': M_pred, 'M_codata_MeV': M_ref,
            'B_pred_MeV': B_pred, 'B_AME_MeV': B_ame,
            'err_M_pct': err_M, 'err_B_pct': err_B,
        })

    witness = {
        'computation': 'derived-only-formula',
        'description': (
            'Strict derived-only mass formula: 3-term Wedderburn + '
            'Wigner T=0 + natural T=1 extension.  No variant-selected '
            'fits.  Phi from inter-gen direct (structural, not fitted).'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'isotopes': rows,
    }
    out = Path(__file__).parent / "derived-only-formula.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
