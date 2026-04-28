#!/usr/bin/env python3
"""
3-term Wedderburn formula with INTER-nucleon-only chains, plus
(2,2)⊢4 Wigner partition correction.

Two refinements vs. the previous wedderburn_mass_3term.py:

1. **Inter-nucleon-only Φ.**  For A = 1 (free nucleon) there are no
   inter-nucleon crossings, so binding correction = 0 by construction.
   m_p (CODATA) and m_n (CODATA) input → atomic mass output for free
   nucleons exactly.  For A ≥ 2 the binding comes from inter-nucleon
   crossings only.  Avoids double-counting the quark confinement
   self-energy already in m_p, m_n CODATA.

2. **Wigner (2,2)⊢4 partition correction.**  For nuclei with both
   p and n (D, T, ³He, ⁴He), add the T=0 isoscalar pairing
   contribution from the self-conjugate (2,2) ⊢ 4 partition:

      Δ_W = m_e · H_q((2,2)) · min(Z,N)/A

   where H_q((2,2)) = [3]_q [2]_q² is the q-deformed hook product
   (paper: wigner-np-pairing.md).  ~6.3 MeV at q_0 per pn pair.

Goal: bridge the np splitting and ⁴He binding gaps using the
specific structural elements the paper identifies.
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
alpha_bind = me * 8 * G   # MeV
q3 = Q0**2 + 1 + QI**2     # [3]_q
q2 = Q0 + QI               # [2]_q
HA2 = H_A**2

# Wigner pairing scale: m_e · [3]_q · [2]_q² = m_e · H_q((2,2))
delta_W_unit = me * q3 * q2**2  # MeV per pn pair


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
    """Per-generator chains.  include_inter=False suppresses inter-
    nucleon crossings; include_intra=False suppresses intra-nucleon."""
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    gens = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=include_inter)
        # Determine which entries are "intra" (same-nucleon) vs "inter"
        # Heuristic: entries with gen index in the k-th nucleon's strand
        # range are intra; otherwise inter.  Actually
        # _step_chain_generic with include_inter=False skips inter
        # entirely.  For finer control we filter by gen range.
        # Strand ranges per nucleon: nucleon i occupies strands 3i, 3i+1, 3i+2.
        # Generator g operates between strands g and g+1.
        # Intra-k generators: g in [3k, 3k+1] (within nucleon k).
        intra_g_lo = 3*k
        intra_g_hi = 3*k + 1  # inclusive
        for c, d, g in chain_k:
            is_intra = (intra_g_lo <= g <= intra_g_hi)
            if (is_intra and include_intra) or (not is_intra and include_inter):
                gens[g].append((c, d))
    return gens


def phi_functionals(Z, N, include_inter=True, include_intra=True):
    chains = per_generator_chains(Z, N, include_inter=include_inter,
                                    include_intra=include_intra)
    Phi1 = mp.mpf(0); Phi2 = mp.mpf(0); Phi3 = mp.mpf(0)
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
    print("3-TERM WEDDERBURN with INTER-only Φ + Wigner (2,2)⊢4 correction")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  α (Borromean) = m_e·8G = {float(alpha_bind):.6f} MeV")
    print(f"  Δ_W per pair  = m_e·[3]_q·[2]_q² = {float(delta_W_unit):.6f} MeV")
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

    # Approach A: full chains (intra+inter) — previous result
    # Approach B: inter-only chains (subtract intra baseline)
    # Approach C: inter-only + Wigner (2,2) correction

    print("  Approach B: inter-nucleon-only Φ functionals + Wigner correction")
    print(f"  {'iso':<8} {'Φ_1':>10} {'Φ_2':>10} {'Φ_3':>10} "
          f"{'binding':>10} {'Δ_W':>8} {'M_pred':>10} {'CODATA':>10} {'err %':>8}")
    rows = []
    # First compute reference: Phi(intra-only) for free p and free n
    Phi1_p_intra, Phi2_p_intra, Phi3_p_intra = phi_functionals(1, 0,
                                                                  include_inter=False,
                                                                  include_intra=True)
    Phi1_n_intra, Phi2_n_intra, Phi3_n_intra = phi_functionals(0, 1,
                                                                  include_inter=False,
                                                                  include_intra=True)

    for name, Z, N, M_ref, B_ame in ISOTOPES:
        # Compute full Φ
        Phi1_full, Phi2_full, Phi3_full = phi_functionals(Z, N,
                                                              include_inter=True,
                                                              include_intra=True)
        # Subtract free-constituent intra contributions:
        Phi1_inter = Phi1_full - Z*Phi1_p_intra - N*Phi1_n_intra
        Phi2_inter = Phi2_full - Z*Phi2_p_intra - N*Phi2_n_intra
        Phi3_inter = Phi3_full - Z*Phi3_p_intra - N*Phi3_n_intra
        binding = float(alpha_bind) * (float(Phi1_inter)
                                          - 2*float(q3)*float(Phi2_inter)
                                          + float(HA2)*float(Phi3_inter))
        # Wigner correction
        A = Z + N
        if A >= 2 and Z >= 1 and N >= 1:
            delta_W = -float(delta_W_unit) * min(Z, N) / A  # negative = bound
        else:
            delta_W = 0.0
        M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
        M_pred = M_free + binding + delta_W
        err = (M_pred - M_ref) / M_ref * 100
        print(f"  {name:<8} {float(Phi1_inter):>+10.4f} {float(Phi2_inter):>+10.4f} "
              f"{float(Phi3_inter):>+10.4f} {binding:>+10.4f} {delta_W:>+8.4f} "
              f"{M_pred:>10.4f} {M_ref:>10.4f} {err:>+7.3f}%")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'Phi_1_inter': float(Phi1_inter),
            'Phi_2_inter': float(Phi2_inter),
            'Phi_3_inter': float(Phi3_inter),
            'binding_MeV': binding,
            'Wigner_MeV': delta_W,
            'M_pred_MeV': M_pred,
            'M_codata_MeV': M_ref,
            'err_pct': err,
            'B_ame_MeV': B_ame,
        })

    print()
    print(f"  Implied bindings vs AME (B > 0 = bound):")
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
    print(f"  Bare np splitting (inter-only Φ):")
    print(f"    M_pred(n) - M_pred(1H) + m_e = {delta_pred:+.6f} MeV")
    print(f"    CODATA Δm_{{n-p}}              = {delta_codata:+.6f} MeV")
    print(f"    err = {(delta_pred-delta_codata)/delta_codata*100:+.3f}%")
    print()
    # With inter-only, Phi for free n and free p should be ~0 — no binding correction
    # Therefore np splitting reverts to pure constituent input (1.293 MeV by construction).

    # Also report Φ_3 contribution alone (per user direction)
    print()
    print(f"  Φ_3 (chirality) contribution to binding alone:")
    print(f"  {'iso':<8} {'a*H_A^2*Phi_3':>14} {'Total binding':>14} {'Phi_3 frac':>12}")
    for r in rows:
        T3 = float(alpha_bind) * float(HA2) * r['Phi_3_inter']
        Tt = r['binding_MeV']
        frac = T3 / Tt if abs(Tt) > 1e-9 else 0.0
        print(f"  {r['iso']:<8} {T3:>+12.4f} {Tt:>+14.4f} {frac:>+12.3f}")

    witness = {
        'computation': 'wedderburn-3term-inter-only',
        'description': (
            'Refined 3-term Wedderburn formula: subtract free '
            'constituent intra-nucleon Phi to avoid double-counting; '
            'add Wigner (2,2)|-4 isoscalar pairing correction Delta_W '
            '= m_e * [3]_q * [2]_q^2 * min(Z,N)/A.  Tests whether '
            'these refinements bridge np splitting and 4He binding gaps.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'alpha_MeV': float(alpha_bind),
        'delta_W_per_pair_MeV': float(delta_W_unit),
        'isotopes': rows,
    }
    out = Path(__file__).parent / "wedderburn-3term-inter-only.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
