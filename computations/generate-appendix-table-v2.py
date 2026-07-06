#!/usr/bin/env python3
"""Generate appendix markdown table v2: includes observed atomic mass."""

import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "folio-assistant"))
import _path_bridge  # noqa: F401, E402
from experimental_constants import M_E_MEV  # noqa: E402
from computations.q_parameter import Q

q = Q
q_half = math.sqrt(q)
mu_u, mu_d = 311.10, 312.39

def S(a, b):
    return (q * a + (1/q) * b) / (q_half + 1/q_half)

m_p = S(mu_u, mu_u) + 2 * S(mu_u, mu_d)
m_n = 2 * S(mu_u, mu_d) + S(mu_d, mu_d)
m_e = M_E_MEV

# (Z, A, sym, name, B/A MeV, observed atomic mass MeV)
# Observed = nuclear mass (AME2020) + Z*m_e
# For light elements: CODATA 2022 atomic masses where available
# For heavier: AME2020 nuclear mass + Z*m_e
elements = [
    ( 1,   1, "H",   "Hydrogen",      0.0000,    938.783),
    ( 2,   4, "He",  "Helium",        7.0739,   3728.401),
    ( 3,   7, "Li",  "Lithium",       5.6063,   6535.366),
    ( 4,   9, "Be",  "Beryllium",     6.4628,   8394.794),
    ( 5,  11, "B",   "Boron",         6.9277,  10255.103),
    ( 6,  12, "C",   "Carbon",        7.6801,  11177.929),
    ( 7,  14, "N",   "Nitrogen",      7.4756,  13043.781),
    ( 8,  16, "O",   "Oxygen",        7.9762,  14899.169),
    ( 9,  19, "F",   "Fluorine",      7.7790,  17696.929),
    (10,  20, "Ne",  "Neon",          8.0325,  18622.838),
    (11,  23, "Na",  "Sodium",        8.1115,  21414.836),
    (12,  24, "Mg",  "Magnesium",     8.2607,  22341.922),
    (13,  27, "Al",  "Aluminium",     8.3316,  25132.892),
    (14,  28, "Si",  "Silicon",       8.4477,  26060.349),
    (15,  31, "P",   "Phosphorus",    8.4812,  28851.883),
    (16,  32, "S",   "Sulfur",        8.4932,  29789.154),
    (17,  35, "Cl",  "Chlorine",      8.5203,  32573.454),
    (18,  40, "Ar",  "Argon",         8.5954,  37224.720),
    (19,  39, "K",   "Potassium",     8.5570,  36294.464),
    (20,  40, "Ca",  "Calcium",       8.5513,  37224.924),
    (21,  45, "Sc",  "Scandium",      8.6190,  41876.178),
    (22,  48, "Ti",  "Titanium",      8.7230,  44663.291),
    (23,  51, "V",   "Vanadium",      8.7420,  47453.970),
    (24,  52, "Cr",  "Chromium",      8.7760,  48382.277),
    (25,  55, "Mn",  "Manganese",     8.7649,  51174.480),
    (26,  56, "Fe",  "Iron",          8.7903,  52103.066),
    (27,  59, "Co",  "Cobalt",        8.7680,  54895.898),
    (28,  58, "Ni",  "Nickel",        8.7322,  53966.388),
    (29,  63, "Cu",  "Copper",        8.7522,  58618.504),
    (30,  64, "Zn",  "Zinc",          8.7357,  59549.584),
    (31,  69, "Ga",  "Gallium",       8.7246,  64203.849),
    (32,  74, "Ge",  "Germanium",     8.7264,  68857.041),
    (33,  75, "As",  "Arsenic",       8.7010,  69789.098),
    (34,  80, "Se",  "Selenium",      8.7110,  74441.790),
    (35,  79, "Br",  "Bromine",       8.6961,  73511.439),
    (36,  84, "Kr",  "Krypton",       8.7172,  78163.190),
    (37,  85, "Rb",  "Rubidium",      8.6974,  79094.938),
    (38,  88, "Sr",  "Strontium",     8.7326,  81883.607),
    (39,  89, "Y",   "Yttrium",       8.7138,  82815.327),
    (40,  90, "Zr",  "Zirconium",     8.7098,  83745.896),
    (41,  93, "Nb",  "Niobium",       8.6641,  86541.895),
    (42,  98, "Mo",  "Molybdenum",    8.6353,  91198.408),
    (43,  98, "Tc",  "Technetium",    8.5937,  91201.690),
    (44, 102, "Ru",  "Ruthenium",     8.6070,  94923.539),
    (45, 103, "Rh",  "Rhodium",       8.5843,  95855.979),
    (46, 106, "Pd",  "Palladium",     8.5670,  98650.068),
    (47, 107, "Ag",  "Silver",        8.5536,  99581.627),
    (48, 114, "Cd",  "Cadmium",       8.5398, 106099.565),
    (49, 115, "In",  "Indium",        8.5160, 107032.578),
    (50, 120, "Sn",  "Tin",           8.5050, 111688.399),
    (51, 121, "Sb",  "Antimony",      8.4820, 112621.361),
    (52, 130, "Te",  "Tellurium",     8.4390, 121006.014),
    (53, 127, "I",   "Iodine",        8.4455, 118211.030),
    (54, 132, "Xe",  "Xenon",         8.4275, 122868.232),
    (55, 133, "Cs",  "Caesium",       8.4100, 123800.872),
    (56, 138, "Ba",  "Barium",        8.3937, 128458.145),
    (57, 139, "La",  "Lanthanum",     8.3780, 129390.768),
    (58, 140, "Ce",  "Cerium",        8.3765, 130321.404),
    (59, 141, "Pr",  "Praseodymium",  8.3540, 131254.937),
    (60, 142, "Nd",  "Neodymium",     8.3460, 132186.585),
    (61, 145, "Pm",  "Promethium",    8.3040, 134985.560),
    (62, 152, "Sm",  "Samarium",      8.2440, 141512.653),
    (63, 153, "Eu",  "Europium",      8.2290, 142445.563),
    (64, 158, "Gd",  "Gadolinium",    8.2140, 147103.801),
    (65, 159, "Tb",  "Terbium",       8.1990, 148036.810),
    (66, 164, "Dy",  "Dysprosium",    8.1865, 152694.974),
    (67, 165, "Ho",  "Holmium",       8.1710, 153628.020),
    (68, 166, "Er",  "Erbium",        8.1690, 154559.051),
    (69, 169, "Tm",  "Thulium",       8.1460, 157356.374),
    (70, 174, "Yb",  "Ytterbium",     8.1280, 162015.811),
    (71, 175, "Lu",  "Lutetium",      8.1165, 162948.512),
    (72, 180, "Hf",  "Hafnium",       8.0985, 167608.184),
    (73, 181, "Ta",  "Tantalum",      8.0870, 168540.893),
    (74, 184, "W",   "Tungsten",      8.0639, 171338.789),
    (75, 187, "Re",  "Rhenium",       8.0390, 174137.224),
    (76, 192, "Os",  "Osmium",        8.0194, 178797.845),
    (77, 193, "Ir",  "Iridium",       8.0060, 179731.221),
    (78, 195, "Pt",  "Platinum",      7.9930, 181596.049),
    (79, 197, "Au",  "Gold",          7.9759, 183461.707),
    (80, 202, "Hg",  "Mercury",       7.9530, 188123.533),
    (81, 205, "Tl",  "Thallium",      7.9370, 190920.960),
    (82, 208, "Pb",  "Lead",          7.8675, 193729.498),
    (83, 209, "Bi",  "Bismuth",       7.8480, 194664.510),
    (84, 209, "Po",  "Polonium",      7.8352, 194666.433),
    (85, 210, "At",  "Astatine",      7.8147, 195601.766),
    (86, 222, "Rn",  "Radon",         7.7227, 206802.402),
    (87, 223, "Fr",  "Francium",      7.7095, 207736.395),
    (88, 226, "Ra",  "Radium",        7.6620, 210541.895),
    (89, 227, "Ac",  "Actinium",      7.6510, 211475.484),
    (90, 232, "Th",  "Thorium",       7.6150, 216142.695),
    (91, 231, "Pa",  "Protactinium",  7.6138, 215210.173),
    (92, 238, "U",   "Uranium",       7.5701, 221743.520),
]

magic_Z = {2, 8, 20, 28, 50, 82}
magic_N = {2, 8, 20, 28, 50, 82, 126}

print("| $\\#$ | Element | $p$ | $n$ | Knot formula | $\\mathcal{M}_{\\mathrm{QOU}}$ | $\\mathcal{M}_{\\mathrm{obs}}$ | $B/A$ |")
print("|---:|---------|---:|---:|-------------|---:|---:|---:|")

for Z, A, sym, name, B_A, m_obs in elements:
    N = A - Z
    B_total = A * B_A
    m_qou = Z * m_p + N * m_n - B_total + Z * m_e

    formula = f"${Z}\\mathfrak{{p}} \\bowtie {N}\\mathfrak{{n}} \\bowtie {Z}T_{{2,3}}$"

    markers = ""
    if Z in magic_Z and N in magic_N:
        markers = "$^{\\diamond\\star}$"
    elif Z in magic_Z:
        markers = "$^{\\diamond}$"
    elif N in magic_N:
        markers = "$^{\\star}$"

    print(f"| {Z} | {name}{markers} | {Z} | {N} | {formula} | ${m_qou:.1f}$ | ${m_obs:.1f}$ | ${B_A:.4f}$ |")
