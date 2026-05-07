#!/usr/bin/env python3
"""
ATOMIC Frobenius co-Casimir trace as the missing binding term.

The paper's frobenius-codim-universal proves:
  τ(C_dim_q) = Σ_{λ ⊢ n} 1/dim_q(λ)

For single nucleon (n=3): Σ = 2 + 1/[2]_q ≈ 2.55 MeV·m_e (proton
residual, paper's Term 6).

Natural atomic extension: replace n=3 with n=3A (atomic strand count).
The atomic Frobenius co-Casimir contribution to mass:

    Δ_F^atom = ±m_e · Σ_{λ ⊢ 3A} 1/dim_q(λ)

Sign convention: this term is INTRINSIC mass (vacuum-mass / vortex
self-energy), separate from BINDING.  For a free nucleon (A=1), it
gives the proton residual.  For an atom (A ≥ 2), it should extend.

Test: compute Σ_{λ⊢3A}1/dim_q(λ) for each A, see if including it
as a NEGATIVE binding correction (more attractive) bridges the
30-76% under-binding gap.
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
Wigner_unit = me * q3_q * q2_q**2


def q_int(n): return (Q0**n - QI**n) / (Q0 - QI)
def q_fact(n):
    out = mp.mpf(1)
    for i in range(2, n+1): out *= q_int(i)
    return out
def hook_product_q(lam):
    out = mp.mpf(1)
    for h in young_hooks(lam): out *= q_int(int(h))
    return out
def dim_q_lam(lam):
    return q_fact(sum(lam)) / hook_product_q(lam)


def frobenius_codim_atom(n_strands):
    """Σ_{λ⊢n} 1/dim_q(λ)."""
    return sum(1 / dim_q_lam(tuple(lam)) for lam in partitions_of(n_strands))


# Per-gen and Φ infra
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
    print("ATOMIC Frobenius co-Casimir: Σ_{λ⊢3A} 1/dim_q(λ)")
    print("=" * 100)
    print()

    # Pre-compute Frobenius co-Casimir per 3A
    print(f"  Frobenius co-Casimir trace per A:")
    print(f"  {'A':>3} {'3A':>3} {'#partitions':>12} {'Σ 1/dim_q':>14} {'m_e · Σ (MeV)':>14}")
    fc_codim = {}
    for A in range(1, 8):
        n = 3 * A
        s = float(frobenius_codim_atom(n))
        fc_codim[A] = s
        print(f"  {A:>3} {n:>3} {len(list(partitions_of(n))):>12} {s:>14.6f} "
              f"{float(me) * s:>14.6f}")
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

    # Try Δ_F^atom with several signs/scalings
    variants = {
        'A: -m_e · Σ_{λ⊢3A} 1/dim_q (binding)':       lambda A: -float(me) * fc_codim[A],
        'B: -m_e · (Σ - 2) (subtract A=1 trivial)':    lambda A: -float(me) * (fc_codim[A] - 2),
        'C: -m_e · (Σ_3A - A·Σ_3) (free-subtraction)': lambda A: -float(me) * (fc_codim[A] - A*fc_codim[1]),
        'D: -m_e · Σ · (A-1)/A':                        lambda A: -float(me) * fc_codim[A] * (A-1)/A if A>0 else 0,
    }

    for vname, vfn in variants.items():
        print(f"  Variant: {vname}")
        print(f"  {'iso':<8} {'binding':>10} {'D_W':>8} {'D_T1':>8} {'D_F^atom':>10} "
              f"{'B_pred':>10} {'AME':>10} {'B err':>10}")
        for name, Z, N, M_ref, B_ame in ISOTOPES:
            A = Z + N
            P1, P2, P3 = phi_inter_gen(Z, N)
            binding = float(alpha_bind) * (float(P1) - 2*float(q3_q)*float(P2) + float(HA2)*float(P3))
            delta_W = (-float(Wigner_unit) * (min(Z,N)/A)
                         if (A >= 2 and Z >= 1 and N >= 1) else 0.0)
            n_pp = Z*(Z-1)//2; n_nn = N*(N-1)//2
            delta_T1 = (-float(Wigner_unit) * ((n_pp + n_nn)/A)
                          if (A >= 2 and (n_pp + n_nn) > 0) else 0.0)
            delta_F = vfn(A) if A >= 2 else 0.0
            M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
            M_pred = M_free + binding + delta_W + delta_T1 + delta_F
            B_pred = -(binding + delta_W + delta_T1 + delta_F)
            err_B = ((B_pred - B_ame) / B_ame * 100) if B_ame != 0 else 0.0
            print(f"  {name:<8} {binding:>+10.3f} {delta_W:>+8.3f} {delta_T1:>+8.3f} "
                  f"{delta_F:>+10.3f} {B_pred:>+10.3f} {B_ame:>+10.3f} {err_B:>+9.2f}%")
        print()


if __name__ == "__main__":
    main()
