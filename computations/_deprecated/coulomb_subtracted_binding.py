#!/usr/bin/env python3
"""
COULOMB-SUBTRACTED BINDING ENERGIES.

Per user direction: subtract Coulomb explicitly before asking the
chirality-residue / Hecke framework to derive the residual nuclear
binding.  The framework's prior 30-96% binding errors at A>=3 may
absorb Coulomb effects sloppily.

Coulomb energy of a uniformly charged sphere of radius R:

    E_Coul = (3/5) · Z(Z-1) · e²/(4πε₀ · R)
           = 0.864 · Z(Z-1) / R    [MeV, R in fm]

Or simpler classical formula:

    E_Coul ≈ 1.44 · Z(Z-1) / (2 R)    [pairs, MeV·fm/fm]

Empirical nuclear charge radii (RMS):

    H:   0.842 fm    D:   2.130 fm   T:   1.755 fm
    3He: 1.96 fm     4He: 1.676 fm   6Li: 2.55 fm    7Li: 2.43 fm

Or use derived R = r_0 · A^(1/3) with r_0 = 1.2 fm.

Comparison: B_AME (deficit) vs B_nuclear = B_AME + E_Coul (without
EM repulsion), then re-evaluate framework error.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

# Use the framework's q_0 just for documentation
from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV


# Empirical RMS charge radii (CODATA / nuclear data tables)
NUCLEAR_RADII_FM = {
    '1H':  0.8420,    # proton charge radius (CODATA)
    'D':   2.1424,    # deuteron charge radius
    'T':   1.7591,    # triton charge radius
    '3He': 1.9661,    # 3He charge radius
    '4He': 1.6755,    # 4He charge radius
    '6Li': 2.5890,    # 6Li charge radius
    '7Li': 2.4440,    # 7Li charge radius
    '9Be': 2.5190,    # 9Be charge radius
    '12C': 2.4702,    # 12C charge radius
    '16O': 2.6991,    # 16O charge radius
}


def coulomb_energy_uniform_sphere(Z, R_fm):
    """E_Coul = (3/5) · Z(Z-1) · α · ℏc / R  (uniform sphere model).

    Numerical: 0.864 · Z(Z-1) / R   MeV  (R in fm).
    """
    if Z < 2:
        return 0.0
    return 0.864 * Z * (Z - 1) / R_fm


def coulomb_energy_pair_average(Z, R_fm):
    """E_Coul = 1.44 · Z(Z-1) / (2R)  [pairs, MeV·fm/fm].

    Equivalent to uniform sphere up to factor of 6/5 · 0.5/0.5 ... they're close.
    """
    if Z < 2:
        return 0.0
    return 1.44 * Z * (Z - 1) / (2.0 * R_fm)


def main():
    print("=" * 100)
    print("COULOMB-SUBTRACTED BINDING ENERGIES")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  α · ℏc = 1.44 MeV·fm")
    print()

    AME_BIND = {
        'D':   2.22456612, 'T':   8.481798,
        '3He': 7.718058,   '4He': 28.29566,
        '6Li': 31.99405,   '7Li': 39.24454,
        '9Be': 58.16498,   '12C': 92.16175,
        '16O': 127.61926,
    }
    isotopes = [
        # name, Z, N, atomic_radius_label
        ('D',     1, 1,  'D'),
        ('T',     1, 2,  'T'),
        ('3He',   2, 1,  '3He'),
        ('4He',   2, 2,  '4He'),
        ('6Li',   3, 3,  '6Li'),
        ('7Li',   3, 4,  '7Li'),
        ('9Be',   4, 5,  '9Be'),
        ('12C',   6, 6,  '12C'),
        ('16O',   8, 8,  '16O'),
    ]

    print(f"  {'iso':<6} {'Z':>2} {'N':>2} {'R(fm)':>8} {'E_Coul(MeV)':>12} "
          f"{'B_AME':>8} {'B_nucl=B+E':>12} {'EM frac':>10}")

    rows = []
    for name, Z, N, rad_key in isotopes:
        R = NUCLEAR_RADII_FM.get(rad_key, 1.2 * (Z + N)**(1/3))
        E_Coul = coulomb_energy_uniform_sphere(Z, R)
        B_AME = AME_BIND.get(name, 0.0)
        B_nucl = B_AME + E_Coul  # Add back Coulomb repulsion
        em_frac = E_Coul / B_AME * 100 if B_AME > 0 else 0
        print(f"  {name:<6} {Z:>2} {N:>2} {R:>8.3f} {E_Coul:>12.4f} "
              f"{B_AME:>8.4f} {B_nucl:>12.4f} {em_frac:>9.2f}%")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': Z+N,
            'R_fm': R, 'E_Coul_MeV': E_Coul,
            'B_AME_MeV': B_AME, 'B_nucl_MeV': B_nucl,
            'EM_fraction_pct': em_frac,
        })

    print()
    print("=" * 100)
    print("  Re-evaluate chirality-residue framework with Coulomb-subtracted target")
    print("=" * 100)

    # Previous framework predictions for binding (from all_isotopes_chirality_residue.py)
    # m_e · Sigma_{3A} alone:
    Sigma_3A = {
        2: mp.mpf('1.6363'),  # m_e · 3.202
        3: mp.mpf('1.2999'),  # m_e · 2.544
        4: mp.mpf('1.1507'),  # m_e · 2.252
    }
    print(f"  {'iso':<6} {'B_pred':>10} {'B_AME':>8} {'err vs AME':>12} "
          f"{'B_nucl':>10} {'err vs B_nucl':>14}")
    for r in rows:
        if r['A'] not in Sigma_3A or r['A'] > 4:
            continue
        B_pred = float(Sigma_3A[r['A']])
        err_ame = (B_pred - r['B_AME_MeV']) / r['B_AME_MeV'] * 100
        err_nucl = (B_pred - r['B_nucl_MeV']) / r['B_nucl_MeV'] * 100
        print(f"  {r['iso']:<6} {B_pred:>+10.4f} {r['B_AME_MeV']:>+8.4f} "
              f"{err_ame:>+11.2f}% {r['B_nucl_MeV']:>+10.4f} {err_nucl:>+13.2f}%")

    # Save witness
    witness = {
        'computation': 'coulomb-subtracted-binding',
        'description': (
            'Subtract Coulomb energy E_Coul = 0.864·Z(Z-1)/R from '
            'AME binding to obtain nuclear-only B_nucl.  Re-evaluate '
            'framework predictions vs B_nucl rather than B_AME.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'alpha_hbar_c_MeV_fm': 1.44,
        'isotopes': rows,
    }
    out = Path(__file__).parent / "coulomb-subtracted-binding.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
