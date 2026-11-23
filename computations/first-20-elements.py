#!/usr/bin/env python3
"""First 20 elements: QOU knot-generation mass vs AME2020/CODATA."""

import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from experimental_constants import M_E_MEV  # noqa: E402
from q_parameter import Q
from codata_constants import M_C12_ATOMIC_MEV_VALIDATION, M_HE4_ATOMIC_MEV_VALIDATION  # noqa: E402  (AME registry)

q = Q
hbar_q = 1.0 - 1.0 / q
q_half = math.sqrt(q)

# Dressed quark masses (MeV) from terminal resolution
mu_u, mu_d = 311.10, 312.39

def S(a, b):
    return (q * a + (1/q) * b) / (q_half + 1/q_half)

m_p = S(mu_u, mu_u) + 2 * S(mu_u, mu_d)   # proton
m_n = 2 * S(mu_u, mu_d) + S(mu_d, mu_d)    # neutron
m_e = M_E_MEV                             # electron (CODATA 2022)

# (Z, N, symbol, name, B/A in MeV from AME2020, observed atomic mass MeV)
elements = [
    ( 1,  0, "H-1",   "Hydrogen",     0.0000,    938.783),
    ( 2,  2, "He-4",  "Helium",       7.0739,   float(M_HE4_ATOMIC_MEV_VALIDATION)),
    ( 3,  4, "Li-7",  "Lithium",      5.6063,   6535.366),
    ( 4,  5, "Be-9",  "Beryllium",    6.4628,   8394.794),
    ( 5,  6, "B-11",  "Boron",        6.9277,  10252.547),
    ( 6,  6, "C-12",  "Carbon",       7.6801,  float(M_C12_ATOMIC_MEV_VALIDATION)),
    ( 7,  7, "N-14",  "Nitrogen",     7.4756,  13043.781),
    ( 8,  8, "O-16",  "Oxygen",       7.9762,  14899.169),
    ( 9, 10, "F-19",  "Fluorine",     7.7790,  17692.300),
    (10, 10, "Ne-20", "Neon",         8.0325,  18622.838),
    (11, 12, "Na-23", "Sodium",       8.1115,  21414.836),
    (12, 12, "Mg-24", "Magnesium",    8.2607,  22341.922),
    (13, 14, "Al-27", "Aluminium",    8.3316,  25132.892),
    (14, 14, "Si-28", "Silicon",      8.4477,  26060.349),
    (15, 16, "P-31",  "Phosphorus",   8.4812,  28851.883),
    (16, 16, "S-32",  "Sulfur",       8.4932,  29789.154),
    (17, 18, "Cl-35", "Chlorine",     8.5203,  32573.454),
    (18, 22, "Ar-40", "Argon",        8.5954,  37224.720),
    (19, 20, "K-39",  "Potassium",    8.5570,  36294.464),
    (20, 20, "Ca-40", "Calcium",      8.5513,  37224.924),
]

print()
print(f"  q = {q},  m_p(QOU) = {m_p:.3f} MeV,  m_n(QOU) = {m_n:.3f} MeV,  m_e = {m_e:.5f} MeV")
print()
print(f"  {'Z':>3}  {'Sym':<7} {'Element':<12} {'A':>3}  {'Knot formula':<32}  "
      f"{'QOU (MeV)':>12}  {'Obs (MeV)':>12}  {'D (MeV)':>10}  {'D/m':>10}")
print(f"  {'---':>3}  {'-------':<7} {'------------':<12} {'---':>3}  {'--------------------------------':<32}  "
      f"{'------------':>12}  {'------------':>12}  {'----------':>10}  {'----------':>10}")

for Z, N, sym, name, B_A, m_obs in elements:
    A = Z + N
    B_total = A * B_A
    m_qou = Z * m_p + N * m_n - B_total + Z * m_e

    delta = m_qou - m_obs
    delta_rel = abs(delta) / m_obs

    # Compact knot formula
    if N == 0:
        formula = f"p + T_{{2,3}}"
    else:
        formula = f"{Z}p + {N}n + {Z}e"

    print(f"  {Z:>3}  {sym:<7} {name:<12} {A:>3}  {formula:<32}  "
          f"{m_qou:>12.3f}  {m_obs:>12.3f}  {delta:>+10.3f}  {delta_rel:>10.2e}")

print()
print(f"  Note: QOU mass = Z*m_p + N*m_n - A*(B/A) + Z*m_e")
print(f"  B/A values from AME2020.  Observed atomic masses from AME2020 + Z*m_e.")
print()
