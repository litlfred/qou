#!/usr/bin/env python3
"""
Direct evaluation of the paper's 3-term Wedderburn mass formula.

   M(Z,N) = Z·m_p + N·m_n + Z·m_e + α·(Φ_1 − 2[3]_q·Φ_2 + H_A²·Φ_3)

with:
  α   = m_e · 8G                         (Borromean binding scale)
  [3]_q = q² + 1 + q⁻²                   (q-deformed 3)
  H_A   = q − q⁻¹                        (Hecke parameter)

  Φ_1 = Σ_i log|z·a_i + b_i|             (Markov-weighted std-trace)
  Φ_2 = Σ_i log|det(M_i)|                (sym × alt eigenvalue product)
  Φ_3 = Σ_i log|λ^sym_i / λ^alt_i|       (chirality)

  per-generator i, with M_i the chained 2×2 transfer matrix and
  λ^sym_i = ∏(c·q + d), λ^alt_i = ∏(−c/q + d).

This formula uses CONSTITUENT m_p and m_n as INPUTS (not derived
from braid).  The α·(...) term is the BINDING correction.

Two checks:
  (a) For p alone (Z=1, N=0): M_pred should equal m_p (binding ≈ 0).
  (b) For D, T, ³He, ⁴He: extract binding B = Z·m_p + N·m_n + Z·m_e − M
      and compare to AME values.

Independent of α-blend phenomenology.  Uses the FULL chain V̂ values,
not approximations.  Includes Wedderburn weights and 3A-partition
sum where per-generator structure naturally lives.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 40

from hecke_core import (h as H_A_F, z as Z_MARKOV, _step_chain_generic)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
H_A = Q0 - QI
me = mp.mpf(str(M_E_MEV))
z_m = mp.mpf(str(float(Z_MARKOV)))
G = mp.catalan
alpha_bind = me * 8 * G   # MeV (Borromean binding scale)
q3 = Q0**2 + 1 + QI**2     # [3]_q
HA2 = H_A**2


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
    """Compute z·a + b after applying all transfer matrices to (0,1)."""
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        a, b = a*(cm*H_A + dm) + b*cm, a*cm + b*dm
    return z_m * a + b


def chain_det(chain):
    """det(M_chain) = ∏ det T(c_i, d_i) = ∏ [d(cH_A+d) − c²]."""
    D = mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        D *= (dm*(cm*H_A + dm) - cm*cm)
    return D


def per_generator_chains(Z, N):
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    gens = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=True)
        for c, d, g in chain_k:
            gens[g].append((c, d))
    return gens


def phi_functionals(Z, N):
    """Compute Φ_1, Φ_2, Φ_3 for atom (Z, N) by summing over generators."""
    chains = per_generator_chains(Z, N)
    Phi1 = mp.mpf(0)
    Phi2 = mp.mpf(0)
    Phi3 = mp.mpf(0)
    for ch in chains:
        if not ch:
            continue
        v_std = chain_std_zb(ch)
        v_det = chain_det(ch)
        l_sym = chain_lambda_sym(ch)
        l_alt = chain_lambda_alt(ch)
        if v_std != 0:
            Phi1 += mp.log(mp.fabs(v_std))
        if v_det != 0:
            Phi2 += mp.log(mp.fabs(v_det))
        if l_sym != 0 and l_alt != 0:
            Phi3 += mp.log(mp.fabs(l_sym / l_alt))
    return Phi1, Phi2, Phi3


def main() -> int:
    print("=" * 100)
    print("PAPER'S FULL 3-TERM WEDDERBURN MASS FORMULA")
    print("  M(Z,N) = Z·m_p + N·m_n + Z·m_e + α·(Φ_1 − 2[3]_q·Φ_2 + H_A²·Φ_3)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  α   = m_e · 8G = {float(alpha_bind):.6f} MeV")
    print(f"  [3]_q = {float(q3):.6f}")
    print(f"  H_A² = {float(HA2):.6f}")
    print()

    # Atomic masses (CODATA): nucleon + Z*m_e - electron binding
    # For Z=1: hydrogen ~ m_p + m_e - 13.6 eV ~ 938.783
    # For Z=2: helium  ~ Z*m_p + N*m_n + Z*m_e - binding
    # Pure neutron has no electron: M = m_n
    AME_BIND = {
        'D':   2.22456612, 'T':   8.481798,
        '³He': 7.718058,   '⁴He': 28.29566,
    }
    M_H_ATOMIC = M_P_MEV + M_E_MEV  # 1H atomic mass (neglecting 13.6 eV binding)
    ISOTOPES = [
        ('p (1H)', 1, 0, M_H_ATOMIC, 0.0),  # hydrogen atom
        ('n',      0, 1, M_N_MEV,    0.0),  # bare neutron
        ('D',      1, 1, 1876.12393, AME_BIND['D']),
        ('T',      1, 2, 2809.43215, AME_BIND['T']),
        ('³He',    2, 1, 2809.41347, AME_BIND['³He']),
        ('⁴He',    2, 2, 3728.40133, AME_BIND['⁴He']),
    ]

    print(f"  Per-isotope Φ functionals and predictions:")
    print(f"  {'iso':<8} {'Φ_1':>10} {'Φ_2':>10} {'Φ_3':>10} "
          f"{'binding(MeV)':>14} {'M_pred':>10} {'CODATA':>10} {'err %':>8}")
    rows = []
    for name, Z, N, M_ref, B_ame in ISOTOPES:
        Phi1, Phi2, Phi3 = phi_functionals(Z, N)
        binding = float(alpha_bind) * (float(Phi1) - 2*float(q3)*float(Phi2) + float(HA2)*float(Phi3))
        M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
        M_pred = M_free + binding
        err = (M_pred - M_ref) / M_ref * 100
        print(f"  {name:<8} {float(Phi1):>+10.4f} {float(Phi2):>+10.4f} {float(Phi3):>+10.4f} "
              f"{binding:>+14.4f} {M_pred:>10.4f} {M_ref:>10.4f} {err:>+7.3f}%")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': Z+N,
            'Phi_1': float(Phi1), 'Phi_2': float(Phi2), 'Phi_3': float(Phi3),
            'binding_MeV': binding,
            'M_free_MeV': M_free,
            'M_pred_MeV': M_pred,
            'M_codata_MeV': M_ref,
            'err_pct': err,
            'B_ame_MeV': B_ame,
        })

    # Binding-energy comparison for nuclei
    print()
    print(f"  Implied bindings vs AME (sign convention: binding > 0 = bound, mass deficit):")
    print(f"  {'iso':<8} {'B_pred':>12} {'B_AME':>10} {'err %':>10}")
    for r in rows:
        if r['B_ame_MeV'] is None or r['B_ame_MeV'] == 0:
            continue
        # AME convention: B > 0 means bound (mass deficit)
        # M = M_free - B  =>  binding_term = -B
        B_pred = -r['binding_MeV']
        err = (B_pred - r['B_ame_MeV']) / r['B_ame_MeV'] * 100
        print(f"  {r['iso']:<8} {B_pred:>+12.4f} {r['B_ame_MeV']:>+10.4f} {err:>+9.3f}%")

    # Term-by-term decomposition for isotopes
    print()
    print(f"  Term-by-term contribution to binding (MeV):")
    print(f"  {'iso':<8} {'a*Phi_1':>12} {'-2a[3]_q*Phi_2':>16} {'a*H_A^2*Phi_3':>16}")
    for r in rows:
        T1 = float(alpha_bind) * r['Phi_1']
        T2 = -2 * float(alpha_bind) * float(q3) * r['Phi_2']
        T3 = float(alpha_bind) * float(HA2) * r['Phi_3']
        print(f"  {r['iso']:<8} {T1:>+12.4f} {T2:>+16.4f} {T3:>+16.4f}")

    # GOAL 1: np mass splitting
    print()
    print(f"  GOAL 1 — np mass splitting from Z*m_p + N*m_n + Z*m_e + binding")
    p_row = next(r for r in rows if r['iso'].startswith('p'))
    n_row = next(r for r in rows if r['iso'] == 'n')
    delta_pred = (n_row['M_pred_MeV'] - p_row['M_pred_MeV'])
    # Adjust for the m_e in the proton (hydrogen) prediction:
    delta_pred_bare = delta_pred + M_E_MEV
    delta_codata = M_N_MEV - M_P_MEV
    print(f"    M_pred(n) - M_pred(1H)         = {delta_pred:+.6f} MeV")
    print(f"    + m_e (back to bare proton)    = {M_E_MEV:+.6f} MeV")
    print(f"    bare predicted Δm_{{n-p}}        = {delta_pred_bare:+.6f} MeV")
    print(f"    CODATA Δm_{{n-p}}                = {delta_codata:+.6f} MeV")
    print(f"    err = {(delta_pred_bare-delta_codata)/delta_codata*100:+.3f}%")

    witness = {
        'computation': 'wedderburn-mass-3term',
        'description': (
            "Direct evaluation of paper's full 3-term Wedderburn mass "
            'formula M = Z·m_p + N·m_n + Z·m_e + α(Φ_1 − 2[3]_q·Φ_2 + '
            'H_A²·Φ_3) with α = m_e·8G.  Uses constituent m_p, m_n as '
            'inputs and computes the binding correction from per-'
            'generator log-functionals.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'alpha_MeV': float(alpha_bind),
        'q3_q': float(q3),
        'HA2': float(HA2),
        'isotopes': rows,
    }
    out = Path(__file__).parent / "wedderburn-mass-3term.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
